import numpy as np


def calculate_sma(list_of_periods, data_frame):
    result_of_sma = list()
    for period in list_of_periods:
        period = period + "T"
        sma = data_frame.resample(period).mean()
        result_of_sma.append(sma)
    print(result_of_sma)

    return result_of_sma


def compare_sma(list_data_frame):
    result = None

    if len(list_data_frame):
        first_sma_data_frame = list_data_frame[0]
        first_column = list(first_sma_data_frame.columns)[0]
        second_sma_data_frame = list_data_frame[1]
        second_column = list(second_sma_data_frame.columns)[0]

        first_sma_data_frame[first_column + "_"] = second_sma_data_frame[second_column]
        first_sma_data_frame = first_sma_data_frame.fillna(0)

        first_sma_data_frame['crossover'] = np.where(
            first_sma_data_frame[first_column] == first_sma_data_frame[first_column + "_"],
            'True', 'False')
        first_sma_data_frame = first_sma_data_frame.loc[first_sma_data_frame['crossover'] == 'True']
        if not len(first_sma_data_frame) == 0:
            first_sma_data_frame.index = first_sma_data_frame.index.map(str)
            result = first_sma_data_frame.index.tolist()

    return result
