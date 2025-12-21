<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 16 &nbsp;&nbsp; ·  &nbsp;&nbsp; Forensics - Registry Furensics</h3>
<p align="center">2025, December 20  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in <a href="https://tryhackme.com">TryHackMe</a>.<br>Learn what the Windows Registry is and how to investigate it. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/registry-forensics-aoc2025-h6k9j2l5p8">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/ee0b461e-7b37-4b9f-b249-dfdaf33aab76"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/ebc91417-b06f-40b1-9977-30a4c85a885d"></p>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/2f301ab5-9918-4001-b383-a917ce3aab6b"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>TBFC is under attack. Systems are exhibiting weird behavior, and the company is now feeling the absence of its lead defender, McSkidy. However, McSkidy made sure the legacy continues.<br>

McSkidy’s team, determined and well-trained, is fully confident in securing all the systems and regaining control before the big event, SOCMAS.<br>

They have now decided to conduct a detailed forensic analysis on one of the most critical systems of TBFC, dispatch-srv01. The dispatch-srv01 coordinates the drone-based gifts delivery during SOCMAS. However, recently it was compromised by King Malhare’s bandits of bunnies.<br>

TBFC’s defenders have decided to split into specialized teams to uncover the attack on this system through detailed forensics. While some of the other team members investigate logs, memory dumps, file systems, and other artefacts, you will work to investigate the registry of this compromised system.</p>

<h6 align="center"><img width="300px" src="https://github.com/user-attachments/assets/293a1f59-5b46-4390-bd4e-3a174b0673a9"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>



<h3>Learning Objectives</h3>
<p>
  
- Understand what the Windows Registry is and what it contains.<br>
- Dive deep into Registry Hives and Root Keys.<br>
- Analyze Registry Hives through the built-in Registry Editor tool.<br>
- Learn Registry Forensics and investigate through the Registry Explorer tool.</p>

<h3>Connecting to the Machine</h3>
<p>Before moving forward, review the questions in the connection card shown below:</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/f82ba0fb-4efa-412b-9959-0e32aab77802"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Start your target VM by clicking the <strong>Start Machine</strong> button below. The machine will need about 3 minutes to fully boot. Additionally, start your AttackBox by clicking the <strong>Start AttackBox</strong> button below. The AttackBox will start in split view. In case you can not see it, click the <strong>Show Split View</strong> at the top of the page.</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p>Alternatively, you can use the credentials below to connect to the target machine via RDP from your own THM VPN connected machine:<br>

- Username: ...<br>
- Password: ...<br>
- IP address: ...<br>
- Connection via: RDP</p>

<br>
<p><em>Answer the question below</em></p>

<p>1.1. <em>I successfully have access to my target machine!</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 &nbsp; ·  &nbsp; Investigate the Gifts Delivery Malfunctioning</h2>
<h3>Windows Registry</h3>
<p>Your brain stores all the information that you need to function effectively. This includes:<br>

- How should you behave?<br>
- What would be the first thing you would do after waking up?<br>
- How would you dress yourself?<br>
- What are your habits?<br>
- What happened in the recent past?<br><br>

These are just a few things. Your brain knows pretty much everything about you. It's just like a database storing the human configuration.<br>

Windows OS is not a human, but it also needs a brain to store all its configurations. This brain is known as the Windows Registry. The registry contains all the information that the Windows OS needs for its functioning.<br>

Now, this Windows brain (Registry) is not stored in one single place, unlike a human brain, which is situated in one single place inside the head. It is made up of several separate files, each storing information on different configuration settings. These files are known as <strong>Hives</strong>.</p>

<h6 align="center"><img width="280px" src="https://github.com/user-attachments/assets/bdb738b8-0cf0-4575-a853-ab7594034f56"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Let's take a look at all these hives in the table below. The first column contains the hive names, the second column contains the type of configuration settings that each hive stores, and the third column contains the location of each hive on the disk. </p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/6d1a7452-cd3a-4e50-b633-3f742dd348de"><br><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><strong>Note</strong>: The configuration settings stored in each hive listed above are just a few examples. Each hive stores more than these.<br>

