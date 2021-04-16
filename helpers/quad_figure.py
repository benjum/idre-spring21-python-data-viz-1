np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(6, 6))

# for hist, use the parameters "width" and "bins" to experiment with different hist plots
axs[0, 0].hist(data[0], width=0.4, bins=6)

# give this scatter plot y range of (-3.5,3.5), x range of (-4,4), and make the points green
axs[1, 0].scatter(data[0], data[1], color='green')
axs[1, 0].set_ylim([-3.5,3.5])
axs[1, 0].set_xlim([-4,4])

# make the lines dotted (the relevant linestyle is ":")
axs[0, 1].plot(data[0], data[1], linestyle=':')

axs[1, 1].hist2d(data[0], data[1])

plt.show()