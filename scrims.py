from discord.ext import commands, tasks
from random import shuffle
import discord

intents = discord.Intents.all()
client = commands.Bot("!", intents=intents)
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('Bridge'))
    print("Connected to discord")

@client.command(aliases=["roll","captains","teams","caps","team","captain","r","swag","townhalllevel10btw","anchans","scythepro","wael","api","gez","iamanchansbitch","wasim","unicorn","noodle","Limqo","!","h","eurth","QnVubnkgR2lybA","random"])
@commands.cooldown(1,0.5,commands.BucketType.channel)
async def queue(ctx):
    if "queue" not in ctx.message.channel.category.name.lower():
        return
    if ctx.message.author.voice is None:
        await ctx.send("Please join a queue before using this command")
        return
    vc = ctx.message.author.voice.channel
    if "queue" not in vc.category.name.lower():
        return await ctx.send("Please join a queue before using this command")
    members = vc.members
    if len(members) < vc.user_limit:
        await ctx.send("This queue is not full yet")
        return
    shuffle(members)
    captain1=members[0].display_name
    captain2=members[1].display_name
    embed = discord.Embed(title="Team Captains:")
    embed.add_field(name="First Captain",value=captain1)
    embed.add_field(name="Second Captain",value=captain2)
    await ctx.send(embed = embed)

client.run("token")
