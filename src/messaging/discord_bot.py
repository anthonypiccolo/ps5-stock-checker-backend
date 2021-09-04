from os import close
import discord
from discord.enums import ChannelType
from discordtoken import token as dctkn

# token file looks like this
# token = "xxxxxtokenherexxxxxx"

# test channel: 883611785968648203

mytoken = dctkn

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
    client.run(dctkn)

notify_discord("attempting to message all subscribed channels")
