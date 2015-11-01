import os
import numpy as np
import pandas as pd
import unittest
from datetime import datetime

from bom_data_parser import read_ssf_csv

class HRSTest(unittest.TestCase):
    def setUp(self):
        self.test_ssf_file = os.path.join(os.path.dirname(__file__), 'data', 'SSF', '410730_FC_10_2015_10_table.csv')

    def test_ssf(self):
        data = read_ssf_csv(self.test_ssf_file)

        self.assertTrue('Streamflow Forecast (GL)' in data.columns)
        self.assertTrue('Historical Reference (GL)' in data.columns)

        self.assertItemsEqual(data.median().values, [6.3275000000000006,  12.258])
        self.assertItemsEqual(data.mean().values, [7.3686599999999967, 13.665890400000013])
