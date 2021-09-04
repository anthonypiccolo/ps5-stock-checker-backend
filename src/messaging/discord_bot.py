from os import close
import discord
from discordtoken import token as discordtoken

# token file looks like this
# token = "xxxxxtokenherexxxxxx"


mytoken = discordtoken
import discord



import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        channel = await client.fetch_channel('883611786547441746')   #the test channel
        await channel.send('Ps5 stock found in XYZ')
        await client.close()

    # async def auto_send():
    #     channel = await client.fetch_channel('883611785968648203')
    #     await channel.send('GOOD MORNING!')

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
# client.run('my token goes here')

client.run(discordtoken)
# client.auto_send()
# client.close()











# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as', self.user)

#     async def on_message(self, message):
#         # don't respond to ourselves
#         if message.author == self.user:
#             return

#         if message.content == 'ping':
#             await message.channel.send('pong')

# client = MyClient()
# client.run("ODgzNTk3NjU2NTkxNTg1Mjkw.YTMQcQ.2N5UuE7e6tHtNNVI0JZ2BPoc6C8")

# bot.run('ODgzNTk3NjU2NTkxNTg1Mjkw.YTMQcQ.2N5UuE7e6tHtNNVI0JZ2BPoc6C8')
