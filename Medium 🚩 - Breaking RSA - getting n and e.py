#!/usr/bin/env python3
from Crypto.PublicKey import RSA
f = open("id_rsa.pub", "r")

key = RSA.importKey(f.read())

n = key.n
e = key.e

print(f"n = {n}")
print(f"e = {e}")
