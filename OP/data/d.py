import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.odr import ODR, Model, Data, RealData
import numpy as np
from pylab import *

freq, UA = np.genfromtxt('d.txt', delimiter='\t', skip_header=1, skip_footer=0, unpack=True)
UA = UA / 2

plt.plot(freq, UA, "bx", label = "Messwerte")

def f(nu, a):
	return a / (2 * np.pi * nu)

fit_freq = freq[:-1]
fit_UA = UA[:-1]

params, covariance = curve_fit(f, fit_freq, fit_UA)
errors = np.sqrt(np.diag(covariance))

fitted = [f(nu, params[0]) for nu in fit_freq]
plt.plot(fit_freq, fitted, "r-", label = "Fit")
print "a", ufloat(params[0], errors[0])

plt.xscale('log')
plt.yscale('log')
plt.xlabel("$\\nu / Hz$")
plt.ylabel("$U_A / V$")
plt.legend(loc='best')
plt.savefig("../protokoll/plot/int.pgf");