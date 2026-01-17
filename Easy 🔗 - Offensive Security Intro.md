<h1 align="center"><a href="https://tryhackme.com/room/offensivesecurityintrokKx12">Offensive Security Intro</a></h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/fec181ad-495b-45ff-8231-c96ac22f3ab7"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2017-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<br>
<h2>Task 1 . Think like a Hacker!</h2>
<p>Offensive Security is about thinking like an attacker to find weaknesses before real hackers do.<br>

In this room, you'll hack your first website in a safe and legal environment to see how ethical hackers operate.</p>


<p><em>Answer the question below</em></p>

<p>1.1. <em>Which term describes simulating a hacker's actions to find weaknesses?</em><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Offensive Security<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Defensive Security<br>
<code>Offensive Security</code></p>


<br>
<h2>Task 2 . Starting the Lab</h2>
<p>This room uses a virtual desktop to simulate a real system. Click the button below to get started!</p>
<p>A browser will automatically open, displaying FakeBank, a fake banking application. This is what you will be targeting.</p>

<p><em>Answer the question below</em></p>

<p>2.1. <em>What is the bank account number in the FakeBank application?</em><br>
<code>8881</code></p>

<br>
<h2>Task 3 . Find Hidden Pages</h2>
<h3>Goal</h3>
<p>Find a weakness in the FakeBank application. One common mistake is leaving hidden pages accessible.</p>

<h3>Open the Terminal</h3>
<p>Open the terminal on the machine. You will be using this to run your first hacking tool, <code>dirbuster</code>. The terminal icon will look like the following:</p>

<h3>Finding the Hidden Pages</h3>
<p>To find hidden pages using Dirbuster, we will use <code>dirb</code> and the URL that we wish to search:</p>

```bash
dirb http://fakebank.thm
```

<p>Any lines from the output that start with <code>+</code> are pages that have been found. Dirb will find two URLs.</p>

<p>3.1. Dirb found one URL, <code>http://fakebank.thm/images</code>. What is the other hidden URL?<br>
<code>http://fakebank.thm/bank-transfer</code></p>

<img width="1278" height="873" alt="image" src="https://github.com/user-attachments/assets/f0d0ce5a-d5a3-440d-b459-35308ea5033f" />


<br>
<br>
<br>
<h2>Task 4 . Attack the Admin Page</h2>
<p>You should now have found a hidden admin panel that lets you add money to your account.<br>

To open this URL in the browser of the simulated desktop:</p>

<p>[ ... ]</p>

<p>Add the following: <code>/bank-transfer</code> to the URL in the browser.<br>

Use your account number 8881 and deposit $2000 (or more). After depositing, return to your account page and confirm the balance is now positive.</p>


<p>4.1. <em>When your balance turns positive, a pop-up with green text appears.Enter the green words as the answer (ALL CAPS)</em><br>
<code>BANK-HACKED</code></p>


<img width="1231" height="433" alt="image" src="https://github.com/user-attachments/assets/36a73913-0f5a-43fc-854e-d52c90f0c57f" />

<br>
<br>
<br>

<img width="1312" height="455" alt="image" src="https://github.com/user-attachments/assets/5bee46bd-9155-44bc-885f-4aa892e41b2a" />

<br>
<br>
<br>
<h1 align="center">Challenge Completed</h1>


<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/228a77ef-9d6a-4b4a-9b6a-be5e2c5b2c2d"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/3db27903-1eb3-467d-9dbe-330c6a77c8cd"></p>


<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|17     |Easy 🔗 - Offensive Security Intro    |16 |     87ᵗʰ  |     3ʳᵈ    |      504ᵗʰ   |        5ᵗʰ     |    139,099  |    1,067    |    88     |
|16     |Hard 🚩 - Spring                      |15 |     87ᵗʰ  |     3ʳᵈ    |      540ᵗʰ   |        4ᵗʰ     |    138,942  |    1,066    |    87     |
|14     |Insane 🚩 - Scheme Catcher            |13 |     87ᵗʰ  |     3ʳᵈ    |      534ᵗʰ   |        5ᵗʰ     |    138,822  |    1,065    |    87     |
|13     |Hard 🚩 - Breachblocker Unlocker      |12 |     86ᵗʰ  |     3ʳᵈ    |      526ᵗʰ   |        5ᵗʰ     |    138,732  |    1,064    |    87     |
|11     |Medium 🚩 - Azure: Eyes Wide Shut     |10 |     86ᵗʰ  |     3ʳᵈ    |      558ᵗʰ   |        5ᵗʰ     |    138,450  |    1,063    |    86     |
|8      |Medium ⚙️ - Phishing Unfolding        | 7 |     86ᵗʰ  |     3ʳᵈ    |      508ᵗʰ   |        4ᵗʰ     |    138,372  |    1,062    |    84     |
|8      |Easy ⚙️ - Introduction to Phishing    | 7 |     96ᵗʰ  |     3ʳᵈ    |    2,479ᵗʰ   |       32ⁿᵈ     |    137,117  |    1,062    |    84     |
|8      |Medium 🔗 - KaffeeSec - SoMeSINT      | 7 |     98ᵗʰ  |     3ʳᵈ    |    2,847ᵗʰ   |       38ᵗʰ     |    137,052  |    1,062    |    84     |
|7      |Hard 🚩 - Hack Back                   | 6 |     98ᵗʰ  |     3ʳᵈ    |    2,798ᵗʰ   |       37ᵗʰ     |    136,908  |    1,061    |    84     |
|7      |Hard 🚩 - Dead End?                   | 6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     | 5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   | 3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence| 2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  | 1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |

</h6></div><br>

<p align="center">Global All Time:    87ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/17fc4af4-bd05-4df2-93d9-4e1ab9f691f1"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/95d62a4d-ffe4-4b5b-a945-f486d0959e5f"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/f8fa7321-1992-42dc-b90c-a7c1b16b6110"><br><br>
                  Global monthly:     504ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/1e4da618-dc65-4876-9e84-ef33094968e3"><br><br>
                  Brazil monthly:       5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/af7b43e2-5326-45ef-bff3-bb9339041194"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p




