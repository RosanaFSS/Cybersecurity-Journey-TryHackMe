<h1 align="center">Minotaur´s Labyrinth</h1>
<p align="center">2025, August 3<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>454</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>The Minotaur threw a fit and captured some people in the Labyrinth. Are you able to help Daedalus free them?</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/0917d300-d0cf-4907-82c4-647cb626c92b"><br>
Click <a href=https://tryhackme.com/room/labyrinth8llv">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src=""></p>

<br>

<h2>Task 1 . Find the flags</h2>
<p>Hi, it's me, Daedalus, the creator of the Labyrinth. I was able to implement some backdoors, but Minotaur was able to (partially) fix them (that's a secret, so don't tell anyone). But let's get back to your task, root this machine and give Minotaur a lesson.<br>

The target machine may take a few minutes to boot up fully.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>What is flag 1? </em><br><a id='1.1'></a>
>> <strong><code>fl4g{tHa75_TH3_$7Ar7_ftPFLA9}</code></strong><br>
<p></p>

<br>

> 1.2. <em>What is flag 2? </em><br><a id='1.2'></a>
>> <strong><code>__________</code></strong><br>
<p></p>

<br>

> 1.3. <em>What is the user flag </em><br><a id='1.3'></a>
>> <strong><code>__________</code></strong><br>
<p></p>

<br>

> 1.4. <em>What is the root flag </em><br><a id='1.4'></a>
>> <strong><code>__________</code></strong><br>
<p></p>

<br>

<h3>nmap</h3>

```bash
:~/Minotaur´sLabyrinth# nmap -p- -vv -T4 TargetIP
...
PORT     STATE SERVICE REASON
21/tcp   open  ftp     syn-ack ttl 64
22/tcp   open  ssh     syn-ack ttl 64
80/tcp   open  http    syn-ack ttl 64
443/tcp  open  https   syn-ack ttl 64
3306/tcp open  mysql   syn-ack ttl 64
```

```bash
:~/Minotaur´sLabyrinth# nmap -sC -sV -p- -T4 TargetIP
...
PORT     STATE SERVICE  VERSION
21/tcp   open  ftp      ProFTPD
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x   3 nobody   nogroup      4096 Jun 15  2021 pub
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     Apache httpd 2.4.48 ((Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1)
|_http-server-header: Apache/2.4.48 (Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1
| http-title: Login
|_Requested resource was login.html
443/tcp  open  ssl/http Apache httpd 2.4.48 ((Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1)
|_http-server-header: Apache/2.4.48 (Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1
| http-title: Login
|_Requested resource was login.html
| ssl-cert: Subject: commonName=localhost/organizationName=Apache Friends/stateOrProvinceName=Berlin/countryName=DE
| Not valid before: 2004-xx-xxTxx:xx:xx
|_Not valid after:  2010-xx-xxTxx:xx:xx
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
3306/tcp open  mysql?
| fingerprint-strings: 
|   DNSVersionBindReqTCP, NULL: 
|_    Host 'ip-10-201-35-134.ec2.internal' is not allowed to connect to this MariaDB server
```

<h3>Nikto</h3>

