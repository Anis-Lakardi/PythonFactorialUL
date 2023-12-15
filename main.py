import numpy as np

def FactLU(A):
    n = len(A)
    L = np.eye(n)
    U = np.copy(A)

    for k in range(n-1):
        for i in range(k+1, n):
            L[i, k] = float(U[i, k] / U[k, k])
            for j in range(k, n):
                U[i, j] = float(U[i, j] - L[i, k] * U[k, j])

    return L, U

def ResolutionSysteme(L, U, B):
    n = len(L)
    Y = np.zeros(n)
    X = np.zeros(n)

     
    for i in range(n):
        Y[i] = B[i]
        for j in range(i):
            Y[i] = Y[i] - L[i, j] * Y[j]

    
    for i in range(n-1, -1, -1):
        X[i] = Y[i]
        for j in range(i+1, n):
            X[i] = X[i] - U[i, j] * X[j]
        X[i] = X[i] / U[i, i]

    return X

def inputMatrix():
     
    print("La matrice doit être carrée")
    size = int(input("Entrez la taille de la matrice: "))

     
    matrix = np.zeros((size, size))

     
    for i in range(size):
        for j in range(size):
            value = float(input(f"Entrez la valeur de la matrice[{i+1},{j+1}] : "))
            matrix[i, j] = value

    return matrix

def inputVecteur():
     
    print("tu vas fournir le vecteur: ")

     
    b = np.zeros(3)

     
    for i in range(3):
        value = float(input(f"Entrez la valeur de la matrice[{i+1}]: "))
        b[i] = value

    return b

def AfficherMatrice(matrice):
    print(matrice)

def AfficherVecteur(vecteur):
    print(vecteur)

  
# le programme prancipal
matrice_A = inputMatrix()
B = inputVecteur()

L, U = FactLU(matrice_A)

print("Matrice L:")
AfficherMatrice(L)
print("Matrice U:")
AfficherMatrice(U)
print("Vecteur B:")
AfficherVecteur(B)

X = ResolutionSysteme(L, U, B)
print("Solution du système:")
print(X)