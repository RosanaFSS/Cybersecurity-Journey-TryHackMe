<h1 align="center">Alert Triage With Splunk</h1>
<p align="center">2025, October 22  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>5343</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Use Splunk to triage alerts and investigate malicious activity efficiently. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/alerttriagewithsplunk">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/b3a5e536-0b6c-42fe-9e26-160733a6ee94"></p>


<h1>Task 1 . Introduction</h1>
<p>As a SOC analyst, it’s important to be able to investigate different types of suspicious activity across a variety of assets in the environment. Knowing what to look for and which details matter most during an investigation is a key part of the role.</p>

<h3>Learning Objectives</h3>
<p>

- Learn how to properly investigate alerts in a SOC environment.<br>
- Understand how to investigate brute-force attacks on Linux systems.<br>
- Discover the persistence mechanism on Windows systems.<br>
- Analyse a web shell on a vulnerable web server.<br>
- Learn how to investigate alerts for three given scenarios using Splunk.</p>

<h3>Room Prerequisites</h3>
<p>It is suggested to complete the following rooms first before proceeding:

- <a href="https://tryhackme.com/room/introtosiem">Introduction to SIEM</a><br>
- <a href="https://www.linkedin.com/in/rosanafssantos/">Splunk: Basics</a><br>
- <a href="https://tryhackme.com/room/windowsloggingforsoc">Windows Logging Capabilities</a><br>
- <a href="https://tryhackme.com/room/loganalysiswithsiem">Log Analysis with SIEM</a><br>
- <a href="https://tryhackme.com/r/room/sysmon"> Sysmon</a></p>

<h3>Lab Access</h3>
<p>Before proceeding, start the lab by clicking the Start Machine button below. You will then have access to the Splunk Web Interface. 
To access Splunk, please follow this link: <code>https://xx-xx-xxx-xxx.reverse-proxy-eu-west-1.tryhackme.com</code>. Please wait 4-5 minutes for the Splunk instance to launch. Use Splunk’s All Time range to search. The indexes where logs are stored for each practical exercise are present in each task.</p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s go!<br>
<code>No answer needed</code></p>

<h1>Task 2 . Initial Access Alert </h1>
<p>We will explore three different scenarios that you, as an analyst, may encounter during your shift. The first one will take place on a Linux host, and you will uncover what exactly happens there during our investigation.</p>

<h3>Alert Scenario</h3>
<p>You’ve just started your first shift as a SOC analyst at an MSSP. Only a few minutes have passed since an alert about a possible brute force attack appeared on the platform.<br>
<strong>Alert Details</strong>:<br>
  
- <strong>Alert Name</strong>: Brute Force Activity Detection<br>
- <strong>Time</strong>: 17/09/2025 9:00:21 AM<br>
- <strong>Target Host</strong>: tryhackme-2404<br>
- <strong>Source IP</strong>: 10.10.242.248<br>

Your job is to investigate this activity and decide whether it should be considered suspicious.</p>

<p>The logs for this task are located in the Splunk index win-alert. Use the following query: <code>index=linux-alert</code></p>

<h3>Investigating the Alert</h3>
<p>Let’s begin our investigation. First, we will focus on the alert data, in particular, two fields that may be of interest: Target Host Time and Source IP. Starting with the IP, as we can see, this is a local IP address. This suggests that, if it is indeed an attacker, they are already inside the organisation’s network, possibly having successfully compromised the VPN or gained access through some other way. As for the host name, we don’t have much information.<br>

We lack an asset inventory table, and based on the hostname alone, it’s hard to determine what system this is. Most likely, it’s some type of organisational server. The activity time appears normal, it’s 9 a.m., during regular working hours.<br>
Therefore, let’s move into the SIEM and check whether brute force activity occurred here or if it's a false positive alert. Let's use this search in Splunk.<br>

This query will search for both successful and failed login attempts, as well as events related to invalid users, which are commonly observed when an attacker is attempting to enumerate accounts before starting brute force attacks on a specific user.

