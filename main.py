import re
import pandas as pd
import json
import os
import requests
from discord.ext import commands
import discord
TOKEN = 'TOKE HERE'
# TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix="dc!")
html = requests.get('https://www.worldometers.info/coronavirus/').text
html = re.sub(r'<.*?>', lambda g: g.group(0).upper(), html)
df = pd.read_html(html)
js = df[0].to_json()
js = json.loads(js)
from ka import keepalive

common_symp = ['fever',
                'dry cough',
                'tiredness']
less_symp = [
    'aches and pains'
    'sore throat',
    'diarrhoea',
    'conjunctivitis',
    'headache',
    'loss of taste or smell',
    'a rash on skin, or discolouration of fingers or toes']

client.remove_command("help")


@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Covid Cases on {len(client.guilds)} servers | dc!help"))


@client.command()
async def hello(ctx):
    await ctx.channel.send(f"Hello! {ctx.author.mention}")


@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(
        title="DisCovid Help", description="Type dc!help <command> for more info on a command.", color=0x800000)
    embed.add_field(name="Covid", value="dc!help Covid", inline=True)
    embed.add_field(name="Symptoms", value="dc!help Symptoms", inline=False)
    embed.add_field(name="ActiveCases", value="dc!help ActiveCases", inline=False)
    embed.add_field(name="TotalDeaths", value="dc!help TotalDeaths", inline=False)
    embed.add_field(name="TotalCases", value="dc!help TotalCases", inline=False)
    embed.add_field(name="TotalRecovered", value="dc!help TotalRecovered", inline=False)
    embed.set_footer(
        text="Suggestions? Go to https://bit.ly/3dGGNzd and Submit your Suggestion :D")
    await ctx.send(embed=embed)


@help.command()
async def Covid(ctx):
    embed = discord.Embed(
        title="Covid", description="What is Covid 19", color=0x800000)
    embed.add_field(name="Syntax", value="dc!Covid", inline=True)
    await ctx.send(embed=embed)


@help.command()
async def ActiveCases(ctx):
    embed = discord.Embed(title="ActiveCases",
                          description="Total Active Cases", color=0x800000)
    embed.add_field(name="Syntax", value="dc!ActiveCases", inline=True)
    await ctx.send(embed=embed)


@help.command()
async def TotalDeaths(ctx):
    embed = discord.Embed(
        title="TotalDeaths", description="Total Deaths Due To Covid", color=0x800000)
    embed.add_field(name="Syntax", value="dc!TotalDeaths", inline=True)
    await ctx.send(embed=embed)


@help.command()
async def TotalCases(ctx):
    embed = discord.Embed(title="TotalCases",
                          description="Total Covid Cases", color=0x800000)
    embed.add_field(name="Syntax", value="dc!TotalCases", inline=True)
    await ctx.send(embed=embed)


@help.command()
async def TotalRecovered(ctx):
    embed = discord.Embed(title="TotalRecovered",
                          description="Total Recovered Cases", color=0x800000)
    embed.add_field(name="Syntax", value="dc!TotalRecovered", inline=True)
    await ctx.send(embed=embed)

@help.command()
async def Symptoms(ctx):
    embed = discord.Embed(title = "Symptoms", description='Symptoms of Covid 19', color=0x800000)
    embed.add_field(name="Syntax", value="dc!Symptoms", inline=True)
    await ctx.send(embed=embed)
    
@client.command()
async def Covid(ctx):
    embed = discord.Embed(title="Covid", color=0x800000)
    embed.set_thumbnail(
        url="https://www.fda.gov/files/Coronavirus_3D_illustration_by_CDC_1600x900.png")
    embed.add_field(name="What is Covid", value="Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. \nMost people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment. \nHOW IT SPREADS \nThe virus that causes COVID-19 is mainly transmitted through droplets generated when an infected person coughs, sneezes, or exhales. These droplets are too heavy to hang in the air, and quickly fall on floors or surfaces. You can be infected by breathing in the virus if you are within close proximity of someone who has COVID-19, or by touching a contaminated surface and then your eyes, nose or mouth.", inline=True)
    embed.set_footer(text="source https://bit.ly/3t1XFHa")
    await ctx.send(embed=embed)


