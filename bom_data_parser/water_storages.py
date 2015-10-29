from datetime import date
from lxml import objectify

import pandas as pd

def read_water_storage_series(xml_file):
    xml = objectify.parse(xml_file)
    root = xml.getroot()

    data = []
    for s in root.series:
        for v in s.dataset.record:
            data.append(float(v.text))

    str_date = root.configuration.xStart.text
    start_date = date(int(str_date[0:4]), int(str_date[5:6]),int(str_date[7:8]))

    dates = pd.date_range(start=start_date, periods=len(data), freq='D')

    return pd.Series(data, dates)
