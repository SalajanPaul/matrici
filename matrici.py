def suma_matrice():
    n = 4
    sdp = 0
    sds = 0
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            print(i, ",", j, end="=")
            matrice[i][j] = int(input())
            if i<j:
                sdp = sdp + matrice[i][j]
            if i+j<n:
                sds = sds + matrice[i][j]
    print("Suma diagonala principala =", sdp)
    print("Suma diagonala secundara =", sds)
    print("")

def matrice_patratice():
    n = 4 #coloane
    m = 5 #renaduri
    matrice = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            print(i , ",",j, end="=")
            matrice[i][j] = int(input())
            matrice[i][j] = matrice[i][j]**2
            print(matrice)

    #afisare matrice
    for i in range(m):
        for j in range(n):
            print(i, " ", j, "=", matrice[i][j], end=",")
        print("")

if __name__ == '__main__':
    suma_matrice()
    matrice_patratice()


