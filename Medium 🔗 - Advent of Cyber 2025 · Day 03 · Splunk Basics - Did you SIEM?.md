<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 3 &nbsp;&nbsp; ·  &nbsp;&nbsp; Splunk Basics - Did you SIEM?</h3>
<p align="center">2025, December 6  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Learn how to ingest and parse custom log data using Splunk. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/splunkforloganalysis-aoc2025-x8fj2k4rqp">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/f8437e99-b000-40ea-b23b-e9afaf2cae9e"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/237d6ff9-bb6f-40d7-9678-599727de9987"></p>

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

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/6f9aeec7-8e6c-4f37-9a88-5379a25700fd"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>On the next page, type <code>index=main</code>c in the search bar to show all ingested logs. Note that we will need to select <code>All time</code> as the time frame from the dropdown on the right of the search bar.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/f970efd7-ec54-49ad-8811-44e49e31e26d"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>After running the query, we will be presented with two separate datasets that have been pre-ingested into Splunk. We can verify this by clicking on the <code>sourcetype</code> field in the fields list on the left of the page.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/f036ee92-bece-41fc-94e4-ec21bb4e97e8"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The two datasets are as follows:<br>

- <code>web_traffic</code>: This data source contains events related to web connections to and from the web server.<br>
- <code>firewall_logs</code>: This data source contains the firewall logs, showing the traffic allowed or blocked. The local IP assigned to the web server is <code>10.10.1.15</code>.<br>

Let's explore the logs and investigate the attack on our servers to identify the culprit.</p>

<br>
<h3>Initial Triage</h3>
<p>Start a basic search across the index using your custom source type <code>web_traffic</code>, using the following query:<br>

<strong>Search query</strong>: <code>index=main sourcetype=web_traffic</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/82b32ef1-5689-4fc5-a884-a69ded102e30"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Let's break down our result for a better understanding:<br>

- <strong>Search query</strong>: This query retrieves all events from the <code>main</code> index that were tagged with the custom source type <code>web_traffic</code>. This marks the beginning of the investigation.<br>
- <strong>Time range</strong>: The time range is currently set to "All time". In security analysis, this range would be tightened (e.g., to the spike window) after initial data loading.<br>
- <strong>Timeline</strong>: This visual histogram shows the distribution of the 17,172 events over time. The graph indicates the successful daily log volume followed by a distinctive traffic spike (a period of high activity, likely the attack window).<br>
- <strong>Selected fields</strong>: These are the fields currently chosen to be displayed in the summary column of the event list (<code>host</code>, <code>source</code>, <code>sourcetype</code>). They represent basic metadata about the log file itself.<br>
- <strong>Interesting fields</strong>: This pane lists all fields that Splunk has automatically extracted or manually added. Fields prefixed with <code>#</code> (e.g., <code>#date_hour</code>) are automatically generated by Splunk's time commands. The presence of <code>user_agent</code>, <code>path</code>, and <code>client_ip</code> confirms the successful parsing of the web log structure.<br>
- <strong>Event details & field extraction</strong>: This section shows the parsed details of a single event with extracted fields like <code>user_agent</code>, <code>path</code>, <code>status</code>, <code>client_ip</code>, and more.<br>

Now that we have an understanding of the Splunk layout and how to read the logs in Splunk. Let's continue our analysis of the logs.</p>

<br>
<h3>Visualizing the Logs Timeline</h3>
<p>Let's chart the total event count over time, grouped by day, to determine the number of events captured per day. This will help us in identifying the day that received an abnormal number of logs.<br>

<strong>Search query</strong>: <code>index=main sourcetype=web_traffic | timechart span=1d count</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/fdbe0df3-58b3-4efb-a2e6-71f91f09bda0"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The above results are now showing the event logs captured per day. This could be interesting, as we can see some days getting a high volume of logs. We can also click on the <code>Visualization</code> tab to examine the graph for better representation, as shown below:</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/11eaef3b-88ff-468f-bc9e-76ebf6c51e6e"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>We can append the <code>reverse</code> function at the end to display the result in descending order, showing the day with the maximum number of events at the beginning.<br>

<strong>Search query</strong>: <code>index=main sourcetype=web_traffic | timechart span=1d count | sort by count | reverse</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/3e967d46-e816-4b08-9b62-cde346a836ea"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>There is a clear period of intense activity during which King Malhare launched his main attack phase.</p>

<br>
<h3>Anomaly Detection</h3>
<p>Now that we have examined the days with the abnormal logs, using the table and the graph, let's use the same search query to examine various fields to hunt for suspicious values. We need to go back to the Events tab to continue.</p>

