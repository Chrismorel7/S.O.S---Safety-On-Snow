import pandas as pd

VIDEO = str(12548)
PATH = 'DataSet/csvFiles/csvDelta/Input_vdo12663_delta.csv'

dfplot = pd.read_csv(PATH)
print("\n\nDataframe :\n")
print(dfplot.dtypes)
print(dfplot.head())
print(dfplot.describe())