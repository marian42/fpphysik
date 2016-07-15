import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.odr import ODR, Model, Data, RealData
import numpy as np
from pylab import *

freq, U1_raw, U2_raw, U3_raw, U4_raw = np.genfromtxt('a.txt', delimiter='\t\t', skip_header=2, skip_footer=0, unpack=True)

U_in = 0.1 #100mV
R1 = 100.0

U1 = U1_raw / 2
U2 = U2_raw / 2 / 1000
U3 = U3_raw / 2
U4 = U4_raw / 2 / 1000

def f(nu, m, b):
	return np.exp(-m * np.log(nu)) * np.exp(b)

def drawplot(U, filename, fit_begin, fit_end, RN):
	print(filename)
	plt.clf();
	amplification = U / U_in # V'

	### Plot
	plt.plot(freq, amplification, "bx", label = "Messwerte")

	### Bandbreite-Verstaerkungs-Faktor
	a_g = amplification[0] / 2**0.5
	plt.axhline(a_g, color = "g")
	i = 0
	while (amplification[i + 1] > a_g):
		i+= 1
	progress = (a_g - min(amplification[i], amplification[i+1])) / (amplification[i] - amplification[i+1])
	nu_g = freq[i] * progress + freq[i+1] * (1.0 - progress)
	plt.axvline(nu_g, color = "g")

	plt.yscale('log')
	plt.xscale('log')
	print "V'_DC ", amplification[0]
	print "nu_g", nu_g
	print "nu_g * V'", (nu_g * amplification[0])

	### Fit
	fit_freq = freq[fit_begin : fit_end]
	fit_amplification = amplification[fit_begin : fit_end]
	
	params, covariance = curve_fit(f, fit_freq, fit_amplification)
	errors = np.sqrt(np.diag(covariance))

	fitted = [f(nu, params[0], params[1]) for nu in fit_freq]
	plt.plot(fit_freq, fitted, "r-", label = "Fit")
	print "m", ufloat(params[0], errors[0])

	### Leerlaufverstaerkung
	Videal = RN / R1
	Vleerlauf = 1 / ((1 / amplification[0]) - (1 / Videal))
	print "V_ideal", Videal
	print "V_Leerlauf", Vleerlauf

	### Speichern
	plt.xlabel("$\\nu / Hz$")
	plt.ylabel("$V'$")
	plt.legend(loc='best')
	plt.savefig(filename);
	print("")


drawplot(U1, "../protokoll/plot/lin1.pgf", 14, 18, 1000)
drawplot(U2, "../protokoll/plot/lin2.pgf", 15, 19, 330)
drawplot(U3, "../protokoll/plot/lin3.pgf", 12, 18, 10000)
drawplot(U4, "../protokoll/plot/lin4.pgf", 12, 18, 480)