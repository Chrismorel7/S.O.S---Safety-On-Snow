"""Create a DataSet based on video 1 data."""

import pandas as pd

class DataSet1(object):
    """Create a DataSet based on video 1 data."""
    def __init__(self):
        self.df_acc = pd.DataFrame()
        self.df_gyr = pd.DataFrame()
        self.input_acc = pd.DataFrame()
        self.input_gyr = pd.DataFrame()
        self.input = pd.DataFrame()

    def getdataframeacc(self, path):
        """Create a Dataframe based on acc csv"""
        self.df_acc = pd.read_csv(path) #DataSet/csvFiles/GH011015_HERO9 Black-ACCL.csv
        return self.df_acc

    def getdataframegyr(self, path):
        """Create a DataFrame based on Gyr csv"""
        self.df_gyr = pd.read_csv(path) #DataSet/csvFiles/GH011015_HERO9 Black-GYRO.csv
        return self.df_gyr

    def dropcolumn(self, column1, column2):
        """Drop useless columns"""
        self.df_acc = self.df_acc.drop(axis=1, columns={column1, column2}) #'temperature [°C]', 'cts'
        self.df_gyr = self.df_gyr.drop(axis=1, columns={column1, column2}) #'temperature [°C]', 'cts'

    def dropuselessvalues(self, intervalstart, intervalend):
        """Drop useless value that were in the csv """
        self.input_acc = self.df_acc.drop(self.df_acc.index[range(intervalstart, intervalend)]) # 7674, len(df_acc)
        self.input_gyr = self.df_gyr.drop(self.df_gyr.index[range(intervalstart, intervalend)]) # 7674, len(df_acc)

    def mergedataframe(self):
        """Merge the accelerometer and gyroscopic DataFrame"""
        self.input = pd.merge(self.input_acc, self.input_gyr)

        self.input = self.input.rename(columns={"Accelerometer [m/s2]": "acc_x",
                                                "acc1": "acc_y",
                                                "acc2": "acc_z",
                                                "Gyroscope [rad/s]": "gyr_x",
                                                "gyr1": "gyr_y",
                                                "gyr2": "gyr_z"})

        self.input = self.input.reindex(["date",
                                        "acc_x",
                                        "acc_y",
                                        "acc_z",
                                        "gyr_x",
                                        "gyr_y",
                                        "gyr_z",
                                        "fall"],
                                        axis=1)

    def addfallingdata(self, fallvaluelimit): #49
        """Add 1 (fall) or 0(user is ok) to the input DataFrame"""
        for i in range(len(self.input)):
            if self.input.loc[i]["acc_x"] <= -fallvaluelimit or self.input.loc[i]["acc_x"] >= fallvaluelimit:
                self.input.loc[i,['fall']] = int(1)
            elif self.input.loc[i]["acc_y"] <= -fallvaluelimit or self.input.loc[i]["acc_y"] >= fallvaluelimit:
                self.input.loc[i,['fall']] = int(1)
            elif self.input.loc[i]["acc_z"] <= -fallvaluelimit or self.input.loc[i]["acc_z"] >= fallvaluelimit:
                self.input.loc[i,['fall']] = int(1)
            else :
                self.input.loc[i,['fall']] = int(0)

    def createcsv(self):
        """Create a csv based on input DataFrame"""
        self.input.to_csv('DataSet/csvFiles/Input_vdo1.csv')
