<h1>Tor</h1>

<br>

![image](https://github.com/user-attachments/assets/bee4061a-5cbb-4d53-847f-cef52fd3f835)

<br>




![image](https://github.com/user-attachments/assets/3bfa2e32-ed0d-4c02-b5df-ab6126c639a1)

<br>

![image](https://github.com/user-attachments/assets/b86b7dc4-b2cc-4e62-afcb-23804f12e990)


<br>

<h2>Task 1. Unit 1 - Tor</h2>

<p>Tor is a free and open-source software for enabling anonymous communication. Tor directs Internet traffic through a free, worldwide, volunteer overlay network consisting of more than seven thousand relays to conceal a user's location and usage from anyone conducting network surveillance or traffic analysis. Using Tor makes it more difficult to trace Internet activity to the user: this includes "visits to Web sites, online posts, instant messages, and other communication forms". Tor's intended use is to protect the personal privacy of its users, as well as their freedom and ability to conduct confidential communication by keeping their Internet activities unmonitored.

In penetration testing, there might be a need to conduct a full-fledged black-box test. This is a form of testing in which security professionals have to deal with such things as firewalls and other mechanisms of restriction on the customer’s side. In this case, the Tor network can be used in order to constantly change IP and DNS addresses and therefore successfully overcome any restrictions.

In this unit, we are going to install the Tor service and learn basic commands.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>Run <code>apt-get install tor</code> to install/update your Tor packages.</em><br><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>


<pre>code>apt-get install tor</code></pre>

<br>


![image](https://github.com/user-attachments/assets/0d5da870-ca0c-4de0-9a68-9ef34c870adc)


<br>

> 1.2. <em>Run <code>service tor start</code>  to start the Tor service.</em><br><a id='1.2'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<pre>code>service tor start</code></pre>

<br>


![image](https://github.com/user-attachments/assets/954436ee-9bd4-42b4-95fe-bf266df8f55d)

<br>

> 1.3. <em>Run <code>service tor status</code>  to check Tor's availability./em><br><a id='1.3'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<pre>code>service tor status</code></pre>

<br>

![image](https://github.com/user-attachments/assets/d178fe4f-9e09-4c1d-a1b9-ad51cacf2b10)

<br>

<br>

> 1.4. <em>Run <code> service tor stop</code> to stop the Tor service.</em><br><a id='1.4'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<pre>code>service tor stop</code></pre>

<br>

![image](https://github.com/user-attachments/assets/67a8c874-943f-4c09-afa1-394803bdb36b)

<br>


<h2>Task 2. Unit 2 - Proxychains</h2>

![image](https://github.com/user-attachments/assets/f3f6b7bc-06ec-409c-896b-5703e871a7e7)

<p>https://github.com/haad/proxychains</p>


<p>Proxychains - a tool that forces any TCP connection made by any given application to follow through proxy like TOR or any other SOCKS4, SOCKS5 or HTTP(S) proxy.<br>

Proxychains is widely used by pentesters during the reconnaissance stage (For example with nmap).</p>

<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 2.1. <em>Let's start running <code>apt install proxychains</code> to install/update proxychains tool.</em><br><a id='2.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<pre>code>apt install proxychains</code></pre>

<br>

![image](https://github.com/user-attachments/assets/18d351eb-b1ff-4197-9f65-77acb75460a0)


<br>

<p>Now it's time to configure proxychains to work properly.</p>

<br>

> 2.2. <em>Run <code>nano /etc/proxychains.conf</code> to edit the settings. (Note: You can use any text editing tool instead of nano.).</em><br><a id='2.2'></a>
>> <code><strong>No answer needed</strong></code>

<pre>code>nano /etc/proxychains.conf</code></pre>

<br>

![image](https://github.com/user-attachments/assets/8c9858c1-d26d-40ab-9922-3be8de1d73ee)

<br>

<p>We can now see, that most of the methods are under comment mark. You can read their description and decide on using one of them in the future. For this lesson let's uncomment <code>dynamic_chain</code> and comment others (simply put <coded>#</coded> to the left). Additionally, it is useful to uncomment <code>proxy_dns</code> in order to prevent DNS leak. Scroll through the document and see whenever you want to add some additional proxies at the bottom of the page (which is not required at this point).</p>

<br>

> 2.3. <em>Apply all the settings.</em><br><a id='2.3'></a>
>> <code><strong>No answer needed</strong></code>

![image](https://github.com/user-attachments/assets/37a746c9-3f48-434b-9a03-bfca41e8bbb0)

<br>

<p>Now let's check our settings.</p>

<br>

> 2.4. <em>Start the TOR service and run <code>proxychains firefox</code>. Usually, you are required to put <code>proxychains</code> command before anything in order to force it to transfer data through Tor.</em><br><a id='2.4'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<pre>code>proxychains firefox</code></pre>

![image](https://github.com/user-attachments/assets/8bc8d591-add9-4ef5-b2bb-d9aabfd42149)

<br>

![image](https://github.com/user-attachments/assets/791bfff6-112a-4be0-b8e8-fc5db77155dd)

<br>

> 2.5. After the Firefox has loaded, check if your IP address has changed with any website that provides such information. Also, try running a test on <code>dnsleaktest.com</code> and see if your DNS address changed too.<br>
NOTE: All other web browser windows should be closed before opening Firefox through proxychains!</em><br><a id='2.5'></a>
>> <code><strong>No answer needed</strong></code>

<br>

![image](https://github.com/user-attachments/assets/cf106454-c25a-46b8-91d6-86a0d7acd4e6)


<br>


<h2>Task 3. Unit 3 - Tor Browser</h2>
<p>Tor browser, as seen from its name, is a browser that transfers all its traffic through TOR and by using firefox headers makes all Tor users look the same.<br>

On a daily basis, Tor browser is useful for anyone who wants to keep their internet activities out of the hands of advertisers, ISPs, and web sites. That includes people getting around censorship restrictions in their country, police officers looking to hide their IP address or anyone else who doesn't want their browsing habits linked to them.<br>

Install Tor browser on your system (It is not necessarily to do this on your Kali Machine).<br>

Windows, Mac OS installation<br>
https://www.torproject.org/<br>

Kali Linux guide<br>
https://www.kali.org/docs/tools/tor/</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>Finish the installation..</em><br><a id='3.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>


![image](https://github.com/user-attachments/assets/4cb37c18-1e1f-4a67-a65c-ae2c0380e330)


> 3.2. <em>Launch the Tor Browser and set your privacy settings to Level 2 (Safer).</em><br><a id='3.2'></a>
>> <code><strong>No answer needed</strong></code>

<br>

> 3.3. <em>What is the search engine at the following onion address: https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/</em><br><a id='3.2'></a>
>> <code><strong>DuckDuckGo</strong></code>

<br>

<p align="center"> <img width="750px" src="https://github.com/user-attachments/assets/97ff49a0-8b6b-4267-aa65-18246972163f"></p>


<br>
<h2>Room Complete<a id='4'></a></h2>
<p>Keep learning, keep growing!</p>

<p align="center"> <img width="750px" src="https://github.com/user-attachments/assets/f404f3e5-290f-4825-b859-b75f9ab358cc"></p>

<br>

<p align="center"> <img width="750px" src="https://github.com/user-attachments/assets/97ff49a0-8b6b-4267-aa65-18246972163f"></p>

<br>

<h2>My Journey<a id='5'></a></h2>
<p>Following I share the status of my journey in TryHackMe.</p>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| December 11, 2024 | 219      |       953 rd |        19 th |      643 rd |       8 th |  61,006  |       465 |

</div>


<p align="center"> <img width="750px" src="https://github.com/user-attachments/assets/f2ce191a-4ee5-454c-9611-9aa92905a5ed"></p>

<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>
