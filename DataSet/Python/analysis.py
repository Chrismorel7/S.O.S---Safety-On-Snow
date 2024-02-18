import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('DataSet/csvFiles/Input_vdo1.csv')
print("\n\nDataframe 1:\n")
print(df1.describe())

df2 = pd.read_csv('DataSet/csvFiles/Input_vdo2.csv')
print("\n\nDataframe 2:\n")
print(df2.describe())

df3 = pd.read_csv('DataSet/csvFiles/Input_vdo3.csv')
print("\n\nDataframe 3:\n")
print(df3.describe())

df1.drop(axis=1, columns='date')

fig, axs = plt.subplots(3, 1, layout='constrained')
axs[0].plot(df1.index, df1.acc_x, df1.index, df1.acc_y, df1.index, df1.acc_z)
axs[1].plot(df2.index, df2.acc_x, df2.index, df2.acc_y, df2.index, df2.acc_z)
axs[2].plot(df3.index, df3.acc_x, df3.index, df3.acc_y, df3.index, df3.acc_z)

axs[0].set_ylim(-80, 80)
axs[0].set_ylabel('Accelerometer [m/s2]')
axs[0].grid(True)
axs[1].set_ylim(-80, 80)
axs[1].set_ylabel('Accelerometer [m/s2]')
axs[1].grid(True)
axs[2].set_ylim(-80, 80)
axs[2].set_ylabel('Accelerometer [m/s2]')
axs[2].grid(True)

plt.legend(loc='best')
plt.show()