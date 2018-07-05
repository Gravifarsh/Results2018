import matplotlib.pyplot as plt
import matplotlib.ticker as  pltticker

from math import log

inp = open("united.csv", "r")

data = [[float(pole) for pole in line.split(",")] for line in list(inp)]

inp.close()

data = [line for line in data if 1310000 < line[0] < 1430000]

time = [line[0] / 1000 for line in data]
height = [line[10] for line in data]

fig = plt.figure()

ax = fig.add_subplot(111)

ax.plot(time, height, label="GPS", linewidth=2)

temp = [line[3] for line in data]
press = [line[1] for line in data]

height = [44330 * (1.0 - (p / 101300) ** 0.1903) for p in press]

x1, y1 = 1330, 700
x2, y2 = 1420, 75
k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1

filtered_h = list()
filtered_t = list()

for i in range(len(data)):
    if 1330 < time[i] < 1420 and abs(k * time[i] + b - height[i]) > 20:
        continue
    filtered_h.append(height[i])
    filtered_t.append(time[i])
    
ax.plot(filtered_t, filtered_h, label="BMP", linewidth=2)
ax.legend()

ax.set_xlabel("Время, с")
ax.set_ylabel("Высота над уровнем моря, м")

oneticker = pltticker.MultipleLocator(2)
twoticker = pltticker.MultipleLocator(20)
ax.xaxis.set_minor_locator(oneticker)
ax.yaxis.set_minor_locator(twoticker)

ax.grid(True, which="major", alpha=0.5)
ax.grid(True, which="minor", alpha=0.2)

fig.tight_layout()

fig.savefig("height.png", dpi=500)
