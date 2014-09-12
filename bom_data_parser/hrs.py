import pandas as pd

from bom_data_parser import mapper

def read_hrs_csv(fname):
    attributes = {}
    hrs_header_len = 18
    with open(fname) as f:
        header=[next(f) for x in range(hrs_header_len)]
        attributes['station_name'] = header[10][3:-2]
        attributes['catchment_area'] = float(header[11].split(',')[2])
        location = header[12].split(',')
        attributes['latitude'] = float(location[2])
        attributes['longitude'] = float(location[4]) * -1 # Negative for 'degrees S'
        header = ''.join(header)

    df = pd.read_csv(fname, parse_dates=True, index_col='Date', skiprows=hrs_header_len)

    return df, attributes
