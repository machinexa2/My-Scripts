# Link scripts
addbinary(){ chmod +x `pwd`"/""$1" && ln -nsf `pwd`"/""$1" /root/MachineYadav/My-Tools/MyBinaries/$2; }
cat PYLINK | while read linkapp
do
	(cd "$linkapp" && addbinary "$linkapp"".py" "$linkapp")
done
