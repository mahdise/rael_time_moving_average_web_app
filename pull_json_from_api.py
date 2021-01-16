import threading
import time
import os
import io
import json
import requests
import pandas as pd

from utils_calculations import calculate_sma, compare_sma
from get_data import ExtractData
exitFlag = 0


class CallApi(threading.Thread):
    def __init__(self, refresh_time, symbol,period_first, period_second, interval_time):
        threading.Thread.__init__(self)
        self.refresh_time = refresh_time
        self.interval_time = interval_time
        self.symbol = symbol
        self.period_first = period_first
        self.period_second = period_second
        self.run_time = True
        self.api_key = 'b97ec7bc8b5e0f368b7db0a58cdebf55'
        self.api_base_url = 'https://api.marketstack.com/v1/'
        self.session = requests.session()
        self.output = os.path.join('data', 'extract', 'prices.json')

    def run(self):

        while self.run_time:
            print("call every " + str(self.refresh_time) + "s")

            list_of_data_frame = list()
            for symbol in self.symbol:

                obj = ExtractData()
                data_list = obj.getData(symbol, '1min')
                # print(data_list)
                df = pd.DataFrame(columns=["date_time", "price"])
                for index, data_time in enumerate(data_list):
                    df.loc[index] = [data_time["date"]] + [data_time["last"]]
                df["date_time"] = pd.to_datetime(df['date_time'])
                # print(df.dtypes)
                # print(df)
                df.set_index('date_time', inplace=True)

                # print(df.dtypes)
                sma = calculate_sma([self.period_first, self.period_second], df)
                crossover_result = compare_sma(sma)
                if crossover_result:
                    print("crossover_time : ",crossover_result)
                else:
                    print("do not have crossover")

            time.sleep(self.refresh_time)


def pull_data_from_api(time_refresh, symbol, period_first, period_second, interval="1min"):
    pull_data = CallApi(time_refresh, symbol,period_first,period_second, interval)
    pull_data.start()


if __name__ == '__main__':
    pull_data_from_api(time_refresh=60, symbol=["AMD"], period_first="2", period_second="5")
