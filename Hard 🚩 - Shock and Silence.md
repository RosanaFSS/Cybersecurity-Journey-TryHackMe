<h1 align="center"Shock and Silence</h1>
<h3 align="center">Honeynet Collapse CTF &nbsp; .  &nbsp; Task 7</h3>
<p align="center">2025, November 14  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>1</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Investigate the fifth, File System part of the Honeynet Collapse! &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/shockandsilence">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/365fd061-4cba-47d1-aa39-a60232928dbb"></p>


<h2>1 . Introduction</h2>
<h3>Meet DeceptiTech</h3>
<p>DeceptiTech is a fast-growing cyber security company specializing in honeypot development and deception technologies. At the heart of their success are DeceptiPots - lightweight, powerful, and configurable honeypots that you can install on any OS and capture every malicious action!<br>

The internal DeceptiTech network is organized around a traditional on-premises Active Directory domain with approximately 50 active users. The product platform, however, is isolated and hosted entirely in the AWS cloud:</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/34793d11-ee28-43ae-a4b0-c2ed81bbd0c6"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Initial Access Pot</h3>
<p>One ordinary morning, DeceptiTech's entire network collapsed. Within minutes, all critical on-premises systems were locked down and encrypted. The IT department hurried to restore backups, while the security team rushed to their SIEM - only to find the backups corrupted and all SIEM data wiped clean.<br>

