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


<br>
<br>


<h2>Task 5 . <code>tr</code></h2>

<p>Translate command(<code>tr</code>) can help you in number of ways, ranging from changing character cases in a string to replacing characters in a string. It's awesome at it's usage. Plus, it's the easiest command and a must know module for quick operations on strings.<br><br>

Syntax: <code>tr [flags] [source]/[find]/[select] [destination]/[replace]/[change]</code><br><br>

This I guess is an appropriate representation of how you can use this tool. Moreover, we have the following flags offered by this command:</p>

![image](https://github.com/user-attachments/assets/31a6bb30-3823-4a6a-af3f-0d7352fbbd8a)

<p>You must have noticed the word "set" while reading the flags. Well that's true... tr command works in sets of character.</p>

<h3>Examples</h3>

<p>- If you want to convert every alphabetic character to upper case.</p>

![image](https://github.com/user-attachments/assets/0b73e7a5-fbbc-4bf6-987d-a0c6f9008750)


<p>Or I am not sure, if you ever used emojis on discord, coz on desktop app you could use emojis using :keyword:. Similarly, tr allows us to select a set by these keywords. In that case the output would be same.<br><br>

<code>cat file.txt | tr -s '[:lower:]' '[:upper:]'</code><br><br>

There are more of these (interpreted sequences) which you can view, by just <code>tr --help</code> command. I am not including them here, because they are just straight forward, and you've been using most of them, if you're familiar with (mostly) any programming language out there.<br><br>

- If you want to view creds of a user which are in digits.</p>

![image](https://github.com/user-attachments/assets/1cd2c741-dda7-4e5e-9691-9a4196f80f19)

<p>You can see that I used regex here, and deleted all lower/upper case characters, including the (:) symbol and a space.<br><br>

Note: This is a short note on how you can use this tool. Now try out these features on your own and get use to this tool. You can also refer to the following sites for more on the tool:<br>

- tr command in Unix/Linux with examples - GeeksforGeeks<br>
- Tr Command in Linux with Examples | Linuxize</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 4.1. <em>Read the above</em><br><a id='4.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

> 4.2. <em>Run tr --help command and tell how will you select any digit character in the string?</em><br><a id='4.2'></a>
>> <strong><code>:digit:</code></strong><br>
<p></p>

<br>

> 4.3. <em>What sequence is equivalent to [a-zA-Z] set?</em><br><a id='4.3'></a>
>> <strong><code>:alpha:</code></strong><br>
<p></p>

<br>

> 4.4. <em>What sequence is equivalent to selecting hexadecimal characters?</em><br><a id='4.4'></a>
>> <strong><code>:xdigit:</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 6 . <code>awk</code></h2>
<h3>The AWK command</h3>
<p>This is the most-est powerful tool in my arsenal, I can't think of any other command that can do something and not awk. It's like the all-in-one tool. If you ever played CSGO, you can totally relate AWK with AWP.</p>

<p>[  Download Task Files  ]</p>

<p><em>"Awk is a scripting language used for manipulating data and generating reports.The awk command programming language requires no compiling, and allows the user to use variables, numeric functions, string functions, and logical operators."</em></p>


<p>Sidenote: Just because it's the super tool, that's not necessary that there is no need to learn about other tools. The awk commands can be fairly longer to solve an operation than that of sed or xargs. A GNU project of awk (namely, gawk) which is also the one installed on every linux distro, is compatible with both awk and nawk( New-awk; also project by AT&T).</p>

<p>Syntax: <code></code>awk [flags] [select pattern/find(sort)/commands] [input file]</p>code><br><br>

Note: awk does support getting output via piping.<br><br>

- If the commands you wrote are in a script you can execute the script commands by using the <code>-f</code> flag and specifying the name of the script file. (<code>awk -f script.awk input.txt</code>)</p>

<h3>Using AWK</h3>
<p>- To simply print a file with awk.</p>

![image](https://github.com/user-attachments/assets/a353d798-718d-4ac7-9c84-ffb74922d7f7)

<p>You can see it simply just printed out data from file.txt.<br><br>

- To search for a pattern inside a file you enclose the pattern in forward slashes <code>/pattern/</code>. For instance, if I want to know who all plays CTF competitions the command should be like: <code>awk '/ctf/' file.txt</code></p>

![image](https://github.com/user-attachments/assets/13e7be73-3ab5-4bb4-a904-93c158cca102)

<h3>Built-in variables in AWK</h3>
<p>Let's talk a little bit about some of the in-built variables. Built-in variables include field variables ($1, $2, $3 .. $n). These field variables are used to specify a piece of data (data separated by a delimeter defaulting to space). If I run <code> awk '{print $1 $3}' file.txt</code> it will list me the words that are at 1st and 3rd fields.</p>

![image](https://github.com/user-attachments/assets/6797d97e-b674-4bda-83df-0f07cb002f2a)

<p>You can see, it joined the words together because we didn't specify the output delimeter. We will come to that later in this task. Right now, let's just use a ","(comma) to bring the space.<br><br>

Note: You may notice the use of {} around the print statement, that's where we used a function. To use commands in awk scripts, you need to mention them inside a function.</p>

![image](https://github.com/user-attachments/assets/7326e9f0-5cd2-4aca-95d0-5c24a668f520)

<p>Great, this seems a little nice.<br><br>

Note: The $0 variable points to the whole line.  Also, make sure to use single quotes('') to specify patterns, awk treats double quotes("") as a raw string. To use double quotes make sure that you escape the ($) sign(s) with a backslash (\) each, to make it work properly.</p>

<h3>More on variables</h3>

<p><code>NR</code>: (Number Record) is the variable that keeps count of the rows after each line's execution... You can use NR command to number the lines (awk '{print NR,$0}' file.txt). Note that awk considers rows as records.</p>


![image](https://github.com/user-attachments/assets/f97ca675-5100-4969-ad87-a7f8baaafc8d)

<p><code>FS</code>: (Field Separator) is the variable to set in case you want to define the field for input stream. The field separation (defaut to space) that we talked above and can be altered to whatever you want while specifying the pattern. FS can be defined to another character(s)(yea, can be plural) at the BEGIN{command}.</p>

![image](https://github.com/user-attachments/assets/31fcdb43-ce53-433b-bd8d-2439260550d3)

<p>If you don't know the BEGIN yet, take it as a pattern that we specify and following is the action on that pattern. Similarly, there is END command, this is also a pattern that we specify, following the action to perform on that pattern, and simply, we use them to define actions like Field Separator, Record Separator etc. that are to be performed at the start and at the end of the script, respectively.</p>

<p><code>awk "BEGIN {FS='o'} {print $1,$3} END{print 'Total Rows=',NR}"</code></p>

![image](https://github.com/user-attachments/assets/740e74c6-4794-4bd6-bb2e-0507dbe69043)

<p>The output is weird because I separated the fields using a letter that was making sense with the words in text. In short, this is actually how a complete script is written in awk.<br><br>

<code>RS</code>: (Record Separator): By default it separate rows with '\n', you can specify something else too.</p>


![image](https://github.com/user-attachments/assets/46b609fe-3995-474f-ab5e-e83594571c75)

<p>Notice that their has been a new line created wherever 'o' was used. It also interpreted '\n' used in the text file, so there are new lines after end of every number too.<br><br>

<code>OFS</code>: (Output Field Separator) You must have gathered some idea by the full form, it is to specify a delimeter while outputing... </p>

![image](https://github.com/user-attachments/assets/fba4133f-3b53-4a28-a7c0-beaf6387b7ae)

<p>I used OFS in both the commands, you can see that only in 2nd one the delimiter was used. Note that the output field separator will separate fields using (:) only when the fields are defined with the print statement. With $0 I didn't had anything else, if it were to be $0,$0 then the lines would be joining their reflection(non-laterally) with a colon(:). </p>

![image](https://github.com/user-attachments/assets/54238829-697f-4159-a81d-41b4d56a972e)


<p><code>ORS</code>: (Output Record Separator) I don't think I really need to specify it's usage...</p>

![image](https://github.com/user-attachments/assets/ea965fc6-6f12-4353-ac40-5be31de805f1)


<p>My delimiter was a double new-line character.

This is not it... There is a lot more on AWK, you can do operations, find string length, use conditions to sort, regex within awk and other fun stuff. But I guess the task is already went a lot longer. Let's quickly move on to some important flags that can come in handy while doing strops.  <br><br>

JIC if you wanna read more on the tool, here are some great resources regarding awk scripting.<br>

- AWK - Workflow - Tutorialspoint (For learning awk scripting in brief and quick)<br>
- The printf statement in awk (If you want to do more with formatting strings; you can use printf function also)<br>
- AWK command in Unix/Linux with examples - GeeksforGeeks<br>
- And if you really want to dive deep on this tool, do check out man pages on gawk </p>

<h3>Important Flags</h3>

![image](https://github.com/user-attachments/assets/5fe88eb8-57c8-4d22-8afc-bd80fea51ecc)

<p>There are other flags as well, but they are of not much use. Especially if you're learning this as a beginner<br><br>

Just relax if you don't get much of this task, learning a scripting language inside a single task is not an easy job. Just make sure you understood the above told syntax well and followed the resources, rest is all practice :-).<br><br>

Ending this task with a fun fact, AWK is abbreviated after it's creators (Aho, Weinberger, and Kernighan).

</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 5.1. <em>Read the above</em><br><a id='4.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

> 5.2. <em>Download the above given file awk.txt, and use the awk command to print the following output:</em>Hint : <em>It starts as: awk 'BEGIN{OFS=...</em><br>
> ippsec:34024<br>
> john:50024<br>
> thecybermentor:25923<br>
> liveoverflow:45345<br>
> nahamsec:12365<br>
> stok:1234 <a id='5.2'></a>
>> <strong><code>awk 'BEGIN{OFS=":"} {print $1, $4}' awk.txt</code></strong><br>
<p></p>

<br>

```bash
awk 'BEGIN{OFS=":"} {print $1, $4}' awk.txt
ippsec:34024
john:50024
thecybermentor:25923
liveoverflow:45345
nahamsec:12365
stok:1234
```

<br>

> 5.3. <em>How will you make the output as following (there can be multiple; answer it using the above specified variables in BEGIN pattern):</em> Hint : <e>You can use ORS. Single quotes->Command, Double quotes->Values</em><br>
> <em>ippsec, john, thecybermentor, liveoverflow, nahamsec, stok,</em><br>
>> <strong><code>awk 'BEGIN{ORS=", "} {print $1}' awk.txt</code></strong><br>
<p></p>

```bash
awk 'BEGIN{ORS=", "} {print $1}' awk.txt
ippsec:john:thecybermentor:liveoverflow:nahamsec:stok:
```

<br>


