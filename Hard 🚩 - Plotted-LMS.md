<h1 align="center">Plotted-LMS</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/7ff9ec0c-480d-4725-8056-b206874ec689"><br>
2025, September 17<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>499</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Everything here is plotted!</em>.<br>
Access it <a href="https://tryhackme.com/room/plottedlms">here</a>.<br>
<img width="1200px" src="    "></p>



<h1 align="center">Task 1 . Another brick in the wall</h1>
<p>Happy Huntung!<br><br>
  
Note: This machine may take up to 5 mins to start its services fully.<br><br>

Tip: Enumeration is key!</p>

<p><em>Answer the questions below</em></p>




<br>
<h1 align="center">Port Scanning<a id='1'></a></h1>
<p align="center"><strong>5</strong> open ports</p>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                                                   |
|-------------------:|:---------------------|:--------------------------------------------------------------|
| `22`               |`SSH`                 |OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)  |
| `80`               |`HTTP`                |Apache httpd 2.4.41 ((Ubuntu))                                 |
| `873`              |`rsync`               |Apache httpd 2.4.52 ((Debian))                                 |
| `8820`             |`HTTP`                |Apache httpd 2.4.41 ((Ubuntu))                                 |
| `9020`             |`tambora`             |Apache httpd 2.4.41 ((Ubuntu))                                 |

</p></div><br>

```bash
:~/Plotted-LMS# nmap -sC -sV -Pn -p- -T5 10.201.83.200
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
873/tcp  open  http    Apache httpd 2.4.52 ((Debian))
|_http-server-header: Apache/2.4.52 (Debian)
|_http-title: Apache2 Debian Default Page: It works
8820/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
9020/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
```

<br>
<h1 align="center">Static Host Name Mapping<a id='2'></a></h1>

```bash
10.201.83.200 plotted-lms.thm
```

<br>
<h1 align="center">Directory and File Enumeration<a id='3'></a></h1>

<div align="center"><p>

| **Port**           | *Directories and Files**                                        |
|-------------------:|:----------------------------------------------------------------|
| `80`               |`/index.html`                                                    |
| `873`              |`/rail`, `/index.html`, `/secret.txt`                            |
| `8820`             |`/admin`, `/.git`, `/learn`, `/index.html`                       |
| `9020`             |`/admin`, `/.git`, `/moodle`, `/user.txt`, `/secret.txt`         |

</p></div><br>

<p align="center">80</p>

```bash
:~/Plotted-LMS# gobuster dir -u http://plotted-lms.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -e -k -q -x bak,git,txt,old,html,php
h...
http://plotted-lms.thm/index.html           (Status: 200) [Size: 10918]
```

<p align="center">873</p>

```bash
:~/Plotted-LMS# gobuster dir -u http://plotted-lms.thm:873/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -e -k -q -x bak,git,txt,old,html,php
...
http://plotted-lms.thm:873/index.html           (Status: 200) [Size: 10701]
http://plotted-lms.thm:873/secret.txt           (Status: 200) [Size: 37]
http://plotted-lms.thm:873/rail                 (Status: 301) [Size: 322] [--> http://plotted-lms.thm:873/rail/]
```

<p align="center">8820</p>

```bash
:~/Plotted-LMS# gobuster dir -u http://plotted-lms.thm:8820/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -e -k -q -x bak,git,txt,old,html,php
http://plotted-lms.thm:8820/.git                 (Status: 200) [Size: 105]
...
http://plotted-lms.thm:8820/index.html           (Status: 200) [Size: 10918]
http://plotted-lms.thm:8820/admin                (Status: 200) [Size: 105]
http://plotted-lms.thm:8820/learn                (Status: 301) [Size: 325] [--> http://plotted-lms.thm:8820/learn/]
...
```

<p align="center">9020</p>

```bash
:~/Plotted-LMS# gobuster dir -u http://plotted-lms.thm:9020/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -e -k -q -x bak,git,txt,old,html,php
http://plotted-lms.thm:9020/.git                 (Status: 200) [Size: 105]
http://plotted-lms.thm:9020/user.txt             (Status: 200) [Size: 129]
http://plotted-lms.thm:9020/admin                (Status: 200) [Size: 105]
http://plotted-lms.thm:9020/secret.txt           (Status: 200) [Size: 105]
http://plotted-lms.thm:9020/moodle               (Status: 301) [Size: 326] [--> http://plotted-lms.thm:9020/moodle/]
...
```

