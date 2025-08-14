<h1 align="center">Systems as Attack Vectors</h1>
<p align="center">2025, August 14<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>465</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn how attackers exploit vulnerable and misconfigured systems, and how you can protect them.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/0c8bcb7f-0b48-4f59-8e72-a391b1dd6b0c"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/systemsattackvectors">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/d5a73436-420b-4537-8b99-a5bcc4871223"></p>

<br>

<h2>Task 1 . Introduction</h2>
<p>Continue exploring the SOC role in protecting the digital world, now focusing on systems as attack vectors. In this room, you will learn what the systems are, why and how threat groups target them, and what you can do as a SOC analyst to keep your company secure.</p>

<h3>Learning Objectives</h3>
<p>

- Learn the role of a system in a modern digital world<br>
- Explore a variety of real-world attacks targeting systems<br>
- Practice the acquired knowledge in two realistic scenarios</p>

<h3>Prerequisites</h3>
<p>

- Complete the <strong>Junior Security Analyst Intro</strong> room
- Complete the <strong>Humans as Attack Vectors</strong> room</p>

<br>
<p><em>Answer the question below</em></p>

<p>1.1. I´m ready to learn!<br>
<code>No answer needed</code></p>
<br>
<br>
<h2>Task 2 . Definition of System</h2>
<p>Imagine a castle again, but now with a trained gatekeeper who knows how to identify phishing and how to combat deepfakes. However, if the lock on the main gate is fragile and cheap, guardian skills do not matter, as the enemy can just sneak into the castle while no one is watching. In cyber terms, threat actors can attack insecure systems directly, without the users' knowledge.</p>

<br>

<h6 align="center"><img width=90px" src="https://github.com/user-attachments/assets/6632e5de-0442-4afc-a139-0270461652a6"><br><em>TryHackMe</em></h6>

<br>
<h3>Definition of System</h3>
<p>Where do the banks store your cards, or where are your emails stored? The answer - on a system: a physical server, a virtual machine, or a cloud platform like Microsoft 365. Protecting such systems is crucial: if the attackers breach one user's mailbox via phishing, they compromise a single mailbox, but if they breach a mail server, they now control all thousands of mailboxes. Each system type can have a different value for threat actors, for example:</p>
<br>

<h6 align="center"><img width=900px" src="https://github.com/user-attachments/assets/fbe96049-24f7-4d9d-89a0-d418e5bf007b"><br><em>TryHackMe</em></h6>

<br>
<p><em>Answer the questions below</em></p>

<p>2.1. Can cyber attacks happen without victim intervention (Yea/Nay)?<br>
<code>Yea</code></p>
<br>

<p>2.2. Can a breach of just a single system lead to disastrous consequences (Yea/Nay)?<br>
<code>Yea</code></p>

<br>
<br> 
<h2>Task 3 . Attacks on Systems</h2>
<p>In most serious attacks, the first goal is to gain access to the target system. What happens next depends on the attacker's motivation: stealing data, deploying ransomware, or even destroying information without a way to recover. However, nearly all attacks begin the same way. Let's look at three examples of how systems are attacked.</p>
<h3>Human-Led Attacks
<p>It's no surprise that system users are often those who start the attack: By inserting a malicious USB found on a street, downloading malware from pirated resources, or simply reusing a weak password everywhere. 81% of breaches involve stolen or breached passwords - check out your passwords too!</p>
<br>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/8b4eebf5-b05d-4d7e-97f4-93f9b0411a57"><br><em>TryHackMe</em></h6>

<br>
<h3>Vulnerabilities</h3>
<p>Every piece of software can have security flaws. In 2024, over 40,000 software vulnerabilities were published and more than 300 were actively exploited in major attacks. Moreover, IT administrators often increase the risks by setting weak passwords and allowing unrestricted access to their systems.</p>
<br>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/eb7f36f3-5726-45ce-b521-a72d0e3f3040"><br><em>TryHackMe</em></h6>

