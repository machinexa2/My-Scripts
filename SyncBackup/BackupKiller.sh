while true
if [[ `cat /tmp/KaliLinuxBackup` -eq 1 ]]; then
	echo "Not killed! Waiting"
	sleep 0.2
else
	echo "Killing"
	kill `pgrep -f SyncBackup_Kali-Linux.sh` 
	exit
fi


