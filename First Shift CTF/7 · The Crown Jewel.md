<h1 align="center"><a href="https://tryhackme.com/room/first-shift-ctf">First Shift CTF</a> &nbsp;&nbsp; · &nbsp;&nbsp; The Crown Jewel</h1>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/98ca2808-1bc3-4f50-8209-00b36a0e2c4a"></h6>

<p align="center">If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2029-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<h2>The Crown Jewel</h2>
<p>You are on a shift, looking at the new alert coming from Imperium Labs - a company under MSSP monitoring long before you joined the team. It's hard to say what the company's primary focus is, but it has a global presence and undoubtedly has secrets to protect, especially those on heavily secured GitLab and Jira servers which store proprietary source code and project data.</p>

<h2>The Alert</h2>
<p>The alert you are looking at is called <code>Reverse Shell Outbound Connection Detected</code>, not something you see every day. Fortunately, you were able to obtain the raw PCAPs and Splunk logs for this event. Can you analyze the network traffic and logs to reconstruct and stop a sophisticated attack aimed at stealing the "Crown Jewel" data?</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/7940024e-a86d-4d9b-a3ef-7240215bcc29"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>


<h2>Machine Access</h2>
<p>To access the VM, click the Start Machine button below. Please give the VM up to five minutes to start and piece together the attack chain:

- Detailed network traffic capture <code>challenge.pcap</code> that you can find on the <code>network_traffic</code> folder on the VM's Desktop<br>
- Pre-ingested Splunk logs (<code>index=network_logs</code>), which can be accessed at <code>MACHINE_IP:8000</code></p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p><em>Answer the questions below</em></p>

<br>
<p>7.1. <em>From which internal IP did the suspicious connection originate?)</em><br>
<code>10.10.10.100</code></p>

<br>
<p>7.2. <em>What outbound connection was detected as a C2 channel? (Answer example: 1.2.3.4:9996)</em><br>
<code>1.1.1.1:8080</code></p>

<img width="984" height="213" alt="image" src="https://github.com/user-attachments/assets/b433e23d-129b-4d07-a8c5-0aa470e3cb3e" />

<br>
<br>

<img width="1295" height="457" alt="image" src="https://github.com/user-attachments/assets/83055314-2623-4ed4-97fe-f40c024a9eec" />

<br>
<br>
<br>
<p>7.3. <em>Which MAC address is impersonating the gateway 10.10.10.1?</em><br>
<code>00:0c:29:11:22:33</code></p>

<img width="1300" height="307" alt="image" src="https://github.com/user-attachments/assets/f775d9cd-ac68-4cd5-858c-4b958e663e07" />

<br>
<br>
<br>
<p>7.4. <em>What is the non-standard User-Agent hitting the Jira instance?</em><br>
<code>CVE-202X-EXPLOIT</code></p>

```bash
index=network_logs extracted_host=jira
|  sort by +_time
```

<img width="1261" height="292" alt="image" src="https://github.com/user-attachments/assets/779b62ac-f4de-46b7-88b4-e177f1162dcc" />

<br>
<br>

<img width="1150" height="696" alt="image" src="https://github.com/user-attachments/assets/0cb7930e-7628-420e-b95f-e6939e410cc1" />

<br>
<br>

```bash
index=network_logs extracted_host=jira   "event.agent"="CVE-202X-EXPLOIT" 
| sort by +_time
```

<img width="1147" height="638" alt="image" src="https://github.com/user-attachments/assets/5f60571e-c15c-4532-af5c-9fbd9ee4ebf2" />

<br>
<br>
<br>
<p>7.5. <em>How many ARP spoofing attacks were observed in the PCAP?</em><br>
<code>90</code></p>

<br>
<p>7.6. <em>What's the payload containing the plaintext creds found in the POST request?</em><br>
<code>username=dev_user&password=SecretPassword!</code></p>

