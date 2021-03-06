BoM data parser
===============

Basic library for parsing data formats supplied by the Australian Bureau of Meteorology.

For the most part this library provides a wrapper around Pandas read methods. This saves effort when trying to get the arguments right when accessing some semi-standard formats available from the Bureau of Meteorology.

Dependencies
------------

Requires Python 2.7, 3.4 or greater (mostly tested with Python 2.7 on Linux),
numpy, pandas, beautifulsoup4, and lxml.

Test suite status when run with Python 2.7, 3.4 and 3.5 using travis-ci:

.. image:: https://secure.travis-ci.org/amacd31/bom_data_parser.png?branch=master
    :target: https://travis-ci.org/amacd31/bom_data_parser

Usage
-----

After importing bom_data_parser the read methods can be called passing in a filename. The read methods return a tuple where the first element is a pandas.DataFrame containing the data and the second element is a dictionary of additional meta-data read from the file. The second element may be None where no additional meta-data exists.

::

 import bom_data_parser as bdp
 dataframe, attributes = bdp.read_hrs_csv('410730_daily_ts.csv')

Supported formats
-----------------

* ACORN-SAT (read_acorn_sat_csv) - http://www.bom.gov.au/climate/change/acorn-sat/
* Climate Data Online (read_climate_data_online_csv) - http://www.bom.gov.au/climate/data/
* Hydrologic Reference Stations (read_hrs_csv) - http://www.bom.gov.au/water/hrs/
* Latest 72 hour observations (read_obs_json) - e.g. http://www.bom.gov.au/products/IDN60901/IDN60901.94767.shtml#other_formats
* SOI data (read_soi_html) - e.g. ftp://ftp.bom.gov.au/anon/home/ncc/www/sco/soi/soiplaintext.html

Notes
-----

The API is still under development so method names will probably change in the future.
