NCAA FOOTBALL STATS SCRAPER 
=============================
(http://espn.go.com/college-football/)
Python scraper for <@espn.com>  that collects ncaa game data from game logs and writes to csv. At the end of the code you can plug in your path, season, and team or teams you want to scrape for. It takes about 3 - 4 minutes to scrape for each season/team combinaiton. It returns about 8 - 9 thousand rows.

=============================
Author: Sean Middleton  
Version: 1.0


Usage
-----
First, edit the scraper settings in `scrapersettings.py`. In particular, be sure to change the two variables at the top, `academic_year` and `year_index`, using the information provided in that file. You can also set what kind of data you'd like saved, and where you'd like it saved.

Then, execute either `ncaab_stats_scraper.sh` or `ncaab_stats_scraper.bat`, depending on your operating system. Alternatively, you can just execute the python files, preferably in this order:

1. create_team_mappings.py
2. create_schedule_mappings.py
3. create_player_mappings_and_agg_stats.py
4. create_ind_stats.py


Requirements
------------
This script requires Python, as well as the urllib2 and BeautifulSoup libraries.


License
--------
This script is licensed under the Mozilla Public License Version 2.0 (see LICENSE file in root folder). TL;DR: feel free to use it commercially, modify it, and distribute it, provided you disclose both the source code and any modifications you make to it.


