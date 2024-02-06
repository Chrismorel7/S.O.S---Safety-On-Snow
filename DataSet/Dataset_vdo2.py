import pandas as pd

GH011042_acc_df = pd.read_csv('DataSet/csvFiles/GH011042_HERO9 Black-ACCL.csv')
GH011042_gyr_df = pd.read_csv('DataSet/csvFiles/GH011042_HERO9 Black-GYRO.csv')

GH011042_acc_df = GH011042_acc_df.drop(axis=1, columns={'temperature [°C]', 'cts'})
GH011042_gyr_df = GH011042_gyr_df.drop(axis=1, columns={'temperature [°C]', 'cts'})

Video2_input = pd.merge(GH011042_acc_df, GH011042_gyr_df)

Video2_input = Video2_input.rename(columns={"Accelerometer [m/s2]": "acc_x",
                                            "acc1": "acc_y",
                                            "acc2": "acc_z",
                                            "Gyroscope [rad/s]": "gyr_x",
                                            "gyr1": "gyr_y",
                                            "gyr2": "gyr_z"})

Video2_input = Video2_input.reindex(["date", "acc_x", "acc_y", "acc_z", "gyr_x", "gyr_y", "gyr_z", "fall"], axis=1)

for i in range(len(Video2_input)):
    Video2_input.loc[i,['fall']] = int(0)

print(Video2_input.head())
print(Video2_input.describe())

Video2_input.to_csv('DataSet/csvFiles/Input_vdo2.csv')
