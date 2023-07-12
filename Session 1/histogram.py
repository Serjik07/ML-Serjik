import matplotlib.pyplot as plt
import random

random.seed(42)
data = [random.normalvariate(0,1) for _ in range(1000)]

plt.hist(data, bins = 30, color = "red", alpha = 0.7)
plt.xlabel("Value")
plt.ylabel("Freequency")
plt.title("Signal Frequency")

plt.show()

