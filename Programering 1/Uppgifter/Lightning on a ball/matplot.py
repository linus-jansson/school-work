from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# quiver(X, Y, Z, U, V, W, **kwargs)
# X, Y, Z: The x, y and z coordinates of the arrow locations
# U, V, W: The x, y and z components of the arrow vectors
# length: [1.0 | float] The length of each quiver, default to 1.0, the unit is the same with the axes
#draw the arrow
ax.quiver(0, 0, 0, 1, 1, 1, length=1.0)

plt.show()