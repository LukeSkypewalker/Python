# Iterative Algorithm (xgcd)
def iterative_egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q  # use x//y for floor "floor division"
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y

# Recursive Algorithm
def recursive_egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = recursive_egcd(b % a, a)
        return g, x - (b // a) * y, y

egcd = recursive_egcd



p=89
q=13
e=7
z = (p - 1) * (q - 1)



def modularInverse(e, z):
    g, x, y = egcd(e, z)
    if g != 1:
        return None
    else:
        return x % z

d = modularInverse(e, z)

MOD = (e*d) % z
print(MOD, d)
