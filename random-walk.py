# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Initialize and populate all_walks
all_walks = []

# Simulate random walk 500 times
for i in range(500):
    random_walk = [0]
    for x in range(100):
		# Set step: last element in random_walk
        step = random_walk[-1]
		
		# Roll the dice
        dice = np.random.randint(1,7)
		
		# Determine next step
        if dice <= 2:
			# Using max to ensure step can't go below 0
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
		
		# Add the clumsiness factor
        if np.random.rand() <= 0.001:
            step = 0
			
		# Add the step taken to the random_walk array
        random_walk.append(step)
		
	# Append random_walk to all_walks
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw and transpose it
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()