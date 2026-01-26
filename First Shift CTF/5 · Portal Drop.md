<h1 align="center"><a href="https://tryhackme.com/room/first-shift-ctf">First Shift CTF</a> &nbsp;&nbsp; · &nbsp;&nbsp; Portal Drop</h1>
<p align="center">If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2024-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>


<h2>Portal Drop</h2>
<p>You are on the day shift in the ProbablyFine when the monitoring dashboard flashes red. A new alert appears in the WAF summary, reporting a web scan on <code>crm.trypatchme.thm</code> followed by a suspicious file upload anomaly. The affected website is TryPatchMe's public-facing CRM portal, a valued customer who provides software patching consulting services.<br>
That should be an easy case, since you have access to both the web access logs and the EDR console. Combined, they should give you a clear answer: either it's a False Positive, or the portal has been breached and TryPatchMe needs to patch the CRM now!</p>


<h2>EDR and Web Logs</h2>
<p> [ Download Task Files ] </p>
<p>For this challenge, you need to download the web access logs by clicking the "Download Task Files" button above, and for some questions, you will need the EDR console below: ...</p>

<p><em>Answer the questions below</em></p>

<br>
<p>5.1. <em>What is the IP address that initiated the brute force on the CRM web portal?</em><br>
<code>...</code></p>

<br>
<p>5.2. <em>How many successful and failed logins are seen in the logs?
Answer Example: 42, 56</em><br>
<code>...</code></p>


<br>
<p>5.3. <em>Following the brute force, which user-agent was used for the file upload?</em><br>
<code>...</code></p>


<br>
<p>5.4. <em>What was the name of the suspicious file uploaded by the attacker?</em><br>
<code>...</code></p>


<br>
<p>5.5. <em>At what time did the attacker first invoke the uploaded script?
Answer Example: 2025-10-24 15:35:50</em><br>
<code>...</code></p>


<br>
<p>5.6. <em>What is the first decoded command the attacker ran on the CRM?</em><br>
<code>...</code></p>


<br>
<p>5.7. <em>Based on the attacker’s activity on the CRM, which MITRE ATT&CK Persistence sub-technique ID is most applicable?</em><br>
<code>...</code></p>


<br>
<p>5.8. <em>Which process image executes attacker commands received from the web?</em><br>
<code>...</code></p>


<br>
<p>5.9. <em>What command allowed the attacker to open a bash reverse shell?</em><br>
<code>...</code></p>


<br>
<p>5.10. <em>Which Linux user executes the entered malicious commands?</em><br>
<code>...</code></p>


<br>
<p>5.11. <em>What sensitive CRM configuration file did the attacker access? </em><br>
<code>...</code></p>


<br>
<p>5.12. <em>Which domain was used to exfiltrate the CRM portal database?</em><br>
<code>...</code></p>


<br>
<p>5.13. <em>What flag do you get after completing all 12 EDR response actions?</em><br>
<code>...</code></p>




