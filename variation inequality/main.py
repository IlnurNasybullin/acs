from cProfile import label
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

k = 10
# a = lambda k : np.log(1 / k)
# b = lambda k : np.sin(np.radians(k))
# c = lambda k: np.cos(np.radians(k))
a = lambda k : np.log(1 / k)
b = lambda k : np.sin(k)
c = lambda k: np.cos(k)

abc = [a(k), b(k), c(k)]

roots = np.poly1d(abc).roots

print(roots)

x = np.linspace(-2, 12, 10000)
y = a(k) * (x ** 2) + b(k) * x + c(k)

alpha1 = np.ones(1000)
alpha2 = -np.ones(1000)

beta1 = 9*np.ones(1000)
beta2 = 11*np.ones(1000)

h = np.linspace(-400, 100, 1000)

fig, ax = plt.subplots(figsize=(12, 10), dpi=80)
# Точки пересечения
# ax.plot(roots[0] * np.ones(100), np.linspace(-5, 5, 100), color='red', linewidth=5)
# ax.plot(roots[1] * np.ones(100), np.linspace(-5, 5, 100), color='red', linewidth=5)

# Оси 
ax.plot(np.linspace(-2, 13, 1000), np.zeros(1000), color='black', linewidth=2)
ax.plot(np.zeros(1000), np.linspace(-400, 100, 1000), color='black', linewidth=2)

# Alpha
ax.plot(alpha1, h, color='teal', linewidth=1, linestyle = '--')
ax.plot(alpha2, h, color='teal', linewidth=1, linestyle = '--')

# Beta
ax.plot(beta1, h, color='green', linewidth=1, linestyle = '--')
ax.plot(beta2, h, color='green', linewidth=1, linestyle = '--')

# График фукнции
ax.plot(x,y, linewidth=2, color='blue')

# Сетка для графика 
ax.grid()
ax.set_xlabel('Ось Х', fontsize=15)
ax.set_ylabel('Ось У', fontsize=15)

# Показать график
plt.show()


