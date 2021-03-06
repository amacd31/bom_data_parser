import os
import pandas as pd
import unittest

from bom_data_parser import read_water_storage_series, read_water_storage_states, read_water_storage_urns

class WaterStoragesTest(unittest.TestCase):
    def setUp(self):
        self.test_xml_file = os.path.join(os.path.dirname(__file__), 'data', 'water_storage', 'urn:bom.gov.au:awris:common:codelist:feature:lakenillahcootie')
        self.test_datasetless_xml_file = os.path.join(os.path.dirname(__file__), 'data', 'water_storage', 'urn:bom.gov.au:awris:common:codelist:feature:brewster')

        self.test_australia_xml_file = os.path.join(os.path.dirname(__file__), 'data', 'water_storage', 'urn:bom.gov.au:awris:common:codelist:region.country:australia')

        self.test_state_xml_file = os.path.join(os.path.dirname(__file__), 'data', 'water_storage', 'urn:bom.gov.au:awris:common:codelist:region.state:victoria')

    def test_read_storage(self):
        with open(self.test_xml_file, 'r') as water_storage_file:
            storage_data = read_water_storage_series(water_storage_file)

        self.assertEqual(storage_data.ix['2015-10-27'], 20929.055)
        self.assertAlmostEqual(storage_data.ix['2013-01-01'], 34895.71)
        self.assertEqual(len(storage_data), 1030)

    def test_list_states(self):
        with open(self.test_australia_xml_file, 'r') as water_storage_file:
            states = read_water_storage_states(water_storage_file)

        self.assertEqual(len(states), 8)

    def test_list_storages(self):
        with open(self.test_state_xml_file, 'r') as water_storage_file:
            storages = read_water_storage_urns(water_storage_file)

        self.assertEqual(len(storages), 71)

    def test_read_storage_without_dataset_attr(self):
        with open(self.test_datasetless_xml_file, 'r') as water_storage_file:
            storage_data = read_water_storage_series(water_storage_file)

        self.assertEqual(storage_data.ix['2014-04-04'], 0.0)
        self.assertEqual(len(storage_data), 459)
