def factorielle1(n):
    """Ceci est une fonction récursive qui appelle
   lui-même pour trouver la factorielle du nombre donné"""
    if n == 1:
        return n
    else:
        return n * factorielle1(n - 1)

print(factorielle1(6))                                                

def factorielle2(n):
    """Ceci est une fonction récursive qui appelle
   lui-même pour trouver la factorielle du nombre donné"""
    if n == 0:
        return 1
    else:
           f=1
           for i in range(2, n+1):
            f=f*i
           return f
print(factorielle2(6))