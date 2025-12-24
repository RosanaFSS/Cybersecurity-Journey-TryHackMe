
<h1>YARA Rules - YARA mean one!</h1>
<p>Learn how YARA rules can be used to detect anomalies.</p>
<p>https://tryhackme.com/room/yara-aoc2025-q9w1e3y5u7</p>

<img width="900" height="900" alt="image" src="https://github.com/user-attachments/assets/0e405d29-3b1b-4ce2-a4ab-dbbc7d328335" />

<p>THM-CTXGR9UKQ5</p>
<p>https://tryhackme-certificates.s3-eu-west-1.amazonaws.com/THM-2TYQPVDXYN.pdf</p>

<img width="1272" height="770" alt="image" src="https://github.com/user-attachments/assets/4bc35ea0-cfa4-4e22-b563-730f45a934fe" />

<img width="907" height="903" alt="image" src="https://github.com/user-attachments/assets/d83e8dd4-d8b6-44ad-8c47-04b328ec4b84" />





<img width="1897" height="396" alt="image" src="https://github.com/user-attachments/assets/48dd4c99-25b4-4b23-a201-89dafed2057a" />


<h2>1 . Introduction</h2>

<img width="1200" height="407" alt="image" src="https://github.com/user-attachments/assets/aaceb9c4-56d3-47ae-9c23-a37804e22a5c" />


<p><em>Answer the questions below</em></p>
<p>1.1. <em>Let's go!</em><br>
<code>No answer needed</code></p>


<h2>2 . YARA Rules</h2>
<h3>YARA Overview</h3>
<p>At this stage, McSkidy, the lead defender, has entrusted you with a mission involving the use of YARA rules. Before jumping into action, let’s take a closer look at what YARA is, how it works, and why it’s such a valuable tool in TBFC’s fight to protect SOC-mas.<br>

YARA is a tool built to identify and classify malware by searching for unique patterns, the digital fingerprints left behind by attackers. Imagine it as a detective’s notebook for cyber defenders: instead of dusting for prints, YARA scans code, files, and memory for subtle traces that reveal a threat’s identity.</p>

<img width="1496" height="995" alt="image" src="https://github.com/user-attachments/assets/9557911e-de9b-40b2-9cb8-4ee91232cc05" />

<p>Within TBFC, YARA serves as a silent guardian, scanning through systems and uncovering the faintest traces of malicious activity that others might overlook. Now, as snow drifts over Wareville and the SOC-mas network trembles under threat, it’s your turn to wield this tool and restore the balance.</p>

<h3>Why YARA Matters and When to Use It</h3>
<p>You might wonder why McSkidy chose this tool for the mission. In the world of cyberattacks, defenders face an endless stream of alerts, suspicious files, and anomalous network fragments. Not every threat stands out; some hide in plain sight, disguised as harmless documents or scripts. That's where YARA shines.
YARA gives defenders the power to detect malware by its behavior and patterns, not just by name. YARA allows you to define your own rules, providing your own view of what constitutes "malicious" behavior. And you’re not alone, many YARA rules have already been written by defenders from other kingdoms that once faced similar threats. You can use, adapt, and improve these shared rules to strengthen TBFC’s defenses and protect SOC-mas together. For the defenders of SOC-mas, this means faster detection, smarter hunts, and fewer threats slipping by unseen.</p>



<h3>YARA Values</h3>


<h3>YARA Rules</h3>


<h3>YARA Study Use Cases</h3>
<p>a trojan known as IcedID to steal credentials from systems. McSkidy's analysts discovered that the malicious files spread across Wareville shared a common signature, the same MZ header found in executable malware used by the Dark Kingdom. These samples were small, lightweight loaders designed to infiltrate systems and later summon more dangerous payloads. Let's write our YARA rule.</p>






<p><em>Answer the questions below</em></p>

<p>2.1. <em>How many images contain the string TBFC?</em><br>
<code>5</code></p>

buntu@tryhackme:~/Downloads/easter$ cat a.yara
rule a
{
  strings:
  $a = "TBFC:" ascii

  condition:
  $a
}


