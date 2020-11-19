#Euler totient upto a number n start

def phi_range(n):
    n += 1
    phi = [i for i in range(n)]
    for i in range(2, n):
        if phi[i] == i:
            for j in range(i, n, i):
                phi[j] -= phi[j]//i
    return phi

#End

if __name__=='__main__':
    print(phi_range(10))