```bash
:~/Plotted-LMS# gobuster dir -u http://plotted-lms.thm:9020/moodle/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -q -x js,css,php
http://plotted-lms.thm:9020/moodle/index.php            (Status: 200) [Size: 4717]
http://plotted-lms.thm:9020/moodle/search               (Status: 301) [Size: 333] [--> http://plotted-lms.thm:9020/moodle/search/]
http://plotted-lms.thm:9020/moodle/privacy              (Status: 301) [Size: 334] [--> http://plotted-lms.thm:9020/moodle/privacy/]
http://plotted-lms.thm:9020/moodle/blog                 (Status: 301) [Size: 331] [--> http://plotted-lms.thm:9020/moodle/blog/]
http://plotted-lms.thm:9020/moodle/rss                  (Status: 301) [Size: 330] [--> http://plotted-lms.thm:9020/moodle/rss/]
http://plotted-lms.thm:9020/moodle/login                (Status: 301) [Size: 332] [--> http://plotted-lms.thm:9020/moodle/login/]
http://plotted-lms.thm:9020/moodle/help.php             (Status: 200) [Size: 1872]
http://plotted-lms.thm:9020/moodle/media                (Status: 301) [Size: 332] [--> http://plotted-lms.thm:9020/moodle/media/]
http://plotted-lms.thm:9020/moodle/files                (Status: 301) [Size: 332] [--> http://plotted-lms.thm:9020/moodle/files/]
http://plotted-lms.thm:9020/moodle/user                 (Status: 301) [Size: 331] [--> http://plotted-lms.thm:9020/moodle/user/]
http://plotted-lms.thm:9020/moodle/calendar             (Status: 301) [Size: 335] [--> http://plotted-lms.thm:9020/moodle/calendar/]
http://plotted-lms.thm:9020/moodle/version.php          (Status: 200) [Size: 1634]
http://plotted-lms.thm:9020/moodle/admin                (Status: 301) [Size: 332] [--> http://plotted-lms.thm:9020/moodle/admin/]
http://plotted-lms.thm:9020/moodle/comment              (Status: 301) [Size: 334] [--> http://plotted-lms.thm:9020/moodle/comment/]
http://plotted-lms.thm:9020/moodle/report               (Status: 301) [Size: 333] [--> http://plotted-lms.thm:9020/moodle/report/]
http://plotted-lms.thm:9020/moodle/local                (Status: 301) [Size: 332] [--> http://plotted-lms.thm:9020/moodle/local/]
http://plotted-lms.thm:9020/moodle/pix                  (Status: 301) [Size: 330] [--> http://plotted-lms.thm:9020/moodle/pix/]
http://plotted-lms.thm:9020/moodle/tag                  (Status: 301) [Size: 330] [--> http://plotted-lms.thm:9020/moodle/tag/]
http://plotted-lms.thm:9020/moodle/group                (Status: 301) [Size: 332] [--> http://plotted-lms.thm:9020/moodle/group/]
http://plotted-lms.thm:9020/moodle/my                   (Status: 301) [Size: 329] [--> http://plotted-lms.thm:9020/moodle/my/]
http://plotted-lms.thm:9020/moodle/install.php          (Status: 200) [Size: 26085]
http://plotted-lms.thm:9020/moodle/install              (Status: 301) [Size: 334] [--> http://plotted-lms.thm:9020/moodle/install/]
http://plotted-lms.thm:9020/moodle/lib                  (Status: 301) [Size: 330] [--> http://plotted-lms.thm:9020/moodle/lib/]
http://plotted-lms.thm:9020/moodle/file.php             (Status: 200) [Size: 3871]
http://plotted-lms.thm:9020/moodle/portfolio            (Status: 301) [Size: 336] [--> http://plotted-lms.thm:9020/moodle/portfolio/]
http://plotted-lms.thm:9020/moodle/cache                (Status: 301) [Size: 332] [--> http://plotted-lms.thm:9020/moodle/cache/]
http://plotted-lms.thm:9020/moodle/notes                (Status: 301) [Size: 332] [--> http://plotted-lms.thm:9020/moodle/notes/]
http://plotted-lms.thm:9020/moodle/message              (Status: 301) [Size: 334] [--> http://plotted-lms.thm:9020/moodle/message/]
http://plotted-lms.thm:9020/moodle/lang                 (Status: 301) [Size: 331] [--> http://plotted-lms.thm:9020/moodle/lang/]
http://plotted-lms.thm:9020/moodle/theme                (Status: 301) [Size: 332] [--> http://plotted-lms.thm:9020/moodle/theme/]
http://plotted-lms.thm:9020/moodle/blocks               (Status: 301) [Size: 333] [--> http://plotted-lms.thm:9020/moodle/blocks/]
http://plotted-lms.thm:9020/moodle/question             (Status: 301) [Size: 335] [--> http://plotted-lms.thm:9020/moodle/question/]
http://plotted-lms.thm:9020/moodle/config.php           (Status: 200) [Size: 754]
http://plotted-lms.thm:9020/moodle/backup               (Status: 301) [Size: 333] [--> http://plotted-lms.thm:9020/moodle/backup/]
http://plotted-lms.thm:9020/moodle/rating               (Status: 301) [Size: 333] [--> http://plotted-lms.thm:9020/moodle/rating/]
http://plotted-lms.thm:9020/moodle/filter               (Status: 301) [Size: 333] [--> http://plotted-lms.thm:9020/moodle/filter/]
http://plotted-lms.thm:9020/moodle/mod                  (Status: 301) [Size: 330] [--> http://plotted-lms.thm:9020/moodle/mod/]
http://plotted-lms.thm:9020/moodle/auth                 (Status: 301) [Size: 331] [--> http://plotted-lms.thm:9020/moodle/auth/]
http://plotted-lms.thm:9020/moodle/course               (Status: 301) [Size: 333] [--> http://plotted-lms.thm:9020/moodle/course/]
http://plotted-lms.thm:9020/moodle/error                (Status: 301) [Size: 332] [--> http://plotted-lms.thm:9020/moodle/error/]
http://plotted-lms.thm:9020/moodle/badges               (Status: 301) [Size: 333] [--> http://plotted-lms.thm:9020/moodle/badges/]
http://plotted-lms.thm:9020/moodle/repository           (Status: 301) [Size: 337] [--> http://plotted-lms.thm:9020/moodle/repository/]
http://plotted-lms.thm:9020/moodle/availability         (Status: 301) [Size: 339] [--> http://plotted-lms.thm:9020/moodle/availability/]
http://plotted-lms.thm:9020/moodle/webservice           (Status: 301) [Size: 337] [--> http://plotted-lms.thm:9020/moodle/webservice/]
http://plotted-lms.thm:9020/moodle/favourites           (Status: 301) [Size: 337] [--> http://plotted-lms.thm:9020/moodle/favourites/]
http://plotted-lms.thm:9020/moodle/plagiarism           (Status: 301) [Size: 337] [--> http://plotted-lms.thm:9020/moodle/plagiarism/]
http://plotted-lms.thm:9020/moodle/brokenfile.php       (Status: 200) [Size: 1162]
http://plotted-lms.thm:9020/moodle/competency           (Status: 301) [Size: 337] [--> http://plotted-lms.thm:9020/moodle/competency/]
...
```

<br>
<h1 align="center">Web Interface Inspection<a id='4'></a></h1>

<p align="center">plotted-lms.thm:873/secret.txt</p>

```bash
:~/Plotted-LMS# curl http://plotted-lms.thm:873/secret.txt
Do you really think it is this easy?
```

<p align="center">plotted-lms.thm:8820/.git</p>

```bash
:~/Plotted-LMS# curl http://plotted-lms.thm:8820/.git
VHJ5IEhhcmRlciEKQW55d2F5cyBoZXJlIHlvdSBnbyA6RApodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PWRRdzR3OVdnWGNR
```

```bash
:~/Plotted-LMS# echo 'VHJ5IEhhcmRlciEKQW55d2F5cyBoZXJlIHlvdSBnbyA6RApodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PWRRdzR3OVdnWGNR' | base64 -d
Try Harder!
Anyways here you go :D
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

<p align="center">plotted-lms.thm:9020/user.txt</p>

```bash
:~/Plotted-LMS# curl http://plotted-lms.thm:9020/user.txt
VHJ5IEhhcmRlciEKCldhaXQgZGlkIHlvdSB0cnkgYWRtaW4vYWRtaW4/CklmIG5vdCwgaHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ==
```

<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/e6bb04b4-c257-4a3c-ba68-0235f2917862"><br>

```bash
:~/Plotted-LMS# echo 'VHJ5IEhhcmRlciEKCldhaXQgZGlkIHlvdSB0cnkgYWRtaW4vYWRtaW4/CklmIG5vdCwgaHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ==' | base64 -d
Try Harder!

