import numpy as np
import matplotlib.pyplot as plt

# define the CT domain
domain = np.linspace(-6, 6, 2000)
# define the DT domain
n = np.unique(np.rint(domain))

# define the original signal & impulse signal
def x(n):
    if n == -4:
        return -1
    elif n == -3:
        return -0.5
    elif n == -2:
        return 0.5
    elif n == -1:
        return 1
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 0.5
    else:
        return 0

def delta_fct(n):
    if n == 0:
        return 1
    else:
        return 0

original_signal = [x(i) for i in n]
delta = [delta_fct(i) for i in n]
x_d = [x(3 * i + 1) for i in n]
x_f = [(x(i - 2) * delta_fct(i - 2)) for i in n]
x_g = [(0.5 * (1 + (-1) ** i) * x(i)) for i in n]
x_h = [x((i - 1) ** 2) for i in n]

# plotting in a window
plt.figure(figsize=(30, 11))

plt.subplot(2,3,1)
plt.stem(n, original_signal, label="Original Signal")
plt.legend()

plt.subplot(2,3,2)
plt.stem(n, delta, label="Impulse Signal")
plt.legend()

plt.subplot(2,3,3)
plt.stem(n, x_d, label="(d)")
plt.legend()

plt.subplot(2,3,4)
plt.stem(n, x_f, label="(f)")
plt.legend()

plt.subplot(2,3,5)
plt.stem(n, x_g, label="(g)")
plt.legend()

plt.subplot(2,3,6)
plt.stem(n, x_h, label="(h)")
plt.legend()

plt.show()

