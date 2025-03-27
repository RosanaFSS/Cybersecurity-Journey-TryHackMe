
<p align="center">March 28, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{325}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/eed07ca3-4235-4190-9c7a-81d93c4593cf"></p>


<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Adventure Time}}$$
</h1>
<p align="center">A CTF based challenge to get your blood pumping... It is classified as an easy-level challenge, and premium: for subscribers only.  It is classified as a hard-level CTF, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Can be accessed clicking <a href="https://tryhackme.com/room/adventuretime">here</a>.</p>
                                                              
<p align="center"> <img width="900px" src=""> </p>

<br>

<h2>Task 1 . Adventure Time</h2>
<p>Time to go on an adventure. Do you have what it takes to help Finn and Jake find BMO's reset code?
Help solve puzzles and try harder to the max....<br>

This is not a real world challenge, but fun and game only (and maybe learn a thing or two along the way).</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 1.1. <em>Content of flag1 – format is tryhackme{************} Hint : Try to recursively enumerate the website.</em>.<a id='1.1'></a>
>> <code><strong>tryhackme{Th1s1sJustTh3St4rt}</strong></code><br>

<p>I started enumerating with <code>nmap</code>.</p>

<ul style="list-style-type:square">
    <li><code>-sC</code>: is equivalent to <code>--script=default</code>.</li>
    <li><code>-sV</code>: Probe open ports to determine service/version info.</li>
    <li><code>-sS</code>: TCP SYN.</li>
    <li><code>-Pn</code>: Treat all hosts as online.</li>
    <li><code>-O</code> : Enable OS detection.</li>
    <li><code>-p-</code>: Scan all ports.</li>
</ul></p>

<p>Identified 5 ports open.</p>

<ul style="list-style-type:square">
    <li><code>21</code>: ftp with <code>Anonymous</code> allowed. It is in <code>ASCII</code>code></li>
    <li><code>22</code>: ssh</li>
    <li><code>80</code>: http</li>
    <li><code>443</code>: ssl/http</li>
    <li><code>31337</code> : Elite?</li>
</ul></p>

<p>Identified domain <code>adventure-time.com</code>.</p>

```bash
:~/AdventureTime# nmap -sC -sV -sS -Pn -O -p- 10.10.63.188
...
PORT      STATE SERVICE  VERSION
21/tcp    open  ftp      vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -r--r--r--    1 ftp      ftp       1401357 Sep 21  2019 1.jpg
| -r--r--r--    1 ftp      ftp        233977 Sep 21  2019 2.jpg
| -r--r--r--    1 ftp      ftp        524615 Sep 21  2019 3.jpg
| -r--r--r--    1 ftp      ftp        771076 Sep 21  2019 4.jpg
| -r--r--r--    1 ftp      ftp       1644395 Sep 21  2019 5.jpg
|_-r--r--r--    1 ftp      ftp         40355 Sep 21  2019 6.jpg
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.37.185
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp    open  ssh      OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp    open  http     Apache httpd 2.4.29
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: 404 Not Found
443/tcp   open  ssl/http Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: You found Finn
| ssl-cert: Subject: commonName=adventure-time.com/organizationName=Candy Corporate Inc./stateOrProvinceName=Candy Kingdom/countryName=CK
...
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
31337/tcp open  Elite?
| fingerprint-strings: 
|   DNSStatusRequestTCP, RPCCheck, SSLSessionReq: 
|     Hello Princess Bubblegum. What is the magic word?
|     magic word is not
|   DNSVersionBindReqTCP: 
|     Hello Princess Bubblegum. What is the magic word?
|     magic word is not 
|     version
|     bind
|   GenericLines, NULL: 
|     Hello Princess Bubblegum. What is the magic word?
|   GetRequest: 
|     Hello Princess Bubblegum. What is the magic word?
|     magic word is not GET / HTTP/1.0
|   HTTPOptions: 
|     Hello Princess Bubblegum. What is the magic word?
|     magic word is not OPTIONS / HTTP/1.0
|   Help: 
|     Hello Princess Bubblegum. What is the magic word?
|     magic word is not HELP
|   RTSPRequest: 
|     Hello Princess Bubblegum. What is the magic word?
|     magic word is not OPTIONS / RTSP/1.0
|   SIPOptions: 
|     Hello Princess Bubblegum. What is the magic word?
|     magic word is not OPTIONS sip:nm SIP/2.0
|     Via: SIP/2.0/TCP nm;branch=foo
|     From: <sip:nm@nm>;tag=root
|     <sip:nm2@nm2>
|     Call-ID: 50000
|     CSeq: 42 OPTIONS
|     Max-Forwards: 70
|     Content-Length: 0
|     Contact: <sip:nm@nm>
|_    Accept: application/sdp
...
```

