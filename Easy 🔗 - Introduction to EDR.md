<h1 align="center">Introduction to EDR</h1>
<p align="center">2025, August 28<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>479</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn the fundamentals of EDR and explore its features and working.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/8aef2fd8-b9fd-4862-9c82-f1815a528ba"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/introductiontoedrs">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/aa7e6aca-93b7-42ad-9f22-137cff53f9ba"></p>

<br>

<h2>Task 1 . Introduction</h2>
<p>Endpoint Detection and Response (EDR) is a security solution designed to monitor, detect, and respond to advanced threats at the endpoint level. As a SOC analyst, it is essential for you to understand how the EDR works since it is a widely adopted solution in organizations to protect their endpoints. In this room, we will see how an EDR differs from a traditional antivirus and what data it collects from the endpoints. We will also discuss the detection and response capabilities it provides.</p>

<h3>Learning Objectives</h3>

<p>
  
- Understand the basics of EDR and how it works<br>
- Differentiate EDR from traditional Antivirus solutions<br>
- Examine the architecture of an EDR solution<br>
- Analyze the types of telemetry it collects from endpoints<br>
- Understand the detection and response capabilities of an EDR<br>
- Investigate a realistic alert in the EDR</p>


<h3>Room Prerequisites</h3>
<p>
  
- Basic knowledge of different endpoints (Windows, Linux, Mac) and the common attacks on them<br>
- Awareness of the role of the SOC team</p>

<p><em>Answer the question below</em></p>

<p>1.1. I am all set!<br>
<code>No answer needed</code></p>


<h2>Task 2 . What is and EDR?</h2>
<p>The increase in the use of digital devices is undeniable. Most of the business's core functions rely on the use of these digital devices. Cyber threats, on the other hand, are also increasing day by day. To protect these devices, organizations implement several security measures, most of which are to protect the network on which they operate these digital devices. However, the fast adoption of Remote Work has exposed these devices as they are out of the perimeter protection deployed on the organization's network. <br>

To ensure these endpoint devices are protected even out of the network, we need a security solution that guards all devices in different areas and is capable of fighting advanced threats. Endpoint Detection and Response (EDR) is a security solution that offers deep-level protection for endpoints. No matter where the endpoints are, the EDR will make sure they are monitored constantly and threats are detected.</p>

<p>Below are some of the EDR solutions in the market:<br>

- <a href="https://www.crowdstrike.com/wp-content/uploads/2022/03/crowdstrike-falcon-insight-data-sheet.pdf">CrowdStrike Falcon</a><br>
- <a href="https://sentinelone.com/resources/datasheets/assets/usecase/sentinel-one-active-#page=1">SentinelOne ActiveEDR</a><br>
- <a href="https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint">Microsoft Defender for Endpoint</a><br>
- <a href="https://www.openedr.com/">OpenEDR</a><br>
- <a href="https://docs.broadcom.com/doc/endpoint-detection-and-response-atp-endpoint-en">Symantec EDR</a><br>

Several other EDR solutions are available in the market. Their underlying architecture is mostly similar, but the features may vary.<br>

Let's take a look at the core features of an EDR. We will be using the screenshots from CrowdStrike Falcon EDR to demonstrate the core features of EDR.</p>

<h6>Note: The screenshots used in this task were taken from CrowdStrike Falcon EDR when this room was created.</h6>

<h3>Features of EDR</h3>
<p>There are three main features of an EDR, which can also be referred to as the three pillars of an EDR solution.</p>

<h3>Visibility </h3>
<p>A good analysis often depends on the available level of visibility of the activity. This is one of the features of EDR that makes it unique from other endpoint security solutions. The level of visibility EDR provides is impressive. It collects detailed data from the endpoints, which includes process modifications, registry modifications, file and folder modifications, user actions, and much more. It then presents this information in a very structured format to the analyst. The analyst can see the whole process tree with a complete activity timeline of the sequence of actions. The analyst can also access the historical data of any endpoint for threat hunting or any other purpose. Any detections in the EDR land with a whole context.</p>

<p>The following screenshot shows graphical representation of a process tree. We can see which processes were spawned on the endpoint. Each node represents a process. The lines connecting them represents their relationship. If we click on the + icon given with each process, we will be able to see all the network connections, registry changes, file changes etc. associated with that process. </p>

<br>

<p>Along with the process trees, there are many other features available in the EDRs which maximize the visibility. </p>

<h3>Detection</h3>

<p>The detection feature of EDR wins over traditional detection capabilities. It incorporates signature-based detections as well as behavior-based detections, such as unexpected user activities. With modern machine learning capabilities, it identifies any deviation from the baseline behavior and instantly flags it. It can also detect fileless malware that resides in memory. It also allows us to feed custom IOCs for threat detections.<br>

The following screenshot shows a dashboard of all the detections happening on the different endpoints. Each detection is represented by a row with different fields including the severity of the detection, time, triggering file, hostname, username, and more. The Tactic via Technique field maps the detection with MITRE. Any detection when clicked will show us rich details which helps a SOC analyst during the analysis.</p>

