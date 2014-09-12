import os
import numpy as np
import pandas as pd
import unittest
from datetime import datetime

from bom_data_parser import read_hrs_csv

class HRSTest(unittest.TestCase):
    def setUp(self):
        self.test_cdo_file = os.path.join(os.path.dirname(__file__), 'data', 'HRS', '410730_daily_ts.csv')

    def test_hrs(self):
        data, attributes = read_hrs_csv(self.test_cdo_file)

        self.assertTrue('Q' in data.columns)
        self.assertTrue('QCode' in data.columns)

        self.assertEqual(attributes['station_name'], 'Cotter River at Gingera (410730)')
        self.assertEqual(attributes['catchment_area'], 130.0)
        self.assertEqual(attributes['latitude'], 148.8212)
        self.assertEqual(attributes['longitude'], -35.5917)

        self.assertEqual(data.index[0], datetime(1963,07,05))
        self.assertEqual(data.index[-1], datetime(2012,10,04))
        self.assertAlmostEqual(data.Q.values[0], 127.312,3)
        self.assertAlmostEqual(data.Q.values[-1], 186.238,3)
        self.assertEqual(data.QCode.values[0], 10)
        self.assertEqual(data.QCode.values[-1], 10)
