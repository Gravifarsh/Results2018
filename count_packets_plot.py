import matplotlib.pyplot as plt
import matplotlib.ticker as  pltticker

with open("actual_freya_packets.csv", "r") as f:
    iri = [float(line.split(",")[3]) / 1000  for line in list(f)]
    
with open("nrfclear.csv", "r") as f:
    nrf = [float(line.split(";")[0]) / 1000 for line in list(f)]
    
with open("sd.csv", "r") as f:
    sd = [float(line.split(";")[0]) / 1000 for line in list(f)]


fig = plt.figure()

#-------------------------------------------
ax = fig.add_subplot(211)

ax.set_ylabel("Источник")
ax.set_xlabel("Время, с")

oneticker = pltticker.MultipleLocator(50)
ax.xaxis.set_minor_locator(oneticker)

ax.grid(True, which="major", alpha=1)
ax.grid(True, which="minor", alpha=0.2)

ax.set_yticks([1, 2, 3])
ax.set_yticklabels(["IRIDIUM", "NRF", "SD"])
ax.set_ylim([0.7, 3.3])

ax.plot(iri, [1 for x in iri], "b.")
ax.plot(nrf, [2 for x in nrf], "r.")
ax.plot(sd, [3 for x in sd], "g.")

#-------------------------------------------
ax = fig.add_subplot(223)

ax.set_ylabel("Кол-во пакетов, сотни")
ax.set_xlabel("Время, с")

oneticker = pltticker.MultipleLocator(50)
ax.xaxis.set_minor_locator(oneticker)
twoticker = pltticker.MultipleLocator(0.5)
ax.yaxis.set_minor_locator(twoticker)

ax.grid(True, which="major", alpha=1)
ax.grid(True, which="minor", alpha=0.2)

ax.plot(iri, [(x + 1) / 100.0 for x in range(len(iri))], "b.", linewidth=3)
ax.plot(nrf, [(x + 1) / 100.0 for x in range(len(nrf))], "r.", linewidth=3)

#-------------------------------------------
ax = fig.add_subplot(224)

ax.set_ylabel("Кол-во пакетов, сотни")
ax.set_xlabel("Время, с")

oneticker = pltticker.MultipleLocator(50)
ax.xaxis.set_minor_locator(oneticker)
twoticker = pltticker.MultipleLocator(40)
ax.yaxis.set_minor_locator(twoticker)

ax.grid(True, which="major", alpha=1)
ax.grid(True, which="minor", alpha=0.2)

ax.plot(sd, [(x + 1) / 100.0 for x in range(len(sd))], "g.", linewidth=3)

fig.tight_layout()

fig.savefig("telemetry_statistics.png", dpi=500)
