import math
import pandas as pd

from datetime import datetime, timedelta, date
from skyfield.api import load, Star, wgs84
from skyfield.data import hipparcos
from zoneinfo import ZoneInfo

tz = ZoneInfo('Europe/Moscow')

# Load Hipparcos catalog and find Sirius
with load.open(hipparcos.URL) as f:
    df = hipparcos.load_dataframe(f)

sirius = Star.from_dataframe(df.loc[32349])

earth = load('de421.bsp')['earth']
sun = load('de421.bsp')['sun']
moscow = earth + wgs84.latlon(55.7558, 37.6173, elevation_m=150)
ts = load.timescale()

def delta_in_minutes(dt):
    mins = dt.minute
    hours = dt.hour
    return mins - 60 if hours == 23 else mins

def get_max_alt(dt):
    t = ts.from_datetime(dt)
    max_alt, _, _ = moscow.at(t).observe(sirius).apparent().altaz()
    max_dt = dt

    for m in range(10, 8 * 6):
        dt = dt + timedelta(minutes=m)
        t = ts.from_datetime(dt)
        alt, _, _ = moscow.at(t).observe(sirius).apparent().altaz()
        if alt.radians > max_alt.radians:
            max_alt = alt
            max_dt = dt
    return max_dt

def sun_sirius_delta(dt):    
    t = ts.from_datetime(dt)
    _, sir_az, _ = moscow.at(t).observe(sirius).apparent().altaz()
    _, sun_az, _ = moscow.at(t).observe(sun).apparent().altaz()
    return sir_az, sun_az 

def get_min_az_delta(dt):
    t = ts.from_datetime(dt)
    _, sir_az, _ = moscow.at(t).observe(sirius).apparent().altaz()
    _, sun_az, _ = moscow.at(t).observe(sun).apparent().altaz()
    min_az_delta = sir_az.radians - 3.1415 + sun_az.radians

    for m in range(10, 8 * 6):
        dt = dt + timedelta(minutes=m)
        t = ts.from_datetime(dt)
        _, sir_az, _ = moscow.at(t).observe(sirius).apparent().altaz()
        _, sun_az, _ = moscow.at(t).observe(sun).apparent().altaz()
        az_delta = sir_az.radians - 3.1415 + sun_az.radians
        if az_delta < min_az_delta:
            min_az_delta = az_delta
    return min_az_delta

def sun_sirius_delta(dt):    
    t = ts.from_datetime(dt)
    _, sir_az, _ = moscow.at(t).observe(sirius).apparent().altaz()
    _, sun_az, _ = moscow.at(t).observe(sun).apparent().altaz()
    return sir_az.radians, sun_az.radians - 2 * math.pi 

if __name__ == "__main__":
    dec_1 = datetime(2025, 12, 15, 23, 59, 59, tzinfo=tz)
    out_df = pd.DataFrame(columns=['date', 'sirius', 'sun'])
    for d in range(0, 30):
        dt = dec_1 + timedelta(days=d)
        sir_az, sun_az = sun_sirius_delta(dt)
        row = {
            'date':  str(dt)[0:10],
            'sirius': sir_az,
            'sun': sun_az
        }
        out_df = pd.concat([out_df, pd.DataFrame([row])], ignore_index=True)
    out_df.to_csv('sirius-sun.csv', index=False)
