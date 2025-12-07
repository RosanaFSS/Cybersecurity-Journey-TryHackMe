<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 5 &nbsp;&nbsp; ·  &nbsp;&nbsp; IDOR - Santa´s Little IDOR</h3>
<p align="center">2025, December 6  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Learn about IDOR while helping pentest the TrypresentMe website. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/idor-aoc2025-zl6MywQid9">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/9ba40c0b-c005-410a-bfad-fcf2f20b81dd"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/a352ac17-edc0-4da5-b967-796680ab91be"></p>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/d327946f-b57b-425a-8eb3-2050bab5e754"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The elves of Wareville are on high alert since McSkidy went missing. Recently, the support team has been receiving many calls from parents who can't activate vouchers on the TryPresentMe website. They also mentioned they are receiving many targeted phishing emails containing information that is not public. The support team is wary and has enlisted the help of the TBFC staff. When looking into this peculiar case, they discovered a suspiciously named account named Sir Carrotbane, which has many vouchers assigned to it. For now, they have deleted the account and retrieved the vouchers. But something is going on. Can you help the TBFC staff investigate the TryPresentMe website and fix the vulnerabilities?</p>

<h3>Learning Objectives</h3>
<p>

- Understand the concept of authentication and authorization<br>
- Learn how to spot potential opportunities for Insecure Direct Object References (IDORs)<br>
- Exploit IDOR to perform horizontal privilege escalation<br>
- Learn how to turn IDOR into SDOR (Secure Direct Object Reference)</p>

<h3>Connecting to the Machine</h3>
<p>Before moving forward, review the questions in the connection card shown below:</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/a1b70744-ced4-4934-aa1b-4ba0eed15fd2"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Start your target VM by clicking thee <strong>Start Machine</strong> button below. The machine will need about 2 minutes to fully boot. Additionally, start your AttackBox by clicking the <strong>Start AttackBox</strong> button below. The AttackBox will start in split view. In case you can not see it, click the Show Split view button at the top of the page. Inside your AttackBox, open a web browser and navigate to the TryPresentMe application at <code>/code> http://MACHINE_IP</code>.</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting both your AttackBox (if you're not using your VPN) and Target Machines, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p><em>Answer the question below</em></p>

<p>1.1. &nbsp;&nbsp; <em>My target machine and the AttackBox have started and I am ready to learn about IDOR.</em><br>
<code>No answer needed</code><p>

<h2>Task 2 &nbsp; ·  &nbsp; IDOR on the Shell</h2>
<h3>It’s Dangerously Obvious, Really</h3>
<p>Have you ever seen a link that looks like this: <code>https://awesome.website.thm/TrackPackage?packageID=1001?</code><br>

When you saw a link like this, have you ever wondered what would happen if you simply changed the packageID to 11 or 12? In its simplest form, this can be a potential case for IDOR.<br>

IDOR stands for <strong>Insecure Direct Object Reference</strong> and is a type of access control vulnerability. Web applications often use references to determine what data to return when you make a request. However, if the web server doesn't perform checks to ensure you are allowed to view that data before sending it, it can lead to serious sensitive information disclosure. A good question to ask then is:<br>

<em>Why does this happen so often</em>?<br>

We need to understand references and web development a bit more to answer this. Let's take a look at what a table storing these package numbers from our link example could look like:</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/3ce6f0ec-2d3d-4039-bd2d-5db064e90160"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>If the user wants to know the status of their package and makes a web request, the simplest method is to allow the user to supply their packageID. We recover data from the database using the simplest SQL query of:<br>

<code>SELECT person, address, status FROM Packages WHERE packageID = value;</code><br>

However, since packageID is a sequential number, it becomes pretty obvious to guess the packageIDs of other customers, and since the web application isn't verifying that the person making the request <strong>is the same</strong> person as the one who owns the package, an IDOR vulnerability appears, allowing attackers to recover the details for packages belonging to other users. Even worse is when a feature like this doesn't require a user to authenticate, then there would be no way to even tell who is making the request! To dive a bit deeper, we need to understand authentication, authorization, and privilege escalation.</p>

<p><strong>A note from one of the co-authors of this task</strong>: I am not a fan of the vulnerability name IDOR. I prefer the name authorization Bypass. If you want to understand my reasoning, expand here, but you don't have to be bored with the details!</p>

