from cmath import e

with open("actual_freya_packets.csv", "r") as f:
    data = list(f)
    
data = [[pole.strip() for pole in line.split(",")[3:]] for line in data]
data = [[float(x) for x in line] for line in data if line[10] and line[11] and line[12]]

with open("sd.csv", "r") as f:
    temp = list(f)

temp = [[pole.strip() for pole in line.split(";")] for line in temp]
temp = [[float(x) for x in line[:13]] + [1 * (line[13] == "True")] for line in temp]

error = 0

res = list()

for i in range(len(temp)):
    temp[i][2] /= 100.0
    temp[i][3] /= 16.0
    temp[i][8] = 3.027 * e**(1.0698 * (5 / 1023 * temp[i][8]))
    temp[i][12], temp[i][10] = temp[i][10], temp[i][12]
    
    try:
        if temp[i][11] != temp[i][11] or temp[i][12] != temp[i][12] or temp[i][10] != temp[i][10]:
            raise ValueError
        
        pre_lat = str(temp[i][11] / 100).split(".")
        pre_lon = str(temp[i][12] / 100).split(".")
        
        temp[i][11] = float(pre_lat[0] + "." + str(int(pre_lat[1]) // 60))
        temp[i][12] = float(pre_lon[0] + "." + str(int(pre_lon[1]) // 60))
    except:
        error += 1
        continue
    
    res.append(temp[i])

print(error)
data += res

with open("nrfclear.csv", "r") as f:
    temp = list(f)

temp = [[float(pole.strip()) for pole in line.split(";")] for line in temp]

for i in range(len(temp)):
    temp[i][2] /= 100.0
    temp[i][3] /= 16.0
    
data += temp

data.sort(key=lambda x: x[0])

for i in range(1, len(data)):
    if len(data[i]) < len(data[i - 1]):
        data[i] += data[i - 1][len(data[i]):]
    data[i][4] *= 10
    data[i][5] *= 10
    data[i][6] *= 10

with open("united.csv", "w") as f:
    for line in data:
        f.write(",".join([str(x) for x in line]) + "\n")


