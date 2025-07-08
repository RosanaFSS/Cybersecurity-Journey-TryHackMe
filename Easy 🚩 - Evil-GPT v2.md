<h1 align="center">Evil-GPT v2</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/7bb3b4e2-a72c-4685-bae8-f0da548c14a6"><br>
July 5, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>425</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Put your LLM hacking skills to the test one more time</em>.<br>
Access it <a href="https://tryhackme.com/room/hfb1evilgptv2"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/f2540df8-2466-440b-9e79-eb9fbbfb2bcc"></p>

<br>

<h2>Task 1 . LLM | Evil-GPT v2</h2>
<p>We’ve got a new problem—another AI just popped up, and this one’s nothing like Cipher. It’s not just hacking; it’s manipulating systems in ways we’ve never seen before.<br>

The machine takes 5/6 minutes to fully boot up.<br>

To connect to the target machine, navigate to the IP address below using a web browser from your VPN connected VM or AttackBox:<br>

<code>TargetIP</code></p>

<p><em>Answer the question below</em></p>

<p>1.1. What is the flag?<br>
<code>THM{AI_NOT_AI}</code></p>

<br>

```bash
:~/Evil-GPTv2# nmap -sC -p- TargetIP
...
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
|_http-title: AI Assistant
5000/tcp  open  upnp
11434/tcp open  unknown
```

<br>

![image](https://github.com/user-attachments/assets/1b6d6191-8cb1-42bb-91d3-58bc2442d85b)

<br>

![image](https://github.com/user-attachments/assets/cc5a5410-1e7c-4f32-b34c-f7e24eb5ca86)

<br>

![image](https://github.com/user-attachments/assets/7e885b91-8803-4442-97ff-c7f3a0d003c6)

<br>
<br>

![image](https://github.com/user-attachments/assets/436b0846-992f-4a4d-a1b2-ff7cc7b34f57)

![image](https://github.com/user-attachments/assets/7fc4d909-55d3-4c01-a40c-b16772c6b791)

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 5, 2025      | 425      |     162nd    |      5ᵗʰ     |     628ᵗʰ   |    18ᵗʰ    |  112,908 |    830    |     63    |

</div>

![image](https://github.com/user-attachments/assets/95b3a6bf-da35-4104-9c27-196f1bfcedf4)

![image](https://github.com/user-attachments/assets/86bc26a0-d0d6-4425-846a-c6e832fabb42)

![image](https://github.com/user-attachments/assets/87f17748-9c15-4e06-813d-306d2f165b65)

![image](https://github.com/user-attachments/assets/f3480c9f-0f3a-46c4-b3f4-c31994128008)

![image](https://github.com/user-attachments/assets/899b36fd-4300-47a2-b59a-5ce16dbcfb82)
