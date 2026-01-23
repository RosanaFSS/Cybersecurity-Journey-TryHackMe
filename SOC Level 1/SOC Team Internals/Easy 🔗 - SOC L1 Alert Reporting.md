
<p align="center">April 17, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{346}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/cfa31fa8-1653-4223-a087-dbe1ad1a7623" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/dbaabd6d-47b5-4cd6-9800-eb50114e599d" alt="streak"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{SOC L1 Alert Reporting}}$$</h1>
<p align="center"><em>Learn how to properly report, escalate, and communicate about high-risk SOC alerts.</em>.<br>
It is classified as an easy-level challenge.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/socl1alertreporting">here</a>.</p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/bd750bca-8ef5-41a0-9186-eabaca1d64b0"> </p>


<br>
<br>

<h2>Task 1 . Introduction</h2>

<p>During or after alert triage, L1 analysts may be uncertain about how to classify the alert, requiring senior support or information from the system owner. Also, L1 may deal with real cyberattacks and breaches that need immediate attention and remediation actions. This room covers these cases by introducing three new terms: alert reporting, escalation, and communication.</p>

<h3>Learning Objectives</h3>
<p>- Understand the need for SOC alert reporting and escalation<br>
- Learn how to write alert comments or case reports properly<br>
- Explore escalation methods and communication best practices<br>
-Apply the knowledge to triage alerts in a simulated environment<br>
-Feel more confident in SOC Simulator and during SAL1 certification</p>

<h3>Prerequesites</h3>
<p>- Complete the preceding SOC L1 Alert Triage room<br>
- Have a basic understanding of common attacks<br>
- Know the responsibilities of SOC L1 analysts</p>

<h3>SOC Dashboard</h3>
<p>Continue your journey in the SOC dashboard! This time you will need it to write professional reports and practice in escalating the alerts. Open the attached website in a separate window by clicking on the SOC dashboard link below and move on to the next task!</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>I am ready to start!</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<p>Accessed the <code>SOC dashboard</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/06d93ca4-a521-4440-8df3-a56755ca3815)


<br><br>

<h2>Task 2 . Alert Funnel</h2>

<p>In the previous room, you learned how to classify and triage the alerts. But you might be curious about what happens next. How does your triage help prevent threats and stop breaches? This is a whole new topic that this room will cover soon, but for now, let's recall the path of the alerts.<br><br>

First, L1 analysts receive the alerts in a SIEM, EDR, or a ticket management platform. Most of the alerts are closed as False Positives or are handled on L1 level, but complex and threatening ones are sent to L2 that remediate most breaches. And to send the alerts further, you need to learn three new terms: reporting, escalation, and communication.</p>

<br>

<h3>Alert Reporting</h3>
<p>Before closing or passing the alert to L2, you might have to report it. Depending on team standards and alert severity, instead of a short alert comment, you can be required to document your investigation in detail, ensuring all relevant evidence is included. This is especially important for True Positives, which require escalation.</p>

<h3>Alert Escalation</h3>
<p>If the True Positive alert requires additional actions or deeper investigation, escalate it to the L2 analyst for further review following the agreed procedures. That's where your alert report comes in handy since L2 will use it to get the initial context and spend less on the analysis from scratch.</p>

<h3>Communication</h3>
<p>You may also need to communicate with other departments during or after the analysis. For example, ask the IT team if they confirm granting administrative privileges to some users or contact HR to get more information about the newly hired employee.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 2.1. <em>What is the number of alerts you see in the SOC dashboard?</em><br><a id='2.1'></a>
>> <strong><code>Alert Escalation</code></strong><br>
<p></p>

<br>


> 2.2. <em>What is the process of formally describing alert details and findings?</em><br><a id='2.2'></a>
>> <strong><code>Alert Reporting</code></strong><br>
<p></p>

<br><br>

<h2>Task 3 .  Reporting Guide</h2>

<p>Before we move on, it is essential to clarify why anyone would want L1 analysts to write reports in addition to marking them as True or False Positives and why this topic can not be underestimated. Having L1 analysts write alert reports serves several key purposes:</p>

<br>

