cnp=str(input("Introduceti CNP-ul di pasaport "))
n=0
if len(cnp)!=13:
    print("Ati introdus un numar mai mic de cifre")
if len(cnp)==13:
    for i in cnp:
        if(ord(i)<=57)and(ord(i)>=48):
            n+=1
    if(n==13):    
        print("CNP-ul este corect(format din cifre)")
    else:
        print("CNP-ul e gresit(nu e format din cifre)")