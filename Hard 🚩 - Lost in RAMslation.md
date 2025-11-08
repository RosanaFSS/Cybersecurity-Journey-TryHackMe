<h1 align="center">Lost in RAMslation</h1>
<p align="center">2025, November 8  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>1</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Use your memory forensics skills to unwrap the third stage of the Honeynet Collapse! &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/lostinramslation">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/10e41fbf-a463-4e79-9209-2593631b4f14"></p>

<h2>1 . Introduction</h2>
<h3>Meet DeceptiTech</h3>
<p>DeceptiTech is a fast-growing cyber security company specializing in honeypot development and deception technologies. At the heart of their success are DeceptiPots - lightweight, powerful, and configurable honeypots that you can install on any OS and capture every malicious action!<br>

The internal DeceptiTech network is organized around a traditional on-premises Active Directory domain with approximately 50 active users. The product platform, however, is isolated and hosted entirely in the AWS cloud:</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/34793d11-ee28-43ae-a4b0-c2ed81bbd0c6"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Lost in RAMslation</h3>
<p>One ordinary morning, DeceptiTech's entire network collapsed. Within minutes, all critical on-premises systems were locked down and encrypted. The IT department hurried to restore backups, while the security team rushed to their SIEM - only to find the backups corrupted and all SIEM data wiped clean.<br>
This room is about the third attack stage (#3 on the network diagram). As part of an external DFIR unit, can you help DeceptiTech perform a full-scope investigation and explain how the attack started?</p>

<br>
<p><em>Answer the question below</em></p>

<p>1.1. Let´s go!<br>
<code>No answer needed</code></p>

<br>
<h2>2 . The Challenge</h2>
<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<h3>Lost in RAMslation</h3>
<p><em>I just need one solid answer, not ten theories" - the project manager complained</em>.<br>

The logs for SRV-DMZ-GW looked normal, but the engineering team kept reporting odd slowdowns. With project deadlines looming, tensions in the office were running high.<br>

Matthew was lost chasing the process responsible for the issue. With deadlines approaching and pressure mounting, can you make sense of what's lost in RAMslation?</p>

<h3>Analysis Approach</h3>
<p>A memory dump that corresponds to the server SRV-DMZ-GW with the name <code>SRV-DMZ-GW-evidence.mem</code> is available at <code>/home/ubuntu/</code>. If you operate from the analyst account, use sudo to access the dump.</p>

<h6 align="center"><img height="900px" hspace="3" src="https://github.com/user-attachments/assets/b47d378b-d8af-4d69-af4b-df770ac0bcdf"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<br>
<p><em>Answer the questions below</em></p>

<br>
<p>2.1. What is the absolute path to the initial malicious file executed on this host?<br>
<code>C:\Windows\Tasks\MicrosoftUpdate.dll</code></p>

```bash
$ grep -E ".dll" pstree.txt
```

<img width="1726" height="149" alt="image" src="https://github.com/user-attachments/assets/9d5adc16-488e-46b6-bc26-734a9212f678" />

<br>
<br>
<p>2.2. Which process ID (PID) was assigned to the process used to execute the initial payload?<br>
<code>2928</code></p>

```bash
$ grep -E MicrosoftUpdate.dll cmdline.txt
```

<img width="1725" height="150" alt="image" src="https://github.com/user-attachments/assets/50251575-9567-4cd3-a79d-bf01e8f637d6" />

<br>
<br>
<p>2.3. What was the full command line used by the attacker to launch initial execution on this host?<br>
<code>rundll32.exe C:\windows\tasks\MicrosoftUpdate.dll, RunMe</code></p>

```bash
$ grep -E MicrosoftUpdate.dll cmdline.txt
```

<img width="1818" height="75" alt="image" src="https://github.com/user-attachments/assets/38f33df9-8850-4159-81ef-2af7838b79f5" />

<br>
<br>
<br>

```bash
$ grep -E 2928 cmdline.txt
```

<img width="1815" height="123" alt="image" src="https://github.com/user-attachments/assets/4a4494f4-1de4-4f4f-a706-e69f4f729bd8" />

<br>
<br>
<p>2.4. The attack launched various processes. What is the name of the final process in the chain?<br>
<code>notepad.exe</code></p>

```bash
$ grep -E 2928 pstree.txt | awk -F" " '{print "           "$2"            "$3"          "$4" "}'
```

```bash
$ grep -E 2676 pstree.txt | awk -F" " '{print "           "$2"            "$3"          "$4"          "$5" "}'
```

```bash
$ grep -E 1444 pstree.txt | awk -F" " '{print "           "$2"            "$3"          "$4"          "$5" "}'
```

<img width="1821" height="201" alt="image" src="https://github.com/user-attachments/assets/0566ce77-c5ef-4f7a-a2ba-edc0b95fe155" />

<br>
<br>
<p>2.5. What are the first five bytes (in hex, e.g., 4d5a9000) of the Meterpreter shellcode injected into it?<br>
<code>fc4889ce48</code></p>

```bash
$ cat malfind.txt
```

<img width="1815" height="807" alt="image" src="https://github.com/user-attachments/assets/4f76e249-263d-4504-9f19-bc8ee1a13da9" />

<br>
<br>
<p>2.6. Which is the IP address that the hosts perform a lateral movement using port 3389?<br>
<code>172.16.2.9</code></p>

```bash
$ grep -i 'ESTABLISHED' netscan.txt | grep -i '3389'
```

<img width="1817" height="89" alt="image" src="https://github.com/user-attachments/assets/1079a578-348a-4e06-b9f6-99e9c72bbaf5" />

<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/50730a1a-2048-46f9-97e7-1febf33c130b"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/90c2cd2f-5eb2-4fd7-8849-488851ab35f1"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, November</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|8       ||Hard 🚩 - Lost in RAMslation          |   1    |      88ᵗʰ    |      4ᵗʰ     |     106ᵗʰ    |     2ⁿᵈ    | 132,037 |  1,015    |    79     |

</h6></div><br>

<br>

<p align="center">Global All Time:   106ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/035d4bae-16f3-4da7-b57b-4077e0a63c47"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/5580eea4-6081-4241-80fc-2d4cf18d5856"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/2b334c14-f571-4aa5-bd1a-fa0cbc86e36c"><br>
                  Global monthly:    330ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/17bb71a4-1e52-40b3-a993-bb7df9a3a09a"><br>
                  Brazil monthly:      5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/206f4848-19c4-435e-a635-b42721bd921b"><br>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
