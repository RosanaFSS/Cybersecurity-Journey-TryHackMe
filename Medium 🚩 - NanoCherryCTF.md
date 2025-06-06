
<h3>nmap</h3>

```bash
:~# nmap -sS -Pn -A -T4 -p- 10.10.58.153
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-server-header: Apache/2.4.52 (Ubuntu)
|_http-title: Cherry on Top Ice Cream Shop
```

<br>

<h3>ssh</h3>
<p>bob-boba</p>

![image](https://github.com/user-attachments/assets/95cb37bd-8c3d-40c3-a680-405035482c89)

<h3>/etc/passwd</h3>
<p>bob-boba::x:1003:1003::/home/bob-boba:/bin/sh</p>

```bash
notsus@ip-10-10-58-153:/tmp$ cat /etc/passwd
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
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:104::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:105:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
usbmux:x:107:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
chad-cherry:x:1000:1000:Chad Cherry:/home/chad-cherry:/bin/bash
molly-milk:x:1001:1001::/home/molly-milk:/bin/sh
sam-sprinkles:x:1002:1002::/home/sam-sprinkles:/bin/sh
bob-boba:x:1003:1003::/home/bob-boba:/bin/sh
notsus:x:1004:1004::/home/.notsus:/bin/sh
lxd:x:999:100::/var/snap/lxd/common/lxd:/bin/false
ssm-user:x:1005:1005::/home/ssm-user:/bin/sh
ubuntu:x:1006:1007:Ubuntu:/home/ubuntu:/bin/bash
notsus@ip-10-10-58-153:/tmp$ clear

```

<h3>linpeas.sh</h3>

```bash
```


![image](https://github.com/user-attachments/assets/418bd8cf-db9c-44f2-9e4c-ae62c7be0826)
