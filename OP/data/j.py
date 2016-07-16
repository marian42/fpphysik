import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.odr import ODR, Model, Data, RealData
import numpy as np
from pylab import *

freq, phi = np.genfromtxt('j.txt', delimiter='\t', skip_header=2, skip_footer=0, unpack=True)

plt.plot(freq, phi, "bx", label = "Messwerte")
plt.xscale('log')
plt.xlabel("$\\nu / Hz$")
plt.ylabel("$\\varphi / \\^{\circ}$")
plt.legend(loc='best')
plt.savefig("../protokoll/plot/phase.pgf");

