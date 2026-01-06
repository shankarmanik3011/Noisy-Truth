import numpy as np
import matplotlib.pyplot as plt

measurements = np.array([0.9, 1.2, 2.0, 3.1, 3.9, 5.2, 6.1, 7.0, 8.1, 9.0])

x = 0.0
P = 1.0

Q = 0.01
R = 0.5

estimates = []

for z in measurements:
    x_pred = x
    P_pred = P + Q

    K = P_pred / (P_pred + R)
    x = x_pred + K * (z - x_pred)
    P = (1 - K) * P_pred

    estimates.append(x)

plt.plot(measurements, label="Measurements")
plt.plot(estimates, label="Kalman Estimate")
plt.legend()
plt.title("1D Kalman Filter")
plt.show()
