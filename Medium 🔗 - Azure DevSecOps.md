<h1 align="center">Azure DevSecOps</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/f9b09cec-4fb7-4b01-a1d0-c189b861086f"><br>
June 10, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>400</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
With this room begins your journey into the world of Azure DevSecOps. <a href="https://tryhackme.com/room/azuredevsecops"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/a4bcc270-14b7-4e26-80db-5fb86cf27e3a"></p>


<h2>Task 1 . Introduction</h2>
<p>So, you’ve learned the basics of DevSecOps, have adopted a shift left mentality, and have gotten to grips with many of the tools and terms that come along with DevSecOps? Well, what now? As you aim to specialise in DevSecOps, the mission then becomes preparing yourself for the real-life scenarios that these roles would find you in. With DevSecOps pipelines becoming more and more prevalent in the cloud, it becomes a more and more valuable skill set. This room aims to give you access to a realistic Azure cloud environment where you will interact with the DevOps services available within Azure, guiding you through how you may interact with these services as a DevSecOps Engineer. </p>

<h3>Learning Prerequisites</h3>
<p>This advanced module assumes knowledge of concepts like CSPs, container technologies, DevSecOps processes, and IaC. If you are unfamiliar with these concepts, it is recommended that you complete the DevSecOps pathway before beginning this room/module.</p>

<h3>Learning Objectives</h3>h3>
<p>

- Understand the Azure cloud platform and how to navigate it<br>
- Understand Azure Repos from a security perspective, including key concepts such as branches and pull requests<br>
- Understand how Azure YAML Pipelines are defined<br>
- Understand Azure App Service and App Service plans<br>
- Understand how to secure an Azure Pipeline</p>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>I'm ready to learn about Azure DevSecOps!</em><br><a id='1.1'></a>
>> <strong><code>No answer neededs</code></strong><br>
<p></p>

<br>

<h2>Task 2 . Azure DevSecOps</h2>
<h3>CI/CD in the Cloud</h3>
<p>In the modern world, CI/CD is practised by an increasing number of organisations, and with this comes a rising need to develop methods of securing the environment that is being built/deployed in and have DevSecOps engineers carry this out. Of course, when you are hired by a company in one of these roles and asked to secure their CI/CD environment, the methods you use to secure it will differ depending on the type of installation. Is it on-premises or cloud-based? Of course, there are overlapping similarities that are common to implementing CI/CD security in both kinds of installations. Still, some unique considerations must be taken into account due to the nature of each. On-premises CI/CD has been covered in the CI/CD and Build Security room. In this room, we begin to focus on how to secure an environment in the cloud. Before we do that, let's explain why you might choose to host your application in the cloud vs. on-premises. <br><br>

<p>An on-premises CI/CD solution offers the security benefit of having complete control over the hardware that runs it, all the configurations made to that hardware, and the isolation of the environment from the Internet using firewall rules. If this complete control is desired or, in many cases, required (by organisations requiring this level of control for compliance purposes), then on-premises would be the way to go. However, a cloud-based solution offers many benefits, including (but not limited to) easy-to-setup, fast, reliable deployments that can scale up or down based on demand. <br><br<

These benefits are enough on their own to make an argument for a cloud-based solution, especially for modern demand-driven applications, with the almost infinite scalability unlocking all kinds of power for your application and the billing for what is used aspect of the cloud providing, in many cases, a more cost-efficient solution. The answer to the question "which one should I use?", of course, entirely depends on what is being hosted/deployed and will change on a case-by-case basis. Still, the vital thing to note for this room is that just because a cloud-based solution doesn't offer full control of hardware, doesn't mean a cloud-based CI/CD solution can't be secure; you just need to know cloud-specific security considerations and the right services/tools to make use of. Welcome then to Azure DevSecOps.</p>

<h3>Azure DevSecOps </h3>
<p>With the scope set at cloud-based CI/CD, let's narrow it even further. The responsibilities of DevSecOps engineers can differ depending on whether the cloud-based CI/CD installation is Self Managed (the cloud-hosted infrastructure that you would install and manage CI/CD software on) or Fully Managed (you are provided with an out-of-the-box pre-installed CI/CD pipeline). For this room/module, we focus on a fully managed CI/CD suite and the greater cloud environment in which it is hosted. The chosen CSP for this module is Azure; you will be placed into a realistic DevOps project, which will need to be secured over the coming rooms using DevSecOps practices. The following task will brief you on your DevSecOps mission and give you the keys to your new Azure home. </p>

