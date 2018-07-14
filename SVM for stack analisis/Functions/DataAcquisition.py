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