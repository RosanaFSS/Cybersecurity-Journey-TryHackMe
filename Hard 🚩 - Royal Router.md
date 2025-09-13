<h1 align="center">Royal Router</h1>
<p align="center"><img width="80px" src="   "><br>
2025, September 13<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>495</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>You will learn how to compromise an IoT device</em>.<br>
Access it <a href="https://tryhackme.com/room/hfb1royalrouter">here</a>.<br>
<img width="1200px" src=""></p>

<h1>Task 1 . IoT . Rotal Router</h1>
<p>Cipher exposes a crucial router at the edge of his network, creating a narrow window for potential intrusions.  It could grant access to the internal network where he stores his operations and compromised systems.<br>

The VM needs 5 minutes to properly boot up.</p>

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/de754c4a-8db2-427d-ab2c-6a0724047e7f"><br>TryHackMe</h6>

<p><em>Answer the question below</em></p>

<p>1.1. What is the flag?<br>
<code></code></p>
<br>

<h2>nikto</h2>

```bash
:~/RoyalRouter# nikto -h xx.xxx.xx.xxx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    xx.xxx.xx.xxx
+ Target Port:        80
+ Start Time:         2025-09-13 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: httpd
+ The anti-clickjacking X-Frame-Options header is not present.
+ All CGI directories 'found', use '-C none' to test none
Use of each() on hash after insertion without resetting hash iterator results in undefined behavior, Perl interpreter: 0x55c1d441a2a0 at /usr/share/perl5/LW2.pm line 947.
Use of each() on hash after insertion without resetting hash iterator results in undefined behavior, Perl interpreter: 0x55c1d441a2a0 at /usr/share/perl5/LW2.pm line 947.
Use of each() on hash after insertion without resetting hash iterator results in undefined behavior, Perl interpreter: 0x55c1d441a2a0 at /usr/share/perl5/LW2.pm line 947.
+ Multiple index files found: index.asp, default.asp
+ /kboard/: KBoard Forum 0.3.0 and prior have a security problem in forum_edit_post.php, forum_post.php and forum_reply.php
+ /lists/admin/: PHPList pre 2.6.4 contains a number of vulnerabilities including remote administrative access, harvesting user info and more. Default login to admin interface is admin/phplist
+ /ssdefs/: Siteseed pre 1.4.2 has 'major' security problems.
+ /sshome/: Siteseed pre 1.4.2 has 'major' security problems.
+ /tiki/: Tiki 1.7.2 and previous allowed restricted Wiki pages to be viewed via a 'URL trick'. Default login/pass could be admin/admin
+ OSVDB-637: /~root/: Allowed to browse root's home directory.
+ /help/: Help directory should not be accessible
+ /cgi.cgi/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /webcgi/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /cgi-914/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /cgi-915/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /bin/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /cgi/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /mpcgi/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /cgi-bin/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /ows-bin/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /cgi-sys/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /cgi-local/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /htbin/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /cgibin/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /cgis/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /scripts/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /cgi-win/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /fcgi-bin/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /cgi-exe/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /cgi-home/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /cgi-perl/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /scgi-bin/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /tsweb/: Microsoft TSAC found. http://www.dslwebserver.com/main/fr_index.html?/main/sbs-Terminal-Services-Advanced-Client-Configuration.html
+ OSVDB-17653: /SiteServer/Admin/commerce/foundation/domain.asp: Displays known domains of which that server is involved.
+ OSVDB-17654: /SiteServer/Admin/commerce/foundation/driver.asp: Displays a list of installed ODBC drivers.
+ OSVDB-17652: /SiteServer/admin/findvserver.asp: Gives a list of installed Site Server components.
+ /SiteServer/Admin/knowledge/dsmgr/default.asp: Used to view current search catalog configurations
+ OSVDB-17656: /SiteServer/Admin/knowledge/dsmgr/users/GroupManager.asp: Used to create, modify, and potentially delete LDAP users and groups.
+ OSVDB-17657: /SiteServer/Admin/knowledge/dsmgr/users/UserManager.asp: Used to create, modify, and potentially delete LDAP users and groups.
+ /prd.i/pgen/: Has MS Merchant Server 1.0
+ /SiteServer/admin/: Site Server components admin. Default account may be 'LDAP_Anonymous', pass is 'LdapPassword_1'. see http://www.wiretrip.net/rfp/p/doc.asp/i1/d69.htm
+ /siteseed/: Siteseed pre 1.4.2 has 'major' security problems.
+ /iisadmin/: Access to /iisadmin should be restricted to localhost or allowed hosts only.
+ /w-agora/: w-agora pre 4.1.4 may allow a remote user to execute arbitrary PHP scripts via URL includes in include/*.php and user/*.php files. Default account is 'admin' but password set during install.
+ /upload.asp: An ASP page that allows attackers to upload files to server
+ /uploadn.asp: An ASP page that allows attackers to upload files to server
+ /uploadx.asp: An ASP page that allows attackers to upload files to server
+ /server/: If port 8000, Macromedia JRun 4 build 61650 remote administration interface is vulnerable to several XSS attacks.
+ /shopa_sessionlist.asp: VP-ASP shopping cart test application is available from the web. This page may give the location of .mdb files which may also be available.
+ /typo3conf/: This may contain sensitive Typo3 files.
+ /webcart/carts/: This may allow attackers to read credit card data. Reconfigure to make this dir not accessible via the web.
+ /webcart/config/: This may allow attackers to read credit card data. Reconfigure to make this dir not accessible via the web.
+ /webcart/orders/: This may allow attackers to read credit card data. Reconfigure to make this dir not accessible via the web.
+ /_mem_bin/auoconfig.asp: Displays the default AUO (LDAP) schema, including host and port.
+ OSVDB-17659: /SiteServer/Admin/knowledge/persmbr/vs.asp: Expose various LDAP service and backend configuration parameters
+ OSVDB-17661: /SiteServer/Admin/knowledge/persmbr/VsLsLpRd.asp: Expose various LDAP service and backend configuration parameters
+ OSVDB-17662: /SiteServer/Admin/knowledge/persmbr/VsPrAuoEd.asp: Expose various LDAP service and backend configuration parameters
+ OSVDB-17660: /SiteServer/Admin/knowledge/persmbr/VsTmPr.asp: Expose various LDAP service and backend configuration parameters
+ /jamdb/: JamDB pre 0.9.2 mp3.php and image.php can allow user to read arbitrary file out of docroot.
+ /securecontrolpanel/: Web Server Control Panel
+ /webmail/: Web based mail package installed.
+ /_cti_pvt/: FrontPage directory found.
+ /upd/: WASD Server can allow directory listings by requesting /upd/directory/. Upgrade to a later version and secure according to the documents on the WASD web site.
+ OSVDB-8450: /3rdparty/phpMyAdmin/db_details_importdocsql.php?submit_show=true&do=import&docpath=../: phpMyAdmin allows directory listings remotely. Upgrade to version 2.5.3 or higher. http://www.securityfocus.com/bid/7963.
+ OSVDB-8450: /phpMyAdmin/db_details_importdocsql.php?submit_show=true&do=import&docpath=../: phpMyAdmin allows directory listings remotely. Upgrade to version 2.5.3 or higher. http://www.securityfocus.com/bid/7963.
+ OSVDB-8450: /3rdparty/phpmyadmin/db_details_importdocsql.php?submit_show=true&do=import&docpath=../: phpMyAdmin allows directory listings remotely. Upgrade to version 2.5.3 or higher. http://www.securityfocus.com/bid/7963.
+ OSVDB-8450: /phpmyadmin/db_details_importdocsql.php?submit_show=true&do=import&docpath=../: phpMyAdmin allows directory listings remotely. Upgrade to version 2.5.3 or higher. http://www.securityfocus.com/bid/7963.
+ OSVDB-8450: /pma/db_details_importdocsql.php?submit_show=true&do=import&docpath=../: phpMyAdmin allows directory listings remotely. Upgrade to version 2.5.3 or higher. http://www.securityfocus.com/bid/7963.
+ OSVDB-6666: /cgi.cgi/hpnst.exe?c=p+i=SrvSystemInfo.html: HP Instant TopTools may be vulnerable to a DoS by requesting hpnst.exe?c=p+i=hpnst.exe multiple times.
+ OSVDB-728: /admentor/adminadmin.asp: Version 2.11 of AdMentor is vulnerable to SQL injection during login, in the style of: ' or =
+ OSVDB-10107: /author.asp: May be FactoSystem CMS, which could include SQL injection problems that could not be tested remotely.
+ OSVDB-4015: /jigsaw/: Jigsaw server may be installed. Versions lower than 2.2.1 are vulnerable to Cross Site Scripting (XSS) in the error page.
+ /ammerum/: Ammerum pre 0.6-1 had several security issues.
+ /ariadne/: Ariadne pre 2.1.2 has several vulnerabilities. The default login/pass to the admin page is admin/muze.
+ /config/: Configuration information may be available remotely.
+ OSVDB-5088: /accounts/getuserdesc.asp: Hosting Controller 2002 administration page is available. This should be protected.
+ /cgi.cgi/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /webcgi/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /cgi-914/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /cgi-915/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /bin/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /cgi/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /mpcgi/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /cgi-bin/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /ows-bin/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /cgi-sys/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /cgi-local/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /htbin/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /cgibin/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /cgis/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /scripts/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /cgi-win/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /fcgi-bin/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /cgi-exe/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /cgi-home/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
...
+ OSVDB-3092: /cgi.cgi/stats_old/: This might be interesting...
+ OSVDB-3092: /webcgi/stats_old/: This might be interesting...
+ OSVDB-3092: /cgi-914/stats_old/: This might be interesting...
+ OSVDB-3092: /cgi-915/stats_old/: This might be interesting...
+ OSVDB-3092: /bin/stats_old/: This might be interesting...
+ OSVDB-3092: /cgi/stats_old/: This might be interesting...
+ OSVDB-3092: /mpcgi/stats_old/: This might be interesting...
+ OSVDB-3092: /cgi-bin/stats_old/: This might be interesting...
+ OSVDB-3092: /ows-bin/stats_old/: This might be interesting...
+ OSVDB-3092: /cgi-sys/stats_old/: This might be interesting...
+ OSVDB-3092: /cgi-local/stats_old/: This might be interesting...
+ OSVDB-3092: /htbin/stats_old/: This might be interesting...
+ OSVDB-3092: /cgibin/stats_old/: This might be interesting...
+ OSVDB-3092: /cgis/stats_old/: This might be interesting...
+ OSVDB-3092: /scripts/stats_old/: This might be interesting...
+ OSVDB-3092: /cgi-win/stats_old/: This might be interesting...
+ OSVDB-3092: /fcgi-bin/stats_old/: This might be interesting...
+ OSVDB-3092: /cgi-exe/stats_old/: This might be interesting...
+ OSVDB-3092: /cgi-home/stats_old/: This might be interesting...
+ OSVDB-3092: /cgi-perl/stats_old/: This might be interesting...
+ OSVDB-3092: /scgi-bin/stats_old/: This might be interesting...
+ OSVDB-3092: /advworks/equipment/catalog_type.asp: This might be interesting...
+ OSVDB-17670: /clocktower/: Site Server sample files.  This might be interesting...
+ OSVDB-17670: /market/: Site Server sample files.  This might be interesting.
+ OSVDB-17670: /mspress30/: Site Server sample files.  This might be interesting...
+ OSVDB-3092: /scripts/postinfo.asp: This might be interesting...
+ OSVDB-3092: /site/iissamples/: This might be interesting...
...
+ /project-admins/: Admin login page/section found.
+ /pureadmin/: Admin login page/section found.
+ /radmind-1/: Admin login page/section found.
+ /radmind/: Admin login page/section found.
+ /rcLogin/: Admin login page/section found.
+ /server_admin_small/: Admin login page/section found.
+ /Server.asp: Admin login page/section found.
+ /ServerAdministrator/: Admin login page/section found.
+ /showlogin/: Admin login page/section found.
+ /simpleLogin/: Admin login page/section found.
+ /smblogin/: Admin login page/section found.
+ /sql-admin/: Admin login page/section found.
+ /ss_vms_admin_sm/: Admin login page/section found.
+ /sshadmin/: Admin login page/section found.
+ /staradmin/: Admin login page/section found.
+ /sub-login/: Admin login page/section found.
+ /Super-Admin/: Admin login page/section found.
+ /support_login/: Admin login page/section found.
+ /sys-admin/: Admin login page/section found.
+ /sysadmin.asp: Admin login page/section found.
+ /sysadmin/: Admin login page/section found.
+ /SysAdmin/: Admin login page/section found.
+ /SysAdmin2/: Admin login page/section found.
+ /sysadmins/: Admin login page/section found.
+ /system_administration/: Admin login page/section found.
+ /system-administration/: Admin login page/section found.
+ /ur-admin.asp: Admin login page/section found.
+ /ur-admin/: Admin login page/section found.
+ /useradmin/: Admin login page/section found.
+ /UserLogin/: Admin login page/section found.
+ /utility_login/: Admin login page/section found.
+ /v2/painel/: Admin login page/section found.
+ /vadmind/: Admin login page/section found.
+ /vmailadmin/: Admin login page/section found.
+ /webadmin.asp: Admin login page/section found.
+ /webmaster/: Admin login page/section found.
+ /websvn/: Admin login page/section found.
+ /wizmysqladmin/: Admin login page/section found.
+ /wp-admin/: Admin login page/section found.
+ /wp-login/: Admin login page/section found.
+ /xlogin/: Admin login page/section found.
+ /yonetici.asp: Admin login page/section found.
+ /yonetim.asp: Admin login page/section found.
+ OSVDB-3092: /test.asp: This might be interesting...
+ /maintenance.asp: This might be interesting...
+ /maint/: This might be interesting...
+ /maint.asp: This might be interesting...
+ 6544 items checked: 474 error(s) and 1071 item(s) reported on remote host
+ End Time:           2025-09-13 xx:xx:xx (GMT1) (184 seconds)
```