<br>
<h3>Supply Chain</h3>
<p>Your PC is home to hundreds of apps, including web browsers, messengers, development, and entertainment software. Every app depends on thousands of libraries. If threat actors manage to breach one of the apps or libraries and push an update to all its users, all of them will be compromised. This technique is called a supply chain attack. The most famous examples are the SolarWinds and 3CX breaches which affected thousands of companies.</p>

<h4>Emerging Threat of Supply Chain</h4>
<p>It is hard to protect from supply chain attacks since you can't always control all the software present on your laptops, servers, and web apps. Even TryHackMe once fell victim to a supply chain in Lottie Player, a library used for room animations. As a SOC analyst, you must be ready for such scenarios and know how to respond!</p>

<p><em>Answer the questions below</em></p>

<p>3.1. What is the term for a security flaw that can be exploited to breach a system?<br>
<code>vulnerability</code></p>
<br>

<p>3.2. What is the name of the attack when malware comes from a trusted app or library?<br>
<code>Supply Chain</code></p>

<br>
<br>  
<h2>Task 4 . Vulnerabilities</h2>
<h3>Software Vulnerabilities</h3>
<p>Every piece of software has flaws, but some take years to be discovered. For example, Shellshock, a major Linux vulnerability, existed since 1992 but wasn't found until 2014. In the worst-case scenario, attackers discover the vulnerability before anyone else. This is known as a zero-day, and only your SOC skills can determine whether it gets detected in time.<br><br>

Once a vulnerability is made public, it is assigned a Common Vulnerabilities and Exposures (CVE) number. From that moment, it's a race: attackers develop exploits while defenders rush to update their systems. Here is the timeline of how Windows vulnerabilities evolve every year:</p>
<br>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/d9400636-7d21-4c59-bd9b-0a3145cf4f72"><br><em>TryHackMe</em></h6>

<br>
<h3>Responding to Vulnerabilities</h3>
<p>An answer to a CVE is always a patch - an update supplied by the software vendor. Even for zero-days, you'll have to wait for a patch, vigilantly monitor for exploitation traces, and try to survive the stressful period before the patch is released. For example, by:<br><br>

- Restricting access to the system to only trusted IPs<br>
- Applying temporary measures provided by the vendor<br>
- Blocking known attack patterns on IPS or WAF</p>

<p><em>Answer the questions below</em></p>

<p>4.1. What is the CVE for the critical SharePoint vulnerability dubbed "ToolShell"? Hint : You might need external research to answer this question.<br>
<code>Nay</code></p>
<br>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/ced99514-1592-43b8-85b6-8386d53a66f3"><br><em>Exploit Database</em></h6>

<br>

<p>4.2. How would you respond to a detected vulnerability on your system? Hint : The answer is a synonym of "update".<br>
<code>patch</code></p>

<br>
<br>
<h2>Task 5 . Misconfigurations</h2>
<h3>Misconfigurations</h3>
<p>On the other hand, a misconfiguration isn't a bug in the software but a mistake in how the system was set up, often by the IT team. These errors happen frequently, usually to make things simpler, like using "1111" instead of typing a long password every time. Let's take a look at some real-world examples.<br><br>

- How "123456" password exposed chats for 64 million McDonald's job applications<br>
- How a misconfigured AWS cloud resulted in a breach of 106 million bank customers<br>
- How improperly configured smart fridges are silently used in full-scale botnet attacks<br><br>
Another common scenario is when the IT department unknowingly introduces new flaws into secure systems. Below is a simple example of how a critical database can be breached because of the insecure configuration:</p>
<br>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/564fcb6e-5319-4aba-9711-f0cd56887c27"><br><em>TryHackMe</em></h6>

<br>
<h3>Responding to Misconfigurations</h3>
<p>Misconfigurations do not require a software update - just a better setup. As a SOC analyst, you'll often spot them only after threat actors exploit them. However, in smaller companies, you might also be responsible for a more proactive response, for example:<br>

