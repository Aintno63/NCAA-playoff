#!/usr/bin/python
##############################################################
# Program name: NCAA FOOTBALL Stats Scraper (Team Mappings Module)
# Version: 1.0
# By: Sean Middleton
# License: MPL 2.0 (see LICENSE file in root folder)
# Additional thanks: 
##############################################################

# Import modules and libraries
import scraper_Ncaa_functions
import scraper_Ncaa_settings
from bs4 import BeautifulSoup

if (scraper_Ncaa_setting.map_teams == 1):
    print "Generating team mappings"
    # Create the file headings
    team_mappingfile_w = open(scraper_Ncaa_settings.team_mappingfile, "w")
    team_mappingfile_w.writelines("team_id\tteam_name\tteam_url\n")

    # Grab data
    # Download the page with the list of teams
    teamlist_data = scraper_Ncaa_functions.grabber(scraper_Ncaa_settings.start_url, scraper_Ncaa_settings.params, scraper_Ncaa_settings.http_header) # Get data from main page
    teamlist_data_soup = BeautifulSoup(teamlist_data) # Soupify that data

    # Create a mapping for teams
    for link in teamlist_data_soup.find_all('a'): # For each hyperlink on the page
        if "team/index/" + str(scraper_Ncaa_settings.year_index) + "?org_id=" in link.get('href'): # If the hyperlink contains this string (limiting it only to team pages)
            team_id = str(link.get('href').split("team/index/" + str(scraper_Ncaa_settings.year_index) + "?org_id=")[1]) # Get the team ID from the URL
            team_name = str(link.get_text()) # Get the text associated with the hyperlink
            team_url = str(scraper_NCaa_settings.domain_base + link.get('href')) # Get the URL and append the base domain
            team_mappingfile_w.writelines(str(team_id) + "\t" + str(team_name) + "\t" + str(team_url) + "\n") # Add lines to our TSV file for archival purposes
    print "Successfully generated team mappings"
