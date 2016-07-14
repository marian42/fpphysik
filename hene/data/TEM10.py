import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit

d2, I4 = np.genfromtxt("TEM10.txt", unpack=True)

def graph(figure, x, y, title, xlabel, ylabel, savefig):
    plt.figure(figure)
    plt.plot(x, y, "b.", label="Messwerte")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc="best")
    plt.grid()
    plt.savefig(savefig + ".png")

def TEM10(x, a, b, c, d):
    return a*((x-c)**2)*math.e**(-2*(x-d)**2/b**2)

params2, covariance2 = curve_fit(TEM10, d2, I4)
errors2 = np.sqrt(np.diag(covariance2))
x_plot2 = np.linspace(np.min(d2), np.max(d2), 1e3)
print("TEM10:")
print("a = ", params2[0], "+/-", errors2[0])
print("b = ", params2[1], "+/-", errors2[1])
print("c = ", params2[2], "+/-", errors2[2])
print("d = ", params2[3], "+/-", errors2[3])
plt.figure(4)
plt.plot(x_plot2, TEM10(x_plot2, *params2), "r-", label="Fit")
graph(4, d2, I4, "$\\mathrm{TEM}_{10}$", "$d/\\mathrm{mm}$", "$I/\mu\\mathrm{A}$", "../protokoll/plots/TEM10")
