vang_top_5.plot.barh(x='Company',
                     figsize=(10,7),
                     cmap='gist_rainbow');

# You can use plt.gca to get the current axes object from pandas plots too
# and then use regular matplotlib methods to alter the plots
# Try doing that here to change limits on the horizontal axis to (0,15)
# and then make xticks of (0,5,10,15)
ax = plt.gca()
ax.set_xlim([0,15])
ax.set_xticks([0,5,10,15]);