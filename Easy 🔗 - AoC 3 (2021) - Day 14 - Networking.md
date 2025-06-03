<h1 align="center">Advent of Cyber 3 (2021) - Networking - Day 14 - Dev(Insecure)Ops</h1> 
<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/6371db5c-9eec-4f49-bdff-02ec11b425c9"><br>Jun 3, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my 393-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
<br>Access Adevent of Cyber 3 (2021) clicking <a href="https://tryhackme.com/room/adventofcyber3"</a>here.<br><br>
<img width="1000px" src=""></p>

<br>
<br>

<p>1.1. How many pages did the <code>dirb</code> scan find with its default wordlist?<br>
<code>4</code><br>

<h3>THM AttackBox</h3>

<p>

- <code>TargetIP</code>:<code>10.10.253.231</code>.<br>
- <code>AttackIP</code>:<code>10.10.43.30</code>.<br>
- Executed <code>dirb</code>.</p>

![image](https://github.com/user-attachments/assets/acd2c91b-3c3b-447e-83a0-8af09cb27a92)

<br>

<p>1.2. How many scripts do you see in the /home/thegrinch/scripts folder?<br>
<code>4</code><br>

<h3>AOC_CICD</h3>

<p>
  
- Navigated to the path <code>/home/thegrinch/script</code>.<br>
- Executed <code>ls</code>.</p>

![image](https://github.com/user-attachments/assets/cb356180-46a3-4785-a695-6c688f5865db)

<br>

<p>1.3. What are the five characters following $6$G in pepper's password hash?<br>
<code>ZUP42</code><br>

<h3>THM AttackBox</h3>

<p>

- Executed <code>ssh</code> with the credentials provided.<br>

![image](https://github.com/user-attachments/assets/72de3045-4c14-454f-8bef-59c04667b6af)

<br>

- Inspected the content of the  <code>loot.sh</code> script.<br>

![image](https://github.com/user-attachments/assets/9eeedb28-a42a-47de-b6bc-0d4cd98ead2e)

<br>

- Launched <code>nano</code> to inspect the content of the <code>loot.sh</code> script.<br>

![image](https://github.com/user-attachments/assets/2f8fa0de-3340-4530-87ff-981b0d494ec7)

<br>

- There is permission to edit <code>loot.sh</code>.<br>
- Changed it.<br>

![image](https://github.com/user-attachments/assets/d4bc108e-0287-4208-a0b4-32d1a0105f3f)

<br>


- Navigated to the path <code>/home/thegrinch/loot</code>.<br>
- Identified <code>4</code> files.<br>

![image](https://github.com/user-attachments/assets/0d5b4d90-139a-4592-8afa-0aed757c7855)

<br>

- Launched the web browser.<br>
- Navigated to <code>10.10.253.231/admin</code>.<br>

![image](https://github.com/user-attachments/assets/29a3cbce-d68b-474a-8524-edba4b006273)


<br>

- Viewed page source.<br>
- Clicked <code>ls.html</code>.<br>

![image](https://github.com/user-attachments/assets/840a6469-6777-4f99-b988-5c956c6dc4f3)

<br>

![image](https://github.com/user-attachments/assets/08240b88-abe9-4de8-a59e-301b13db7cfe)

<br>

![image](https://github.com/user-attachments/assets/61be6c74-c520-4892-90b0-6ba5ed3ee062)


<br>

<p>1.4. What is the content of the flag.txt file on the Grinch's user’s desktop?<br>
<code>____</code><br>


<br>


<br>
<br>

<h1 align="center">Challenge in Progress, 60%</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/c8e905ef-e357-4b57-a5a1-8d2eb1e7df5f"></p>
                   
<h1 align="center">My TryHackMe Journey</h1>


<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| Jun 3, 2025       |     393    |          205ᵗʰ         |            4ᵗʰ       |        5,648ᵗʰ       |           95ᵗʰ        |       105,955      |             762       |    62       |

</div>

<p align="center"> Global All Time: 205ᵗʰ <br><img width="300px" src="https://github.com/user-attachments/assets/098b3c2c-f36e-4d8e-801d-9737842d1284" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/a56654c5-8cba-40e2-81e9-61a8850f553e"><br><br>
                   Brazil All Time:   4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/d95638f5-9949-4d85-8e38-c13046e20ba4"><br><br>
                   Global monthly: 5,648ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/d6a17191-1e9d-49e3-a02a-0c7f94ab67cc"><br><br>
                   Brazil monthly:   95ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/710fdd3c-76f6-402b-871e-cd4a1d66183e"><br><br></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br><br>
<h1 align="center">Thank you very much ben, ashu, tryhackme, cmnatic, timtaylor, strategos, umairalizafar, jcfarris, and wesladd for developinng this experience so that I could sharpen my skills!</h1>
