import os
from time import *
import random
filename = "apt.txt"
c = 0
with open(filename) as f:
    lines = f.read().splitlines()
while True:
    try:
        rnd0 = random.choice(lines)
        rnd1 = random.choice(lines)
        rnd2 = random.choice(lines)
        rnd3 = random.choice(lines)
        rnd4 = random.choice(lines)
        rnd5 = random.choice(lines)
        lines.remove(rnd0)
        lines.remove(rnd1)
        lines.remove(rnd2)
        lines.remove(rnd3)
        lines.remove(rnd4)
        lines.remove(rnd5)
        os.system("apt install {} {} {} {} {} {} -y".format(rnd0,rnd1,rnd2,rnd3,rnd4,rnd5))
    
        print("COMPLETED")
    except:
        c += 1
        print("Error!")
        sleep(0.3)
        os.system("clear")
        if c == 30:
            exit(0)
