"""Create a DataSet based on video 2 data."""

import pandas as pd

df_acc = pd.read_csv('DataSet/csvFiles/GH011042_HERO9 Black-ACCL.csv')
df_gyr = pd.read_csv('DataSet/csvFiles/GH011042_HERO9 Black-GYRO.csv')

df_acc = df_acc.drop(axis=1, columns={'temperature [°C]', 'cts'})
df_gyr = df_gyr.drop(axis=1, columns={'temperature [°C]', 'cts'})

Input = pd.merge(df_acc, df_gyr)

Input = Input.rename(columns={"Accelerometer [m/s2]": "acc_x",
                                            "acc1": "acc_y",
                                            "acc2": "acc_z",
                                            "Gyroscope [rad/s]": "gyr_x",
                                            "gyr1": "gyr_y",
                                            "gyr2": "gyr_z"})

Input = Input.reindex(["date",
                                     "acc_x",
                                     "acc_y",
                                     "acc_z",
                                     "gyr_x",
                                     "gyr_y",
                                     "gyr_z",
                                     "fall"],
                                    axis=1)

for i in range(len(Input)):
    Input.loc[i,['fall']] = int(0)

print(Input.head())
print(Input.describe())

Input.to_csv('DataSet/csvFiles/Input_vdo2.csv')
