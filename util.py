import juliandate as jd
from dateutil.easter import easter, EASTER_JULIAN, EASTER_ORTHODOX
import datetime

def get_easter(year):
    return (
        easter(year, method=EASTER_JULIAN),
        easter(year, method=EASTER_ORTHODOX),
    )

def to_gregorian(y, m, d):
    return jd.to_gregorian(jd.from_julian(y, m, d, 0, 0, 0, 0))
