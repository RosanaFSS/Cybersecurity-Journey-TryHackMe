<h1 align="center"><a href="https://tryhackme.com/room/operationslitherIU">Operation Slither</a></h1>
<p align="center">Follow the leads and find who's behind this operation.<br><br><img width="1200px" src=""><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2031-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p
Follow the leads and find who's behind this operation.

<br>
<h2>Task 1 . The Leader</h2>

<h6 align="center"><img width="100px" src="https://github.com/user-attachments/assets/50fb1eec-96f9-4ce5-ade4-20d404e7b56f"><br>This image and all the<br>theoretical content of<br> the present article is<br> TryHackMe´s property.</h6>

<p><em>We got access to a hacker forum and found the info of our company on sale! All the info we have is in this post. Find any information related to the leader of the Sneaky Viper group.</em></p>

```bash
Full user database TryTelecomMe on sale!!!

As part of Operation Slither, we've been hiding for weeks in their network and have now started to exfiltrate information. 
This is just the beginning. We'll be releasing more data soon. Stay tuned!

@v3n0mbyt3_

---
```

<h3>Reconnaissance Guide</h3>
<p>

- Begin with the provided username and perform a broad search across common social platforms.<br>
- Correlate discovered profiles to confirm ownership and authenticity.<br>
- Review interactions, posts, and replies for potential leads.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. Aside from Twitter / X, what other platform is used by v3n0mbyt3_? Answer in lowercase.<br>
<code>Threads</code></p>

<br>
<p>1.2. What is the value of the flag?<br>
<code>THM{sl1th3ry_tw33tz_4nd_l34ky_r3pl13s!}</code></p>
<br>
<p><strong>Google Dorking</strong>, also known as <strong>Google Hacking</strong>, is a technique using advanced search queries to uncover information on the internet such as usernames, profiles, or public posts across the web. It leverages the capabilities of Google’s search algorithms to locate specific text strings within search results. Contrary to the illicit connotations of "hacking," <strong>Google Dorking</strong> itself is legal and is often utilized by security professionals to identify vulnerabilities in systems​​.</p>

<h3>Essential Google Dorking Queries for User Searching:</h3>
<p>
  
- <strong>Locate Profiles by Name</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; <code>site:linkedin.com/in "username"</code> or <code>site:twitter.com "username"</code>.<br>
- <strong>Find Usernames in URLs</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; <code>inurl:"/user/" "username"</code> or <code>inurl:"/members/" "username"</code>.<br>
- <strong>Search Profiles by Keyword</strong> &nbsp;&nbsp; : &nbsp; <code>site:site.com "username" "keywords"</code> (e.g., city, hobby).<br>
- <strong>Find Specific Files by User</strong> &nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; <code>site:example.com filetype:pdf "username"</code> to locate documents.<br>
- <strong>Search Cached Information</strong> &nbsp;&nbsp; : &nbsp; <code>cache:url</code> to view deleted or older versions of a user's page.<br>
- <strong>Cross-Reference Accounts</strong> &nbsp;&nbsp;&nbsp; : &nbsp; <code>("username" OR "fullname") -site:twitter.com</code> to see if a username appears elsewhere. </p>

<br>

<img width="1765" height="507" alt="image" src="https://github.com/user-attachments/assets/f4977885-5542-4dfd-8bb6-e9e754e96be9" />

<br>
<br>
<p>

- Click over the first <strong>Threads</strong>´ result.</p>

<img width="1897" height="648" alt="image" src="https://github.com/user-attachments/assets/5add93d2-7e4b-4b95-8bfb-ee138763825a" />

<br>
<br>
<p>

- Click on <strong>Replies</strong>.<br>
- Copy the encoded string: <strong>VEhNe3NsMXRoM3J5X3R3MzN0el80bmRfbDM0a3lfcjNwbDEzcyF9</strong>.</p>

<img width="1879" height="503" alt="image" src="https://github.com/user-attachments/assets/d537dfa1-c764-405b-9264-a12824c7e94f" />

<br>
<br>
<p>

- Paste it on <strong>CyberChef</strong>.<br>
- Decode <strong>From Base64</strong>.</p>

<img width="1904" height="237" alt="image" src="https://github.com/user-attachments/assets/a257477d-b547-4e3c-8524-aea8da154244" />


<br>
<br>
<br>
<h2>Task 2 . The Sidekick</h2>

