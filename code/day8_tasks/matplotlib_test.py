import numpy as np
import matplotlib.pyplot as plt

# sin(x)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.show()

# 1/x
x = np.linspace(-10, -0.1, 500)
x2 = np.linspace(0.1, 10, 500)

plt.plot(x, 1/x)
plt.plot(x2, 1/x2)
plt.show()

# circle 参数方程
t = np.linspace(0, 2*np.pi, 1000)
x = np.cos(t)
y = np.sin(t)

plt.plot(x, y)
plt.axis("equal")
plt.show()

# 多条线绘制
plt.plot(x, x, label="y=x")
plt.plot(x, x**2, label="y=x^2")
plt.plot(x, np.sin(x), label="y=sin(x)")
plt.legend()
plt.show()