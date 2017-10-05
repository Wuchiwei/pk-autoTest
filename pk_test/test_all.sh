#!/bin/bash
cd registe
sh registe.sh
cd ..
cd login
sh login.sh
cd ..
cd livehome
sh livehome.sh
cd ..

cd ..
cd import
rm -rf ./*.pyc

cd ..
cd pk_test
