
import os, sys
syspath = os.path.abspath(os.path.join(os.path.dirname(__file__), '.')).replace(os.sep, '/')
if syspath not in sys.path:
    sys.path.append(syspath)

import pandas as pd
from pytz import timezone
from log_utils import WARNING, INFO
from fileio_utils import absolute_path, unix_path

def mask_times(df0: pd.DataFrame, start: str, end: str) -> pd.Series:
    tmp = df0.copy().set_index(pd.DatetimeIndex(df0['Timestamp']), drop=False)\
        .between_time(start,end).reset_index(drop=True)

    if len(tmp) < 2:
        return (df0['Timestamp'] != df0['Timestamp'])

    mask = (df0['Timestamp'] >= min(tmp['Timestamp'])) & \
        (df0['Timestamp'] <= max(tmp['Timestamp']))
    return mask

def between_times(df0:pd.DataFrame, start="00:00:00", end="23:59:59", start_date:str|None=None, end_date:str|None=None):
    mask = df0['Timestamp'].notna()
    tz = min(df0['Timestamp']).tzname()
    #TODO: this is in datset_types. rerun main
    ts_convert = {
        'MDT':'US/Mountain',
        #'MST':'US/Phoenix',
    }
    if tz in ts_convert.keys():
        tz = ts_convert[tz]
    if start_date is not None:
        mask &= (df0['Timestamp'] > pd.to_datetime(start_date).tz_localize(tz))
    if end_date is not None:
        mask &= (df0['Timestamp'] < pd.to_datetime(end_date).tz_localize(tz))

    mask &= mask_times(df0[mask], start=start, end=end)
    return df0[mask]

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
