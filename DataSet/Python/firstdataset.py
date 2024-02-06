"""Create a DataSet based on video 1 data."""

import pandas as pd

df_acc = pd.read_csv('DataSet/csvFiles/GH011015_HERO9 Black-ACCL.csv')
df_gyr = pd.read_csv('DataSet/csvFiles/GH011015_HERO9 Black-GYRO.csv')

df_acc = df_acc.drop(axis=1, columns={'temperature [°C]', 'cts'})
df_gyr = df_gyr.drop(axis=1, columns={'temperature [°C]', 'cts'})

Input_acc = pd.DataFrame(df_acc.drop(df_acc.index[range(7674, len(df_acc))]))
Input_gyr = pd.DataFrame(df_gyr.drop(df_gyr.index[range(7674, len(df_gyr))]))
Input = pd.merge(Input_acc, Input_gyr)

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
    if Input.loc[i]["acc_x"] <= -49 or Input.loc[i]["acc_x"] >= 49:
        Input.loc[i,['fall']] = int(1)
    elif Input.loc[i]["acc_y"] <= -49 or Input.loc[i]["acc_y"] >= 49:
        Input.loc[i,['fall']] = int(1)
    elif Input.loc[i]["acc_z"] <= -49 or Input.loc[i]["acc_z"] >= 49:
        Input.loc[i,['fall']] = int(1)
    else :
        Input.loc[i,['fall']] = int(0)

print(Input.head())
print(Input.describe())

Input.to_csv('DataSet/csvFiles/Input_vdo1.csv')
