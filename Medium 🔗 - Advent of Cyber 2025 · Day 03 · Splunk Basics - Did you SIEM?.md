<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 2 &nbsp;&nbsp; ·  &nbsp;&nbsp; Splunk Basics - Did you SIEM?</h3>
<p align="center">2025, December 6  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Learn how to ingest and parse custom log data using Splunk. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/splunkforloganalysis-aoc2025-x8fj2k4rqp">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/237d6ff9-bb6f-40d7-9678-599727de9987"></p>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/15c21f5f-a88d-48bb-8e1a-8d7cc94fd346"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>It’s almost Christmas in Wareville, and the team of The Best Festival Company (TBFC) is busy preparing for the big celebration. Everything is running smoothly until the SOC dashboard flashes red. A ransom message suddenly appears: </p>

<h6 align="center"><img width="300px" src="https://github.com/user-attachments/assets/2cc8ff6f-aa3a-4ccd-b37c-d3adda3115de"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<p>The message comes from King Malhare, the jealous ruler of HopSec Island, who’s tired of Easter being forgotten. He’s sent his Bandit Bunnies to attack TBFC’s systems and turn Christmas into his new holiday, EAST-mas.<br>

With McSkidy missing and the network under attack, the TBFC SOC team will utilize Splunk to determine how the ransomware infiltrated the system and prevent King Malhare’s plan from being compromised before Christmas.</p>

<h3>Learning Objectives</h3>
<p>

- Ingest and interpret custom log data in Splunk<br>
- Create and apply custom field extractions<br>
- Use Search Processing Language (SPL) to filter and refine search results<br>
- Conduct an investigation within Splunk to uncover key insights</p>

<h3>Connecting to the Machine</h3>
<p>Before moving forward, review the questions in the connection card shown below:</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/cfb6ae2e-3a94-495c-a37c-16db4be4a35e"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Start your VM by clicking the <strong>Start Machine</strong> button below. The machine will need about 2-3 minutes to fully boot. Once the machine is up and running, you can connect to the Splunk SIEM by visiting <code>https://LAB_WEB_URL.p.thmlabs.com</code> in your browser.<br><strong>Note</strong>: If you get a 502 error when accessing the link, please give the Splunk instance more time to fully boot up.</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p><em>Answer the question below</em></p>

<p>1.1. &nbsp;&nbsp; <em>I successfully have access to the Splunk instance!</em><br>
<code>No answer needed</code><p>

<h2>Task 2 &nbsp; ·  &nbsp; Log Analysis with Splunk</h2>
<h3>Exploring the Logs</h3>
<p>In the Splunk instance, the data has been pre-ingested for us to investigate the incident. On the Splunk interface, click on Search & Reporting on the left panel, as shown below:</p>




<p>On the next page, type index=main in the search bar to show all ingested logs. Note that we will need to select All time as the time frame from the dropdown on the right of the search bar.</p>




<p>After running the query, we will be presented with two separate datasets that have been pre-ingested into Splunk. We can verify this by clicking on the sourcetype field in the fields list on the left of the page.</p>



<p>The two datasets are as follows:<br>

- web_traffic: This data source contains events related to web connections to and from the web server.<br>
- firewall_logs: This data source contains the firewall logs, showing the traffic allowed or blocked. The local IP assigned to the web server is 10.10.1.15.<br>

Let's explore the logs and investigate the attack on our servers to identify the culprit.</p>

<br>
<h3>Initial Triage</h3>
<p>Start a basic search across the index using your custom source type web_traffic, using the following query:<br>

Search query: index=main sourcetype=web_traffic</p>

<p>Let's break down our result for a better understanding:<br>

- Search query: This query retrieves all events from the main index that were tagged with the custom source type web_traffic. This marks the beginning of the investigation.<br>
- Time range: The time range is currently set to "All time". In security analysis, this range would be tightened (e.g., to the spike window) after initial data loading.<br>
- Timeline: This visual histogram shows the distribution of the 17,172 events over time. The graph indicates the successful daily log volume followed by a distinctive traffic spike (a period of high activity, likely the attack window).<br>
- Selected fields: These are the fields currently chosen to be displayed in the summary column of the event list (host, source, sourcetype). They represent basic metadata about the log file itself.<br>
- Interesting fields: This pane lists all fields that Splunk has automatically extracted or manually added. Fields prefixed with # (e.g., #date_hour) are automatically generated by Splunk's time commands. The presence of user_agent, path, and client_ip confirms the successful parsing of the web log structure.<br>
- Event details & field extraction: This section shows the parsed details of a single event with extracted fields like user_agent, path, status, client_ip, and more.<br>

