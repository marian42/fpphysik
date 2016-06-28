import numpy as np
import matplotlib.pyplot as plt

L1, I1 = np.genfromtxt("stabil1.txt", unpack=True)
L2, I2 = np.genfromtxt("stabil2.txt", unpack=True)

def graph(figure, x, y, title, xlabel, ylabel, savefig):
    plt.figure(figure)
    plt.plot(x, y, "b.", label="Messwerte")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc="best")
    plt.grid()
    plt.savefig(savefig + ".png")

graph(1, L1 - 8.6, I1, "Resonatorabstand für $r_1=r_2=140\\mathrm{cm}$", '$L/\\mathrm{cm}$', "$I/\mu\\mathrm{A}$", "../protokoll/plots/stabil1")
graph(2, L2 - 8.6, I2, "Resonatorabstand für $r_1=\infty,r_2=140\\mathrm{cm}$", '$L/\\mathrm{cm}$', "$I/\mu\\mathrm{A}$", "../protokoll/plots/stabil2")
