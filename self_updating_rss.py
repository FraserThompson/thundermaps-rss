#!/usr/bin/env python
# Used to update Thundermaps with ISS sightings from NASA's spot the station.

import updater

# Key, account, categories...
THUNDERMAPS_API_KEY = "03a01ba4d1d3c60feec7fe7a4cc832b6"
THUNDERMAPS_ACCOUNT_ID = ""
RSS_FEED_URL = 'http://spotthestation.nasa.gov/sightings/xml_files/New_Zealand_None_Wellington.xml'

# Create updater
nasa_updater = updater.Updater(THUNDERMAPS_API_KEY, THUNDERMAPS_ACCOUNT_ID, RSS_FEED_URL)

# Start updating
nasa_updater.start()