Now that you understand where these Registry Hives are stored, you may be tempted to double-click and open these files from their respective locations to view the data they contain. But here's the twist. These Registry Hives contain binary data that cannot be opened directly from the file. So, double-clicking them would only display things you won't ever understand. Then how can we possibly view the registry data?<br>

The Windows OS has a built-in tool known as the <strong>Registry Editor</strong>, which allows you to view all the registry data available in these hives. You can go ahead and open this tool by simply typing Registry Editor in your search bar.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/03689710-61b2-4c53-bb07-bc7e6a33fa25"><br><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>As you can see in the Registry Editor screenshot above, there are some folders named <code>HKEY_LOCAL_MACHINE</code>, <code>HKEY_CURRENT_USER</code>, and more. But didn't we expect <code>SYSTEM</code>, <code>SECURITY</code>, <code>SOFTWARE</code>, etc., to be seen so we can view their data? Don't worry, Windows organizes all the Registry Hives into these structured Root Keys. Instead of seeing the Registry Hives, you would always get these registry root keys whenever you open the registry. Now, which registry key contains which registry hive's data? To answer this question, we have a table below that maps the registry keys with their respective Registry Hives.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/61c1a826-b121-4891-80e2-a601c4447712"><br><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>In the table above, you can see that most of the Registry Hives are located under the <code>HKEY_LOCAL_MACHINE (HKLM)</code> key. We can verify this by clicking on the little toggle arrow at the on the left side of the <code>HKLM</code> key in the Registry Editor, as shown in the screenshot below:</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/997f459f-a159-49cf-8888-d344f00a9a30"><br><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>As you can see, the <code>SYSTEM</code>, <code>SOFTWARE</code>, <code>SECURITY</code>, and <code>SAM</code> hives are under the <code>HKLM</code> key. <code>NTUSER.DAT</code> and <code>USRCLASS.DAT</code> are located under <code>HKEY_USERS (HKU)</code> and <code>HKEY_CURRENT_USER (HKCU)</code>.<br>

<strong>Note</strong>: The other two keys (<code>HKEY_CLASSES_ROOT (HKCR)</code> <code>and HKEY_CURRENT_CONFIG (HKCC)</code>) are not part of any separate hive files. They are dynamically populated when Windows is running.<br>

So far, we have learned what the registry is, where it is located (in separate Registry Hives), and how to view the registry through the Registry Editor, which displays the registry keys backed by these Registry Hives.<br>

Now, let's see how we can actually extract information from the registry. Think of it like navigating to different files in the file explorer. If you know the path where the file is stored, you can go directly to that location to find the file. Let's take a look at a few examples:</p>

<h3>Example 1: View Connected USB Devices</h3>
<p><strong>Note</strong>: The registry key contents explained in this example are not available in the attached VM.<br>

The registry stores information on the USB devices that have been connected to the system. This information is present in the <code>SYSTEM</code> hive. To view it:<br>

- Open the Registry Editor.
- Navigate to the following path: <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR</code>.
- Here you will see the USB devices' information (make, model, and device ID).
- Each device will have the following:<br>A main subkey that is the identification of the type and manufacturer of the USB device.<br>A subkey under the above (for example) that represents the unique devices under this model.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/b40b21f7-8729-47be-8bc5-71a31e00793b"><br><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>


<h3>Example 2: View Programs Run by the User</h3>
<p>The registry stores information on the programs that the user ran using the Run dialog Win + R. This information is present in the NTUSER.DAT hive. To view it:<br>

- Open the Registry Editor.<br>
- Navigate to the following path: <code>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU</code>.<br>
- Here you will see the list of commands typed by the user in the Run dialog to run applications.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/58fa7427-1d3a-4cfa-b6f8-961429da7761"><br><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Registry Forensics</h3>
<p>Since the registry contains a wide range of data about the Windows system, it plays a crucial role in forensic investigations. Registry forensics is the process of extracting and analyzing evidence from the registry. In Windows digital forensic investigations, investigators analyze registry, event logs, file system data, memory data, and other relevant data to construct the whole incident timeline.<vr></vr>

