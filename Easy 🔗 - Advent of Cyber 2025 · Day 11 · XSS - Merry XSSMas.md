<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 11 &nbsp;&nbsp; ·  &nbsp;&nbsp; XSS - Merry XSSMas</h3>
<p align="center">2025, December 20  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in <a href="https://tryhackme.com">TryHackMe</a>.<br>Learn about types of XSS vulnerabilities and how to prevent them. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/xss-aoc2025-c5j8b1m4t6">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/ee6dff73-8349-492d-ba5e-cd781dbad215"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/2b2222b7-5f0f-4d46-ab6a-0724e4da4631"></p>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/75868fb2-8c3d-4414-bfc8-ecb6220e3bff"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>After last year's automation and tech modernisation, Santa's workshop got a new makeover. McSkidy has a secure message portal where you can contact her directly with any questions or concerns. However, lately, the logs have been lighting up with unusual activity, ranging from odd messages to suspicious search terms. Even Santa's letters appear to be scripts or random code. Your mission, should you choose to accept it: dig through the logs, uncover the mischief, and figure out who's trying to mess with McSkidy. </p>

<h3>Learning Objectives</h3>
<p>
  
- Understand how XSS works<br>
- Learn to prevent XSS attacks</p>

<h3>Connecting to the Machine</h3>
<p>Before moving forward, review the questions in the connection card shown below:</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/83021242-4d29-4f96-8913-322ef84b5b27"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Start your target VM by clicking the <strong>Start Machine</strong> button below. The machine will need about 2 minutes to fully boot. Additionally, start your AttackBox by clicking the <strong>Start AttackBox</strong> button below. The AttackBox will start in split view. In case you can not see it, click the <strong>Show Split View</strong> at the top of the page.</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting both your AttackBox (if you're not using your VPN) and Target Machines, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<br>
<p><em>Answer the question below</em></p>

<p>1.1. <em>I have successfully started the AttackBox and target machine!</em><br>
<code>No answer needed</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/968501bd-68b4-423f-a8b0-bea3f53aca88"><br>Rosana´s hands-on</h6>

<br>
<h2>Task 2 &nbsp; ·  &nbsp; Leave the Cookies, Take the Payload</h2>
<h3>Equipment Check</h3>
<p>For today's room we will be using a the web app found under http://MACHINE_IP. You can use the browser of your AttackBox to navigate to it. You will see a page as shown below:</p>

<img width="2890" height="1698" alt="image" src="https://github.com/user-attachments/assets/2d749b18-fdf8-4f1a-9812-bb62e1f40aff" />

<p>Let's review some key material regarding potential attacks on websites like this portal, specifically <a href="https://tryhackme.com/room/axss">Cross-Site Scripting (XSS)</a>.<br>

XSS is a web application vulnerability that lets attackers (or evil bunnies) inject malicious code (usually JavaScript) into input fields that reflect content viewed by other users (e.g., a form or a comment in a blog). When an application doesn't properly validate or escape user input, that input can be interpreted as code rather than harmless text. This results in malicious code that can steal credentials, deface pages, or impersonate users. Depending on the result, there are various types of XSS.  In today’s task, we focus on <strong>Reflected XSS</strong> and <strong>Stored XSS</strong>.</p>

<h3>Reflected XSS</h3>
<p>You see reflected variants when the injection is immediately projected in a response. Imagine a toy search function in an online toy store, you search via:<br>

<code>https://trygiftme.thm/search?term=gift</code><br>

