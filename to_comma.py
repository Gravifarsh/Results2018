i = open("nrf.csv", "r")
o = open("nrfcomma.csv", "w")
o.write(i.read().replace(";", ","))
i.close()
o.close()
