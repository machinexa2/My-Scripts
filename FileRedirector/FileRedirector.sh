if [ $# -eq 1 ]; then
	cat pypy | sed s/^/"echo \""/g | sed s/$/"\" >> somepath_i_dont_know "/g >> $1
	rm pypy 2>/dev/null
elif [ $# -eq 2 ]; then
	cat pypy | sed s/^/"echo \""/g | sed s/$/"\" >> "/g > pypy2
	cat pypy2 | while read line; do
		echo "$line" "$2" >> $1
	done
	rm pypy2 2>/dev/null
	rm pypy 2>/dev/null
else
	echo  "PYTHON ERROR"
fi
