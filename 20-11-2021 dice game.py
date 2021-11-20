import random

l = []
user_data = []
extra_chance = []
another_extra_chance = []

loop = input("press 's' to start the game : ")

while loop == 's' :
    
    player = int(input("How many player you want : "))
    
    for i in range(player) :
        p = input("Enter the name : ")
        l.append(p)

    gameState = input("Type 'start' to Roll the Dice : ")
    
    while gameState == "start" :
        
        for i in range (len(l)) :
            
            user = random.randint(1 , 6)
            user_data.append(user)
            
        print("Result of player :" ,user_data)
        m = max(user_data)
        print("Winner is : ",m )
        user_data.clear()
        l.clear()
        
        if m == 6 :
            
            print("Wait you got extra chance!")
            c = random.randint(1 , 6)
            extra_chance.append(c)
            print("Result of extra chance : " , extra_chance)
            
            if c == 6 :
                
                print("wow you so lucky you got another extra chance!")
                y = random.randint(1 , 6)
                another_extra_chance.append(y)
                print("Result of another extra chance : " , y)
                
#         if loop != 's' :
#             gameState = 'END'

        break
    
    loop = input("Do you want to play 1 more Round type 's' : ")
        
    
    

