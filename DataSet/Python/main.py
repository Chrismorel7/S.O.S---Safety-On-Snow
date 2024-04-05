"""main"""
import dataset as ds
import pandas as pd

# ----------  Video 1  ----------
Dataset1 = ds.DataSet()
df_acc_vdo_1 = Dataset1.getdataframeacc("DataSet/csvFiles/Originals/GH011015_HERO9 Black-ACCL.csv")
df_gyr_vdo_1 = Dataset1.getdataframegyr("DataSet/csvFiles/Originals/GH011015_HERO9 Black-GYRO.csv")
Dataset1.dropcolumn('temperature [°C]', 'cts')
Dataset1.dropuselessvalues(7674, len(Dataset1.df_acc))
Dataset1.mergedataframe()
Dataset1.renamecolumns()
Dataset1.addfallingdata(49)
Dataset1.createcsv('DataSet/csvFiles/csv/Input_vdo1.csv')
print("Video 1 : DONE !")


# ----------  Video 2  ----------
Dataset2 = ds.DataSet()
df_acc_vdo_2 = Dataset2.getdataframeacc('DataSet/csvFiles/Originals/GH011042_HERO9 Black-ACCL.csv')
df_gyr_vdo_2 = Dataset2.getdataframegyr('DataSet/csvFiles/Originals/GH011042_HERO9 Black-GYRO.csv')
Dataset2.dropcolumn('temperature [°C]', 'cts')
Dataset2.input = pd.merge(df_acc_vdo_2, df_gyr_vdo_2)
Dataset2.renamecolumns()
Dataset2.addfallingdata(9999)
Dataset2.input.to_csv('DataSet/csvFiles/csv/Input_vdo2.csv')
print("Video 2 : DONE !")


# ----------  Video 3  ----------
Dataset3 = ds.DataSet()
df_acc_vdo_3 = Dataset3.getdataframeacc("DataSet/csvFiles/Originals/GX012550_HERO9 Black-ACCL.csv")
print(df_acc_vdo_3.head())
df_gyr_vdo_3 = Dataset3.getdataframegyr("DataSet/csvFiles/Originals/GX012550_HERO9 Black-GYRO.csv")
print(df_gyr_vdo_3.head())
Dataset3.dropcolumn('temperature [°C]', 'cts')
Dataset3.input = pd.merge(df_acc_vdo_3, df_gyr_vdo_3, on='date')
Dataset3.renamecolumns()
Dataset3.addfallingdata(9999)
Dataset3.input.to_csv('DataSet/csvFiles/csv/Input_vdo3.csv')
print("Video 3 : DONE !")


# ----------  ALL  ----------
#ds.dfcombined("DataSet/csvFiles/Input_vdo1.csv",
#              "DataSet/csvFiles/Input_vdo2.csv", 
#              "DataSet/csvFiles/Input_vdo3.csv", 
#              "DataSet/csvFiles/Input.csv")
#

## ----------  Video 1 (delta) ----------
Dataset1_delta = ds.DataSet()
Dataset1_delta.input = Dataset1.input.drop(axis=1, columns={'date'})
Dataset1_delta.createdeltadf()
print(Dataset1_delta.input)
print(Dataset1_delta.inputdelta)
print(Dataset1_delta.input.dtypes)
Dataset1_delta.createdeltacsv('DataSet/csvFiles/csvDelta/Input_vdo1_delta.csv')
print("Video 1 delta : DONE !")


# ----------  Video 2 (delta) ----------
Dataset2_delta = ds.DataSet()
Dataset2_delta.input = Dataset2.input.drop(axis=1, columns={'date'})
Dataset2_delta.createdeltadf()
print(Dataset2_delta.input)
print(Dataset2_delta.inputdelta)
print(Dataset2_delta.input.dtypes)
Dataset2_delta.createdeltacsv('DataSet/csvFiles/csvDelta/Input_vdo2_delta.csv')
print("Video 2 delta : DONE !")


# ----------  Video 3 (delta) ----------
Dataset3_delta = ds.DataSet()
Dataset3_delta.input = Dataset3.input.drop(axis=1, columns={'date'})
Dataset3_delta.createdeltadf()
print(Dataset3_delta.input)
print(Dataset3_delta.inputdelta)
print(Dataset3_delta.input.dtypes)
Dataset3_delta.createdeltacsv('DataSet/csvFiles/csvDelta/Input_vdo2_delta.csv')
print("Video 3 delta : DONE !")
