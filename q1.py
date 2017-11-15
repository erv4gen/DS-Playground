import csv
import pip
import os
import pandas as pd
import numpy as np


filepath= './data/Energy Indicators.xls'

imp1 = pd.ExcelFile(filepath)
Energysh = imp1.parse(0)

print(Energysh.head)

def answer_one():
    return "ANSWER"