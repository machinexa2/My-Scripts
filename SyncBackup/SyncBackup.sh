#!/bin/bash
if [[ `pgrep -f $0` != "$$" ]]; then
	echo "Exiting"
	exit
fi
while inotifywait -r -e modify,create /root/MachineYadav
do
	echo "0" > /tmp/KaliLinuxBackup
	sleep 1
	if [[ `du -s /root/MachineYadav/ | awk '{print $1}'` -gt `du -s /mnt/Restricted/Window/Kali-Mirror | awk '{print $1}'` ]]; then
		echo "1" > /tmp/KaliLinuxBackup
		echo "starting" && sleep 1
		rsync /root/MachineYadav/ /mnt/Restricted/Window/Kali-Mirror/ -av
	fi
	echo "Finishing" && sleep 0.5
done
