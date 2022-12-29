import json
import time
import discord
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def sellp(ctx):
    channel = bot.get_channel(1054813117592371322)   

    post = {}
    posting = []
    while True:
        
        with open('dico.json', 'r') as dicojson:
            sell=json.load(dicojson)
               
        
        for paire in sell:
            post = sell[paire]['url']
            if post in posting:
                print("rr")
                continue
            else:
                embed=discord.Embed(title=f"👟**__{paire}__**", url=sell[paire]['url'],color=discord.Color.blue())
                embed.set_author(name=sell[paire]['shop'], url="",icon_url="")
                embed.add_field(name="``prix``", value=sell[paire]['prix'], inline=True)
                embed.add_field(name="``prix-reduit``", value=sell[paire]['prixreduit'], inline=True)
                embed.add_field(name="``code-promo``", value=sell[paire]['code'], inline=True)
                embed.set_thumbnail(url=sell[paire]['image'])
                embed.set_footer(text=f"by citr//",icon_url="https://pbs.twimg.com/profile_images/1606253758589161472/Q2pIZAM-_400x400.jpg")
                print("nouvel item")
                posting.append(post)
                await channel.send(embed=embed)







bot.run("NzA3MTg5NTcyNTU5MTc1NzEw.GpEZVX.xjKTLhbKkGm5N2HrurdNi4DHUU2R-cNHMEtwME")
