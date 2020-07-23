import random
import os
os.system("whoami 1>/tmp/tmp")
uid = [line.rstrip('\n') for line in open('/tmp/tmp','r')][0]
path = os.path.dirname(os.path.realpath(__file__))
cowfile = path+"/Cowsay"
cowcow = [line.rstrip('\n') for line in open(cowfile)]
random = random.choice(cowcow)
text = """cowsay -f %s {Hello %s} """ % (random, uid)
os.system(text)
