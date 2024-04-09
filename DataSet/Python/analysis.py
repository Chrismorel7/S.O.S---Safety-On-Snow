import pandas as pd
import matplotlib.pyplot as plt

VIDEO = str(12645)

dfplot = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo'+VIDEO+'_delta.csv')
print("\n\nDataframe :\n")
print(dfplot.dtypes)
print(dfplot.head())
print(dfplot.describe())

fig, axs = plt.subplots(3, 1, layout='constrained')
axs[0].plot(dfplot.index, dfplot.acc_x, dfplot.index, dfplot.acc_y, dfplot.index, dfplot.acc_z)
axs[1].plot(dfplot.index, dfplot.gyr_x, dfplot.index, dfplot.gyr_y, dfplot.index, dfplot.gyr_z)
axs[2].plot(dfplot.index, dfplot.fall)

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