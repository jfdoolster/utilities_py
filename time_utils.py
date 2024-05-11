import datetime
import numpy as np
import pandas as pd

def show_timedelta(time_initial:str, time_final: str, ret='sec'):
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

def current_timestamp_str():
    return str(datetime.datetime.now())

if __name__ == "__main__":
    from datetime import datetime

    t0 = "2024-03-13 07:01:03.063"
    tf = "2024-03-13 13:01:37.790"

    show_timedelta(t0, tf)
