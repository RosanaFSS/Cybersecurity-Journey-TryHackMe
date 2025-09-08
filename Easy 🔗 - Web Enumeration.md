<h1 align="center">Web Enumeration</h1>
<p align="center">2025, September 8<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>490</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn the methodology of enumerating websites by using tools such as Gobuster, Nikto and WPScan</em><br>
<img width="80px" src="image" src="https://github.com/user-attachments/assets/6e0971b8-6c5d-4d01-8303-8571ffa96e14"><br>
Access this TryHackMe´s walkthrough <a href=https://tryhackme.com/room/webenumerationv2">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/84368097-0b43-4b6d-8c01-318aca035ab0"></p>

<br>


<h2>Task 1 . Introduction</h2>
<h3>Introduction</h3>
<p>Welcome to Web Enumeration! In this room, we'll be showcasing some of the most fundamental tools used in the enumeration stage of a web target. Good enumeration skills are vital in penetration testing -- how else are you supposed to know what you're targeting?! It is, however, rather easy to fall into rabbit holes. <br>

The tools we'll showcase will hopefully make this process easier. You'll be able to apply the knowledge gained for each tool on an Instance dedicated to each tool.</p>

<h3>Prerequisities for this lab</h3>

<p>You will need to be connected to the TryHackMe network if you are not using the TryHackMe AttackBox or Kali instance. Other than that, all you need is a good posture and some willpower!<br>

Note: This room has been written as if you were using the TryHackMe AttackBox</p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s get started<br>
<code>No answer needed</code>
  
<h2>Task 2 . Manual Enumeration</h2>

<p>2.1. I gotcha!<br>
<code>No answer needed</code>

<h2>Task 3 . Introduction to Gobuster</h2>

<p><em>Answer the question below</em></p>

<p>3.1. No questions<br>
<code>No answer needed</code>

<h2>Task 4 . Gobuster Modes</h2>

<p><em>Answer the question below</em></p>

<p>4.1. I get the hang of it!<br>
<code>No answer needed</code>

<h2>Task 5 . Useful Wordlists</h2>
<h3>Useful Wordlists</h3>
<p>There are many useful wordlists to use for each mode. These may or may not come in handy later on during the VM portion of the room! I'll go over some of the ones that are on Kali by default as well as a short section on SecLists.</p>

<h3>Kali Linux Default Lists</h3>
<p>Below you will find a useful list of wordlists that are installed on Kali Linux by default. This is as of the latest version at the time of writing which is 2020.3. Anything with a wildcard (*) character indicates there's more than one list that matches. Keep in mind, a lot of these can be interchanged between modes. For example, "dir" mode wordlists (such as ones from the dirbuster directory) will contain words like "admin", "index", "about", "events", etc. A lot of these could be subdomains as well. Give them a try with the different modes!<br>

- /usr/share/wordlists/dirbuster/directory-list-2.3-*.txt<br>
- /usr/share/wordlists/dirbuster/directory-list-1.0.txt<br>
- /usr/share/wordlists/dirb/big.txt<br>
- /usr/share/wordlists/dirb/common.txt<br>
- /usr/share/wordlists/dirb/small.txt<br>
- /usr/share/wordlists/dirb/extensions_common.txt - Useful for when fuzzing for files!</p>

<h3>Non=Standard Lists</h3>
<p>In  addition to the above, Daniel Miessler has created an amazing GitHub repo called SecLists. It compiles many different lists used for many different things. The best part is, it's in apt! You can sudo apt install seclists and get the entire repo! We won't dive into any other lists as there are many. However, between what's installed by default on Kali and the SecLists repo, I doubt you'll need anything else.</p>


<p><em>Answer the question below</em></p>

<p>5.1. No questions<br>
<code>No answer needed</code>

<h2>Task 6 . Practical Gobuster (Deploy 1)</h2>
<h3>Gobuster Challenges</h3>
<p>Now's your chance to check what you've learned. Deploy the VM, allow five minutes for it to fully deploy and answer the following questions! Good luck!<br>

You will also need to add "webenum.thm" to your /etc/hosts file to start off with like so:<br>

<code>echo "MACHINE_IP webenum.thm" >> /etc/hosts</code><br>

