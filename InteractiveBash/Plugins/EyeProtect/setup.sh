apt install x11-xserver-utils sct -y

user="`whoami`"
if [[ $user != "root" ]]; then
        user="/home/`whoami`"
else
        user="/root"
fi

cd Plugins/EyeProtect
echo "" >> $user/.bashrc
echo "if [[ \`echo \"\$(date +%T)\"  | awk -F ':' '{print \$1*60*60+\$2*60+\$3}'\` -lt 68400 ]]; then " >> $user/.bashrc
echo "	xrandr --output LVDS-1 --brightness 1 && echo 10 | tee /sys/class/backlight/acpi_video0/brightness 1>/dev/null && sct 7500 " >> $user/.bashrc
echo "elif [[ \`echo \"\$(date +%T)\"  | awk -F ':' '{print \$1*60*60+\$2*60+\$3}'\` -lt 75600 ]]; then	" >> $user/.bashrc
echo "	xrandr --output LVDS-1 --brightness 0.80 && echo 2 | tee /sys/class/backlight/acpi_video0/brightness 1>/dev/null && sct 4000" >> $user/.bashrc
echo "else" >> $user/.bashrc
echo "	xrandr --output LVDS-1 --brightness 0.80 && echo 1 | tee /sys/class/backlight/acpi_video0/brightness 1>/dev/null && sct 2350" >> $user/.bashrc
echo "fi" >> $user/.bashrc
cd ../../
