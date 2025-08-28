<h1 align="center">Web Security Essentials</h1>
<p align="center">2025, August 28<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>479</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn how the web works, common website security risks, and protections for a safer internet.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/f5632150-32ef-4139-8e38-0bc699bf2d1a"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/websecurityessentials">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/24850cd1-b2af-4559-b6a8-961c4a5e83a8"></p>

<br>

<h2 align="center">Task 1 . Introduction</h2>
<p>The internet is behind many aspects of modern life, from banking and shopping to social media and beyond. As a result, websites and web applications are among attackers' most targeted assets. Whether you're defending a company's website or investigating an incident, understanding how the web works and how to secure it is crucial.</p>

<h3 align="center">Learning Objectives</h3>

<p>

- Understand the shift from desktop applications to web applications<br>
- Learn why web applications are common targets for attackers<br>
- Explore web infrastructure and the tools we use to protect the web<br>
- Practice applying security measures to harden a new web application<br>
</p>


<h3 align="center">Prerequisites</h3>
<p>

- <a href="https://tryhackme.com/room/webapplicationbasics">Web Application Basics</a> provides an excellent overview of the essentials of web applications<br>
- Complete <a href="https://tryhackme.com/room/httpindetail">HTTP In Detail</a> to brush up on web requests, response codes, and all things HTTP</p>

<p><em>Answer the question below</em></p>

<p>1.1. I understand the learning objectives and am ready to learn about web security!<br>
<code>No answer needed</code></p>

<br>
<h2 align="center">Task 2 . Why Web?</h2>
<p>The shift from desktop to web-based applications has been ongoing for decades. In the 1990s, desktop applications were the norm because of speed and connectivity limitations. As web technology advanced, the 2000s gave way to much more widely used dynamic web applications for email, social media, and banking. In the 2010s, there was a massive rise in cloud computing and software as a service (SaaS), and today, nearly everything can be done in a browser.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/e6037956-d218-4614-aa67-f58c4c2e90db"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3 align="center">From a Security Perspective</h3>
<p>The shift to web apps brings some amazing advantages, including increased accessibility, faster updates, better compatibility, and reduced resource usage on the user's end. Think of it, you can browse online marketplaces and social networks, play games, edit images and video, and even run virtual machines all through your browser. However, these benefits come with tradeoffs in terms of security. The more powerful and widespread the web becomes, the more opportunities it introduces for attackers.<br>

Web applications are among the most common entry points for attackers because they are always available and exposed. They often connect to back-end systems like databases and other infrastructure, offering attackers high-impact opportunities. A vulnerable web application is often the first stage in a larger attack sequence. Let's take a look at the risks faced by both web app owners and their users.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/7aa1440d-ad92-4539-8da4-d7420d33a5d3"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3 align="center">Real-World Examples</h3>

<p>In 2017,  <a href="https://archive.epic.org/privacy/data-breach/equifax/">Equifax´s</a> sensitive customer data of nearly 150 million Americans was compromised due to an Apache <a href="https://www.cve.org/CVERecord?id=CVE-2017-5638">Equifax´s</a>. By abusing this vulnerability, the attackers were able to access internal databases storing valuable customer data.<br>

<a href="https://www.capitalone.com/digital/facts2019/">Capital One</a> faced a similar-scale breach in 2019, in which a misconfigured web application firewall (WAF) exposed over 100 million customers' sensitive personal and financial information. This misconfiguration allowed internal access to the company's cloud infrastructure and databases.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. Have applications shifted from desktop to web over the past couple of decades (Yea/Nay)?<br>
<code>Yea</code></p>

<p>2.2. Who is ultimately responsible for ensuring the security of users' data within a web application?<br>
<code>Web App Owner</code></p>

<br>
<h2 align="center">Task 3 . Web Infrasctructure</h2>
<p>When you visit a website, your browser sends a request to a web server. The server processes the request, verifies access, and returns a response to the user. This response can be a webpage, an image, or data like search results or your account information. This request-response cycle is the foundation of how the web functions. Attackers can abuse this request-response cycle by overwhelming servers with requests, bypassing access controls, or even tricking the server into executing harmful commands.</p>

<h3 align="center">Components of a Web Service</h3>
<p>For example, any web service, like <a href="https://tryhackme.com/">tryhackme.com</a>, requires three main components to function.

