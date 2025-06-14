<h1 align="center">DFIR, Digital Forensics and Incident Response<br>macOS Forensics<br><img width="660px" src="https://github.com/user-attachments/assets/5e7f8c2d-53bf-43b7-81af-08b943f5b2b0"><br>macOS Forensics: Applications</h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/a2c9e9c5-8d86-4447-8d3b-0a395b457c20"><br>
June 14, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>404</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
Learn about macOS forensic artefacts related to different applications. Access it <a href="https://tryhackme.com/room/macosforensicsapplications"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/c05c5979-05d8-4644-9a2f-8d9025672fbe"></p>

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


<p>Volume 4</p>

```bash
ubuntu@tryhackme:~$ apfsutil mac-disk.img
Found partitions:
69646961-6700-11AA-11AA-00306543ECAC B4782C91-2F42-4887-9AAB-F1D600786E1F 0000000000000028 00000000000FA027 0000000000000000 iBootSystemContainer
7C3457EF-0000-11AA-11AA-00306543ECAC 2F091A53-8341-4774-D38F-9EF3A47DF781 00000000000FA028 0000000005000027 0000000000000000 Container
52637672-7900-11AA-11AA-00306543ECAC 8B484BA1-3C0A-4EFF-F5BA-FB27DA5681E2 0000000005000028 00000000059FFFD7 0000000000000000 RecoveryOSContainer
First APFS partition is 1

Volume 0 4A63C141-38C0-42DD-B1EB-7DAC6CD3AAD6
---------------------------------------------
Role:               System
Name:               Macintosh HD (Case-insensitive)
Capacity Consumed:  11244146688 Bytes
FileVault:          No
Snapshots:
    35 : 'com.apple.os.update-83920663FCCF8FEE21340F708B980423F7822AE195EAD15998C70BD0F7B8AF23'

Volume 1 7FE047CD-AF2F-4E4B-A96A-39A3E4A3ED52
---------------------------------------------
Role:               Preboot
Name:               Preboot (Case-insensitive)
Capacity Consumed:  6065201152 Bytes
FileVault:          No
Snapshots:

Volume 2 7E8AC68F-1100-438C-A154-2F1AB49F2C12
---------------------------------------------
Role:               Recovery
Name:               Recovery (Case-insensitive)
Capacity Consumed:  1003020288 Bytes
FileVault:          No
Snapshots:

Volume 3 66A495E5-2A2F-45DF-9A4B-8E8E7746464B
---------------------------------------------
Role:               Update
Name:               Update (Case-insensitive)
Capacity Consumed:  233472 Bytes
FileVault:          No
Snapshots:

Volume 4 1975111D-300A-4FDF-9BE1-7ECBA3E3189D
---------------------------------------------
Role:               Data
Name:               Data (Case-insensitive)
Capacity Consumed:  9581592576 Bytes
FileVault:          No
Snapshots:

Volume 5 D604C892-E4F4-481F-B1F0-87B5A40B02D1
---------------------------------------------
Role:               VM
Name:               VM (Case-insensitive)
Capacity Consumed:  20480 Bytes
FileVault:          No
Snapshots:
```


```bash
ubuntu@tryhackme:~$ sudo su
root@tryhackme:/home/ubuntu# apfs-fuse
apfs-fuse [options] <device> <dir>

Options:
-d level      : Enable debug output in the console.
-f device     : Specify secondary device for fusion drives.
-o options    : Additional mount options (see below).
-v volume-id  : Specify number of volume to be mounted.
-r passphrase : Specify volume passphrase. The driver will ask for it if it is
                needed and hasn't been specified here.
-s offset     : Specify offset to the beginning of the container.
-p partition  : Specify partition id containing the container.
-l            : Allow driver to return potentially corrupt data instead of
                failing, if it can't handle something.

Additional mount options (using -o):
uid=N         : Pretend that all files have UID N.
gid=N         : Pretend that all files have GID N.
vol=N         : Same as -v, select volume id to mount.
blksize=N     : Set physical block size. Only needed if a partition table needs
                to be parsed and the sector size is not 512 bytes.
pass=...      : Specify volume passphrase (same as -r).
xid=N         : Mount specific xid.
snap=N        : Mount snapshot with given id. Use apfsutil for getting the ids.

root@tryhackme:/home/ubuntu# 
```

```bash
root@tryhackme:/home/ubuntu# apfs-fuse -v 4 mac-disk.img mac
root@tryhackme:/home/ubuntu# ls
APOLLO   Documents  Music     Public     Videos     bomutils  mac-disk.img  macimg
Desktop  Downloads  Pictures  Templates  apfs-fuse  mac       mac_apt       snap
root@tryhackme:/home/ubuntu# cd mac
root@tryhackme:/home/ubuntu/mac# ls
private-dir  root
...
root@tryhackme:/home/ubuntu/mac_apt# ls
AUTHORS.md   Libraries_For_Windows  extract_apfs_fs.py        mac_apt_mounted_sys_data.py  plugins
CHANGES.txt  Licenses               ios_apt.py                macos_installer              requirements.txt
Dockerfile   README.md              mac_apt.py                other_dependencies           version.py
LICENSE.txt  __pycache__            mac_apt_artifact_only.py  plugin.py
root@tryhackme:/home/ubuntu/mac_apt# 
```


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
>> <strong><code>thmguy535@gmail.com</code></strong><br>
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
root@tryhackme:/home/ubuntu/APOLLO/modules# cat interaction_contact_interactions.txt
root@tryhackme:/home/ubuntu/APOLLO/modules# cat interaction_contact_interactions.txt 
...

[Module Metadata]
AUTHOR=Sarah Edwards/mac4n6.com/@iamevltwin
MODULE_NOTES=Contact Interaction

[Database Metadata]
DATABASE=interactionC.db
PLATFORM=IOS,MACOS
VERSIONS=9,10,11,12,13,10.15,10.16,14

[Query Metadata]
QUERY_NAME=interaction_contact_interactions
ACTIVITY=Contact Interaction
KEY_TIMESTAMP=START DATE

