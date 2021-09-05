from os import close
import discord
import json
from discord.enums import ChannelType
import os

# token file looks like this
# with open("/Users/adam/development/ps5-stock-selector-config/.discordtoken", 'r') as dst:
#     dctkn_json = json.load(dst)

def get_discord_env_var():
    return os.environ.get('DISCORD_BOT_TOKEN', 'Specified environment variable for the discord bot is not set.')

# test channel: 883611785968648203

mytoken = get_discord_env_var()

def notify_discord(discord_message):
    """ will send a message to a channel the bot is part of"""
    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as {0}!'.format(self.user))
            for guild in self.guilds:
                for channel in guild.channels:
                    if str(channel.type) == 'text':
                        print(channel.id, channel.type)
                        mychannel = await client.fetch_channel( channel.id )
                        await mychannel.send(str(discord_message))                    
            await client.close()


    client = MyClient()
    client.run(mytoken)

# notify_discord("attempting to message all subscribed channels")