<br>
<h3>It Doesn´t Obviously Ralate</h3>
<p>The full term, Insecure Direct Object Reference, sounds fancy, but it doesn’t really describe what’s going wrong. The “Direct Object Reference” part just means that a system uses an ID (like <code>/user/1</code>) to point to something. That’s not the problem. The real issue is that the system doesn’t check whether the person making the request is allowed to access it.<br>

A lot of people try to “fix” IDORs by hiding or encoding IDs. For example, changing <code>/user/1</code> to <code>/user/ea21f09b2</code>. That might make it look harder to guess, but if the server still isn’t checking permissions, it’s just as insecure. The vulnerability isn’t about how the object is referenced, it’s about missing authorization checks.<br>

That’s why I prefer to call it an Authorization Bypass instead. It explains exactly what’s happening: someone is bypassing the rules that decide who can see or change something. Whether the ID is a number, a hash, or a random string, the risk stays the same if the server doesn’t verify access. You can read more  <a href="https://www.mwrcybersec.com/whats-the-deal-with-idor">here</a> if you want.</p>

<br>
<h3>Identity Defines Our Reach</h3>
<p>To understand the root cause of IDOR, it is important to understand the basic principles of authentication and authorization:<br>

- <strong>Authentication</strong>: The process by which you verify who you are. For example, supplying your username and password.<br>
- <strong>Authorization</strong>: The process by which the web application verifies your permissions. For example, are you allowed to visit the admin page of a web application, or are you allowed to make a payment using a specific account?<br>

You may think that authentication only happens once when you supply your username and password, but that is actually not the case! After providing your credentials, you receive a cookie or a token, called session information. Every subsequent request you make to the application includes this session information, which is verified by the application. This initial verification process is still authentication and happens for each request. This is why websites will often redirect you back to the login page. It means your session information has expired, and thus, you need to reauthenticate with your credentials to receive new session information.<br>

Authorization cannot happen before authentication. If the application doesn't know who you are, it cannot verify what permissions your user has. This is very important to remember. If your IDOR doesn't require you to authenticate (login or provide session information), such as in our package tracking example, we will have to fix authentication first before we can fix the authorization issue of making sure that users can only get information about packages they own.<br>

The last bit of theory to cover is privilege escalation types:<br>

- <strong>Vertical privilege escalation</strong>: This refers to privilege escalation where you gain access to more features. For example, you may be a normal user on the application, but can perform actions that should be restricted for an administrator.<br>
- <strong>Horizontal privilege escalation</strong>: This refers to privilege escalation where you use a feature you are authorized to use, but gain access to data that you are not allowed to access. For example, you should only be able to see your accounts, not someone else's accounts.<br>

IDOR is usually a form of horizontal privilege escalation. You are allowed to make use of the track package functionality. But you should be restricted to only performing that tracking action for packages you own. Now that we understand the theory, let's look at how to exploit IDOR practically!</p>


<br>
<h3>Iterate Digits, Observe Responses</h3>
<p>Let's start with the simplest example of IDOR. On the web application, let's authenticate to the application using the details below.</p>

<br>
<h3>Credentials</h3>

<p>Once authenticated, you should see a dashboard like this:</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/2a177d0e-c5be-4f97-a816-2d5c5fdb3bb0"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Let's start by using the Developer Tools of our browser to better understand what is happening in the background. Right-click on the page and click Inspect, then click on the Network tab as shown below:</p>

<h6 align="center"><img width="1000px" src="https://github.com/user-attachments/assets/9edaada2-a06b-4ab2-8f26-e0cb08598cab"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Now let's refresh the page and see what requests are being made. It should look something like this:</p>

<img width="1440" height="303" alt="image" src="https://github.com/user-attachments/assets/653427ea-42df-41d1-bc85-ad9da2ebd8e4" />


<p>Let's take a closer look at the view_accountinfo request. Click on it and you will see the following:</p>

<img width="688" height="752" alt="image" src="https://github.com/user-attachments/assets/101f3cec-4944-4156-8e2a-82824f543c1d" />


<p>In the above image we can see that the user_id with the value of 10 was used for the request. If we click and expand the Response tab, we can see that this user_id corresponds to our user:</p>

<img width="459" height="359" alt="image" src="https://github.com/user-attachments/assets/4782bc6d-926d-47c2-9fda-03b843ca9361" />


