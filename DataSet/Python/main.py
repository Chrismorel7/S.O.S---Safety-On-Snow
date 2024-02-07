"""main"""
import dataset as ds


# ----------  Video 1  ----------
Dataset1 = ds.DataSet()
df_acc_vdo_1 = Dataset1.getdataframeacc("DataSet/csvFiles/GH011015_HERO9 Black-ACCL.csv")
df_gyr_vdo_1 = Dataset1.getdataframegyr("DataSet/csvFiles/GH011015_HERO9 Black-GYRO.csv")
Dataset1.dropcolumn('temperature [°C]', 'cts')
Dataset1.dropuselessvalues(7674, len(Dataset1.df_acc))
Dataset1.mergedataframe()
Dataset1.addfallingdata(49)
Dataset1.createcsv('DataSet/csvFiles/Input_vdo1.csv')

# ----------  Video 2  ----------
Dataset2 = ds.DataSet()
df_acc_vdo_2 = Dataset2.getdataframeacc("DataSet/csvFiles/GH011042_HERO9 Black-ACCL.csv")
df_gyr_vdo_2 = Dataset2.getdataframegyr("DataSet/csvFiles/GH011042_HERO9 Black-GYRO.csv")
Dataset2.dropcolumn('temperature [°C]', 'cts')
Dataset2.mergedataframe()
Dataset2.addfallingdata(999) # beacause there's no fall in this video
Dataset2.createcsv('DataSet/csvFiles/Input_vdo2.csv')
