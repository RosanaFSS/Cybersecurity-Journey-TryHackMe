<h1 align="center">Cryptosystem</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/3b101da1-7e3c-4894-8962-1b27a895b8a2"><br>
July 4, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>424</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn public-key cryptography concepts by analyzing data</em>.<br>
Access it <a href="https://tryhackme.com/room/hfb1cipherssecretmessage"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/039f4bf1-c4e9-47d5-8ac6-9486cad599dc"></p>


<br>

<h2>Task 1 . Cryprosystem</h2>

<p>We intercepted a communication between Cipher and some 3 associates: Rivest, Shamir and Adleman. We were only able to retrieve a file.<br>

ORDER: Get the secret key from the recovered file.</p>

```bash
from Crypto.Util.number import *
from random import randrange
from flag import FLAG

def primo(n):
    n += 2 if n & 1 else 1
    while not isPrime(n):
        n += 2
    return n

p = getPrime(1024)
q = primo(p)
n = p * q
e = 0x10001
d = inverse(e, (p-1) * (q-1))
c = pow(bytes_to_long(FLAG.encode()), e, n)
#c = 3591116664311986976882299385598135447435246460706500887241769555088416359682787844532414943573794993699976035504884662834956846849863199643104254423886040489307177240200877443325036469020737734735252009890203860703565467027494906178455257487560902599823364571072627673274663460167258994444999732164163413069705603918912918029341906731249618390560631294516460072060282096338188363218018310558256333502075481132593474784272529318141983016684762611853350058135420177436511646593703541994904632405891675848987355444490338162636360806437862679321612136147437578799696630631933277767263530526354532898655937702383789647510
#n = 15956250162063169819282947443743274370048643274416742655348817823973383829364700573954709256391245826513107784713930378963551647706777479778285473302665664446406061485616884195924631582130633137574953293367927991283669562895956699807156958071540818023122362163066253240925121801013767660074748021238790391454429710804497432783852601549399523002968004989537717283440868312648042676103745061431799927120153523260328285953425136675794192604406865878795209326998767174918642599709728617452705492122243853548109914399185369813289827342294084203933615645390728890698153490318636544474714700796569746488209438597446475170891
```

<p><em>Answer the question below</em></p>

<p>1.1. What is the flag?<br>
<code></code></p>

```bash
from Crypto.Util.number import long_to_bytes, inverse, isPrime
import math

# Given n
n = 159562501620631698192829474437432743700486432744167426553488178239733838293647005739547092563912458265131077847139303789635516477067774797782854733026>

# Start from p approximate, since p is 1024 bits, we attempt to find p near sqrt(n)
sqrt_n = int(math.isqrt(n))
# Since p and q are close, try to find p by checking primes near sqrt(n)
# We'll check around sqrt(n). Given the specific construction, q is close to p

# Define a function to find p by checking candidates
def find_prime_factors(n):
    # Check a range around sqrt(n)
    for delta in range(-2*10**6, 2*10**6):
        p_candidate = sqrt_n + delta
        if p_candidate <= 1:
            continue
        if n % p_candidate == 0:
            q_candidate = n // p_candidate
            # Check if q_candidate is prime
            if isPrime(q_candidate):
                return p_candidate, q_candidate
    return None, None

# Implement isPrime (or import from Crypto.Util.number if available)
def isPrime(num):
    from Crypto.Util.number import isPrime
    return isPrime(num)

p, q = find_prime_factors(n)
if p is None or q is None:
    print("Failed to factor n with this method.")
else:
    # Compute phi
    phi = (p - 1) * (q - 1)
    e = 0x10001
    d = inverse(e, phi)
    # Given c
    c = 35911166643119869768822993855981354474352464607065008872417695550884163596827878445324149435737949936999760355048846628349568468498631996431042544>

    # Decrypt to get the message
    m_long = pow(c, d, n)
    MESSAGE_bytes = long_to_bytes(m_long)
    print("Recovered MESSAGE:", MESSAGE_bytes.decode())
```

```bash
Recovered MESSAGE: THM{Just_s0m3_small_amount_of_RSA!}
```

![image](https://github.com/user-attachments/assets/bf4b3cf8-5adc-4690-9b15-193db80e70a3)

<br>
<br>

![image](https://github.com/user-attachments/assets/9925917c-423b-4e27-93a8-839fe716393b)

![image](https://github.com/user-attachments/assets/5fa0aae1-788f-489e-a05a-cbf9e1661506)

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 4, 2025      | 424      |     164ᵗʰ    |      5ᵗʰ     |    2,291st  |     52nd   |  112,788 |    826    |     63    |

</div>

![image](https://github.com/user-attachments/assets/169edb4b-7f72-4389-b29f-7217d6d8f76f)

![image](https://github.com/user-attachments/assets/ad71ec5d-ad1b-4df7-86ca-0f57dfd2948b)

![image](https://github.com/user-attachments/assets/db39c9ea-ecfb-4d8c-9168-57d53c4d6cf6)

![image](https://github.com/user-attachments/assets/0d82d2cb-f899-4ad0-b540-103c056395c0)

![image](https://github.com/user-attachments/assets/fc90cc10-7ce4-4c36-bd68-166b0453f27c)
