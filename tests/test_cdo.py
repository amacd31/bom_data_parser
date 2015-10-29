import os
import numpy as np
import pandas as pd
import unittest

from bom_data_parser import read_climate_data_online_csv as read_cdo_csv
from bom_data_parser import read_climate_data_online_zip as read_cdo_zip

class CDOTest(unittest.TestCase):
    def setUp(self):
        self.test_cdo_data_file = os.path.join(os.path.dirname(__file__), 'data', 'CDO', 'IDCJAC0011_040004_1800_Data.csv')
        self.test_cdo_zip_file = os.path.join(os.path.dirname(__file__), 'data', 'CDO', 'IDCJAC0011_040004_1800.zip')

    def test_cdo_csv(self):
        data, attributes = read_cdo_csv(self.test_cdo_data_file)

        self.__tst_results(data, attributes)

    def test_cdo_zip(self):
        data, attributes = read_cdo_zip(self.test_cdo_zip_file)

        self.__tst_results(data, attributes)


    def __tst_results(self, data, attributes):

        self.assertTrue('airtemp_min' in data.columns)

        self.assertEqual(data.airtemp_min.iloc[-1], 2.2)
        self.assertEqual(len(data.airtemp_min), 26911)
        self.assertEqual(
            attributes,
            {
                'Product code': 'IDCJAC0011',
                'Bureau of Meteorology station number': 40004
            }
        )

