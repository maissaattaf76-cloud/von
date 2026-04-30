import discord
import asyncio
import time

TOKEN = input("🔑 توكن البوت: ")
SERVER_LINK = "https://discord.gg/k3P8kWQag"

MESSAGE = f"👹 ПРИВЕТ ИЗ АДА 👹\n🔥 {SERVER_LINK}"

sent = 0
fail = 0

class FastBot(discord.Client):
    async def on_ready(self):
        global sent, fail
        
        print(f"✅ {self.user}")
        
        # جمع الأعضاء
        members = []
        for g in self.guilds:
            await g.chunk()
            members.extend([m for m in g.members if not m.bot])
        
        print(f"🚀 إرسال إلى {len(members)} عضو - السرعة: 10/ثانية")
        start = time.time()
        
        # إرسال على دفعات
        batch_size = 10  # 10 رسائل كل مرة
        for i in range(0, len(members), batch_size):
            batch = members[i:i+batch_size]
            tasks = []
            
            for member in batch:
                tasks.append(self.send_safe(member))
            
            await asyncio.gather(*tasks)
            
            # انتظار 1 ثانية بين كل دفعة
            await asyncio.sleep(1)
            
            print(f"📦 تقدم: {min(i+batch_size, len(members))}/{len(members)}")
        
        elapsed = time.time() - start
        print(f"\n✅ تم! {sent} رسالة في {elapsed:.1f} ثانية")
        print(f"سرعة: {sent/elapsed:.1f} رسالة/ثانية")
        await self.close()
    
    async def send_safe(self, user):
        global sent, fail
        try:
            await user.send(MESSAGE)
            sent += 1
            print(f"✅ {sent} | {user.name}")
        except:
            fail += 1

bot = FastBot(intents=discord.Intents.all())
bot.run(TOKEN)