But imagine you send this to your friend who is looking for a gift for their nephew (please don't do this):<br>

<code>https://trygiftme.thm/search?term=<script>alert( atob("VEhNe0V2aWxfQnVubnl9") )</script></code><br>

If your friend clicks on the link, it will execute code instead.</p>

<h4>Impact</h4>
You could act, view information, or modify information that your friend or any user could do, view, or access. It's usually exploited via phishing to trick users into clicking a link with malicious code injected.</p>

<h3>Stored XSS</h3>
<p>A Stored XSS attack occurs when malicious script is saved on the server and then loaded for every user who views the affected page. Unlike Reflected XSS, which targets individual victims, Stored XSS becomes a "set-and-forget" attack, anyone who loads the page runs the attacker’s script.<br>

To understand how this works, let’s use the example of a simple blog where users can submit comments that get displayed below each post.</p>

<h3>Normal Comment Submission</h3>

```bash
POST /post/comment HTTP/1.1
Host: tgm.review-your-gifts.thm

postId=3
name=Tony Baritone
email=tony@normal-person-i-swear.net
comment=This gift set my carpet on fire but my kid loved it!
```

<p>The server stores this information and displays it whenever someone visits that blog post.<p>

<h3>Malicious Comment Submission (Stored XSS Example)</h3>
<p>If the application does not sanitize or filter input, an attacker can submit JavaScript instead of a comment:</p>

```bash
POST /post/comment HTTP/1.1
Host: tgm.review-your-gifts.thm

postId=3
name=Tony Baritone
email=tony@normal-person-i-swear.net
comment=<script>alert(atob("VEhNe0V2aWxfU3RvcmVkX0VnZ30="))</script> + "This gift set my carpet on fire but my kid loved it!"
```

<p>Because the comment is saved in the database, every user who opens that blog post will automatically trigger the script.<br>
This lets the attacker run code as if they were the victim in order to perform malicious actions such as:<br>

- Steal session cookies<br>
- Trigger fake login popups<br>
- Deface the page</p>

<p>The server stores this information and displays it whenever someone visits that blog post.</p>

<h3>Protecting against XSS</h3>
<p>Each service is different, and requires a well-thought-out, secure design and implementation plan, but key practices you can implement are:<br>

- <code>Disable dangerous rendering paths</code>: Instead of using the <code>innerHTML</code> property, which lets you inject any content directly into HTML, use the <code>textContent</code> property instead, it treats input as text and parses it for HTML.<br><br>
- <code>Make cookies inaccessible to JS</code>: Set session cookies with the <a href="https://owasp.org/www-community/HttpOnly">HttpOnly</a>, <a href="https://owasp.org/www-community/controls/SecureCookieAttribute">Secure</a>, and <a href="https://owasp.org/www-community/SameSite">SameSite</a> attributes to reduce the impact of XSS attacks.<br><br>
- <code>Sanitise input/output and encode</code>:<br>In some situations, applications may need to accept limited HTML input—for example, to allow users to include safe links or basic formatting. However it's critical to sanitize and encode all user-supplied data to prevent security vulnerabilities. Sanitising and encoding removes or escapes any elements that could be interpreted as executable code, such as scripts, event handlers, or JavaScript URLs while preserving safe formatting.<br>

To exploit XSS vulnerabilities, we need some type of input field to inject code. There is a search section, let's start there.</p>

<h3>Exploiting Reflected XSS</h3>
<p>To exploit reflected XSS, we can use test payloads to check if the app runs the code injected. If you want to test more advanced payloads, there are <a href="https://portswigger.net/web-security/cross-site-scripting/cheat-sheet">chat sheets</a> online that you can use to craft them. For now, we'll pick the following payload:<br>

<code><script>alert('Reflected Meow Meow')</script></code><br>

Inject the code by adding the payload to the search bar and clicking "<strong>Search Messages</strong>". If it shows the alert text, we have confirmed reflected XSS. So, what happened?<br>

- The search input is reflected directly in the results without encoding<br>
- The browser interprets your HTML/JavaScript as executable code<br>
- An alert box appeared, demonstrating successful XSS execution<br>

You can track the behaviour and how the system interprets your actions by checking the "<strong>System Logs</strong>" tab at the bottom of the page:</p>

<img width="1414" height="270" alt="image" src="https://github.com/user-attachments/assets/ca96464a-1f72-4646-a1a2-d3e78b6937db" />

<p>Now that we have confirmed reflected XSS, let's investigate if it's susceptible to stored XSS. This vector must be different, as it needs to be persisted. Looking at the website, we can see that you are able to send messages, which are stored on the server for McSkidy to view later (as opposed to searching, which is stored temporarily on the client side).<br>

Navigate to the message form, and enter the malicious payload we used before (others work too):<br>

<code><script>alert('Stored Meow Meow')</script></code><br>

Click the "<strong>Send Message</strong>" button. Because messages are stored on the server, every time you navigate to the site or reload, the alert will display.</p>

<h3>Wrapping Up</h3>
<p>So it's confirmed! The site is vulnerable to XSS; it's no wonder that unusual payloads have been detected in the logs. The team will now harden the site to prevent future malicious code from being injected.</p>

<p>2.1. <em>Which type of XSS attack requires payloads to be persisted on the backend?</em><br>
<code>Stored</code></p>

<br>
<p>2.2. <em>What's the reflected XSS flag?</em><br>
<code>THM{Evil_Bunny}</code></p>

<br>
<p align="center">http://MACHINE_IP/search?term==<script>alert( atob("VEhNe0V2aWxfQnVubnl9") )</script></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c47ef23c-2411-4cbc-977d-a6c923854bdf"><br>Rosana´s hands-on</h6>

<br>
<p>2.3. <em>What's the stored XSS flag?</em><br>
<code>THM{Evil_Stored_Egg}</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/6eb64b15-8fda-40a7-986c-c09068d7b347"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/25c1e242-fb50-4e86-8b78-4de7f6eba2b6"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/7eed4c2f-008f-4ca7-9a9f-d20bf63c0117"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/9c156682-6b77-46f1-b7a7-6c88da716393"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/778e9f26-c07e-40ba-865a-6f5d6766f564"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/6d196ab6-d0a3-45da-9dbb-5b1173efd8d7"><br>Rosana´s hands-on</h6>

<br>
<p>2.4. <em>If you enjoyed todays's room, you might want to have a look at the <a href="https://tryhackme.com/room/xss">Intro to Cross-site Scripting</a> room!</em><br>
<code>No answer needed</code></p>

<h6 align="center"><a href="https://github.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/blob/Red-Teaming/2.3.%20Password%20Attacks.md">Password Attacks</a><br> 2024, September 24<br><img width="1200px" src="https://github.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/blob/CTFs-%26-Infos/Easy%20%F0%9F%94%97%20-%20Intro%20to%20Cross-Site%20Scripting.md"><br>Rosana´s hands-on</h6>

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/cbde390f-78ba-4893-a905-877ca7b549f1"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/ad3340e7-be0a-4f07-bd42-1725ed7e8720"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/108eca7e-7fff-4d61-99ec-ccd821b6404d"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|20      |Easy 🔗 - XSS - Merry XSSMas                     |4 |     100ᵗʰ  |     3ʳᵈ    |   23,069ᵗʰ   |      256ᵗʰ     |    134,792  |    1,040    |    84     |
|20      |Easy 🔗 -  Race Conditions - Toy to The World    |4 |     100ᵗʰ  |     3ʳᵈ    |   24,717ᵗʰ   |      275ᵗʰ     |    134,768  |    1,039    |    84     |
|20      |Medium 🔗 -  SOC Alert Triaging - Tinsel Triage  |4 |     100ᵗʰ  |     3ʳᵈ    |   25,202ⁿᵈ   |      286ᵗʰ     |    134,752  |    1,038    |    84     |
|19      |Medium 🔗 -  ICS/Modbus - Claus for Concern      |3 |     101ˢᵗ  |     3ʳᵈ    |   28,869ᵗʰ   |      337ᵗʰ     |    134,658  |    1,037    |    84     |
|19      |Easy 🔗 -  Passwords - A Cracking Christmas      |3 |     101ˢᵗ  |     3ʳᵈ    |   29,583ʳᵈ   |      340ᵗʰ     |    134,642  |    1,036    |    84     |
|18      |Easy 🔗 -  Prompt Injection - Sched-yule conflict|2 |     101ˢᵗ  |     3ʳᵈ    |   30,518ᵗʰ   |      353ʳᵈ     |    134,626  |    1,035    |    84     |
|18      |Medium 🔗 -  Obfuscation - The Egg Shell File    |2 |     101ˢᵗ  |     3ʳᵈ    |   30,967ᵗʰ   |      358ᵗʰ     |    134,618  |    1,034    |    84     |
|17      |Medium 🔗 - CyberChef - Hoperation Save McSkidy  |1 |     101ˢᵗ  |     3ʳᵈ    |   32,378ᵗʰ   |      374ᵗʰ     |    134,602  |    1,033    |    84     |
|7       |Medium 🔗 - Malware Analysis - Egg-xecutable     |2 |      95ᵗʰ  |     3ʳᵈ    |   11,604ᵗʰ   |      145ᵗʰ     |    134,544  |    1,034    |    84     |
|7       |Easy 🔗 - Network Discovery - Scan-ta Clause     |2 |      95ᵗʰ  |     3ʳᵈ    |   18,575ᵗʰ   |      208ᵗʰ     |    134,522  |    1,033    |    84     |
|7       |Easy 🔗 - React2Shell: CVE-2025-55182            |2 |      95ᵗʰ  |     3ʳᵈ    |   28,593ʳᵈ   |      326ᵗʰ     |    134,474  |    1,032    |    81     |
|6       |Medium 🔗 - IDOR - Santa´s Little IDOR           |1 |      95ᵗʰ  |     3ʳᵈ    |   27,309ᵗʰ   |      328ᵗʰ     |    134,450  |    1,031    |    81     |
|6       |Easy 🔗 - AI in Security - old sAInt nick        |1 |      95ᵗʰ  |     3ʳᵈ    |   41,626ᵗʰ   |      526ᵗʰ     |    134,426  |    1,030    |    81     |
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?        |1 |      95ᵗʰ  |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas              |1 |      96ᵗʰ  |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells               |1 |      97ᵗʰ  |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>

<p align="center">Global All Time:    101ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/9c2fe268-eeb8-4fe0-95cd-fd4c26850c05"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/ae1072ad-23e8-43fb-95d2-d8941b23ea6a"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/e2f37e96-3531-4b28-9d2e-baa6d546674e"><br><br>
                  Global monthly:  23,069ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/8408111b-1aba-4d2f-96c4-dfbc2568d1be"><br><br>
                  Brazil monthly:     256ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d782732e-ab2a-4b66-b0c3-824092605e5c"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