Now that we have an understanding of the Splunk layout and how to read the logs in Splunk. Let's continue our analysis of the logs.</p>

<br>
<h3>Visualizing the Logs Timeline</h3>
<p>Let's chart the total event count over time, grouped by day, to determine the number of events captured per day. This will help us in identifying the day that received an abnormal number of logs.<br>

Search query: index=main sourcetype=web_traffic | timechart span=1d count</p>




<p>The above results are now showing the event logs captured per day. This could be interesting, as we can see some days getting a high volume of logs. We can also click on the Visualization tab to examine the graph for better representation, as shown below:</p>



<p>We can append the reverse function at the end to display the result in descending order, showing the day with the maximum number of events at the beginning.<br>

Search query: index=main sourcetype=web_traffic | timechart span=1d count | sort by count | reverse </p>

<p>There is a clear period of intense activity during which King Malhare launched his main attack phase.</p>

<br>
<h3>Anomaly Detection</h3>
<p>Now that we have examined the days with the abnormal logs, using the table and the graph, let's use the same search query to examine various fields to hunt for suspicious values. We need to go back to the Events tab to continue.</p>

<br>
<h4>User Agent</h4>

<p>Let's click on the user_agent field in the left panel, as shown below. It will show us the details about the user agents captured so far. </p>



<p>Upon closer examination, it becomes clear that, apart from legitimate user agents like Mozilla's variants, we are receiving a large number of suspicious ones, which we will need to investigate further.</p>

<br>
<h4>client_ip</h4>

<p>The second field we will examine is the client_ip, which contains the IP addresses of the clients accessing the web server. We can immediately see one particular IP address standing out, which we will investigate further.</p>



<br>
<h4>path</h4>
<p>The third field we will examine is path, which contains the URI being requested and accessed by the client IPs. The results shown below clearly indicate some attacks worth investigating.</p>

<br>
<h3>Filtering out Benign Values</h3>
<p>We know King Malhare's bunnies use scripts and tools, not standard browsers. Let's filter out all standard traffic.<br>

Let's exclude common legitimate user agents. The following query will remove legitimate user agents from the results and only show the suspicious ones, which we will further investigate.<br>

<strong>Search query</strong>: <code>index=main sourcetype=web_traffic user_agent!=*Mozilla* user_agent!=*Chrome* user_agent!=*Safari* user_agent!=*Firefox*</code></p>



<p>The output reveals interesting results. By clicking on the client_ip field we can see a single IP address being responsible for all the suspicious user agents. Let's note that down for further investigation and fill in the <REDACTED> portions of the upcoming queries with that IP.</p>

<br>
<h3>Narrowing Down Suspucuous IPS</h3>
<p>In real-world scenarios, we often encounter various IP addresses constantly attempting to attack our servers. To narrow down on the IP addresses that do not send requests from common desktop or mobile browsers, we can use the following query:.<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic user_agent!=*Mozilla* user_agent!=*Chrome* user_agent!=*Safari* user_agent!=*Firefox* | stats count by client_ip | sort -count | head 5</code></p>




<p>The result confirms the top IP used by the Bandit Bunnies. In the search query, the - in the sort -count part will sort the result by count in reverse order, it's the same as using the reverse function. Let's pick this IP address and filter out to see what the footprints of the activities captured.</p>

<h3>Tracing the Attack Chain</h3>
<p>We will now focus on the selected attacker IP to trace their steps chronologically, confirming the use of multiple tools and payloads. Don’t forget to replace <REDACTED> with the IP we noted down previously.</p>

<br>
<h4>Reconnaissance (Footprinting)</h4>
<p>We will start searching for the initial probing of exposed configuration files using the query below:<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic client_ip="<REDACTED>" AND path IN ("/.env", "/*phpinfo*", "/.git*") | table _time, path, user_agent, statu</code></p>



<p>The result confirms the attacker used low-level tools (curl, wget) and was met with 404/403/401 status codes.</p>

<br>
<h4>Enumeration (Vulnerability Testing)</h4>
<p>Search for common path traversal and open redirect vulnerabilities.<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic client_ip="<REDACTED>" AND path="*..*" OR path="*redirect*"</code></p>




<p>The output shows the resources the attacker is trying to access. Let's update the search query to get the count of the resources requested by the attacker. This search query is filtering on the paths that contain either ../../ or the term redirect in it, as shown below. This is done to look for footprints of path traversal attempts (../../). To, we need to update in the search query to escape the characters like ..\/..\/.<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic client_ip="<REDACTED>" AND path="*..\/..\/*" OR path="*redirect*" | stats count by path"</code></p>




