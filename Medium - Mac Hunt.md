<h1 align="center">DFIR, Digital Forensics and Incident Response<br>macOS Forensics<br><img width="660px" src="https://github.com/user-attachments/assets/5e7f8c2d-53bf-43b7-81af-08b943f5b2b0"><br>Mac Hunt</h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/a2c9e9c5-8d86-4447-8d3b-0a395b457c20"><br>
June 14, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>404</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
Utilize your macOS investigation skills to reveal the mystery behind a compromise. Access it <a href="https://tryhackme.com/room/machunt"</a>here.<br>
<img width="1200px" src=""></p>

<h2> Task 1 . Job Phish</h2>


<h3 align="left"> Answer the question below</h3>

> 1.1. <em>What is the name of the most recently accessed folder by the user?</em><br><a id='1.1'></a>
>> <strong><code>Download</code></strong><br>
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
>> <strong><code>Download</code></strong><br>
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


