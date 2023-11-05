import random
z=1
while z==1:
  
  print("")
  choice=int(input('''WE HAVE FEW PROGRAMS TO ENTERTAIN YOU!
1.RANDOM NUMBER GUESSING!
2.RANDOM DICE ROLLING SIMULATOR!
3.RANDOM PASSWORD GENERATOR!
4.EXIT

So what would you choose: '''))
  print(" ")
  if choice==1:
    n = random.randrange(1,100)
    print("Lets play a game of guessing random numbers between 1 to 100!")
    print(" ")
    a=input("DO YOU WANT TO PLAY? (Y/N) ").upper()
    while a=='Y':
      if a!='Y':
        break
        z=1
      else:
        print("YOU WILL GET 5 CHANCES TO GUESS THE NUMBER!")
        print(" ")
        print("Chance Remaining: ",5)
        guess = int(input("Enter any number: ")) 
        for y in range (4,-1,-1):
          if guess >= n-5 and guess <= n-1:
             print("Your are close but, The number you guessed is lower!")
             print(" ")
             if y<1:
                  print("Better luck next time !")
                  print(" ")
                  break
             else:
                print("Chance Remaining: ",y)
                guess = int(input("Enter number again: "))
          elif guess >= n+1 and guess <= n+5:
                print("Your are close but, The number you guessed is higher!")
                print(" ")
                if y<1:
                   print("Better luck next time !")
                   print(" ")
                   break
                else:
                   print("Chance Remaining: ",y)
                   guess = int(input("Enter number again: "))
          elif guess < n and guess >= 1:
               print("The number you guessed is lower!")
               print(" ")
               if y<1:
                   print("Better luck next time !")
                   print(" ")
                   break
               else:
                   print("Chance Remaining: ",y)
                   guess = int(input("Enter number again: "))
          elif guess > n and guess <= 100:
               print("The number you guessed is higher!")
               print(" ")
               if y<1:
                  print("Better luck next time !")
                  print(" ")
                  break
               else:
                  print("Chance Remaining: ",y)
                  guess = int(input("Enter number again: ")) 
          elif guess >100:
               print("INVALID INPUT : CHOOSE NUMBERS BETWEEN 1 - 100!")
               print(" ")
               if y<1:
                  print("Better luck next time !")
                  print(" ")
                  break
               else:
                  print("Chance Remaining: ",y)
                  guess = int(input("Enter number again: "))
          elif guess==n:
               print("you guessed it right!!")
               print(" ")   
               break
        a=input("DO YOU WANT TO PLAY AGAIN ? (Y/N) ").upper()

  elif choice==2:
    b=input("DO YOU WANNA ROLL THE DICE? (Y/N) ").upper()  
    while b=='Y':  
     if b!='Y':
         break
         z=1
     else:
        print ("LETS ROLL THE DICE !")
        num=random.randint(1,6)
        print("THE NUMBER OBTAINED AFTER ROLLING THE DICE IS:",num)
        if num==1:
           print(
        '''
        -------
       [       ]
       [   0   ]
       [       ]
        -------
       '''
        )
        elif num==2:
           print(
        '''
        -------
       [ 0     ]
       [       ]
       [     0 ]
        -------
       '''
           )
        elif num==3:
           print(
        '''
        -------
       [ 0     ]
       [   0   ]
       [     0 ]
        -------
       '''
              )
        elif num==4:
           print(
        '''
        -------
       [ 0   0 ]
       [       ]
       [ 0   0 ]
        -------
       '''
              )
        elif num==5:
           print(
        '''
        -------
       [ 0   0 ]
       [   0   ]
       [ 0   0 ]
        -------
       '''
              )
        elif num==6:
           print(
         '''
        -------
       [ 0 0 0 ]
       [ 0 0 0 ]
       [ 0 0 0 ]
        -------
       '''
             )
     b=input("DO YOU WANNA ROLL THE DICE AGAIN ? (Y/N) ").upper()
           
  elif choice==3:
    char="abcdefghijklmnopqrstuvwxyzAQZWSXEDCVFRTGBNHYUJMKILOP1234567890!@#$%^&*_?|!?"
    c=input("DO YOU WANT TO GENERATE A PASSWORD? (Y/N) ").upper()
    while c=='Y':
      if c!='Y':
       break
       z=1
      else:
        password_len=int(input("What length would you like your password to be : "))
        password_count=int(input("How many passwords would you like : "))
        for i in range(0,password_count):
          password=""
          for j in range(0,password_len):
            password_char=random.choice(char)
            password+=password_char
          print("Here is your password : ",password)
        c=input("DO YOU WANT TO GENERATE A  NEW PASSWORD ? (Y/N) ").upper()
  elif choice==4:
      print("BYE BYE")
      break
  else:
      print("Invalid choice!")
  
