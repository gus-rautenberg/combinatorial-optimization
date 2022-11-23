import numpy
import random
from Individual import Individual
from functions import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def f(x, y):
    return -(x**2 + y**2) + 4
# Surface
# x = numpy.arange(-10, 10, 0.1)
# y = numpy.arange(-10, 10, 0.1)

# X, Y = numpy.meshgrid(x, y)

# Z = f(X, Y)
# fig = plt.figure()

# ax = plt.axes(projection="3d")
# surf = ax.plot_surface(X, Y, Z)

# plt.show()

# Points


x = numpy.arange(-10, 10, 0.1)
y = numpy.arange(-10, 10, 0.1)
z = f(x, y)

ax = plt.axes(projection="3d")
ax.scatter(x, y, z)
plt.show()
