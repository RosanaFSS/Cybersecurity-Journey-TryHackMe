<h1 align="center">Web Enumeration</h1>
<p align="center">2025, September 8<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>490</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn the methodology of enumerating websites by using tools such as Gobuster, Nikto and WPScan</em><br>
<img width="80px" src="image" src="https://github.com/user-attachments/assets/6e0971b8-6c5d-4d01-8303-8571ffa96e14"><br>
Access this TryHackMe´s walkthrough <a href=https://tryhackme.com/room/webenumerationv2">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/354bd09f-8e2f-402e-aba0-d3d68583dd4c"></p>

<h2>Task 1 . Introduction</h2>
<h3>Introduction</h3>
<p>Welcome to Web Enumeration! In this room, we'll be showcasing some of the most fundamental tools used in the enumeration stage of a web target. Good enumeration skills are vital in penetration testing -- how else are you supposed to know what you're targeting?! It is, however, rather easy to fall into rabbit holes. <br>

The tools we'll showcase will hopefully make this process easier. You'll be able to apply the knowledge gained for each tool on an Instance dedicated to each tool.</p>

<h3>Prerequisities for this lab</h3>

<p>You will need to be connected to the TryHackMe network if you are not using the TryHackMe AttackBox or Kali instance. Other than that, all you need is a good posture and some willpower!<br>

Note: This room has been written as if you were using the TryHackMe AttackBox</p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s get started<br>
<code>No answer needed</code>

<br>  
<h2>Task 2 . Manual Enumeration</h2>

<p>2.1. I gotcha!<br>
<code>No answer needed</code>

<br>
<h2>Task 3 . Introduction to Gobuster</h2>
<br>

<p><em>Answer the question below</em></p>

<p>3.1. No questions<br>
<code>No answer needed</code>

<h2>Task 4 . Gobuster Modes</h2>
<br>

<p><em>Answer the question below</em></p>

<p>4.1. I get the hang of it!<br>
<code>No answer needed</code>

<br>
<h2>Task 5 . Useful Wordlists</h2>
<h3>Useful Wordlists</h3>
<p>There are many useful wordlists to use for each mode. These may or may not come in handy later on during the VM portion of the room! I'll go over some of the ones that are on Kali by default as well as a short section on SecLists.</p>

<h3>Kali Linux Default Lists</h3>
<p>Below you will find a useful list of wordlists that are installed on Kali Linux by default. This is as of the latest version at the time of writing which is 2020.3. Anything with a wildcard (*) character indicates there's more than one list that matches. Keep in mind, a lot of these can be interchanged between modes. For example, "dir" mode wordlists (such as ones from the dirbuster directory) will contain words like "admin", "index", "about", "events", etc. A lot of these could be subdomains as well. Give them a try with the different modes!<br>

- /usr/share/wordlists/dirbuster/directory-list-2.3-*.txt<br>
- /usr/share/wordlists/dirbuster/directory-list-1.0.txt<br>
- /usr/share/wordlists/dirb/big.txt<br>
- /usr/share/wordlists/dirb/common.txt<br>
- /usr/share/wordlists/dirb/small.txt<br>
- /usr/share/wordlists/dirb/extensions_common.txt - Useful for when fuzzing for files!</p>

<h3>Non=Standard Lists</h3>
<p>In  addition to the above, Daniel Miessler has created an amazing GitHub repo called SecLists. It compiles many different lists used for many different things. The best part is, it's in apt! You can sudo apt install seclists and get the entire repo! We won't dive into any other lists as there are many. However, between what's installed by default on Kali and the SecLists repo, I doubt you'll need anything else.</p>


<p><em>Answer the question below</em></p>

<p>5.1. No questions<br>
<code>No answer needed</code>

