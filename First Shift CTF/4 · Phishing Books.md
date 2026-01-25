<h1 align="center"><a href="https://tryhackme.com/room/first-shift-ctf">First Shift CTF</a> &nbsp;&nbsp; · &nbsp;&nbsp; Phishing Books</h1>
<p align="center">If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2024-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>


<br>
<h2>Phishing Books</h2>
<p>It's another typical day at ProbablyFine Ltd. Your SOC dashboard is glowing with endless alerts, most of them false positives, as usual. Your team manages several education-sector clients, including universities, schools, and research institutes across the UK. Today, you are in charge of monitoring alerts from universities in London.<br>

Normally, things stay quiet. These universities are very targeted by phishing attacks, but most attempts get stopped by the email filters before anyone even sees them. But today is different. You got an email from a university teacher:</p>

```bash
Subject: MFA Removal Requests
From: Dr. Isabella <isabella@kingford.ac.uk>

Hey, ProbablyFine SOC Team,
I've been getting several emails asking me to approve my MFA.
Are you performing any tests? Should I approve these requests?
Dr. Isabella
```

<p>You contact Dr. Isabella directly, and it becomes clear that she has been targeted by a phishing email designed to steal her credentials, which is why she is receiving multiple MFA requests! You advise her to reset her password immediately.<br>

Now it's time to dig deeper: No alerts were triggered in your SIEM, so you requested the original <code>.eml</code> file of the phishing email to perform a manual investigation. Was this an isolated hit, or part of a larger phishing campaign targeting universities? Start the analysis machine and examine the email. Let's see what’s really going on!</p>

<h2>Machine Access</h2>
<p>For this challenge, you are given an instance containing the <code>.eml</code> file reported by Dr. Isabella. Ensure that you test and analyze the file inside the VM environment. Please start the machine by clicking the "Start Machine" button below.</p>


<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead. ...</p>

<p>You also have access to TryDetectThis, a threat intelligence database to check the reputation and other details of IP addresses, domains, and file hashes. To access this platform, please navigate to the following URL in your own browser, outside the VM environment: ...</p>

<p><em>Answer the questions below</em></p>

<br>
<p>4.1. <em>Which specific check within the headers explains the bypass of email filters?
Answer Example: "CHECK=value"</em><br>
<code>DMARC=none</code></p>

<img width="1234" height="619" alt="image" src="https://github.com/user-attachments/assets/dbb48c66-bb40-4608-9070-fa178859e21a" />

<br>
<br>
<br>
<p>4.2. <em>What technique did the attacker use to make the message seem legitimate?</em><br>
<code>Typosquatting</code></p>

<p>

- library@king<code>l</code>ord.ac.uk<br>
- isabella@king<code>f</code>ord.ac.uk</p>

<img width="1070" height="115" alt="image" src="https://github.com/user-attachments/assets/a2e3e937-4bf4-4a09-999e-fd52ff4f0c0b" />

<br>
<br>

<img width="1239" height="667" alt="image" src="https://github.com/user-attachments/assets/d0055fff-b15e-499a-93e1-e4f2b124c2bf" />

<br>
<br>
<br>
<p>4.3. <em>What technique did the attacker use to make the message seem legitimate?</em><br>
<code>T1583.001</code></p>

<p>https://attack.mitre.org/techniques/T1583/001/</p>

<img width="1896" height="641" alt="image" src="https://github.com/user-attachments/assets/daf23d3b-0838-43ae-9467-66c208e669f2" />

<br>
<br>
<br>
<p>4.4. <em>What is the file extension of the attached file?</em><br>
<code>.html</code></p>

<img width="1217" height="578" alt="image" src="https://github.com/user-attachments/assets/faeb504d-78a0-4747-87d3-e9c1cf0b583c" />

<br>
<br>

<img width="1222" height="273" alt="image" src="https://github.com/user-attachments/assets/dd5516d9-0f25-46d3-ab91-8c281dc0f981" />

<br>
<br>
<br>
<p>4.5. <em>What is the MD5 hash of the .HTML file?</em><br>
<code>442f2965cb6e9147da7908bb4eb73a72</code></p>

<img width="907" height="142" alt="image" src="https://github.com/user-attachments/assets/1e2c6ec1-9863-44c5-9dc8-d28fed9a4570" />

<br>
<br>

