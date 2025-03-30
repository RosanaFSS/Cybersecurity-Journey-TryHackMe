
<p align="center">March 26, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{324}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/e8c02e37-2847-445d-9504-728b988618bf6"></p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Breaking RSA}}$$
</h1>
<p align="center">Hop in and break poorly implemented RSA using Fermat's factorization algorithm. It is classified as a medium-level challenge, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Can be accessed clicking <a href="https://tryhackme.com/room/breakrsa">here</a>.</p>
                                                              
<p align="center"> <img width="900px" src="> </p>

<br>
<br>

<h2>Task 1 . Capture the flag</h2>
<h3>﻿A brief overview of RSA</h3>
<p>The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers, the "factoring problem". RSA key pair is generated using 3 large positive integers -</p>

![image](https://github.com/user-attachments/assets/6c332142-b272-4918-8751-e8062dc225a1)


<p>(e, n) are public variables and make up the public key. d is the private key and is calculated using p and q. If we could somehow factorize n into p and q, we could then be able to calculate d and break RSA. However, factorizing a large number is very difficult and would take some unrealistic amount of time to do so, provided the two prime numbers are randomly chosen.</p>

<h3>Introduction</h3>
<p>In a recent analysis, it is found that an organization named JackFruit is using a deprecated cryptography library to generate their RSA keys. This library is known to implement RSA poorly. The two randomly selected prime numbers (p and q) are very close to one another, making it possible for an attacker to generate the private key from the public key using Fermat's Factorization method.<br>

Below is an implementation of Fermat's factorization algorithm in Python.</p>

```bash
Below is an implementation of Fermat's factorization algorithm in Python.
#!/usr/bin/python3
# gmpy2 is a C-coded Python extension module that supports
# multiple-precision arithmetic.
# pip install gmpy2
from gmpy2 import isqrt
from math import lcm

def factorize(n):
    # since even nos. are always divisible by 2, one of the factors will
    # always be 2
    if (n & 1) == 0:
        return (n/2, 2)

    # isqrt returns the integer square root of n
    a = isqrt(n)

    # if n is a perfect square the factors will be ( sqrt(n), sqrt(n) )
    if a * a == n:
        return a, a

    while True:
        a = a + 1
        bsq = a * a - n
        b = isqrt(bsq)
        if b * b == bsq:
            break

    return a + b, a - b

print(factorize(105327569))
```

I suggest using the <a href="https://pypi.org/project/pycryptodome/">pycryptodome</a> Python library to answer the RSA-related questions below.



<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>How many services are running on the box?</em><br><a id='1.1'></a>
>> <strong><code>2</code></strong><br>
<p></p>

Used <code>nmap</code>.<br>

![image](https://github.com/user-attachments/assets/5cd475ae-11f8-419b-b46c-04722928757f)

<br>

> 1.2. <em>What is the name of the hidden directory on the web server? (without leading '/')</em><br><a id='1.2'></a>
>> <strong><code>development</code></strong><br>
<p></p>

Used <code>gobuster</code>.<br>

![image](https://github.com/user-attachments/assets/fec7eb17-88bd-4157-908d-4e5e0c8c246d)

<br>

> 1.3. <em>What is the length of the discovered RSA key? (in bits)</em><br><a id='1.3'></a>
>> <strong><code>4096</code></strong><br>
<p></p>

Navigated to <code>http://Target_IP</code>.<br>

![image](https://github.com/user-attachments/assets/6185f1bf-7dab-4c1c-8591-f75c3cd46461)

<br>

Navigated to <code>http://Target_IP/development</code>.<br>

![image](https://github.com/user-attachments/assets/791aeed1-2f8c-4c56-a877-76d58ce27154)

<br>

Navigated to <code>http://Target_IP/development/log.txt</code>.<br>

![image](https://github.com/user-attachments/assets/213f6c52-923c-45cf-9fbc-8faa4bb48023)


<br>

Navigated to <code>http://Target_IP/development/id_rsa.pub</code>.<br>
Downloaded <code>id_rsa.pub</code>.<br>

![image](https://github.com/user-attachments/assets/f7149fd3-b707-40f5-94d6-38ed6de615aa)

<p>Navigate to <code:http://Target_IP/development/log.txt</code> and identified <code>log.txt</code> content.</p>


<br>

Visualized the content of <code>id_rsa</code> using <code>cat</code>.<br>
Used <code>ssh-keygen -l -f id_rsa.pub</code> to determine the lenght in bits of the Public Key. .<br>

![image](https://github.com/user-attachments/assets/c36ee36e-021b-4c97-8384-ad9ff2c4f868)

<br>

 1.4. <em>What are the last 10 digits of n? (where 'n' is the modulus for the public-private key pair)</em><br><a id='1.4'></a>
>> <strong><code>1225222383</code></strong><br>
<p></p>

<p>It is important that you have installed <code>istall python3-gmp2</code>...</p>


<br>

![image](https://github.com/user-attachments/assets/3a419da0-e15c-4c44-ad02-d7247e4722c5)

```bash
#!/usr/bin/env python3
from Crypto.PublicKey import RSA
f = open("id_rsa.pub", "r")

key = RSA.importKey(f.read())

n = key.n
e = key.e

print(f"n = {n}")
print(f"e = {e}")


```


> 1.5. <em>Factorize n into prime numbers p and q</em><br><a id='1.5'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<p align="left">Ran the script below.</p>

```bash
import gmpy2

from Crypto.PublicKey import RSA

def fermat_factorization(n):
    """Fermat's Factorization Method"""
    a = gmpy2.isqrt(n) + 1
    b2 = gmpy2.square(a) - n
    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n
    p = a + gmpy2.isqrt(b2)
    q = a - gmpy2.isqrt(b2)
    return p, q


def calculate_private_key(p, q, e):
    """Calculate the private key 'd'"""
    phi = (p - 1) * (q - 1)
    d = gmpy2.invert(e, phi)
    return d


# Open the RSA key file
with open("id_rsa.pub", "r") as f:
    # Import the RSA key
    key = RSA.importKey(f.read())


# Retrieve the modulus (n) and public exponent (e)
n = key.n
e = key.e

# Print the modulus and public exponent
print(f"Modulus (n): {n}")
print(f"Public Exponent (e): {e}")

# Factorize n into p and q using Fermat's Factorization
p, q = fermat_factorization(n)

# Calculate private key 'd' using p, q, and public exponent 'e'
n = key.n
e = key.e

# Print the modulus and public exponent
print(f"Modulus (n): {n}")
print(f"Public Exponent (e): {e}")

# Factorize n into p and q using Fermat's Factorization
p, q = fermat_factorization(n)

# Calculate private key 'd' using p, q, and public exponent 'e'
d = calculate_private_key(p, q, e)
difference = abs(p - q)
print(f"p : {p}")
print(f"q : {q}")
print(f"Dference between q and p: {difference}")
print(f"Private Key (d): {d}")



key_params = (n, e, d, p, q)

key = RSA.construct((n,e,int(d)))



# Export the private key to a file

with open('id_rsa', 'wb') as f:
    f.write(key.export_key('PEM'))



print("\033[92mPrivate key generated and saved as 'id_rsa'.\033[0m")
```

<br>

<br>

<br>

1.6. <em>What is the numerical difference between p and q?</em><br><a id='1.6'></a>
>> <strong><code>1502</code></strong><br>
<p><br></p>

<P>Discovered the answer in 1.5.</P>

<br>

1.7. <em>Generate the private key using p and q (take e = 65537)</em><br><a id='1.7'></a>
>> <strong><code>No answer needed_______</code></strong><br>
<p><br></p>

<br>



1.8. <em>Generate the private key using p and q (take e = 65537)</em><br><a id='1.7'></a>
>> <strong><code>No answer needed</code></strong><br>
<p><br></p>


<br>

1.9. <em>What is the flag?</em><br><a id='1.7'></a>
>> <strong><code>________</code></strong><br>
<p><br></p>















