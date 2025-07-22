
<h1 align="centerFollina MSDT</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/c0f58782-fd5e-49ad-9990-d7e2466b1f87"><br>
<em>A walkthrough on the CVE-2022-30190, the MSDT service, exploitation of the service vulnerability, and consequent detection techniques and remediation processes</em>.<br>
Access it <a href="https://tryhackme.com/room/follinamsdt">here</a>.<br><br>
July 22, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>442</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="1200px" src=""></p>

<br>

<h2>Task 1 . Introduction</h2>

<br>

<h3 align="left"> Answer the question below</h3>

<p>1.1. Hope you enjoy this room<br>
<code>No answer needed</code></p>


<br>

<h2>Task 2 . CVE-2022-30190</h2>
<p>The MSDT exploit is not something new - in fact, a bachelor’s thesis has been published August of 2020 regarding techniques on how to use MSDT for code execution. Almost two years after that initial publication, pieces of evidence of MSDT exploitation as well as code execution via Office URIs has triggered several independent researchers to file separate reports to MSRC, the latter of which has been patched (specifically in Microsoft Teams) whereas the former remained vulnerable.<br><br>

It’s not until the discovery of nao_sec, which has been made public in twitter, that attacks using this particular vector is actively being made in the wild. This is consequently picked up by Kevin Beaumont who publicly identified it as a zero day that Microsoft EDR products are failing to detect, and then later classified by Microsoft as a zero day with the vulnerability name CVE-2022-30190</p>

<p>Summarized timeline of its discovery:

- August 1st 2020  — A bachelor thesis is published detailing how to use MSDT to execute code<br>
- March 10th 2021  — researchers report to Microsoft how to use Microsoft Office URIs to execute code using Microsoft Teams as an example. Microsoft fail to issue a CVE or inform customers, but stealth patched it in Microsoft Teams in August 2021. They did not patch MSDT in Windows or the vector in Microsoft Office (Link)<br>
- April 12th 2022  — first report to Microsoft MSRC of exploitation in wild via MSDT, by leader of Shadowchasing1, an APT hunting group. This document is an in the wild, real world exploit targeting Russia, themed as a Russian job interview<br>

<img width="1212" height="562" alt="image" src="https://github.com/user-attachments/assets/e2287b53-32cb-47c9-95b8-26962ea5462a" />

- April 21st 2022  — Microsoft MSRC closed the ticket saying not a security related issue (for the record, msdt executing with macros disabled is an issue)<br>

<img width="1400" height="354" alt="image" src="https://github.com/user-attachments/assets/c93c614a-7c7a-44cc-a796-9447c99fffbb" />

- May 27th 2022  — Security vendor Nao tweet a document uploaded from Belarus, which is also an in the wild attack.<br>
- May 29th 2022  — Kevin Beaumont identified this was a zero day publicly as it still works against Office 365 Semi Annual channel, and ‘on prem’ Office versions and EDR products are failing to detect<br>
- May 31st 2022  — Microsoft classify this a zero day in Microsoft Defender Vulnerability Management<br>

<img width="630" height="573" alt="image" src="https://github.com/user-attachments/assets/37507ad4-4c9e-4c94-9425-d64e22f5e4d3" />

- June 14th 2022  — a fix for this vulnerability, CVE-2022–30190, is available in June 2022’s Patch Tuesday</p>

<p>Further readings::<br>

- Follina — a Microsoft Office code execution vulnerability | by Kevin Beaumont | May, 2022 | DoublePulsar<br>
- Full timeline, early details regarding the vulnerability, and “Follina” namesake courtesy of Kevin Beaumont<br>
- Rapid Response: Microsoft Office RCE - “Follina” MSDT Attack (huntress.com)
</p>

<br>

<h3 align="left"> Answer the questions below</h3>

<p>2.1. Hope you enjoy this room<br>
<code>No answer needed</code></p>
