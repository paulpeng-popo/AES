import sys
import base64
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

# ============== user compose data ==============
print("Welcome to Nmail")
print("Compose a mail: (EOF for completion)")
msg = ""
for line in sys.stdin:
    msg += line
msg = str.encode(msg)

# ============== generate private key ==============
key = get_random_bytes(32)
key_inbase64 = base64.b64encode(key).decode("utf-8")
print("\nYour private key: ", end="")
print(key_inbase64)

# ============== save private key ==============
keypath = "private_key"
with open(keypath, "wb") as f:
    f.write(key)

# ============== data encryption ==============
cipher = AES.new(key, AES.MODE_EAX)
cipheredData, tag = cipher.encrypt_and_digest(msg)

print(base64.b64encode(cipher.nonce).decode("utf-8"))
print(base64.b64encode(tag).decode("utf-8"))
print(base64.b64encode(cipheredData).decode("utf-8"))

with open("data", "wb") as f:
    f.write(cipher.nonce)
    f.write(tag)
    f.write(cipheredData)