```bash
index="linux-alert" sourcetype="linux_secure" 10.10.242.248 
| search "Accepted password for" OR "Failed password for" OR "Invalid user"
| sort + _time
```

<p>The first thing we notice is a rather large number of events associated with this IP. Secondly, what’s interesting is that there are several login attempts for non-existent users, which is suspicious, wouldn’t you agree?</p>

<h6 align="center"><img height="900px" hspace="3" src="https://github.com/user-attachments/assets/35725358-ab87-4e56-93fa-4c7e2e32c2cd"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>So far, we haven’t found any signs of brute force. Therefore, let’s run another search to see the number of login attempts made for each user.</p>

```bash
index="linux-alert" sourcetype="linux_secure" 10.10.242.248
| rex field=_raw "^\d{4}-\d{2}-\d{2}T[^\s]+\s+(?<log_hostname>\S+)"
| rex field=_raw "sshd\[\d+\]:\s*(?<action>Failed|Accepted)\s+\S+\s+for(?: invalid user)? (?<username>\S+) from (?<src_ip>\d{1,3}(?:\.\d{1,3}){3})"
| eval process="sshd"
| stats count values(src_ip) as src_ip values(log_hostname) as hostname values(process) as process by username
| sort + _time
```

<p>Now the results are more interesting. As we can see from the search output, the login attempts from this IP targeted four different users, but only <strong>john.smith</strong> shows a significantly high number of <strong>503</strong> attempts, which is a clear indicator of brute force activity.</p>

<h6 align="center"><img height="170px" hspace="3" src="https://github.com/user-attachments/assets/7eb6339a-750d-4b92-9de7-dfb00e481225">
                  <img height="170px" src="https://github.com/user-attachments/assets/093ec566-3880-4612-a706-eed231bba57f"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>We know that the brute force attempts targeted john.smith, but at this point, we don’t yet know whether the attack was successful. Therefore, let’s use the following search to determine whether the attacker actually gained access to the system.</p>

```bash
index="linux-alert" sourcetype="linux_secure" 10.10.242.248
| rex field=_raw "^\d{4}-\d{2}-\d{2}T[^\s]+\s+(?<log_hostname>\S+)"
| rex field=_raw "sshd\[\d+\]:\s*(?<action>Failed|Accepted)\s+\S+\s+for(?: invalid user)? (?<username>\S+) from (?<src_ip>\d{1,3}(?:\.\d{1,3}){3})"
| eval process="sshd"
| stats count values(action) values(src_ip) as src_ip values(log_hostname) as hostname values(process) as process  by username
```

<p>As a result, we detect a successful login only for the <strong>john.smith</strong> account, which gives us sufficient grounds to confirm that the brute force attack was successful and that the threat actor gained access to the host <strong>tryhackme-2404</strong>. We have clear indicators to classify this activity as a <strong>True Positive</strong>. In addition, we must immediately escalate this to the SOC L2 analyst for further investigation, with the possible involvement of the Incident Response team.</p>

<h6 align="center"><img height="170px" hspace="3" src="https://github.com/user-attachments/assets/63e730b1-6469-480e-825e-2cbce299fb3f">
                  <img height="170px" src="https://github.com/user-attachments/assets/dce63746-ee37-47c8-bdd5-6d76e55a3383"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Next Investigation Steps</h3>
<p>At this point, your investigation of this activity as a SOC Level 1 analyst comes to an end, since your responsibility is to identify malicious activity and escalate it to the Level 2 analyst. Therefore, let’s now discuss what will happen next and what questions still remain for the SOC team regarding this case.<br>

- Why did the attacker have a local IP address? Could it be that they are already inside our network? If so, for how long?<br>
- How did the attacker obtain information about the users, specifically their usernames?<br>
- What happened after the attacker gained access to the tryhackme-2404 host?<br>

