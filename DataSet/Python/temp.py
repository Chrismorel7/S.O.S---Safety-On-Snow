import dataset as ds
import pandas as pd

VIDEO = 12644

Dataset = ds.DataSet()
df_acc = Dataset.getdataframeacc("DataSet/csvFiles/Originals/GX0"+str(VIDEO)+"_HERO9 Black-ACCL.csv")
df_gyr = Dataset.getdataframegyr("DataSet/csvFiles/Originals/GX0"+str(VIDEO)+"_HERO9 Black-GYRO.csv")
print("Video : Get Data Frame DONE !")
Dataset.dropcolumn('temperature [°C]', 'cts')
print("Video : Drop Column DONE !")
#Dataset.dropuselessvalues(5000, len(Dataset.df_acc))
print("Video : Drop Useless values DONE !")
Dataset.input = pd.merge(df_acc, df_gyr, on='date')
print("Video : Merge DataFrame DONE !")
Dataset.renamecolumns()
print("Video : Rename Column DONE !")
Dataset.addfallingdata(9999)
print("Video 1 : Add Falling Data DONE !")
Dataset.createcsv('DataSet/csvFiles/csv/Input_vdo'+str(VIDEO)+'.csv')
print("Video : DONE !")


Dataset_delta = ds.DataSet()
Dataset_delta.input = Dataset.input.drop(axis=1, columns={'date'})
Dataset_delta.createdeltadf()
print(Dataset_delta.input)
print(Dataset_delta.inputdelta)
print(Dataset_delta.input.dtypes)
Dataset_delta.createdeltacsv('DataSet/csvFiles/csvDelta/Input_vdo'+str(VIDEO)+'_delta.csv')
print("Video 1 delta : DONE !")