<img width="1291" height="271" alt="image" src="https://github.com/user-attachments/assets/7d39430a-10ac-466e-87e4-d1b1773a1ff2" />

<br>
<br>

<img width="1035" height="42" alt="image" src="https://github.com/user-attachments/assets/b8fbd477-9a2d-446c-88d8-78f5e3e40d4b" />

<br>
<br>
<br>
<p>4.6. <em>What is the landing page of the phishing attack?</em><br>
<code>http://lib-service.com:8083</code></p>

<p>

- download the e-mail attachment clicking on the down arrow<br>
- double-click <strong>library.invoice.pdf.html</strong></p>

<img width="1183" height="88" alt="image" src="https://github.com/user-attachments/assets/2a290a12-90ce-4137-8f6b-4d3afcea484f" />

<br>
<br>

<img width="1135" height="536" alt="image" src="https://github.com/user-attachments/assets/527b052a-0260-4bfa-bda6-8497dc32556f" />

<br>
<br>
<p>4.7. <em>What is the landing page of the phishing attack?</em> Hint: You need to navigate within the attached machine!<br>
<code>T1027</code></p>

<p>https://attack.mitre.org/techniques/T1027/</p>

<img width="1891" height="512" alt="image" src="https://github.com/user-attachments/assets/baecc311-18a9-4c8e-9ef9-7091f67ec5d0" />

<br>
<br>
<br>
<p>4.8. <em>What is the hidden message the attacker left in the file?</em><br>
<code>I love to phish books from libraries ^^</code></p>

<img width="1246" height="358" alt="image" src="https://github.com/user-attachments/assets/0397581d-7a6e-4956-ba3f-bcae7ecc81ac" />

<br>
<br>

<img width="1913" height="758" alt="image" src="https://github.com/user-attachments/assets/48611e0b-b101-499b-8dae-014636bd1d5b" />

<br>
<br>

<img width="1908" height="489" alt="image" src="https://github.com/user-attachments/assets/98fb3543-3693-4861-b644-474f3b62672f" />

<br>
<br>
<br>
<p>4.9. <em>Which line in the attached file is responsible for decoding the URL redirect?</em> Hint: Paste the full line exactly as you see in the file.<br>
<code>var src = reversed.split("").reverse().join("");</code></p>

<img width="1731" height="336" alt="image" src="https://github.com/user-attachments/assets/11ac3520-79eb-4d68-8046-97f3d76eb660" />

<br>
<br>
<br>
<p>4.10. <em>What is the first URL in the redirect chain?</em> Hint: Consider the browser visualization.<br>
<code>http://xn--librarytlu-13cwe32432-kwr.com:8082/</code></p>

<img width="1009" height="187" alt="image" src="https://github.com/user-attachments/assets/b3a680c5-fa9e-43ec-bf3e-a7ee96a88b7e" />

<br>
<br>

<img width="1047" height="104" alt="image" src="https://github.com/user-attachments/assets/e8813679-a8d6-4f9f-adfa-afc4650d856a" />

<br>
<br>

<img width="909" height="167" alt="image" src="https://github.com/user-attachments/assets/129b7fbf-4b77-40a3-a354-fec0d20e4a7e" />


<br>
<br>

<img width="957" height="84" alt="image" src="https://github.com/user-attachments/assets/01d0cd27-57cf-4fb0-89cf-b7e89ea5c6e6" />

<br>
<br>

<img width="1224" height="478" alt="image" src="https://github.com/user-attachments/assets/69510b4e-9a0c-4ac8-95d9-94cba1eda542" />

<br>
<br>
<br>
<p>4.11. <em>What is the Threat Actor associated with this malicious file and/or URL?</em> Hint: Add the exact information from TryDetectThis.<br>
<code>Cobalt Dickens | Silent Librarian</code></p>

<p>https://attack.mitre.org/groups/G0122/</p>

<img width="1891" height="585" alt="image" src="https://github.com/user-attachments/assets/6dfa7123-ba33-422c-9709-afdcbab11914" />


<br>
<br>
<br>
<p>4.12. <em>What is the main target of this Threat Actor according to MITRE?</em><br>
<code>Research and Proprietary Data</code></p>

<p>https://attack.mitre.org/groups/G0122/</p>

<img width="1891" height="585" alt="image" src="https://github.com/user-attachments/assets/6dfa7123-ba33-422c-9709-afdcbab11914" />
