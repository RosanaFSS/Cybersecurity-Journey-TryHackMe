<h5 align="center">December 4, 2024<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{212}}$$-day-streak in  <a href="https://tryhackme.com/">TryHackMe</a>.</h5>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Advent of Cyber 2024}}$$</h1>

<h5 align="center">Dive into the wonderful world of cyber security by engaging<br>
in festive beginner-friendly exercises every day in the lead-up to Christmas!</h5>

<p align="center">
<img height="90px" hspace="20" src="https://github.com/user-attachments/assets/0d8d7f29-525a-49ad-85ba-9223bdec089b">
<img width="500px" src="https://github.com/user-attachments/assets/57999429-f784-46a1-81ab-4d68041f470f"></p>

<p align="center">Access this 🆓 TryHackMe CTF challenge clicking <a href="https://tryhackme.com/r/room/adventofcyber2024">Advent of Cyber 2024</a>.</p>

<h2 align="center"> $$\textcolor{yellow}{\textnormal{Day 4 - Atomic Red Team}}$$<br>
$$\textcolor{yellow}{\textnormal{I’m all atomic inside!}}$$</h2>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/c81cd5bb-2ded-4166-9a45-45bed67cd3dd"></p>

<p>SOC-mas is approaching! And the town of Warewille started preparations for the grand event.<br>

Glitch, a quiet, talented security SOC-mas engineer, had a hunch that these year's celebrations would be different. With looming threats, he decided to revamp the town's security defences. Glitch began to fortify the town's security defences quietly and meticulously. He started by implementing a protective firewall, patching vulnerabilities, and accessing endpoints to patch for security vulnerabilities. As he worked tirelessly, he left "breadcrumbs," small traces of his activity.<br>

Unaware of Glitch's good intentions, the SOC team spotted anomalies: Logs showing admin access, escalation of privileges, patched systems behaving differently, and security tools triggering alerts. The SOC team misinterpreted the system modifications as a sign of an insider threat or rogue attacker and decided to launch an investigation using the Atomic Red Team framework.</p>


<p align="center"><img src="https://github.com/user-attachments/assets/f054e181-2496-4ace-bb46-244099d02cae" width="400"></p>

<h3><strong>Learning Objectives</strong></h3>
<p>While it might seem like using the SOC superpower makes things super easy, that is not always the case. There are cases which can act as Kryptonite to the SOC superpower
    
<ul style="list-style-type:square">
    <li>Learn how to identify malicious techniques using the MITRE ATT&CK framework.</li>
    <li>Learn about how to use Atomic Red Team tests to conduct attack simulations.</li>
    <li>Understand how to create alerting and detection rules from the attack tests.</li>
</ul></p>

<h3><strong>Connecting to the Machine</strong></h3>

<p>Before moving forward, review the questions in the connection card below:</p>

<p align="center"><img width="300px" src="https://github.com/user-attachments/assets/cddb96af-873f-4217-815f-d108c56fcea8"></p>

<p>Click on the green <code>Start Machine</code> button below to start the virtual machine machine and wait 1-2 minutes for the system to boot completely in a split-screen view.</p>

<p><code>Start Machine</code></p>

<p>YIf the virtual machine isn't visible, use the blue <code>Show Split View</code> button at the top of the page.<br>

Additionally, if you wish to connect to the machine via RDP, use the credentials below:</p>

<p align="center"><img width="300px" src="https://github.com/user-attachments/assets/278d53a8-148f-4323-bec8-dfdc94cd205b"></p>

<p>The VM has Atomic Red Team and Sysmon installed. This will allow us to emulate an attack using TTPs described in the MITRE ATT&CK framework.</p>

<br>
<br>
<h2><strong>Detection Gaps</strong></h2>
<p>While it might be the utopian dream of every blue teamer, we will rarely be able to detect every attack or step in an attack kill chain. This is a reality that all blue teamers face: there are gaps in their detection. But worry not! These gaps do not have to be the size of black holes; there are things we can do to help make these gaps smaller.<br>

Detection gaps are usually for one of two main reasons:</p>

- <code>Security is a cat-and-mouse game</code>. As we detect more, the threat actors and red teamers will find new sneaky ways to thwart our detection. We then need to study these novel techniques and update our signature and alert rules to detect these new techniques.
- <code>The line between anomalous and expected behaviour is often very fine and sometimes even has significant overlap</code>. For example, let's say we are a company based in the US. We expect to see almost all of our logins come from IP addresses in the US. One day, we get a login event from an IP in the EU, which would be an anomaly. However, it could also be our CEO travelling for business. This is an example where normal and malicious behaviour intertwine, making it hard to create accurate detection rules that would not have too much noise.

