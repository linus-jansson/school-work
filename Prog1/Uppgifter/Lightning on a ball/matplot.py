import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# quiver(X, Y, Z, U, V, W, **kwargs)
# X, Y, Z: The x, y and z coordinates of the arrow locations
# U, V, W: The x, y and z components of the arrow vectors
# length: [1.0 | float] The length of each quiver, default to 1.0, the unit is the same with the axes
#draw the arrow
ax.quiver(0, 0, 0, 10, 10, 10, length=1.0)

# draw sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]

print("u")
print(u)

print("v")
print(v)
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="r")

plt.show()