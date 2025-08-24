<h1 align="center">VulnNet: Active</h1>
<p align="center">2025, August 23<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>474</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>VulnNet Entertainment just moved their entire infrastructure... Check this out...</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/183b30b9-5b5a-425b-83ba-d289f3914547"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/vulnnetactive">here </a>.<br>
<img width="1200px" src=""></p>

<br>
<h2>Task 1 . VulnNet: Active</h2>
<p>﻿VulnNet Entertainment had a bad time with their previous network which suffered multiple breaches. Now they moved their entire infrastructure and hired you again as a core penetration tester. Your objective is to get full access to the system and compromise the domain.<br><br>

- Difficulty: Medium
- Operating System: Windows<br><br>
Another Windows machine. Do your best and breach it, good luck!<br><br>

Note: Since this is a windows machine you might need to give it up to 5 minutes to boot.<br><br>

Icon made by <a href="https://www.freepik.com/">Freepik</a> from <a href="http://www.flaticon.com/">www.flaticon.com</a></p>

<p><em>Answer the questions below</em></p>

<p>1.1. What is the user flag? (Desktop\user.txt)<br>
<code>________</code></p>

<br>

<p>1.2. What is the system flag? (Desktop\system.txt)<br>
<code>________</code></p>

<br>

<h3>Nmap</h3>
<p> 14 open ports:

- &nbsp;&nbsp;&nbsp; <code>53</code> &nbsp; : &nbsp; DNS<br>
- &nbsp; &nbsp; <code>135</code> &nbsp; : &nbsp; MSRPC<br>
- &nbsp;&nbsp; <code>139</code> &nbsp; : &nbsp; SMB<br>
- &nbsp;&nbsp; <code>445</code> &nbsp; : &nbsp; SMB<br>
- &nbsp;&nbsp; <code>464</code> &nbsp; : &nbsp; kpasswd5<br>
- &nbsp; <code>6379</code> &nbsp; : &nbsp; Redis &nbsp; : &nbsp; 2.8.2402<br>
- &nbsp; <code>9389</code> &nbsp; : &nbsp; .Net Message Framing<br>
- <code>49666</code> &nbsp; : &nbsp; Microsoft Windows RPC<br>
- <code>49668</code> &nbsp; : &nbsp; Microsoft Windows RPC<br>
- <code>49669</code> &nbsp; : &nbsp; Microsoft Windows RPC<br>
- <code>49670</code> &nbsp; : &nbsp; Microsoft Windows RPC<br>
- <code>49677</code> &nbsp; : &nbsp; Microsoft Windows RPC<br>
- <code>49704</code> &nbsp; : &nbsp; Microsoft Windows RPC<br>
- <code>49796</code> &nbsp; : &nbsp; Microsoft Windows RPC</p>

```bash
:~/VulnNetActive# nmap -sT xx.xxx.xx.xx
...
PORT    STATE SERVICE
53/tcp  open  domain
135/tcp open  msrpc
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds
464/tcp open  kpasswd5
```

```bash
:~/VulnNetActive# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xx
...
PORT      STATE SERVICE       VERSION
53/tcp    open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
6379/tcp  open  redis         Redis key-value store 2.8.2402
9389/tcp  open  mc-nmf        .NET Message Framing
49666/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49670/tcp open  msrpc         Microsoft Windows RPC
49677/tcp open  msrpc         Microsoft Windows RPC
49704/tcp open  msrpc         Microsoft Windows RPC
49796/tcp open  msrpc         Microsoft Windows RPC
...
Host script results:
|_clock-skew: -1s
|_nbstat: NetBIOS name: VULNNET-BC3TCK1, NetBIOS user: <unknown>, NetBIOS MAC: xx:xx:xx:xx:xx:xx (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-08-23Txx:xx:xx
|_  start_date: N/A
```

<h3>enum4linux</h3>

<p>

- Got domain/workgroup name: VULNNET<br>
- VULNNET-BC3TCK1 <20> -         B <ACTIVE>  File Server Service<br>
- VULNNET-BC3TCK1 <00> -         B <ACTIVE>  Workstation Service<br>
- Server vulnnet.thm allows sessions using username '', password ''<br>
- SMB1 disabled -- no workgroup available</p>

