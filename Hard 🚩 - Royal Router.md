<h1 align="center">Royal Router</h1>
<p align="center"><img width="80px" src="   "><br>
2025, September 13<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>495</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>You will learn how to compromise an IoT device</em>.<br>
Access it <a href="https://tryhackme.com/room/hfb1royalrouter">here</a>.<br>
<img width="1200px" src=""></p>

<h1>Task 1 ...</h1>


<h6 align="center"><img width="200px" src=""><br>TryHackMe</h6>

<p><em>Answer the question below</em></p>
<br>

<br>


<br>

<h3>nmap</h3>

```bash
:~/RoyalRouter# nmap -p- -vv TargetIP
...
PORT      STATE SERVICE REASON
22/tcp    open  ssh     syn-ack ttl 64
23/tcp    open  telnet  syn-ack ttl 63
80/tcp    open  http    syn-ack ttl 63
9999/tcp  open  abyss   syn-ack ttl 63
20443/tcp open  unknown syn-ack ttl 63
24433/tcp open  unknown syn-ack ttl 63
28080/tcp open  unknown syn-ack ttl 63
50628/tcp open  unknown syn-ack ttl 63
```

```bash
:~/RoyalRouter# nmap -sC -sV -Pn -T4 -p22,23,80,9999,20443,24433,28080,50628 TargetIP
...
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 8.9p1 Ubuntu 3ubuntu0.13 (Ubuntu Linux; protocol 2.0)
23/tcp    open  tcpwrapped
80/tcp    open  http       DD-WRT milli_httpd
|_http-server-header: httpd
|_http-title: D-LINK CORPORATION, INC | WIRELESS ROUTER | LOGIN
9999/tcp  open  tcpwrapped
20443/tcp open  tcpwrapped
24433/tcp open  tcpwrapped
28080/tcp open  tcpwrapped
50628/tcp open  tcpwrapped
```

<h3>DD-WRT milli-httpd</h3>

<img width="660" height="152" alt="image" src="https://github.com/user-attachments/assets/3ea97c48-a543-4b93-a1e8-3ac45e8faa46" />


<h3>searchploit</h3>

```bash
:~/RoyalRouter# searchsploit DD-WRT
------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                               |  Path
------------------------------------------------------------------------------------------------------------- ---------------------------------
DD-WRT - Site Survey SSID Script Injection                                                                   | multiple/remote/32189.py
DD-WRT 24-preSP2 - Information Disclosure                                                                    | hardware/remote/15842.txt
DD-WRT 45723 - UPNP Buffer Overflow (PoC)                                                                    | hardware/dos/49730.py
DD-WRT HTTP v24-SP1 - Command Injection                                                                      | linux/remote/10030.rb
DD-WRT HTTPd Daemon/Service - Arbitrary Command Execution (Metasploit)                                       | cgi/webapps/16856.rb
DD-WRT HTTPd Daemon/Service - Remote Command Execution                                                       | hardware/remote/9209.txt
DD-WRT v24-sp1 - Cross-Site Reference Forgery                                                                | hardware/remote/7389.html
------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

```bash
:~/RoyalRouter#  searchsploit -m /hardware/remote/9209.txt
  Exploit: DD-WRT HTTPd Daemon/Service - Remote Command Execution
      URL: https://www.exploit-db.com/exploits/9209
     Path: /opt/exploitdb/exploits/hardware/remote/9209.txt
    Codes: OSVDB-57143, CVE-2009-2766, CVE-2009-2765, OSVDB-55990, CVE-2008-6975, OSVDB-55636, CVE-2008-6974
...
:~/RoyalRouter# ls
9209.txt
```

<br>

<img width="976" height="334" alt="image" src="https://github.com/user-attachments/assets/c7d95861-803f-4432-859e-a27e9dca2f99" />


<H3>TargetIP</H3>

<img width="1074" height="351" alt="image" src="https://github.com/user-attachments/assets/83d28eaa-ae14-4826-af9c-d246f85e8971" />



```bash

```

