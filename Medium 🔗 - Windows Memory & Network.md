<h1 align="center"> Windows Memory & Network<br><img width="1200px" src="https://github.com/user-attachments/assets/3c611801-4d91-40e8-b35b-a2395cf04ada"></h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/eec07c31-df33-48de-a52b-2b9b701ba625"><br>
June 11, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my401-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Identify C2 traffic & post-exploit activity in Windows memory. <a href="https://tryhackme.com/room/windowsmemoryandnetwork"</a>here.<br><br>
<img width="1000px" src="5"></p>

<br>
<br>

<h2> Task 1 . Introduction</h2>

<p>This room continues the memory investigation from the previous analysis. This is the last room out of 3, and we will be focusing on how network activity and post-exploitation behavior are captured in RAM. We’ll examine artifacts from a live attack involving advance payloads like Meterpreter, suspicious child processes, and unusual outbound connections. All analyses will be performed using Volatility 3 and hands-on techniques applied directly to the memory dump.<br><br>

We’ll walk through real indicators tied to remote shells, persistence via startup folder abuse, and malware attempting outbound communications. Users will use memory structures, plugin outputs, and process inspection to track network behavior step by step.</p>

<h3>Learning Objectives</h3>
<p>

-  Identify network connections in a memory dump.<br>
- Identify suspicious ports and remote endpoints.<br>
- Link connections to processes.<br>
- Detect reverse shells and memory injections in a memory dump.<br>
- Trace PowerShell and C2 activity in memory.
- 
</p>

<h3>Prerequisites</h3>

<p>

- Volatility <br>
- Yara<br>
- Windows Memory & Processes<br>
- Windows Memory & User Activity
</p>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>Click to continue the room</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 2 . Scenario Information</h2>

<h3>Scenario</h3>
<p></p>You are part of the incident response team handling an incident at TryHatMe - a company that exclusively sells hats online. You are tasked with analyzing a full memory dump of a potentially compromised Windows host. Before you, another analyst had already taken a full memory dump and gathered all the necessary information from the TryHatMe IT support team. You are a bit nervous since this is your first case, but don't worry; a senior analyst will guide you.</p>

<h3>Information Incident THM-0001</h3>

<p>

- On May 5th, 2025, at 07:30 CET, TryHatMe initiated its incident response plan and escalated the incident to us. After an initial triage, our team found a Windows host that was potentially compromised. The details of the host are as follows:<br>
--- Hostname: WIN-001<br>
--- OS: Windows 1022H 10.0.19045<br><br<
  
- At 07:45 CET, our analyst Steve Stevenson took a full memory dump of the Windows host and made a hash to ensure its integrity. The memory dump details are:<br>
---Name: <code>THM-WIN-001_071528_07052025.dmp</code><br>
---MD5-hash: <code>78535fc49ab54fed57919255709ae650</code></p>


<h3>Company Information TryHatMe</h3>
<h4>Network Map</h4>

