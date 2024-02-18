import pandas as pd

df1 = pd.read_csv('DataSet/csvFiles/Input_vdo1.csv')
print("\n\nDataframe 1:\n")
print(df1.describe())

df2 = pd.read_csv('DataSet/csvFiles/Input_vdo2.csv')
print("\n\nDataframe 2:\n")
print(df2.describe())

df3 = pd.read_csv('DataSet/csvFiles/Input_vdo3.csv')
print("\n\nDataframe 3:\n")
print(df3.describe())