Wait did you try admin/admin?
If not, https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

<p align="center">plotted-lms.thm:9020/secret.txt</p>

```bash
:~/Plotted-LMS# curl http://plotted-lms.thm:9020/secret.txt
VHJ5IEhhcmRlciEKQW55d2F5cyBoZXJlIHlvdSBnbyA6RApodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PWRRdzR3OVdnWGNR
```

```bash
:~/Plotted-LMS# echo 'VHJ5IEhhcmRlciEKQW55d2F5cyBoZXJlIHlvdSBnbyA6RApodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PWRRdzR3OVdnWGNR' | base64 -d
Try Harder!
Anyways here you go :D
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

<p align="center">plotted-lms.thm:9020/.git</p>

```bash
:~/Plotted-LMS# curl http://plotted-lms.thm:9020/.git
VHJ5IEhhcmRlciEKQW55d2F5cyBoZXJlIHlvdSBnbyA6RApodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PWRRdzR3OVdnWGNR
```
```bash
:~/Plotted-LMS# echo 'VHJ5IEhhcmRlciEKQW55d2F5cyBoZXJlIHlvdSBnbyA6RApodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PWRRdzR3OVdnWGNR' | base64 -d
Try Harder!
Anyways here you go :D
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

<br>
<h1 align="center">Web Vulberability Scanning<a id='5'></a></h1>

```bash
:~/Plotted-LMS# nikto -h http://plotted-lms.thm:873/rail/
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    plotted-lms.thm
+ Target Port:        873
+ Start Time:         2025-10-15 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.52 (Debian)
+ Cookie PHPSESSID created without the httponly flag
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: HEAD, GET, POST, OPTIONS 
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ OSVDB-877: HTTP TRACK method is active, suggesting the host is vulnerable to XST
+ /rail/config.php: PHP Config file may contain database IDs and passwords.
+ OSVDB-5034: /rail/admin/login.php?action=insert&username=test&password=test: phpAuction may allow user admin accounts to be inserted without proper authentication. Attempt to log in with user 'test' password 'test' to verify.
+ OSVDB-3268: /rail/database/: Directory indexing found.
+ OSVDB-3093: /rail/database/: Databases? Really??
+ /rail/admin/login.php: Admin login page/section found.
+ 6544 items checked: 0 error(s) and 10 item(s) reported on remote host
+ End Time:           2025-10-15 xx:xx:xx (GMT1) (9 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~/Plotted-LMS# nikto -h http://plotted-lms.thm:9020/moodle/
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.201.48.234
+ Target Hostname:    plotted-lms.thm
+ Target Port:        9020
+ Start Time:         2025-10-15 00:40:52 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /moodle/, fields: 0x126d 0x5a7fb078f1240 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ /moodle/config.php: PHP Config file may contain database IDs and passwords.
+ OSVDB-3092: /moodle/admin/: This might be interesting...
+ OSVDB-3092: /moodle/auth/: This might be interesting...
+ OSVDB-3092: /moodle/files/: This might be interesting...
+ OSVDB-3092: /moodle/lib/: This might be interesting...
+ OSVDB-3092: /moodle/message/: This might be interesting...
+ OSVDB-3092: /moodle/user/: This might be interesting...
+ OSVDB-3093: /moodle/admin/auth.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /moodle/admin/index.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3092: /moodle/INSTALL.txt: Default file found.
+ OSVDB-3092: /moodle/install.php: install.php file found.
+ OSVDB-3092: /moodle/my/: This might be interesting... potential country code (Malaysia)
+ /moodle/help.php: A help file was found.
+ OSVDB-: /moodle/?-s: PHP allows retrieval of the source code via the -s parameter, and may allow command execution. See http://www.kb.cert.org/vuls/id/520827
+ 6544 items checked: 0 error(s) and 17 item(s) reported on remote host
+ End Time:           2025-10-15 00:41:17 (GMT1) (25 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```



hrqvr0f4bmeu97be5t06rqchj9

<p align="center">http://plotted-lms.thm:9020/moodle/config.php</p>


```bash
<html><head></head><body>dbtype    = 'mysqli';
$CFG-&gt;dblibrary = 'native';
$CFG-&gt;dbhost    = 'localhost';
$CFG-&gt;dbname    = 'moodle';
$CFG-&gt;dbuser    = 'moodle_user';
$CFG-&gt;dbpass    = 'MoodleItIs@123';
$CFG-&gt;prefix    = 'mdl_';
$CFG-&gt;dboptions = array (
  'dbpersist' =&gt; 0,
  'dbport' =&gt; '',
  'dbsocket' =&gt; '',
  'dbcollation' =&gt; 'utf8mb4_0900_ai_ci',
);

$CFG-&gt;wwwroot   = "http://".$_SERVER["HTTP_HOST"]."/moodle";
$CFG-&gt;dataroot  = '/var/www/uploadedfiles';
$CFG-&gt;admin     = 'admin';

$CFG-&gt;directorypermissions = 0777;

require_once(__DIR__ . '/lib/setup.php');

// There is no php closing tag in this file,
// it is intentional because it prevents trailing whitespace problems!
</body></html>
```

<p align="center">http://plotted-lms.thm:9020/moodle/auth.php</p>

