<h1 align="center"><a href="https://tryhackme.com/room/sentinelingestdata">MS Sentinel: Ingest Data</a></h1>
<h3 align="center">Defending Azure Learning Path &nbsp;|&nbsp; Microsoft Sentinel</h3>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/6d1085bb-31ad-44a2-9d3a-906218ce2fb2"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2025%2C%20APR%2016-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>
<br>
<br>

<h2>Task 1 . Getting Ready To Ingest Data</h2>

<p>In the previous <a href="https://github.com/RosanaFSS/Azure-Defending/blob/1.Microsoft-Sentinel/Easy%20%F0%9F%94%97%20-%20MS%20Sentinel%20%3A%20Deploy.md">MS Sentinel: Deploy</a> room, we deployed an instance of Microsoft Sentinel. The next logical phase is to plan and execute the log data ingestion process. In Microsoft Sentinel, logs are sent to Log Analytics workspaces via data connectors.<br><br>

As a Microsoft Security Analyst, it is essential to know how to connect log data from different sources. The organization may have data from Microsoft and non-Microsoft resources as well as on-premise and network appliances.</p>

<h3>Learning Objectives</h3>
<p>In this room, we will look into the options for ingesting data and how to connect them so that Microsoft Sentinel starts to analyze and correlate logs. The main parts of this room will be:<br>

- <code>Data connectors</code><br>
- <code>Content hub</code> solutions<br>
- How to <code>install</code> Content hub solutions<br>
- How to <code>connect</code> data connectors<br><br>

Let's dive in!</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>What is used to ingest log data into Microsoft Sentinel?</em><br><a id='1.1'></a>
>> <strong><code>data connectors</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . Data Connectors Introduction</h2>
<h3>Data Sources and Data Connectors</h3>
<p>...</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 2.1. <em>Are data connectors specific to each data source? (Yea/Nay)</em><br><a id='2.1'></a>
>> <strong><code>Yea</code></strong><br>
<p></p>

<br>

> 2.2. <em>Data connectors are available in how many ways?</em><br><a id='2.2'></a>
>> <strong><code>2</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 3 . Content Hub Introduction</h2>

<p>...</p>

<br>

<h3>Content Source: Standalone vs. Solutions</h3>

<p>...</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>What are bundles of data connectors, workbooks, analytic rules, and playbooks called in Microsoft Sentinel?</em><br><a id='3.1'></a>
>> <strong><code>solutions</code></strong><br>
<p></p>

<br>

> 3.2. <em>Content source can either be a Solution or?</em><br><a id='3.2'></a>
>> <strong><code>standalone</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 4 . Lab Instructions</h2>
<p>...</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 4.1. <em>I now know how to connect to the lab environment.</em><br><a id='4.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 5 . Lab-02: Install Content Hub Solutions</h2>
<p><code>Context</code>: Your company recently deployed Microsoft Sentinel. However, no Content hub solutions have been installed yet.<br><br>

<code>Role</code>: You are logged in as:<br>

- Microsoft Sentinel Contributor<br>
- Log Analytics Contributor</p>

<br>


<p><code>Lab scenario</code>: Following the initial deployment of Microsoft Sentinel, you are tasked with <code>installing a Content hub solution</code>.<br>

- First, make sure <code>Sentinel is enabled for the workspace</code>.<br>
- Then, you will install a <code>Content hub solution</code><br>
- Finally, you will <code>review</code> the results</code></p>

<br>

<p>Access your lab by clicking the <code>Cloud Details</code> button below in conjunction with the lab instructions from Task 4:</p>

<p>[ Cloud Details ]</p>

<br>

<p>...</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 5.1. <em>What Content source type is Microsoft Entra ID?</em><br><a id='5.1'></a>
>> <strong><code>Solution</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/8a5ed47d-92c6-4620-a541-3f2ba2cb7a6e)


<br>

> 5.2. <em>What category is the Microsoft Entra ID?</em><br><a id='5.2.'></a>
>> <strong><code>Identity, Security - Automation (SOAR)</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/29c87b79-0734-4fb3-8d05-f0c77216bf79)

<br>


> 5.3. <em>I have installed the Content hub solution Microsoft Entra ID.</em><br><a id='5.3.'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/6bfe0414-f27e-4bec-b88d-009f710c6282)

<br>