<br>
<h2>Task 6 . Practical Gobuster (Deploy #1)</h2>
<h3>Gobuster Challenges</h3>
<p>Now's your chance to check what you've learned. Deploy the VM, allow five minutes for it to fully deploy and answer the following questions! Good luck!<br>

You will also need to add "webenum.thm" to your /etc/hosts file to start off with like so:<br>

<code>echo "MACHINE_IP webenum.thm" >> /etc/hosts</code><br>

You will also need to add any virtual hosts that you discover through the same way, before you can visit them in your browser i.e.:<br>

<code>echo "MACHINE_IP mysubdomain.webenum.thm" >> /etc/hosts</code><br>

Any answer that has a list of items will have its answer formatted in the following way: ans1,ans2. Be sure to format your answers like that to get credit.</p>

<p><em>Answer the questions below</em></p>


<p>6.1. Run a directory scan on the host. Other than the standard css, images and js directories, what other directories are available?<br>
<code>public,Changes,VIDEO</code>


<img width="1016" height="394" alt="image" src="https://github.com/user-attachments/assets/c4283e68-6697-4395-8f5a-61575dbf1c74" />

<br>
<p>6.2. Run a directory scan on the host. In the "C******" directory, what file extensions exist?<br>
<code>conf,js</code>

<img width="1189" height="381" alt="image" src="https://github.com/user-attachments/assets/24e83636-66b2-450f-bab4-2ad90a05b164" />

<br>
<p>6.3. There's a flag out there that can be found by directory scanning! Find it!<br>
<code>thm{n1c3_w0rk}</code>

<img width="1060" height="282" alt="image" src="https://github.com/user-attachments/assets/3d51a7cc-e406-4a1c-bf28-78283536b779" />

<img width="1063" height="217" alt="image" src="https://github.com/user-attachments/assets/04f6c76d-27e2-4d44-bbf8-23b0a3099fa1" />


<br>
<p>6.4. There are some virtual hosts running on this server. What are they?<br>
<code>learning,products</code>

```bash
:~/WebEnumeration# ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "HOST: FUZZ.webenum.thm" -u http://xx.xxx.xx.xxx -fs 1202
```

<img width="947" height="354" alt="image" src="https://github.com/user-attachments/assets/44e4f38d-e089-4cfd-a2ea-23b276bc759b" />

<br>

```bash
:~/WebEnumeration# ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -H "HOST: FUZZ.webenum.thm" -u http://xx.xxx.xx.xxx -fs 1202
```

<img width="959" height="385" alt="image" src="https://github.com/user-attachments/assets/b2fd898a-92af-47cb-9952-eb7b3df7af6d" />


<br>
<p>6.5. There's another flag to be found in one of the virtual hosts! Find it!<br>
<code>thm{gobuster_is_fun}</code>

<img width="1289" height="403" alt="image" src="https://github.com/user-attachments/assets/d91b5612-f89f-4bdc-9b3a-62201704b463" />

<img width="1056" height="167" alt="image" src="https://github.com/user-attachments/assets/3ab4fdc4-2d85-4391-ab74-fd67d0909dbe" />


<br>
<br>
<h2>Task 7 . Introduction to WPScan</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>7.1.Letps explore WPScan.<br>
<code>No answer needed</code>


<h2>Task 8 . WPScan Modes</h2>
<br>

<p><em>Answer the questions below</em></p>

<br>
<p>8.1. What would be the full URL for the theme "twentynineteen" installed on the WordPress site: "http://cmnatics.playground"<br>
<code>http://cmnatics.playground/wp-content/themes/twentynineteen</code></p>

<br>
<p>8.2. What argument would we provide to enumerate a WordPress site?<br>
<code>enumerate</code></p>

<br>
<p>8.3. What is the name of the other aggressiveness profile that we can use in our WPScan command?<br>
<code>enumerate</code></p>

<br>
<h2>Task 9 . Practical: WPScan (Deploy #2)</h2>
<br>

<p><em>Answer the questions below</em></p>

<br>
<p>9.1. Enumerate the site, what is the name of the theme that is detected as running?<br>
<code>twentynineteen</code>

<img width="857" height="170" alt="image" src="https://github.com/user-attachments/assets/793edd57-3970-4991-ab2e-720dd8bc5b4d" />

<br>
<p>9.2. Enumerate the site, what is the name of the plugin that WPScan has found?<br>
<code>nextgen-gallery</code>

```bash
:~/WebEnumeration# wpscan --url http://cmnatics.playground/
```

<img width="813" height="412" alt="image" src="https://github.com/user-attachments/assets/bc4f44f5-5f09-4c4a-87e2-17233f863601" />

<br>
<p>9.3. Enumerate the site, what username can WPScan find?<br>
<code>phreakazoid</code>

```bash
:~/WebEnumeration# wpscan --url http://cmnatics.playground/ --enumerate u
```

<img width="798" height="140" alt="image" src="https://github.com/user-attachments/assets/5877053e-8ffa-4f75-9b9d-33c24ac2c9ff" />


<br>
<p>9.4. Construct a WPScan command to brute-force the site with this username, using the rockyou wordlist as the password list. What is the password to this user? <br>
<code>linkinpark</code>

```bash
:~/WebEnumeration# wpscan --url http://cmnatics.playground/ --passwords /usr/share/wordlists/rockyou.txt --usernames phreakazoid
```

<img width="810" height="132" alt="image" src="https://github.com/user-attachments/assets/0efc948a-ea05-4096-838b-59c0043e4ee4" />

<br>
<br>
<h2>Task 10 . Introduction to Nikto</h2>
<br>

<p><em>Answer the question below</em></p>

<p>10.1. Let's dive into the world of Nikto<br>
<code>No answer needed</code></p>

<h2>Task 11 . Nikto Modes</h2>
<h3>Basic Scanning</h3>

<p>The most basic scan can be performed by using the -h flag and providing an IP address or domain name as an argument. This scan type will retrieve the headers advertised by the webserver or application (I.e. Apache2, Apache Tomcat, Jenkins or JBoss) and will look for any sensitive files or directories (i.e. login.php, /admin/, etc)<br>

An example of this is the following: nikto -h vulnerable_ip</p>

<img width="1276" height="481" alt="image" src="https://github.com/user-attachments/assets/acc8a4c3-a3f7-4f42-9cf5-5ea77d79fb44" />


<p>Note a few interesting things are given to us in this example:<br>

- Nikto has identified that the application is Apache Tomcat using the favicon and the presence of "/examples/servlets/index.html" which is the location for the default Apache Tomcat application.<br>
- HTTP Methods "PUT" and "DELETE" can be performed by clients - we may be able to leverage these to exploit the application by uploading or deleting files.</p>

<h3>Scanning Multiple Hosts & Ports</h3>


<h3>Introduction to Plugins</h3>


<h3>Verbosing our Scan</h3>


<h3>Tuning Your Scan for Vulnerability Searching</h3>


<h3>Saving Your Findings</h3>


<p><em>Answer the questions below</em></p>

<p>11.1. What argument would we use if we wanted to scan port 80 and 8080 on a host?<br>
<code>-p 80,8080</code></p>

```bash
:~/WebEnumeration# nikto -h xx.xxx.xx.xxx -p 80,8080
- Nikto v2.1.5
---------------------------------------------------------------------------
+ No web server found on cmnatics.playground:8080
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    cmnatics.playground
+ Target Port:        80
+ Start Time:         2025-09-09 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ Uncommon header 'link' found, with contents: <http://wpscan.thm/index.php?rest_route=/>; rel="https://api.w.org/"
+ All CGI directories 'found', use '-C none' to test none
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ /cgi.cgi/post-query: Echoes back result of your POST
+ /webcgi/post-query: Echoes back result of your POST
+ /cgi-914/post-query: Echoes back result of your POST
+ /cgi-915/post-query: Echoes back result of your POST
+ /bin/post-query: Echoes back result of your POST
+ /cgi/post-query: Echoes back result of your POST
+ /mpcgi/post-query: Echoes back result of your POST
+ /cgi-bin/post-query: Echoes back result of your POST
+ /ows-bin/post-query: Echoes back result of your POST
+ /cgi-sys/post-query: Echoes back result of your POST
+ /cgi-local/post-query: Echoes back result of your POST
+ /htbin/post-query: Echoes back result of your POST
+ /cgibin/post-query: Echoes back result of your POST
+ /cgis/post-query: Echoes back result of your POST
+ /scripts/post-query: Echoes back result of your POST
+ /cgi-win/post-query: Echoes back result of your POST
+ /fcgi-bin/post-query: Echoes back result of your POST
+ /cgi-exe/post-query: Echoes back result of your POST
+ /cgi-home/post-query: Echoes back result of your POST
+ /cgi-perl/post-query: Echoes back result of your POST
+ /scgi-bin/post-query: Echoes back result of your POST
+ OSVDB-2754: /guestbook/?number=5&lng=%3Cscript%3Ealert(document.domain);%3C/script%3E: MPM Guestbook 1.2 and previous are vulnreable to XSS attacks.
+ OSVDB-28260: /_vti_bin/shtml.dll/_vti_rpc?method=server+version%3a4%2e0%2e2%2e2611: Gives info about server settings. CVE-2000-0413, CVE-2000-0709, CVE-2000-0710, http://www.securityfocus.com/bid/1608, http://www.securityfocus.com/bid/1174.
+ OSVDB-28260: /_vti_bin/shtml.exe/_vti_rpc?method=server+version%3a4%2e0%2e2%2e2611: Gives info about server settings.
+ OSVDB-3092: /_vti_bin/_vti_aut/author.dll?method=list+documents%3a3%2e0%2e2%2e1706&service%5fname=&listHiddenDocs=true&listExplorerDocs=true&listRecurse=false&listFiles=true&listFolders=true&listLinkInfo=true&listIncludeParent=true&listDerivedT=false&listBorders=fals: We seem to have authoring access to the FrontPage web.
+ OSVDB-3092: /_vti_bin/_vti_aut/author.exe?method=list+documents%3a3%2e0%2e2%2e1706&service%5fname=&listHiddenDocs=true&listExplorerDocs=true&listRecurse=false&listFiles=true&listFolders=true&listLinkInfo=true&listIncludeParent=true&listDerivedT=false&listBorders=fals: We seem to have authoring access to the FrontPage web.
+ OSVDB-3093: /cgi.cgi/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /webcgi/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /cgi-914/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /cgi-915/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /bin/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /cgi/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /mpcgi/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /cgi-bin/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /ows-bin/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /cgi-sys/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /cgi-local/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /htbin/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /cgibin/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /cgis/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /scripts/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /cgi-win/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /fcgi-bin/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /cgi-exe/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /cgi-home/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /cgi-perl/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /scgi-bin/rightfax/fuwww.dll/?: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-4314: /texis.exe/?-dump: Texis installation may reveal sensitive information.
+ OSVDB-4314: /texis.exe/?-version: Texis installation may reveal sensitive information.
+ Server leaks inodes via ETags, header found with file /icons/README, fields: 0x13f4 0x438c034968a80 
+ OSVDB-3233: /icons/README: Apache default file found.
+ OSVDB-3092: /license.txt: License file found may identify site software.
+ /wp-login/: Admin login page/section found.
+ /wordpress/: A Wordpress installation was found.
+ Cookie wordpress_test_cookie created without the httponly flag
+ Uncommon header 'x-frame-options' found, with contents: SAMEORIGIN
+ 6544 items checked: 0 error(s) and 59 item(s) reported on remote host
+ End Time:           2025-08-09 xx:xx:xx (GMT1) (338 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<p>11.2. What argument would we use if we wanted to see any cookies given by the web server? <br>
<code>-Display 2</code></p>

<br>
<h2>Task 12 . Nikto Practical (#3)</h2>
<p>Deploy the Instance attached to this task. Allow five minutes for it to fully deploy before you begin your Nikto scans!<br>

Use Nikto to assess the ports on MACHINE_IP to answer the following questions:</p>

<p><em>Answer the questions below</em></p>

<p>12.1. What is the name & version of the web server that  Nikto has determined running on port 80?<br>
<code>Apache/2.4.7</code></p>

```bash
:~/WebEnumeration# nikto -h xx.xxx.xxx.xxx -p 80,8080
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xxx.xxx
+ Target Hostname:    xx.xxx.xxx.xxx
+ Target Port:        80
+ Start Time:         2025-09-08 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.7 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x40e0 0x5a0311fe9980a 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, HEAD, POST, OPTIONS 
+ OSVDB-3092: /sitemap.xml: This gives a nice listing of the site content.
+ OSVDB-3268: /images/: Directory indexing found.
+ OSVDB-3268: /images/?pattern=/etc/*&sort=name: Directory indexing found.
+ OSVDB-3233: /icons/README: Apache default file found.
+ 6544 items checked: 0 error(s) and 7 item(s) reported on remote host
+ End Time:           2025-09-08 xx:xx:xx (GMT1) (7 seconds)
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xxx.xxx
+ Target Hostname:    xx.xxx.xxx.xxx
+ Target Port:        8080
+ Start Time:         2025-09-08 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache-Coyote/1.1
+ Retrieved x-powered-by header: Servlet/3.0; JBossAS-6
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OSVDB-39272: favicon.ico file identifies this server as: JBoss Server
+ Allowed HTTP Methods: GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS 
+ OSVDB-397: HTTP method ('Allow' Header): 'PUT' method could allow clients to save files on the web server.
+ OSVDB-5646: HTTP method ('Allow' Header): 'DELETE' may allow clients to remove files on the web server.
+ Cookie JSESSIONID created without the httponly flag
+ 6544 items checked: 0 error(s) and 5 item(s) reported on remote host
+ End Time:           2025-09-08 xx:xx:xx (GMT1) (23 seconds)
---------------------------------------------------------------------------
+ 2 host(s) tested
```

<br>
<p>12.2. There is another web server running on another port. What is the name & version of this web server?<br>
<code>Apache-Coyote/1.1</code></p>

<br>
<p>12.3. What is the name of the Cookie that this JBoss server gives?<br>
<code>JSESSIONID</code></p>

<br>
<h2>Task 13 . Conclusion</h2>
<br>

<br>
<p>13.1. I´ll check this out<br>
<code>No answer needed</code></p>

<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/09933bcb-d6bc-49f2-949f-4a2be5c62ce0"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/469fae72-595a-462e-9334-609531380842"></p>

<h2 align="center">My TryHackMe Journey</h2>


<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time   |   All Time   |   Monthly   |   Monthly  | Points   | Rooms     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                                       |         |    Global    |    Brazil    |   Global    |   Brazil   |          | Completed |           |
| 2025, Sep 8       |Easy 🔗 - <code><strong>Web Enumeration</strong></code>| 490| 112ⁿᵈ | 5ᵗʰ   |    663ʳᵈ    |     10ᵗʰ    | 124,986  |  952      |    73     |
| 2025, Sep 8       |Easy 🔗 - iOS: Forensics| 490| 113ʳᵈ | 5ᵗʰ   |    548ᵗʰ    |     9ᵗʰ    | 124,850  |  951      |    73     |
| 2025, Sep 7       |Medium 🚩 - VulnNet: Active| 489| 114ᵗʰ | 5ᵗʰ   |    542ⁿᵈ    |     9ᵗʰ    | 124,746  |  950      |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489|     114ᵗʰ |     5ᵗʰ      |    535ᵗʰ   |     9ᵗʰ    | 124,716  |  949      |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489     |     113ʳᵈ    |     5ᵗʰ      |    508ᵗʰ   |     9ᵗʰ    | 124,886  |  948      |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488     |     114ᵗʰ    |      5ᵗʰ     |     683ᵗʰ   |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ   |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ   |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488     |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ   |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487     |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ   |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487     |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ   |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486     |	   113ʳᵈ   |	     5ᵗʰ   	|      579ᵗʰ   |	  10ᵗʰ    |	124,018  |	  940	   |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486     |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ   |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485     |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ   |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484     |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ   |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483     |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ   |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   112ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/331c9f68-c23f-43e6-9799-e1e621b85535"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/e3f923ba-f39e-48c2-9f40-2120a1f3b306"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/e19039f9-4212-4452-80a8-39a0e0fec744"><br>
                  Global monthly:    663ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/0fef4dbe-45d9-435d-b7e5-2907f95cf43d"><br>
                  Brazil monthly:      10ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/686f4c65-b0b5-43fa-8cff-f4b0a869f868"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>  
