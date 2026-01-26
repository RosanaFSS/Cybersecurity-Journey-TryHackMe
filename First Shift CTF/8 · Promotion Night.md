<h1 align="center"><a href="https://tryhackme.com/room/first-shift-ctf">First Shift CTF</a> &nbsp;&nbsp; · &nbsp;&nbsp; Promotion Night</h1>
<p align="center">If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2024-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>


<h2>Promotion Night</h2>
<p>It was a glorious Friday at ProbablyFine Ltd. After weeks of sales calls and PoC demos, the team finally signed a contract with DeceptiTech - a major tech company recently hit with ransomware and in need of an MSSP. Monitoring was set to begin on Monday, but some of their clouds and on-premises systems had already been onboarded into the SIEM.<br>

To celebrate the win, the entire SOC team headed out for a big teambuilding.<br>
Everyone except you - the Level 1 analyst covering the night shift, just in case.<br>

The shift was quiet. Too quiet. Then a critical alert appeared: "Potential Ransom Note on DC-01". You blinked. Then blinked again. Then called your Level 2. No answer - just the automated message saying it's probably fine. Now, it's up to you to triage the alert alone. Tonight will either earn you the quickest promotion ever or be your last day at ProbablyFine. Good luck!</p>

<h2>Machine Access</h2>
<p>For this challenge, you are given a Splunk instance containing the scenario index. To access Splunk, click the Start Machine button below. Please give the VM up to five minutes to start and access it with this link from AttackBox or your VPN-connected device:

- https://LAB_WEB_URL.p.thmlabs.com</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p><em>Answer the questions below</em></p>

<br>
<p>8.1. <em>What was the network share path where ransomware was placed?</em><br>
<code>\\DC-01\SYSVOL\gaze.exe</code></p>

<p>

- 2025-10-24 16:37:37</p>

```bash
index=* cmd.exe
|  table _time, TargetFilename, CommandLine, ComputerName Image, Host, signature, TargetUser| sort by +_time
```

<img width="1304" height="331" alt="Screenshot 2026-01-24 194003" src="https://github.com/user-attachments/assets/6f2274e7-727c-4a24-b088-86da44de9e13" />

<br>
<br>
<br>
<p>8.2. <em>What is the value ransomware created to persist on reboot?</em> Hint : Provide the file name, task or service name, or a registry entry.<br>
<code>BabyLockerKZ</code></p>

<p>

- 2025-10-24 16:37:38</p>

```bash
index=* EventCode=13 "*gaze.exe"
| table _time, Image, TargetObject, ComputerName, User
| sort by +_time
```

<img width="1783" height="511" alt="image" src="https://github.com/user-attachments/assets/e8a3a072-f170-4bd6-924f-d46103c1f4d7" />

<br>
<br>
<br>
<p>8.3. <em>What was the most likely extension of the encrypted files?</em><br>
<code>._______</code></p>

```bash
index=* "*gaze.exe"
|  table _time, Description, OriginalFileName, CommandLine, TargetFileName
|  sort by +_time
```

```bash
index=* "*gaze.exe"
| table TargetFileName
|  stats count by TargetFileName
```


<br>
<p>8.4. <em>Which MITRE technique ID was used to deploy ransomware?</em><br>
<code>T1047</code></p>

<img width="1890" height="510" alt="image" src="https://github.com/user-attachments/assets/12b30f53-f01d-4d0d-b8cb-dfad0f21dd66" />

<br>
<br>
<br>
<p>8.5. <em>What ports of SRV-ITFS did the adversary successfully scan?</em>Specify via comma in the ascending order.</em><br>
<code>135, 139, 445, 3389, 5985</code></p>

<br>
<p>8.6. <em>What is the full path to the malware that performed the Discovery?</em><br>
<code>C:\Windows\System32\fr-FR\ruche.dll</code></p>

<img width="1306" height="272" alt="Screenshot 2026-01-24 194439" src="https://github.com/user-attachments/assets/181fea71-8cb9-41f8-b42e-ed9256877585" />

<br>
<br>
<br>
<p>8.7. <em>Which artifact did the adversary create to persist on the beachhead?</em><br>
<code>LanguageSync</code></p>

<img width="1295" height="698" alt="image" src="https://github.com/user-attachments/assets/ca7be0c4-d8eb-49e4-8d52-04eb324aea8b" />

<br>
<br>
<br>
<p>8.8. <em>What is the MD5 hash of the embedded initial shellcode?</em><br>
<code>____________________</code></p>

```bash
index=* "_______" Hashes!=""
| table CommandLine, Image, Hashes
|  sort by +_time
```
   

<br>
<p>8.9. <em>Which C2 framework was used by the adversary in the intrusion?</em><br>
<code>Cobalt Strike</code></p>


<br>
<p>8.10. <em>What hostname did the adversary log in from on the beachhead?</em><br>
<code>DESKTOP-J9PR0CO</code></p>

<img width="1286" height="669" alt="image" src="https://github.com/user-attachments/assets/f5340b6a-348e-4e6c-a225-11c058fd17b6" />

<br>
<br>
<br>
<p>8.11. <em>What was the UNC path that likely contained AWS credentials?</em><br>
<code>\\SRV-ITFS\Integrations\cloud-keys.csv</code></p>

<img width="1026" height="195" alt="image" src="https://github.com/user-attachments/assets/f30e0732-5ead-4b70-8d1f-662feba1acdd" />

<br>
<br>
<br>
<p>8.12. <em>From which IP address did the adversary access AWS?</em><br>
<code>152.42.128.207</code></p>

<img width="1283" height="664" alt="image" src="https://github.com/user-attachments/assets/529d51c5-35da-4253-840c-f848c3674d5c" />

<br>
<br>
<br>
<p>8.13. <em>Which two sensitive files did the adversary exfiltrate from AWS?</em> Hint: Specify via comma in the alphabetic order.<br>
<code>beta.tar.gz, latest.tar.gz</code></p>

index=* src_ip="152.42.128.207"  signature=GetObject | sort by +_time

<img width="1292" height="488" alt="image" src="https://github.com/user-attachments/assets/035f1480-d463-4b2f-8d4e-d3d9ea2039af" />

<br>
<br>
<br>
<p>8.14. <em>What file did the adversary upload to S3 in place of the wiped ones?</em><br>
<code>YOU-HAVE-BEEN-PWNED.txt</code></p>

<img width="1283" height="664" alt="image" src="https://github.com/user-attachments/assets/529d51c5-35da-4253-840c-f848c3674d5c" />

<br>
<br>

<img width="1289" height="438" alt="image" src="https://github.com/user-attachments/assets/201c2d65-63e6-4381-b829-f961b593e303" />

<br>
<br>