```bash
:~/Minotaur´sLabyrinth# nikto -h TargetIP
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          TargetIO
+ Target Hostname:    ip-xx-xxx-xx-xx.ec2.internal
+ Target Port:        80
+ Start Time:         2025-08-03 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.48 (Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1
+ Cookie PHPSESSID created without the httponly flag
+ Retrieved x-powered-by header: PHP/8.0.7
+ The anti-clickjacking X-Frame-Options header is not present.
+ Root page / redirects to: login.html
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ OSVDB-44056: /sips/sipssys/users/a/admin/user: SIPS v0.2.2 allows user account info (including password) to be retrieved remotely.
+ OSVDB-3268: /imgs/: Directory indexing found.
+ OSVDB-3092: /imgs/: This might be interesting...
+ OSVDB-3268: /logs/: Directory indexing found.
+ OSVDB-3092: /logs/: This might be interesting...
+ OSVDB-3268: /icons/: Directory indexing found.
+ Server leaks inodes via ETags, header found with file /icons/README, fields: 0x13f4 0x438c034968a80 
+ OSVDB-3233: /icons/README: Apache default file found.
+ /login.html: Admin login page/section found.
+ /login.php: Admin login page/section found.
+ 6544 items checked: 0 error(s) and 14 item(s) reported on remote host
+ End Time:           2025-08-03 xx:xx:xx (GMT1) (22 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>

<h3></h3>

<h3>Web 80</h3>

<img width="1129" height="579" alt="image" src="https://github.com/user-attachments/assets/867bd4a6-eca8-4f2b-a1d5-aff997caaa12" />

<p>

- redirects to <code>/login.html</code><br>
- identified <code>js/login.js</code><br>
- identified <code>/jebaith.html</code><br></p>

<img width="1198" height="688" alt="image" src="https://github.com/user-attachments/assets/5b8d65dd-92c4-4055-9baf-560b12693fad" />

<br>

<h3>/js/login.js</h3>

<p>

- identified info that might be related to <code>Dedalus</code> password</p>

```bash
function pwdgen() {
    a = ["0", "h", "?", "1", "v", "4", "r", "l", "0", "g"]
    b = ["m", "w", "7", "j", "1", "e", "8", "l", "r", "a", "2"]
    c = ["c", "k", "h", "p", "q", "9", "w", "v", "5", "p", "4"]
}
//pwd gen for Daedalus a[9]+b[10]+b[5]+c[8]+c[8]+c[1]+a[1]+a[5]+c[0]+c[1]+c[8]+b[8]
```

<img width="1139" height="612" alt="image" src="https://github.com/user-attachments/assets/fab9c7b9-7688-4f17-9b40-bb224415d92f" />

<p>

- crafted a Python script<br>
- uncovered <code>daedalus</code> : <code>g2e55kh4ck5r</code></p>

```bash
#!/usr/bin/env python3

def pwdgen():
        a = ["0", "h", "?", "1", "v", "4", "r", "l", "0", "g"]
        b = ["m", "w", "7", "j", "1", "e", "8", "l", "r", "a", "2"]
        c = ["c", "k", "h", "p", "q", "9", "w", "v", "5", "p", "4"]

        print(a[9]+b[10]+b[5]+c[8]+c[8]+c[1]+a[1]+a[5]+c[0]+c[1]+c[8]+b[8])

pwdgen()
```

<img width="860" height="104" alt="image" src="https://github.com/user-attachments/assets/7c42f4ba-5bf1-42a1-b564-38357fb9fb83" />


<br>

<img width="1226" height="524" alt="image" src="https://github.com/user-attachments/assets/f7818a39-ee6a-400e-9692-d55ced22adf1" />


<h3>/js/userlvl.js</h3>

<img width="1203" height="712" alt="image" src="https://github.com/user-attachments/assets/8ad68997-59c3-42fa-a67c-668199620778" />


<h3>/api/people</h3>

<img width="1185" height="256" alt="image" src="https://github.com/user-attachments/assets/573986d1-ffcf-48bf-b53c-df6bc3baafca" />


<br>

<h3>/jebaith.html</h3>

<p>

- spayc
- xenox
</p>

<img width="1291" height="247" alt="image" src="https://github.com/user-attachments/assets/6f2d08a0-1274-47a9-b734-4ba146c4fdda" />

<h3>/x.com/JeagerXenox</h3>

<img width="1296" height="582" alt="image" src="https://github.com/user-attachments/assets/638f9a6d-ca23-48eb-8a73-eab8d8d07792" />

<br>

<h3>//app.intigriti.com/profile/xenoxjeager</h3>

<img width="1282" height="598" alt="image" src="https://github.com/user-attachments/assets/4f22f0dc-8842-425c-8827-34d382f1e733" />

<br>

<h3>/x.com/spayc4</h3>

<img width="1156" height="472" alt="image" src="https://github.com/user-attachments/assets/807df239-92b0-4660-ac6b-889dd719dfe0" />


<h3>gobuster</h3>

```bash

