import numpy as np
import pandas as pd

from bom_data_parser import mapper

def read_climate_data_online_csv(fname):
    df = pd.read_csv(fname, parse_dates={'Date': [2,3,4]})

    column_names = []
    for column in df.columns:
        column_names.append(mapper.convert_key(column))

    df.columns = column_names

    df = df.set_index('Date')

    redundant_columns = [
            'Product code',
            'Bureau of Meteorology station number'
        ]

    attributes = {}

    for column in redundant_columns:
        assert np.all(df[column] == df[column][0])
        attributes[column] = df[column][0]
        df = df.drop(column, axis = 1)

    return df, attributes
