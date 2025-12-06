<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 2 &nbsp;&nbsp; ·  &nbsp;&nbsp; Phishing - Merry Clickmas</h3>
<p align="center">2025, December 6  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Learn how to use the Social-Engineer Toolkit to send phishing emails. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/phishing-aoc2025-h2tkye9fzU">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/2144a1e4-c112-4f09-a40c-ec911a7d96ae"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/982c1b13-22d3-4f16-bb4a-a0ca63ccf94c"></p>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/8c13fd21-90fc-4f1e-9aa4-5250302e7193"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>In light of several recent cyber security threats against The Best Festival Company (TBFC), the local red team has scheduled several penetration tests. The red teamers proceeded to carry out a regular penetration test against their TBFC. Part of this exercise is to ensure that the employees are diligent when clicking links and that the company is well protected against the latest phishing attacks. This type of authorised phishing is a proven way to learn whether the cyber security awareness training has fruited.<br>

In this task, you will be part of the TBFC local red team with the elves Recon McRed, Exploit McRed, and Pivot McRed. You will help them plan and execute their phishing campaign. It is time to see if more cyber security awareness training is required.</p>

<h3>Learning Objectives</h3>
<p>

- Understand what social engineering is<br>
- Learn the types of phishing<br>
- Explore how red teams create fake login pages<br>
- Use the Social-Engineer Toolkit to send a phishing email</p>

<h3>Connecting to the Machine</h3>
<p>Before moving forward, review the questions in the connection card shown below:</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/d64b5e98-8121-4b5a-a194-933ef0f9a647"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Start your target VM by clicking the <strong>Start Machine</strong> button below. The machine will need about 2 minutes to fully boot. Additionally, start your AttackBox by clicking the <strong>Start AttackBox</strong> button below. The AttackBox will start in split view. In case you can not see it, click the <strong>Show Split View</strong> button at the top of the page.</p>

<p><em>Answer the question below</em></p>

<p>1.1. &nbsp;&nbsp; <em>I have successfully started the AttackBox and the target machine!</em><br>
<code>No answer needed</code><p>


<h2>Task 2 &nbsp; ·  &nbsp; Phishing Exercise for TBFC</h2>
<h3>Social Engineering</h3>
<p><strong>Social engineering</strong> refers to manipulating a user to make a mistake. Examples of such mistakes include sharing a password, opening a malicious file, and approving a payment. The term “social” means that the target of such an attack is human beings, not computer systems. Consequently, the attacker relies on psychological tricks to get the target user to cooperate. Some psychological factors that can play a key role in the success of such attacks are urgency, curiosity, and authority. This is why some would refer to social engineering as “human hacking”.</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/4596ae1a-2e21-44cb-8aa0-2a5d52950b43"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<h3>Phishing</h3>
<p>Phishing is a subset of social engineering in which the communication medium is mostly messages. At one point, the most common phishing attacks happened via email; however, the spread of smartphones, along with ubiquitous Internet access, has spread phishing to short text messages (smishing), voice calls (vishing), QR codes (quishing), and social-media direct messages. The attacker’s purpose is to make the target user click, open, or reply to a message so that the attacker can steal information, money, or access.<br>

Unfortunately, phishing attacks are becoming harder to spot. Even careful people might fall target to such attacks if they don’t exercise proper care. TBFC cyber security awareness training teaches users about two anti-phishing mnemonics written as S.T.O.P. The first S.T.O.P. is from <a href="https://www.linkedin.com/in/rosanafssantos/">All Things Secured</a>, which tells users to ask the following questions before acting on an email:<br>

- <strong>Suspicious?</strong><br>
- <strong>Telling me</strong> to click something?<br>
- <strong>Offering me</strong> an amazing deal?<br>
- <strong>Pushing me</strong> to do something now?<br>

The second S.T.O.P. reminds users to follow the following instructions:<br>