```bash
<?php

/**
 * Allows admin to edit all auth plugin settings.
 *
 * JH: copied and Hax0rd from admin/enrol.php and admin/filters.php
 *
 */

require_once('../config.php');
require_once($CFG->libdir.'/adminlib.php');
require_once($CFG->libdir.'/tablelib.php');

require_admin();

$returnurl = new moodle_url('/admin/settings.php', array('section'=>'manageauths'));

$PAGE->set_url($returnurl);

$action = optional_param('action', '', PARAM_ALPHANUMEXT);
$auth   = optional_param('auth', '', PARAM_PLUGIN);

get_enabled_auth_plugins(true); // fix the list of enabled auths
if (empty($CFG->auth)) {
    $authsenabled = array();
} else {
    $authsenabled = explode(',', $CFG->auth);
}

if (!empty($auth) and !exists_auth_plugin($auth)) {
    print_error('pluginnotinstalled', 'auth', $returnurl, $auth);
}

////////////////////////////////////////////////////////////////////////////////
// process actions

if (!confirm_sesskey()) {
    redirect($returnurl);
}

switch ($action) {
    case 'disable':
        // remove from enabled list
        $key = array_search($auth, $authsenabled);
        if ($key !== false) {
            unset($authsenabled[$key]);
            set_config('auth', implode(',', $authsenabled));
        }

        if ($auth == $CFG->registerauth) {
            set_config('registerauth', '');
        }
        \core\session\manager::gc(); // Remove stale sessions.
        core_plugin_manager::reset_caches();
        break;

    case 'enable':
        // add to enabled list
        if (!in_array($auth, $authsenabled)) {
            $authsenabled[] = $auth;
            $authsenabled = array_unique($authsenabled);
            set_config('auth', implode(',', $authsenabled));
        }
        \core\session\manager::gc(); // Remove stale sessions.
        core_plugin_manager::reset_caches();
        break;

    case 'down':
        $key = array_search($auth, $authsenabled);
        // check auth plugin is valid
        if ($key === false) {
            print_error('pluginnotenabled', 'auth', $returnurl, $auth);
        }
        // move down the list
        if ($key < (count($authsenabled) - 1)) {
            $fsave = $authsenabled[$key];
            $authsenabled[$key] = $authsenabled[$key + 1];
            $authsenabled[$key + 1] = $fsave;
            set_config('auth', implode(',', $authsenabled));
        }
        break;

    case 'up':
        $key = array_search($auth, $authsenabled);
        // check auth is valid
        if ($key === false) {
            print_error('pluginnotenabled', 'auth', $returnurl, $auth);
        }
        // move up the list
        if ($key >= 1) {
            $fsave = $authsenabled[$key];
            $authsenabled[$key] = $authsenabled[$key - 1];
            $authsenabled[$key - 1] = $fsave;
            set_config('auth', implode(',', $authsenabled));
        }
        break;

    default:
        break;
}

redirect($returnurl);
```


<p align="center">http://plotted-lms.thm:873/rail/database</p>

<img width="1127" height="290" alt="image" src="https://github.com/user-attachments/assets/dffdf020-2d5f-4509-adf2-c6110f57f034" />



<p align="center">http://plotted-lms.thm:873/rail/admin/login.php</p>

<img width="1125" height="678" alt="image" src="https://github.com/user-attachments/assets/d4bf9cce-d198-41f2-9280-e8a21cf8bb96" />

download database

<img width="1122" height="141" alt="image" src="https://github.com/user-attachments/assets/d600d457-5d85-4506-bf76-ffc253a0da98" />

Open database


pass123456

<img width="1127" height="173" alt="image" src="https://github.com/user-attachments/assets/1c018e59-057a-4a7d-af4e-1bec33f2709b" />

200 OK

<img width="1020" height="339" alt="image" src="https://github.com/user-attachments/assets/efc2142b-3408-402f-8698-aadc47e92836" />


```bash
:~/Plotted-LMS# curl -s http://plotted-lms.thm:873/rail/admin/login.php?action=insert&username=lala&password=123456 | html2text -utf8
...
     <!-- jQuery -->
    <script src="http://plotted-lms.thm:873/rail/plugins/jquery/jquery.min.js"></script>
    <!-- jQuery UI 1.11.4 -->
    <script src="http://plotted-lms.thm:873/rail/plugins/jquery-ui/jquery-ui.min.js"></script>
    <!-- SweetAlert2 -->
    <script src="http://plotted-lms.thm:873/rail/plugins/sweetalert2/sweetalert2.min.js"></script>
    <!-- Toastr -->
    <script src="http://plotted-lms.thm:873/rail/plugins/toastr/toastr.min.js"></script>
    <script>
...
[2]   Done                    curl -s http://plotted-lms.thm:873/rail/admin/login.php?action=insert
[3]-  Done                    username=lala
```



</html>[2]   Done                    curl http://plotted-lms.thm:873/rail/admin/login.php?action=insert
[3]-  Done                    username=lili


<h4 align="center">80</h4>

<img width="1057" height="325" alt="image" src="https://github.com/user-attachments/assets/2c5099c7-030a-42b3-9f11-fb38ea939005" />

<h4 align="center">873</h4>

<img width="1052" height="371" alt="image" src="https://github.com/user-attachments/assets/62004bdf-9062-4dc0-b887-da503c22e97e" />

<h4 align="center">8820</h4>

<img width="1056" height="348" alt="image" src="https://github.com/user-attachments/assets/097ae029-6019-410f-a51c-4c4cb432d58d" />

<h4 align="center">9020</h4>

<img width="1061" height="296" alt="image" src="https://github.com/user-attachments/assets/db816776-1950-4ede-807f-34b0c42e8de7" />



```bash
:~/PlottedLMS# gobuster dir -u http://plottedlms.thm:873/rail/ -w /usr/share/dirb/wordlists/common.txt -t 60 -q -e -k
http://plottedlms.thm:873/rail/admin                (Status: 301) [Size: 326] [--> http://plottedlms.thm:873/rail/admin/]
http://plottedlms.thm:873/rail/build                (Status: 301) [Size: 326] [--> http://plottedlms.thm:873/rail/build/]
http://plottedlms.thm:873/rail/classes              (Status: 301) [Size: 328] [--> http://plottedlms.thm:873/rail/classes/]
http://plottedlms.thm:873/rail/database             (Status: 301) [Size: 329] [--> http://plottedlms.thm:873/rail/database/]
http://plottedlms.thm:873/rail/dist                 (Status: 301) [Size: 325] [--> http://plottedlms.thm:873/rail/dist/]
http://plottedlms.thm:873/rail/inc                  (Status: 301) [Size: 324] [--> http://plottedlms.thm:873/rail/inc/]
http://plottedlms.thm:873/rail/libs                 (Status: 301) [Size: 325] [--> http://plottedlms.thm:873/rail/libs/]
http://plottedlms.thm:873/rail/index.php            (Status: 200) [Size: 21076]
http://plottedlms.thm:873/rail/plugins              (Status: 301) [Size: 328] [--> http://plottedlms.thm:873/rail/plugins/]
http://plottedlms.thm:873/rail/.htaccess            (Status: 403) [Size: 32]
http://plottedlms.thm:873/rail/.htpasswd            (Status: 403) [Size: 32]
http://plottedlms.thm:873/rail/.hta                 (Status: 403) [Size: 32]
http://plottedlms.thm:873/rail/uploads              (Status: 301) [Size: 328] [--> http://plottedlms.thm:873/rail/uploads/]
```

