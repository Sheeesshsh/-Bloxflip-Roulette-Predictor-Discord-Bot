```from time import sleep

import discord

from discord import app_commands 

import cloudscraper as cs

class aclient(discord.Client):

    def __init__(self):

        super().__init__(intents = discord.Intents.default())

        self.synced = False

    async def on_ready(self):

        await self.wait_until_ready()

        if not self.synced:

            await tree.sync()

            self.synced = True

        print(f"We have logged in as {self.user}.")

client = aclient()

tree = app_commands.CommandTree(client)

scraper = cs.create_scraper()

@tree.command( name = 'roulette', description='roulette predictor') 

async def slash2(interaction: discord.Interaction):

    try:

        a = scraper.get('https://api.bloxflip.com/games/roulette').json()['history'][0]['winningColor']

        b = scraper.get('https://api.bloxflip.com/games/roulette').json()['history'][1]['winningColor']

        c = scraper.get('https://api.bloxflip.com/games/roulette').json()['history'][2]['winningColor']

        past_Games = a,b,c

        print(past_Games)

        rCount = past_Games.count("red")

        pCount = past_Games.count("purple")

        rChance = 100 - (rCount * 25)

        pChance = 100 - (pCount * 25)

        if rChance == 100:

            rChance -= 10

        elif pChance == 100:

            pChance -= 10

        print(f"Red {rChance}")

        print(f"Purple {pChance}")

        if rChance > pChance:

            em = discord.Embed(title=f'Prediction: Red\nChance: {rChance}%', color=0xff3525)

            await interaction.response.send_message(embed=em)

        elif pChance > rChance:

            em = discord.Embed(title=f'Prediction: Purple\nChance: {pChance}%', color=0x9900ff)

            await interaction.response.send_message(embed=em)

    except:

        await interaction.response.send_message("Failed to send request try command again")

client.run('MTAzNTUxMzg1OTc3MzAzODY1Mw.GoWdTA.v1oyHeIMkD9LWx1NauO2HYsOsbW-hg6DgigOTU')
