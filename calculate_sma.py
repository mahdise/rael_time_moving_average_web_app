import pandas as pd
from get_data import ExtractData
#seam
def read_and_procees_data():
    obj = ExtractData()
    data = obj.getData('AMD','1hour')
    
   # print("from calculate sma",data)

    df = pd.DataFrame(data)
    return df



#mahdi
def resample_data_based_on_input(interval_time=1, data_frame=None):
    index = pd.date_range('2/1/2020', periods=9, freq='T')
    df = pd.DataFrame(data=range(9), index=index, columns=['count'])

    return data_frame.resample(interval_time).mean()

#moving average
def moving_average(data_frame, size):
    """This function is to find the moving average"""

    data_frame['sma'] = round(data_frame['sales'].rolling(window=size).mean(), 3)
    return  data_frame['sma']

print(moving_average(df, 3))

if __name__ == '__main__':
   # procees_data = read_and_procees_data
   df = read_and_procees_data()
   print(df.head())


