#!/bin/bash

now=$(date)
echo "$now" >> test_runtime.text

cd registe
sh registe.sh
cd ..
cd login
sh login.sh
cd ..
cd livehome
sh livehome.sh
cd ..

now=$(date)
echo "\n$now" >> test_runtime.text

cd ..
cd import
rm -rf ./*.pyc

cd ..
cd pk_test