```bash
:~/PlottedLMS# gobuster dir -u http://plottedlms.thm:873/rail/admin/ -w /usr/share/dirb/wordlists/common.txt -t 60 -q -e -k
http://plottedlms.thm:873/rail/admin/.htaccess            (Status: 403) [Size: 32]
http://plottedlms.thm:873/rail/admin/.htpasswd            (Status: 403) [Size: 32]
http://plottedlms.thm:873/rail/admin/.hta                 (Status: 403) [Size: 32]
http://plottedlms.thm:873/rail/admin/inc                  (Status: 301) [Size: 330] [--> http://plottedlms.thm:873/rail/admin/inc/]
http://plottedlms.thm:873/rail/admin/inquiries            (Status: 301) [Size: 336] [--> http://plottedlms.thm:873/rail/admin/inquiries/]
http://plottedlms.thm:873/rail/admin/index.php            (Status: 200) [Size: 23528]
http://plottedlms.thm:873/rail/admin/reservations         (Status: 301) [Size: 339] [--> http://plottedlms.thm:873/rail/admin/reservations/]
http://plottedlms.thm:873/rail/admin/user                 (Status: 301) [Size: 331] [--> http://plottedlms.thm:873/rail/admin/user/]
```

```bash
:~/PlottedLMS# gobuster dir -u http://plottedlms.thm:873/rail/admin/ -w /usr/share/dirb/wordlists/common.txt -t 60 -q -e -k
http://plottedlms.thm:873/rail/admin/.htaccess            (Status: 403) [Size: 32]
http://plottedlms.thm:873/rail/admin/.htpasswd            (Status: 403) [Size: 32]
http://plottedlms.thm:873/rail/admin/.hta                 (Status: 403) [Size: 32]
http://plottedlms.thm:873/rail/admin/inc                  (Status: 301) [Size: 330] [--> http://plottedlms.thm:873/rail/admin/inc/]
http://plottedlms.thm:873/rail/admin/inquiries            (Status: 301) [Size: 336] [--> http://plottedlms.thm:873/rail/admin/inquiries/]
http://plottedlms.thm:873/rail/admin/index.php            (Status: 200) [Size: 23528]
http://plottedlms.thm:873/rail/admin/reservations         (Status: 301) [Size: 339] [--> http://plottedlms.thm:873/rail/admin/reservations/]
http://plottedlms.thm:873/rail/admin/user                 (Status: 301) [Size: 331] [--> http://plottedlms.thm:873/rail/admin/user/]
```


```bash
:~/PlottedLMS# gobuster dir -u http://plottedlms.thm:8820/learn/ -w /usr/share/dirb/wordlists/common.txt -t 60 -q -e -k -x php,txt,html
http://plottedlms.thm:8820/learn/.html                (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/.htaccess.html       (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/.htpasswd            (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/.htaccess.txt        (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/.htaccess.php        (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/.htaccess            (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/.hta.php             (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/.hta.html            (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/.hta.txt             (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/.hta                 (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/.htpasswd.html       (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/.htpasswd.txt        (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/admin                (Status: 301) [Size: 329] [--> http://plottedlms.thm:8820/learn/admin/]
http://plottedlms.thm:8820/learn/about.php            (Status: 200) [Size: 1533]
http://plottedlms.thm:8820/learn/announcements.php    (Status: 200) [Size: 5274]
http://plottedlms.thm:8820/learn/.htpasswd.php        (Status: 403) [Size: 104]
http://plottedlms.thm:8820/learn/count.php            (Status: 200) [Size: 1426]
http://plottedlms.thm:8820/learn/db                   (Status: 301) [Size: 326] [--> http://plottedlms.thm:8820/learn/db/]
http://plottedlms.thm:8820/learn/directories.php      (Status: 200) [Size: 588]
http://plottedlms.thm:8820/learn/footer.php           (Status: 200) [Size: 77]
http://plottedlms.thm:8820/learn/header.php           (Status: 200) [Size: 1738]
http://plottedlms.thm:8820/learn/history.php          (Status: 200) [Size: 1282]
http://plottedlms.thm:8820/learn/index.php            (Status: 200) [Size: 769]
http://plottedlms.thm:8820/learn/index.php            (Status: 200) [Size: 769]
http://plottedlms.thm:8820/learn/link.php             (Status: 200) [Size: 1558]
http://plottedlms.thm:8820/learn/login.php            (Status: 200) [Size: 952]
http://plottedlms.thm:8820/learn/logout.php           (Status: 200) [Size: 78]
http://plottedlms.thm:8820/learn/progress.php         (Status: 200) [Size: 6675]
http://plottedlms.thm:8820/learn/read.php             (Status: 200) [Size: 417]
http://plottedlms.thm:8820/learn/reply.php            (Status: 200) [Size: 649]
http://plottedlms.thm:8820/learn/script.php           (Status: 200) [Size: 4157]
http://plottedlms.thm:8820/learn/session.php          (Status: 200) [Size: 258]
http://plottedlms.thm:8820/learn/sitemap.xml          (Status: 200) [Size: 535]
```


<h4 align="center">9020</h4>

```bash
:~/PlottedLMS# gobuster dir -u http://plotted.thm:9020 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://plotted.thm:9020
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/user.txt             (Status: 200) [Size: 129]
/admin                (Status: 200) [Size: 105]
/secret.txt           (Status: 200) [Size: 105]
/moodle               (Status: 301) [Size: 318] [--> http://plotted.thm:9020/moodle/]
/server-status        (Status: 403) [Size: 104]
/credentials          (Status: 200) [Size: 105]
Progress: 654825 / 654828 (100.00%)
```


user.txt

<img width="1170" height="161" alt="image" src="https://github.com/user-attachments/assets/fb821c7d-1175-44ae-8678-ef695275cb9d" />

```bash
:~/PlottedLMS# echo 'VHJ5IEhhcmRlciEKCldhaXQgZGlkIHlvdSB0cnkgYWRtaW4vYWRtaW4/CklmIG5vdCwgaHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ==' | base64 -d
Try Harder!

Wait did you try admin/admin?
If not, https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

<h4>secret.txt</h4>

<img width="1177" height="154" alt="image" src="https://github.com/user-attachments/assets/9323a98e-0c93-4168-805c-bc35e9c1a71f" />

```bash
VHJ5IEhhcmRlciEKQW55d2F5cyBoZXJlIHlvdSBnbyA6RApodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PWRRdzR3OVdnWGNR

```bash
:~/PlottedLMS# echo 'VHJ5IEhhcmRlciEKQW55d2F5cyBoZXJlIHlvdSBnbyA6RApodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PWRRdzR3OVdnWGNR' |  base64 -d
Try Harder!
Anyways here you go :D
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

/credentials

<img width="1171" height="152" alt="image" src="https://github.com/user-attachments/assets/d90ea919-86cb-4008-a29f-8e402c2cc259" />

```bash
~/PlottedLMS# echo 'VHJ5IEhhcmRlciEKQW55d2F5cyBoZXJlIHlvdSBnbyA6RApodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PWRRdzR3OVdnWGNR' | base64 -d
Try Harder!
Anyways here you go :D
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