<img width="1248" height="570" alt="image" src="https://github.com/user-attachments/assets/faff1792-46bb-41a5-a6d0-bc0ca871db4e" />

<br>
<br>

<img width="1235" height="473" alt="image" src="https://github.com/user-attachments/assets/2ae03baf-b167-4ef7-88a9-0d006ea605f0" />

<br>
<br>
<br>
<p>7.7. <em>What domain, owned by the attacker, was used for data exfiltration?</em><br>
<code>exfil-domain.xyz</code></p>

<img width="1291" height="216" alt="image" src="https://github.com/user-attachments/assets/e1c806f2-92ea-44a5-a90c-292065009f82" />

<br>
<br>
<br>
<p>7.8. <em>After examining the logs, which protocol was used for data exfiltration?</em><br>
<code>dns</code></p>

<img width="1295" height="748" alt="image" src="https://github.com/user-attachments/assets/2489d4cc-4114-4f0f-a08d-e4e859580a40" />

<br>
<br>
<h1 align="center">Walkthrough Room Completed</h1>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/1a97bbd4-ee29-4fe4-8c5f-a40c3dd21b1f"><br>
                  <img width="700px" src="https://github.com/user-attachments/assets/293b1a54-f4e8-4ea5-aa2f-d1ae36980a8e"></p>

                
