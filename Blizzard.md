<p>July 7, 2025</p>
<h1>Blizzard</h1>

<h2>Task 1 . Introduction: Analysing the Impact</h2>
<p>Health Sphere Solutions, a healthcare systems provider on the path to expansion, is taking its first steps towards fortifying its infrastructure security. With the rise of cyber threats, particularly the emergence of Midnight Blizzard, a sophisticated threat group targeting the healthcare sector, the company recognizes the urgent need to protect sensitive customer data.</p>

<p>Midnight Blizzard, a notorious threat group, has been implicated in cyber-attacks against healthcare providers. Employing ransomware and phishing tactics, this group has successfully breached healthcare systems, causing significant data loss and operational interruptions.</p>

<h3>Prerequisites</h3>
<p>It is suggested to clear the following rooms first before proceeding with this room:<br>

- Windows Forensics 1<br>
- Expediting Registry Analysis<br>
- Windows Network Analysis<br>
- Windows User Activity Analysis<br>
- Windows User Account Forensics<br>
- Windows Applications Forensics</p>

<h3>Scenario</h3>
<p>A critical alert was detected on one of Health Sphere Solutions' database servers, highlighting the company's early challenges in securing its network. </p>

![image](https://github.com/user-attachments/assets/7ce0c360-5d17-4cf4-b3eb-a4c2a65e50c2)

<p>Since the security controls are still being established, alerts have only come from servers, and only network-level events are being audited, it's essential to manually investigate both servers and workstations to connect the dots and fully understand the incident.</p>

<h3>Connection Details</h3>

<p>Before we proceed with the investigation, start the attached virtual machine by clicking the Start Machine button at the top-right of this task. The machine will start in Split-Screen view. If the VM is not visible, use the blue Show Split View button at the top of the page. You can also use these credentials to access the machine via RDP.</p>

<br>

<p>In addition, your team has prepared the following items to assist your investigation:<br>

- Standalone tools in the C:\Tools directory.
- Tools prepared as desktop shortcuts.</p>

<h3>Investigation Guide</h3>
<p>As part of your playbook, you are tasked to determine the following information during the investigation:<br>

- Determine any unusual login attempts to the database server.<br>
- Note any suspicious binaries executed within the server.<br>
- Look for typical persistence mechanisms deployed in the server.</p>

<p>The IT team has also shared that the infected database server is set up for internal access only and is not yet linked to other systems, as it is still in the setup phase. This information could help narrow down potential sources of the threat.</p>

<p><em>Answer the questions below</p>em></p>

<p>1.1. <em>When did the attacker access this machine from another internal machine? (format: MM/DD/YYYY HH:MM:SS)</em><br>
<code>03/24/2024 19:38:48</code></p>

![image](https://github.com/user-attachments/assets/04537ed7-a4c7-4c7f-a2db-891f8526355e)

<h3>EvtxECmd</h3>

![image](https://github.com/user-attachments/assets/782b549d-1aa7-4fc7-9ef1-6479d51187a4)

<br>

<h3>Timeline Explorer</h3>

![image](https://github.com/user-attachments/assets/f38046e1-1fc2-4dd9-80a0-d91a41df8634)

![image](https://github.com/user-attachments/assets/5b7a7393-12e7-46b5-a5ee-ef3ed57491b7)

![image](https://github.com/user-attachments/assets/dadc7a69-ad5f-4959-ba65-827ee7d7e1d6)

<br>

<h3>Event Viewer</h3>

![image](https://github.com/user-attachments/assets/6e0af797-5e86-4fc1-8765-3066b60dfb53)

![image](https://github.com/user-attachments/assets/b17dc81a-72e0-4abf-8fd0-28236ef09d10)

![image](https://github.com/user-attachments/assets/a501f349-eb5a-4702-843d-994e863ef092)

![image](https://github.com/user-attachments/assets/467d0300-1847-4459-88cb-cce1d67b6c25)

<br>


<p>1.2. <em>What is the full file path of the binary used by the attacker to exfiltrate data?</em><br>
<code>C:\Users\dbadmin\.rclone\rclone-v1.66.0-windows-amd64\rclone.exe</code></p>

<h3>Windows Explorer</h3>

![image](https://github.com/user-attachments/assets/90d06c81-c741-4e7a-9b6d-c438e792cd03)

![image](https://github.com/user-attachments/assets/f219a75c-b422-460d-92a7-992feeaa6fe6)

![image](https://github.com/user-attachments/assets/a8346961-0bb5-49c4-8a60-4f9b5a41f1a8)

![image](https://github.com/user-attachments/assets/8e26f65e-49e4-4910-ab36-2af9bd0134c7)

<br>

<p>Practiced using another method.</p>

<h3>AppCompatCacheParser</h3>

![image](https://github.com/user-attachments/assets/37fc1256-cdae-4277-a120-789b77650ea9)

![image](https://github.com/user-attachments/assets/9a9e8abc-9474-4c74-bb66-1abe31f5e874)

![image](https://github.com/user-attachments/assets/02a2307c-4aa9-4bd8-8cc5-1e23bc0e8bd2)

<br>

<p>1.3. <em>What email is used by the attacker to exfiltrate sensitive data?</em><br>
<code>annajones291@hotmail.com</code></p>

<h3>Windows Explorer</h3>
<p><em>rclone.conf</em></p>

<p>with Windows PowerShell</p>

![image](https://github.com/user-attachments/assets/99b5c6bb-4afd-47e8-aa56-c706835d1aa0)

![image](https://github.com/user-attachments/assets/f0b8702c-1404-444e-8a0e-2f69162a2d70)

<p>with Windows Explorer</p>

![image](https://github.com/user-attachments/assets/5c133a91-d530-4836-ba40-9aacbaedecb0)

![image](https://github.com/user-attachments/assets/5c133a91-d530-4836-ba40-9aacbaedecb0)

<br>

<p>1.4. <em>Where did the attacker store a persistent implant in the registry? Provide the registry value name.</em><br>
<code>SecureUpdate</code></p>


<h3>Registry Editor</h3>

![image](https://github.com/user-attachments/assets/979ae801-5ccd-48bb-912f-27649f11fc0c)

![image](https://github.com/user-attachments/assets/8bc80e6a-d855-4989-80dd-840bb4f7e8db)

<br>

<p>1.5. <em>Aside from the registry implant, another persistent implant is stored within the machine. When did the attacker implant the alternative backdoor? (format: MM/DD/YYYY HH:MM:SS).</em><br>
<code>03/24/2024 20:04:05</code></p>

```bash
PS C:\Users\Administrator> Get-ScheduledTask | Where-Object {$_.Date —ne $null —and $_.State —ne "Disabled"} | Sort-Object Date | select Date,TaskName,Author,State,TaskPath | ft
```

![image](https://github.com/user-attachments/assets/f2480007-1618-4ddf-9520-c10832b9eecb)


<p><em>CDPUserSvc_9286x</em></p>

![image](https://github.com/user-attachments/assets/1d1c35b5-1e8b-451a-8461-7c2db658ab8a)

![image](https://github.com/user-attachments/assets/ba17980f-7ae6-48b1-84d0-fbdf3c8015c1)

![image](https://github.com/user-attachments/assets/296cf905-38d8-4323-8bb1-f1520f8b317f)

<p>code>2024-03-24 20:04:05</code> --> <code>03/24/2024 20:04:05</code></p>

<br>

<h2>Task 2 . Lateral Movemnt: Backtracking the Pivot Point</h2>






