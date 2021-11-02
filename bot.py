import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f'目前登入身份：{client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '嗨':
        await message.channel.send('你好呀')
    if message.content == '我是你爹':
        await message.channel.send('我是你儿子')

client.run('Your Token')#Write your Token here