<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|29     |Medium 🚩 - First Shift CTF           |28|      61ˢᵗ  |     3ʳᵈ    |       66ᵗʰ   |        2ⁿᵈ     |    144,624  |    1,075    |    90     |
|27     |Medium 🔗 - GeoServer: CVE-2025-58360 |26 |     67ᵗʰ  |     3ʳᵈ    |       73ʳᵈ   |        2ⁿᵈ     |    144,174  |    1,074    |    90     |
|26     |Medium 🚩 - First Shift CTF, in progress|25|    66ᵗʰ  |     3ʳᵈ    |       73ʳᵈ   |        2ⁿᵈ     |    144,102  |    1,073    |    90     |
|25     |Medium 🔗 - MS Entra ID: Zero Trust   |24 |     70ᵗʰ  |     3ʳᵈ    |       79ᵗʰ   |        2ⁿᵈ     |    143,292  |    1,073    |    88     |
|24     |Medium 🚩 - First Shift CTF, in progress|23|    70ᵗʰ  |     3ʳᵈ    |       76ᵗʰ   |        2ⁿᵈ     |    143,104  |    1,072    |    88     |
|24     |Easy ⚔️ - Health Hazard               |23 |     78ᵗʰ  |     3ʳᵈ    |       94ᵗʰ   |        2ⁿᵈ     |    142,264  |    1,072    |    88     |
|23     |Medium ⚙️ - BlackCat                  |22 |     79ᵗʰ  |     3ʳᵈ    |      104ᵗʰ   |        2ⁿᵈ     |    142,189  |    1,072    |    88     |
|22     |Hard 🚩 - Azure: Tapper               |21 |     82ⁿᵈ  |     3ʳᵈ    |      176ᵗʰ   |        2ⁿᵈ     |    141,154  |    1,072    |    88     |
|22     |Easy ⚙️ - Hidden Hooks                |21 |     82ⁿᵈ  |     3ʳᵈ    |      189ᵗʰ   |        3ʳᵈ     |    141,059  |    1,071    |    88     |
|22     |Medium 🔗 - ret2libc                  |21 |     82ⁿᵈ  |     3ʳᵈ    |      193ʳᵈ   |        3ʳᵈ     |    140,979  |    1,071    |    88     |
|20     |Easy 🔗 - MS Entra ID: Hybrid Identities|19|    82ⁿᵈ  |     3ʳᵈ    |      184ᵗʰ   |        2ⁿᵈ     |    140,971  |    1,069    |    88     |
|19     |Easy ⚙️ - Upload and Conquer          |18 |     81ˢᵗ  |     3ʳᵈ    |      181ˢᵗ   |        2ⁿᵈ     |    140,859  |    1,068    |    88     |
|18     |Easy 🔗 - MS Entra ID: Identities     |17 |     83ʳᵈ  |     3ʳᵈ    |      341ˢᵗ   |        3ʳᵈ     |    139,864  |    1,068    |    88     |
|18     |Easy ⚙️ - APT28: Initial Access       |17 |     84ᵗʰ  |     3ʳᵈ    |      341ˢᵗ   |        3ʳᵈ     |    139,752  |    1,067    |    88     |
|18     |Easy ⚙️ - Hidden Hooks                |17 |           |     3ʳᵈ    |              |                |             |    1,067    |    88     |
|17     |Easy 🔗 - MS Entra ID: Introduction   |17 |     83ʳᵈ  |     3ʳᵈ    |      359ᵗʰ   |        3ʳᵈ     |    139,657  |    1,067    |    88     |
|17     |Easy ⚙️ - APT28: Credential Access    |17 |           |     3ʳᵈ    |              |                |             |    1,067    |    88     |
|17     |Medium ⚙️ - Open Door                 |17 |           |     3ʳᵈ    |              |                |             |     1,067   |    88     |
|17     |Easy 🔗 - Offensive Security Intro    |16 |     87ᵗʰ  |     3ʳᵈ    |      504ᵗʰ   |        5ᵗʰ     |    139,099  |    1,067    |    88     |
|16     |Hard 🚩 - Spring                      |15 |     87ᵗʰ  |     3ʳᵈ    |      540ᵗʰ   |        4ᵗʰ     |    138,942  |    1,066    |    87     |
|14     |Insane 🚩 - Scheme Catcher            |13 |     87ᵗʰ  |     3ʳᵈ    |      534ᵗʰ   |        5ᵗʰ     |    138,822  |    1,065    |    87     |
|13     |Hard 🚩 - Breachblocker Unlocker      |12 |     86ᵗʰ  |     3ʳᵈ    |      526ᵗʰ   |        5ᵗʰ     |    138,732  |    1,064    |    87     |
|11     |Medium 🚩 - Azure: Eyes Wide Shut     |10 |     86ᵗʰ  |     3ʳᵈ    |      558ᵗʰ   |        5ᵗʰ     |    138,450  |    1,063    |    86     |
|8      |Medium ⚙️ - Phishing Unfolding        | 7 |     86ᵗʰ  |     3ʳᵈ    |      508ᵗʰ   |        4ᵗʰ     |    138,372  |    1,062    |    84     |
|8      |Easy ⚙️ - Introduction to Phishing    | 7 |     96ᵗʰ  |     3ʳᵈ    |    2,479ᵗʰ   |       32ⁿᵈ     |    137,117  |    1,062    |    84     |
|8      |Medium 🔗 - KaffeeSec - SoMeSINT      | 7 |     98ᵗʰ  |     3ʳᵈ    |    2,847ᵗʰ   |       38ᵗʰ     |    137,052  |    1,062    |    84     |
|7      |Hard 🚩 - Hack Back                   | 6 |     98ᵗʰ  |     3ʳᵈ    |    2,798ᵗʰ   |       37ᵗʰ     |    136,908  |    1,061    |    84     |
|7      |Hard 🚩 - Dead End?                   | 6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     | 5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   | 3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence| 2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  | 1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |

</h6></div><br>

<p align="center">Global All Time:     61ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/d8d09c13-04f6-4a7a-9d81-160631af9c0e"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/c71db723-f0b0-4c0a-8aca-762fe878e23e"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/bc78c11a-43d5-48ab-932e-4ae9762620fd"><br><br>
                  Global monthly:      66ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/e6627d0d-797b-43d3-a811-f875954c4d97"><br><br>
                  Brazil monthly:       2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/19699f5c-481f-4609-bf0e-209191ccb787"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
