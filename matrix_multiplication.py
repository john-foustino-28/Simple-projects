def main():
    n=int(input("Enter the order of the matrix : "))
    print("Enter elements in m1")
    m1=getinput(n)
    print("Enetr elements in m2")
    m2=getinput(n)
    k=matmulti(m1,m2,n)
    print("m1:")
    printmat(m1)
    print("m2:")
    printmat(m2)
    print("Answer:")
    printmat(k)
    
    

#to input elements into the array
def getinput(n):
    x=[0]*n
    for i in range(n):
        x[i]=[0]*n
        for j in range(n):
            x[i][j]=int(input())
    return x

#multiplies the matrices
def matmulti(x,y,n):
    z=[0]*n
    for i in range(n):
        z[i]=[0]*n
        for j in range(n):
            z[i][j]=rowxcol(i,j,x,y)
    return z

#to multiply rows and columns
def rowxcol(row,col,x,y):
    sum=0
    for i in range(len(x)):
        sum+=x[row][i]*y[i][col]
    return sum

#to print out an entire matrix
def printmat(a):
    for i in range(len(a)):
        print(a[i])

main()
