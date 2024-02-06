# Importation des bibliothèque
## pandas --> Gerer les fichiers csv + DataScience
## numpy --> Gerer des matrices et des tables de données
## pyplot --> Gerer les matrices et les afficher sous forme de graphique
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

GH011015_acc_df = pd.read_csv('DataSet/csvFiles/GH011015_HERO9 Black-ACCL.csv') #import video1 acc csv
GH011015_gyr_df = pd.read_csv('DataSet/csvFiles/GH011015_HERO9 Black-GYRO.csv') #import video1 gyr csv
GH011042_acc_df = pd.read_csv('DataSet/csvFiles/GH011042_HERO9 Black-ACCL.csv') #import video2 acc csv
GH011042_gyr_df = pd.read_csv('DataSet/csvFiles/GH011042_HERO9 Black-GYRO.csv') #import video2 gyr csv

GH011015_acc_df = GH011015_acc_df.drop(axis=1, columns={'temperature [°C]', 'cts'})
GH011015_gyr_df = GH011015_gyr_df.drop(axis=1, columns={'temperature [°C]', 'cts'})
GH011042_acc_df = GH011042_acc_df.drop(axis=1, columns={'temperature [°C]', 'cts'})
GH011042_gyr_df = GH011042_gyr_df.drop(axis=1, columns={'temperature [°C]', 'cts'})

print('011015_acc :')
print(GH011015_acc_df.describe())
print('\n\n')

Video1_Input_acc = pd.DataFrame(GH011015_acc_df.drop(GH011015_acc_df.index[range(7674, len(GH011015_acc_df))]))
print(Video1_Input_acc.head())
Video1_Input_gyr = pd.DataFrame(GH011015_gyr_df.drop(GH011015_gyr_df.index[range(7674, len(GH011015_gyr_df))]))
print(Video1_Input_gyr.head())

Video1_Input = pd.merge(Video1_Input_acc, Video1_Input_gyr)

Video1_Input = Video1_Input.rename(columns={"Accelerometer [m/s2]": "acc_x",
                                            "acc1": "acc_y",
                                            "acc2": "acc_z",
                                            "Gyroscope [rad/s]": "gyr_x",
                                            "gyr1": "gyr_y",
                                            "gyr2": "gyr_z"})