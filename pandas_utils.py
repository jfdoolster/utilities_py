
import os, sys
syspath = os.path.abspath(os.path.join(os.path.dirname(__file__), '.')).replace(os.sep, '/')
if syspath not in sys.path:
    sys.path.append(syspath)

import pandas as pd
from log_utils import WARNING, INFO
from fileio_utils import absolute_path, unix_path

def df2csv(df0: pd.DataFrame, csv_path: str, display=True, float_format=None) -> str:
    _path = absolute_path(csv_path)
    _path = f"{os.path.splitext(_path)[0]}.csv"
    if not os.path.isdir(os.path.dirname(_path)):
        WARNING(f"{os.path.dirname(_path):s} does not exist. CSV was not saved.")
        return _path
    df0.to_csv(_path, index=False, float_format=float_format)
    if display:
        INFO(f"{unix_path(_path):s}", hdr='CSV', show_func=False)
    return _path

def df2print(df0:pd.DataFrame, precision=2, latex:bool=False) -> None:
    og = pd.get_option('display.precision')
    pd.set_option('display.precision', precision)
    df = df0.copy()
    if latex:
        fmt = "{: ."+f"{precision:02d}"+"f}"
        df = df.to_latex(index=False, float_format=fmt.format)
    print(); print(df); print()
    pd.set_option('display.precision', og)
