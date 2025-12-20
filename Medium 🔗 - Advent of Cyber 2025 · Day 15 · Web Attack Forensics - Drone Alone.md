<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 15 &nbsp;&nbsp; ·  &nbsp;&nbsp; Web Attack Forensics - Drone Alone</h3>
<p align="center">2025, December 20  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in <a href="https://tryhackme.com">TryHackMe</a>.<br>Explore web attack forensics using Splunk. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/webattackforensics-aoc2025-b4t7c1d5f8">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/9ebacb27-2c12-4c67-9640-7d1df3b86295"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/dbbed480-b5db-4f71-9a0b-5f3ad6a893ee"></p>


<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/4a01eaff-f172-49f4-93b8-13f16ed450c3"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>TBFC’s drone scheduler web UI is getting strange, long HTTP requests containing Base64 chunks. Splunk raises an alert: “Apache spawned an unusual process.” On some endpoints, these requests cause the web server to execute shell code, which is obfuscated and hidden within the Base64 payloads. For this room, your job as the Blue Teamer is to triage the incident, identify compromised hosts, extract and decode the payloads and determine the scope.<br>

You’ll use Splunk to pivot between web (Apache) logs and host-level (Sysmon) telemetry.<br>

Follow the investigation steps below; each corresponds to a Splunk query and investigation goal.</p>

<h3>Learning Objectives</h3>
<p>
  
- Detect and analyze malicious web activity through Apache access and error logs<br>
- Investigate OS-level attacker actions using Sysmon data<br>
- Identify and decode suspicious or obfuscated attacker payloads<br>
- Reconstruct the full attack chain using Splunk for Blue Team investigation</p>

<h3>Connecting to the Machine</h3>
<p>Before moving forward, review the questions in the connection card shown below:</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/4a8a25be-a3f3-4943-acb0-ec04967b4abe"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Start your target VM by clicking the <strong>Start Machine</strong> button below. The machine will need about 3 minutes to fully boot. Additionally, start your AttackBox by clicking the <strong>Start AttackBox</strong> button below. The AttackBox will start in split view. In case you can not see it, click the <strong>Show Split View</strong> at the top of the page.</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting both your AttackBox (if you're not using your VPN) and Target Machines, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<br>
<p><em>Answer the question below</em></p>

<p>1.1. <em>I have successfully started the AttackBox and the target machine!</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 &nbsp; ·  &nbsp; Web Attack Forensics</h2>
<h3>Logging into Splunk</h3>

<p>After you have started the AttackBox and the target machine in the previous task, allow the system around 3 minutes to fully boot, then use Firefox on the AttackBox to access the Splunk dashboard at <code>http://MACHINE_IP:8000</code> using the credentials below.</p>

<br>
<h3>Credentials</h3>
<p>To access Splunk dashboard<br>

- Username: Blue<br>
- Password: ...<br>
- IP address: ...<br>
- Connection via: HTTP<br>

The Splunk login page should look similar to the screenshot shown below.</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/379d0cba-c521-4b4f-ac09-383bfe21d08e"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>After logging in successfully, you will be taken to the Search Page as shown in the screenshot below.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/e9ac8cb8-6f6c-43b9-9b6c-cfbd51d91292"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Make sure to adjust the Splunk time range to include the time of the events (e.g., "Last 7 days" or "All time"). If the default range is too narrow, you may see "<em></em>No results found</em>."<br>

A Blue Teamer would explore various attack angles via Splunk. In this task, we will follow elf Log McBlue, who uses his Splunk magic to unravel the attack path.</p>

<br>
<h3>Detect Suspicious Web Commands</h3>
<p>In the first step, let’s search for HTTP requests that might show malicious activity. The query below searches the <strong>web access logs</strong> for any HTTP requests that include signs of command execution attempts, such as <code>cmd.exe</code>, <code>PowerShell</code>, or <code>Invoke-Expression</code>. This query helps identify possible Command Injection attacks, where the evil attacker tries to execute system commands through a vulnerable CGI script (<code>hello.bat</code>).<br>

