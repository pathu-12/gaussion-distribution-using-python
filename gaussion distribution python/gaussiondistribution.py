#This program plot and fit the gaussian distribution

import matplotlib
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(450386798)

#mean distribution
mu = 0

#standard deviation of the distribution
sigma = 25

x = mu + (sigma*np.random.randn(673))

nbins = 25

fig, gauss = plt.subplots()

#histogram definition
n, bins, patches = gauss.hist(x, nbins, density=1, facecolor='g')

# fit the plot
y = ((1 /(np.sqrt(2 * np.pi ) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
gauss.plot(bins, y, '-')
gauss.set_xlabel("Random Numbers")
gauss.set_ylabel("Probability density")
gauss.set_title("Normalized Gaussian Distribution")
plt.savefig("gaussian_dist.png")
plt.show()