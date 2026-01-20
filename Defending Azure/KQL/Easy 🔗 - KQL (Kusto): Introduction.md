<h1 align="center"><a href="https://tryhackme.com/room/kqlkustointroduction">KQL (Kusto): Introduction</a></h1>
<h3 align="center">Defending Azure Learning Path &nbsp;|&nbsp; KQL</h3>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3173f362-97ba-4ed0-94d9-db155ceea96e"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2025%2C%20APR%2015-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<br>
<br>

<h2>Task 1 . Introduction</h2>

<p>This room introduces you to the analysis of security logs with Microsoft Sentinel KQL. As security engineers, we think of security logs as treasures because they can help us discover the hidden activities within our infrastructure. A quick background intro: Microsoft Sentinel is a cloud-native security information and event management (SIEM) product that utilizes ingested logs to provide better visibility into your environment. On the other hand, Kusto Query Language (KQL) is the tool used to proactively reveal the hidden secrets within those logs if you are the curious and hands-on type.<br><br>

Imagine being able to:<br>

- Track down rogue user activities accurately and identify potential breaches before they happen.<br>
- Unravel complex security incidents by correlating events and figuring out every attacker's moves.<br>
- Automating repeated tasks to focus on more serious threats and investigations.</p>

<br>
<p>The focus of this room is Kusto Query Language (KQL), which empowers you, the security analyst/engineer, to become a security sleuth, proactively hunting for threats to ensure your organization's digital infrastructure is safe from attackers. Let's dive into the world of KQL to discover the power of security logs analysis.</p>

<br>

<h3>Learning Objectives</h3>
<p>This room aims to provide you with the fundamental knowledge and skills necessary to use Kusto Query Language (KQL) for security analysis within MS Sentinel Log Analytics workspace. Upon completion, you will be able to:<br>

- Better understand the core concepts and functionalities of Microsoft Sentinel as a Security Information and Event Management (SIEM) solution.<br>
- Easily understand the benefits of using Kusto Query Language (KQL) in Microsoft Sentinel for day-to-day security operations.<br>
- Understand how KQL interacts with data stored within MS Sentinel Log Analytics workspaces and its uses in querying and analyzing them.</p>

<br>


<h3>Prerequisites</h3>
<p>- Having completed the Microsoft Sentinel module.</p>



<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Let's go!</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>



<br>
<br>

<h2>Task 2 . Overview of Microsoft Sentinel</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 2.1. <em>In addition to being a SIEM solution, what else is Microsoft Sentinel? (use the abbreviation)</em><br><a id='2.1'></a>
>> <strong><code>SOAR</code></strong><br>
<p></p>

<br>

> 2.2. <em>How does MS Sentinel support other security solutions that are not included in the built-in connectors? </em><br><a id='2.2'></a>
>> <strong><code>REST API integration</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 3 . What is KQL</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>What initial service was KQL created for?</em><br><a id='3.1'></a>
>> <strong><code> Azure Data Explorer</code></strong><br>
<p></p>

<br>

> 3.2. <em>Analyze the example query from the task. How many computers will the query return?</em><br><a id='3.2'></a>
>> <strong><code>10</code></strong><br>
<p></p>

<br>

> 3.3. <em>What table is the example query retrieving its data from?</em><br><a id='3.3'></a>
>> <strong><code>Heartbeat</code></strong><br>
<p></p>


<br>

