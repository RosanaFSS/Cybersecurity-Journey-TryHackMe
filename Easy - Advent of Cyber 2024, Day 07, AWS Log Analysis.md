<h5 align="center">December 7,  2024<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{215}}$$-day-streak in  <a href="https://tryhackme.com/">TryHackMe</a>.</h5>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Advent of Cyber 2024}}$$</h1>

<h5 align="center">Dive into the wonderful world of cyber security by engaging<br>
in festive beginner-friendly exercises every day in the lead-up to Christmas!</h5>

<p align="center">
<img height="90px" hspace="20" src="https://github.com/user-attachments/assets/0d8d7f29-525a-49ad-85ba-9223bdec089b">
<img width="500px" src="https://github.com/user-attachments/assets/854e55ce-0938-42c1-aec9-d39e1c046530"></p>

<p align="center">Access this 🆓 TryHackMe CTF challenge clicking <a href="https://tryhackme.com/r/room/adventofcyber2024">Advent of Cyber 2024</a>.</p>

<h2 align="center"> $$\textcolor{yellow}{\textnormal{Day 7 - AWS Log Analysis}}$$<br>
$$\textcolor{yellow}{\textnormal{Oh, no. I'M SPEAKING IN CLOUDTRAIL!}}$$</h2>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/1b251b72-ef5a-4565-ad02-93a78ca644fe"></p>

<h5 align="center"> <em>As SOC-mas approached, so did the need,<br>
To provide those without, with something to read.<br>
Care4Wares tried, they made it their mission,<br>
A gift for all wares, a SOC-mas tradition.<br>
Although they had some, they still needed more,<br>
To pick up some books, they’d head to the store.<br>
The town’s favourite books, would no doubt make them jolly,<br>
They ticked off the list, as they filled up the trolley.<br>
With the last book ticked off, the shopping was done,<br>
When asked for their card, the ware handed them one.<br>
“I’m sorry” he said, as the shop clerk reclined,<br>
“I can’t sell you these books, as your card has declined.”<br>
The ware put them back, as they walked in confusion,<br>
How could this be? An attack? An intrusion?<br>
And when they logged on, the ware got a scare,<br>
To find the donations, they just weren’t there!</em></h5>

<p align="center"><img width="300px" src="https://github.com/user-attachments/assets/8da3dc9a-1afd-4994-a07a-2e98ed1423a9"></p>

<h2><strong>Monitoring in an AWS Environment</strong></h2>
<p>Care4Wares' infrastructure runs in the cloud, so they chose AWS as their Cloud Service Provider (CSP). Instead of their workloads running on physical machines on-premises, they run on virtualised instances in the cloud. These instances are (in AWS) called EC2 instances (Amazon Elastic Compute Cloud). A few members of the Wareville SOC aren't used to log analysis on the cloud, and with a change of environment comes a change of tools and services needed to perform their duties. Their duties this time are to help Care4Wares figure out what has happened to the charity's funds; to do so, they will need to learn about an AWS service called CloudWatch.</p>

<h3><strong>CloudWatch</strong></h3>
<p> AWS CloudWatch is a monitoring and observability platform that gives us greater insight into our AWS environment by monitoring applications at multiple levels. CloudWatch provides functionalities such as the monitoring of system and application metrics and the configuration of alarms on those metrics for the purposes of today's investigation, though we want to focus specifically on CloudWatch logs. Running an application in a cloud environment can mean leveraging lots of different services (e.g. a service running the application, a service running functions triggered by that application, a service running the application backend, etc.); this translates to logs being generated from lots of different sources. CloudWatch logs make it easy for users to access, monitor and store the logs from all these various sources. A CloudWatch agent must be installed on the appropriate instance for application and system metrics to be captured.<br>

A key feature of CloudWatch logs that will help the Warevile SOC squad and us make sense of what happened in their environment is the ability to query application logs using filter patterns. Here are some CloudWatch terms you should know before going further:</p>
  
<ul style="list-style-type:square">
    <li><code>Log Events</code>: A log event is a single log entry recording an application "event"; these will be timestamped and packaged with log messages and metadata.</li>
    <li><code>Log Streams</code>: Log streams are a collection of log events from a single source.</li>
    <li><code>Log Groups</code>: Log groups are a collection of log streams. Log streams are collected into a log group when logically it makes sense, for example, if the same service is running across multiple hosts.</li>
</ul></p>

<h3><strong>CloudTrail</strong></h3>
<p>CloudWatch can track infrastructure and application performance, but what if you wanted to monitor actions in your AWS environment? These would be tracked using another service called AWS CloudTrail. Actions can be those taken by a user, a role (granted to a user giving them certain permissions) or an AWS service and are recorded as events in AWS CloudTrail. Essentially, any action the user takes (via the management console or AWS CLI) or service will be captured and stored. Some features of CloudTrail include:</p>

<ul style="list-style-type:square">
    <li><code>Always On</code>: CloudTrail is enabled by default for all users</li>
    <li><code>JSON-formatted:</code>: All event types captured by CloudTrail will be in the CloudTrail JSON format</li>
    <li><code>Event History</code>:When users access CloudTrail, they will see an option "Event History", event history is a record of the actions that have taken place in the last 90 days. These records are queryable and can be filtered on attributes such as "resource" type.</li>
    <li><code>Trails</code>: The above-mentioned event history can be thought of as the default "trail," included out of the box. However, users can define custom trails to capture specific actions, which is useful if you have bespoke monitoring scenarios you want to capture and store <code>beyond the 90-day event history retention period</code>.</li>
    <li><code>Deliverable</code>: As mentioned, CloudWatch can be used as a single access point for logs generated from various sources; CloudTrail is no different and has an optional feature enabling <code>CloudTrail logs to be delivered to CloudWatch</code></li>
</ul></p>


<p align="center"><img height="150px" src="https://github.com/user-attachments/assets/a8e16f4d-0576-450e-b6ed-224408802cd1"></p>

<p>As mentioned, Cloudtrail helps capture and record actions taken. These actions could be interactions with any number of AWS services. For example, services like <code>S3</code> (Amazon Simple Storage Service used for object storage) and <code>IAM</code> (AWS's Identity and Access Management service can be used to secure access to your AWS environment with the creation of identities and the assigning of access permissions to those identities) will have actions taken within their service recorded. These recorded events can be very helpful when performing an investigation.</p>

<h2><strong>Intro to JQ</strong></h2>

<h3><strong>What is JQ?</strong></h3>

<p>Earlier, it was mentioned that Cloudtrail logs were JSON-formatted. When ingested in large volumes, this machine-readable format can be tricky to extract meaning from, especially in the context of log analysis. The need then arises for something to help us transform and filter that JSON data into meaningful data we can understand and use to gain security insights. That's exactly what JQ is (and does!). Similar to command line tools like sed, awk and grep, JQ is a lightweight and flexible command line processor that can be used on JSON.</p>


<p align="center"><img height="150px" src="https://github.com/user-attachments/assets/267f0ad7-9a3d-4445-b4cf-f8f6a8e9fe22"></p>

<h3><strong>How Can It Be Used?</strong></h3>
<p>Now, let's take a look at how we use JQ to transform and filter JSON data. The wares being the wares, they stored their shopping list from the trip to the bookstore in JSON format. Let's take a look at that:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/87e0400b-b3b1-4bb2-9e64-fa9896a0f447"></p>


<p>JQ takes two inputs: the filter you want to use, followed by the input file. We start our JQ filter with a . which just tells JQ we are accessing the current input. From here, we want to access the array of values stored in our JSON (with the []). Making our filter a .[]. For example, let’s run the following command. </p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/5abadbbf-f0d4-4b7b-a6d8-298fb01ac3c1"></p>

<p>The command above would result in this output:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/7e7c29da-7ef8-4e90-876a-97ff287ee761"></p>

<p>Once we've accessed the array, we can grab elements from that array by going one step deeper. For example, we could run this JQ command:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/0fc18ac7-3319-457b-ace9-98adcff7e15f"></p>

<p>If we wanted to view all the book titles contained within this JSON file, this would return a nicely formatted output like this:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/5d69677e-6ded-486f-9325-a79caeddf744"></p>

<p>That's a lot nicer to look at, isn't it? It gives you an idea of what JQ is and what it does. Of course, JQ can filter and transform JSON data in many additional ways. In our upcoming investigation, we'll see the tool in action.</p>

<h2><strong>The Peculiar Case of Care4Wares’ Dry Funds</strong></h2>
<p>Now that we have refreshed our knowledge of AWS Cloudtrail and JQ alongside McSkidy, let’s investigate this peculiar case of Care4Wares’ dry funds.<br>

<p>The responsible ware for the Care4Wares charity drive gave us the following info regarding this incident:</p>

<p><em>We sent out a link on the 28th of November to everyone in our network that points to a flyer with the details of our charity. The details include the account number to receive donations. We received many donations the first day after sending out the link, but there were none from the second day on. I talked to multiple people who claimed to have donated a respectable sum. One showed his transaction, and I noticed the account number was wrong. I checked the link, and it was still the same. I opened the link, and the digital flyer was the same except for the account number.</em></p>

<p>McSkidy recalls putting the digital flyer, <code>wareville-bank-account-qr.png</code>, in an Amazon AWS S3 bucket named <code>wareville-care4wares</code>. Let’s assist McSkidy and start by finding out more about that link. Before that, let’s first review the information that we currently have to start the investigation:</p>

<ul style="list-style-type:square">
    <li>The day after the link was sent out, several donations were received.</li>
    <li>Since the second day after sending the link, no more donations have been received.</li>
    <li>A donator has shown proof of his transaction. It was made 3 days after he received the link. The account number in the transaction was not correct.</li>
    <li>McSkidy put the digital flyer in the AWS S3 object named <code>wareville-bank-account-qr.png</code> under the bucket <code>wareville-care4wares</code>.</li>
    <li>The link has not been altered.</li>
</ul></p>


<h2><strong>Connection Details</strong></h2>
<p>Now that we have enough information, let's start the attached Virtual Machine in this task by clicking the Start Machine button below. Note that the machine may take 3-5 minutes to initialise. </p>

<p><code>Start Machine</code></p>

<p>The machine will start in a split-screen view. If the VM is not visible, use the blue Show Split View button at the top right of the page. </p>

<p align="center"><img width="300px" src="https://github.com/user-attachments/assets/b30e463b-38e1-448d-8bf3-80c6ca3ee932"></p>

<h2><strong>Glitch Did It</strong></h2>
<p>Let’s examine the Cloudtrail logs related to the wareville-care4wares S3 bucket. For a quick example, a typical S3 log entry looks like this:</p>

<p align="center"><img width="300px" src="https://github.com/user-attachments/assets/8353374b-aae1-4277-9c3d-12649901bb04"></p>

<p>It might be overwhelming to see the sheer amount of information in one event, but there are some elements that we can focus on for our investigation:</p>

<p align="center"><img width="300px" src="https://github.com/user-attachments/assets/e0501001-c92a-444d-ba2b-9241c860c38c"></p>

<p>By using the guide above, we can read the example log entry as follows: </p>

<ul style="list-style-type:square">
    <li>The IAM user, <code>wareville_collector</code>, listed all objects (ListObjects event) of the S3 bucket named <code>aoc-cloudtrail-wareville</code>.</li>
    <li>The IP address from which this request originated is <code>4.247.218.56</code>.</li>
    <li>The user agent indicates that the request was made using the <code>AWS SDK tool for Go</code>.</li>
</ul></p>


<p>Now that we know where to look, let’s use JQ to filter the log for events related to the <code>wareville-bank-account-qr.png</code> S3 object. The goal is to use the same elements to filter the log file using JQ and format the results into a table to make it more readable. According to McSkidy, the logs are stored in the <code>>~/wareville_logs</code> directory.

To start, click the <code>Terminal</code> icon on the Desktop and enter the two commands below:


<p>...................................</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>What is the other activity made by the user glitch aside from the ListObject action?</em><br><a id='1.1'></a>
>> <code><strong>PutObject</strong></code>

<br>

<pre><code>ubuntu@tryhackme:~/wareville_logs$ jq -r '["Event_Time", "Event_Source", "Event_Name", "User_Name", "Source_IP"],(.Records[] | select(.userIdentity.userName == "glitch") | [.eventTime, .eventSource, .eventName, .userIdentity.userName // "N/A", .sourceIPAddress // "N/A"]) | @tsv' cloudtrail_log.json | column -t -s $'\t'</code></pre>

<br>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/444f5b05-eb26-4cb9-b48e-bb620ab865ad"></p>

<br>

> 1.2. <em>What is the source IP related to the S3 bucket activities of the user glitch?</em><br><a id='1.2'></a>
>> <code><strong>53.94.201.69</strong></code>

<br>

<pre><code>ubuntu@tryhackme:~/wareville_logs$ jq -r '["Event_Time", "Event_Source", "Event_Name", "User_Name", "Source_IP"],(.Records[] | select(.userIdentity.userName == "glitch") | [.eventTime, .eventSource, .eventName, .userIdentity.userName // "N/A", .sourceIPAddress // "N/A"]) | @tsv' cloudtrail_log.json | column -t -s $'\t'</code></pre>

<br>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/b5794d46-9eca-4a46-9bfa-cb2797975c63"></p>

<br>


> 1.3. <em>Based on the eventSource field, what AWS service generates the ConsoleLogin event?</em><br><a id='1.3'></a>
>> <code><strong>signin.amazonaws.com</strong></code>

<br>

<pre><code>ubuntu@tryhackme:~/wareville_logs$ jq -r '["Event_Time", "Event_Source", "Event_Name", "User_Name", "Source_IP"],(.Records[] | select(.userIdentity.userName == "glitch") | [.eventTime, .eventSource, .eventName, .userIdentity.userName // "N/A", .sourceIPAddress // "N/A"]) | @tsv' cloudtrail_log.json | column -t -s $'\t'</code></pre>

<br>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/dc5d22a3-5b94-4300-8717-03c87dd7f1e9"></p>

<br>

> 1.4. <em>When did the anomalous user trigger the ConsoleLogin event?</em><br><a id='1.4'></a>
>> <code><strong>2024-11-28T15:21:54Z</strong></code>

<br>

<pre><code>ubuntu@tryhackme:~/wareville_logs$ jq -r '["Event_Time", "Event_Source", "Event_Name", "User_Name", "Source_IP"],(.Records[] | select(.userIdentity.userName == "glitch") | [.eventTime, .eventSource, .eventName, .userIdentity.userName // "N/A", .sourceIPAddress // "N/A"]) | @tsv' cloudtrail_log.json | column -t -s $'\t'</code></pre>

<br>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/58a7a798-8487-44c6-a8f9-551bf336d3be"></p>

<br>

> 1.5. <em>What was the name of the user that was created by the mcskidy user?</em><br><a id='1.5'></a>
>> <code><strong>glitch</strong></code>

<br>

<pre><code>ubuntu@tryhackme:~/wareville_logs$ jq -r '["Event_Time", "Event_Source", "Event_Name", "User_Name", "Source_IP"],(.Records[] | select(.userIdentity.userName == "glitch") | [.eventTime, .eventSource, .eventName, .userIdentity.userName // "N/A", .sourceIPAddress // "N/A"]) | @tsv' cloudtrail_log.json | column -t -s $'\t'</code></pre>

<br>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/23b40953-725e-4736-9af4-977cf8fa9f79"></p>

<br>

> 1.6. <em>What type of access was assigned to the anomalous user?</em><br><a id='1.6'></a>
>> <code><strong>AdministratorAccess</strong></code>

<br>

<pre><code>ubuntu@tryhackme:~/wareville_logs$ jq '.Records[] | select(.eventSource=="iam.amazonaws.com" and .eventName== "AttachUserPolicy")' cloudtrail_log.json</code></pre>

<br>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/0797b4b4-2501-4970-bc68-e80a9e7ceaff9"></p>

<br>

> 1.7. <em>Which IP does Mayor Malware typically use to log into AWS?</em><br><a id='1.7'></a>
>> <code><strong>53.94.201.69</strong></code>

<br>

<pre><code>ubuntu@tryhackme:~/wareville_logs$ jq '.Records[] | select(.eventSource=="iam.amazonaws.com" and .eventName== "AttachUserPolicy")' cloudtrail_log.json</code></pre>

<br>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/3ae9e9a8-101d-4dbb-82cf-dfb6baff5ca7"></p>

<br>

> 1.8. <em>What is McSkidy's actual IP address?</em><br><a id='1.8'></a>
>> <code><strong>31.210.15.79</strong></code>

<br>

<pre><code>ubuntu@tryhackme:~/wareville_logs$ jq -r '["Event_Time","Event_Source","Event_Name", "User_Name","User_Agent","Source_IP"],(.Records[] | select(.userIdentity.userName=="mcskidy") | [.eventTime, .eventSource, .eventName, .userIdentity.userName // "N/A",.userAgent // "N/A",.sourceIPAddress // "N/A"]) | @tsv' cloudtrail_log.json | column -t -s $'\t'</code></pre>

<br>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/a79f47a2-90e1-4d69-a0cd-b80a5236f50c"></p>

<br>


> 1.9. <em>What is the bank account number owned by Mayor Malware?</em><br><a id='1.9'></a>
>> <code><strong>2394 6912 7723 1294</strong></code>

<br>

<pre><code>ubuntu@tryhackme:~/wareville_logs$ grep Mayor rds.log</code></pre>


<br>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/897b2780-a426-473d-90ab-5299b4ccb225"></p>

<br>

> 1.10. <em>Want to learn more about log analysis and how to interpret logs from different sources? Check out the Log Universe room!</em><br><a id='1.10'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<br>

<h2>Task Completed<a id='2'></a></h2>
<p>Keep learning, keep growing!<br>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/91acddd7-b141-41a5-8446-8b10cec0d627"> </h3>


<h2>My Journey<a id='3'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| December 7, 2024  | 215      |     1,015 th |        21 st |    2,751 th |      32 nd | 59,692   |       457 |

</div>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/0fedc4db-ccbd-4c1a-b35c-df71f5376263"> </h3>


<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>