![image](https://github.com/user-attachments/assets/e49f94a0-0100-446a-9c11-5a4f9ee749aa)

<br>

<h3>Report Format</h3>
<p>Imagine yourself as an L2 analyst, a DFIR team member, or an IT professional who needs to understand the alert. What would you want to see in the report? We recommend you follow the Five Ws approach and include at least these items in the report:<br>

- Who: Which user logs in, runs the command, or downloads the file<br>
- What: What exact action or event sequence was performed<br>
- When: When exactly did the suspicious activity start and ended<br>
- Where: Which device, IP, or website was involved in the alert<br>
- Why: The most important W, the reasoning for your final verdict</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>According to the SOC dashboard, which user email leaked the sensitive document?</em><br><a id='3.1'></a>
>> <strong><code>m.boslan@tryhackme.thm</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/f594486a-ff9f-47d2-8cd5-156ee659ac50)


<br>


> 3.2. <em>Looking at the new alerts, who is the "sender" of the suspicious, likely phishing email?</em><br><a id='3.2'></a>
>> <strong>support@microsoft.com</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/738bac99-9328-435a-8cc6-915376c1aaa5)

<br>


> 3.3. <em>Open the phishing alert, read its details, and try to understand the activity.Using the Five Ws template, what flag did you receive after writing a good report?</em>Hint : <em>See previously closed alerts for reference on how to write alert reports.</em><br><a id='3.3'></a>
>> <strong>THM{nice_attempt_faking_microsoft_support}</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/7aabce0d-d1a7-467c-b164-cb340c36e680)



<br><br>

<h2>Task 4 . Escalation Guide</h2>
<p>After you have made a verdict and written your alert report, you must choose whether to escalate the alert to L2. Again, the answer may differ from team to team, but the following recommendations would generally fit most SOC teams. You should escalate the alerts if:<br>

The alert is an indicator of a major cyberattack requiring deeper investigation or DFIR<br>
- Remediation actions like malware removal, host isolation, or password reset are required<br>
- Communication with customers, partners, management, or law enforcement agencies is required<br>
- You just do not fully understand the alert and need some help from more senior analysts</p>

<h3>Escalation Steps</h3>
<p>To escalate the alert, in most cases, all you have to do is to reassign the alert to the L2 on shift and ping them in corporate chat or in person. In some teams though, you may be required to create a formal written escalation request with dozens of required fields.<br><br>

No matter what the agreements are, L2 will eventually receive the ticket from you, read your report, and contact you in case of any questions. Once everything is clear, the L2 analyst will typically research the alert details further, validate if the alert is indeed a True Positive, communicate with other departments if needed, and, for major incidents, start a formal Incident Response process.</p>

<h4>SOC Dashboard Escalation Procedure</h4>
<p>1. Write an alert report and provide your verdict; move the alert to In Progress status<br>
2. Assign the alert to your L2 on shift. L2 will receive a notification and start from your report</p>

<h3>Escalating Threats to L2</h3>

![image](https://github.com/user-attachments/assets/76a65a4b-bd07-4e8f-b2da-c4ea0f9734ff)

<h3>Requesting L2 Support</h3>

![image](https://github.com/user-attachments/assets/08a6489b-87cb-4acf-8b87-930881d6a3e6)

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 4.1. <em>Who is your current L2 in the SOC dashboard that you can assign (escalate) the alerts to?</em><br><a id='4.1'></a>
>> <strong><code>E.Fleming</code></strong><br>
<p></p>

<br>


> 4.2. <em>What flag did you receive after correctly escalating the alert from the previous task to L2? Note: If you correctly escalated the alert earlier, just edit the alert and click "Save" again</em><br><a id='4.2'></a>
>> <strong><code>THM{good_job_escalating_your_first_alert}</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/df6ad5b6-f1a8-479c-88e9-90b3668c23cf)

<br>

> 4.3. <em>Now, investigate the second new alert in the queue and provide a detailed alert comment. Then, decide if you need to escalate this alert and move on according to the process. After you finish your triage, you should receive a flag, which is your answer!</em>Hint : <em>You should add a correct comment, verdict, status, and assignee.</em><br><a id='4.3'></a>
>> <strong><code>THM{looks_like_webshell_via_old_exchange}</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/534f43f5-792f-4536-9ba0-fc4ada6ba563)



<br><br>

