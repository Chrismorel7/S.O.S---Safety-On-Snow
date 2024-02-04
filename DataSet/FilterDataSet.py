# Importation des bibliothèque
## pandas --> Gerer les fichiers csv + DataScience
## numpy --> Gerer des matrices et des tables de données
## pyplot --> Gerer les matrices et les afficher sous forme de graphique
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

GH011015_acc_df = pd.read_csv('DataSet/csvFiles/GH011015_HERO9 Black-ACCL.csv')
GH011015_gyr_df = pd.read_csv('DataSet/csvFiles/GH011015_HERO9 Black-GYRO.csv')
GH011042_acc_df = pd.read_csv('DataSet/csvFiles/GH011042_HERO9 Black-ACCL.csv')
GH011042_gyr_df = pd.read_csv('DataSet/csvFiles/GH011042_HERO9 Black-GYRO.csv')