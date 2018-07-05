import matplotlib.pyplot as plt
import matplotlib.ticker as  pltticker

inp = open("united.csv", "r")

data = [[float(pole) for pole in line.split(",")] for line in list(inp)]

inp.close()

#data = [line for line in data if 1310000 < line[0] < 1430000]

time = [line[0] / 1000 for line in data]
height = [line[10] for line in data]
ticks = [line[9] for line in data]

delta = 46
start_t = 0
for i in range(len(data)):
    if time[i] - time[start_t] >= delta:
        stop_t = i
        break
        
radiation = [0] * stop_t

while stop_t < len(data):
    while time[stop_t] - time[start_t] > delta:
        start_t += 1
    radiation.append(ticks[stop_t] - ticks[start_t])
    stop_t += 1
    
begin = end = 0
for i in range(len(data)):
    begin = i
    if time[i] > 1310: 
        break
for i in range(len(data)):
    end = i
    if time[i] > 1430: 
        break   

fig = plt.figure()

#---------------------------------
ax = fig.add_subplot(211)

ax.plot(time[begin:end], height[begin:end], label="GPS", linewidth=2)

oneticker = pltticker.MultipleLocator(2)
twoticker = pltticker.MultipleLocator(25)
ax.xaxis.set_minor_locator(oneticker)
ax.yaxis.set_minor_locator(twoticker)

ax.grid(True, which="major", alpha=0.5)
ax.grid(True, which="minor", alpha=0.2)

ax.legend()

ax.set_ylabel("Высота над уровнем\nморя, м")

#---------------------------------
ax = fig.add_subplot(212)

ax.plot(time[begin:end], radiation[begin:end], "orange", linewidth=2, label="GEIGER")

oneticker = pltticker.MultipleLocator(2)
twoticker = pltticker.MultipleLocator(1)
ax.xaxis.set_minor_locator(oneticker)
ax.yaxis.set_minor_locator(twoticker)

ax.grid(True, which="major", alpha=0.5)
ax.grid(True, which="minor", alpha=0.2)

ax.legend()

ax.set_ylabel("Радиационный\nфон, мкРн/ч")
ax.set_xlabel("Время, с")


fig.tight_layout()

fig.savefig("radiation.png", dpi=500)



