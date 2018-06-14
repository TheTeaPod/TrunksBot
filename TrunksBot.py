import discord
from discord.ext import commands
import random
import time
import sys
TrunksID = 'NDU2ODUxMjI2OTg2OTM4MzY4.DgQjYA.--wJPx2uh1HT-wFc6dKWQ0hL1ig'
bot = commands.Bot("!")
@bot.event
async def on_ready():
	print("TrunksBot Beta Online!")

@bot.command(pass_context=True)
async def ping(ctx):
	"Check my response time"
	await bot.say("Pong!")

@bot.command(pass_context=True)
async def nut(ctx):
	"When you finally get that corner combo down"
	await bot.upload('nut.png')
@bot.command(pass_context=True)
async def ispotathot(ctx):
	"Somewhere near"
	await bot.upload('thot.png')
@bot.command(pass_context=True)
async def BnBs(ctx):
	"Some basic BnBs and combos for beginners"
	embed = discord.Embed(title = "Trunks BnBs", description ="basic combos for toranksuru", color = 0x00ff00)
	embed.add_field(name = "Midscreen BnB",value ="2M>M>j.M>L>L>2H>SD>M>L>L>2H>j.L>L>L")
	embed.add_field(name = "more info",value = "this does 4185 damage and yields a little over 1 meter")
	embed.add_field(name = "Corner BnB",value = "2M>M>j.M>L>L>2H>SD>M>L>L>2H>j.L>L>(delay)S>214L>L>L>L")
	embed.add_field(name = "more info",value = "this does 4505 damage and yields about 1.3 meter")
	embed.add_field(name = "More Damaging Corner Combo",value =  "M>M>S>214S>(delay)2M>M>H>S>214L>L>L>S>214L>L>L>2H>j.L>L>L>vanish>214H>Burning Attack")
	embed.add_field(name = "more info:", value ="This does 6334 damage and costs 2 meter (builds one during combo)")
	await bot.say(embed = embed)
bot.run(TrunksID)
