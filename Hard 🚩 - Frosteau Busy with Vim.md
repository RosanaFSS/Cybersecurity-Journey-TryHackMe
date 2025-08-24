<h1 align="center">Frosteau Busy with Vim</h1>
<p align="center">2025, August 24<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>474</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Use your defence evasion skills to take control of a secure network.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/8cab783d-2a47-4e1b-bb76-71ba226fa3b1"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/bypass">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/a692f188-386c-49ad-a516-3c47e7ea5dde"></p>

<br>
<h2>Task 1 . Bypass</h2>

<p>Start the VM by clicking the <code>Start Machine</code> button at the top right of the task. You can complete the challenge by connecting through a VPN or the AttackBox containing all the essential tools.</p>

<p><em>The network security team has implemented state-of-the-art protection mechanisms using an IDS. Your task is to bypass the network security solution and gain access to the CCTV web panel of the company.</em></p>

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

<img width="997" height="204" alt="image" src="https://github.com/user-attachments/assets/feeb9c85-a532-410f-9a30-74d40c8f4ff4" />

<br>

<img width="991" height="309" alt="image" src="https://github.com/user-attachments/assets/64079947-0008-4efe-b118-71264fa4e535" />

<br>

<img width="998" height="197" alt="image" src="https://github.com/user-attachments/assets/8ea70a29-3d1a-4f99-8928-d0ddcb472f63" />

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

<img width="912" height="848" alt="image" src="https://github.com/user-attachments/assets/6a838c4d-df48-4efe-8df4-bf398c49e97b" />

<br>

<img width="1106" height="750" alt="image" src="https://github.com/user-attachments/assets/152705d3-5ed6-4a8b-bad2-be6d6bc28716" />


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


<img width="588" height="682" alt="image" src="https://github.com/user-attachments/assets/dc603d08-eb9e-422a-88ab-d13c01d21a79" />

<br>

<img width="590" height="680" alt="image" src="https://github.com/user-attachments/assets/badbbcf4-60a4-40c3-8c28-67c4e119909f" />

<br>

<img width="587" height="683" alt="image" src="https://github.com/user-attachments/assets/1c6779b5-bba7-4da9-b52a-2a8396d25d41" />

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
$ nmap -A -p 22,80,8065,8075,8095,24641,29972 -T4 10.10.123.117 -vvv
```
