<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 4 &nbsp;&nbsp; ·  &nbsp;&nbsp; AI in Security - old sAInt nick</h3>
<p align="center">2025, December 6  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Unleash the power of AI by exploring it's uses within cyber security. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/AIforcyber-aoc2025-y9wWQ1zRgB">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/8a97bcab-c344-47e2-9c66-1c5a83fd510f"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/1f5b6288-7ccf-4160-97c1-7c91d9c922f6"></p>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/f053c544-b2db-4e69-a7d4-d952ce09aaf0"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The lights glimmer and servers hum blissfully at The Best Festival Company (TBFC), melting the snow surrounding the data centre. TBFC has continued its pursuit of AI excellence. After the past two years, they realise that Van Chatty, their in-house chatbot, wasn’t quite meeting their standards.<br>

Unfortunately for the elves at TBFC, they are also not immune to performance metrics. The elves aim to find ways of increasing their velocity; something to manage the tedious, distracting tasks, which allows the elves to do the real magic.<br>

TBFC, adventurous as ever, is trialling their brand new cyber security AI assistant, Van SolveIT, which is capable of helping the elves with all their defensive, offensive, and software needs. They decide to put this flashy technology to use as Christmas approaches, to identify, confirm, and resolve any potential vulnerabilities, before any nay-sayers can.</p>

<h3>Learning Objectives</h3>
<p>

- How AI can be used as an assistant in cyber security for a variety of roles, domains and tasks<br>
- Using an AI assistant to solve various tasks within cyber security<br>
- Some of the considerations, particularly in cyber security, surrounding the use of AI</p>

<h3>Connecting to the Machine</h3>
<p>Before moving forward, review the questions in the connection card shown below:</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/a68e593e-4a65-4b74-b540-3373c955c49e"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Start your target VM by clicking thee <strong>Start Machine</strong>  button below. The machine will need about 2 minutes to fully boot. Additionally, start your AttackBox by clicking the <strong>Start AttackBox</strong> button below. The AttackBox will start in split view. In case you can not see it, click the <strong>Show Split View</strong> button at the top of the page.</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting both your AttackBox (if you're not using your VPN) and Target Machines, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.

<p><em>Answer the question below</em></p>

<p>1.1. &nbsp;&nbsp; <em>I have successfully started the AttackBox and the target machine!</em><br>
<code>No answer needed</code><p>

<h2>Task 2 &nbsp; ·  &nbsp; AI for Cyber Security Showcase</h2>
<h3>The Boom of AI Assistants</h3>
<p>Ah, yes, artificial intelligence, that buzzword that seems here to stay. Who would have thought? Today’s room will highlight some ways AI is utilised in cyber security, along with important considerations to bear in mind when deploying AI for such tasks.<br>

Particularly at the time of writing, AI is increasingly seen as a tool to boost speed by handling often tedious, time-consuming tasks, allowing humans to perform the real magic. Organisations want to see experience, not avoidance, in how these tools are operated.<br>

GPT this, GPT that, we’ve all heard it often. And it’s likely to persist. As AI’s capabilities expand daily, we’ve observed a shift from AI being just “something to ask because you were too lazy to Google” (a mistake I’ve made myself). Now, AI is being embedded into everyday workflows, transforming how tasks are done and boosting productivity like never before.<br>

With that said, let’s begin today’s room!</p>

<h3>AI in Cyber Security</h3>
<p>The use of artificial intelligence has seen a significant boost in cyber security. Visit almost any vendor, and they'll now have some form of AI powering a solution somewhere. Why? Well, it's not just because they're capitalising on the buzzword (although that's certainly a part of it), but rather, the benefits from artificial intelligence really do apply here. Let's explore some of these in the table below:</p>

<h6 align="center"><img width="450px" src="https://github.com/user-attachments/assets/9eec72e1-319c-448f-8430-bb1a298af176"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Defensive Security</h3>
<p>AI agents are being used in blue teaming to speed up detection, investigation, and response, making them quicker and more dependable. Acting like automated assistants, these agents continuously process telemetry (logs, network flows, endpoint signals) and add context to alerts. Furthermore, we are witnessing the integration of AI into vendor appliances—such as AI-assisted firewalling and intrusion detection systems.<br>

Beyond just detecting threats, AI can also assist in automating responses. Picture your system automatically isolating an infected device, blocking a suspicious email, or flagging an unusual login attempt — all in real time.</p>

<h3>Offensive Security</h3>
<p>AI agents have made a notable impact on offensive security by automating and handling the often very labourious and time-consuming tasks that a pentester might traditionally undertake.<br>

For example, AI can be a powerful tool in a penetration tester's workflow for reconnaissance and information gathering, from OSINT to analysing noisy scanner outputs and mapping attack surfaces. This allows the pentester to spend more time on the crucial tasks that require a human touch.</p>

<h3>Software</h3>
<p>AI-driven software development, rightfully, sounds a bit frightening. Isn't that so? Well, you wouldn't be wrong to feel this way; we've all heard about the popularity of vibe coding and the vulnerabilities introduced by AI.<br>

However, AI has proven to be a valuable addition to the software development process in several ways. One example is a virtual "colleague" to bounce ideas off while writing the code itself. More importantly, it is used as a SAST/DAST scanner. These scanners audit and analyse written code and applications for potential vulnerabilities.<br>

Yes, it's somewhat ironic. AI agents can be great at identifying vulnerabilities, but are not quite as effective at writing secure code.</p>

