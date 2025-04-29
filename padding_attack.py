import requests
import base64
from rich.console import Console
from rich.progress import track
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import random

console = Console()

URL_CIPHER = "http://localhost:5000/ciphertext"
URL_ORACLE = "http://localhost:5000/oracle"

cipher_b64 = requests.get(URL_CIPHER).content
cipher = base64.b64decode(cipher_b64)
iv, ct = cipher[:16], cipher[16:]
blocks = [iv] + [ct[i:i+16] for i in range(0, len(ct), 16)]

recovered = b""

console.print("[bold cyan] Starting Padding Oracle Attack...[/bold cyan]")
console.print(f"[gray]Intercepted {len(blocks)-1} encrypted block(s)[/gray]")

def query_oracle(modified_cipher):
    r = requests.post(URL_ORACLE, data=base64.b64encode(modified_cipher))
    return r.status_code == 200

for b in range(1, len(blocks)):
    prev, curr = bytearray(blocks[b-1]), blocks[b]
    recovered_block = bytearray(16)

    console.print(f"\n[bold green] Decrypting Block {b}[/bold green]")
    for i in track(range(15, -1, -1), description="Decrypting byte..."):
        padding = 16 - i
        for guess in range(256):
            modified = bytearray(prev)
            for j in range(i+1, 16):
                modified[j] ^= recovered_block[j] ^ padding
            modified[i] ^= guess ^ padding

            attempt = bytes(modified) + curr
            if query_oracle(attempt):
                recovered_block[i] = guess
                break

    recovered += recovered_block

plaintext = recovered.rstrip(b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10")
console.print(f"\n\n[bold magenta] Recovered Plaintext: {plaintext.decode()}[/bold magenta]")