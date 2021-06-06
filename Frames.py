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
        self.data = df_

    def SizzSub(self,col):
        first_ = int(self.data[col].index[0])
        self.data['index'] = self.data[col].index
        self.data['colval'] = self.data['index'].apply(lambda x: self.data[col][x] if ( x == first_) else self.data[col][x-1])
        self.data[col + "SizzSub"] = abs( (self.data[col] - self.data['colval']).round(4) )

        self.data.drop('index',axis=1, inplace=True)
        self.data.drop('colval',axis=1, inplace=True)
        
    def SizzRep(self,col):
        self.data['index'] = self.data[col].index
        self.data['colval'] = self.data['index'].apply(lambda x: self.data[col][x] if ( x == first_) else self.data[col][x-1])
        #self.data[col + "SizzRep"] = abs( (self.data[col] - self.data['colval']).round(4) )

        #self.data.drop('index',axis=1, inplace=True)
        #self.data.drop('colval',axis=1, inplace=True)
        


