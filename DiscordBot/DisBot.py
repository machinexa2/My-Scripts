#!/usr/bin/python3

import discord
import asyncio
import os

from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
from humanize import intcomma

from lib.Globals import discord_server as myserver

stonedbot_token = os.getenv('STONEDBOT_ACCESS_TOKEN')
if not stonedbot_token:
    print("Token not found")
    exit()

class BotClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.corona = "https://www.worldometers.info/coronavirus/"
        self.bg_task = self.loop.create_task(self.publish_corona())

    async def on_ready(self):
        print(f"{client.user} is connected to Discord")
        myguild = discord.utils.find(lambda g: g.name == myserver, client.guilds)
        print(f'Logged in as: {self.user.name}({self.user.id})')
        print(f"My Server: {myguild.name}({myguild.id})")

    async def publish_corona(self):
        await self.wait_until_ready()
        corona_channel = self.get_channel(790767464229109811)
        while not self.is_closed():
            infection, death = self.fetch_corona()
            curdate = datetime.now().strftime("%B %d %Y")
            send_string = f"**SARS-CoV-2 Status** ({datetime.now().strftime('%B %d %Y %H:%M:%S')})\n"
            send_string += f"Infection: {intcomma(infection)}\nDeath: {intcomma(death)}\n"
            await corona_channel.send(send_string)
            self.previous_infection, self.previous_death = infection, death
            await asyncio.sleep(15500)

    def fetch_corona(self):
        response = get(self.corona)
        parsed_response = BeautifulSoup(response.text, 'html.parser')
        infection, death = tuple(filter(lambda string: ',' in string, parsed_response.find_all('title')[0].text.lower().split(':')[-1].strip(' ').split('from')[0].strip(' ').split(' ')))
        return int(infection.replace(',', '')), int(death.replace(',', ''))

client = BotClient()
client.run(stonedbot_token)