<h6 align="center"><img width="100px" src="https://github.com/user-attachments/assets/37cce63a-082f-44b8-a0f0-548972d3faf3"><br><br>This image and all the<br>theoretical content of<br> the present article is<br> TryHackMe´s property.</h6>

<p><em>A second message has been made public! Our accountt in their forum was deleted, so we couldn't get the operator's handle this time. Follow the crumbs from the first task and hunt any information related to the second operator of the group.</em></p>

```bash
60GB of data owned by TryTelecomMe is now up for bidding!

Number of users: 64500000 Accepting all types of crypto
For takers, send your bid on Threads via this handle:

HIDDEN CONTENT 
----------------------------------------------------------------------------------------------------- 
You must register or log in to view this content
```

<h3>Reconnaissance Guide</h3>
<p>

- Use related usernames or connections identified in earlier steps to expand reconnaissance.<br>
- Enumerate additional platforms for linked accounts and shared content.<br>
- Follow media or resource references across platforms to trace information flow.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. What is the username of the second operator talking to v3n0mbyt3 from the previous platform?<br>
<code>_myst1cv1x3n_</code></p>
<p>

- Discovered the answer in <strong>1.2</strong>.</p>

<img width="1879" height="503" alt="image" src="https://github.com/user-attachments/assets/1d5208c4-1a99-4858-8eac-d303c7d8d44c" />

<br>
<br>
<br>
<p>2.2. What is the value of the flag?<br>
<code>THM{s0cm1nt_00ps3c_f1ng3r_m1scl1ck}</code></p>
<p>

- Navigate to <strong>whatsmyname.me</strong>.<br>
- Paste the operator name just discovered.<br>
- Click <strong>Search</strong>.</p>

<img width="1891" height="503" alt="image" src="https://github.com/user-attachments/assets/c26a80e7-f208-41ca-85b5-da2e50e5b3e1" />

<br>
<p>

- Click on the <strong>Visit Link</strong> of the second <strong>SoundCloud.com</strong> result.<br>
- Discover that there is a link to a second profile in SoundCloud <code>v1x3n</code> and a link for Instagam <code>v1x3nnnn__</code>.</p>

<img width="1864" height="663" alt="image" src="https://github.com/user-attachments/assets/7eb400bc-1373-4f23-9b18-393b7f54477d" />

<br>
<p>

- Search for <code>v1x3n</code> via <strong>whatsmyname.me</strong>.<br>
- Click on the second link discovered in <strong>SoundCloud.com</strong> for <code>v1x3n_</code>.</p>

<img width="1869" height="330" alt="image" src="https://github.com/user-attachments/assets/3c5ccd29-f632-42f0-9bd8-d5e3b48917a8" />

<br>
<p>

- Note that <code>v1x3n_</code> has <code>4</code> tracks with the name starting with <code>Prototype</code>.<br>
- Note that <code>Prototype</code> <code>2</code> has <code>3</code> <strong>Reposts</strong> and <code>4</code> <strong>Likes</strong> despite the others that do not have any.<br>
- Test another approach:<br>Copy _myst1cv1x3n_´s profile image.<br>Search via Google for <strong>Exact Matches</strong>.<br>Discover <code>v1x3n_</code> profile in <strong>SoundCloud</strong>.</p>

<img width="1881" height="898" alt="image" src="https://github.com/user-attachments/assets/3002c077-5f85-43a3-aebf-412363907f18" />

<br>
<br>

<img width="1743" height="427" alt="image" src="https://github.com/user-attachments/assets/ee0697b7-b0a0-422f-b142-29197573b3a1" />


</p>

- Click on  <code>Prototype</code> <code>2</code>.<br>
- Copy the encoded string: <strong>VEhNe3MwY20xbnRfMDBwczNjX2Yxbmczcl9tMXNjbDFja30=</strong>.</p>

<img width="1892" height="851" alt="image" src="https://github.com/user-attachments/assets/1ad78c1e-04be-4ac3-bfcb-8b4b9d6ad253" />

<br>
<p>
  
- Paste it on <strong>CyberChef</strong>.<br>
- Decode <strong>From Base64</strong>.</p>

<img width="1902" height="234" alt="image" src="https://github.com/user-attachments/assets/0cbbf4e6-a9f2-45e3-9616-57014e2027d6" />

<br>
<br>
<br>
<h2>Task 3 . The Last Operator</h2>
                                
