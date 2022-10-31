def calculateA(n):
    if n > 0:
        k = n ** 2
        print(k)
      
        calculateB(n - 1)
      


def calculateB(n):
    if n > 0:
        k = n ** 2
        print(k)
      
        calculateA(n - 1)


calculateA(3)
calculateB(4)



