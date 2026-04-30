import discord
import asyncio
import time
import sys

# ========== إعداداتك ==========
SERVER_LINK = "https://discord.gg/k3P8kWQag"

# الرسالة بالروسية - يمكنك تعديلها كما تريد
MESSAGE = f"""╔══════════════════════════════════════════════════════╗
║              👹 **ПРИВЕТ ИЗ АДА** 👹                    ║
╚══════════════════════════════════════════════════════╝

🔥 **Твой ад ждёт тебя:**
{SERVER_LINK}

💀 *Не пытайся сбежать... тебя уже заметили* 💀

👁️  *Сообщение отправлено автоматически*"""
# =========================================================

sent_count = 0
fail_count = 0
rate_limit_wait = 0

class MassDMBot(discord.Client):
    async def on_ready(self):
        global sent_count, fail_count
        
        print(f"\n{'='*55}")
        print(f"✅ البوت شغال: {self.user}")
        print(f"📡 عدد السيرفرات: {len(self.guilds)}")
        print(f"👥 إجمالي الأعضاء: {sum(g.member_count for g in self.guilds)}")
        print(f"{'='*55}\n")
        
        if len(self.guilds) == 0:
            print("❌ البوت ليس في أي سيرفر!")
            print("💡 أضف البوت إلى سيرفر أولاً")
            await self.close()
            return
        
        # تجهيز قائمة بكل الأعضاء (بدون بوتات)
        all_members = []
        for guild in self.guilds:
            await guild.chunk()  # تحديث قائمة الأعضاء
            for member in guild.members:
                if not member.bot:  # استبعاد البوتات
                    all_members.append(member)
        
        print(f"🎯 عدد الأعضاء الحقيقيين: {len(all_members)}")
        print(f"⚡ سرعة الإرسال: رسالة كل 0.5 ثانية (لتفادي الحظر)")
        print(f"{'='*55}\n")
        
        start_time = time.time()
        
        # الإرسال بشكل متسلسل مع تأخير
        for i, member in enumerate(all_members, 1):
            try:
                await member.send(MESSAGE)
                sent_count += 1
                print(f"✅ [{sent_count}/{len(all_members)}] {member.name} | {member.guild.name}")
                
            except discord.Forbidden:
                fail_count += 1
                print(f"❌ [خاص مغلق] {member.name}")
                
            except discord.HTTPException as e:
                if e.status == 429:  # Rate limit
                    retry = e.retry_after if hasattr(e, 'retry_after') else 1
                    print(f"⚠️ Rate limit! انتظار {retry:.1f} ثانية...")
                    await asyncio.sleep(retry)
                    try:
                        await member.send(MESSAGE)
                        sent_count += 1
                        print(f"✅ [{sent_count}/{len(all_members)}] {member.name} (بعد إعادة المحاولة)")
                    except:
                        fail_count += 1
                else:
                    fail_count += 1
                    print(f"⚠️ [خطأ HTTP {e.status}] {member.name}")
                    
            except Exception as e:
                fail_count += 1
                print(f"⚠️ [خطأ] {member.name}: {str(e)[:50]}")
            
            # تأخير أساسي بين كل رسالة لتجنب Rate Limit
            await asyncio.sleep(0.5)
        
        elapsed = time.time() - start_time
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        
        print(f"\n{'='*55}")
        print(f"📊 **النتائج النهائية**")
        print(f"{'='*55}")
        print(f"⏱️  الوقت المستغرق: {minutes} دقيقة و {seconds} ثانية")
        print(f"📨 إجمالي الأعضاء: {len(all_members)}")
        print(f"✅ تم الإرسال بنجاح: {sent_count}")
        print(f"❌ فشل الإرسال: {fail_count}")
        if sent_count + fail_count > 0:
            print(f"📈 نسبة النجاح: {sent_count/(sent_count+fail_count)*100:.1f}%")
        print(f"{'='*55}")
        
        print("\n🟢 البوت أنهى عمله. سيتم إغلاقه بعد 3 ثواني...")
        await asyncio.sleep(3)
        await self.close()

def clear_screen():
    """مسح الشاشة - يعمل على كل الأنظمة"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║     🤖 **بوت الإرسال الجماعي - Discord Mass DM Bot** 🤖     ║
    ║                                                              ║
    ║     ⚡ يعمل بسرعة ذكية: رسالة كل 0.5 ثانية                   ║
    ║     🛡️  يتجنب تلقائياً Rate Limit من Discord                ║
    ║                                                              ║
    ║     ⚠️  **أنت تتحمل المسؤولية الكاملة لأي استخدام**  ⚠️      ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    print("\n📌 **التعليمات:**")
    print("   1️⃣  أدخل توكن البوت (سيتم طلبه منك)")
    print("   2️⃣  البوت سيرسل رابط سيرفرك لكل أعضاء أي سيرفر موجود فيه")
    print("   3️⃣  الإرسال يبدأ فوراً بعد التشغيل")
    print("   4️⃣  البوت يتعامل مع Rate Limit تلقائياً")
    print("\n" + "="*55)
    
    # طلب التوكن بطريقة آمنة
    token = input("\n🔑 **أدخل توكن البوت:** ").strip()
    
    if not token:
        print("\n❌ خطأ: لم تدخل أي توكن!")
        sys.exit(1)
    
    print("\n🟡 جاري تشغيل البوت...")
    print("💡 إذا لم يشتغل، تأكد من:")
    print("   - صحة التوكن")
    print("   - تفعيل Intents في Developer Portal")
    print("   - أن البوت مضاف إلى سيرفر\n")
    
    # إعداد الـ Intents
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    
    bot = MassDMBot(intents=intents)
    
    try:
        bot.run(token)
    except discord.LoginFailure:
        print("\n❌ **خطأ: التوكن غير صالح!**")
        print("💡 الحل: اذهب إلى https://discord.com/developers/applications")
        print("   واضغط 'Reset Token' ثم استخدم التوكن الجديد")
    except Exception as e:
        print(f"\n❌ خطأ غير متوقع: {e}")

if __name__ == "__main__":
    main()
