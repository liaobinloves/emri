import numpy as np
from astropy import constants as cons
from astropy import units as u

class t:
    abc = 123
    print(abc)


# t.abc = 7

t1 = t()
t1.abc = 7
t2 = t()
print(t1.abc)