- <strong>Slow down</strong>. Scammers run on your adrenaline.<br>
- <strong>Type the address yourself</strong>. Don’t use the message’s link.<br>
- <strong>Open nothing unexpected</strong>. Verify first.<br>
- <strong>Prove the sender</strong>. Check the real From address/number, not just the display name.<br>

After hours of periodic cyber security training, the red team checks to see if the TBFC staff can dodge “fishy” emails.</p>

<h3>Building the Trap</h3>
<p>You must sound very convincing as a penetration tester for a successful phishing attack. It’s not only how you write the phishing email or messages, but also how you set up the trap for the target. The trap can be anything, depending on your objectives and the research you conduct on the target. Sometimes, attackers aim to compromise the target’s machine, and they achieve this by attaching a malicious file to their phishing email. Attackers sometimes craft a web page that mimics a legitimate login page to steal the target’s credentials.<br>

In this task, we aim to acquire the target user’s login credentials. Our trap would be a fake TBFC portal login page, which we attach to the phishing email and send to the target. But a login page itself is not enough. We need to host it and implement some logic to capture the credentials entered by the target. To facilitate your task, we have already set up a script that, when run, will host a fake login page. The phoney login page we created will capture all the credentials entered into the page.<br>

The script is already placed on the AttackBox at <code>~/Rooms/AoC2025/Day02</code>. Alternatively, if you want to use your own THM VPN connected machine, you can download the script via the <strong>Download Task Files</strong> button below. Make sure to keep both files in the same directory.<br>

To run the script, use <code>./server.py</code> and it will start listening for any credentials. If the target gets trapped and enters the credentials, it will be shown on the same terminal.</p>

<p align="center">AttackBox Terminal</p>

```bash
root@attackbox:~# cd ~/Rooms/AoC2025/Day02
root@attackbox:~/Rooms/AoC2025/Day02# ./server.py
Starting server on http://0.0.0.0:8000
```

<p>The above message indicates that the phishing web application is listening on port 8000; moreover, the <code>0.0.0.0</code> implies that it is bound to all interfaces. To confirm what the user will see, use Firefox on the AttackBox and browse to <code>http://CONNECTION_IP:8000</code> or <code>http://127.0.0.1:8000</code>; either of these addresses will show you what the user will see. With this set, it is time to email this link to test our users’ vigilance.</p>

<h3>Delivering via Social-Engineer Toolkit (SET)</h3>
<p>As our phishing page is ready, we can now prepare and send the phishing email to our target users. Sending it from our personal email is the worst idea. Ideally, the email should appear to be coming from a legitimate-looking sender; for example, we can pretend to be somebody the target user trusts or expects to get such an email from them. The more a phishing email appears realistic, the more likely it is for the target user to believe it and get phished. The question is how we can send a realistic-looking email that contains our fake login page.<br>

One solution is to use the <a href="https://github.com/trustedsec/social-engineer-toolkit">Social-Engineer Toolkit (SET)</a>. It is an open-source tool primarily designed by David Kennedy for social engineering attacks. It offers a wide range of features. In particular, it lets you compose and send a phishing email. In the current scenario, we will use this tool to create and send a phishing email to the target user. <br>

Let’s start creating the phishing email through the SET tool. Before you use this tool, please remember that it will involve multiple steps, each asking different questions about the phishing email you intend to send. So, please be patient and follow along the process.<br>

To start the tool, type <code>setoolkit</code> into the terminal, and it will present you with a menu containing multiple options. At the bottom, you will see <code>set></code>, where you can input your desired option number. For our case, we would select option <code>1</code>, i.e., <code>Social-Engineering Attacks</code>. If you choose the wrong option at any stage, the option <code>99</code> will take you back to the main menu, where you can start again. However, if you commit any mistake while writing the phishing email, you would have to press <code>Ctrl + C</code> to return to the main menu. The social engineering attacks cover various attacks from spear-phishing and mass mailer attacks to wireless access point attacks.</p>


<p align="center">AttackBox Terminal</p>

