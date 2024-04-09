import dataset as ds
import pandas as pd
import numpy as np

VIDEO = str(12640)
FALLVALUELIMIT = 40

Dataset = ds.DataSet()
df_acc = Dataset.getdataframeacc("DataSet/csvFiles/Originals/GX0"+VIDEO+"_HERO9 Black-ACCL.csv")
df_gyr = Dataset.getdataframegyr("DataSet/csvFiles/Originals/GX0"+VIDEO+"_HERO9 Black-GYRO.csv")
print("Video : Get Data Frame DONE !")
Dataset.dropcolumn('temperature [°C]', 'cts')
print("Video : Drop Column DONE !")
#Dataset.dropuselessvalues(5000, len(Dataset.df_acc))
print("Video : Drop Useless values DONE !")
Dataset.input = pd.merge(df_acc, df_gyr, on='date')
print("Video : Merge DataFrame DONE !")
Dataset.renamecolumns()
print("Video : Rename Column DONE !")
Dataset.input = Dataset.input.drop(axis=1, columns={'date'})
print("Video : Column date delted DONE !")
Dataset.input = Dataset.input.shift(1) - Dataset.input
print("Video : Convert to delta DONE !")

for i in range(len(Dataset.input)):
    if Dataset.input.loc[i]["acc_x"] <= -FALLVALUELIMIT or Dataset.input.loc[i]["acc_x"] >= FALLVALUELIMIT:
        Dataset.input.loc[i,['fall']] = np.absolute(int(1))
    elif Dataset.input.loc[i]["acc_y"] <= -FALLVALUELIMIT or Dataset.input.loc[i]["acc_y"] >= FALLVALUELIMIT:
        Dataset.input.loc[i,['fall']] = np.absolute(int(1))
    elif Dataset.input.loc[i]["acc_z"] <= -FALLVALUELIMIT or Dataset.input.loc[i]["acc_z"] >= FALLVALUELIMIT:
        Dataset.input.loc[i,['fall']] = np.absolute(int(1))
    else :
        Dataset.input.loc[i,['fall']] = int(0)

print("Video : Add Falling Data DONE !")
print(Dataset.input.dtypes)
print(Dataset.input.describe())
print(Dataset.input.head())
Dataset.createcsv('DataSet/csvFiles/csvDelta/Input_vdo'+VIDEO+'_delta.csv')
print("Video : csv DONE !")