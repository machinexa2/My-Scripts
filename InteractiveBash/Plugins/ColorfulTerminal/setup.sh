apt install sudo wget python3 cmatrix oneko neofetch -y
apt install cowsay fortune lolcat -y 
apt install imagemagick x11-apps figlet -y
apt install toilet xcowsay -y
rm /usr/share/figlet/*.flc
user="`whoami`"
if [[ $user != "root" ]]; then
        user="/home/`whoami`"
else
        user="/root"
fi

cd Plugins/ColorfulTerminal 
echo "export PATH=/usr/games:\$PATH" >> $user/.bashrc 
echo "COWPATH=\"`pwd`\"\"/\"" >> $user/.bashrc 
echo "COWPATH=\"\$COWPATH\"\"Cowsay.py\"" >> $user/.bashrc 
echo "random=\$(od -An -N4 -i < /dev/urandom) " >> $user/.bashrc 
echo "" >> $user/.bashrc 
echo "if [ \$(( \$random % 5 )) -eq 1 ]; then" >> $user/.bashrc 
echo "	RANDOM1=\$RANDOM" >> $user/.bashrc 
echo "	if [ \$(( \$RANDOM1 % 2 )) -eq 0 ]; then" >> $user/.bashrc 
echo "		RANDOM2=\$RANDOM" >> $user/.bashrc 
echo "		if [ \$(( \$RANDOM2 % 3 )) -eq 0 ]; then" >> $user/.bashrc 
echo "			python3 \"\$COWPATH\"" >> $user/.bashrc 
echo "			echo" >> $user/.bashrc 
echo "		elif [ \$(( \$RANDOM2 % 3 )) -eq 1 ]; then " >> $user/.bashrc 
echo "			python3 \"\$COWPATH\"" >> $user/.bashrc 
echo "			oneko 1>/dev/null 2>/dev/null &" >> $user/.bashrc 
echo "			echo	" >> $user/.bashrc 
echo "		elif  [ \$(( \$RANDOM2 % 3 )) -eq 2 ]; then " >> $user/.bashrc 
echo "			python3 \"\$COWPATH\" | lolcat" >> $user/.bashrc 
echo "			echo" >> $user/.bashrc 
echo "		fi" >> $user/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 2 )) -eq 1 ]; then" >> $user/.bashrc 
echo "		RANDOM2=\$RANDOM" >> $user/.bashrc 
echo "		if [ \$(( \$RANDOM2 % 3 )) -eq 0 ]; then" >> $user/.bashrc 
echo "			xcowsay \"Text\"" >> $user/.bashrc 
echo "			echo" >> $user/.bashrc 
echo "		elif [ \$(( \$RANDOM2 % 3 )) -eq 1 ]; then " >> $user/.bashrc 
echo "			xcowsay \"Text\"" >> $user/.bashrc 
echo "			xeyes 1>/dev/null 2>/dev/null &" >> $user/.bashrc 
echo "			echo	" >> $user/.bashrc 
echo "		elif  [ \$(( \$RANDOM2 % 3 )) -eq 2 ]; then " >> $user/.bashrc 
echo "			fortune | xcowsay" >> $user/.bashrc 
echo "			echo" >> $user/.bashrc 
echo "		fi" >> $user/.bashrc 
echo "	fi " >> $user/.bashrc 
echo "elif [ \$(( \$random % 5 )) -eq 2 ]; then" >> $user/.bashrc 
echo "	RANDOM1=\$RANDOM" >> $user/.bashrc 
echo "	if [ \$(( \$RANDOM1 % 2 )) -eq 0 ]; then" >> $user/.bashrc 
echo "		fortune" >> $user/.bashrc 
echo "		echo " >> $user/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 2 )) -eq 1 ]; then" >> $user/.bashrc 
echo "		fortune | lolcat" >> $user/.bashrc 
echo "		timeout 300 oneko -dog 1>/dev/null 2>/dev/null &" >> $user/.bashrc 
echo "		echo " >> $user/.bashrc 
echo "	fi" >> $user/.bashrc 
echo "elif [ \$(( \$random % 5 )) -eq 3 ]; then" >> $user/.bashrc 
echo "	RANDOM1=\$RANDOM" >> $user/.bashrc 
echo "	if [ \$(( \$RANDOM1 % 2 )) -eq 0 ]; then" >> $user/.bashrc 
echo "		neofetch" >> $user/.bashrc 
echo "		echo " >> $user/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 2 )) -eq 1 ]; then" >> $user/.bashrc 
echo "		neofetch | lolcat" >> $user/.bashrc 
echo "		echo" >> $user/.bashrc 
echo "	fi" >> $user/.bashrc 
echo "elif [ \$(( \$random % 5 )) -eq 4 ]; then" >> $user/.bashrc 
echo "	RANDOM1=\$RANDOM" >> $user/.bashrc 
echo "	if [ \$(( \$RANDOM1 % 3 )) -eq 0 ]; then" >> $user/.bashrc 
echo "		RANDOM2=\$RANDOM" >> $user/.bashrc 
echo "		if [ \$(( \$RANDOM2 % 2 )) -eq 0 ]; then" >> $user/.bashrc 
echo "			timeout 10 cmatrix -bos" >> $user/.bashrc 
echo "			echo" >> $user/.bashrc 
echo "		elif [ \$(( \$RANDOM2 % 2 )) -eq 1 ]; then" >> $user/.bashrc 
echo "			timeout 10 cmatrix -ns -C red" >> $user/.bashrc 
echo "		fi" >> $user/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 3 )) -eq 1 ]; then" >> $user/.bashrc 
echo "		timeout 10 cmatrix -s | lolcat" >> $user/.bashrc 
echo "		echo " >> $user/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 3 )) -eq 2 ]; then " >> $user/.bashrc 
echo "		timeout 10 cmatrix -as -C blue" >> $user/.bashrc 
echo "		oneko -sakura 1>/dev/null 2>/dev/null &" >> $user/.bashrc 
echo "	fi" >> $user/.bashrc 
echo "elif [ \$(( \$random % 5 )) -eq 0 ]; then" >> $user/.bashrc 
echo "	RANDOM1=\$RANDOM" >> $user/.bashrc 
echo "	toilet_array=(\`ls /usr/share/figlet | xargs\`)" >> $user/.bashrc 
echo "	TOILET=\$(( \$RANDOM % \${#toilet_array[@]} ))" >> $user/.bashrc 
echo "	toilet_font=\${toilet_array[\$TOILET]}" >> $user/.bashrc 
echo "	if [ \$(( \$RANDOM1 % 4 )) -eq 0 ]; then" >> $user/.bashrc 
echo "		toilet -f \$toilet_font -F gay \"Text\"" >> $user/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 4 )) -eq 1 ]; then" >> $user/.bashrc 
echo "		toilet -f \$toilet_font \"Text\"" >> $user/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 4 )) -eq 2 ]; then" >> $user/.bashrc 
echo "		toilet -f \$toilet_font -F border \"Text\"" >> $user/.bashrc 
echo "	elif [ \$(( \$RANDOM1 % 4 )) -eq 3 ]; then" >> $user/.bashrc 
echo "		toilet -F metal	-f \$toilet_font" >> $user/.bashrc 
echo "	fi " >> $user/.bashrc 
echo "fi" >> $user/.bashrc 
echo "disown -a" >> $user/.bashrc 
cd ../../
