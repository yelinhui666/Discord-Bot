import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f'目前登入身份：{client.user}')


@client.event
async def on_message(message):
    # Ignore your own information, prevent endless loops
    if message.author == client.user:
        return

    # Simple auto reply
    if message.content == '嗨':
        await message.channel.send('你好呀')
    if message.content == '我是你爹':
        await message.channel.send('我是你儿子')
    if message.content == '1':
        await message.channel.send('2')
    if message.content == 'Urgot':
        await message.channel.send('You cannot know strength... Until you are broken')

    if message.content.startswith("say"):
        tmp = message.content.split(" ", 1)
        if len(tmp) == 1:
            await message.channel.send(f"{message.author.mention} 你要我說什麼啦？")
        else:
            await message.channel.send(f"{message.author.mention} 他逼得我說「{tmp[1]}」")


client.run('your token')  # Write your Token here
