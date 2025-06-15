<h5 align="center">December 3, 2024<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{211}}$$-day-streak in  <a href="https://tryhackme.com/">TryHackMe</a>.</h5>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Advent of Cyber 2024}}$$</h1>

<h5 align="center">Dive into the wonderful world of cyber security by engaging<br>
in festive beginner-friendly exercises every day in the lead-up to Christmas!</h5>

<p align="center">
<img height="90px" hspace="20" src="https://github.com/user-attachments/assets/0d8d7f29-525a-49ad-85ba-9223bdec089b">
<img width="500px" src="https://github.com/user-attachments/assets/57999429-f784-46a1-81ab-4d68041f470f"></p>

<p align="center">Access this 🆓 TryHackMe CTF challenge clicking <a href="https://tryhackme.com/r/room/adventofcyber2024">Advent of Cyber 2024</a>.</p>

<h2 align="center"> $$\textcolor{yellow}{\textnormal{Day 3 - Log Analysis}}$$<br>
$$\textcolor{yellow}{\textnormal{Even if I wanted to go, their vulnerabilities wouldn't allow it.}}$$</h2>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/e7bce5af-bc21-491e-833d-ce1bfbf389ff"></p>


<h5 align="center">Today's AoC challenge follows a rather unfortunate series of events for the Glitch. Here is a little passage which sets the scene for today's task:</h5>

<h5 align="center"><em>Late one Christmas evening the Glitch had a feeling,<br>
Something forgotten as he stared at the ceiling.<br>
He got up out of bed and decided to check,<br>
A note on his wall: ”Two days! InsnowSec”.<br>
<br>
With a click and a type he got his hotel and tickets,<br>
And sank off to sleep to the sound of some crickets.<br>
Luggage in hand, he had arrived at Frosty Pines,<br>
“To get to the conference, just follow the signs”.<br>
<br>
Just as he was ready the Glitch got a fright,<br>
An RCE vulnerability on their website ?!?<br>
He exploited it quick and made a report,<br>
But before he could send arrived his transport.<br>
<br>
In the Frosty Pines SOC they saw an alert,<br>
This looked quite bad, they called an expert.<br>
The request came from a room, but they couldn’t tell which,<br>
The logs saved the day, it was the room of…the Glitch.</em></h5>

<br>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/6045ad39-ba6d-4420-91cd-cb618b51746b"></p>

<p>In this task, we will cover how the SOC team and their expert were able to find out what had happened (Operation Blue) and how the Glitch was able to gain access to the website in the first place (Operation Red). Let's get started, shall we?</p>

<h3><strong>Learning Objectives</strong></h3>
<p>While it might seem like using the SOC superpower makes things super easy, that is not always the case. There are cases which can act as Kryptonite to the SOC superpower
    
<ul style="list-style-type:square">
    <li>Learn about Log analysis and tools like ELK.</li>
    <li>Learn about KQL and how it can be used to investigate logs using ELK.</li>
    <li>Learn about RCE (Remote Code Execution), and how this can be done via insecure file upload.</li>
</ul></p>

<h3><strong>Connecting to the Machine</strong></h3>

<p>Before moving forward, review the questions in the connection card below:</p>

<p align="center"><img width="300px" src="https://github.com/user-attachments/assets/c725d61b-a27a-4f89-8028-18acf18ae691"></p>

<p>Click on the green <code>Start Machine</code> button below to start the virtual machine for the practical. The practical VM may take 5 minutes to become accessible.</p>

<p><code>Start Machine</code></p>

<p>You will also need to start the AttackBox by pressing the <code>Strat AttackBox</code> button at the top of the room. Alternatively, you can connect your own hacking machine by using the TryHackMe VPN.</p>

<br>
<br>
<h3><strong>OPERATION BLUE</strong></h3>
<p>In this section of the lesson, we will take a look at what tools and knowledge is required for the blue segment, that is the investigation of the attack itself using tools which enable is to analyse the logs.<br>

For the first part of Operation Blue, we will demonstrate how to use ELK to analyse the logs of a demonstration web app - WareVille Rails. Feel free to following along for practice. </p>

<h3><strong>Log Analysis & Introducing ELK</strong></h3>
<p>Log analysis is crucial to blue-teaming work, as you have likely discovered through this year's Advent of Cyber.<br>

Analysing logs can quickly become overwhelming, especially if you have multiple devices and services. ELK, or Elasticsearch, Logstash, and Kibana, combines data analytics and processing tools to make analysing logs much more manageable. ELK forms a dedicated stack that can aggregate logs from multiple sources into one central place.<br>

Explaining how ELK collates and processes these logs is out of the scope of today's task. However, if you wish to learn more, you can check out the Investigating with ELK 101 room. For now, it's important to note that multiple processes behind the scenes achieve this.<br>

The first part of today's task is to investigate the attack on Frosty Pines Resort's Hotel Management System to see what it looks like to a blue teamer. You will then test your web app skills by recreating the attack.</p>

<h3><strong>Using ELK</strong></h3>

<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/635631ea-e3aa-49fe-8972-9a7551f4aedf"></p>

<p>We will need to select the collection that is relevant to us. A collection is a group of logs. For this stage of Operation Blue, we will be reviewing the logs present within the "wareville-rails" collection. To select this collection, click on the dropdown on the left of the display.</p>

<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/b6cde583-34ce-40fc-a5f3-7a8b3e9e8398"></p>

<p>Once you have done this, you will be greeted with a screen saying, "No results match your search criteria". This is because no logs have been ingested within the last 15 minutes. Do not panic; we will discuss how to change this shortly.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/0755da54-d44a-47f3-9ba4-1c7b422094cf"></p>

<p>To change the date and time, click the text located on the right side of the box that has the calendar icon. Select "Absolute" from the dropdown, where you can now select the start date and time. Next, click on the text on the right side of the arrow to and repeat the process for the end date and time.<br>

For the WareVille Rails collection, we will need to set the start time to October 1 2024 00:00:00, and the end time to October 1 23:59:59<br>

If you are stuck, refer to the GIF below. Please note that the day and time in this demonstration of WareVille Rails will differ from the times required to review the FrostyPines Resorts collection in the second half of the practical .</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/fa18d7a2-bea2-491c-a4d9-f9c7e2cf4f19"></p>

<p>Now that we can see some entries, let's go over the basics of the Kibana Discover UI.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/cf05c14d-8b3b-44c0-9f1f-44d9a402b00c"></p>

<p>.....</p>

<h3><strong>Kibana Query Language (KQL)</strong></h3>
<p>KQL, or Kibana Query Language, is an easy-to-use language that can be used to search documents for values. For example, querying if a value within a field exists or matches a value. If you are familiar with Splunk, you may be thinking of SPL (Search Processing Language).<br>

For example, the query to search all documents for an IP address may look like ip.address: "10.10.10.10". </p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/6fb79fe5-f23e-4519-a7be-42a62965be0b"></p>

<p>Alternatively, Kibana also allows using Lucene query, an advanced language that supports features such as fuzzy terms (searches for terms that are similar to the one provided), regular expressions, etc. For today's task, we will stick with using KQL, which has been enabled by default. The table below contains a mini-cheatsheet for KQL syntax that you may find helpful in today's task.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/36509b11-5911-4059-9766-0c31555ed416"></p>

<h3><strong>Investigating a Web Attack With ELK</strong></h3>
<p><strong>Scenario</strong>: Thanks to our extensive intrusion detection capabilities, our systems alerted the SOC team to a web shell being uploaded to the WareVille Rails booking platform on Oct 1, 2024. Our task is to review the web server logs to determine how the attacker achieved this.<br>

If you would like to follow along, ensure that you have the "<strong>wareville-rails</strong>" collection selected like so:</p>

<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/d998a02a-7221-49c0-958e-319ccf46517f"></p>

<p>To investigate this scenario, let's change the time filter to show events for the day of the attack, setting the start date and time to "<strong>Oct 1, 2024 @ 00:00:00.000</strong>" and the end date and time to "<strong>Oct 2, 2024 @ 00:00:00.000</strong>".</p>

<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/e0825547-f725-4ab3-9d83-b991d033e3a1"></p>

<p>You will see the logs have now populated within the display. Please note that the quantity of entries (hits) in this task may differ to the amount on the practical VM.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/b5e72d01-6cce-4362-adb2-d192cb6d309b"></p>

<p>An incredibly beneficial feature of ELK is that we can filter out noise. A web server (especially a popular one) will likely have a large number of logs from user traffic—completely unrelated to the attack. Using the fields pane on the left, we can click on the "+" and "-" icons next to the field to show only that value or to remove it from the display, respectively.<br>

<strong>Fun fact</strong>: Clicking on these filters is actually just applying the relevant KQL syntax.<br>

Note in the GIF below how the logs are being filtered to only show logs containing the IP address 10.13.27.115 (reducing the count from 1,028 to 423 hits). We can combine filtering multiple fields in or out to drill down specifically into the logs.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/54b9482e-c44f-469c-8cd9-362ceae977a7"></p>

<p>To remove applied filters, simply click on the "x" alongside the filter, just below the search bar.</p>

<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/a7b8de18-9865-4fb0-a721-3624a9cf465b"></p>

<p>In this investigation, let's look at the activity of the IP address 10.9.98.230. We can click on the "<strong>clientip</strong>" field to see the IPs with the most values.</p>

<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/1c4944a7-d1db-4e46-a833-7342fd6a4305"></p>

<p>Using the timeline at the top, we can see a lot of activity from this IP address took place between 11:30:00 and 11:35:00. This would be a good place to begin our analysis.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/0416af9f-d90a-4015-9994-2f9275badaa6"></p>

<p>Each log can be expanded by using the ">" icon located on the left of the log/document. Fortunately, the logs are pretty small in this instance, so we can browse through them to look for anything untoward.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/3d8327e9-6e39-4f73-86ef-58d0740d68eb"></p>

<p>After some digging, a few logs stand out. Looking at the request field, we can see that a file named "shell.php" has been accessed, with a few parameters "c" and "d" containing commands. These are likely to be commands input into some form of web shell.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/c7f0ef68-1885-40a9-be72-5e4c2a16e876"></p>

<p>Now that we have an initial lead, let’s use a search query to find all logs that contain "shell.php". Using the search bar at the top, the query message: "shell.php" will search for all entries of "shell.php" in the message field of the logs.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/62cab578-ab56-406a-925e-0c03fac48658"></p>

<br>
<br>
<h3><strong>OPERATION RED</strong></h3>
<p>In this section we will now take a look at the red aspect. In other words, the attack itself and how it was carried out.</p>

<h3>Why Do Websites Allow File Uploads</h3>
<p>File uploads are everywhere on websites, and for good reason. Users often need to upload files like profile pictures, invoices, or other documents to update their accounts, send receipts, or submit claims. These features make the user experience smoother and more efficient. But while this is convenient, it also creates a risk if file uploads aren't handled properly. If not properly secured, this feature can open up various vulnerabilities attackers can exploit.</p>

<h3>File Upload Vulnerabilities</h3>
<p>File upload vulnerabilities occur when a website doesn't properly handle the files that users upload. If the site doesn't check what kind of file is being uploaded, how big it is, or what it contains, it opens the door to all sorts of attacks. For example:</p>
- RCE: Uploading a script that the server runs gives the attacker control over it.<br>
- XSS: Uploading an HTML file that contains an XSS code which will steal a cookie and send it back to the attacker's server.<br>

<p>These can happen if a site doesn't properly secure its file upload functionality.</p>

<h3>Why Unrestricted File Uploads Are Dangerous</h3>
<p>Unrestricted file uploads can be particularly dangerous because they allow an attacker to upload any type of file. If the file's contents aren't properly validated to ensure only specific formats like PNG or JPG are accepted, an attacker could upload a malicious script, such as a PHP file or an executable, that the server might process and run. This can lead to code execution on the server, allowing attackers to take over the system.<br>

Examples of abuse through unrestricted file uploads include:</p>
- Uploading a script that the server executes, leading to RCE.<br>
- Uploading a crafted image file that triggers a vulnerability when processed by the server.<br>
- Uploading a web shell and browsing to it directly using a browser.<br>

<h3>Usage of Weak Credentials</h3>
<p>One of the easiest ways for attackers to break into systems is through weak or default credentials. This can be an open door for attackers to gain unauthorised access. Default credentials are often found in systems where administrators fail to change initial login details provided during setup. For attackers, trying a few common usernames and passwords can lead to easy access.<br>

Below are some examples of weak/default credentials that attackers might try:</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/edb8f789-4ce8-4750-ae7d-50edd10a4e97"></p>

<p>Attackers can use tools or try these common credentials manually, which is often all it takes to break into the system.</p>

<h3>What is Remote Code Execution (RCE)</h3>
<p>Remote code execution (RCE) happens when an attacker finds a way to run their own code on a system. This is a highly dangerous vulnerability because it can allow the attacker to take control of the system, exfiltrate sensitive data, or compromise other connected systems.</p>


<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/4dca3ef9-062a-4b6d-b35a-b9ca2bba7429"></p>


<h3>What Is a Web Shell</h3>
<p>.....</p>


<h3>Practice Makes Perfect</h3>
<p>.....</p>



<h3>Exploiting RCE via File Upload</h3>
<p>.....</p>



<h3>Making the Most of It</h3>
<p>.....</p>



<h3>Practical</h3>
<p>.....</p>








<br>
<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em><code>BLUE</code>: Where was the web shell uploaded to?<br>
> <code>Answer format</code>: /directory/directory/directory/filename.php</em><br><a id='1.1'></a>
>> <code><strong>/media/images/rooms/shell.php</strong></code>

<br>


![image](https://github.com/user-attachments/assets/cdc49766-affe-4f69-931b-f0d3fd8b9ad0)


<br>
<br>

> 1.2. <em><code>BLUE</code>: What IP address accessed the web shell?</em><br><a id='1.2'></a>
>> <code><strong>10.11.83.34</strong></code>

<br>

![image](https://github.com/user-attachments/assets/c21daf6d-4870-45c4-8174-938af80c67d6)


<br>
<br>

> 1.3. <em><code>RED</code>: What is the contents of the flag.txt?</em><br><a id='1.3'></a>
>> <code><strong>THM{Gl1tch_Was_H3r3}</strong></code>

<br>

<br>
<br>


![image](https://github.com/user-attachments/assets/fdff286b-9b23-4056-8f55-7c6a3a944c69)

<br>

![image](https://github.com/user-attachments/assets/6819fe65-2c2f-480e-a0e4-0cde80b1bfc8)

<br>

![image](https://github.com/user-attachments/assets/4416bd98-2a36-4838-94f6-c748f9c3c2e8)

<br>

![image](https://github.com/user-attachments/assets/97865346-679d-4a67-a436-d5e1123d3563)

<br>

![image](https://github.com/user-attachments/assets/4e1fcfe4-556d-4083-b684-8f9efd8fba65)

<br>

![image](https://github.com/user-attachments/assets/657d1e8e-240c-463e-8169-8ac843302fbb)

<br>

![image](https://github.com/user-attachments/assets/8395db20-f793-40bc-8daa-13260208aca2)

<br>

![image](https://github.com/user-attachments/assets/56a917c8-ab4b-4630-a008-52132380cf76)

<br>

![image](https://github.com/user-attachments/assets/6f61a544-c2d7-42c3-8dea-f1f7ffafbade)

<br>

![image](https://github.com/user-attachments/assets/27911039-737a-44f6-8100-a64f3017bbc4)

<br>

![image](https://github.com/user-attachments/assets/fb887578-db92-44f0-8b91-cbdbf4daff1a)

<br>

![image](https://github.com/user-attachments/assets/fe89bafc-7c1a-4fe9-884c-c03ef05e5b67)


<br>

![image](https://github.com/user-attachments/assets/0477e380-0377-4dbe-9de7-028cd6d7a583)

<br>

<pre><code>http://frostypines.thm/media/images/rooms/shell.php</code></pre>

<br>

![image](https://github.com/user-attachments/assets/2c17c8c4-2608-4941-a4b1-0a8d5db16923)

<br>

<p>whoami</p>

![image](https://github.com/user-attachments/assets/be0a0ccc-29b6-4064-bbb2-e6ff85bb38f2)

<p>pwd</p>

![image](https://github.com/user-attachments/assets/8ab9823e-4298-48bc-991a-f1a12fd0a379)

<p>ls -la</p>

![image](https://github.com/user-attachments/assets/8ab9823e-4298-48bc-991a-f1a12fd0a379)

<p>cat flag.txt</p>

![image](https://github.com/user-attachments/assets/f3db3a20-0b1d-42fe-8237-46c4ed131351)

> 1.4. <em>If you liked today's task, you can learn how to harness the power of advanced ELK queries.</em><br><a id='1.4'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task Completed<a id='2'></a></h2>
<p>Keep learning, keep growing!<br>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/3059dcb7-6d8d-415f-9dcf-a772bb25a393"> </h3>

<h2>My Journey<a id='3'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| December 3, 2024  | 211      |     1,056 th |        22 nd |    2,938 th |      44 th | 58,802   |       450 |

</div>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/f5ab9c52-bc01-4d77-b6b8-252d1edee1ac"> </h3>

<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>
