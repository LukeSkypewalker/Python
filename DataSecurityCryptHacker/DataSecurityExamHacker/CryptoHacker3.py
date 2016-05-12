names = ['Finogina', 'Israelit', 'Ivanov', 'Kajatt-Vaccari', 'Kashinskaya', 'Khomenko', 'Kruglik', 'Kumar', 'Mityashov',
         'Tsitsulin']
grades = [768, 140, 298, 463, 800, 1431, 1118, 525, 233, 699]

# ASCII A=65..Z=90
# possible_p = [67, 71, 73, 79, 83, 89, 97]
# possible_q = [7, 11, 13, 17]

P = [67, 67, 71, 71, 71, 73, 79, 79, 79, 83, 89, 89, 97]
Q = [11, 13, 17,  7, 11, 11, 11, 13, 17, 11, 13, 17, 11]




def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modInverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m

def isRelativelyPrime(a, b):
    while b:
        a, b = b, a % b
    return a == 1


def getKeys(p, q):
    minEDProduct = 100000
    minEDSum = 100000
    z = (p - 1) * (q - 1)
    for e in range(2, 1000):
        if not isRelativelyPrime(e, z): continue
        d = modInverse(e,z)
        if e * d < minEDProduct:
            minEDProduct = e * d
            minEDSum = e + d
            E = e
            D = d
        elif minEDProduct == e * d and e + d < minEDSum:
            E = e
            D = d

    return D, E, minEDProduct


def decrypt(grade, p, q):
    n = p * q
    d, e, minEDProduct = getKeys(p, q)

    gradeD = grade ** d % n
    if 13 <= gradeD <= 30:
        print(names[nameIndex], "grade^D = ", gradeD, " encryptedGrade = ", grade, "     p = ", p, "q = ", q, "e = ", e,
              "d = ",
              d, "   minProduct = ", minEDProduct, )

    if d != e:
        gradeE = grade ** e % n
        if 13 <= gradeE <= 30:
            print(names[nameIndex], "grade^E = ", gradeE, " encryptedGrade = ", grade, "     p = ", p, "q = ", q,
                  "e = ", e, "d = ",
                  d, "   minProduct = ", minEDProduct, )


nameIndex = 0
for grade in grades:
    for i in range(len(P)):
        decrypt(grade, P[i], Q[i])
    nameIndex += 1