ubuntu@tryhackme:~/Downloads/easter$ ls
easter1.jpg   easter16.jpg  easter22.jpg  easter29.jpg  easter35.jpg  easter41.jpg  easter48.jpg  easter54.jpg  easter60.jpg
easter10.jpg  easter17.jpg  easter23.jpg  easter3.jpg   easter36.jpg  easter42.jpg  easter49.jpg  easter55.jpg  easter7.jpg
easter11.jpg  easter18.jpg  easter24.jpg  easter30.jpg  easter37.jpg  easter43.jpg  easter5.jpg   easter56.jpg  easter8.jpg
easter12.jpg  easter19.jpg  easter25.jpg  easter31.jpg  easter38.jpg  easter44.jpg  easter50.jpg  easter57.jpg  easter9.jpg
easter13.jpg  easter2.jpg   easter26.jpg  easter32.jpg  easter39.jpg  easter45.jpg  easter51.jpg  easter58.jpg  embeds
easter14.jpg  easter20.jpg  easter27.jpg  easter33.jpg  easter4.jpg   easter46.jpg  easter52.jpg  easter59.jpg
easter15.jpg  easter21.jpg  easter28.jpg  easter34.jpg  easter40.jpg  easter47.jpg  easter53.jpg  easter6.jpg



ubuntu@tryhackme:~/Downloads/easter$ yara -r a.yara /home/ubuntu/Downloads/easter/
a /home/ubuntu/Downloads/easter//a.yara
a /home/ubuntu/Downloads/easter//easter46.jpg
a /home/ubuntu/Downloads/easter//embeds
a /home/ubuntu/Downloads/easter//easter16.jpg
a /home/ubuntu/Downloads/easter//easter10.jpg
a /home/ubuntu/Downloads/easter//easter52.jpg
a /home/ubuntu/Downloads/easter//easter25.jpg


<img width="1078" height="406" alt="image" src="https://github.com/user-attachments/assets/f2f4ce85-4f90-4001-ba26-46c2b0a2d350" />




<p>2.2. <em>What regex would you use to match a string that begins with TBFC: followed by one or more alphanumeric ASCII characters?</em><br>
<code>/TBFC:[A-Za-z0-9]+/</code></p>


<p>2.3. <em>W</em><br>
<code>Find me in HopSec Island</code></p>


ubuntu@tryhackme:~/Downloads/easter$ cat a.yara
rule a
{
  strings:
  $a = /TBFC:[A-Za-z0-9]+/

  condition:
  $a
}



ubuntu@tryhackme:~/Downloads/easter$ yara -r -s a.yara /home/ubuntu/Downloads/easter/
a /home/ubuntu/Downloads/easter//easter46.jpg
0x2f78a:$a: TBFC:HopSec
a /home/ubuntu/Downloads/easter//easter10.jpg
0x137da8:$a: TBFC:Find
a /home/ubuntu/Downloads/easter//easter16.jpg
0x3bb7f7:$a: TBFC:me
a /home/ubuntu/Downloads/easter//easter52.jpg
0x2a2ad2:$a: TBFC:Island
a /home/ubuntu/Downloads/easter//easter25.jpg
0x42c778:$a: TBFC:in


<img width="1164" height="356" alt="image" src="https://github.com/user-attachments/assets/9917f6a2-9804-434e-93dc-3a63e285f71c" />




<br>

<h1 align="center">Completed</h1>



<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/03027d73-89ad-441b-af1f-846fc59014ea"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/1876f36d-25e6-4a01-b64f-78bdb60a7d15"><br><br>
                  <img width="350px" src="https://github.com/user-attachments/assets/9106f594-329c-4a73-a011-50824f8d07c0"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/af4bf78b-b8e7-4dc7-902f-4af21975c211"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|24      |Medium 🔗 - YARA Rules - YARA mean one!          |8 |     100ᵗʰ  |     3ʳᵈ    |   10,263ʳᵈ   |      127ᵗʰ     |    135,168  |    1,050    |    84     |
