#!/bin/sh
windows=Emage1234
linux=dustinbackendpu
# file log for windows server
sshpass -p $windows scp -P 25 dustin@viws.ddns.net:C:/Users/dustin/Desktop/monitoring/*.log ./windows

# create list of user
sshpass -p $linux ssh -oStrictHostKeyChecking=no -oCheckHostIP=no dustin@viws.ddns.net "cd ~/Desktop/server && ./getList.sh"
sshpass -p $linux scp -P 24 dustin@viws.ddns.net:/home/dustin/Desktop/server/*.log ./runcode/Userlist
# file log for emageAI server
sshpass -p $linux scp -P 24 dustin@viws.ddns.net:/home/dustin/Desktop/server/report_c_g_pu/*.log ./viralint
# file log for emage server
# scp dustin@viws.ddns.net:/home/dustin/monitoring/*.log ./emage
# create list of user
sshpass -p $linux ssh -oStrictHostKeyChecking=no -oCheckHostIP=no dustin@emagevision.ddns.net "cd /home/dustin && ./getList.sh"
sshpass -p $linux scp dustin@emagevision.ddns.net:/home/dustin/*.log ./runcode/Userlist
# file log for emage vision server
sshpass -p $linux scp dustin@emagevision.ddns.net:/home/dustin/report/*.log ./emagevision
sshpass -p $linux scp dustin@emagevision.ddns.net:/home/dustin/report/result/*.log ./emagevision