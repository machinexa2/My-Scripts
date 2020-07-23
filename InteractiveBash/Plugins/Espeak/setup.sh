cd Plugins/Espeak
apt install espeak -y
user="`whoami`"
cronfile="/var/spool/cron/crontabs/""$user"

if [[ $user != "root" ]]; then
        user="/home/`whoami`"
else
        user="/root"
fi

echo "*/25	*/4	*	*	*	\`echo \$(curl https://thesimpsonsquoteapi.glitch.me/quotes) | gron | grep quote | cut -d '=' -f 2 | cut -d '\"' -f 2 | espeak\`" >> $cronfile 
cd ../../
