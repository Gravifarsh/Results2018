i = open("sd.csv", "r")
o = open("sdclear.csv", "w")

lines = [line.split(";") for line in list(i)]
i.close()
count = 0

for num in  range(1, len(lines) - 1):
    if int(lines[num - 1][0]) > int(lines[num][0]) or int(lines[num + 1][0]) < int(lines[num][0]):
        count += 1
        continue
    o.write(";".join(lines[num]))

o.close()

print(count)
