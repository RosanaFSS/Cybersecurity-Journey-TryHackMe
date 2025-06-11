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
>> <strong><code>____</code></strong><br>
<p></p>

<br>

> 2.2. <em>What is the name of the package used to install Microsoft Word?</em><br><a id='2.1'></a>
>> <strong><code>____</code></strong><br>
<p></p>

<br>


```bash
ubuntu@tryhackme:~$ apfsutil mac-disk.img
```

![image](https://github.com/user-attachments/assets/219aabc6-c057-41d5-b3ed-0d3f39fb23b5)

```bash
ubuntu@tryhackme:~$ sudo su
root@tryhackme:/home/ubuntu# apfs-fuse mac-disk.img mac/
root@tryhackme:/home/ubuntu# ls mac
private-dir  root
...
root@tryhackme:/home/ubuntu/mac/root# ls
Applications  Library  System  Users  Volumes  bin  cores  dev  etc  opt  private  sbin  tmp  usr  var
root@tryhackme:/home/ubuntu/mac/root#