- <strong>Application</strong>: The code, images, styles, and icons that dictate how the website looks and functions.<br>
- <strong>Web Server</strong>: This component hosts the application. It listens for requests and returns a response to the user.<br>
- <strong>Host Machine</strong>: The underlying operating system, Linux or Windows, that runs the web server and the application.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/649ed413-c41e-4740-b302-7a4c84d0cdfc"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>In the next task, we will investigate the security measures available to protect these three components.</p>

<h3 align="center">Web Servers</h3>
<p>When you visit a website, your web browser sends a request to a web server, as discussed above. Web servers listen for incoming requests and return an appropriate response. Web servers are positioned in front of websites and applications, making them a crucial aspect of the internet's foundation. Because they are publicly exposed and handle all incoming web requests, web servers are a common target for attackers.</p>

<p>Here are some of the most common web servers that you will encounter.<br>

- <strong>Apache</strong>: The most popular web server to host simple websites and blogs, most commonly WordPress.<br>
- <strong>Nginx</strong>: An industry standard for high-performance web apps. Used by companies like Netflix, Airbnb, and GitHub.<br>
- <strong>Internet Information Services (IIS)</strong>: A Microsoft-developed web server commonly used in enterprise environments.</p>


<p><em>Answer the questions below</em></p>

<p>3.1. What does your web browser send to a server to receive a web page?<br>
<code>Request</code></p>

<p>3.2. What web server is most commonly used to host WordPress websites?<br>
<code>Apache</code></p>

<p>3.3. What do we call the OS and environment that runs the web server and application?<br>
<code>Host Machine</code></p>

<br>
<h2 align="center">Task 4 . Protecting the Web</h2>

<h3 align="center">Best Practices</h3>
<p>Various security measures are available when securing websites and web applications. Some solutions provide visibility, while others can actively stop or limit an attack, commonly known as mitigation. Referencing Task 3, where we discussed the three essential components of any web service: the application, the web server, and the host machine, let's now examine the protections available for each of these components.</p>

<h4 align="center"><strong>Protecting the Application</strong></h4>
<p>

- Secure Coding: Avoid insecure functions, ensure proper handling of errors, and remove sensitive information.<br>
- Input Validation & Sanitization: Validate and sanitize user input to prevent injection attacks.<br>
- Access Control: Restrict access based on user roles.</p>

<h4 align="center"><strong>Protecting the Web Server</strong></h4>
<p>

- Logging: Keep a detailed record of all web requests with access logs.<br>
- Web Application Firewall (WAF): Filter and block harmful traffic based on defined rules.<br>
- Content Delivery Network (CDN): Reduce direct exposure to your server and use integrated WAFs.</p>

<h4><strong>Protecting the ost Machine</strong></h4>
<p>

- Least Privilege: Use low-privilege users for services.<br>
- System Hardening: Disable unnecessary services and close unused ports.<br>
- Antivirus: Add endpoint-level protection that blocks known malware.</p>

<h4 align="center"><strong>Security Tips for All Three Components</strong></h4>
<p>

- Strong Authentication: Don't just let anyone access your code, admin panels, or host machine.<br>
Patch Management: Ensure your app dependencies, web server, and host machine are up to date.</p>

<h3 align="center">Logging</h3>
<p>Web servers can create logs for every request they receive. We call these access logs, and they are incredibly valuable from a security perspective because they track information about every interaction with the server, including the client's IP address, timestamp, requested page or data, response status from the server, and user agent. These fields can play an important role in investigations, helping analysts detect potential malicious activity and trace attacker behavior.<br><br>

Let's take a look at a benign series of events that we might find in an access log to get a feel for the type of data we can observe.<br>
Note that <code>GET</code> requests are used to retrieve a resource from the server, like a specific web page.<br>
<code>POST</code> requests are used to submit data to the server, such as login credentials.<br><br>

- The user, from the client IP <code>10.10.10.100</code>, visits the website's homepage at <code>/index.html</code>.
- Next, they navigate to the login page at <code>/login.html</code>.
- They then enter their credentials and submit the form, signified by the <code>POST</code> request.
- Finally, they access their account page at <code>/myaccount.html</code>.<br><br>

Although this series of events is expected and not out of the ordinary, you can see how the verbosity of these logs can help analysts and incident responders reconstruct a possible attack sequence.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/ff8862e6-29f0-4c52-a6cf-b6b00e67d2a3"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the questions below</em></p>