<h2>Task 5 . SOC Communication</h2>
<p>The escalation and reporting topics should sound straightforward and logical to you. But, as always, it's easier said than done, and you should be prepared for unexpected scenarios and know what to do in critical cases. In the best scenario, the SOC team has its own Crisis Communication procedures - the guides and processes to help you and your teammates resolve the issues. If not, you are advised to read the cases below and be prepared to handle them effectively.</p>


<h3>Initial Actions</h3>
<p>The initial steps are designed to ensure that you take ownership of the assigned alert and avoid interfering with alerts being handled by other analysts, and confirm that you are fully prepared to proceed with the detailed investigation. You achieve it by first assigning the alert to yourself, moving it to In Progress, and then familiarising yourself with the alert details like its name, description, and key indicators.</p>

<h3>Communication Cases</h3>
<p>This is the most complex step, requiring you to apply your technical knowledge and experience to understand the activity and properly analyse its legitimacy in SIEM or EDR logs. To support L1 analysts with this step, some teams develop Workbooks (also known as playbooks or runbooks) - instructions on how to investigate the specific category of alerts. If workbooks are not available, below are some key recommendations:<br>
<ol type="1. ">
    <li>You need to escalate an urgent, critical alert, but L2 is unavailable and does not respond for 30 minutes.
Ensure you know where to find emergency contacts. First, try to call L2, then L3, and finally your manager.</li>
    <li>The alert about Slack/Teams account compromise requires you to validate the login with the affected user.
Do not contact the user through the breached chat - use alternative contact methods like a phone call.</li>
    <li>You receive an overwhelming number of alerts during a short period of time, some of which are critical.
Prioritise the alerts according to the workflow, but inform your L2 on shift about the situation.</li>
    <li>After a few days, you realise that you misclassified the alert and likely missed a malicious action.
Immediately reach out to your L2 explaining your concerns. Threat actors can be silent for weeks before impact.</li>
    <li>You can not complete the alert triage since the SIEM logs are not parsed correctly or are not searchable.
Do not skip the alert - investigate what you can and report the issue to your L2 on shift or SOC engineer.</li>
</ol></p>

<br>

<h3>Communication By L2</h3>

![image](https://github.com/user-attachments/assets/fc8e25d9-d408-48a0-9f4e-52c712be2fdf)



<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 5.1. <em>Should you first try to contact your manager in case of a critical threat (Yea/Nay)?</em><br><a id='5.1'></a>
>> <strong><code>Nay</code></strong><br>
<p></p>

<br>


> 5.2. <em>Should you immediately contact your L2 if you think you missed the attack (Yea/Nay)?</em><br><a id='5.2'></a>
>> <strong><code>Yea</code></strong><br>
<p></p>


<br><br>

<h2>Task 6 . Conclusion</h2>
<p>Great job learning three important SOC skills: alert reporting, escalation, and communication. These skills are essential for any L1 analysts: Alert reporting helps to preserve and provide activity context for L2, escalation ensures threats are remediated in time, and communication makes the coordination between SOC and other departments clear and effective.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 6.1. <em>I am ready to move on!</em><br><a id='6.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/e0a94ad4-d6f3-4497-88e3-3ee1b8dba4a0"><br>
<img width="900px" src="https://github.com/user-attachments/assets/f0cf789a-cca0-430e-a4a4-e277a0a06acf"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">


| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |   Brazil     |    Global   |   Brazil   |          | Completed |           |
| April 17, 2025    |   346    |     271ˢᵗ    |     6ᵗʰ      |      40ᵗʰ   |     2ⁿᵈ    |  95,513  |    672    |    59     |

</div>

<br>


<p align="center"> Global All Time: 271ˢᵗ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/c5ab5e94-44fa-4b15-8cd1-81b443f425d7"> </p>

<p align="center"> Brazil All Time:    6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/639c2124-98b9-4451-aac5-a4e50a016233"> </p>

<p align="center"> Global monthly:     40ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/277e5955-486a-4250-a1e7-005e49f973f8"> </p>

<p align="center"> Brazil monthly:      2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/0e90fcab-7bde-4922-833b-4eea5e6c352b"> </p>


<br>

<p align="center">Weekly League: Silver 3ʳᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/30a85e18-496e-4088-b525-715c62222b17"> </p>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and  <a href="https://tryhackme.com/p/TactfulTurtle">TactfulTurtle</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 
