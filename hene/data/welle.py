from scipy.stats import sem
import numpy as np
import math

g = 1/80000 #Gitterkonstante in m
alpha1 = math.atan(0.1/2)
alpha2 = math.atan(0.2/2)
alpha3 = math.atan(0.305/2)
welle1 = g*math.sin(alpha1)
welle2 = g*math.sin(alpha2)/2
welle3 = g*math.sin(alpha3)/3
welle = ([welle1, welle2, welle3])

print("Wellenlänge:")
print("l = ", np.mean(welle), "+/-", sem(welle))
