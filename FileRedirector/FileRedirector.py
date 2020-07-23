import sys
import pathlib
import subprocess
import argparse
from time import *
parser = argparse.ArgumentParser(description='File Redirector', epilog='Redirects file')
parser.add_argument('-i', '--input', type=str, help='Input script')
parser.add_argument('-o', '--output', type=str, help='Output script')
parser.add_argument('-c', '--content', type=str, help='Content to redirect inside output script')
argv = parser.parse_args()
if not argv.input or not argv.output or not argv.content:
    print("Use -h")
    exit()

iamsmart = True
if iamsmart:
    import os;os.system('rm pypy 2>/dev/null')
    f1 =[line.rstrip('\n') for line in open(argv.input)]
    f2 = open('pypy', 'w+')
    for line in f1:
        line = line.replace('$', '\$')
        #line = line.replace('\$', '\\\$')
        line = line.replace('`', '\`')
        #line = line.replace('\`', '\\\`')
        line = line.replace('"', '\\\"')
        #line = line.replace('\"', '\\\\\"')
        print(line)
        f2.write(line)
        f2.write('\n')
    f2.close()
    sublist = []
    paths = '/bin/bash'
    sublist.append(paths)
    paths = str(pathlib.Path(__file__).parent.absolute())
    paths += '/FileRedirector.sh'
    sublist.append(paths)
    sublist.append(argv.output)
    print(sublist)
    subprocess.run(sublist) 
