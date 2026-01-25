<h1 align="center"><a href="https://tryhackme.com/room/first-shift-ctf">First Shift CTF</a> &nbsp;&nbsp; · &nbsp;&nbsp; Probably Just Fine</h1>
<p align="center">If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2024-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>


<br>
<h2>Probably Just Fine</h2>
<p>Welcome to your first shift! You are greeted by an internal alert on the SOC dashboard titled "Unusual VPN login of susan.martin@probablyfine.thm from 37.19.201.132 (Singapore)."<br>

<h2>TryDetectThis</h2>
<p>TryDetectThis is a threat intelligence database to check the reputation and other details of IP addresses, domains, and file hashes. To access this platform, please navigate to the following URL in your own browser: ...</p>

<h2>Is It Really Fine</h2>
<p>That login IP looks suspicious, doesn't it? Your teammates reached out to Susan, and she confirmed she did not log in to the company VPN. She also mentioned that while using a public Wi-Fi hotspot at a cafe, she was suddenly prompted to install a "security check" tool, which she did. The host telemetry reveals a suspicious binary with the hash <strong>b8e02f2bc0ffb42e8cf28e37a26d8d825f639079bf6d948f8debab6440ee5630</strong>. Can you help us figure out what this binary exactly does and answer the remaining questions?</p>

<p><em>Answer the questions below</em></p>

<br>
<p>3.1. <em>What is the ASN number related to the IP?</em><br>
<code>212238</code></p>

<img width="1281" height="505" alt="image" src="https://github.com/user-attachments/assets/6ed64b7c-4c31-4075-827e-c16078769e7f" />

<br>
<br>

<img width="1273" height="301" alt="image" src="https://github.com/user-attachments/assets/3ec7522f-d533-4b96-9dc8-1501d29e9bc4" />

<br>
<br>
<br>
<p>3.2. <em>Which service is offered from this IP?</em><br>
<code>VPN</code></p>

<img width="436" height="70" alt="image" src="https://github.com/user-attachments/assets/2c418184-80f5-401e-b1cd-5e7bb68289f4" />

<br>
<br>

<img width="516" height="668" alt="image" src="https://github.com/user-attachments/assets/3852b360-bbe1-48e5-9d21-d1c316e43fb7" />

<br>
<br>
<br>
<p>3.3. <em>What is the filename of the file related to the hash?</em><br>
<code>zY9sqWs.exe</code></p>

<img width="1202" height="598" alt="image" src="https://github.com/user-attachments/assets/8d2f116d-2ba6-4f1b-95bf-5c4c6b09c38c" />

<br>
<br>

<img width="1270" height="623" alt="image" src="https://github.com/user-attachments/assets/9cf0b00b-1452-45f3-a7b3-709699a31002" />

<br>
<br>
<br>
<p>3.4. <em>What is the threat signature that Microsoft assigned to the file?</em><br>
<code>Trojan:Win32/LummaStealer.PM!MTB</code></p>

<img width="1226" height="253" alt="image" src="https://github.com/user-attachments/assets/ac67776f-b998-469f-a246-b9b9e88c5fb2" />

<br>
<br>
<br>
<p>3.5. <em>One of the contacted domains is part of a large malicious infrastructure cluster.
Based on its HTTPS certificate, how many domains are linked to the same campaign?</em><br>
<code>151</code></p>

<img width="1268" height="480" alt="image" src="https://github.com/user-attachments/assets/d6080b0b-cfa2-4c35-ba99-540a4117f93f" />

<br>
<br>

<img width="1258" height="735" alt="image" src="https://github.com/user-attachments/assets/146d06ed-b8fb-4d58-b882-f52a357e0b99" />

<br>
<br>

<img width="1278" height="145" alt="image" src="https://github.com/user-attachments/assets/52685978-22d8-48f0-a46f-e16f63476660" />

<br>
<br>

<img width="1276" height="830" alt="image" src="https://github.com/user-attachments/assets/2bf919aa-2d07-460b-ae9c-8bcff3dfc465" />

<br>
<br>

<img width="1274" height="251" alt="image" src="https://github.com/user-attachments/assets/c4c97eee-0401-4d60-b535-d15fe1d17d88" />

<br>
<br>

<img width="1278" height="281" alt="image" src="https://github.com/user-attachments/assets/3a3e9888-e308-41f0-8a5a-c8f9d33be419" />

<br>
<br>

<img width="1274" height="820" alt="image" src="https://github.com/user-attachments/assets/4c2498be-97cb-4108-98f9-bdba081045b6" />

<br>
<br>
<img width="1281" height="757" alt="image" src="https://github.com/user-attachments/assets/ee9cf4c3-ea56-4ca0-96ae-d7b4f59c3c48" />



</rb>
<br>
<br>
<br>
<p>3.6. <em>The file matches one of the YARA rules made by "kevoreilly".
What line is present in the rule's "condition" field?</em><br>
<code>uint16(0) == 0x5a4d and any of them</code></p>

<img width="1350" height="334" alt="image" src="https://github.com/user-attachments/assets/9eea22b2-09cc-41ea-94be-d5002f1ad820" />

<br>
<br>
<br>
<p>3.7. <em>The file is also mentioned in one of the TI reports.
What is the title of the report mentioning this hash?</em><br>
<code>Behind the Curtain: How Lumma Affiliates Operate</code></p>

<img width="1252" height="280" alt="image" src="https://github.com/user-attachments/assets/9c0d68e4-e94d-47b1-8063-5a381e6c974a" />

<br>
<br>
<br>
<p>3.8. <em>Which team did the author of the malware start collaborating with in early 2024?</em><br>
<code>GhostSocks</code></p>

<img width="1102" height="170" alt="image" src="https://github.com/user-attachments/assets/44f5da87-9bb3-456e-a84d-61c6f631c331" />


<br>
<br>
<br>
<p>3.9. <em>A Mexican-based affiliate related to the malware family also uses other infostealers.
Which mentioned infostealer targets Android systems?</em><br>
<code>CraxsRAT</code></p>

<img width="1013" height="151" alt="image" src="https://github.com/user-attachments/assets/f68ab966-b0c3-4d97-8448-fc57cd3432b2" />

<br>
<br>
<br>
<p>3.10. <em>The report states that the affiliates behind the malware use the services of AnonRDP.
Which MITRE ATT&CK sub-technique does this align with?</em><br>
<code>T1583.003</code></p>



<img width="1007" height="317" alt="image" src="https://github.com/user-attachments/assets/85a2da21-2ad7-41ca-8494-3e1ed754db5c" />

<br>
<br>

<img width="1050" height="412" alt="image" src="https://github.com/user-attachments/assets/abc6d1ea-e169-4d14-9039-c4d35c648025" />
