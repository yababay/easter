import math
import sys
from skyfield.api import load
from skyfield.framelib import ecliptic_frame
from util import get_easter, to_gregorian 
from moon import get_equinox

eph = load('de422.bsp') 
sun, moon, earth = eph['sun'], eph['moon'], eph['earth']
ts = load.timescale()

def get_historical_moon(year, month, day, hour=12):
    t = ts.utc(year, month, day, hour)
    e = earth.at(t)
    m = e.observe(moon).apparent()
    s = e.observe(sun).apparent()
    _, slon, _ = s.frame_latlon(ecliptic_frame)
    _, mlon, _ = m.frame_latlon(ecliptic_frame)
    phase = (mlon.degrees - slon.degrees) % 360.0
    percent_illuminated = 100.0 * m.fraction_illuminated(sun)

    return {
        "date": t.utc_strftime('%Y-%m-%d %H:%M'),
        "illumination": percent_illuminated,
        "phase": phase
    }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Please provide year as argument')
    else: 
        year = int(sys.argv[1])
        y, m, d = get_equinox(year)
        d_equinox = to_gregorian(y, m, d)
        d_easter  = get_easter(year)
        print(f"Дата новолуния: {d_equinox}")
        print(f"Дата Пасхи: {d_easter[1]}")
