import scipy.stats as ss
import numpy as np
from matplotlib import pyplot as plt

b = ss.distributions.binom

for flips in [5,10,20,40,80]:
    success = np.arange(flips) # a-range not arrange
    our_distribution = b.pmf(success, flips, .5)
    plt.hist(success, flips, weights = our_distribution)
    
plt.xlim(0, 55);
plt.show()
