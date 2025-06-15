
<p align="center">December 5, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{213}}$$-day-streak in  <a href="https://tryhackme.com/r/hacktivities">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Advent of Cyber 2023, Day 13, Instrusion Detection}}$$

</h1>
<p align="center">Get started with Cyber Security in 24 Days - Learn the basics by doing a new, beginner friendly security challenge every day leading up to Christmas.</p>
<p align="center">Access this 🆓 TryHackMe CTF Room clicking <a href="https://tryhackme.com/r/room/adventofcyber2023">Advent of Cyber 2023</a>.</p><br>
<p align="center">
  <img height="100px" hspace="20" src="https://github.com/user-attachments/assets/8d077e24-767e-4ac1-83f9-808a1dc8c077">
  <img width="700px" src="https://github.com/user-attachments/assets/8fc535bc-3f81-4cc2-819a-cd3e17713a22">
</p>


<h2>[Day 13] Intrusion Detection - To the Pots, Through the Walls<a id='1'></a></h2>

<p align="center">
  <img width="700px" src="https://github.com/user-attachments/assets/ecce579a-b7b9-40ab-9e86-57dd5dfb57fe">
</p>

<p>The proposed merger and suspicious activities have kept all teams busy and engaged. So that the Best Festival Company's systems are safeguarded in the future against malicious attacks, McSkidy assigns The B Team, led by McHoneyBell, to research and investigate mitigation and proactive security.<br>

The team's efforts will be channelled into the company's defensive security process. You are part of the team – a security researcher tasked with gathering information on defence and mitigation efforts.</p>

<h3>Learning Objectives</h3>
<p>In today's task, you will:</p>
- Learn to understand incident analysis through the Diamond Model.<br>
- Identify defensive strategies that can be applied to the Diamond Model.<br>
- Learn to set up firewall rules and a honeypot as defensive strategies.<br>

<h3>Accessing the Machine</h3>
<p>Before moving forward, review the questions in the connection card shown below:</p>

<p align="center">
  <img height="200px" src="https://github.com/user-attachments/assets/350234f2-679e-4929-9f10-6baccc5c9b0f">
</p>

<p>Launch the virtual machine by pressing the green <code>Start Machine</code> button at the top–right of this task and the AttackBox by pressing the Start AttackBox button on the upper right of this page. Use the SSH credentials below to access the VM and follow along the practical sections of the task.</p>

<p align="center">
  <img height="100px" src="https://github.com/user-attachments/assets/f6d903b4-794f-4d3f-8b41-7d29c5765bfd">
</p>

<h3>Introduction</h3>
<p>Intrusion detection and prevention is a critical component of cyber security aimed at identifying and mitigating threats. When set up early, intrusion detection becomes a proactive security measure. However, in our story, the Best Festival Company has to develop ways to improve their security, given the magnitude of the recent breaches.<br>

In this epic task, we'll embark on a thrilling journey through fundamental concepts, detection strategies, and the application of the Diamond Model of Intrusion Analysis in defensive security.</p>

<h3>Incident Analysis</h3>
<p>Consider the cyber threat events that have recently taken place within the Best Festival Company and AntarctiCrafts. We have identified clues and artefacts, but we're yet to piece them together to lead us to the attacker. We need a framework to profile the attacker, understand their moves, and help us strengthen our defences.</p>

<p align="center">
  <img width="80px" src="https://github.com/user-attachments/assets/d87f0e71-7b75-478a-98ef-d2df6737290b">
</p>

<p>The DiamondModel is a security analysis framework that seasoned professionals use to unravel the mysteries of adversary operations and identify the elements used in an intrusion. It comprises four core facets, interconnected to form a well-orchestrated blueprint of the attacker's plans:</p>
- Adversary<br>
- Victim<br>
- Infrastructure<br>
- Capability<br>

<p>We'll wield the knowledge we gained from the previous days of Advent of Cyber to unlock the secrets hidden within these core features.</p>

