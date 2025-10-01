<h1 align="center">Network Discovery Detection</h1>
<p align="center">2025, October 1<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>479</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Understand how attackers discover assets in a network, and how to detect that activity</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/ed94084a-a1da-47fa-ab6c-56c9b8fcfd07"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/networkdiscoverydetection">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/9f78f041-cbb7-4e20-8f74-5031bf5c87b6"></p>

<h2>Task 1 . Introduction</h2>
<br>

<p><em>Answer the question below</em></p>

<p>1.1 Let´s begin<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Network Discovery</h2>
<br>

<p><em>Answer the question below</em></p>

<p>2.1 What do attackers scan, other than, IP addresses, ports, and OS version, in order to identify vulnerabilities in a network?<br>
<code>Services</code></p>

<br>
<h2>Task 3 . External vs Internal Scanning</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>3.1 Which file contains logs that showcase internal scanning activity?<br>
<code>log-session-2.csv</code></p>

```bash
ubuntu@tryhackme:~/Downloads/logs$ grep -oE '\b192\.168\.230\.[0-9]{1,3}\b' log-session-2.csv | sort -u
192.168.230.1
192.168.230.127
192.168.230.145
```

<img width="993" height="230" alt="image" src="https://github.com/user-attachments/assets/7af04af7-a3c8-4531-93f8-9d364bb0edfe" />

<br>
<br>
<br>
<p>3.2. How many log entries are present for the internal IP performing internal scanning activity?<br>
<code>2276</code><br>
  
```bash
ubuntu@tryhackme:~/Downloads/logs$ cat log-session-2.csv | cut -d "," -f3 | uniq -c
      1 "source.port"
   2276 "192.168.230.127"
```  

<br>
<p>3.3. What is the external IP address that is performing external scanning activity?<br>
<code>203.0.113.25</code>

<img width="995" height="110" alt="image" src="https://github.com/user-attachments/assets/12d5856c-0e82-42e6-88dc-2721c77c2704" />

<br>
<br>
<br>
<h2>Task 4 . Horizontal vs Vertical Scanning</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>4.1 One of the log files contains evidence of a horizontal scan. Which IP range was scanned? Format X.X.X.X/X<br>
<code>203.0.113.0/24</code></p>

```bash
:~/Downloads/logs$ grep -oE '\b203\.0\.113\.[0-9]{1,3}\b' log-session-2.csv | sort -u
203.0.113.10
203.0.113.100
203.0.113.101
203.0.113.102
203.0.113.103
203.0.113.104
203.0.113.105
203.0.113.106
203.0.113.107
203.0.113.108
203.0.113.109
203.0.113.11
203.0.113.110
203.0.113.111
203.0.113.112
...
```  

<img width="994" height="489" alt="image" src="https://github.com/user-attachments/assets/e43df8b1-1c8f-472e-bc72-aa87afd8be30" />

<br>
<br>
<br>
<p>4.2. In the same log file, there is one IP address on which a vertical scan is performed. Which IP address is this?<br>
<code>192.168.230.145</code></p>

```bash
ubuntu@tryhackme:~/Downloads/logs$ grep -oE '\b192\.168\.230\.[0-9]{1,3}\b' log-session-2.csv | sort -u
192.168.230.1
192.168.230.127
192.168.230.145
```  

<img width="993" height="126" alt="image" src="https://github.com/user-attachments/assets/dcd033b9-257b-45cd-8aea-21c5032e888e" />

<br>
<br>
<br>
<p>4.3. On one of the IP addresses, only a few ports are scanned which host common services. Which are the ports that are scanned on this IP address? Format: port1, port2, port3 in ascending order.<br>
<code>80, 445, 3389</code></p>

```bash
ubuntu@tryhackme:~/Downloads/logs$ cat log-session-2.csv | cut -d "," -f5,6 | grep -v "203.0" | grep -v "230.145" | sort | uniq -c
      2 "192.168.230.1","-"
      2 "192.168.230.1",0
      2 "192.168.230.1",3389
      2 "192.168.230.1",445
      1 "192.168.230.1",80
      1 "239.255.255.250",3702
      1 "destination.port","rule.name"
```  

