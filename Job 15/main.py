def arrondi_et_trie(L):
    def arrondir(n):
        entier = int(n)
        if n - entier >= 0.5:
            return entier + 1  
            return entier  
    
 
    arrondis = []
    for num in L:
        arrondis.append(arrondir(num))
    
    
    for i in range(len(arrondis) - 1):
        for j in range(i + 1, len(arrondis)):
            if arrondis[i] > arrondis[j]:
                arrondis[i], arrondis[j] = arrondis[j], arrondis[i]
    
    return arrondis

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
resultat = arrondi_et_trie(L)


print(resultat)
