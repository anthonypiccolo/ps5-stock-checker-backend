# ps5-stock-checker-backend
Scraping PS5 stock level data from major retailers

We're hosting with Firebase because we want to be able to interact with buckets without much fuss as part of the fundamental website. We'll also be using bigquery for analytics on this. 

Services: 
- GCP/Firebas CloudStorage: Storing our stuff
- Firebase Hosting with GatsbyJs for react frontend
- Firebase Cloud Functions for execution



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
- https://github.com/Rapptz/discord.py - discord package
- https://disbotgen.zaytunhub.com/ discord bot invide link builder


## Environment Variables

### locally

when running locally, you'll need to create a `.env` file in your project root. 
You can paste the following in:

```
# environment variables defined inside a .env file
# use this as a template and put it in your root directory as a .env

FIRESTORE_PROJECT_ID=<firestore project name here>
GOOGLE_APPLICATION_CREDENTIALS=<credentials here>

# messaging specific

DISCORD_BOT_TOKEN=<discord bot token here> 
```

### in GCP

if we're using GCP cloudfunctions, you can add the the environment variables when deploying the instance via the console. 

_NOTE_ There's probably a way to do this via the cli. We should look into this.

## To launch locally via Docker

```bash
#build the image from a Dockerfile
docker build -t ps5-stock-checker .

```


### startup

compatibility matrix for selenium
https://support.leapwork.com/hc/en-us/articles/360004941392-Web-Browser-and-Driver-Compatibility-Matrix-LEAPWORK

### Via vanilla VM startup script

uses cron jobs to fire off a job every minute

#### Useful Cron commands 

Create new cron job without nano:

```
crontab -l | { cat; echo "* * * * * /app/cron_execute.sh >> /app/out.txt  2>&1"; } | crontab -
```
```
* * * * * = cron scehdule (eg every minute here)
/app/cron_execute.sh = path to script
>> = pipe output
/app/out.txt = where to pipe the output
2>&1 = capture stderr and stdout

```

Delete all cron jobs 
```
crontab -r
```

Review cron logs for execution history
```
grep CRON /var/log/syslog
```