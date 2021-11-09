"""on cherche le plus grand element du tableau qui en ajoutant a la somme est inferieur au montant a payer"""
p = [25,10,5,1] #le type de piece acceptée 
r = []          #le resultat
n = int(input("entrer le montant à payer :"))
s = 0

#fonction permettant de trouver le max
def max(p:list,s:int,n:int)->int:
    for e in p:
        temp = s+e 
        if temp<=n:
            return e 

while s<n:
    m = max(p,s,n)
    s += m
    r.append(m)
print(r)