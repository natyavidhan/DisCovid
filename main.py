import json
import os
import requests
from discord.ext import commands
import discord
TOKEN = 'TOKEN'
# TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix="dc!")
def generate():
    url = "https://api.quarantine.country/api/v1/summary/latest"
    response = requests.get(url)
    data = response.json()
    return data

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
    embed.add_field(name="Country", value="dc!Country", inline=False)
    embed.add_field(name="World", value="dc!World", inline=False)
    embed.set_footer(
        text="Suggestions? Go to https://bit.ly/3dGGNzd and Submit your Suggestion :D")
    await ctx.send(embed=embed)


@help.command(aliases=['covid'])
async def Covid(ctx):
    embed = discord.Embed(
        title="Covid", description="What is Covid 19", color=0x800000)
    embed.add_field(name="Syntax", value="dc!Covid", inline=True)
    await ctx.send(embed=embed)


@help.command()
async def Country(ctx):
    embed = discord.Embed(title="Country",
                          description="Stats of a particular country", color=0x800000)
    embed.add_field(name="Syntax", value="dc!Country", inline=True)
    await ctx.send(embed=embed)
    
@help.command()
async def World(ctx):
    embed = discord.Embed(title="Country",
                          description="Stats of World", color=0x800000)
    embed.add_field(name="Syntax", value="dc!World", inline=True)
    await ctx.send(embed=embed)


@help.command()
async def Symptoms(ctx):
    embed = discord.Embed(title = "Symptoms", description='Symptoms of Covid 19', color=0x800000)
    embed.add_field(name="Syntax", value="dc!Symptoms", inline=True)
    await ctx.send(embed=embed)
    
@client.command(aliases=['covid'])
async def Covid(ctx):
    embed = discord.Embed(title="Covid", color=0x800000)
    embed.set_thumbnail(
        url="https://www.fda.gov/files/Coronavirus_3D_illustration_by_CDC_1600x900.png")
    embed.add_field(name="What is Covid", value="Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. \nMost people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment. \nHOW IT SPREADS \nThe virus that causes COVID-19 is mainly transmitted through droplets generated when an infected person coughs, sneezes, or exhales. These droplets are too heavy to hang in the air, and quickly fall on floors or surfaces. You can be infected by breathing in the virus if you are within close proximity of someone who has COVID-19, or by touching a contaminated surface and then your eyes, nose or mouth.", inline=True)
    embed.set_footer(text="source https://bit.ly/3t1XFHa")
    await ctx.send(embed=embed)


@client.command(aliases=['Country'])
async def country(ctx, country):
    country = country.lower()
    embed = discord.Embed(title=f"Covid Stats of {country}", url="https://www.worldometers.info/coronavirus/",
                          description="Stats", color=0xa30000)
    embed.set_thumbnail(
        url="https://www.fda.gov/files/Coronavirus_3D_illustration_by_CDC_1600x900.png")
    data = generate()
    embed.add_field(name="Total Cases", value=data['data']['regions'][country]['total_cases'], inline=False)
    embed.add_field(name="Active Cases", value=data['data']['regions'][country]['active_cases'], inline=False)
    embed.add_field(name="Total Deaths", value=data['data']['regions'][country]['deaths'], inline=False)
    embed.add_field(name="Total Recovered", value=data['data']['regions'][country]['recovered'], inline=False)
    embed.add_field(name="Critical", value=data['data']['regions'][country]['critical'])
    embed.add_field(name="Tested", value=data['data']['regions'][country]['tested'], inline=False)
    embed.add_field(name="Death ratio", value=data['data']['regions'][country]['death_ratio'], inline=False)
    embed.add_field(name="Recovery ratio", value=data['data']['regions'][country]['recovery_ratio'], inline=False)
    await ctx.send(embed=embed)
    
@client.command(aliases=['World'])
async def world(ctx):
    embed = discord.Embed(title=f"Covid Stats of World", url="https://www.worldometers.info/coronavirus/",
                          description="Stats", color=0xa30000)
    embed.set_thumbnail(
        url="https://www.fda.gov/files/Coronavirus_3D_illustration_by_CDC_1600x900.png")
    data = generate()
    embed.add_field(name="Total Cases", value=data['data']['summary']['total_cases'], inline=False)
    embed.add_field(name="Active Cases", value=data['data']['summary']['active_cases'], inline=False)
    embed.add_field(name="Total Deaths", value=data['data']['summary']['deaths'], inline=False)
    embed.add_field(name="Total Recovered", value=data['data']['summary']['recovered'], inline=False)
    embed.add_field(name="Critical", value=data['data']['summary']['critical'])
    embed.add_field(name="Tested", value=data['data']['summary']['tested'], inline=False)
    embed.add_field(name="Death ratio", value=data['data']['summary']['death_ratio'], inline=False)
    embed.add_field(name="Recovery ratio", value=data['data']['summary']['recovery_ratio'], inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['symptoms'])
async def Symptoms(ctx):
    embed=discord.Embed(title="Symptoms", description='Symptoms of Covid 19', color=0xa30000)
    embed.add_field(name="Most Common Symptoms", value="fever \ndry cough \ntiredness", inline=False)
    embed.add_field(name="Less Common Symptoms", value="aches and pains \nsore throat \ndiarrhoea \nconjunctivitis \nheadache \nloss of taste or smell \na rash on skin, or discolouration of fingers or toes", inline=False)
    embed.set_footer(text="source https://bit.ly/3t1XFHa")
    await ctx.send(embed=embed)

client.run(TOKEN)