```

<h3>FTP</h3>

```bash
:~/Minotaur´sLabyrinth# ftp TargetIP
...
Name (TargetIP:root): anonymous
331 Anonymous login ok, send your complete email address as your password
Password:
230 Anonymous access granted, restrictions apply
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
200 PORT command successful
150 Opening ASCII mode data connection for file list
drwxr-xr-x   3 root     root         4.0k Jun 15  2021 .
drwxr-xr-x   3 root     root         4.0k Jun 15  2021 ..
drwxr-xr-x   3 nobody   nogroup      4.0k Jun 15  2021 pub
226 Transfer complete
ftp> cd pub
250 CWD command successful
ftp> ls -lah
200 PORT command successful
150 Opening ASCII mode data connection for file list
drwxr-xr-x   3 nobody   nogroup      4.0k Jun 15  2021 .
drwxr-xr-x   3 root     root         4.0k Jun 15  2021 ..
drwxr-xr-x   2 root     root         4.0k Jun 15  2021 .secret
-rw-r--r--   1 root     root          141 Jun 15  2021 message.txt
ftp> get message.txt
local: message.txt remote: message.txt
200 PORT command successful
150 Opening BINARY mode data connection for message.txt (141 bytes)
226 Transfer complete
141 bytes received in 0.00 secs (2.8014 MB/s)
ftp> cd .secret
250 CWD command successful
ftp> ls -lah
200 PORT command successful
150 Opening ASCII mode data connection for file list
drwxr-xr-x   2 root     root         4.0k Jun 15  2021 .
drwxr-xr-x   3 nobody   nogroup      4.0k Jun 15  2021 ..
-rw-r--r--   1 root     root           30 Jun 15  2021 flag.txt
-rw-r--r--   1 root     root          114 Jun 15  2021 keep_in_mind.txt
226 Transfer complete
ftp> get flag.txt
local: flag.txt remote: flag.txt
200 PORT command successful
150 Opening BINARY mode data connection for flag.txt (30 bytes)
226 Transfer complete
30 bytes received in 0.00 secs (81.6069 kB/s)
ftp> get keep_in_mind.txt
local: keep_in_mind.txt remote: keep_in_mind.txt
200 PORT command successful
150 Opening BINARY mode data connection for keep_in_mind.txt (114 bytes)
226 Transfer complete
114 bytes received in 0.00 secs (275.5647 kB/s)
ftp> exit
221 Goodbye.
```

```bash
:~/Minotaur´sLabyrinth# ls
flag.txt  keep_in_mind.txt  message.txt
```

```bash
:~/Minotaur´sLabyrinth# cat flag.txt
fl4g{tHa75_TH3_$7Ar7_ftPFLA9}
```

<p>

- Dedalus
- Minotaur  
</p>

```bash
:~/Minotaur´sLabyrinth# cat message.txt
Daedalus is a clumsy person, he forgets a lot of things arount the labyrinth, have a look around, maybe you'll find something :)
-- Minotaur
```

<p>

- timer  
</p>

```bash
:~/Minotaur´sLabyrinth# cat keep_in_mind.txt
Not to forget, he forgets a lot of stuff, that's why he likes to keep things on a timer ... literally
-- Minotaur
```

<br>

<h3>/etc/hosts</h3>

```bash
TargetIP   soupedecode.thm
```

<h3>/etc/hosts</h3>

```bash
TargetIP   soupedecode.thm
```

<h3>/etc/hosts</h3>

```bash
TargetIP   soupedecode.thm
```

