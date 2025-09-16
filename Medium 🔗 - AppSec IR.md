<h1 align="center">AppSec IR</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/9b42d2c0-9f84-4f23-b46b-0d735f91013c"><br>
2025, September 15<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>497</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>An introduction into the overlapping worlds of AppSec and IR</em>.<br>
Access it <a href="https://tryhackme.com/room/appsecir">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/a42c0e98-ecbc-4fb3-978d-04de2910ecfb"></p>

<br>
<h1 align="center">Task 1 . Introduction</h1>
<p></p>In this room, we will examine application security (AppSec) and incident response (IR). More specifically, we will learn how shifts in threat landscapes, software architecture, and attacker behaviour have made AppSec IR, an intersection of these two practices, increasingly relevant and teach the basics of this hybrid function.</p>

<h3 align="center">Learning Prerequisites</h3>
<p>While this room has no hard prerequisites, in covering AppSec incident response, it does assume an understanding of application security, including some common application-level attacks. Before attempting this room, ensure you understand the basics of these topics:<br>

- <a href="https://tryhackme.com/room/owaspbrokenaccesscontrol">OWASP Broken Access Control</a><br>
- <a href="https://tryhackme.com/room/incidentresponsefundamentals">Incident Response Fundamentals</a></p>

<h3 align="center">Learning Objectives</h3>
<p>

- Understand the intersection between AppSec and incident response<br>
- Understand the steps that can be taken to prepare for an application incident<br>
- Understand the process of responding to an application incident<br>
- Understand the importance of learning from an application incident</p>

<p><em>Answer the question below</em></p>

<p>1.1. I´m ready to learn about AppSec IR!<br>
<code>No answer needed</code></p>

<br>
<h1 align="center">Task 2 . AppSec IR Fundamentals</h1>
<h3 align="center">AppSec IR & Why it Matters</h3>
<p>Application security incident response (AppSec IR) refers to the overall practice of handling security incidents involving application-layer vulnerabilities, exploits, or breaches. It sits at the intersection of traditional incident response and application security. The AppSec IR process covers preparation for application security incidents all the way to recovery from an incident that has occurred, essentially looking at IR through an AppSec Lens. This approach has become crucial because modern breaches increasingly originate at the application layer (take this <a href="https://www.verizon.com/business/resources/Ta5a/reports/2023-dbir-public-sector-snapshot.pdf">report from Verizon</a>, which found that web applications are now the top asset involved in security breaches, affected in around 60% of breaches).</p>

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/c817456e-1724-4417-84f7-7e419f7abcc3"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

<p>The ultimate goal of AppSec IR is to leverage AppSec practices like secure coding, code review, and application testing to influence each stage of incident response:<br>

- Preparation<br>
- Detection & Identification<br>
- Containment<br> 
- Eradication<br>
- Recovery<br>

This room is structured in a way that it will take you through how each of these IR stages can be influenced by an AppSec perspective. After all, an AppSec-aware responder is able to think about how a vulnerability got introduced, how it might have been prevented, and how fixing it ties back into the development process. Integrating these practices makes for a proactive stance where security is embedded early and developers and security teams share responsibility, with the aim of reducing the number of application-level incidents and ensuring the response is effective when one does occur.</p>

<h3 align="center">The AppSec IR Collaboration</h3>
<p>One of the biggest differences between AppSec IR and traditional IT incident response is the level of collaboration required between security responders and the development/AppSec IR teams. In AppSec IR, there are no outrightly defined roles or responsibilities outlined because the implementation will differ depending on the internal infrastructure of an organisation. For a general idea of how this would realistically work in practice, though, consider this example: An IR team would lead the overall investigation, monitoring and containment, but the application security and development teams must be involved to advise on application specifics and implement code fixes.</p>

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/c49d8c76-22ba-4068-a665-00ed8212dc7b"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6><br>

