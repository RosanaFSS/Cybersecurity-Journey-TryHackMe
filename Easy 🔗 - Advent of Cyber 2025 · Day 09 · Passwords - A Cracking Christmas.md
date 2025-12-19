<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 9 &nbsp;&nbsp; ·  &nbsp;&nbsp; Passwords - A Cracking Christmas</h3>
<p align="center">2025, December 19  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in <a href="https://tryhackme.com">TryHackMe</a>.<br>Learn how to crack password-based encrypted files. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/attacks-on-ecrypted-files-aoc2025-asdfghj123">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/012eb2a4-97c8-4d38-b86c-857921a1d963"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/fb90ca90-d95d-4f14-ae5f-1ea6d27cf89e"></p>

<br>
<br>

<h2 align="center">Check out my upcoming walkthrough on Medium!</h2>

<br>
<br>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>


<br>
<p><em>Answer the question below</em></p>

<p>1.1. <em>I have successfully started the target machine in split view, or connected via the THM VPN and SSH!</em><br>
<code>No answer needed</code></p>

<img width="1358" height="673" alt="image" src="https://github.com/user-attachments/assets/5fac8f84-6da6-4b9b-9392-47f41df9216d" />

<br>
<br>
<h2>Task 2 &nbsp; ·  &nbsp; Attacks Against Encrypted Files</h2>

<h3>How Attackers Recover Weak Passwords</h3>

<h4>Dictionary Attacks</h4>

<h4>Mask Attacks</h4>

<h3>Detection of Indicators and Telemetry</h3>

<h4>GPU and Resource Artefacts</h4>

<h4>Network Hints, Light but Useful</h4>

<h4>Unsual File Reads</h4>

<h4>Detections</h4>

<h4>Response Playbook</h4>


<br>
<p><em>Answer the questions below</em></p>

<p>2.1. <em>What is the flag inside the encrypted PDF?</em><br>
<code>THM{Cr4ck1ng_PDFs_1s_34$y}</code></p>
<br>

```bash
ubuntu@tryhackme:~$ pwd
```

```bash
ubuntu@tryhackme:~$ cd Desktop
```

```bash
ubuntu@tryhackme:~/Desktop$ ls
```

<img width="1260" height="146" alt="image" src="https://github.com/user-attachments/assets/0b7589b8-4a45-48a4-9d5f-96a72365c6bf" />

<br>
<br>
<br>
<br>

```bash
ubuntu@tryhackme:~/Desktop$ file flag.pdf
```

```bash
ubuntu@tryhackme:~/Desktop$ file flag.zip
```

<img width="1266" height="112" alt="image" src="https://github.com/user-attachments/assets/8ff95867-e61f-41d3-94a6-9f93a067c966" />

<br>
<br>
<br>
<br>

```bash
ubuntu@tryhackme:~/Desktop$ pdfcrack
```

<img width="1181" height="311" alt="image" src="https://github.com/user-attachments/assets/ae452d4d-4021-4f6f-b659-f855e7a037c4" />

<br>
<br>
<br>
<br>
<p align="center">naughtylist</p>

```bash
ubuntu@tryhackme:~/Desktop$ pdfcrack -f flag.pdf -w /usr/share/wordlists/rockyou.txt 
```

<img width="1180" height="230" alt="image" src="https://github.com/user-attachments/assets/b8c1fc4f-229d-476d-9dfe-a21f63ccdf3d" />

<br>
<br>

<img width="1217" height="346" alt="image" src="https://github.com/user-attachments/assets/9dc82fba-46b2-4068-84a7-79d00ebeb230" />

<br>
<br>

<img width="1216" height="293" alt="image" src="https://github.com/user-attachments/assets/4864b76e-062c-4870-ad1d-eb992653ef6c" />

<br>
<br>
<br>
<p>2.2. <em>What is the flag inside the encrypted zip file?</em><br>
<code>THM{Cr4ck1n6_z1p$_1s_34$yyyy}</code></p>

<br>
<br>

```bash
ubuntu@tryhackme:~/Desktop$ zip2john flag.zip > Hash
```

```bash
ubuntu@tryhackme:~/Desktop$ ls
```

```bash
ubuntu@tryhackme:~/Desktop$ cat Hash
```

<img width="1177" height="136" alt="image" src="https://github.com/user-attachments/assets/5086e64b-4890-4513-bd07-9ad45c1460a9" />


<br>
<br>
<br>
<br>

<p align="center">winter4ever</p>

```bash
ubuntu@tryhackme:~/Desktop$ john --wordlist=/usr/share/wordlists/rockyou.txt Hash
```

