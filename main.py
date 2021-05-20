from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import threading
import discord
import os
from discord.ext import commands, tasks


myurl = 'https://finance.yahoo.com/quote/DOGE-USD/'
uClient = uReq(myurl)
page_html = uClient.read()
page_soup = soup(page_html, "html.parser")

container = page_soup.findAll("span", {"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
close_price = [entry.text for entry in page_soup.find_all('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})]
print(close_price)

def printprice():
    threading.Timer(2, printprice).start()
    print(close_price)


TOKEN = 'ODQ0OTY4NjE4ODI3ODQxNTc5.YKaIWQ.DUOTakg7UjJ4Jl7GCRs1DpZHXZA'

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'price':
        myurl = 'https://finance.yahoo.com/quote/DOGE-USD/'
        uClient = uReq(myurl)
        page_html = uClient.read()
        page_soup = soup(page_html, "html.parser")

        container = page_soup.findAll("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
        close_price = [entry.text for entry in page_soup.find_all('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})]
        channel = client.get_channel(844976720779935795)
        await channel.send(close_price)

client.run(TOKEN)








