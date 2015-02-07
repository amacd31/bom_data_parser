import pandas as pd
import StringIO

from bs4 import BeautifulSoup
from datetime import datetime

def read_soi_html(input_file):
    soup = BeautifulSoup(input_file.read())

    soi_data = pd.read_table(StringIO.StringIO(soup.pre.text.replace('*', '').strip()), index_col='Year').drop('Unnamed: 13', 1).unstack()

    soi_data = pd.DataFrame({"soi": soi_data.values}, index=soi_data.index.map(lambda i: datetime.strptime("{0} {1}".format(i[0], i[1]), "%b %Y"))).sort_index().dropna().asfreq('MS')

    return soi_data

