<h1 align="center">Lumberjack Turtle</h1>
<p align="center"><img width="80px" src=""><br>
July 3, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>423</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>No logs, no crime... so says the lumberjack.</em>.<br>
Access it <a href="https://tryhackme.com/room/lumberjackturtle"</a>here.<br>
<img width="1200px" src=""></p>

<br>




<br>

<h3>Nmap</h3>
<p>
  
- <code>22/ssh/OpenSSH 7.6p1</code><br>
- <code>80/nagios-nsca</code></p>

```bash
:~/LumberjackTurtle# nmap -sC -sV -p- -T5 10.10.121.55
...
PORT   STATE SERVICE     VERSION
22/tcp open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  nagios-nsca Nagios NSCA
|_http-title: Site doesn't have a title (text/plain;charset=UTF-8).
MAC Address: 02:17:76:BE:0E:C9 (Unknown)
...
```

<h3>dirb</h3>

<p>

- <code>/~logs</code><br>
- <code>/error</code></p>

```bash
:~/LumberjackTurtle# dirb http://lumberjackturtle.thm
...
URL_BASE: http://lumberjackturtle.thm/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://lumberjackturtle.thm/ ----
+ http://lumberjackturtle.thm/~logs (CODE:200|SIZE:29)                                                                                                                  
+ http://lumberjackturtle.thm/error (CODE:500|SIZE:73)                                                                                                                  
```

<p>- <code>/log4j</code></p>

```bash
:~/LumberjackTurtle# dirb http://lumberjackturtle.thm/~logs
...
URL_BASE: http://lumberjackturtle.thm/~logs/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                                                                           

---- Scanning URL: http://lumberjackturtle.thm/~logs/ ----
+ http://lumberjackturtle.thm/~logs/log4j (CODE:200|SIZE:47)                                                                                                           
```

```bash
:~/LumberjackTurtle# dirsearch -u http://lumberjackturtle.thm/~logs/ -w /usr/share/dirb/wordlists/common.txt

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 4613

Output File: /root/LumberjackTurtle/reports/http_lumberjackturtle.thm/_~logs__25-07-03_23-30-45.txt

Target: http://lumberjackturtle.thm/

[...] Starting: ~logs/
[...] 200 -   47B  - /~logs/log4j

Task Completed
                                                                                                    
```

<p>- <code>/log4j</code></p>

```bash
:~/LumberjackTurtle# dirb http://lumberjackturtle.thm/~logs
...
URL_BASE: http://lumberjackturtle.thm/~logs/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                                                                           

---- Scanning URL: http://lumberjackturtle.thm/~logs/ ----
+ http://lumberjackturtle.thm/~logs/log4j (CODE:200|SIZE:47)                                                                                                           
```


![image](https://github.com/user-attachments/assets/f47a9ec8-c63c-4bdf-87e8-39a471166b4b)

![image](https://github.com/user-attachments/assets/99a9cb28-94c2-43fd-8482-13a47eb36576)

<br>

<h3><code>CVE-2021-44228</code> in <code>X-Api-Version</code></h3>

![image](https://github.com/user-attachments/assets/b0fce418-0531-4a0d-aef9-9558d14f8cd3)

![image](https://github.com/user-attachments/assets/53d458c3-14ee-4ddf-8fe5-b07c6faaf279)

<br>

<h3>maven</h3>


![image](https://github.com/user-attachments/assets/c448eedf-ceeb-4223-955a-41b74c3dca2f)

```bash
:~/LumberjackTurtle# sudo apt install maven
Reading package lists... Done
Building dependency tree       
Reading state information... Done
...                                                                                                   
```

