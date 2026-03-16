import math
import sys
from skyfield.api import load
from skyfield.framelib import ecliptic_frame
from datetime import date, timedelta

eph = load('de422.bsp') 
sun, moon, earth = eph['sun'], eph['moon'], eph['earth']
ts = load.timescale()

def get_moon_illumination(year, month, day, hour=0):
    t = ts.utc(year, month, day, hour)
    e = earth.at(t)
    m = e.observe(moon).apparent()
    return 100.0 * m.fraction_illuminated(sun)

def get_brightest(dt):
    y = dt.year
    m = dt.month
    d = dt.day
    best_illum = get_moon_illumination(y, m, d)
    best_date = dt
    count = 0
    while True:
        dt = dt - timedelta(days=1)
        y = dt.year
        m = dt.month
        d = dt.day
        prev = get_moon_illumination(y, m, d)
        count += 1
        if prev > best_illum: 
            best_illum = prev
            best_date = date(y, m, d)
        if m == 3 and d == 22 or count > 14: return best_date

if __name__ == "__main__":

    brst = get_brightest(date(2026, 4, 12))
    print(brst)