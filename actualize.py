i1 = open("iridium_packets.csv", "r")
i2 = open("freya_packets.csv", "r")

iri = list(i1)
fre = list(i2)

i1.close()
i2.close()

o1 = open("actual_iridium_packets.csv", "w")
o2 = open("actual_freya_packets.csv", "w")

#o1.write(iri[0])
for line in iri[1:]:
    if int(line.split(",")[0]) >= 126:
        o1.write(line)

#o2.write(fre[0])       
for line in fre[1:]:
    if int(line.split(",")[1]) >= 126:
        o2.write(line)
