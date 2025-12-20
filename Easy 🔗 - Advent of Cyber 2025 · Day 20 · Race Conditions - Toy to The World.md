<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 20 &nbsp;&nbsp; ·  &nbsp;&nbsp; Race Conditions - Toy to The World</h3>
<p align="center">2025, December 20  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in <a href="https://tryhackme.com">TryHackMe</a>.<br>Learn how to exploit a race condition attack to oversell the limited-edition SleighToy. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/race-conditions-aoc2025-d7f0g3h6j9">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/539fe70d-298d-47f6-bcd3-29327ea22af4"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/c42c4c75-b53d-4a1c-adc2-7991b7f22eae"></p>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/b0e145c0-6fd0-4b79-8849-9f1b7ccc775f"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The Best Festival Company (TBFC) has launched its limited-edition SleighToy, with only ten pieces available at midnight. Within seconds, thousands rushed to buy one, but something strange happened. <strong>More than ten lucky customers received confirmation emails stating that their orders were successful</strong>. Confusion spread fast. How could everyone have bought the "last" toy? McSkidy was called in to investigate.<br>

She quickly noticed that multiple buyers purchased at the exact moment, slipping through the system’s timing flaw. Sir Carrotbane’s mischievous Bandit Bunnies had found a way to exploit this chaos, flooding the checkout with rapid clicks. By morning, TBFC faced angry shoppers, missing stock, and a mystery that revealed just how dangerous a few milliseconds could be during the holiday rush.</p>

<h3>Learning Objectives</h3>
<p>
  
- Understand what race conditions are and how they can affect web applications.<br>
- Learn how to identify and exploit race conditions in web requests.<br>
- How concurrent requests can manipulate stock or transaction values.<br>
- Explore simple mitigation techniques to prevent race condition vulnerabilities.</p>

<h3>Connecting to the Machine</h3>
<p>Before moving forward, review the questions on the connection card below:</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/1b213f50-ffc3-4a98-8f38-a9a37e8ecab6"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Start your target VM by clicking the <strong>Start Machine</strong> button below. The machine will need about 2 minutes to fully boot. Additionally, start your AttackBox by clicking the <strong>Start AttackBox</strong> button below. The AttackBox will start in split view. In case you can not see it, click the <strong>Show Split View</strong> button at the top of the page. Once the machine is up and running, you can access the application by visiting http://MACHINE_IP in the browser of your AttackBox.</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting both your AttackBox (if you're not using your VPN) and Target Machines, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<br>
<p><em>Answer the question below</em></p>

<p>1.1. <em>I can successfully connect to the machine.</em><br>
<code>No answer needed</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/62658010-3f13-4f9b-b596-c5a2af7d9bbc"><br>Rosana´s hands-on</h6>

<br>
<h2>Task 2 &nbsp; ·  &nbsp; Race Condition</h2>
<p>A race condition happens when two or more actions occur at the same time, and the system’s outcome depends on thebunny character showing car racing. order in which they finish. In web applications, this often happens when multiple users or automated requests simultaneously access or modify shared resources, such as inventory or account balances. If proper synchronisation isn’t in place, this can lead to unexpected results, such as duplicate transactions, oversold items, or unauthorised data changes.</p>

<h6 align="center"><img width="280px" src="https://github.com/user-attachments/assets/513fd1f7-db99-4780-a358-122e998ecef8"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<h3>Types of Race Conditions</h3>
<p>Generally, race condition attacks can be divided into three categories:<br>

- <code>Time-of-Check to Time-of-Use (TOCTOU)</code>: A TOCTOU race condition happens when a program checks something first and uses it later, but the data changes in between. This means what was true at the time of the check might no longer be true when the action happens. It’s like checking if a toy is in stock, and by the time you click "Buy" someone else has already bought it. For example, two users buy the same "last item" at the same time because the stock was checked before it was updated.<br><br>
- <code>Shared resource</code>: This occurs when multiple users or systems try to change the same data simultaneously without proper control. Since both updates happen together, the final result depends on which one finishes last, creating confusion. Think of two cashiers updating the same inventory spreadsheet at once, and one overwrites the other’s work.<br><br>
- <code>Atomicity violation</code>: An atomic operation should happen all at once, either fully done or not at all. When parts of a process run separately, another request can sneak in between and cause inconsistent results. It’s like paying for an item, but before the system confirms it, someone else changes the price. For example, a payment is recorded, but the order confirmation fails because another request interrupts the process.</p>

