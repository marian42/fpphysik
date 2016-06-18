import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

I, B_mT = np.genfromtxt('ib.txt', delimiter='\t', skip_header=1, skip_footer=0, unpack=True)
	
B = B_mT / 1000.0

def f(x, m):
	return m*x

popt, pcov = curve_fit(f, I, B)
errors = np.sqrt(np.diag(pcov))

m = ufloat(popt[0], errors[0])

print(m)
I_plot = np.linspace(0, 16, 100)
plt.plot(I, B, 'bx', label = 'Messwerte')
plt.plot(I_plot, f(I_plot, *popt), 'r-', label = 'Fit')

plt.ylabel('$B/\\mathrm{T}$')
plt.xlabel('$I/\\mathrm{A}$')
plt.legend(loc='best')
plt.tight_layout()

plt.savefig('../protokoll/plot/ib.pgf')
	
#plt.show()