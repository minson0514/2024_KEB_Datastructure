import mymath

if __name__ == "__main__": #모듈 배울 때 했다네요~
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n}C{r} = {mymath.nCr(n,r)}")
    #f = int(input())
    #print(mymath.factorial(f))