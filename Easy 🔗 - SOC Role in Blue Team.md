<h1 align="center">SOC Role in Blue Team</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/41a37fcf-1794-4eea-b36d-9b29558c3e8c"><br>
2025, September 10<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>492</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Discover security roles and learn how to advance your SOC career, starting from the L1 analyst</em>.<br>
Access it <a href="https://tryhackme.com/room/pythonplayground"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/7b2b3736-fb94-4d71-a450-023e4be9adaf"></p>

<h2>Task 1 . Introduction</h2>

<h3>Introduction</h3>
<p>You've learned about a SOC L1 analyst role in the Junior Security Analyst Intro room. But where is it placed in a company structure? Who is overseeing your team? What other security departments exist? Which skills do you need to advance through your career ladder? Let's find out!</p>

<h3>Learning Objectives</h3>
<p>

- Understand the concept and purpose of the Blue Team<br>
- Explore a place of the SOC within the company structure<br>
- Find out about your career path as a SOC L1 analyst.</p>

<h3>Prerequisites</h3>
<p>

- Complete the <a href="https://tryhackme.com/room/jrsecanalystintrouxo">Intro to Cyber Threat Intel</a> room<br>
- Remind yourself of <a href="https://tryhackme.com/room/socfundamentals">Intro to Cyber Threat Intel</a></p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s find out!<br>
<code>No answer needed</code></p>

<h2>Task 2 . Security Hierarchy</h2>
<h3>Security Hierarchy</h3>
<p>Cyber security priorities are different for every company.<br>
  
- For law firms, the goal is the privacy of the legal documents.<br>
- For factories, the availability of production lines.<br>
- For hospitals, patient safety.<br>

That's why every company has a unique security approach and security team structure.<br>
Let's take a look at the high-level example of it:</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/4e5b0bab-9a4f-4298-8888-90c988612b96"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Looking at the diagram above, top executives like the CEO usually focus on global business objectives and don't manage technical aspects. That's why they hire a Chief Information Security Officer (CISO) or a similar role who knows the business needs and can create the most suitable security departments.</p>

<h3>Security Departments</h3>
<p>In tiny companies, the IT department takes the role of securing the company. Small to medium-sized companies may have a generic "Information Security" team that does all sorts of tasks. For this room, we will focus on bigger companies with a CISO overseeing multiple security teams, each handling a specific task. For example:<br>

- <strong>Red Team</strong>: Offensive security experts, pentesters, or ethical hackers who look for security issues<br>
- <strong>GRC Team</strong>: Specialists managing policies and ensuring compliance with regulations like <a href="https://tryhackme.com/room/socfundamentals">PCI DSS</a><br>
- <strong>Blue Team</strong>: Defensive security experts like SOC analysts, engineers, or incident responders</p>

<p><em>Answer the questions below</em></p>

<p>2.1. Which senior role typically makes key cyber security decisions?<br>
<code>CISO</code></p>

<p>2.2. What is the common name for roles like SOC analysts and engineers?<br>
<code>Blue Team</code></p>

<h2>Task 3 . Meet the Blue Team</h2>
<p>Blue Team is about defensive security, meaning it constantly monitors for attacks and tries to respond to them quickly. Depending on a company's size and sector, Blue Team can include a lot of different roles and subdepartments, usually counting 3 to 50 members total. Now, let's explore the most common Blue Team departments.</p>
<h3>Security Operations Center (SOC)</h3>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/91cc502e-9cfd-4f57-a620-9fa5ccf5b66e"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>That's where you are most likely to start your cyber security journey! SOC is the central hub for an organization's cyber security - they are the first line of defense, work with various alerts, and handle most attacks. You can read more about SOC structure in <a href="https://tryhackme.com/room/socfundamentals">this room</a>, but an efficient SOC is usually composed of the following roles:<br>

- <strong>L1 Analysts</strong>: Junior members who triage alerts and pass complex cases to L2<br>
- <strong>L2 Analysts</strong>: Experienced members who investigate more advanced attacks<br>
- <strong>Engineers</strong>: Experts in configuring security tools like EDR or SIEM<br>
- <strong>Manager</strong>: A person who manages the whole SOC team</p>

<h3>Cyber Incident Response Team (CIRT)</h3>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/6aca9b6a-5381-45fc-a512-37e9d63041b0"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>If SOC expertise is not enough or the incident goes out of control, you urgently call the "firefighters" - CIRT, also called CSIRT or CERT. The members should have a broad knowledge of cyber threats and handle breaches without depending on tools like EDR or SIEM. A CIRT job is stressful and responsible, but also rewarding. Here are a few CIRT examples:<br>

- <a href="https://www.jpcert.or.jp/english">JPCERT</a>: Japan's CERT handling nation-wide breaches<br>
- <a href="https://www.mandiant.com/">Mandiant</a>: A private team responding to global cyber incidents<br>
- <a href="https://aws.amazon.com/security-incident-response">AWS CIRT</a>: Investigates security incidents of AWS customers</p>

<h3>Specialized Defensive Roles</h3>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7898bd9a-cd5f-49a2-a75d-5154d561812e"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Large companies, technology-focused startups, and government agencies often require narrow and specialized Blue Team roles - exciting and highly valuable, but requiring deep topic knowledge and broad experience in broader fields like SOC or IT. These narrow roles can include:<br>

