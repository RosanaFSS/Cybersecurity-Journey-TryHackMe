
<p align="center">April 10, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{339}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="160px" src="https://github.com/user-attachments/assets/f091ab8b-6389-45e2-a36d-01b50b863eeb"></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{REmux The Tmux}}$$</h1>


<p align="center">"Updated, how to use tmux guide. Defaults and customize your workflow." <br>
It is classified as an info room.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/tmuxremux">here</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>
<br>

<h2>Task 1 . Tmux practice machine</h2>
<p>Tmux is known as a terminal multiplexer. That allows you to craft a single terminal however you need it.<br>

﻿Here is a machine you can use to complete the room if you don't have tmux installed on your local machine. Also comes with all the code and plugins needed for future tasks.<br>

Username: Redacted<br>

Password: Redacted</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Start the VM if you need it and ssh in.</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>


<br>

<p>Used <code>ssh</code> with the credentials provided to access the vm.</p>

<br>

![image](https://github.com/user-attachments/assets/f966cd63-4fbd-49e6-9c11-94d34817e3ad)

<br>
<br>

<h2>Task 2 . Starting tmux "Sessions" and default tmux "prefix"</h2>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>Do the ctrl and b keys need to be held down the whole time with every commands to work? yea/nay</em><br><a id='2.1'></a>
>> <strong><code>nay</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/273166d0-f0a1-4aa4-9465-56b3f473e067)

<br>

> 2.2. <em>How to start tmux with the session with the name "thm"?</em> Hint : <em>new session name without ""'s</em><br><a id='2.2'></a>
>> <strong><code>tmux new -s thm</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/93fc80c1-41f2-4ca1-b205-ede8525a9baf)

<br>

> 2.3. <em>How to change the current tmux session name?</em> Hint : <em>$ sign not the number 4</em><br><a id='2.3'></a>
>> <strong><code>ctrl b shift $</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/7a84975a-1c66-46c9-a644-f331a89372d0)

<br>

> 2.4. <em>How to quit a tmux session without closing the session? To attach back later.</em><br><a id='2.4'></a>
>> <strong><code>ctrl b d</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/bf4e58f1-4d90-4840-8b16-b12b40f55e3c)

<br>

> 2.5. <em>How to list all tmux sessions?</em>Hint : <em>short version of list-sessions</em><br><a id='2.5'></a>
>> <strong><code>tmux ls</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/f88aff97-10f2-4aac-90d9-52b9af858bc4)

<br>

> 2.6. <em>How to reattach to a detached tmux session with the session name of "thm"</em>Hint : <em>current session name without ""'s</em><br><a id='2.6'></a>
>> <strong><code>tmux a -t thm</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/6a79fe88-5cd3-43af-bf9d-d0500b2121da)


<br>

> 2.7. <em>How to create a new tmux session from your current tmux session with the name kali?</em><br><a id='2.7'></a>
>> <strong><code>tmux new -s kali d</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/f8bbd9fa-1c99-4106-9790-bbcc493f88e9)

<br>

> 2.8. <em>How to switch between two or more tmux sessions without detaching from the current tmux session?</em>Hint : <em>use the arrow keys to move up or down. Select sessions with the enter key.</em><br><a id='2.8'></a>
>> <strong><code>ctrl b s</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/52345ed0-a597-4333-96d8-04d93240b55a)

<br>

> 2.9. <em>How do you force kill the tmux session named "thm" if it's not responsive from a new terminal window or tmux session?</em><br><a id='2.9'></a>
>> <strong><code>tmux kill-session -t thm</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/3f683cab-2e97-4615-9ee2-5fe15b2811fc)


<br>

> 2.10. <em>Within a nested tmux session. A second tmux session within the first one. How to change the session name of the second/internal tmux session?</em>Hint : <em>need to use ctrl b for every tmux session.</em><br><a id='2.10'></a>
>> <strong><code>ctrl b ctrl b shift $</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/c50a3b38-7d65-49e9-a2cd-c95043256c8b)


<br>

> 2.11. <em>How to get into a tmux prompt to run/type tmux commands?</em>Hint : <em>: not ;</em><br><a id='2.11'></a>
>> <strong><code>ctrl b shift :</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/098ec209-6a46-4375-83c6-8705aba7618d)



<br>

> 2.12. <em>Are there more than one way to exit a tmux prompt? yea/nay</em><br><a id='2.12'></a>
>> <strong><code>yea</code></strong><br>
<p></p>

<br>

<h2>Task 3 . Manage tmux "Panes"</h2>




<h2>Task 4 . Manage tmux "Windows"</h2>





<h2>Task 5 . Tmux "copy" mode</h2>



<h2>Task 6 . Oh My Tmux and beyond</h2>



<h2>Task 7 . Oreo´s open-source .tmux.conf file/h2>








