#!/usr/bin/env python3
"""
Mecha Break Memory Scanner – Find health and ammo addresses.
Open source – no game memory modification.
"""

import pymem
import pymem.process
import time

def main():
    print("[INFO] Searching for Mecha Break process...")
    try:
        pm = pymem.Pymem("MechaBreak.exe")
        print("[SUCCESS] Process found!")
    except pymem.exception.ProcessNotFound:
        print("[ERROR] Game not running. Start Mecha Break first.")
        return

    module = pymem.process.module_from_name(pm.process_handle, "MechaBreak.exe")
    base = module.lpBaseOfDll
    print(f"[INFO] Base address: {hex(base)}")

    print("[INFO] This is a demo. The full trainer is in Releases.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()