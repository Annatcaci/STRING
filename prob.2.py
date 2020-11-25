s=str(input("Introduceti un si de caractere"))
n=m=p=0
for i in s:
    #a)
    if (ord(i)>=65) and (ord(i)<=90):
        n=n+1
    #b)
    if (ord(i)>=48) and (ord(i)<=57):
        m=m+1
    #c)
    if((ord(i)>=33)and(ord(i)<=47))or((ord(i)>=58)and(ord(i)<=64))or((ord(i)>=91)and(ord(i)<=96))or((ord(i)>=123)and(ord(i)<=127)):
        p=p+1
print("Numere majuscule sunt",n)
print("Cifre sunt",m)
print("Caractere speciale sunt",p)
