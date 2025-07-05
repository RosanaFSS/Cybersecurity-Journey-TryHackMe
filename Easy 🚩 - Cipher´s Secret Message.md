<h1 align="center">Cipher´s Secret Message</h1>
<p align="center"><img width="80px" src="Sharpen your cryptography skills by analyzing code to get the flag."><br>
July 4, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>424</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Sharpen your cryptography skills by analyzing code to get the flag.</em>.<br>
Access it <a href="https://tryhackme.com/room/hfb1cipherssecretmessage"</a>here.<br>
<img width="1200px" src=""></p>

![image](https://github.com/user-attachments/assets/ed955759-2b59-4cd8-b1e0-4597741ad0bc)


<br>

<h2>Task 1 . Cipher´s Secret Message</h2>

<p>One of the Ciphers' secret messages was recovered from an old system alongside the encryption algorithm, but we are unable to decode it.<br>

Order: Can you help void to decode the message?<br>

Message : a_up4qr_kaiaf0_bujktaz_qm_su4ux_cpbq_ETZ_rhrudm<br>

Encryption algorithm :</p>

```bash
from secret import FLAG

def enc(plaintext):
    return "".join(
        chr((ord(c) - (base := ord('A') if c.isupper() else ord('a')) + i) % 26 + base) 
        if c.isalpha() else c
        for i, c in enumerate(plaintext)
    )

with open("message.txt", "w") as f:
    f.write(enc(FLAG))
```

<p>Note: Wrap the decoded message within the flag format THM{} </p>

<p>Answer the question below</p>

<p>1.1. What is the flag?<br>
<code></code></p>

```bash
from secret import FLAG

def enc(plaintext):
    return "".join(
        chr((ord(c) - (base := ord('A') if c.isupper() else ord('a')) + i) % 26 + base) 
        if c.isalpha() else c
        for i, c in enumerate(plaintext)
    )

with open("message.txt", "w") as f:
    f.write(enc(FLAG))
```


<p>Based on the script provided I crafted the script below:</p>

```bash
def dec(encoded_text):
    result = []
    for i, c in enumerate(encoded_text):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            shift = i % 26
            # To reverse shift: subtract i (i.e., shift back)
            original_char = chr((ord(c) - base - shift) % 26 + base)
            result.append(original_char)
        else:
            result.append(c)
    return "".join(result)

encoded_message = "a_up4qr_kaiaf0_bujktaz_qm_su4ux_cpbq_ETZ_rhrudm"
decoded_message = dec(encoded_message)
print(decoded_message)
```

![image](https://github.com/user-attachments/assets/22ca0e50-c8d2-4c66-a306-808593bf92f3)


![image](https://github.com/user-attachments/assets/4b171bb8-77a7-43c6-8f69-af9e39d93e11)




![image](https://github.com/user-attachments/assets/f4c7828d-3393-4c47-a318-a92ea96632a8)

