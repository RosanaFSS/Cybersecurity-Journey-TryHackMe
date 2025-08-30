```bash
:~/Voyage# nmap -sT -p- -T4 10.201.41.41
...
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
2222/tcp open  EtherNetIP-1
```

```bash
:~/Voyage# nmap -A 10.201.41.41 -p 22,80,2222
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.58 ((Ubuntu))
|_http-generator: Joomla! - Open Source Content Management
| http-robots.txt: 16 disallowed entries (15 shown)
| /joomla/administrator/ /administrator/ /api/ /bin/ 
| /cache/ /cli/ /components/ /includes/ /installation/ 
|_/language/ /layouts/ /libraries/ /logs/ /modules/ /plugins/
|_http-server-header: Apache/2.4.58 (Ubuntu)
|_http-title: Home
2222/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
```


<h2>xx.xxx.xx.xx or xx.xxx.xx.xx/index.php</h2>
<p>
  
- grid-child container-component<br>mod-breadcrumbs__wrapper<br>Breadcrumbs<br>mod-breadcrumbs breadcrumb px-3 py-2<br>mod-breadcrumbs__item breadcrumb-item activ<br><br>
- system-message-container<br>polite<br>https://schema.org/Blog<br><br>
- grid-child container-sidebar-right<br>action= index.php, method=post<br><br>
- sidebar-right card<br>mod-login__userdata userdata<br>mod-login__username form-group<br>input-group<br>type="text" name="username" class="form-control" autocomplete="username" placeholder="Username"><br>class="input-group-text" title="Username"<br>
- mod-login__password form-group<br>type="password" name="password" autocomplete="current-password" class="form-control" placeholder="Password"><br>mod-login__remember form-group<br>Remember Me<br>mod-login__options list-unstyled<br><br>
- /index.php/component/users/reset?Itemid=101<br><br>Forgot your password?<br>/index.php/component/users/remind?Itemid=101<br><br>Forgot your username?<br><br>type="hidden" name="option" value="com_users"<br>put type="hidden" name="task" value="user.login"<br>type="hidden" name="return" value="aHR0cDovLzEwLjIwMS40MS40MS8="<br>type="hidden" name="86785eab33b627e9955afd7cd086754c" value="1"</p>

<img width="1107" height="502" alt="image" src="https://github.com/user-attachments/assets/38872d3b-2f2c-4042-bbce-33b61d81a9f3" />


<h2>xx.xxx.xx.xx/robots.txt</h2>

```bash
# If the Joomla site is installed within a folder
# eg www.example.com/joomla/ then the robots.txt file
# MUST be moved to the site root
# eg www.example.com/robots.txt
# AND the joomla folder name MUST be prefixed to all of the
# paths.
# eg the Disallow rule for the /administrator/ folder MUST
# be changed to read
# Disallow: /joomla/administrator/
#
# For more information about the robots.txt standard, see:
# https://www.robotstxt.org/orig.html

User-agent: *
Disallow: /administrator/
Disallow: /api/
Disallow: /bin/
Disallow: /cache/
Disallow: /cli/
Disallow: /components/
Disallow: /includes/
Disallow: /installation/
Disallow: /language/
Disallow: /layouts/
Disallow: /libraries/
Disallow: /logs/
Disallow: /modules/
Disallow: /plugins/
Disallow: /tmp/
```

<h2>xx.xxx.xx.xx/administrator</h2>

<img width="1121" height="602" alt="image" src="https://github.com/user-attachments/assets/e5f389ec-6f21-4acc-8a7a-933799133afa" />


<h2>xx.xxx.xx.xx/administrator/components</h2>

<img width="1127" height="571" alt="image" src="https://github.com/user-attachments/assets/e9d94931-49f5-468e-a49a-6d23660865b4" />

<h2>xx.xxx.xx.xx/administrator/manisfests/files/joomla.xml</h2>
<p>