<p>Accessed <code>ftp</code> and downloaded all the files using <code>mget *</code> command.</p>

```bash
:~/AdventureTime# ls
1.jpg  2.jpg  3.jpg  4.jpg  5.jpg  6.jpg
root@ip-10-10-122-76:~/AdvenntureTime# 

:~/AdventureTime# ftp 10.10.63.188
Connected to 10.10.63.188.
220 (vsFTPd 3.0.3)
Name (10.10.63.188:root): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Sep 21  2019 .
drwxr-xr-x    2 ftp      ftp          4096 Sep 21  2019 ..
-r--r--r--    1 ftp      ftp       1401357 Sep 21  2019 1.jpg
-r--r--r--    1 ftp      ftp        233977 Sep 21  2019 2.jpg
-r--r--r--    1 ftp      ftp        524615 Sep 21  2019 3.jpg
-r--r--r--    1 ftp      ftp        771076 Sep 21  2019 4.jpg
-r--r--r--    1 ftp      ftp       1644395 Sep 21  2019 5.jpg
-r--r--r--    1 ftp      ftp         40355 Sep 21  2019 6.jpg
226 Directory send OK.
ftp> mget *
mget 1.jpg? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for 1.jpg (1401357 bytes).
226 Transfer complete.
1401357 bytes received in 0.32 secs (4.1195 MB/s)
mget 2.jpg? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for 2.jpg (233977 bytes).
226 Transfer complete.
233977 bytes received in 0.09 secs (2.5800 MB/s)
mget 3.jpg? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for 3.jpg (524615 bytes).
226 Transfer complete.
524615 bytes received in 0.10 secs (5.0726 MB/s)
mget 4.jpg? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for 4.jpg (771076 bytes).
226 Transfer complete.
771076 bytes received in 0.29 secs (2.5531 MB/s)
mget 5.jpg? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for 5.jpg (1644395 bytes).
226 Transfer complete.
1644395 bytes received in 0.18 secs (8.5536 MB/s)
mget 6.jpg? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for 6.jpg (40355 bytes).
226 Transfer complete.
40355 bytes received in 0.07 secs (537.4296 kB/s)
ftp> exit
221 Goodbye.
```

<p>Used <code>exiftool</code> to analyze the downloaded <code>.jpg</code> files.</p>

```bash
:~/AdventureTime# for i in {1..6}; do exiftool $i.jpg | grep "XP Comment" | cut -d ":" -f2;done
 01111001 01101111 01110101 00100000
 01110010 01100101 01100001 01101100 01101100 01111001 00100000
 01101100 01101001 01101011 01100101 00100000
 01110100 01101111 00100000
 01110000 01110101 01111010 01111010 01101100 01100101 00100000
 01100100 01101111 01101110 00100111 01110100 00100000 01111001 01100001
```

<p>Navigated to <code>https://Target_IP</code>.<br>
I found <code>Finn</code>, discovered about <code>Jake</code>, and read the CA.<br>
Confirmed <code>the-adveture-time.com</code>code> from <code>nmap</code> output, and a new one: <code>land-of-ooo.com</code></p>

