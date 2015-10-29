import numpy as np
import pandas as pd
import zipfile

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

def read_climate_data_online_zip(fname):
    """
        Read data straight out of zipfile.

        ..note: Requires the filename to have been unchanged because it is used for identifying the contained data file.
    """
    filename = fname.split('.')[0]
    with zipfile.ZipFile('{0}.zip'.format(filename)) as zf:
        #notes = zf.read('{0}_Note.txt'.format(filename))
        with zf.open('{0}_Data.csv'.format(filename)) as dfile:
            df, attributes = read_climate_data_online_csv(dfile)

    return df, attributes
