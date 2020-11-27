print("Luati cuvinte cu mai mult de 3 caractere ")
n=str(input("Inroduceti numele:"))
p=str(input("Introduceti numele orasului in care traiti:"))
a=str(input("Introduceti obiectul preferat:"))
b=str(input("Introduceti animalul preferata:"))
if (len(n)>2)and(len(p)>2)and(len(a)>2)and(len(b)>2):
    s=n[:2]+p[2]+a[:3]+b[:len(b)//2]
    print(s)
else:
    print("Cuvinte mai lungi de 3 litere !!!!!!!!!!! ")
