<h1 align="center"> Windows Memory & Network<br><img width="1200px" src="https://github.com/user-attachments/assets/3c611801-4d91-40e8-b35b-a2395cf04ada"></h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/d7050f1e-1ab4-48ec-a5a2-6f5e33e422dc5"><br>
June 11, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>401</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
Identify C2 traffic & post-exploit activity in Windows memory.<a href="https://tryhackme.com/room/windowsmemoryandnetwork"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/2179ec73-213f-4b57-9115-4ae96682c9b9"></p>

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

<p>We can observe in the output above that some connections are marked as <code>ESTABLISHED</code>. We can notice that PID <code>10032</code> (<code>updater.exe</code>) is connected to IP <code>10.0.0.129 on port 8081</code>. That is an external network and suggests it may be the attacker's infrastructure. Another connection of interest is from PID <code>6984</code> (<code>powershell.exe</code>) reaching out to <code>192.168.0.30:22</code>, suggesting lateral movement. Also, as we know from previous analysis, the binary <code>windows-update.exe</code> is also part of the chain of execution we are investigating and was placed for persistence purposes in the <code>C:\Users\operator\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup\</code>code> directory. It is listening on port 4443, which makes sense to be set up like that since it seems to be the one listening for instructions. Let’s now move on to confirm this and spot which active listening ports are.</p>

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


<h3 align="left"> Answer the questions below</h3>

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
<p>In the previous task, we discovered that updater.exe (PID 10032) was communicating with the external IP 10.0.0.129 over port 8081. This activity was flagged as highly suspicious, especially considering the context: a process spawned from a malicious Word document chain, and now reaching out to what appears to be attacker infrastructure.<br><br>

Let’s take a closer look at this binary. The goal now is to determine whether this process was being used to maintain remote access. through a Meterpreter session or another C2 framework, and whether any evidence of post-exploitation activity can be uncovered directly in memory.</p>

<h3>Confirming Process Relationships</h3>

<p>We already confirmed in the previous room the relationship between this process and their PIDs, but if we need to gather the information again, we can use the commands listed below to identify them.<br><br>

<code>vol -f THM-WIN-001_071528_07052025.mem windows.pslist > pslist.txt</code><br>
<code>vol -f THM-WIN-001_071528_07052025.mem windows.cmdline > cmdline.txt</code><br>

This matches the chain we had already suspected: A Word document opened by the user, followed by the execution of three suspicious binaries in sequence, pddfupdater.exe, windows-update.exe, leading to updater.exe. On the other hand, from the cmdline plugin output that we already have (we can execute the command to get the output again by typing: <code>vol -f THM-WIN-001_071528_07052025.mem windows.cmdline > cmdline.txt</code>), we can try to determine how it was invoked. Let's inspect with the following command to filter by process ID <code>cat cmdline.txt | grep 10032</code></p>

<p>Example Terminal</p>

```bash
user@tryhackme~$ cat cmdline.txt | grep 10032
10032	updater.exe	"C:\Users\operator\Downloads\updater.exe"
```

<p>As we can observe, no arguments have been passed. This is common for binaries that serve as droppers or loaders, especially those that use in-memory injection or reflective loading techniques, something Meterpreter is known for. Let's try to confirm our suspicions.</p>

<h3>Scanning for Code Injection: Detecting Meterpreter</h3>
<p>We’ll now inspect whether any foreign code was injected into updater.exe. Volatility’s windows.malfind plugin is useful for detecting memory regions with suspicious execution permissions (like PAGE_EXECUTE_READWRITE), or shellcode that was injected at runtime using the command vol -f THM-WIN-001_071528_07052025.mem windows.malfind --pid 10032 > malfind_10032.txt. Then, let's analyze the output using cat, as displayed below.</p>

<p>Example Terminal</p>