<h3>Time for Some Action</h3>
<p>Now that we understand the basic concepts, let's take the example of the TBFC shopping cart app and exploit the race condition.</p>

<h3>Configuring the Environment</h3>
<p>First, we will configure Firefox to route traffic through Burp Suite. On the AttackBox, open <code>Firefox</code>, click the <code>FoxyProxy</code> icon (1) and select the <code>Burp</code> profile (2) so all browser requests are sent to Burp, as shown below:</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/b9a61eae-768a-4c7a-ad05-4d420dd4f24e"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Next, click on the Burp Suite icon on the <code>Desktop</code> to launch the application. </p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/ba6bd625-aeae-4635-b80a-2e085a80ef4c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>You will see an introductory screen; choose <code>Temporary project in memory</code> and click <code>Next</code>.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/84940a7f-983c-4ffb-a5bd-eb9a1ab4f6fc"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>On the configuration screen, click <code>Start Burp</code> to start the application.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/67761e44-f6d9-400d-8d3a-a9a5498dd2ee"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Once the application is started, you will see the following screen, where we will use the <code>Proxy</code> and <code>Repeater</code> option to exploit the race condition.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/adbe8229-5b5a-46b7-bcaa-e6418546f58c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Before proceeding, ensure that you turn off "<code>Intercept</code>" in Burp Suite. Open the <code>Proxy</code> tab and check the <code>Intercept</code> sub-tab; If the button says "<strong>Intercept on</strong>", click it so it changes to "<strong>Intercept off</strong>". This step ensures that Burp Suite no longer holds your browser requests and allows them to pass through normally.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/458968ac-f69d-469c-99a2-69e13d811e70"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Making a Legitimate Request</h3>
<p>Now that the environment is configured, make a normal request. Open <code>Firefox</code>, visit the webapp at <code>http://MACHINE_IP</code> and you will see the following login page</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/e1de8bd1-5c30-4733-b747-4cc9cf49e33c"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>On the site’s login panel, enter the credentials, username: <code>attacker</code> and password: <code>attacker@123</code>. After logging in, you’ll arrive at the main dashboard, which shows the limited-edition SleighToy with only 10 units available.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/5ee72ec9-8f08-41b5-a466-7d0301c56d61"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<p>To make a legitimate purchase, click <code>Add to Cart</code> for the SleighToy and then click <code>Checkout</code> to go to the checkout page.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/d258ce8c-8aab-4e94-8a13-47292d965780"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<p>On the checkout page, click <code>Confirm & Pay</code> to complete the purchase. You should see a success message confirming the order, as shown below:</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/83316f6e-625d-4db2-a4b7-6e8cf63f4dac""><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Exploiting the Race Condition</h3>
<p>Now that we have made a legitimate request, navigate back to Burp Suite and click on  <code>Proxy > HTTP history</code> and find the POST request to the <code>/process_checkout</code> endpoint created by our legitimate checkout request. Right-click that entry and choose <code>Send to Repeater</code>, which will copy the exact HTTP request (headers, cookies, body) into Burp’s Repeater tool as shown below:</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/9daf655e-0e1d-4bca-b893-8d520871b62e"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<p>Next, switch to the <code>Repeater</code> tab and confirm the request appears there, right-click on the first tab, select <code>Add tab to group</code>, and click on <code>Create tab group</code>.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/d7573da7-322b-41b5-b262-1a98004117dc"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<p>Enter a name for the tab group, such as <code>cart</code>, and click <strong>Create</strong>, which will create a tab group named <code>cart</code>.</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/30728084-9df6-4f85-bf73-eca780a24693"><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Then, right-click the request tab and select <code>Duplicate tab</code>. When prompted, enter the number of copies you want (for example, 15). You’ll now have that many identical request tabs inside the cart group.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/4b32a7ba-baae-4d94-8c6c-69c8988344aa"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Next, use the Repeater toolbar <code>Send</code> dropdown menu and select <code>Send group in parallel (last-byte sync)</code>, which launches all copies at once and waits for the final byte from each response, maximising the timing overlap to trigger race conditions.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/2aa18295-aed8-475c-8245-b674e598cf32"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Once this is done, click <code>Send group in parallel</code>; this will launch all 15 requests to the server simultaneously. The server will attempt to handle them simultaneously, which will cause the timing bug to appear (due to multiple orders being processed at once).</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/015144a4-7f19-4f00-b6c5-74199a4b3891"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Finally, visit the web app, and you will see multiple confirmed orders and the SleighToy stock reduced (possibly going negative). </p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/aa767845-9258-4442-988f-895e9b48d29b"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Mitigation</h3>
<p>The attacker logged in and made a normal purchase of the limited SleighToy. Using Burp Suite, he captured the checkout request and sent it multiple times in parallel. Because the app didn’t <strong>handle simultaneous checkouts correctly</strong>, each request succeeded before the stock could update. This allowed the attacker to buy more toys than available, resulting in a race condition and pushing the stock into negative values. Here are a few mitigation measures to avoid the vulnerability:<br>
  