<h3>Considerations of AI in Cyber Security</h3>
<p>Now, I’m not entirely here to sing the praises of AI and say it’s the silver bullet to all your needs. If you’ve used AI before, you’ll know the pitfalls and frustrations one can face. And nowhere is that truer than in cyber security.<br>

While the usual considerations of using AI apply, such as not owning the output from AI, there are specific factors to consider before deploying it in cyber security.<br>

One such consideration is the use of AI in activities like offensive penetration testing. While we have discussed some of AI's applications in these areas, caution remains essential. You do not want to explain to a client that their services and websites are down because an AI has caused a race condition or overwhelmed their systems.<br>

We must think carefully about the data AI learns from, how transparent and fair its decisions are, and how reliable it remains when the unexpected occurs. We cannot assume the output from AI is 100% correct. Efforts must be made to verify the information it provides. Additionally, managing challenges such as keeping data private, securing AI models, and informing users properly requires careful consideration.</p>

<h3>Practical</h3>
<p>Phew! Ready for an exciting exercise? You will be interacting with Van SolveIT, who will guide you through three showcases of how AI can be used in cyber security:<br>

- <strong>Red</strong>: Generate and use an exploit script.<br>
- <strong>Blue</strong>: Analyse web logs of an attack that has occurred.<br>
- <strong>Software</strong>: Analyse source code for vulnerabilities.<br>

When you're ready, you can access Van SolveIT at <code>http://MACHINE_IP</code>. Remember, you will need to do so either from the AttackBox or your own device connected to the VPN.<br>

<em>If you are on a small display, we recommend expanding the AttackBox into full screen mode which can be done by pressing the "two arrows" icon (left of the "+" icon) in the split-screen view to expand it into full screen</em>.</p>

<h3>Usage Tips</h3>
<p>

- Chatbot responses may appear blank for a minute or two while it generates the reply. You will start to see Van SolveIT's responses in real time.<br>
- If the chatbot gets confused at any time, press the <strong>Restart Chat</strong> button at the top right of the page.<br>
- As you progress throughout the showcase, stages will unlock. You can go back to any stage that you have unlocked by clicking on the stage name on the top left.</p>

<p><em>Answer the questions below</em></p>

<br>
<p>2.1. &nbsp;&nbsp; <em>Complete the AI showcase by progressing through all of the stages. What is the flag presented to you?</em> Hint: Click the "Complete Stage" button on the left in the Van SolveIT web app when you are ready to proceed to the next stage. The flag will be presented once all stages have been completed.<br>
<code>THM{AI_MANIA}</code><p>

<p>

- <strong>Stage 1</strong>: click <strong>Complete Stage to Continue</strong><br>
- <strong>Stage 2</strong>: type <strong>yes</strong> and hit <strong>Enter</strong>. Click <strong>Complete Stage to Continue</strong><br>
- <strong>Stage 3</strong>: type <strong>analyse logs</strong> and hit <strong>Enter</strong>. Click <strong>Complete Stage to Continue</strong><br>
- <strong>Stage 4</strong>: type <strong>yes</strong> and hit <strong>Enter</strong>. Click <strong>Click to Complete Showcase</strong></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/92523255-a7e2-4305-a693-739b0da3026f"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/1bcfaefb-2076-4304-a828-5142c6d2a162"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/2612c751-38f4-4d3a-9e6d-49e6d68b092a"></p>

<br>
<p>2.2. &nbsp;&nbsp; <em>Execute the exploit provided by the red team agent against the vulnerable web application hosted at <code>http://MACHINE_IP</code>. What flag is provided in the script's output after it? Remember, you will need to update the IP address placeholder in the script with the IP of your vulnerable machine (<code>http://MACHINE_IP</code>)</em><br>
<code>THM{SQLI_EXPLOIT}</code><p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3df71c24-6a69-4615-9ad2-58ce3638c689"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/8c9d2efa-4458-4e11-81cd-775ef449ef14"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/e0ffdc3e-0478-4976-8a11-2c61f56e1157"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/27984c46-5da2-44ae-8085-b6dd034aaabc"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/f0b91b93-8e3f-46d7-851b-db142ab8c1fc"></p>

<br>
<p>2.3. &nbsp;&nbsp; <em>If you enjoyed today's room, feel free to check out the <a href="https://tryhackme.com/room/defadversarialattacks">Defending Adverserial Attacks</a> room, where you will learn how to harden and secure AI models.</em><br>
<code>No answer needed</code><p>


<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/973dfb58-fbf4-4d37-ad0b-bce769aadaa2"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/98e986ff-46d7-42c0-89fe-d02dc83bd130"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/6aa9da97-157f-4cb4-a699-1c2fcbe46bcf"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|6       |Easy 🔗 - AI in Security - old sAInt nick|  1  |      95ᵗʰ    |     3ʳᵈ    |   41,626ᵗʰ   |      526ᵗʰ     |    134,426  |    1,030    |    81     |
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?|  1  |      95ᵗʰ    |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas   |   1    |      96ᵗʰ    |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells    |   1    |      97ᵗʰ    |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>

<p align="center">Global All Time:     95ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/5e65146d-423c-42d8-84d0-35c26a61aee2"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/cbf75abb-6254-431b-beb6-6c6cd1c9e2f5"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/5193e48d-bf1d-4148-b57b-54aea559188b"><br><br>
                  Global monthly:  41,626ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/9170ce37-303e-47e6-955f-06587cc670d0"><br><br>
                  Brazil monthly:     526ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/ee63dea9-9285-44d5-b658-480584abd8f5"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

