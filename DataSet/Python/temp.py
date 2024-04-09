import dataset as ds
import pandas as pd

Dataset = ds.DataSet()
df_acc = Dataset.getdataframeacc("DataSet/csvFiles/Originals/GX012639_HERO9 Black-ACCL.csv")
df_gyr = Dataset.getdataframegyr("DataSet/csvFiles/Originals/GX012639_HERO9 Black-GYRO.csv")
print("Video : Get Data Frame DONE !")
Dataset.dropcolumn('temperature [°C]', 'cts')
print("Video : Drop Column DONE !")
#Dataset.dropuselessvalues(5000, len(Dataset.df_acc))
print("Video : Drop Useless values DONE !")
Dataset.input = pd.merge(df_acc, df_gyr, on='date')
print("Video : Merge DataFrame DONE !")
Dataset.renamecolumns()
print("Video : Rename Column DONE !")
Dataset.addfallingdata(999)
print("Video 1 : Add Falling Data DONE !")
Dataset.createcsv('DataSet/csvFiles/csv/Input_vdo12639.csv')
print("Video : DONE !")


Dataset_delta = ds.DataSet()
Dataset_delta.input = Dataset.input.drop(axis=1, columns={'date'})
Dataset_delta.createdeltadf()
print(Dataset_delta.input)
print(Dataset_delta.inputdelta)
print(Dataset_delta.input.dtypes)
Dataset_delta.createdeltacsv('DataSet/csvFiles/csvDelta/Input_vdo12639_delta.csv')
print("Video 1 delta : DONE !")