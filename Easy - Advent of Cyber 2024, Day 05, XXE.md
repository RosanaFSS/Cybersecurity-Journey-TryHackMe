<h5 align="center">December 5, 2024<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{213}}$$-day-streak in  <a href="https://tryhackme.com/">TryHackMe</a>.</h5>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Advent of Cyber 2024}}$$</h1>

<h5 align="center">Dive into the wonderful world of cyber security by engaging<br>
in festive beginner-friendly exercises every day in the lead-up to Christmas!</h5>

<p align="center">
<img height="90px" hspace="20" src="https://github.com/user-attachments/assets/0d8d7f29-525a-49ad-85ba-9223bdec089b">
<img width="500px" src="https://github.com/user-attachments/assets/6ecf2478-64f0-4403-8a05-ceaa81611fee"></p>


<p align="center">Access this 🆓 TryHackMe CTF challenge clicking <a href="https://tryhackme.com/r/room/adventofcyber2024">Advent of Cyber 2024</a>.</p>

<h2 align="center"> $$\textcolor{yellow}{\textnormal{Day 5 - XXE}}$$<br>
$$\textcolor{yellow}{\textnormal{SOC-mas XX-what-ee?}}$$</h2>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/c10e152b-363e-441a-a2cb-6413e7acfffc"></p>

<br>

<p>The days in Wareville flew by, and Software's projects were nearly complete, just in time for Christmas. One evening, after wrapping up work, Software was strolling through the town when he came across a young boy looking dejected. Curious, Software asked, "What would you like for Christmas?" The boy replied with a sigh, "I wish for a teddy bear, but I know that my family can't afford one."

This brief conversation sparked an idea in Software's mind—what if there was a platform where everyone in town could share their Christmas wishes, and the Mayor's office could help make them come true? Excited by the potential, Software introduced the idea to Mayor Malware, who embraced it immediately. The Mayor encouraged the team to build the platform for the people of Wareville.

Through the developers' dedication and effort, the platform was soon ready and became an instant hit. The townspeople loved it! However, in their rush to meet the holiday deadline, the team had overlooked something critical—thorough security testing. Even Mayor Malware had chipped in to help develop a feature in the final hours. Now, it's up to you to ensure the application is secure and free of vulnerabilities. Can you guarantee the platform runs safely for the people of Wareville?</p>

<br>

<p align="center"><img height="200px" src="https://github.com/user-attachments/assets/62152f0a-d80b-4946-be33-b7a73ec10836"></p>

<br>

<h2><strong>Learning Objectives</strong></h2>
<ul style="list-style-type:square">
    <li>Understand the basic concepts related to XML.</li>
    <li>Explore XML External Entity (XXE) and its components.</li>
    <li>Learn how to exploit the vulnerability.</li>
    <li>Understand remediation measures.</li>
</ul></p>

<br>


<h2><strong>Connecting to the Machine</strong></h2>

<p>Before moving forward, review the questions in the connection card below:</p>

<p align="center"><img width="300px" src="https://github.com/user-attachments/assets/6a0436ab-d8a0-4a42-85c9-7680b003ba24"></p>

<p>Click on the green <code>Start Machine</code> button below to start the virtual machine. While the virtual machine starts, click on the <code>Start AttackBox</code> button at the top of the page and browse <code>Wareville's WishVille</code> application at <code>http://MACHINE_IP</code>. Please wait 1-2 minutes after the system boots completely to let the auto scripts run successfully.</p>

<p><code>Start Machine</code></p>

<br>
<h2><strong>Practical</strong></h2>
<p>Now that you understand the basic concepts related to XML and XXE, we will analyse an application that allows users to view and add products to their carts and perform the checkout activity. You can access the Wareville application hosted on http://MACHINE_IP. This application allows users to request their Christmas wishes.</p>

<br>
<h3><strong>Flow of the Application</strong></h3>
<p>As a penetration tester, it is important to first analyse the flow of the application. First, the user will browse through the products and add items of interest to their wishlist at http://MACHINE_IP/product.php. Click on the Add to Wishlist under Wareville's Jolly Cap, as shown below:</p>

