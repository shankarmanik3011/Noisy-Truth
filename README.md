# Noisy Truth – WiDS Analytics Club Project

## About this project

In this project, I tried to understand how noise affects real world sensor data and how we can estimate the true values using Kalman Filters.

In many systems, sensor measurements are noisy and not accurate. Kalman Filters help in reducing this noise and give a better estimate of the actual state. This project is my learning journey to understand these ideas step by step.



## What I learned

During WiDS, I learned:

- Basics of probability and Gaussian noise
- How sensor measurements contain errors
- Concept of state estimation
- Kalman Filter theory (prediction and update steps)
- How Kalman Gain balances trust between model and measurement
- Implementing filters using Python and NumPy
- Using GitHub to manage projects


## Work done

### 1. Noisy data simulation
I created a simple simulation to generate true position and noisy sensor measurements to see how noise affects data.

File:
simulate_data.py



### 2. 1D Kalman Filter
I implemented a basic 1D Kalman Filter to estimate position from noisy measurements.  
The filter smooths the noisy data and gives better estimates.

File:
kalman_1d.py



### 3. 2D Kalman Filter (final improvement)
For the final submission, I extended the idea to 2D tracking.  
This tracks motion in both x and y directions and is closer to real-world applications.

File:
kalman_2d.py



## How to run

Install required libraries:

pip install -r requirements.txt

Run:

python simulate_data.py  
python kalman_1d.py  
python kalman_2d.py

Each file shows graphs comparing true values, noisy measurements, and filtered estimates.


## Files in this repository

- simulate_data.py – generates noisy measurements
- kalman_1d.py – 1D Kalman Filter
- kalman_2d.py – 2D Kalman Filter
- requirements.txt – required Python libraries


## Challenges faced

- Understanding Kalman Filter equations at first
- Learning GitHub and repository setup
- Installing Python libraries and fixing errors
- Debugging code

These helped me learn more practically.


## Future work

- Implement Unscented Kalman Filter (UKF)
- Try multi-sensor fusion
- Apply filtering to real datasets
- Explore robotics and localization problems


## Conclusion

This project helped me understand how theory can be applied to real data.  
I now have a clear understanding of noise modelling and Kalman Filters, and I feel more confident working with analytics and estimation problems.
