import pandas as pd
import numpy as np


filepath= './data/Energy Indicators.xls'

energy = pd.read_excel(filepath,header=16,skip_footer=38)

(energy.index.set_index())

print(energy.columns)



energy.to_csv('./data/exti.csv')


def answer_one():
    return "ANSWER"