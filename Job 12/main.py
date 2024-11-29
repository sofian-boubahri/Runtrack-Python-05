def tri_insertion(L):
    N = len(L)
    for n in range(1, N):
        cle = L[n]
        j = n - 1
        while j >= 0 and L[j] > cle:
            L[j + 1] = L[j]  #
            j = j - 1
        L[j + 1] = cle

L = [99, 1, 5, 6, 1, 5, 88]
tri_insertion(L)

print(L)
