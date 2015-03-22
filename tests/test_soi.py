import os
import numpy as np
import pandas as pd
import unittest

from bom_data_parser import read_soi_html

class SOITest(unittest.TestCase):
    def setUp(self):
        self.test_soi_file = os.path.join(os.path.dirname(__file__), 'data', 'SOI', 'soiplaintext.html')

    def test_soi(self):
        with open(self.test_soi_file, 'r') as soi_file:
            soi_data = read_soi_html(soi_file)

        self.assertEqual(soi_data.ix['1876-01'].values.item(), 11.3)
        self.assertEqual(soi_data.ix['1984-12'].values.item(), -1.4)
        self.assertEqual(soi_data.ix['2015-01'].values.item(), -7.8)
