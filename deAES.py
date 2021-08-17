import base64
from Cryptodome.Cipher import AES

with open("data", "rb") as f:
    nonce = f.read(16)
    tag = f.read(16)
    cipheredData = f.read()

with open("private_key", "rb") as f:
    key = f.read()

key_inbase64 = base64.b64encode(key).decode("utf-8")
print("\nYour private key: ", end="")
print(key_inbase64)

cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(cipheredData, tag)

print("====================")
print(data.decode("utf-8"))
print("====================")
