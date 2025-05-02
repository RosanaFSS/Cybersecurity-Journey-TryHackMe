<p align="center">May 2, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{361}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/1acd3213-b0f0-4ec2-a142-8e36ab0df272"><br></p>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{SSTI}}$$</h1>
<p align="center">Learn what Server Side Template Injection is and how to exploit it!<br>
It is classified a medium-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/learnssti">here</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>


<h2>Task 1 . Introduction</h2>
<h3>What is Server Side Template Injection?</h3>
<p>Server Side Template Injection (SSTI) is a web exploit which takes advantage of an insecure implementation of a template engine.</p>

<h3>What is a template engine?﻿</h3>
<p>A template engine allows you to create static template files which can be re-used in your application.

What does that mean? Consider a page that stores information about a user, <code>/profile/<user></code>. The code might look something like this in Python's Flask:</p>

![image](https://github.com/user-attachments/assets/fd8e92e9-bc05-4b8b-ac8c-bb2c0390cf07)

<p>This code creates a template string, and concatenates the user input into it. This way, the content can be loaded dynamically for each user, while keeping a consistent page format.
Note: Flask is the web framework, while Jinja2 is the template engine being used.</p>

<h3>How is SSTI exploitable?</h3>
<p>Consider the above code, specifically the <code>template</code> string. The variable user (which is user input) is concatenated directly into the template, rather than passed in as data. This means whatever is supplied as user input will be interpreted by the engine.<br><br>

Note: The template engines themselves aren't vulnerable, rather an insecure implementation by the developer.</p>

<h3>What is the impact of SSTI?</h3>
<p>As the name suggests, SSTI is a server side exploit, rather than client side such as cross site scripting (XSS).<br><br>

This means that vulnerabilities are even more critical, because instead of an account on the website being hijacked (common use of XSS), the server instead gets hijacked.<br><br>

The possibilities are endless, however the main goal is typically to gain remote code execution.</p>

<h3>Deploy!</h3>
<p>Deploy the virtual machine associated with this lab and follow along as we exploit SSTI together!<br><br>

You can access the web server by navigating to <code>http://XX.XX.XXX.XXX::5000.<br><br>

Note: The endpoint / does not exist, and you will receive a 404 error.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Understand all of the above.</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . Detection</h2>
<h3>Finding an injection point</h3>
<p>The exploit must be inserted somewhere, this is called an injection <br><br>

There are a few places we can look within an application, such as the URL or an input box (make sure to check for hidden inputs).<br><br>

In this example, there is a page that stores information about a user: http://10.10.211.207:5000/profile/<user>, which takes in user input.<br><br>

We can find the intended output by providing an expected name:</p>

![image](https://github.com/user-attachments/assets/dff43db3-cf8a-4be4-9d45-4caed3cae148)


<h3>Fuzzing</h3>
<p>Fuzzing is a technique to determine whether the server is vulnerable by sending multiple characters in hopes to interfere with the backend system.<br><br>

This can be done manually, or by an application such as BurpSuite's Intruder. However, for educational purposes, we will look at the manual process.<br><br>

Luckily for us, most template engines will use a similar character set for their "special functions" which makes it relatively quick to detect if it's vulnerable to SSTI.<br><br>

For example, the following characters are known to be used in quite a few template engines: ${{<%[%'"}}%.<br><br>

To manually fuzz all of these characters, they can be sent one by one following each other.<br><br>

The fuzzing process looks as follows:</p>

![image](https://github.com/user-attachments/assets/d01cd9d5-afde-470d-91d8-26e76b1270a8)

<br>

![image](https://github.com/user-attachments/assets/cf23b40a-ce02-4448-a832-6d9381c2a021)

<br>

<p>Continue with this process until you either get an error, or some characters start disappearing from the output.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>What sequence of characters causes the application to throw an error?</em> Hint : <em>Remember that not all characters in the sequence are mandatory. </em><br><a id='2.1'></a>
>> <strong><code>{{</code></strong><br>
<p></p>

<br>

<p>Navigated to <code>http://XX.XX.XXX.XXX:5000/profile/jake</code></p>

![image](https://github.com/user-attachments/assets/a0c23b2a-643b-49f0-8eb4-2ec9e725336e)


<p>Tried <code>http://XX.XX.XXX.XXX:5000/profile/$</code></p>

![image](https://github.com/user-attachments/assets/b57fa852-b43c-471f-ab8e-7334bf5ba8b4)


<br>

<p>Tried <code>http://XX.XX.XXX.XXX:5000/profile/${</code></p>

![image](https://github.com/user-attachments/assets/d07e1f02-b8da-4b9c-bae8-cdf5c5a50ff4)

<br>

<p>Tried <code>http://XX.XX.XXX.XXX:5000/profile/{{</code> and got an error.</p>

![image](https://github.com/user-attachments/assets/3459e3c7-2989-440e-9ba8-653afe4cd647)

<br>
<br>

<h2>Task 3 . Identification</h2>
<p>Now that we have detected what characters caused the application to error, it is time to identify what template engine is being used.<br><br>

In the best case scenario, the error message will include the template engine, which marks this step complete!<br><br>

However, if this is not the case, we can use a decision tree to help us identify the template engine:</p>


![image](https://github.com/user-attachments/assets/6cd8a106-da7b-44c3-8488-d56016cef249)

<p>﻿Photo Credit: PortSwigger<br><br>

To follow the decision tree, start at the very left and include the variable in your request. Follow the arrow depending on the output:<br>

- Green arrow - The expression evaluated (i.e 42)<br>
- Red arrow - The expression is shown in the output (i.e ${7*7})<br><br>

In the case of our example, the process looks as follows:</p>

![image](https://github.com/user-attachments/assets/de74af7e-1000-42e5-95e0-4176a28921ec)

<p>The application mirrors the user input, so we follow the red arrow:</p>

![image](https://github.com/user-attachments/assets/59680b63-dcdc-4a00-9b49-b091dc892bbc)


<p>The application evaluates the user input, so we follow the green arrow.<br><br>

Continue with this process until you get to the end of the decision tree.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 3.1. <em>What template engine is being used in this application?</em><br><a id='3.1'></a>
>> <strong><code>Jinja2</code></strong><br>
<p></p>

<br>

<p>Tried <code>http://XX.XX.XXX.XXX:5000/profile/${7*7}</code> and did not get any error.</p>

![image](https://github.com/user-attachments/assets/bbc68f27-03f6-48ee-a78e-30f99e204e18)

<br>

![image](https://github.com/user-attachments/assets/4133e61e-1951-4390-9cfb-226f17fcb53b)


<br>

<p>Tried <code>http://XX.XX.XXX.XXX:5000/profile/${{7*7}}</code> and did not get any error.</p>

![image](https://github.com/user-attachments/assets/840e72a7-85f4-4a5c-8efa-72b19b4ced92)

<br>

![image](https://github.com/user-attachments/assets/229a1012-4ff0-4c8a-991d-9ef49e2db0bb)


<br>

<p>Tried <code>http://XX.XX.XXX.XXX:5000/profile/${{7*7}}</code> and did not get any error.</p>

![image](https://github.com/user-attachments/assets/1f84cc56-6194-4593-a250-f3d2101eb916)

<br>

![image](https://github.com/user-attachments/assets/5cfa3a20-9260-484d-86b0-6cb1a7d721e9)


<br>
<br>

<h2>Task 4 . Syntax</h2>

<p>After having identified the template engine, we now need to learn its syntax.<br><br>

Where better to learn than the official documentation?<br><br>

Always look for the following, no matter the language or template engine:<br>

- How to start a print statement<br>
- How to end a print statement<br>
- How to start a block statement<br>
- How to end a block statement<br><br>

In the case of our example, the documentation states the following:<br>

- {{ - Used to mark the start of a print statement<br>
- }} - Used to mark the end of a print statement<br>
- {% - Used to mark the start of a block statement<br>
- %} - Used to mark the end of a block statement</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 4.1. <em>How do you start a comment in Jinja2?</em><br><a id='4.1'></a>
>> <strong><code>{#</code></strong><br>
<p></p>

<br>

<p>Navigated to the documentation link provided in the walkthrough.</p>

![image](https://github.com/user-attachments/assets/7fd6f910-43a5-480b-9cf9-b2d32aa099ca)

<br>
<br>

<h2>Task 5 . Explotation</h2>
<p>At this point, we know:<br>

- The application is vulnerable to SSTI<br>
- The injection point<br>
- The template engine<br>
- The template engine syntax</p>

<br>

<h3>Planning</h3>
<p>Let's first plan how we would like to exploit this vulnerability.<br><br>

Since Jinja2 is a Python based template engine, we will look at ways to run shell commands in Python. A quick Google search brings up a blog that details different ways to run shell commands. I will highlight a few of them below:</p>