Following this, the Incident Response team should carry out a series of containment and remediation steps.<br>
Not an easy shift you’ve got, huh!</p>

<p><em>Answer the questions below</em></p>

<p>2.1.  How many failed login attempts were made on the user john.smith?<br>
<code>500</code></p>

<br>
<p>2.2.  What was the duration of the brute force attack in minutes?<br>
<code>9</code></p>

<br>
<p>2.3. What username was the attacker able to privilege escalate to?<br>
<code>root</code></p>

<h6 align="center"><img height="1200px" src="https://github.com/user-attachments/assets/adebf5b4-2efc-47e2-97e7-6390a7646724"></h6>

<br>
<p>2.4. What is the name of the user account created by the attacker for persistence?<br>
<code>system-utm</code></p>

<h6 align="center"><img height="1200px" src="https://github.com/user-attachments/assets/b7163897-d5d0-4c4a-b812-c9e13050b374"></h6>
  
<h1>Task 3. Persistence Alert</h1>
<p>The second scenario will focus on activity in a Windows environment, which SOC analysts come across on a regular basis. That’s why knowing how to carry out the analysis is really important for you.</p>

<h3>Alert Scenario</h3>
<p>You are working as a Level 1 SOC Analyst on shift at an MSSP. An alert has come through indicating that a suspicious scheduled task was created on a host.<br>
<strong>Alert Details</strong>:<br>
  
- <strong>Alert Name</strong>: Potential Task Scheduler Persistence Identified<br>
- <strong>Time</strong>:30/08/2025 10:06:07 AM<br>
- <strong>Target Host</strong>: WIN-H015<br>
- <strong>Source IP</strong>: oliver.thompson<br>
-  <strong>Task Name</strong>: AssessmentTaskOne<br>

The logs for this task are located in the Splunk index win-alert. Use the following query: <code>index=win-alert</code></p>

<h3>Investigating the Alert</h3>
<p>Let’s look at how to approach this analysis. First, pause - don’t jump straight into the SIEM. Begin with the alert details.<br>

Focus on <strong>Host</strong> and <strong>User</strong>. Work out what kind of host it is: workstation or server. This context is key before continuing. Many organisations have an Asset Inventory (sometimes in Confluence or Notion) for this, but if not, naming conventions can help.<br>

Servers often use prefixes like <strong>SRV</strong>, <strong>WEB</strong>,  <strong>MYSQL</strong>, while workstations are labelled  <strong>WIN</strong> or  <strong>HOST</strong>. In our case,  <strong>WIN-H015</strong> suggests it’s a workstation.<br>

Next, check the  <strong>User</strong>. Use the identity table to see their role. This helps decide if the activity fits their job. For example, it’s odd if HR is creating tasks, but normal for IT staff. You can also check the user’s location and working hours to see if the timing makes sense. In our case,  <strong>Oliver Thompson</strong> is a System Engineer.<br>
Once we’ve gathered this information, we will have an initial picture of where the activity took place and who carried it out. Now, let’s move into the SIEM for a deeper analysis.<br>

To start, we’ll query the task name <code>AssessmentTaskOne</code> along with event ID <code>4698</code>, which indicates that a scheduled task was created. Since we also know the exact time of the activity, we can filter by timestamp to speed up the search. Note: For now, we won’t filter by host. This way, we can check whether the activity is isolated to a single machine or present across multiple hosts.</p>

```bash
index="win-alert" EventCode=4698 AssessmentTaskOne
| table _time EventCode user_name host Task_Name Message
```

<p>From our search, we can see that there’s only a single event related to this activity. </p>

<h6 align="center"><img height="900px" src="https://github.com/user-attachments/assets/3dc850e2-3bba-41f6-9603-a444de65f1ea"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Now, let’s look at the <strong>Message</strong> field to understand what this task actually does. Let’s go step by step, starting with the <strong>Triggers</strong> section.</p>

