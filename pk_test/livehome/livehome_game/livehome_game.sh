#!/bin/bash
cd function_game
python signout.py
python game_ordinary_chpage.py
cd ..

cd game_ordinary
sh game_ordinary.sh
cd ..

cd latest_game_ordinary
sh latest_game_ordinary.sh
cd ..

cd sort_game_ordinary
sh sort_game_ordinary.sh
cd ..

cd game_anchor
sh game_anchor.sh
cd ..
