apt install cmatrix oneko neofetch -y
apt install cowsay fortune lolcat -y 
apt install imagemagick x11-apps figlet -y
apt install toilet -y
rm /usr/share/figlet/*.flc
user="`whoami`"
if [[ $user != "root" ]]; then
        user="/home/`whoami`"
else
        user="/root"
fi

cd Plugins/ColorfulTerminal
export PATH=/usr/games:$PATH
COWPATH="`pwd`""/"
COWPATH="$COWPATH""Cowsay.py"
random=$(od -An -N4 -i < /dev/urandom) 

if [ $(( $random % 5 )) -eq 1 ]; then
	RANDOM1=$RANDOM
	if [ $(( $RANDOM1 % 2 )) -eq 0 ]; then
		RANDOM2=$RANDOM
		if [ $(( $RANDOM2 % 3 )) -eq 0 ]; then
			python3 "$COWPATH"
			echo
		elif [ $(( $RANDOM2 % 3 )) -eq 1 ]; then 
			python3 "$COWPATH"
			oneko 1>/dev/null 2>/dev/null &
			echo	
		elif  [ $(( $RANDOM2 % 3 )) -eq 2 ]; then 
			python3 "$COWPATH" | lolcat
			echo
		fi
	elif [ $(( $RANDOM1 % 2 )) -eq 1 ]; then
		RANDOM2=$RANDOM
		if [ $(( $RANDOM2 % 3 )) -eq 0 ]; then
			xcowsay "Text"
			echo
		elif [ $(( $RANDOM2 % 3 )) -eq 1 ]; then 
			xcowsay "Text"
			xeyes 1>/dev/null 2>/dev/null &
			echo	
		elif  [ $(( $RANDOM2 % 3 )) -eq 2 ]; then 
			fortune | xcowsay
			echo
		fi
	fi 
elif [ $(( $random % 5 )) -eq 2 ]; then
	RANDOM1=$RANDOM
	if [ $(( $RANDOM1 % 2 )) -eq 0 ]; then
		fortune
		echo 
	elif [ $(( $RANDOM1 % 2 )) -eq 1 ]; then
		fortune | lolcat
		timeout 300 oneko -dog 1>/dev/null 2>/dev/null &
		echo 
	fi
elif [ $(( $random % 5 )) -eq 3 ]; then
	RANDOM1=$RANDOM
	if [ $(( $RANDOM1 % 2 )) -eq 0 ]; then
		neofetch
		echo 
	elif [ $(( $RANDOM1 % 2 )) -eq 1 ]; then
		neofetch | lolcat
		echo
	fi
elif [ $(( $random % 5 )) -eq 4 ]; then
	RANDOM1=$RANDOM
	if [ $(( $RANDOM1 % 3 )) -eq 0 ]; then
		RANDOM2=$RANDOM
		if [ $(( $RANDOM2 % 2 )) -eq 0 ]; then
			timeout 10 cmatrix -bos
			echo
		elif [ $(( $RANDOM2 % 2 )) -eq 1 ]; then
			timeout 10 cmatrix -ns -C red
		fi
	elif [ $(( $RANDOM1 % 3 )) -eq 1 ]; then
		timeout 10 cmatrix -s | lolcat
		echo 
	elif [ $(( $RANDOM1 % 3 )) -eq 2 ]; then 
		timeout 10 cmatrix -as -C blue
		oneko -sakura 1>/dev/null 2>/dev/null &
	fi
elif [ $(( $random % 5 )) -eq 0 ]; then
	RANDOM1=$RANDOM
	toilet_array=(`ls /usr/share/figlet | xargs`)
	TOILET=$(( $RANDOM % ${#toilet_array[@]} ))
	toilet_font=${toilet_array[$TOILET]}
	if [ $(( $RANDOM1 % 4 )) -eq 0 ]; then
		toilet -f $toilet_font -F gay "Text"
	elif [ $(( $RANDOM1 % 4 )) -eq 1 ]; then
		toilet -f $toilet_font "Text"
	elif [ $(( $RANDOM1 % 4 )) -eq 2 ]; then
		toilet -f $toilet_font -F border "Text"
	elif [ $(( $RANDOM1 % 4 )) -eq 3 ]; then
		toilet -F metal	-f $toilet_font
	fi 
fi
disown -a
cd ../../
