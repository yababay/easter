import sys
from util import get_easter, to_gregorian 
from equinox import get_equinox
#from moon import get_moon_illumination
from util import get_easter

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
