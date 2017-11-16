import pandas as pd
import numpy as np


filepath= './data/Energy Indicators.xls'

energy = pd.read_excel(filepath)
energy = energy[16:243]
energy = energy.drop(energy.columns[[0, 1]], axis=1)

print(energy.columns)



energy.to_csv('./data/exti.csv')


def answer_one():
    return "ANSWER"