<h3 align="left"> Answer the questions below</h3>

> 2.1. <em>Which solution would give you more control over your environment?</em><br><a id='2.1'></a>
>> <strong><code>On-premises</code></strong><br>
<p></p>

> 2.2. <em>Which solution is ideal for environments which to scale up or down rapidly?</em><br><a id='2.2'></a>
>> <strong><code>Cloud</code></strong><br>
<p></p>

<br>

<h2>Task 3 . Welcome to Azure</h2>
<h3>Setting the Scene</h3>
<p>Welcome to the Team! That is, today is your first day in the DevSecOps Engineering team for a company called FinkFactory. FinkFactory is an online merchant which sells PC parts to those looking to build a PC. They sell everything from storage, to processors, to RAM, and cases. If you’re building a PC, it’s a one-stop shop! They are a fully online operation and have no physical stores so all business takes place through their eShop web application. Their web application is currently being hosted in the cloud, on an Azure tenant. You have been hired to help secure the development and deployment processes of this web application. However, before you can help FinkFactory secure their Azure-hosted web application, you’ll need access to the Azure tenant!</p>

<p>[ ... ]</p>

![image](https://github.com/user-attachments/assets/c10bea7a-c2e0-4b6c-a7c1-34e62ea42686)


<h3 align="left"> Answer the questions below</h3>

> 3.1. <em>Which Azure DevOps service would you use to access source code?</em><br><a id='3.1'></a>
>> <strong><code>Azure Repos</code></strong><br>
<p></p>

> 3.2. <em>If your teammate was looking to share a python package with you (and the rest of the team), which Azure DevOps service would they use?</em><br><a id='3.2'></a>
>> <strong><code>Azure Artefacts</code></strong><br>
<p></p>

> 3.2. <em>In which Azure DevOps service would your application be built and released?</em><br><a id='3.2'></a>
>> <strong><code>Azure Pipelines</code></strong><br>
<p></p>

<br>

<h2>Task 4 . Azure Repos</h2>

<h3 align="left"> Answer the questions below</h3>

> 4.1. <em>What Azure Repo security practice allows you to secure important branches by, for example, requiring a minimum number of approvers?</em><br><a id='4.1'></a>
>> <strong><code>branch policies</code></strong><br>
<p></p>

> 4.2. <em>What would you use to ensure only certain authorised users can approve changes?</em><br><a id='4.2'></a>
>> <strong><code>branch protection rules</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/2e2f036d-82ca-455e-944e-c29fcc7d4a57)

<br>

<h2>Task 5 . Azure Pipelines</h2>


<h3 align="left"> Answer the questions below</h3>

> 5.1. <em>The Azure App Service runs within a what?</em><br><a id='5.1'></a>
>> <strong><code>Azure App Service Plan</code></strong><br>
<p></p>


> 5.2. <em>Azure App Service has some security benefits, including the ability to protect against which vulnerability?</em><br><a id='5.2'></a>
>> <strong><code>subdomain takeovers</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/47601ca9-e336-40f7-abc7-8a037ce438a4)

