<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 19 &nbsp;&nbsp; ·  &nbsp;&nbsp; ICS/Modbus - Claus for Concern</h3>
<p align="center">2025, December 19  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in <a href="https://tryhackme.com">TryHackMe</a>.<br>Learn to identify and exploit weaknesses in Industrial Control Systems (ICS) systems. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/ICS-modbus-aoc2025-g3m6n9b1v4">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/863d1e21-3a7e-4053-9505-ecd61fbe2d2c"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/08555dc0-9f0e-4930-8d55-0d35e9765227"></p>

<br>
<br>

<h2 align="center">Check out my upcoming walkthrough on Medium!</h2>

<br>
<br>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<img width="1200" height="407" alt="image" src="https://github.com/user-attachments/assets/c8fd2244-15f7-4a66-9fc6-5fc00b1b912e" />

<p>The snow falls heavily over Wareville as chaos erupts at TBFC headquarters. What should be the busiest shipping day of the season has turned into a disaster.<br>

"Another chocolate egg?!" shouts a frustrated warehouse worker, holding up yet another Easter-themed package."We're supposed to be shipping Christmas presents!"<br>

The delivery drones buzz overhead, their mechanical hums sounding almost... mocking. Each one returns from its route empty, having successfully delivered its cargo. But the cargo is all wrong.<br>

You're called into the command centre, where screens flicker with delivery statistics. Everything looks normal on the surface—1,000 presents in stock, 98% success rate, and all systems are operational. But the phones won't stop ringing with confused citizens asking why they're receiving chocolate eggs instead of the toys and gifts they ordered.<br>

The logistics manager pulls up a delivery manifest. "Look at this", she says, pointing at the screen."The system indicates that we delivered a teddy bear to the Miller family, but they received a chocolate bunny instead. It's the same weight, exact dimensions, but completely different items."<br>

Then, on one of the monitoring screens, a message flashes for just a second before disappearing:</p>

<img width="800" height="51" alt="image" src="https://github.com/user-attachments/assets/326044da-c353-4a22-8ada-d82992c5ed3f" />

<p>Someone has compromised the drone fleet's control systems. The attack is sophisticated, falsifying sensor data, manipulating inventory selection, and erasing all traces. This isn't just a prank - it's a calculated assault on Christmas itself.
Your mission is clear: investigate the TBFC Drone Delivery System, uncover how King Malhare's Eggsploit team has compromised it, and restore Christmas deliveries before SOC-mas is ruined.
But be warned: King Malhare doesn't leave systems undefended. Traps are waiting for the careless investigator. One wrong move and you might make things much worse.</p>

<h3>A Mysterious Discovery</h3>

<h3>Learning Objectives</h3>

<h3>Connecting to the Machine</h3>

<h3>Set up your virtual environment</h3>



<br>
<p><em>Answer the question below</em></p>

<p>1.1. <em>The clock is ticking, investigator. Christmas is hanging by a thread, and only you can pull it back from the brink.</em><br>
<code>No answer needed</code></p>


<br>
<br>
<h2>Task 2 &nbsp; ·  &nbsp; SCADA (Supervisory Control and Data Acquisition)</h2>

<h3>What is SCADA?</h3>

<h3>Components of a SCADA System</h3>

<h3>Why SCADA Systems Are Targeted</h3>


<br>
<p><em>Answer the question below</em></p>

<p>2.1. <em>What port is commonly used by Modbus TCP?</em><br>
<code>502</code></p>
<br>
<br>
<h2>Task 3 &nbsp; ·  &nbsp;PLC & Modbus Protocol</h2>
<h3>What is a PLC?</h3>

<h3>What is Modbus?</h3>

<h3>Modbus Data Types</h3>

<h3>Modbus Addressing</h3>

<h3>Modbus TCP vs Serial Modbus</h3>

<h3>The Security Problem</h3>

<h3>Connecting the Dots</h3>

<br>
<p><em>Answer the question below</em></p>

<p>3.1. <em>Now that you understand how the system works, the mission is yours, hack it back and save Christmas!</em><br>
<code>No answer needed</code></p>
<br>
<br>
<h2>Task 4 &nbsp; ·  &nbsp;Practical</h2>
<p>Now that you understand the basic concepts related to ICS and Modbus, we will analyse the compromised TBFC Drone Control System and learn how to safely restore it ...</p>

<br>
<p><em>Answer the question below</em></p>

<p>4.1. <em>What's the flag?</em><br>
<code>THM{eGgMas0V3r}</code></p>

```bash
:~# nmap -sV -p 22,80,502 xx.xx.xxx.xxx
...
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http    Werkzeug/3.1.3 Python/3.12.3
502/tcp open  mbap?
```

<img width="1383" height="235" alt="image" src="https://github.com/user-attachments/assets/2100062f-929c-414e-a0d0-5495b640e056" />

<br>
<br>

<img width="1338" height="565" alt="image" src="https://github.com/user-attachments/assets/1796abfa-f4ba-4a22-9219-854c0ce2f6aa" />

<br>
<br>

<img width="1330" height="324" alt="image" src="https://github.com/user-attachments/assets/eb783f7a-99fb-4f43-87ed-5e50288bff71" />

```bash
/ Correct SECRET API PATH
    const API_URL = "/api/3a9c9bde0f1a471aa1a2/state";
```

<img width="1335" height="216" alt="image" src="https://github.com/user-attachments/assets/5a40930d-208d-4aad-873c-405cd0bba89f" />

<br>
<br>

<img width="1381" height="78" alt="image" src="https://github.com/user-attachments/assets/6b21458d-97a9-4d08-bec3-97937b4c6733" />

<br>
<br>

<img width="1379" height="345" alt="image" src="https://github.com/user-attachments/assets/c1af65b9-847d-4225-9e3b-b13c683afe7d" />

<br>
<br

<img width="1378" height="605" alt="image" src="https://github.com/user-attachments/assets/c58392ec-e99d-464f-96f8-bbc2be651eb1" />

<br>
<br>

<img width="1352" height="707" alt="image" src="https://github.com/user-attachments/assets/51f4113f-812a-4fc9-af97-86b0f3387af5" />

<br>
<br>

<img width="1355" height="706" alt="image" src="https://github.com/user-attachments/assets/7830dc36-82ca-49ae-83f9-90bac2532843" />

<br>
<br>

<img width="1334" height="600" alt="image" src="https://github.com/user-attachments/assets/8630ec67-7d7f-45ca-844b-8d7096195bae" />

<br>
<br>

<p>4.2. <em>If you enjoyed today's room, feel free to check out our OT challenge: Industrial Intrusion</em><br>
<code>No answer needed</code></p>

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/b3aa3875-c3a5-416d-81a8-66cd3119e767"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/e97c9645-829a-4815-a729-7c9af3ab3438"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/a8fa999b-6b10-47e9-9d10-0f4b77dd7eb2"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|19      |Medium 🔗 -  ICS/Modbus - Claus for Concern      |3 |101ˢᵗ    |     3ʳᵈ    |   28,869ᵗʰ   |      337ᵗʰ     |    134,658  |    1,037    |    84     |
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

<p align="center">Global All Time:    101ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/a452ade1-046f-440c-8b31-c01eed1cec9d"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/b2d7fe5c-4ca0-4db2-a43f-bb4b442c0793"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/e8b9a638-5180-4a15-b68d-e07b091373e6"><br><br>
                  Global monthly:  28,869ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b6b17366-aa70-4fe6-811e-94ff6ecb0d02"><br><br>
                  Brazil monthly:     337ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3ba14951-6301-4d11-9e12-b67b226a4528"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
