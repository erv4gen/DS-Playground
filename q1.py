import pandas as pd
import numpy as np

filepath= './data/Energy Indicators.xls'

#read file
energy = pd.read_excel(filepath)

#cleaning data
energy = (energy[16:243]
    .drop(energy.columns[[0, 1]], axis=1)
    .rename(columns={'Environmental Indicators: Energy': 'Country',
                     'Unnamed: 3':'Energy Supply',
                     'Unnamed: 4' : 'Energy Supply per Capita',
                     'Unnamed: 5':'% Renewable'})
    .set_index('Country')
          )
#clean missing values
energy.replace('...',np.nan,inplace =True)


#change rows
rows_to_Change = {"Republic of Korea": "South Korea",
                  "United States of America": "United States",
                  "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                  "China, Hong Kong Special Administrative Region": "Hong Kong"}
#change rows
energy['Energy Supply'] = energy['Energy Supply'] * 1000

energy = energy.reset_index()
energy.replace({"Country": rows_to_Change},inplace = True)
energy['Country'] = (energy['Country'].apply(lambda x: x.split('(')[0].rstrip(' ').replace(r"\d+",''))
    .apply(lambda a: "".join([x for x in a if x.isalpha()]))
                     )


#energy = energy.set_index('Country')

print(energy.loc[43])

energy.to_csv('./data/exti.csv')




def answer_one():
    return "ANSWER"