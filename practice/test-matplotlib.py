import matplotlib.pyplot as plt
import numpy as np

# График 1

plt.figure(figsize=(6, 4))
x1 = [1, 5, 10, 15, 20]
y_red = [1, 7, 3, 5, 11]
y_green = [4, 3, 1, 8, 12]

plt.plot(x1, y_red, color='tab:red', marker='o', linestyle='-', label='line 1')
plt.plot(x1, y_green, color='green', marker='o', linestyle='-.', label='line 1')

plt.legend(loc='upper left')
plt.tight_layout()
plt.show()


# График 2

fig = plt.figure(figsize=(10, 5))
x2 = [1, 2, 3, 4, 5]

ax1 = plt.subplot(2, 1, 1)
y2_top = [1, 7, 6, 3, 5]
ax1.plot(x2, y2_top)

ax2 = plt.subplot(2, 2, 3)
y2_left = [9, 4, 2, 4, 9]
ax2.plot(x2, y2_left)

ax3 = plt.subplot(2, 2, 4)
y2_right = [-7, -4, 2, -4, -7]
ax3.plot(x2, y2_right)

plt.tight_layout()
plt.show()


# График 3

plt.figure(figsize=(6, 4))
x3 = np.linspace(-5, 5, 11)
y3 = x3**2
plt.plot(x3, y3)

plt.annotate('min', xy=(0, 0), xytext=(0, 10),
             arrowprops=dict(facecolor='green', shrink=0.05, width=6, headwidth=15),
             horizontalalignment='center')
plt.tight_layout()
plt.show()


# График 4

plt.figure(figsize=(7, 4))

np.random.seed(0)
data = np.random.randint(0, 11, size=(7, 7))

plt.pcolormesh(data, cmap='viridis', vmin=0, vmax=10)
plt.colorbar()
plt.xlim(0, 7)
plt.ylim(0, 7)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
x5 = np.linspace(0, 5, 500)
y5 = np.cos(np.pi * x5)

plt.plot(x5, y5, color='tab:red')
plt.fill_between(x5, y5, 0, color='tab:blue')
plt.ylim(-1.1, 1.1)
plt.tight_layout()
plt.show()


# График 6

plt.figure(figsize=(6, 4))
x6 = np.linspace(0, 5, 500)
y6 = np.cos(np.pi * x6)

y6_masked = np.copy(y6)
y6_masked[y6_masked < -0.5] = np.nan

plt.plot(x6, y6_masked, linewidth=3, color='tab:blue')
plt.ylim(-1.0, 1.0)
plt.tight_layout()
plt.show()


# График 7

fig, axs = plt.subplots(1, 3, figsize=(12, 3.5))
x7 = np.arange(7)
y7 = np.arange(7)

axs[0].step(x7, y7, where='pre', color='green')
axs[0].plot(x7, y7, 'go')
axs[0].grid(True)

axs[1].step(x7, y7, where='post', color='green')
axs[1].plot(x7, y7, 'go')
axs[1].grid(True)

axs[2].step(x7, y7, where='mid', color='green')
axs[2].plot(x7, y7, 'go')
axs[2].grid(True)

plt.tight_layout()
plt.show()


# График 8

plt.figure(figsize=(6, 4))
x8 = np.linspace(0, 10, 11)


y1 = np.linspace(0, 5.0, len(x8))
y2 = np.linspace(0, 10.0, len(x8))
y3 = np.linspace(0, 20.0, len(x8))

plt.stackplot(x8, y1, y2, y3, labels=['y1', 'y2', 'y3'])
plt.legend(loc='upper left')
plt.xlim(-0.5, 10.5)
plt.ylim(0, 28)
plt.tight_layout()
plt.show()


# График 9

plt.figure(figsize=(6, 4))
labels = ['Ford', 'Toyota', 'BMV', 'AUDI', 'Jaguar']
sizes = [2.5, 1.5, 5, 2, 3.5]
explode = (0, 0, 0.15, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, startangle=0)
plt.tight_layout()
plt.show()


# График 10

plt.figure(figsize=(6, 4))
labels = ['Ford', 'Toyota', 'BMV', 'AUDI', 'Jaguar']
sizes = [2.5, 1.5, 5, 2, 3.5]

plt.pie(sizes, labels=labels, startangle=0, wedgeprops=dict(width=0.5))
plt.tight_layout()
plt.show()
