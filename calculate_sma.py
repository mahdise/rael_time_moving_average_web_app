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
    data_frame = {'time': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                  'price': [290, 260, 288, 300, 310, 303, 329, 340, 316, 330, 308, 310]}

    df = pd.DataFrame(data_frame)
    resample_data_frame = None
    return resample_data_frame
    pass

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