<br>
<h4>User Agent</h4>

<p>Let's click on the <code>user_agent</code> field in the left panel, as shown below. It will show us the details about the user agents captured so far. </p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/ca4a6d09-80b7-4c75-b14d-3cf6c1a4d50e"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>


<p>Upon closer examination, it becomes clear that, apart from legitimate user agents like Mozilla's variants, we are receiving a large number of suspicious ones, which we will need to investigate further.</p>

<br>
<h4>client_ip</h4>

<p>The second field we will examine is the <code>client_ip</code>, which contains the IP addresses of the clients accessing the web server. We can immediately see one particular IP address standing out, which we will investigate further.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/4622b9a8-9689-4d12-91db-3efefd5d9be8"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<br>
<h4>path</h4>
<p>The third field we will examine is path, which contains the URI being requested and accessed by the client IPs. The results shown below clearly indicate some attacks worth investigating.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/36443c63-9400-4113-95e7-539ce16838de"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<br>
<h3>Filtering out Benign Values</h3>
<p>We know King Malhare's bunnies use scripts and tools, not standard browsers. Let's filter out all standard traffic.<br>

Let's exclude common legitimate user agents. The following query will remove legitimate user agents from the results and only show the suspicious ones, which we will further investigate.<br>

<strong>Search query</strong>: <code>index=main sourcetype=web_traffic user_agent!=*Mozilla* user_agent!=*Chrome* user_agent!=*Safari* user_agent!=*Firefox*</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/fa4d5879-4d86-4e36-936c-3e408520814d"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The output reveals interesting results. By clicking on the <code>client_ip</code> field we can see a single IP address being responsible for all the suspicious user agents. Let's note that down for further investigation and fill in the <code><REDACTED></code> portions of the upcoming queries with that IP.</p>

<br>
<h3>Narrowing Down Suspicious IPS</h3>
<p>In real-world scenarios, we often encounter various IP addresses constantly attempting to attack our servers. To narrow down on the IP addresses that do not send requests from common desktop or mobile browsers, we can use the following query:.<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic user_agent!=*Mozilla* user_agent!=*Chrome* user_agent!=*Safari* user_agent!=*Firefox* | stats count by client_ip | sort -count | head 5</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/82eed845-f6b7-4fad-a16c-52b97872f579"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The result confirms the top IP used by the Bandit Bunnies. In the search query, the <code>-</code> in the <code>sort -count</code> part will sort the result by count in reverse order, it's the same as using the reverse function. Let's pick this IP address and filter out to see what the footprints of the activities captured.</p>

<h3>Tracing the Attack Chain</h3>
<p>We will now focus on the selected attacker IP to trace their steps chronologically, confirming the use of multiple tools and payloads. Don’t forget to replace <code><REDACTED></code> with the IP we noted down previously.</p>

<br>
<h4>Reconnaissance (Footprinting)</h4>
<p>We will start searching for the initial probing of exposed configuration files using the query below:<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic client_ip="<REDACTED>" AND path IN ("/.env", "/*phpinfo*", "/.git*") | table _time, path, user_agent, statu</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/7def4426-f0e1-4f74-8877-a9d65eed20a6"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The result confirms the attacker used low-level tools (<code>curl</code>, <code>wget</code>) and was met with <strong>404</strong>/<strong>403</strong>strong>/<strong>401</strong> status codes.</p>

<br>
<h4>Enumeration (Vulnerability Testing)</h4>
<p>Search for common path traversal and open redirect vulnerabilities.<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic client_ip="<REDACTED>" AND path="*..*" OR path="*redirect*"</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/54d5379b-d471-4557-9577-075f5ca6c53c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The output shows the resources the attacker is trying to access. Let's update the search query to get the count of the resources requested by the attacker. This search query is filtering on the paths that contain either <code>../../</code> or the term redirect in it, as shown below. This is done to look for footprints of path traversal attempts (<code>../../</code>). To, we need to update in the search query to escape the characters like <code>..\/..\/</code>.<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic client_ip="<REDACTED>" AND path="*..\/..\/*" OR path="*redirect*" | stats count by path"</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/e14a447d-7f73-40e9-83d1-2bfb1d2b824f"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>


