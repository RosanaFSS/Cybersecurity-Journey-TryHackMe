#!/usr/bin/env python3
import sqlite3
import hashlib
import string

first_chunk = "03c96ceff1a9758a1ea7c3cb8d43264616949d88"

def hopper_hash(ch, rounds):
    res = ch
    for _ in range(rounds):
        res = hashlib.sha1(res.encode()).hexdigest()
    return res

charset = string.printable
for rounds in (5000, 1000, 2000, 3000, 4000):
    for ch in charset:
        if hopper_hash(ch, rounds) == first_chunk:
           print("________________________________________________________________________________\n")
           print("TryHackMe BreachBlocker Unlock by Rosana")
           print(f"sbreachblocker@easterbunnies.thm contains  : {repr(ch)}")
           print("________________________________________________________________________________\n")
raise SystemExit
print("[-]                                            No Match.")