<h2>nmap</h2>

```bash
:~/RoyalRouter# nmap -p- -vv TargetIP
...
PORT      STATE SERVICE REASON
22/tcp    open  ssh     syn-ack ttl 64
23/tcp    open  telnet  syn-ack ttl 63
80/tcp    open  http    syn-ack ttl 63
9999/tcp  open  abyss   syn-ack ttl 63
20443/tcp open  unknown syn-ack ttl 63
24433/tcp open  unknown syn-ack ttl 63
28080/tcp open  unknown syn-ack ttl 63
50628/tcp open  unknown syn-ack ttl 63
```

```bash
:~/RoyalRouter# nmap -sC -sV -Pn -T4 -p22,23,80,9999,20443,24433,28080,50628 TargetIP
...
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 8.9p1 Ubuntu 3ubuntu0.13 (Ubuntu Linux; protocol 2.0)
23/tcp    open  tcpwrapped
80/tcp    open  http       DD-WRT milli_httpd
|_http-server-header: httpd
|_http-title: D-LINK CORPORATION, INC | WIRELESS ROUTER | LOGIN
9999/tcp  open  tcpwrapped
20443/tcp open  tcpwrapped
24433/tcp open  tcpwrapped
28080/tcp open  tcpwrapped
50628/tcp open  tcpwrapped
```

