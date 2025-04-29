<p align="center">April 29, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{358}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="300px" src="https://github.com/user-attachments/assets/9050e33f-101f-4a0f-bb58-9640a7b72eff" alt="streak"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Linux Modules}}$$</h1>
<p align="center"><em>Learn linux modules in a fun way</em>.<br>
It is classified as an easy-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/linuxmodules">here</a>.</p>

<p align="center"> <img width="1000px" src=""> </p>

<br>
<br>


<h2>Task 1 . Let´s introduce </h2>

<p>[ ...]</p>

<h3>Scope ot this room</h3>
<p>﻿This room is based on understanding these tools so that they can reduce our effort while working with the command line. Also, this skill that you develop will help you manage your terminal sessions efficiently while working on a pentest or any project.<br><br>

Just make sure that you're using a linux VM, so that you can get a hands on if you want to. Or simply start the attackbox(free users can deploy the attackbox for an hour, which I think is pretty much enough time to complete this room). I highly recommend to complete the "Linux Fundamentals" rooms before proceeding further with these topics. <br><br>

Happy Learning ;)</p>

                                      

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Read the above</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 2 . <code>du</code></h2>
<h3>About the command</h3>
<p><code>du</code> is a command in linux (short for disk usage) which helps you identify what files/directories are consuming how much space. If you run a simple du command in terminal...</p>

<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>Read the above</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 3 . <code>Grep</code>, <code>EGrep</code>, <code>FGrep</code></h2>
<p>IMPORTANT: To proceed further with this task, make sure you have completed the "Regular Expressions" room by concatenate. This room will brief you about the regular expressions that can come handy while working with egrep.

There are a lot of rooms that you must have already done where you used grep a lot of times, so most of this task will sound familiar to you, or this is your first attempt on reading about grep, in any case, a 5 min read won't harm your busy day...</p>

<p>[ Download Task Files ]</p>

<h3>Introduction</h3>
<p>[ ... ]</p>

<h3>The Famuly Tree</h3>
<p>egrep and fgrep are no different from grep(other than 2 flags that can be used with grep to function as both). In simple words, egrep matches the regular expressions in a string, and fgrep searches for a fixed string inside text. Now grep can do both their jobs by using -E and -F flag, respectively.

<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>Read the above</em><br><a id='3.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

> 3.2. <em>Is there a difference between egrep and fgrep? (Yea/Nay)</em><br><a id='3.2'></a>
>> <strong><code>Yea</code></strong><br>
<p></p>

<br>

> 3.3. <em>Which flag do you use to list out all the lines NOT containing the 'PATTERN'?</em><br><a id='3.3'></a>
>> <strong><code>-v</code></strong><br>
<p></p>

<br>

> 3.4. <em>Download the above given file and answer the following questions.</em><br><a id='3.4'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

> 3.5. <em>What user did you find in that file?</em>Hint : <em>Case Insensitive may be??</em><br><a id='3.5'></a>
>> <strong><code>bobthebuilder</code></strong><br>
<p></p>

<br>

```bash
grep -i "user" grep.txt
uxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7FuSeR:bobthebuilder6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6f
```

<br>

> 3.6. <em>What is the password of that user?</em>Hint : <em>Uhm, did you checked the line properly?</em><br><a id='3.6'></a>
>> <strong><code>LinuxIsGawd</code></strong><br>
<p></p>

<br>

```bash
grep -i "password" grep.txt
qEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTthispAsSwOrDistoosensitive:'LinuxIsGawd'XqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTX
```

<br>

> 3.7. <em>Can you find the comment that user just left?</em><br><a id='3.7'></a>
>> <strong><code>fs0ciety</code></strong><br>
<p></p>

<br>

```bash
grep -i "comment" grep.txt
8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2comment:'fs0ciety'u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM
```

<br>
<br>


<h2>Task 4 . Did someone said <code>STROPS</code></h2>

<p>I believe from here on, things are going to be a little different other than grepping the patterns. To keep things as simple as possible, we are going to start with a short note on what and where.</p>p>

<h3>String Manipulations (STRing OPerationS)</h3>

<p>Many people discard this topic in their tutorials/courses, which I believe is leaving behind the true power of linux and it's terminal interface. You ever see someone typing a very long command piping their outputs into some other commands? Well believe me when I say, you can select a single byte character from a GB long array of string bytes, if you could master that.<br><br>

If you're from a programming background you might have used indexing in arrays, slicing in python, or even grepping in terminal... All are a means of string manipulations. Especially in bash, we have a TON of tools to perform a same kind of operation, with different flags or string patterns specified, but obviously we will be choosing the one, providing us the shortest and easiest syntax possible. <br><br>

For strops, we have the following tools that I always keep in my arsenal and you should too:<br>

- tr<br>
- awk<br>
- sed<br>
- xargs<br><br>
Other commands to be familiar with:<br>

- sort<br>
- uniq<br><br>
I am gonna walk you through the commands I mentioned above in the following tasks.  </p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 4.1. <em>Press any key to continue...</em><br><a id='4.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
