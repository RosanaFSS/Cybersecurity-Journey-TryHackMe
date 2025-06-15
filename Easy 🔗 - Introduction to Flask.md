<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Introduction to Flask}}$$</h1>
<p align="center">June 16, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my $$\textcolor{#FF69B4}{\textbf{4058}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
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
:~# sudo apt update && apt upgrade -y
...
:~# sudo apt install python3-pip -y
...
:~# pip3 install virtualenv
...
:~# mkdir venv
:~# cd venv
:~/venv# python3 -m venv ./venv
:~/venv# source ./venv/bin/activate
(venv) root@ip-10-10-163-109:~/venv# 
(.venv) :~# pip3 install Flask
(.venv) :~# pip install Flask
...
```

```bash
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():   
    return 'Hello TryHackMe community!!!'
```

```bash
(.venv) :~/my# export FLASK_APP=hello.py
(.venv) :~/my# flask run
(venv) root@ip-10-10-163-109:~/venv# flask run
 * Serving Flask app 'hello.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

```

<br>

![image](https://github.com/user-attachments/assets/99512bf2-d98f-4b96-8870-dfe02759f787)

<br>

![image](https://github.com/user-attachments/assets/dd7f4d1e-5b82-4c3f-bb8a-910af4f35ff2)

<br>

![image](https://github.com/user-attachments/assets/47a8cd4e-7d90-490d-875b-cd712d5435ee)

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
>> <code><strong>yay</strong></code>

![image](https://github.com/user-attachments/assets/f666324c-40ce-4693-8120-4b713986c247)

<br>

![image](https://github.com/user-attachments/assets/266dae20-7cab-48fc-af0e-0bc720805361)

<br>

![image](https://github.com/user-attachments/assets/dd164be1-6473-432c-81ab-3c23bf7a4cfc)

<br>

![image](https://github.com/user-attachments/assets/9e56e577-4980-4cc6-8367-b54752539617)

<br>

![image](https://github.com/user-attachments/assets/52414082-30b0-4522-aa09-d46b29d72fe0)


<br>

![image](https://github.com/user-attachments/assets/d5c9254c-da58-4bd6-947f-728183d239d1)

<br>


```bash
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/admin')
def admin():
    return 'Admin Page'
```

<br>

![image](https://github.com/user-attachments/assets/9088aef4-b1bd-413e-bdbc-82fd7277b172)


![image](https://github.com/user-attachments/assets/62093242-0760-4914-84a6-50150ccf302b)

<br>



<h2>Task 4 . HTTP Methods and Template Rendering</h2>

<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>
<br>

> 4.1. <em>Does Flask support POST requests? (yay/nay)</em><br><a id='4.1'></a>
>> <code><strong>yay</strong></code>

<br>

> 4.2. <em>What markdown language can you use to make templates for Flask? </em><br><a id='4.2'></a>
>> <code><strong>html</strong></code>

<br>


![image](https://github.com/user-attachments/assets/30b073b4-0df4-4f8a-bca8-fd84c7bf813b)


<br>

![image](https://github.com/user-attachments/assets/09bc64c3-3634-4f5c-a207-49cf349984ce)

<br>

<h2>Task 5 . File Upload</h2>

<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 5.1. <em>Awesome!</em><br><a id='5.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<p><em>fileupload.py</em></p>

```bash
from flask import request
from werkzeug.utils import secure_filename
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['filename']
        f.save('uploads/' + secure_filename(f.filename))
    return render_template('upload.html')
```

![image](https://github.com/user-attachments/assets/3003ab9c-8e3c-42ce-b2d2-7b52103eb725)

<br>

<p><em>upload.html</em></p>

```bash
<!DOCTYPE html>
<html>
<body>

<p>Click on the "Choose File" button to upload a file:</p>

<form action="{{ url_for('upload_file') }}" method="POST" enctype="multipart/form-data">
  <input type="file" id="myFile" name="filename">
  <input type="submit">
</form>
</body>
</html>
```

![image](https://github.com/user-attachments/assets/c7878e9c-4e7b-4b19-82cc-b4d04c0eb0c0)



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
>> <code><strong>THM{flask_1njected}</strong></code>

<br>


<p>Navigated to <code>targetIP:5000/vuln?name={{ person.password }}</code></p>

![image](https://github.com/user-attachments/assets/7d61f8c4-e6f3-4838-8f8b-fcb49c6299cc)

<p>Navigated to <code>>http://TargetIP:5000/vuln?name=={{ get_user_file("/etc/passwd") }</code></p>

![image](https://github.com/user-attachments/assets/1a8df1de-f9ad-4de7-94cd-c235b91affed)

<p>Navigated to <code>http://TargetIP:5000/vuln?name={{%20get_user_file(%22/home/flask/flag.txt%22)%20}}</code>p>
<br>

![image](https://github.com/user-attachments/assets/f4833651-531f-4e23-b2dd-fb868f4e141b)

<br>

<h2>Task 7 . References and Sources</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 7.1. <em>See you in the next room!</em><br><a id='7.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

