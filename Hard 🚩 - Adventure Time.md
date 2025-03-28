
<p align="center">March 27, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{325}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/eed07ca3-4235-4190-9c7a-81d93c4593cf"></p>


<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Adventure Time}}$$
</h1>
<p align="center">A CTF based challenge to get your blood pumping... It is classified as an easy-level challenge, and premium: for subscribers only.  It is classified as a hard-level CTF, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Can be accessed clicking <a href="https://tryhackme.com/room/adventuretime">here</a>.</p>
                                                              
<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/b0d2990a-4f13-4b4a-9345-91fe7d5fa7eb"> </p>

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

<p>Discovered the first flag.</p>

![image](https://github.com/user-attachments/assets/568e5d01-7e9c-4e42-9d53-ff9135a032dd)


<br>
<br>

> 1.2. <em>Content of flag2 – format is tryhackme{************} Hint : Can you search for someones files?</em>.<a id='1.2'></a>
>> <code><strong>tryhackme{N1c30n3Sp0rt}</strong></code><br>
<br>


<p>Used <code>cat mbox</code> and dicovered <code>marceline</code>.</p>

![image](https://github.com/user-attachments/assets/49f5ea7d-41f7-46f3-8c8d-7de565c70978)


<p>Used <code>find / -user marceline -type f 2>/dev/null</code> researching for files owned by <code>marceline</code>.<br>
Discovered <code>/etc/fonts/helper</code></p>.

![image](https://github.com/user-attachments/assets/1825ec7a-f57b-4072-b656-6f5ac134520b)


<p>Ran <code>helper</code>: <code>./helper</code>.<br>
I answered <code>no</code>.<br>
Discovered <code>Gpnhkse</code>.</p>

![image](https://github.com/user-attachments/assets/1de81411-0126-4e46-8511-24c8d245dace)


<br>

<p>Used <code>Vigenere Decoder</code>: https://www.dcode.fr/vigenere-cipher.<br>
Discovered <code>Abadeer</code></p>

![image](https://github.com/user-attachments/assets/b4675ce9-1f6c-409e-952f-93b42c13b299)

<br>

<p>Ran <code>helper</code> again, answered <code>yes</code>, typed what I discovered and got <code>My password</code>:<code>My friend Finn</code>.</p>

![image](https://github.com/user-attachments/assets/9eff6264-948d-4732-8ede-3c2c7e1231e7)


<p>Used <code>su marceline</code> with the password just discovered.<br>
Discovered the second flag.<br>
Discovered  a secret message.</p>

![image](https://github.com/user-attachments/assets/56dc55b1-2ebc-4914-af8b-494d9120b830)

<br>

```bash
marceline@at:~$ cat I-got-a-secret.txt
Hello Finn,

I heard that you pulled a fast one over the banana guards.
B was very upset hahahahaha.
I also heard you guys are looking for BMO's resetcode.
You guys broke him again with those silly games?

You know I like you Finn, but I don't want to anger B too much.
So I will help you a little bit...

But you have to solve my little puzzle. Think you're up for it?
Hahahahaha....I know you are.

111111111100100010101011101011111110101111111111011011011011000001101001001011111111111111001010010111100101000000000000101001101111001010010010111111110010100000000000000000000000000000000000000010101111110010101100101000000000000000000000101001101100101001001011111111111111111111001010000000000000000000000000001010111001010000000000000000000000000000000000000000000001010011011001010010010111111111111111111111001010000000000000000000000000000000001010111111001010011011001010010111111111111100101001000000000000101001111110010100110010100100100000000000000000000010101110010100010100000000000000010100000000010101111100101001111001010011001010010000001010010100101011100101001101100101001011100101001010010100110110010101111111111111111111111111111111110010100100100000000000010100010100111110010100000000000000000000000010100111111111111111110010100101111001010000000000000001010
marceline@at:~$ 
```


<br>
<br>

> 1.3. <em>Content of flag3 – format is tryhackme{************} Hint : If stuck do research on cutlery.</em>.<a id='1.3'></a>
>> <code><strong>tryhackme{N0Bl4ckM4g1cH3r3}</strong></code><br>
<br>


![image](https://github.com/user-attachments/assets/9d2e6b67-cf65-4d5d-8341-ea7946373a1a)


<br>

<p><code>CyberChef</code>´s <code>Magic</code> tool was not able to discovered the encoding type.<br>
Researched and discovered that it is about <code>spoon</code>.<br>
Used https://www.dcode.fr/spoon-language and discovered <code>ApplePie</code>.</p>

![image](https://github.com/user-attachments/assets/978d3988-94ea-4b08-8200-cb8cb3173757)

<br>

<p>Used <code>nc Target_IP 31337</code> and the last magic word.<br>
Discovered <code>peppermint-butler</code>:<code>That Black Magic</code>.</p>

![image](https://github.com/user-attachments/assets/05a362ef-4dc7-44f1-ac53-963d6ad73c93)

<br>

<p>Discovered the third flag.</p>

![image](https://github.com/user-attachments/assets/b0e35639-5232-4806-b944-d5a7c3e2fba2)


<br>
<br>

> 1.4. <em>Content of flag4 – format is tryhackme{************} Hint : Things can be hidden and hidden things can be unfold with the right passwords.</em>.<a id='1.4'></a>
>> <code><strong>tryhackme{P1ngu1nsRul3!}</strong></code><br>
<br>


<p>Downloaded <code>butler-1.jpg</code> to <code>THM AttackBox</code> using <code>scp</code> command.</p>

![image](https://github.com/user-attachments/assets/f1b14d38-e4f5-43bb-b86e-33ea1f3fb4a3)

<br>

![image](https://github.com/user-attachments/assets/57e478ac-5851-44a1-aded-2f7da8906930)

<br>

![image](https://github.com/user-attachments/assets/f4197379-84f2-4cf2-9724-2defa6da0e3e)


<br>

![image](https://github.com/user-attachments/assets/39bf5404-4c20-4027-a5db-ce29610bf2dc)

<br>


<p>Used <code>steghide</code> and <code>ToKeepASecretSafe</code>.<br>
Extratec <code>secrets.zip</code>.</p>

![image](https://github.com/user-attachments/assets/ef0e7ecd-227d-4a22-a14d-28f98b3cfe67)

<br>






```bash
peppermint-butler@at:~$ scp peppermint-butler@Target_IP:/home/peppermint-butler/butler-1.jpg .
...
peppermint-butler@Target_IP's password: 
butler-1.jpg                                                                                                                                                    100%   84KB 942.4KB/s   00:00    
peppermint-butler@at:~$ 

```

![image](https://github.com/user-attachments/assets/7535e7a3-1a83-4929-a606-ea54e2017885)

<br>


<p>Used <code>find</code> looking for files owned by <code>peppermint-butler</code>.<br>
Discovered <code>/usr/share/xml/steg.txt</code></p>

```bash
peppermint-butler@at:~$ find / -type f -user peppermint-butler 2>/dev/null
/usr/share/xml/steg.txt
/etc/php/zip.txt
/proc/1920/task/1920/fdinfo/0
/proc/1920/task/1920/fdinfo/1
/proc/1920/task/1920/fdinfo/2
/proc/1920/task/1920/fdinfo/255
/proc/1920/task/1920/environ
/proc/1920/task/1920/auxv
/proc/1920/task/1920/status
/proc/1920/task/1920/personality
/proc/1920/task/1920/limits
/proc/1920/task/1920/sched
/proc/1920/task/1920/comm
/proc/1920/task/1920/syscall
/proc/1920/task/1920/cmdline
/proc/1920/task/1920/stat
/proc/1920/task/1920/statm
/proc/1920/task/1920/maps
/proc/1920/task/1920/children
/proc/1920/task/1920/numa_maps
/proc/1920/task/1920/mem
/proc/1920/task/1920/mounts
/proc/1920/task/1920/mountinfo
/proc/1920/task/1920/clear_refs
/proc/1920/task/1920/smaps
/proc/1920/task/1920/smaps_rollup
/proc/1920/task/1920/pagemap
/proc/1920/task/1920/attr/current
/proc/1920/task/1920/attr/prev
/proc/1920/task/1920/attr/exec
/proc/1920/task/1920/attr/fscreate
/proc/1920/task/1920/attr/keycreate
/proc/1920/task/1920/attr/sockcreate
/proc/1920/task/1920/attr/display_lsm
/proc/1920/task/1920/attr/selinux/current
/proc/1920/task/1920/attr/selinux/prev
/proc/1920/task/1920/attr/selinux/exec
/proc/1920/task/1920/attr/selinux/fscreate
/proc/1920/task/1920/attr/selinux/keycreate
/proc/1920/task/1920/attr/selinux/sockcreate
/proc/1920/task/1920/attr/smack/current
/proc/1920/task/1920/attr/apparmor/current
/proc/1920/task/1920/attr/apparmor/prev
/proc/1920/task/1920/attr/apparmor/exec
/proc/1920/task/1920/wchan
/proc/1920/task/1920/stack
/proc/1920/task/1920/schedstat
/proc/1920/task/1920/cpuset
/proc/1920/task/1920/cgroup
/proc/1920/task/1920/oom_score
/proc/1920/task/1920/oom_adj
/proc/1920/task/1920/oom_score_adj
/proc/1920/task/1920/loginuid
/proc/1920/task/1920/sessionid
/proc/1920/task/1920/io
/proc/1920/task/1920/uid_map
/proc/1920/task/1920/gid_map
/proc/1920/task/1920/projid_map
/proc/1920/task/1920/setgroups
/proc/1920/task/1920/patch_state
/proc/1920/fdinfo/0
/proc/1920/fdinfo/1
/proc/1920/fdinfo/2
/proc/1920/fdinfo/255
/proc/1920/environ
/proc/1920/auxv
/proc/1920/status
/proc/1920/personality
/proc/1920/limits
/proc/1920/sched
/proc/1920/autogroup
/proc/1920/comm
/proc/1920/syscall
/proc/1920/cmdline
/proc/1920/stat
/proc/1920/statm
/proc/1920/maps
/proc/1920/numa_maps
/proc/1920/mem
/proc/1920/mounts
/proc/1920/mountinfo
/proc/1920/mountstats
/proc/1920/clear_refs
/proc/1920/smaps
/proc/1920/smaps_rollup
/proc/1920/pagemap
/proc/1920/attr/current
/proc/1920/attr/prev
/proc/1920/attr/exec
/proc/1920/attr/fscreate
/proc/1920/attr/keycreate
/proc/1920/attr/sockcreate
/proc/1920/attr/display_lsm
/proc/1920/attr/selinux/current
/proc/1920/attr/selinux/prev
/proc/1920/attr/selinux/exec
/proc/1920/attr/selinux/fscreate
/proc/1920/attr/selinux/keycreate
/proc/1920/attr/selinux/sockcreate
/proc/1920/attr/smack/current
/proc/1920/attr/apparmor/current
/proc/1920/attr/apparmor/prev
/proc/1920/attr/apparmor/exec
/proc/1920/wchan
/proc/1920/stack
/proc/1920/schedstat
/proc/1920/cpuset
/proc/1920/cgroup
/proc/1920/oom_score
/proc/1920/oom_adj
/proc/1920/oom_score_adj
/proc/1920/loginuid
/proc/1920/sessionid
/proc/1920/coredump_filter
/proc/1920/io
/proc/1920/uid_map
/proc/1920/gid_map
/proc/1920/projid_map
/proc/1920/setgroups
/proc/1920/timers
/proc/1920/timerslack_ns
/proc/1920/patch_state
/proc/2275/task/2275/fdinfo/0
/proc/2275/task/2275/fdinfo/1
/proc/2275/task/2275/fdinfo/2
/proc/2275/task/2275/fdinfo/3
/proc/2275/task/2275/fdinfo/4
/proc/2275/task/2275/fdinfo/5
/proc/2275/task/2275/fdinfo/7
/proc/2275/task/2275/fdinfo/8
/proc/2275/task/2275/fdinfo/9
/proc/2275/task/2275/fdinfo/10
/proc/2275/task/2275/environ
/proc/2275/task/2275/auxv
/proc/2275/task/2275/status
/proc/2275/task/2275/personality
/proc/2275/task/2275/limits
/proc/2275/task/2275/sched
/proc/2275/task/2275/comm
/proc/2275/task/2275/syscall
/proc/2275/task/2275/cmdline
/proc/2275/task/2275/stat
/proc/2275/task/2275/statm
/proc/2275/task/2275/maps
/proc/2275/task/2275/children
/proc/2275/task/2275/numa_maps
/proc/2275/task/2275/mem
/proc/2275/task/2275/mounts
/proc/2275/task/2275/mountinfo
/proc/2275/task/2275/clear_refs
/proc/2275/task/2275/smaps
/proc/2275/task/2275/smaps_rollup
/proc/2275/task/2275/pagemap
/proc/2275/task/2275/attr/current
/proc/2275/task/2275/attr/prev
/proc/2275/task/2275/attr/exec
/proc/2275/task/2275/attr/fscreate
proc/2275/task/2275/attr/keycreate
/proc/2275/task/2275/attr/sockcreate
/proc/2275/task/2275/attr/display_lsm
/proc/2275/task/2275/attr/selinux/current
/proc/2275/task/2275/attr/selinux/prev
/proc/2275/task/2275/attr/selinux/exec
/proc/2275/task/2275/attr/selinux/fscreate
/proc/2275/task/2275/attr/selinux/keycreate
/proc/2275/task/2275/attr/selinux/sockcreate
/proc/2275/task/2275/attr/smack/current
/proc/2275/task/2275/attr/apparmor/current
/proc/2275/task/2275/attr/apparmor/prev
/proc/2275/task/2275/attr/apparmor/exec
/proc/2275/task/2275/wchan
/proc/2275/task/2275/stack
/proc/2275/task/2275/schedstat
/proc/2275/task/2275/cpuset
/proc/2275/task/2275/cgroup
/proc/2275/task/2275/oom_score
/proc/2275/task/2275/oom_adj
/proc/2275/task/2275/oom_score_adj
/proc/2275/task/2275/loginuid
/proc/2275/task/2275/sessionid
/proc/2275/task/2275/io
/proc/2275/task/2275/uid_map
/proc/2275/task/2275/gid_map
/proc/2275/task/2275/projid_map
/proc/2275/task/2275/setgroups
/proc/2275/task/2275/patch_state
/proc/2275/fdinfo/0
/proc/2275/fdinfo/1
/proc/2275/fdinfo/2
/proc/2275/fdinfo/3
/proc/2275/fdinfo/4
/proc/2275/fdinfo/6
/proc/2275/fdinfo/7
/proc/2275/environ
/proc/2275/auxv
/proc/2275/status
/proc/2275/personality
/proc/2275/limits
/proc/2275/sched
/proc/2275/autogroup
/proc/2275/comm
/proc/2275/syscall
/proc/2275/cmdline
/proc/2275/stat
/proc/2275/statm
/proc/2275/maps
/proc/2275/numa_maps
/proc/2275/mem
/proc/2275/mounts
/proc/2275/mountinfo
/proc/2275/mountstats
/proc/2275/clear_refs
/proc/2275/smaps
/proc/2275/smaps_rollup
/proc/2275/pagemap
/proc/2275/attr/current
/proc/2275/attr/prev
/proc/2275/attr/exec
/proc/2275/attr/fscreate
/proc/2275/attr/keycreate
/proc/2275/attr/sockcreate
/proc/2275/attr/display_lsm
/proc/2275/attr/selinux/current
/proc/2275/attr/selinux/prev
/proc/2275/attr/selinux/exec
/proc/2275/attr/selinux/fscreate
/proc/2275/attr/selinux/keycreate
/proc/2275/attr/selinux/sockcreate
/proc/2275/attr/smack/current
/proc/2275/attr/apparmor/current
/proc/2275/attr/apparmor/prev
/proc/2275/attr/apparmor/exec
/proc/2275/wchan
/proc/2275/stack
/proc/2275/schedstat
/proc/2275/cpuset
/proc/2275/cgroup
/proc/2275/oom_score
/proc/2275/oom_adj
/proc/2275/oom_score_adj
/proc/2275/loginuid
/proc/2275/sessionid
/proc/2275/coredump_filter
/proc/2275/io
/proc/2275/uid_map
/proc/2275/gid_map
/proc/2275/projid_map
/proc/2275/setgroups
/proc/2275/timers
/proc/2275/timerslack_ns
/proc/2275/patch_state
/home/peppermint-butler/.bashrc
/home/peppermint-butler/.profile
/home/peppermint-butler/flag3
/home/peppermint-butler/.cache/motd.legal-displayed
/home/peppermint-butler/.bash_logout
/home/peppermint-butler/butler-1.jpg
/home/peppermint-butler/.ssh/known_hosts
peppermint-butler@at:~$ 

```

![image](https://github.com/user-attachments/assets/642e78d7-3fe4-4f78-b91f-a69136064e94)

<br>

<p>Used <code>cat</code> against <code>steg.txt</code>and discovered <code>ToKeepASecretSafe</code>.</p>

![image](https://github.com/user-attachments/assets/c0d1c11a-004e-4dce-9925-a7919727c561)

<br>

<p>Used <code>cat</code> against <code>zip.txt</code>and discovered <code>ThisIsReallySave</code>.</p>

![image](https://github.com/user-attachments/assets/2e9ede6a-df55-4725-8274-cd0e12161c5f)

<br>

<p>Used <code>steghide</code>against <code>butler-1.jpg</code>.<br>
Discovered <code>gunter</code>code> and <code>The Ice King s????</code>.</p>

<br>

```bash
:~/AdventureTime# steghide extract -sf butler-1.jpg
```

<br>

<p>Used <code>file</code> to confirm the file type of <code>secrets.zip</code>.<br>
Used <code>unzip</code> and the password discovered in <code>zip.txt</code>file.</p>

![image](https://github.com/user-attachments/assets/31cd1b6c-92f0-414a-9902-c27efad229b0)

<br>

<p>Used <code>cat</code> against <code>secrets.txt</code>.</p>

![image](https://github.com/user-attachments/assets/2f3fac82-0f5c-4458-8d09-222102cfbf34)

<br>

<p>Navigated to <code>https://scrabblewordfinder.org/5-letter-words-starting-with/s</code> and downloaded a wordlist with 5 letters starting wit <code>s</code>.</p>

![image](https://github.com/user-attachments/assets/87aabda8-5517-4b7d-9dc4-9a0f9723b81a)

<br>


<p>Used <code>hydra</code> and discovered <code>The Ice King sucks</code>.</p>

```bash
:~/AdventureTime# hydra -l gunter -P passwords_gunter.txt ssh://Target_IP
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-03-28 ...
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 3581 login tries (l:1/p:3581), ~224 tries per task
[DATA] attacking ssh://Target_IP/
...
[22][ssh] host: Target_IP   login: gunter   password: The Ice King sucks
1 of 1 target successfully completed, 1 valid password found
```


<p>Used <code>su gunter</code>.</p>

![image](https://github.com/user-attachments/assets/45f3538e-e128-406c-8ec5-7f53abd4f128)


<p>Changed directory and discovered the fourth flag.</p>

![image](https://github.com/user-attachments/assets/b3e8d077-5f9e-4b61-be4d-cb17d3dae9af)

<br>


<br>
<br>

> 1.5. <em>Content of flag5 – format is tryhackme{************}</em>.<a id='1.5'></a>
>> <code><strong>tryhackme{Th1s1s4c0d3F0rBM0}</strong></code><br>
<br>


<p>User <code>gunter</code> can not <code>sudo</code>.</p>

<p>Used <code>find</code> to discover files owned by <code>gunter</code>.</p>

![image](https://github.com/user-attachments/assets/87d7791a-13a0-4fd1-b8f4-695dfc78cc08)

<br>

<p>Ran <code>exim --version</code>.<br>
Version = 4.90_1<br>
Configuration file is <code>/var/lib/exim4/config.autogenerated</code>.</p>

![image](https://github.com/user-attachments/assets/6d16a4d9-0214-4211-aab0-d9977083a432)

<br>

![image](https://github.com/user-attachments/assets/ede7b0b8-a560-4409-a4ca-50ffe2b459a7)



<p>Googled <code>Exploit-DB</code>.<br>
Searched for <code>exim 4.90</code><br>
-->  https://www.exploit-db.com/</p>

<p>Downloaded <code>46974.txt</code> related to <code>CVE-2019-10149</code>.</p>

![image](https://github.com/user-attachments/assets/c5d9dd2a-1ea0-4b90-87a3-636bfeb95aff)

<br>

![image](https://github.com/user-attachments/assets/74ba9a5a-2523-46aa-a26b-758982dbb805)


<br>

![image](https://github.com/user-attachments/assets/32038b5a-305f-480e-b27c-6ef08f7ec9d6)



<p>Opened <code>/etc/exim4/update-exim4.conf.conf</code> using <code>nano</code>.<br>
Discovered: <code>127.0.0.1.60000</code></p>

![image](https://github.com/user-attachments/assets/48f75fdc-c770-46f3-8800-07b611a3378b)



```bash
gunter@at:/etc/exim4$ ls -la
total 108
drwxr-xr-x   3 root root         4096 sep 20  2019 .
drwxr-xr-x 128 root root        12288 sep 23  2019 ..
drwxr-xr-x   9 root root         4096 sep 20  2019 conf.d
-rw-r--r--   1 root root        78843 feb 14  2018 exim4.conf.template
-rw-r-----   1 root Debian-exim   204 feb 14  2018 passwd.client
-rw-r--r--   1 root root         1024 sep 20  2019 update-exim4.conf.conf
gunter@at:/etc/exim4$ nano update-exim4.conf.conf
gunter@at:/etc/exim4$ grep interface update-exim4.conf.conf 
dc_local_interfaces='127.0.0.1.60000'
gunter@at:/etc/exim4

```


<p>Decided to use <code>Metasploit framework.</code> Did not work.</p>

![image](https://github.com/user-attachments/assets/68c5d047-b7d1-4094-befd-e48ccc012cce)

<br>

<p>Used command <code>loginctl</code> to discover the <code>session</code>.</p>

![image](https://github.com/user-attachments/assets/7bd27f52-079b-41d5-8338-cc97492fcca5)


<p>Cloned a repository after dedicating some time researching.<br>
https://raw.githubusercontent.com/AzizMea/CVE-2019-10149-privilege-escalation/master/wizard.py</p>


![image](https://github.com/user-attachments/assets/dc4ff159-d10f-4aa8-a84e-cf8bf7133377)

<br>

![image](https://github.com/user-attachments/assets/7987995f-452c-4005-a7f9-488d99cb6ff7)


<p>...</p>

![image](https://github.com/user-attachments/assets/522b6c6b-5667-4df5-bee4-670c1042e2f8)

<p>...</p>

![image](https://github.com/user-attachments/assets/dae727ed-86e3-422c-8044-7aaaa45054df)


<p>...</p>

![image](https://github.com/user-attachments/assets/ec921fba-f8ab-427e-9b2f-7d9b54501360)

<br><br>


<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/9027c22e-9bcf-46cb-b10e-4956af734ad0"> </p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/a48de6c1-0a4a-474b-9ffd-4fceb1b2f4f7"> </p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$
</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |           |
| March 27, 2025    | 325      |     338ᵗʰ    |        8ᵗʰ   |   473ʳᵈ     |     7ᵗʰ    |  88,606  |       631 |   59      |

</div>

<p align="center"> Global All Time:  338ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/6d2b5da4-5dd6-4cb4-8e62-f073f553bcba"> </p>


<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/17d1280b-251c-4112-bf2e-817767dd6e14"> </p>


<p align="center"> Global monthly: 473ʳᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/31ccfa6d-dbad-4a7c-a722-836d52ad62bc"> </p>

<p align="center"> Brazil monthly: 7ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/fa9661cd-de26-4437-bb9b-8d120c24f2c0"> </p>

