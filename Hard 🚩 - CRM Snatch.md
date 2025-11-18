<h1 align="center">CRM Snatch</h1>
<h3 align="center">Honeynet Collapse CTF &nbsp; .  &nbsp; Task 6 &nbsp; .  &nbsp; Initial Access Pot</h3>
<p align="center">2025, November 14  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>1</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Investigate the fourth, Disk part of the Honeynet Collapse! &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/crmsnatch">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/34fc2809-96bf-46fe-af34-cd9abf49e57f"></p>


<h2>1 . Introduction</h2>
<h3>Meet DeceptiTech</h3>
<p>DeceptiTech is a fast-growing cyber security company specializing in honeypot development and deception technologies. At the heart of their success are DeceptiPots - lightweight, powerful, and configurable honeypots that you can install on any OS and capture every malicious action!<br>

The internal DeceptiTech network is organized around a traditional on-premises Active Directory domain with approximately 50 active users. The product platform, however, is isolated and hosted entirely in the AWS cloud:</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/34793d11-ee28-43ae-a4b0-c2ed81bbd0c6"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Initial Access Pot</h3>
<p>One ordinary morning, DeceptiTech's entire network collapsed. Within minutes, all critical on-premises systems were locked down and encrypted. The IT department hurried to restore backups, while the security team rushed to their SIEM - only to find the backups corrupted and all SIEM data wiped clean.<br>