You will also need to add any virtual hosts that you discover through the same way, before you can visit them in your browser i.e.:<br>

<code>echo "MACHINE_IP mysubdomain.webenum.thm" >> /etc/hosts</code><br>

Any answer that has a list of items will have its answer formatted in the following way: ans1,ans2. Be sure to format your answers like that to get credit.</p>

<p><em>Answer the questiona below</em></p>


<p>6.1. Run a directory scan on the host. Other than the standard css, images and js directories, what other directories are available?<br>
<code>public,Changes,VIDEO</code>


<img width="1016" height="394" alt="image" src="https://github.com/user-attachments/assets/c4283e68-6697-4395-8f5a-61575dbf1c74" />

<br>
<p>6.2. Run a directory scan on the host. In the "C******" directory, what file extensions exist?<br>
<code>conf,js</code>

<img width="1189" height="381" alt="image" src="https://github.com/user-attachments/assets/24e83636-66b2-450f-bab4-2ad90a05b164" />

<br>
<p>6.3. There's a flag out there that can be found by directory scanning! Find it!<br>
<code>thm{n1c3_w0rk}</code>

<img width="1060" height="282" alt="image" src="https://github.com/user-attachments/assets/3d51a7cc-e406-4a1c-bf28-78283536b779" />

<img width="1063" height="217" alt="image" src="https://github.com/user-attachments/assets/04f6c76d-27e2-4d44-bbf8-23b0a3099fa1" />


<br>
<p>6.4. There are some virtual hosts running on this server. What are they?<br>
<code>_____________</code>



<br>
<p>6.5. There's another flag to be found in one of the virtual hosts! Find it!<br>
<code>thm{gobuster_is_fun}</code>

<img width="1289" height="403" alt="image" src="https://github.com/user-attachments/assets/d91b5612-f89f-4bdc-9b3a-62201704b463" />

<img width="1056" height="167" alt="image" src="https://github.com/user-attachments/assets/3ab4fdc4-2d85-4391-ab74-fd67d0909dbe" />


<br>
<br>


<p>To be continued ...</p>




<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src=""><br>
                  <img width="800px" src=""></p>

<h2 align="center">My TryHackMe Journey</h2>


<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time   |   All Time   |   Monthly   |   Monthly  | Points   | Rooms     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                                       |         |    Global    |    Brazil    |   Global    |   Brazil   |          | Completed |           |
| 2025, Sep 8       |Easy 🔗 - <code><strong>Web Enumeration</strong></code>| 490| 113ʳᵈ | 5ᵗʰ   |    553ʳᵈ    |     9ᵗʰ    | 124,882  |  951      |    73     |
| 2025, Sep 8       |Easy 🔗 - iOS: Forensics| 490| 113ʳᵈ | 5ᵗʰ   |    548ᵗʰ    |     9ᵗʰ    | 124,850  |  951      |    73     |
| 2025, Sep 7       |Medium 🚩 - VulnNet: Active| 489| 114ᵗʰ | 5ᵗʰ   |    542ⁿᵈ    |     9ᵗʰ    | 124,746  |  950      |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489|     114ᵗʰ |     5ᵗʰ      |    535ᵗʰ   |     9ᵗʰ    | 124,716  |  949      |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489     |     113ʳᵈ    |     5ᵗʰ      |    508ᵗʰ   |     9ᵗʰ    | 124,886  |  948      |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488     |     114ᵗʰ    |      5ᵗʰ     |     683ᵗʰ   |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ   |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ   |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488     |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ   |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487     |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ   |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487     |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ   |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486     |	   113ʳᵈ   |	     5ᵗʰ   	|      579ᵗʰ   |	  10ᵗʰ    |	124,018  |	  940	   |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486     |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ   |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485     |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ   |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484     |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ   |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483     |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ   |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   114ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/b54c6b23-3201-4220-abc0-13122ac9838c"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/a3a366cf-e2ce-4ec8-8f4b-0e0190e35c73"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f37a18b1-fe1e-4af0-9f02-2948583b4f9d"><br>
                  Global monthly:    553ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/0fef4dbe-45d9-435d-b7e5-2907f95cf43d"><br>
                  Brazil monthly:      9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3f3435a5-6669-4560-8362-6517a3ad4bd2"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>  
