<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 18 &nbsp;&nbsp; ·  &nbsp;&nbsp; Obfuscation - The Egg Shell File</h3>
<p align="center">2025, December 18  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in<a href="https://tryhackme.com"> TryHackMe</a>.<br>McSkidy keeps her focus on a particular alert that caught her interest: an email posing as northpole-hr. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/obfuscation-aoc2025-e5r8t2y6u9">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/e19fe801-c3c4-4a8f-9009-b56bcb8cc227"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/103151e3-5a62-42e5-ae96-58de3fe7bf34"></p>

<br>
<h2 align="center">Read my complete walkthrough in Medium.<br>
Click here ➡️  <a href="https://medium.com/@RosanaFS/obfuscation-the-egg-shell-file-advent-of-cyber-2025-day-18-tryhackme-walkthrough-ac037fc4c371">Obfuscation - The Egg Shell File</a></h2>
<br>
<br>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<br>
<p><em>Answer the question below</em></p>

<p>1.1. <em>Start the target machine and continue with the next task.</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 &nbsp; ·  &nbsp; Obfuscation & Deobfuscation</h2>

<h3>Understanding the Gibberish</h3>

<h3>Obfuscation in the Real World</h3>

<h3>Detecting Patterns</h3>

<h3>Unfamiliar Patterns</h3>

<h3>Layered Obfuscation</h3>

<h3>Unwrapping the Easter Egg</h3>


<br>
<p><em>Answer the question below</em></p>

<p>2.1. <em>What is the first flag you get after deobfuscating the C2 URL and running the script?</em> Hint: The variable name is a hint to the encoding used.<br>
<code>THM{C2_De0bfuscation_29838}</code></p>
<p>

- use Visual Studio to open SantaStealer.ps1</p>

<img width="1307" height="235" alt="image" src="https://github.com/user-attachments/assets/a02df7f9-f4ff-4c4b-b762-e952ab15eb77" />

<br>
<p>

- use CyberChef to deobfuscate the C2 URL</p>

<img width="1916" height="279" alt="image" src="https://github.com/user-attachments/assets/0baf3e69-19ad-43fc-ae2e-d7ec1ad3cb1a" />

<br>
<p>

- update and save SantaStealer.ps1</p>

<img width="1303" height="310" alt="image" src="https://github.com/user-attachments/assets/d31fee82-3e6a-4949-bcdd-4608b3cce7f0" />

<br>
<p>

- use PowerShell to execute SantaStealer.ps1</p>

<img width="1385" height="363" alt="image" src="https://github.com/user-attachments/assets/1eaa6999-8595-4dff-b452-33f62a5b5f92" />

<br>
<br>
<p>2.2. <em>What is the second flag you get after obfuscating the API key and running the script again?</em><br>
<code>THM{API_Obfusc4tion_ftw_0283}</code></p>
<p>

- navigate to Part 2: Obfuscation</p>

<img width="1312" height="288" alt="image" src="https://github.com/user-attachments/assets/d37caa53-49eb-446d-a7ad-f816c25e1728" />

<br>
<p>
  
- use XOR recipe in CyberChef with the decimal equivalent of 0x37 as key, which is 55</p>

<img width="1911" height="262" alt="image" src="https://github.com/user-attachments/assets/8028a989-ad58-4685-889a-c154528b3810" />

<br>
<p>
  
- update $ObfAPIKEY with CyberChef´s output<br>
- save SantaStealer.ps1</p>

<img width="1309" height="261" alt="image" src="https://github.com/user-attachments/assets/8ed083e6-7403-4eb6-8b23-d0e373f8fe42" />

<br>
<p>

- use PowerShell to execute SantaStealer.ps1</p>

<img width="1382" height="309" alt="image" src="https://github.com/user-attachments/assets/1aee89fb-1ed0-452f-b1af-95098cab88b6" />


<br>
<p>2.3. <em>If you want to learn more about Obfuscation, check out our Obfuscation Principles room!</em><br>
<code>No answer needed</code></p>

<img width="1909" height="836" alt="image" src="https://github.com/user-attachments/assets/8d1b8793-c072-49ca-90d4-3f1e986eace6" />

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/f5421859-8b26-4b7c-9d14-c2ca57f9f9f6"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/53581028-8d55-4156-baef-d806e41c44b1"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/c1c89c99-1993-4e47-ac94-9b65dd39b981"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
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

<p align="center">Global All Time:    101ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/146f2f20-da0f-4d9d-8e18-cce4eaca3ce3"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/58bb9c45-9781-4c27-b7dd-8609c0b20dba"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/2bf0b199-0ba5-44ac-929b-c76c21ad19e2"><br><br>
                  Global monthly:  30,967ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/01a72966-94c7-48f5-8901-337a87cbab39"><br><br>
                  Brazil monthly:     358ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/dbe78d27-ff67-4f24-bb2b-0e4d4cfdf78f"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
