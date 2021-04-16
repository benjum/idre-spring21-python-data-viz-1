# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm

fig = plt.figure(figsize=(8,8))
ax = fig.gca(projection='3d')

# Make data.

x = np.linspace(0, 4*np.pi, 100)
y = np.linspace(-2, 2, 100)
Xgrid, Ygrid = np.meshgrid(x,y)

f = np.exp(-Ygrid**2) * np.cos(Xgrid)

#X = np.arange(-5, 5, 0.25)
#Y = np.arange(-5, 5, 0.25)
#X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)

# Plot the surface.
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
surf = ax.plot_surface(Xgrid, Ygrid, f, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)

ax.set_xticks([0,2*np.pi,4*np.pi])
ax.set_xticklabels(['0','$2\pi$','$4\pi$'])

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=10)

plt.show()