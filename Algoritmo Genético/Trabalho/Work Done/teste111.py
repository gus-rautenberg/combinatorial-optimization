import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 101)
y = np.linspace(-5, 5, 101)
# full coordinate arrays
xx, yy = np.meshgrid(x, y)
zz = np.sqrt(xx**2 + yy**2)
# sparse coordinate arrays
xs, ys = np.meshgrid(x, y, sparse=True)
zs = np.sqrt(xs**2 + ys**2)
np.array_equal(zz, zs)

print(x.shape)
print(y.shape)
print(zs.shape)

h = plt.contourf(x, y, zs)
plt.axis('scaled')
plt.colorbar()
plt.show()
