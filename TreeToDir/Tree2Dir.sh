path_=""
lsdata="`ls -l | awk -F ' ' '{print $9}'`"
for ls in $lsdata; do
	abs_path="`echo "$path_""$ls"`"
	echo $abs_path 
	data="`cat $abs_path | awk -F '--' '{print $2}' | cut -d ' ' -f 2 | head -n 5`"
	if [[ $data  == "" ]]; then
		data="`cat drupal.txt | awk -F "──" '{print $2}'`"
		echo "$data" | sort -u | tr ' ' ':'  | sed s/':'/''/g | cut -d '.' -f 1 | tee -a /tmp/tree2dir
	else
		echo "$data" | sort -u | cut -d '.' -f 1 | sort -u | tee -a /tmp/tree2dir

	fi
	sleep 0.3
done
