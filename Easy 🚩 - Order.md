<h1 align="center">Order</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/6eab5e86-d9b1-4474-9f84-dd5ed984bcac"><br>
July 4, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>424</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>erform a known-plaintext attack to recover a repeating-key XOR key and decrypt a hidden message</em>.<br>
Access it <a href="https://tryhackme.com/room/hfb1order"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/452a3eef-3e09-4871-82cf-13b76ff5db43"></p>

<br>

<h2>Task 1 . Order</h2>

<p>We intercepted one of Cipher's messages containing their next target. They encrypted their message using a repeating-key XOR cipher. However, they made a critical error—every message always starts with the header:

<code>ORDER:</code><br>
Can you help void decrypt the message and determine their next target?<br>
Here is the message we intercepted:<br>

<code>1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373</code><br>

<code>1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60</code></p>

<p><em>Answer the question below</em></p>

<p>1.1. What is the flag?<br>
<code>THM{the_hackfinity_highschool}</code></p>

<br>

```bash
from itertools import cycle

ciphertext_hex = (
    "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373"
    "1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60")

ciphertexts = bytes.fromhex(ciphertext_hex)

known_prefix = b"ORDER:"

key = bytes(c ^ p for c, p in zip(ciphertexts, known_prefix))

decrypted = bytes(c ^ k for c, k in zip(ciphertexts, cycle(key)))

print("The decrypted message is:", decrypted.decode())
```

![image](https://github.com/user-attachments/assets/594776a5-7fbf-4fe3-b540-5a3b0112b33f)

<br>
<br>

![image](https://github.com/user-attachments/assets/c8aae5c9-684b-4999-b48e-7fe2058bdecf)

![image](https://github.com/user-attachments/assets/162143a8-5c5d-4135-8b48-cbebe22a1b78)


<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 4, 2025      | 424      |     163rdʰ   |      5ᵗʰ     |   1,045ᵗʰ   |    28ᵗʰ    |  112,848 |    828    |     63    |

</div>

![image](https://github.com/user-attachments/assets/f8f7d85b-6f83-44cd-9516-9ec16641d1e0)

![image](https://github.com/user-attachments/assets/9bdffbbb-bb14-44c7-ac51-0be6b1bbf611)

![image](https://github.com/user-attachments/assets/242d6008-c013-4135-ae36-2c7148150a19)

![image](https://github.com/user-attachments/assets/eb45b4f7-286f-4b7c-8e0f-31f89b39c160)

![image](https://github.com/user-attachments/assets/b226e878-1be6-47f8-866a-25f764cd94e1)
