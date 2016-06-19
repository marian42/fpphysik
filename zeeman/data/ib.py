import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.odr import ODR, Model, Data, RealData
import numpy as np
from pylab import *


I, B_mT = np.genfromtxt('ib.txt', delimiter='\t', skip_header=1, skip_footer=0, unpack=True)
	
B = B_mT / 1000.0
B_err = [b * 0.005 for b in B]
I_err = 0.2

def f(params, x):
	return params[0]*x

data = RealData(I, B, I_err, B_err)
model = Model(f)

odr = ODR(data, model, [0])
odr.set_job(fit_type=2)
output = odr.run()
output.pprint()

m = ufloat(output.beta[0], output.sd_beta[0])

print(m)
I_plot = np.linspace(0, 18, 100)
plt.plot(I, B, 'bx', label = 'Messwerte')
plt.plot(I_plot, f([output.beta[0]], I_plot), 'r-', label = 'Fit')
plt.errorbar(I, B, fmt='bx', xerr=I_err, yerr=B_err);

plt.xlim(0, 17)
plt.ylabel('$B/\\mathrm{T}$')
plt.xlabel('$I/\\mathrm{A}$')
plt.legend(loc='upper left')
plt.tight_layout()

plt.savefig('../protokoll/plot/ib.pgf')
	
#plt.show()

print()
for i in range(len(B)):
	print(str(I[i]) + " \pm " + str(I_err) + " & " + str(B[i] * 1000) + " \pm " + str(B_err[i] * 1000) + "\\\\")

I_neu = [5, 10, 19]

print()
for i in I_neu:
	print(m * ufloat(i, 0.2))