<h4>Adversary</h4>
<p>In our exciting storyline, we have discovered a suspected insider threat causing trouble within the Best Festival Company and interfering with the proposed merger with AntarctiCrafts. This individual, who we'll call the adversary operator, is not just an ordinary troublemaker. They are the clever attackers or malicious threat actors responsible for cyberattacks or intrusions. Adversary operators can be an individual or an entire organisation aiming to disrupt the operations of another.<br>

That's not the only type of adversary. The adversary customer is another intriguing player in this grand scheme. They are the one who reaps the rewards from the cyberattack and can consolidate the efforts of various adversary operators.<br>

Picture this: a collection of adversaries working together to orchestrate widespread security breaches, just like the enigmatic advanced persistent threat (APT) groups.</p>

<h4>Victim</h4>
<p>This is none other than the target of the adversary's wicked intentions. It could be a single individual or domain or an entire organisation with multiple network and data assets. The Best Festival Company finds itself at the mercy of these adversaries, and we must shield them from further harm.</p>

<h4>Infrastructure</h4>
<p>Every adversary needs tools. They require software or hardware to execute their malicious objectives. Infrastructure represents the physical and logical interconnections that an adversary employs. Our story takes an interesting twist as we uncover the USB drive that Tracy McGreedy cunningly plugged in, disrupting Santa's meticulously crafted plans.<br>

But beware. Adversarial infrastructure can be owned and controlled by adversaries or even intermediaries like service providers.</p>

<h4>Capability</h4>
<p>Ah, what capabilities these adversaries have; what skills, tools, and techniques they employ!<br>

Here, we shine a light on the tactics, techniques, and procedures (TTPs) that shape adversaries' devious endeavours. Intruders or adversaries may employ various tactics, techniques, and procedures for malicious activities. Some examples include:</p>

- Phishing: Adversaries may use deceptive emails or messages to trick individuals into revealing sensitive information or clicking on malicious links.<br>
- Exploiting vulnerabilities: Adversaries can exploit weaknesses or vulnerabilities in software, systems, or networks to gain unauthorised access or perform malicious actions. This was very well showcased on AOC Day 10, where we covered SQL injection as one of the techniques used.<br>
- Social engineering: This involves manipulating individuals through psychological tactics to gain unauthorised access or obtain confidential information.<br>
- Malware attacks: Adversaries may deploy malicious software, such as viruses, worms, or ransomware, to gain control over systems or steal data.<br>
- Insider threat: This refers to individuals within an organisation who misuse their access privileges to compromise systems, steal data, or disrupt operations.<br>
- Denial–of–service (DoS) Attacks: Adversaries may overwhelm a target system or network with excessive traffic or requests, causing it to become unresponsive or crash.<br>

<h3>Defensive Diamond Model</h3>
<p>But fear not, for we shall not be mere observers in this cosmic battle! We will harness the power of the Diamond Model's components, particularly capability and infrastructure, for our defensive endeavours. We will forge The Best Festival Company into a formidable defender – no longer a hapless victim.</p>

<h4>Defensive Capability</h4>
<p>It is said that defence is the best offence. In the quest for protection against adversaries, the Best Festival Company must equip itself with powerful defensive capabilities. Two key elements of this are threat hunting and vulnerability management.<br>

Threat hunting is a proactive and iterative process, led by skilled security professionals, to actively search for signs of malicious activities or security weaknesses within the organisation's network and systems. Organisations can detect adversaries early in their attack lifecycle by conducting regular threat hunts. Threat hunters analyse behavioural patterns, identify advanced threats, and improve incident response. Developing predefined hunting playbooks and fostering collaboration among teams ensures a systematic and efficient approach to threat hunting.<br>

Vulnerability management is a structured process of identifying, assessing, prioritising, mitigating, and monitoring vulnerabilities in an organisation's systems and applications. Regular vulnerability scanning helps identify weaknesses that adversaries could exploit. Prioritising vulnerabilities based on their severity and potential impact, promptly patching or remediating vulnerabilities, and maintaining an up–to–date asset inventory is essential. Continuous monitoring, integration with threat intelligence feeds, and periodic penetration testing further strengthen the organisation's security posture. Meanwhile, reporting and accountability provide visibility into security efforts.<br>

