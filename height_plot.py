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

ax.plot(time, height, label="GPS")

temp = [line[3] for line in data]
press = [line[1] for line in data]

for i in range(1, len(data)):
    h = 44330 * (1.0 - pow(press[i]/press[0], 0.1903));
    height.append(h)
    
ax.plot(time, height, label="BMP")
ax.legend()

ax.set_xlabel("Время, с")
ax.set_ylabel("Высота над уровнем моря, м")

oneticker = pltticker.MultipleLocator(10)
twoticker = pltticker.MultipleLocator(50)
ax.xaxis.set_minor_locator(oneticker)
ax.yaxis.set_minor_locator(twoticker)

ax.grid(True, which="major", alpha=0.5)
ax.grid(True, which="minor", alpha=0.2)

fig.tight_layout()

fig.savefig("height.png", dpi=500)