<p>Blue teams constantly refine and improve their detection rules to close the gaps they experience due to the two reasons mentioned above. Let's take a look at how this can be done!</p>

<br>
<br>
<h2><strong>Cyber Attacks and the Kill Chain</strong></h2>
<p>Before diving into creating new detection rules, we first have to discuss some key topics. The first topic to discuss is the Cyber Kill chain. All cyber attacks follow a fairly standard process, which is explained quite well by the Unified Cyber Kill chain:</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/6d4e38f4-4ab9-46f2-b2c7-70105f1ec0b0"></p>

<p>As a blue teamer, it would be our dream to prevent all attacks at the start of the kill chain. So even just when threat actors start their reconnaissance, we already stop them dead in their tracks. But, as discussed before, this is not possible. The goal then shifts slightly. If we are unable to fully detect and prevent a threat actor at any one phase in the kill chain, the goal becomes to perform detections across the entire kill chain in such a way that even if there are detection gaps in a single phase, the gap is covered in a later phase. The goal is, therefore, to ensure we can detect the threat actor before the very last phase of goal execution.</p>

<br>
<br>
<h2><strong>MITRE ATT&CK</strong></h2>
<p>A popular framework for understanding the different techniques and tactics that threat actors perform through the kill chain is the <a href="https://attack.mitre.org/">MITRE ATT&CK framework</a>. The framework is a collection of tactics, techniques, and procedures that have been seen to be implemented by real threat actors. The framework provides a <a href="https://mitre-attack.github.io/attack-navigator/">navigator tool</a> where these TTPs can be investigated:</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/328b7875-c99e-467a-b1d2-cf3153b3f0bd"></p>

<p>However, the framework primarily discusses these TTPs in a theoretical manner. Even if we know we have a gap for a specific TTP, we don't really know how to test the gap or close it down. This is where the Atomics come in!</p>

<br>
<br>
<h2><strong>Atomic Red</strong></h2>
<p>The Atomic Red Team library is a collection of red team test cases that are mapped to the MITRE ATT&CK framework. The library consists of simple test cases that can be executed by any blue team to test for detection gaps and help close them down. The library also supports automation, where the techniques can be automatically executed. However, it is also possible to execute them manually.</p>

<br>
<br>
<h2><strong>Dropping the Atomic</strong></h2>
<p>McSkidy has a vague idea of what happened to the "compromised machine." It seems someone tried to use the Atomic Red Team to emulate an attack on one of our systems without permission. The perpetrator also did not clean up the test artefacts. Let's have a look at what happened.</p>

<br>
<br>
<h2><strong>Running an Atomic</strong></h2>
<p>McSkidy suspects that the supposed attacker used the MITRE ATT&CK technique  <a href="https://attack.mitre.org/techniques/T1566/001/">T1566.001 Spearphishing</a> with an attachment. Let's recreate the attack emulation performed by the supposed attacker and then look for the artefacts created.<br>

Open up a PowerShell prompt as administrator and follow along with us. Let's start by having a quick peek at the help page. Enter the command <code>Get-Help Invoke-Atomictest</code>. You should see the output below:</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/5cdfa921-3bf4-43cd-a121-a28d8bfeb491"></p>

<p>The help above only shows what parameters are available without any explanation. Even though most parameter names are self-explanatory, let us have a quick overview of the parameters we will use in this walkthrough:</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/90f712c2-d71c-42fa-b809-ef6b2d2b84fd"></p>

<h3><strong>Our First Command</strong></h3>
<p>We can build our first command now that we know which parameters are available. We would like to know more about what exactly happens when we test the Technique T1566.001. To get this information, we must include the name of the technique we want information about and then add the flag <code>-ShowDetails</code> to our command. Let's have a look at the command we constructed: <code>Invoke-AtomicTest T1566.001 -ShowDetails</code>. This command displays the details of all tests included in the T1566.001 Atomic.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/20ae7604-a9db-47c0-bf42-da7bf7558c96"></p>

<p>The output above is clearly split up into multiple parts, each matching a test. Let's examine what type of information is provided in a test. We will use the test we want to run as an example.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/17e102f1-17f1-43ee-91eb-18f76becc0c2"></p>

<h3><strong>Phishing: Spearphishing Attachment T1566.001 Emulated</strong></h3>

<p>Let's continue and run the first test of T1566.001. Before running the emulation, we should ensure that all required resources are in place to conduct it successfully. To verify this, we can add the flag <code>-Checkprereq</code> to our command. The command should look something like this: <code>Invoke-AtomicTest T1566.001 -TestNumbers 1 -CheckPrereq</code>.<br>

