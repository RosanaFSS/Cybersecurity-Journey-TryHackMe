
<p align="center">April 10, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{339}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="160px" src="https://github.com/user-attachments/assets/f091ab8b-6389-45e2-a36d-01b50b863eeb"></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{SOC L1 Alert Triage}}$$</h1>


<p align="center">"Learn more about SOC alerts and build a systematic approach to efficiently triaging them." <br>
It is classified as an easy-level walkthrough room.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/socl1alerttriage">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/b07902ee-d6f5-4adf-b647-1aa34b7ba849"> </p>

<br>
<br>

<h2>Task 1 . Introduction</h2>

<p>An alert is a core concept for any SOC team, and knowing how to handle it properly ultimately decides whether a security breach is detected and prevented, or missed and devastating. This is an entry level but essential room for SOC L1 analysts to understand the concept and lifecycle of alerts, from event generation to correct resolution.</p>

<h3>Learning Objectives</h3>
<p>- Familiarise with the concept of SOC alert<br>
- Explore alert fields, statuses, and classification<br>
- Learn how to perform alert triage as an L1 analyst<br>
- Practice with real alerts and SOC workflows<br>
- Prepare for SOC Simulator and SAL1 certification</p>

<h3>Prerequesites</h3>
<p>- Understand common attacks on networks, Windows, and Linux<br>
- Know SOC roles and duties, especially of L1 analysts</p>

<h3>SOC Dashboard</h3>
<p>You were granted access to the SOC dashboard in the TryHackMe SIEM, and you will need it to complete most of the tasks. Open the attached website in a separate window, familiarise yourself with it, and move on to the next task!</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>I am ready to start!</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br><br>

<h2>Task 2 . Events and Alerts</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 2.1. <em>What is the number of alerts you see in the SOC dashboard?</em><br><a id='2.1'></a>
>> <strong><code>5</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/43314fe1-9d0b-43fe-a4bc-20566cb44f32)

<br>


> 2.2. <em>What is the name of the most recent alert you see?</em><br><a id='2.2'></a>
>> <strong><code>Double-Extension File Creation</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/6b2a8fe9-2157-4422-ab70-7e24e2263c43)

<br>

<br><br>

<h2>Task 3 .  Alert Properties</h2>
<p>Now that you know how alerts are generated, it's time to review their content. While the details differ for every SIEM or security solution, the alerts generally have a few main properties you must understand before taking them. Don't worry if you find some confusing, as you will hear more about some in the upcoming tasks.</p>

<br>

![image](https://github.com/user-attachments/assets/d6096eb2-b346-42b4-9584-ac98b9cffe01)

<h3>Alert Properties</h3>

<br>

![image](https://github.com/user-attachments/assets/c602afea-8410-45b3-a407-dfd39a491a07)


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>What was the verdict for the "Unusual VPN Login Location" alert?</em><br><a id='3.1'></a>
>> <strong><code>False Positive</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/01e90150-fdca-4e52-8541-24b474fd1fd7)

<br>


> 3.2. <em>What user was mentioned in the "Unusual VPN Login Location" alert?</em><br><a id='3.2'></a>
>> <strong><code>M.Clark</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/c5dab760-1f41-4290-8981-adf2da4ee328)

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