<p>This tells us that the application is using our user_id as the reference for getting details. Let's see what happens when we change this. In the Developer Tools, navigate to the Storage tab and expand the Local Storage dropdown on the left side and click the URL inside it:</p>

<img width="1437" height="219" alt="image" src="https://github.com/user-attachments/assets/2465a4ed-bee8-4416-bf90-8b472f1240c6" />


<p>Let's change the user_id to 11 and see what happens. Double-click on the Value field of the auth_user data entry, update the user_id to 11 and save it by pressing Enter. Now refresh the page. All of a sudden it seems like you are a completely different user!<br>

This is the simplest form of IDOR. Simply changing the user_id to something else means we can see other users' data. Some IDORs might be slightly more hidden. Just because you don't see a direct number doesn't mean it doesn't exist! Let's dive deeper. To continue onto the next challenges of the task, go and change the id back to 10 using the same steps you followed above. Alternatively, you can log out of the application and log back in using the username and password.</p>

<br>
<h3>In Disguise: Obvious References</h3>
<p>Sometimes, IDOR may not be as simple as just a number. In certain cases, encoding may have been used. On the loaded profile, click the eye icon next to the first child as shown on the image below.</p>

<img width="1386" height="583" alt="image" src="https://github.com/user-attachments/assets/15520e7f-7c02-40c6-8afa-8e073c86d0d6" />


<p>Now go back to the Network tab and take a look at the requests being made; you should see a request like this:</p>

<img width="1440" height="495" alt="image" src="https://github.com/user-attachments/assets/35b88f0b-437c-49ec-b325-f77bdd8b7c57" />


<p>Simply put, the Mg== is just the base64 encoded version of the number 2. You could still perform IDOR using this request, but you would have to base64 encode the number first.</p>

<br>
<h3>In Digests, Objects Remain</h3>
<p>Encoding isn't the only thing that can be used to hide potential IDOR vulnerabilities. Sometimes the values may look like a hash, such as MD5 or SHA1. If you want to see what that would look like, take a look at the request that happens when you click the edit icon next to a child.</p>

<img width="1437" height="469" alt="image" src="https://github.com/user-attachments/assets/2568cbcd-fc89-4366-88a3-2bd3f9f6d40d" />


<p>While the string may look random, upon further investigation, you can see that it is a type of hash. If we understand what value was used to generate the hash, we can perform an IDOR attack by simply replicating the hashing function. Using something like a hash identifier can help you quickly understand what hashing algorithm is being used and can often tell you what data was hashed.</p>

<br>
<h3>It´s Deterministic, Obviously Reproducible</h3>
<p>Sometimes you have to dig quite deep for IDOR. Sometimes IDOR is not as clear. Sometimes the IDOR stems from the actual algorithm being used. In this last case, let's take a look at our vouchers. While the values may look random, we need to investigate what algorithm was used to generate them. Their format looks like a UUID, so let's use a website such as UUID Decoder to try to understand what UUID format was used. Copy one of the vouchers to the website for decoding, and you should see something like this:</p>

<img width="1144" height="686" alt="image" src="https://github.com/user-attachments/assets/398ce814-ecc0-44f2-abb3-51cd51c37cfc" />


<p>While these look completely random, we can see that the UUID version 1 was used. The issue with UUID 1 is that if we know the exact date when the code was generated, we can recover the UUID. For example, suppose we knew the elves always generated vouchers between 20:00 - 21:00. In that case, we can create UUIDs for that entire time period (3600 UUIDs since we have 60 minutes, and 60 seconds in a minute), which we could use in a brute force attack to aim to recover a valid voucher and get more gifts.<br>

Now that we have seen the various IDORs that can be found, let's discuss how to fix them and avoid them!</p>


<br>
<h3>Improve Design, Obliterate Risk</h3>
<p>Now that we learned about what IDOR is, let's discuss how to fix it. The best way to stop IDOR is to make sure the server checks who is asking for the data every time. It's not enough to hide or change the ID number; the system must confirm that the logged-in user is authorized to see or change that information.<br>

Don't rely on tricks like Base64 or hashing the IDs; those can still be guessed or decoded. Instead, keep all the real permission checks on the server. Whenever a request comes in, check: "Does this user own or have permission to view this item?"<br>

