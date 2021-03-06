import threading
import time
import os
import requests
import pandas as pd

from stockcrossover.checkcrossover.utils import calculate_sma, compare_sma
from stockcrossover.checkcrossover.extract_data_from_api import ExtractData

exitFlag = 0


class CallApi(threading.Thread):
    def __init__(self, symbol, period_first, period_second, refresh_time, interval_time):
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

            crossover_ = dict()

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
                    crossover_[symbol] = crossover_result
                    # Todo (need to save into data base)
                    # need to save into data base
                else:
                    crossover_[symbol] = "No Crossover"

                #     print("crossover_time : ", crossover_result)
                # else:
                #     print("do not have crossover")
            print(crossover_)
            time.sleep(self.refresh_time)


def pull_data_from_api(symbol, period_first, period_second, time_refresh=60, interval="1min"):
    pull_data = CallApi( symbol, period_first, period_second,time_refresh, interval)
    pull_data.start()


if __name__ == '__main__':
    pull_data_from_api(symbol=["AMD","AAPL"], period_first="2", period_second="5",time_refresh=30)
