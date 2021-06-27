import numpy as np

n = 1000000
low_id = 100000000
high_id = 999999999
max_number = 999
id = np.random.randint(low_id, high_id, size=(n, 1))
number = np.random.randint(max_number, size=(n, 1))
# id = np.array2string(id)
# number = np.array2string(number)
f = open("data2.txt", "w")
f = open("data2.txt", "a")
for i in range(n):
    f.write(str(id[i][0]) + " " + str(number[i][0]) + "\n")
f.close()
