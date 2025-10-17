<h1 align="center">Network Traffic Basics</h1>
<p align="center">2025, October 17  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>529</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>This room teaches the basics of Network Traffic Analysis. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/networktrafficbasics">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/80b68132-dc56-4305-b4be-e9b89afef897"></p>


<h2>Task 1 . Introduction</h2>
<h3>Meet DeceptiTech</h3>
<p>DeceptiTech is a fast-growing cyber security company specializing in honeypot development and deception technologies. At the heart of their success are DeceptiPots - lightweight, powerful, and configurable honeypots that you can install on any OS and capture every malicious action!<br>

The internal DeceptiTech network is organized around a traditional on-premises Active Directory domain with approximately 50 active users. The product platform, however, is isolated and hosted entirely in the AWS cloud:</p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/e395fb77-ea8f-41f6-81c2-e5badbb2ebb0"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<h3>Initial Access Pot</h3>
<p>One ordinary morning, DeceptiTech's entire network collapsed. Within minutes, all critical on-premises systems were locked down and encrypted. The IT department hurried to restore backups, while the security team rushed to their SIEM - only to find the backups corrupted and all SIEM data wiped clean.<br>

This room is about the first attack stage (#1 on the network diagram). As a part of an external DFIR unit, can you help DeceptiTech to perform a full-scope investigation and explain how the attack started?</p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s go!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . The Challenge</h2>
<h3>Set up your environement</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<h3>Initial Access Pot</h3>
<p><em>We sell hundreds of DeceptiPots to the world every month, but we don't even use them in our network. Show me the value of our product, test it well, and schedule the demo. Deadline - next Monday!</em><br>

This is the task Emily Ross received from the company CEO. As a newly hired junior IT personnel at DeceptiTech, Emily didn't really know what to do but still decided to prepare for the demo: Configure DeceptiPot to replicate a corporate WordPress blog, deploy the machine in the corporate DMZ, expose it to the Internet, and see what it captures over the weekend. Little did she know, threat actors around the globe enjoyed testing the DeceptiPot, too! Can you find out how the attack on DeceptiTech started?

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/895e0fb1-96b4-4fcb-88d4-fb124c747a40"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<p><em>Answer the questions below</em></p>

<p>2.1. Which web page did the attacker attempt to brute force?<br>
<code>/wp-login.php</code></p>

<p><em>/var/log/apache2/access.log</em></p>

<img width="1328" height="285" alt="image" src="https://github.com/user-attachments/assets/d5317b2c-b68b-4287-8285-603668e691b3" />

<br>
<br>
<br>
<p>2.2. What is the absolute path to the backdoored PHP file?<br>
<code>/var/www/html/wordpress/wp-content/themes/blocksy/404.php</code></p>

```bash
ubuntu@deceptipot-demo:/var/log/apache2# cat access.log | grep 'theme'
```

<img width="1885" height="281" alt="image" src="https://github.com/user-attachments/assets/b599af74-1146-47ba-807a-5f2325207305" />

<br>
<br>

<img width="1802" height="194" alt="image" src="https://github.com/user-attachments/assets/87b35e6d-ed9f-4e05-abb6-19c53eb7935e" />

<br>
<br>
<br>
<p>2.3. Which file path allowed the attacker to escalate to root?<br>
<code>/etc/ssh/id_ed25519.bak</code></p>

```bash
ubuntu@deceptipot-demo:/var/log/audit$ ausearch -i -if audit.log | grep proctitle=
```

<img width="1288" height="511" alt="image" src="https://github.com/user-attachments/assets/27c6ed44-9326-4917-b59f-e36ad1e720e5" />

<br>
<br>
<br>
<p>2.4. Which IP was port-scanned after the privilege escalation?<br>
<code>172.16.8.216</code></p>

<img width="1257" height="627" alt="image" src="https://github.com/user-attachments/assets/d212e0c6-c340-4097-9e62-fd9968b16edc" />

<br>
<br>
<br>

<img width="1704" height="671" alt="image" src="https://github.com/user-attachments/assets/62c85479-801a-4ae9-97d9-ca9990f252f8" />

<br>
<br>
<br>
<p>2.5. What is the MD5 hash of the malware persisting on the host?<br>
<code>d6f2d80e78f264aff8c7aea21acb6ca6</code></p>

<img width="1675" height="419" alt="image" src="https://github.com/user-attachments/assets/4bd23249-733a-45c8-8876-f9ba0f302efe" />

<br>
<br>
<br>

<img width="1704" height="671" alt="image" src="https://github.com/user-attachments/assets/ee1a8650-1f2f-49f8-b9a3-7feb5d9f0116" />

<br>
<br>
<br>

```bash
root@deceptipot-demo:/etc/systemd/system# md5sum /usr/sbin/kworker
```

<img width="1674" height="507" alt="image" src="https://github.com/user-attachments/assets/861038e7-7039-420f-abbf-3b54dbedaec4" />

<br>
<br>
<br>

<p>2.6. Can you access the DeceptiPot in recovery mode? HInt: <em>Think beyond the logs and artifacts here!</em><br>
<code>THM{***************}</code></p>

<img width="1137" height="745" alt="image" src="https://github.com/user-attachments/assets/b2279495-7c0a-4cc2-8247-829e67037ed6" />

<br>
<br>
<br>

<img width="1236" height="210" alt="image" src="https://github.com/user-attachments/assets/ffec9c6f-a430-43d2-966b-582444363d1b" />


<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b88f92c8-a253-44f2-98c0-8a30ca78cc38"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/96008de3-ee38-4fea-8fc6-ea70ef59378a"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>


<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|17      |Hard 🚩 - Initial Access Pot           | 529    |      90ᵗʰ    |      4ᵗʰ     |      68ᵗʰ    |     2ⁿᵈ    | 131,456  |  1,006    |    79     |
|17      |Medium 🔗 - AllSignsPoint2Pwnage       | 529    |      90ᵗʰ    |      4ᵗʰ     |      87ᵗʰ    |     2ⁿᵈ    | 131,186  |  1,005    |    79     |
|16      |Easy 🔗 - Network Traffic Basics       | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,138  |  1,004    |    79     |
|16      |Medium 🔗 - Linux Threat Detection 3   | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,066  |  1,003    |    79     |
|15      |Medium 🔗 - Windows PrivEsc, in progress| 527   |      91ˢᵗ    |      4ᵗʰ     |      83ʳᵈ    |     2ⁿᵈ    | 131,050  |  1,002    |    79     |
|13      |Hard 🚩 - M4tr1x: Exit Denied          | 525    |      92ⁿᵈ    |      4ᵗʰ     |      76ᵗʰ    |     2ⁿᵈ    | 130,938  |  1,002    |    79     |
|12      |Easy 🔗 - Atlas                        | 524    |     101ˢᵗ    |      4ᵗʰ     |     251ˢᵗ    |     3ʳᵈ    | 129,902  |  1,001    |    76     |
|11      |Easy 🔗 - Brute Force Heroes           | 523    |     101ˢᵗ    |      4ᵗʰ     |     217ᵗʰ    |     3ʳᵈ    | 129,878  |  1,000    |    76     |
|11      |Hard 🚩 - Rocket                       | 523    |     102ⁿᵈ    |      4ᵗʰ     |     211ˢᵗ    |     3ʳᵈ    | 129,870  |    999    |    76     |
|10      |Easy 🚩 - Shadow Trace                 | 522    |     101ˢᵗ    |      4ᵗʰ     |     159ᵗʰ    |     3ʳᵈ    | 129,810  |    998    |    76     |
|10      |Easy 🔗 - Defensive Security Intro     | 522    |     103ʳᵈ    |      4ᵗʰ     |     357ᵗʰ    |     3ʳᵈ    | 129,405  |    997    |    76     |
|10      |Easy 🔗 - 25 Days of Cyber Security, Day 2| 522|      103ʳᵈ    |      4ᵗʰ     |     355ᵗʰ    |     3ʳᵈ    | 129,405  |    996    |    76     |
|9       |Medium 🔗 - Linux Threat Detection 2   | 521    |     103ʳᵈ    |      4ᵗʰ     |     326ᵗʰ    |     3ʳᵈ    | 129,373  |    996    |    76     |
|9       |Medium 🚩 - WWBuddy                    | 521    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,293  |    995    |    76     |
|8       |Hard 🚩 - Motunui                      | 520    |     103ʳᵈ    |      4ᵗʰ     |     383ʳᵈ    |     4ᵗʰ    | 129,201  |    994    |    76     |
|8       |Easy 🔗 - Man-in-the-Middle            | 520    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,141  |    993    |    76     |
|7       |Medium 🚩 - Profiles, in progress      | 519    |              |              |              |            | 129,021  |    992    |    76     |
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129,021  |    992    |    76     |
|6       |Easy 🚩 - DearQA                       | 518    |     105ᵗʰ    |      4ᵗʰ     |     333ʳᵈ    |     6ᵗʰ    | 128,991  |    991    |    76     |
|5       |Medium 🚩 - Frank & Herby try again.....| 517   |     106ᵗʰ    |      4ᵗʰ     |     300ᵗʰ    |     5ᵗʰ    | 128,931  |    990    |    76     |
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     233ʳᵈ    |     3ʳᵈ    | 128,871  |    989    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>

<br>

<p align="center">Global All Time:   90ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/a41f39c1-b371-46ea-8d14-133555f266e4"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/24917337-c85d-40e0-965c-2c6e39980e51"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/030763c2-6dab-443b-a4e1-64a350ece4e4"><br>
                  Global monthly:     68ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/64ff6155-1676-423c-937d-cec3873dbccd"><br>
                  Brazil monthly:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/9625a973-1201-4374-9f0e-06d9e346056c"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
