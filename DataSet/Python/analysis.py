import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo1_delta.csv')
print("\n\nDataframe 1:\n")
print(df1.dtypes)
print(df1.head())
print(df1.describe())

df2 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo2_delta.csv')
print("\n\nDataframe 2:\n")
print(df2.dtypes)
print(df2.head())
print(df2.describe())

df3 = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo3_delta.csv')
print("\n\nDataframe 3:\n")
print(df3.dtypes)
print(df3.head())
print(df3.describe())

fig, axs = plt.subplots(6, 1, layout='constrained')
axs[0].plot(df1.index, df1.acc_x, df1.index, df1.acc_y, df1.index, df1.acc_z)
axs[1].plot(df1.index, df1.gyr_x, df1.index, df1.gyr_y, df1.index, df1.gyr_z)
axs[2].plot(df2.index, df2.acc_x, df2.index, df2.acc_y, df2.index, df2.acc_z)
axs[3].plot(df2.index, df2.gyr_x, df2.index, df2.gyr_y, df2.index, df2.gyr_z)
axs[4].plot(df3.index, df3.acc_x, df3.index, df3.acc_y, df3.index, df3.acc_z)
axs[5].plot(df3.index, df3.gyr_x, df3.index, df3.gyr_y, df3.index, df3.gyr_z)

axs[0].set_ylim(-150, 150)
axs[0].set_ylabel('Video 1: Acc')
axs[0].grid(True)

axs[1].set_ylim(-20, 20)
axs[1].set_ylabel('Video 1: Gyro')
axs[1].grid(True)

axs[2].set_ylim(-150, 150)
axs[2].set_ylabel('Video 2: Acc')
axs[2].grid(True)

axs[3].set_ylim(-20, 20)
axs[3].set_ylabel('Video 2: Gyro')
axs[3].grid(True)

axs[4].set_ylim(-150, 150)
axs[4].set_ylabel('Video 3: Acc')
axs[4].grid(True)

axs[5].set_ylim(-20, 20)
axs[5].set_ylabel('Video 3: Gyro')
axs[5].grid(True)

plt.legend(loc='best')
plt.show()