<br>

<h3>Response</h3>
<p>EDR also empowers analysts to take action on detected threats. These actions can be taken at any endpoint within the central EDR console. Imagine getting a detection on the EDR with full-fledged details on when, where, and what happened, and you have to opt for the best possible action for that detection. As an analyst, you may decide to isolate a complete endpoint, terminate a process, or quarantine some files. You can also connect to the host remotely and execute actions independently. You can do this all from within the EDR console.<br>

The following screenshot shows the actions available that can be taken on the host after connecting to it. </p>

<br>

<p>There are several other actions that the analyst can take during the investigation.</p>

<h6>Note: In Task #6, we will be covering the Detection and Response capabilities of an EDR in more detail.</h6>

<p>With advanced visibility, detection, and response, EDR becomes a very powerful tool. However, it's also important to remember that an EDR is a host-only security solution and does not detect network-level threats.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. Which feature of EDR provides a complete context for all the detections?<br>
<code>Visibility</code></p>

<p>2.2. Which process spawned sc.exe?<br>
<code>cmd.exe</code></p>


<h2>Task 3 . Beyond the Antivirus</h2>

<p><em>Answer the questions below</em></p>

<p>3.1. In the given analogy, what presents an AV?<br>
<code>immigration check</code></p>

<p>3.2. Which legitimate process was hijacked by the attacker in the scenario?<br>
<code>svchost.exe</code></p>

<p>3.3. Which security solution might mark this activity as clean?<br>
<code>Antivirus</code></p>


<h2>Task 4 . How EDR works?</h2>

<p><em>Answer the questions below</em></p>

<p>4.1. Which component of the EDR is responsible for collecting telemetry from the endpoints?<br>
<code>Agent</code></p>

<p>4.2. An EDR agent is also known as a?<br>
<code>sensor</code></p>

<h2>Task 5 . EDR Telemetry</h2>

<p><em>Answer the questions below</em></p>

<p>5.1. Which telemetry data helps in detecting C2 communications?<br>
<code>Network Connections</code></p>

<p>5.2. Where are the configuration settings of a Windows system primarily stored?<br>
<code>registry</code></p>

<h2>Task 6 . Detection And Response Capabilities</h2>

<p><em>Answer the question below</em></p>

<p>6.1. Which feature of the EDR helps you identify threats based on known malicious behaviours? <br>
<code>IOC Matching</code></p>

<h2>Task 7 . Investigate and alert on EDR</h2>

<p><em>Answer the questions below</em></p>

<p>7.1. Which feature of the EDR helps you identify threats based on known malicious behaviours?<br>
<code>****.***</code></p>

<p>7.2. What is the absolute path to the downloaded malware on the DESKTOP-HR01 machine?<br>
<code>***************************</code></p>

<p>7.3. What is the absolute path to the suspicious syncsvc.exe on the WIN-ENG-LAPTOP03 machine?<br>
<code>*************************************************</code></p>

<p>7.4. On which URL was the exfiltration attempt being made on WIN-ENG-LAPTOP03?<br>
<code>**********************************************************************</code></p>

<p>7.5. What was UpdateAgent.exe labelled by Threat Intel on DESKTOP-DEV01?<br>
<code>***** ******** ** ******* ****</code></p>

<h2>Task 8 . Conclusion</h2>
<p>Congratulations! We have learned one of the essential tools used in the Security Operations Center (SOC), Endpoint Detection and Response (EDR). As a SOC analyst, we now understand the basic architecture of EDR and its capabilities beyond Antivirus. We explored the detailed telemetry that an EDR provides. We also saw the powerful detection and response capabilities of EDR solutions. Lastly, we practiced investigating some detections on a simulated EDR.<br>

This sets a strong baseline for working with essential security solutions. In the upcoming rooms of this module, we will explore some other security solutions that a SOC analyst works on in a Security Operations Center (SOC).</p>

<p><em>Answer the questions below</em></p>

<p>8.1. Complete the room.<br>
<code>No answer needed</code></p>

<br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/0be8eae5-46a2-4df8-be64-6261f3a193d6"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/ef827cee-45ed-4d03-bd97-a02b3859e3ab"></p>


<br>
<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 85   | 479      |     113ʳᵈ    |      5ᵗʰ     |     249ᵗʰ   |     5ᵗʰ    | 123,012  |    930    |    73     |

</div>


<p align="center">Global All Time:   113ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/de816e6f-3f61-4e1f-ba47-8a8b293d804b"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/c3a68ff1-1df1-454d-a574-e0760df4f2e9"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b7db00c9-a14c-46ad-a844-46f7a0aa5877"><br>
                  Global monthly:    249ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/0a49434d-0263-46b6-a069-7cb2b3e195ba"><br>
                  Brazil monthly:      6ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/81aab0e4-cf1b-4325-917c-2fcefd1a610c"><br>

<br>
<br>

<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
