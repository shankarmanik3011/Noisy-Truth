import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

true_position = np.linspace(0, 10, 50)
noise = np.random.normal(0, 1, 50)
measured_position = true_position + noise

plt.plot(true_position, label="True Position")
plt.scatter(range(50), measured_position, color='red', label="Noisy Measurements")
plt.legend()
plt.title("Noisy Sensor Measurements")
plt.show()
