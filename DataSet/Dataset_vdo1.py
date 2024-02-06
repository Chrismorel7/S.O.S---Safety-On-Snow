# Importation des bibliothèque
## pandas --> Gerer les fichiers csv + DataScience
import pandas as pd

GH011015_acc_df = pd.read_csv('DataSet/csvFiles/GH011015_HERO9 Black-ACCL.csv')
GH011015_gyr_df = pd.read_csv('DataSet/csvFiles/GH011015_HERO9 Black-GYRO.csv')

GH011015_acc_df = GH011015_acc_df.drop(axis=1, columns={'temperature [°C]', 'cts'})
GH011015_gyr_df = GH011015_gyr_df.drop(axis=1, columns={'temperature [°C]', 'cts'})

Video1_Input_acc = pd.DataFrame(GH011015_acc_df.drop(GH011015_acc_df.index[range(7674, len(GH011015_acc_df))]))
Video1_Input_gyr = pd.DataFrame(GH011015_gyr_df.drop(GH011015_gyr_df.index[range(7674, len(GH011015_gyr_df))]))
Video1_Input = pd.merge(Video1_Input_acc, Video1_Input_gyr)

Video1_Input = Video1_Input.rename(columns={"Accelerometer [m/s2]": "acc_x",
                                            "acc1": "acc_y",
                                            "acc2": "acc_z",
                                            "Gyroscope [rad/s]": "gyr_x",
                                            "gyr1": "gyr_y",
                                            "gyr2": "gyr_z"})

Video1_Input = Video1_Input.reindex(["date", "acc_x", "acc_y", "acc_z", "gyr_x", "gyr_y", "gyr_z"], axis=1)

for i in range(len(Video1_Input)):
    if Video1_Input.loc[i]["acc_x"] <= -49 or Video1_Input.loc[i]["acc_x"] >= 49:
        Video1_Input.loc[i,['fall']] = int(1)
    elif Video1_Input.loc[i]["acc_y"] <= -49 or Video1_Input.loc[i]["acc_y"] >= 49:
        Video1_Input.loc[i,['fall']] = int(1)
    elif Video1_Input.loc[i]["acc_z"] <= -49 or Video1_Input.loc[i]["acc_z"] >= 49:
        Video1_Input.loc[i,['fall']] = int(1)
    else :
        Video1_Input.loc[i,['fall']] = int(0)
        
print(Video1_Input.head())
print(Video1_Input.describe())

Video1_Input.to_csv('DataSet/csvFiles/Video1_Input.csv')