

import numpy as np
base = 63957
a1 = 90175
r1 = np.power(a1/base, 1/4) - 1
y1 = np.power(1+r1, 12) -1
a2 = 75680
r2 = np.power(a2/base, 1/4) - 1
y2 = np.power(1+r2, 12) -1

print (r1)
print (y1)
print (r2)
print (y2)
print (a1/base)
print (a2/base)