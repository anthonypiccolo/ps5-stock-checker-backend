# ps5-stock-checker-backend
Scraping PS5 stock level data from major retailers

We're hosting with Firebase because we want to be able to interact with buckets without much fuss as part of the fundamental website. We'll also be using bigquery for analytics on this. 

Services: 
- GCP/Firebas CloudStorage: Storing our stuff
- Firebase Hosting with GatsbyJs for react frontend
- Firebase Cloud Functions for execution

## Environment variables

Environment variables are stored in fireh


## Messaging Connectors

This script will message multiple locations.

- Discord (done)
- Slack (not done)
- email (not done)
- twitter (not done)

### Disord

The discord bot is built in python and utlizes discord.py which is a wrapper currently in the process of being sunset. ETA for the sunset is ~2022 sometime. Ye be warned. 

Basically, it activates a bot and the bot will post a message to all channels it's part of. 

setup details I found useful: 
- https://discordpy.readthedocs.io/en/latest/discord.html - bot setup
- https://discord.com/developers/ - set up a developer team
- discord package - https://github.com/Rapptz/discord.py