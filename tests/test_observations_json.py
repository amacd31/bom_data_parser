import os
import numpy as np
import pandas as pd
import six
import unittest

from datetime import datetime

from bom_data_parser import read_obs_json

class ObsJSONTest(unittest.TestCase):
    def setUp(self):
        self.test_obs_json_file = os.path.join(os.path.dirname(__file__), 'data', 'IDN60901.94767.json')

    def test_obs_json(self):
        data, attributes = read_obs_json(file(self.test_obs_json_file))

        six.assertCountEqual(
            self,
            attributes.keys(),
            [
                'station_id',
                'name',
                'history_product',
                'wmo',
                'lat',
                'lon',
                'header',
                'notice'
            ]
        )

        self.assertEqual(data.index[0], datetime(2014,9,6,11,0,0))
        self.assertEqual(data['air_temp'].iloc[0], 15.1)
        self.assertEqual(data['press'].iloc[0], 1030.6)
        self.assertEqual(data['press_msl'].iloc[0], 1030.6)
        self.assertEqual(data['press_qnh'].iloc[0], 1030.6)
        self.assertEqual(data['press_tend'].iloc[0], 'F')
        self.assertEqual(data['rain_trace'].iloc[0], 3.4)
        self.assertEqual(data['rel_hum'].iloc[0], 69)

        self.assertEqual(data.index[-1], datetime(2014,9,9,10,30,0))
        self.assertEqual(data['air_temp'].iloc[-1], 20.6)
        self.assertEqual(data['dewpt'].iloc[-1], 12.0)
        self.assertEqual(data['delta_t'].iloc[-1], 4.8)
