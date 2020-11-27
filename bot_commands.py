from secret_stuff import bot_prefix
from common_funcs import reply
import asyncio

async def command_test(user_message):
    await reply(user_message, 'not implemented')
    return

async def command_help(user_message):

    output = 'currently available:'

    counter = 1
    for command in commands_list:
        output += '\n**' + str(counter) + ')** ' + command
        counter += 1

    await reply(user_message, output)
        
    return

async def command_countdown(user_message):
    # message.content of form "<bot_prefix> countdown ..."
    # where ... can be anything
    # expected: "<bot_prefix> countdown [duration belongs [0, 60]]"

    input = user_message.content.lower().split()

    if len(input) != 3:
        await reply(user_message, 'Invalid number of Arguments. Type **' + bot_prefix + 'help countdown** for syntax')
        return

    if not input[2].isnumeric():
        await reply(user_message, 'Duration must be a positive integer')
        return

    duration = int(input[2])

    if (duration > 60 or duration < 1):
        await reply(user_message, 'Duration must belong to [0, 60]')
        return

    await reply(user_message, 'Countdown Started!')
    countdown_message = await user_message.channel.send(user_message.author.mention + ' Seconds Left: ' + str(duration))

    for i in range(duration-1):
        await countdown_message.edit(content = user_message.author.mention + ' Seconds Left: ' + str(duration-i-1))
        await asyncio.sleep(1)

    await reply(user_message, 'Countdown Over!')    


async def command_say(user_message):
    await user_message.channel.send(user_message.content[len(bot_prefix + ' say'):].lstrip())

    
commands_list = { 'test' : command_test, 'help' : command_help,
                    'countdown' : command_countdown, 'say' : command_say }