<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 22 &nbsp;&nbsp; ·  &nbsp;&nbsp; C2 Detection - Command & Carol</h3>
<p align="center">2025, December 24  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in <a href="https://tryhackme.com">TryHackMe</a>.<br>Explore how to analyze a large PCAP and extract valuable information. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/detecting-c2-with-rita-aoc2025-m9n2b5v8c1">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/bcb6aaf3-0f1d-4ac5-8672-5bbfa1650c4b"><br><br><img width="1200px" src="https://github.com/user-attachments/assets/9c418033-6bb9-40f5-895a-c18231a32d4f"></p>
<br>
<h2 align="center">Read my complete walkthrough in Medium.<br>
Click here ➡️  <a href="https://medium.com/@RosanaFS/c2-detection-command-carol-advent-of-cyber-2025-day-22-tryhackme-walkthrough-beeee1606cd5">C2 Detection - Command & Carol</a></h2>
<br>
<br>
<br>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/3f9cffca-4518-40de-ba14-bca09661fd41"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>One of our stealthiest infiltrated elves managed to hop their way into Sir Carrotbane’s office and, lo and behold, discovered a bundle of cloud credentials just lying around on his desktop like forgotten carrots. The agent suspects these could be the key to regaining access to TBFC’s cloud network. If only the poor hare had the faintest clue what “the cloud” is, he’d burrow in himself. Let's help the elf utilise these credentials to try to regain access to TBFC's cloud network.</p>

<h3>Learning Objectives</h3>
<p></p>

- Learn the basics of AWS accounts.<br>
- Enumerate the privileges granted to an account, from an attacker's perspective.<br>
- Familiarise yourself with the AWS CLI.</p>

<h3>Lab Connection</h3>
<p>Before moving forward, review the questions in the connection card shown below:<br>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/620f08e1-a8d4-4a6e-b64b-b64a0b054bd7"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Start your target machine by clicking the <strong>Start Machine</strong> button below. The machine will open in split view and need about 2 minutes to fully boot. In case you can not see it, click the <strong>Show Split View</strong> button at the top of the page.</p>

<p><em>Answer the question below</em></p>
<br>
<p>1.1. <em>I have successfully started my target machine!</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 1 &nbsp; ·  &nbsp; Detecting C2 with RITA</h2>
<h3>The Magic of RITA</h3>


<h3>PCAP, I Convert Ye to Zeek logs</h3>


<h3>Now, Analyze This RITA</h3>



<h4>Search bar</h4>



<h4>Results pane</h4>


<h4>Details pane</h4>

<h3>What Is This?</h3>


<h3>Each Will Do His Part</h3>
<p>Now that everyone has gone through the manual, let's hunt those "malrabbits" down! We have put a lot of effort into capturing network traffic. Please analyze the ~/pcaps/rita_challenge.pcap with RITA and answer the questions below. Note: Use the learned steps to process the PCAP and analyze it with RITA.</p>

<p><em>Answer the questions below</em></p>
<br>
<p>2.1. <em>How many hosts are communicating with malhare.net?</em><br>
<code>6</code></p>

<br>
<p>2.2. <em>Which Threat Modifier tells us the number of hosts communicating to a certain destination?</em><br>
<code>prevalence</code></p>

<br>
<p>2.3. <em>What is the highest number of connections to rabbithole.malhare.net?</em><br>
<code>40</code></p>

<br>
<p>2.4. <em>Which search filter would you use to search for all entries that communicate to rabbithole.malhare.net with a beacon score greater than 70% and sorted by connection duration (descending)?</em><br>
<code>dst:rabbithole.malhare.net beacon:>=70 sort:duration-desc</code></p>

<br>
<p>2.5. <em>Which port did the host 10.0.0.13 use to connect to rabbithole.malhare.net?</em><br>
<code>80</code></p>


<br>
<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/555f1fd5-8cc8-4d18-b8ff-e9c46cb9f5fc"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/d47b2706-3c7c-4ffa-9c85-1a05c127cdb7"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/293aaa2e-fd0e-40d9-a574-352d81203999"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
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

<p align="center">Global All Time:   101ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/e48fc1a0-7ef8-4894-8802-16f38be579b5"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/1b1b020e-b9d3-4ec6-a6a2-764c689eac04"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/ab840231-d50f-455b-9703-8e668925d7fc"><br><br>
                  Global monthly:  17,260ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/187778a5-444a-465b-b595-58d21fde63db"><br><br>
                  Brazil monthly:     193ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/dd2e9a2f-72f4-4358-aa48-2b5a386e8b6f"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
