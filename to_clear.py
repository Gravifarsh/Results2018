i = open("actual_freya_packets.csv", "r")
o = open("actual_freya_packetsclear.csv", "w")

lines = [line.split(",") for line in list(i)]
i.close()
count = 0

for num in  range(1, len(lines) - 1):
    if int(lines[num - 1][3]) > int(lines[num][3]) or int(lines[num + 1][3]) < int(lines[num][3]):
        count += 1
        continue
    o.write(";".join(lines[num]))

o.close()

print(count)
