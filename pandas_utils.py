
import os
import pandas as pd

def df2csv(df0: pd.DataFrame, csv_path: str, display=True, float_format=None) -> str:
    _path = os.path.abspath(csv_path).replace(os.sep, '/')
    _path = f"{os.path.splitext(_path)[0]}.csv"
    if not os.path.isdir(os.path.dirname(_path)):
        print(f"{'WARN':5s} : [df2csv()] {os.path.dirname(_path):s} does not exist. CSV was not saved.")
        return _path
    df0.to_csv(_path, index=False, float_format=float_format)
    if display:
        print(f"{'CSV':5s} : {_path}")
    return _path

def df2print(df0:pd.DataFrame, precision=2):
    og = pd.get_option('display.precision')
    pd.set_option('display.precision', precision)
    print(df0)
    pd.set_option('display.precision', og)
