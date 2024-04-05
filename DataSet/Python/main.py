"""main"""
import dataset as ds
import pandas as pd


# ----------  Video 1  ----------
#Dataset1 = ds.DataSet()
#df_acc_vdo_1 = Dataset1.getdataframeacc("DataSet/csvFiles/GH011015_HERO9 Black-ACCL.csv")
#df_gyr_vdo_1 = Dataset1.getdataframegyr("DataSet/csvFiles/GH011015_HERO9 Black-GYRO.csv")
#Dataset1.dropcolumn('temperature [°C]', 'cts')
#Dataset1.dropuselessvalues(7674, len(Dataset1.df_acc))
#Dataset1.mergedataframe()
#Dataset1.renamecolumns()
#Dataset1.addfallingdata(49)
#Dataset1.createcsv('DataSet/csvFiles/Input_vdo1.csv')
#
## ----------  Video 2  ----------
#Dataset2 = ds.DataSet()
#df_acc_vdo_2 = Dataset2.getdataframeacc('DataSet/csvFiles/GH011042_HERO9 Black-ACCL.csv')
#df_gyr_vdo_2 = Dataset2.getdataframegyr('DataSet/csvFiles/GH011042_HERO9 Black-GYRO.csv')
#Dataset2.dropcolumn('temperature [°C]', 'cts')
#Dataset2.input = pd.merge(df_acc_vdo_2, df_gyr_vdo_2)
#Dataset2.renamecolumns()
#Dataset2.addfallingdata(9999)
#Dataset2.input.to_csv('DataSet/csvFiles/Input_vdo2.csv')
#
## ----------  Video 3  ----------
#Dataset3 = ds.DataSet()
#df_acc_vdo_3 = Dataset3.getdataframeacc("DataSet/csvFiles/GX012550_HERO9 Black-ACCL.csv")
#print(df_acc_vdo_3.head())
#df_gyr_vdo_3 = Dataset3.getdataframegyr("DataSet/csvFiles/GX012550_HERO9 Black-GYRO.csv")
#print(df_gyr_vdo_3.head())
#Dataset3.dropcolumn('temperature [°C]', 'cts')
#Dataset3.input = pd.merge(df_acc_vdo_3, df_gyr_vdo_3, on='date')
#Dataset3.renamecolumns()
#Dataset3.addfallingdata(9999)
#Dataset3.input.to_csv('DataSet/csvFiles/Input_vdo3.csv')

# ----------  ALL  ----------
##ds.dfcombined("DataSet/csvFiles/Input_vdo1.csv",
#              "DataSet/csvFiles/Input_vdo2.csv", 
#              "DataSet/csvFiles/Input_vdo3.csv", 
#              "DataSet/csvFiles/Input.csv")
#

# ----------  Video 1 (delta) ----------
Dataset1_delta = ds.DataSet()
df_acc_vdo_1 = Dataset1_delta.getdataframeacc("DataSet/csvFiles/GH011015_HERO9 Black-ACCL.csv")
df_gyr_vdo_1 = Dataset1_delta.getdataframegyr("DataSet/csvFiles/GH011015_HERO9 Black-GYRO.csv")
Dataset1_delta.dropcolumn('temperature [°C]', 'cts')
Dataset1_delta.dropuselessvalues(7674, len(Dataset1_delta.df_acc))
Dataset1_delta.mergedataframe()
Dataset1_delta.renamecolumns()
Dataset1_delta.input = Dataset1_delta.input.drop(axis=1, columns={'date'})
Dataset1_delta.createdeltadf()
print(Dataset1_delta.input)
print(Dataset1_delta.inputdelta)
print(Dataset1_delta.input.dtypes)
Dataset1_delta.createdeltacsv('DataSet/csvFiles/Input_vdo1_delta.csv')