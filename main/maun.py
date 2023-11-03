import discord
from discord.ext import commands
import openai

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def gpt(v):
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Ты бот, который следит за экологией и переживаешь за окружающий мир, когда тебе задают вопрос, ты отвечаешь на него с уклоконом в экологию, вот такой вопрос - '{v}'"}
        ])
    
    return completion.choices[0].message.content



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    t = gpt(message.content).split('.')
    for x in t:
        await message.channel.send(x)


client.run("MTE2MDE1MzM4MDQ2ODAzMTUyMA.GbWey9.n4M9DVek8hmr5TC0iCkVtFzVHSx1QoSE4MUhRA")
