while true
do
	if [[ `cat /tmp/KaliLinuxBackup` -eq 1 ]]; then
		echo "Not killed! Waiting"
		sleep 0.2
	else
		echo "Killing"
		kill "`pgrep -f SyncBackup.sh`" 
		break
	fi
done
