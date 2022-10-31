def climb():
           X = int(input(""))
           Y = int(input(""))
            

           if X<Y:
                return 0    
           else:
                return (X-Y)%10

climb()
