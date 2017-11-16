import pandas as pd
import numpy as np


filepath= './data/Energy Indicators.xls'

energy = pd.read_excel(filepath)
energy = (energy[16:243]
    .drop(energy.columns[[0, 1]], axis=1)
    .rename(columns={'Environmental Indicators: Energy': 'Country',
                     'Unnamed: 3':'Energy Supply',
                     'Unnamed: 4' : 'Energy Supply per Capita',
                     'Unnamed: 5':'% Renewable'})
    .set_index('Country')
          )


print(energy.columns)



energy.to_csv('./data/exti.csv')
print("done!")

def answer_one():
    return "ANSWER"