![image](https://github.com/user-attachments/assets/32b6a505-ccd7-4fef-b229-e9a416a1ecb3)


<h3 align="left"> Answer the question below</h3>

> 2.1. <em>I went through the case details and am ready to find out more.</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 3 . Environment & Setup</h2>

<p>Before moving forward, start the VM by clicking the Start Machine button on the right.<br><br>

It will take around 2 minutes to load properly. The VM will be accessible on the right side of the split screen. If the VM is not visible, use the blue Show Split View button at the top of the page.<br><br>

The details for the assignment are:<br>

- File Name: <code>THM-WIN-001_071528_07052025.mem</code><br>
- File MD5 Hash: <code>78535fc49ab54fed57919255709ae650</code><br>
- File Location: <code>/home/ubuntu</code></p>

<p>To run volatility, you can use the vol command in the VM. For example: vol -h will display the help menu for volatility.</p>

<h3 align="left"> Answer the question below</h3>

> 3.1. <em>Click here if you were able to start your environment.</em><br><a id='3.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 4 . Analyzing Active Connections</h2>
<p>In the previous room, we focused on identifying user activity within memory. Now, we shift our attention to network connections established by the suspected malicious actor. We'll begin by searching for artifacts in memory that reveal what connections were made and what kind of network activity took place during the intrusion.</p>

<h3>Scanning Memory for Network Evidence</h3>

<p>Let's start by scanning the memory dump with the <code>Windows.netscan</code> plugin. This plugin inspects kernel memory pools for evidence of <code>TCP</code> and <code>UDP</code> socket objects, regardless of whether the connections are still active. It's beneficial in cases where the process we are investigating may have terminated or cleaned up connections.<br><br>

To inspect the network connections, volatility locates the EPROCESS structure to extract PIDs and map these to active <code>TCP ENDPOINT</code> or <code>UDP ENDPOINT</code> objects (undocumented) found in memory. This approach works even if a connection has already been closed, making it more useful than <code>netstat</code> on a live system.<br><br>

When analysing connections to look for supicious traffic, we should be aware of the following:<br>

- Unusual port activity or outbound connections to unfamiliar addresses<br>
- Communication with external IPs on non-standard ports<br>
- Local processes holding multiple sockets<br>
- PIDs tied to previously identified suspicious binaries</p>

<p>Let's look for the patterns mentioned above. We'll start by running the following command <code>vol -f THM-WIN-001_071528_07052025.mem windows.netscan > netscan.txt</code>, which will save the output in the <code>netscan.txt</code> file as shown below. We can then inspect it using the <code>cat</code> command or any text visualizer.<br><br>

Note: This command can take some time to finish, depending on CPU usage and the size of the memory dump. In case you do not want to wait, you can access the same output in the already existing file <code>netscan-saved.txt</code>. There are also some other commands that have been pre-saved to save time if needed.</p>

<p>Example Terminal</p>


```bash
user@tryhackme~$ vol -f THM-WIN-001_071528_07052025.mem windows.netscan >  netscan.txt
user@tryhackme$cat netscan.txt

Offset	Proto	LocalAddr	LocalPort	ForeignAddr	ForeignPort	State	PID	Owner	Created
[REDACTED]
0x990b28ae34c0	UDPv4	169.254.106.169	138	*	0		4	System	2025-05-07 07:08:58.000000 UTC
0x990b28bf3230	TCPv4	169.254.106.169	139	0.0.0.0	0	LISTENING	4	System	2025-05-07 07:08:58.000000 UTC
0x990b28bf3650	TCPv4	0.0.0.0	4443	0.0.0.0	0	LISTENING	10084	windows-update	2025-05-07 07:13:05.000000 UTC
[REDACTED]
0x990b299a81f0	UDPv4	127.0.0.1	1900	*	0		9496	svchost.exe	2025-05-07 07:09:11.000000 UTC
0x990b29ab8010	TCPv4	192.168.1.192	[REDACTED]	192.168.0.30	22	ESTABLISHED	6984	powershell.exe	2025-05-07 07:15:15.000000 UTC
0x990b29ade8a0	TCPv4	192.168.1.192	4443	10.0.0.129	47982	ESTABLISHED	10084	windows-update	2025-05-07 07:13:35.000000 UTC
0x990b2a32ca20	TCPv4	192.168.1.192	[REDACTED]	10.0.0.129	8081	ESTABLISHED	10032	updater.exe	[REDACTED] UTC
0x990b2a630a20	TCPv6	::1	55986	::1	445	CLOSED	4	System	2025-05-07 07:14:06.000000 UTC
0x990b2a824770	UDPv6	fe80::185b:1837:f9f7:bffd	49595	*	0		9496	svchost.exe	2025-05-07 07:09:11.000000 UTC
0x990b2a824900	UDPv6	fe80::185b:1837:f9f7:bffd	1900	*	0		9496	svchost.exe	2025-05-07 07:09:11.000000 UTC
0x990b2a824db0	UDPv6	::1	1900	*	0		9496	svchost.exe	2025-05-07 07:09:11.000000 UTC
[REDACTED] 
```

<p>We can observe in the output above that some connections are marked as <code>ESTABLISHED</code>. We can notice that PID <code>10032</code> (<code>updater.exe</code>) is connected to IP <code>10.0.0.129 on port 8081</code>. That is an external network and suggests it may be the attacker's infrastructure. Another connection of interest is from PID <code>6984</code> (<code>powershell.exe</code>) reaching out to <code>192.168.0.30:22</code>, suggesting lateral movement. Also, as we know from previous analysis, the binary <code>windows-update.exe</code> is also part of the chain of execution we are investigating and was placed for persistence purposes in the <code>C:\Users\operator\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup\<\code> directory. It is listening on port 4443, which makes sense to be set up like that since it seems to be the one listening for instructions. Let’s now move on to confirm this and spot which active listening ports are.</p>

<p>Example Terminal</p>

```bash
user@tryhackme~$ cat netscan.txt |grep LISTENING
0x990b236b3310	TCPv4	0.0.0.0	445	0.0.0.0	0	LISTENING	4	System	2025-05-07 07:08:50.000000 UTC
[REDACTED]
0x990b27ffee90	TCPv4	0.0.0.0	3389	0.0.0.0	0	LISTENING	364	svchost.exe	2025-05-07 07:08:49.000000 UTC
0x990b27ffee90	TCPv6	::	3389	::	0	LISTENING	364	svchost.exe	2025-05-07 07:08:49.000000 UTC
0x990b28bf3230	TCPv4	169.254.106.169	139	0.0.0.0	0	LISTENING	4	System	2025-05-07 07:08:58.000000 UTC
0x990b28bf3650	TCPv4	0.0.0.0	4443	0.0.0.0	0	LISTENING	10084	windows-update	2025-05-07 07:13:05.000000 UTC
0x990b28de7e10	TCPv4	0.0.0.0	49671	0.0.0.0	0	LISTENING	3020	svchost.exe	2025-05-07 07:08:51.000000 UTC
0x990b28de80d0	TCPv4	0.0.0.0	49671	0.0.0.0	0	LISTENING	3020	svchost.exe	2025-05-07 07:08:51.000000 UTC
0x990b28de80d0	TCPv6	::	49671	::	0	LISTENING	3020	svchost.exe	2025-05-07 07:08:51.000000 UTC
0x990b28de8390	TCPv4	0.0.0.0	5040	0.0.0.0	0	LISTENING	6124	svchost.exe	2025-05-07 07:08:59.000000 UTC
0x990b28de8910	TCPv4	192.168.1.192	139	0.0.0.0	0	LISTENING	4	System	2025-05-07 07:08:51.000000 UTC
```

<p>We can observe several system processes like svchost.exe and lsass.exe listening on common Windows ports. However, we can also confirm that the only non-standard process listening is windows-update.exe (PID 10084), which is listening on port 4443.<br><br>

This seems to be highly irregular. We already know that the process had established a connection with the potential attacker and is accepting inbound connections. This could be for file staging, secondary payloads, or as we already confirmed, for persistence.<br><br>

Note: As a sanity check, try also running windows.netstat. This plugin relies on live system structures instead of scanning memory, so it may return fewer results, but it is useful to compare what's still active and also to check the connection's order by timestamp.<br><br>

Great, at this point, we’ve confirmed:<br>

- updater.exe (PID 10032) was in an active session with a known attacker IP using port 8081.<br>
- windows-update.exe (PID 10084) had its own established session and was listening on port 4443.<br>
- powershell.exe (PID 6984) connected to 192.168.0.30:22, likely the next internal target.</p>


<p>These findings help confirm suspicions of remote control via C2, plus lateral movement activity. In the next section, we'll explore more into this in order to confirm our findings.</p>


<h3 align="left"> Answer the question below</h3>

> 4.1. <em>What is the remote source port number used in the connection between 192.168.1.192 and 10.0.0.129:8081?</em><br><a id='4.1'></a>
>> <strong><code>55985</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/0f5a9212-1e51-4775-8ab1-c7c258eb240e)