- type="file" method="upgrade"<br>
- admin@joomla.org<br>
- version = 4.2.7</p>
- creation date = 2023-01<br>
- script file = administrator/components/com_admin/script.php<br>
- schema path type = mysql = administrator/components/com_admin/sql/updates/mysql<br>
- schema path type = postgresql = administrator/components/com_admin/sql/updates/postgresql<br>
- administrator, api, cache, cli, components, images, includes, language, layouts, libraries, media, modules, plugins, templates, tmp, htaccess.txt, web.config.txt, LICENSE.txt, README.txt, index.php<b>
- name = Joomla! Core<br>
- type = collection = https://update.joomla.ord/core/list.xml


<img width="1120" height="565" alt="image" src="https://github.com/user-attachments/assets/2b65afdd-ccdb-43b1-a5b3-ea3ca1b2d81a" />


<h2>xx.xxx.xx.xx/web.config.txt</h2>

```bash
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
   <location path=".">
   <system.webServer>
       <directoryBrowse enabled="false" />
       <rewrite>
           <rules>
               <rule name="Joomla! Common Exploits Prevention" stopProcessing="true">
                   <match url="^(.*)$" ignoreCase="false" />
                   <conditions logicalGrouping="MatchAny">
                       <add input="{QUERY_STRING}" pattern="base64_encode[^(]*\([^)]*\)" ignoreCase="false" />
                       <add input="{QUERY_STRING}" pattern="(&gt;|%3C)([^s]*s)+cript.*(&lt;|%3E)" />
                       <add input="{QUERY_STRING}" pattern="GLOBALS(=|\[|\%[0-9A-Z]{0,2})" ignoreCase="false" />
                       <add input="{QUERY_STRING}" pattern="_REQUEST(=|\[|\%[0-9A-Z]{0,2})" ignoreCase="false" />
                   </conditions>
                   <action type="CustomResponse" url="index.php" statusCode="403" statusReason="Forbidden" statusDescription="Forbidden" />
               </rule>
               <rule name="Joomla! API Application SEF URLs">
                   <match url="^api/(.*)" ignoreCase="false" />
                   <conditions logicalGrouping="MatchAll">
                     <add input="{URL}" pattern="^/api/index.php" ignoreCase="true" negate="true" />
                     <add input="{REQUEST_FILENAME}" matchType="IsFile" ignoreCase="false" negate="true" />
                     <add input="{REQUEST_FILENAME}" matchType="IsDirectory" ignoreCase="false" negate="true" />
                   </conditions>
                   <action type="Rewrite" url="api/index.php" />
               </rule>
               <rule name="Joomla! Public Frontend SEF URLs">
                   <match url="(.*)" ignoreCase="false" />
                   <conditions logicalGrouping="MatchAll">
                     <add input="{URL}" pattern="^/index.php" ignoreCase="true" negate="true" />
                     <add input="{REQUEST_FILENAME}" matchType="IsFile" ignoreCase="false" negate="true" />
                     <add input="{REQUEST_FILENAME}" matchType="IsDirectory" ignoreCase="false" negate="true" />
                   </conditions>
                   <action type="Rewrite" url="index.php" />
               </rule>
           </rules>
       </rewrite>
       <httpProtocol>
           <customHeaders>
               <add name="X-Content-Type-Options" value="nosniff" />
               <!-- Protect against certain cross-origin requests. More information can be found here: -->
               <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/Cross-Origin_Resource_Policy_(CORP) -->
               <!-- https://web.dev/why-coop-coep/ -->
               <!-- <add name="Cross-Origin-Resource-Policy" value="same-origin" /> -->
               <!-- <add name="Cross-Origin-Embedder-Policy" value="require-corp" /> -->
           </customHeaders>
       </httpProtocol>
   </system.webServer>
   </location>
</configuration>
```


<h2>xx.xxx.xx.xx/htaccess.txt</h2>