```bash
root@attackbox:~# setoolkit
[...]
 Select from the menu:

   1) Social-Engineering Attacks
   2) Penetration Testing (Fast-Track)
   3) Third Party Modules
   4) Update the Social-Engineer Toolkit
   5) Update SET configuration
   6) Help, Credits, and About

  99) Exit the Social-Engineer Toolkit
     
set> 1
```

<p>Choosing <code>1</code> will display another menu with the type of social engineering attack we want to use in our attack. In this case, we will pick <strong>Mass Mailer Attack</strong> by typing <code>5</code>.</p>

<p align="center">AttackBox Terminal</p>

```bash
 Select from the menu:

   1) Spear-Phishing Attack Vectors
   2) Website Attack Vectors
   3) Infectious Media Generator
   4) Create a Payload and Listener
   5) Mass Mailer Attack
   6) Arduino-Based Attack Vector
   7) Wireless Access Point Attack Vector
   8) QRCode Generator Attack Vector
   9) PowerShell Attack Vectors
  10) Third-Party Modules

  99) Return back to the main menu.

set> 5
```

<p>Now, we would be asked to select between two options. One option allows us to send the phishing email to a single address, while the other option enables us to send an email to many people. Here, we would select option <code>1</code>, i.e., <code>E-Mail Attack Single Email Address</code>.</p>

<p align="center">AttackBox Terminal</p>

```bash
   Social Engineer Toolkit Mass E-Mailer

   There are two options on the mass e-mailer: the first is to email one person. The second option
   will allow you to import a list and send it to as many people as
   you want within that list.

   What do you want to do:

    1. E-Mail Attack Single Email Address
    2. E-Mail Attack Mass Mailer

    99. Return to the main menu.
   
set:mailer> 1
```

<p>Now, we will have several questions to answer and various fields to fill out. The first set of questions concerns the email addresses and how the email will be routed and delivered. After each input provided, we can press <strong>Enter</strong> to get to the next question.<br>

- <strong>Send email to</strong>: Let’s begin by targeting <code>factory@wareville.thm</code><br>
- <strong>How to deliver the email</strong>: We will choose <code>Use your own server or open relay</code><br>
- <strong>From address</strong>: We know that the guys at the toy factory communicate regularly with Flying Deer, the shipping company, so that we will use <code>updates@flyingdeer.thm</code> as the source email address<br>
- <strong>From name</strong>: Let’s use the name <code>Flying Deer</code><br>
- <strong>Username for open-relay</strong>: We will leave it blank and just hit the <strong>Enter</strong> key<br>
- <strong>Password for open-relay</strong>: We will leave it blank and just hit the <strong>Enter</strong> key<br>
- <strong>SMTP email server address</strong>: We will deliver directly to the TBFC mail server by entering <code>MACHINE_IP</code>.<br>
- <strong>Port number for the SMTP server</strong>: We leave the default value of <code>25</code> and just hit the <strong>Enter</strong> key<br>

The next set of questions will ask if you want to send it as a high priority or attach a file.<br>

- <strong>Flag this message as high priority</strong>: The choice is entirely up to you, depending on your knowledge of the circumstances, but we will answer with <code>no</code><br>
- <strong>Do you want to attach a file</strong>: We will answer with <code>n</code><br>
- <strong>Do you want to attach an inline file</strong>: Again, let’s answer with  <code>n</code><br>

Finally, we pick an email subject and enter the message contents in plaintext or HTML.<br>

- <strong>Email subject</strong>: We need to think of something convincing, for example, “Shipping Schedule Changes”<br>
- <strong>Send the message as HTML or plain</strong>: We will keep the default choice of plaintext and just hit the Enter key<br>
- <strong>Enter the body of the message, and type END (capitals) when finished</strong>: Create and type any convincing message. Make sure to include the URL <code>http://CONNECTION_IP:8000</code> to check if the target will fall for this trick.<br>

An example interaction is shown in the terminal below.</p>

<p align="center">AttackBox Terminal</p>

