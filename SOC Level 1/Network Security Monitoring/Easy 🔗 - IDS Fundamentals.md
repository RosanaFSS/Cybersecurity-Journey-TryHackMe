<h3> Welcome to the <em>TryHackMe ...</em></h3>
<h1>SOC Level 1 Learning Path ><br> Network Security Monitoring > IDS Fundamentals</h1>
<p>Learn the fundamentals of IDS, along with the experience of working with Snort.</p>
<p>October 22, 2024<br></p>

<center>
<img src="https://github.com/user-attachments/assets/c1dda32b-bfb6-417d-b1dd-9a06155fecf5"
height="200" width="200">
</center>

![image](https://github.com/user-attachments/assets/d44524ba-3154-460d-a5d4-de69cfaf2153)


<p>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure. TryHackMe classified this CTF as Easy. It´s key part of my 169-day-streak. Let´s get started!!<br><br>
Access this TryHackMe Room clicking <a href="https://tryhackme.com/r/room/idsfundamentals)">IDS Fundamentals</a></p>

<h2>Task 1 - Whats is IDS</h2>
<p>In the previous room, Intro to Firewalls, we studied the role of a firewall, a security solution usually deployed on the boundary of a network to protect its incoming and outgoing traffic. The firewall checks the traffic when a connection is going to take place and denies it if it violates the firewall rules. However, there should be some security to detect the activities of the connection that passed through the firewall and have already taken place. So, if an attacker successfully bypasses a firewall via a legitimate-looking connection and then performs any malicious activities inside the network, there should be something to detect it timely. For this purpose, we have a security solution inside the network. This solution is known as an Intrusion Detection System (IDS).<br><br>

Think of an example of a building’s security. A firewall acts as the gatekeeper, checking the people coming in and going out. There is always a chance that some bad actor will successfully sneak inside and start performing malicious activities. He was missed at the gate, but what if we catch him even after he gets in? This can be done by the surveillance cameras present throughout the building. The IDS plays the role of surveillance cameras. It sits in a corner, monitors the network traffic based on its signature and anomaly-based detections, and detects any abnormal traffic going out or inside the network. Upon every detection, an alert is generated for the security administrators. IDS does not act on those detections; it only notifies the security administrators about the malicious activity.<br><br>

This room will equip you with sound knowledge of IDS solutions. In the upcoming tasks, we will also explore the most popular open-source IDS solution.<br></p>
<h3>Learning Objectives</h3>
<p>Types of IDS and their detection capabilities<br>
Working of Snort IDS<br>
Default and custom rules in Snort IDS<br>
Making a custom rule in Snort IDS</p>

> 1.1 - <em>Can an intrusion detection system (IDS) prevent the threat after it detects it? Yea/Nay.</em><br>
>> <strong>Nay</strong><br>
<p></p>

<h2>Task 2 - Type of IDS</h2>
<p>IDS can be categorized differently depending on certain factors. An IDS’s main categorization depends on its deployment and detection modes.</p>
<p></p>

> 2.1 - <em>Which type of IDS is deployed to detect threats throughout the network?</em><br>
>> <strong>Network Intrusion Detection System</strong><br>
<p></p>

> 2.2 - <em>Which IDS leverages both signature-based and anomaly-based detection techniques?</em><br>
>> <strong>Hybrid IDS</strong><br>
<p></p>

<h2>Task 3 - IDS Example: Snort</h2>

> 3.1 - <em>Which mode of Snort helps us to log the network traffic in a PCAP file?</em><br>
>> <strong>Packet Logging Mode</strong><br>
<p></p>

> 3.2 - <em>What is the primary mode of Snort called?</em><br>
>> <strong>Network Intrusion Detection System Mode</strong><br>
<p></p>

<h2>Task 4 - Snort Usage</h2>

> 4.1 - <em>Where is the main directory of Snort that stores its files?</em><br>
>> <strong>/etc/snort</strong><br>
<p></p>

> 4.2 - <em>Which field in the Snort rule indicates the revision number of the rule?</em><br>
>> <strong>rev</strong><br>
<p></p>

> 4.3 - <em>Which protocol is defined in the sample rule created in the task?</em><br>
>> <strong>icmp</strong><br>
<p></p>

> 4.4 - <em>What is the file name that contains custom rules for Snort?</em><br>
>> <strong>local.rules</strong><br>
<p></p>


<h2>Task 5 - Practical Lab</h2>

>5.1 - <em>What is the IP address of the machine that tried to connect to the subject machine using SSH?</em><br>
>> <strong>10.11.90.211</strong><br>
<p></p>
<pre><code>sudo snort -q -l /etc/snort -r Intro_to_IDS.pcap -A console -c /etc/snort/snort.conf</code></pre>


![image](https://github.com/user-attachments/assets/042881a6-cd9f-4026-aa07-54c9a64d0c6e)

> 5.2 - <em>What other rule message besides the SSH message is detected in the PCAP file? </em><br>
>> <strong>Ping Detected</strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/d315214d-e1b1-4609-bbbd-e5fa045551da)

> 5.3 - <em>What is the sid of the rule that detects SSH?</em><br>
>> <strong>1000002</strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/0415856e-a0d5-42f2-aa1b-7674b148f732)


<h2>Room Completed</h2>

<p>Keep learning, keep growing!<br>
    
<a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a></p>

![image](https://github.com/user-attachments/assets/fd8e1dcc-2cf5-4754-8c88-2ec3b2244291)