```bash
##
# @package    Joomla
# @copyright  (C) 2005 Open Source Matters, Inc. <https://www.joomla.org>
# @license    GNU General Public License version 2 or later; see LICENSE.txt
##

##
# READ THIS COMPLETELY IF YOU CHOOSE TO USE THIS FILE!
#
# The line 'Options +FollowSymLinks' may cause problems with some server configurations.
# It is required for the use of Apache mod_rewrite, but it may have already been set by
# your server administrator in a way that disallows changing it in this .htaccess file.
# If using it causes your site to produce an error, comment it out (add # to the
# beginning of the line), reload your site in your browser and test your sef urls. If
# they work, then it has been set by your server administrator and you do not need to
# set it here.
##

## MISSING CSS OR JAVASCRIPT ERRORS
#
# If your site looks strange after enabling this file, then your server is probably already
# gzipping css and js files and you should comment out the GZIP section of this file.
##

## OPENLITESPEED
#
# If you are using an OpenLiteSpeed web server then any changes made to this file will
# not take effect until you have restarted the web server.
##

## Can be commented out if causes errors, see notes above.
Options +FollowSymlinks
Options -Indexes

## No directory listings
<IfModule mod_autoindex.c>
	IndexIgnore *
</IfModule>

## Suppress mime type detection in browsers for unknown types
<IfModule mod_headers.c>
	Header always set X-Content-Type-Options "nosniff"
</IfModule>

## Protect against certain cross-origin requests. More information can be found here:
## https://developer.mozilla.org/en-US/docs/Web/HTTP/Cross-Origin_Resource_Policy_(CORP)
## https://web.dev/why-coop-coep/
#<IfModule mod_headers.c>
#	Header always set Cross-Origin-Resource-Policy "same-origin"
#	Header always set Cross-Origin-Embedder-Policy "require-corp"
#</IfModule>

## Disable inline JavaScript when directly opening SVG files or embedding them with the object-tag
<FilesMatch "\.svg$">
  <IfModule mod_headers.c>
    Header always set Content-Security-Policy "script-src 'none'"
  </IfModule>
</FilesMatch>

## These directives are only enabled if the Apache mod_rewrite module is enabled
<IfModule mod_rewrite.c>
	RewriteEngine On

	## Begin - Rewrite rules to block out some common exploits.
	# If you experience problems on your site then comment out the operations listed
	# below by adding a # to the beginning of the line.
	# This attempts to block the most common type of exploit `attempts` on Joomla!
	#
	# Block any script trying to base64_encode data within the URL.
	RewriteCond %{QUERY_STRING} base64_encode[^(]*\([^)]*\) [OR]
	# Block any script that includes a <script> tag in URL.
	RewriteCond %{QUERY_STRING} (<|%3C)([^s]*s)+cript.*(>|%3E) [NC,OR]
	# Block any script trying to set a PHP GLOBALS variable via URL.
	RewriteCond %{QUERY_STRING} GLOBALS(=|\[|\%[0-9A-Z]{0,2}) [OR]
	# Block any script trying to modify a _REQUEST variable via URL.
	RewriteCond %{QUERY_STRING} _REQUEST(=|\[|\%[0-9A-Z]{0,2})
	# Return 403 Forbidden header and show the content of the root home page
	RewriteRule .* index.php [F]
	#
	## End - Rewrite rules to block out some common exploits.

	## Begin - Custom redirects
	#
	# If you need to redirect some pages, or set a canonical non-www to
	# www redirect (or vice versa), place that code here. Ensure those
	# redirects use the correct RewriteRule syntax and the [R=301,L] flags.
	#
	## End - Custom redirects

	##
	# Uncomment the following line if your webserver's URL
	# is not directly related to physical file paths.
	# Update Your Joomla! Directory (just / for root).
	##

	# RewriteBase /

	## Begin - Joomla! core SEF Section.
	#
	# PHP FastCGI fix for HTTP Authorization, required for the API application
	RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
	# -- SEF URLs for the API application
	# If the requested path starts with /api, the file is not /api/index.php
	# and the request has not already been internally rewritten to the
	# api/index.php script
	RewriteCond %{REQUEST_URI} ^/api/
	RewriteCond %{REQUEST_URI} !^/api/index\.php
	# and the requested path and file doesn't directly match a physical file
	RewriteCond %{REQUEST_FILENAME} !-f
	# and the requested path and file doesn't directly match a physical folder
	RewriteCond %{REQUEST_FILENAME} !-d
	# internally rewrite the request to the /api/index.php script
	RewriteRule .* api/index.php [L]
	# -- SEF URLs for the public frontend application
	# If the requested path and file is not /index.php and the request
	# has not already been internally rewritten to the index.php script
	RewriteCond %{REQUEST_URI} !^/index\.php
	# and the requested path and file doesn't directly match a physical file
	RewriteCond %{REQUEST_FILENAME} !-f
	# and the requested path and file doesn't directly match a physical folder
	RewriteCond %{REQUEST_FILENAME} !-d
	# internally rewrite the request to the index.php script
	RewriteRule .* index.php [L]
	#
	## End - Joomla! core SEF Section.
</IfModule>

## These directives are only enabled if the Apache mod_rewrite module is disabled
<IfModule !mod_rewrite.c>
	<IfModule mod_alias.c>
		# When Apache mod_rewrite is not available, we instruct a temporary redirect
		# of the start page to the front controller explicitly so that the website
		# and the generated links can still be used.
		RedirectMatch 302 ^/$ /index.php/
		# RedirectTemp cannot be used instead
	</IfModule>
</IfModule>

## GZIP
## These directives are only enabled if the Apache mod_headers module is enabled.
## This section will check if a .gz file exists and if so will stream it
##     directly or fallback to gzip any asset on the fly
## If your site starts to look strange after enabling this file, and you see
##     ERR_CONTENT_DECODING_FAILED in your browser console network tab,
##     then your server is already gzipping css and js files and you don't need this
##     block enabled in your .htaccess
<IfModule mod_headers.c>
	# Serve gzip compressed CSS files if they exist
	# and the client accepts gzip.
	RewriteCond "%{HTTP:Accept-encoding}" "gzip"
	RewriteCond "%{REQUEST_FILENAME}\.gz" -s
	RewriteRule "^(.*)\.css" "$1\.css\.gz" [QSA]

	# Serve gzip compressed JS files if they exist
	# and the client accepts gzip.
	RewriteCond "%{HTTP:Accept-encoding}" "gzip"
	RewriteCond "%{REQUEST_FILENAME}\.gz" -s
	RewriteRule "^(.*)\.js" "$1\.js\.gz" [QSA]

	# Serve correct content types, and prevent mod_deflate double gzip.
	RewriteRule "\.css\.gz$" "-" [T=text/css,E=no-gzip:1]
	RewriteRule "\.js\.gz$" "-" [T=text/javascript,E=no-gzip:1]

	<FilesMatch "(\.js\.gz|\.css\.gz)$">
		# Serve correct encoding type.
		Header append Content-Encoding gzip

		# Force proxies to cache gzipped &
		# non-gzipped css/js files separately.
		Header append Vary Accept-Encoding
	</FilesMatch>
</IfModule>
```

