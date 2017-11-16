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
energy['Energy Supply'] = energy['Energy Supply'] * 1000

#change rows
rows_to_Change = {"Republic of Korea": "South Korea",
                  "United States of America": "United States",
                  "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                  "China, Hong Kong Special Administrative Region": "Hong Kong"}

energy = energy.reset_index()
energy.replace({"Country": rows_to_Change},inplace = True)
energy = energy.set_index('Country')

#

print(energy.head())



energy.to_csv('./data/exti.csv')
print("done!")

def answer_one():
    return "ANSWER"