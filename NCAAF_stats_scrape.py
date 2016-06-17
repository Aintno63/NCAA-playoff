#!/bin/bash 
############################################################## 
# Program name: NCAA Basketball Stats Scraper 

# Usage: Edit the settings file (scrapersettings.py) and simply run this script
##############################################################

# No editing is required here
python create_team_mappings.py
python create_schedule_mappings.py
python create_player_mappings_and_agg_stats.py
python create_ind_stats.py
