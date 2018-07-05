import matplotlib.pyplot as plt
import matplotlib.ticker as  pltticker

inp = open("united.csv", "r")

data = [[float(pole) for pole in line.split(",")] for line in list(inp)]

inp.close()

data = [line for line in data if 1310000 < line[0] < 1430000]

time = [line[0] / 1000 for line in data]
press = [line[1] / 1000 for line in data]
btemp = [line[2] for line in data]
dtemp = [line[3] for line in data]
x = [line[4] for line in data]
y = [line[5] for line in data]
z = [line[6] for line in data]

fig = plt.figure(figsize=(16, 9))

#-------------------------------------------
ax = fig.add_subplot(311)
#ax.set_title("Ускорение")
#ax.set_xlabel("Время, с")
ax.set_ylabel("Ускорение, g")

ax.set_ylim([-12, 22])

oneticker = pltticker.MultipleLocator(10)
twoticker = pltticker.MultipleLocator(5)
ax.xaxis.set_major_locator(oneticker)
ax.yaxis.set_major_locator(twoticker)

oneticker = pltticker.MultipleLocator(1)
twoticker = pltticker.MultipleLocator(1)
ax.xaxis.set_minor_locator(oneticker)
ax.yaxis.set_minor_locator(twoticker)

ax.grid(True, which="major", alpha=0.5)
ax.grid(True, which="minor", alpha=0.2)

ax.plot(time, x, color="red", linewidth=1, label="x")
ax.plot(time, y, color="blue", linewidth=1, label="y")
ax.plot(time, z, color="green", linewidth=1, label="z")
ax.legend(loc="upper right", ncol=3)

#-------------------------------------------
ax = fig.add_subplot(312)
#ax.set_title("Давление")
#ax.set_xlabel("Время, с")
ax.set_ylabel("Давление, кПа")

ax.set_ylim([92, 105])

oneticker = pltticker.MultipleLocator(10)
twoticker = pltticker.MultipleLocator(2)
ax.xaxis.set_major_locator(oneticker)
ax.yaxis.set_major_locator(twoticker)

oneticker = pltticker.MultipleLocator(1)
twoticker = pltticker.MultipleLocator(0.5)
ax.xaxis.set_minor_locator(oneticker)
ax.yaxis.set_minor_locator(twoticker)

ax.grid(True, which="major", alpha=0.5)
ax.grid(True, which="minor", alpha=0.2)

ax.plot(time, press, linewidth=1, label="BMP")
ax.legend(loc="lower right")
    
#-------------------------------------------
ax = fig.add_subplot(313)
#ax.set_title("Температура")
#ax.set_xlabel("Время, с")
ax.set_xlabel("Время, с")
ax.set_ylabel("Температура, C")

ax.set_ylim([20, 45])

oneticker = pltticker.MultipleLocator(10)
twoticker = pltticker.MultipleLocator(2)
ax.xaxis.set_major_locator(oneticker)
ax.yaxis.set_major_locator(twoticker)

oneticker = pltticker.MultipleLocator(1)
twoticker = pltticker.MultipleLocator(0.5)
ax.xaxis.set_minor_locator(oneticker)
ax.yaxis.set_minor_locator(twoticker)

ax.grid(True, which="major", alpha=0.5)
ax.grid(True, which="minor", alpha=0.2)

ax.plot(time, btemp, linewidth=1, label="BMP")
ax.plot(time, dtemp, linewidth=1, label="DS")
ax.legend(loc="upper left")

fig.tight_layout()

fig.savefig("base.png", dpi=500)
