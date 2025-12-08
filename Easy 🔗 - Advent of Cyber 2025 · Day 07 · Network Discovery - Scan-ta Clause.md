<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 7 &nbsp;&nbsp; ·  &nbsp;&nbsp; Network Discovery - Scan-ta Clause</h3>
<p align="center">2025, December 7  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Discover how to scan network ports and uncover what is hidden behind them. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/networkservices-aoc2025-jnsoqbxgky">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/94608e60-8fcf-4a09-b96e-d2b0c57ba620"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/1d2d805c-a943-41f6-8bd0-3326ae9b69f6"></p>


<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/1959e343-fc99-4041-a3aa-6703f0d5635b"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<br>
<p><em>Answer the question below</em></p>

<p>1.1. <em>I have successfully launched the target machine and the AttackBox.</em></p>
<code>No answer needed</code></p>

<br>
<h2>Task 2 &nbsp; ·  &nbsp; Discover Network Services</h2>
<br>
<p><em>Answer the questions below</em></p>

<p>2.1. <em>What evil message do you see on top of the website?</em></p>
<code>Pwned by HopSec</code></p>

```bash
:~# nmap -p- -T5 10.65.163.202
...
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
21212/tcp open  trinket-agent
25251/tcp open  unknown
```

<img width="1119" height="115" alt="image" src="https://github.com/user-attachments/assets/bf998bec-6645-4940-9485-ce86aec9f7b8" />

```bash
:~# ftp 10.65.163.202 21212
Connected to 10.65.163.202.
220 (vsFTPd 3.0.5)
Name (10.65.163.202:root): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp            13 Oct 22 16:27 tbfc_qa_key1
226 Directory send OK.
ftp> get tbfc_qa_key1
local: tbfc_qa_key1 remote: tbfc_qa_key1
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for tbfc_qa_key1 (13 bytes).
226 Transfer complete.
13 bytes received in 0.00 secs (16.5089 kB/s)
ftp> exit
221 Goodbye.
```

```bash
:~# cat tbfc_qa_key1
KEY1:3aster_
```

<p>2.2. <em>What is the first key part found on the FTP server?</em></p>
<code>3aster_</code></p>


```bash
:~# nc 10.65.163.202 25251
TBFC maintd v0.2
Type HELP for commands.
HELP    
Commands: HELP, STATUS, GET KEY, QUIT
GET KEY
KEY2:15_th3_
QUIT
bye
```

<p>2.3. <em>What is the second key part found in the TBFC app?</em><br>
<code>15_th3_</code></p>

```bash
:~# nmap -sU 10.65.163.202
...
PORT   STATE SERVICE
53/udp open  domain
```

<p>2.4. <em>What is the second key part found in the TBFC app?</em><br>
<code>15_th3_</code></p>

```bash
:~# dig @10.65.163.202 TXT key3.tbfc.local +short
"KEY3:n3w_xm45"
```


<img width="1113" height="302" alt="image" src="https://github.com/user-attachments/assets/7d371b25-f14c-4361-8957-082b27ba2373" />

<br>
<br>
<p>2.5. <em>Which port was the MySQL database running on?</em><br>
<code>3306</code></p>

<br>
<p>2.6. <em>Which port was the MySQL database running on?</em><br>
<code>THM{4ll_s3rvice5_d1sc0vered}</code></p>

<img width="1290" height="511" alt="image" src="https://github.com/user-attachments/assets/18d14563-0472-442c-86ee-541427a2fc7a" />

<br>
<br>
<p>2.7. <em>If you enjoyed today's room, feel free to check out the Nmap: The Basics room.</em><br>
<code>No answer needed</code></p>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/bbcd761a-3e75-4195-b396-27a0c92bcd9e"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/def500ce-48ff-40fd-bdb6-7b78a7251c7e"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/6bcb5f58-a600-4531-a6b8-58b5d91c588d"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|7       |Easy 🔗 - Network Discovery - Scan-ta Clause.md|2|    95ᵗʰ    |     3ʳᵈ    |   18,575ᵗʰ   |      208ᵗʰ     |    134,522  |    1,033    |    84     |
|7       |Easy 🔗 - React2Shell: CVE-2025-55182 |  2     |      95ᵗʰ    |     3ʳᵈ    |   28,593ʳᵈ   |      326ᵗʰ     |    134,474  |    1,032    |    81     |
|6       |Medium 🔗 - IDOR - Santa´s Little IDOR|  1     |      95ᵗʰ    |     3ʳᵈ    |   27,309ᵗʰ   |      328ᵗʰ     |    134,450  |    1,031    |    81     |
|6       |Easy 🔗 - AI in Security - old sAInt nick|  1  |      95ᵗʰ    |     3ʳᵈ    |   41,626ᵗʰ   |      526ᵗʰ     |    134,426  |    1,030    |    81     |
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?|  1  |      95ᵗʰ    |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas   |   1    |      96ᵗʰ    |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells    |   1    |      97ᵗʰ    |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>


<p align="center">Global All Time:     95ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/3936405c-c2ef-40ef-a903-419f43bf2038"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/802d9f65-a78f-4c10-b0ae-809f1e8e542b"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/b904fde5-2d02-4282-b45d-3c4c6aa032a5"><br><br>
                  Global monthly:  18,575ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/ff9824a2-c87e-43e8-9ca2-17cc8edd4ba0"><br><br>
                  Brazil monthly:     208ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/6fbd23c0-71cd-4a1a-8057-2bf1f990d5bd"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>