<p>4.1. What cyber security concept involves stopping or limiting damage from threats?<br>
<code>mitigation</code></p>

<p>4.2. What security control involves ensuring all software and components are up to date?<br>
<code>Patch Management</code></p>

<br>
<h2 align="center">Task 5 . Defense Systems</h2>
<h3 align="center">Content Delivery Network (CDN)</h3>
<p><strong>CDN</strong>s store and serve cached content from servers closer to the user to reduce latency. Imagine you have a main server housed in a central location. This main server provides information to edge servers worldwide so your customers can access data more quickly and safely. Aside from speed, CDNs also help in a security sense by acting as a buffer between the user and the origin server.</p>

<h4 align="center"><strong>Security Benefits</strong></h4>

<p>

- IP Masking: Hides the origin server IP address, which makes it harder for attackers to target.<br>
- DDoS Protection: CDNs can absorb a large amount of traffic, making denial-of-service attacks less effective.<br>
- Enforced HTTPS: Encrypted communication via TLS is enforced by default by most CDNs.<br>
- Integrated WAF: Many CDNs, including Cloudflare CDN, Amazon CloudFront & Azure Front Door, integrate web application firewalls.</p>

<p>In essence, CDNs allow web apps to deliver data to customers more efficiently and securely.</p>

<h3 align="center">Web Application Firewall (WAF)</h3>
<p><strong>WAF</strong>s are a powerful tool that can be integrated as another layer of protection for websites and web applications. They inspect incoming HTTP traffic and block or log potentially harmful requests based on security rules. Think of the analogy of a bouncer at a bar or club. Every person (web request) that wants to enter must be checked by the bouncer (firewall). Anyone (any request) that doesn't meet the standard requirement will be rejected.<br>

Let's take a closer look at the types of WAFs available to us as defenders, then dive deeper into their functionality.</p>

<p>

- Cloud-based (Reverse Proxy): Sits in front of the web server. These WAFs are easy to deploy and have great scalability.<br>
- Host-based: Software deployed directly on the web server and offers control for each application.<br>
- Network-based: A physical or virtual appliance situated on the network perimeter. More suited for enterprise environments.</p>

<h4 align="center"><strong>Functionatility</strong></h4>
<p>As stated above, WAFs inspect HTTP requests to detect anomalies, attacks, or known suspicious patterns. Below are some of the methods used, along with examples of requests that may be blocked.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/588ee2eb-3beb-4081-90ad-4e2fabb8b99c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The above table is not exhaustive, as detection methods are constantly evolving, and custom rules can be created based on the specific needs of the web application owner.

Below is a screenshot of the Cloudflare dashboard for <code>tryhackme.thm</code>, focused on the security panel. In it, we can see all requests for the last 24 hours, including requests blocked by the integrated web application firewall.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/2faf9f92-5fa4-4d17-baab-77566700cbb7"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3 align="center">Antivirus (AV)</h3>

<p><strong>AV</strong>s are often misunderstood as a blanket protection measure, but they are primarily made to safeguard endpoints, such as desktops, laptops, and servers, from known malicious files and programs. Most AVs rely on signature-based detection, which means they compare files with a database of known malware or patterns.<br>

While web attacks usually target the application layer, not the host machine, AVs still play an important role in host protection, as discussed in Task 3. They can help detect malicious file uploads, such as web shells, post-exploitation tools, and other malicious software. AVs are just one layer in a broader defense-in-depth strategy and should be combined with other security measures to provide stronger protection.</p>


<p><em>Answer the questions below</em></p>

<p>5.1. Which type of Web Application Firewall operates by running on the same system as the application itself?<br>
<code>host-based</code></p>

<p>5.2. Which common WAF detection technique works by matching incoming requests against known malicious patterns?<br>
<code>signature-based</code></p>

<br>
<h2 align="center">Task 6 . Practice Scenario</h2>

<p><em>Answer the questions below</em></p>
<p>Let's take a more hands-on look at the security measures you've learned about in this room by applying them to a real-world scenario. Your site, Secure-A-Site, is currently being developed and will be deployed soon. Your goal is to help prepare the web application, web server, and host machine for launch by ensuring they are as secure as possible. </p>

<p>You'll work through the three layers and apply the best practices that you learned about in the previous tasks:<br>

- Web Application<br>
- Web Server<br>
- Host Machine</p>

