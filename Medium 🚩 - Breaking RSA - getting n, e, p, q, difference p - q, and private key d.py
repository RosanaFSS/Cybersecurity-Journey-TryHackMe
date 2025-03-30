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