<img width="1364" height="197" alt="image" src="https://github.com/user-attachments/assets/3c8be1bd-1a08-4c1a-9e84-f55048d4190d" />

<br>
<br>

<img width="1270" height="393" alt="image" src="https://github.com/user-attachments/assets/0458ab6f-a520-4342-8838-876b2935d90f" />

<br>
<br>

<img width="1261" height="292" alt="image" src="https://github.com/user-attachments/assets/4fa5c945-3924-45e3-80a1-dd332a758ce3" />

<br>
<br>

<img width="1250" height="292" alt="image" src="https://github.com/user-attachments/assets/b3bd57b7-b1b2-4a07-881a-58a99994fc41" />

<br>
<br>

<img width="1341" height="293" alt="image" src="https://github.com/user-attachments/assets/3ce6053a-2c78-4673-bced-863a0e29526c" />

<br>
<br>


<img width="1293" height="228" alt="image" src="https://github.com/user-attachments/assets/694590dc-a33f-414f-88b9-89ee2a57b5b7" />

<br>
<br>
<p>2.3. <em>For those who want another challenge, have a look around the VM to get access to the key for Side Quest 2! Accessible through our Side Quest Hub!</em><br>
<code>No answer needed</code></p>

<br>
<p>2.4. <em>If you enjoyed this task, feel free to check out the Password Attacks room.</em><br>
<code>No answer needed</code></p>

<p align="center"><a href="https://github.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/blob/Red-Teaming/2.3.%20Password%20Attacks.md">Password Attacks</a><br>October 13, 2024<br><img width="1200px" src="https://github.com/user-attachments/assets/c2a6d1da-0f56-4b00-86e2-94bb793c82a1"></p>

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/7b2c983f-39de-4bf2-96d2-2150a3a05b4b"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|19      |Easy 🔗 -  Passwords - A Cracking Christmas      |3 |101ˢᵗ    |     3ʳᵈ    |   29,583ʳᵈ   |      340ᵗʰ     |    134,642  |    1,036    |    84     |
|18      |Easy 🔗 -  Prompt Injection - Sched-yule conflict|2 |101ˢᵗ    |     3ʳᵈ    |   30,518ᵗʰ   |      353ʳᵈ     |    134,626  |    1,035    |    84     |
|18      |Medium 🔗 -  Obfuscation - The Egg Shell File  | 2  |101ˢᵗ    |     3ʳᵈ    |   30,967ᵗʰ   |      358ᵗʰ     |    134,618  |    1,034    |    84     |
|17      |Medium 🔗 - CyberChef - Hoperation Save McSkidy| 1  |101ˢᵗ    |     3ʳᵈ    |   32,378ᵗʰ   |      374ᵗʰ     |    134,602  |    1,033    |    84     |
|7       |Medium 🔗 - Malware Analysis - Egg-xecutable   |  2 | 95ᵗʰ    |     3ʳᵈ    |   11,604ᵗʰ   |      145ᵗʰ     |    134,544  |    1,034    |    84     |
|7       |Easy 🔗 - Network Discovery - Scan-ta Clause   |  2 | 95ᵗʰ    |     3ʳᵈ    |   18,575ᵗʰ   |      208ᵗʰ     |    134,522  |    1,033    |    84     |
|7       |Easy 🔗 - React2Shell: CVE-2025-55182 |  2     |      95ᵗʰ    |     3ʳᵈ    |   28,593ʳᵈ   |      326ᵗʰ     |    134,474  |    1,032    |    81     |
|6       |Medium 🔗 - IDOR - Santa´s Little IDOR|  1     |      95ᵗʰ    |     3ʳᵈ    |   27,309ᵗʰ   |      328ᵗʰ     |    134,450  |    1,031    |    81     |
|6       |Easy 🔗 - AI in Security - old sAInt nick|  1  |      95ᵗʰ    |     3ʳᵈ    |   41,626ᵗʰ   |      526ᵗʰ     |    134,426  |    1,030    |    81     |
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?|  1  |      95ᵗʰ    |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas   |   1    |      96ᵗʰ    |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells    |   1    |      97ᵗʰ    |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>

<p align="center">Global All Time:    101ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/98fadf39-37c1-4da6-83b8-8d45a0d75351"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/6ee263d9-9062-481f-8273-a91b87adf908"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/8a9eb772-fdb5-49d2-9a22-ddb595a9baa5"><br><br>
                  Global monthly:  29,583ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/26ebbd66-2f29-4454-a3cb-620fbd94af04"><br><br>
                  Brazil monthly:     340ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/400a7e95-2abc-4ee9-a0ab-14794610e28a"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
