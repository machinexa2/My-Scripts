#!/usr/bin/python3

import discord
import asyncio

from requests import get
from random import randrange
from os import getenv as os_getenv
from bs4 import BeautifulSoup
from datetime import datetime
from humanize import intcomma

from lib.Globals import discord_server as myserver

stonedbot_token = os_getenv('STONEDBOT_ACCESS_TOKEN')
if not stonedbot_token:
    print("Token not found")
    exit()

def percentage(a, b):
    try:
        return abs(((b - a) / b) * 100)
    except ZeroDivisionError:
        return 0

def fetch_pulls(url):
    response = BeautifulSoup(get(url).text, "html.parser")
    for resp in response.find_all("span", {"data-content": "Pull requests"}):
        for sibling in resp.next_siblings:
            if not sibling or sibling == '\n':
                continue
            open_pr =  f"{sibling['title']}"
    for resp in response.find_all("a", {"data-ga-click": "Pull Requests, Table state, Closed"}):
        closed = str(resp).split('</path></svg>')[-1].strip(' ').split('Closed')[0].strip('\n').strip(' ')
        break
    return int(open_pr.replace(',', '')), int(closed.replace(',', ''))

def fetch_corona():
    response = BeautifulSoup(get("https://www.worldometers.info/coronavirus/").text, 'html.parser')
    i, d = tuple(filter(lambda s: ',' in s, response.find_all('title')[0].text.lower().split(':')[-1].strip(' ').split('from')[0].strip(' ').split(' ')))
    return int(i.replace(',', '')), int(d.replace(',', ''))

class BotClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop.create_task(self.publish_corona())
        self.loop.create_task(self.publish_personal())

    async def on_ready(self):
        #server = discord.utils.find(lambda g: g.name == myserver, client.guilds)
        #print(f"My Server: {server.name}({server.id})")
        print(f'Logged in as: {self.user.name}({self.user.id})')

    async def publish_corona(self):
        await self.wait_until_ready()
        channel = self.get_channel(790767464229109811)
        while True:
            infection, death = fetch_corona()
            send_string = f"**SARS-CoV-2 Status** ({datetime.now().strftime('%B %d %Y %H:%M:%S')})\n"
            send_string += f"Infection: {intcomma(infection)}\nDeath: {intcomma(death)}\n"
            await channel.send(send_string)
            await asyncio.sleep(randrange(86400))

    async def publish_personal(self):
        await self.wait_until_ready()
        channel = self.get_channel(803301891772907552)
        repositories = ("python/CPython", "golang/Go", "nuitka/nuitka")
        while True:
            for _ in repositories:
                active, closed = fetch_pulls(f"https://github.com/{_}/pulls")
                send_string = f"**{_.split('/')[-1]}**: \nActive: {intcomma(active)} :white_check_mark:, Total: {intcomma(active + closed)} :skull_crossbones:\n"
                await channel.send(send_string)
            await asyncio.sleep(randrange(86400))
client = BotClient()
client.run(stonedbot_token)
