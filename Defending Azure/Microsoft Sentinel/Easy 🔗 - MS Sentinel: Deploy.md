<h1 align="center"><a href="https://tryhackme.com/room/sentineldeploy">MS Sentinel: Deploy</a></h1>
<h3 align="center">Defending Azure Learning Path &nbsp;|&nbsp; Microsoft Sentinel</h3>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/f9f20912-24d1-423a-95fa-2fce799ed960"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2025%2C%20APR%2016-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<br>
<br>

<h2>Task 1 . Getting Ready for Deployment</h2>

<h3>Azure Service vs. Azure Resource</h3>

<p>...</p>

<h3>Microsoft Sentinel Architecture</h3>
<p>The core component of MS Sentinel architecture is Log Analytics workspaces (LAWs).<br><br>
Essentially, a LAW is an Azure resource where the logs are stored. </p>

<p>...</p>

<p>When it comes to implementing Microsoft Sentinel, there are mainly three options:<br>

- Single Tenant - Single Log Analytics workspace<br>
- Single Tenant - Multiple Log Analytics workspaces (Regional)<br>
- Multi-Tenant</p>

<p>...</p>

<p>To recap, on a high level, the following considerations will shape your Microsoft Sentinel architecture and deployment options:<br>

- Tenancy<br>
- Compliance<br>
- Region<br>
- Access</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>Is Microsoft Sentinel a resource or a service?</em><br><a id='1.1'></a>
>> <strong><code>service</code></strong><br>
<p></p>

<br>

> 1.2. <em>What is a potential concern due to logs travelling across the Azure regions?</em><br><a id='1.2'></a>
>> <strong><code>Bandwidth costs</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . Log Analytics Workspace</h2>

<p>So far, we have mentioned Log Analytics workspaces (LAWs) as a log storage mechanism but haven't defined them. In this task, let's provide a more detailed definition.</p>

<h3>What Is a Log Analytics Workspace</h3>

<p>In Microsoft Sentinel, Log Analytics workspaces are crucial in <code>collecting</code>, <code>storing</code>, and <code>analyzing log data</code> from various sources to provide security insights and threat detection capabilities.</p>

<p>...</p>

<br>

<h3>Microsoft Sentinel Workspace</h3>
<p>Sometimes, we also refer to Log Analytics workspace as Microsoft Sentinel workspace. This actually means the same as Log Analytics workspace, with a minor difference in Microsoft Sentinel service being enabled (or onboarded) on it. Back to the cupcake analogy, it merely means there is icing on the cupcake now (Microsoft Sentinel)!</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 2.1. <em>What does a Log Analytics workspace, where log data from different sources is aggregated, essentially serve as?</em><br><a id='2.1'></a>
>> <strong><code>centralized repository</code></strong><br>
<p></p>

<br>

> 2.2. <em>How can we also refer to a Log Analytics workspace once Microsoft Sentinel is enabled on it?</em><br><a id='2.2'></a>
>> <strong><code>Microsoft Sentinel workspace</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 3 . How to Create a LAW</h2>
<h3>Prequisites</h3>

<p>To enable Microsoft Sentinel, Microsoft Sentinel Contributor permissions are required at the resource group level where the Microsoft Sentinel workspace resides. </p>

<h3>Creating a Log Analytics Workspace</h3>

<p>...</p>

<h3>Adding Microsoft Sentinel to a Log Analytics Workspace</h3>

<p>...</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>What permissions do you need to enable Microsoft Sentinel?</em><br><a id='3.1'></a>
>> <strong><code>Microsoft Sentinel Contributor</code></strong><br>
<p></p>

<br>

> 3.2. <em>Do you need to have a Log Analytics workspace created before you can enable/onboard Microsoft Sentinel? (yea/nay)</em><br><a id='3.2'></a>
>> <strong><code>yea</code></strong><br>
<p></p>

<br>

> 3.3. <em>While creating a LAW instance, which setting defines where the log data will reside?</em><br><a id='3.3'></a>
>> <strong><code>Region</code></strong><br>
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

<h2>Task 5 . Lab-01: Deploy Microsoft Sentinel</h2>
<p><code>Context</code>: You recently joined a company's SOC team as a Security Engineer associate. You will mostly be working with Microsoft Sentinel and want to work towards advancing your skills with it.<br><br>

<code>Role</code>: You are logged in with the following Azure job function role assignments:<br>

- Log Analytics Contributor<br>
- Microsoft Sentinel Contributor</p>

<br>


<p><code>Lab scenario</code>: A SIEM product needs to be utilized as part of organizational security policies. Your initial assignment is to onboard Microsoft Sentinel for the organization. You will:<br>

- First, create a <code>Log Analytics workspace</code>.<br>
- Then, enable/onboard <code>Microsoft Sentinel</code> to that workspace.</p>

<br>

<p>Access your lab by clicking the Cloud Details button below in conjunction with the lab instructions from Task 4:</p>

