x = np.linspace(0, 2*np.pi, 100)
y1 = 3 + np.cos(x)
y2 = 1 + 0.5*np.cos(1+x/0.75)

# Make these lines dashed
plt.plot(x, y1, color='green', linestyle='--', linewidth=1)
plt.plot(x, y2, color='blue', linestyle='--', linewidth=1)

plt.ylim(0,4.5)
# Make the x axis range from 0 to 2pi
plt.xlim(0,2*np.pi)

plt.yticks([0, 1, 2, 3, 4], fontsize=14)
# Make the xticks at (0, pi, 2pi)
plt.xticks([0,np.pi,2*np.pi])

plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)

# Change this title to be "Anatomy of a figure"
plt.title('Anatomy of a figure', fontsize=16)

# Shift the following text to be below the title, make it more descriptive, color it blue 
plt.text(3,4.3,'Title',color='blue')

# Use this annotation command to make another annotation pointing to the green line
plt.annotate('Spine', xy=(6.28, 1.5), xytext=(5.5, 1.0),
            weight='bold', color='blue',
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color='blue'))
plt.annotate('Green line', xy=(0.8, 3.8), xytext=(1.5, 3.4),
            weight='bold', color='blue',
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color='blue'))

plt.show();