```bash
:~/VulnNetActive# enum4linux -a vulnnet.thm
...
 ========================== 
|    Target Information    |
 ========================== 
Target ........... vulnnet.thm
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 =================================================== 
|    Enumerating Workgroup/Domain on vulnnet.thm    |
 =================================================== 
[+] Got domain/workgroup name: VULNNET

 =========================================== 
|    Nbtstat Information for vulnnet.thm    |
 =========================================== 
Looking up status of xx.xxx.xx.xx
	VULNNET-BC3TCK1 <20> -         B <ACTIVE>  File Server Service
	VULNNET-BC3TCK1 <00> -         B <ACTIVE>  Workstation Service
	VULNNET         <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	VULNNET         <1c> - <GROUP> B <ACTIVE>  Domain Controllers
	VULNNET         <1b> -         B <ACTIVE>  Domain Master Browser

	MAC Address = xx-xx-xx-xx-xx-xx

 ==================================== 
|    Session Check on vulnnet.thm    |
 ==================================== 
[+] Server vulnnet.thm allows sessions using username '', password ''

 ========================================== 
|    Getting domain SID for vulnnet.thm    |
 ========================================== 
Domain Name: VULNNET
Domain Sid: S-1-5-21-1405206085-1650434706-76331420
[+] Host is part of a domain (not a workgroup)

 ===================================== 
|    OS information on vulnnet.thm    |
 ===================================== 
Use of uninitialized value $os_info in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 464.
[+] Got OS info for vulnnet.thm from smbclient: 
[+] Got OS info for vulnnet.thm from srvinfo:
do_cmd: Could not initialise srvsvc. Error was NT_STATUS_ACCESS_DENIED

 ============================ 
|    Users on vulnnet.thm    |
 ============================ 
[E] Couldn't find users using querydispinfo: NT_STATUS_ACCESS_DENIED

[E] Couldn't find users using enumdomusers: NT_STATUS_ACCESS_DENIED

 ======================================== 
|    Share Enumeration on vulnnet.thm    |
 ======================================== 

	Sharename       Type      Comment
	---------       ----      -------
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on vulnnet.thm

 =================================================== 
|    Password Policy Information for vulnnet.thm    |
 =================================================== 
[E] Dependent program "polenum.py" not present.  Skipping this check.  Download polenum from http://labs.portcullis.co.uk/application/polenum/
...
 ====================================================================== 
|    Users on vulnnet.thm via RID cycling (RIDS: 500-550,1000-1050)    |
 ====================================================================== 
[E] Couldn't get SID: NT_STATUS_ACCESS_DENIED.  RID cycling not possible.

 ============================================ 
|    Getting printer info for vulnnet.thm    |
 ============================================ 
do_cmd: Could not initialise spoolss. Error was NT_STATUS_ACCESS_DENIED
```

<h3>crackmapexec smb</h3>

```bash
:~/VulnNetActive# crackmapexec smb vulnnet.thm
SMB         xx.xxx.xx.xx    445    VULNNET-BC3TCK1  [*] Windows 10.0 Build 17763 x64 (name:VULNNET-BC3TCK1) (domain:vulnnet.local) (signing:True) (SMBv1:False)
```

<h3>Redis</h3>

```bash
:~/VulnNetActive# apt install redis-tools
```

```bash
:~/VulnNetActive# redis-cli -h vulnnet.thm
vulnnet.thm:6379> info
# Server
redis_version:2.8.2402
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:b2a45a9622ff23b7
redis_mode:standalone
os:Windows  
arch_bits:64
multiplexing_api:winsock_IOCP
process_id:2112
run_id:fd5deedf4803915e1c9d9977c607e834a7d47642
...
```

```bash
vulnnet.thm:6379> config get *
  1) "dbfilename"
  2) "dump.rdb"
  3) "requirepass"
  4) ""
  5) "masterauth"
...
104) "C:\\Users\\enterprise-security\\Downloads\\Redis-x64-2.8.2402"
...
```

<br>

<img width="768" height="189" alt="image" src="https://github.com/user-attachments/assets/f8e02cc4-f944-4615-b501-dc6ba2bb0fbc" />

<br>
<h3>searchploit</h3>
<p>

- researched <code>GitHub Redis 2.8.2402 exploit</code><br>
- identified Redis RCE related to this version<br>
- learned in HackTricks how to enumerate Redis</p>