@client.command(aliases=['total', 'TotalCases'])
async def totalcases(ctx):
    embed = discord.Embed(title="Total Covid Cases", url="https://www.worldometers.info/coronavirus/",
                          description="Total covid cases in the whole world, All continents and top 10 countries", color=0xa30000)
    embed.set_thumbnail(
        url="https://www.fda.gov/files/Coronavirus_3D_illustration_by_CDC_1600x900.png")
    embed.add_field(name="World", value=js["TotalCases"]["7"], inline=False)
    embed.add_field(name="Continents", value='5 Continents', inline=False)
    for i in range(5):
        embed.add_field(name=js["Country,Other"][str(i+1)],
                        value=js["TotalCases"][str(i+1)])
    embed.add_field(name="Top 3 countries", value='3 Countries', inline=False)
    for i in range(3):
        embed.add_field(name=js["Country,Other"][str(i+8)],
                        value=js["TotalCases"][str(i+8)])
    embed.set_footer(text="source: https://www.worldometers.info/coronavirus/")
    await ctx.send(embed=embed)


@client.command(aliases=['deaths', 'TotalDeaths'])
async def totaldeaths(ctx):
    embed = discord.Embed(title="Total Deaths Due To Covid", url="https://www.worldometers.info/coronavirus/",
                          description="Total Deaths Due To Covid in the whole world, All continents and top 10 countries", color=0xa30000)
    embed.set_thumbnail(
        url="https://www.fda.gov/files/Coronavirus_3D_illustration_by_CDC_1600x900.png")
    embed.add_field(name="World", value=js["TotalDeaths"]["7"], inline=False)
    embed.add_field(name="Continents", value='5 Continents', inline=False)
    for i in range(5):
        embed.add_field(name=js["Country,Other"][str(i+1)],
                        value=js["TotalDeaths"][str(i+1)])
    embed.add_field(name="Top 3 countries", value='3 Countries', inline=False)
    for i in range(3):
        embed.add_field(name=js["Country,Other"][str(i+8)],
                        value=js["TotalDeaths"][str(i+8)])
    embed.set_footer(text="source: https://www.worldometers.info/coronavirus/")
    await ctx.send(embed=embed)


@client.command(aliases=["recovered", "totalrecovered"])
async def TotalRecovered(ctx):
    embed = discord.Embed(title="Total Recovered Covid Cases", url="https://www.worldometers.info/coronavirus/",
                          description="Total Recovered covid cases in the whole world, All continents and top 10 countries", color=0xa30000)
    embed.set_thumbnail(
        url="https://www.fda.gov/files/Coronavirus_3D_illustration_by_CDC_1600x900.png")
    embed.add_field(
        name="World", value=js["TotalRecovered"]["7"], inline=False)
    embed.add_field(name="Continents", value='5 Continents', inline=False)
    for i in range(5):
        embed.add_field(name=js["Country,Other"][str(i+1)],
                        value=js["TotalRecovered"][str(i+1)])
    embed.add_field(name="Top 3 countries", value='3 Countries', inline=False)
    for i in range(3):
        embed.add_field(name=js["Country,Other"][str(i+8)],
                        value=js["TotalRecovered"][str(i+8)])
    embed.set_footer(text="source: https://www.worldometers.info/coronavirus/")
    await ctx.send(embed=embed)


@client.command(aliases=['Active', 'activecases'])
async def ActiveCases(ctx):
    embed = discord.Embed(title="Total Active Covid Cases", url="https://www.worldometers.info/coronavirus/",
                          description="Total Active covid cases in the whole world, All continents and top 10 countries", color=0xa30000)
    embed.set_thumbnail(
        url="https://www.fda.gov/files/Coronavirus_3D_illustration_by_CDC_1600x900.png")
    embed.add_field(name="World", value=js["ActiveCases"]["7"], inline=False)
    embed.add_field(name="Continents", value='5 Continents', inline=False)
    for i in range(5):
        embed.add_field(name=js["Country,Other"][str(i+1)],
                        value=js["ActiveCases"][str(i+1)])
    embed.add_field(name="Top 3 countries", value='3 Countries', inline=False)
    for i in range(3):
        embed.add_field(name=js["Country,Other"][str(i+8)],
                        value=js["ActiveCases"][str(i+8)])
    embed.set_footer(text="source: https://www.worldometers.info/coronavirus/")
    await ctx.send(embed=embed)


@client.command()
async def Symptoms(ctx):
    embed=discord.Embed(title="Symptoms", description='Symptoms of Covid 19', color=0xa30000)
    embed.add_field(name="Most Common Symptoms", value="fever \ndry cough \ntiredness", inline=False)
    embed.add_field(name="Less Common Symptoms", value="aches and pains \nsore throat \ndiarrhoea \nconjunctivitis \nheadache \nloss of taste or smell \na rash on skin, or discolouration of fingers or toes", inline=False)
    embed.set_footer(text="source https://bit.ly/3t1XFHa")
    await ctx.send(embed=embed)

keepalive()
client.run(TOKEN)