<br>

> 4.2. <em>Which internal IP address received a connection on port 22 from the compromised host?</em><br><a id='4.2'></a>
>> <strong><code>192.168.0.30</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/81dbd147-ce00-421f-90fb-dfee3cc155b1)

<br>

> 4.3. <em>What is the exact timestamp when the connection from the IP addresses in question 1 was established?</em><br><a id='4.3'></a>
>> <strong><code>2025-05-07 07:13:56.000000</code></strong><br>
<p></p>


![image](https://github.com/user-attachments/assets/7d73be26-fa2f-4496-a5ee-cdaa9dc3f61d)


> 4.4. <em>What is the local port used by the system to initiate the SSH connection to 192.168.0.30?</em><br><a id='4.4'></a>
>> <strong><code>55987</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/8315c4fe-7089-426f-a035-c81f952827f3)

<br>

> 4.5. <em>What is the protocol used in the connection from 192.168.1.192:55985 to 10.0.0.129:8081?</em><br><a id='4.5'></a>
>> <strong><code>TCPv4</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/1043309a-b367-4e4a-9bd2-4ea6d06f20a7)

<br>

> 4.6. <em>What is the order in which the potential malicious processes established outbound connections?</em><br><a id='4.6'></a>
>> <strong><code>windows-update.exe, updater.exe, powershell.exe</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/dc9bf320-f3aa-4cb6-914d-1dc743425638)

<br>

<h2> Task 5 .  Investigating Remote Access and C2 Communications</h2>

<h2> Task 6 .  Post-Exploitation Communication</h2>

<h2> Task 7 .  Putting it All Together</h2>

<h2> Task 8 .  Conclusion</h2>




