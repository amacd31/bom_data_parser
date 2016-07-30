import logging
import pandas as pd

from bom_data_parser import mapper

logger = logging.getLogger(__name__)

def read_hrs_csv(fname):
    attributes = {}
    hrs_header_len = 26
    with open(fname) as f:
        header=[next(f) for x in range(hrs_header_len)]
        logging.debug(header)
        if header[3] == '#,"Daily streamflow (ML/day) and quality code"\n':
            logging.debug("Original format HRS")
            hrs_header_len = 18
            attributes['station_name'] = header[10][3:-2]
            attributes['catchment_area'] = float(header[11].split(',')[2])
            location = header[12].split(',')
            attributes['latitude'] = float(location[2])
            attributes['longitude'] = float(location[4]) * -1 # Negative for 'degrees S'
        elif header[3] == '#,"Dataset version: October, 2015"\n':
            logging.debug("October 2015, format HRS")
            hrs_header_len = 26
            attributes['station_name'] = header[14][3:-2]
            attributes['catchment_area'] = float(header[15].split(',')[2])
            location = header[16].split(',')
            attributes['latitude'] = float(location[2])
            attributes['longitude'] = float(location[4]) * -1 # Negative for 'degrees S'
        else:
            raise NotImplementedError("Unsupported HRS data format.")

    logging.debug("hrs_header_len: %s", hrs_header_len)
    df = pd.read_csv(fname, parse_dates=True, index_col='Date', skiprows=hrs_header_len)

    return df, attributes
