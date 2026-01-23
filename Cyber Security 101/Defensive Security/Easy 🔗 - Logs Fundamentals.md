<h3> Welcome to the <em>TryHackMe ...</em></h3>
<h1>Cyber Security 101 learning path ><br>Defensive Security > Logs Fundamentals</h1>
<p>Learn what logs are and how to analyze them for effective investigation.</p><br>
<p>October 27, 2024<br></p><br>

<div style="display: flex; justify-content: center; align-items: center;">
    <img src="https://github.com/user-attachments/assets/5bd77071-e8ae-4204-b47f-13c8f925a0b7" width="150px" height="150px"/>
</div>
<br>

![image](https://github.com/user-attachments/assets/6fdd2484-6ea9-4a81-ab98-3b2efed30fe0)


<p>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s key part of my <strong>174</strong>-day-streak.<br><br>
Let´s get started!!<br><br>
Access this TryHackMe Room clicking <a href="https://tryhackme.com/r/room/logsfundamentals">Logs Fundamentals</a>.</p><br>

<h2>Task 1 - Introduction to Logs</h2>
<p>Attackers are clever. They avoid leaving maximum traces on the victim’s side to avoid detection. Yet, the security team successfully determines how the attack was executed and is even sometimes successful in finding who was behind the attack.<br>

Suppose a few policemen are investigating the disappearance of a precious locket in a snowy jungle cabin. They observed that the wooden door of the cabin was brutally damaged, and the ceiling collapsed. There were some footprints on the snowy path to that cabin. Lastly, they discovered some CCTV footage from a neighbouring residence. By placing together all these traces, the police successfully determined who was behind the attack. Various traces are found in several such cases; putting all these together takes you closer to the criminal.</p>

![image](https://github.com/user-attachments/assets/d80284a3-3dca-486b-bb07-b233b493d494)

<p>It seems like these traces play a big role in the investigations.<br>

What if something happened within a digital device? Where do we find all these traces to investigate further?<br>

There are various places inside a system where the traces of an attack could be fetched. The logs contain most of these traces. Logs are the digital footprints left behind by any activity. The activity could be a normal one or the one with malicious intent. Tracing down the activity and the individual behind the execution of that activity becomes easier through logs.</p>

![image](https://github.com/user-attachments/assets/e657a883-250b-4ae7-ad5d-0c77cb38251e)

<h3>Use Cases of Logs</h3>
<p>The following are some key areas in which the logs play an integral role.</p>

![image](https://github.com/user-attachments/assets/048c2ba2-2896-449c-8c31-1cd5a7fef4b8)

<p>This room will equip you with an understanding of various types of logs maintained in different systems. We will also be practically investigating logs as traces of different attacks.</p>

<h3>Learning Objectives</h3>
<ul style="list-style-type:square">
    <li>The different types of logs</li>
    <li>How to analyze logs</li>
    <li>Analyzing Windows Event logs</li>
    <li>Analyzing Web Access logs</li>  
</ul></p>

> 1.1 - <em>Where can we find the majority of attack traces in a digital system?</em>
>> <strong><code>Logs</code></strong>
<p></p><br>

<h2>Task 2 - Types of Logs</h2>
<br>

<p>In the previous task, we saw various use cases of logs. But there is a challenge. Imagine you have to investigate an issue in a system through the logs; you open the log file of that system, and now you are lost after seeing numerous events of different categories.<br>

Here is the solution: Logs are segregated into multiple categories according to the type of information they provide. So now you just need to look into the specific log file for which the issue relates.<br>

For example, you need to investigate the successful logins from yesterday at a specific timeframe in Windows OS. Instead of looking into all the logs, you only need to see the system’s Security Logs to find the login information. We also have other types of logs that are useful in investigating different incidents. Let’s have a look at them.</p>

![image](https://github.com/user-attachments/assets/1a71d7ee-2f66-4ee5-a599-affe50849287)

![image](https://github.com/user-attachments/assets/01b2a5c5-80ca-4b0a-a70d-cb5911f465b4)

<p><code>Note</code>: There can be various other types of logs depending on the different applications and the services they provide.<br>

Now that we understand what these logs are and how various types of logs can be helpful in different scenarios, let’s see how we analyze these logs and extract valuable information required from them. Log Analysis is a technique for extracting valuable data from logs. It involves looking for any signs of abnormal or unusual activities. Searching for a specific activity or abnormalities in the logs with the naked eye is impossible. For this reason, we have several manual and automated techniques for log analysis. We will manually carry out log analysis on Windows and Web Server Access Logs in the upcoming tasks.</p>

> 2.1 - <em>Which type of logs contain information regarding the incoming and outgoing traffic in the network?</em>
>> <strong><code>Network Logs</code></strong>
<p></p><br>

> 2.2 - <em>Which type of logs contain the authentication and authorization events?</em>
>> <strong><code>Security Logs</code></strong>
<p></p><br>

<h2>Task 3 - Windows Event Logs Analysis</h2>
<br>

<p>Like other operating systems, Windows OS also logs many of the activities that take place. These are stored in segregated log files, each with a specific log category. Some of the crucial types of logs stored in a Windows Operating System are:</p>

<ul style="list-style-type:square">
    <li><code>Application</code>: There are many applications running on the operating system. Any information related to those applications is logged into this file. This information includes errors, warnings, compatibility issues, etc.</li>
    <li><code>System</code>: The operating system itself has different running operations. Any information related to these operations is logged in the System log file. This information includes driver issues, hardware issues, system startup and shutdown information, services information, etc.</li>
    <li><code>Security</code>: This is the most important log file in Windows OS in terms of security. It logs all security-related activities, including user authentication, changes in user accounts, security policy changes, etc.</li>
</ul>

<p>Besides these, several other log files in the Windows operating system are designed for logging activities related to specific actions and applications.<br>

Unlike other log files studied in the previous tasks, which had no built-in application to view them, Windows OS has a utility known as Event Viewer, which gives a nice graphical user interface to view and search for anything in these logs.<br>

To open Event Viewer, click on the Start button of Windows and type ‘Event Viewer’. It will open the Event Viewer for you, as shown below. The highlighted area in the screenshot below shows the different available logs. </p>

![image](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1719215860668)

<p>You can click ‘Windows Logs’ from the highlighted section to see the different types of logs we discussed at the beginning of this task. 
The first highlighted portion shows the different log files. When we click one of these log files, we will see the different logs, as can be seen in the second highlighted portion. Lastly, in the third highlighted portion, we have different options for analyzing the logs.</p>

![image](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1719215860882)

<p>Let’s double-click on one of these logs to see its contents. </p>

![image](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1719215860911)

<p>This is how a Windows event log looks. It has different fields. The major fields are discussed below:</p>

<ul style="list-style-type:square">
    <li><code>Description</code>: This field has a detailed information of the activity..</li>
    <li><code>Log Name</code>: The Log Name indicates the log file name..</li>
    <li><code>Logged</code>: This field indicates the time of the activity.</li>
    <li><code>Event ID</code>: Event IDs are unique identifiers for a specific activity..</li>
</ul>

<p>Numerous event IDs are available in Windows event logs. We can use these event IDs to search for any specific activity. For example, event ID 4624 uniquely identifies the activity of a successful login, so you only need to search for this event ID 4624 when investigating successful logins.<br>

Here is a table of some important Event IDs in Windows Operating System.</p>

![image](https://github.com/user-attachments/assets/2c628482-d9f6-420f-be0e-284fb2ab53f7)

<p>There are many more event IDs. It is not necessary to remember all of them, but it is good to remember the crucial event IDs.<br>

Event Viewer allows us to search for the logs related to a specific event ID with its ‘Filter Current Log’ feature. We can click on this feature to apply any filter. </p>

![Image](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1719215860856)

<p>When we click on the ‘Filter Current Log’ option, we will be prompted to enter the event IDs we want to filter. In the screenshot below, I filtered the event ID 4624. </p>

![Image](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1719215860786)

<p>Once I hit the 'OK' button, I can see all the logs with the event ID: 4624. I can now view any of these logs by double-clicking them. </p>

![Image](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1719215860652)

<h3>Exercise</h3>
<p>On Friday, a critical organization reported being a victim of a cyber attack. Upon investigation, critical data was exfiltrated from a file server in the organization’s network. The security team was successful in determining the user name and IP address of the compromised system in the network, which had access to the file server at the time of the attack.<br>

You are tasked to find out the activities of the attacker in this compromised system before he took access to the file server.<br>

First, let’s start the Virtual Machine by pressing the Start Machine button given below. The machine will start in Split-Screen view.</p>

<p>In case the VM is not visible, use the blue Show Split View button at the top of the page. The machine will open in GUI for you. You can also connect with the machine via VPN using the RDP credentials given below.
</p>

![image](https://github.com/user-attachments/assets/58dfe63d-03b1-405d-9e85-6222b7d936c2)

<p><code>Note</code>: All the questions below can be answered by looking into the logs.</p>

<br>

> 3.1 - <em>What is the name of the last user account created on this system?</em>
>> <strong><code>hacked</code></strong>
<p></p><br>

![image](https://github.com/user-attachments/assets/485b28de-6880-4e00-a3a1-c5d9276c9ad5)

<br>

![image](https://github.com/user-attachments/assets/b17a6d13-9572-4214-8a41-97ad544616f8)

<br>

![image](https://github.com/user-attachments/assets/7c679cd9-ae61-49a0-9faa-aca4da9eb043)

<br>


![image](https://github.com/user-attachments/assets/ebb616bf-446e-484e-9ddb-b486f8787763)

<br>

![image](https://github.com/user-attachments/assets/f08f4167-7ceb-4081-955b-2190453289dd)

<br>

![image](https://github.com/user-attachments/assets/4cfa115b-0d0e-4d34-8eaa-bf397605ee39)

<br>

![image](https://github.com/user-attachments/assets/fe49c924-7945-4d10-a52f-f3de08e075fd)

<br>

> 3.2 - <em>Which user account created the above account?</em>
>> <strong><code>Administrator</code></strong>
<p></p><br>

> 3.3 - <em>On what date was this user account enabled? Format: M/D/YYYY</em>
>> <strong><code>6/7/2024</code></strong>
<p></p><br>

![image](https://github.com/user-attachments/assets/4097a53c-ca52-41bd-add4-b2bd4f308a24)

<br>


![image](https://github.com/user-attachments/assets/c5aeaa45-0137-4a20-8b90-47856a982c19)

<br>

> 3.4 - <em>Did this account undergo a password reset as well? Format: Yes/No?</em>
>> <strong><code>Yes</code></strong>
<p></p><br>


![image](https://github.com/user-attachments/assets/956dbb54-ed3d-40b1-94fa-ba7dc038981e)

<br>

![image](https://github.com/user-attachments/assets/7f2a8d0b-cf60-4e15-8b0c-756874e935c1)


<h2>Task 4 - Web Server Access Logs Analysis</h2>
<br>

<p>We interact with many websites daily. Sometimes, we just want to view the website, and sometimes, we want to log in or upload a file into any available input field. These are just different kinds of requests we make to a website. All these requests are logged by the website and stored in a log file on the web server running that website.<br>

This log file contains all the requests made to the website along with the information on the timeframe, the IP requested, the request type, and the URL. Following are the fields taken from a sample log from an Apache web server access log file which can be found in the directory: /var/log/apache2/access.log  </p>


> 4.1 - <em>What is the IP which made the last GET request to URL: “/contact”?</em>
>> <strong><code>10.0.0.1</code></strong>
<p></p><br>

<pre><code>$ root@ip-[REDACTED]:~/Rooms/logs# cat access.log | grep "/contact"
</code></pre>

![image](https://github.com/user-attachments/assets/f1c8b17d-d1c4-4c5b-bcc2-26fca7b9b530)


> 4.2 - <em>When was the last POST request made by IP: “172.16.0.1”? </em>
>> <strong><code>06/Jun/2024:13:55:44</code></strong>
<p></p><br>

<pre><code>$ root@ip-[REDACTED]:~/Rooms/logs# grep "172.16.0.1" access.log
</code></pre>

![image](https://github.com/user-attachments/assets/1570d794-4207-401f-9a53-dd68d5aac7da)

<br>


> 4.3 - <em>Based on the answer from question number 2, to which URL was the POST request made? </em>
>> <strong><code>/contact</code></strong>
<p></p><br>


<pre><code>$ root@ip-[REDACTED]:~#  sqlmap -u "http://[REDACTED]/ai/includes/user_login?email=rosana@local.com&password=test" --level=5 --dbs</code></pre>

<BR>

<h2>Task 5 - Conclusion</h2>
<br>

> 5.1 - <em>Complete the room.</em>
>> <strong><code>No answer needed</code></strong>
<p></p><br>


<h2>Room Complete</h2>
<br>
<p>Keep learning, keep growing!<br>

![image](https://github.com/user-attachments/assets/4fbd22ba-ae68-418e-913d-46c201bed248)


<h2>My journey</h2>
<br>
<p></p>Following I share the status of my journey in TryHackMe.</p>

![image](https://github.com/user-attachments/assets/58de92f3-0c79-4dbf-bc18-74fade6151e8)

<p></p>

<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>
