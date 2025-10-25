<h1 align="center">Elevating Movement</h1>
<p align="center">2025, October 25  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>537</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Investigate the second, Windows part of the Honeynet Collapse! &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/elevatingmovement">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/7c99579b-0a08-4e18-9045-80dad21d2287"></p>

<h2>Task 1 . Introduction</h2>
<h3>Meet DeceptiTech</h3>
<p>DeceptiTech is a fast-growing cyber security company specializing in honeypot development and deception technologies. At the heart of their success are DeceptiPots - lightweight, powerful, and configurable honeypots that you can install on any OS and capture every malicious action!<br>

The internal DeceptiTech network is organized around a traditional on-premises Active Directory domain with approximately 50 active users. The product platform, however, is isolated and hosted entirely in the AWS cloud:</p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/e395fb77-ea8f-41f6-81c2-e5badbb2ebb0"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<h3>Elevating Movement</h3>
<p>One ordinary morning, DeceptiTech's entire network collapsed. Within minutes, all critical on-premises systems were locked down and encrypted. The IT department hurried to restore backups, while the security team rushed to their SIEM - only to find the backups corrupted and all SIEM data wiped clean.<br>

This room is about the second attack stage (#2 on the network diagram). As part of an external DFIR unit, can you help DeceptiTech perform a full-scope investigation and explain how the attack continued?</p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s go!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . The Challenge</h2>
<h3>Set up your environement</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<h3>Elevating Movement</h3>
<p><em>Hey Emily, when you are done with DeceptiPot deployment, can you take a look at SRV-IT-QA? It became unstable after we replaced the motherboard, so maybe you can debug what's going on there. ~ Matthew<br>

While Emily worked on the issue from a local admin account, the threat actor continued the attack. With the entry point secured and Emily's domain credentials stolen, they now wanted to explore opportunities for privilege escalation. Leveraging your knowledge of Windows forensics, can you uncover the elevating movement?</em></p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/6449fe3f-794e-4508-9ffb-ebff35d9c7c6"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<p><em>Answer the questions below</em></p>

<br>
<p>2.1. When did the attacker perform RDP login on the server? Answer Format Example: 2025-01-15 19:30:45<br>
<code>2025-06-30 16:33:18</code></p>


<img width="986" height="529" alt="image" src="https://github.com/user-attachments/assets/e834b26e-eeee-4afd-9f81-9929bc18c70c" />



<br>
<p>2.2. What is the full path to the binary that was replaced for persistence and privesc?<br>
<code>C:\Users\emily.ross\Documents\Coreinfo64.exe</code></p>

<img width="1394" height="342" alt="image" src="https://github.com/user-attachments/assets/9a935f7a-7f35-4e5a-a9eb-b17eaccb79a3" />





<br>
<p>2.3. What is the type or malware family of the replaced binary?<br>
<code>Meterpreter</code></p>


PS C:\Users\emily.ross\Documents> Get-FileHash "Coreinfo64.exe" -Algorithm MD5

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
MD5             42050FD1614C70266DDCEF0A419478C8                                       C:\Users\emily.ross\Documents...


PS C:\Users\emily.ross\Documents>



<img width="1886" height="886" alt="image" src="https://github.com/user-attachments/assets/4192b652-cd47-4204-be16-448bcff4ad3e" />

<br>
<p>2.4. Which full command line was used to dump the OS credentials?<br>
<code>____</code></p>



<img width="1361" height="393" alt="image" src="https://github.com/user-attachments/assets/c82732db-56e9-4279-ace6-3d42f2fa4cd6" />


<img width="896" height="218" alt="image" src="https://github.com/user-attachments/assets/d08a033c-8547-4eed-a420-15575beaabe6" />



<br>
<p>2.5. Using the stolen credentials, when did the attacker perform lateral movement? Answer Format Example: 2025-01-15 19:30:45<br>
<code>____</code></p>



<br>
<p>2.6. What is the NTLM hash of matthew.collins' domain password?<br>
<code>____</code></p>



<br>
<br>
<br>
