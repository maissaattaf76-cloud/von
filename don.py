import discord
import asyncio

# طلب التوكن عند التشغيل
TOKEN = input("🔑 أدخل توكن البوت: ")

SERVER_LINK = "https://discord.gg/k3P8kWQag"

class Bot(discord.Client):
    async def on_ready(self):
        print(f"✅ شغال: {self.user}")
        
        members = []
        for g in self.guilds:
            await g.chunk()
            members.extend([m for m in g.members if not m.bot])
        
        print(f"🚀 إرسال إلى {len(members)} عضو...")
        
        tasks = [m.send(f"👹 {SERVER_LINK}") for m in members]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        success = sum(1 for r in results if not isinstance(r, Exception))
        print(f"✅ تم: {success} | ❌ فشل: {len(members)-success}")
        await self.close()

bot = Bot(intents=discord.Intents.all())
bot.run(TOKEN)