This command will use the data included in the "dependencies" part of the test details to verify if all required resources are present. Looking at the test 1 dependencies of the T1566.001 Atomic, no additional resources are required. Run the same command for test 2, and it will state that Microsoft Word needs to be installed, as shown below:</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/d3b80b42-7d51-4e29-a9df-fb0f167c1693"></p>

<p>Now that we have verified the dependencies, let us continue with the emulation. Execute the following command to start the emulation: <code>Invoke-AtomicTest T1566.001 -TestNumbers 1</code> and you should get the following output:</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/3c2eee17-81bf-4d18-9662-fdf12971a551"></p>

<p>Based on the output, we can determine that the test was successfully executed. We can now analyse the logs in theWindows Event Viewer to find Indicators of Attack and Compromise.</p>


<br>
<br>
<h2><strong>Detecting the Atomic</strong></h2>
<p>Now that we have executed the T1566.001 Atomic, we can look for log entries that point us to this emulated attack. For this purpose, we will use the Windows Event Logs. This machine comes with Sysmon installed. System Monitor (Sysmon) provides us with detailed information about process creation, network connections, and changes to file creation time.<br>

To make it easier for us to pick up the events created for this emulation, we will first start with cleaning up files from the previous test by running the command Invoke-AtomicTest T1566.001 -TestNumbers 1 -cleanup.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/ed61e03d-f40c-4a50-9569-a4997ddfd541"></p>


<p>Now, we will clear the Sysmon event log:</p>

- Open up Event Viewer by clicking the icon in the taskbar, or searching for it in the Start Menu.<br>
- Navigate to Applications and Services => Microsoft => Windows => Sysmon => Operational on the left-hand side of the screen.<br>
- Right-click Operational on the left-hand side of the screen and click Clear Log. Click Clear when the popup shows.<br>

<p>Now that we have cleaned up the files and the sysmon logs, let us run the emulation again by issuing the command Invoke-AtomicTest T1566.001 -TestNumbers 1.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/902f157f-ce73-4991-95d9-111f3e1bc6a8"></p>

<p>Next, go to the Event Viewer and right-click on the Operational log on the left-hand side of the screen and then click on Refresh. There should be new events related to the emulated attack. Now sort the table on the Date and Time column to order the events chronologically (oldest first). The first two events of the list are tests that Atomic executes for every emulation. We are interested in 2 events that detail the attack:</p>

- First, a process was created for PowerShell to execute the following command: "powershell.exe" & {$url = 'http://localhost/PhishingAttachment.xlsm' Invoke-WebRequest -Uri $url -OutFile $env:TEMP\PhishingAttachment.xlsm}.
- Then, a file was created with the name PhishingAttachment.xlsm.

<p>Click on each event to see the details. When you select an event, you should see a detailed overview of all the data collected for that event. Click on the Details tab to show all the EventData in a readable format. Let us take a look at the details of these events below. The data highlighted is valuable for incident response and creating alerting rules.</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/a70437be-908b-4265-b3e9-1a91cde1fab7"></p>

<p>Navigate to the directory C:\Users\Administrator\AppData\Local\Temp\, and open the file PhishingAttachment.txt. The flag included is the answer to question 1. Make sure to answer the question now, as the cleanup command will delete this file.

Let's clean up the artefacts from our spearphishing emulation. Enter the command Invoke-AtomicTest T1566.001-1 -cleanup.

Now that we know which artefacts were created during this spearphishing emulation, we can use them to create custom alerting rules. In the next section, we will explore this topic further.</p>

<br>
<br>
<h2><strong>Alerting on the Atomic</strong></h2>
<p>In the previous paragraph, we found multiple indicators of compromise through the Sysmon event log. We can use this information to create detection rules to include in our EDR, SIEM, IDS, etc. These tools offer functionalities that allow us to import custom detection rules. There are several detection rule formats, including Yara, Sigma, Snort, and more. Let's look at how we can implement the artefacts related to T1566.001 to create a custom Sigma rule.<br>

Two events contained possible indicators of compromise. Let's focus on the event that contained the Invoke-WebRequest command line:<br>

"powershell.exe" & {$url = 'http://localhost/PhishingAttachment.xlsm' Invoke-WebRequest -Uri $url -OutFile $env:TEMP\PhishingAttachment.xlsm}"<br>

We can use multiple parts of this artefact to include in our custom Sigma rule.</p>

- Invoke-WebRequest: It is not common for this command to run from a script behind the scenes.

- $url = 'http://localhost/PhishingAttachment.xlsm': Attackers often use a specific malicious domain to host their payloads. Including the malicious URL in the Sigma rule could help us detect that specific URL.

- PhishingAttachment.xlsm: This is the malicious payload downloaded and saved on our system. We can include its name in the Sigma rule as well.

