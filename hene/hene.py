from scipy.stats import sem
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit

L1, I1 = np.genfromtxt("stabil1.txt", unpack=True)
L2, I2 = np.genfromtxt("stabil2.txt", unpack=True)
d1, I3 = np.genfromtxt("TEM00.txt", unpack=True)
d2, I4 = np.genfromtxt("TEM10.txt", unpack=True)
phi, I5 = np.genfromtxt("polfilter.txt", unpack=True)

def graph(figure, x, y, title, xlabel, ylabel, savefig):
    plt.figure(figure)
    plt.plot(x, y, "b.")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.savefig(savefig + ".png")

############################
### Stabilitätsparameter ###
############################
"""
graph(1, L1 - 8.6, I1, "Resonatorabstand für $r_1=r_2=140\\mathrm{cm}$", '$L/\\mathrm{cm}$', "$I/\mu\\mathrm{A}$", "stabil1")
graph(2, L2 - 8.6, I2, "Resonatorabstand für $r_1=\infty,r_2=140\\mathrm{cm}$", '$L/\\mathrm{cm}$', "$I/\mu\\mathrm{A}$", "stabil2")
"""
#################
### TEM-Moden ###
#################
"""
def TEM00(x, a, b):
    return a*math.e**(-2*(x-15)**2/b**2)

params = curve_fit(TEM00, d1, I3)
x_plot = np.linspace(np.min(d1), np.max(d1))
plt.figure(3)
plt.plot(x_plot, TEM00(x_plot, params[0][0], params[1][1][1]), "r-", label="Fit")
plt.legend(loc="best")
graph(3, d1, I3, "$\\mathrm{TEM}_{00}$", "$d/\\mathrm{mm}$", "$I/\mu\\mathrm{A}$", "TEM00")

def TEM10(x, a, b):
    return a*((8*x**2)/(b**2))*math.e**(-2*x**2/b**2)

params = curve_fit(TEM10, d2, I4)
x_plot2 = np.linspace(np.min(d2), np.max(d2))
plt.figure(4)
plt.plot(x_plot2, TEM10(x_plot2, *params), "r-", label="Fit")
plt.legend(loc="best")
graph(4, d2, I4, "$\\mathrm{TEM}_{10}$", "$d/\\mathrm{mm}$", "$I/\mu\\mathrm{A}$", "TEM10")
"""
####################
### Polarisation ###
####################

def pol(x, a, b):
    return a*(np.sin(x / 360 * 3.14159 * 2 - b))**2

params, covariance = curve_fit(pol, phi, I5)
print(params[0])
x_plot3 = np.linspace(0, 360, 1e3)
plt.figure(5)
plt.plot(x_plot3, pol(x_plot3, params[0], params[1]), "r-", label="Fit")
plt.plot(phi, I5, "bx", label="Daten")
plt.legend(loc="best")
print(params)
print(covariance)
plt.show()
#graph(5, phi, I5, "Polarisationsmessung", "$\phi/°$", "$I/\mu\\mathrm{A}$", "pol")

###################
### Wellenlänge ###
###################
"""
g = 1/80000 #Gitterkonstante in m
alpha1 = math.atan(0.1/2)
alpha2 = math.atan(0.2/2)
alpha3 = math.atan(0.305/2)
welle1 = g*math.sin(alpha1)
welle2 = g*math.sin(alpha2)/2
welle3 = g*math.sin(alpha3)/3
welle = ([welle1, welle2, welle3])

print(welle1)
print(welle2)
print(welle3)
print(np.mean(welle))
print(sem(welle))
"""
#eof
