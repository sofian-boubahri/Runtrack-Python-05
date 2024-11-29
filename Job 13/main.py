def supprimer_doublons(L):
    result = []
    
    for element in L:
        present = False
        for unique in result:
            if unique == element:
                present = True
                break
        if not present:
            result.append(element)
    
    return result

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
L_sans_doublons = supprimer_doublons(L)

print(L_sans_doublons)
