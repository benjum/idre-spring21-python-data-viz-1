x = np.linspace(0, 2*np.pi, 100)
y1 = 3 + np.cos(x)
y2 = 1 + 0.5*np.cos(1+x/0.75)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1,aspect=1)

# Make these lines dashed
ax.plot(x, y1, color='green', linestyle='--', linewidth=1)
ax.plot(x, y2, color='blue', linestyle='--', linewidth=1)

ax.set_ylim(0,4.5)
# Make the x axis range from 0 to 2pi
ax.set_xlim(0,2*np.pi)

ax.set_yticks([0, 1, 2, 3, 4])
ax.tick_params(labelsize=14)
# ax.tick_params(axis='both', which='major', labelsize=14)
# Make the xticks at (0, pi, 2pi)
ax.set_xticks([0,np.pi,2*np.pi])

ax.set_xlabel('x', fontsize=16)
ax.set_ylabel('y', fontsize=16)

# Change this title to be "Anatomy of a figure"
ax.set_title('Anatomy of a figure', fontsize=16)

# Shift the following text to be below the title, make it more descriptive, color it blue 
ax.text(3,4.3,'Title',color='blue')

# Use this annotation command to make another annotation pointing to the green line
ax.annotate('Spine', xy=(6.28, 1.5), xytext=(5.5, 1.0),
            weight='bold', color='blue',
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color='blue'))
ax.annotate('Green line', xy=(0.8, 3.8), xytext=(1.5, 3.4),
            weight='bold', color='blue',
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color='blue'))

plt.show();