- <p>Combining all these pieces of information in a Sigma rule would look something like this:</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/01fd1877-6356-4fd4-b368-260556a7b47a"></p>

<p>The <code>detection</code> part is where the effective detection is happening. We can see clearly the artefacts that we discovered during the emulation test. We can then import this rule into the main tools we use for alerts, such as the EDR, SIEM, XDR, and many more.

Now that Glitch has shown us his intentions, let's continue with his work and run an emulation for ransomware.</p>

<br>
<br>
<h2><strong>Challenge</strong></h2>
<p>As Glitch continues to prepare for SOC-mas and fortifies Wareville's security, he decides to conduct an attack simulation that would mimic a ransomware attack across the environment. He is unsure of the correct detection metrics to implement for this test and asks you for help. Your task is to identify the correct atomic test to run that will take advantage of <code>a command and scripting interpreter</code>, conduct the test, and extract valuable artefacts that would be used to craft a detection rule.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>What was the flag found in the .txt file that is found in the same directory as the <code>PhishingAttachment.xslm</code> artefact?</em><br><a id='1.1'></a>
>> <code><strong>THM{GlitchTestingForSpearphishing}</strong></code>

<br>

![image](https://github.com/user-attachments/assets/c08542f5-e068-49ad-b7aa-e11bb707514e)

<br>

![image](https://github.com/user-attachments/assets/7b30fb1d-81c3-40b2-8ae7-a2cd0d3831b9)

<br>

![image](https://github.com/user-attachments/assets/a0be7306-4476-4cf0-b637-0f2bb911f5d9)

<br>
<br>

> 1.2. <em>What ATT&CK technique ID would be our point of interest?</em><br><a id='1.2'></a>
>> <code><strong>T1059</strong></code>

<br>

![image](https://github.com/user-attachments/assets/0ba27ba0-36db-4f0d-9960-1b9e62d4bfa5)

<br>

![image](https://github.com/user-attachments/assets/52ddda63-1a30-4eed-baa5-8bf5d045c91a)


<br>
<br>

> 1.3. <em>What ATT&CK subtechnique ID focuses on the Windows Command Shell?</em><br><a id='1.3'></a>
>> <code><strong>T1059.003</strong></code>

<br>

![image](https://github.com/user-attachments/assets/4b6023a1-9c89-452a-b0de-8c6931a75f2f)

<br>
<br>


> 1.4. <em>What is the name of the Atomic Test to be simulated?</em><br><a id='1.4'></a>
>> <code><strong>Simulate BlackByte Ransomware Print Bombing</strong></code>

<br>

<pre><code> Invoke-AtomicTest T1059.003 -ShowDetails</code></pre>

<br>

![image](https://github.com/user-attachments/assets/eb65b3dd-65ff-4689-8f91-39b1b0531e1a)


<p>...</p>

![image](https://github.com/user-attachments/assets/24c5acd2-98b1-4aaf-b228-04b8870641f9)


<p>...</p>

![image](https://github.com/user-attachments/assets/e7bf8341-063e-4874-a78e-545465f3db8a)


<p>...</p>

![image](https://github.com/user-attachments/assets/4333b853-697f-4e0f-8cf5-cf77fbe10ee3)

<p>...</p>

![image](https://github.com/user-attachments/assets/af8d50bf-cd8d-4896-98ec-66632c4b4f6d)


<br>
<br>


> 1.5. <em>What is the name of the file used in the test?</em><br><a id='1.5'></a>
>> <code><strong>Wareville_Ransomware.txt</strong></code>

<br>

![image](https://github.com/user-attachments/assets/4f9c72cf-b84b-495a-857c-65f8f9077e4e)

<br>
<br>



> 1.6. <em>What is the flag found from this Atomic Test?</em><br><a id='1.6'></a>
>> <code><strong>THM{R2xpdGNoIGlzIG5vdCB0aGUgZW5lbXk=}</strong></code>

<br>

![image](https://github.com/user-attachments/assets/0451bab1-014a-4ff6-80b4-c4c3ec62a1aa)



<br>
<br>

> 1.7. <em>Learn more about the Atomic Red Team via the linked room.?</em><br><a id='1.7'></a>
>> <code><strong>No answer needed</strong></code>

<br>


<br>
<br>

<h2>Task Completed<a id='2'></a></h2>
<p>Keep learning, keep growing!<br>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/3a5fcb9a-1336-49f5-9b60-642c74787343"> </h3>


<h2>My Journey<a id='3'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| December 4, 2024  | 212      |     1,049 th |        22 nd |     2,852th |      39 th |  58,986  |       453 |

</div>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/07b733fc-b209-4302-8112-7e9f3caf2831"> </h3>
