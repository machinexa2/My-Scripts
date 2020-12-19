DIRNAME="InteractiveBash"
CURRENT="`pwd`"

if [[ $# -eq 0 ]]; then
	USERDIR="`whoami`"
	if [[ $USERDIR != "root" ]]; then
		USERDIR="/home/`whoami`"
	else
		USERDIR="/root"
	fi

	mkdir "$USERDIR""/.bash_interactive/backup" -p
	cp "$USERDIR""/.bashrc" "$USERDIR""/.bash_interactive/backup/.bashrc"
	cd .. && cp InteractiveBash/ ~/.bash_interactive/ -r
	bash "$USERDIR""/.bash_interactive/InteractiveBash/setup.sh" $USERDIR 
fi

if [[ $# -eq 1 ]]; then
	cd "$1""/.bash_interactive/InteractiveBash/" || exit

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