```bash
user@tryhackme~$ cat malfind_10032.txt 
Volatility 3 Framework 2.26.0

PID	Process	Start VPN	End VPN	Tag	Protection	CommitCharge	PrivateMemory	File output	Notes	Hexdump	Disasm

10032	updater.exe	0x1a0000	0x1d1fff	VadS	PAGE_EXECUTE_READWRITE	50	1	Disabled	MZ header	
4d 5a 41 52 55 48 89 e5 48 83 ec 20 48 83 e4 f0 MZARUH..H.. H...
e8 00 00 00 00 5b 48 81 c3 37 5e 00 00 ff d3 48 .....[H..7^....H
81 c3 b4 b1 02 00 48 89 3b 49 89 d8 6a 04 5a ff ......H.;I..j.Z.
d0 00 00 00 00 00 00 00 00 00 00 00 f8 00 00 00 ................    
[REDACTED]:    pop    r10
[REDACTED]:    push   r10
[REDACTED]:    push   rbp
[REDACTED]:    mov    rbp, rsp
[REDACTED]:    sub    rsp, 0x20
[REDACTED]:    and    rsp, 0xfffffffffffffff0
[REDACTED]:    call   0x1a0015
[REDACTED]:    pop    rbx
[REDACTED]:    add    rbx, 0x5e37
[REDACTED]:    call   rbx
[REDACTED]:    add    rbx, 0x2b1b4
[REDACTED]:    mov    qword ptr [rbx], rdi
[REDACTED]:    mov    r8, rbx
[REDACTED]:    push   4
[REDACTED]:    pop    rdx
[REDACTED]:    call   rax
```

<p>If we spot a memory region marked with suspicious flags and containing what looks like a shellcode or executable, this is a strong indication of runtime injection. Meterpreter, in particular, is known to use reflective DLL injection, which shows up this way. From the above, we can observe an injection or traces of process injection since we can observe the characters MZ, which are usually the first bytes of a PE executable, meaning that updater.exe injected this into memory.<br><br>

Note: We can dump the memory for the process updater.exe PID (10032) for further inspection with the following command vol -f THM-WIN-001_071528_07052025.mem windows.memmap --pid 10032 --dump. This should create a file called pid.10032.dmp in our current directory, which contains the information on the process in memory.</p>

<h3>Confirming Meterpreter with YARA</h3>
<p>YARA is often used to search for known patterns or signatures inside malicious files. It allows us to define readable string or byte patterns that can help identify specific tools or payloads, like Meterpreter, based on their presence in memory or binaries.<br><br>

Since we suspect that updater.exe may be running a Meterpreter session, we can validate this by applying a YARA rule that searches for known Meterpreter-related patterns within the process memory. We'll use a rule based on common Meterpreter patterns as shown below.</p>

```bash
rule meterpreter_reverse_tcp_shellcode {
    meta:
        description = "Metasploit reverse_tcp shellcode"
    strings:
        $s1 = { fce8 8?00 0000 60 }
        $s2 = { 648b ??30 }
        $s3 = { 4c77 2607 }
        $s4 = "ws2_"
        $s5 = { 2980 6b00 }
        $s6 = { ea0f dfe0 }
        $s7 = { 99a5 7461 }
    condition:
        5 of them
}
```

<p>The rule below is designed to detect Metasploit's reverse_tcp shellcode by matching a combination of known byte patterns and strings commonly found in such payloads. It triggers if at least 5 of the listed patterns are present. Let's execute the command vol -f THM-WIN-001_071528_07052025.mem windows.vadyarascan --pid 10032 --yara-file meterpreter.yar to see if we can have match. This will scan only the memory regions allocated to the specified process, increasing the accuracy of detection. If the condition is met, it strongly suggests the presence of Meterpreter shellcod</p>

<p>Example Terminal</p>

```bash
user@tryhackme~$ vol -f THM-WIN-001_071528_07052025.mem windows.vadyarascan --pid 10032 --yara-file meterpreter.yar
Volatility 3 Framework 2.26.0
Progress:  100.00		PDB scanning finished                        
Offset	PID	Rule	Component	Value

0x140004104	10032	meterpreter_reverse_tcp_shellcode	$s3	
4c 77 26 07                                     Lw&.            
0x1400040d9	10032	meterpreter_reverse_tcp_shellcode	$s4	
77 73 32 5f                                     ws2_            
0x140004115	10032	meterpreter_reverse_tcp_shellcode	$s5	
29 80 6b 00                                     ).k.            
0x140004135	10032	meterpreter_reverse_tcp_shellcode	$s6	
ea 0f df e0                                     ....            
0x14000414a	10032	meterpreter_reverse_tcp_shellcode	$s7	
99 a5 74 61                                     ..ta   
```