Use random or hard-to-guess IDs for public links, but remember that random IDs alone don't make your app safe. Always test your app by trying to open another user's data and making sure it's blocked. Finally, record and monitor failed access attempts; they can be early signs of someone trying to exploit an IDOR.</p>

<p><em>Answer the questions below</em></p>

<br>
<p>2.1. &nbsp;&nbsp; <em>What does IDOR stand for?</em><br>
<code>Insecure Object Direct Reference</code><p>

<br>
<p>2.2. &nbsp;&nbsp; <em>What type of privilege escalation are most IDOR cases?</em><br>
<code>Horizontal</code><p>

<br>
<p>2.3. &nbsp;&nbsp; <em>Exploiting the IDOR found in the <code>view_accounts</code> parameter, what is the <code>user_id</code> of the parent that has 10 children?</em> Hint: Using the task example, change the ID value of your token and refresh the page. Work in incrementing steps from your user's ID.<br>
<code>15</code><p>

<img width="1310" height="107" alt="image" src="https://github.com/user-attachments/assets/cefdae9e-60a3-4838-bf86-d0bb2f07333c" />

<img width="1310" height="407" alt="image" src="https://github.com/user-attachments/assets/88bb15a0-3d72-4138-80a6-17eafbaa0624" />

<img width="1128" height="147" alt="image" src="https://github.com/user-attachments/assets/51f8b3ae-7b8a-4b45-afde-bb240c62eb83" />

<img width="1157" height="361" alt="image" src="https://github.com/user-attachments/assets/20e05043-4fca-4d10-affc-63e1e83b40e7" />

<img width="1159" height="196" alt="image" src="https://github.com/user-attachments/assets/45a08d8c-61d9-4e76-b2c2-2e358164a965" />

<br>
<p>2.4. &nbsp;&nbsp; <em><strong>Bonus Task</strong>: If you want to dive even deeper, use either the base64 or md5 child endpoint and try to find the <code>id_number</code> of the child born on 2019-04-17? To make the iteration faster, consider using something like Burp's Intruder. If you want to check your answer, click the hint on the question.</em><br>
<code>No answer needed</code><p>




<br>
<p>2.5. &nbsp;&nbsp; <em><strong>Bonus Task</strong>: Want to go even further? Using the <code>/parents/vouchers/claim</code> endpoint, find the voucher that is valid on 20 November 2025. Insider information tells you that the voucher was generated exactly on the minute somewhere between 20:00 - 24:00 UTC that day. What is the voucher code? If you want to check your answer, click the hint on the question.</em><br>
<code>No answer needed</code><p>

<img width="1161" height="151" alt="image" src="https://github.com/user-attachments/assets/be9b8aa9-c2f3-4fbd-9e16-dc640a8f607a" />



<p>2.6. &nbsp;&nbsp; <em>If you enjoyed today's room, check out our complete IDOR room!</em><br>
<code>No answer needed</code><p>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/51bee370-35cc-4cb2-b8b3-11059723c767"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/ca244b28-ea88-4720-b8d0-b7e35b9526aa"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/abb5cb1e-ab01-492b-902e-19077dcf58f3"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|6       |Medium 🔗 - IDOR - Santa´s Little IDOR|  1     |      95ᵗʰ    |     3ʳᵈ    |   27,309ᵗʰ   |      328ᵗʰ     |    134,450  |    1,031    |    81     |
|6       |Easy 🔗 - AI in Security - old sAInt nick|  1  |      95ᵗʰ    |     3ʳᵈ    |   41,626ᵗʰ   |      526ᵗʰ     |    134,426  |    1,030    |    81     |
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?|  1  |      95ᵗʰ    |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas   |   1    |      96ᵗʰ    |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells    |   1    |      97ᵗʰ    |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>


<p align="center">Global All Time:     95ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/d4ffdef2-46c2-4194-beef-80250e8a7b1e"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/50743277-85ec-43f7-ab79-85ccbc8278d9"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/3dae05b5-61aa-46cb-8f98-22b36b89b63e"><br><br>
                  Global monthly:  27,309ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/0b002fa8-36c9-4724-b126-7d723728920c"><br><br>
                  Brazil monthly:     328ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b9e077c5-6a75-4b3b-97dd-e4ee50f8362e"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>