<p>When an application-level incident occurs, this collaboration (the intersection of the two teams makes AppSec IR crucial and is what can make the difference in responding to the incident swiftly and effectively. For example, the AppSec team might identify the exact code flaw and provide a patch, while the incident responders deploy a WAS rule to hold off the attacker until that patch can be applied. AppSec IR is about ensuring that both of these teams are integrated into each other's processes, so each team has a level of understanding to make this collaboration possible.</p>

<h3 align="center">Key Tools for Application-Layer Incident Response</h3>
<p>Like any discipline in cyber security, we can help ourselves in achieving our goals (in this case, a quick and effective response to application-layer incidents) by adopting the use of tools. Here is a rundown of some of the types of tools we might be using when thinking about AppSec IR:<br>

- <strong>Application Logs & SIEM</strong>: When responding to an application incident, it is fundamental to harness and track user activities, errors, input validation failures, etc., in application logs and couple this with a SIEM (Security Information and Event Management) system. SIEMS can help by aggregating events found in application logs, providing an efficient way to detect malicious activities (e.g., unauthorised account creation). Where SIEM ingestion isn’t available, use log parsing & normalisation tools to structure application logs and enable searching and alerting.<br>
- <strong>Web Application Firewalls (WAF)</strong>: A WAF is a security filter that sits in front of web applications to intercept malicious HTTP traffic. It can be thought of as the first line of defence, blocking common attacks like SQL injection and XSS based on rule sets. WAFs can also serve as a quick reaction tool in AppSec IR and can be especially useful during the containment phase, as a new rule can instantly mitigate an ongoing exploit. A Content Delivery Network (CDN) can also complement a WAF by absorbing edge traffic, caching content, and providing controls like rate limiting and geo/IP blocking to reduce attack impact.<br>
- <strong>Threat Intelligence (feeds/platforms)</strong>: Use IOCs (Indicator of Compromise), context, and emerging TTPs to enrich detections, tune WAF/RASP rules, and guide triage/prioritisation.<br>
- <strong>Runtime Application Self-Protection (RASP)</strong>: RASP is an in-app security technology that monitors an application from the inside. Real-time attacks can be detected and blocked by monitoring for dangerous actions within the running application itself. This can be key in mitigating some application-level security attacks, especially those like zero-day attacks, which will bypass external defences (like WAF). Detailed, context-rich alerts can also be sent by RASP tools, which further helps responders quickly understand what an attacker has tried to do.<br>

These tools provide a foundation for those used in AppSec IR. Of course, there are others, with a further overlap being DevSecOps, with pipelines and automation further helping teams to rapidly deploy patches or roll back to a safe version. More about this can be found in the  <a href="https://tryhackme.com/room/introductiontodevsecops">Introduction to DevSecOps</a> room. This task has aimed to provide you with an insight into where AppSec and IR intersect. We will now begin going through the IR process, giving us a closer look at how each stage can be considered from an AppSec perspective.<br>

Throughout this room, we will follow a scenario to illustrate how each stage of IR manifests in AppSec. "ShopSmart" is an online retail platform. During a seasonal sale, attackers exploit a SQL injection vulnerability in the product search API, aiming to access customer order data. We’ll see how each IR stage applies as the team responds.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. Which tool type analyses logs and aggregates security events across applications?<br>
<code>SIEM</code></p>

<p>2.2. Which IR phase focuses on deploying emergency WAF rules to stop an ongoing exploit?<br>
<code>Containment</code></p>

<br>
<h1 align="center">Task 3 . Preparing for Application Incidents</h1>
<h3 align="center">Fail to Prepare? Prepare to Fail</h3>
<p>It will come as no surprise to a cyber security enthusiast that one of the most important stages of responding to AppSec incidents occurs before the incident has even happened. As with most disciplines in cyber security, being prepared is paramount to ensuring incidents that occur on an application level are contained and responded to in an effective manner. The preparation phase of incident response can help us achieve this with our application incidents, and there are a few things which an AppSec professional can do to ensure they are ready before an application breach happens.</p>

<h4 align="center">Prenvention</h4>
<p>One of the most effective ways of combating application security incidents is by preventing them from happening in the first place. In the context of AppSec, one of the best ways we can do this is by strengthening the Software Development Life Cycle (SDLC). A common turn of phrase in security, which bears repeating: security should not be an afterthought or a last-minute add-on; it needs to be built in from day one. This is known as adopting a "Secure by Design" (or shifting left) approach, which can help to turn our SDLC into SSDLC (Secure Software Development Life Cycle). This involves tactics like following secure coding practices to avoid common flaws (like XSS), performing threat modelling early on, and adopting SAST/DAST into an organisation's CI/CD pipeline. The aim here is to dramatically reduce the likelihood of serious application incidents occurring by adopting a strong preventive posture, backed by developer training and security testing. For more on this subject, check out our <a href="https://tryhackme.com/room/securesdlc">SSDLC</a> room.

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/48918361-37e8-44b9-b1bc-ad07a85e8fbb"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6><br>

<h4 align="center">Observability</h4>
<p>Despite taking all preventative measures at your disposal, incidents can still occur, so we now turn our focus to being able to detect them, as the only thing worse than an incident is an incident which goes unnoticed. The goal then is to avoid this and achieve effective observability. The first step we can take towards this is ensuring that your application logs all key events, such as:<br>

- Authentication attempts<br>
- API calls or transactions<br>
- Server errors<br>

Effective logging is half the battle, but events can go unseen for some time, so effective monitoring is also required. Organisations should aggregate and watch these logs in real time using centralised log management or SIEMS tools (examples include: Elastic Stack, Splunk, Azure Sentinel). By using these tools, alerts can be triggered on suspicious patterns, such as repeated failed logins, observed unusual spikes in traffic or application failures/errors. With OWASP listing insufficient logging and monitoring as one of the top security risk <a href="https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/">(A09: Security Logging and Monitoring Failures)</a>, it's hard to understate the importance of setting up dashboards and alerts for your application logs, to maximise your observability and increase your chances of catching an incident early. </p>

<h4 align="center">Containment Readiness and Incident Response Playbooks</h4>
<p>The idea in the preparation phase is to first limit the chances of an incident occurring, and secondly, to give engineers the best chance at success in later stages of IR. As will be expanded on later in the room, the containment phase involves ensuring damage is contained after an incident occurs. Containment readiness means having the ability to isolate or quarantine affected components to stop an attacker's spread, but also clearly defining roles and responsibilities so that when an incident does occur, time is not wasted answering questions that could have already been asked. Sometimes, though, the questions that should be asked aren't always clear without the benefit of hindsight. One method of asking the right questions (and so getting the right answers in advance) is with the development of IR playbooks. Want to learn more about IR playbooks? Check out or <a href="https://tryhackme.com/room/irplaybooks">IR Playbooks</a> room!</p>

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/a4fac3e0-f45f-4531-adfc-c305613fc2ec"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6><br>

<p>IR playbooks are one of the best tools in an incident responder's toolkit, and the benefits they offer extend to an AppSec scenario. An IR playbook is essentially a documented procedure that provides step-by-step guidance on how to detect, contain, eradicate, and recover from a specific threat. When incidents occur, it can be a highly stressful environment; this stress breeds chaos, and this chaos breeds human error.<br>

IR playbooks give us a way to turn this chaos into an organised response, identifying potential areas of ambiguity or confusion in advance and giving clear and direct instructions to prevent this, resulting in faster incident response times, less damage to the application and supporting systems and improved team coordination. Keep all incident notes in one place (e.g., Aurora IR or your ticketing tool). Record the timeline, decisions, evidence, and communications there. For each playbook step, name an owner and spell out the exact action from the IR Plan. Include a short checklist, specify who approves, and outline when to escalate so that everyone knows what to do.<br>

Consider the following example playbook scenario:<br>

- <strong>SQL injection attack</strong>: A playbook made for responding to an injection attack might direct responders to immediately update WAF rules to block malicious SQL patterns and blocklist offending IP addresses to contain the attack. The playbook would then instruct engineers to analyse database logs to assess damage and take the appropriate remediation actions, such as patching the vulnerable code or applying a virtual patch via the WAF until a code fix is deployed. The playbook could then instruct the engineers to verify data integrity and continue to monitor for any further malicious activities.<br>

From this, it is clear that IR playbooks can help us be prepared for AppSec incidents. The idea is to combine all of the practices above to ensure the rest of the incident response process goes as smoothly as possible, considering the circumstances you may find yourself in. In our ShopSmart example, the preparation stage would have meant integrating SAST scans into the CI/CD pipeline and having a documented playbook for API-based SQLi attacks; steps that, as we’ll see later, could have shortened the response window when the sale-day attack began.</p>

<p><em>Answer the questions below</em></p>

<p>3.1. Which approach reduces the likelihood of serious application incidents occurring? <br>
<code>Secure by Design</code></p>

<p>3.2. Which OWASP Top 10 category highlights the risk of poor observability in applications?<br>
<code>A09: Security Logging and Monitoring Failures</code></p>

<p>3.3. What type of document outlines step-by-step actions to contain and respond to specific security incidents?<br>
<code>IR Playbooks</code></p>

<br>
<h1 align="center">Task 4 . Responding to an Application Incident</h1>
<p>As has been said, you can prepare all you want, but in all likelihood, you will experience an application incident at some point. When this does occur, it is important that it is  <strong>detected</strong>strong> swiftly and the threat is <strong>contained</strong>. In this task, we will go over how this can be done in an AppSec IR context.</p>

<h3 align="center">Detection & Identification</h3>
<p>Okay, so how do we know something is wrong with our application? In a real incident, detection usually comes from one of the following triggers:

- <strong>Log anomalies</strong>: If the appropriate preparations have been made, as discussed in the previous task, then your application will have sufficient logging and monitoring in place. This means suspicious patterns, a surge of error messages, etc., can be captured and monitored, and then alerts will be generated depending on the severity of what has been found. These alerts are a common method of detecting an incident.<br>
- <strong>User complaints or reports</strong>: Never underestimate the importance of end users and their feedback. Having a channel where users can report issues, and those reports can be received and analysed quickly, can make all the difference when a user-facing application incident occurs. Certain user reports indicate that an application component is becoming unavailable. Could hint at a potential ongoing security incident.<br>
- <strong>Bug bounty</strong>: Sometimes, depending on the scope of your organisation/application, it can be a good idea to set up a bug bounty program where third parties are incentivised through a reward (hence "bounty") to identify existing vulnerabilities in your application.<br>

Once the attack has been <strong>detected</strong>, it needs to undergo an initial triage to <strong>identify</strong> the vulnerability and validate what has been detected. Imagine the scenario we prepared for in the previous task with our IR playbook, which has come to fruition, an alert in our monitoring system, and some bug bounty reports claiming an SQL injection is taking place in a specific API route. Engineers would then follow a process, ideally outlined in the playbook.</p>

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/185d3531-cde1-4a9b-8813-632b4103b0d0"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6><br>

<p>First evidence would be gathered by examining the web server logs and details provided within the alerts and bug bounty reports and looking for the appropriate anomalies in the flagged time frame. Using this information, identify the attack/vulnerability and validate its existence. The final part of the identification stage is determining the scope. You don't want to go any further until you assess the severity and impact of the attack. Is user data or sensitive data at risk? Is it user-facing? These are important questions to ask at this stage.

For ShopSmart, the first clue comes from a spike in database query errors logged in the SIEM, coinciding with a customer support report that the search function is returning strange error messages. An automated alert flags a potential injection attack, triggering the team’s detection and containment process.</p>

<h3 align="center">Containment</h3>
<p>Once it has been confirmed that an incident is in fact ongoing, containment measures must be taken swiftly to ensure minimal impact to the application and its users. What we want to achieve at this stage is to limit the attackers' window of opportunity, making temporary but swift changes that help stop further damage/data loss. Here are some common containment actions that can be taken during an ongoing incident:<br>

- <strong>Disable vulnerable feature / route</strong>: If a specific feature or API endpoint has been confirmed as the breach vector, consider turning it off temporarily until the incident has been resolved. This will prevent the attacker (and everyone else) from accessing the affected feature / route until it has been secured. Many modern applications are built with feature flags/toggles - essentially kill switches - which enable engineers to quickly deactivate a feature without the need for a full redeploy. If this is an option, it can buy your team time while a proper fix is found.<br>
- <strong>Apply WAF rules / block malicious traffic</strong>: A WAF can be updated on the fly, so if your observability is high and you have context-rich alerts and logging, you may be able to pinpoint an IP address where the attack is originating and block it. In the example of the SQLi attack, specific attack patterns can be blocked as well, but it should be noted that these are not permanent fixes, an attacker can change their payload or IP address, this simply buys us time. </p>

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/d3ec7555-97d7-45c2-b46a-a306d3f5198c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6><br>

<p>
  
- <strong>App restrictions</strong>: Containment methods can differ from incident to incident; a decision must be made depending on the severity of the issue facing the application. For example, if an incident is underway and account theft is happening, this would be considered high severity. During a high-severity incident, you want to assess how long realistically this incident will take to fix, this will ultimately be determined by how prepared you are for this specific incident. If you are seeing a critical data leak and have no means to stop it, it may be time to consider taking the application offline temporarily, or disabling key features such as new logins.<br>
- <strong>Stop the spread</strong>: Containment also refers to stopping the attack from spreading to other systems. For this containment method, imagine a malware or web shell attack. The goal would be to segregate the compromised server (for example, by removing it from the load balancer routing). In a web application, this may also mean revoking any compromised tokens or credentials so they can't be reused (for example if an admin account was compromised immediately reset the password and revoke active sessions).<br>

These steps should happen within minutes of identifying the threat. As stated, these are temporary fixes only meant to "stop the bleeding" and give the team enough time to analyse the impact and implement a more permanent fix. At ShopSmart, within minutes, the IR team updates WAF rules to block the malicious SQL patterns and uses a feature flag to disable the vulnerable search endpoint. Customers see a “Search temporarily unavailable” banner, but the attacker’s queries stop immediately. Once the hotfix is live at ShopSmart, the team runs targeted tests to confirm the vulnerability is closed, then quietly reactivates the search feature. Monitoring alerts stay quiet, and normal customer searches return to their pre-incident patterns.</p>

<p><em>Answer the questions below</em></p>

<p>4.1. What is a common detection method involving incentivising third parties to find vulnerabilities?<br>
<code>Bug Bounty</code></p>

<p>4.2. What specific mechanism allows a vulnerable feature to be disabled instantly without redeploying the application?<br>
<code>Feature Flag</code></p>

<p>4.3. What type of tool is commonly used to block specific malicious traffic patterns or IP addresses during an incident?<br>
<code>WAF</code></p>

<br>
<h1 align="center">Task 5 . Remediation & Recovery</h1>
<p>After applying some temporary containment measures, you may be able to take your application back online, but that does not mean the incident is over. After containing the attack, teams must work together to fully <strong>eradicate</strong> the threat and <strong>recover</strong> systems, taking any <strong>lessons learned</strong> from this incident and feeding them back into preparation (so incidents like that can be avoided in the future, or at the very least responded to in a more efficient fashion). In this task, we will outline these stages and how these critical post-containment stages can be carried out effectively. </p>

<h4 align="center">Removing a Threat</h4>
<p>With the threat contained, our attention now turns to eradication. In other words, we want to eliminate the root cause of the incident as well as any other lingering malicious artefacts from our application. We will now discuss some key eradication actions:<br>

- <strong>Patching vulnerabilities</strong>: If the incident was a result of a vulnerability present in the application, like the SQLi example discussed earlier, then this needs to be patched to eradicate it fully. From an AppSec IR perspective, this will likely look like a recommendation to the development team to write a code fix / configuration change (a "hotfix") to close the security hole. This should be done quickly, but with great care, so it does not break other functionalities within the app.<br>
- <strong>Remove malicious artefacts</strong>: If the attacker gained authorised access to an application, they have left behind malicious artefacts. These should be found and removed. This can include malware, web shells, or any malicious code/injections from servers and databases. This can be achieved by running anti-malware tools, restoring clean versions of files and, in extreme cases, compromised systems may need to be rebuilt from scratch.<br>
- <strong>Preserve forensic evidence</strong>: While the process of cleanup and eradication is taking place, it is important to preserve evidence of the attack. In practice this may look like a team member being assigned to take backups or snapshots of relevant data (logs, malicious code samples, query history, etc.) as this evidence may be needed for deeper investigation or legal purposes later.<br>
- <strong>Reset credentials/revoke accounts</strong>: Depending on whether the attacker took control of certain accounts during privilege escalation or even created accounts entirely, these accounts should be cleaned up. Reset passwords/API keys to accounts that are needed, remove ones that are not.</p>

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/4772cbb2-53a2-4c84-b06e-f8df7298e881"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6><br>

<p>While applications should always be closely monitored, this is especially true following a recent incident. While cleaning up further indicators of compromise can be found, these can be fed into your security tools to help spot any remaining malicious presence. At ShopSmart, eradication means deploying a code hotfix for the vulnerable API endpoint, removing a malicious admin account that the attacker created, and restoring clean database backups. Only after penetration testing confirms the fix do they fully reopen the search feature.</p>

<h4 align="center">Restoring and Validating Systems</h4>
<p>With the threat eradicated, we now want to safely restore our application and underlying systems to full working order. Here are a few steps that can be taken at this stage:<br>

- <strong>Validation and testing</strong>: Before an incident can safely be declared over, you should validate that systems are fully functional and secure. Ensure the application, databases, and network devices are working as expected and confirm the vulnerability has indeed been fixed. Security testing and ensuring that vulnerabilities can not be reproduced are critical at this stage. <br>
- <strong>System restoration</strong>: Once it has been confirmed that the application is safe, systems should be brought back online. This can involve reenabling endpoints that were disabled during the containment phase. Now that they have been fixed, prioritise critical services first to resume business operations.<br>
- <strong>Monitoring for recurrence</strong>: As with after eradication, it is critical to keep an extra close eye on your application when it returns to production. You and your team have confirmed the vulnerability is not reproducible, but attackers should never be underestimated, so logs and alerts should be monitored rigorously.</p>

<h4 align="center">Learning Lessons</h4>
<p>Once operations have been restored, the focus should now turn to <strong>what lessons, as a team, can be learned</strong> from this incident going forward, often called a post-mortem. It is very important to approach this with a blameless mindset. Our objective at this stage is to understand what happened and how to improve, not to shame anyone for making mistakes. After the post-mortem has taken place, a detailed incident report should be made, including: A timeline of events, root cause analysis, response evaluation, lessons learned, and recommendations. This report can often be a goldmine in terms of transforming your team's posture, taking all these findings and recommendations and feeding them into preparation so an incident like this won't take place again.</p>

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/790e9ad1-737a-4524-8592-17f0214af1fe"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6><br>

<p><em>Answer the questions below</em></p>

<p>5.1. A developer will push a ______ in order to patch the vulnerability and close the security hole.<br>
<code>hotfix</code></p>

<p>5.2. Routes disabled during the ___________ phase can now be re-enabled during the restoration phase.<br>
<code>Containment</code></p>

<p>5.3. The process of discussing what lessons can be learned from this incident going forward is called what?<br>
<code>Post-mortem</code></p>

<p>5.4. Following this process, what should be produced?<br>
<code>Incident Report</code></p>

<br>
<h1 align="center">Task 6 . Practical</h1>
<h3 align="center">Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting both your AttackBox (if you're not using your VPN) and Target Machines, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<h3 align="center">AppSec IR in Action!</h3>
<p>It's time to put all you've learned into practice. This task aims to demonstrate how to respond to an application incident in real time. This practical puts you in the shoes of an AppSec engineer who has just been told there is an application-level breach. You are on the ground floor for this incident, and it is up to you to utilise the IR phases outlined in this room to respond to this application-wide incident in a fast and efficient manner. 

To get started, boot up the AttackBox or your local machine (conntected to the VPN), and the target machine. Allow 1-2 minutes for the machines to boot up. Once it has booted, you should be able to access your application front end on <code>MACHINE_IP</code> using the browser. Here, there will be a "Flag Submission" option in the navbar. Between the web application and the logs, you will be able to solve the practical and retrieve the flag. To access the log, you can SSH into the target machine with the command: <code>ssh appsecir@MACHINE_IP</code>, the password is <code>**********</code>. You can then find the application logs here: <code>/home/appsecir/Documents/Logs</code>. Use the provided logs to identify what happened in the incident (note the timestamp and the victim's user ID/email), then reproduce it in the live app.<br>

That's it! Good luck!</p>

<p><em>Answer the question below</em></p>

<p>6.1. Can you investigate the incident, confirm the presence of an application vulnerability, and then answer all the questions to obtain the flag?<br>
<code>THM{*************************}</code></p>

<br>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/c557ae00-ebb5-4297-87a9-601d30b3ecb3"><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/a5b34c48-22b4-4f02-a994-e422bbf57e13"><br><br></h6>


<br>
<h2 align="center">Practical &nbsp;&nbsp; ・ &nbsp;&nbsp; Preparation</h2>
<p>What should have been in place to prevent the discovered vulnerability from reaching production? Select two.<br>

- [ ] Authentication middleware on all routes<br>
- [x] Secure coding practices and code review<br>
- [ ] Logging and alerting in production<br>
- [x] A threat model identifying access control flaws<br>
- [ ] Asset inventory of all public endpoints<br>
- [ ] Input sanitization on all user fields</p>

<h2 align="center">Practical &nbsp;&nbsp; ・ &nbsp;&nbsp; Detection & Identification</h2>
<p>What vulnerability did you identifify?<br>
<code>IDOR</code></p>

<p>At what time did the attacker successfully authenticate into an account that wasn´t their? (YYYY-MM-DD HH:MM:SS)<br>
<code>2025-08-24 19:17:32</code></p>

<p>What is the user email attached to user with account ID 105?<br>
<code>john.doe@company.thm</code></p>

<h2 align="center">Practical &nbsp;&nbsp; ・ &nbsp;&nbsp; Containment</h2>
<p>Can you disable the affected endpoint using the admin user with user ID 999?<br>
<code>IDOR</code></p>

<h2 align="center">Practical &nbsp;&nbsp; ・ &nbsp;&nbsp; Eradication - Fix the Root Cause</h2>
<p>What should be recommended to the web development team to fix the IDOR vulnerability?<br>

- [ ] Sanitize all user inputs<br>
- [ ] Add authentication middleware to the /users/:id/profile endpoint<br>
- [x] Enforce server-side validation that the session user matches the requested user ID<br>
- [] Change the HTTP method from GET to POST</p>


<h2 align="center">Practical &nbsp;&nbsp; ・ &nbsp;&nbsp; Recovery</h2>
<p>What log pattern or keyword should be monitored after the patch is deployed? <em>Check the audit trail for the first unauthorized profile view - use the value in the msg fields as your monitoring keyword.</em><br>
<code>user_id mismatch</code></p>

```bash
{"event_id":"...","ts":"2025-08-24T19:17:32Z","level":"WARN","logger":"security.audit","msg":"user_id mismatch","src_ip":"...","method":"GET","path":"/users/103/profile","status":200,"response_ms":34,"session_id":"...","auth":{"user_id":106,"email":"sam.jones@company.thm"},"requested_user_id":103,"accessed_profile":{"user_id":103,"email":"aaron.miller@company.thm","name":"Aaron Miller","account_tier":"Pro"},"rule":"ACCESS_CONTROL_VIOLATION","alert":"access_control_violation"}
```

<h2 align="center">Practical &nbsp;&nbsp; ・ &nbsp;&nbsp; IR Follow-Up</h2>
<p>What document should be updated after this incident to include IDOR response procedures?<br>
<code>IR playbook</code></p>

<h2 align="center">Practical &nbsp;&nbsp; ・ &nbsp;&nbsp; Post-Incident Summary Report</h2>
<p>An Insecure <strong>Direct Object Reference (IDOR)</strong> vulnerability was identified in the /users/:id/profile endpoint. This allowed authenticated users to access the profiles of other users by altering the user ID in the URL without proper authorisation enforcement.

<h3 align="center">Confirmed Vulnerability:</h3>
<p>

- <strong>Type</strong>: IDOR (Insecure Direct Object Reference)<br>
- <strong>Affected Endpoint</strong>: /users/:id/profile<br>
- <strong>Attacker Activity</strong>: Confirmed unauthorised access to another user's account<br>
- <strong>Affected User</strong>: Account ID 103 - Email: aaron.miller@company.thm</p>

<h3 align="center">Containment Action:</h3>
<p>The vulnerable profile endpoint was <strong>successfully disabled</strong>, halting further unauthorised access during the investigation.</p>

<h3 align="center">Eradication Recommendation:</h3>
<p>Implement <strong>server-side validation</strong> to ensure the session user matches the user ID requested in the URL.

<h3 align="center">Recovery Considerations</h3>
<p>
  
- <strong>Monitoring Guidance</strong>: Add detection logic to monitor for the keyword: user_id mismatch in application logs post-deployment to identify future access control violations.<br>
- <strong>Playbook Update</strong>: Update the Incident Response Playbook to include detection, triage, and containment guidance for IDOR-style access control issues.</p>

<p>What document should be updated after this incident to include IDOR response procedures?<br>
<code>IR playbook</code></p>

<br>
<br>
<h2 align="center">nmap</h2>
<p>

- <strong>22</strong> &nbsp;&nbsp; : &nbsp;&nbsp; ssh &nbsp;&nbsp; : &nbsp;&nbsp; OpenSSH 9.6p1<br>
- <strong>80</strong> &nbsp;&nbsp; : &nbsp;&nbsp; http &nbsp;&nbsp; : &nbsp;&nbsp; nginx 1.24.0<br></p>

```bash
:~/AppsecIR# nmap -sC -sV -Pn -n -p- -T4 partpickerparadise.thm
...
PORT    STATE  SERVICE VERSION
22/tcp  open   ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
80/tcp  open   http    nginx 1.24.0 (Ubuntu)
|_http-server-header: nginx/1.24.0 (Ubuntu)
|_http-title: PartPickerParadise
443/tcp closed https
```

<h2 align="center">/etc/hosts</h2>

```bash
xx.xxx.xx.xxx  partpickerparadise.thm
```
<h2 align="center">dirsearch</h2>
<p>

- /assets/<br>
- /images</p>

```bash
:~/AppSecIR# dirsearch -u http://partpickerparadise.thm/ -i200,301,02,401 -w /usr/share/wordlists/dirb/common.txt
...
[xx:xx:xx/ 201  -  178B  -  /assets  ->  http://partpickerparadise.thm/assets/
[xx:xx:xx/ 201  -  178B  -  /images  ->  http://partpickerparadise.thm/images/

Task Completed
```

<h2 align="center">Web 80</h2>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/ae714f03-9891-4b8f-b1d6-9fb57a92bec6"></h6>

<br>
<br>
<p></p>
  
- identified Broken Access Control</p>

<h2 align="center">http://partpickerparadise.thm/assets/index-1rIfu-CQ.js</h2>

```bash
...
Incident Responder",username:"Incident_Responder",password:"xxxxxxxxxxxx",email:"incident_responder@company.thm",phone:"(xxx) xxx-xxxx",address:"xxx xxxxxxxx xxxx, xxxxx xxxxx, xx xxxxx",ssn:"***-**xxxxx",creditCard:"****-****-****xxxxx",role:"Security Analyst",department:"Information Security",joinDate:"xxxx-xx-xx",isAdmin:!1},

101:{id:101,name:"Jessica Warner",username:"jessica",password:"xxxxxxxxxx",email:"jessica@company.thm",phone:"(xxx) xxx-xxxx",address:"xxx xxxxxxxx xx, xxxxxxxx xxxx, BC xxxxxx",ssn:"xxx-xx-xxxx",creditCard:"xxxx-xxxx-xxxx-xxxx",role:"Software Developer",department:"Engineering",joinDate:"xxxx-xx-xx",isAdmin:!1},

102:{id:102,name:"Bob Williams",username:"bob",password:"xxxxxx",email:"bob.williams@company.thm",phone:"(xxx) xxx-xxxx",address:"xxx xxxxx xxx, xxxxxxxxx xxxx, xx xxxxx",ssn:"xxx-xx-xxxx",creditCard:"xxxx-xxxx-xxxx-xxxx",role:"Marketing Manager",department:"Marketing",joinDate:"xxxx-xx-xx",isAdmin:!1},

103:{id:103,name:"Aaron Miller",username:"aaron",password:"xxxxxxxx",email:"aaron.miller@company.thm",phone:"(xxx) xxx-xxxx",address:"xxx xxxxxx xx, xxxxxxxxxxx xxxx, xx xxxxx",ssn:"xxx-xx-xxxx",creditCard:"xxxx-xxxx-xxxx-xxxx",role:"HR Specialist",department:"Human Resources",joinDate:"xxxx-xx-xx",isAdmin:!1},

104:{id:104,name:"David Brown",username:"david",password:"david123",email:"david.brown@company.thm",phone:"(xxx) xxx-xxxx",address:"xxx xxxxxxxx xxxxx, xxxxxxxx xxxx, xx xxxxx",ssn:"xxx-xx-xxxx",creditCard:"xxxx-xxxxxx-xxxxx",role:"Finance Analyst",department:"Finance",joinDate:"xxxx-xx-xx",isAdmin:!1},

105:{id:105,name:"John Doe",username:"john",password:"xxxxxxxx",email:"john.doe@company.thm",phone:"(xxx) xxx-xxxx",address:"xxx xxxxxxxx xxxxx, xxxxxxxx xxxx, xxxxxxx",ssn:"xxx-xx-xxxx",creditCard:"xxxx-xxxx-xxxx-xxxx",role:"Software Developer",department:"Engineering",joinDate:"xxxx-xx-xx",isAdmin:!1},

106:{id:106,name:"Sam Jones",username:"sam",password:"sam1234",email:"sam.jones@company.thm",phone:"(xxx) xxx-xxxx",address:"654 xxxxxxxx xxxxx, xxxxxxxx xxxx, xx xxxxx",ssn:"xxx-xx-xxxx",creditCard:"xxxx-xxxx-xxxx-xxxx",role:"Software Developer",department:"Engineering",joinDate:"xxxx-xx-xx",isAdmin:!1},

999:{id:999,name:"System Administrator",username:"admin",password:"xxxxxxxx",email:"admin@company.thm",phone:"(xxx) xxx-xxxx",address:"x xxxx xxxxx, xxxxxx xxxxxx, xx xxxxx",ssn:"xxx-xx-xxxx",creditCard:"xxxx-xxxx-xxxx-xxxx",role:"System Administrator",department:"IT Operations",joinDate:"xxxx-xx-xx",isAdmin:!0}},nn={HOME:"/",LOGIN:"/login",PROFILE:"/users/:id/profile",FLAG_SUBMISSION:"/flag-submission"},$2=[{name:"xxxxx x xxxxX",description:"6-Core, 12-Thread Unlocked Desktop Processor",price:xxx.xx,image:"xxx.xxx",category:"xxxxxxxxx's xxxxxxx"},{name:"xxxxx xxxx xx-xxxxxx",description:"xxxx xx xxxxx xxxx xx Processor",price:xxx.xx,image:"xxx.xxx",category:"xxxxxxxxx's xxxxxxx"},{name:"xxxx x xxxxX",description:"xx-
...
```

<h2 align="center">appsecir</h2>


```bash
:~/AppSecIR# ssh appsecir@partpickerparadise.thm
...
appsecir@tryhackme-2404:~$ id
uid=1001(appsecir) gid=1001(appsecir) groups=1001(appsecir),100(users)
appsecir@tryhackme-2404:~$ pwd
/home/appsecir
```

<h2>linpeas</h2>

```bash
...
[+] Analyzing .service files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#services
/run/user/1001/systemd/generator.late/app-snap\x2duserd\x2dautostart@autostart.service
/run/user/1001/systemd/generator.late/app-xdg\x2duser\x2ddirs@autostart.service
/run/user/1001/systemd/generator.late/xdg-desktop-autostart.target.wants/app-snap\x2duserd\x2dautostart@autostart.service
/run/user/1001/systemd/generator.late/xdg-desktop-autostart.target.wants/app-xdg\x2duser\x2ddirs@autostart.service
You can't write on systemd PATH so I'm not going to list relative paths executed by services
...
[+] Users with console
appsecir:x:1001:1001:,,,:/home/appsecir:/bin/bash
root:x:0:0:root:/root:/bin/bash
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
...
[+] All users & groups
uid=0(root) gid=0(root) groups=0(root)
...
...
[+] Searching Cloud-Init conf file
Found readable /etc/cloud/cloud.cfg
    lock_passwd: True
    groups: [adm, cdrom, dip, lxd, sudo]
    sudo: ["ALL=(ALL) NOPASSWD:ALL"]
```

<h2 align="center">http://partpickerparadise.thm/login</h2>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/1bedf954-af9e-45a2-a363-65078794054"><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/18623867-8884-4cb1-b73c-8050f43d797a"><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/f64346a4-bad3-4be0-8b5a-89cd7d94492a"><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/3f57cb33-8a93-4e4f-b360-ae01c3dcd440"><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/963cffc5-7a89-40bd-81ce-57a83e8db8ca"><br><br>


<br>
<h1 align="center">Task 7 . Conclusion</h1>
<h2 align="center">Turning Incidents Into Win-Cidents!</h2>
<p>This room has covered the overlap between AppSec and incident response, showing how the two practices can be leveraged to increase the efficiency of the other. With applications being targeted more and more, it has never been more important to be prepared for incidents and respond to them in a timely and effective manner. Here is a summary of what has been covered in this room:<br>

- Why <strong>AppSec IR</strong> matters and what tools can be used to achieve it<br>
- The importance of being <strong>prepared</strong> for application incidents, and the steps that can be taken to ensure that you are<br>
- How to effectively <strong>detect</strong> and <strong>contain</strong> an application threat/attack<br>
- Considerations to be taken when <strong>recovering</strong> from an application incident <br>
- How crucial drawing <strong>lessons learned</strong> from an incident is in ensuring future application incidents are better handled, or even better prevented</p>

<p><em>Answer the question below</em></p>

<p>7.1. All done!<br>
<code>No answer needed</code></p>

<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/f04ad4a5-cc76-4671-bc90-82b4fd42ba2d"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/73c56414-dd87-4ad3-886a-b7ae5985a36b"></p>


<h2 align="center">My TryHackMe Journey ・ 2025, September</h2>

<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time<br>Global   |   All Time<br>Brazil   |   Monthly<br>Global   |   Monthly<br>Brazil  | Points   | Rooms<br>Completed     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
| 2025, Sep 15      |Medium 🔗 - <code><strongAppSec IR</strong></code>| 497| 108ᵗʰ |      5ᵗʰ     |     352ⁿᵈ    |     7ᵗʰ    | 126,404  |    964    |    74     |
| 2025, Sep 14      |Hard 🚩 - Misguided Ghosts, in progress| 496    |     108ᵗʰ    |      5ᵗʰ     |     389ᵗʰ    |     6ᵗʰ    | 126,300  |    963    |    74     |
| 2025, Sep 14      |Hard 🚩 - VulnNet: Endgame             | 496    |     108ᵗʰ    |      5ᵗʰ     |     394ᵗʰ    |     6ᵗʰ    | 126,270  |    963    |    74     |
| 2025, Sep 13      |Hard 🚩 - Royal Router                 | 495    |     107ᵗʰ    |      5ᵗʰ     |     388ᵗʰ    |     6ᵗʰ    | 126,160  |    962    |    74     |
| 2025, Sep 13      |Medium 🚩 - Void Execution             | 495    |     107ᵗʰ    |      5ᵗʰ     |     383ʳᵈ    |     6ᵗʰ    | 126,120  |    961    |    73     |
| 2025, Sep 12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     6ᵗʰ    | 126,056  |    960    |    73     |
| 2025, Sep 12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
| 2025, Sep 11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
| 2025, Sep 10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
| 2025, Sep 9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
| 2025, Sep 9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
| 2025, Sep 9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
| 2025, Sep 8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
| 2025, Sep 8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
| 2025, Sep 7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	    5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,018  |   940    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |
</h6></div><br>

<br>

<p align="center">Global All Time:   108ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/81b8a18b-1cc8-470d-974f-ac6b986c2344"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/c1d05c54-609a-4b2f-a5da-4ba25abeb002"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d3dff14e-651a-484f-ac68-c784095c7005"><br>
                  Global monthly:    352ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/10efb653-2d8c-4bf1-8ea4-8db1d62ed346"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/786ed5d0-15b9-4cf7-8374-c68f3bd9991d"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
