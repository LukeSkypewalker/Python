names = ['Finogina', 'Israelit', 'Ivanov', 'Kajatt-Vaccari', 'Kashinskaya', 'Khomenko', 'Kruglik', 'Kumar', 'Mityashov', 'Tsitsulin']
grades = [768,140,298,463,800,1431,1118,525,233,699]

#ASCII A=65..Z=90
possible_p = [67, 71, 73, 79, 83, 89, 97]
possible_q = [7, 11, 13, 17]

def isRelativelyPrime(a,b):
    while b:
        a,b = b, a%b
    return a == 1

def decrypt(grade,p,q):
    n=p*q
    z=(p-1)*(q-1)
    minProduct = 1000000
    for a in range (2,1000):
        if isRelativelyPrime(a,z):
            for b in range (2,1000):
                if a*b % z == 1:
                    if minProduct > a*b:
                        minProduct = a*b
                        e=a
                        d=b

    gradeD = grade**d % n
    gradeE = grade**e % n

    if 13 <= gradeD <=30:
        print (names[i], "grade^D = ", gradeD, " encryptedGrade = ", grade, "     p = ", p, "q = ", q, "e = ", e, "d = ",d , "   minProduct = ", minProduct , )

    if 13 <= gradeE <=30:
        print (names[i], "grade^E = ", gradeE, " encryptedGrade = ", grade, "     p = ", p, "q = ", q, "e = ", e, "d = ",d , "   minProduct = ", minProduct , )

i=0
for grade in grades:
    for p in possible_p:
        for q in possible_q:
            decrypt(grade,p,q)
    i+=1
