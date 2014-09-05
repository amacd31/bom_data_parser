import pandas as pd

from bom_data_parser import mapper

def read_acorn_sat_csv(fname):
    with open(fname) as f:
        header_line = f.readline()

    measurand = mapper.convert_key(header_line[0:8])

    missing_value_key = 'missing_value='
    missing_value_start = header_line.index(missing_value_key)+len(missing_value_key)
    missing_value = header_line[missing_value_start:].split(' ')[0]

    df = pd.read_csv(fname, parse_dates=[0], index_col=0, sep=r"\s+", header=None, skiprows=1, na_values=missing_value, names=['Date',measurand])

    return df, None
