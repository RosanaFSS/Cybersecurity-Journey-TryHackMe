<h1 align="center">Threat Hunting Simulator<br>Health Hazard</h1>
<p align="center">July 22, 2025<br><br>
<img width="80px" src="https://github.com/user-attachments/assets/5004481d-32ab-4e7a-93e4-a81298688e73"></p>


<br>

<h2>Briefing</h2>
<p>After months of juggling content calendars and caffeine-fueled brainstorming, co-founder Tom Whiskers finally carved out time to build the company’s first website. It was supposed to be simple: follow a tutorial, install a few packages, and bring the brand to life with lightweight JavaScript magic.<br>

But between sleepless nights and copy-pasted code, Tom started feeling off. Not sick exactly, just off. The terminal scrolled with reassuring green text, the site loaded fine, and everything looked normal.<br>

Then, a strange file appeared on the system. No one could say where it came from. It wasn’t part of the tutorial, didn’t match any known dependencies, and didn’t even run.<br>

It just waited.</p>

<h3>Hypothesis</h3>
<p>An attacker may have leveraged a compromised third-party software package to gain initial access to the system and silently stage a payload for later execution. They likely established persistence to maintain access without immediate detection.</p>

<h2>Objectives</h2>

<p>

- Determine how a threat actor first gained a foothold on the system. Identify suspicious activity that may point to the initial compromise method.<br>
- Investigate signs of malicious execution following the initial access. Analyse the logs and system behaviour to uncover the attacker's actions.<br>
- Identify any mechanisms the attacker used to maintain access across system restarts or user sessions. Look for indicators of persistence that could allow long-term control.
  
</p>

<h2>Practice</h2>





<p>

- <code>Review threat intel and hypothesis</code>: The Threat Intel hub contains IOCs, attack timelines, analyst notes, and a working hypothesis to assess. Study the intel closely to understand the full context and spot any gaps. Your task is to prove or disprove the hypothesis through investigation.<br>
- <code>Investigate and reconstruct the attack chain</code>: Use the SIEM and virtual machine to trace the attack. Correlate logs, analyze forensic data, and map each step the adversary took. Build your attack chain to understand how and why it happened.<br>
- <code>Review report and conclude</code>: Submit your attack chain and review the AI-generated report, which details the timeline from initial foothold to full compromise. Then, state whether you accept or refute the hypothesis. Hit Submit to finish.
</p>
