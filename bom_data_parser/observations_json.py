import json
import pandas as pd

def parse_json(station_json):
    if list(station_json.keys()) != ['observations']:
        raise Exception('No observations key; Not 72 hour observations json format')

    attributes = {
            'station_id': station_json['observations']['header'][0]['ID'],
            'name': station_json['observations']['data'][0]['name'],
            'history_product': station_json['observations']['data'][0]['history_product'],
            'wmo': station_json['observations']['data'][0]['wmo'],
            'lat': station_json['observations']['data'][0]['lat'],
            'lon': station_json['observations']['data'][0]['lon'],
            'header': station_json['observations']['header'][0],
            'notice': station_json['observations']['notice'][0]
            }

    df = pd.read_json(json.dumps(station_json['observations']['data']))
    df['aifstime_utc'] = pd.to_datetime(df.aifstime_utc.map(str), format="%Y%m%d%H%M%S", utc=True)

    df['local_date_time_full'] = pd.to_datetime(df.local_date_time_full.map(str), format="%Y%m%d%H%M%S")

    df = df.set_index('aifstime_utc')
    df = df.drop('history_product',1)
    df = df.drop('name',1)
    df = df.drop('wmo',1)
    df = df.drop('lat',1)
    df = df.drop('lon',1)
    df = df.drop('sort_order',1)
    df = df.sort_index()

    return df, attributes

def read_obs_json(filelike):
    return parse_json(json.load(filelike))
