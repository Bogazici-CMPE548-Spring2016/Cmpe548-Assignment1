import math
import numpy as np
import matplotlib.pyplot as plt


r_inverse_cdf = lambda y: math.sqrt(y)
theta_inverse_cdf = lambda y: 2 * y * math.pi

points = [(r_inverse_cdf(np.random.uniform(0,1,1)[0]), theta_inverse_cdf(np.random.uniform(0,1,1)[0])) for i in range(1000)]
rs = np.array([p[0] for p in points])
thetas = np.array([p[1] for p in points])

ax = plt.subplot(111, projection='polar')
ax.plot(thetas, rs, '.')