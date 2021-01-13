import pandas as pd
import numpy as np
# for i in range(0,df.shape[0]-2):
#     df.loc[df.index[i+1],'SMA_3'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] )/2),1)
#print(df)


raw_data = {'month': [1,2,3,4,5,6,7,8,9,10,11,12], 'sales':[290.50,260,288,300,310,303,329.893,340.993,316,330.909,308,310]}
df = pd.DataFrame(raw_data)

def moving_average(data_frame, size):
    """This function is to find the moving average"""

    data_frame['sma'] = round(data_frame['sales'].rolling(window=size).mean(), 3)
    return  data_frame['sma']

print(moving_average(df, 3))
