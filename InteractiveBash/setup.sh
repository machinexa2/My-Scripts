#By Machine Yadav
if [[ $# -eq 0 ]]; then

user="`whoami`"
if [[ $user != "root" ]]; then
	user="/home/`whoami`"
else
	user="/root"
fi

mkdir $user/.bash_interactive/backup -p
cp $user/.bashrc $user/.bash_interactive/backup/.bashrc
cd ..
cp InteractiveBash ~/.bash_interactive/ -r
bash $user/.bash_interactive/InteractiveBash/setup.sh "$user/.bash_interactive/InteractiveBash/" 

fi
if [[ $# -eq 1 ]]; then
cd "$1" 

#Plugin No 1. ColorfulTerminal 
chmod +x Plugins/ColorfulTerminal/setup.sh
bash Plugins/ColorfulTerminal/setup.sh

#Plugin No 2. Screensaver
chmod +x Plugins/ScreenSaver/setup.sh
bash Plugins/ScreenSaver/setup.sh

#Plugin No 3. Espeak
chmod +x Plugins/Espeak/setup.sh
bash Plugins/Espeak/setup.sh

#Plugin No 4. EyeProtect
chmod +x Plugins/EyeProtect/setup.sh
bash Plugins/EyeProtect/setup.sh

fi
