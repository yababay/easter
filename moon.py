import math
import sys
from skyfield.api import load
from skyfield.framelib import ecliptic_frame
from util import get_easter, to_gregorian 
from moon import get_equinox

eph = load('de422.bsp') 
sun, moon, earth = eph['sun'], eph['moon'], eph['earth']
ts = load.timescale()

def get_moon_illumination(year, month, day, hour=12):
    t = ts.utc(year, month, day, hour)
    e = earth.at(t)
    m = e.observe(moon).apparent()
    #s = e.observe(sun).apparent()
    #_, slon, _ = s.frame_latlon(ecliptic_frame)
    #_, mlon, _ = m.frame_latlon(ecliptic_frame)
    # phase = (mlon.degrees - slon.degrees) % 360.0
    return 100.0 * m.fraction_illuminated(sun)
#
#    return {
#        "date": t.utc_strftime('%Y-%m-%d %H:%M'),
#        "illumination": percent_illuminated,
#        "phase": phase
#    }
