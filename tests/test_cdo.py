import os
import numpy as np
import pandas as pd
import unittest

from bom_data_parser import read_climate_data_online_csv as read_cdo

class CDOTest(unittest.TestCase):
    def setUp(self):
        self.test_cdo_file = os.path.join(os.path.dirname(__file__), 'data', 'CDO', 'IDCJAC0011_040004_1800_Data.csv')

    def test_cdo(self):
        data, attributes = read_cdo(self.test_cdo_file)

        self.assertTrue('airtemp_min' in data.columns)
