import datetime
import numpy as np
import pandas as pd

def show_timedelta(time_initial:str, time_final:str) -> float:
    t0 = pd.to_datetime(time_initial)
    tf = pd.to_datetime(time_final)

    total_seconds = (tf-t0).total_seconds()
    total_minutes = total_seconds / 60
    total_hours   = total_seconds / 3600

    hours   = np.floor(total_minutes / 60)
    minutes = np.floor(total_minutes % 60)
    seconds = total_seconds % 60

    check = hours * 3600 + minutes * 60 + seconds

    print(f" t0 = {t0}")
    print(f" tf = {tf}")
    print(f"\n dt = {total_hours:f} hrs\n dt = {total_minutes:f} min\n dt = {total_seconds:f} sec\n(dt = {check:f} sec)\n")
    print(f" timedelta(hours={hours:f}, minutes={minutes:f}, seconds={seconds:f})\n")

    return seconds

def current_timestamp_str() -> str:
    return str(datetime.datetime.now())

def shift_timestamp_forward(df0:pd.DataFrame, seconds:float=0, minutes:float=0, hours:float=0, days:float=0, timestamp_col:str='Timestamp') -> pd.DataFrame:
    df = df0.copy()
    df[timestamp_col] = df[timestamp_col] + \
                        pd.to_timedelta(seconds, unit='sec') + \
                        pd.to_timedelta(minutes, unit='min') + \
                        pd.to_timedelta(minutes, unit='hour') + \
                        pd.to_timedelta(days, unit='days')
    return df

def localize_df(df0: pd.DataFrame, timezone_str: str) -> pd.DataFrame:
    try:
        df0['Timestamp'] = pd.DatetimeIndex(df0['Timestamp']).tz_localize(timezone_str)
    except TypeError:
        df0['Timestamp'] = pd.DatetimeIndex(df0['Timestamp']).tz_convert(timezone_str)

    # todo: i hate this
    try:
        df0['Timestamp_UTC'] = pd.DatetimeIndex(df0['Timestamp']).tz_localize('UTC')
    except TypeError:
        df0['Timestamp_UTC'] = pd.DatetimeIndex(df0['Timestamp']).tz_convert('UTC')

    return df0

if __name__ == "__main__":
    from datetime import datetime

    t0 = "2024-03-13 07:01:03.063"
    tf = "2024-03-13 13:01:37.790"

    show_timedelta(t0, tf)
