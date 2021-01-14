import pandas as pd
from utils_calculations import calculate_sma, compare_sma
from pull_json_from_api import pull_data_from_api

def example_calculate_sma():
    index = pd.date_range('2/1/2020', periods=20, freq='T')
    df = pd.DataFrame(data=range(20), index=index, columns=['count'])
    print(df)
    # print()
    result = calculate_sma(["2", "3"], df)
    return result


def example_compare_sma(data):
    print(compare_sma(data))


def exampale_data_pull_from_api(time_refresh, symbol):
    pull_data_from_api(time_refresh)
if __name__ == '__main__':
    # test sma
    result_sma = example_calculate_sma()
    example_compare_sma(result_sma)
