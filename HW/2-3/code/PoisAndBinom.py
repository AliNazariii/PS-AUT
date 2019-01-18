import numpy as np
import matplotlib.pyplot as plt

# s = np.random.poisson(6, 500)
# s = np.random.poisson(6, 5000)
# s = np.random.binomial(500, 6/500, 1000)
s = np.random.binomial(5000, 6/5000, 1000)
count, bins, ignored = plt.hist(s, 30)
plt.show()
