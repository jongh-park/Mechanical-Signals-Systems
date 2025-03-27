import numpy as np
import matplotlib.pyplot as plt

def function(t):
    if -2 <= t < -1: return t + 1
    elif -1 <= t < 0: return 1
    elif 0 <= t < 1: return 2
    elif 1 <= t < 2: return -t + 2
    else: return 0

def u(t):
    if t >= 0: return 1
    else: return 0

# t value
t = np.linspace(-3, 3, 1500)

# functions
original_fct = [function(i) for i in t]
x_a = [function(i - 1) for i in t]
x_c = [function(2 * i + 1) for i in t]
x_e = [(function(i) + function(-i)) * u(i) for i in t]
unit_fct = [u(i) for i in t]

# plotting in a window
plt.figure(figsize=(30, 11))

plt.subplot(2,3,1)
plt.plot(t, original_fct, label='Original Function', color='black')
plt.plot(t, x_a, label='x(a)', color='blue')
plt.plot(t, x_c, label='x(c)', color='orange')
plt.plot(t, x_e, label='x(e)', color='green')
plt.plot()
plt.axhline(0, color='gray', linewidth=0.5)  # x축 표시
plt.axvline(0, color='gray', linewidth=0.5)  # y축 표시
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.title('Problem 1')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()

plt.subplot(2,3,2)
plt.plot(t, unit_fct, label='u(t)', color='red')
plt.legend()

plt.subplot(2,3,3)
plt.plot(t, original_fct, label='Original Function', color='black')
plt.legend()

plt.subplot(2,3,4)
plt.plot(t, x_a, label='x(a)', color='blue')
plt.legend()

plt.subplot(2,3,5)
plt.plot(t, x_c, label='x(c)', color='orange')
plt.legend()

plt.subplot(2,3,6)
plt.plot(t, x_e, label='x(e)', color='green')
plt.legend()

plt.show()