![image](https://github.com/user-attachments/assets/774fe06c-bfa3-4fc1-8c4b-72b8f2a260a9)

<br>

![image](https://github.com/user-attachments/assets/36f12199-185c-46c4-a30e-ff9d150fc74b)


<br>

![image](https://github.com/user-attachments/assets/f577c211-5589-4e57-859e-b2b21d26c5fa)

<br>

![image](https://github.com/user-attachments/assets/2c4421e6-8a65-4a4e-bbf2-825e3a1e8388)

<br>
<br>

<h2>Task 6 . Connecting Data Connectors</h2>
<p>...</p>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 6.1. <em>Where can you find all the details about a connector?</em><br><a id='6.1'></a>
>> <strong><code>connector page</code></strong><br>
<p></p>

<br>

> 6.2. <em>In order to configure the Microsoft Entra ID data connector, what permissions are required on the Log Analytics workspace?</em>Hint : <em>Check the prerequisites on the connector page</em><br><a id='6.2.'></a>
>> <strong><code>Microsoft Sentinel Contributor</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/61c34e57-0803-42b8-a6b6-d34141a4d1d9)

<br>

![image](https://github.com/user-attachments/assets/26b903a2-031a-4869-8117-cd397aade976)



<br>
<br>

<h2>Task 7 . Lab-03: Connect and Configure a Data Connector</h2>

<p><code>Context</code>: Your company recently deployed Microsoft Sentinel and a Content hub solution is installed. A data connector is populated; however, it has not been connected yet.<br><br>

<code>Role</code>: You are logged in as:<br>

- Microsoft Sentinel Contributor<br>
- Log Analytics Contributor</p>

<br>


<p><code>Lab scenario</code>: Following the installation of the Content hub solution, you are tasked with <code>configuring data connectors</code>.<br>

- First, you will install another Content hub solution: <code>Threat Intelligence</code><br>
- Then, you will connect the <code>data connector</code>
- Finally, you will <code>review</code> the ingested <code>Threat Intelligence</code> data

<br>

<p>First, leave the lab we started in Task 5 by pressing the <code>Leave Lab</code> button on the <code></code>Cloud Details</code> pop-up from Task 5. Then, access your new lab by clicking the <code>Cloud Details</code> bbutton below in conjunction with the lab instructions from Task 4:</p>

<p>[ Cloud Details ]</p>

<br>

<p>...</p>

<br>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 7.1. <em>What does the Microsoft Defender Threat Intelligence (MDTI) connector import?</em><br><a id='7.1'></a>
>> <strong><code>Indicators of Compromise</code></strong><br>
<p></p>

<br>

> 7.2. <em>Can threat indicators include IP addresses and domains? (Yea/Nay)</em>Hint : <em>Check the MDTI description</em><br><a id='7.2.'></a>
>> <strong><code>Yea</code></strong><br>
<p></p>

<br>

> 7.3. <em>Let the log data flow!</em><br><a id='7.3.'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/92693447-b9fb-4b30-a0d5-3dfd51658ad2)

<br>

![image](https://github.com/user-attachments/assets/845dd76a-50d6-4376-b623-aca3497eb392)

<br>

![image](https://github.com/user-attachments/assets/59456487-a399-4b33-b2d1-63e8e18b3ed1)

<br>

![image](https://github.com/user-attachments/assets/331a6116-439d-4e20-8480-07861cf6cedc)


<br>

![image](https://github.com/user-attachments/assets/51ad0b50-ec3b-43cf-9d5e-2a2c1eb39854)

<br>

![image](https://github.com/user-attachments/assets/17919877-9b87-4559-9437-e92ba697d107)

<br>

<p>It took about 10 min for log data start to flow.</p>


<br>

![image](https://github.com/user-attachments/assets/b055093b-3a1c-4ef1-bcc4-4652947b275d)


<br>


![image](https://github.com/user-attachments/assets/ddc7747d-4caf-44da-ab93-ae14edd4261f)



<br>
<br>

<h2>Task 8 . Conclusion</h2>

<p>After completing this room, you should better understand what a Content hub solution is and what Data connectors are. Now, you should be able to:<br>

- Describe what Content hub solutions and Data Connectors are<br>
- Install a Content hub solution<br>
- Connect and configure a Data connector<br>
- Confirm the connection results by reviewing ingested logs</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 8.1. <em>Finally, some logs are flowing into Microsoft Sentinel. Time to put on the SOC Analyst hat!</em><br><a id='8.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>


<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/8c1c54e6-e641-426b-aca8-59a7ba96f1aa"><br>
<img width="900px" src="https://github.com/user-attachments/assets/730af996-fb39-4eff-9e70-2215bb3296a4"></p>


<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
|   April 16, 2025  |   345    |     276ᵗʰ    |      6ᵗʰ     |     91ˢᵗ    |     2ⁿᵈ    |  94,923  |    669    |   59      |

</div>

<br>


<p align="center"> Global All Time:  276ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/12d61987-c3af-424b-b124-cccd3ec25f08"> </p>

<p align="center"> Brazil All Time:   6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/50bbec1c-6f15-4376-9d0e-8fc1e432e896"> </p>

<p align="center"> Global monthly:   91ˢᵗ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/e145f62f-543d-48cf-b52c-07ed2a3bdd67"> </p>

<p align="center"> Brazil monthly:     2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/f825827b-8dda-4998-8d2d-1bc9676d5afd"> </p>



<br>


<p align="center">Weekly League: 3ʳᵈ Silver<br><br><img width="1000px" src="https://github.com/user-attachments/assets/7f3d7023-d23a-417f-af15-a3461f052737"> </p>

<br>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a>, <a href="https://tryhackme.com/p/zieglers">zieglers</a> and <a href="https://tryhackme.com/p/huamanejard">huamanejard</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p>