![image](https://github.com/user-attachments/assets/48b7ccb5-c26c-4ae6-b26a-dacd968ceb2d)

<br>


![image](https://github.com/user-attachments/assets/b464ae84-f6de-4d00-a4a7-d601d0ff6487)

<br>

![image](https://github.com/user-attachments/assets/c85fc0b9-b601-4bb4-8cd1-6fbf60e8ff41)



<br>

<p>Used <code>gobuster</code>.<br>
Discovered <code>/candybar</code>.</p>

```bash
:~/AdventureTime# gobuster dir -u https://Target_IP -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -k
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     https://Target_IP
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/candybar             (Status: 301) [Size: 317] [--> https://Target_IPcandybar/]
/server-status        (Status: 403) [Size: 301]
Progress: 207643 / 207644 (100.00%)
===============================================================
Finished
===============================================================

```


![image](https://github.com/user-attachments/assets/a5f2b2e4-a107-4ab7-9057-ecb4f0ba93fc)

<br>

<p>Added <code>Target_IP</code> and the 2 domain names to <code>/etc/hosts/</code>.</p>

![image](https://github.com/user-attachments/assets/9ea88b96-bad3-4bfb-8111-45261a0757f1)


<br>

<p>Navigated to <code>https://land-of-ooo.com</code>.<br>
Discovered <code>Jake</code>.</p>

![image](https://github.com/user-attachments/assets/a2d0c1f3-0d94-476e-97cc-63f2262031da)

<p>Used <code>gobuster</code>.<br>
Discovered <code>/yellowdog</code>.</p>

```bash
:~/AdventureTime# gobuster dir -u https://land-of-ooo.com -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -k
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     https://land-of-ooo.com
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/yellowdog            (Status: 301) [Size: 322] [--> http://land-of-ooo.com/yellowdog/]
/server-status        (Status: 403) [Size: 303]
Progress: 207643 / 207644 (100.00%)
===============================================================
Finished
===============================================================


```

<p>Navigated to <code>https://land-of-ooo.com/yellowdog</code>.</p>

![image](https://github.com/user-attachments/assets/eb2864a6-8816-4b57-8bc3-48153b082040)

<p>Saved the <code>yellow dog</code> image = <code>jake-2.png</code>.<br>
Inspected it with <code>exiftool</code> ... nothing interesting.</p>

![image](https://github.com/user-attachments/assets/9106441f-1001-452a-acd2-ba5d328291cf)


<p>Used <code>gobuster</code>.<br>
Discovered <code>/bananastock</code>.</p>


```bash
:~/AdventureTime# gobuster dir -u https://land-of-ooo.com/yellowdog/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -k
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     https://land-of-ooo.com/yellowdog/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/bananastock          (Status: 301) [Size: 334]
Progress: 207643 / 207644 (100.00%)
===============================================================
Finished
===============================================================

```

<p>Navigated to <code>https://land-of-ooo.com/yellowdog/bananastock</code>.<br>
Discovered a <code>Morse</code> encoded message.</p>

```bash
<!-- _/..../.\_.../._/_./._/_./._/...\._/._./.\_/..../.\_..././.../_/_._.__/_._.__/_._.__ -->
```

![image](https://github.com/user-attachments/assets/3e12d97c-9226-4f79-a7c2-4eb4858361c8)


<P>Used <code>Morse Code Decoder</code>: https://www.dcode.fr/morse-code.<br>
Discovered: <code>THE BANANAS ARE THE BEST!!!</code></p>

<br>

![image](https://github.com/user-attachments/assets/0d860316-6d69-4880-8573-9fffb22b8609)



<p>Used <code>gobuster</code>.<br>
Discovered <code>/princess</code>.</p>


```bash
:~/AdventureTime# :~# gobuster dir -u https://land-of-ooo.com/yellowdog/bananastock/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -k
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     https://land-of-ooo.com/yellowdog/bananastock/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/princess             (Status: 301) [Size: 343]

```

<br>

<p>Navigated to <code>https://land-of-ooo.com/yellowdog/bananastock/princess/</code>.</p>

![image](https://github.com/user-attachments/assets/fe320f0d-28c4-4886-a653-77ed3ae86795)

<br>

<p>Viewed <code>Page Source</code> and discovered <code>Secrettext</code>, <code>Key</code>, <code>IV</code>, <code>Mode</code>, <code>Input</code> and <code>Output</code>.</p>

![image](https://github.com/user-attachments/assets/48d26b63-fb4e-4d46-915c-2d28b44b2abc)


<p>Used <code>CyberChef</code> with the parameters just discovered.<br>
The decoded information is <code>the magic safe is accessibel at port 31337. the magic word is: ricardio</code></p>


![image](https://github.com/user-attachments/assets/7d08a515-01ee-4e04-a53b-8ac1559addab)

<br>

<p>Used <code>nc</code> command and dicovered that the new username is <code>apple-guards</code>.</p>

![image](https://github.com/user-attachments/assets/e60a59a4-22d4-4a39-8940-5c8a8d83ee91)

<p>Used <code>ssh</code>.<br>
ssh <code>apple-guards@land-of-ooo.com</code><br>
password: <code>THE BANANAS ARE THE BEST!!!</code>.</p>

```bash
:~/AdventureTime# ssh apple-guards@land-of-ooo.com
...
apple-guards@at:~$

```



<p>tryhackme{Th1s1sJustTh3St4rt}
</p>

![image](https://github.com/user-attachments/assets/ed003a23-8794-4b55-88fc-8b157e1540ce)

<br>

![image](https://github.com/user-attachments/assets/04e0d922-5e1d-44ef-bc68-3a526aaa71dd)


<p>./helper</p>

![image](https://github.com/user-attachments/assets/46f4dd59-846a-481e-a399-1a2c0ceb4bb1)

<br>

![image](https://github.com/user-attachments/assets/2b0b6266-8be2-4e0b-bc46-66969d317366)

<br>

![image](https://github.com/user-attachments/assets/ec30bcc4-1ada-4243-91ac-dfbc87b4c12c)


<br>

![image](https://github.com/user-attachments/assets/b4675ce9-1f6c-409e-952f-93b42c13b299)


<br>

![image](https://github.com/user-attachments/assets/4937802c-f211-4ff6-8df0-858c7c7d654f)

<p>su marceline<br>
My friend Finn</p>

![image](https://github.com/user-attachments/assets/2847ce5b-3e41-4c63-ad78-ccbe5a87b969)







> 1.2. <em>Content of flag2 – format is tryhackme{************} Hint : Can you search for someones files?</em>.<a id='1.2'></a>
>> <code><strong>tryhackme{N1c30n3Sp0rt}</strong></code><br>
<br>





111111111100100010101011101011111110101111111111011011011011000001101001001011111111111111001010010111100101000000000000101001101111001010010010111111110010100000000000000000000000000000000000000010101111110010101100101000000000000000000000101001101100101001001011111111111111111111001010000000000000000000000000001010111001010000000000000000000000000000000000000000000001010011011001010010010111111111111111111111001010000000000000000000000000000000001010111111001010011011001010010111111111111100101001000000000000101001111110010100110010100100100000000000000000000010101110010100010100000000000000010100000000010101111100101001111001010011001010010000001010010100101011100101001101100101001011100101001010010100110110010101111111111111111111111111111111110010100100100000000000010100010100111110010100000000000000000000000010100111111111111111110010100101111001010000000000000001010

https://www.dcode.fr/spoon-language


![image](https://github.com/user-attachments/assets/aa743022-8267-4300-b3a6-e57a1d5c2ddd)

<p>The magic word you are looking for is ApplePi</p>

<br>

![image](https://github.com/user-attachments/assets/56057e23-a99a-4338-88a9-1fbd1a5055fe)





