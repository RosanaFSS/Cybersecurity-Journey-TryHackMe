<h1 align="center">DFIR, Digital Forensics and Incident Response<br>macOS Forensics<br><img width="660px" src="https://github.com/user-attachments/assets/5e7f8c2d-53bf-43b7-81af-08b943f5b2b0"><br>macOS Forensics: Applications</h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/a2c9e9c5-8d86-4447-8d3b-0a395b457c20"><br>
June 11, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>401</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
Learn about macOS forensic artefacts related to different applications. Access it <a href="https://tryhackme.com/room/macosforensicsapplications"</a>here.<br>
<img width="1200px" src=""></p>

<h2> Task 1 . Introduction</h2>

<p>In modern operating systems, users use applications to perform different activities. Therefore, when performing forensics, it is imperative to learn about the forensic artefacts created using various applications to fully understand user activity. In this room, we will learn about the forensic artefacts related to applications in macOS.</p>

<h3>Learning Objectives</h3>
<p>
- Leverage application data to perform forensic analysis on a Mac device.<br>
- Explore persistence mechanisms in macOS.<br>
- Identify user activity in built-in apps such as mail, calendar, phone, and messages.<br>

</p>

<h3>Prerequisites</h3>

<p>Before starting this room, it is highly recommended that you complete:<br>

- macOS Forensics: The Basics<br>
- macOS Forensics: Artefacts<br>

Please note that, similar to the previous room, this room requires advanced knowledge of the Linux command line and an understanding of the tools and techniques used in the earlier rooms.</p>

<h3>Machine Access</h3>
<p>Before moving forward, please press the Start Machine button below to start the attached VM.<br>
[ Start Machine ]<br>
The machine will open in split view. The attached machine is a Linux machine with a macOS disk image named mac-disk.img. The image is placed in the home directory. As we learned previously, we will mount this disk image using the apfs-fuse utility and perform analysis on the image.<br>

In the coming tasks, we will demonstrate the artefacts on a live Mac machine and practice analysing them on the disk image in the attached Linux VM. Instructions will be provided on accessing the artefacts in the Linux VM if they differ from those in a live machine.</p>


<h3 align="left"> Answer the question below</h3>

> 1.1. <em>Let's see what application artefacts are present in macOS!</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<p>macOS disk image named <code>mac-disk.img</code></p>

