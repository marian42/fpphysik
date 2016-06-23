import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy

dispersionsgebiet = 27*10**(-12)
h_bar = 6.62607 * 10**(-34)
c = 299792458
l = 480 * 10**(-9)
mu_B = 9.274 * 10**(-24)
B = ufloat(1.156, 0.019)

Ds, ds = np.genfromtxt('anormal-pi.txt', delimiter='\t', skip_header=1, skip_footer=0, unpack=True)

dlambda = 0.5 * ds / Ds * dispersionsgebiet

deltaE = h_bar * c / l**2 * dlambda

g_J = deltaE / (mu_B * B)

for i in range(len(Ds)):
	print(
		"%.0f" % (Ds[i]) + " & " +
		"%.0f" % (ds[i]) + " & " +
		"%.2f" % (dlambda[i] * 10**12) + " & " +
		"%.2f" % (g_J[i].nominal_value) + "\\pm" + "%.2f" % (g_J[i].std_dev) + "\\\\"
	)

mittelwert = np.mean(g_J)
print(" ")
print(mittelwert)