```bash
:~/PlottedLMS# gobuster dir -u http://plottedlms.thm:9020/moodle/ -w /usr/share/dirb/wordlists/common.txt -t 60 -q -e -k -x php,txt,html
http://plottedlms.thm:9020/moodle/.hta.php             (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/.htpasswd.php        (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/.htaccess.php        (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/.htaccess            (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/.htpasswd.txt        (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/.htpasswd            (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/.htaccess.txt        (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/.htaccess.html       (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/.htpasswd.html       (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/admin                (Status: 301) [Size: 330] [--> http://plottedlms.thm:9020/moodle/admin/]
http://plottedlms.thm:9020/moodle/analytics            (Status: 301) [Size: 334] [--> http://plottedlms.thm:9020/moodle/analytics/]
http://plottedlms.thm:9020/moodle/.html                (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/auth                 (Status: 301) [Size: 329] [--> http://plottedlms.thm:9020/moodle/auth/]
http://plottedlms.thm:9020/moodle/.hta.html            (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/.hta                 (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/backup               (Status: 301) [Size: 331] [--> http://plottedlms.thm:9020/moodle/backup/]
http://plottedlms.thm:9020/moodle/.hta.txt             (Status: 403) [Size: 104]
http://plottedlms.thm:9020/moodle/blocks               (Status: 301) [Size: 331] [--> http://plottedlms.thm:9020/moodle/blocks/]
http://plottedlms.thm:9020/moodle/blog                 (Status: 301) [Size: 329] [--> http://plottedlms.thm:9020/moodle/blog/]
http://plottedlms.thm:9020/moodle/calendar             (Status: 301) [Size: 333] [--> http://plottedlms.thm:9020/moodle/calendar/]
http://plottedlms.thm:9020/moodle/cache                (Status: 301) [Size: 330] [--> http://plottedlms.thm:9020/moodle/cache/]
http://plottedlms.thm:9020/moodle/comment              (Status: 301) [Size: 332] [--> http://plottedlms.thm:9020/moodle/comment/]
http://plottedlms.thm:9020/moodle/course               (Status: 301) [Size: 331] [--> http://plottedlms.thm:9020/moodle/course/]
http://plottedlms.thm:9020/moodle/config.php           (Status: 200) [Size: 754]
http://plottedlms.thm:9020/moodle/error                (Status: 301) [Size: 330] [--> http://plottedlms.thm:9020/moodle/error/]
http://plottedlms.thm:9020/moodle/files                (Status: 301) [Size: 330] [--> http://plottedlms.thm:9020/moodle/files/]
http://plottedlms.thm:9020/moodle/file.php             (Status: 200) [Size: 3871]
http://plottedlms.thm:9020/moodle/filter               (Status: 301) [Size: 331] [--> http://plottedlms.thm:9020/moodle/filter/]
http://plottedlms.thm:9020/moodle/group                (Status: 301) [Size: 330] [--> http://plottedlms.thm:9020/moodle/group/]
http://plottedlms.thm:9020/moodle/help.php             (Status: 200) [Size: 1872]
http://plottedlms.thm:9020/moodle/index.php            (Status: 200) [Size: 4717]
http://plottedlms.thm:9020/moodle/index.php            (Status: 200) [Size: 4717]
http://plottedlms.thm:9020/moodle/install              (Status: 301) [Size: 332] [--> http://plottedlms.thm:9020/moodle/install/]
http://plottedlms.thm:9020/moodle/install.php          (Status: 200) [Size: 26085]
http://plottedlms.thm:9020/moodle/lang                 (Status: 301) [Size: 329] [--> http://plottedlms.thm:9020/moodle/lang/]
http://plottedlms.thm:9020/moodle/lib                  (Status: 301) [Size: 328] [--> http://plottedlms.thm:9020/moodle/lib/]
http://plottedlms.thm:9020/moodle/local                (Status: 301) [Size: 330] [--> http://plottedlms.thm:9020/moodle/local/]
http://plottedlms.thm:9020/moodle/login                (Status: 301) [Size: 330] [--> http://plottedlms.thm:9020/moodle/login/]
http://plottedlms.thm:9020/moodle/media                (Status: 301) [Size: 330] [--> http://plottedlms.thm:9020/moodle/media/]
http://plottedlms.thm:9020/moodle/message              (Status: 301) [Size: 332] [--> http://plottedlms.thm:9020/moodle/message/]
http://plottedlms.thm:9020/moodle/mod                  (Status: 301) [Size: 328] [--> http://plottedlms.thm:9020/moodle/mod/]
http://plottedlms.thm:9020/moodle/my                   (Status: 301) [Size: 327] [--> http://plottedlms.thm:9020/moodle/my/]
http://plottedlms.thm:9020/moodle/notes                (Status: 301) [Size: 330] [--> http://plottedlms.thm:9020/moodle/notes/]
http://plottedlms.thm:9020/moodle/pix                  (Status: 301) [Size: 328] [--> http://plottedlms.thm:9020/moodle/pix/]
http://plottedlms.thm:9020/moodle/portfolio            (Status: 301) [Size: 334] [--> http://plottedlms.thm:9020/moodle/portfolio/]
http://plottedlms.thm:9020/moodle/privacy              (Status: 301) [Size: 332] [--> http://plottedlms.thm:9020/moodle/privacy/]
http://plottedlms.thm:9020/moodle/question             (Status: 301) [Size: 333] [--> http://plottedlms.thm:9020/moodle/question/]
http://plottedlms.thm:9020/moodle/rating               (Status: 301) [Size: 331] [--> http://plottedlms.thm:9020/moodle/rating/]
http://plottedlms.thm:9020/moodle/README.txt           (Status: 200) [Size: 1176]
http://plottedlms.thm:9020/moodle/report               (Status: 301) [Size: 331] [--> http://plottedlms.thm:9020/moodle/report/]
http://plottedlms.thm:9020/moodle/repository           (Status: 301) [Size: 335] [--> http://plottedlms.thm:9020/moodle/repository/]
http://plottedlms.thm:9020/moodle/rss                  (Status: 301) [Size: 328] [--> http://plottedlms.thm:9020/moodle/rss/]
http://plottedlms.thm:9020/moodle/search               (Status: 301) [Size: 331] [--> http://plottedlms.thm:9020/moodle/search/]
http://plottedlms.thm:9020/moodle/tag                  (Status: 301) [Size: 328] [--> http://plottedlms.thm:9020/moodle/tag/]
http://plottedlms.thm:9020/moodle/theme                (Status: 301) [Size: 330] [--> http://plottedlms.thm:9020/moodle/theme/]
http://plottedlms.thm:9020/moodle/user                 (Status: 301) [Size: 329] [--> http://plottedlms.thm:9020/moodle/user/]
http://plottedlms.thm:9020/moodle/version.php          (Status: 200) [Size: 1634]
http://plottedlms.thm:9020/moodle/webservice           (Status: 301) [Size: 335] [--> http://plottedlms.thm:9020/moodle/webservice/]
```


