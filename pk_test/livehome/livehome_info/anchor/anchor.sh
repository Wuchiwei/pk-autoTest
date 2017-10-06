#!/bin/bash
cd anchor_info
sh anchor_info.sh
cd ..
cd anchor_income
sh anchor_income.sh
cd ..
cd anchor_otherset
sh anchor_otherset.sh
cd ..
python anchor_signout.py
