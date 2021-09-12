# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing permissions and limitations under the
# License.

# FROM ubuntu:latest

FROM python:3.8

#####################
### initial setup ###
#####################

# Adding trusting keys to apt for repositories
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Install Cron so we can set up a cron job
RUN apt-get install -y cron

RUN apt install -y python3-pip

# Magic happens
# RUN apt-get install -y google-chrome-stable
# RUN apt install -y chromium-browser
RUN apt-get install chromium -y 
#debian based image


# Installing Unzip
# RUN apt-get install -yqq unzip
RUN apt-get install -yqq unzip curl


# Download the Chrome Driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_90`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable
ENV DISPLAY=:99

#####################
### app install ###
#####################
RUN mkdir app
COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip

RUN echo "Getting list of location"
RUN ls

RUN pip3 install -r /app/requirements.txt

# CMD ["python", "./app.py"]

######
### Setup Cron job ###
#####
RUN chmod +x /app/cron_execute.sh
#create the cron job to run every minute
RUN crontab -l | { cat; echo "* * * * * python3 /app/main.py"; } | crontab -
# RUN crontab -l | { cat; echo "* * * * * echo hello > /app/hello.txt"; } | crontab -
#start the service 
RUN service cron start


RUN echo "setup complete. Launched scraper"