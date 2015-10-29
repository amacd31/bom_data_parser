from bom_data_parser.acorn_sat import read_acorn_sat_csv
from bom_data_parser.climate_data_online import read_climate_data_online_csv
from bom_data_parser.climate_data_online import read_climate_data_online_zip
from bom_data_parser.hrs import read_hrs_csv
from bom_data_parser.observations_json import read_obs_json
from bom_data_parser.soi import read_soi_html
from bom_data_parser.water_storages import read_water_storage_series

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
