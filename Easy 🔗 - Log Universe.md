<h1 align="center">Log Universe</h1>
<h3 align="center"> Practice $$\textcolor{#3bd62d}{\textnormal{ULogViewer}}$$.</h3>
<p align="center">Explore log files from various systems and learn how to carve data to adopt a course of action! Click <a href="https://tryhackme.com/room/loguniverse">here </a>to access this TryHackMe CTF<br>
August 1, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>452</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="80px" src="https://github.com/user-attachments/assets/26cdddef-0a94-480a-9645-be58cb7c33f4"><br>
<img width="1200px" src="https://github.com/user-attachments/assets/4c36267d-6c2c-43ac-819c-f1614daac306"></p>

<br>

<h2>Task 1 .Introduction</h2>


<h2>Task 2 . Treasure Among the Lines: Logs</h2>


<h2>Task 3 . Toolset and Hints</h2>


<h2>Task 4 . Zoom In: Windows Event Logs</h2>
<h3>Windows Event Log Anatomy</h3>
<p>Windows event logs provide in-depth footprint information on the system, security, and applications installed on a Windows operating system. Windows provides a generous amount of logs, and you will need to activate them according to your visibility needs and capacity. Remember, the logging scope is fully configurable, and the default settings are not enough for the current state of the threats. Being comfortable with logs is a vital skill, but it is also important to have the general characteristics before deep diving into each log source's details. Now, let's take a look at the Windows event log characteristics. Below are the main specifications of the Windows event logs.</p>

<img width="917" height="445" alt="image" src="https://github.com/user-attachments/assets/9a7aad88-72fc-4cea-b94d-7e376a573c21" />

<p>As explained in the table above, Windows event logs can be generated and stored in a variety of extensions and formats. The alternatives here provide great flexibility in the logging and analysis process, allowing the environment to be painlessly set up for the analysis phase and to take advantage of alternative components. <br>

After getting familiar with the log file formats, it is time to identify the event log file categories. By default, there are two main log categories in Windows. The details are shown in the table below.</p>

<img width="919" height="325" alt="image" src="https://github.com/user-attachments/assets/8f69f6ba-e39b-4f92-bab6-ca79973ed061" />

<p>We've already mentioned that Windows systems are very generous when it comes to logging. Windows systems can generate hundreds of logs for the two categories mentioned above. Some are commonly used, and others need to be activated by configuration. Now, let's look at common log files and find out what information they provide! The table below highlights the commonly used event logs.</p>

<img width="917" height="635" alt="image" src="https://github.com/user-attachments/assets/4a45ff90-5cde-4b8f-897d-45e1b75b0d48" />

<p>The following table breaks down the anatomy of the event logs and explains the main elements. In case you can't recall what a Windows event Log file looks like, use the given hints and image. </p>

<img width="921" height="97" alt="image" src="https://github.com/user-attachments/assets/0ab7f13a-cc21-4935-bd1c-a4a0847c0f6a" />

<br>

<img width="980" height="404" alt="image" src="https://github.com/user-attachments/assets/7ac56478-7c1c-4f2d-854e-4b81b7a625f0" />

<br>

<p>Now, let's cover the main parts of the log file. </p>

<img width="814" height="812" alt="image" src="https://github.com/user-attachments/assets/7935b89a-d8d2-4675-a390-2d2a9e1618dd" />

<p>Remember that you will use the ULogViewer to view and filter the logs. The sample log is parsed as shown in the figure below. Field details are opened by double-clicking on the field or clicking on the "view more" section.</p>

<img width="768" height="151" alt="image" src="https://github.com/user-attachments/assets/6b4a4898-8716-42e6-b54d-b59a953491a3" />

<p>PID and TID data are beneficial for process tracing, correlation, and understanding the natural flow of events during log analysis. The timestamp also plays an essential role in determining which processes and threads were running at a particular time or during the workflow and, if applicable, the call times of the child processes and threads created by the user or execution flow.<br>
 
Learning the anatomy of the Windows log files is essential, but you will also need to know the indicative event log IDs and details. Therefore, you will be able to track and understand the details of a potential anomaly or an intrusion attempt. Some useful Windows event log IDs are listed below.</p>

<img width="815" height="522" alt="image" src="https://github.com/user-attachments/assets/96aa3ecf-9f2a-40e5-86cf-8c174d67bef4" />

<p>Note that each source produces different logs for different purposes. The Intro to logs room covers common log types, formats and standards. You will find more information in this space if you are still getting familiar with logs. You can also visit the Windows Event Logs and Sysmon rooms for more details about the event you are interested in.<br>
 
Now, switch to the given VM and analyse the "Windows Questions" log file using ULogViewer.</p>


<p><em>Answer the questions below</em></p>

<p>4.1. What is the Thread ID of the user creation event?<br>
<code>744</code></p>

<img width="1397" height="848" alt="image" src="https://github.com/user-attachments/assets/817ebc46-0c74-4451-9f43-9f0503dec72e" />

<br>
<p>4.2. What is the account name that creates the new user?<br>
<code>Administrator</code></p>

<img width="1387" height="837" alt="image" src="https://github.com/user-attachments/assets/7ddc4cf8-2e0e-46e6-baf1-686783efd6eb" />

<br>
<p>4.3. What is the name of the created account name?<br>
<code>Administrator</code></p>

<img width="1389" height="851" alt="image" src="https://github.com/user-attachments/assets/b8f56438-adeb-46d0-af7f-c327ea7256e1" />

<br>
<p>4.4. What is the "SubjectLogonID" value of the "account reset attempt" event?<br>
<code>0x4B666</code></p>

<img width="1388" height="851" alt="image" src="https://github.com/user-attachments/assets/9de66486-038e-405a-83e2-f339c8ff4df1" />

<br>

<h2>Task 5 . Zoom In: Linux Logs</h2>
<h3>Linux Logs Anatomy</h3>
<p>Like Windows event logs, Linux logs provide in-depth footprint information on the system, security, and applications installed. Again, the logging scope is fully configurable, and the default settings are not enough for the current state of the threats. Let's take a deep dive into the Unix-like system logs!</p>

<img width="817" height="372" alt="image" src="https://github.com/user-attachments/assets/0bec6e02-42e6-4148-8e9b-540e82e955d7" />

<h3>Common Logs Generated by Unix-like Systems</h3>
<h4>Cleartext Formatted Logs</h4>
<p>Cleartext logs can be viewed and analysed using multiple tools, as highlighted in the above table.</p>

<img width="833" height="259" alt="image" src="https://github.com/user-attachments/assets/84488d6a-72d9-46b6-8e87-b37ba49637d9" />

<h4>Logs Require Specific Binary to View</h4>
<p>Some binary formatted logs can be viewed and analysed only with the corresponding tool.</p>

<img width="701" height="209" alt="image" src="https://github.com/user-attachments/assets/8b04bbdb-f0cc-48c9-8a40-1b54984990bf" />

<p>The Syslog log file structure is defined by RFC 5424 - 5426. Also, it is widely used and easy to process with native granular system tools like tail and grep. The structure details are explained in the following table.</p>

<img width="819" height="362" alt="image" src="https://github.com/user-attachments/assets/51e3e086-301a-4165-83ea-e276f53df4af" />

<p>While RFC defines the main structure, there are alternative implementations of message presentations. The common structure (IETF) is shown below.<br>

- <strong>IETF log format</strong>:<br>

<code>timestamp hostname process[pid]: message</code></p>

<h3>Sample Log: Syslog<br>
Case: Command Execution</h3>

<p>

- <strong>Example log in IETF format</strong>:<br>
<code>2023-09-28T15:05:55.333333Z TempServer sudo[2345]: [AUTH] User alice executed command '/usr/bin/apt-get update'.</code><br><br>

- <strong>Evaluation</strong><br>
The above log entry showcases an event where the user "Alice" executed the command '/usr/bin/apt-get update' using the 'sudo' command on the server "TempServer". This log entry provides valuable insights into user actions, including the executed command and authentication details, which can aid in auditing and monitoring system activities.<br>
As the previous example shows, reading and understanding a single log entry in a structured format can be relatively straightforward. However, the challenge increases when dealing with voluminous log files containing numerous lines of entries. In such cases, extracting the relevant attributes and establishing correlations becomes essential to comprehensively understand specific events within the log data.<br>

Analysing multi-line logs requires high attention to detail and the ability to filter and extract significant details. This process involves identifying and filtering timestamps, hostnames, process IDs, and event descriptions, among other critical details. By effectively analysing and correlating these attributes, it is possible to uncover the sequence of events, diagnose problems, and gain valuable insight into system behaviour, security incidents, or operational performance.<br>

In summary, while individual log entries may seem manageable, the complexity arises when dealing with large log datasets. The magic lies in organising the extraction and analysis of key attributes to reveal the underlying story hidden within the logs, making log management and monitoring an essential part of maintaining system health and security.<br>

The following log examples are a series of timestamped entries from "TempServer" that show critical system events and resource management. These logs provide insight into memory issues, process terminations, and system reboots. Each log entry includes essential information such as timestamp, server name (TempServer), log source (Kernel or Systemd), process IDs (PID), and detailed event descriptions. It's important to note that these logs are presented in a generic system log format, with no specific categorisation, providing an insight into the server's operational challenges and the need for memory management and system recovery.</p>

<h3>Sample Log: Syslog<br>
Case: Restart Due to Insufficient RAM</h3>

<p>

- <strong>Example log in IETF format</strong>:<br>
<code>2023-09-25T08:15:20.123456Z TempServer kernel: Out of memory: Killed process 5678 (myapp); system reboot required.<br>
2023-09-25T11:30:45.987654Z TempServer kernel: Memory cgroup out of memory: Kill process 9876 (database) score 500 or sacrifice child.<br>
2023-09-26T03:45:10.234567Z TempServer systemd[1]: Reached memory limit at process 1234 (myapp), restarting.<br>
2023-09-26T12:20:35.543210Z TempServer kernel: Swap space exhausted; system restarting to free up memory.<br>
2023-09-27T07:55:50.765432Z TempServer systemd[1]: Server running low on memory, initiating reboot for recovery. </code><br><br>

- <strong>Evaluation</strong><br>
The above log entries showcase events on "TempServer" that include crucial memory-related events. It shows that processes with IDs "5678" (myapp), "9876" (database), and "1234" (myapp) caused memory problems and resulted in process terminations, memory limit violations, swap space exhaustion, and low memory warnings, ultimately requiring reboots for recovery and stability.<br>

Now, switch to the given VM and analyse the "Linux" log file using ULogViewer. Remember that you will use the ULogViewer and select the "Linux System Log Files" profile to view and filter the logs. The sample log is parsed as shown in the figure below.<br>

<img width="820" height="152" alt="image" src="https://github.com/user-attachments/assets/1a3effe0-5b80-4642-901b-0a6a5280f5ca" />

</p>

<p><em>Answer the questions below</em></p>

<p>5.1. What is the number of successful sync events done by the NTPD service?<br>
<code>28</code></p>

<img width="1298" height="853" alt="image" src="https://github.com/user-attachments/assets/24975573-7f21-44c9-a7f3-bef5664d9601" />

<br>

<img width="1305" height="855" alt="image" src="https://github.com/user-attachments/assets/2870abbe-366b-4c92-b808-9a90e0a4d204" />

<br>

<img width="1303" height="853" alt="image" src="https://github.com/user-attachments/assets/affe8537-ae10-43a8-b425-8ea5a71a6e55" />

<br>
<p>5.2. Which user logged in using the SSHD service?<br>
<code>THMjohn-p</code></p>

<img width="1298" height="257" alt="image" src="https://github.com/user-attachments/assets/f7ad76b6-d464-4aa2-aa79-6e85f4ddd067" />

<br>
<p>5.3. What is the PID number of the Apache web server?<br>
<code>5678</code></p>

<img width="1304" height="292" alt="image" src="https://github.com/user-attachments/assets/74796e7d-8849-4e82-be05-2b09e7ecaeae" />

<br>
<p>5.4. Which service is stopped due to RAM issues?<br>
<code>nginx</code></p>

<img width="1299" height="168" alt="image" src="https://github.com/user-attachments/assets/c27427e8-b3d4-4e69-88f8-c019a3c482b4" />

<br>
<p>5.5. Which service is stopped due to CPU issues?<br>
<code>Apache Tomcat</code></p>

<img width="1310" height="177" alt="image" src="https://github.com/user-attachments/assets/fe4e3207-bf35-4ff3-bf89-6fe2fa736598" />

<br>
<p>5.6. What is the timestamp of the second time reset event? Hint: <em>Whole timestamp data.</em><br>
<code>03/27 15:51:56</code></p>

<img width="1305" height="195" alt="image" src="https://github.com/user-attachments/assets/93ec6f66-7e3f-46fb-bc87-2b36165b90c7" />

<br>

<h2> Task 6 . Zoom IN: Misc Logs</h2>
<h3>Misc Logs: Application Logs</h3>
<p>Misc logs provide in-depth footprint information on application-based events, giving more insights on application and process-based details that will help analysts in security operations, including monitoring, threat hunting, and incident response. This task will cover the details of Apache logs.</p>

<h3>Apache Logs</h3>
<h4>Apache Logs: Access.log</h4>
<p>Access logs are invaluable records generated by web servers, containing essential attributes that form the backbone of effective log analysis. These attributes, including IP addresses, timestamps, HTTP methods, URLs, status codes, and user agent information, play a vital role in web server management and security.<br>

These attributes enable administrators and analysts to ensure server health, diagnose problems, detect security threats, and optimise web services for a seamless user experience. Understanding the importance of these attributes is essential before embarking on log analysis, as it provides the baseline for informed decision making and effective web server management.<br>

The anatomy of the Apache access.log's "Combined log format" is detailed in the given table.</p>

<img width="819" height="563" alt="image" src="https://github.com/user-attachments/assets/5f80c8f1-d10f-4db5-b028-33d319fa3c05" />

<p>Apache access logs are identified by the "Common Log Format" and "Combined Log Format". Both formats focus on visibility but serve different purposes. The standard format is more lightweight and focuses on the basics, capturing only the essentials such as IP, URL and response. The combined format captures more details, such as referrer and user agent data, which is useful for in-depth analysis. The combined log format structure is shown in the below section.</p>

<p>

- <strong>Combined log format</strong><br>
<code>LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\"" combined</code></p>

<h4>Sample Log: Access Log<br>
Case: Using HTTP POST Method</h4>

<p>

- <strong>Example log in combined log format:</strong><br>
  <code>192.168.1.100 - THMjohn [15/Nov/2025:10:30:45 -0500] "POST /api/data HTTP/1.1" 404 1234 "https://www.LogUniverse-THM.com/page" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"</code><br><br>
- <strong>Evaluation:</strong><br>
  The above log file showcases a client IP 192.168.1.100 made a POST request to the "/api/data" URL on the server. It also shows that the server responded with a 404 "Not Found" status code. The client was referred by the "https://www.LogUniverse-THM.com/page" using the Mozilla web browser on the Windows 10 operating system.<br>
  Note that the web browser and operating system information can be manipulated or changed by an attacker crafting custom packets or using an attack or audit tool.<br>
  The sample log is parsed as shown in the figure below.<br>
  
  <img width="779" height="175" alt="image" src="https://github.com/user-attachments/assets/1c799834-e15b-428a-9438-5997999aec8a" /></p>

<h4>Apache Logs: Error.log</h4>
<p>Error logs are an essential component of web server management, providing critical insight into system health and potential issues that can impact server performance and user experience. These logs capture essential attributes such as timestamps, error messages, file paths, and originating IP addresses. These attributes are essential for administrators and analysts to diagnose and resolve errors, identify vulnerabilities, and maintain server security. Before delving into error log analysis, it is vital to understand the importance of these attributes as they provide the foundation for proactive problem resolution and continuous improvement of web server stability and reliability.<br>

The anatomy of the Apache error.log is detailed in the given table.</p>

<img width="815" height="382" alt="image" src="https://github.com/user-attachments/assets/e4b0909c-30e2-44c4-8b5d-0582ef4f60e9" />

<p>Unlike access.log, error.log is identified under a single format named "ErrorLogFormat" and focuses on providing additional information to the log message. The structure is shown in the below section.</p>

<p>

- <strong>ErrorLogFormat:</strong><br>
  <code>ErrorLogFormat "[%t] [%l] [pid %P] %F: %E: [client %a] %M"</code><br><br>

<h4>Sample Log: Error Log<br>
Case: Resource Availabilityd</h4>

- <strong>Example log in ErrorLogFormat:</strong><br>
  <code>[Thu May 12 08:28:57.652118 2011] [core:error] [pid 8777] [client ::1] File does not exist: /usr/local/apache2/htdocs/favicon.ico</code><br><br>
  
- <strong>Evaluation</strong><br>
  The above log file showcases a loopback address <code>::1</code>, which means an internal request made to the resource <code>favicon.ico</code> located on the same server. The message part highlights that the directory <code>/usr/local/apache2/htdocs</code> doesn't contain the requested file.<br>
  This error is valuable as it shows a missing resource on the server. This can help administrators to identify and fix the resource availability issue. Note that <code>::1</code> is a loopback address <code>127.0.0.1</code> in IPv6.<br>
  Now, switch to the given VM and use the tools and datasets to answer the questions.<br>
  Remember that you will use the ULogViewer to view and filter the logs. <strong>The sample log is parsed as shown in the figure below. Note that you need to use the "Raw Text In Files" format for the Apache Error.log file</strong>!<br>
  
  <img width="818" height="179" alt="image" src="https://github.com/user-attachments/assets/8ea2dec2-b8ae-47c6-90af-1c8c067d03ca" /></p>

<p><em>Answer the questions below</em></p>

<p>6.1. <strong>Use the Access.log file to answer the first few questions</strong>. What is the user's IP address who accessed "/secure.html"? (In defanged format). Hint: <em>CyberChef can defang.</em><br>
<code>203[.]45[.]78[.]103</code></p>

<img width="1390" height="852" alt="image" src="https://github.com/user-attachments/assets/af5aa200-5eda-4e46-aa3a-acf3593951cb" />

<img width="1507" height="282" alt="image" src="https://github.com/user-attachments/assets/4367066f-7da5-4c72-95b4-78e3a9303dfe" />

<img width="1914" height="786" alt="image" src="https://github.com/user-attachments/assets/189a5e20-ea90-4b80-b5b7-9bcd7d2dfe57" />

<p><code>203.45.78.103</code> defanged is <code>203[.]45[.]78[.]103</code></p>

<br>
<p>6.2. Which user failed to access the settings page?<br>
<code>buyer986</code></p>

<img width="1904" height="534" alt="image" src="https://github.com/user-attachments/assets/4d66b5c4-7a82-46ad-992d-5dd84ee97b51" />

<br>
<p>6.3. Which user accessed the malicious page? Hint: <em>Status codes are important to notice. Regex hint: (payload|\?|param|passwd|shell)</em><br>
<code>adv8779</code></p>

<img width="1899" height="659" alt="image" src="https://github.com/user-attachments/assets/8a33c0c4-44f4-4d7a-93be-41200f85b03f" />

<img width="1914" height="546" alt="image" src="https://github.com/user-attachments/assets/8310f8af-e357-4df8-9335-b9577f554b9c" />

<br>
<p>6.4. What is the user agent that discovered the malicious page?<br>
<code>nikto/2.1.5 (OpenVAS)</code></p>

<img width="1899" height="659" alt="image" src="https://github.com/user-attachments/assets/6e159967-2458-405e-a5ed-1fba21e55d3e" />

<br>
<p>6.5. <strong>Use the Error.log file to answer the rest of the questions.</strong> What is the PID of the process that causes permission error?<br>
<code>7654</code></p>

<img width="1906" height="672" alt="image" src="https://github.com/user-attachments/assets/b3398ade-88d1-4d8b-a212-97df34de6812" />

<img width="1908" height="519" alt="image" src="https://github.com/user-attachments/assets/f15ac9fe-7d19-4696-9adc-a515666c376e" />

<br>
<p>6.6. What is the request that contains an invalid method?<br>
<code>\x80\x03\x01\x00\x01</code></p>

<img width="1901" height="289" alt="image" src="https://github.com/user-attachments/assets/0c5b33ca-1b66-4a2a-a450-287a767d35db" />

<br>
<p>6.7. What pattern match triggered the access error in ModSecurity? Hint: <em>Don't forget to also use the quotation marks around the pattern.</em><br>
<code>"SELECT.+FROM"</code></p>

<img width="1906" height="561" alt="image" src="https://github.com/user-attachments/assets/e4280dbf-8657-480f-9d2e-c27430974a7b" />

<br>
<p>6.8. What is the path value of the file that tries to remove data from the system?<br>
<code>/etc/httpd/conf.d/malicious.conf</code></p>

<img width="1907" height="528" alt="image" src="https://github.com/user-attachments/assets/0defb65d-70b8-499b-a087-703dab3cccaa" />


<br>
<h2>Task 7 . Conclusion</h2>
<h3>﻿Congratulations!</h3>
<p>You just finished the "Log Operations" room. In this room, we dived deep into Windows, Linux and Apache log file configurations attributes and discovered the data carving points for in-depth log analysis operations by covering:<br>

- Windows event log structure<br>
- Linux syslog structure<br>
- Apache access and error log structure<br><br>
Now, you have a solid understanding of the common log formats and are ready to carve data to adopt a course of action! So, it's time to visit the Advanced Splunk and Advanced ELK modules to fire advanced queries focused on bits of the log files!</p>

<p><em>Answer the question below</em></p>

<p>7.1. Click and continue learning!<br>
<code>No answer needed</code></p>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ec3adeed-c4ee-43f0-bee9-5d6f78c5a43"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/ccf7439e-5dbd-4f44-9ee3-9297839a9bac"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 1    | 452      |     142ⁿᵈ    |      5ᵗʰ     |   2,645ᵗʰ   |    31ˢᵗ    | 118,384  |    887    |    73     |



</div>

<p align="center">Global All Time:   142ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/6f03e5b2-b5d2-4fa7-adef-ddcae96280f0"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/e34c9e2a-8f75-4c9a-9b99-971e217c1960"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3ab8dc46-cb3a-4e2d-9bc7-9e8b57263471"><br>
                  Global monthly:   2,645ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/a6e9e22d-bb63-4926-8fca-642d7e3fbc22"><br>
                  Brazil monthly:      31ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/bd02f264-ad45-4619-ad6c-eb9e6b597391"><br>

  <br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