plottedlms.thm:837/rail

<img width="1162" height="476" alt="image" src="https://github.com/user-attachments/assets/57a53dc3-7b5f-4fbc-a119-61ca5378cfdd" />

<img width="1166" height="588" alt="image" src="https://github.com/user-attachments/assets/2ae41cc3-37ea-4ad3-9a04-5212a0fe4551" />


plottedlms.thm:837/rail/admin/login.php

<img width="1167" height="645" alt="image" src="https://github.com/user-attachments/assets/1aba0de1-bd35-43a8-ab07-01ddd9ce36aa" />








plottedlms.thm:9020/secret.txt


<img width="1058" height="184" alt="image" src="https://github.com/user-attachments/assets/b762b1a9-be36-440a-8bc7-2d5ed3ee51da" />

<br>

<img width="1226" height="165" alt="image" src="https://github.com/user-attachments/assets/b9d6499a-2261-4d78-be3e-e17a586fe131" />


plottedlms.thm:9020/moodle

<img width="1173" height="443" alt="image" src="https://github.com/user-attachments/assets/f9c6f7e2-d9b1-40b7-8cfb-03d0eb76d726" />


/moodle/README.txt

<img width="1167" height="335" alt="image" src="https://github.com/user-attachments/assets/bb91722a-76d1-4ac1-b8aa-f9934b4719eb" />



<h2 align="center">nikto</h2>
<h4 align="center">80</h4>

