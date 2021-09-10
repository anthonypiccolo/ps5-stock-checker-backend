#! /bin/bash
# use this for deploying to a vanilla VM without docker

#####################
### initial setup ###
#####################

#lets run this on an ubuntu 18.04 instance because python is already installed 

# Updating apt to see and install Google Chrome
apt-get -y update

# installing git, python, pip
apt-get install -y git
python3 --version
apt install -y python-pip
# apt install python3.8 #already installed on ubuntu 18.04


# Adding trusting keys to apt for repositories
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - 

# Adding Google Chrome to the repositories
# sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Install Cron so we can set up a cron job
apt-get install -y cron

# Magic happens
# apt-get install -y google-chrome-stable #does not work
apt-get install -y chromium-browser #does work

# Installing Unzip
# RUN apt-get install -yqq unzip
apt-get install -yqq unzip curl


# Download the Chrome Driver - this isn't working
# wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
# unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable
# ENV DISPLAY=:99

#####################
### app install ###
#####################
mkdir /app

#clone into /app

#git clone https://github.com/anthonypiccolo/ps5-stock-checker-backend /app
git clone --branch VM_cloudcompute https://github.com/anthonypiccolo/ps5-stock-checker-backend/tree/VM_cloudcompute /app

apt install -y python3-pip

pip3 install --upgrade pip
pip3 install -r /app/requirements.txt



######
### Setup Cron job ###
#####

python3 /app/src/install_chromium.py

#create the cron job to run every minute
crontab -l | { cat; echo "* * * * * python /app/main.py"; } | crontab -
# RUN crontab -l | { cat; echo "* * * * * echo hello > /app/hello.txt"; } | crontab -
#start the service 
service cron start


echo "setup complete. Launched scraper"