This room is about the fourth attack stage (#4 on the network diagram). As a part of an external DFIR unit, can you help DeceptiTech to perform a full-scope investigation?</p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s go!<br>
<code>No answer needed</code></p>

<br>
<h2>2 . The Challenge</h2>
<h3> Set up virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<h3>CRM Sntach</h3>
<p><em>Hey Alex, did you finish patching the Odoo server? Can you have a look at the nightly exports on SRV-CRM-01? Finance says yesterday's customer CSV file vanished from the share.  ~ Matthew</em></p>
<p>Little did they know that the attacker had already slipped into the server with Matthew's stolen credentials and used the distraction to complete the snatch. The latest customer export was grabbed, hidden inside a password-protected archive, and quietly transferred to the external buckets. In the process, event logs were wiped, and shadow copies were deleted on the way out.<br>

With a forensic snapshot of the disk, can you unravel the timeline, expose the masqueraded tools, and prove the exfiltration?</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/ad29faef-4041-46f1-857c-bc7972c4b92d"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the questions below</em></p>

<br>
<p>6.3. <em>What was the attacker's C2 IP address used for staging and exfiltration?</em><br>
<code>167.172.41.141</code></p>

- launch <code>AccessData FTK Imager</code><br>
- select <code>File</code> &nbsp; > &nbsp; <code>Add Evidence Item ...</code> &nbsp; > &nbsp; <code>Image File</code><br>
- browse and select <code>C:\Users\Administrator\Desktop\Image</code><br>
- select the E01 File <code>CRM-Snatch-01.E01</code></p>

<img width="1374" height="367" alt="image" src="https://github.com/user-attachments/assets/3b544fe1-d022-4e7c-bdc4-3f160749f6eb" />

<br>
<br>

<img width="1271" height="537" alt="image" src="https://github.com/user-attachments/assets/6cab9c81-c9e6-4af9-a2e1-d1aacd0a379b" />

<br>
<p>

- hit <code>Finish</code><br>
- navigate to <code>Partition 1 [...]</code> &nbsp; > &nbsp; <code>NONAME [NTFS]</code> &nbsp; > &nbsp; <code>[root]</code> &nbsp; > &nbsp; <code>Users</code> &nbsp; > &nbsp; <code>matthew.collins</code><br>
- navigate to <code>AppData</code> > <code>Roaming</code> &nbsp; > &nbsp; <code>Microsoft</code> &nbsp; > &nbsp; <code>Windows</code> &nbsp; > &nbsp; <code>Powershell</code> <code>PSReadLine</code><br>
- identify <code>ConsoleHost_history.txt</code></p>

<img width="1347" height="740" alt="image" src="https://github.com/user-attachments/assets/1f50738d-a968-46d7-a53d-1bed502dce42" />

<br>
<p>

- right-click <code>ConsoleHost_history.txt</code><br>
- hit <code>Export Files...</code><br>
- browse and select path<br>
- save<br>
- open in <code>Notepad</code><br>
- identify the attacker's C2 IP address used for staging and exfiltration</p>

<img width="1366" height="195" alt="image" src="https://github.com/user-attachments/assets/14c3d704-36de-4d73-b6ca-a83c980f5c0f" />

<br>
<br>

<img width="1299" height="324" alt="image" src="https://github.com/user-attachments/assets/321b9a21-ff73-42bd-9574-e8a0232beb61" />

<br>
<br>
<p>6.4. <em>Which well-known tool was used to exfiltrate the collected data?</em><br>
<code>rclone</code></p>
<p>

- identify the answer in 6.3.</p>

<img width="1302" height="366" alt="image" src="https://github.com/user-attachments/assets/c7d5069b-8e8a-437f-a231-fac17a6a6155" />

<br>
<br>
<p>6.1. <em>Which domain account was used to initiate the remote session onto the host?</em><br>
<code>matthew.collins</code></p>
<p>

- identify the answer in the description of the challenge</p>

<img width="428" height="136" alt="image" src="https://github.com/user-attachments/assets/343d88df-868e-4a54-b23a-e0119c40a4ec" />

<br>
<p>

- confirm it in <code>ConsoleHost_history.txt</code> identifying <code>C:\Users\MATTHE~1.COL\AppData\...</code></p>

<img width="1305" height="432" alt="image" src="https://github.com/user-attachments/assets/a17ecb7f-7229-4e7f-885e-391549fc7d85" />

<br>
<br>
<p>6.2. <em>For how many seconds did the attacker maintain their PowerShell session active?</em><br>
<code>3455</code></p>
<p>

- right-click <code>NTUSER.DAT</code></p>

<img width="1380" height="475" alt="image" src="https://github.com/user-attachments/assets/ee2c4a6a-4272-49e6-8b47-6b0c0ad23302" />

<br>
<p>
  
- hit <code>Export Files...</code><br>
- browse and select path<br>
- save<br></p>

<img width="1358" height="344" alt="image" src="https://github.com/user-attachments/assets/6719ec3f-816e-45d8-a6ac-b1d5a07bc693" />

<p>

- launch <code>Registry Explorer</code><br>
- select <code>File</code> &nbsp; > &nbsp; <code>Load hive</code> &nbsp; > &nbsp; <code>NTUSER.DAT</code></p>

<img width="351" height="180" alt="image" src="https://github.com/user-attachments/assets/606e7b13-c69d-47e1-a9b3-3ca566127815" />

<p>

- select <code>Software</code> &nbsp; > &nbsp; <code>Microsoft</code> &nbsp; > &nbsp; <code>Windows</code> &nbsp; > &nbsp; <code>CurrentVersion</code> &nbsp; > &nbsp; <code>Explorer</code> &nbsp; > &nbsp; <code>User Assist</code><br>
- identifiy <code>{System}\WindowsPowerShell\v1.0\powershell.exe</code> &nbsp; : &nbsp; <code>0</code>d, <code>0</code>h, <code>57</code>m, <code>35</code>s</code><br>
- calculate the time in seconds &nbsp;&nbsp; → &nbsp;&nbsp; <code>57</code> x 60 &nbsp;&nbsp; + &nbsp;&nbsp; <code>35</code> &nbsp;&nbsp; = &nbsp;&nbsp; <code>3455</code></p>

<img width="1311" height="697" alt="image" src="https://github.com/user-attachments/assets/156a66bf-c86e-4963-9187-229949e786b2" />

<br>
<br>
<p>6.5. <em>What is the obscured password to the attacker-controlled Mega?</em><br>
<code>yWKgVA7Rv1iIoG-VWAr7NAFbwKHNiMZGNybJ4QybJHtiFg</code></p>
<p>

- identify <code>C:\ProgramData\sync\mega.conf</code> in 6.3</p>

<img width="1299" height="402" alt="image" src="https://github.com/user-attachments/assets/67bfec0b-fc60-4a3d-a63a-533bdb2b5ab7" />

<p>

- select <code>Partition 1 [...]</code> &nbsp; > &nbsp; <code>NONAME [NTFS]</code> &nbsp; > &nbsp; <code>[root]</code> &nbsp; > &nbsp; <code>ProgramData</code> &nbsp; > &nbsp; <code>sync</code> &nbsp;&nbsp; in &nbsp;&nbsp; <code>FTK Imager</code><br>
- identify <code>mega.conf</code><br>
- click it<br>
- identify the obscured password to the attacker-controlled Mega</p>

<img width="1361" height="386" alt="image" src="https://github.com/user-attachments/assets/8eb5052d-b70d-4567-b82f-7575669475e3" />

<br>
<br>
<p>6.6. <em>What is Lucas's email address found in the exfiltrated data?</em><br>
<code>lucas.rivera@deceptitech.thm</code></p>
<p>

- select <code>Partition 1 [...]</code> &nbsp; > &nbsp; <code>NONAME [NTFS]</code> &nbsp; > &nbsp; <code>[root]</code> &nbsp; > &nbsp; <code>Exil_Temp</code> &nbsp; > &nbsp; <code>CRM-Exports</code> &nbsp;&nbsp; in &nbsp;&nbsp; <code>FTK Imager</code><br>
- identify <code>customers_export.csv</code><br>
- click it<br>
- identify Lucas's email address</p>

<img width="1373" height="736" alt="image" src="https://github.com/user-attachments/assets/cfc31d12-3039-4286-a585-1eb34127d83a" />

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/a51a662a-9a4f-457d-902f-90fa1930bacc"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/e6559a75-d6d9-4490-9cb1-97120893d9da"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, November</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|14      |Hard 🚩 - CRM Snatch                   |   1    |      95ᵗʰ    |     4ᵗʰ    |   1,526ᵗʰ   |     12ⁿᵈ     |    132,822  |    1,019    |    80     |
|8       |Easy 🔗 - Living of the Land Attacks   |   1    |      91ˢᵗ    |     4ᵗʰ    |   1,759ᵗʰ   |     17ᵗʰ     |    132,642  |    1,018    |    80     |
|8       |Hard 🚩 - Lost in RAMslation           |   1    |      91ˢᵗ    |     4ᵗʰ    |   2,547ᵗʰ   |     25ᵗʰ     |    132,580  |    1,017    |    80     |
|8       |Easy 🔗 - MITRE                        |   1    |       -      |     4ᵗʰ    |      -      |      -       |          -  |       -     |    80     |

</h6></div><br>

<p align="center">Global All Time:     95ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/e132f2dc-8343-4079-a4f0-c81f4fd87502"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/b7d5ce35-ede8-42cd-8f61-69866ab16b9a"><br><br>
                  Brazil All Time:      4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c8e8a89c-5ae5-4705-af60-5caabb067ece"><br><br>
                  Global monthly:   1,526ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/bf2766ba-5d45-46f3-9103-19abba9bb3ae"><br><br>
                  Brazil monthly:     12ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/7faad6f4-dda0-4ef1-85db-fd91c0bd9a89"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