- <strong>Digital Forensics Analyst</strong>: Uncover hidden threats in disk and memory<br>
- <strong>Threat Intelligence Analyst</strong>: Gather data about emerging threat groups<br>
- <strong>AppSec Engineer</strong>: Maintain a secure software development lifecycle<br>
- <strong>AI Researcher</strong>: Study AI threats and how to defend against them</p>

<p><em>Answer the questions below</em></p>

<p>3.1. Does Blue Team focus on defensive or offensive security?<br>
<code>defensive</code></p>

<p>3.2. Which departament handles active or urgent cyber incidents? Hint : <em> Also known as CSIRT or CERT.</em><br>
<code>CIRT</code></p>

<h2>Task 4 . Advancing SOC Career</h2>
<h3>SOC Path</h3>

<p>Starting as a SOC L1 analyst may be a great option to broaden your cyber world awareness and better understand the more specialized roles.<br>Moreover, even the entry-level SOC L1 role can be fun and engaging: You will<br>
  
- deal with real attacks,
- protect the company from advanced threat groups
- learn a lot during the process.<br>

Let's see how you can start:<br>

- Gain core <a href="https://tryhackme.com/path/outline/soclevel1">SOC skills</a> and practice them. Related skills like red teaming or general IT would help, too!<br>
- Be proactive, try yourself in CTFs, stay in the loop of cyber news, and consider the <a href="https://tryhackme.com/certification/security-analyst-level-1">SAL certification</a>!<br>
- Prepare for an interview, learn the difference between an internal SOC and MSSP, and apply for a job!<br>
- After working for some time in a junior position, consider preparing and advancing to more senior roles!</p>

<h3>Internal SOC vs MSSP</h3>
<p>Not every organization has the expertise to operate a SOC on its own and relies on a Managed Security Services Provider (MSSP), a company that delivers outsourced security services, most commonly SOC, to its clients. Working at MSSP is typically high-pressure, but it is also a good option to quickstart your career. While we recommend applying for any open SOC position as your first job, it's also important to understand the differences:</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7d0dbbb7-7cfa-43e1-a455-7f5f8e3641b2"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Next steps</h3>
<p>Your most natural next step after L1 is to become a SOC L2 analyst, but you are free to choose another path! While handling a SIEM alert, you might notice that engineering work appeals to you more. During a cyber attack, you may be fascinated by CIRT actions. You may also find yourself well-suited as a manager and build your path to the CISO role. No matter what, your first year or two is to get real work experience, and to spend this time effectively, follow the tips below!</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/4012e517-6017-43f1-a282-e64bff4ceaf7"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the questions below</em></p>

<p>4.1. How do you call a cyber security company providing SOC services?<br>
<code>MSSP</code></p>

<p>4.2. Which role naturally continues your SOC L1 analyst journey?<br>
<code>SOC L2 Analyst</code></p>

<h2>Task 5 . Final Challenge</h2>
<h3>Final Challenge</h3>
<p>For this task, imagine yourself as a CISO of TrySecureMe, a big multinatnional company. You oversee multiple departments and deal with incidents every month. This time, as many as seven incidents are happening at the same time, and you have to choose the right people to deal with every one of them. Do you know security roles well enough to complete this challenge?</p>

<h4>Website instructions</h4>
<p>[  View Site  ]</p>

<p>Open the attached website by clicking the <strong>View Site</strong> button above and consider resizing or opening it in full screen for a better view. Then, drag and drop the roles from the left to the incidents on the right. If your choices are correct, claim your flag and complete the task! You can reset the website at any time by clicking the <strong>Reset</strong> button.</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/00eca289-05cb-4305-9438-0c57c77f5f72"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the questions below</em></p>

<p>5.1. What flag did you claim after completing the final challenge?<br>
<code>THM{***********************}</code></p>

<h2>Task 6 . COnclusion</h2>
<p>Great job completing the challenge! Now you know how SOC team works, where it is placed in the security structure, and what you to do to start your career journey. Now, continue to the next rooms and learn what does SOC actually protect: humans and systems.</p

<h3>Next Rooms in Path</h3>
- <a href="https://tryhackme.com/path/outline/soclevel1">Humans as Attack Vectors</a><br>
- <a href="https://tryhackme.com/room/systemsattackvectors">Systems as Attack Vectors</a></p>

<p><em>Answer the question below</em></p>

<p>6.1. Complete the room!<br>
<code>No answer needed!</code></p>


<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d5aa0df0-d3e3-4aa1-8367-cca6918e83b5"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/fb762000-fc17-4d76-a22e-5aa8da42ab24"></p>

<h2 align="center">My TryHackMe Journey</h2>


<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time   |   All Time   |   Monthly   |   Monthly  | Points   | Rooms     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                                       |         |    Global    |    Brazil    |   Global    |   Brazil   |          | Completed |           |
| 2025, Sep 9       |Hard 🚩 - <code><strong>Python Playground</strong></code>| 491| 111ˢᵗ | 5ᵗʰ   |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
| 2025, Sep 9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
| 2025, Sep 9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
| 2025, Sep 8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
| 2025, Sep 8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
| 2025, Sep 7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ᵗʰ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486    |      113ʳᵈ   |	    5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,018  |   940    |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   111ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/b038b6ee-1e9a-4966-bb42-57aac87a3f90"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/8f7f0673-390b-4edc-9707-6f61913cb4b0"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/90036076-ddfe-4bae-b0e6-439222e11e20"><br>
                  Global monthly:    693ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/225fa3c4-0914-4e80-94bf-f282252d1b03"><br>
                  Brazil monthly:      9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/eae02176-4e19-4f69-9a7f-a60fb77cb80b"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>  
