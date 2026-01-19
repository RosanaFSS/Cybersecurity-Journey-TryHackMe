<h1 align="center">SOC Simulator &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;&nbsp; <a href="https://github.com/user-attachments/assets/ec1c1bc3-8096-4bae-8db5-7ab9201a1b6f"> Upload and Conquer</a></h1>
<p align="center"><img width="590px" src="https://github.com/user-attachments/assets/881f1504-cecd-4098-afee-d005341cdd9b"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2019-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Overview](#1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Objectives](#2) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Methodology](#3) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Practice ](#4)

<br>
<h2>Overview<a id='1'></a></h2>
<p>An old, forgotten upload page on an e-commerce website becomes every hacker's dream when it pops up during a routine recon scan. Exploiting this weak spot, the attacker uploads a simple web shell and begins their journey through the server, hunting for privilege escalation opportunities with one goal in mind: exfiltration.<br>

Can you follow the attack chain and uncover the overlooked misconfigurations that made this breach possible?</p>
<br>
<br>
<h2>Objectives<a id='2'></a></h2>
<p>

- Recognise and analyse malicious activity in web logs.<br>
- Practice analysing logs to trace file upload attempts and command execution.<br>
- Uncover how attackers leverage system misconfigurations to escalate privileges and execute malicious scripts.</p>

<br>
<br>
<h2>Methodology<a id='3'></a></h2>
<p>
  
- Step 1 · <strong>Find all the true positives</strong><br>To complete a Scenario, find all the True Positive alerts. Keep triaging alerts until you've closed them all!<br><br>
- Step 2 · <strong>Read the documentation</strong><br>Before diving into the triage, take a moment to review the provided documentation. This will give you essential context and strategies for investigation.<br><br>
- Step 3 · <strong>Investigate the alert queu</strong><br>Your journey starts in the alert queue. Investigate each alert, and prioritise what seems most critical. Understanding the types of alerts can help you manage your time effectively.<br><br>
- Step 4 · <strong>Take ownership of an alert</strong><br>Click on an alert to take ownership. This action starts the timer for MTTR, so act fast! Use this to strategise how you spend time on each alert.<br><br>
- Step 5 · <strong>Deep dive with the SIEM & VM</strong><br>Use the SIEM to search logs and investigate indicators. The VM is there for deeper analysis. Combine these tools to verify what’s real and what’s a false alarm.<br><br>
- Step 6 · <strong>Write your findings as a report</strong><br>For each alert, determine whether it's a true positive or a false positive. Clearly document your findings, analysis, and actions taken. Submit the report when you're confident in your conclusions—accurate and well-written reports will earn you more points!<br><br>
- Step 7 · <strong>Analyse your performance</strong><br>After completing the scenario, dive into your wrap-up report to see how you performed. You’ll receive detailed feedback on your MTTR, points scored, the number of closed alerts, and personalised AI insights to enhance your future reporting.</p>

<br>
<h2>Practice<a id='4'></a></h2>
<h3>Alerts</h3>

<div align="left"><h6>

|ID<br><br><br>|Severity<br><br><br>|Alert rule<br><br><br>                    |Type<br><br><br>        |Classification<br><br><br>       |Score<br><br><code>660</code>|Value<br><br><code>740</code>|
|:----|:--------|:------------------------------------|:---------------|:----------------------------|----:|----:|
|1042 |Low      |Possible SQL Injection Attempt       |Web Attack      |False Positive               |5    |    5|
|1043 |Low      |Possible SQL Injection Attempt       |Web Attack      |True Positive                |55   |   55|
|1044 |Low      |Possible SQL Injection Attempt       |Web Attack      |True Positive                |55   |   55|
|1045 |Low      |Possible SQL Injection Attempt       |Web Attack      |True Postivie                |55   |   55|
|1046 |Low      |Possible SQL Injection Attempt       |Web Attack      |True Positive                |55   |   55|
|1047 |Medium   |Path Traversal Attempt               |Web Attack      |True Positive                |95   |  160|
|1048 |Low      |Possible SQL Injection Attempt       |Web Attack      |False Positive               |5    |    5|
|1049 |High     |Remote Command Execution             |RCE             |True Positive                |115  |  125|
|1050 |Low      |Possible SQL Injection Attempt       |Web Attack      |True Positive                |55   |   55|
|1051 |Low      |Possible SQL Injection Attempt       |Web Attack      |True Positive                |55   |   55|
|1052 |Low      |Possible SQL Injection Attempt       |Web Attack      |True Positive                |55   |   55|
|1053 |Low      |Possible SQL Injection Attempt       |Web Attack      |True Positive                |55   |   55|
|1054 |Low      |Possible SQL Injection Attempt       |Web Attack      |False Positive               |5    |    5|

</h6></div>

<h3>1044 · Possible SQL Injection Attempt · Low · Web Attack</h3>

> ALERT
>> **Description**: An attempt at SQL code injection has been detected in the web request. Investigate further to determine if it was successful.<br>
>> **datasource**: web_log<br>
>> **host**: store.tryhatme.thm<br>
>> **client_ip**: 109.70.100.1<br>
>> **ident**: -<br>
>> **user**: -<br>
>> **timestamp**: 01/19/2026 16:52:00.853<br>
>> **method**: GET<br>
>> **uri**: /products/view.php?id=1%20UNION%20SELECT%20username%2Cpassword%20FROM%20users--<br>
>> **protocol**: HTTP/1.1<br>
>> **status**: 200<br>
>> **bytes**: 34614<br>
>> **referer**: -<br>
>> **user_agent**: sqlmap/1.7-dev-59e8f7c (https://sqlmap.org)<br>
>
> REPORT
>> **Time of activity**: 01/19/2026 16:52:00.853<br><br>
>> **List of Affected Entities**:  host: store.tryhatme.thm<br><br>
>> **Reason for Classifying as True Positive**:<br>
>> ⦿  Clear Attack Syntax: The URI contains a classic Union-Based SQL Injection payload: UNION SELECT username,password FROM users--.<br>
>> ⦿  Automated Tooling: The User-Agent is explicitly sqlmap/1.7-dev-59e8f7c, confirming the use of an automated penetration testing tool.<br>
>> ⦿ Attack Volume: The logs show high-frequency requests from IP 109.70.100.1 testing various payloads (e.g., AND 1=1, extractvalue) within a short timeframe.<br><br>
>> **Reason for Escalating the Alert**:<br>
>> ⦿ Successful Data Exfiltration: The specific alerted request (querying for username,password) returned a 200 OK status and a response size of 34,614 bytes.<br>
>> ⦿ Comparison: A normal valid request for id=1 (seen at 17:12:39) returned only 22,591 bytes.<br>
>> ⦿ Conclusion: The additional ~12KB of data strongly suggests the server successfully returned the contents of the users table (credentials).<br>
>> ⦿ Destructive Intent: A later log entry at 17:15:27.853 shows the attacker attempting to execute DROP TABLE users. This indicates an intent to destroy the database after stealing the information.<br><br>
>> **Recommended Remediation Actions**:<br>⦿ Block the Attacker: Immediately block IP 109.70.100.1 at the perimeter firewall/WAF.<br>⦿ Password Reset: Force a global password reset for all users immediately, as the logs indicate the users table (containing credentials) was dumped. ⦿ Database Restoration: Check the database integrity to ensure the DROP TABLE command (attempted at 17:15) did not succeed. Restore from backup if necessary.<br>⦿ Code Patching: The development team must implement "Prepared Statements" (parameterized queries) in view.php and search.php to prevent SQL injection.<br><br>
>> **List of Attack Indicators**: <br>
>>⦿  method: GET<br>
⦿  uri: /products/view.php?id=1%20UNION%20SELECT%20username%2Cpassword%20FROM%20users--<br>
⦿  protocol: HTTP/1.1<br>
⦿  status: 200<br>
⦿ bytes: 34614<br>
⦿  referer: -<br>
⦿ user_agent: sqlmap/1.7-dev-59e8f7c (https://sqlmap.org)<br>
>
> TRUE POSITIVE<br>
>
> ESCALATION NEEDED

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3b42f0d3-6691-4253-9945-cf4deb2c5f69"><br>Rosana´s hands-on.</p>

<br>
<br>
<h3 align="center"><em>I´ll soon share more about this invaluable experience</em>.</h3>

<br>
<br>
<br>
<h1 align="center">SOC Simulator Completed</h1>


<p align="center"><img width="600px" src="https://github.com/user-attachments/assets/881f1504-cecd-4098-afee-d005341cdd9b"></p>


<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|19     |Easy ⚙️ - Upload and Conquer          |17 |     81ˢᵗ  |     3ʳᵈ    |      181ˢᵗ   |        2ⁿᵈ     |    140,859  |    1,068    |    88     |
|18     |Easy 🔗 - MS Entra ID: Identities     |17 |     83ʳᵈ  |     3ʳᵈ    |      341ˢᵗ   |        3ʳᵈ     |    139,864  |    1,068    |    88     |
|18     |Easy ⚙️ - APT28: Initial Access       |17 |     84ᵗʰ  |     3ʳᵈ    |      341ˢᵗ   |        3ʳᵈ     |    139,752  |    1,067    |    88     |
|18     |Easy ⚙️ - Hidden Hooks                |17 |           |     3ʳᵈ    |              |                |             |    1,067    |    88     |
|17     |Easy 🔗 - MS Entra ID: Introduction   |17 |     83ʳᵈ  |     3ʳᵈ    |      359ᵗʰ   |        3ʳᵈ     |    139,657  |    1,067    |    88     |
|17     |Easy ⚙️ - APT28: Credential Access    |17 |           |     3ʳᵈ    |              |                |             |    1,067    |    88     |
|17     |Medium ⚙️ - Open Door                 |17 |           |     3ʳᵈ    |              |                |             |     1,067   |    88     |
|17     |Easy 🔗 - Offensive Security Intro    |16 |     87ᵗʰ  |     3ʳᵈ    |      504ᵗʰ   |        5ᵗʰ     |    139,099  |    1,067    |    88     |
|16     |Hard 🚩 - Spring                      |15 |     87ᵗʰ  |     3ʳᵈ    |      540ᵗʰ   |        4ᵗʰ     |    138,942  |    1,066    |    87     |
|14     |Insane 🚩 - Scheme Catcher            |13 |     87ᵗʰ  |     3ʳᵈ    |      534ᵗʰ   |        5ᵗʰ     |    138,822  |    1,065    |    87     |
|13     |Hard 🚩 - Breachblocker Unlocker      |12 |     86ᵗʰ  |     3ʳᵈ    |      526ᵗʰ   |        5ᵗʰ     |    138,732  |    1,064    |    87     |
|11     |Medium 🚩 - Azure: Eyes Wide Shut     |10 |     86ᵗʰ  |     3ʳᵈ    |      558ᵗʰ   |        5ᵗʰ     |    138,450  |    1,063    |    86     |
|8      |Medium ⚙️ - Phishing Unfolding        | 7 |     86ᵗʰ  |     3ʳᵈ    |      508ᵗʰ   |        4ᵗʰ     |    138,372  |    1,062    |    84     |
|8      |Easy ⚙️ - Introduction to Phishing    | 7 |     96ᵗʰ  |     3ʳᵈ    |    2,479ᵗʰ   |       32ⁿᵈ     |    137,117  |    1,062    |    84     |
|8      |Medium 🔗 - KaffeeSec - SoMeSINT      | 7 |     98ᵗʰ  |     3ʳᵈ    |    2,847ᵗʰ   |       38ᵗʰ     |    137,052  |    1,062    |    84     |
|7      |Hard 🚩 - Hack Back                   | 6 |     98ᵗʰ  |     3ʳᵈ    |    2,798ᵗʰ   |       37ᵗʰ     |    136,908  |    1,061    |    84     |
|7      |Hard 🚩 - Dead End?                   | 6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     | 5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   | 3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence| 2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  | 1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |

</h6></div><br>

<p align="center">Global All Time:     81ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/3ca21a8f-6914-42e4-a6d9-db9b6ff92495"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/616f2830-81c7-4fed-a988-8087e711a498"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/200917c0-fc88-441d-a6c1-33a3094a558f"><br><br>
                  Global monthly:     181ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/37ff1148-6bbc-4a6c-b1ab-7018c4c9dd6f"><br><br>
                  Brazil monthly:       2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/56db88da-eb42-4d94-b933-5cac17e44d35"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
