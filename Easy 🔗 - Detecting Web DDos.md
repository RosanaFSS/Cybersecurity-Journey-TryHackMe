<h1 align="center">Detecting Web DDos</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/ab52f61f-cea2-4e50-bf2c-34d7f50b396e"><br>
2025, September 18<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>500</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Explore denial-of-service attacks, detection techniques, and strategies for protection</em>.<br>
Access it <a href="https://tryhackme.com/room/detectingwebddos">here</a>.<br>
<img width="1200px" src=""https://github.com/user-attachments/assets/8b3f17b3-9029-47fb-b302-345456c3a709"></p>

<h1 align="center">Task 1 . Introduction</h1>
<p><strong>Denial-of-Service (DoS)</strong> attacks can take many forms, but their ultimate aim is to disrupt or completely block access to a website or web service. In this room, you will explore how DoS and DDoS attacks target the application layer, the techniques behind them, and how you, as a defender, can detect and mitigate these common threats.</p>
<h3 align="center">Objectives</h3>
<p>

- Learn how denial-of-service attacks function<br>
- Understand attacker motives behind the disruptive attacks<br>
- See how web logs can help you reveal signs of web DoS and DDoS<br>
- Get practice analyzing denial-of-service attacks through log analysis<br>
- Discover detection and mitigation techniques defenders can use</p>

<h3 align="center">Prerequisites</h3>
<p>

- Check out <a href="https://tryhackme.com/room/securityprinciples">Security Principles</a> for an overview of the CIA triad<br>
- Complete <a href="https://tryhackme.com/room/webapplicationbasics">Web Application Basics</a> to learn HTTP methods and codes<br>
- Work through <a href="https://tryhackme.com/room/websecurityessentials">Web Security Essentials</a> for web infrastructure basics<br>
- Review <a href="https://tryhackme.com/room/splunk101">Splunk: Basics</a> for an overview of Splunk searches</p>

<h3 align="center">Virtual environment set up</h3>

<p><em>Answer the question below</em></p>

<p>1.1. I understand the learning objectives and am ready to embark on a Denial-of-Service adventure!<br>
<code>No answer needed</code></p>

<br>
<h1 align="center">Task 2 . DoS and DDos Attacks</h1>
<br>

<p><em>Answer the questions below</em></p>

<p>2.1. What class of attack relies on disrupting the availability of a web service?<br>
<code>Denial-of-Service</code></p>

<br>
<p>2.2. What class of attack relies on disrupting the availability of a web service?<br>
<code>Botnet</code></p>

<br>
<h1 align="center">Task 3 . Attack Motives</h1>
<br>

<p><em>Answer the questions below</em></p>

<p>3.1. Which attacker motive aims to make customers lose confidence in a company?<br>
<code>Reputational Damage</code></p>

<br>
<p>3.2. Which motive most likely drove the 2023 DDoS attack against Microsoft?<br>
<code>Hacktivism</code></p>

<br>
<h1 align="center">Task 4 . Log Analysis</h1>
<p>Web server logs are a valuable source of evidence when investigating denial-of-service attacks. Every major web service, whether Apache, NGINX, or Microsoft IIS, records web requests in a somewhat standardized log format. By examining these logs, analysts and responders can uncover patterns that help distinguish between normal user traffic and malicious activity. In this task, we will look at some key indicators of a potential DoS and DDoS attack, and highlight the strengths and limitations of relying on logs for detection.<br>

From the previous tasks, we know that denial-of-service attacks often rely on sending a flood of HTTP requests to the target, but can also utilize individually specially crafted web requests to halt a service.<br>

Take a look at the indicators below:</p>

<img width="728" height="451" alt="image" src="https://github.com/user-attachments/assets/1b055f5d-f3eb-4113-880c-8dbeecfc27f0" />

<p>Analysts should look for multiple, layered signals forming a picture of a DDoS attempt. For example, imagine an attacker controlling a worldwide botnet aimed at a single site. You might see requests from a wide range of IP addresses across different geographic regions. These requests could hammer several resource-intensive endpoints with the same User-Agent string or a variety to appear more legitimate. Maintaining a watchlist of common indicators to be on the lookout for can be a valuable tool in an analyst's arsenal.</p>

<h2 align="center">Targeted Resosurces</h2>
<p>If an attacker aims to disrupt a web service like we've discussed, they will likely focus on endpoints that consume the most server resources per request or are most critical to maintain site functionality. Pages like /login or search forms are prime targets because each request forces the server to query a database, validate input, and return results. This makes the requests far more expensive to process than static content like product pages or images.<br>

Commonly targeted endpoints and reasoning:<br>

- /login - involves authentication processes<br>
- /search - requires complex database queries<br>
- /api endpoints - critical for dynamic content delivery<br>
- /register or /signup - requires database writes and validation<br>
- /contact or /feedback - requires database entries and can trigger email notifications<br>
- /cart or /checkout - requires session management, inventory checks, and payment processing<br>

