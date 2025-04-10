
<p align="center">April 10, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{339}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="160px" src="https://github.com/user-attachments/assets/f091ab8b-6389-45e2-a36d-01b50b863eeb"></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Servidae: Log Analysis in ELK}}$$</h1>


<p align="center">"Analyze the logs of an affected workstation to determine the attacker's indicators of compromise." <br>
It is classified as an easy-level walkthrough room.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/servidae">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/04406bd9-e5fa-4974-adf5-38098e180fcc"> </p>

<br>
<br>

<h2>Task 1 . Introduction</h2>

<p>In this room, we will analyze the log data from a compromised workstation using the Kibana interface. Within this room's tasks, we will explore the components of the Elastic (ELK) Stack and gain insights into the various search and filter functions available in Kibana. Our ultimate goal will be to decipher the actions executed by a malicious actor on the affected system. Additionally, to ensure that our findings are useful in practice, we will map indicators of compromise (IOCs) identified in the logs to relevant tactics and techniques outlined in the MITRE ATT&CK framework.</p>

<h3>Room Objectives</h3>

<p>.  Get familiar with the Elastic (ELK) Stack and its components.<br>
.  Understand the significance of log data analysis in detecting and investigating security incidents.<br>
.  Get introduced to Kibana and its key functionalities for data analysis, visualization, and exploration.<br>
.  Gain hands-on experience with analyzing log data to identify real-world security threats and anomalies.</p>

<h3>Room Prerequisites</h3>

<p>.  General familiarity with Windows - check out the Windows Fundamentals module.<br>
.  General context on SIEMs and how they're used - the Introduction to SIEM is an excellent room for this.</p>

<p>Once you are ready to go, click on the Start Machine button attached to this task! I recommend starting it now, as Elasticsearch may take up to 5 minutes to fully start up.</p><br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Click and continue learning!</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . The Elastic Stack</h2>

<h3>The Elastic (ELK) Stack</h3>
<p>The Elastic Stack (commonly and formerly known as ELK Stack) is a collection of open-source software components developed by Elastic. The "stack" mainly consists of three core products: Elasticsearch, Logstash, and Kibana. When used together, the Elastic Stack becomes a very versatile toolset that can be used for a wide range of use cases, including log analysis, application performance monitoring, security analytics, and business intelligence. The stack's components are designed to work together seamlessly, allowing for the simplified collection, processing, and analysis of data from various sources.<br>

To further our understanding, we can discuss each component in a bit more detail:</p>

