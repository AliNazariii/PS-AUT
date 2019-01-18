import numpy as np
import matplotlib.pyplot as plt

s1 = np.random.binomial(100, 0.3, 1000)
s2 = np.random.binomial(100, 0.5, 1000)
s3 = np.random.binomial(200, 0.5, 1000)
s4 = s1 + s2
s5 = s2 + s3
count, bins, ignored = plt.hist(s5, 30)
plt.show()