This room is about the fifth attack stage (#5 on the network diagram). As a part of an external DFIR unit, can you help DeceptiTech to perform a full-scope investigation?</p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s go!<br>
<code>No answer needed</code></p>

<br>
<h2>2 . The Challenge</h2>
<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<h3>Shock and Silence</h3>
<p><em>You thought that was the end? Oh no, no, no... deep down, we all knew where this was heading</em>.<br>

Logan Hall had enjoyed a productive week and decided Friday was the perfect time to roll out new Group Policies to the DC-01 domain controller. Confident and calm, he remoted in - but what he saw made his blood run cold.<br>

Most of the files on the server had an unfamiliar extension - renamed into gibberish and completely unreadable. Trying to stay calm, he noticed a ReadMe file sitting ominously on the Desktop. He opened it... and that's when the real panic began:</p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/b2f5c21e-680a-49fc-92ab-199c4bc8965d"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Taking a deep breath, Logan pulled himself together and reported the incident. Time to take over and analyze the only available evidence - a partial disk image of DC-01 acquired after the encryption. Now it's all in your hands!</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/0d9937f7-8bcc-4096-8686-e520871f44b7"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the questions below</em></p>

<p>7.1. <em>What is the full URL from which the ransomware was downloaded to the system?</em><br>
<code>https://store5.gofile.io/download/web/e23cb33f-0e4d-4a5f-8c55-ea2d78057d40/HiddenFile.zip</code></p>
<p>
  
- identify <code>DC-01-NTFS-logs.ad1</code> &nbsp; in &nbsp; <code>C:\Users\DFIR Analyst\Desktop</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d571bb3c-23ba-4421-8167-a3f84c2f7c5b"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/5f0773ab-02ec-4c0a-bf38-88c0da656b02"></h6>

<p>

- launch <code>FTK Imager</code><br>
- select <code>File</code> &nbsp; > &nbsp; <code>Add Evidence Item ...</code> &nbsp; > &nbsp; <code>Image File</code><br>
- hit <code>Next</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/52620508-06df-41f9-9745-3eab6a1e053a"></h6>

<p>

- perform the following for <code>$J</code> and <code>$MFT</code> &nbsp;&nbsp; → &nbsp;&nbsp; 1️⃣ browse and select a folder, 2️⃣ hit <code>OK</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3111df83-75b4-44eb-bab1-33f472217a50"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/fca37a57-281a-47ac-b6f1-ad5b088f30f4"></h6>

<p>

- execute <code>MFTECmd</code> against <code>$J</code> to generate a <code>Journal.csv</code> file</p>

```bash
PS C:\Users\DFIR Analyst\DFIR-Tools\MFTECmd> .\MFTECmd.exe -f 'C:\Users\DFIR Analyst\DFIR-Tools\Evidence\$J' --csv 'C:\Users\DFIR Analyst\DFIR-Tools\Evidence' --csvf Journal.csv
```

<p>

- execute <code>MFTECmd</code> against <code>$MFT</code> to generate a <code>MFT.csv</code> file</p>

```bash
PS C:\Users\DFIR Analyst\DFIR-Tools\MFTECmd> .\MFTECmd.exe -f 'C:\Users\DFIR Analyst\DFIR-Tools\Evidence\$MFT' --csv 'C:\Users\DFIR Analyst\DFIR-Tools\Evidence' --csvf MFT.csv
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/01d67950-7581-46ec-81a9-e354b8d7353b"></h6>

<p>

- launch <code>Timeline Explorer</code><br>
- open <code>MFT.csv</code><br>
- identify <code>HiddenFile.zip</code> and its path</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/108f175f-cf14-44cb-b34c-1990d7cfec30"></h6>

<br>
<p>7.2. <em>What was the original file name of the ransomware executable downloaded to the host?</em><br>
<code>pb.exe</code></p>
<p>

- identify the answer in 7.1.</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/57d69e20-33de-445a-8295-e07b7a0773d4"></h6>

<br>
<p>7.3. <em>Which executable file initiated the encryption process on the system?</em><br>
<code>HpAgent.exe</code></p>
<p>

- identify the answer filtering <code>Journal.csv</code> by <code>.exe</code> extension</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/a94737a9-ceaa-4273-8e34-e5670db1068b"></h6>

<br>
<p>7.4. <em>What file extension was appended to the encrypted files?</em><br>
<code>EeUfy</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/0e8f32de-442e-4961-9a40-9a4f4510a255"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/596f2071-66a5-49ea-9c88-bd855054a2b4"></h6>

<br>
<p>7.5. <em>Go beyond the obvious - which ransomware group targeted the organisation?</em> Hint: Perform some OSINT and look deeper - the true story lies beneath the surface. You're looking for the group that got breached!<br>
<code>BlackLock</code></p>

<p>

- review the ReadMe file presented in the challenge details<br>
- identify a typo: <code>Ehe</code><br>
- identify in sequence <code>decryptor will be destroyed</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/792b7051-983d-41e5-be55-9a336467a56d"></h6>

<p>

- look for <code>Ehe decryptor will be destroyed</code><br>
- identify <code>b88c5dde0bd63bdf553babb181....</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b71ac02e-dec5-451d-b358-abc58319deb4"></h6>

<p>

- navigate to the link just discovered<br>
- visualize <code>Ehe decryptor will be destroyed</code><br>
- identify a Blog link related to <code>onion</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/a659ecf0-3d2d-4e22-aec2-94f662fc50da"></h6>

<p>

- launch <code>Tor</code><br>
- discover that there is an onion to symbolize Tor</p>

<h6 align="center"><img width="280px" src="https://github.com/user-attachments/assets/6b84d791-a3f7-4888-b129-794d80a2ad4f"><br>Discover that there is an onion to symbolize Tor</h6>

<p>

- navigate to the Blog link<br>
- discover the ransomware group that targeted the organisation</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/659d509a-5e0f-49a1-b1d6-1ed892018738"></h6>

<br>
<p>7.6. <em>What is the filename containing additional ransom instructions for the victim?</em><br>
<code>IMPORTANT NOTICE.oxps</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/499770f0-2657-461b-bef1-1b998d0d2f77"></h6>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/34208fda-1d6c-4dc9-93ce-f8fc4fe3ac1d"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/03f8d373-6616-42a6-b1ef-1b94c3019bca"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, November</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|14      |Hard 🚩 - Shock and Silence            |   1    |      94ᵗʰ    |     4ᵗʰ    |     749ᵗʰ   |      7ᵗʰ     |    133,095  |    1,021    |    80     |
|14      |Easy 🔗 - Input Manipulation & Prompt Injection| 1 |   95ᵗʰ    |     4ᵗʰ    |   1,290ᵗʰ   |     12ⁿᵈ     |    132,822  |    1,020    |    80     |
|14      |Hard 🚩 - CRM Snatch                   |   1    |      95ᵗʰ    |     4ᵗʰ    |   1,526ᵗʰ   |     12ⁿᵈ     |          -  |    1,019    |    80     |
|8       |Easy 🔗 - Living of the Land Attacks   |   1    |      91ˢᵗ    |     4ᵗʰ    |   1,759ᵗʰ   |     17ᵗʰ     |    132,642  |    1,018    |    80     |
|8       |Hard 🚩 - Lost in RAMslation           |   1    |      91ˢᵗ    |     4ᵗʰ    |   2,547ᵗʰ   |     25ᵗʰ     |    132,580  |    1,017    |    80     |
|8       |Easy 🔗 - MITRE                        |   1    |       -      |     4ᵗʰ    |      -      |      -       |          -  |       -     |    80     |

</h6></div><br>

<p align="center">Global All Time:     94ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/68f0cdf6-48d7-4210-9176-66ca9b9a0df9"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/7960b17b-5128-44d9-8e50-36d50e806a3b"><br><br>
                  Brazil All Time:      4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/1c8b1690-afa7-4fe2-901b-23ca46c5c6ed"><br><br>
                  Global monthly:     749ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/2d0f4286-f4c4-4a87-977d-ca43fe154d14"><br><br>
                  Brazil monthly:       7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/4fd30c73-3537-48e1-80d4-7d625cb744ca"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
