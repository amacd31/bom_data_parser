import pandas as pd
try:
    from StringIO import StringIO
except:
    from io import StringIO

from bs4 import BeautifulSoup
from datetime import datetime

def read_soi_html(input_file):
    soup = BeautifulSoup(input_file.read(), "lxml")

    soi_data = pd.read_table(StringIO(soup.pre.text.replace('*', '').strip()), index_col='Year', sep='\s+').unstack()

    soi_data = pd.DataFrame({"soi": soi_data.values}, index=soi_data.index.map(lambda i: datetime.strptime("{0} {1}".format(i[0], i[1]), "%b %Y"))).sort_index().dropna().asfreq('MS')

    return soi_data.soi

