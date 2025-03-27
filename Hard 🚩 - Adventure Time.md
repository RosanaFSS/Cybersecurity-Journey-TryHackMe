
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

> 1.1. <em>What type of accounts are used by the Windows operating system and various apps?</em>.<a id='1.1'></a>
>> <code><strong>System and Service Accounts</strong></code><br>

<p>I started enumerating with nmap.</p>

<ul style="list-style-type:square">
    <li><code>-sC</code>: is equivalent to <code>--scritp=default</code>.</li>
    <li><code>-sV</code>: Probe open ports to determine service/version info.</li>
    <li><code>-sS</code>: TCP SYN.</li>
    <li><code>-Pn</code>: Treat all hosts as online.</li>
    <li><code>-O</code> : Enable OS detection.</li>
    <li><code>-p-</code>: Scan all ports.</li>
</ul></p>

<p>Identified 5 ports open.</p>

<ul style="list-style-type:square">
    <li><code>21</code>: ftp with <code>Anonymous</code> allowed.</li>
    <li><code>22</code>: ssh.</li>
    <li><code>80</code>: http.</li>
    <li><code>443</code>: ssl/http.</li>
    <li><code>31337</code> : Elite?.</li>
    <li><code>-p-</code>: Scan all ports.</li>
</ul></p>

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

<br>

> 1.2. <em>What centrally manages local user accounts and domain accounts?</em>.<a id='1.2'></a>
>> <code><strong>Domain Controller</strong></code>

<br>
