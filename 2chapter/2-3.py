# https://pysdr.org/content/frequency_domain.html

import numpy as np
t = np.arange(100)
s = np.sin(0.15*2*np.pi*t)
print(s)

sf = np.fft.fft(s)
print(sf)

import matplotlib.pyplot as plt
S_mag = np.abs(sf)
S_phase = np.angle(sf)
plt.plot(t,S_mag,'.-')
plt.show()
plt.plot(t,S_phase,'.-')
