import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('DataSet/csvFiles/Input_vdo1_delta.csv')
print("\n\nDataframe 1:\n")
print(df1.dtypes)
print(df1.head())
print(df1.describe())


fig, axs = plt.subplots(3, 1, layout='constrained')
axs[0].plot(df1.index, df1.acc_x, df1.index, df1.acc_y, df1.index, df1.acc_z)
axs[1].plot(df1.index, df1.gyr_x, df1.index, df1.gyr_y, df1.index, df1.gyr_z)

axs[0].set_ylim(-200, 200)
axs[0].set_ylabel('Accelerometer [m/s2]')
axs[0].grid(True)
axs[1].set_ylim(-200, 200)
axs[1].set_ylabel('Accelerometer [m/s2]')
axs[1].grid(True)

plt.legend(loc='best')
plt.show()