- Use <strong>atomic database transactions</strong> so stock deduction and order creation execute as a single, consistent operation.<br>
- Perform a <strong>final stock validation</strong> right before committing the transaction to prevent overselling.<br>
- Implement <strong>idempotency keys</strong> for checkout requests to ensure duplicates aren’t processed multiple times.<br>
- Apply <strong>rate limiting</strong> or concurrency controls to block rapid, repeated checkout attempts from the same user or session.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>What is the flag value once the stocks are negative for SleighToy Limited Edition?</em><br>
<code>THM{WINNER_OF_R@CE007}</code></p>


<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/a4d8d2f0-4121-45b2-943b-fc6e37984be7"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/02137783-7b35-4053-b4ac-d5d27249d8d5"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/06bbcdc5-e74b-40d9-ab1f-b16af77da876"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5646f6e5-695b-4e8a-be77-1b6c222886e9"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/8564427f-432f-4b48-8468-7bab70865487"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/17ee06fd-294d-48eb-b432-1904190b67ab"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/954f8aaa-e4bc-4733-b2ec-ba0fa0d97645"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/a82435a1-bff5-42da-9702-e3012b779d85"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7a969f33-7d6e-40b7-93f5-0a5b45c0d7b3"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5ceebe4f-4a90-4ac3-b8e3-35ced89d198f"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d222928b-4acf-4638-a1cb-ba228133a934"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/2953e781-bb03-4ce9-ada9-907c68947860"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/1109267a-5907-448f-b4c8-f6dae26d3777"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/4fb6673c-0823-4c54-98f6-c2f6210c2361"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7ffe06d2-6c13-4f6e-9775-153f1e6f9682"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/495dd081-eea1-48cf-9712-f033a5266db7"><br>Rosana´s hands-on</h6>

<br>
<br>
<p align="center">Refresh</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5fc54148-90c6-44e8-b1f1-83390be6f0f8"><br>Rosana´s hands-on</h6>

<br>
<p>2.2. <em>Repeat the same steps as were done for ordering the SleighToy Limited Edition. What is the flag value once the stocks are negative for <strong>Bunny Plush (Blue)</strong>?</em><br>
<code>THM{WINNER_OF_Bunny_R@ce}</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/fa4e1a7a-5c70-4657-9105-d5716ec0b6f3"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3bd117d7-954a-4cc2-95a3-e3e419cc0fab"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7e3c030f-5838-405a-954d-b077c50a3000"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/4136e7e2-cf29-4fd6-908e-8551068b2e59"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3f60de41-d6bb-4955-a8ef-80f9ede290f8"><br>Rosana´s hands-on</h6>

<br>
<br>
<p align="center">Refresh</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/eed2f18b-fd5e-4492-8245-772c9740e0b9"><br>Rosana´s hands-on</h6>

<br>
<p>2.3. <em>Feel free to check out the <a href="https://tryhackme.com/r/room/raceconditionsattacks">Race Conditions</a> room if you enjoyed this task.</em><br>
<code>No answer needed</code></p>

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/4a599d92-f6dc-43d6-97fb-7b8af7a191fc"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/3e86194b-fdb5-418f-a853-5dfc54db53d8"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/1bda2b20-58b2-46da-888e-88f8036c114c"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
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

<p align="center">Global All Time:    100ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/405a887c-8f25-45f3-b3d4-661a71496d2b"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/4d997946-e9af-4288-a363-ef141e9e66b8"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/26833b34-3f3a-45ab-83eb-a0f8e93793b5"><br><br>
                  Global monthly:  24,717ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/5ad517a7-1a52-41a5-8968-000e0c2f23b8"><br><br>
                  Brazil monthly:     275ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b08645c8-19cb-47cc-8a9c-5afa47ec7d29"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
