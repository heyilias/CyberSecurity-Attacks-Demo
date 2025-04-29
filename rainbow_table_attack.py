import hashlib
import time
import sys
import random
from tqdm import tqdm
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# --- Generate a big fake rainbow table ---
# 1000 fake passwords + real password inside
fake_passwords = [f"userpass{i}" for i in range(1000)]
real_password = "supersecret"

# Build the rainbow table
rainbow_table = {hashlib.md5(p.encode()).hexdigest(): p for p in fake_passwords}

# Inject the real password randomly into the table
rainbow_table[hashlib.md5(real_password.encode()).hexdigest()] = real_password

# Shuffle keys (simulate more random attack)
rainbow_table_items = list(rainbow_table.items())
random.shuffle(rainbow_table_items)

# --- Target hash we want to crack ---
target_hash = hashlib.md5(real_password.encode()).hexdigest()

print(Fore.CYAN + "\nStarting Big Rainbow Table Attack...\n")
time.sleep(1)

# Display progress bar
for hash_value, password in tqdm(rainbow_table_items, desc="🔎 Searching Rainbow Table", ncols=100):
    time.sleep(0.05)  # small delay (fast but still visible)

    print(Fore.YELLOW + f"Trying password: {password} ", end="")
    sys.stdout.flush()

    if hash_value == target_hash:
        print(Fore.GREEN + f"\n\n✅ Password Found: {password}\n")
        break
    else:
        print(Fore.RED + "Not a match.")

else:
    print(Fore.RED + "\nPassword Not Found in Rainbow Table.\n")

print(Fore.CYAN + "Attack Finished!\n")