<p>Quite interesting results. Reveals attempts to read system files (<code>../../*</code>), showing the attacker moved beyond simple scanning to active vulnerability testing.</p>

<br>
<h4>SQL Injection Attack</h4>
<p>Find the automated attack tool and its payload by using the query below:<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic client_ip="<REDACTED>" AND user_agent IN ("*sqlmap*", "*Havij*") | table _time, path, status</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/a4ea1b0e-7065-46df-8e98-6387de4b6695"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Above results confirms the use of known SQL injection and specific attack strings like <code>SLEEP(5)</code>. A 504 status code often confirms a successful time-based SQL injection attack.</p>

<br>
<h3>Exfiltration Attempts</h3>
<p>Search for attempts to download large, sensitive files (backups, logs). We can use the query below:<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic client_ip="<REDACTED>" AND path IN ("*backup.zip*", "*logs.tar.gz*") | table _time path, user_agent</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/6f51b6ef-aad6-41b8-89a5-c2214d70371e"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The results indicate the attacker was exfiltrating large chunks of compressed log files using tools like <code>curl</code>, <code>zgrab</code>, and more. We can confirm the details about these connections in the firewall logs.</p>

<br>
<h3>Ransomware Staging & RCE</h3>
<p>Requests for sensitive archives like <code>/logs.tar.gz</code> and <code>/config</code> indicate the attacker is gathering data for double-extortion. In the logs, we identified some requests related to bunnylock and shell.php. Let's use the following query to see what those search queries are about.<br>

<strong>Search query</strong>: <code>sourcetype=web_traffic client_ip="<REDACTED>" AND path IN ("*bunnylock.bin*", "*shell.php?cmd=*") | table _time, path, user_agent, status</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/9992dcfa-0452-45cd-910e-fcf0692e9388"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Above results clearly confirm a successful webshell. The attacker has gained full control over the web server and is also able to run commands. This type of attack is called Remote code Execution (RCE). The execution of <code>/shell.php?cmd=./bunnylock.bin</code> indicates a ransomware like program executed on the server. </p>

<br>
<h3>Correlate Outbound C2 Communication</h3>
<p>We pivot the search to the <code>firewall_logs</code> using the Compromised Server IP (<code>10.10.1.5</code>) as the source and the attacker IP as the destination.<br>

<strong>Search query</strong>: <code>sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="<REDACTED>" AND action="ALLOWED" | table _time, action, protocol, src_ip, dest_ip, dest_port, reason</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/ad55da8f-6605-4b8b-8a4f-a188d1110669"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>This query proves the server immediately established an outbound connection to the attacker's C2 IP on the suspicious <code>DEST_PORT</code>. The <code>ACTION=ALLOWED</code> and <code>REASON=C2_CONTACT</code> fields confirm the malware communication channel was active.</p>

<br>
<h3>Volume of Data Exfiltrated</h3>
<p>We can also use the sum function to calculate the sum of the bytes transferred, using the bytes_transferred field, as shown below:<br>

<strong>Search query</strong>: <code>sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="<REDACTED>" AND action="ALLOWED" | stats sum(bytes_transferred) by src_ip</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/01e0ce84-d287-4a96-9ae9-bc59d694e18e"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The results show a hugh volume of data transferred from the compromised webserver to C2 server.</p>

<br>
<h3>Conclusion</h3>
<p>

- <strong>Identity found</strong>: The attacker was identified via the highest volume of malicious web traffic originating from the external IP.<br>
- <strong>Intrusion vector</strong>: The attack followed a clear progression in the web logs (<code>sourcetype=web_traffic</code>).<br>
- <strong>Reconnaissance</strong>: Probes were initiated via cURL/Wget, looking for configuration files (<code>/.env</code>) and testing path traversal vulnerabilities.<br>
- <strong>Exploitation</strong>: The use of <code>SQLmap</code> user agents and specific payloads (<code>SLEEP(5)</code>) confirmed the successful exploitation phase.<br>
- <strong>Payload delivery</strong>: The Action on Objective was established by the final successful execution of the command <code>cmd=./bunnylock.bin</code> via the webshell.<br>
- <strong>C2 confirmation</strong>: The pivot to the firewall logs (<code>sourcetype=firewall_logs</code>) proved the post-exploitation activity. The internal, compromised server (<code>SRC_IP: 10.10.1.5</code>) established an outbound C2 connection to the attacker's IP.</p>

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
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?|  1    |      95ᵗʰ    |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas   |   1    |      96ᵗʰ    |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells    |   1    |      97ᵗʰ    |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>


<p align="center">Global All Time:     95ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/2c9368e2-81ef-4908-8a84-0990ed3c351d"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/d9cfc742-7ebf-46fa-9142-5ffdfde5dcee"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/6949e27e-7ac6-4920-bc0f-9d9ee6fec571"><br><br>
                  Global monthly:  44,647ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/9131f25a-1044-4955-9050-802b43579874"><br><br>
                  Brazil monthly:     560ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f192c161-d235-4b16-8f12-1582e3165acd"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

