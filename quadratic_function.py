import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(0, 5, 100)
y = f(x)

plt.plot(x, y, label="f(x)")
plt.show()