<h6 align="center"><img height="600px" src="https://github.com/user-attachments/assets/2a39dd87-104a-4809-b856-9388e699af83"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>We can see that the task runs every day at the same time on a user workstation, which is quite unusual. Let’s continue by analysing the <strong>Message</strong> field, focusing on the <strong>Exec</strong> and <strong>Principals</strong> sections, to see what task is being executed and under which user account.</p>

<h6 align="center"><img height="900px" src="https://github.com/user-attachments/assets/9f137feb-75d1-4857-96ae-057d7cbf33b5"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>At this point, we can already see the first signs of malicious activity. This task will use <code>certutil</code> to download <code>rv.exe</code> from the tryhotme domain into the Temp folder under the name <code>DataCollector.exe</code>. It will then launch this file using a <code>Start-Process</code> PowerShell command. All of this activity will be executed under the user <strong>oliver.thompson</strong>. This is a clear example of persistence.<br>
What else can you find out? Try looking up the domain in Threat Intelligence platforms, it might be linked to a known attacker infrastructure. We classified this activity as a <strong>True Positive</strong>. Also, this activity should be escalated to an L2 analyst for deeper investigation.</p>

<p><em>Answer the questions below</em></p>

<p>3.1. What is the ProcessId of the process that created this malicious task?<br>
<code>5816</code></p>

<img width="1258" height="157" alt="image" src="https://github.com/user-attachments/assets/2ff1efd6-30fa-4300-acd0-e28acb7b94ff" />

<br>

<img width="1244" height="331" alt="image" src="https://github.com/user-attachments/assets/0e5679bc-a35f-495e-a720-38d1bba0f129" />

<br>
<p>3.2. What is the name of the parent process for the process that created this malicious task?<br>
<code>cmd.exe</code></p>

<br>
<p>3.3. Which local group did the attacker enumerate during discovery?<br>
<code>Administrators</code></p>

<img width="1257" height="69" alt="image" src="https://github.com/user-attachments/assets/aaa46d72-118f-4ad3-a3c3-4ba6d7e5f287" />

<br>
<p>3.4. What is the name of the workstation from which the Threat Actor logged into this host?<br>
<code>Dev-QA-Server</code></p>

<img width="474" height="214" alt="image" src="https://github.com/user-attachments/assets/ac7a5d02-dc89-426e-a2db-493d3616baa2" />

<br>
<h1>Task 4 . Possible Web Shell Alert</h1>
<p>The last scenario will focus on activity in a vulnerable web server. We’ll be investigating possible web shell exploitation.</p>
<h3>Alert Scenario</h3>
<p>Your shift as an L1 SOC analyst continues, and you’ve now received the next alert that needs to be investigated. This time, the activity is related to the web.<br>
<strong>Alert Details</strong>:<br>

- <strong>Alert Name</strong>: Potential Web Shell Upload Detected<br>
- <strong>Time</strong>: 14/09/2025 09:31:51 AM<br>
- <strong>Resource</strong>: http://web.trywinme.thm<br>
- <strong>Suspicious IP</strong>: 171.251.232.40<br>

Your job is to investigate this activity and decide whether it should be considered suspicious.<br>
The logs for this task are located in the Splunk index win-web. Use the following query: <code>index=web-alert</code></p>

<h3>Investigating the Alert</h3>
<p>As with the previous cases, we begin by examining the details contained in the alert. The first thing of interest is the resource where the activity occurred, in this case, <code>http://web.trywinme.thm</code>, which is the organisation’s website hosted on the web server. The next point of interest here is the Suspicious IP address. We can check it across various Threat Intelligence platforms to gather more information. Let’s use AbuseIPDB for this. As we can see, this IP address has been flagged as malicious more than 3000 times. Let’s make a note of this.</p>
<p>...</p>

<h3>Next Investigation Steps</h3>
<p>These questions should be reviewed by the SOC Level 2 analyst:<br>

