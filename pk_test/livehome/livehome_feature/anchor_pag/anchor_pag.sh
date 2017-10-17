#!/bin/bash
cd function
python clean_follow.py
cd ..

cd anchor_popular
sh popular_anchor.sh
cd ..

cd function
python clean_follow.py
cd ..

cd anchor_list
sh list_anchor.sh
cd ..