![image](https://github.com/user-attachments/assets/b6c07b96-e740-4d05-886f-fdaa24942193)


<br>

<h2> Task 2 . Common Application Information</h2>
<h3>Package Containers</h3>
<p>Like the Program Files directory in Windows, most macOS applications are installed in the /Applications directory. If we navigate this directory, we can see the installed applications in macOS as .app files.</p>

<p>Applications Directory</p>

```bash
umair@Umairs-MacBook-Pro /Applications % pwd
/Applications
umair@Umairs-MacBook-Pro /Applications % ls
Adobe Acrobat Reader.app
AnyDesk.app
Arc.app
Arduino IDE.app
Asana.app	
Blackmagic Disk Speed Test.app
CapCut.app
DB Browser for SQLite.app
Developer.app	
Discord.app	
Docker.app
```

<p>Each .app file is a directory, and we can navigate into this directory to view its contents. In the Finder app, we can do this by clicking Show Package Contents from the right-click menu. We can then navigate the files in the package.</p>

![image](https://github.com/user-attachments/assets/73d357b5-3e9d-4ba2-8086-0b79994d3864)

<p>Similarly, we can see in the terminal that these files are marked as directories, as seen below. </p>

<p>Application Packages in Terminal</p>

```bash
umair@Umairs-MacBook-Pro /Applications % ls -l
total 0
drwxrwxr-x   3 root   wheel   96 Oct  5  2024 Adobe Acrobat Reader.app
drwxr-xr-x@  3 umair  admin   96 Oct 30 18:20 AnyDesk.app
drwxr-xr-x@  4 umair  admin  128 Apr 12 05:07 Arc.app
drwxr-xr-x@  3 umair  staff   96 Sep 25  2024 Arduino IDE.app
drwxr-xr-x@  3 umair  staff   96 Dec 16 21:26 Asana.app
drwxr-xr-x@  3 root   wheel   96 Oct 11  2024 Blackmagic Disk Speed Test.app
.
.
.
```

<p>We see a Contents directory when we navigate inside the .app directory for any application. This directory contains all the information and resources the application requires to function properly.</p>

<p>Contents of .app Files</p>

```bash
umair@Umairs-MacBook-Pro /Applications % ls -l
total 0
drwxrwxr-x   3 root   wheel   96 Oct  5  2024 Adobe Acrobat Reader.app
drwxr-xr-x@  3 umair  admin   96 Oct 30 18:20 AnyDesk.app
drwxr-xr-x@  4 umair  admin  128 Apr 12 05:07 Arc.app
drwxr-xr-x@  3 umair  staff   96 Sep 25  2024 Arduino IDE.app
drwxr-xr-x@  3 umair  staff   96 Dec 16 21:26 Asana.app
drwxr-xr-x@  3 root   wheel   96 Oct 11  2024 Blackmagic Disk Speed Test.app
.
.
.
```

<p>On a high level, every app contains the following parts to function properly.</p>

![image](https://github.com/user-attachments/assets/cc40a735-46ae-4be5-aa46-7b51a765fcf2)


<h3>Application Install History</h3>
<p>A plist file located at <code></code>/Library/Receipts/InstallHistory.plist</p>code> contains valuable information about application installation. Information about each application is enclosed in a <code><dict></code> tag. It includes the date of application installation, display name, display version, package identifier, and the application/process used to install the application. Possible process names could be one of the following:</p>

![image](https://github.com/user-attachments/assets/c69bbf6a-510c-4319-939d-26f3b27df2ba)

<p>The following terminal shows a sample <code>InstallHistory.plist</code> file.</p>

<p>InstallHistory.plist</p>

```bash
umair@Umairs-MacBook-Pro Receipts % cat InstallHistory.plist 
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
 <dict>
 <key>date</key>
 <date>2024-04-17T01:25:11Z</date>
 <key>displayName</key>
 <string>macOS 14.4</string>
 <key>displayVersion</key>
 <string>14.4</string>
 <key>processName</key>
 <string>softwareupdated</string>
 </dict>
 <dict>
 <key>date</key>
 <date>2024-04-17T01:27:14Z</date>
 <key>displayName</key>
 <string>Setup macOS Recovery Dependencies</string>
 <key>displayVersion</key>
 <string></string>
 <key>packageIdentifiers</key>
 <array>
 <string>com.apple.cdm.pkg.SetupMacOSRecoveryDependencies</string>
 </array>
 <key>processName</key>
 <string>installer</string>
 </dict>
 <dict>
 <key>date</key>
 <date>2024-07-25T02:38:09Z</date>
 <key>displayName</key>
 <string>‎WhatsApp</string>
 <key>displayVersion</key>
 <string>24.14.85</string>
 <key>packageIdentifiers</key>
 <array>
 <string>net.whatsapp.WhatsApp</string>
 </array>
 <key>processName</key>
 <string>appstoreagent</string>
 </dict>
```

<p>Further information about the installer process is available in the location /private/var/db/receipts/<app-name>.plist. This file also contains the install date, package version, and install prefix path. In the same directory, there is a <app-name>.bom file as well, which contains more details about the application install. This file can be opened using the lsbom utility, which is available in macOS by default but has also been installed in the attached VM.</p>

<p>Install Log Details</p>

```bash
umair@Umairs-MacBook-Pro receipts % plutil -p com.microsoft.package.Microsoft_Outlook.app.plist 
{
  "InstallDate" => 2025-04-23 08:34:21 +0000
  "InstallPrefixPath" => "Library/Caches/com.microsoft.autoupdate.helper/Clones.noindex"
  "InstallProcessName" => "installer"
  "PackageFileName" => "Microsoft_Outlook.pkg"
  "PackageIdentifier" => "com.microsoft.package.Microsoft_Outlook.app"
  "PackageVersion" => "16.96.25042021"
}
```

<p>Finally, we can also find information about installation details in the <code>/private/var/log/install.log</code> file. We can search for Installed in this log file to get the installation date and version information for installed applications.</p>

<p>Install Log</p>

```bash
umair@Umairs-MacBook-Pro ~ % cat /var/log/install.log|grep Installed
2024-04-16 18:27:14-07 MacBook-Pro installd[547]: Installed "Setup macOS Recovery Dependencies" ()
2024-04-16 18:27:28-07 MacBook-Pro system_installd[557]: Installed "MAContent10_AssetPack_0048_AlchemyPadsDigitalHolyGhost" (2.0.0.0)
2024-04-16 18:27:30-07 MacBook-Pro system_installd[557]: Installed "MAContent10_AssetPack_0310_UB_DrumMachineDesignerGB" (2.0.0.0)
2024-04-16 18:27:32-07 MacBook-Pro system_installd[557]: Installed "MAContent10_AssetPack_0312_UB_UltrabeatKitsGBLogic" (2.0.0.0)
.
.
.
2025-04-05 12:20:19+04 Umairs-MacBook-Pro system_installd[879]: Installed "Command Line Tools for Xcode" (16.3)
	    "__installState" = Installed;
2025-04-06 13:39:42+04 Umairs-MacBook-Pro installd[1790]: Installed "‎WhatsApp" (25.9.72)
2025-04-06 17:25:22+04 Umairs-MacBook-Pro installd[1790]: Installed "Microsoft OneDrive" ()
2025-04-07 18:43:40+04 Umairs-MacBook-Pro installd[1790]: Installed "Microsoft Teams" (25072.1704.3539.4369)
2025-04-08 23:54:13+04 Umairs-MacBook-Pro system_installd[879]: Installed "XProtectPlistConfigData" (5293)
2025-04-12 05:08:33+04 Umairs-MacBook-Pro installd[59531]: Installed "‎WhatsApp" (25.10.72)
2025-04-13 12:10:33+04 Umairs-MacBook-Pro installd[98329]: Installed "Microsoft OneDrive" ()
2025-04-15 20:51:03+04 Umairs-MacBook-Pro installd[98329]: Installed "Microsoft Excel" ()
2025-04-15 20:51:43+04 Umairs-MacBook-Pro installd[98329]: Installed "Microsoft Outlook" ()
```

<p>Now let's practice extracting these artefacts from the disk image in the attached VM.</p>

<h3 align="left"> Answer the questions below</h3>

> 2.1. <em>When was Microsoft 365 and Office installed on the disk image in the attached VM? Format in GMT YYYY-MM-DD hh:mm:ss</em><br><a id='2.1'></a>
>> <strong><code>2025-04-26 06:41:43</code></strong><br>
<p></p>

```bash
ubuntu@tryhackme:~$ sudo su
root@tryhackme:/home/ubuntu# apfs-fuse -v 4 mac-disk.img mac
...
root@tryhackme:/home/ubuntu/mac/root/Library/Receipts# ls
InstallHistory.plist  db
root@tryhackme:/home/ubuntu/mac/root/Library/Receipts# cat InstallHistory.plist
...
root@tryhackme:/home/ubuntu/mac/root/Library/Receipts# plistutil -p InstallHistory.plist
...
{
    "date": 2025-04-26 06:41:43 +0000,
    "displayName": "Microsoft 365 and Office for Mac",
    "displayVersion": "",
    "packageIdentifiers": [
      "com.microsoft.package.Microsoft_Word.app",
      "com.microsoft.package.Microsoft_Outlook.app",
      "com.microsoft.package.Microsoft_AutoUpdate.app",
      "com.microsoft.pkg.licensing",
      "com.microsoft.package.DFonts",
      "com.microsoft.package.Frameworks",
      "com.microsoft.package.Proofing_Tools"
    ],
    "processName": "Installer"
  }
]
root@tryhackme:/home/ubuntu/mac/root/Library/Receipts# 
```

![image](https://github.com/user-attachments/assets/986ebc8b-4e54-4b0a-9aa0-c8cb95ae6469)


<br>

> 2.2. <em>What is the name of the package used to install Microsoft Word?</em><br><a id='2.1'></a>
>> <strong><code>Microsoft_Word_Internal.pkg</code></strong><br>
<p></p>

<br>

```bash
root@tryhackme:/home/ubuntu/mac/root# plistutil -p private/var/db/receipts/com.microsoft.package.Microsoft_Word.app.plist
{
  "PackageVersion": "16.96.25041326",
  "PackageIdentifier": "com.microsoft.package.Microsoft_Word.app",
  "InstallPrefixPath": "Applications",
  "InstallDate": 2025-04-26 06:41:42 +0000,
  "PackageFileName": "Microsoft_Word_Internal.pkg",
  "InstallProcessName": "Installer"
}
```

![image](https://github.com/user-attachments/assets/f3a472f2-e988-4ff8-ba7a-637ce0245b74)


<br>

<h2> Task 3 . Autostart Items</h2>
<p>We might have observed that applications can be configured to start at login in macOS. When applications restart, they often start from the same context from which they were shut down.</p>

<h3>Launch Agents and Daemons</h3>
<p>There are often background (or foreground) applications running in the OS that start with every reboot or login event, similar to applications in the autorun registry keys or Services in Windows. In macOS, these are called LaunchAgents or LaunchDaemons. LaunchAgents are user applications that execute at login, and LaunchDaemons are system applications that run with elevated privileges. LaunchAgents and LaunchDaemons are present in the /System/Library, /Library and ~/Library directories, e.g. ~/Library/LaunchAgents/net.tunnelblick.tunnelblick.LaunchAtLogin.plist as shown in the terminal below. </p>

<p>LaunchAgent Plist File</p>

```bash
umair@Umairs-MacBook-Pro LaunchAgents % pwd   
/Users/umair/Library/LaunchAgents
umair@Umairs-MacBook-Pro LaunchAgents % plutil -p net.tunnelblick.tunnelblick.LaunchAtLogin.plist 
{
  "ExitTimeOut" => 0
  "Label" => "net.tunnelblick.tunnelblick.LaunchAtLogin"
  "LimitLoadToSessionType" => "Aqua"
  "ProcessType" => "Interactive"
  "ProgramArguments" => [
    0 => "/Applications/Tunnelblick.app/Contents/Resources/Tunnelblick-LaunchAtLogin"
  ]
  "RunAtLoad" => 1
}
```

<p>We can see some critical information in this plist file that can be helpful. We can see that the ProcessType has a value of Interactive, meaning this is a process with a GUI. The ProgramArguments key contains the executable path that will execute when logged in. We can also see that the RunAtLoad key has a value of 1, indicating that this application is supposed to run at login. Please note that this information can be different for different types of files, as seen in the example below.</p>


<p>Launch Agents and Daemons</p>

```bash
umair@Umairs-MacBook-Pro LaunchAgents % pwd   
/Library/LaunchAgents
umair@Umairs-MacBook-Pro LaunchAgents % plutil -p com.microsoft.OneDriveStandaloneUpdater.plist 
{
  "Label" => "com.microsoft.OneDriveStandaloneUpdater"
  "Program" => "/Applications/OneDrive.app/Contents/StandaloneUpdater.app/Contents/MacOS/OneDriveStandaloneUpdater"
  "ProgramArguments" => [
  ]
  "RunAtLoad" => 1
  "StartInterval" => 86400
}
umair@Umairs-MacBook-Pro LaunchAgents % cd ..
umair@Umairs-MacBook-Pro /Library % cd LaunchDaemons 
umair@Umairs-MacBook-Pro LaunchDaemons % plutil -p org.filezilla-project.filezilla-server.service.plist 
{
  "AssociatedBundleIdentifiers" => [
    0 => "org.filezilla-project.filezilla-server"
  ]
  "Disabled" => 0
  "EnvironmentVariables" => {
    "LC_CTYPE" => "en_US.UTF-8"
  }
  "GroupName" => "wheel"
  "Label" => "org.filezilla-project.filezilla-server.service"
  "ProgramArguments" => [
    0 => "/Applications/FileZilla Server.app/Contents/MacOS/filezilla-server"
    1 => "--config-dir=/Library/Preferences/org.filezilla-project.filezilla-server.service"
  ]
  "RunAtLoad" => 1
  "UserName" => "root"
}
umair@Umairs-MacBook-Pro LaunchDaemons % cd /System/Library/LaunchAgents
umair@Umairs-MacBook-Pro LaunchAgents % plutil -p com.apple.wallpaper.plist  
{
  "KeepAlive" => {
    "AfterInitialDemand" => 1
    "SuccessfulExit" => 0
  }
  "Label" => "com.apple.wallpaper.agent"
  "LimitLoadToSessionType" => [
    0 => "Aqua"
  ]
  "MachServices" => {
    "com.apple.usernotifications.delegate.com.apple.wallpaper.notifications.sonoma-first-run" => 1
    "com.apple.wallpaper" => 1
    "com.apple.wallpaper.CacheDelete" => 1
  }
  "POSIXSpawnType" => "App"
  "Program" => "/System/Library/CoreServices/WallpaperAgent.app/Contents/MacOS/WallpaperAgent"
  "RunAtLoad" => 0
  "ThrottleInterval" => 1
}
```

<p>Here, we explore three different plist files and observe that they often contain different information depending on the type of plist file and the program. <br><br>

Since macOS is based on Unix, it also supports cron jobs. However, most persistence mechanisms in macOS use LaunchAgents and LaunchDaemons, and cron jobs are rarely used.</p>

<h3>Saved Application State</h3>
<p>When a system reboots or a user logs in, the applications that are executed often execute in the same state as they were before the reboot. These saved states can be set when the user selects to reopen windows when logging in during a reboot or shutdown event. Therefore, we can consider the existence of these artefacts as evidence that the user used these applications at some point. <br><br>

This information about the state of applications is saved in macOS in the directory ~/Library/Saved Application State/<application>.savedState for legacy applications, and ~/Library/Containers/<application>/Data/Library/Application Support/<application>/Saved Application State/<application>.savedState for sandboxed macOS applications. </p>

<p>Saved Application States</p>

```bash
Saved Application States
umair@Umairs-MacBook-Pro ~ % cd Library/Saved\ Application\ State 
umair@Umairs-MacBook-Pro Saved Application State % ls
cc.arduino.Arduino.savedState
cc.arduino.IDE2.savedState
com.Autodesk.eagle.savedState
com.amazon.aiv.AIVApp.savedState
org.filezilla-project.filezilla.savedState
com.apple.Maps.savedState				
com.electron.ollama.savedState				
org.raspberrypi.imagingutility.savedState
com.apple.Notes.savedState
com.apple.iCal.savedState
```

<h3 align="left">Answer the question below</h3>

> 3.1. <em>What arguments does the Microsoft update agent launch with? Format "Argument 1", "Argument 2"</em><br><a id='3.1'></a>
>> <strong><code>"/Library/Application Support/Microsoft/MAU2.0/Microsoft AutoUpdate.app/Contents/MacOS/Microsoft Update Assistant.app/Contents/MacOS/Microsoft Update Assistant", "--launchByAgent"</code></strong><br>
<p></p>

```bash
root@tryhackme:/home/ubuntu/mac/root/Library/LaunchAgents# plistutil -p com.microsoft.update.agent.plist
{
  "ProgramArguments": [
    "/Library/Application Support/Microsoft/MAU2.0/Microsoft AutoUpdate.app/Contents/MacOS/Microsoft Update Assistant.app/Contents/MacOS/Microsoft Update Assistant",
    "--launchByAgent"
  ],
  "StartInterval": 7200,
  "Label": "com.microsoft.update.agent",
  "Disabled": false,
  "RunAtLoad": true,
  "MachServices": {
    "com.microsoft.update.xpc": true
  }
}
```

![image](https://github.com/user-attachments/assets/ea9ec25d-5005-477f-bfd6-0e7bd42cfa1d)


<br>

<h2> Task 4 . Notifications and Permissions</h2>

<p>[ ... ]</p>


<h3 align="left"> Answer the question below</h3>

> 4.1. <em>Which application has Full Disk Access permissions?</em><br><a id='2.1'></a>
>> <strong><code>com.apple.Terminal</code></strong><br>
<p></p>



```bash
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm# ls
Desktop  Documents  Downloads  Library  Movies  Music  Pictures  Public
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm# ls Library/Group\ Containers/group.com.apple.usernoted/db2/db
'Library/Group Containers/group.com.apple.usernoted/db2/db'
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm#
```

```bash
...
ubuntu@tryhackme:~$ mkdir sql
...
ubuntu@tryhackme:~/sql$ mkdir notifications
ubuntu@tryhackme:~/sql$
```


```bash
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm# cp Library/Group\ Containers/group.com.apple.usernoted/db2/db* /home/ubuntu/sql/notifications/
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm# 
```

![image](https://github.com/user-attachments/assets/27e7f9b4-d669-4448-b78b-07cf8b693e96)

![image](https://github.com/user-attachments/assets/bab244d4-b2cd-4c6f-98d8-bc882d2f5e8f)


```bash
ubuntu@tryhackme:~$ cd ~/APOLLO
ubuntu@tryhackme:~/APOLLO$ ubuntu@tryhackme:~/APOLLO$ ls
LICENSE  README.md  apollo.py  modules
ubuntu@tryhackme:~/APOLLO$ cd modules
ubuntu@tryhackme:~/APOLLO/modules$ ls
...
netusage_zprocess.txt
notifications_db.txt
passes23_unique_passes_cards.txt
...
ubuntu@tryhackme:~/APOLLO/modules$ cat notifications_db.txt
# --------------------------------------------------------------------------------
#       Copyright (c) 2018-2020 Sarah Edwards (Station X Labs, LLC, 
#       @iamevltwin, mac4n6.com). All rights reserved.
...
[Module Metadata]
AUTHOR=Sarah Edwards/mac4n6.com/@iamevltwin
MODULE_NOTES=App Notifications (Under /db2/)

[Database Metadata]
DATABASE=db
PLATFORM=MACOS
VERSIONS=10.13,10.14,10.15,10.16

[Query Metadata]
QUERY_NAME=notifications
ACTIVITY=Notification
KEY_TIMESTAMP=DATE DELIVERED

[SQL Query 10.14,10.15,10.16]
QUERY=
	SELECT 
		DATETIME(RECORD.DELIVERED_DATE+978307200,'UNIXEPOCH') AS 'DATE DELIVERED',
		APP.IDENTIFIER AS 'BUNDLE ID',
		APP.BADGE AS 'APP BADGE',
		RECORD.PRESENTED AS 'PRESENTED',
		RECORD.STYLE AS 'STYLE',
		RECORD.SNOOZE_FIRE_DATE AS 'SNOOZE FIRE DATE',
		HEX(RECORD.DATA) AS 'NOTIFICATION DATA (HEX)',
		HEX(CATEGORIES.CATEGORIES) AS 'CATEGORIES (HEX)',
		RECORD.REQUEST_DATE AS 'REQUEST DATE',
		RECORD.REQUEST_LAST_DATE AS 'REQUEST LAST DATE',
		HEX(RECORD.UUID) AS 'UUID (HEX)',
		RECORD.REC_ID AS "RECORD TABLE ID"
	FROM RECORD
	LEFT JOIN APP ON APP.APP_ID == RECORD.APP_ID
	LEFT JOIN CATEGORIES ON CATEGORIES.APP_ID == RECORD.APP_ID

[SQL Query 10.13]
QUERY=
	SELECT 
		DATETIME(RECORD.DELIVERED_DATE+978307200,'UNIXEPOCH') AS 'DATE DELIVERED',
		APP.IDENTIFIER AS 'BUNDLE ID',
		RECORD.PRESENTED AS 'PRESENTED',
		RECORD.STYLE AS 'STYLE',
		RECORD.SNOOZE_FIRE_DATE AS 'SNOOZE FIRE DATE',
		HEX(RECORD.DATA) AS 'NOTIFICATION DATA (HEX)',
		RECORD.REQUEST_DATE AS 'REQUEST DATE',
		RECORD.REQUEST_LAST_DATE AS 'REQUEST LAST DATE',
		HEX(RECORD.UUID) AS 'UUID (HEX)',
		RECORD.REC_ID AS "RECORD TABLE ID"
	FROM RECORD
ubuntu@tryhackme:~/APOLLO/modules$ 
```

![image](https://github.com/user-attachments/assets/a32a5141-c667-48ac-984f-68d8e0edcc9c)

![image](https://github.com/user-attachments/assets/ebda6cce-aa89-4fb2-836d-a54625ced339)

![image](https://github.com/user-attachments/assets/54a2a1f7-dc2a-4dd7-939e-a1d73b49221e)


```bash
root@tryhackme:/home/ubuntu/mac/root/Library/Application Support/com.apple.TCC# cp /home/ubuntu/mac/root/Library/'Application Support'/com.apple.TCC/* /home/ubuntu/sql/
root@tryhackme:/home/ubuntu/mac/root/Library/Application Support/com.apple.TCC# 
```

![image](https://github.com/user-attachments/assets/f4d4db64-bd48-4cf0-bedf-554a145c78ce)

![image](https://github.com/user-attachments/assets/fc03f1b5-ff31-4afc-b92e-7e363a7b959b)

![image](https://github.com/user-attachments/assets/eb295206-903d-40ec-bbc2-8c9d5937573b)


```bash
SELECT 
		DATETIME(LAST_MODIFIED,'UNIXEPOCH') AS "LAST MODIFIED",
		SERVICE AS 'SERVICE',
		CLIENT AS 'CLIENT',
		CASE AUTH_VALUE 
			WHEN 0 THEN 'NOT ALLOWED'
			WHEN 2 THEN 'ALLOWED'
		END AS 'ALLOWED',
		AUTH_REASON AS 'AUTH REASON',
		CLIENT_TYPE AS 'CLIENT TYPE',
		INDIRECT_OBJECT_IDENTIFIER AS 'INDIRECT OBJECT IDENTIFIER'
	FROM ACCESS
```

![image](https://github.com/user-attachments/assets/17a084c6-0d7f-409b-97ed-6da9fe02f492)


<br>

<h2> Task 5 . Contacts, Calls, and Messages</h2>

<p>[ ... ]</p>


<h3 align="left"> Answer the questions below</h3>

> 5.1. <em>What is the email address of the user using this machine?</em><br><a id='5.1'></a>
>> <strong><code>______</code></strong><br>
<p></p>


```bash
root@tryhackme:/home/ubuntu/mac/root/private/var/db/CoreDuet/People# ls
Feedback  interactionC.db  interactionC.db-shm  interactionC.db-wal
root@tryhackme:/home/ubuntu/mac/root/private/var/db/CoreDuet/People# cp interactionC.db /home/ubuntu/sql
root@tryhackme:/home/ubuntu/mac/root/private/var/db/CoreDuet/People# 
```

<br>

![image](https://github.com/user-attachments/assets/80c419af-7a77-41d5-a6c5-d44356e71ca0)

```bash
root@tryhackme:/home/ubuntu/mac/root/private/var/db/CoreDuet/People# ls
Feedback  interactionC.db  interactionC.db-shm  interactionC.db-wal
root@tryhackme:/home/ubuntu/mac/root/private/var/db/CoreDuet/People# cp interactionC.db /home/ubuntu/sql
root@tryhackme:/home/ubuntu/mac/root/private/var/db/CoreDuet/People# 
```


> 5.2. <em>A call was made using FaceTime on 2025-04-26 05:40:04. Was this call answered? Y/N</em><br><a id='5.2'></a>
>> <strong><code>______</code></strong><br>
<p></p>

<br>

> 5.3. <em>The user received a message on 2025-04-26 05:38:20. This message contained an image as an attachment. What animal is present in that image?</em><br><a id='5.3'></a>
>> <strong><code>______</code></strong><br>
<p></p>


<br>

> 5.4. <em>On what date and time was the previous message read? Format YYYY-MM-DD hh:mm:ss</em><br><a id='5.3'></a>
>> <strong><code>______</code></strong><br>
<p></p>
