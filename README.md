# 🔐 CyberSecurity Attacks Demo

This project showcases practical demonstrations of common cybersecurity attacks for **educational** and **awareness** purposes.  
These scripts are built to simulate how attackers exploit vulnerabilities using different techniques.

## 🧠 Included Attacks

- 🧩 **Padding Oracle Attack**  
- 🔓 **Brute Force Attack**  
- 🌈 **Rainbow Table Attack**  
- 🕶️ **Man-in-the-Middle (MITM) Attack**

---

## 📁 Project Structure


---

## 🔍 Attack Explanations

### 🧩 Padding Oracle Attack

**What it is:**  
This attack exploits how padding is validated in encrypted data using **CBC (Cipher Block Chaining)** mode.

**How it works:**  
- Encrypted messages are broken into blocks.
- The attacker modifies the ciphertext and observes responses (valid/invalid padding).
- With enough tries, the attacker decrypts the message byte-by-byte.

**Demo Features:**
- Color-coded terminal outputs (red = failed guess, white = success).
- Shows the guessing process per block.
- Time-consuming to simulate a real-life brute-force attack.

---

### 🔓 Brute Force Attack

**What it is:**  
Attempts every possible combination of characters until it finds the correct password.

**Demo Features:**
- Simple logic for clear explanation.
- Can simulate long time using a delay between tries.
- Ideal for explaining password strength importance.

---

### 🌈 Rainbow Table Attack

**What it is:**  
Pre-computed tables of hashes are used to reverse hashed passwords faster than brute force.

**Demo Features:**
- Slower lookup simulated (~30 seconds).
- Emphasizes the risk of using **unsalted** hashes.

---

### 🕶️ MITM Attack (Fake Login Page)

**What it is:**  
A fake login page that captures credentials from unsuspecting users.

**How it works:**
- Victim visits a page that looks like a social media or banking site.
- Once credentials are entered, they're saved on the attacker’s server.
- A professional UI and retry option adds realism to the demo.

**Demo Features:**
- Styled HTML login page with fake branding.
- After submission, it redirects with a “Login Failed” message and retry button.
- Flask backend logs the credentials.

---

## 💡 Presentation Tips

- 📽️ Use this for **classroom** or **conference demos**.
- 🧠 Explain **CBC mode** before starting the Padding Oracle attack.
- 🎵 Optional: Add spy/hacking background music while demonstrating.
- 🎬 Use movie analogy: like a thief turning a lock dial until they hear the correct click – every guess gives feedback!

---

## ⚙️ How to Run

Install requirements (for MITM):
```bash
pip install flask

---

✅ **Next step:** Go to GitHub, create a new repo called `CyberSecurity-Attacks-Demo`, upload your scripts, add this `README.md`, and you’re good to go!

Want me to generate the LICENSE and `.gitignore` for you too?
