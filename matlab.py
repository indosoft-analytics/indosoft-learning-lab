import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create plot
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(x, y, 'b-', linewidth=2, label='Sine Wave')
ax.set_title('Basic Matplotlib Example')
ax.set_xlabel('X values')
ax.set_ylabel('Y values')
ax.legend()
plt.show()
