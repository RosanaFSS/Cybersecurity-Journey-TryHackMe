
<p align="center">April 17, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{346}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/dbaabd6d-47b5-4cd6-9800-eb50114e599d" alt="streak"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{SOC L1 Reporting}}$$</h1>
<p align="center"><em>Learn how to properly report, escalate, and communicate about high-risk SOC alerts.</em>.<br>
It is classified as an easy-level challenge.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/socl1alertreporting">here</a>.</p>

<p align="center"> <img width="1000px" src=""> </p>

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
>> <strong>___</code></strong><br>
<p></p>

<br>


<br><br>

<h2>Task 4 . Alert Prioritisation</h2>
<p>Okay, you can now read and understand the alert. What's next? Recall the second task, where you see hundreds of alerts but have to choose which to pick up first. The process of deciding which to take is called Alert Prioritisation, and it is crucial to ensure timely detection of a threat, especially with many alerts in the queue.</p>


<h3>Picking the Right Alert</h3>
<p>Every SOC team decides on its own prioritisation rules and usually automates them by setting the appropriate alert sorting logic in SIEM or EDR. Below, you may see the generic, simplest, and most commonly used approach:<br>
<ol type="1. ">
    <li><code>Filter the alerts</code> | Make sure you don't take the alert that other analysts have already reviewed, or that is already being investigated by one of your teammates. You should only take new, yet unseen and unresolved alerts.</li>
    <li><code>Sort by severity</code> | Start with critical alerts, then high, medium, and finally low. This is because detection engineers design rules so that critical alerts are much more likely to be real, major threats and cause much more impact than medium or low ones.</li>
    <li><code>Sort by time</code> | Start with the oldest alerts and end with the newest ones. The idea is that if both alerts are about two breaches, the hacker from the older breach is likely already dumping your data, while the "newcomer" has just started the discovery.</li>
</ol></p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 4.1. <em>Should you first prioritise medium over low severity alerts? (Yea/Nay)</em><br><a id='4.1'></a>
>> <strong><code>Yea</code></strong><br>
<p></p>

<br>

> 4.2. <em>Should you first take the newest alerts and then the older ones? (Yea/Nay)</em><br><a id='4.2'></a>
>> <strong><code>Nay</code></strong><br>
<p></p>

<br>

> 4.3. <em>Assign yourself to the first-priority alert and change its status to In Progress.<br>The name of your selected alert will be the answer to the question.</em><br><a id='4.3'></a>
>> <strong><code>Potential Data Exfiltration</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/a7234faa-c891-42e2-81f2-438ef167f068)



<br><br>

<h2>Task 5 . Alert Triage</h2>
<p>Finally, you are ready to review the chosen alert! The process is quite operationally heavy, but you will soon see why every step is important. Also, note that the alert review by SOC analysts can also be called alert triage, alert handling, alert processing, alert investigation, or alert analysis. During this module, we will stick to the Alert Triage option.</p>