<p>As we can observe from the output above, there are five matches within the process 10032 (updater.exe), confirming the presence of a Meterpreter session.<br><br>

By combining live connection details from windows.netscan, process ancestry and launch context via pslist and cmdline, memory injection indicators from malfind, signature-based confirmation through yarascan, and dump analysis using memdump and strings, we've confirmed that updater.exe isn't just suspicious by behavior. It was injected with malicious code and was almost certainly acting as a reverse shell handler (Meterpreter), closing the loop on the attacker’s foothold.<br><br>

In the next task, we’ll shift focus to possible exfiltration attempts or further staging activity using HTTP requests or services found in memory.</p>

<h3 align="left"> Answer the questions below</h3>

> 5.1. <em>What Volatility plugin can be used to correlate memory regions showing suspicious execution permissions with processes, helping to detect Meterpreter-like behavior?</em><br><a id='5.1'></a>
>> <strong><code>windows.malfind</code></strong><br>
<p></p>

<br>

> 5.2. <em>What is the virtual memory address space of the suspicious injected region in updater.exe? Answer format: 0xABCDEF</em> Hint : <em>Locate the pop r10 instruction using malfind.</em><br><a id='5.2'></a>
>> <strong><code>0x1a0000</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/403f4e9c-da51-4fdd-a627-7c77d7ac8960)

<br>

> 5.3. <em>What is the first 2-bytes signature found in the shellcode that was extracted from updater.exe using windows.malfind? Answer format: In hex.</em><br><a id='5.3'></a>
>> <strong><code>4d5a</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/fa2b5bec-b804-4f51-a9e3-89018881c2ce)

<br>

