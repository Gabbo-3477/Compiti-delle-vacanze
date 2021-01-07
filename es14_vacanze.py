coppianum = int(input("Quante coppie di numeri vuoi vedere la loro so,ma o differenza?"))
for n in range(1, coppianum + 1):
    n1 = int(input("inserisci il valore di n1"))
    n2 = int(input("inserisci il valore di n2"))
    if n1*n2 > 10:
        if n1 < n2:
            print("la differenza dei numeri è, ",n2-n1)
        else:
            print("la differenza dei numeri è, ",n1-n2) 
        if n1*n2 <= 10:
            print("la somma dei numeri è", n1+n2)