The table below lists some registry keys that are particularly useful during forensic investigations.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/3e8cc951-0fb8-4dd9-a792-6f89a6efdc90"><br><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Numerous other registry keys can be used for extracting important evidence from a Windows system during an incident investigation. The investigation of these registry keys during forensics cannot be done via the built-in Registry Editor tool. It is because the Registry analysis cannot be done on the system under investigation (due to the chance of modification), so we collect the Registry Hives and open them offline into our forensic workstation. However, the Registry Editor does not allow opening offline hives. The Register editor also displays some of the key values in binary which are not readable.<br>

To solve this problem, there are some tools built for registry forensics. In this task you will use the  <a href="https://ericzimmerman.github.io/">Registry Explorer</a> tool which is a registry forensics tool. It is open source and can parse the binary data out of the registry, and we can analyze it without the fear of modification.</p>

<h3>Practical</h3>
<p>In this practical example, we will use the Registry Explorer tool to analyze the Registry Hives from the compromised system, <code>dispatch-srv01</code>. The Registry Hives have been collected and are available in the folder <code></code>C:\Users\Administrator\Desktop\Registry</code> Hives on the machine attached to this task.</p>

<h4>Step 1: Launch Registry Explorer</h4>
<p>Click on the Registry Explorer icon pinned to the taskbar of the target machine to launch it.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/b3179f4e-6ed8-4551-9a2b-1dc94d223ba4"><br><br>This image and all the theoretical content ofthe present article is TryHackMe´s property.</h6>

<h4>Step 2: Load the Registry Hives</h4>
<p>Once Registry Explorer opens with an empty interface, follow these steps to load the hives:<br>

- Click the File option from the top menu<br>
- Select Load hive from the dropdown</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/dae29207-7cee-4dd5-8904-8e17a3ad8d53"><br><br>This image and all the theoretical content ofthe present article is TryHackMe´s property.</h6>

<h4>Step 3: Handling Dirty Hives</h4>
<p>While loading Registry Hives, it is important to know that these Registry Hives can sometimes be "dirty" when collected from live systems, meaning they may have incomplete transactions. To ensure clean loading:<br>

- On the Load hives pop-up, navigate to C:\Users\Administrator\Desktop\Registry Hives<br>
- Select the desired hive file (e.g., SYSTEM)<br>
- Hold SHIFT, then press Open to load associated transaction log files. This ensures you get a clean, consistent hive state for analysis.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/799db118-528b-4947-b11e-4fb74aedd90a"><br><br>This image and all the theoretical content ofthe present article is TryHackMe´s property.</h6>

<p>
  
- You'll be prompted with a message indicating successful replay for transaction logs<br>
- Repeat the same process for all the other hives you want to load</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/639bf194-de34-4292-90a8-3079fb4d56f0"><br><br>This image and all the theoretical content ofthe present article is TryHackMe´s property.</h6>

<h4>Step 4: Investigating Registry Keys</h4>
<p>After loading the <code>SYSTEM</code> hive, you can navigate to specific registry keys for investigation. Let's practice by finding the computer name:<br>

- Navigate to: <code>ROOT\ControlSet001\Control\ComputerName\ComputerName</code>. Or you can also just type "ComputerName" in the search bar to quickly locate the key, as shown below.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/1cb48f1f-99ac-4c0d-8e73-238ac7a9ad1b"><br><br>This image and all the theoretical content ofthe present article is TryHackMe´s property.</h6>

<p>

- Alternatively, you can click the <strong>Available Bookmarks</strong> tab and navigate to the <strong>ComputerName</strong> key from there.<br>
- Examine the values to identify the system's hostname. Under the <strong>Data</strong> value, you'll find <code>DISPATCH-SRV01</code>.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/e6df0b44-5271-472b-8bb0-52efca9475b0"><br><br>This image and all the theoretical content ofthe present article is TryHackMe´s property.</h6>


