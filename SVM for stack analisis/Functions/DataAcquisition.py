import time , os
from tqdm import tqdm
import pandas as pd
from datetime import datetime
import os
from bs4 import BeautifulSoup
import quandl
from time import mktime



def quandl_stocks_host_price(symbol, date='2008-01-02'):
    """
    ===---This function returns the Historical quotes of the selected ticket---===
    
    symbol is a string representing a stock symbol, e.g. 'AAPL'
 
    start_date and end_date are tuples of integers representing the year, month,
    and day
 
    end_date defaults to the current date when None
    """
    quandl.ApiConfig.api_key = '3epFW-eMFHf54_jpDFyS'
    query_list = 'WIKI' + '/' + symbol
    
    responce = quandl.get(query_list, 
            returns='pandas', 
            start_date=date,
            end_date=date,
            collapse='daily',
            order='asc'
            )
    if responce.shape[0]==0:
        new_date = [int(x) for x in date.split('-')] 
        if new_date[2]>2:
            new_date[2] -=2
        else:
            new_date[2] +=2
        new_date = '-'.join([str(x) for x in x1])
        new_responce = quandl.get(query_list, 
            returns='pandas', 
            start_date=date,
            end_date=new_date,
            collapse='daily',
            order='asc'
            )
        if new_responce.shape[0]==0:
            raise ValueError('Data not found for this day(weekend adj.)')
        return new_responce
    else:
        return responce['Adj. Close'].item()
    
    
    
    
    
def GetStats(gathers = None,path='', limit = None):
    '''
    This function Return Finance multiplicators from all snp500 stocks
    input : gathers = ['var1', 'var2','var3', ...] ; limit = for test only ; path = path to dataset 
    ouptut : Pandas dataframe with columns ['Date','Unix Time', ' Ticket','var1', 'var2','var3',..]
    
    '''
    if not gathers:
        print("input gathers as a list")
        return None
    #INIT Data##################
    columns = ['Date',
                'Unix',
                'Ticker']
    columns.extend(gathers)
    
    print(*gathers,sep=',')
    stock_files = path+ '_KeyStats'
    stock_list = [x[0] for x in os.walk(stock_files)]
    df = pd.DataFrame(columns=columns)
    
    #print(stacks_list)
    amount_of_files = len(stock_list[1:])
    if limit:
        print("Limit set to:", limit)
    else:
        print("Will Crowl All dataset")
    counter = -1
    
    ##################
    
    #Go through Each Ticker (folder)
    for each_dir in tqdm(stock_list[1:]):
        counter +=1
        if limit==counter:
            break
        ticker = each_dir.split('\\')[-1]
        print('Start working with: ',ticker)
        each_file = os.listdir(each_dir)
        
        if len(each_file)>0:
            #Get all historic data 
            for file in tqdm(each_file):
                
                date_stamp = datetime.strptime(file,'%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_path_file = each_dir +'\\'+file
                with open(full_path_file,'r') as f:
                    source =f.read()
                soup = BeautifulSoup(source, 'html.parser')
                data = []
                rows = soup.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    data.extend([cell.text for cell in cols])
                try:
                    values = {}

                    for gather in  gathers:
                        try:
                            value = data[data.index(gather+':')+1]
                            if '%' in value:
                                value = float(value.strip('%')) / 100.
                            else:
                                value = float(value)
                            values[gather] = value
                        except Exception as e: 
                            values[gather] = -99999.0
                    
                    #Get stock price for spesific date
                    new_row = {**{'Date':date_stamp,
                                    'Unix':unix_time,
                                    'Ticker':ticker,
                                   },**values}
                    df = df.append(new_row,ignore_index=True)
                except Exception as e:
                    print(e)
    return df