from secret_stuff import bot_token, bot_prefix, bot_testing_channel_id

import discord
import asyncio

from common_funcs import reply
from bot_commands import commands_list
from bot_commands import command_test, command_help, command_countdown
from bot_commands import command_say

class MyClient(discord.Client):
    
    async def on_ready(self):
        
        print('Logged on as', self.user)
        bot_testing_channel = client.get_channel(bot_testing_channel_id)
        await bot_testing_channel.send('**Police Back On Duty**')

    async def on_message(self, message):
        
        if message.author == self.user:
            return # ignore own messages

        if type(message.channel) is discord.DMChannel:
            await message.channel.send("I don't work with DMs")
            return

        if type(message.channel) is discord.GroupChannel:
            await message.channel.send("I don't work with GDMs")
            return

        if message.content.lower().startswith(bot_prefix):
            await message.add_reaction('\U0001F46E')
            await parse_input(message)


async def parse_input(user_message):
    
    input = user_message.content.lower().split()
    if input[0] != bot_prefix:
        await reply(user_message, 'My prefix is **' + bot_prefix + '**, not ' + str(input[0]))
        return
        
    if len(input) == 1:
        await reply(user_message, '**' + bot_prefix + '** is my prefix, gimme a command')
        return
    
    input_command = input[1].lower()
    for command in commands_list:
        if input_command == command:
            await commands_list[command](user_message)
            return

    await reply(user_message, 'Invalid Command! Type **' + bot_prefix + 'help** for list'
                               ' of commands/')


client = MyClient()
client.run(bot_token)