<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Custom Tooling using Burp}}$$</h1>
<p align="center"><img width="180px" src="https://github.com/user-attachments/assets/a74da0a4-04dc-432a-add8-95a9454fd5ef"><br>
May 27, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my $$\textcolor{#FF69B4}{\textbf{386}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Creating custom tooling for application testing using Burp Plugins. Access it clicking <a href="https://tryhackme.com/room/customtoolingviaburp"</a>here.<br><br>
<img width="1000px" src=""></p>

<br>
<br>

<h2>Task 1 . Introduction</h2>

<p>The ability to create your own custom tooling is critically important for web application red teaming. Rarely will you be able to find a tool or plugin that will do exactly what you need. This then calls for you to develop custom tooling! This custom tooling module will showcase different ways you can approach this problem. Each option is unique and has its benefits and drawbacks.

<br>
<br>
In this room, we will focus on using <code>Burp</code> plugins to create tools and exploit them. Burp acts as an intercepting proxy, allowing you to view and modify requests and responses as the web application interfaces with it. Burp has several features, such as repeating requests or performing automated brute forcing of specific requests and payloads. This makes plugins a unique option when you need additional versatility in your tooling to be used in an automated and manual fashion. While we will showcase using Burp plugins in this room, the principles can be applied to any intercepting proxy you choose. Let's dive in and use Burp plugins to create our very own custom tools and exploits!</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>


> 1.1. <em>I am ready to learn about creating custom Burp plugins!</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . Using a Proxy for Custom Tooling</h2>
<h3>Why Create Your Own Tools?</h3>

<p>[ ... ]</p>

<h3>Custom Crypto Cryptonite</h3>

<p>[ ... ]</p>

<h3>Interesting Intercepting Proxies and Where to Find Them</h3>

<p>[ ... ]</p>

<h3>Beautiful Burp</h3>

<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 2.1. <em>Which intercepting proxy currently only has support for Windows?</em><br><a id='2.1'></a>
>> <strong><code>Fiddler</code></strong><br>
<p></p>

<br>

> 2.2. <em>Which intercepting proxy allows us to write plugins using TypeScript?</em><br><a id='2.2'></a>
>> <strong><code>Caido</code></strong><br>
<p></p>

<br>

> 2.3. <em>Which intercepting proxy allows plugins to be written in the most amount of different coding languages?</em><br><a id='2.3'></a>
>> <strong><code>Burp</code></strong><br>
<p></p>


<br>
<br>

<h2>Task 3 . Using Extensions in Burp</h2>
<p>In this task, we will explore Burp extensions and how they ease a pentester’s job by automating routine tasks. Burp offers built-in extensions that enhance basic security testing capabilities, such as logging, request/response modification, and simple automation. Some of the extensions are available for free, while a few require Burp Professional.</p>

<h3>Playing with Extensions</h3>
<p>In the attached VM, click on the <code>Burp</code> icon on the left pane to open the Burp Sutie Community Edition. Once Burp is open, click on the <code>Extension</code> tab and then click on the <code>BApp Store</code> to view multiple extensions offered by Burp and uploaded by community users worldwide. </p>

<br>

![image](https://github.com/user-attachments/assets/65094468-a106-4d2c-8f1c-e0e6e152f6d4)

<br>

<p>In this task, we will install the famous extension <code>Decoder Improved</code>, which allows for the encoding and decoding of URLs and HTML, and hashing of input. This extension comes in handy when you are dealing with a complex web application that has incorporated multiple encoding mechanisms; therefore, instead of using any other application or custom script, you can simply use this extension to perform decoding. 

<br>
<br>

In the list of available extensions, find <code>Decoder Improved</code> and you will find the <code>Install</code> button on the right side to install it (Do not click the button yet), as shown below:</p>

<br>

![image](https://github.com/user-attachments/assets/1d721d88-ce2c-4183-ba5e-d22320a123a6)

<br>

<p>Note: Since the attached VM is not connected to the internet, we will install the extension in offline mode. However, on an internet-connected machine, you can simply click the Install button to install the extension directly.<br><br>

On the same screen, click the Manual Install button as shown below, and select the Decoder-Improved.bapp file from /home/ubuntu/lib, as shown below:</p>

<br>

![image](https://github.com/user-attachments/assets/813c5ee0-3015-4176-9760-5bdfd16e3766)

<br>

<p>Once the installation is complete, a new tab will appear, allowing you to access the extension's features.<br><br>

Now, let's explore the Decoder Improved extension and use it to Base64 encode a simple string. First, navigate to the Decoder Improved tab to access the extension's GUI. On the right side, select the Text (1) radio button, then choose Encode as (1) from the dropdown menu and select Base64 (1) as the encoding option. In the upper window, on the left side, enter TryHackMe (2), and the extension will automatically generate the Base64-encoded output in the bottom window, as shown below:</p>

<br>

![image](https://github.com/user-attachments/assets/87f43311-46b6-4754-9043-15f7f2b705c1)

<br>

<p>This is a simple demonstration of how extensions help a pentester ease routine tasks. Burp offers a variety of other extensions, such as Hackvertor, Logger++, XSS Validator, Turbo Intruder and many more, to enable automation and custom tooling.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 3.1. <em>What is the decoded value for the string VEhNezEwMUJ1cnB9?</em><br><a id='3.1'></a>
>> <strong><code>THM{101Burp}</code></strong><br>
<p></p>

<br>


> 3.2. <em>Does Burp only offer paid extensions developed by users worldwide? (yea/nay) </em><br><a id='3.2'></a>
>> <strong><code>nay</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/64919d82-4cc3-4a65-a66b-dd19a3409d2b)

<br>

![image](https://github.com/user-attachments/assets/5ccbec4b-70de-426f-bca3-ed8a4e253f62)

<br>

![image](https://github.com/user-attachments/assets/5bfbecbd-e4be-416c-82d9-58bfaa44e03b)

<br>
<br>

<h2>Task 4 . Creating a Basic Burp Extension</h2>

<br>

<p>TargetIP:8443</p>

![image](https://github.com/user-attachments/assets/3065ed8a-d2db-4e51-b635-17938535ad48)



<br>
<br>

<h2>Task 5 . Modifying a Burp Extension</h2>

<br>
<br>

<h2>Task 6 . Challenge</h2>

<br>
<br>

<h2>Task 7 . Conclusion</h2>
<h3>Mastering Plugins and Proxies</h3>
<p>Custom plugins within intercepting proxies are an essential skillset for any red teamer dealing with mobile applications or complex client-side protections. When traditional tools fall short due to custom cryptography or application hardening, custom plugins give you the power to intercept, decrypt, and modify requests and responses in real-time.
<br>
<br>

In this room, we explored why intercepting proxies like Burp Suite are so valuable—especially when paired with custom logic designed to reverse engineer and bypass protections. Rather than building an exploit from scratch, the goal here was to enable visibility and control, allowing your existing red teaming tools and techniques to shine.
<br>
<br>

Whether you're decrypting payloads, injecting modified parameters, or simply trying to understand how an application communicates with its API, building plugins directly into your proxy gives you a tactical advantage that can’t be overstated.
<br>
<br>

By combining solid intercepting proxy knowledge with scripting or plugin development skills, you'll be better equipped to deal with hardened applications, extract hidden data, and bypass defences—putting you one step ahead in any red team engagement.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 7.1. <em>I understand the importance of using plugins to develop custom tooling!</em><br><a id='7.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