<h3 align="center">Practice</h3>
<p align="center">[ View Site ]</p>
<p align="center">Open <strong>Secure-A-Site</strong> by clicking the <strong>View Site</strong> button above. Once you complete each section, claim the flags and answer the task questions!</p>

<h6 align="center"><img width="300px" src="https://github.com/user-attachments/assets/99876d70-98a5-48c2-91ad-5bf793327abd"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<br>

<p>6.1. What flag did you receive for securing the Web Application?<br>
<code>THM{****************}</code></p>

<br>
<br>

<p align="center"><strong>Welcome to Secure-A-Site!</strong><br>Help prepare your site for launch bysecuring each component of your web service.<br>Answer the questions and claim the flags!<br><img width="700px" src="https://github.com/user-attachments/assets/30a37e47-7b14-47b2-9ce0-bd951b00b127"><br>Rosana´s Practice</p>

<br>
<br>

<p align="center"><strong>Secure your Web Application 1 of 3</strong><br><img width="700px" src="https://github.com/user-attachments/assets/1ebf1050-5549-4b8f-9fbc-5d549b23c1f1"><br>Rosana´s Practice</p>

<br>
<br>

<p align="center"><strong>Secure your Web Application 2 of 3</strong><br><img width="700px" src="https://github.com/user-attachments/assets/a2a9a3d2-bf73-4cce-b3f3-39ec11fe655b"><br>Rosana´s Practice</p>

<br>
<br>

<p align="center"><strong>Secure your Web Application 2 of 3</strong><br><img width="700px" src="https://github.com/user-attachments/assets/dd2c5f48-1603-4d17-aca8-9a9ed42c2fb8"><br>Rosana´s Practice</p>

<br>
<br>
<p>6.2. What flag did you receive for securing the Web Server?<br>
<code>THM{**********************}</code></p>

<br>
<br>

<p align="center"><strong>Secure your Web Server 1 of 3</strong><br><img width="700px" src="https://github.com/user-attachments/assets/f3e1b481-8c43-4d3a-a909-4fe4c9d62619"><br>Rosana´s Practice</p>

<br>
<br>

<p align="center"><strong>Secure your Web Server 2 of 3</strong><br><img width="700px" src="https://github.com/user-attachments/assets/70814993-ce74-4f6d-bdd7-74187637678f"><br>Rosana´s Practice</p>

<br>
<br>

<p align="center"><strong>Secure your Web Server 3 of 3</strong><br><img width="700px" src="https://github.com/user-attachments/assets/f1bb9e36-491c-46b0-85d2-5a9589f1b642"><br>Rosana´s Practice</p>

<br>
<br>
<p>6.3. What flag did you receive for securing the Host Machine?<br>
<code>THM{***********************}</code></p>

<br>
<br>

<p align="center"><strong>Secure your Host Machine 1 of 3</strong><br><img width="700px" src="https://github.com/user-attachments/assets/17964ec5-62ae-420a-b8b9-c7e6f3d4c264"><br>Rosana´s Practice</p>

<br>
<br>

<p align="center"><strong>Secure your Host Machine 2 of 3</strong><br><img width="700px" src="https://github.com/user-attachments/assets/c8cc5ac0-4593-495d-b82b-bdd31ea7775e"><br>Rosana´s Practice</p>

<br>
<br>

<p align="center"><strong>Secure your Host Machine 3 of 3</strong><br><img width="700px" src="https://github.com/user-attachments/assets/c7cc5a69-0751-4877-86ee-7456c512e0e2"><br>Rosana´s Practice</p>

<br>
<br>

<p align="center"><strong>Practice Completion</strong><br><img width="700px" src="https://github.com/user-attachments/assets/a7b7b386-5d5a-4bbb-a899-717a2f70b4cc"><br>Rosana´s Practice</p>

<br>
<br>
<h2 align="center">Task 7 . Conclusion</h2>
<p>In this room, you explored the essentials of web security, starting with the shift from traditional desktop applications to modern web applications. You learned why web applications are targeted by attackers, often holding sensitive data and serving as entry points into larger systems. We covered how web requests and servers work. Finally, we learned about the protections used by security professionals to prevent, detect, and mitigate common threats to web applications.</p>

<p><em>Answer the question below</em></p>

<p>7.1. Complete the room and continue on your cyber learning journey!<br>
<code>No answer needed</code></p>

<br>

<br>

