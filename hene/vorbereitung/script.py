import matplotlib.pyplot as plt

STEPS = 200

def createPlot(r1, r2):
	maxL = r1 + r2
	if maxL > 100000:
		maxL = 2
	L = [float(maxL) * i / STEPS for i in range(STEPS)]
	s = [1 - L_i / r2 - L_i / r1 + L_i**2 / (r1 * r2) for L_i in L]
	plt.plot(L, s, 'r-')
	plt.axhline(0)
	plt.axhline(1)
	#plt.xlim([0, maxL])
	plt.xlabel('$L / \\mathrm{m}$')
	plt.ylabel('$g_1 \\cdot g_2$')
	plt.title('Stabilitaetsparameter fuer $r_1 = ' + str(r1) + '$, $r_2 = ' + str(r2) + '$')
	#plt.show()
	plt.savefig(str(r1) + "-" + str(r2) + ".png")

createPlot(1, 1.4)