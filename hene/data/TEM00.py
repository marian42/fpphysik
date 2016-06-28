import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit

d1, I3 = np.genfromtxt("TEM00.txt", unpack=True)

def graph(figure, x, y, title, xlabel, ylabel, savefig):
    plt.figure(figure)
    plt.plot(x, y, "b.", label="Messwerte")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc="best")
    plt.grid()
    plt.savefig(savefig + ".png")

def TEM00(x, a, b, c):
    return a*math.e**(-2*(x-c)**2/b**2)

params1, covariance1 = curve_fit(TEM00, d1, I3)
x_plot = np.linspace(np.min(d1), np.max(d1), 1e3)
errors1 = np.sqrt(np.diag(covariance1))
print("TEM00:")
print("a = ", params1[0], "+/-", errors1[0])
print("b = ", params1[1], "+/-", errors1[1])
print("c = ", params1[2], "+/-", errors1[2])
plt.figure(3)
plt.plot(x_plot, TEM00(x_plot, *params1), "r-", label="Fit")
graph(3, d1, I3, "$\\mathrm{TEM}_{00}$", "$d/\\mathrm{mm}$", "$I/\mu\\mathrm{A}$", "../protokoll/plots/TEM00")
