from datetime import date
from lxml import objectify

import pandas as pd

def read_water_storage_series(xml_file):
    xml = objectify.parse(xml_file)
    root = xml.getroot()

    data = []
    for s in root.series:
        if not hasattr(s, 'dataset'):
            continue
        for v in s.dataset.record:
            data.append(float(v.text))

    str_date = root.configuration.xStart.text
    start_date = date(int(str_date[0:4]), int(str_date[5:6]),int(str_date[7:8]))

    dates = pd.date_range(start=start_date, periods=len(data), freq='D')

    return pd.Series(data, dates)

def read_water_storage_states(xml_file):
    xml = objectify.parse(xml_file)
    root = xml.getroot()

    state_urns = []
    for child in root.getchildren():
        if hasattr(child, 'region') and child.region.type == 'urn:bom.gov.au:awris:common:codelist:regiontype:state':
            state_urns.append(child.region.identifier.text)

    return state_urns

def read_water_storage_urns(xml_file):
    xml = objectify.parse(xml_file)
    root = xml.getroot()

    storage_urns = []
    for child in root.getchildren():
        if hasattr(child, 'region') and child.region.type == 'urn:bom.gov.au:awris:common:codelist:featuretype:waterstorage':
            storage_urns.append(child.region.identifier.text)

    return storage_urns