<img width="1198" height="180" alt="image" src="https://github.com/user-attachments/assets/372c6bf2-e09a-4378-9a36-257b163eedab" />

<br>
<br>
<br>
<h2>Task 5 . The Mechanism of Scanning</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>5.1. Which source IP performs a ping sweep attack across a whole subnet?<br>
<code>192.168.230.127</code></p>

```bash
ubuntu@tryhackme:~/Downloads/logs$ cat log-session-1.csv | cut -d "," -f3,4 | grep -v "PING" | sort | uniq -c
   1004 "203.0.113.25",39118
   1003 "203.0.113.25",39120
      1 "203.0.113.25",43524
      3 "203.0.113.25",49033
      3 "203.0.113.25",49035
      1 "source.port","destination.ip"
```

```bash
ubuntu@tryhackme:~/Downloads/logs$ cat log-session-2.csv | cut -d "," -f3,4 | grep -v "PING" | sort | uniq -c
      2 "192.168.230.127","-"
      3 "192.168.230.127",41482
      3 "192.168.230.127",41484
      1 "192.168.230.127",45671
      1 "192.168.230.127",45673
      6 "192.168.230.127",52422
      5 "192.168.230.127",52424
      1 "192.168.230.127",55787
    999 "192.168.230.127",64703
    999 "192.168.230.127",64705
    256 "192.168.230.127",8
      1 "source.port","destination.ip"
```  

<img width="1265" height="492" alt="image" src="https://github.com/user-attachments/assets/521e782c-e426-4e21-8ac8-bbdcf3da7e1a" />

<br>
<br>
<br>

<img width="1191" height="379" alt="image" src="https://github.com/user-attachments/assets/c97a013e-07b9-4768-82fa-0fe62a3563b9" />

<br>
<br>
<br>

<p>5.2. The zeek.conn.conn_state value shows the connection state. Using the information provided by this value, identify the type of scan being performed by 203.0.113.25 against 192.168.230.145<br>
<code>TCP SYN Scan</code></p>

<img width="1263" height="498" alt="image" src="https://github.com/user-attachments/assets/08d36e31-517e-4cd1-96cf-68acd980870c" />

<br>
<br>
<br>

```bash
ubuntu@tryhackme:~/Downloads/logs$ grep -v '203.0.113.25' log-session-2.csv | grep -v '192.168.230.145' | cut -d "," -f18 | sort | uniq -c
```

<img width="1191" height="174" alt="image" src="https://github.com/user-attachments/assets/ee6093b2-eeba-4a92-be62-f5aa3fbefe86" />

<br>
<br>
<br>

<img width="1264" height="508" alt="image" src="https://github.com/user-attachments/assets/ba430077-5559-4799-9e06-d5cc8eeb7a0a" />

<br>
<br>
<br>

<img width="1265" height="668" alt="image" src="https://github.com/user-attachments/assets/cffaa825-80a2-494c-ba4d-d12a85cbe66c" />

<br>
<br>
<br>

<p>5.3. Is there any UDP scanning attempt in the logs? Y/N<br>
<code>N</code></p>

<br>
<h2>Task 6 . Conclusion</h2>
<p>And that's all for this room. In this room, we have learned:<br>

- What is network discovery<br>
- The difference between external and internal scanning, and the severity on each.<br>
- Port scanning and host scanning, and why each of those is performed.<br>
- How different types of scans are performed at a more granular room.<br>

For further study, you can head on to the MiTM detection room. How did you find this room? Let us know in our Discord channel or X account. See you around.</p>

<p><em>Answer the question below</em></p>

<p>6.1. Heading to the next room!<br>
<code>No answer needed</code></p>

<br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/1d43cb5c-949b-4ffb-9d88-322868398648"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/1b9df090-cac2-4bec-93b9-eeb89748b8ee"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    73     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    73     |

</h6></div>
<br>

<p align="center">Global All Time:   108ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/99945b28-a35f-4398-be5c-3358c3251610"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/f3e3ed45-d943-42d6-a6f8-ce9802907594"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d3cf92f0-9efd-4fac-9e4a-7d429e17e8ed"><br>
                  Global monthly:    875ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/518063ae-7a99-4d14-a628-fd0367e9324f"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/4c63f889-8fa5-4c13-8f99-d59e19ec0a08"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