-Was the brute force attack using Hydra successful?<br>
-How did the attacker upload the web shell to the server, given that SOC L1 did not identify any traces of the upload?<br>
-What specific actions did the attacker perform on the server using commands through the web shell?<br>

After this, containment and remediation actions should take place.<br>

That was quite an intense shift. I hope you’ve learned how to properly conduct an investigation and what you can identify in the logs.</p>

<p><em>Answer the questions below</em></p>

<p>4.1. What time did the brute-force activity using Hydra begin?<br>
<code>2025-09-14 21:20:27</code></p>

```bash
index=web-alert 171.251.232.40
| table _time clientip useragent uri_path method status 
| sort + _time
```

<img width="1310" height="524" alt="image" src="https://github.com/user-attachments/assets/2bea026b-b1b4-47d9-8156-f1c397c7bd5a" />

<br>
<br>
<p>4.2. Which user agent did the attacker use when interacting with the web shell?<br>
<code>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36</code></p>

```bash
index=web-alert 171.251.232.40 useragent!="Mozilla/5.0 (Hydra)"  method="POST"
| table  _time method status clientip useragent uri_path referer referer_domain
| sort +_time
```

<img width="1326" height="658" alt="image" src="https://github.com/user-attachments/assets/f40821b4-7c37-4f25-b704-a0e49ad12760" />

<br>
<br>
<p>4.3. What was the number of requests made by the attacker to the server via the web shell?<br>
<code>4</code></p>

```bash
index=web-alert 171.251.232.40 b374k.php
| table  _time method status clientip useragent uri_path referer referer_domain
| sort +_time
```

<img width="1329" height="689" alt="image" src="https://github.com/user-attachments/assets/8d495a04-26f9-4c7e-bf25-5b46f1766bcf" />

<br>
<h1>Task 5 . Conclusion</h1>
<p>Great job completing this room! You've now gained practical experience in investigating different types of alerts you can encounter in the real world.<br>

- Detecting anomalies on Windows and Linux systems.<br>
- Analysing web shell activity and identifying its traces.<br>

More exciting challenges await you next!</p>

<p><em>Answer the question below</em></p>

<p>5.1. Well Done!<br>
<code>No answer needed</code></p>

