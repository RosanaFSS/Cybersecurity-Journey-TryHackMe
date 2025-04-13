
<p align="center">April 11, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{340}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/5cd808a1-d047-4a49-b4e0-00f2682a28e4" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/6fcbf656-d31e-4b81-950f-0c4c980e3b43"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{REmux The Tmux}}$$</h1>
<p align="center">"Updated, how to use tmux guide. Defaults and customize your workflow." <br>
It is classified as an info room.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/tmuxremux">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/b5977194-1f76-4924-aa5a-214538257091"> </p>


<br>
<br>

<p>.  As my contribution I share the official <code>REMnux</code>  <a href="https://remnux.org/<br><br>">website</a>.<br>

.  REMnux® is a Linux Toolkit for Malware Analysis.<br><br>
.  REMnux® is a Linux toolkit for reverse-engineering and analyzing malicious software. REMnux provides a curated collection of free tools created by the community. Analysts can use it to investigate malware without having to find, install, and configure the tools.</p><br><br>



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

![image](https://github.com/user-attachments/assets/089ab743-1efa-49e5-8de6-8e51f718d807)


<br>

<h2>Task 2 . Starting tmux "Sessions" and default tmux "prefix"</h2>
<p>﻿To start a new tmux session just run the tmux command with no arguments. The first session create will have the name "0". By default, tmux status bar will be green. With session name on the left. Windows in the middle and window names in the middle. Hostname, time, and date on the right of the bottom green bar.</p>

<br>

![image](https://github.com/user-attachments/assets/60215eda-a049-496f-9272-5c19055f4fe0)

<br>

<p>﻿Tmux doesn't allow to create of a nested tmux within a tmux unless you force it to. When running the tmux command a second time.</p>

<br>

![image](https://github.com/user-attachments/assets/1d9620ed-f364-4e89-93d0-21eca2db6d55)

<br>

<p>To change the session name from "0" -> "box-dev". Must first learn how tmux is called. All commands within a tmux session all start with the tmux prefix is. By default, the tmux prefix is "Ctrl b".<br>

After the tmux prefix. To the hotkeys to change the current tmux session's name is "shift $". </p>

<h3>ctrl b shift $</h3>

<p>Retype the new name and then enter-key to save the new session name.</p>

<br>

![image](https://github.com/user-attachments/assets/35cd225c-ba9d-4b88-b8a9-98a2e76178e3)

<br>

![image](https://github.com/user-attachments/assets/bec14419-82e6-40d2-8a44-ad826a9653e3)

<br>


<p>If there is a need to create another tmux session within the current one. Use the -d argument with the tmux command. To spawn a new tmux session without attaching to it. In the example image below. The -s argument is used to specify the session name for the new session. Typed as "tmux new -s <new-session-name> -d".</p>

<br>

![image](https://github.com/user-attachments/assets/917c8a48-6541-4490-9420-a889a469fdc6)

<br>

<p>To list all active tmux sessions. Run tmux with list-sessions. Or the short version of list-sessions as ls. In the example below. Running tmux ls also shows the current session in use. Marked by "(attached)".</p>

<br>

![image](https://github.com/user-attachments/assets/a10e1dc6-fe85-48c0-9e21-c8ec840074cf)

<br>

<p>Exiting a tmux session without closing it can be done with the prefix. Followed by d</p><br>

<h3>ctrl b d</h3>
<p>Checking again with the tmux ls command. "(attached)" is missing from both sessions. This means the sessions are active but we are detached and are unable to interact with either session.</p>

<br>

![image](https://github.com/user-attachments/assets/3a124f37-0719-4b09-b80a-af7ae80caf03)


<br>

<p>To reattach to an active tmux session. Run tmux with the attach option and -t followed by the desired session name.</p>

<br>

![image](https://github.com/user-attachments/assets/e02120d5-ae82-4025-ac26-92de4edec326)

<br>

<p>The tmux session name has changed to the attached session of "tryhackme". Double-checking with tmux ls. Can confirm that "(attached)" also on the "tryhackme" session name.</p>

<br>

![image](https://github.com/user-attachments/assets/b9ba851a-9231-4719-bc5c-30f9f0ebb275)

<br>

<p>Delete a single session by its session name. Is done with the kill-session option with tmux. Followed by -t and the <target-session-name-to-delete></p>


<br>

![image](https://github.com/user-attachments/assets/c36c3748-d56f-40c6-8439-52482b9cec19)

<br>

<p>Listing sessions with tmux ls. This shows that the session name of box-dev has been removed. WARNING! By deleting the session. Anything open in that session will be lost if not saved before the tmux kill-session.</p>

<br>

![image](https://github.com/user-attachments/assets/f3ee4528-f38a-470b-9eeb-649a9e8b1fe5)

<br>

<p>In the example below there are many sessions open. Another way to swap sessions without having to detach and reattach to another session. Is to use the prefix. Followed by the s-key to list all open sessions. Using up or down arrow keys to navigate to the desired tmux session. Then enter to select the new session.</p>

<br>

<h3>ctrl b s</h3>

<br>

![image](https://github.com/user-attachments/assets/71defe81-1f20-4316-bae2-6db1c5883eab)

<br>

<p>Change from session name "0" to "tmux_remux" without having to leave the current tmux session.</p>

<br>

![image](https://github.com/user-attachments/assets/e1a2035b-5f15-4e9f-9963-689dbec54c61)

<br>


![image](https://github.com/user-attachments/assets/944f1bb9-fae5-4182-a2c5-9717b749cff9)

<br>

<p>From the five active sessions above. If there was a need to kill all the sessions except for a single one. When using the tmux kill-session. Use the -a argument to close all sessions except the one specified by the -t argument. Closing all tmux sessions except for the one named "is-0day-0k?". Checked with the tmux list-sessions.</p>

<br>

![image](https://github.com/user-attachments/assets/9e2b19fc-8858-4566-bd3b-2dfe9333d788)

<br>

<p>When spliting the session into different sized panes ("which will be covered in more detail in a later task"). The new pane will spawn in the directory that the tmux session was first started in. </p>

<br>

![image](https://github.com/user-attachments/assets/04d8b683-6f36-49a0-9464-d4ee5ef0ac77)

<br>

<p>To change the base starting directory. Must first learn about tmux prompt or command mode. The tmux prompt allows tmux sessions to run tmux commands without the tmux binary name. Useful when the terminal has been filled with other text. Enter a tmux prompt with prefix shift :</p>

<br>

<h3>ctrl b shift :</h3>

<p>Followed by "attach -c /path/to/new/starting/directory"</p>

<br>

![image](https://github.com/user-attachments/assets/539bb2b0-b0ab-43cf-82b2-b6ba1e589158)


<br>

<p>With the updated starting or base directory done above as /dev/shm. Creating a new pane start in the /dev/shm directory.</p>

<br>

![image](https://github.com/user-attachments/assets/ef119be9-e341-43a0-bf29-1fa5a0902ca3)

<br>

<p>Even though at the start tmux doesn't allow nested tmux within a tmux. Attaching or starting a new tmux session on another computer by an ssh connection. Can make a nested tmux. Not a problem. Just by changing the number of prefix used before the following command. Can determine which session gets the command.<br>

prefix, prefix, and command. This will run on the second nested tmux session of the ssh ubuntu machine.<br>

prefix and command. This will run on the first tmux session. The session running on the current machine's localhost.</p>

<br>

![image](https://github.com/user-attachments/assets/d7a462ed-b5c5-43e5-b92d-4afd72881432)


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

> 2.13. <em>Is tmux case sensitive. Will hitting the caps lock break tmux? yea/nay</em><br><a id='2.13'></a>
>> <strong><code>yea</code></strong><br>
<p></p>

<br>

> 2.14. <em>Within tmux prompt or command mode how would you change the tmux directory? Where a new window or pane will start from the changed directory of /opt.</em>Hint : <em>the short version of attach -c /new/path</em><br><a id='2.14'></a>
>> <strong><code>a -c /opt</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/e26562a8-26f8-4d2e-88fe-cd8753cbfd3e)

<br>

> 2.15. <em>How to kill all tmux sessions accept the one currently in use? With the name "notes".</em>Hint : <em>the short version of attach -c /new/path</em><br><a id='2.15'></a>
>> <strong><code>tmux kill-session -t notes -a</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/132ab1b1-8b2e-42d6-8fce-0551aa93f2d5)

<br>
<br>




<h2>Task 3 . Manage tmux "Panes"</h2>

<br>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 3.1. <em>How to create a new pane split horizontally?</em><br><a id='3.1'></a>
>> <strong><code>ctrl b shift "</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/f86540ef-d69c-4456-9124-65b371dd24f1)



<br>

> 3.2. <em>How to close a tmux pane like closing a ssh session?</em><br><a id='3.2'></a>
>> <strong><code>exit</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/7ce05736-c684-483a-914c-755599c3888d)



<br>

> 3.3. <em>How to create a new pane split vertically?</em><br><a id='3.3'></a>
>> <strong><code>ctrl b shift %</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/ae3eae99-54f8-407c-bb8c-c6a4ee871f0c)



<br>

> 3.4. <em>How to cycle between tmux pre built layout options? Starting with the number 1.</em><br><a id='3.4'></a>
>> <strong><code>ctrl b esc 1</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/574d75e7-2def-4d13-a381-b56fa712d507)


<br>


> 3.5. <em>How to cycle/toggle between tmux layouts, one at a time?</em><br><a id='3.5'></a>
>> <strong><code>ctrl b spacebar</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/4e80a8f0-cf01-4784-b284-494c7b0d9953)



<br>

> 3.6. <em>How to force quit a frozen, crashed or borked pane?</em><br><a id='3.6'></a>
>> <strong><code>ctrl b x y</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/e9f35bf3-d657-454f-b5b9-7a8e5e162747)



<br>

> 3.7. <em>How to move between the two must used tmux panes for the current tmux window?</em><br><a id='3.7'></a>
>> <strong><code>ctrl b ;</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/51ea0577-af0b-4935-bce6-f784a4d5ea61)



<br>

> 3.8. <em>Can you use the arrow to move to the desired pane? yea/nay</em><br><a id='3.8'></a>
>> <strong><code>yea</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/47260759-c161-4898-a824-fd26c77102b2)


<br>

> 3.9.<em>How to move the currently selected pane <code>clockwise/code>?</em><br><a id='3.9'></a>
<p></p>

![image](https://github.com/user-attachments/assets/b41b2d1b-7ee2-4497-a57a-1518ddf726a1)


<br>

![image](https://github.com/user-attachments/assets/3c3e65ea-0cb8-4bd5-b654-6127b35dc952)



<br>

> 3.10.<em>How to move the currently selected pane <code>counter-clockwise</code>?</em><br><a id='3.10'></a>
<p></p>

![image](https://github.com/user-attachments/assets/619059e4-fb94-4585-bba5-2cd8ca739cfe)


![image](https://github.com/user-attachments/assets/929627a3-044b-4703-9e6f-006666a90a62)



<br>

> 3.11.<em>Before using swap-pane. How to check for which pane has what number?</em><br><a id='3.11'></a>
>> <strong><code>ctrl b q</code></strong><br>
<p></p>


<br>

> 3.12.<em>How to swap two panes and move with the swapped pane?  Within tmux prompt mode. 1 -> 3 location</em><br><a id='3.12'></a>
>> <strong><code>swap-pane -s 3 -t 1</code></strong><br>
<p></p>


<br>

> 3.13.<em>How to swap two panes without changing the currently selected pane location? Within tmux prompt mode. 1 -> 4 pane number?</em><br><a id='3.13'></a>
>> <strong><code>swap-pane -t 4 -s 1</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/d2e3c88f-6d40-498d-82e7-8733eb70e6eb)



<br>
<br>



<h2>Task 4 . Manage tmux "Windows"</h2>





<h2>Task 5 . Tmux "copy" mode</h2>



<h2>Task 6 . Oh My Tmux and beyond</h2>



<h2>Task 7 . Oreo´s open-source .tmux.conf file/h2>




<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src=""><br>
<img width="900px" src=""></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 11, 2025    | 340      |     295ᵗʰ    |        8ᵗʰ   |    286ᵗʰ    |     2ⁿᵈ    |  92,590  |       653 |   59      |

</div>

<br>


<p align="center">Weekly League: Bronze 5ᵗʰ<br><br><img width="300px" src="https://github.com/user-attachments/assets/5c28fd77-9b27-4571-9e24-e04b84eff5f1"> </p>


<br>

<p align="center"> Global All Time: 295ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/0c8c3bba-497b-4d08-a366-0786ef1c75be"> </p>

<p align="center"> Brazil All Time:   8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/b384cfec-ea7a-46c2-ab7d-b01a2fe9d073"> </p>

<p align="center"> Global monthly:  286ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/da5f644c-21f2-4a1c-800a-5c27025b7bad"> </p>

<p align="center"> Brazil monthly:   2ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/2f89ef68-bd53-462d-af65-cc2fa971635a"> </p>


<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/OreoByte">OreoByte</a> and <a href="https://tryhackme.com/p/0day">0day</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 
