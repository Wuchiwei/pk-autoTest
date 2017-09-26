#!/bin/bash
cd registe_userid
sh  registe_userid.sh
cd ..
cd registe_passwd
sh  registe_passwd.sh
cd ..
cd registe_agn_passwd
sh  registe_agn_passwd.sh
cd ..
cd registe_phone_nub
sh  registe_phone_nub.sh
cd ..
python registe_seccs.py
cd ..