```bash
:~# nikto -h xx.xxx.xxx.xx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xxx.xx
+ Target Hostname:    xx.xxx.xxx.xx
+ Target Port:        80
+ Start Time:         2025-09-17 xx:xx:xx (GMT1)
--------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x5d6d5c41143e4 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
+ End Time:           2025-09-17 xx:xx:xx (GMT1) (29 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h4 align="center">873</h4>

```bash
:~/PlottedLMS# nikto -h 10.201.104.98:873
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.201.104.98
+ Target Hostname:    10.201.104.98
+ Target Port:        873
+ Start Time:         2025-09-17 21:06:02 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.52 (Debian)
+ Server leaks inodes via ETags, header found with file /, fields: 0x29cd 0x5d707cdcc1440 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
+ End Time:           2025-09-17 21:06:18 (GMT1) (16 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h4 align="center">8820</h4>

```bash
:~/PlottedLMS# nikto -h xx.xxx.xxx.xx 8820
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.201.104.98
+ Target Hostname:    10.201.104.98
+ Target Port:        8820
+ Start Time:         2025-09-17 21:05:28 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x5d6d78ef5e021 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
+ End Time:           2025-09-17 21:05:42 (GMT1) (14 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h4 align="center">9020</h4>

```bash
:~/PlottedLMS# nikto -h 10.201.104.98:9020
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.201.104.98
+ Target Hostname:    10.201.104.98
+ Target Port:        9020
+ Start Time:         2025-09-17 21:06:51 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x5d6d7bed2719e 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
+ End Time:           2025-09-17 21:07:05 (GMT1) (14 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

<h2 align="center">/etc/hosts</h2>

```bash

```

<h2 align="center">nmap</h2>

<p>

- 21 : FTP<br>
- 22 : SSH<br>
- 80 : HTTP : Apache httpd 2.4.41 ((Ubuntu))<br>
- 5900 : mysql : MySQL 5.5.5-10.3.31-MariaDB-0+deb10u1<br>
- 8890 : HTTP : Apache httpd 2.4.41 ((Ubuntu))</p>

```bash
:~# nmap -sT -p- -T4 xx.xxx.xx.xxx
...
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
80/tcp   open  http
5900/tcp open  vnc
8890/tcp open  ddi-tcp-3
```

```bash
:~# nmap -sC -sV -p- -T4 xx.xxx.xx.xxx
...
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:xx.xxx.xx.xxx
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
5900/tcp open  mysql   MySQL 5.5.5-10.3.31-MariaDB-0+deb10u1
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.31-MariaDB-0+deb10u1
|   Thread ID: 44
|   Capabilities flags: 63486
|   Some Capabilities: Support41Auth, Speaks41ProtocolOld, IgnoreSigpipes, SupportsTransactions, ConnectWithDatabase, DontAllowDatabaseTableColumn, ODBCClient, FoundRows, InteractiveClient, SupportsCompression, LongColumnFlag, SupportsLoadDataLocal, IgnoreSpaceBeforeParenthesis, Speaks41ProtocolNew, SupportsMultipleResults, SupportsMultipleStatments, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: :-ry(Yi&zX(]~#/b!zel
|_  Auth Plugin Name: mysql_native_password
8890/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
```

<h2 align="center">gobuster</h2>

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 60
...
/admin                (Status: 200) [Size: 33]
/shadow               (Status: 200) [Size: 61]
/passwd               (Status: 200) [Size: 61]
/server-status        (Status: 403) [Size: 278]
```

```bash
:~# gobuster dir --url http://xx.xxx.xx.xxx/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt -t 60
...
/index.html           (Status: 200) [Size: 10918]
/admin                (Status: 200) [Size: 33]
/.php                 (Status: 403) [Size: 278]
/.html                (Status: 403) [Size: 278]
/shadow               (Status: 200) [Size: 61]
/passwd               (Status: 200) [Size: 61]
/server-status        (Status: 403) [Size: 278]
```

<br>

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx:8890/ -w /usr/share/dirb/wordlists/common.txt
...
/.hta                 (Status: 403) [Size: 280]
/.htaccess            (Status: 403) [Size: 280]
/.htpasswd            (Status: 403) [Size: 280]
/index.html           (Status: 200) [Size: 10918]
/portal               (Status: 301) [Size: 322] [--> http://xx.xxx.xx.xxx:8890/portal/]
/server-status        (Status: 403) [Size: 280]
```

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx:8890/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 60
...
/portal               (Status: 301) [Size: 322] [--> http://xx.xxx.xx.xxx:8890/portal/]
/80                   (Status: 301) [Size: 318] [--> http://xx.xxx.xx.xxx:8890/80/]
/server-status        (Status: 403) [Size: 280]
Progress: 218275 / 218276 (100.00%)
```

```bash
:~# gobuster dir --url http://xx.xxx.xx.xxx:8890/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt -t 60
...
/index.html           (Status: 200) [Size: 10918]
/.php                 (Status: 403) [Size: 280]
/.html                (Status: 403) [Size: 280]
/portal               (Status: 301) [Size: 322] [--> http://xx.xxx.xx.xxx:8890/portal/]
/80                   (Status: 301) [Size: 318] [--> http://xx.xxx.xx.xxx:8890/80/]
/server-status        (Status: 403) [Size: 280]
```

```bash
:~# gobuster dir --url http://xx.xxx.xx.xxx:8890/portal/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt -t 60
===============================================================
Gobuster v3.6
...
===============================================================
/.html                (Status: 403) [Size: 280]
/index.php            (Status: 302) [Size: 0] [--> interface/login/login.php?site=default]
/.php                 (Status: 403) [Size: 280]
/templates            (Status: 301) [Size: 332] [--> http://xx.xxx.xx.xxx:8890/portal/templates/]
/services             (Status: 301) [Size: 331] [--> http://xx.xxx.xx.xxx:8890/portal/services/]
/modules              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/modules/]
/common               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/common/]
/library              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/library/]
/public               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/public/]
/version.php          (Status: 200) [Size: 0]
/admin.php            (Status: 200) [Size: 1124]
/portal               (Status: 403) [Size: 280]
/tests                (Status: 301) [Size: 328] [--> http://xx.xxx.xx.xxx:8890/portal/tests/]
/sites                (Status: 301) [Size: 328] [--> http://xx.xxx.xx.xxx:8890/portal/sites/]
/images               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/images/]
/custom               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/custom/]
/contrib              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/contrib/]
/interface            (Status: 301) [Size: 332] [--> http://xx.xxx.xx.xxx:8890/portal/interface/]
/vendor               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/vendor/]
/config               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/config/]
/setup.php            (Status: 200) [Size: 1214]
/Documentation        (Status: 301) [Size: 336] [--> http://xx.xxx.xx.xxx:8890/portal/Documentation/]
/sql                  (Status: 301) [Size: 326] [--> http://xx.xxx.xx.xxx:8890/portal/sql/]
/controller.php       (Status: 403) [Size: 280]
/LICENSE              (Status: 200) [Size: 35147]
/ci                   (Status: 301) [Size: 325] [--> http://xx.xxx.xx.xxx:8890/portal/ci/]
/cloud                (Status: 301) [Size: 328] [--> http://xx.xxx.xx.xxx:8890/portal/cloud/]
/ccr                  (Status: 301) [Size: 326] [--> http://xx.xxx.xx.xxx:8890/portal/ccr/]
/patients             (Status: 301) [Size: 331] [--> http://xx.xxx.xx.xxx:8890/portal/patients/]
/repositories         (Status: 301) [Size: 335] [--> http://xx.xxx.xx.xxx:8890/portal/repositories/]
/myportal             (Status: 301) [Size: 331] [--> http://xx.xxx.xx.xxx:8890/portal/myportal/]
/entities             (Status: 301) [Size: 331] [--> http://xx.xxx.xx.xxx:8890/portal/entities/]
/controllers          (Status: 301) [Size: 334]
```

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx:8890/portal/ -w /usr/share/dirb/wordlists/common.txt
...
/.hta                 (Status: 403) [Size: 280]
/.htaccess            (Status: 403) [Size: 280]
/.htpasswd            (Status: 403) [Size: 280]
/common               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/common/]
/config               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/config/]
/contrib              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/contrib/]
/controllers          (Status: 301) [Size: 334] [--> http://xx.xxx.xx.xxx:8890/portal/controllers/]
/custom               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/custom/]
/images               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/images/]
/index.php            (Status: 302) [Size: 0] [--> interface/login/login.php?site=default]
/interface            (Status: 301) [Size: 332] [--> http://xx.xxx.xx.xxx:8890/portal/interface/]
/LICENSE              (Status: 200) [Size: 35147]
/admin.php            (Status: 200) [Size: 937]
/services             (Status: 301) [Size: 331] [--> http://xx.xxx.xx.xxx:8890/portal/services/]
/modules              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/modules/]
/public               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/public/]
/portal               (Status: 403) [Size: 280]
/library              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/library/]
/sites                (Status: 301) [Size: 328] [--> http://xx.xxx.xx.xxx:8890/portal/sites/]
/sql                  (Status: 301) [Size: 326] [--> http://xx.xxx.xx.xxx:8890/portal/sql/]
/templates            (Status: 301) [Size: 332] [--> http://xx.xxx.xx.xxx:8890/portal/templates/]
/tests                (Status: 301) [Size: 328] [--> http://xx.xxx.xx.xxx:8890/portal/tests/]
/vendor               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/vendor/]
```


<h2 align="center">FTP</h2>

```bash
:~# ftp xx.xxx.xx.xxx
Connected to xx.xxx.xx.xxx.
220 (vsFTPd 3.0.3)
Name (xx.xxx.xx.xxx:root): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
dr-xr-xr-x    3 ftp      ftp          4096 Oct 17  2021 .
drwxr-xr-x    3 ftp      ftp          4096 Oct 17  2021 .-
dr-xr-xr-x    3 ftp      ftp          4096 Oct 17  2021 ..
226 Directory send OK.
ftp> cd .
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
dr-xr-xr-x    3 ftp      ftp          4096 Oct 17  2021 .
drwxr-xr-x    3 ftp      ftp          4096 Oct 17  2021 .-
dr-xr-xr-x    3 ftp      ftp          4096 Oct 17  2021 ..
226 Directory send OK.
ftp> cd .-
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Oct 17  2021 .
dr-xr-xr-x    3 ftp      ftp          4096 Oct 17  2021 ..
drwxr-xr-x    2 ftp      ftp          4096 Oct 17  2021 ...
226 Directory send OK.
ftp> cd ...
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Oct 17  2021 .
drwxr-xr-x    3 ftp      ftp          4096 Oct 17  2021 ..
-rw-r--r--    1 ftp      ftp           178 Oct 17  2021 you_are_determined.txt
226 Directory send OK.
ftp> get you_are_determined.txt
local: you_are_determined.txt remote: you_are_determined.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for you_are_determined.txt (178 bytes).
226 Transfer complete.
178 bytes received in 0.00 secs (73.8124 kB/s)
ftp> bye
221 Goodbye.
```