<h2>searchsploit</h2>

<img width="1113" height="171" alt="image" src="https://github.com/user-attachments/assets/f6b75536-cdf7-4d1c-aeae-d4572e3b4351" />

```bash
:~/Voyage# searchsploit joomla 4.2.7
------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                    |  Path
------------------------------------------------------------------ ---------------------------------
Joomla! Component MaQma Helpdesk 4.2.7 - 'id' SQL Injection       | php/webapps/41399.txt
------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
```

```bash
:~/Voyage# searchsploit -m php/webapps/41399.txt
  Exploit: Joomla! Component MaQma Helpdesk 4.2.7 - 'id' SQL Injection
      URL: https://www.exploit-db.com/exploits/41399
     Path: /opt/exploitdb/exploits/php/webapps/41399.txt
    Codes: N/A
 Verified: False
File Type: ASCII text
Copied to: /root/Voyage/41399.txt
```

```bash
:~/Voyage# cat 41399.txt
# # # # #
# Exploit Title: Joomla! Component MaQma Helpdesk v4.2.7 - SQL Injection
# Google Dork: inurl:index.php?option=com_maqmahelpdesk
# Date: 20.02.2017
# Vendor Homepage: http://componentslab.com/
# Software Buy: https://extensions.joomla.org/extensions/extension/clients-a-communities/help-desk/maqma-helpdesk/
# Demo: http://demo.componentslab.com/index.php/department/software-support
# Version: 4.2.7
# Tested on: Win7 x64, Kali Linux x64
# # # # #
# Exploit Author: Ihsan Sencan
# Author Web: http://ihsan.net
# Author Mail : ihsan[@]ihsan[.]net
# # # # #
# SQL Injection/Exploit :
# http://localhost/[PATH]/index.php?option=com_maqmahelpdesk&task=pdf_kb&id=[SQL]
```




    ____  _____  _____  __  __  ___   ___    __    _  _ 
   (_  _)(  _  )(  _  )(  \/  )/ __) / __)  /__\  ( \( )
  .-_)(   )(_)(  )(_)(  )    ( \__ \( (__  /(__)\  )  ( 
  \____) (_____)(_____)(_/\/\_)(___/ \___)(__)(__)(_)\_)
			(1337.today)
   
    --=[OWASP JoomScan
    +---++---==[Version : 0.0.7
    +---++---==[Update Date : [2018/09/23]
    +---++---==[Authors : Mohammad Reza Espargham , Ali Razmjoo
    --=[Code name : Self Challenge
    @OWASP_JoomScan , @rezesp , @Ali_Razmjo0 , @OWASP

Processing http://10.201.41.41 ...



[+] FireWall Detector
[++] Firewall not detected

[+] Detecting Joomla Version
[++] Joomla 4.2.7

[+] Core Joomla Vulnerability
[++] Target Joomla core is not vulnerable

[+] Checking Directory Listing
[++] directory has directory listing : 
http://10.201.41.41/administrator/components
http://10.201.41.41/administrator/modules
http://10.201.41.41/administrator/templates
http://10.201.41.41/images/banners


[+] Checking apache info/status files
[++] Readable info/status files are not found

[+] admin finder
[++] Admin page : http://10.201.41.41/administrator/

[+] Checking robots.txt existing
[++] robots.txt is found
path : http://10.201.41.41/robots.txt 

Interesting path found from robots.txt
http://10.201.41.41/joomla/administrator/
http://10.201.41.41/administrator/
http://10.201.41.41/api/
http://10.201.41.41/bin/
http://10.201.41.41/cache/
http://10.201.41.41/cli/
http://10.201.41.41/components/
http://10.201.41.41/includes/
http://10.201.41.41/installation/
http://10.201.41.41/language/
http://10.201.41.41/layouts/
http://10.201.41.41/libraries/
http://10.201.41.41/logs/
http://10.201.41.41/modules/
http://10.201.41.41/plugins/
http://10.201.41.41/tmp/


[+] Finding common backup files name
[++] Backup files are not found

[+] Finding common log files name
[++] error log is not found

[+] Checking sensitive config.php.x file
[++] Readable config files are not found


Your Report : reports/10.201.41.41/


root
RootPassword@1234

joomla_db


```
wget https://downloads.joomla.org/cms/joomla4/4-2-6/Joomla_4-2-6-Stable-Full_Package.zip?format=zip
```


:~/Voyage/joomla/joomscan# ffuf -u http://10.201.41.41/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -recursion -recursion-depth 1 -ic -c -e .php,.html,.js,.txt,.zip



