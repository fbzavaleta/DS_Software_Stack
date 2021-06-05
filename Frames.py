import pandas as pd
import matplotlib.pyplot as plt
import math

class Frame():

    def __init__(self, path_):

        self.path = path_
        self.data =pd.read_csv(filepath_or_buffer=path_, delimiter=',')

    def clean(self, subs:bool):
        Ncol = len( self.data.columns )
        self.data.dropna(inplace=True, thresh=Ncol, axis=0)# elimina lineas vacias

        if subs:
            for i in self.data.columns[1:]:
                self.data[i].fillna( method='ffill', inplace=True)

    def split_datetime(self, col:str, delimiter:str, dropit:bool):
        field_split = self.data[col].str.split(delimiter)
        self.data['Fecha'] = field_split.apply(lambda x: x[0])
        self.data['Time']  = field_split.apply(lambda x: x[1])
        self.data.drop(col,axis=1, inplace=True)

    def dec_time(self, delimiter:str):
        field_split = self.data['Time'].str.split(delimiter)
        self.data['Hora']     = field_split.apply(lambda x: float(x[0]) + float(x[1]) / 60 + float(x[2])/3600)

    def check_decimals(self, col:str, digits:int, dropit:bool):
        self.data[col+'ajus'] = self.data[col].apply( lambda x: (x/(pow(10, len(str(round(x))) - digits))) if (digits != len(str(round(x)))) else x)
        self.data.drop(col,axis=1, inplace=True)

class Granularity():

    def __init__(self, df_):
        self.df = df_

    def fname(arg):
        pass
        
class Utilities():

    def __init__(self, df_):
        self.df = df_

    def SizzSub(col):
        first_ = self.df[col].index[0]
        self.df['index'] = self.df[col].index
        self.df['colval'] = self.df['index'].apply(lambda x: 0 if ( x == first_) else df_[col][x-1])
        self.df[col + "SizzSub"] = (self.df[col] - self.df['colval']).round(4)

        self.df.drop('index',axis=1, inplace=True)
        self.df.drop('colval',axis=1, inplace=True)
        
        


