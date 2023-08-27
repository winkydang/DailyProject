import numpy as np
from matplotlib import pyplot as plt  # plt.subplots(1, 2) creates a figure with one row and two columns of subplots.

_, axes = plt.subplots(1, 2)
# The first value returned by plt.subplots() (which is represented by _) is typically ignored or discarded because it refers to the figure.
# The second value returned by plt.subplots() (which is represented by axes) is a NumPy array containing references to the subplot axes. In this case, you'll have two axes objects in the array, one for each subplot.
# You can then use the axes array to plot data on each subplot,
# Plot on the first subplot (left)
# axes[0].plot([1,2,3], [3,2,1])
axes[0].plot(np.array([1,2,8]),np.array([3,2,1]))

# Plot on the second subplot (right)
axes[1].plot([7,9], [8,16])

# You can customize each subplot as needed
axes[0].set_title("Subplot 1")
axes[1].set_title("Subplot 2")

# Finally, display the figure
plt.show()