<p>Now that you understand how to load hives and navigate in Registry Explorer, you're ready to begin your forensic investigation and uncover evidence of the TBFC intrusion on the Dispatch server!<br>

<strong>Note</strong>: The abnormal activity on the <code>dispatch-srv01</code> started on 21st October, 2025.<br>

<strong>Tip</strong>: The table given in the Registry Forensics explanation is going to be your friend.</p>


<p><em>Answer the questions below</em></p>

<p>2.1. <em>What application was installed on the <code>dispatch-srv01</code> before the abnormal activity started?</em> Hint: Hive: Software. Key: This key stores information on the installed programs. Refresh your memory with the Registry Keys table in the task. Navigate to: HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall<br>
<code>DroneManager Updater</code></p>

<br>
<p align="center"><strong>dispatch-svr01</strong>´s activity detected between <strong>2025-10-20</strong> 10:29:12 and <strong>2025-10-21</strong> 20:55:18.<br><br>
<img width="1200px" src="https://github.com/user-attachments/assets/ca275efd-3301-49ac-802c-46d0c82ba95f"><br>
<img width="1200px" src="https://github.com/user-attachments/assets/b5b9192e-885d-41d6-9c90-b4704da81233"><br>Rosana´s hands-on</p>

<br>
<p align="center"><strong>DroneManager Updater</strong> installation was performed on <strong>2025-10-21</strong> 20:52:37 and uninstallation on <strong>2025-10-21</strong> 20:52:37.<br><br>
<img width="1200px" src="https://github.com/user-attachments/assets/75ec0bb7-e493-43c3-aeb6-decdc2cc1668"><br>Rosana´s hands-on</p>

<br>
<p>2.2. <em>What is the full path where the user launched the application (found in question 1) from?</em> Hint: Hive: NTUSER.DAT. Key: This key stores information on recently accessed applications launched via the GUI. Refresh your memory with the Registry Keys table in the task. Navigate to either: HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist or ROOT\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Store<br>
<code>C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/aa7aa503-98ce-49a9-a3d6-bddc17c202a3"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/193da9ac-6eb6-4542-bb63-0f4b78c8463b"><br>Rosana´s hands-on</h6>

<br>
<p>2.3. <em>Which value was added by the application to maintain persistence on startup?</em> Hint: Hive: SOFTWARE. Key: This key stores information on the programs that are set to automatically start when the users logs in. Navigate to: ROOT\Microsoft\Windows\CurrentVersion\Run<br>
<code>"C:\Program Files\DroneManager\dronehelper.exe" --background</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/a87f884a-b9d4-437c-b350-b2d8013f6e00"><br>Rosana´s hands-on</h6>

<br>
<p>2.4. <em>If you enjoyed today's room, feel free to check out the <a href="https://tryhackme.com/room/expregistryforensics">Expediting Registry Analysis</a> room.</em><br>
<code>No answer needed</code></p>

