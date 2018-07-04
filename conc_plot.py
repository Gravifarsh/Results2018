import matplotlib.pyplot as plt
import matplotlib.ticker as  pltticker

from math import log

inp = open("united.csv", "r")

data = [[float(pole) for pole in line.split(",")] for line in list(inp)]

inp.close()

data = [line for line in data if 1310000 < line[0] < 1430000]

time = [line[0] / 1000 for line in data]
height = [line[10] for line in data]
co2 = [line[7] for line in data]
co = [line[8] for line in data]

fig = plt.figure()

#-------------------------------------------
ax = fig.add_subplot(311)
ax.set_ylabel("Концентрация,\n ppm")

ax.plot(time, co, label="CO")

ax.legend()

oneticker = pltticker.MultipleLocator(1)
twoticker = pltticker.MultipleLocator(1)
ax.xaxis.set_minor_locator(oneticker)
ax.yaxis.set_minor_locator(twoticker)

ax.grid(True, which="major", alpha=0.5)
ax.grid(True, which="minor", alpha=0.2)

#-------------------------------------------
ax = fig.add_subplot(312)
ax.set_ylabel("Концентрация,\n ppm")

ax.plot(time, co2, "orange", label="CO2")

ax.legend()

oneticker = pltticker.MultipleLocator(1)
twoticker = pltticker.MultipleLocator(1)
ax.xaxis.set_minor_locator(oneticker)
ax.yaxis.set_minor_locator(twoticker)

ax.grid(True, which="major", alpha=0.5)
ax.grid(True, which="minor", alpha=0.2)

#-------------------------------------------
ax = fig.add_subplot(313)
ax.set_xlabel("Время, с")
ax.set_ylabel("Высота, м")

ax.plot(time, height, "green", label="GPS")

ax.legend()

oneticker = pltticker.MultipleLocator(1)
twoticker = pltticker.MultipleLocator(25)
ax.xaxis.set_minor_locator(oneticker)
ax.yaxis.set_minor_locator(twoticker)

ax.grid(True, which="major", alpha=0.5)
ax.grid(True, which="minor", alpha=0.2)

fig.tight_layout()

#plt.show()
fig.savefig("conc.png", dpi=500)