<h3>DD-WRT milli-httpd</h3>

<img width="660" height="152" alt="image" src="https://github.com/user-attachments/assets/3ea97c48-a543-4b93-a1e8-3ac45e8faa46" />


<h3>searchploit</h3>

```bash
:~/RoyalRouter# searchsploit DD-WRT
------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                               |  Path
------------------------------------------------------------------------------------------------------------- ---------------------------------
DD-WRT - Site Survey SSID Script Injection                                                                   | multiple/remote/32189.py
DD-WRT 24-preSP2 - Information Disclosure                                                                    | hardware/remote/15842.txt
DD-WRT 45723 - UPNP Buffer Overflow (PoC)                                                                    | hardware/dos/49730.py
DD-WRT HTTP v24-SP1 - Command Injection                                                                      | linux/remote/10030.rb
DD-WRT HTTPd Daemon/Service - Arbitrary Command Execution (Metasploit)                                       | cgi/webapps/16856.rb
DD-WRT HTTPd Daemon/Service - Remote Command Execution                                                       | hardware/remote/9209.txt
DD-WRT v24-sp1 - Cross-Site Reference Forgery                                                                | hardware/remote/7389.html
------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

```bash
:~/RoyalRouter#  searchsploit -m /hardware/remote/9209.txt
  Exploit: DD-WRT HTTPd Daemon/Service - Remote Command Execution
      URL: https://www.exploit-db.com/exploits/9209
     Path: /opt/exploitdb/exploits/hardware/remote/9209.txt
    Codes: OSVDB-57143, CVE-2009-2766, CVE-2009-2765, OSVDB-55990, CVE-2008-6975, OSVDB-55636, CVE-2008-6974
...
:~/RoyalRouter# ls
9209.txt
```

<br>

<img width="976" height="334" alt="image" src="https://github.com/user-attachments/assets/c7d95861-803f-4432-859e-a27e9dca2f99" />


<H3>TargetIP</H3>

<img width="1074" height="351" alt="image" src="https://github.com/user-attachments/assets/83d28eaa-ae14-4826-af9c-d246f85e8971" />



```bash

```

