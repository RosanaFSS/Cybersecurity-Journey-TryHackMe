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

<h4>Stage 1 of 3</h4>
<p>  

- Title: Initial Access<br>
- Adversary step descrirption: Initial Access was gained at Jul 21st 2025 10:58:27 by installing  "healthchk-lib@1.0.1" NPM package. Next "postintall.ps1" was downloaded and installed through PowerShell employing the following syntax to cover the related actions "-NoP -W Hidden -EncodedCommand".  "postinstall.ps1" execute automotically and was downloaded from global-update.windows.thm.<br>
- Timestamp: Jul 21st 2025 10:58:27<br>
- Tactic: Initial Acces<br>
- Technique: Supply Chain Compromise<br>
- User: tom@pawpress.me<br>
- Asset: paw-tom<br>
- List of IOCs:<br>
   --- Host = pwa-tom
   --- Current Directory = C:\Development\node_modules\healthchk-lib\<br>
   --- Process ID = 5880<br>
   --- Image = C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe<br>
   --- Parent Image = C:\Windows\System32\cmd.exe<br>
   --- Parent Process ID = 1616<br>
- SIEM URL Link: Redacted
</p>


<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ae24ab3d-a36b-4b24-b6de-33b71433c964"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/85017168-5759-4541-9d99-ce42cd57a03b"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/c03e7479-1977-4590-acba-965af0f48a2c"><br>
                  <img width="250px" src="https://github.com/user-attachments/assets/0639c45a-2532-48af-89c4-2776c1c8080b"></p>
                  


