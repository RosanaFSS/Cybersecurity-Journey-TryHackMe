<h1 align="center">The Last Trial</h1>
<h3 align="center">Honeynet Collapse CTF &nbsp; .  &nbsp; Task 8</h3>
<p align="center">2025, November 22  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>1</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Investigate the sixth, macOS part of the Honeynet Collapse! &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/shockandsilence">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/0db9134b-a524-4c5a-b601-f1e7c3c74bcc"></p>

<h2>1 . Introduction</h2>
<h3>Meet DeceptiTech</h3>
<p>DeceptiTech is a fast-growing cyber security company specializing in honeypot development and deception technologies. At the heart of their success are DeceptiPots - lightweight, powerful, and configurable honeypots that you can install on any OS and capture every malicious action!<br>

The internal DeceptiTech network is organized around a traditional on-premises Active Directory domain with approximately 50 active users. The product platform, however, is isolated and hosted entirely in the AWS cloud:</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/34793d11-ee28-43ae-a4b0-c2ed81bbd0c6"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Initial Access Pot</h3>
<p>One ordinary morning, DeceptiTech's entire network collapsed. Within minutes, all critical on-premises systems were locked down and encrypted. The IT department hurried to restore backups, while the security team rushed to their SIEM - only to find the backups corrupted and all SIEM data wiped clean.<br>

