import sys
import pandas as pd

from datetime import date
from util import get_easter, to_gregorian 
from equinox import get_equinox
from moon import get_moon_illumination, get_brightest
from util import get_easter

df = pd.DataFrame(columns=['easter', 'ortodox_moon_greg', 'illumination', 'brightest_moon', 'diff_in_days', 'ortodox_moon_jul'])

def get_row(year):
    yj, mj, dj = get_equinox(year)
    yg, mg, dg = to_gregorian(yj, mj, dj)
    illum = get_moon_illumination(yg, mg, dg)
    easter  = get_easter(year)
    brightest = get_brightest(easter)
    diff = (date(yg, mg, dg) - brightest).days
    return {
        'easter': easter,
        'ortodox_moon_greg': date(yg, mg, dg), 
        'ortodox_moon_jul':  date(yj, mj, dj), 
        'brightest_moon':    brightest, 
        'diff_in_days':      diff,
        'illumination':      get_moon_illumination(yg, mg, dg)
    }

if __name__ == "__main__":

    if len(sys.argv) != 2:
        for year in range(325, 2027): #(325, 2027):
            if year % 10: continue
            print(year)
            row = get_row(year)
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        df.to_csv('output.csv', index=False)

    else: 
        year = int(sys.argv[1])
        y, m, d = get_equinox(year)
        yg, mg, dg = to_gregorian(y, m, d)
        illum = get_moon_illumination(yg, mg, dg)
        d_easter  = get_easter(year)
        brightest = get_brightest(d_easter)
        print(f"Дата Пасхи: {d_easter}")
        print(f"Дата полнолуния: {date(yg, mg, dg)}")
        print(f"Дата полнолуния (астр.): {brightest}")
        print(f"Дата полнолуния (юл.): {date(y, m, d)}")
        print(f"Освещенность Луны: {illum:10.2f} %")
