a=str(input("Introduceti numele si prenumele "))
b=a.split()
if b[0]==b[0].title(): 
    if b[1]==b[1].title():
        print("Numele introdus este corecte")
else:
    print("Numele introdus este gresit")