<code>index=windows_apache_access (cmd.exe OR powershell OR "powershell.exe" OR "Invoke-Expression") | table _time host clientip uri_path uri_query status</code></p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/e6477638-913c-4473-a1af-636485e4721a"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<p>At this step, we are primarily interested in base64-encoded strings, which may reveal various types of activities. Once you spot encoded PowerShell commands, decode them using base64decode.org or your favourite base64 decoder to understand what the attacker was trying to do. Based on the results we received, let’s copy the encoded PowerShell string <code>VABoAGkAcwAgAGkAcwAgAG4AbwB3ACAATQBpAG4AZQAhACAATQBVAEEASABBAEEASABBAEEA</code> and paste it into https://www.base64decode.org/ upper field, then click on decode as shown in the screenshot below.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/67c586bb-1cc0-492b-8fd2-951b8decaaae"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<br>
<h3>Looking for Server-Side Errors or Command Execution in Apache Error Logs</h3>
<p>In this stage, we will focus on inspecting web server error logs, as this would help us uncover any malicious activity. We will use the following query:<br>

<code>index=windows_apache_error ("cmd.exe" OR "powershell" OR "Internal Server Error")</code><br>

This query inspects the Apache error logs for signs of execution attempts or internal failures caused by malicious requests. As you can tell, we are searching for error messages with particular terms such as <code>cmd.exe</code> and <code>powershell</code>.<br>

Please make sure you select <code>View: Raw</code> from the dropdown menu above the <code>Event</code> display field.</p
                                                                                                                       
<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/797e7a64-7cd9-4c30-82f1-40dd45b26378"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>If a request like <code>/cgi-bin/hello.bat?cmd=powershell</code> triggers a 500 “Internal Server Error,” it often means the attacker’s input was processed by the server but failed during execution, a key sign of exploitation attempts.<br>

Checking these results helps confirm whether the attack reached the backend or remained blocked at the web layer.</p>

<br>
<h3>Trace Suspicious Process Creation From Apache</h3>

<p>Let’s explore Sysmon for other malicious executable files that the web server might have spawned. We will do that using the following Splunk query:<br>

<code>index=windows_sysmon ParentImage="*httpd.exe"</code><br>

This query focuses on process relationships from Sysmon logs, specifically when the parent process is Apache (<code>httpd.exe</code>).<br>

Select <code>View: Table</code> on the dropdown menu above the <code>Event</code> display field.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/10ccf340-84d9-4365-95da-148e170a9c81"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Typically, Apache should only spawn worker threads, not system processes like <code>cmd.exe</code> or <code>powershell.exe</code>.<br>

If results show child processes such as:<br>

<code>ParentImage = C:\Apache24\bin\httpd.exe</code><br>

<code>Image        = C:\Windows\System32\cmd.exe</code><br>

It indicates a successful command injection where Apache executed a system command.<br>

The finding above is one of the strongest indicators that the web attack penetrated the operating system.</p>

<br>
<h3>Confirm Attacker Enumeration Activity</h3>
<p>In this step, we aim to discover what specific programs we found from previous queries do. Let’s use the following query.<br>

<code>index=windows_sysmon *cmd.exe* *whoami*</code><br>

This query looks for <strong>command execution logs</strong> where <code>cmd.exe</code> ran the command <code>whoami</code>.<br>

Attackers often use the <code>whoami</code> command immediately after gaining code execution to determine which user account their malicious process is running as.<br>

Finding these events confirms the attacker’s post-exploitation reconnaissance, showing that the injected command was executed on the host.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/81ac6eb8-7ab3-4139-b4d2-9ae23218cd04"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<br>
<h3>Identify Base64-Encoded PowerShell Payloads</h3>
<p>In this final step, we will work to find all successfully encoded commands. To search for encoded strings, we can use the following Splunk query:<br>

<code>index=windows_sysmon Image="*powershell.exe" (CommandLine="*enc*" OR CommandLine="*-EncodedCommand*" OR CommandLine="*Base64*")</code><br>

