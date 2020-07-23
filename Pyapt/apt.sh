apt update 
apt list --upgradable | cut -d '/' -f 1 | sort -u > apt.txt
python3 apt.py