<h6 align="center"><img width="100px" src="https://github.com/user-attachments/assets/6007eba8-3c88-48ae-905d-20012bbfcc0f"><br><br>This image and all the<br>theoretical content of<br> the present article is<br> TryHackMe´s property</h6>

<p><em>A new post is up. Hunt the third operator using past discoveries and find any details related to the infrastructure used for the attack.</em></p>

```bash
FOR SALE

Advanced automation scripts for phishing and initial access!

Inclusions:
- Terraform scripts for a resilient phishing infrastructure 
- Updated Google Phishlet (evilginx v3.0)
- GoPhish automation scripts
- Google MFA bypass script
- Google account enumerator
- Automated Google brute-forcing script
- Cobalt Strike aggressor scripts
- SentinelOne, CrowdStrike, Cortex XDR bypass payloads

PRICE: $1500
Accepting all types of crypto
Contact me on REDACTED@protonmail.com 

---
```

<h3>Reconnaissance Guide</h3>
<p>

- Identify secondary accounts through visible interactions (likes, follows, collaborations).<br>
- Extend reconnaissance into developer or technical platforms associated with the identity.<br>
- Analyse activity history (such as repositories or commits) for embedded information.</p>

<p><em>Answer the questions below</em></p>

<p>3.1. What is the handle of the third operator?<br>
<code>sh4d0wF4NG</code></p>

<p>

- Click <strong>View all</strong> in the <strong>FOLLOWERS</strong> section of <strong>SoundCloud.com</strong>.</p>

<img width="1809" height="428" alt="image" src="https://github.com/user-attachments/assets/949b83e9-5f60-4339-bdd7-8aadcae85104" />

<br>
<br>

<img width="1891" height="330" alt="image" src="https://github.com/user-attachments/assets/7599be9a-fbc5-4919-af7a-9747c02acfbd" />

<br>
<br>

<img width="1880" height="683" alt="image" src="https://github.com/user-attachments/assets/5dbc0c25-5d8f-40e7-b403-fa21e83b4e06" />

<br>
<br>
<br>
<p>3.2. What other platform does the third operator use? Answer in lowercase.<br>
<code>GitHub</code></p>
<p>
  
- Navigate to <strong>whatsmyname.me</strong>.<br>
- Paste the operator name just discovered.<br>
- Click <strong>Search</strong>.<br>
- Navigate to the <strong>GitHub</strong> result.</p>

<img width="1847" height="638" alt="image" src="https://github.com/user-attachments/assets/abc6ca01-9644-4221-8e45-9c64db0d1b35" />

<br>
<br>

<img width="1846" height="837" alt="image" src="https://github.com/user-attachments/assets/464c49da-0da1-41cb-80ea-2767e2c74729" />

<br>
<br>
<br>
<p>3.3. What is the value of the flag?<br>
<code>THM{••••••••••••••••••••••••••••}</code></p>
<p>

  
- Click on <strong>red-team-infra</strong>.<br>
- Click on <strong>Activity</strong>.</p>


<img width="1663" height="668" alt="image" src="https://github.com/user-attachments/assets/e636bc52-5b61-4421-9b1d-cda0199d3807" />

<br>
<br>

<img width="1639" height="841" alt="image" src="https://github.com/user-attachments/assets/681823f5-0e9f-46b7-99b1-20fb5d05f34a" />

<br>
<p>
  
- Click on <strong>Created new gophish script</strong>.</p>

<img width="1678" height="730" alt="image" src="https://github.com/user-attachments/assets/deb0c891-8dd0-4bb1-8168-20a8c12678ac" />

<br>
<p>
  
- Click on the parent commit.<br>
- Scroll down.<br>
- Copy the value<br>
- Paste it on <strong>CyberChef</strong>.<br>
- Decode <strong>From Base64</strong>.</p>


<img width="1897" height="519" alt="image" src="https://github.com/user-attachments/assets/a32393d9-e23c-4750-956b-d8e0681cb213" />

<br>
<br>

<img width="1889" height="378" alt="image" src="https://github.com/user-attachments/assets/b3572258-10ba-491c-8e45-982dee59d69f" />

<br>
<br>

<img width="1909" height="234" alt="image" src="https://github.com/user-attachments/assets/2a3960b3-6e6d-4fa1-acaf-0da02dad2ff2" />

<br>
<br>
<br>