<p>[ Cloud Details ]</p>

<br>

<p>...</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 5.1. <em>Is every Log Analytics workspace a Microsoft Sentinel workspace? (Yea/Nay)</em><br><a id='5.1'></a>
>> <strong><code>Nay</code></strong><br>
<p></p>

<br>

> 5.2. <em>What do you need to create before enabling or onboarding Microsoft Sentinel?</em><br><a id='5.2.'></a>
>> <strong><code>Log analytics workspace</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/a482428f-9c1f-4ea2-ab05-0ca948e14b73)

<br>

![image](https://github.com/user-attachments/assets/f08d9cb1-3700-468c-8578-9e764890173e)

<br>

![image](https://github.com/user-attachments/assets/f279648f-e942-48fa-b5df-cc6106aca81f)


<br>

![image](https://github.com/user-attachments/assets/af608445-b696-4a98-85a9-b28c775914cd)

<br>

![image](https://github.com/user-attachments/assets/014c115d-4627-46a1-aa05-19a606866695)


<br>

![image](https://github.com/user-attachments/assets/cab4a9a5-3b1f-48ce-a946-43b40ee79b2a)

<br>

![image](https://github.com/user-attachments/assets/b5bffc0d-9d74-42b2-9327-fa09d55e5010)


<br>

![image](https://github.com/user-attachments/assets/02e1941b-2c5a-44ed-8455-a5234ff74fd1)


<br>

![image](https://github.com/user-attachments/assets/a99172a4-6663-4053-89e5-ebcb06250ff2)


<br>
<br>

<h2>Task 6 . MS Sentinel Roles and Permissions</h2>
<p>...</p>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 6.1. <em>You are an incident responder who needs to manage incidents, such as assigning and dismissing them. Which role do you need?</em><br><a id='6.1'></a>
>> <strong><code>Microsoft Sentinel Responder</code></strong><br>
<p></p>

<br>

> 6.2. <em>You are a security engineer, and you are tasked with enabling pre-packaged Solutions from Content Hub. Which role do you need?</em><br><a id='6.2.'></a>
>> <strong><code>Microsoft Sentinel Contributor</code></strong><br>
<p></p>

<br>

> 6.3. <em>You are the CISO of the organization. You need visibility into Sentinel data, but you don't directly manage the Sentinel environment. Which role do you need?</em><br><a id='6.3.'></a>
>> <strong><code>Microsoft Sentinel Reader</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 7 . MS Sentinel Settings</h2>

<p>...</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 7.1. <em>How many sets of settings are there for Microsoft Sentinel?</em><br><a id='7.1'></a>
>> <strong><code>2</code></strong><br>
<p></p>

<br>

> 7.2. <em>Can Data Retention settings be found under Microsoft Sentinel workspace settings? (Yea/Nay)</em><br><a id='7.2.'></a>
>> <strong><code>Yea</code></strong><br>
<p></p>

<br>

> 7.3. <em>Under which subcategory of settings are the Data Retention settings tucked in?</em><br><a id='7.3.'></a>
>> <strong><code>Usage and estimated costs</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/e72309d5-6864-4328-9dd9-09d04fffad3b)


<br>

![image](https://github.com/user-attachments/assets/f086a6a5-79b3-4e72-80c3-2f6274b0aa6e)



<br>
<br>

<h2>Task 8 . Conclusion</h2>

<p>...</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 8.1. <em>Now that Microsoft Sentinel is up and running, I'm ready to ingest some data in the MS Sentinel: Ingest Data room.</em><br><a id='8.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>


<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/59341d27-9f82-4826-9693-a98175cf2837"><br>
<img width="900px" src="https://github.com/user-attachments/assets/c39d3657-f231-455c-8dda-8e42741a318c"></p>


<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
|   April 16, 2025  |   345    |     277ᵗʰ    |      6ᵗʰ     |     80ᵗʰ    |     2ⁿᵈ    |  94,835  |    668   |   59      |

</div>

<br>


<p align="center"> Global All Time: 277ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/e5fcaee3-a6d6-4bcd-af39-0b8c54d92caf"> </p>

<p align="center"> Brazil All Time:   6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/8d69d8df-e5a0-4d0d-ae51-6be78950c941"> </p>

<p align="center"> Global monthly:   80ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/8ad28120-50fd-41f1-8971-0b706a3c41e2"> </p>

<p align="center"> Brazil monthly:     2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/567a82aa-682a-4911-8877-d3c26a55a6dd"> </p>



<br>


<p align="center">Weekly League: 2ⁿᵈ Silver<br><br><img width="1000px" src="https://github.com/user-attachments/assets/5e92f57e-f3f1-403a-b89b-1a9e6b5313ce"> </p>

<br>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a>, <a href="https://tryhackme.com/p/zieglers">zieglers</a> and <a href="https://tryhackme.com/p/huamanejard">huamanejard</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p>
