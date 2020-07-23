while true; do if [[ `date +%T | awk -F ':' '{print $1*60*60+$2*60+$3}'` -gt 84600 ]]; then notify-send Poweroff Powering_off_Save_your_work_you_have_5_minute -u critical; sleep 300; poweroff; else echo "Less than 84600";sleep 10;clear ; fi; done

