
import os
import pandas as pd


def df2csv(df0: pd.DataFrame, csv_path: str, shorten=True, display=True, float_format=None) -> str:
    csv_path = os.path.abspath(csv_path)
    if float_format is not None:
        df0.to_csv(csv_path, index=False, float_format=float_format)
    else:
        df0.to_csv(csv_path, index=False)
    if display:
        print(f"dataframe: {csv_path}")
    return csv_path