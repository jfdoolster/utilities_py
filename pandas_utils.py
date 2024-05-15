import os, sys
parent = os.path.abspath(os.path.join(os.path.dirname(__file__), '.')).replace(os.sep, '/')
if parent not in sys.path:
    sys.path.append(parent)

import pandas as pd
from log_utils import WARNING, INFO

def df2csv(df0: pd.DataFrame, csv_path: str, display=True, float_format=None) -> str:
    _path = os.path.abspath(csv_path).replace(os.sep, '/')
    _path = f"{os.path.splitext(_path)[0]}.csv"
    if not os.path.isdir(os.path.dirname(_path)):
        WARNING(f"{os.path.dirname(_path):s} does not exist. CSV was not saved.")
        return _path
    df0.to_csv(_path, index=False, float_format=float_format)
    if display:
        INFO(f"{_path:s}", TYPE='CSV', show_func=False)
    return _path

def df2print(df0:pd.DataFrame, precision=2):
    og = pd.get_option('display.precision')
    pd.set_option('display.precision', precision)
    print(df0)
    pd.set_option('display.precision', og)