<p>Quite interesting results. Reveals attempts to read system files (../../*), showing the attacker moved beyond simple scanning to active vulnerability testing.</p>



<br>
<h4>SQL Injection Attack</h4>
<p>Find the automated attack tool and its payload by using the query below:<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic client_ip="<REDACTED>" AND user_agent IN ("*sqlmap*", "*Havij*") | table _time, path, status</code></p>



<p>Above results confirms the use of known SQL injection and specific attack strings like SLEEP(5). A 504 status code often confirms a successful time-based SQL injection attack.</p>

<br>
<h3>Exfiltration Attempts</h3>
<p>Search for attempts to download large, sensitive files (backups, logs). We can use the query below:<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic client_ip="<REDACTED>" AND path IN ("*backup.zip*", "*logs.tar.gz*") | table _time path, user_agent</code></p>



<p>The results indicate the attacker was exfiltrating large chunks of compressed log files using tools like curl, zgrab, and more. We can confirm the details about these connections in the firewall logs.</p>

<br>
<h3>Ransomware Staging & RCE</h3>
<p>Requests for sensitive archives like /logs.tar.gz and /config indicate the attacker is gathering data for double-extortion. In the logs, we identified some requests related to bunnylock and shell.php. Let's use the following query to see what those search queries are about.<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic client_ip="<REDACTED>" AND path IN ("*bunnylock.bin*", "*shell.php?cmd=*") | table _time, path, user_agent, status</code></p>



<p>Above results clearly confirm a successful webshell. The attacker has gained full control over the web server and is also able to run commands. This type of attack is called Remote code Execution (RCE). The execution of /shell.php?cmd=./bunnylock.bin indicates a ransomware like program executed on the server. </p>

<br>
<h3>Correlate Outbound C2 COmmunication</h3>
<p>We pivot the search to the firewall_logs using the Compromised Server IP (10.10.1.5) as the source and the attacker IP as the destination.<br>

<strong>Search query</strong>: <code>sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="<REDACTED>" AND action="ALLOWED" | table _time, action, protocol, src_ip, dest_ip, dest_port, reason</code></p>



<p>This query proves the server immediately established an outbound connection to the attacker's C2 IP on the suspicious DEST_PORT. The ACTION=ALLOWED and REASON=C2_CONTACT fields confirm the malware communication channel was active.</p>


<br>
<h3>Volume of Data Exfiltrated</h3>
<p>We can also use the sum function to calculate the sum of the bytes transferred, using the bytes_transferred field, as shown below:<br>

<strong>Search query</strong>: <code>sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="<REDACTED>" AND action="ALLOWED" | stats sum(bytes_transferred) by src_ip</code></p>



<p>The results show a hugh volume of data transferred from the compromised webserver to C2 server.</p>

<br>
<h3>Conclusion</h3>
<p>

- Identity found: The attacker was identified via the highest volume of malicious web traffic originating from the external IP.<br>
- Intrusion vector: The attack followed a clear progression in the web logs (sourcetype=web_traffic).<br>
- Reconnaissance: Probes were initiated via cURL/Wget, looking for configuration files (/.env) and testing path traversal vulnerabilities.<br>
- Exploitation: The use of SQLmap user agents and specific payloads (SLEEP(5)) confirmed the successful exploitation phase.<br>
- Payload delivery: The Action on Objective was established by the final successful execution of the command cmd=./bunnylock.bin via the webshell.<br>
- C2 confirmation: The pivot to the firewall logs (sourcetype=firewall_logs) proved the post-exploitation activity. The internal, compromised server (SRC_IP: 10.10.1.5) established an outbound C2 connection to the attacker's IP.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. &nbsp;&nbsp; <em>What is the attacker IP found attacking and compromising the web server?</em><br>
<code>198.51.100.55</code></p>

```bash
index=main sourcetype=web_traffic user_agent!=*Mozilla* user_agent!=*Chrome* user_agent!=*Safari* user_agent!=*Firefox*
```

<p>

- select <code>client_ip</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/44df4a63-eac0-42db-ab5a-9720a45a0794"></p>

<br>
<p>2.2. &nbsp;&nbsp; <em>Which day was the peak traffic in the logs? (Format: YYYY-MM-DD)</em><br>
<code>2025-10-12</code></p>

```bash
index=main sourcetype=web_traffic
|  timechart span=1d count
|  sort by count
|  reverse
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b1a313c0-55ab-44e9-b892-da41854c654f"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/d20a551f-7fd6-4140-87d2-188f1c405ae1"></p>

<br>
<p>2.3. &nbsp;&nbsp; <em>What is the count of Havij user_agent events found in the logs?</em><br>
<code>993</code></p>

<p>

- select <code>user_agent</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/bfead410-48a0-4553-aefe-81bf9506ec8a"></p>

<br>
<p>2.4. &nbsp;&nbsp; <em>How many path traversal attempts to access sensitive files on the server were observed?</em><br>
<code>658</code></p>

```bash
index=main sourcetype=web_traffic user_agent!=*Mozilla* user_agent!=*Chrome* user_agent!=*Safari* user_agent!=*Firefox*
```

<p>

- select <code>path</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/564c0747-d64a-49b7-9623-eef307cb1d5e"></p>


```bash
index=main sourcetype=web_traffic
|  stats count by client_ip
|  sort -count
|  head 5
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/55dca240-ab27-4743-b1c5-56c3ea5ca1c3"></p>


```bash
index=main sourcetype=web_traffic client_ip=198.51.100.55
|  stats count by path
|  sort -count
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/263e19a5-65cd-48c6-bbcf-7b37579ddb8e"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/110a0245-6dac-4803-9bc1-2c6daa90fc1e"></p>

```bash
index=main sourcetype=web_traffic client_ip=198.51.100.55 AND path IN ("/.env","/.*phpinfo","/.git*")
| table _time, path, user_agent, status
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/54d11039-2629-44e2-9fc5-6ef8b2a88f23"></p>

```bash
index=main sourcetype=web_traffic client_ip=198.51.100.55 AND path="*..*" OR path="*redirect*"
| table _time, path, user_agent, status
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/52fc2347-22bd-43c8-8523-61ff6b456cef"></p>

```bash
index=main sourcetype=web_traffic client_ip=198.51.100.55 AND path="*..*" OR path="*redirect*"
| table _time, path, user_agent, status
|  stats count by path
|  sort -count
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/960e5f4a-7d2d-4141-b4c3-5954f2403ab0"></p>

<br>
<p>2.5. &nbsp;&nbsp; <em>Examine the firewall logs. How many bytes were transferred to the C2 server IP from the compromised web server?</em> Hint: Use the sum command to get the accumulative result.<br>
<code>126167</code></p>

```bash
index=main sourcetype=web_traffic client_ip=198.51.100.55 AND user_agent IN ("*sqlmap*","*Havij*") 
|  table _time, path, status
```

<p>

- status <code>504</code> indicates a successfull timebased SQl Injection</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/1c4cf8c7-7d7c-4b9b-b745-9a332267ce8d"></p>

```bash
index=main sourcetype=web_traffic client_ip=198.51.100.55 AND user_agent IN ("*sqlmap*","*Havij*")  AND status=200
|  table _time, path, size_bytes, status
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/e2f6f6ce-8e49-4106-a0b6-5903afde1726"></p>

```bash
sourcetype=web_traffic client_ip="198.51.100.55" AND path IN ("*bunnylock.bin*", "*shell.php?cmd=*")
| table _time, path, user_agent, status
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/1dcad605-3cdd-4e6e-b8d8-4c9705e389a9"></p>

```bash
sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="198.51.100.55" AND action="ALLOWED"
| table _time, action, protocol, src_ip, dest_ip, dest_port, reason
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c2522cf1-6c0d-479b-8164-2385369d78af"></p>

```bash
sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="198.51.100.55" AND action="ALLOWED"
| stats sum(bytes_transferred) by src_ip
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/bb3079ea-a937-4c4c-9eb5-ebad85d16a3b"></p>


<br>
<p>2.6. &nbsp;&nbsp; <em>If you enjoyed today's room, check out the Incident Handling With Splunk room to learn more about analyzing logs with Splunk.</em><br>
<code>No answer needed</code></p>


<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/c88c6087-40d0-4e48-ac20-a9db7fd4f062"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/4710e78c-db64-44b1-a100-909b6041c665"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/92d63afb-00fd-48e5-a354-2145cd201502"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|6       |Easy 🔗 - Phishing - Merry Clickmas   |   1    |      96ᵗʰ    |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells    |   1    |      97ᵗʰ    |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>

<p align="center">Global All Time:     96ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/23e3f2b0-560f-4cfb-b7bc-5fa78788710a"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/3c09a013-4d93-4faa-b297-7709b9871025"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/10721f5c-3afb-4c00-8b52-ed3dd9cd2af0"><br><br>
                  Global monthly:  53,003ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/ac55c469-2223-4ddd-b68b-edadb33cb81c"><br><br>
                  Brazil monthly:     674ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c1ef4a77-50e9-41f4-b8ff-c340bb829d0f"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