By integrating threat hunting and vulnerability management, organisations can proactively defend against adversaries, detect threats early, and reduce the attack surface. These defensive capabilities form a solid foundation for incident response and ensure the best possible defence for the Best Festival Company.</p>

<h4>Defensive Infrastructure</h4>
<p>The Best Festival Company will construct their bastion of defence, fortified with tools and infrastructure to repel cyber-attacks. Layer upon layer of hardware and software will be deployed, ranging from intrusion defence and prevention systems to robust anti-malware solutions. The objective is to impede attackers by limiting their options to predetermined paths and disrupting their malicious actions with increased noise.<br>

This strategy serves as a deterrent to the attacker, making it more difficult for them to carry out their intended activities and providing an opportunity for detection and response. By implementing this approach, organisations can strengthen their cyber security posture and reduce the risk of successful attacks.<br>

In this section, we'll guide Van Twinkle on her quest to understand two essential components of defence infrastructure: mighty firewalls and cunning honeypots.</p>

<h4>Firewall</h4>
<p>The mighty firewall is a guardian of networks and a sentinel of cyber security! This network security device stands vigilant, monitoring and controlling the ebb and flow of incoming and outgoing network traffic. With its predetermined security rules, a firewall can repel a wide range of threats, from unauthorised access to malicious traffic and even attempts to breach sensitive data.<br>

Firewalls come in many forms, including hardware, software, or a combination. Their presence is vital, a cornerstone of any cyber security defence strategy. The following are the common types of firewalls that exist:</p>
- Stateless/packet-filtering: This firewall provides the most straightforward functionality by inspecting and filtering individual network packets based on a set of rules that would point to a source or destination IP address, ports and protocols. The firewall doesn’t consider any context of each connection when making decisions and effectively blocks denial–of–service attacks and port scans.<br>
- Stateful inspection: This firewall is more sophisticated. It is used to track the state of network connections and use this information to make filtering decisions. For example, if a packet being channelled to the network is part of an established connection, the stateful firewall will let it pass through. However, the packet will be blocked if it is not part of an established connection.
- Proxy service: This firewall protects the network by filtering messages at the application layer, providing deep packet inspection and more granular control over traffic content. The firewall can block access to certain websites or block the transmission of specific types of files.<br>
- Web application firewall (WAF): This firewall is designed to protect web applications. WAFs block common web attacks such as SQL injection, cross-site scripting, and denial-of-service attacks.<br>
- Next-generation firewall: This firewall combines the functionalities of the stateless, stateful, and proxy firewalls with features such as intrusion detection and prevention and content filtering.<br>

<p>For the remainder of the task, we shall focus on one application of a stateful inspection firewall in the form of the uncomplicated firewall (ufw).</p>

<h4>Configuring Firewalls to Block Traffic</h4>
<p>Van Twinkle knows that the uncomplicated firewall is the default firewall configuration tool available on Ubuntu hosts, and she decides to use it for this experiment. Initially, it's turned off by default, so we can check the status by running the command below:</p>

<h3>Van Twinkle´s Challenge</h3>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 1.1. <em>Which security model is being used to analyse the breach and defence strategies?</em><br><a id='1.1'></a>
>> <code><strong>Diamond Model</strong></code>

<br>

> 1.2. <em>Which defence capability is used to actively search for signs of malicious activity?</em><br><a id='1.2'></a>
>> <code><strong>Threat hunting</strong></code>

<br>

> 1.3. <em>What are our main two infrastructure focuses? (Answer format: answer1 and answer2)</em><br><a id='1.3'></a>
>> <code><strong>Firewall and Honeypot</strong></code>

<br>

> 1.4. <em>What is the name of the layer between the Input and Output layers of a Neural Network?</em><br><a id='1.4'></a>
>> <code><strong>Hidden Layer</strong></code>

<br>

> 1.5. <em>Which firewall command is used to block traffic?</em><br><a id='1.5'></a>
>> <code><strong>Deny</strong></code>

<br>

> 1.6. <em>There is a flag in one of the stories. Can you find it?</em><br><a id='1.6'></a>
>> <code><strong>THM{P0T$_W@11S_4_S@N7@}</strong></code>