|24      |Easy 🔗 - Exploitation with cURL - Hoperation Eggsploit|8 |100ᵗʰ |     3ʳᵈ    |   12,804ᵗʰ   |      154ᵗʰ     |    135,144  |    1,049    |    84     |
|24      |Medium 🔗 - Phishing - Phismas Greetings         |8 |     100ᵗʰ  |     3ʳᵈ    |   14,507ᵗʰ   |      174ᵗʰ     |    135,112  |    1,048    |    84     |
|24      |Easy 🔗 - n8n: CVE-2025-68613                    |8 |     102ⁿᵈ  |     3ʳᵈ    |   18,279ᵗʰ   |      205ᵗʰ     |    135,064  |    1,047    |    84     |
|24      |Medium 🔗 - C2 Detection - Command & Carol       |8 |     101ˢᵗ  |     3ʳᵈ    |   17,260ᵗʰ   |      193ʳᵈ     |    135,048  |    1,046    |    84     |
|23      |Easy 🔗 - AWS Security - S3cret Santa            |7 |      99ᵗʰ  |     3ʳᵈ    |   16,068ᵗʰ   |      182ⁿᵈ     |    135,008  |    1,045    |    84     |
|23      |Easy 🔗 - Malware Analysis - Malhare.exe         |7 |      99ᵗʰ  |     3ʳᵈ    |   17,332ⁿᵈ   |      191ˢᵗ     |    134,968  |    1,044    |    84     |
|20      |Medium 🔗 - Containers - DoorDasher's Demise     |4 |     100ᵗʰ  |     3ʳᵈ    |   18,059ᵗʰ   |      206ᵗʰ     |    134,864  |    1,043    |    84     |
|20      |Medium 🔗 - Forensics - Registry Furensics       |4 |     100ᵗʰ  |     3ʳᵈ    |   20,497ᵗʰ   |      239ᵗʰ     |    134,832  |    1,042    |    84     |
|20      |Medium 🔗 - Web Attack Forensics - Drone Alone   |4 |     100ᵗʰ  |     3ʳᵈ    |   21,935ᵗʰ   |      243ʳᵈ     |    134,808  |    1,041    |    84     |
|20      |Easy 🔗 - XSS - Merry XSSMas                     |4 |     100ᵗʰ  |     3ʳᵈ    |   23,069ᵗʰ   |      256ᵗʰ     |    134,792  |    1,040    |    84     |
|20      |Easy 🔗 -  Race Conditions - Toy to The World    |4 |     100ᵗʰ  |     3ʳᵈ    |   24,717ᵗʰ   |      275ᵗʰ     |    134,768  |    1,039    |    84     |
|20      |Medium 🔗 -  SOC Alert Triaging - Tinsel Triage  |4 |     100ᵗʰ  |     3ʳᵈ    |   25,202ⁿᵈ   |      286ᵗʰ     |    134,752  |    1,038    |    84     |
|19      |Medium 🔗 -  ICS/Modbus - Claus for Concern      |3 |     101ˢᵗ  |     3ʳᵈ    |   28,869ᵗʰ   |      337ᵗʰ     |    134,658  |    1,037    |    84     |
|19      |Easy 🔗 -  Passwords - A Cracking Christmas      |3 |     101ˢᵗ  |     3ʳᵈ    |   29,583ʳᵈ   |      340ᵗʰ     |    134,642  |    1,036    |    84     |
|18      |Easy 🔗 -  Prompt Injection - Sched-yule conflict|2 |     101ˢᵗ  |     3ʳᵈ    |   30,518ᵗʰ   |      353ʳᵈ     |    134,626  |    1,035    |    84     |
|18      |Medium 🔗 -  Obfuscation - The Egg Shell File    |2 |     101ˢᵗ  |     3ʳᵈ    |   30,967ᵗʰ   |      358ᵗʰ     |    134,618  |    1,034    |    84     |
|17      |Medium 🔗 - CyberChef - Hoperation Save McSkidy  |1 |     101ˢᵗ  |     3ʳᵈ    |   32,378ᵗʰ   |      374ᵗʰ     |    134,602  |    1,033    |    84     |
|7       |Medium 🔗 - Malware Analysis - Egg-xecutable     |2 |      95ᵗʰ  |     3ʳᵈ    |   11,604ᵗʰ   |      145ᵗʰ     |    134,544  |    1,034    |    84     |
|7       |Easy 🔗 - Network Discovery - Scan-ta Clause     |2 |      95ᵗʰ  |     3ʳᵈ    |   18,575ᵗʰ   |      208ᵗʰ     |    134,522  |    1,033    |    84     |
|7       |Easy 🔗 - React2Shell: CVE-2025-55182            |2 |      95ᵗʰ  |     3ʳᵈ    |   28,593ʳᵈ   |      326ᵗʰ     |    134,474  |    1,032    |    81     |
|6       |Medium 🔗 - IDOR - Santa´s Little IDOR           |1 |      95ᵗʰ  |     3ʳᵈ    |   27,309ᵗʰ   |      328ᵗʰ     |    134,450  |    1,031    |    81     |
|6       |Easy 🔗 - AI in Security - old sAInt nick        |1 |      95ᵗʰ  |     3ʳᵈ    |   41,626ᵗʰ   |      526ᵗʰ     |    134,426  |    1,030    |    81     |
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?        |1 |      95ᵗʰ  |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas              |1 |      96ᵗʰ  |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells               |1 |      97ᵗʰ  |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>


<p align="center">Global All Time:    100ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/23c7b0be-8da0-4407-a8a4-0002fe83c58c"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/42896565-24bd-4a8a-9984-6b379de402a3"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/457f6039-c9f7-4a54-b75d-7a0fb237f74a"><br><br>
                  Global monthly:  10,263ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/1e84a0a7-6336-4fa5-b692-617f5affde96"><br><br>
                  Brazil monthly:     127ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/9a7d7198-adb8-4c09-8c04-7f849b8ece99"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>






