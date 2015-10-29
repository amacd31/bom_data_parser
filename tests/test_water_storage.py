import os
import pandas as pd
import unittest

from bom_data_parser import read_water_storage_series

class WaterStoragesTest(unittest.TestCase):
    def setUp(self):
        self.test_xml_file = os.path.join(os.path.dirname(__file__), 'data', 'water_storage', 'urn:bom.gov.au:awris:common:codelist:feature:lakenillahcootie')

    def test_read_storage(self):
        with open(self.test_xml_file, 'r') as water_storage_file:
            storage_data = read_water_storage_series(water_storage_file)

        self.assertEqual(storage_data.ix['2015-10-27'], 20929.055)
        self.assertAlmostEqual(storage_data.ix['2013-01-01'], 34895.71)
        self.assertEqual(len(storage_data), 1030)
