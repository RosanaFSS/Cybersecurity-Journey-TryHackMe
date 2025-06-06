
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

<h3>wfuzz</h3>

![image](https://github.com/user-attachments/assets/9eb94647-9055-4408-b4d0-5757d50b1c53)


<h3>http://cherryontop.thm</h3>

<p>- Scrolled down.<br>
- Discovered a video.<br>
- The video provides a hint: there is a secret club and If we are part of it, we should "check those subdomains".</p>

![image](https://github.com/user-attachments/assets/1c053b95-8589-4a70-b1d1-fb354b1d53f7)

![image](https://github.com/user-attachments/assets/919e142e-baa2-49bf-a545-f65037bef738)

![image](https://github.com/user-attachments/assets/c22f7765-2b39-48f3-a7d6-4ff9cf52d525)

![image](https://github.com/user-attachments/assets/beb90b45-b05f-4734-8b49-71e8a8d0305a)

<h3>http://nano.cherryontop.thm</h3>

![image](https://github.com/user-attachments/assets/f0eb8306-918b-4422-a6e3-c1d8859c2999)



<h3>ssh</h3>
<p>bob-boba</p>

![image](https://github.com/user-attachments/assets/95cb37bd-8c3d-40c3-a680-405035482c89)

<br>

![image](https://github.com/user-attachments/assets/69804947-1026-45b9-83c8-ffce755c5d5e)

<br>

![image](https://github.com/user-attachments/assets/77322e5f-ca45-42ea-a112-301f92b310ff)

<br>

![image](https://github.com/user-attachments/assets/2ad07753-0329-4fca-bc16-abcd1673a115)

<br>

![image](https://github.com/user-attachments/assets/4d16d678-afe4-420a-b7ab-a69ee6c88cf7)

<br>

![image](https://github.com/user-attachments/assets/687234ab-0ebc-42e8-a889-af84ab839a9a)


<p>THM{BL4CK_M4I1}</p>

![image](https://github.com/user-attachments/assets/cdc6177a-8a42-40f1-a6d4-e36eba86539a)

![image](https://github.com/user-attachments/assets/e06b49bf-df73-46e6-98fa-86b459283224)


<p>ChadCherrysFutureWife</p>

![image](https://github.com/user-attachments/assets/306b9001-e090-4a1b-95d7-4669e0fd4b64)

<p><code>n4n0ch3rry</code></p>

![image](https://github.com/user-attachments/assets/0a43fdae-2364-41d0-ba3f-ab2b974585e8)



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

![image](https://github.com/user-attachments/assets/3da6d3ed-a1bf-4c53-888b-3a19ed51fc1a)

![image](https://github.com/user-attachments/assets/1b386e27-bec2-44d4-a6b8-55f38247d9c8)


![image](https://github.com/user-attachments/assets/f31a632a-cd7d-457f-bbff-feacf8e365b7)

![image](https://github.com/user-attachments/assets/5a1360ac-829a-48e2-bb33-838260bd15cd)

![image](https://github.com/user-attachments/assets/7d83956b-b50d-49c6-aabe-5994eab95df3)

<h3>Target VM</h3>

```bash
notsus@ip-10-10-58-153:/tmp$ echo "10.10.218.30 cherryontop" >> /etc/hosts
```

<h3>Exploit</h3>

![image](https://github.com/user-attachments/assets/b85b448f-2d84-40cc-886c-d4ad0efc893e)








