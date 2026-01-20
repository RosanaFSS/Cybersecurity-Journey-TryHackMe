<h1 align="center"><a href=https://tryhackme.com/room/sentinelinvestigate">MS Sentinel: Investigate</a></h1>
<h3 align="center">Defending Azure Learning Path &nbsp;|&nbsp; Microsoft Sentinel</h3>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/8c473b43-224e-4c60-9727-df8c51d761fa"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2025%2C%20APR%2020-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<br>


<h2>Task 1 . Introduction</h2>
<p>Our Microsoft Sentinel journey continues. Let's take a quick snapshot of where we are in this journey and review the milestones we've passed in the previous rooms:
Onboarding - Microsoft Sentinel concepts, planning and initial deployment<br><br>
  
- Configuration - Installing Content hub solutions<br>
- Configuration - Connecting Data connectors<br>
- Threat detection - Analytics rules enabled</p>


<h3>Learning Objectives</h3>
<p>In this room, we will look into incident investigation and management concepts to see how we can easily manage security incidents in Microsoft Sentinel.<br><br>

- Firstly, we'll introduce incident tools and features in Microsoft Sentinel<br>
- Then, investigate sample incidents<br>
- Finally, we'll see how we can manage incidents, hand them over, or escalate them a higher level security team</p>


<h3>Prerequisites</h3>

<p>A good understanding of previous Sentinel rooms is recommended to fully leverage the benefits of this room:<br><br>

- MS Sentinel: Introduction<br>
- MS Sentinel: Deploy<br>
- MS Sentinel: Ingest Data<br>
- MS Sentinel: Detect</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Let's go!</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 2 . Events / Alerts / Incidents</h2>
<p>[ ... ]</p>

<h3>Real-Life Analogy - House Monitoring System</h3>
<p>To better understand the similarities and differences between events, alerts, and incidents, let's imagine a typical daily scenario: a House Monitoring System.<br><br>
  
Imagine a 24/7 camera monitoring the entrance of a house. This camera will surely capture many snapshots of activities happening. Let's further assume a family of 3–4 household members living there. Surely, this family will go about their days and will be entering and exiting the house, back and forth, many times during the day.<br><br>

With this background context, consider the following situations in which each moment is captured by the camera. Let's use these moments to explain events, alerts, and incidents.</p>

<h4>Scene 1 : Event</h4>
<p>[ ... ]</p>

<br>

<h4>Scene 2 : Alert</h4>
<p>[ ... ]</p>

<br>

<h4>Scene 3 : Incident</h4>
<p>[ ... ]</p>

<br>


<p>With the above mental picture in mind, let's define events, alerts, and incidents in the context of IT security operations.</p>

<br>