<h2 align="center">Log Sample</h2>
<p>Let's examine a sample condensed access log to see how a DoS attack might appear in a post-incident scenario.<br>

- Normal User Traffic - Every few seconds, a user requests a page and receives a response as expected<br>
- DoS Attack - Beginning at 10:01:10, you can see the IP address 203.0.113.55 begin to send repeated GET requests to /login.php<br>
- Web Server Down - Users are requesting pages and receiving 503 responses indicating the service is unavailable<br>

This log snippet is highly condensed, and a DoS or DDoS may have hundreds or thousands of requests flooding the logs simultaneously</p>

<img width="690" height="330" alt="image" src="https://github.com/user-attachments/assets/85f5ba17-70ba-4972-9ec8-b12e06c40a7a" />

<h2 align="center">Hands On</h2>
<p>Your bicycle parts website has undergone a denial-of-service attack. Open up the access.log file on the user's Desktop to begin your investigation. The logs include a mix of normal user-generated traffic and attacker traffic. While you comb the logs, be on the lookout for repeated requests to the same page and remember the indicators you learned about in this task. Best of luck!</p>

<img width="378" height="329" alt="image" src="https://github.com/user-attachments/assets/cc9fbe02-6a7c-4d9a-ad65-b80a8f8746f3" />

<br>
<p><em>Answer the questions below</em></p>

<p>3.1. What is the attacker’s IP address?<br>
<code>203.12.23.195</code></p>

<img width="1304" height="525" alt="image" src="https://github.com/user-attachments/assets/ee3c61a1-03b1-4e8f-857b-d06c43316e36" />

<br>
<br>
<p>3.2. Which page is repeatedly targeted by the attacker’s requests?<br>
<code>/login</code></p>

<br>
<p>3.3.After the attack, what error code do legitimate users receive?<br>
<code>503</code></p>

<img width="1040" height="529" alt="image" src="https://github.com/user-attachments/assets/4ade4559-be96-4ba9-96ef-1c17eeaf1d79" />

<br>
<br>
<h1 align="center">Task 5 . Leveraging SIEMs</h1>
<br>

<p><em>Answer the questions below</em></p>

<p>5.1. What was the most frequently requested uri?<br>
<code>/search</code></p>

<img width="1309" height="383" alt="image" src="https://github.com/user-attachments/assets/a8fc5627-543b-48dd-b84d-988bfb618a62" />

<br>
<br>
<p>5.2. Which clientip made the first request to the target uri?<br>
<code>203.0.113.12</code></p>

```bash
index="main" uri="/search"
|  timechart span=1ms count by uri
```

<img width="1305" height="479" alt="image" src="https://github.com/user-attachments/assets/719bee43-6398-4c29-bd27-755393b765e5" />

<br>
<br>

<img width="1314" height="584" alt="image" src="https://github.com/user-attachments/assets/6e32b801-97b0-46c8-8946-5ca4e0d378c2" />

<br>
<br>
<p>5.3.How many IP addresses were part of the botnet that attacked your website?br>
<code>/search</code></p>

```bash
index="main" "GET /search"
| stats dc(clientip) as Unique_Clientip
```

<img width="1309" height="268" alt="image" src="https://github.com/user-attachments/assets/cfc32b66-c281-4159-8e8a-7f392ece6765" />

<br>
<br>
<p>5.4. Which useragent was most commonly used by the attacking traffic?<br>
<code>Java/1.8.0_181</code></p>

```bash
index="main" uri="/search"
|  stats count by useragent
|  sort -count
```

<img width="1306" height="416" alt="image" src="https://github.com/user-attachments/assets/58e56628-8d6a-4c81-a43a-c853c815aa37" />

<br>
<br>
<p>5.5. Use the timechart command to visualize the requests.
What is the peak number of requests made per second during the attack?<br>
<code>207</code></p>

```bash
index="main" uri="/search"
| timechart span=1s count by request
```

<img width="1308" height="449" alt="image" src="https://github.com/user-attachments/assets/38e91199-12f6-4227-bd98-58c41405aedb" />

<p>5.6. Which legitimate (non-attacking) clientip received the first 503 response status post-attack?<br>
<code></code></p>

```bash
index="main" status="503" NOT uri="/search"
| sort 0 _time
| head 1
| table clientip, _time, status, _raw
```

<img width="1314" height="387" alt="image" src="https://github.com/user-attachments/assets/ac9f3c2a-02be-47a4-9453-75a3989f0073" />

<br>
<h1 align="center">Task 6 . Defense</h1>
<br>


<p><em>Answer the questions below</em></p>

<p>6.1. What type of security challenge blocks bots by asking users to solve a simple puzzle?<br>
<code>CAPTCHA</code></p>

<p>6.2. Which legitimate (non-attacking) clientip received the first 503 response status post-attack?<br>
<code>Load-balancing</code></p>

