import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(0)

# Define the colors
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown', 'pink', 'cyan', 'magenta']

# Generate random frequencies for the colors
color_frequencies = {color: np.random.randint(1, 100) for color in colors}

# Plot the distribution of colors as a pie chart
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.pie(color_frequencies.values(), labels=color_frequencies.keys(), autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Distribution of Colors (Pie Chart)')

# Plot the distribution of colors as a histogram
plt.subplot(1, 2, 2)
plt.bar(color_frequencies.keys(), color_frequencies.values(), color=colors, edgecolor='black')
plt.title('Distribution of Colors (Histogram)')
plt.xlabel('Color')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