This room is about the sixth attack stage (#6 on the network diagram). As a part of an external DFIR unit, can you help DeceptiTech to perform a full-scope investigation?!</p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s go!<br>
<code>No answer needed</code></p>

<br>
<h2>2 . The Challenge</h2>
<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<h3>The Last Trial</h3>
<p>Until now, the threat actor has managed to move laterally across the domain to gain access to the most critical systems. During this time, the security team is focused on the containment and detailed investigation of the whole attack. But, amidst this primary attack, another critical compromise took place, this time on a macOS system. Lucas, the lead developer of DeceptiTech, unintentionally became a victim of a different compromise.<br>

Not every attack is targeted. Sometimes, your curiosity makes you fall into a trap.<br>

Lucas, always interested in researching AI to enhance his development skills, stumbled upon a free trial of an AI development tool while browsing online. Who knew this would be Lucas’s last experiment with the deceptive software trials?</p>

<h3>Analysis Approach</h3>
<p>The disk image is available at <code>/home/ubuntu/Lucas_Disk.img</code>. To mount the image, you can use the command: <code>sudo apfs-fuse -v 4 /home/ubuntu/Lucas_Disk.img /home/ubuntu/mac_mount</code>. Then, switch to the root user with sudo su to analyze the mounted image available in <code>/home/ubuntu/mac_mount</code>.<br>

If you wish to run automated analysis through the <code>mac_apt tool</code>, you can switch to the root user and activate the virtual environment by using: <code>source /root/mac_apt/venv/bin/activate</code>, then move to the mac_apt folder: <code>cd /root/mac_apt</code>. Now, you can run the <code>mac_apt.py</code> script on the disk image for analysis.<br>

Note: The VM might take 4 minutes to boot when you click the <code>Start Machine</code> button.<br>
<p><em>Answer the questions below</em></p>

<br>
<p>8.1. <em>What was the website from which the user downloaded the malicious application's installer?</em><br>
<code>developai.thm</code></p>
<br>
<p>

- my reference = [macOS Forensics: Applications](https://github.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/blob/CTFs-%26-Infos/Hard%20%F0%9F%94%97%20-%20macOS%20Forensics%3A%20Applications.md)</p>

<p align="center"><br><img width="800px" src="https://github.com/user-attachments/assets/4c46991f-2ed5-42a1-921a-524441ee3f0c"></p>

<p>Reference: TryHackMe <code>macOS Forensics: Applications</code> walkthrough</p>

```bash
ubuntu@tryhackme:~$ apfsutil Lucas_Disk.img
Found partitions:
69646961-6700-11AA-11AA-00306543ECAC 72949B7C-3908-4369-E3B3-6AD10369BDE0 0000000000000028 00000000000FA027 0000000000000000 iBootSystemContainer
7C3457EF-0000-11AA-11AA-00306543ECAC 1BC5283A-658B-4C62-98A0-D63926A02EA2 00000000000FA028 0000000003C00027 0000000000000000 Container
52637672-7900-11AA-11AA-00306543ECAC DCD7939F-0A71-4091-2791-D18739EFE387 0000000003C00028 00000000045FFFD7 0000000000000000 RecoveryOSContainer
First APFS partition is 1

Volume 0 DD4A038C-E37A-4CC9-8A04-ABE8397A2764
---------------------------------------------
Role:               System
Name:               Macintosh HD (Case-insensitive)
Capacity Consumed:  11244240896 Bytes
FileVault:          No
Snapshots:
    38 : 'com.apple.os.update-52F3A2F592F324F6AC5DE35D538FA237771DB7715C76582E51C5C432D80587DD'

Volume 1 D870538B-4F42-4683-B9B1-745348A1BDF0
---------------------------------------------
Role:               Preboot
Name:               Preboot (Case-insensitive)
Capacity Consumed:  6065659904 Bytes
FileVault:          No
Snapshots:

Volume 2 2843EAEF-F61F-43F0-B985-F2D96B683EAF
---------------------------------------------
Role:               Recovery
Name:               Recovery (Case-insensitive)
Capacity Consumed:  1004126208 Bytes
FileVault:          No
Snapshots:

Volume 3 886820C0-401B-45D1-9860-63A2EBCFCC25
---------------------------------------------
Role:               Update
Name:               Update (Case-insensitive)
Capacity Consumed:  352256 Bytes
FileVault:          No
Snapshots:

Volume 4 61217557-DB23-4B0D-B172-2D3FE202C932
---------------------------------------------
Role:               Data
Name:               Data (Case-insensitive)
Capacity Consumed:  7277621248 Bytes
FileVault:          No
Snapshots:

Volume 5 D692623D-7010-46CC-90AD-F3C29EB47496
---------------------------------------------
Role:               VM
Name:               VM (Case-insensitive)
Capacity Consumed:  1073762304 Bytes
FileVault:          No
Snapshots:
```

```bash
root@tryhackme:/home/ubuntu# sudo apfs-fuse -v 4 /home/ubuntu/Lucas_Disk.img /home/ubuntu/mac_mount
```

```bash
root@tryhackme:/home/ubuntu# sudo su
```

```bash
root@tryhackme:/home/ubuntu# cd mac_mount
root@tryhackme:/home/ubuntu/mac_mount# ls
private-dir  root
root@tryhackme:/home/ubuntu/mac_mount# cd root
root@tryhackme:/home/ubuntu/mac_mount/root# ls
Applications  Library  MobileSoftwareUpdate  System  Users  Volumes  cores  home  mnt  opt  private  sw  usr
```

<p>/home/ubuntu/mac_mount/root/Users/lucasrivera/Library/Safari</p>

<p>http://<code>developai.thm</code>/DevelopAIInstaller.pkg</p>


```bash
root@tryhackme:/home/ubuntu/mac_mount/root/Users/lucasrivera/Library/Safari# plistutil -p Downloads.plist
{
  "DownloadHistory": [
    {
      "DownloadEntryProgressTotalToLoad": 352511,
      "DownloadEntryProgressBytesSoFar": 352511,
      "DownloadEntryPath": "/Users/lucasrivera/Downloads/DevelopAIInstaller.pkg",
      "DownloadEntryDateAddedKey": 2025-07-04 10:08:23 +0000,
      "DownloadEntryRemoveWhenDoneKey": false,
      "DownloadEntryShouldUseRequestURLAsOriginURLIfNecessaryKey": false,
      "DownloadEntryProfileUUIDStringKey": "DefaultProfile",
      "DownloadEntryDateFinishedKey": 2025-07-04 10:08:25 +0000,
      "DownloadEntryURL": "http://developai.thm/DevelopAIInstaller.pkg",
      "DownloadEntrySandboxIdentifier": "5E5E49EB-A07C-489C-B6D6-BCE05557044C",
      "DownloadEntryBookmarkBlob": <626f6f6b cc020000 00000410 30000000 ... 04 00000000 000000>,
      "DownloadEntryIdentifier": "CFD61E24-2396-4249-B6E7-225ADF3EF599"
    }
  ]
}
```

<br>
<br>
<p>8.2. <em>What is the name of the malicious application's installer?</em><br>
<code>DevelopAIInstaller.pkg</code></p>

<img width="1258" height="514" alt="image" src="https://github.com/user-attachments/assets/ca11fc65-c95f-404c-b18b-3f1123b9878a" />

<br>
<br>
<p>8.3. <em>When was the malicious application installed in the system?</em> Answer Format Example: 2025-01-15 12:30:45</em><br>
<code>2025-07-04 10:09:03</code></p>

```bash
root@tryhackme:/home/ubuntu/mac_mount/root/Library/Receipts# plistutil -p InstallHistory.plist
```

<img width="1259" height="390" alt="image" src="https://github.com/user-attachments/assets/cf3e0977-77f9-4fcd-a4e2-7952f6c7a1c7" />

<br>
<br>

<img width="1253" height="211" alt="image" src="https://github.com/user-attachments/assets/31e18d95-78cb-4896-b638-9c3e272b2df3" />

<br>
<br>
<br>
<p>8.4. <em>Which TCC permission did the application request first?</em><br>
<code>kTCCServiceSystemPolicyDesktopFolder</code></p>

<h3>ApplicationPermissions</h3>
<p><em>~/Users/lucasrivera/Library/Application Support/com.apple.TCC/TCC.db</em></p>

<p>https://github.com/mac4n6/APOLLO/tree/master/modules</p>

<p align="center"><br><img width="800px" src="https://github.com/user-attachments/assets/6766ed2d-54e8-4e63-81d2-9f6f6fa78901"></p>

```bash
root@tryhackme:/home/ubuntu/mac_mount/root/Library/Application Support/com.apple.TCC# ls
AdhocSignatureCache  REG.db  TCC.db
root@tryhackme:/home/ubuntu/mac_mount/root/Library/Application Support/com.apple.TCC# cp TCC.db /home/ubuntu/storage/.
```

<p align="center"><br><img width="800px" src="https://github.com/user-attachments/assets/d257edd2-2b93-4781-b885-6efacc74ad8b"></p>

<br>
<br>
<p>8.5. <em>What is the full C2 URL to which the application exfiltrated data?</em><br>
<code>http://c7.macos-updatesupport.info:8080</code></p>

```bash
ubuntu@tryhackme:~/storage/Installer/DevelopAI.app/Contents/MacOS$ file DevelopAI
DevelopAI: Mach-O universal binary with 2 architectures: [x86_64:\012- Mach-O 64-bit x86_64 executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL|PIE>] [\012- arm64:\012- Mach-O 64-bit arm64 executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL|PIE>]
```

<img width="1265" height="248" alt="image" src="https://github.com/user-attachments/assets/2e7494dc-4453-458e-bbd4-52596efd90ba" />

<br>
<br>

```bash
ubuntu@tryhackme:~/storage/Installer/DevelopAI.app/Contents/Resources$ file script
script: Bourne-Again shell script, ASCII text executable
```

<img width="1266" height="240" alt="image" src="https://github.com/user-attachments/assets/e86f6bf4-4d97-4b22-9d0d-20fb14a53553" />

<br>
<br>

```bash
ubuntu@tryhackme:~/storage/Installer/DevelopAI.app/Contents/Resources$ cat script
```

<img width="1260" height="506" alt="image" src="https://github.com/user-attachments/assets/572d21cd-908c-43a2-87bd-cb203e48c76c" />

<br>
<br>
<br>
<p>8.6. <em>Which persistence mechanism did the application use?</em><br>
<code>LaunchAgents</code></p>

```bash
root@tryhackme:/home/ubuntu/mac_mount/root/Users/lucasrivera/Library/LaunchAgents# ls
DevelopAI.sh  com.developai.agent.plist
```

<img width="1249" height="455" alt="image" src="https://github.com/user-attachments/assets/2599aaf3-f581-48ff-b690-7d6deb435f07" />

<br>
<br>

<img width="1261" height="243" alt="image" src="https://github.com/user-attachments/assets/0081d060-c05e-4e11-9c34-6e5a4d60d6f5" />


<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/090f3f28-8241-4302-81aa-444b38640e3c"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/0391c45f-b93b-4034-a719-3acb069766e8"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, November</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|22      |Hard 🚩 - The Last Trial               |   1    |      91ˢᵗ    |     3ʳᵈ    |     532ⁿᵈ   |      6ᵗʰ     |    133,762  |    1,030    |    80     |
|22      |Medium 🔗 - Data Integrity & Model Poisoning|   1|     94ᵗʰ    |     3ʳᵈ    |     762ⁿᵈ   |      7ᵗʰ     |    133,492  |    1,029    |    80     |
|22      |Easy 🔗 - LLM Output Handling and Privacy Risks|   1|  94ᵗʰ    |     3ʳᵈ    |     809ᵗʰ   |      7ᵗʰ     |    133,444  |    1,028    |    80     |
|22      |Easy 🔗 - Advent of Cyber Prep Track   |   1    |      94ᵗʰ    |     3ʳᵈ    |     826ᵗʰ   |      8ᵗʰ     |    133,428  |    1,027    |    80     |
|19      |Easy 🔗 - WAF: Introduction            |   2    |      91ˢᵗ    |     3ʳᵈ    |     737ᵗʰ   |      7ᵗʰ     |    133,348  |    1,026    |    80     |
|19      |Easy 🔗 - Django: CVE-2025-64459       |   2    |      93ʳᵈ    |     3ʳᵈ    |     877ᵗʰ   |      8ᵗʰ     |    133,224  |    1,025    |    80     |
|19      |Easy 🔗 - Django: CVE-2025-64459       |   2    |      93ʳᵈ    |     3ʳᵈ    |     877ᵗʰ   |      8ᵗʰ     |    133,224  |    1,025    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: Insecure Data Handling| 1        |      93ʳᵈ    |     3ʳᵈ    |     894ᵗʰ   |      8ᵗʰ     |    132,207  |    1,024    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: Application Design Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     927ᵗʰ   |      8ᵗʰ     |    132,183  |    1,023    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: IAAA Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     971ˢᵗ   |      8ᵗʰ     |    132,151  |    1,022    |    80     |
|14      |Hard 🚩 - Shock and Silence            |   1    |      94ᵗʰ    |     4ᵗʰ    |     749ᵗʰ   |      7ᵗʰ     |    133,095  |    1,021    |    80     |
|14      |Easy 🔗 - Input Manipulation & Prompt Injection| 1 |   95ᵗʰ    |     4ᵗʰ    |   1,290ᵗʰ   |     12ⁿᵈ     |    132,822  |    1,020    |    80     |
|14      |Hard 🚩 - CRM Snatch                   |   1    |      95ᵗʰ    |     4ᵗʰ    |   1,526ᵗʰ   |     12ⁿᵈ     |          -  |    1,019    |    80     |
|8       |Easy 🔗 - Living of the Land Attacks   |   1    |      91ˢᵗ    |     4ᵗʰ    |   1,759ᵗʰ   |     17ᵗʰ     |    132,642  |    1,018    |    80     |
|8       |Hard 🚩 - Lost in RAMslation           |   1    |      91ˢᵗ    |     4ᵗʰ    |   2,547ᵗʰ   |     25ᵗʰ     |    132,580  |    1,017    |    80     |
|8       |Easy 🔗 - MITRE                        |   1    |       -      |     4ᵗʰ    |      -      |      -       |          -  |       -     |    80     |

</h6></div><br>

<p align="center">Global All Time:     91ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/021801c9-466b-4b5b-a985-67cc01b405fe"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/280c45b3-de33-408c-9133-9fab59fc3274"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/a10ecc5d-4298-43cd-907f-d9e6cd7aaac8"><br><br>
                  Global monthly:     532ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/c90b927b-9d7f-46f3-8fc4-63434a6dfb1c"><br><br>
                  Brazil monthly:       6ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/e5c10f37-ed31-49ed-a4b0-512f8f824080"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