<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d13c6469-c3ab-4a14-ba13-7f2edfe115a9"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/61c60f46-9127-499e-8837-4be5994934c2"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|22      |Medium 🔗 - Alert Tryage With Splunk   | 534    |      87ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,865  |  1,013    |    79     |
|21      |Easy 🔗 - Cyber Scotland 2021          | 533    |      87ᵗʰ    |      4ᵗʰ     |      87ᵗʰ    |     2ⁿᵈ    | 131,777  |  1,012    |    79     |
|21      |Medium 🔗 - Windows PrivEsc            | 533    |      87ᵗʰ    |      4ᵗʰ     |      88ᵗʰ    |     2ⁿᵈ    | 131,737  |  1,011    |    79     |
|20      |Hard 🚩 - Enterprise                   | 532    |      87ᵗʰ    |      4ᵗʰ     |      81ˢᵗ    |     2ⁿᵈ    | 131,729  |  1,010    |    79     |
|19      |Hard 🚩 - Misguided Ghosts             | 531    |      87ᵗʰ    |      4ᵗʰ     |      77ᵗʰ    |     2ⁿᵈ    | 131,661  |  1,009    |    79     |
|18      |Hard 🚩 - Year of the Pig              | 530    |      89ᵗʰ    |      4ᵗʰ     |      72ⁿᵈ    |     2ⁿᵈ    | 131,531  |  1,008    |    79     |
|18      |Easy 🚩 - The Phishing Pond            | 530    |      90ᵗʰ    |      4ᵗʰ     |      74ᵗʰ    |     2ⁿᵈ    | 131,501  |  1,007    |    79     |
|17      |Hard 🚩 - Initial Access Pot           | 529    |      90ᵗʰ    |      4ᵗʰ     |      68ᵗʰ    |     2ⁿᵈ    | 131,456  |  1,006    |    79     |
|17      |Medium 🔗 - AllSignsPoint2Pwnage       | 529    |      90ᵗʰ    |      4ᵗʰ     |      87ᵗʰ    |     2ⁿᵈ    | 131,186  |  1,005    |    79     |
|16      |Easy 🔗 - Network Traffic Basics       | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,138  |  1,004    |    79     |
|16      |Medium 🔗 - Linux Threat Detection 3   | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,066  |  1,003    |    79     |
|13      |Hard 🚩 - M4tr1x: Exit Denied          | 525    |      92ⁿᵈ    |      4ᵗʰ     |      76ᵗʰ    |     2ⁿᵈ    | 130,938  |  1,002    |    79     |
|12      |Easy 🔗 - Atlas                        | 524    |     101ˢᵗ    |      4ᵗʰ     |     251ˢᵗ    |     3ʳᵈ    | 129,902  |  1,001    |    76     |
|11      |Easy 🔗 - Brute Force Heroes           | 523    |     101ˢᵗ    |      4ᵗʰ     |     217ᵗʰ    |     3ʳᵈ    | 129,878  |  1,000    |    76     |
|11      |Hard 🚩 - Rocket                       | 523    |     102ⁿᵈ    |      4ᵗʰ     |     211ˢᵗ    |     3ʳᵈ    | 129,870  |    999    |    76     |
|10      |Easy 🚩 - Shadow Trace                 | 522    |     101ˢᵗ    |      4ᵗʰ     |     159ᵗʰ    |     3ʳᵈ    | 129,810  |    998    |    76     |
|10      |Easy 🔗 - Defensive Security Intro     | 522    |     103ʳᵈ    |      4ᵗʰ     |     357ᵗʰ    |     3ʳᵈ    | 129,405  |    997    |    76     |
|10      |Easy 🔗 - 25 Days of Cyber Security, Day 2| 522|      103ʳᵈ    |      4ᵗʰ     |     355ᵗʰ    |     3ʳᵈ    | 129,405  |    996    |    76     |
|9       |Medium 🔗 - Linux Threat Detection 2   | 521    |     103ʳᵈ    |      4ᵗʰ     |     326ᵗʰ    |     3ʳᵈ    | 129,373  |    996    |    76     |
|9       |Medium 🚩 - WWBuddy                    | 521    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,293  |    995    |    76     |
|8       |Hard 🚩 - Motunui                      | 520    |     103ʳᵈ    |      4ᵗʰ     |     383ʳᵈ    |     4ᵗʰ    | 129,201  |    994    |    76     |
|8       |Easy 🔗 - Man-in-the-Middle            | 520    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,141  |    993    |    76     |
|7       |Medium 🚩 - Profiles, in progress      | 519    |              |              |              |            | 129,021  |    992    |    76     |
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129,021  |    992    |    76     |
|6       |Easy 🚩 - DearQA                       | 518    |     105ᵗʰ    |      4ᵗʰ     |     333ʳᵈ    |     6ᵗʰ    | 128,991  |    991    |    76     |
|5       |Medium 🚩 - Frank & Herby try again.....| 517   |     106ᵗʰ    |      4ᵗʰ     |     300ᵗʰ    |     5ᵗʰ    | 128,931  |    990    |    76     |
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     233ʳᵈ    |     3ʳᵈ    | 128,871  |    989    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>

<br>

<p align="center">Global All Time:   87ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/788e064a-8fc4-4eb8-9bb3-a6259e17ccc5"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/d6637750-e782-44f7-843f-f9ac6305a76d"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/e593e65a-bdf5-41f8-a8e3-08963f3beebe"><br>
                  Global monthly:     89ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/a3a46a99-3116-407e-ad8e-71d9dd9b2b79"><br>
                  Brazil monthly:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/9da6002c-9ea7-4614-bdb9-70aab41c460a"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
