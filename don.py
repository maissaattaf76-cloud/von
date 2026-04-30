import discord
import asyncio
import time

TOKEN = input("🔑 توكن البوت: ")
SERVER_LINK = "https://discord.gg/k3P8kWQag"

MESSAGE = f"""👹 **ПРИВЕТ ИЗ АДА** 👹

Твой ад ждёт тебя: {SERVER_LINK}"""

class UltraFastBot(discord.Client):
    async def on_ready(self):
        print(f"✅ شغال: {self.user}")
        
        # تشغيل 200 مهمة متزامنة
        tasks = []
        for guild in self.guilds:
            for member in guild.members:
                if not member.bot:
                    tasks.append(self.send_dm(member))
                    
                    # كل 200 مهمة ننفذها فوراً
                    if len(tasks) >= 200:
                        await asyncio.gather(*tasks)
                        tasks = []
        
        if tasks:
            await asyncio.gather(*tasks)
        
        print("✅ تم الانتهاء!")
        await self.close()
    
    async def send_dm(self, user):
        try:
            await user.send(MESSAGE)
            print(f"✅ {user.name}")
        except:
            pass

bot = UltraFastBot(intents=discord.Intents.default())
bot.run(TOKEN)