![image](https://github.com/user-attachments/assets/47fd400b-c940-410e-82db-a8f34b62322b)

<br>

![image](https://github.com/user-attachments/assets/602a4857-a1bb-4ac3-8c3d-24a1fc6ff168)

<br>


![image](https://github.com/user-attachments/assets/9f584bfa-4d3e-4670-bf15-799f7f1e36e3)


<br>

![image](https://github.com/user-attachments/assets/8ba95c66-c344-48e5-b65a-933b715d8202)





<br>
<br>

<h2>Task 4 . KQL Concepts in Microsoft Sentinel</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 4.1. <em>What operator can be used to output results in graphical form?</em><br><a id='4.1'></a>
>> <strong><code>render</code></strong><br>
<p></p>

<br>

> 4.2. <em>What operator can be used to filter a specified table based on specified conditions?</em><br><a id='4.2'></a>
>> <strong><code>where</code></strong><br>
<p></p>

<br>

> 4.3. <em>What user account name was queried in our second example query above?</em><br><a id='4.3'></a>
>> <strong><code>JBOX00$</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/1394506e-2bfa-45db-87b1-a4674a1d48f9)

<br>

![image](https://github.com/user-attachments/assets/95da9b56-66fa-4f19-9fcb-a74d466faddb)

<br>

![image](https://github.com/user-attachments/assets/434b7f30-2c1d-4dc6-8d15-8484b56b42a3)

<br>

![image](https://github.com/user-attachments/assets/422c5ad5-b0e9-4500-9c34-7d2f1b3fe7c1)




<br>
<br>

<h2>Task 5 . KQL Statement Structure</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 5.1. <em>What is the name of the table queried in our example query?</em><br><a id='5.1'></a>
>> <strong><code>SecurityEvent</code></strong><br>
<p></p>

<br>

> 5.2. <em>Analyze the example query from the task. What does the query aggregate per computer?</em><br><a id='5.2'></a>
>> <strong><code>EventCount</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/c3ed4889-105d-468f-b0bd-3514fb9a0137)

<br>

![image](https://github.com/user-attachments/assets/052aa91c-03da-4629-9dbd-b7fbb40ae4db)



<br>
<br>

<h2>Task 6 . KQL Use Cases</h2>

<p>Congratulations! You did it. I am confident that you now understand the concept and structure of KQL queries. Let's explore real-world scenarios to see how KQL can support you, the security analyst, in gaining deeper insights into your security logs.</p>

<br>

<h3>Real-Life Example</h3>
<p>Scenario: Today at the office, you need to identify failed login attempts for a specific user account to investigate potential unauthorized access.<br><br>

Solution: To identify failed login attempts, you can search the SecurityEvent table for failed login attempts using the query below. This will find all failed login attempts across your organization. You can modify the time range to expand your search.</p>

<br>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 6.1. <em>What is the name of the table queried in our example query?</em>Hint : <em>Run the example query and expand the details to see the Activity entry.</em><br><a id='6.1'></a>
>> <strong><code>An account failed to log on</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/b142d512-8fa7-4498-86b0-fb2e0db8457a)

<br>

![image](https://github.com/user-attachments/assets/26a6efad-a9a1-409d-a0ce-2bfcd8098b4e)


<br>

> 6.2. <em>Run the second example query from the task. What is the account type found?</em><br><a id='6.2'></a>
>> <strong><code>User</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/eff9e255-2dbb-45e4-a900-3fea581620a2)

<br>

![image](https://github.com/user-attachments/assets/faceda52-d89c-4765-90ba-872ae9fed4ae)




<br>
<br>

<h2>Task 7 . Conclusion</h2>

<h3>Summary</h3>
<p>Let's summarise what we have learned so far:<br><br>

We discussed MS Sentinel as a robust SIEM solution that enables organizations to easily identify, investigate, and respond to security threats. KQL, on the other hand, is an effective method of querying and analyzing security logs. When combined, they form a holistic security operations tool for securing modern digital infrastructure.<br><br>

As we continue to explore KQL, you'll discover its extensive capabilities for enhancing your organization's overall security posture.</p>

<br>

![image](https://github.com/user-attachments/assets/a7e82d34-811a-4c79-b431-a40c2d16ed0a)


<br><br>

<h3>Learning Curve</h3>
<p>To become a skilled security analyst and threat hunter, here are some pointers to get you going:<br>

- Start simple: Begin with basic queries to identify core security events, and gradually progress to more complex ones as you gain confidence.<br>
- Practice makes perfect: The more you practice writing KQL queries, the more comfortable and proficient you'll become.<br>
- Unlock potential: As your KQL proficiency grows, you can delve into advanced concepts like joins, parse, and user-defined functions. These offer even greater capabilities for complex data analysis and threat-hunting scenarios.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 7.1. <em>I am ready to learn more about KQL in the KQL (Kusto): Basic Queries room.</em><br><a id='7.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/41bfdcb5-84a6-4917-b83a-927a366e5027"><br>
<img width="900px" src="https://github.com/user-attachments/assets/2d89f2e2-d14f-48b6-8df1-ce665bb77227"></p>


<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
|   April 15, 2025  |   344    |     286ᵗʰ    |      7ᵗʰ     |     241ˢᵗ   |     3ʳᵈ    |  93,845  |    666    |   59      |

</div>

<br>


<p align="center"> Global All Time: 286ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/08d35cc9-0a61-4e09-bc2f-db36af44d7c2"> </p>

<p align="center"> Brazil All Time: 7ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/33ca0edc-5342-46f0-a2a0-a16f2d95c3c40"> </p>

<p align="center"> Global monthly: 241ˢᵗ<br><br><img width="900px" src="https://github.com/user-attachments/assets/fff190a0-2031-4c51-9763-40033b36cb71"> </p>

<p align="center"> Brazil monthly: 3ʳᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/16fdc401-5f06-48f4-8957-23dc06bc0644"> </p>


<br>


<p align="center">Weekly League: 9ᵗʰ Silver<br><br><img width="300px" src="https://github.com/user-attachments/assets/5f84cf43-d0aa-4888-bdde-9acb4b0cf627"> </p>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a>, <a href="https://tryhackme.com/p/zieglers">zieglers</a> and <a href="https://tryhackme.com/p/huamanejard">huamanejard</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p>