<br>

> 1.7. <em>If you enjoyed this task, feel free to check out the Network Device Hardening room.</em><br><a id='1.6'></a>
>> <code><strong>No answer needed</strong></code>

<br>

![image](https://github.com/user-attachments/assets/6d1609d6-5293-48b7-88f3-5bb7255c226e)

<br>

<pre><code>
vantwinkle@ip-10-10-23-150:~$ pwd
/home/vantwinkle
vantwinkle@ip-10-10-23-150:~$ sudo ufw status
[sudo] password for vantwinkle: 
Status: inactive
vantwinkle@ip-10-10-23-150:~$ 
</code></pre>

<br>

<pre><code>vantwinkle@[Target]:~$ sudo su
root@[Target]:/home/vantwinkle# ufw default allow outgoing
Default outgoing policy changed to 'allow'
(be sure to update your rules accordingly)
</code></pre>

<b>

<pre><code>vantwinkle@[Target]:/home/vantwinkle# ufw default deny incoming
Default incoming policy changed to 'deny'
(be sure to update your rules accordingly)
</code></pre>

<br>

<pre><code>vantwinkle@[Target]:/home/vantwinkle# ufw allow 22/tcp
Rules updated
Rules updated (v6)
</code></pre>

<br>

<pre><code>vantwinkle@[Target]:/home/vantwinkle# ufw deny from [Specific IP 1]
Rules updated
</code></pre>

<br>

<pre><code>vantwinkle@[Target]:/home/vantwinkle# ufw deny in on eth0 from [Specific IP 2]
Rules updated</code></pre>


<br>

<pre><code>vantwinkle@[Target]:/home/vantwinkle# ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
</code></pre>

<br>

<pre><code>vantwinkle@[Target]:/home/vantwinkle# ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere                  
Anywhere                   DENY IN     [Specific IP 1]           
Anywhere on eth0           DENY IN     [Specific Ip 2]            
22/tcp (v6)                ALLOW IN    Anywhere (v6)</code></pre>

<br>

<pre><code>vantwinkle@[Target]:/home/vantwinkle# fw reset
Resetting all rules to installed defaults. This may disrupt existing ssh
connections. Proceed with operation (y|n)? y
Backing up 'user.rules' to '/etc/ufw/user.rules.[Redacted]'
Backing up 'before.rules' to '/etc/ufw/before.rules.[Redacted]'
Backing up 'after.rules' to '/etc/ufw/after.rules.[Redacted]'
Backing up 'user6.rules' to '/etc/ufw/user6.rules.[Redacted]'
Backing up 'before6.rules' to '/etc/ufw/before6.rules.[Redacted]'
Backing up 'after6.rules' to '/etc/ufw/after6.rules.[Redacted]'
</code></pre>

<br>

![image](https://github.com/user-attachments/assets/a612f73e-3da1-400c-bb71-0680b2e870ab)

<br>

![image](https://github.com/user-attachments/assets/4d24b18b-07bb-4904-a4c4-078fbc975778)

<br>

![image](https://github.com/user-attachments/assets/98c3a8b3-4626-4a63-88e9-19cef7de54fb)

<br>

![image](https://github.com/user-attachments/assets/fb3a47ed-a96d-4680-ab4d-221c52511d52)

<br>

![image](https://github.com/user-attachments/assets/0f1d9f53-2052-4bb0-9727-06a748132538)

<br>


<p>And see what we got ... <code>INTRUSION ATTEMPt DETECTED!</code></p>

![image](https://github.com/user-attachments/assets/4aab3ce9-38be-4930-964e-da5800019250)

<br>

<pre><code>vantwinkle@[Target]:/home/vantwinkle/pentbox/pentbox-1.8# ufw status
Status: inactive
root@ip-10-10-23-150:/home/vantwinkle/pentbox/pentbox-1.8# cd ..
root@ip-10-10-23-150:/home/vantwinkle/pentbox# cd ..
root@ip-10-10-23-150:/home/vantwinkle# ls
Van_Twinkle_rules.sh  pentbox  sudo
root@ip-10-10-23-150:/home/vantwinkle# cat Van_Twinkle_rules.sh 
#!/bin/bash
sudo ufw --force reset
sudo ufw default allow incoming
sudo ufw allow http 
sudo ufw allow ssh
sudo ufw deny 21/tcp
sudo ufw deny from any to any port 8088
sudo ufw deny 8090/tcp
sudo ufw enable 
root@ip-10-10-23-150:/home/vantwinkle#
</code></pre>

<br>

<pre><code>root@[THM AttackBox]:~/Day13# nmap [Target]
Starting Nmap 7.80 ( https://nmap.org ) at 2024-12-06 02:51 GMT
Nmap scan report for ip-[Target].eu-west-1.compute.internal ([Target])
Host is up (0.00026s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
8090/tcp open  opsmessaging
MAC Address: 02:4F:10:2A:DB:95 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.30 seconds
</code></pre>


<br>

<pre><code>vantwinkle@[Target]:/home/vantwinkle/# ./Van_Twinkle_rules.sh
Backing up 'user.rules' to '/etc/ufw/user.rules.20241206_025354'
Backing up 'before.rules' to '/etc/ufw/before.rules.20241206_025354'
Backing up 'after.rules' to '/etc/ufw/after.rules.20241206_025354'
Backing up 'user6.rules' to '/etc/ufw/user6.rules.20241206_025354'
Backing up 'before6.rules' to '/etc/ufw/before6.rules.20241206_025354'
Backing up 'after6.rules' to '/etc/ufw/after6.rules.20241206_025354'

Default incoming policy changed to 'allow'
(be sure to update your rules accordingly)
Rules updated
Rules updated (v6)
Rules updated
Rules updated (v6)
Rules updated
Rules updated (v6)
Rules updated
Rules updated (v6)
Rules updated
Rules updated (v6)
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
</code></pre>


<br>

<pre><code>vantwinkle@[Target]:/home/vantwinkle/# ufw status verbose
Status: active
Logging: on (low)
Default: allow (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
80/tcp                     ALLOW IN    Anywhere                  
22/tcp                     ALLOW IN    Anywhere                  
21/tcp                     DENY IN     Anywhere                  
8088                       DENY IN     Anywhere                  
8090/tcp                   DENY IN     Anywhere                  
80/tcp (v6)                ALLOW IN    Anywhere (v6)             
22/tcp (v6)                ALLOW IN    Anywhere (v6)             
21/tcp (v6)                DENY IN     Anywhere (v6)             
8088 (v6)                  DENY IN     Anywhere (v6)             
8090/tcp (v6)              DENY IN     Anywhere (v6)       
</code></pre>

<br>

<pre><code>vantwinkle@[Target]:/home/vantwinkle/# ufw allow 8090/tcp
Rule updated
Rule updated (v6)
root@ip-10-10-23-150:/home/vantwinkle# ufw status verbose
Status: active
Logging: on (low)
Default: allow (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
80/tcp                     ALLOW IN    Anywhere                  
22/tcp                     ALLOW IN    Anywhere                  
21/tcp                     DENY IN     Anywhere                  
8088                       DENY IN     Anywhere                  
8090/tcp                   ALLOW IN    Anywhere                  
80/tcp (v6)                ALLOW IN    Anywhere (v6)             
22/tcp (v6)                ALLOW IN    Anywhere (v6)             
21/tcp (v6)                DENY IN     Anywhere (v6)             
8088 (v6)                  DENY IN     Anywhere (v6)             
8090/tcp (v6)              ALLOW IN    Anywhere (v6)
</code></pre>


![image](https://github.com/user-attachments/assets/482108e3-7519-48a8-96b6-96c3c8508195)

<br>

![image](https://github.com/user-attachments/assets/1b2a6145-1c97-4de1-a892-ce073f486fd2)



<h2>Task Complete<a id='2'></a></h2>
<p>Keep learning, keep growing!<br>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/3121d8ac-e625-4879-abef-a212688796bc"> </h3>


<h2>My Journey<a id='3'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/59d1b17c-70aa-40eb-b666-b834a7b47056"> </h3>

