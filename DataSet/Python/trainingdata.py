import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo11015_delta.csv')
df2 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo11042_delta.csv')
df3 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12548_delta.csv')
df4 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12549_delta.csv')
df5 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12550_delta.csv')
df6 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12638_delta.csv')
df7 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12639_delta.csv')
df8 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12640_delta.csv')
df9 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12644_delta.csv')
df10 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12645_delta.csv')
df11 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12649_delta.csv')
df12= pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12650_delta.csv')
df13 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12653_delta.csv')
df14 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12656_delta.csv')
df15 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12659_delta.csv')
df16 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo12663_delta.csv')

combineddf = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16], ignore_index=True)

print(combineddf.dtypes)
print(combineddf.head())
print(combineddf.describe())

combineddf.to_csv('trainingdata.csv')

fig, axs = plt.subplots(3, 1, layout='constrained')
axs[0].plot(combineddf.index, combineddf.acc_x, combineddf.index, combineddf.acc_y, combineddf.index, combineddf.acc_z)
axs[1].plot(combineddf.index, combineddf.gyr_x, combineddf.index, combineddf.gyr_y, combineddf.index, combineddf.gyr_z)
axs[2].plot(combineddf.index, combineddf.fall)
axs[0].set_ylim(-150, 150)
axs[0].set_ylabel('Accelerometre [m/s2]')
axs[0].grid(True)
axs[1].set_ylim(-40, 40)
axs[1].set_ylabel('Gyroscope [rad/s]')
axs[1].grid(True)
axs[2].set_ylim(-0.5, 1.5)
axs[2].set_ylabel('Fall')
axs[2].grid(True)
plt.legend(loc=1)
plt.show()

