import numpy as np
import matplotlib.pyplot as plt

total_time = 100
rate = 1
colors = ['red', 'blue']
probabilities = [1/4, 3/4]

inter_arrival_times = np.random.exponential(scale=1/rate, size=1000)

arrival_times = np.cumsum(inter_arrival_times)
arrival_times = arrival_times[arrival_times <= total_time]

plt.figure(figsize=(10, 5))
for arrival_time in arrival_times:
    color = np.random.choice(colors, p=probabilities)
    plt.plot(arrival_time, 1, 'o', color=color)

plt.title('Mining Processes with Different Probabilities for Colors')
plt.xlabel('Time')
plt.ylabel('Arrivals')
plt.xlim(0, total_time)
plt.ylim(0, 2)
plt.yticks([])
plt.grid(True)
plt.show()