![image](https://github.com/user-attachments/assets/fdb42bfc-2c87-433b-a3c5-414a6bbdede5)

<h3>Initial Actions</h3>
<p>The initial steps are designed to ensure that you take ownership of the assigned alert and avoid interfering with alerts being handled by other analysts, and confirm that you are fully prepared to proceed with the detailed investigation. You achieve it by first assigning the alert to yourself, moving it to In Progress, and then familiarising yourself with the alert details like its name, description, and key indicators.</p>

<h3>Investigation</h3>
<p>This is the most complex step, requiring you to apply your technical knowledge and experience to understand the activity and properly analyse its legitimacy in SIEM or EDR logs. To support L1 analysts with this step, some teams develop Workbooks (also known as playbooks or runbooks) - instructions on how to investigate the specific category of alerts. If workbooks are not available, below are some key recommendations:<br>
<ol type="1. ">
    <li>Understand who is under threat, like the affected user, hostname, cloud, network, or website</li>
    <li>Note the action described in the alert, like whether it was a suspicious login, malware, or phishing</li>
    <li>Review surrounding events, looking for suspicious actions shortly after or before the alert</li>
    <li>Use threat intelligence platforms or other available resources to verify your thoughts</li>
</ol></p>

<h3>Final Actions</h3>
<p>Your decisions here determine whether you found or missed the potential cyberattack. Some actions like Escalation or Commenting will be explained in the following rooms, so don't worry if they sound complex right now. First, decide if the alert you investigated is malicious (True Positive) or not (False Positive). Then, prepare your detailed comment explaining your analysis steps and verdict reasoning, return to the dashboard and move it to the Closed status.</p>

<h4>SOC Dashboard Notes</h4>
<p>If you didn't receive a flag after your triage, it means that the values you set are wrong.<br>
You can reset the SOC dashboard by clicking Restart on the top right in the TryHackMe SIEM.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 5.1. <em>Which flag did you receive after you correctly triaged the first-priority alert?</em> Hint : <em>Triage means providing a comment and setting the correct status, verdict, and assignee.</em><br><a id='5.1'></a>
>> <strong><code>THM{looks_like_lots_of_zoom_meetings}</code></strong><br>
<p></p>

<br>

<p>I set up the <code>Status</code> to <code>In Progress</code>, <code>Assignee</code> as You anc clicked <code>Save</code><br>
Next I analysed the scenario.  Afterwards I choose the <code>Verdict</code> as <code>False Positive</code> and wrote my analysis in the <code>Analyst Comment</code>.<br>
To finish this process I chose <code>Close</code> and clicked <code>Save</code>.</p>

![image](https://github.com/user-attachments/assets/41af7237-2ca3-4a74-8a75-d4e063d70ebe)

<br>


> 5.2. <em>Which flag did you receive after you correctly triaged the second-priority alert?</em><br><a id='5.2'></a>
>> <strong><code>THM{how_could_this_user_fall_for_it?}</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/a0871647-f4a5-4118-8432-4efecfd8d13c)

<br>


> 5.3. <em>Which flag did you receive after you correctly triaged the third-priority alert?</em><br><a id='5.3'></a>
>> <strong><code>THM{should_we_allow_github_for_devs?}</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/989e31f0-d03d-4bd2-b9a0-732d9eb285ae)


<br>

<br><br>

<h2>Task 6 . Conclusion</h2>
<p>Congratulations on successfully triaging the alerts! Of course, closing the alert as True Positive won't prevent the attack, but it is a great start. Next, you will learn about proper alert commenting and case reporting, correct escalation procedures, and actions made by L2 analysts after the escalation. We hope you enjoyed the room!</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questionsbelow}}$$ </h3>

<br>

> 6.1. <em>I am ready to move on!.</em><br><a id='6.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/ceaeb216-fe67-4aa9-9ba1-a32e80fd7722"><br>
<img width="900px" src="https://github.com/user-attachments/assets/473e4439-5baf-4c76-b8bb-37bcd9e29a49"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 10, 2025    | 339      |     298ᵗʰ    |        8ᵗʰ   |    250ᵗʰ    |     2ⁿᵈ    |  92,222  |       652 |   59      |

</div>

<br>

<p align="center">League<br><br><img width="300px" src="https://github.com/user-attachments/assets/29b35e41-b041-4696-985d-7b4bd6fb88ff"> </p>


<br>

<p align="center"> Global All Time: 298ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/d52c4fd8-067f-449a-aa9a-d11f9f899241"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/a8f0de66-46ad-4594-8ed0-ddda17bc1981"> </p>

<p align="center"> Global monthly: 250ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/30c2bf9f-7ce8-4ca3-95d9-c901bb0e86a9"> </p>

<p align="center"> Brazil monthly: 2ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/057a1277-d151-457c-aa6e-f4b0ae5ac00e"> </p>


<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and  <a href="https://tryhackme.com/p/TactfulTurtle">TactfulTurtle</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 