<h6 align="center"><a href="https://github.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/blob/CTFs-%26-Infos/Medium%20%F0%9F%94%97%20-%20Expediting%20Registry%20Analysis.md">Expediting Registry Analysis</a><br> 2024, December 17<br><br><img width="1200px" src="https://github.com/user-attachments/assets/b1bb0461-c1d0-423c-a29d-a309df98060d"><br>Rosana´s hands-on</h6>

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/78610f76-f7eb-48f3-bb17-21ada2b7d467"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/43c77567-85e4-48bc-8c90-32253a97cd08"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/53d11371-5c83-4227-92e9-888ba2ff2bc3"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|20      |Medium 🔗 - Forensics - Registry Furensics       |4 |     100ᵗʰ  |     3ʳᵈ    |   20,497ᵗʰ   |      239ᵗʰ     |    134,832  |    1,042    |    84     |
|20      |Medium 🔗 - Web Attack Forensics - Drone Alone   |4 |     100ᵗʰ  |     3ʳᵈ    |   21,935ᵗʰ   |      243ʳᵈ     |    134,808  |    1,041    |    84     |
|20      |Easy 🔗 - XSS - Merry XSSMas                     |4 |     100ᵗʰ  |     3ʳᵈ    |   23,069ᵗʰ   |      256ᵗʰ     |    134,792  |    1,040    |    84     |
|20      |Easy 🔗 -  Race Conditions - Toy to The World    |4 |     100ᵗʰ  |     3ʳᵈ    |   24,717ᵗʰ   |      275ᵗʰ     |    134,768  |    1,039    |    84     |
|20      |Medium 🔗 -  SOC Alert Triaging - Tinsel Triage  |4 |     100ᵗʰ  |     3ʳᵈ    |   25,202ⁿᵈ   |      286ᵗʰ     |    134,752  |    1,038    |    84     |
|19      |Medium 🔗 -  ICS/Modbus - Claus for Concern      |3 |     101ˢᵗ  |     3ʳᵈ    |   28,869ᵗʰ   |      337ᵗʰ     |    134,658  |    1,037    |    84     |
|19      |Easy 🔗 -  Passwords - A Cracking Christmas      |3 |     101ˢᵗ  |     3ʳᵈ    |   29,583ʳᵈ   |      340ᵗʰ     |    134,642  |    1,036    |    84     |
|18      |Easy 🔗 -  Prompt Injection - Sched-yule conflict|2 |     101ˢᵗ  |     3ʳᵈ    |   30,518ᵗʰ   |      353ʳᵈ     |    134,626  |    1,035    |    84     |
|18      |Medium 🔗 -  Obfuscation - The Egg Shell File    |2 |     101ˢᵗ  |     3ʳᵈ    |   30,967ᵗʰ   |      358ᵗʰ     |    134,618  |    1,034    |    84     |
|17      |Medium 🔗 - CyberChef - Hoperation Save McSkidy  |1 |     101ˢᵗ  |     3ʳᵈ    |   32,378ᵗʰ   |      374ᵗʰ     |    134,602  |    1,033    |    84     |
|7       |Medium 🔗 - Malware Analysis - Egg-xecutable     |2 |      95ᵗʰ  |     3ʳᵈ    |   11,604ᵗʰ   |      145ᵗʰ     |    134,544  |    1,034    |    84     |
|7       |Easy 🔗 - Network Discovery - Scan-ta Clause     |2 |      95ᵗʰ  |     3ʳᵈ    |   18,575ᵗʰ   |      208ᵗʰ     |    134,522  |    1,033    |    84     |
|7       |Easy 🔗 - React2Shell: CVE-2025-55182            |2 |      95ᵗʰ  |     3ʳᵈ    |   28,593ʳᵈ   |      326ᵗʰ     |    134,474  |    1,032    |    81     |
|6       |Medium 🔗 - IDOR - Santa´s Little IDOR           |1 |      95ᵗʰ  |     3ʳᵈ    |   27,309ᵗʰ   |      328ᵗʰ     |    134,450  |    1,031    |    81     |
|6       |Easy 🔗 - AI in Security - old sAInt nick        |1 |      95ᵗʰ  |     3ʳᵈ    |   41,626ᵗʰ   |      526ᵗʰ     |    134,426  |    1,030    |    81     |
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?        |1 |      95ᵗʰ  |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas              |1 |      96ᵗʰ  |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells               |1 |      97ᵗʰ  |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>

<p align="center">Global All Time:    100ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/b95d34bd-4d39-44b2-b0ca-0a90d395f613"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/a0a2d6c7-6a26-428f-9561-8318e6cf97d1"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/4be15818-af75-4c9a-bae5-e2a711335742"><br><br>
                  Global monthly:  20,497ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f262ca3c-f0cd-42b5-bfd2-7fb0caa7baae"><br><br>
                  Brazil monthly:     239ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/82f14ae2-b1c0-483c-bd8d-4cd64d22cee1"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>