This query detects PowerShell commands containing -EncodedCommand or Base64 text, a common technique attackers use to <strong>hide their real commands</strong>.

If your defences are correctly configured, this query should return <strong>no results</strong>, meaning the encoded payload (such as the “Muahahaha” message) never ran.

If results appear, you can decode the Base64 command to inspect the attacker’s true intent.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/e7dca22c-9396-4bbd-9067-448f87baefef"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the questions below</em></p>

<br>
<p>2.1. <em>What is the reconnaissance executable file name?</em><br>
<code>whoami.exe</code></p>

<br>
<p>2.2. <em>What executable did the attacker attempt to run through the command injection?</em><br>
<code>PowerShell.exe</code></p>

```bash
index=windows_apache_access (cmd.exe OR powershell OR "powershell.exe" OR "Invoke-Expression")
| table _time host clientip uri_path uri_query status source
| sort +_time
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/801fd4fd-ed90-464d-984d-ab45f1bcb3cc"><br>Rosana´s hands-on</h6>
<br>
<br>
<br>

```bash
index=windows_apache_error ("cmd.exe" OR "powershell" OR "Internal Server Error")
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/74b797b8-b5b8-4fb4-9313-d7484a1bbdc7"><br>Rosana´s hands-on</h6>
<br>
<br>
<br>

```bash
index=windows_sysmon ParentImage="*httpd.exe"
| sort +_time
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/45af2973-a3c8-4758-b3a3-253bb0793951"><br>Rosana´s hands-on</h6>
<br>
<br>
<br>

```bash
index=windows_sysmon *cmd.exe* *whoami*
| table _time User Computer Image CommandLine ParentCommandLine
| sort +_time
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/f7e0f470-c05d-45cd-afff-903c617981b0"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/55fd42d6-7f7b-4ec3-b00b-06fab5250216"><br>Rosana´s hands-on</h6>
<br>
<br>
<br>

```bash
index=windows_sysmon ParentUser="WEBAPPSERVER\\apache_svc"
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b24ed75a-684f-408c-86c9-19a748e92068"><br>Rosana´s hands-on</h6>
<br>
<br>
<br>

```bash
index=windows_sysmon *cmd.exe* *whoami*
| table _time CommandLine Image ParentCommandLine Computer User
| sort +_time
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/55d77a00-7511-445d-9679-efa870bd3673"><br>Rosana´s hands-on</h6>




<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/dcb74100-be6d-4588-9ce9-d31552a635c2"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/fe780da4-1cfa-4791-83c2-e44b737ce7a9"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/2ee7914d-fc05-4a4e-8628-a8b22c492173"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|20      |Medium 🔗 - Web Attack Forensics - Drone Alone   |4 |     100ᵗʰ  |     3ʳᵈ    |   21,935ᵗʰ   |      243ʳᵈ     |    134,808  |    1,041    |    84     |
|20      |Easy 🔗 - XSS - Merry XSSMas                     |4 |     100ᵗʰ  |     3ʳᵈ    |   23,069ᵗʰ   |      256ᵗʰ     |    134,792  |    1,040    |    84     |
|20      |Easy 🔗 -  Race Conditions - Toy to The World    |4 |     100ᵗʰ  |     3ʳᵈ    |   24,717ᵗʰ   |      275ᵗʰ     |    134,768  |    1,039    |    84     |
|20      |Medium 🔗 -  SOC Alert Triaging - Tinsel Triage  |4 |     100ᵗʰ  |     3ʳᵈ    |   25,202ⁿᵈ   |      286ᵗʰ     |    134,752  |    1,038    |    84     |
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


<p align="center">Global All Time:    100ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/39240617-4498-4ed3-bcd4-207ce3e4a6e4"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/defc8ed4-eae6-4c95-a4fd-e128c236dacb"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/32c6bb43-f746-4842-8d58-4f923e55f02b"><br><br>
                  Global monthly:  21,935ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/91322df2-eda4-41fa-85e1-b0e223152f18"><br><br>
                  Brazil monthly:     243ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/adfcffdf-c0ce-45bf-af4c-c843dfdb4147"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>