![image](https://github.com/user-attachments/assets/32fa75dc-2511-46a5-a4b4-9ce0c5c9dfc1)

<br>

<p>Event data can be vast; in this case, only certain events passing defined thresholds will be categorized as alerts. In the context of Microsoft Sentinel, these rules and thresholds are defined in Analytics rules, as seen in the MS Sentinel: Detect room.<br><br>
Understanding these terms, their differences, and how they relate to any security monitoring application is crucial for investigating and managing incidents.<br><br>
After the real-life analogy above and explanations, I hope all three terms are as clear as mud. Let's move on to see how to perform investigations and manage incidents throughout the rest of this room. Specifically, we will look into how events, alerts, and incidents are represented and managed in different parts and screens of Microsoft Sentinel.<br><br>
Let's move on to incident triage and investigations.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 2.1. <em>What is a normal activity that happens at a point in time, neither good nor bad called?</em><br><a id='2.1'></a>
>> <strong><code>event</code></strong><br>
<p></p>

<br>

> 2.2. <em>What is a negative event that disrupts normal operations and requires investigation called?</em><br><a id='2.2'></a>
>> <strong><code>incident</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 3 . Incidents Overview</h2>
<p>Now that all the fundamental security concepts - events, alerts, incidents - are covered in detail, let's see how Microsoft Sentinel presents these concepts and what additional information is available for investigation.</p>

<br>

![image](https://github.com/user-attachments/assets/5aff0287-5919-4c92-b82d-fea5fe5f61cb)


<br>


<p>1. Showing the number of Open, New, and Active incidents.<br>
2. Show all incidents based on the filters applied, e.g., the last 30 days.<br>
3. Incident management details for the selected incident: This part will be relevant later when we discuss triaging and taking ownership of an incident.<br><br>

. Owner: Unassigned or assigned owner<br>
. Status: New, Active, Closed<br>
. Severity: High, Medium, Low, Informational<br><br>

4. Evidence: Events and Alerts related to the selected incident.<br>
The right pane only summarizes the incident; more details can be found by clicking "View full details" for investigation purposes. MITRE Tactics and Techniques mapped to this incident can also be seen on the incident overview pane.</p>

<br>

![image](https://github.com/user-attachments/assets/09a5ceb7-31f4-47a8-80df-0102f8fbd120)


<br>

<p>It is also important to note that the source of alerts resulting in incidents may not always be Microsoft Sentinel itself. Other security products may also contribute to incidents, as seen below. In fact, this is the most common scenario: Once connected to Microsoft Sentinel, alerts from these products will produce the majority of the incidents, such as the Microsoft Defender products suite.</p>

<br>

![image](https://github.com/user-attachments/assets/00f1131d-abf5-49d3-b01d-6617001202a3)

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 3.1. <em>Is Microsoft Sentinel the only product contributing to incidents? (Yea/Nay)</em><br><a id='3.1'></a>
>> <strong><code>Nay</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 4 . Triage and Investigate - Ownership, Status, Tasks</h2>
<h3>Incident Ownership</h3>
<p>In a standard setting, every incident must be allocated to a designated security team member. This individual, known as the incident owner, is responsible for overseeing the entire incident management process, encompassing investigation and providing status updates. Ownership can be transferred at any point to delegate the incident to another member of the security team for additional investigation or escalation.<br><br>
As for a SOC analyst, triaging and investigating an incident usually starts by taking ownership of the incident by changing the owner and status. This could be done from the incident overview pane by:</p>

<br>

<p>. Assigning the incident owner to yourself.</p>

<br>

![image](https://github.com/user-attachments/assets/150e93b0-869a-45b5-9835-ba056778e7c7)

<br>

<p>. Changing the incident status from New to Active.</p>

<br>

![image](https://github.com/user-attachments/assets/c69708aa-9cfe-40cf-b4ae-92ce6cc7b8bb)

<br>

<h3>Incident Severity</h3>
<p>The severity of an incident is initially determined by the rule or Microsoft security source that triggered it. Typically, the severity of an incident remains unchanged, but there's the possibility of adjusting it if you determine that the initial classification is inaccurate. Severity options range from Informational, Low, Medium, to High.<br><br>
Using the incident overview pane, you can also add tags and take some initial actions for the incident, such as:</p>

<br>

<p>. Investigate<br>
. Run playbook<br>
. Create automation rule<br>
. Create team</p>

<br>

![image](https://github.com/user-attachments/assets/3dd8bc5d-711f-4772-977a-497e1cf89b65)


<br>

<h3>Incident Details</h3>
<p>When it's time for a more in-depth investigation, the Incident Details page will reveal many details for the SOC analyst. By clicking "View full details", we get to the page where most investigation actions can be performed.</p>

<br>


![image](https://github.com/user-attachments/assets/1014acc3-d845-4a67-80c6-fc48ed203f34)


<br>

<p>At the top of the page, you can find:<br><br>

. Logs: To open the Log Analytics query window<br>
. Tasks: To see the tasks assigned for the incident<br>
. Activity log: To see any actions taken for the incident</p>


<h3>Incident Tasks</h3>
<p>Ensuring the smooth and efficient operation of security operations (SecOps) hinges greatly on process standardization. SOC analysts are tasked with a series of steps - triaging, investigating, or remediating incidents; hence, formalizing these procedures is crucial. By establishing a standardized list of tasks, your Security Operations Center (SOC) can maintain consistency across all analysts, regardless of their shifts.</p>

<br>

![image](https://github.com/user-attachments/assets/010c8d45-7952-426d-a1f4-2a08af8ab8a2)

<br>

<p>This approach guarantees that every incident receives uniform treatment and adheres to Service Level Agreements (SLAs). With predefined steps set by SOC management or senior analysts (lvl 2/3), drawing from common security frameworks like NIST, past incident experience, or recommendations from security vendors, analysts can work efficiently without deliberating on the next steps or fearing missing critical actions.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>


> 4.1. <em>What ensures the smooth and efficient operation of security operations (SecOps)?</em><br><a id='4.1'></a>
>> <strong><code>process standardization</code></strong><br>
<p></p>

<br>


> 4.2. <em>What helps to guarantee that every incident receives uniform treatment?</em><br><a id='4.2'></a>
>> <strong><code>Incident Tasks</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 5 . Triage and Investigate - Timeline, Logs, Entities, Visual</h2>
<h3> Incident Timeline</h3>
<p>[ ... ]</p>

<br>

<h3> Investigate With Logs</h3>
<p>[ ... ]</p>

<br>

<h3> Incident Entities</h3>
<p>[ ... ]</p>

<h3>Visual Investigation</h3>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>


> 5.1. <em>Which link can you click to see the specific logs of an alert without leaving the context of the incident details page?</em><br><a id='5.1'></a>
>> <strong><code>Link to LA</code></strong><br>
<p></p>

<br>


> 5.2. <em>During graphical investigation, which queries can be utilized to deepen the investigation?</em><br><a id='5.2'></a>
>> <strong><code>exploration</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 6. Incident Closure - True / Benign / False Positives</h2>
<h3>Closing Incidents</h3>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>


> 6.1. <em>You investigate an incident and conclude that it is due to red team activities. What is your closure classification?</em><br><a id='6.1'></a>
>> <strong><code>Benign Positive</code></strong><br>
<p></p>

<br>

> 6.2. <em>How do you eliminate a false positive without modifying the analytics rule?</em><br><a id='6.2'></a>
>> <strong><code>Automation rule</code></strong><br>
<p></p>

<br>


> 6.3. <em>What do you classify an actual threat as?</em><br><a id='6.3'></a>
>> <strong><code>True Positive</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 7 . Lab Instructions</h2>

<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>


> 7.1. <em>I now understand how to connect to the lab environment!</em><br><a id='7.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<br>
<br>

<h2>Task 8 . Lab-05: Investigate Incidents</h2>

<p>Context: In your company's Microsoft Sentinel environment, previously enabled Analytics rules started to generate incidents.<br><br>
Role: You are logged in as:<br>
. Microsoft Sentinel Contributor<br>
. Log Analytics Contributor</p>

<br>

<p>Lab scenario: As a SOC LVL 1 Analyst, you need to start triaging and investigating the incidents. You will:<br><br>

. First, review open incidents and take ownership<br>
. Then, investigate the incident<br>
. Finally, escalate the incident to SOC LVL 2 for in-depth investigation and threat hunting</p>

<br>

<p>Access your lab by clicking the Cloud Details button below in conjunction with the lab instructions from Task 7:<br><br>
[ Cloud Details ]<br><br>
Please make sure to have performed these actions on the Cloud Details pop-up:</p>

<br>

![image](https://github.com/user-attachments/assets/bb026097-86fa-413d-ba94-b759ae128f35)

<br>

<p>Note: Deployment and ingesting logs might take up to 15 minutes. You can check the deployment status by navigating to the following within the Azure portal: Resource groups -> Select the available resource group -> Settings -> Deployments</p>

<h3>Wakthrough - Step 1: Investigate Incidents - Take Ownership</h3>
<p>[ ... ]</p>

<br>

<h3>Wakthrough - Step 2: Investigate Incidents - Incident Details</h3>
<p>[ ... ]</p>

<br>

<h3>Wakthrough - Step 3: Escalate Incident to SOC LVL 2 for Threat Hunting</h3>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


<br>


> 8.1. <em>What is the MITRE Tactics classification for Solorigate incidents? Hint : Can be found in the incident's details pane.</em><br><a id='7.1'></a>
>> <strong><code>Command and Control</code></strong><br>
<p></p>


<br>

> 8.2. <em>Investigate the incident "Sign-ins from IPs that attempt sign-ins to disabled accounts". What is the IP entity involved in this incident?</em><br><a id='7.2'></a>
>> <strong><code>175.45.176.99</code></strong><br>
<p></p>

<br>

> 8.3. <em>Check out this IP's geolocation. What is the city?</em><br><a id='7.3'></a>
>> <strong><code>Korea</code></strong><br>
<p></p>
<p></p>

<br>

> 8.4. <em>Now, dive back into the alert logs for this incident. Which disabled account was targeted by attackers? Hint : Click Link to LA on the latest alert.</em><br><a id='7.3'></a>
>> <strong><code>johns@m365x816222.onmicrosoft.com</code></strong><br>
<p></p>
<p></p>

<br>

> 8.5. <em>How many login attempts were there for this disabled account? Hint : Check the disabledAccountLoginAttempts value.</em><br><a id='7.5'></a>
>> <strong><code>4</code></strong><br>
<p></p>
<p></p>

<br>
<br>

<h2>Task 9 . Conclusion</h2>
<p>In this room, you should have learned about triaging, incident handling, and management. Now, you should be able to:<br><br>

. Describe what events, alerts, and incidents are<br>
. Identify different sections of the incidents and Incident Details pages<br>
. Take ownership of incidents<br>
. Investigate the incidents as SOC LVL 1 Analyst<br>
. Close the incidents with the right classification<br>
. If needed, escalate the incident to SOC LVL 2 Analysts for deeper investigation and hunting</p>
<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>


> 9.1. <em>Now I know how to triage, investigate, and manage incidents in Microsoft Sentinel.</em><br><a id='7.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

![image](https://github.com/user-attachments/assets/cc741689-6406-4710-ad7c-5090e8bf167f)

<br>

![image](https://github.com/user-attachments/assets/6eeff88c-23f2-41f4-936f-0e24011c6f06)

<br>

![image](https://github.com/user-attachments/assets/e524e639-c494-4053-a08a-c5677de70310)

<br>

![image](https://github.com/user-attachments/assets/bce6abca-bdb6-40b6-ac47-36f2b5a4d8db)

