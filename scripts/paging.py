import numpy as np
import matplotlib.pyplot as plt

# mess around with this script to see how the effective access time changes as you modify the paramets


def eat(probability, memory_access_time, page_fault_time):
  return (1-probability)*memory_access_time + probability*page_fault_time

x = np.arange(0, 1, 0.01)

y = [eat(i, 10,10000) for i in x]

plt.plot(x, y)
plt.xlabel('Probability of page fault')
plt.ylabel('Effective Access Time (nanoseconds)')
plt.show()