<br>
<h1 align="center">Task 7 . Conclusion</h1>
<p>In this room, you explored different types of <strong>Denial-of-Service</strong> attacks, how they work, and the motives behind them, supported by some real-world examples. You practiced identifying DoS and DDoS activity in web server logs by analyzing common indicators and learned how SIEM platforms help analysts investigate and manage large volumes of traffic. Through a hands-on Splunk exercise, you uncovered evidence of a DDoS attack. Finally, you examined how CDNs and WAFs can help defend websites and applications against these attacks.</p>

<p><em>Answer the question below</em></p>

<p>7.1. Complete the room and continue on your cyber learning journey!<br>
<code>No answer needed</code></p>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/95a56f23-4515-4a44-956e-8612e232b8ab"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/68ab774c-a607-4598-9ff5-9063936d8230"></p>

<h1 align="center">Celebrated a 500 day-streak</h1>
<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/ee075564-9cf8-4688-95a7-6644166fa3e7"></p>

<h1 align="center">Earned one streak freeze</h1>
<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/563cbd02-4a41-4683-b832-6e2d2ae074a0"></p>

<br>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|-------------:|------------:|------------:|------------:|------------:|------------:|
|18      |Easy 🔗 - <code><strong>Detecting Web DDos</strong></code>| 500| 106ᵗʰ| 4ᵗʰ   |     312ⁿᵈ   |     4ᵗʰ    | 126,674  |    970    |    76     |
|17      |Medium 🔗 - DLL Hijacking              | 499    |     106ᵗʰ    |      4ᵗʰ     |     348ᵗʰ   |     7ᵗʰ    | 126,554  |    969    |    75     |
|17      |Medium 🔗 - The Docker Rodeo           | 499    |     106ᵗʰ    |      4ᵗʰ     |     346ᵗʰ   |     7ᵗʰ    | 126,546  |    968    |    75     |
|17      |Easy 🔗 - Linux Logging for SOC        | 499    |     106ᵗʰ    |      4ᵗʰ     |     345ᵗʰ   |     7ᵗʰ    | 126,538  |    967    |    74     |
|16      |Hard 🚩 - TryHack3M: TriCipher Summit  | 498    |     107ᵗʰ    |      4ᵗʰ     |     364ᵗʰ   |     7ᵗʰ    | 126,420  |    966    |    74     |
|16      |Easy 🔗 - Chaining Vulnerabilities     | 498    |     108ᵗʰ    |      5ᵗʰ     |     365ᵗʰ   |     7ᵗʰ    | 126,420  |    965    |    74     |
|15      |Medium 🔗 - AppSec IR                  | 497    |     108ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ   |     7ᵗʰ    | 126,404  |    964    |    74     |
|14      |Hard 🚩 - Misguided Ghosts, in progress| 496    |     108ᵗʰ    |      5ᵗʰ     |     389ᵗʰ   |     6ᵗʰ    | 126,300  |    963    |    74     |
|14      |Hard 🚩 - VulnNet: Endgame             | 496    |     108ᵗʰ    |      5ᵗʰ     |     394ᵗʰ   |     6ᵗʰ    | 126,270  |    963    |    74     |
|13      |Hard 🚩 - Royal Router                 | 495    |     107ᵗʰ    |      5ᵗʰ     |     388ᵗʰ   |     6ᵗʰ    | 126,160  |    962    |    74     |
|13      |Medium 🚩 - Void Execution             | 495    |     107ᵗʰ    |      5ᵗʰ     |     383ʳᵈ   |     6ᵗʰ    | 126,120  |    961    |    73     |
|12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ   |     6ᵗʰ    | 126,056  |    960    |    73     |
|12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ   |     9ᵗʰ    | 125,606  |    959    |    73     |
|11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ   |     9ᵗʰ    | 125,516  |    958    |    73     |
|11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ   |     9ᵗʰ    | 125,516  |    958    |    73     |
|10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ   |     9ᵗʰ    | 125,428  |    957    |    73     |
|10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ   |     9ᵗʰ    | 125,292  |    956    |    73     |
|9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ   |     9ᵗʰ    | 125,236  |    955    |    73     |
|9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ   |    10ᵗʰ    | 125,146  |    954    |    73     |
|9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ   |    10ᵗʰ    | 125,016  |    953    |    73     |
|8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
|8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
|7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
|7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
|7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
|6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
|6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
|6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
|6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
|5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
|5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
|4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
|4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	     5ᵗʰ    |     579ᵗʰ     |    10ᵗʰ    | 124,018  |   940     |    73     |
|3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
|2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
|1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   106ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/e7eea077-9846-4757-8a08-28cb20ca4b77"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/bba9b762-2f66-4520-a18c-00d71d9fd4bb"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/9a1bd97a-06bf-455f-8913-adaa8667bafc"><br><br>
                  Global monthly:    312ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/e26a6034-c1b9-44ad-8326-8a0bb50b7fbd"><br><br>
                  Brazil monthly:      4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/072ff665-3c90-49e4-a917-945d08db8c09"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
