#!/bin/bash
##############################################################
# Program name: NCAA FOOTBALL Stats Scraper
# Version: 1.0
# By: Sean Middleton
# License: MPL 2.0 (see LICENSE file in root folder)
# Additional thanks: 
# Usage: Edit the settings file (scraper_Ncaa_setting.py) and simply run this script
##############################################################

# No editing is required here
python create_team_mappings.py
python create_schedule_mappings.py
python create_player_mappings_and_agg_stats.py
python create_ind_stats.py
