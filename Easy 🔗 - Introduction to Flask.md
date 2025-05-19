<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Introduction to Flask}}$$</h1>
<p align="center">May 19, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my $$\textcolor{#FF69B4}{\textbf{378}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
How it works and how can I exploit it? It is an easy-level walkthrough. You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.  Access it clicking <a href="https://tryhackme.com/room/flask"</a>here.<br>
<img width="1000px" src=""></p>

<br>

<h2>Task 1 . Introduction</h2>
<p>This room continues my python-frameworks series. Learning Python can be extremely useful for penetration testers, and a simple understanding of its frameworks can be a key to success. In this room (lesson), we are going to learn about one of the easiest and fastest ones. <br><br>

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies, and several common framework related tools. <br>
[Source: Wikipedia]</p>

<p>To be short, Flask does not require much work from you and can be coded and deployed in a matter of a couple of minutes!</p>

<p>You'll find Flask especially easy if you find <a href="https://tryhackme.com/room/django"</a> Django too complicated :)</p>

<p>https://github.com/Swafox/Flask-examples <-- Here's the collection of all scripts that are going to be used in this room.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 1.1. <em>Let´s go!</em><br><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 2 . Installation and Deployment basics</h2>
<p>Let's proceed with basic installation. For this room, we are going to use Python3. You can get it for both Windows and Linux here:<br><br>
<a href="https://www.python.org/"</a>Link</p>

<p>Now open up a terminal/cmd and install Flask by running:<br><br>
<code>pip3 install Flask</code><br><br>

After a couple of seconds, you'll get everything you need for using Flask.<br><br>

Make a separate directory for your demo project and start a virtual environment there. Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages. Python 3 comes bundled with the venv module to create virtual environments. (tl;dr a virtual environment isolates your project from the system to prevent any conflicts). 
Run <code>pip3 install virtualenv</code> if you get an error running venv later on.</p>

<h3>On Linux run:</h3>
<p><code>mkdir myproject<br>
cd myproject<br>
python3 -m venv venv</code></p>

<br>

![image](https://github.com/user-attachments/assets/bab4d0f4-255f-47f9-8bde-1bc1d63499d2)

<br>

<h3>On Windows run:</h3>
<p><code>mkdir myproject<br>
cd myproject<br>
py-3 -m venv venv</code></p>

<br>

![image](https://github.com/user-attachments/assets/51add159-82cd-4a72-acfc-bb31839febb2)

<br>

<p>Now you need to create and set a Flask file, aka a script that is going to contain the flask code. Create a file with a name of your choice and run the following command depending on your system:<br><br>

Windows: <code>set FLASK_APP=hello.py</code><br>
Linux: <code>export FLASK_APP=hello.py</code><br>
(Change <code>hello.py</code> to whatever name you came up with earlier)<br><br>


And that's that! All you have to do now is run<br>
<code>flask run</code><br>
or<br>
<code>flask run --host=0.0.0.0</code><br>
to deploy a flask app locally or publically (on your network).<br><br>

Note: You are going to get an error if you deploy the app at this point since we have no code written.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 2.1. <em>Which environment variable do you need to change in order to run Flask?</em><br><a id='2.1'></a>
>> <code><strong>FLASK_APP</strong></code>

<br>

<p>Navigated to the provided repository.</p>

<br>

![image](https://github.com/user-attachments/assets/b2a14645-4b39-4dd8-be03-a005b96a1f13)

<br>

![image](https://github.com/user-attachments/assets/3a5c24c7-6124-4bf1-961a-25a461a81f6e)



```bash
:~/IntroductionToFlask# sudo apt update && apt upgrade -y
...
:~/IntroductionToFlask# sudo apt install python3-pip -y
...
:~/IntroductionToFlask# pip3 install Flask
...
:~/IntroductionToFlask# mkdir myproject
:~/IntroductionToFlask# cd myproject
:~/IntroductionToFlask# python3 -m venv .venv
:~/IntroductionToFlask# source .venv/bin/activate
:~/IntroductionToFlask# pip install Flask
:~/IntroductionToFlask/myproject# export FLASK_APP=hello.py
```

<br>
<br>

<h2>Task 3 . Basic syntax and routing</h2>

<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>
<br>

> 3.1. <em>What's the default deployment port used by Flask?</em><br><a id='3.1'></a>
>> <code><strong>FLASK_APP</strong></code>

<br>

> 3.2. <em>Is it possible to change that port? (yay/nay)</em><br><a id='3.2'></a>
>> <code><strong>yayP</strong></code>

![image](https://github.com/user-attachments/assets/f666324c-40ce-4693-8120-4b713986c247)


<br>
<br>

<h2>Task 4 . HTTP Methods and Template Rendering</h2>

<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>
<br>

> 4.1. <em>Does Flask support POST requests? (yay/nay)</em><br><a id='4.1'></a>
>> <code><strong>yay</strong></code>

<br>

> 4.2. <em>What markdown language can you use to make templates for Flask? </em><br><a id='4.2'></a>
>> <code><strong>HTML</strong></code>

<br>
<br>

<h2>Task 5 . File Upload</h2>

<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 5.1. <em>Awesome!</em><br><a id='5.1'></a>
>> <code><strong>No answer needed</strong></code>


<br>
<br>

<h2>Task 6 . Flask Injection</h2>

<p>At this point, it looks like Flask is a great framework for young developers. It definitely is a great tool but a simple misconfiguration may lead to severe security consequences. A major vulnerability was found in Flask's template rendering. The template engine provided within the Flask framework may allow developers to introduce Server-Side Template Injection (SSTI) vulnerabilities.  An attacker can execute code within the context of the server. In some cases, it may lead to a full Remote Code Execution (RCE).<br><br>

For the sake of this room let's take a look at a bad code configuration and see how it can be used to exploit a Local File Inclusion (LFI)!</p>

<br>

![image](https://github.com/user-attachments/assets/083e298b-03bf-4219-8e59-268cb4df4d4f)

<br>

<p>The main reason for this vulnerability is that Jinja2 (template rendering engine) uses curly braces to surround variables used in the template. As you can see on the line with # Problem, our template is put in ''' ''' brackets which allow us to abuse the Jinja template mechanism. A variable after hello is parsing a name from a variable person. But because this is a vulnerable code we can make it output the password.<br><br>

Go to the <code>MACHINE_IP:5000/vuln?name=</code><br><br>

Simply put <code>{{ person.password }}</code> at the end of the link to see the password being displayed in cleartext. </p>

<br>

![image](https://github.com/user-attachments/assets/eaf39fff-8624-4405-b313-eb01e8246865)

<br>

<p>Now let's take that vulnerability to another level and read files (LFI).<br><br>
<code>{{ get_user_file("/etc/passwd") }}</code>

The above string will allow you to read the /etc/passwd file or any other if you simply change the name.<br><br>

This vulnerability can be easily mitigated by using a single quotation mark (' ') in the template variable (instead of ''' '''').  It may look ridiculous, but many python developers make these kinds of mistakes, and unintentionally make their websites vulnerable to SSTI.</p>



<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 6.1. <em>What's inside /home/flask/flag.txt ?</em><br><a id='6.1'></a>
>> <code><strong>_____</strong></code>

<br>

<h2>Task 7 . References and Sources</h2>

