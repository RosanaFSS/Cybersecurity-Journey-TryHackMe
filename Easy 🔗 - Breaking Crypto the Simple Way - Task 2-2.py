
from sympy import factorint
from Crypto.Util.number import inverse, long_to_bytes

n = " " # Update n value here
c = " "  # Update c value here

# Get p and q values navigating to https://factordb.com/ and update it below
p = " "
q = " "

phi_n = (p - 1) * (q - 1)
print("Phi(n) =", phi_n)

e = 65537
d = inverse(e, phi_n)
print("Private key (d):", d)

plaintext = pow(c, d, n)
flag = long_to_bytes(plaintext)
print(flag.decode())
print("Decrypted Plaintext:", flag)
