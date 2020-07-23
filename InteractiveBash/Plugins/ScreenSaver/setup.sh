current_pwd="`pwd`"

sudo apt-get install libcurses-perl xprintidle -y
cd /tmp && wget http://search.cpan.org/CPAN/authors/id/K/KB/KBAUCOM/Term-Animation-2.4.tar.gz && tar -zxvf Term-Animation-2.4.tar.gz
cd Term-Animation-*/ && sudo perl Makefile.PL && sudo make && sudo make test && sudo make install
cd /tmp && wget http://www.robobunny.com/projects/asciiquarium/asciiquarium.tar.gz && tar -zxvf asciiquarium.tar.gz
cd asciiquarium_*/ && sudo cp asciiquarium /usr/local/bin && sudo chmod 0755 /usr/local/bin/asciiquarium

cd "$current_pwd"

user="`whoami`"
if [[ $user != "root" ]]; then
        user="/home/`whoami`"
else
        user="/root"
fi

cd Plugins/ScreenSaver
echo "FILE="/tmp/interactive_screen_count"" >> $user/.bashrc
echo "if [[ -f /tmp/interactive_screen_count ]]; then" >> $user/.bashrc
echo "	if [[ \$(cat \$FILE 2>/dev/null) -gt 10 ]]; then" >> $user/.bashrc
echo "		rm /tmp/interactive_screen_count 2>/dev/null" >> $user/.bashrc
echo "		asciiquarium" >> $user/.bashrc
echo "	fi" >> $user/.bashrc
echo "	if [[ \$(cat \$FILE 2>/dev/null) -le 10 ]]; then" >> $user/.bashrc
echo "		sec_data=\$(cat \$FILE)" >> $user/.bashrc
echo "		rm /tmp/interactive_screen_count 2>/dev/null" >> $user/.bashrc
echo "		sec_data=\$(( \$sec_data + 1 ))" >> $user/.bashrc
echo "		echo "\$sec_data" > /tmp/interactive_screen_count" >> $user/.bashrc
echo "		" >> $user/.bashrc
echo "	fi" >> $user/.bashrc
echo "" >> $user/.bashrc
echo "else" >> $user/.bashrc
echo "	echo "0" > /tmp/interactive_screen_count" >> $user/.bashrc
echo "fi" >> $user/.bashrc
cd ../../
