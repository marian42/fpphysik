import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data
import numpy as np
import numpy.linalg as la
import scipy.stats

lattice_constants = []
angles = []

def create_image(name, h1, h2, n1, n2):
	im = plt.imread(name + '.png')
	plt.imshow(im, extent=[0, 2, 0, 2])
	
	x1 = [h1[0][0], h1[1][0]]
	y1 = [h1[0][1], h1[1][1]]
	x2 = [h2[0][0], h2[1][0]]
	y2 = [h2[0][1], h2[1][1]]

	plt.plot(x1, y1)
	plt.plot(x2, y2)
	plt.xlim([0, 2])
	
	plt.ylim([0, 2])

	plt.ylabel('$y / \\mathrm{nm}$')
	plt.xlabel('$x / \\mathrm{nm}$')
	
	g1 = [(h1[1][0] - h1[0][0]) / n1, (h1[1][1] - h1[0][1]) / n1]
	g2 = [(h2[1][0] - h2[0][0]) / n2, (h2[1][1] - h2[0][1]) / n2]

	g1_norm = (g1[0]**2 + g1[1]**2)**0.5
	g2_norm = (g2[0]**2 + g2[1]**2)**0.5

	lattice_constants.append(g1_norm)
	lattice_constants.append(g2_norm)

	print name
	print '|g1|:', g1_norm
	print '|g2|:', g2_norm

	g1 = np.array(g1)
	g2 = np.array(g2)
	cosang = np.dot(g1, g2)
	sinang = la.norm(np.cross(g1, g2))
	angle = np.arctan2(sinang, cosang) * 180 / np.pi
	print "angle:", angle
	angles.append(angle)

	plt.savefig(name + '.pgf')
	#plt.show()
	plt.clf()

create_image('down-backward',
	h1 = [[1.91527, 0.414226], [0.17356, 0.07949]], 
	h2 = [[1.91527, 0.414226], [0.65883, 1.50984]],
	n1 = 8,
	n2 = 6)

create_image('down-forward',
	h1 = [[1.77929, 0.382845], [0.246862, 0.116109]], 
	h2 = [[1.77929, 0.382845], [0.330782, 1.63013]],
	n1 = 7,
	n2 = 7)

create_image('up-backward',
	h1 = [[0.356695, 0.142259], [1.91527, 0.403766]], 
	h2 = [[0.356695, 0.142259], [0.166758, 1.33215]],
	n1 = 6,
	n2 = 6)

create_image('up-forward',
	h1 = [[0.325314, 0.15795], [1.84728, 0.403766]], 
	h2 = [[0.325314, 0.15795], [0.164024, 1.14079]],
	n1 = 6,
	n2 = 5)

print ""
print "g:", np.mean(lattice_constants), scipy.stats.sem(lattice_constants) # Literatur 0.246nm
print "alpha:", np.mean(angles), scipy.stats.sem(angles) # Literatur: 60