![image](https://github.com/user-attachments/assets/e1726518-236e-46a9-95f4-828410cbbb12)

<h3>Elasticsearch</h3>
<p>As the central component of the Elastic Stack, Elasticsearch is an open-source, distributed search and analytics engine designed for storing and indexing large volumes of data. Its highly scalable system can store and search various data types, including structured, unstructured, and semi-structured data. Elasticsearch is built on top of Apache Lucene, an open-source search engine library, and provides a simple REST API for indexing, searching, and analyzing data.

In a typical SOC environment, an analyst could use Elasticsearch to store and index security logs, such as firewall logs, for fast searching and analysis.</p>

<h3>logstash</h3>
<p>Logstash is a data ingestion and processing tool primarily used to collect, process, and transform data from various sources and prepare it for storage in Elasticsearch or other systems. For example, Logstash can ingest and parse logs from multiple sources and systems and then send the data to Elasticsearch for indexing and storage.<br>

Logstash is designed to handle various data types, including logs, metrics, events, and other structured or unstructured data. It provides an extensive collection of input, filter, and output plugins that can be used to collect data from many sources, parse and transform it, and then send it to various destinations.<br>

In the SOC environment example, an analyst could use Logstash to parse, transform, and standardize security logs from different antivirus and EDR solutions running in the enterprise.</p>

<h3>Kibana</h3>
<p>Kibana is the interactive graphical and visual front-end powering the Elastic Stack. Kibana provides a user-friendly interface that allows users to create interactive dashboards, visualizations, and reports based on the data stored in Elasticsearch. Along with the ability to search and filter log events, Kibana supports a variety of charts for reporting and visualization, including line charts, bar charts, pie charts, heat maps, and many others.<br>

Using Kibana as an interactive interface for data stored within Elasticsearch lets you quickly gain insights and find patterns. Combined with the rest of the Elastic Stack, Kibana is a crucial solution for analyzing and making sense of large volumes of data.<br>

In a SOC environment, Kibana would be the front-end interface for visualizing and monitoring security events in real time, such as live graphs of network traffic, top sources of security alerts, or a map showing the geolocation of potentially malicious IP addresses.</p>


<h3>Beats</h3>
<p>Using Beats is not mandatory in the Elastic Stack, but they can be crucial in providing efficient and secure data collection capabilities. Beats are lightweight data "shippers" that collect various types of data from different sources (endpoints) and can then forward that data directly to Elasticsearch or Logstash for further processing. Organizations can tailor various Beats to specific use cases, such as collecting system logs, network traffic data, or metrics from servers and applications.<br>

Beats have a smaller footprint than Logstash, making them more suitable for simple use cases or where resource usage is a concern, such as IoT devices or smaller systems. Logstash, on the other hand, is a more robust and complex tool for processing and transforming data, making it more suitable for complex use cases where data requires significant transformation before being stored or analyzed.<br>

Now that we better understand the main components that make up the Elastic Stack, let's move on to a much more practical hands-on scenario!</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 2.1. <em>What is the name of the open-source search engine library that Elasticsearch is built on?</em><br><a id='2.1'></a>
>> <strong><code>Apache Lucene</code></strong><br>
<p></p>

<br>

> 2.2. <em>Which component of the Elastic Stack would you use to perform advanced filtering and processing of data before it gets stored?</em><br><a id='2.2'></a>
>> <strong><code>Logstash</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 3 . A Compromised Workstation: Scenario</h2>
<h3>A compromised Workstation: Scenario</h3>
<p>Bill Smith, a senior Finance Executive at Servidae Industries, stated that he received an email from an unknown sender containing a PDF file attachment that required his action. At first glance, this email appeared legitimate, and he downloaded and opened it without any suspicion. After some time, Bill noticed his computer was acting abnormally and contacted IT Support, claiming that his workstation was slow and freezing up intermittently. Soon after, security alerts indicated suspicious network activity and unauthorized commands executed on Bill's workstation.<br>

A copy of the security alert from the organization's Endpoint Detection & Response (EDR) solution reads:<br>

This is an automated security alert generated by EndDefender EDR. Suspicious network activity and potential remote access were detected on workstation SERVIDAE-BOB-FIN-04 within the specified time range of: May 11, 2023 @ 18:45:00.000 to May 11, 2023 @ 19:01:00.000.<br>

As a SOC Analyst at Servidae Industries, it's up to you to investigate the security alert by reviewing the logs to identify the cause and nature of the suspicious activity on Bill's computer. Fortunately, the organization recently implemented an Elastic Stack solution, and an Elastic Agent was installed to collect logs from Bill's workstation. We have access to the Kibana dashboard, which contains logs from the time of the incident. Let's walk through the investigation and determine if there were any signs of account compromise or malicious user activity.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>I'm ready to investigate!</em><br><a id='3.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 4 . Kibana: Basics</h2>

<h3> Accessing Kibana</h3>
<p>We're now ready to access our Kibana dashboard. Ensure you've already clicked Start Machine in the first task. You can now start the AttackBox by pressing the Start AttackBox button on the top-right of this room.<br>

Navigate to http://TargetIP in the AttackBox's web browser.</p>

<p>You should see the Elastic login page. Please log in using the following credentials:<br>

.  Username: elastic<br>
.  Password: Redacted</p>

![image](https://github.com/user-attachments/assets/c9f52880-fae0-4fa9-a95b-ae25dec6c875)

<br>

<p>If you see a Bad Gateway response, give the system more time to start up Elasticsearch and Kibana. It can typically take up to 5 minutes to start each service.</p>


<h3>Discover</h3>
<p>By default, you'll be directed to the home dashboard, which displays several options for managing the Elastic Stack and integrations. Kibana is an incredibly powerful visualization tool, and we can't cover everything it offers in this room. To remain focused on our investigation, head over to the Discover page, which is found by clicking the left-hand menu icon and selecting Discover under the Analytics tab.</p>

<br>

![image](https://github.com/user-attachments/assets/05bd2f03-721d-4978-816e-f8972facbffd)

<br>


<p>The Discover tab in Kibana is a user interface that allows you to explore, search, and analyze data in real time. It is a powerful tool that helps you quickly and easily find patterns, anomalies, and trends based on log data. To accomplish this, you can search for specific terms, fields, or patterns in the data and add numerous filters to narrow down the results based on criteria such as time range, source, or type.</p>


<h3>Time Filter</h3>
<p>Systems and endpoints produce a massive amount of logs, so it's crucial to use filters to examine them efficiently. Kibana's time filter, for starters, enables you to narrow the records to a specific time range, making it easier to identify the events leading up to and during the incident.<br>

Note: By default, Kibana uses your browser's local time to determine how to present log events. To achieve consistency with this walkthrough, please ensure your Timezone in Kibana is set to Europe/London.<br>

You can edit the timezone settings here: http://TargetIP/app/management/kibana/settings?query=time+zone</p>


<br>

![image](https://github.com/user-attachments/assets/18ecc219-3b7c-407c-bdb6-e8eebf2e2a18)

<br>

<p>For this investigation, our team's alert mentioned that the incident occurred on May 11, 2023, roughly between 18:45-19:01. Let's filter the dashboard to only include logs within that period.<br>

First, click on the Date quick select icon:</p>

<br>

![image](https://github.com/user-attachments/assets/3bdf7153-3c83-4c17-b520-8f44651093d8)

<br>

<p>By default, Kibana always shows logs from the last 15 minutes. Click the Absolute tab from the date window that expands. You can then select the Start date and time through the calendar and time UI or by typing in the date under the Start date text field. Set this to May 11, 2023 @ 18:45:00.000.</p>

<br>

![image](https://github.com/user-attachments/assets/f69b9ce4-d6d4-402d-b0f4-01a88ce33952)

<br>

<p>Once set, click on the now button and do the same thing, this time setting an Absolute date and time of May 11, 2023 @ 19:01:00.000.</p>

<br>

![image](https://github.com/user-attachments/assets/1212f3f8-e5cd-46b6-a5d5-1b0e1592e19c)

<br>

<p>Click the green Update button, and you should now see some logs and metrics appearing!<br>

That's a great start; we've narrowed our search to the dates and times we are interested in.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 4.1. <em>Update the date and time filter as specified. How many total hits were captured within the selected time period?</em> Hint : <em>The top left of the green histogram chart shows the total number of log events (hits) that occurred within the specified time range.</em><br><a id='4.1'></a>
>> <strong><code>920</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/64fd36b9-0cb2-49d9-adc6-432a695f22bf)


<br>
<br>

<h2>Task 5 . Kibana: Fields and Values</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 5.1. <em>Look at the Top values under the destination.ip field. Which IP address stands out?</em> Hint : <em>Most of the top 5 values are from within the same network or localhost. There is one external IP address that stands out.</em><br><a id='5.1'></a>
>> <strong><code>84.237.252.156</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/0d3892c2-4677-44a8-8908-c18aadb2d633)

<br>

<br>

> 5.2. <em>Use an IP address lookup tool (such as iplocation.io). What country does this IP address originate from?</em> Hint : <em>Paste the IP address into a lookup tool and check the Country or Country Name field in the response.</em><br><a id='5.2'></a>
>> <strong><code>Latvia</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/89a97f98-0d90-43d8-8f9d-87f4287cf7ad)


<br>

![image](https://github.com/user-attachments/assets/0dce833c-6cb9-4bd9-9147-b7aed427f8c9)

<br>

<br>

> 5.3. <em>Which process name is running the most frequently on the compromised workstation?</em> Hint : <em>Look under the Top Values of the process.name field.</em><br><a id='5.2'></a>
>> <strong><code>curl.exe</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/6b048f2e-0a71-4777-bc3f-ceccf3a899f9)

<br>

![image](https://github.com/user-attachments/assets/cb75383f-fcf7-400b-8cc5-08ec4a17f988)

<br>
<br>
<h2>Task 6 . Kibana: Sorting and Filtering</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 6.1. <em>What was the process ID (PID) of the potentially malicious PowerShell script?</em> Hint : <em>You can find this information under the "message" field or the "process.pid" field on the third page.</em><br><a id='6.1'></a>
>> <strong><code>6712</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/e16e9620-5efb-4b78-b7b9-e53b816d9c67)

<br>

![image](https://github.com/user-attachments/assets/1ea0afd8-420d-4147-a586-e5be795b3094)


<br>

![image](https://github.com/user-attachments/assets/ce6b945e-8af7-449d-b24a-6b149534ec5d)


<br>

![image](https://github.com/user-attachments/assets/67e96db6-cca5-4b78-b040-e1d8e2d31731)

<br>

![image](https://github.com/user-attachments/assets/83718ca2-e50b-4125-a245-c54022cf2ae6)

<br>

![image](https://github.com/user-attachments/assets/d468fa39-8a82-4ffc-a5b6-5b42a420cc99)

<br>

![image](https://github.com/user-attachments/assets/23d225e4-ee8f-4f18-b9b1-365b3bc7aac0)


<br>

![image](https://github.com/user-attachments/assets/6ab380eb-2fc7-4730-b6c7-0661ec587a91)


<br>

> 6.2. <em>What was the parent process name of the process that spawned powershell.exe?</em> Hint : <em>Check under "process.parent.name".</em><br><a id='6.2'></a>
>> <strong><code>explorer.exe</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/2a5c9f06-9177-425d-8c17-91ecb74fc709)

<br>

![image](https://github.com/user-attachments/assets/d510db38-8930-4c69-ae72-e0c0d9eaaf00)

<br>
<br>
<h2>Task 7 . Indicator of Compromise: Discovery</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 7.1. <em>What is the domain name of the attacker's server hosting the winPEAS executable?</em>Hint : <em>You can find this in the "-Uri" argument of the PowerShell command.</em><br><a id='7.1'></a>
>> <strong><code>evilparrot.thm</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/df6329e4-5341-4e4c-b31b-d40a5d8262fa)

<br>

![image](https://github.com/user-attachments/assets/47b734eb-677d-4b8c-8191-123dc7f039bc)

<br>

> 7.2. <em>What is the full path of the HKEY_LOCAL_MACHINE registry entry that was queried?</em>Hint : <em>Check under the process.command_line field! Ensure you're looking at the correct registry tree..</em><br><a id='7.2'></a>
>> <strong><code>HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/6c1c04b1-8fe5-4429-8859-23051ee18c8d)

<br>
<br>
<h2>Task 8 . Indicator of Compromise: Privilege Escalation</h2>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 8.1. <em>What is the name of the malicious .msi file?</em>Hint : <em>Expand the event logs to see what was run. The file name was specified in the -OutFile argument of the PowerShell cmdlet.</em><br><a id='8.1'></a>
>> <strong><code>adminshell.msi</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/e1dce8fa-d6b2-4c9f-8252-6989fb638d6c)


<br>
<br>
<h2>Task 9 . Indicator of Compromise: Persistence</h2>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 9.1. <em>What is the name of the user account that the attacker created to maintain privileged access?</em>Hint : <em>The syntax for this command is typically "net user [username] [password]".</em><br><a id='9.1'></a>
>> <strong><code>backdoor</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/6ffd0734-7215-4ba9-8ade-3422e3379ebe)

<br>

![image](https://github.com/user-attachments/assets/e12864ca-d7ae-4f39-ac83-78d9e8fbbd47)

<br>

![image](https://github.com/user-attachments/assets/927557a8-f796-426a-8f1b-27bf272c30e2)


<br>

> 9.2. <em>What is the flag sent via cURL requests to the evilparrot.thm server?</em>Hint : <em>The flag can be found in the URL parameter of the HTTP request. The URL parameters follow the "?" character in the URL.</em><br><a id='9.1'></a>
>> <strong><code>THM{C4N_y0U_h34r_m3}</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/7e9ad464-5dc5-4dc9-bada-8beae4a01867)

<br>

> 9.3. <em>What is the name of the registry value that the attacker added?</em>Hint : <em>In the "reg add" command, the "/v" flag is used to specify the name of the registry value being added or modified.</em><br><a id='9.1'></a>
>> <strong><code>BackdoorShell</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/d6440f43-5085-49df-9995-0ec1463558c1)


<br>
<br>
<h2>Task 10 . Indicator of Compromise: Lateral Movement</h2>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 10.1. <em>What was the password that the attacker used to access Bill's user account on the internal payroll website?</em>Hint : <em>The PHPSESSID KQL query mentioned earlier may come in handy here.</em><br><a id='10.1'></a>
>> <strong><code>Password123!</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/d6c4bc7a-142c-4135-957a-7b345485ecbe)


<br>

> 10.2. <em>What flag was included within the HTTP requests during the attacker's successful logins?</em>Hint : <em>Check the request parameters for the flag.</em><br><a id='10.2'></a>
>> <strong><code>THM{1m_1N_Y0ur_P4YR0LL}!</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/5a1b480e-84bd-4eea-a38f-a1ea757c0eae)

<br>

> 10.3. <em>What was the session cookie value that the attacker included in the cURL request at 18:58:08.001?</em>Hint : <em>PHPSESSID=*******</em><br><a id='10.3'></a>
>> <strong><code>bank-details.csv</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/4ed938a1-a990-4e4d-8f65-f0daeb33fefb)

<br>

> 10.4. <em>What is the name of the sensitive file that the attacker downloaded?</em>Hint : <em>PHPSESSID=*******</em><br><a id='10.4'></a>
>> <strong><code>dt5qhq423goknmq269rg1tal1a</code></strong><br>
</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/a50ed049-cba5-4737-8d99-8c83f9c70894)

<br>
<br>
<h2>Task 11 . Conclusion</h2>

<h3>Conclusion</h3>
<p>To summarize our analysis, we identified several indicators of compromise on Bill's workstation. We mapped several of these log events to common tactics and techniques conducted by threat actors. Through a comprehensive exploration of search and filter functions in Kibana, we successfully deciphered the actions performed by a malicious actor on the compromised system.

We gained practical insights into the attacker's tactics and techniques and enhanced our understanding of real-world cyber security incident scenarios. This exercise highlighted the significance of log analysis and its role in detecting and mitigating security incidents, reinforcing the importance of continuous monitoring and analysis of log data to fortify our defences against malicious actors.</p>

<br>

<h3>Next Steps</h3>
<p>After completing the log analysis and gaining valuable insights into the actions of the malicious actor, it is essential to highlight that the analysis phase is just one component of the broader incident response process. Typically, the remaining incident response process involves additional crucial steps that are beyond the scope of this room but equally as important:<br>

.  Containment: Isolating the affected system or network segment to prevent further damage.<br>
.  Eradication: Removing the malicious presence from the compromised system.<br>
.  Recovery: Restoring the system or network to its normal functioning state.<br>
.  Post-Incident Activity: Assessing the incident, identifying root causes, documenting lessons learned, and implementing security enhancements.<br><br>

The Computer Security Incident Handling Guide by NIST (National Institute of Standards and Technology) is a fantastic resource for in-depth guidelines and best practices for effectively responding to computer security incidents.</p>

<h3>Further Research</h3>
<p>.  elastic.co/elastic-stack: The Elastic Stack's official website.<br>
.  ECS Field Reference: ECS (Elastic Common Schema) field reference guide.<br>
.  attack.mitre.org: The official website of the MITRE ATT&CK framework.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 11.1. <em>Click and continue learning!</em><br><a id='11.1'></a>
>> <strong><code>Click and continue learning!</code></strong><br>
<p></p>

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/0942f634-b12f-43f2-953b-9a544a6fdd13"><br>
<img width="900px" src="https://github.com/user-attachments/assets/b7577cee-53ae-443e-8284-577379e50948"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 10, 2025    | 339      |     298ᵗʰ    |        8ᵗʰ   |    257ᵗʰ    |     2ⁿᵈ    |  92,366  |       653 |   59      |

</div>

<br>


<p align="center">Weekly League: Bronze 7ᵗʰ<br><br><img width="300px" src="https://github.com/user-attachments/assets/e08f6039-88ca-4e21-8ec9-a29e1104081a"> </p>


<br>

<p align="center"> Global All Time: 298ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/1a765417-841e-4e48-98f0-4fdd634780e7"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/6b620e38-c130-4f22-8b13-eea6b36e79d1"> </p>

<p align="center"> Global monthly: 257ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/0b936b49-5462-42fc-88fa-0a0e361f18bf"> </p>

<p align="center"> Brazil monthly: 2ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/9314c3ba-1011-4199-9dfd-1866bee6ba71"> </p>


<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 
