import discord
from discord.ext import commands
import asyncio
import os
import sys

# الرابط الذي تريد إرساله للناس (سيرفرك)
YOUR_SERVER_LINK = "https://discord.gg/k3P8kWQag"

# الرسالة بالروسية (وصف شيطاني)
MESSAGE_TEXT = """╔══════════════════════════════════════════════════════╗
║              👹 **ПРИВЕТ ИЗ АДА** 👹                    ║
╚══════════════════════════════════════════════════════╝

**{user_name}**, ты был(а) выбран(а)...

🔥 **Твой ад ждёт тебя:**
{YOUR_SERVER_LINK}

💀 *Не пытайся сбежать... тебя уже заметили* 💀

————————————————————————
👁️  *Сообщение отправлено автоматически*"""

# قائمة لتجنب إرسال رسائل مكررة
sent_users = set()

async def send_message_to_user(user, server_name):
    """إرسال رسالة لمستخدم معين"""
    try:
        message = MESSAGE_TEXT.format(
            user_name=user.name,
            YOUR_SERVER_LINK=YOUR_SERVER_LINK
        )
        await user.send(message)
        sent_users.add(user.id)
        print(f"✅ [تم] {user.name} | {user.id} | في سيرفر: {server_name}")
        return True
    except discord.Forbidden:
        print(f"❌ [خاص مغلق] {user.name} | في سيرفر: {server_name}")
        return False
    except Exception as e:
        print(f"⚠️ [خطأ] {user.name} | {e}")
        return False

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)
    
    async def on_ready(self):
        print(f"\n{'='*60}")
        print(f"🔥 البوت شغال كـ: {self.user}")
        print(f"📡 عدد السيرفرات: {len(self.guilds)}")
        print(f"{'='*60}\n")
        
        total_members = 0
        total_sent = 0
        
        for guild in self.guilds:
            print(f"\n{'='*60}")
            print(f"🎯 سيرفر: {guild.name}")
            print(f"👥 أعضاء السيرفر: {guild.member_count}")
            print(f"{'='*60}")
            
            # جلب الأعضاء الحقيقيين (بدون بوتات)
            members = [m for m in guild.members if not m.bot]
            total_members += len(members)
            
            print(f"\n📨 بدء الإرسال إلى {len(members)} عضو...\n")
            
            for i, member in enumerate(members, 1):
                print(f"[{i}/{len(members)}] جاري الإرسال إلى {member.name}...", end=" ")
                
                result = await send_message_to_user(member, guild.name)
                if result:
                    total_sent += 1
                
                # انتظار 1 ثانية بين كل رسالة (لتجنب الحظر)
                await asyncio.sleep(1)
            
            print(f"\n✅ تم الانتهاء من سيرفر: {guild.name}")
        
        print(f"\n{'='*60}")
        print(f"📊 ملخص التشغيل:")
        print(f"   - عدد السيرفرات: {len(self.guilds)}")
        print(f"   - إجمالي الأعضاء: {total_members}")
        print(f"   - تم الإرسال بنجاح: {total_sent}")
        print(f"   - فشل الإرسال: {total_members - total_sent}")
        print(f"{'='*60}")
        print("\n🟢 البوت جاهز لاستقبال الأعضاء الجدد...")
    
    async def on_member_join(self, member):
        """عند دخول عضو جديد لأي سيرفر"""
        if member.bot:
            return
        
        if member.id not in sent_users:
            await asyncio.sleep(2)
            await send_message_to_user(member, member.guild.name)
        else:
            print(f"⚠️ {member.name} استلم الرسالة سابقاً")

def clear_screen():
    """مسح الشاشة"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║     🔥 بوت الإرسال التلقائي - Discord Mass DM Bot 🔥        ║
    ║                                                              ║
    ║     ⚠️  أنت تتحمل المسؤولية الكاملة لأي استخدام للبوت  ⚠️    ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    print("\n📌 تعليمات:")
    print("   1. أدخل توكن البوت")
    print("   2. البوت سيرسل رابط سيرفرك لكل أعضاء أي سيرفر موجود فيه")
    print("   3. الإرسال يبدأ فور تشغيل البوت")
    print("\n" + "="*60)
    
    # طلب التوكن من المستخدم
    token = input("\n🔑 أدخل توكن البوت: ").strip()
    
    if not token:
        print("\n❌ خطأ: لم تدخل أي توكن!")
        sys.exit(1)
    
    print("\n🟡 جاري تشغيل البوت...\n")
    
    # تشغيل البوت
    bot = MyBot()
    
    try:
        bot.run(token)
    except discord.LoginFailure:
        print("\n❌ خطأ: التوكن غير صالح!")
        print("💡 تأكد من أن التوكن صحيح وأن البوت مفعل")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ خطأ: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