![image](https://github.com/user-attachments/assets/c4c76a49-53bb-4ea4-9d1a-835760dc86e4)

<br>


<h2> Task 6 .  Post-Exploitation Communication</h2>
<p>In the previous step, we discovered that updater.exe had been injected with shellcode matching known Meterpreter patterns. That connection reached out to the attacker's infrastructure at <code>10.0.0.129:8081</code>. In this task, we shift focus to what happened after that foothold was established.</p>p>

<h3>Looking for Post-Exploitation Traffic</h3>
<p></p>Now that the attacker had a reverse shell running, it’s reasonable to expect secondary connections for lateral movement, data staging, or command retrieval. We already observed two suspicious indicators from the <code>windows.netscan</code> output:<br>

- powershell.exe (<code>PID 6984</code>) established a connection to <code>192.168.0.30:22</code>, which appears to be a lateral move within the internal network.<br>
- windows-update.exe (</code>PID 10084</code>), previously seen listening on port <code>4443</code>, may have also generated outbound traffic.</p>

<p>Let’s confirm if any of these processes performed external communication.<br><br>

We'll begin by confirming again that the network session is tied to <code>powershell.exe</code>. Re-analyzing the output of the command <code>vol -f THM-WIN-001_071528_07052025.mem windows.netscan</code>, which we previously saved in netscan.txt. We’ll search for any connection entries associated with the <code>powershell.exe</code>. process using grep, as shown below.</p>

<p>Example Terminal</p>

```bash
Example Terminal
user@tryhackme~$ cat netscan.txt |grep powershell
0x990b29ab8010	TCPv4	192.168.1.192	55987	192.168.0.30	22	ESTABLISHED	6984	powershell.exe	2025-05-07 07:15:15.000000 UTC    
```

<p>The <code>PID</code> of the process <code>powershell.exe</code> can be observed above (<code>6984</code>). Let's dump that process and investigate further with the command <code>vol -f THM-WIN-001_071528_07052025.mem windows.memmap --pid 6984 --dump</code>code><br><br>

After that, we could look for interesting strings, but since we are already familiar with the connection we spotted, we can search for the IP we observed the connection made to, <code>192.168.0.30</code>. We can achieve that with the command strings, as shown below.</p>

<p>Example Terminal</p>

```bash
user@tryhackme~$ strings pid.6984.dmp|grep "192.168.0.30"
$client=New-Object Net.Sockets.TcpClient; $client.Connect("192.168.0.30",22); while($client.Connected){Start-Sleep 1}
$client=New-Object Net.Sockets.TcpClient; $client.Connect("192.168.0.30",22); while($client.Connected){Start-Sleep 1}
```

<p>As we can observe, we had two matches from our search, revealing the command used to connect to the host at 192.168.0.30 (server network) that was used to connect to and from the previous analysis. We know it's involved in the attack chain and was installed for persistence.<br><br>

Let’s dump the memory space of the process that initiates this chain: windows-update.exe (PID 10084) to examine whether HTTP content was stored in memory, perhaps from a C2 address or data exfiltration, for that, we'll use the command vol -f THM-WIN-001_071528_07052025.mem windows.memmap --pid 10084 --dump<br><br>

After creating the dump, we can search for the known domain attacker.thm by using the strings command in combination with grep, as shown below.</p>

<p>Example Terminal</p>

```bash
user@tryhackme~$ strings pid.10084.dmp |grep "attacker.thm"
attacker.thm
http://attacker.thm/updater.exe
external-attacker.thm
Failed to connect to external-attacker.thm:25
Connected to external-attacker.thm:25 successfully.
[REDACTED]
```

<p>We can see that, in addition to the domain attacker.thm, a subdomain external.attacker.thm also appears in the process memory. There's also a possible connection over port 25 (SMTP), based on the extracted strings.<br><br>

Next, we’ll search for the term POST to check if any HTTP requests were made, possibly as part of a data exfiltration attempt. We'll use the -C 8 option with grep to display 8 lines before and after each match for better context.</p>

<p>Example Terminal</p>

```bash
ubuntu@tryhackme:~$ strings pid.10084.dmp |grep "POST" -C 8
bad cast
attacker.thm
C:\Windows\System32\drivers\etc\hosts
[!] Failed to open hosts file.
Exfiltrator
[!] InternetOpenA failed.
[!] InternetConnectA failed.
Content-Type: application/x-www-form-urlencoded
POST
[!] HttpOpenRequestA failed.
[!] HttpSendRequestA failed.
[+] Hosts file exfiltrated to http://
[*] Executing hello()
```

<p>As we can observe, the process tried a <code>POST</code> connection, but it seemed to fail. We've confirmed that <code>powershell.exe</code> established a live connection to another host, and windows-update.exe attempted to send an <code>HTTP</code> <code>POST</code> request to the attacker's domain. These behaviors point to continued activity beyond initial access, suggesting both processes were involved in the post-exploitation stage of the attack.</p>

<h3 align="left"> Answer the questions below</h3>

> 6.1. <em>Which local port was used by powershell.exe to connect to the internal host 192.168.0.30?</em><br><a id='6.1'></a>
>> <strong><code>55987</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/73b7d4b7-9398-4e70-92d0-7e757a990edb)


<br>

> 6.2. <em>What was the remote IP address targeted by windows-update.exe during its HTTP POST attempt?</em><br><a id='6.2'></a>
>> <strong><code>10.0.0.129</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/60d69473-8fc7-421b-ac35-c53b38583add)


<br>

> 6.3. <em>What port was windows-update.exe listening on, based on the netscan output?</em><br><a id='6.3'></a>
>> <strong><code>4443</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/175f98af-92c2-4233-8e56-7c821f339df5)

<br>


<h2> Task 7 .  Putting it All Together</h2>

<p>Across these three rooms, we reconstructed a full attack chain that started with a phishing-style document and ended with a Meterpreter shell and lateral movement. Each stage was uncovered by correlating memory artifacts using Volatility 3. Our starting point was a malicious macro-enabled Word document (.docm) opened by WINWORD.EXE. Using plugins like pslist, cmdline, and memmap, we observed the macro spawning pdfupdater.exe, a first-stage dropper that quickly launched windows-update.exe.<br><br>

