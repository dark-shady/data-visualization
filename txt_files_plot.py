# Grabs all .txt files in folder and plots the data they contain

import matplotlib
import matplotlib.pyplot as plt
import glob
plt.style.use('ggplot')

files = glob.glob("*.txt")
data = []

for i in range(len(files)):
    f = open(files[i], "r")
    data.append(f.read().split("\t")[:-1])
    f.close()
    plt.plot(data[i], label="{}. {}".format(i, files[i][:-4])) # Tested with python 3.5, no f strings


plt.axhline(y=.008, color='r', linestyle='dashed', label='Spec', linewidth=1)
plt.legend(loc='upper left')
plt.show()
