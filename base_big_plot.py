import matplotlib.pyplot as plt
import matplotlib.ticker as  pltticker

inp = open("sd.csv", "r")

data = [line.split(";") for line in list(inp)]

inp.close()

data = [[float(column) for column in line[:13]] + [line[13].strip()] for line in data]
data = [line for line in data if 5000 < line[0]]

time = [line[0] / 1000 for line in data]
x = [line[4] * 10 for line in data]
y = [line[5] * 10 for line in data]
z = [line[6] * 10 for line in data]
press = [line[1] / 1000 for line in data]
btemp = [line[2] / 100 for line in data]
dtemp = [line[3] / 16 for line in data]

fig = plt.figure()

#-------------------------------------------
ax = fig.add_subplot(311)
ax.set_title("SD: {} packets".format(len(data)))
#ax.set_title("Ускорение")
#ax.set_xlabel("Время, с")
ax.set_ylabel("Ускорение, g")

#ax.set_ylim([-20, 20])

#oneticker = pltticker.MultipleLocator(10)
#twoticker = pltticker.MultipleLocator(5)
#ax.xaxis.set_major_locator(oneticker)
#ax.yaxis.set_major_locator(twoticker)

#oneticker = pltticker.MultipleLocator(1)
#twoticker = pltticker.MultipleLocator(1)
#ax.xaxis.set_minor_locator(oneticker)
#ax.yaxis.set_minor_locator(twoticker)

#ax.grid(True, which="major", alpha=0.5)
#ax.grid(True, which="minor", alpha=0.2)

ax.plot(time, x, color="red", linewidth=1)
ax.plot(time, y, color="blue", linewidth=1)
ax.plot(time, z, color="green", linewidth=1)

#-------------------------------------------
ax = fig.add_subplot(312)
#ax.set_title("Давление")
#ax.set_xlabel("Время, с")
ax.set_ylabel("Давление, кПа")

#ax.set_ylim([90, 110])

#oneticker = pltticker.MultipleLocator(10)
#twoticker = pltticker.MultipleLocator(1)
#ax.xaxis.set_major_locator(oneticker)
#ax.yaxis.set_major_locator(twoticker)

#oneticker = pltticker.MultipleLocator(1)
#twoticker = pltticker.MultipleLocator(0.5)
#ax.xaxis.set_minor_locator(oneticker)
#ax.yaxis.set_minor_locator(twoticker)

#ax.grid(True, which="major", alpha=0.5)
#ax.grid(True, which="minor", alpha=0.2)

ax.plot(time, press, linewidth=1)
    
#-------------------------------------------
ax = fig.add_subplot(313)
#ax.set_title("Температура")
#ax.set_xlabel("Время, с")
ax.set_xlabel("Время, с")
ax.set_ylabel("Температура, C")

#ax.set_ylim([20, 40])

#oneticker = pltticker.MultipleLocator(10)
#twoticker = pltticker.MultipleLocator(1)
#ax.xaxis.set_major_locator(oneticker)
#ax.yaxis.set_major_locator(twoticker)

#oneticker = pltticker.MultipleLocator(1)
#twoticker = pltticker.MultipleLocator(0.5)
#ax.xaxis.set_minor_locator(oneticker)
#ax.yaxis.set_minor_locator(twoticker)

#ax.grid(True, which="major", alpha=0.5)
#ax.grid(True, which="minor", alpha=0.2)

ax.plot(time, btemp, linewidth=1)
ax.plot(time, dtemp, linewidth=1)

fig.tight_layout()

plt.show()