From there, windows-update.exe launched updater.exe. Using netscan, we identified an active outbound connection from updater.exe to an external IP address (10.0.0.129:8081). Following this, we observed post-exploitation activity. cmd.exe and powershell.exe were both launched under the same session as the earlier processes, and PowerShell established a connection to an internal host (192.168.0.30) over port 22. This behavior strongly indicates lateral movement. We can summarize the attack chain below.<br><br>

- Initial Access: The user opened a macro-enabled .docm document with WINWORD.EXE, which loaded a .docm template file containing a VBA macro. The macro downloaded and executed pdfupdater.exe.
- Execution & Persistence: pdfupdater.exe launched windows-update.exe, a malicious binary placed in the user’s Startup folder for persistence. This process spawned updater.exe.
- Remote Access (C2): updater.exe established an outbound connection to 10.0.0.129:8081, where reflective DLL injection was confirmed using malfind, and Meterpreter shellcode was detected via vadyarascan.
- Post-Exploitation: Following the C2 session, cmd.exe and powershell.exe were launched. The latter connected to 192.168.0.30:22, suggesting lateral movement to a second internal host. The PowerShell payload was recovered from memory.
- Exfiltration Attempts: Memory strings in windows-update.exe showed attempts to POST data to attacker.thm and external-attacker.thm, although the exfiltration failed.</p>


<h3>MITRE ATT&CK Technique Mapping</h3>
<p>Below is a table summarizing each discovery, the corresponding Volatility plugin used to uncover it, and the mapped MITRE ATT&CK technique.</p>

![image](https://github.com/user-attachments/assets/5888f172-07e8-4b24-a46a-e5dd7fd68f6c)

<h3 align="left"> Answer the questions below</h3>

> 7.1. <em>What IP did updater.exe connect to for the reverse shell?</em><br><a id='7.1'></a>
>> <strong><code>10.0.0.129</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/085692b3-5e18-4cb6-911e-18d249dd649e)


<br>

> 7.2. <em>Which folder is used for persistence by the attack we analyzed within this memory dump?</em><br><a id='7.2'></a>
![image](https://github.com/user-attachments/assets/2dc5a77a-3206-4015-8ab1-23a0801a7257)


![image](https://github.com/user-attachments/assets/f340a34a-bf40-4193-a1f0-c4575c59be12)

<br>

> 7.3. <em>Which MITRE technique matches the reflective DLL injection used by updater.exe?</em><br><a id='7.3'></a>
>> <strong><code>T1055.002</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/fe1015bd-224b-4e27-b1eb-35ba79e30b73)

<br>

> 7.4. <em>What is the domain that was discovered within the windows-update.exe file?</em><br><a id='7.4'></a>
>> <strong><code>external-attacker.thm</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/a115095c-f747-4b61-ac87-9f2962975cf7)


<br>

<h2> Task 8 .  Conclusion</h2>
<p>In this room, we extended our forensic investigation by focusing on network activity and post-exploitation behavior captured in memory. We traced connections to attacker infrastructure, confirmed malicious payloads, and uncovered evidence of lateral movement, all from a single memory snapshot.<br><br>

What we practiced:<br>

- Identifying active and closed network connections
- Correlating connections with processes.
- Detecting memory injection.
- Dumping and analyzing process memory.
- Matching Meterpreter shellcode.
- Investigating PowerShell-based lateral movement and HTTP from memory.<br><br>

Let's continue our memory analysis journey in the next room of this module.</p>

<h3 align="left"> Answer the questions below</h3>

> 8.1. <em>Click to finish the room.</em><br><a id='8.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>


<br>
<br>

<h1 align="center">Room Completed</h1>
<br>
<p align="center"><img width="1000px" src="https://github.com/user-attachments/assets/c05f961c-a881-4b1c-aeb3-4167fc648734"><br>
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