![image](https://github.com/user-attachments/assets/0b84c70e-996a-48a2-8775-e00cd9851012)

![image](https://github.com/user-attachments/assets/b4d835de-bea7-48d9-91a0-6c312961bbcf)

![image](https://github.com/user-attachments/assets/1961cc8e-f1d0-4796-bafd-9893aa63b514)

![image](https://github.com/user-attachments/assets/f34a23e3-9175-4d0c-b7d2-956818f57239)


<br>

<h2>Task 6 . Azure Pipelines</h2>
<h3>Securing Pipelines</h3>h3>
<p>As a DevSecOps Engineer, part of your job would be to implement security controls around the application and deployment code written by the dev team. Let's take the FinkFactory web app deployment pipeline YAML as an example. As described in the previous task, this YAML pipeline sets up various reusable variables before the 'steps' section defines a series of tasks that deploy the application code as an Azure App Service. We will now take a look at some ways we can secure this process.</p>

<p>[ ... ]</p>

<h3 align="left"> Answer the questions below</h3>

> 6.1. <em>Azure CLI supports bash and what other language? </em><br><a id='6.1'></a>
>> <strong><code>PowerShell</code></strong><br>
<p></p>

> 6.2. <em>What flag is used in the Azure CLI command/script to enforce HTTPS on the Azure App Service? </em><br><a id='6.2'></a>
>> <strong><code>--httpsOnly=true</code></strong><br>
<p></p>

> 6.3. <em>We were able to require a minimum amount of reviewers using a what?  </em><br><a id='6.3'></a>
>> <strong><code>Branch Policy</code></strong><br>
<p></p>


![image](https://github.com/user-attachments/assets/ba13ce04-83fc-4fbe-8ef7-9df236a59abf)

![image](https://github.com/user-attachments/assets/438a24b1-5657-4aab-94fe-2745a1192717)

![image](https://github.com/user-attachments/assets/6595f5d2-6e2b-4eb9-a3f6-e0b6f072839c)

![image](https://github.com/user-attachments/assets/32a05283-e785-4395-b3a7-148bf218c75d)

![image](https://github.com/user-attachments/assets/38d1b566-9909-464f-8b41-d09895bc2c6c)

<br>

<h2>Task 7 . Conclusion</h2>

<h3>A Warm Welcome to the World of Azure DevSecOps</h3>
<p>This room has introduced you to your new role as DevSecOps Engineer at FinkTech as well as DevSecOps in the world of Azure. Step by step, you have been down around your new ‘office in the cloud’, so as you continue to learn more advanced Azure DevSecOps topics, you can be familiar with your environment and all of the services that integrate to enable FinkFactory's workflow. In the process, we have covered:<br>

The benefits of hosting a web application in a cloud-hosted environment<br>

- Azure DevOps and it's landscape<br>
-Azure Repos service and some security considerations <br>
-Azure Pipelines, Azure YAML Pipelines, and Azure App Services / App Service plans<br>
-Methods of securing a web application running in an Azure web applications and how to implement some basic branch policies</p>


<h3 align="left"> Answer the questions below</h3>

> 7.1. <em>All done!</em><br><a id='7.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>


![image](https://github.com/user-attachments/assets/d33f748e-7ff3-44b8-9613-7bb21a6232f5)

![image](https://github.com/user-attachments/assets/5cb41a0a-7ab9-4709-bc95-754f7a10264d)

<br>
<br>


![image](https://github.com/user-attachments/assets/e74b42b6-0597-43bd-8000-81c89017d1bc)

![image](https://github.com/user-attachments/assets/da8d4f7a-177d-432a-97ff-7521aa6698a4)


![image](https://github.com/user-attachments/assets/54542d83-4372-4568-ab84-9e72f53c2cf6)

![image](https://github.com/user-attachments/assets/e91925d8-2ea2-4312-bd91-9bacfbd0be61)

![image](https://github.com/user-attachments/assets/c9938d7a-e20b-4cc8-a652-e678c1f55a36)


<br>
<br>

<h1 align="center">Room Completed</h1>
<br>
<p align="center"><img width="1000px" src="https://github.com/user-attachments/assets/8e4e9166-b6dc-43ba-82c2-f38d42bacb82"><br>
                  <img width="1000px" src="https://github.com/user-attachments/assets/6d77d2c7-50bf-4a4e-9bd1-2d3deef073d0"></p>


<h1 align="center"> My TryHackMe Journey</h1>
<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 11 2025      | 401      |     204ᵗʰ    |      4ᵗʰ     |     721ˢᵗ   |    15ᵗʰ    |  107,051  |    773    |     60    |

</div>

<p align="center"> Global All Time:  204ᵗʰ<br><br>
<img width="240px" src="https://github.com/user-attachments/assets/e2dbc695-ba3c-4d5e-badc-6305ef0f6688"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/799b2dc8-a596-4b43-8457-3a597f3261ed"> </p>

<p align="center"> Brazil All Time:    4ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/89053e09-b1cd-45f0-8dea-d1e98862d74e"> </p>
"> </p>

<p align="center"> Global monthly:    721ˢᵗ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/60a3f005-9d8e-43cb-86a1-6d2e62b3e4c5"> </p>

<p align="center"> Brazil monthly:    15ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/b77b4e0d-751a-46ad-af56-2511e8aa85fe"> </p>

<h1 align="center">Thanks for coming!!!</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<h1 align="center">Thank you</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a>  and <a href="https://tryhackme.com/p/rePl4stic">rePl4stic</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 



