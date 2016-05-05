import numpy as np
import math
import sympy
import uncertainties
import matplotlib.pyplot as plt
import scipy.constants as const
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem

########################################################

def molIsochor(cp, temp, alpha):
    return  cp - (9 * (alpha**2) * kappa * v0 * temp)

def temperatur(r):
    return 0.00134 * (r**2) + 2.296 * r - 243.02

def poly(x, a, b, c, d, e, f, g):
    return a * x**6 + b * x**5 + c * x**4 + d * x**3 + e * x**2 + f * x + g

############
### 5 a) ###
############

zeitMess, widMess1, stromMess1, spannMess1 = np.genfromtxt('messdaten.txt', unpack=True)

stromMess2 = stromMess1[0:25]
spannMess2 = spannMess1[0:25]

#Messunsicherheiten
zeit = [ufloat(x, 1) for x in zeitMess]
wid = [ufloat(x, 0.1) for x in widMess1]
strom = [ufloat(x, 0.01) for x in stromMess2]
spann = [ufloat(x, 0.001) for x in spannMess2]

#Zeitdifferenzen
deltaZeit = []
for i in range(0, 25):
    deltaZeit.append(zeit[i+1] - zeit[i])

#Temperaturdifferenzen
temp = const.C2K(temperatur(np.array(wid)))
deltaTemp = []
for i in range(0, 25):
    deltaTemp.append(temp[i+1] - temp[i])

temp2 = temp[0:len(temp) - 1]

energie = np.array(spann) * np.array(strom) * np.array(deltaZeit) * 1e-3

#Isobare Molwärme
cp = 63.55/342 * np.array(energie) / np.array(deltaTemp) #Molekulargewicht durch Gesamtmasse

'''
np.savetxt('5aEnergie.txt', energie)
np.savetxt('5aZeitDiff.txt', deltaZeit)
np.savetxt('5aTemp.txt', temp2)
np.savetxt('5aTempDiff.txt', deltaTemp)
'''
############
### 5 b) ###
############

alpha, temptab = np.genfromtxt('ausdehnungskoeff.txt', unpack=True)

kappa = 1.378e11   #in N/m² Kompressionsmodul (goodfellow.com) für Polykristallin
v0 = 7.11e-6    #m³/mol Molvolumen

params, covariance = curve_fit(poly, temptab, alpha * 1e-6) #1e-6 wegen Tabellenangabe

errors = np.sqrt(np.diag(covariance))

alphaFit = poly(np.array(temp), 
    ufloat(params[0], errors[0]),
    ufloat(params[1], errors[1]),   
    ufloat(params[2], errors[2]),   
    ufloat(params[3], errors[3]),   
    ufloat(params[4], errors[4]),   
    ufloat(params[5], errors[5]),
    ufloat(params[6], errors[6])
    )

alphaFit2 = alphaFit[0:len(alphaFit) - 1]

alphaNominal = np.zeros(25)
for i in range(0, len(alphaFit2)):
    alphaNominal[i] = alphaFit2[i].n

tempNominal = np.zeros(25)
for i in range(0, len(temp2)):
    tempNominal[i] = temp2[i].n

cpNominal = np.zeros(25)
for i in range(0, len(cp)):
    cpNominal[i] = cp[i].n

#Isochore Molwärme
cvErr = molIsochor(cp, temp2, alphaFit2)
cv = molIsochor(cpNominal, tempNominal, alphaNominal)

plt.plot(tempNominal, cv, 'r.', label='Isochore Molwärme')
plt.xlabel('$T/K$')
plt.ylabel('$C_V/\\frac{Jmol}{K}$')
plt.legend(loc='best')
plt.grid()

'''
np.savetxt('5bCV.txt', cvErr)
np.savetxt('5bAlpha.txt', alphaFit2)
'''

############
### 5 c) ###
############

tempTheta, thetaT = np.genfromtxt('debyeDaten.txt', unpack=True)

debye = tempTheta * thetaT

############
### 5 d) ###
############

vlong = 4.7e3
vtrans = 2.26e3
masse = 0.342
mAtom = 63.55 * 1.66e-27
dichte = 8.92e3
teilchenzahl = masse / mAtom
volumen = masse / dichte
omegaD = ( ((18 * (np.pi**2) * teilchenzahl) / volumen) * (1 / ((1/(vlong**3)) + (1/(vtrans**3)))) )**(1/3)
thetaD = (const.hbar * omegaD) / const.k
