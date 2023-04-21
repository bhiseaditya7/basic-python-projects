print('''
*******************************************************************************
         
                 /,   ,|   ,|
             /| /(  ,' / ,//
          \`( |/ /,'  (,/ |
           \ \ ` `   `  /--,
         _,_\ `  ` `  ``  /__
          '-.____________`  /
            [  \@,    :] `--,-..-
            [__________]__,'-._/
             )'o\ ' o) \/ )
             \  /   __  ./
              \=`   ==,\..
               \ -. `,' (333
               3`--''    \33.
             ,333_) /mm33333:.
            |:#:mmmmmm333333::
            |:#:333333333::##'
            ':#:ctr3333''#####\
             |:#:#\###########\
             |:#:##\###########\
             |:#:###\########|#\
             /:#:|:::\|::::::|:(
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("Welcome to the treasure island")
print("your mission is ti find the treasure")
print()
first=input("you are at crossroad where do you want to go? type left or right: ").lower()
if first=="right":
  print("Fall into a hole Game over")
elif first=="left":
  second=input("NOW swim or wait: ").lower()
  if second=="swim":
    print("Attack by a tror Game over!!")
  elif second=="wait":
    third=input("Which door red ,blue or yellow: ").lower()
    if third=="yellow":
      print("you win")
    elif third=="red":
      print("burned by fire game over")
    elif third=="blue":
      print("eaten by beast game over")
    else:
      print("game over")
  else:
    print("game over")
else:
  print("game over")
    
  
                    
                    