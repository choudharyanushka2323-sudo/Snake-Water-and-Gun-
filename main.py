import random
  
'''
1 for sanke 
-1 for water
0 for gun 
'''

computer = random.choice([ 1 , -1 , 0 ])
you = input( " Enter your choice : ")
youDict = { "s" : 1 , "w" : -1 , "g" : 0 }

print( repr(you))
print( repr(youDict))
if you not in youDict :
    print( " Invalid Input ! 😞 Please choose from 's', 'w', or 'g'.")
    exit()

younum = youDict[ you]

if ( computer == younum ) :
    print( " its draw !😆")

else :
      if( computer == -1 and younum == 0) :
         print( " You Loose ! 😞")
         
      elif( computer == -1 and younum == 1) :
        print( " You Win ! 😊")
      elif ( computer == 1 and younum == -1) :
        print( " You Win ! 😊")
      else :
         print( " Something went wrong !")
