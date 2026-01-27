<h1 align="center"><a href="https://tryhackme.com/room/first-shift-ctf">First Shift CTF</a> &nbsp;&nbsp; · &nbsp;&nbsp; Zero Trust</h1>
<p align="center">If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2026-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>


<h2>Zero Trust</h2>
<p>It was supposed to be a regular morning at ProbablyFine Ltd. L2 had just returned from paternity leave. L3 was hosting a live webinar on "Proactive Threat Hunting." The morning standup was the usual mix of coffee, ticket updates, and small talk about last night's football match. Then the Slack notification came through from Sales:<br>

"<strong>NEW CLIENT ONBOARDED - VaultSecure Banking - Tier 1 Priority - Live monitoring starts NOW</strong>"

VaultSecure Banking wasn't just any client. They're a regional bank with two million customers. They had just fired their previous MSSP after a compliance audit revealed endpoints that had gone unmonitored for six months. The contract ProbablyFine signed was massive, enough to fund the company for the next two years. However, there’s a catch: a 90-day probation period with a "zero tolerance" clause - miss one critical alert, and the contract is terminated.</p>


<h2>The Alert</h2>
<p>You were barely skimming the onboarding docs before the SIEM lights up with a critical alert:<br>

"<strong>CRITICAL: Suspicious Persistence Mechanism Detected - VaultSecure Banking</strong>"<br>

You just stare at it for a second. It's been less than 4 hours since monitoring went live, and you're already staring at a critical alert. Your L2 is in back-to-back meetings with the new client. Your L3 is live on a webinar with 500 attendees. The company's future literally depends on how you handle this. For now, it's just you and this alert. It's time to show VaultSecure Banking why they chose ProbablyFine!</p>

<h2>Machine Access</h2>
<p>Start the lab by clicking the Start Machine button below. You will then have access to the Splunk Web Interface. Please wait 4-5 minutes for the Splunk instance to launch. To access Splunk, please follow this link:<br>

- <a href="https://lab_web_url.p.thmlabs.com/en-US/app/search/search?q=search%20index%3D*&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=0&latest="> Splunk Web Interface</a><br>

You may also need downloadable artifacts from the compromised VM:<br>

- Google Drive <a href="https://drive.google.com/file/d/1YLn1Os_kfeeZadjG4cevcJBXheV06XCt/view?usp=sharing"> Link</a></p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p><em>Answer the questions below</em></p>

<br>
<p>6.1. <em>What is the hostname where the Initial Access occurred?</em><br>
<code>JP-BROWN-WS</code></p>


