<h1 align="center"><a href="https://tryhackme.com/room/first-shift-ctf">First Shift CTF</a> &nbsp;&nbsp; · &nbsp;&nbsp; The Crown Jewel</h1>
<p align="center">If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2028-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<h2>The Crown Jewel</h2>
<p>You are on a shift, looking at the new alert coming from Imperium Labs - a company under MSSP monitoring long before you joined the team. It's hard to say what the company's primary focus is, but it has a global presence and undoubtedly has secrets to protect, especially those on heavily secured GitLab and Jira servers which store proprietary source code and project data.</p>

<h2>The Alert</h2>
<p>The alert you are looking at is called <code>Reverse Shell Outbound Connection Detected</code>, not something you see every day. Fortunately, you were able to obtain the raw PCAPs and Splunk logs for this event. Can you analyze the network traffic and logs to reconstruct and stop a sophisticated attack aimed at stealing the "Crown Jewel" data?</p>

<img width="1166" height="839" alt="image" src="https://github.com/user-attachments/assets/7940024e-a86d-4d9b-a3ef-7240215bcc29" />


<h2>Machine Access</h2>
<p>To access the VM, click the Start Machine button below. Please give the VM up to five minutes to start and piece together the attack chain:

- Detailed network traffic capture challenge.pcap that you can find on the network_traffic folder on the VM's Desktop<br>
- Pre-ingested Splunk logs (index=network_logs), which can be accessed at MACHINE_IP:8000</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p><em>Answer the questions below</em></p>

<br>
<p>7.1. <em>From which internal IP did the suspicious connection originate?)</em><br>
<code>10.10.10.100</code></p>

<br>
<p>7.2. <em>What outbound connection was detected as a C2 channel? (Answer example: 1.2.3.4:9996)</em><br>
<code>1.1.1.1:8080</code></p>

<img width="984" height="213" alt="image" src="https://github.com/user-attachments/assets/b433e23d-129b-4d07-a8c5-0aa470e3cb3e" />

<br>
<br>

<img width="1295" height="457" alt="image" src="https://github.com/user-attachments/assets/83055314-2623-4ed4-97fe-f40c024a9eec" />

<br>
<br>
<br>
<p>7.3. <em>Which MAC address is impersonating the gateway 10.10.10.1?</em><br>
<code>00:0c:29:11:22:33</code></p>

<img width="1300" height="307" alt="image" src="https://github.com/user-attachments/assets/f775d9cd-ac68-4cd5-858c-4b958e663e07" />

<br>
<br>
<br>
<p>7.4. <em>What is the non-standard User-Agent hitting the Jira instance?</em><br>
<code>CVE-202X-EXPLOIT</code></p>
  
index=network_logs extracted_host=jira
|  sort by +_time

<img width="1261" height="292" alt="image" src="https://github.com/user-attachments/assets/779b62ac-f4de-46b7-88b4-e177f1162dcc" />

<br>
<br>

<img width="1150" height="696" alt="image" src="https://github.com/user-attachments/assets/0cb7930e-7628-420e-b95f-e6939e410cc1" />

<br>
<br>

index=network_logs extracted_host=jira   "event.agent"="CVE-202X-EXPLOIT" 
| sort by +_time

<img width="1147" height="638" alt="image" src="https://github.com/user-attachments/assets/5f60571e-c15c-4532-af5c-9fbd9ee4ebf2" />

<br>
<br>
<br>
<p>7.5. <em>How many ARP spoofing attacks were observed in the PCAP?</em><br>
<code>90</code></p>

<br>
<p>7.6. <em>What's the payload containing the plaintext creds found in the POST request?</em><br>
<code>username=dev_user&password=SecretPassword!</code></p>

<img width="1248" height="570" alt="image" src="https://github.com/user-attachments/assets/faff1792-46bb-41a5-a6d0-bc0ca871db4e" />

<br>
<br>

<img width="1235" height="473" alt="image" src="https://github.com/user-attachments/assets/2ae03baf-b167-4ef7-88a9-0d006ea605f0" />

<br>
<br>
<br>
<p>7.7. <em>What domain, owned by the attacker, was used for data exfiltration?</em><br>
<code>exfil-domain.xyz</code></p>

<img width="1291" height="216" alt="image" src="https://github.com/user-attachments/assets/e1c806f2-92ea-44a5-a90c-292065009f82" />

<p>7.7. <em>What domain, owned by the attacker, was used for data exfiltration?</em><br>
<code>exfil-domain.xyz</code></p>

<img width="1291" height="216" alt="image" src="https://github.com/user-attachments/assets/e1c806f2-92ea-44a5-a90c-292065009f82" />

<br>
<br>
<br>
<p>7.8. <em>After examining the logs, which protocol was used for data exfiltration?</em><br>
<code>dns</code></p>

<img width="1295" height="748" alt="image" src="https://github.com/user-attachments/assets/2489d4cc-4114-4f0f-a08d-e4e859580a40" />

<br>
<br>

<img width="1900" height="892" alt="image" src="https://github.com/user-attachments/assets/1a97bbd4-ee29-4fe4-8c5f-a40c3dd21b1f" />


<br>
<br>
<br>
<img width="1328" height="497" alt="image" src="https://github.com/user-attachments/assets/12c78cac-9ce1-401e-8f29-0f2be84c8334" />