![image](https://github.com/user-attachments/assets/c20d3c46-a7ad-49de-92e1-f8c2502562f6)

<p>After adding products to the wishlist, click the Cart button or visit http://MACHINE_IP/cart.php to see the products added to the cart. On the Cart page, click the Proceed to Checkout button to buy the items as shown below:</p>

![image](https://github.com/user-attachments/assets/2a270740-b8cf-4b96-a1d3-619f1b3b5c7c)

<p>On the checkout page, the user will be prompted to enter his name and address as shown below:</p>

![image](https://github.com/user-attachments/assets/98561977-8f6b-450e-8fae-026858f9e64c)

<p>Enter any name of your choice and address, and click on Complete Checkout to place the wish. Once you complete the wish, you will be shown the message "Wish successful. Your wish has been saved as Wish #21", as shown below:</p>

![image](https://github.com/user-attachments/assets/8206ba4f-2885-4b9f-841e-0b117098cc60)

<p>Wish #21 indicates the wishes placed by a user on the website. Once you click on Wish #21, you will see a forbidden page because the details are only accessible to admins. But can we try to bypass this and access other people's wishes? This is what we will try to perform in this task.</p>

![image](https://github.com/user-attachments/assets/539d3e95-a91d-40a2-a032-30b7397e9ee6)

<br>
<h2><strong>Intercepting the Request</strong></h2>
<p>Before discussing exploiting XXE on the web, let's learn how to intercept the request. First, we need to configure the environment so that, as a pentester, all web traffic from our browser is routed through Burp Suite. This allows us to see and manipulate the requests as we browse.<br>

We will use Burp Suite, a powerful web vulnerability scanner, to intercept and modify requests for this exploitation. You can access Burp Suite in the AttackBox. On the desktop of the AttackBox, you will see a Burp Suite icon as shown below:</p>

![image](https://github.com/user-attachments/assets/31db3300-a391-426b-b3b3-d42794ee4a0d)

<p>Once you click the icon, Burp Suite will open with an introductory screen. You will see a message like "Welcome to Burp Suite". Click on the Next button. </p>

![image](https://github.com/user-attachments/assets/ba1873f4-a1c4-4455-ac7a-e928060e99be)

<p>On the next screen, you will have the option to Start Burp. Click on the Start Burp button to start the tool.</p>

![image](https://github.com/user-attachments/assets/4325b553-6595-4424-b5c5-c3edf02dd0a5)

<p>Once Burp Suite has started, you will see its main interface with different tabs, such as Proxy, Intruder, Repeater and others.</p>

![image](https://github.com/user-attachments/assets/66cfbdc9-53a1-46df-8614-d7d6143d21ff)

<p>Inside Burp Suite, click the Settings tab at the top right. You will see Burp's browser option available under the Tools section. Enable Allow Burp's browser to run without a sandbox option and click on the close icon on the top right corner of the Settings tab as shown below:</p>

![image](https://github.com/user-attachments/assets/fe9c86d7-3b10-4868-b78c-5d830b82c05a)

<p>After allowing the browser to run without a sandbox, we would now be able to start the browser with pre-configured Burp Suite's proxy. Navigate to the Open browser option located at the Proxy -> Intercept section of Burp.  Open the browser by clicking the Open browser as shown below and browse the URL http://MACHINE_IP, so that all requests are intercepted: </p>

![image](https://github.com/user-attachments/assets/cb54b35d-73ac-48b6-9e68-7e4b5303dc33)

<p>Once you browse the URL, all the requests are intercepted and can be seen under the Proxy->HTTP history tab.</p>

![image](https://github.com/user-attachments/assets/bf80dff8-6087-4802-ad60-fc5ee0e056ba)


<br>
<h3><strong>What is Happening in the Backend?</strong></h3>
<p>Now, when you visit the URL, http://MACHINE_IP/product.php, and click Add to Wishlist, an AJAX call is made to wishlist.php with the following XML as input. </p>


![image](https://github.com/user-attachments/assets/ba478be4-201b-4b18-8c34-37173a66e84d)

<p>In the above XML, <product_id> tag contains the ID of the product, which is 1 in this case. Now, let's review the Add to Wishlist request logged in Burp Suite's HTTP History option under the proxy tab. As discussed above, the request contains XML being forwarded as a POST request, as shown below:</p>

![image](https://github.com/user-attachments/assets/34124554-5d55-4b6e-b86f-861c00c842b6)

<p>This wishlist.php accepts the request and parses the request using the following code:</p>

![image](https://github.com/user-attachments/assets/572e970e-19df-4c37-859d-e88ebdd91121)

<br>
<h3><strong>Preparing the Payload</strong></h3>

<p>When a user sends specially crafted XML data to the application, the line libxml_disable_entity_loader(false) allows the XML parser to load external entities. This means the XML input can include external file references or requests to remote servers. When the XML is processed by simplexml_load_string with the LIBXML_NOENT option, the web app resolves external entities, allowing attackers access to sensitive files or allowing them to make unintended requests from the server.<br>

What if we update the XML request to include references for external entities? We will use the following XML instead of the above XML:</p>

![image](https://github.com/user-attachments/assets/1a483131-b423-4605-b890-cfc12379c551)

<p>When we send this updated XML payload, the first two lines introduce an external entity called payload. The line <!ENTITY payload SYSTEM "/etc/hosts"> tells the XML parser to replace the &payload; reference with the contents of the file /etc/hosts on the server. When the XML is processed, instead of a normal product_id, the application will try to load and include the contents of the file specified in the entity (/etc/hosts).</p>

<br>
<h3><strong>Exploitation</strong></h3>

<p>Now, let's perform the exploitation by repeating the request we captured earlier. The Burp Suite tool has a feature known as Repeater that allows you to send multiple HTTP requests. We will use this feature to duplicate our HTTP POST request and send it multiple times to exploit the vulnerability. Right-click on the wishlist.php POST request and click on Send to Repeater.</p>

![image](https://github.com/user-attachments/assets/342157e7-56b5-4c75-bf80-49d410963f2c)

<p>Now, switch to the Repeater tab, where you'll find the POST request that needs to be modified. We will update the XML payload with the new data as shown below and then send the modified request:</p>

![image](https://github.com/user-attachments/assets/12e9c888-0447-4201-a30d-e9e8308e95b1)

<p>Place the mouse cursor inside the request in the Repeater tab in Burp Suite and press Ctrl+V  or paste the payload in the above-highlighted area.</p>

![image](https://github.com/user-attachments/assets/db7c9be2-fff4-4976-8990-20f01c508b5e)

<p>When we clicked Send, the server processed the malicious XML payload, which included the external entity reference to /etc/hosts. As a result, the wishlist.php responded with the contents of the /etc/hosts file, leading to an XXE vulnerability.</p>
<br>
<br>
<h2><strong>Time for Some Action</strong></h2>

<p>Now that you've identified a vulnerability in the application, it's time to see it in action! McSkidy Software has tasked us with finding loopholes, and we've successfully uncovered one in the wishlist.php endpoint. But our work doesn't end there—let's take it a step further and assess the potential impact this vulnerability could have on the application.<br>

Earlier, we discovered a page accessible only by administrators, which seems like an exciting target. What if we could use the vulnerability we've found to access sensitive information, like the wishes placed by the townspeople?</p>

<p align="center"><img height="200px" src="https://github.com/user-attachments/assets/6fca74e1-52be-4b07-a119-66f732324972"></p>

<p>Now that our objective is clear, let's leverage the vulnerability we discovered to read the contents of each wishes page and demonstrate the full extent of this flaw to help McSkidy secure the platform. To get started, let's recall the page that is only accessible by admins - /wishes/wish_1.txt. Using this path, we just need to guess the potential absolute path of the file. Typically, web applications are hosted on /var/www/html. With that in mind, let's build our new payload to read the wishes while leveraging the vulnerability.</p>
<p><strong>Note: Not all web applications use the path /var/www/html, but web servers typically use it.</strong></p>

<br>

![image](https://github.com/user-attachments/assets/858e573f-a5a5-4779-bfa9-06cf7495016c)

<br>

![image](https://github.com/user-attachments/assets/8b2fbb16-fbbd-45f6-8566-e11551aaf66e)

<p>Surprisingly, we got lucky that our assumption worked. The next thing to do is see whether we can view more wishes using our discovery. To do this, let's try replacing the wish_1.txt with wish_2.txt.</p>

![image](https://github.com/user-attachments/assets/80182dd0-0212-4147-a1f8-140e13518d4e)

<p>As a result, we were able to view the next wish. You may observe that we just incremented the number by one. Given this, you may continue checking the other wishes and see all the wishes stored in the application.

After iterating through the wishes, we have proved the potential impact of the vulnerability, and anyone who leverages this could read the wishes submitted by the townspeople of Wareville.</p>

<br>
<br>
<h2><strong>Conclusio</strong></h2>
<p>It was confirmed that the application was vulnerable, and the developers were not at fault since they only wanted to give the townspeople something before Christmas. However, it became evident that bypassing security testing led to an application that did not securely handle incoming requests.<br>

As soon as the vulnerability was discovered, McSkidy promptly coordinated with the developers to implement the necessary mitigations. The following proactive approach helped to address the potential risks against XXE attacks:</p>

- Disable External Entity Loading: The primary fix is to disable external entity loading in your XML parser. In PHP, for example, you can prevent XXE by setting libxml_disable_entity_loader(true) before processing the XML.<br>
- Validate and Sanitise User Input: Always validate and sanitise the XML input received from users. This ensures that only expected data is processed, reducing the risk of malicious content being included in the request. For example, remove suspicious keywords like /etc/host, /etc/passwd, etc, from the request.<br>

<p>After discovering the vulnerability, McSkidy immediately remembered that a CHANGELOG file exists within the web application, stored at the following endpoint: http://MACHINE_IP/CHANGELOG. After checking, it can be seen that someone pushed the vulnerable code within the application after Software's team.</p>

![image](https://github.com/user-attachments/assets/8a8ab936-0947-412c-bae1-af6f530a604b)

<p>With this discovery, McSkidy still couldn't confirm whether the Mayor intentionally made the application vulnerable. However, the Mayor had already become suspicious, and McSkidy began to formulate theories about his possible involvement.</p>

<p align="center"><img height="150px" src="https://github.com/user-attachments/assets/64288112-0c55-4e49-89e3-8dd991a4cbf0"></p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>What is the flag discovered after navigating through the wishes?</em><br><a id='1.1'></a>
>> <code><strong>THM{Brut3f0rc1n6_mY_w4y}</strong></code>

<br>

> 1.2. <em>What is the flag discovered after navigating through the wishes?</em><br><a id='1.2'></a>
>> <code><strong>THM{m4y0r_m4lw4r3_b4ckd00rs}</strong></code>

<br>

> 1.3. <em>If you want to learn more about the XXE injection attack, check out the XXE room! </em><br><a id='1.3'></a>
>> <code><strong>No answer needed</strong></code>

<br>

> 1.4. <em>Following McSkidy's advice, Software recently hardened the server. It used to have many unneeded open ports, but not anymore. Not that this matters in any way.</em><br><a id='1.3'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>My hands-on</h2>
<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 1](https://github.com/user-attachments/assets/099e3dfe-0299-4b5d-8edd-8c6bd9d00b95)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 2](https://github.com/user-attachments/assets/d67b13de-0790-47e6-a12c-c8758d1da5f5)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 3](https://github.com/user-attachments/assets/20659d36-e55d-40cd-83cf-25595ed3ef53)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 4](https://github.com/user-attachments/assets/ad347f0c-f704-448a-ae2b-6edc1853e485)

<br>

![5December 5, 2024  - TryHackMe - Day 5 - Image 4](https://github.com/user-attachments/assets/cd351c9f-03c7-474c-b48f-89b20c03231b)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 6](https://github.com/user-attachments/assets/bd993f41-f25f-4cf4-a81a-203d2e70ea13)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 7](https://github.com/user-attachments/assets/df9c51da-a9cf-4a6a-8026-450bd227c7ba)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 8](https://github.com/user-attachments/assets/15b070ba-c9a4-485f-891a-3569c5497ca8)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 9](https://github.com/user-attachments/assets/9fbf6816-e7b4-46da-b5f2-b6e0e3fc1b51)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 10](https://github.com/user-attachments/assets/8de829b6-c079-49a7-8874-340a4e35cc2c)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 11](https://github.com/user-attachments/assets/267dfbff-93fb-4077-8b1a-6d2127f3659a)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 12](https://github.com/user-attachments/assets/83abe69d-83e4-4f4d-aaa3-1433add391d0)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 13](https://github.com/user-attachments/assets/64b90e15-d96d-4fc3-ad5e-66875b2d02c7)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 14](https://github.com/user-attachments/assets/d998cab6-b41f-46b2-bed9-64fab11935b0)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 15](https://github.com/user-attachments/assets/5fe2ff53-bc39-4d89-8af6-043b46a177d7)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 16](https://github.com/user-attachments/assets/f509408c-51dc-41fe-9513-72fe05ff6459)

<br>

![December 5, 2024  - TryHackMe - Day 5 - Image 17](https://github.com/user-attachments/assets/daa1bf1e-1510-4178-ae51-e2d203465de8)



<br>
<br>

<h2>Task Completed<a id='2'></a></h2>
<p>Keep learning, keep growing!<br>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/e6a96032-935d-4289-8b2f-69d7ac4dbdcc"> </h3>


<h2>My Journey<a id='3'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| December 5, 2024  | 213      |     1,032 nd |        22 nd |    7,799 th |      71 st | 59,288   |       453 |

</div>


<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/fd80f7e4-a7af-4540-9211-d12c6c57eaab"> </h3>


<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>
