print("Questo programma calcola il valore di un incognita x nell'equazione ax + b = 0")
a = int(input("inserire valore di a: "))
b = int(input("inserire valore di b: "))
if a == 0 and b == 0:
    print("Equazione indeterminata")
if a == 0 and b>0 or b<0:
    print("Equazione impossibile")
if a<0 or a>0 and b == 0:
    print("x = 0")
if a<0 or a>0 and b>0 or b<0:
    print("x=", -b/a)