- Penetration Testing: Hire ethical "hackers" who simulate an attack and report on discovered security flaws<br>
- Vulnerability Scans: Periodically run tools that can detect default passwords or outdated software<br>
- Configuration Audits: Manually review the systems to match best practices like CIS benchmarks</p>

<p><em>Answer the questions below</em></p>

<p>5.1.Can a system patch or software update fix the misconfigurations (Yea/Nay)?<br>
<code>Nay</code></p>

<br>

<p>5.2. Which activity involves an authorized cyber attack to detect the misconfigurations?<br>
<code>Penetration Testing</code></p>

<br>
<br>
<h2>Task 6 . Practice</h2>
<p>Remember our fortress analogy? Attackers are opportunists. They'll often seek the easiest path, whether through a flaw in the building itself or by manipulating someone to open a door. Attackers don't see "human hacking" and "system hacking" as separate, so you should apply equal effort into protecting both humans and systems, combining <strong>Mitigation</strong> and <strong>Detection</strong>:</p>

<br>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/32cca28f-c545-40ad-9755-3fdde5d1cf81"><br><em>TryHackMe</em></h6>

<br>

<p>Unlike humans, you can't train the system to spot the attack. However, you can train your IT department to configure the systems and explain how to avoid simple mistakes. Below are the most common mitigation measures to protect your systems:</p>
<br>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/00573785-eadd-426a-ab2d-e36d057545e9"><br><em>TryHackMe</em></h6>

<br>

<h3>Practice</h3>
<p>[ View Site ]</p>
<p>For this lab, continue your SOC analyst journey at TryHackMe. This time, decide what to do with the <strong>Systems at Risk</strong> and choose the best measures to protect your systems at the <strong>Remediation Plan</strong> tabs. Open the security dashboard by clicking the <strong>View Site</strong> button, complete the tasks, and claim the flags to answer the task questions!</p>

<br>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/58742cc2-85fc-407c-9939-88c95c53c846"><br><em>TryHackMe</em></h6>

<br>

<p><em>Answer the questions below</em></p>

<p>6.1. What flag did you receive after completing the "Systems at Risk" challenge?<br>
<code>THM{patch_or_reconfigure?}</code></p>

<br>

<p>6.2. What flag did you receive after completing the "Remediation Plan" challenge?<br>
<code>THM{best_systems_defender!}</code></p>

<br>
<br>
<h2>Task 7 . Conclusion</h2><br><br>
<p>Even though SOC analysts don't typically manage systems directly, understanding the common attacks and defenses, and sharing them with the IT department, is a key to broadening your cyber security perspective. If you want to grow quickly and be a strong team player, stay updated on the latest threats and always share the news with others!

- The DFIR Report: How Real Intrusions Happen<br>
- CISA: Known Exploited Vulnerabilities Catalog<br>
- BleepingComputer: Latest Supply Chain Attacks<br>
- CheckPoint: Interactive Live Cyber Threat Map</p>

<p><em>Answer the question below</em></p>

<p>7.1. Complete the room!<br>
<code>No answer needed</code></p>

<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c53eaace-633f-42b0-97a7-bad05af2974e"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/fc8af68a-2368-4b2a-ad29-dac5251d26a7"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 14   |   465    |     120ᵗʰ    |      5ᵗʰ     |     302ⁿᵈ   |     9ᵗʰ    | 121,354  |    918    |    73     |


</div>

<p align="center">Global All Time:   120ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/8d119e4e-91b6-4ab8-a3af-3fbfa679d192"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/61afe0ca-9142-4ea4-819c-0d88fd813c0e"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/81f47408-c7fd-44d9-90be-7af80e29a569"><br>
                  Global monthly:    302ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/118c785e-5529-477c-a07b-5eaf5c64c6b1"><br>
                  Brazil monthly:      9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/2499cbee-ad76-46b4-9add-aa1ddf53215b"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
