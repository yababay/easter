import juliandate as jd
from dateutil.easter import easter, EASTER_JULIAN, EASTER_ORTHODOX

def get_easter(year, method=EASTER_ORTHODOX):
    return easter(year, method)

def to_gregorian(y, m, d):
    yg, mg, dg, _, _, _, _ = jd.to_gregorian(jd.from_julian(y, m, d, 0, 0, 0, 0))
    return (yg, mg, dg)