```bash
set:mailer>1
set:phishing> Send email to:factory@wareville.thm

  1. Use a Gmail account for your email attack.
  2. Use your own server or open relay

set:phishing>2
set:phishing> From address (ex: moo@example.com):updates@deershipping.thm
set:phishing> The FROM NAME the user will see:Deer Shipping
set:phishing> Username for open-relay [blank]:
Password for open-relay [blank]: 
set:phishing> SMTP email server address (ex. smtp.youremailserveryouown.com):10.65.141.58
set:phishing> Port number for the SMTP server [25]:  
set:phishing> Flag this message/s as high priority? [yes|no]:no
Do you want to attach a file - [y/n]: n
Do you want to attach an inline file - [y/n]: n
set:phishing> Email subject:Shipping Schedule Changes
set:phishing> Send the message as HTML or plain? 'h' or 'p' [p]:
[!] IMPORTANT: When finished, type END (all capital) then hit {return} on a new line.
set:phishing> Enter the body of the message, type END (capitals) when finished:Dear elves, 
Next line of the body: Kindly note that there have been significant changes to the shipping schedules due to increased shipping orders.
Next line of the body: Please confirm the new schedule by visiting http://10.65.112.199:8000
Next line of the body: Best regards,
Next line of the body: Flying Deer
Next line of the body: END
[*] SET has finished sending the emails

      Press <return> to continue
```

<p>Now, the phishing email has been sent to the target. The <strong>"Press <return> to continue"</return></strong>strong> button is just the Enter button to restart the tool. Open the terminal where our <code>server.py</code> script is running to see if the user gets trapped and enters their credentials.<br>

Note: You may have to wait for 1 - 2 minutes and observe the terminal for any credentials entered by the user.<br>

To the TBFC red team’s surprise, they received at least one set of working credentials. This result is alarming; it means that an adversary could succeed in a similar attack if it has not already been done. Considering the received credentials, if an adversary gains such access, they can easily wreck the whole gift delivery system. It is vital to check if such an attack has taken place and act accordingly.</p>


<p><em>Answer the questions below</em></p>

<p>2.1. &nbsp;&nbsp; <em>What is the password used to access the TBFC portal?</em><br>
<code>unranked-wisdom-anthem</code><p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/4ce75bef-fe60-40c0-8089-afbc91b6bb1b"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/cad80dd0-4bf8-44e6-9038-9481517f830a"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/990bf6d7-c548-4028-926b-65591533d9aa"></p>

<br>
<p>2.2. &nbsp;&nbsp; <em>Browse to <code>http://MACHINE_IP</code></code> from within the AttackBox and try to access the mailbox of the <code>factory</code> user to see if the previously harvested <code>admin</code> password has been reused on the email portal. What is the total number of toys expected for delivery?</em><br>
<code>1984000</code><p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/dea14621-9a18-4690-af35-082f1e479ce3"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/7bea97bd-a142-4f8a-9f5d-680900a954f4"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/4aaacf46-f66b-4f4b-98e6-b9181f8d4bda"></p>

<br>
<p>2.3. &nbsp;&nbsp; <em>If you enjoyed today's room, feel free to check out the Phishing Prevention room.</em><br>
<code>No answer needed</code><p>
  
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/400d7adb-c276-4f70-9343-31af8ff73977"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/383d1a42-05b8-4106-9507-a1e5ddef8f6b"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/a8653074-45cc-4bcc-9443-92581877b65d"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|6       |Easy 🔗 - Phishing - Merry Clickmas   |   1    |      96ᵗʰ    |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells    |   1    |      97ᵗʰ    |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>

<p align="center">Global All Time:     96ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/23e3f2b0-560f-4cfb-b7bc-5fa78788710a"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/3c09a013-4d93-4faa-b297-7709b9871025"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/10721f5c-3afb-4c00-8b52-ed3dd9cd2af0"><br><br>
                  Global monthly:  53,003ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/ac55c469-2223-4ddd-b68b-edadb33cb81c"><br><br>
                  Brazil monthly:     674ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c1ef4a77-50e9-41f4-b8ff-c340bb829d0f"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
