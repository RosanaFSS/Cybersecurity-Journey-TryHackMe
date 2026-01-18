<h1 align="center">SOC Simulator &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;&nbsp; <a href="https://tryhackme.com/soc-sim/scenarios?scenario=apt28-link-to-trouble-initial-access"> APT28: Initial Access</a></h1>
<p align="center"><img width="590px" src="https://github.com/user-attachments/assets/02f7e84c-766d-4ec6-935f-cfc5e59063e4"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2018-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Overview](#1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Objectives](#2) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Methodology](#3) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Resources](#4)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Practice 1](#5) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Practice 2](#6)


<br>
<br>
<h2>Overview<a id='1'></a></h2>
<p>Here at <code>TryGovMe</code>, our partners have been consistently targeted by <code>APT28</code> over the past few weeks and we are now preparing for a potential intrusion ourselves. To all SOC analysts on shift - please remain focused and prepared for a possible attack!<br>
Chapter of the APT28: Link to Trouble scenario.</p>

<br>
<br>
<h2>Objectives<a id='2'></a></h2>
<p>

- Identify and triage security alerts indicating malicious behaviour consistent with <code>APT28</code> activity.<br>
- Analyse <code>initial access techniques</code> used by <code>APT28</code> in enterprise environments.<br>
- Analyse and correlate various log types to identify anomalies and gain insight into adversary activity.</p>

<br>
<br>
<h2>Methodology<a id='3'></a></h2>
<p>
  
- Step 1<br><strong>Find all the true positives</strong><br>To complete a Scenario, find all the True Positive alerts. Keep triaging alerts until you've closed them all!<br><br>
- Step 2<br><strong>Read the documentation</strong><br>Before diving into the triage, take a moment to review the provided documentation. This will give you essential context and strategies for investigation.<br><br>
- Step 3<br><strong>Investigate the alert queu</strong><br>Your journey starts in the alert queue. Investigate each alert, and prioritise what seems most critical. Understanding the types of alerts can help you manage your time effectively.<br><br>
- Step 4<br><strong>Take ownership of an alert</strong><br>Click on an alert to take ownership. This action starts the timer for MTTR, so act fast! Use this to strategise how you spend time on each alert.<br><br>
- Step 5<br><strong>Deep dive with the SIEM & VM</strong><br>Use the SIEM to search logs and investigate indicators. The VM is there for deeper analysis. Combine these tools to verify what’s real and what’s a false alarm.<br><br>
- Step 6<br><strong>Write your findings as a report</strong><br>For each alert, determine whether it's a true positive or a false positive. Clearly document your findings, analysis, and actions taken. Submit the report when you're confident in your conclusions—accurate and well-written reports will earn you more points!<br><br>
- Step 7<br><strong>Analyse your performance</strong><br>After completing the scenario, dive into your wrap-up report to see how you performed. You’ll receive detailed feedback on your MTTR, points scored, the number of closed alerts, and personalised AI insights to enhance your future reporting.</p>

<br>
<br>
<h2>Resources<a id='4'></a></h2>
<p></p>

- MITRE ATT&CK - Groups &nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; <a href="https://attack.mitre.org/groups/G0007/">APT28</a><br>
- APT28 in the Snare &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; <a href="https://medium.com/@RosanaFS/apt28-in-the-snare-tryhackme-walkthrough-blue-team-advanced-persistent-threats-apts-ca5b1eafcb29">TryHackMe Walkthrough</a><br>
- APT28 Inception Theory &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; <a href="https://medium.com/@RosanaFS/apt28-inception-theory-681b3db08072">TryHackMe Walkthrough</a></p>

<br>
<br>
<h2>Practice 1<a id='5'></a></h2>

<h3>Suspicious Archive File Download Detected</h3>
<p>
  
- Severity:  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>Medium</code><br>
- Type:  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>Download</code><br>
- <strong>Time of activity</strong>:  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>2024-12-07 15:22:30.966</code><br>
- <strong>List of Affected Entities</strong>:<br>User: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>DEV-QA-SERVER\Tom Barry</code><br>ComputerName: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>Dev-QA-Server</code><br>ProcessId: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>4980</code><br>
- <strong>Reason for Classifying as True Positive</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Confirmed malicious file download.<br>User <code>DEV-QA-SERVER\Tom Barry</code> used Google Chrome (<strong>chrome.exe</strong>) on  <code>2024-12-07 15:22:30.966</code><br> to download a <strong>.rar</strong> file in the path C:\Users\Tom Barry\Downloads\Service_Configuration_Guide.rar that might be a potential risk. There is the presence of <strong>:Zone.Identifier</strong> confirms that the file originated from the internet.  The use of a compressed archive file <strong>.rar</strong> for a <strong>Configuration Guide</strong> is susupicious as legitimate documention is typically distributed as <strong>.pdf</strong> or <strong>.docx</strong>.<br>
- <strong>Reason for Escalating the Alert</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; User <code>DEV-QA-SERVER\Tom Barry</code> donwloaded a <strong>.rar</strong> suspicious Configuration Guide which might contain malicious content.<br>
- <strong>Recommended Remediation Actions</strong>.pdf</strong>: &nbsp;&nbsp;&nbsp;&nbsp; Isolate, Kill, Delete the malicious file.<br>
- <strong>List of Attack Indicators</strong>:<br>RuleName: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>files_downloads</code><br>Image: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>C:\Program Files\Google\Chrome\Application\chrome.exe</code><br>TargetFilename: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>C:\Users\Tom Barry\Downloads\Service_Configuration_Guide.rar:Zone.Identifier</code><br></p>

<p>Feedback:<br>
  
- Incident classification: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>True Positive</code> &nbsp;&nbsp;&nbsp;&nbsp; 10/10<br>
- Require Escalation? &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>Yes</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10/10<br>
- Missing Details: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 45/65<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 65/95 points</p>



<br>
<br>
<h2>Practice 2<a id='6'></a></h2
