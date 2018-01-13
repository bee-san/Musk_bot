f = open("ElonMuskTxt.txt", 'r')
f_read = f.readlines()
f.close()

f = open("ElonMuskTxt.txt", 'w')

for line in f_read:
    line = line[2:-2]
    line = line + "\n"
    f.write(line)



f.close()