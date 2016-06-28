import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit

phi, I5 = np.genfromtxt("polfilter.txt", unpack=True)

def graph(figure, x, y, title, xlabel, ylabel, savefig):
    plt.figure(figure)
    plt.plot(x, y, "b.", label="Messwerte")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc="best")
    plt.grid()
    plt.savefig(savefig + ".png")

def pol(x, a, b):
    return a*(np.sin(x / 360 * 3.14159 * 2 - b))**2

params3, covariance3 = curve_fit(pol, phi, I5)
x_plot3 = np.linspace(0, 360, 1e3)
errors3 = np.sqrt(np.diag(covariance3))
print("Polarisation:")
print("a = ", params3[0], "+/-", errors3[0])
print("b = ", params3[1], "+/-", errors3[1])
plt.figure(5)
plt.plot(x_plot3, pol(x_plot3, *params3), "r-", label="Fit")
graph(5, phi, I5, "Polarisationsmessung", "$\phi/°$", "$I/\mu\\mathrm{A}$", "../protokoll/plots/pol")
