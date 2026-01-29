import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# true motion in 2D
t = np.linspace(0, 10, 50)
true_x = t
true_y = 0.5 * t

noise_x = np.random.normal(0, 1, 50)
noise_y = np.random.normal(0, 1, 50)

meas_x = true_x + noise_x
meas_y = true_y + noise_y

x_est = np.array([0.0, 0.0])
P = np.eye(2)

Q = np.eye(2) * 0.01
R = np.eye(2) * 1

estimates = []

for z in zip(meas_x, meas_y):
    z = np.array(z)

    # predict
    x_pred = x_est
    P_pred = P + Q

    # update
    K = P_pred @ np.linalg.inv(P_pred + R)
    x_est = x_pred + K @ (z - x_pred)
    P = (np.eye(2) - K) @ P_pred

    estimates.append(x_est.copy())

estimates = np.array(estimates)

plt.scatter(meas_x, meas_y, label="Measurements")
plt.plot(estimates[:,0], estimates[:,1], label="Kalman Estimate")
plt.plot(true_x, true_y, label="True Path")
plt.legend()
plt.title("2D Kalman Filter Tracking")
plt.show()