[SQL Query 13,10.15,10.16,14]
QUERY=
   SELECT
      DATETIME(ZINTERACTIONS.ZSTARTDATE + 978307200, 'UNIXEPOCH') AS 'START DATE',
      DATETIME(ZINTERACTIONS.ZENDDATE + 978307200, 'UNIXEPOCH') AS 'END DATE',
      ZINTERACTIONS.ZBUNDLEID AS 'BUNDLE ID',
      ZINTERACTIONS.ZACCOUNT AS 'ACCOUNT',
      ZINTERACTIONS.ZTARGETBUNDLEID AS 'TARGET BUNDLE ID',
      CASE ZINTERACTIONS.ZDIRECTION
         WHEN '0' THEN 'INCOMING'
         WHEN '1' THEN 'OUTGOING'
      END 'DIRECTION',
      ZCONTACTS.ZDISPLAYNAME AS 'SENDER DISPLAY NAME',
      ZCONTACTS.ZIDENTIFIER AS 'SENDER IDENTIFIER',
      ZCONTACTS.ZPERSONID AS 'SENDER PERSONID',
      RECEIPIENTCONACT.ZDISPLAYNAME AS 'RECIPIENT DISPLAY NAME',
      RECEIPIENTCONACT.ZIDENTIFIER AS 'RECIPIENT IDENTIFIER',
      RECEIPIENTCONACT.ZPERSONID AS 'RECIPIENT PERSONID',
      ZINTERACTIONS.ZRECIPIENTCOUNT AS 'RECIPIENT COUNT',  
      ZINTERACTIONS.ZDOMAINIDENTIFIER AS 'DOMAIN IDENTIFIER',   
      ZINTERACTIONS.ZISRESPONSE AS 'IS RESPONSE',
      ZATTACHMENT.ZCONTENTTEXT AS 'CONTEXT TEXT',
      ZATTACHMENT.ZUTI AS 'UTI',
      ZATTACHMENT.ZCONTENTURL AS 'CONTENT URL',
      ZATTACHMENT.ZSIZEINBYTES AS 'SIZE IN BYTES',
      ZATTACHMENT.ZPHOTOLOCALIDENTIFIER AS 'PHOTO LOCAL IDENTIFIER',
      HEX(ZATTACHMENT.ZIDENTIFIER) AS 'ATTACHMENT ID',
      ZATTACHMENT.ZCLOUDIDENTIFIER AS 'CLOUD IDENTIFIER',
      ZCONTACTS.ZINCOMINGRECIPIENTCOUNT AS 'INCOMING RECIPIENT COUNT', 
      ZCONTACTS.ZINCOMINGSENDERCOUNT AS 'INCOMING SENDER COUNT', 
      ZCONTACTS.ZOUTGOINGRECIPIENTCOUNT AS 'OUTGOING RECIPIENT COUNT', 
      DATETIME(ZINTERACTIONS.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ZINTERACTIONS CREATION DATE',
      DATETIME(ZCONTACTS.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ZCONTACTS CREATION DATE',
      DATETIME(ZCONTACTS.ZFIRSTINCOMINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'FIRST INCOMING RECIPIENT DATE',
      DATETIME(ZCONTACTS.ZFIRSTINCOMINGSENDERDATE + 978307200, 'UNIXEPOCH') AS 'FIRST INCOMING SENDER DATE',
      DATETIME(ZCONTACTS.ZFIRSTOUTGOINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'FIRST OUTGOING RECIPIENT DATE',
      DATETIME(ZCONTACTS.ZLASTINCOMINGSENDERDATE + 978307200, 'UNIXEPOCH') AS 'LAST INCOMING SENDER DATE',
      CASE ZCONTACTS.ZLASTINCOMINGRECIPIENTDATE 
         WHEN '0' THEN '0' 
         ELSE DATETIME(ZCONTACTS.ZLASTINCOMINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') 
      END 'LAST INCOMING RECIPIENT DATE', 
      DATETIME(ZCONTACTS.ZLASTOUTGOINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'LAST OUTGOING RECIPIENT DATE', 
      ZCONTACTS.ZCUSTOMIDENTIFIER AS 'CUSTOM IDENTIFIER', 
      ZINTERACTIONS.ZCONTENTURL AS 'CONTENT URL', 
      ZINTERACTIONS.ZLOCATIONUUID AS 'LOCATION UUID', 
      ZINTERACTIONS.ZGROUPNAME AS 'GROUP NAME',
      ZINTERACTIONS.ZDERIVEDINTENTIDENTIFIER AS 'DERIVIED INTENT ID',
      ZINTERACTIONS.Z_PK AS 'ZINTERACTIONS TABLE ID' 
   FROM ZINTERACTIONS 
   LEFT JOIN ZCONTACTS ON ZINTERACTIONS.ZSENDER = ZCONTACTS.Z_PK
   LEFT JOIN Z_1INTERACTIONS ON ZINTERACTIONS.Z_PK == Z_1INTERACTIONS.Z_3INTERACTIONS
   LEFT JOIN ZATTACHMENT ON Z_1INTERACTIONS.Z_1ATTACHMENTS == ZATTACHMENT.Z_PK
   LEFT JOIN Z_2INTERACTIONRECIPIENT ON ZINTERACTIONS.Z_PK== Z_2INTERACTIONRECIPIENT.Z_3INTERACTIONRECIPIENT
   LEFT JOIN ZCONTACTS RECEIPIENTCONACT ON Z_2INTERACTIONRECIPIENT.Z_2RECIPIENTS== RECEIPIENTCONACT.Z_PK 

[SQL Query 12]
QUERY=
   SELECT
      DATETIME(ZINTERACTIONS.ZSTARTDATE + 978307200, 'UNIXEPOCH') AS 'START DATE',
      DATETIME(ZINTERACTIONS.ZENDDATE + 978307200, 'UNIXEPOCH') AS 'END DATE',
      ZINTERACTIONS.ZBUNDLEID AS 'BUNDLE ID',
         ZINTERACTIONS.ZACCOUNT AS 'ACCOUNT',
      ZINTERACTIONS.ZTARGETBUNDLEID AS 'TARGET BUNDLE ID',
      CASE ZINTERACTIONS.ZDIRECTION
         WHEN '0' THEN 'INCOMING'
         WHEN '1' THEN 'OUTGOING'
      END 'DIRECTION',
      ZCONTACTS.ZDISPLAYNAME AS 'SENDER DISPLAY NAME',
      ZCONTACTS.ZIDENTIFIER AS 'SENDER IDENTIFIER',
      ZCONTACTS.ZPERSONID AS 'SENDER PERSONID',
      RECEIPIENTCONACT.ZDISPLAYNAME AS 'RECIPIENT DISPLAY NAME',
      RECEIPIENTCONACT.ZIDENTIFIER AS 'RECIPIENT IDENTIFIER',
      RECEIPIENTCONACT.ZPERSONID AS 'RECIPIENT PERSONID',
      ZINTERACTIONS.ZRECIPIENTCOUNT AS 'RECIPIENT COUNT',  
      ZINTERACTIONS.ZDOMAINIDENTIFIER AS 'DOMAIN IDENTIFIER',  
      ZINTERACTIONS.ZISRESPONSE AS 'IS RESPONSE',
      ZATTACHMENT.ZCONTENTTEXT AS 'CONTEXT TEXT',
      ZATTACHMENT.ZUTI AS 'UTI',
      ZATTACHMENT.ZCONTENTURL AS 'CONTENT URL',
      ZATTACHMENT.ZSIZEINBYTES AS 'SIZE IN BYTES',
      HEX(ZATTACHMENT.ZIDENTIFIER) AS 'ATTACHMENT ID',
      ZATTACHMENT.ZCLOUDIDENTIFIER AS 'CLOUD IDENTIFIER',
            ZCONTACTS.ZINCOMINGRECIPIENTCOUNT AS 'INCOMING RECIPIENT COUNT', 
        ZCONTACTS.ZINCOMINGSENDERCOUNT AS 'INCOMING SENDER COUNT', 
         ZCONTACTS.ZOUTGOINGRECIPIENTCOUNT AS 'OUTGOING RECIPIENT COUNT', 
      DATETIME(ZINTERACTIONS.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ZINTERACTIONS CREATION DATE',
      DATETIME(ZCONTACTS.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ZCONTACTS CREATION DATE',
      DATETIME(ZCONTACTS.ZFIRSTINCOMINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'FIRST INCOMING RECIPIENT DATE',
      DATETIME(ZCONTACTS.ZFIRSTINCOMINGSENDERDATE + 978307200, 'UNIXEPOCH') AS 'FIRST INCOMING SENDER DATE',
      DATETIME(ZCONTACTS.ZFIRSTOUTGOINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'FIRST OUTGOING RECIPIENT DATE',
      DATETIME(ZCONTACTS.ZLASTINCOMINGSENDERDATE + 978307200, 'UNIXEPOCH') AS 'LAST INCOMING SENDER DATE',
         CASE ZCONTACTS.ZLASTINCOMINGRECIPIENTDATE 
            WHEN '0' THEN '0' 
            ELSE DATETIME(ZCONTACTS.ZLASTINCOMINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') 
         END 'LAST INCOMING RECIPIENT DATE', 
         DATETIME(ZCONTACTS.ZLASTOUTGOINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'LAST OUTGOING RECIPIENT DATE', 
         ZCONTACTS.ZCUSTOMIDENTIFIER AS 'CUSTOM IDENTIFIER', 
         ZINTERACTIONS.ZCONTENTURL AS 'CONTENT URL', 
         ZINTERACTIONS.ZLOCATIONUUID AS 'LOCATION UUID', 
         ZINTERACTIONS.Z_PK AS 'ZINTERACTIONS TABLE ID' 
      FROM
         ZINTERACTIONS 
         LEFT JOIN
            ZCONTACTS 
            ON ZINTERACTIONS.ZSENDER = ZCONTACTS.Z_PK
         LEFT JOIN Z_1INTERACTIONS ON ZINTERACTIONS.Z_PK == Z_1INTERACTIONS.Z_3INTERACTIONS
         LEFT JOIN ZATTACHMENT ON Z_1INTERACTIONS.Z_1ATTACHMENTS == ZATTACHMENT.Z_PK
         LEFT JOIN Z_2INTERACTIONRECIPIENT ON ZINTERACTIONS.Z_PK== Z_2INTERACTIONRECIPIENT.Z_3INTERACTIONRECIPIENT
         LEFT JOIN ZCONTACTS RECEIPIENTCONACT ON Z_2INTERACTIONRECIPIENT.Z_2RECIPIENTS== RECEIPIENTCONACT.Z_PK 

[SQL Query 10,11]
QUERY=
   SELECT
      DATETIME(ZINTERACTIONS.ZSTARTDATE + 978307200, 'UNIXEPOCH') AS 'START DATE',
      DATETIME(ZINTERACTIONS.ZENDDATE + 978307200, 'UNIXEPOCH') AS 'END DATE',
      ZINTERACTIONS.ZBUNDLEID AS 'BUNDLE ID',
      ZCONTACTS.ZDISPLAYNAME AS 'DISPLAY NAME',
      ZCONTACTS.ZIDENTIFIER AS 'IDENTIFIER',
      ZCONTACTS.ZPERSONID AS 'PERSONID',
      ZINTERACTIONS.ZDIRECTION AS 'DIRECTION',
      ZINTERACTIONS.ZISRESPONSE AS 'IS RESPONSE',
      ZINTERACTIONS.ZMECHANISM AS 'MECHANISM',
      ZINTERACTIONS.ZRECIPIENTCOUNT AS 'RECIPIENT COUNT',
      DATETIME(ZINTERACTIONS.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ZINTERACTIONS CREATION DATE',
      DATETIME(ZCONTACTS.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ZCONTACTS CREATION DATE',
      DATETIME(ZCONTACTS.ZFIRSTINCOMINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'FIRST INCOMING RECIPIENT DATE',
      DATETIME(ZCONTACTS.ZFIRSTINCOMINGSENDERDATE + 978307200, 'UNIXEPOCH') AS 'FIRST INCOMING SENDER DATE',
      DATETIME(ZCONTACTS.ZFIRSTOUTGOINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'FIRST OUTGOING RECIPIENT DATE',
      DATETIME(ZCONTACTS.ZLASTINCOMINGSENDERDATE + 978307200, 'UNIXEPOCH') AS 'LAST INCOMING SENDER DATE',
      CASE
         ZLASTINCOMINGRECIPIENTDATE 
         WHEN
            '0' 
         THEN
            '0' 
         ELSE
            DATETIME(ZCONTACTS.ZLASTINCOMINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') 
      END AS 'LAST INCOMING RECIPIENT DATE', 
      DATETIME(ZCONTACTS.ZLASTOUTGOINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'LAST OUTGOING RECIPIENT DATE', 
      ZINTERACTIONS.ZACCOUNT AS 'ACCOUNT', 
      ZINTERACTIONS.ZDOMAINIDENTIFIER AS 'DOMAIN IDENTIFIER', 
      ZCONTACTS.ZINCOMINGRECIPIENTCOUNT AS 'INCOMING RECIPIENT COUNT', 
      ZCONTACTS.ZINCOMINGSENDERCOUNT AS 'INCOMING SENDER COUNT', 
      ZCONTACTS.ZOUTGOINGRECIPIENTCOUNT AS 'OUTGOING RECIPIENT COUNT', 
      ZCONTACTS.ZCUSTOMIDENTIFIER AS 'CUSTOM IDENTIFIER', 
      ZINTERACTIONS.ZCONTENTURL AS 'CONTENT URL', 
      ZINTERACTIONS.ZLOCATIONUUID AS 'LOCATION UUID', 
      ZINTERACTIONS.Z_PK AS 'ZINTERACTIONS TABLE ID' 
   FROM
      ZINTERACTIONS 
      LEFT JOIN
         ZCONTACTS 
         ON ZINTERACTIONS.ZSENDER = ZCONTACTS.Z_PK

[SQL Query 9]
QUERY=
   SELECT
      DATETIME(ZINTERACTIONS.ZSTARTDATE + 978307200, 'UNIXEPOCH') AS 'START DATE',
      DATETIME(ZINTERACTIONS.ZENDDATE + 978307200, 'UNIXEPOCH') AS 'END DATE',
      DATETIME(ZINTERACTIONS.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ZINTERACTIONS CREATION DATE',
      ZINTERACTIONS.ZBUNDLEID AS 'BUNDLE ID',
      ZCONTACTS.ZDISPLAYNAME AS 'DISPLAY NAME',
      ZCONTACTS.ZIDENTIFIER AS 'IDENTIFIER',
      ZCONTACTS.ZPERSONID AS 'PERSONID',
      ZINTERACTIONS.ZDIRECTION AS 'DIRECTION',
      ZINTERACTIONS.ZISRESPONSE AS 'IS RESPONSE',
      ZINTERACTIONS.ZMECHANISM AS 'MECHANISM',
      DATETIME(ZCONTACTS.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ZCONTACTS CREATION DATE',
      DATETIME(ZCONTACTS.ZFIRSTINCOMINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'FIRST INCOMING RECIPIENT DATE',
      DATETIME(ZCONTACTS.ZFIRSTINCOMINGSENDERDATE + 978307200, 'UNIXEPOCH') AS 'FIRST INCOMING SENDER DATE',
      DATETIME(ZCONTACTS.ZFIRSTOUTGOINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'FIRST OUTGOING RECIPIENT DATE',
      DATETIME(ZCONTACTS.ZLASTINCOMINGSENDERDATE + 978307200, 'UNIXEPOCH') AS 'LAST INCOMING SENDER DATE',
      CASE
         ZLASTINCOMINGRECIPIENTDATE 
         WHEN
            '0' 
         THEN
            '0' 
         ELSE
            DATETIME(ZCONTACTS.ZLASTINCOMINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') 
      END AS 'LAST INCOMING RECIPIENT DATE', 
      DATETIME(ZCONTACTS.ZLASTOUTGOINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'LAST OUTGOING RECIPIENT DATE', 
      ZINTERACTIONS.ZACCOUNT AS 'ACCOUNT', 
      ZINTERACTIONS.ZDOMAINIDENTIFIER AS 'DOMAIN IDENTIFIER', 
      ZCONTACTS.ZINCOMINGRECIPIENTCOUNT AS 'INCOMING RECIPIENT COUNT', 
      ZCONTACTS.ZINCOMINGSENDERCOUNT AS 'INCOMING SENDER COUNT', 
      ZCONTACTS.ZOUTGOINGRECIPIENTCOUNT AS 'OUTGOING RECIPIENT COUNT', 
      ZINTERACTIONS.ZCONTENTURL AS 'CONTENT URL', 
      ZINTERACTIONS.ZLOCATIONUUID AS 'LOCATION UUID', 
      ZINTERACTIONS.Z_PK AS 'ZINTERACTIONS TABLE ID' 
   FROM
      ZINTERACTIONS 
      LEFT JOIN
         ZCONTACTS 
         ON ZINTERACTIONS.ZSENDER = ZCONTACTS.Z_PKroot@tryhackme:/home/ubuntu/APOLLO/modules# 
```

```bash
SELECT
      DATETIME(ZINTERACTIONS.ZSTARTDATE + 978307200, 'UNIXEPOCH') AS 'START DATE',
      DATETIME(ZINTERACTIONS.ZENDDATE + 978307200, 'UNIXEPOCH') AS 'END DATE',
      ZINTERACTIONS.ZBUNDLEID AS 'BUNDLE ID',
      ZINTERACTIONS.ZACCOUNT AS 'ACCOUNT',
      ZINTERACTIONS.ZTARGETBUNDLEID AS 'TARGET BUNDLE ID',
      CASE ZINTERACTIONS.ZDIRECTION
         WHEN '0' THEN 'INCOMING'
         WHEN '1' THEN 'OUTGOING'
      END 'DIRECTION',
      ZCONTACTS.ZDISPLAYNAME AS 'SENDER DISPLAY NAME',
      ZCONTACTS.ZIDENTIFIER AS 'SENDER IDENTIFIER',
      ZCONTACTS.ZPERSONID AS 'SENDER PERSONID',
      RECEIPIENTCONACT.ZDISPLAYNAME AS 'RECIPIENT DISPLAY NAME',
      RECEIPIENTCONACT.ZIDENTIFIER AS 'RECIPIENT IDENTIFIER',
      RECEIPIENTCONACT.ZPERSONID AS 'RECIPIENT PERSONID',
      ZINTERACTIONS.ZRECIPIENTCOUNT AS 'RECIPIENT COUNT',  
      ZINTERACTIONS.ZDOMAINIDENTIFIER AS 'DOMAIN IDENTIFIER',   
      ZINTERACTIONS.ZISRESPONSE AS 'IS RESPONSE',
      ZATTACHMENT.ZCONTENTTEXT AS 'CONTEXT TEXT',
      ZATTACHMENT.ZUTI AS 'UTI',
      ZATTACHMENT.ZCONTENTURL AS 'CONTENT URL',
      ZATTACHMENT.ZSIZEINBYTES AS 'SIZE IN BYTES',
      ZATTACHMENT.ZPHOTOLOCALIDENTIFIER AS 'PHOTO LOCAL IDENTIFIER',
      HEX(ZATTACHMENT.ZIDENTIFIER) AS 'ATTACHMENT ID',
      ZATTACHMENT.ZCLOUDIDENTIFIER AS 'CLOUD IDENTIFIER',
      ZCONTACTS.ZINCOMINGRECIPIENTCOUNT AS 'INCOMING RECIPIENT COUNT', 
      ZCONTACTS.ZINCOMINGSENDERCOUNT AS 'INCOMING SENDER COUNT', 
      ZCONTACTS.ZOUTGOINGRECIPIENTCOUNT AS 'OUTGOING RECIPIENT COUNT', 
      DATETIME(ZINTERACTIONS.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ZINTERACTIONS CREATION DATE',
      DATETIME(ZCONTACTS.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ZCONTACTS CREATION DATE',
      DATETIME(ZCONTACTS.ZFIRSTINCOMINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'FIRST INCOMING RECIPIENT DATE',
      DATETIME(ZCONTACTS.ZFIRSTINCOMINGSENDERDATE + 978307200, 'UNIXEPOCH') AS 'FIRST INCOMING SENDER DATE',
      DATETIME(ZCONTACTS.ZFIRSTOUTGOINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'FIRST OUTGOING RECIPIENT DATE',
      DATETIME(ZCONTACTS.ZLASTINCOMINGSENDERDATE + 978307200, 'UNIXEPOCH') AS 'LAST INCOMING SENDER DATE',
      CASE ZCONTACTS.ZLASTINCOMINGRECIPIENTDATE 
         WHEN '0' THEN '0' 
         ELSE DATETIME(ZCONTACTS.ZLASTINCOMINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') 
      END 'LAST INCOMING RECIPIENT DATE', 
      DATETIME(ZCONTACTS.ZLASTOUTGOINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'LAST OUTGOING RECIPIENT DATE', 
      ZCONTACTS.ZCUSTOMIDENTIFIER AS 'CUSTOM IDENTIFIER', 
      ZINTERACTIONS.ZCONTENTURL AS 'CONTENT URL', 
      ZINTERACTIONS.ZLOCATIONUUID AS 'LOCATION UUID', 
      ZINTERACTIONS.ZGROUPNAME AS 'GROUP NAME',
      ZINTERACTIONS.ZDERIVEDINTENTIDENTIFIER AS 'DERIVIED INTENT ID',
      ZINTERACTIONS.Z_PK AS 'ZINTERACTIONS TABLE ID' 
   FROM ZINTERACTIONS 
   LEFT JOIN ZCONTACTS ON ZINTERACTIONS.ZSENDER = ZCONTACTS.Z_PK
   LEFT JOIN Z_1INTERACTIONS ON ZINTERACTIONS.Z_PK == Z_1INTERACTIONS.Z_3INTERACTIONS
   LEFT JOIN ZATTACHMENT ON Z_1INTERACTIONS.Z_1ATTACHMENTS == ZATTACHMENT.Z_PK
   LEFT JOIN Z_2INTERACTIONRECIPIENT ON ZINTERACTIONS.Z_PK== Z_2INTERACTIONRECIPIENT.Z_3INTERACTIONRECIPIENT
   LEFT JOIN ZCONTACTS RECEIPIENTCONACT ON Z_2INTERACTIONRECIPIENT.Z_2RECIPIENTS== RECEIPIENTCONACT.Z_PK 
```

![image](https://github.com/user-attachments/assets/31b1cef0-0088-4e35-b8eb-edd9f68cc64a)


![image](https://github.com/user-attachments/assets/5c38658d-634a-4d19-8166-55163d185d85)

<br>


> 5.2. <em>A call was made using FaceTime on 2025-04-26 05:40:04. Was this call answered? Y/N</em><br><a id='5.2'></a>
>> <strong><code>N</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/a8bcee22-7c32-4107-bd9e-5d3f6c402553)

![image](https://github.com/user-attachments/assets/59b59a16-19e8-4af3-8cd7-acda980ec281)

<br>

> 5.3. <em>The user received a message on 2025-04-26 05:38:20. This message contained an image as an attachment. What animal is present in that image?</em><br><a id='5.3'></a>
>> <strong><code>Dog</code></strong><br>
<p></p>


```bash
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Application Support/CallHistoryDB# ls
CallHistory.storedata  CallHistory.storedata-shm  CallHistory.storedata-wal  com.apple.callhistory.databaseInfo.plist
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Application Support/CallHistoryDB# cp CallHistory.storedata /home/ubuntu/sql/CallHistory.storedata
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Application Support/CallHistoryDB# 
```

![image](https://github.com/user-attachments/assets/8d77f089-482d-47ef-b124-295694e20f80)

```bash
root@tryhackme:/home/ubuntu/APOLLO/modules# cat call_history.txt
...
QUERY=
	SELECT 
		DATETIME(ZDATE+978307200,'UNIXEPOCH') AS "TIMESTAMP",
		ZANSWERED AS "WAS ANSWERED", 
		ZDISCONNECTED_CAUSE AS "DISCONNECTED  CAUSE",
		ZCALLTYPE AS "CALL TYPE", 
		ZORIGINATED AS "ORIGINATED", 
		ZDURATION/60.00 AS "DURATION (IN MINUTES)",
		ZDURATION AS "DURATION (IN SECONDS)",
		ZISO_COUNTRY_CODE AS "ISO COUNTRY CODE",
		ZLOCATION AS "LOCATION", 
		ZSERVICE_PROVIDER AS "SERVICE PROVIDER",
		HEX(CAST(ZADDRESS AS TEXT)) AS "ADDRESS",
		ZCALLRECORD.Z_PK AS "ZCALLRECORD TABLE ID"
	FROM ZCALLRECORD

[SQL Query 9,10,11,12,13,14]
QUERY=
	SELECT
		DATETIME(ZDATE+978307200,'UNIXEPOCH') AS "TIMESTAMP",
		CAST(ZADDRESS AS TEXT) AS "ADDRESS",
		ZANSWERED AS "WAS ANSWERED", 
		ZCALLTYPE AS "CALL TYPE", 
		ZORIGINATED AS "ORIGINATED", 
		ZDURATION/60.00 AS "DURATION (IN MINUTES)",
		ZDURATION AS "DURATION (IN SECONDS)",
		ZISO_COUNTRY_CODE AS "ISO COUNTRY CODE",
		ZLOCATION AS "LOCATION", 
		ZSERVICE_PROVIDER AS "SERVICE PROVIDER",
		ZCALLRECORD.Z_PK AS "ZCALLRECORD TABLE ID"
	FROM ZCALLRECORD

[SQL Query 8]
QUERY=
	SELECT
		DATETIME(ZDATE+978307200,'UNIXEPOCH') AS "TIMESTAMP",
		CAST(ZADDRESS AS TEXT) AS "ADDRESS", 
		ZANSWERED AS "WAS ANSWERED", 
		ZCALLTYPE AS "CALL TYPE", 
		ZORIGINATED AS "ORIGINATED",
		ZDURATION/60.00 AS "DURATION (IN MINUTES)", 
		ZDURATION AS "DURATION (IN SECONDS)",
		ZISO_COUNTRY_CODE AS "ISO COUNTRY CODE",
		ZCALLRECORD.Z_PK AS "ZCALLRECORD TABLE ID"
	FROM ZCALLRECORD
root@tryhackme:/home/ubuntu/APOLLO/modules# 

```

```bash
SELECT
		DATETIME(ZDATE+978307200,'UNIXEPOCH') AS "TIMESTAMP",
		CAST(ZADDRESS AS TEXT) AS "ADDRESS",
		ZANSWERED AS "WAS ANSWERED", 
		ZCALLTYPE AS "CALL TYPE", 
		ZORIGINATED AS "ORIGINATED", 
		ZDURATION/60.00 AS "DURATION (IN MINUTES)",
		ZDURATION AS "DURATION (IN SECONDS)",
		ZISO_COUNTRY_CODE AS "ISO COUNTRY CODE",
		ZLOCATION AS "LOCATION", 
		ZSERVICE_PROVIDER AS "SERVICE PROVIDER",
		ZCALLRECORD.Z_PK AS "ZCALLRECORD TABLE ID"
	FROM ZCALLRECORD
```


```bash
root@tryhackme:/home/ubuntu/APOLLO/modules# cat sms_chat.txt
QUERY=
	SELECT
		CASE
			WHEN LENGTH(MESSAGE.DATE)=18 THEN DATETIME(MESSAGE.DATE/1000000000+978307200,'UNIXEPOCH')
			WHEN LENGTH(MESSAGE.DATE)=9 THEN DATETIME(MESSAGE.DATE + 978307200,'UNIXEPOCH')
			ELSE "N/A"
    		END "MESSAGE DATE",			
		CASE 
			WHEN LENGTH(MESSAGE.DATE_DELIVERED)=18 THEN DATETIME(MESSAGE.DATE_DELIVERED/1000000000+978307200,"UNIXEPOCH")
			WHEN LENGTH(MESSAGE.DATE_DELIVERED)=9 THEN DATETIME(MESSAGE.DATE_DELIVERED+978307200,"UNIXEPOCH")
			ELSE "N/A"
		END "DATE DELIVERED",
		CASE 
			WHEN LENGTH(MESSAGE.DATE_READ)=18 THEN DATETIME(MESSAGE.DATE_READ/1000000000+978307200,"UNIXEPOCH")
			WHEN LENGTH(MESSAGE.DATE_READ)=9 THEN DATETIME(MESSAGE.DATE_READ+978307200,"UNIXEPOCH")
			ELSE "N/A"
		END "DATE READ",
		MESSAGE.TEXT AS "MESSAGE",
		HANDLE.ID AS "CONTACT ID",
		MESSAGE.SERVICE AS "SERVICE",
		MESSAGE.ACCOUNT AS "ACCOUNT",
		MESSAGE.IS_DELIVERED AS "IS DELIVERED",
		MESSAGE.IS_FROM_ME AS "IS FROM ME",
		ATTACHMENT.FILENAME AS "FILENAME",
		ATTACHMENT.MIME_TYPE AS "MIME TYPE",
		ATTACHMENT.TRANSFER_NAME AS "TRANSFER TYPE",
		ATTACHMENT.TOTAL_BYTES AS "TOTAL BYTES"
	FROM MESSAGE
	LEFT OUTER JOIN MESSAGE_ATTACHMENT_JOIN ON MESSAGE.ROWID = MESSAGE_ATTACHMENT_JOIN.MESSAGE_ID
	LEFT OUTER JOIN ATTACHMENT ON MESSAGE_ATTACHMENT_JOIN.ATTACHMENT_ID = ATTACHMENT.ROWID
root@tryhackme:/home/ubuntu/APOLLO/modules# 
```

```bash
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Messages# cp chat.db /home/ubuntu/sql/chat.db
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Messages# 
```

```bash
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Messages/Attachments/dd/13/913B654F-F703-418D-9873-0C18BFC89CE5# ls
IMG_0027.jpeg
```


![image](https://github.com/user-attachments/assets/950eb20f-f609-4993-83ee-0a1af937b222)

 
![image](https://github.com/user-attachments/assets/0115a4f5-104f-4442-a1d5-aa540d7693c2)


<br>

> 5.4. <em>On what date and time was the previous message read? Format YYYY-MM-DD hh:mm:ss</em><br><a id='5.3'></a>
>> <strong><code>2025-04-26 05:38:23</code></strong><br>
<p></p>

```bash
SELECT
      DATETIME(ZINTERACTIONS.ZSTARTDATE + 978307200, 'UNIXEPOCH') AS 'START DATE',
      DATETIME(ZINTERACTIONS.ZENDDATE + 978307200, 'UNIXEPOCH') AS 'END DATE',
      ZINTERACTIONS.ZBUNDLEID AS 'BUNDLE ID',
      ZCONTACTS.ZDISPLAYNAME AS 'DISPLAY NAME',
      ZCONTACTS.ZIDENTIFIER AS 'IDENTIFIER',
      ZCONTACTS.ZPERSONID AS 'PERSONID',
      ZINTERACTIONS.ZDIRECTION AS 'DIRECTION',
      ZINTERACTIONS.ZISRESPONSE AS 'IS RESPONSE',
      ZINTERACTIONS.ZMECHANISM AS 'MECHANISM',
      ZINTERACTIONS.ZRECIPIENTCOUNT AS 'RECIPIENT COUNT',
      DATETIME(ZINTERACTIONS.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ZINTERACTIONS CREATION DATE',
      DATETIME(ZCONTACTS.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ZCONTACTS CREATION DATE',
      DATETIME(ZCONTACTS.ZFIRSTINCOMINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'FIRST INCOMING RECIPIENT DATE',
      DATETIME(ZCONTACTS.ZFIRSTINCOMINGSENDERDATE + 978307200, 'UNIXEPOCH') AS 'FIRST INCOMING SENDER DATE',
      DATETIME(ZCONTACTS.ZFIRSTOUTGOINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'FIRST OUTGOING RECIPIENT DATE',
      DATETIME(ZCONTACTS.ZLASTINCOMINGSENDERDATE + 978307200, 'UNIXEPOCH') AS 'LAST INCOMING SENDER DATE',
      CASE
         ZLASTINCOMINGRECIPIENTDATE 
         WHEN
            '0' 
         THEN
            '0' 
         ELSE
            DATETIME(ZCONTACTS.ZLASTINCOMINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') 
      END AS 'LAST INCOMING RECIPIENT DATE', 
      DATETIME(ZCONTACTS.ZLASTOUTGOINGRECIPIENTDATE + 978307200, 'UNIXEPOCH') AS 'LAST OUTGOING RECIPIENT DATE', 
      ZINTERACTIONS.ZACCOUNT AS 'ACCOUNT', 
      ZINTERACTIONS.ZDOMAINIDENTIFIER AS 'DOMAIN IDENTIFIER', 
      ZCONTACTS.ZINCOMINGRECIPIENTCOUNT AS 'INCOMING RECIPIENT COUNT', 
      ZCONTACTS.ZINCOMINGSENDERCOUNT AS 'INCOMING SENDER COUNT', 
      ZCONTACTS.ZOUTGOINGRECIPIENTCOUNT AS 'OUTGOING RECIPIENT COUNT', 
      ZCONTACTS.ZCUSTOMIDENTIFIER AS 'CUSTOM IDENTIFIER', 
      ZINTERACTIONS.ZCONTENTURL AS 'CONTENT URL', 
      ZINTERACTIONS.ZLOCATIONUUID AS 'LOCATION UUID', 
      ZINTERACTIONS.Z_PK AS 'ZINTERACTIONS TABLE ID' 
   FROM
      ZINTERACTIONS 
      LEFT JOIN
         ZCONTACTS 
         ON ZINTERACTIONS.ZSENDER = ZCONTACTS.Z_PK
```

<br>

<h2> Task 6 . Productivity Apps</h2>

<p>[ ... ]</p>


<h3 align="left"> Answer the questions below</h3>

> 6.1. <em>The user received a calendar invite in the mail from someone. What date is the calendar invite for? Format YYYY-MM-DD hh:mm:ss</em><br><a id='6.1'></a>
>> <strong><code>2025-04-27 11:00:00</code></strong><br>
<p></p>


```bash
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Group Containers/group.com.apple.calendar# cp Calendar.sqlitedb /home/ubuntu/calendar
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Group Containers/group.com.apple.calendar# .
```

![image](https://github.com/user-attachments/assets/d6dbc2ba-35b2-4630-b137-21d8be691d3e)

<p>CalendarItem</p>

![image](https://github.com/user-attachments/assets/b1bf52ac-9042-451d-9b42-dd90883761c0)

<p>com.apple.mail</p>

![image](https://github.com/user-attachments/assets/3e3ce2a4-de4d-4c1f-b606-5d3b1a041c96)

<p>https://www.epochconverter.com/coredata</p>

![image](https://github.com/user-attachments/assets/3eec2d22-ccca-4d51-a595-f3f7b9f4014e)


<br>

> 6.2. <em>What was the timezone of the sender of the email invite? Format: GMT+XX:XX</em><br><a id='6.2'></a>
>> <strong><code>GMT+03:00</code></strong><br>
<p></p>

<p>Asia/Riyadh</p>

![image](https://github.com/user-attachments/assets/83fa7b2b-c053-4f42-95cd-a18ff2507d7d)

![image](https://github.com/user-attachments/assets/e2de1da8-e958-4e23-bf4e-d358c28b47ea)


```bash
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Mail/V10/DEC2D507-7869-4151-98C3-E2F920A935CF/[Gmail].mbox/Trash.mbox/708E1A15-F24E-40B5-8A69-FFD9A89FF251/Data/Messages# cat 25.partial.emlx | grep GMT
Subject: Invitation: Discussion @ Sun Apr 27, 2025 2pm - 3pm (GMT+3) (thmguy535@gmail.com)
```

![image](https://github.com/user-attachments/assets/a4233b1b-8444-4f9c-86a3-c63dcfda7c11)

<br>

> 6.3. <em>The user's calendar has another entry named "Jungle cruise". When is this event going to start? Format in GMT YYYY-MM-DD hh:mm:ss</em><br><a id='6.3'></a>
>> <strong><code>2025-04-25 16:00:00</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/aedf506b-1e15-4bbb-a800-504183d7d0fb)

<p>https://www.epochconverter.com/coredata</p>

![image](https://github.com/user-attachments/assets/7dfa2b32-8f35-42a8-a01a-ecb037862698)

<br>

> 6.4. <em>The user saved two notes. Both have the same title. What is the title?</em><br><a id='6.4'></a>
>> <strong><code>Aquickbrownfoxjumpedoverthelazydog</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/ca2f7744-191e-4d15-a379-d54e6a76ea9e)

```bash
ubuntu@tryhackme:~/mac_apt$ python3 mac_apt.py -o /home/ubuntu/notes -c DD /home/ubuntu/mac-disk.img notes
Output path was : /home/ubuntu/notes
MAIN-INFO-Started macOS Artifact Parsing Tool, version 1.12.0.dev (20250110)
MAIN-INFO-Dates and times are in UTC unless the specific artifact being parsed saves it as local time!
MAIN-INFO-Python version = 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0]
MAIN-INFO-Pytsk  version = 20221228
MAIN-INFO-Pyewf  version = 20240506
MAIN-INFO-Pyvmdk version = 20240510
MAIN-INFO-PyAFF4 version = 0.31
MAIN-INFO-Plugins to run: NOTES
MAIN-INFO-Plugins not to run: 
MAIN-INFO-Opened image /home/ubuntu/mac-disk.img
MAIN-INFO-Looking at FS with volume label 'iBootSystemContainer'  @ offset 20480
MAIN-INFO-Looking at FS with volume label 'Container'  @ offset 524308480
MAIN-INFO-Found an APFS container with uuid: 6274F385-52F7-4FF3-98FF-4E2EF18E3826
MAIN-INFO-Reading APFS volumes from container, this may take a few minutes ...
MAIN.HELPERS.APFS_READER-INFO-Vol_2_Preboot Type=inode  Count=138
MAIN.HELPERS.APFS_READER-INFO-Vol_2_Preboot Type=xattr  Count=18
MAIN.HELPERS.APFS_READER-INFO-Vol_2_Preboot Type=dstream_id  Count=66
MAIN.HELPERS.APFS_READER-INFO-Vol_2_Preboot Type=file_extent  Count=84
...
MAIN-INFO---------------------------------------------------
MAIN-INFO-Running plugin NOTES
MAIN.NOTES-INFO-Processing notes for user 'umair-thm' from file /Users/umair-thm/Library/Containers/com.apple.Notes/Data/Library/Notes/NotesV7.storedata
MAIN.NOTES-INFO-Processing notes for user 'umair-thm' from file /Users/umair-thm/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite
MAIN.NOTES-INFO-2 note(s) found
MAIN-INFO---------------------------------------------------
MAIN-INFO-Finished in time = 00:02:22
MAIN-INFO-Review the Log file and report any ERRORs or EXCEPTIONS to the developers
ubuntu@tryhackme:~/mac_apt$ 
```

![image](https://github.com/user-attachments/assets/ac0d3762-4132-4e0e-8a69-f21e1ef5f2b3)

![image](https://github.com/user-attachments/assets/03a61fc8-2ed5-4122-9ced-43e35e85b474)

![image](https://github.com/user-attachments/assets/173ab0cc-24c1-43f1-87b1-38b06be33d9e)

<br>

> 6.5. <em>One of the notes has an attachment we already viewed while analysing iMessage. What animal is present in the other attachment?</em><br><a id='6.5'></a>
>> <strong><code>Giraffe</code></strong><br>
<p></p>


![image](https://github.com/user-attachments/assets/13f47979-6a51-44b3-993d-fe87996d84bb)


```bash
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Mail/V10/DEC2D507-7869-4151-98C3-E2F920A935CF/[Gmail].mbox/All Mail.mbox/708E1A15-F24E-40B5-8A69-FFD9A89FF251/Data/Messages# cat 16.emlx | grep name
	filename=IMG_0027.jpeg
	name="IMG_0027.jpeg"
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Mail/V10/DEC2D507-7869-4151-98C3-E2F920A935CF/[Gmail].mbox/All Mail.mbox/708E1A15-F24E-40B5-8A69-FFD9A89FF251/Data/Messages# 

...
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Mail/V10/DEC2D507-7869-4151-98C3-E2F920A935CF/[Gmail].mbox/All Mail.mbox/708E1A15-F24E-40B5-8A69-FFD9A89FF251/Data/Messages# cat 17.partial.emlx | grep name
	filename=IMG_3050.jpeg
	name=IMG_3050.jpeg
...
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Mail/V10/DEC2D507-7869-4151-98C3-E2F920A935CF/[Gmail].mbox/All Mail.mbox/708E1A15-F24E-40B5-8A69-FFD9A89FF251/Data/Attachments/17/2# cp IMG_3050.jpeg /home/ubuntu/IMG_3050.jpeg
```

![image](https://github.com/user-attachments/assets/3a446e0d-b251-414c-8ada-5961a4f1a0ef)

<br>

> 6.6. <em>The user has saved a reminder that has not been completed yet. What is the due date of this reminder? Format in GMT YYYY-MM-DD hh:mm:ss</em> Hint : <em>Check the columns in the database to find the one reminder not completed. Convert time from Mac Epoch to human readable as discussed previously.</em><br><a id='6.6'></a>
>> <strong><code>2025-04-26 21:00:00</code></strong><br>
<p></p>

```bash
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Group Containers/group.com.apple.reminders/Container_v1/Stores# ls
Data-2FBE6ADB-3265-4593-A7AD-037852BE690E.sqlite      Data-A49B540B-861A-43FD-AADF-E33510CDEA4E.sqlite      Data-D3B1D04C-086F-41BF-9D99-5DDE225D0B6D.sqlite      Data-local.sqlite
Data-2FBE6ADB-3265-4593-A7AD-037852BE690E.sqlite-shm  Data-A49B540B-861A-43FD-AADF-E33510CDEA4E.sqlite-shm  Data-D3B1D04C-086F-41BF-9D99-5DDE225D0B6D.sqlite-shm  Data-local.sqlite-shm
Data-2FBE6ADB-3265-4593-A7AD-037852BE690E.sqlite-wal  Data-A49B540B-861A-43FD-AADF-E33510CDEA4E.sqlite-wal  Data-D3B1D04C-086F-41BF-9D99-5DDE225D0B6D.sqlite-wal  Data-local.sqlite-wal
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Group Containers/group.com.apple.reminders/Container_v1/Stores# cp Data-2FBE6ADB-3265-4593-A7AD-037852BE690E.sqlite* /home/ubuntu/sql
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Group Containers/group.com.apple.reminders/Container_v1/Stores# cp Data-A49B540B-861A-43FD-AADF-E33510CDEA4E.sqlite* /home/ubuntu/sql
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Group Containers/group.com.apple.reminders/Container_v1/Stores# cp Data-D3B1D04C-086F-41BF-9D99-5DDE225D0B6D.sqlite* /home/ubuntu/sql
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Group Containers/group.com.apple.reminders/Container_v1/Stores# cp Data-local.sqlite* /home/ubuntu/sql
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Group Containers/group.com.apple.reminders/Container_v1/Stores# 
```

![image](https://github.com/user-attachments/assets/4573946c-e075-4843-87d7-a07760c29a34)

<p>767394000</p>

![image](https://github.com/user-attachments/assets/2f9bf10d-ec13-4aa6-8bba-8dfa86d37eb9)

<br>

> 6.7. <em>What is the complete path of the last file opened using Microsoft Word?</em><br><a id='6.7'></a>
>> <strong><code>/Users/umair-thm/Downloads/Report-final-updated.pdf</code></strong><br>
<p></p>

```bash
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Containers/com.microsoft.Word/Data/Library/Preferences# plistutil -p com.microsoft.Word.securebookmarks.plist
```

![image](https://github.com/user-attachments/assets/4b5632ff-2579-4d73-b6d6-1cf69c8aaa43)

<br>

<h2>Task 7 . Browsing History, Downloads, and Bookmarks</h2>

<p>[ ... ]</p>

<h3 align="left"> Answer the question below</h3>

> 7.1. <em>The user seems to be a fan of TryHackMe. What is the URL of the THM room the user visited using Safari?</em><br><a id='7.1'></a>
>> <strong><code>https://tryhackme.com/room/macosforensicsartefacts</code></strong><br>
<p></p>


```bash
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Safari# ls
 AutoFillCorrections.db           CloudAutoFillCorrections.db-shm        'Favicon Cache'                     LocalStorage                           RecentlyClosedTabs.plist
 AutoFillCorrections.db-shm       CloudAutoFillCorrections.db-wal         History.db                        'Metadata Cache'                        SitesAllowedToAutoplay.plist
 AutoFillCorrections.db-wal       CloudBookmarksMigrationCoordinator      History.db-lock                    OfflineSearchRemoteDisablement.plist  'Template Icons'
 AutomaticBookmarksBackup.html    CloudHistoryRemoteConfiguration.plist   History.db-shm                     PasswordBreachStore.plist              TopSites.plist
 BlockedBannerHighlights.db       ContentBlockerStatistics.db             History.db-wal                     PerSitePreferences.db                 'Touch Icons Cache'
 BlockedBannerHighlights.db-wal   ContentBlockerStatistics.db-wal         IgnoredSiriSuggestedSites.db       PerSitePreferences.db-shm              UserDefinedContentBlockers.db
 Bookmarks.plist                  Databases                               IgnoredSiriSuggestedSites.db-shm   PerSitePreferences.db-wal              UserDefinedContentBlockers.db-shm
 CloudAutoFillCorrections.db      Downloads.plist                         IgnoredSiriSuggestedSites.db-wal   PerSiteZoomPreferences.plist           UserDefinedContentBlockers.db-wal
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Safari# cp History.db /home/ubuntu/sql
root@tryhackme:/home/ubuntu/mac/root/Users/umair-thm/Library/Safari#
```

![image](https://github.com/user-attachments/assets/6764a3b2-f492-4afe-bae0-e0f3f630f1c3)


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


![image](https://github.com/user-attachments/assets/46d85b9b-ac35-4684-b33e-3e43fe55b8d1)

![image](https://github.com/user-attachments/assets/27894aa9-8652-4b96-967a-8b491e65e8fa)

<br>

<h2>Task 8 . Photos and Apple Pay</h2>

<p>[ ... ]

<h3 align="left"> Answer the questions below</h3>

> 8.1. <em>When using APOLLO queries to parse passes, to what should we change the field PAYMENT_TRANSACTION.PASS_PID on newer macOS versions?</em><br><a id='8.1'></a>
>> <strong><code>PAYMENT_TRANSACTION.PID</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/b210e64e-77d2-44c8-a7ff-759a90fa7f5d)


![image](https://github.com/user-attachments/assets/ab113cc5-1b8b-4cb8-a88c-572defc3277c)

<br>

<h2>Task 9 . COnclusion</h2>
<p>And that's a wrap! In this room, we learned to trace user activity across multiple applications. In summary, we discovered:<br><br>

- Where applications reside in macOS and how to trace their installation history.<br>
- What type of persistence mechanisms are present in macOS<br>
- How do you extract notifications from different applications, and what permissions do the applications have?<br>
- Contacts and interactions with contacts using calls, messages and FaceTime on a Mac.<br>
- What kind of artefacts do productivity apps like Notes, Reminders, and Calendars leave on macOS.<br>
- Sensitive information of a Mac user, such as browsing history, photos, and wallet information.<br><br>

Do you know of any other artefacts that can be found in a macOS machine? Let us know in our Discord channel or X account. See you around.</p>

<h3 align="left"> Answer the questions below</h3>

> 9.1. <em>I am confident I can forensicate a Mac now and am ready for a challenge!</em><br><a id='9.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h1 align="center">Room Completed</h1>
<br>
<p align="center"><img width="1000px" src="https://github.com/user-attachments/assets/72df4890-1a75-4f3f-b2cf-0356b51d4bbc"><br>
                  <img width="1000px" src="https://github.com/user-attachments/assets/9486aff2-0b5e-43da-a961-63254f65a812"></p>

<h1 align="center"> My TryHackMe Journey</h1>
<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 14 2025      | 404      |     203ʳᵈ    |      4ᵗʰ     |     450ᵗʰ   |     8ᵗʰ    |  107,665 |    777    |     62    |

</div>

<p align="center"> Global All Time:  203ʳᵈ<br><br>
<img width="240px" src="https://github.com/user-attachments/assets/b5f40ba3-ab25-4b57-a798-9df6f95c8d5"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/d606c3cc-5af5-4d55-9953-6c31245a51f5"></p>
<p align="center"> Brazil All Time:     4ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/5458a0d4-1895-45e5-8717-a4fcf6004e39"> </p>
<p align="center"> Global monthly:    450ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/07c12d0f-f38a-40c5-8bab-4a0195a5cff4"> </p
<p align="center"> Brazil monthly:       8ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/8be1eb6c-2b1e-4dcb-b486-bd592b72d55b"> </p>

<h1 align="center">Thanks for coming!!!</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<h1 align="center">Thank you</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and <a href="https://tryhackme.com/p/umairalizafar">umairalizafar</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
