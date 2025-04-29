import time
import random
import sys
import os

# Matrix rain effect
def matrix_rain(lines=20):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    for _ in range(lines):
        line = "".join(random.choice(chars) for _ in range(80))
        print(f"\033[1;32m{line}\033[0m")
        time.sleep(0.05)

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Password to crack
password = "abt1"

# Characters to try
charset = "abcdefghijklmnopqrstuvwxyz0123456789"

found = False
attempt = ""
tries = 0

start_time = time.time()

clear()
print("Initiating Brute Force Attack...\n")
time.sleep(1)

# Brute-force logic with animation
for a in charset:
    for b in charset:
        for c in charset:
            for d in charset:
                attempt = a + b + c + d
                tries += 1
                sys.stdout.write(f"\rTrying: {attempt} | Attempts: {tries}")
                sys.stdout.flush()
                time.sleep(0.001)  # Speed adjust here
                if attempt == password:
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        break

elapsed = time.time() - start_time

clear()
matrix_rain(30)
print("\n\033[1;32m PASSWORD FOUND:\033[0m", attempt)
print(f"\033[1;34m Attempts:\033[0m {tries} | \033[1;34mTime taken:\033[0m {elapsed:.2f} seconds\n")
print("\033[1;32mACCESS GRANTED \033[0m")
