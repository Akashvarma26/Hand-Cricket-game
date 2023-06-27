#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as ran
flag=1
runs=0
Toss_comp=["BAT","BALL"]
print("                                              GAME: ODD/EVEN")
Player_choice=input("Enter ODD or EVEN: ").upper()
if Player_choice == "ODD":
    Comp="EVEN"
else:
    Comp="ODD"
num1=int(input("Enter a number for tossing: "))
num2=ran.randint(1,6)
print("Computer  CHOSE ",num2," for tossing.")
if ((num1+num2)%2==0 and Player_choice=="EVEN")  or  ((num1+num2)!=0 and Player_choice=="ODD"):
    flag=1
    print("Player has won the Toss!")
elif ((num1+num2)%2==0 and Comp=="EVEN")  or  ((num1+num2)!=0 and Comp=="ODD"):
    flag=0
    print("Computer has won the Toss!")
if flag==1:
    Player_win=input("Select BAT or BALL: ").upper()
    if Player_win=="BAT":
        while True:
            num1=int(input("Enter the number(1-6) of runs to score: "))
            num2=ran.randint(1,6)
            print("Computer chose ",num2)
            if num1!=num2:
                runs=runs+num1
            else:
                print("Player is OUT!")
                print("Total runs made by player is, ",runs)
                target=runs+1
                print("Target is ",target)
                break
        print("Time for Computer's batting and player's balling")
        while True:
            num1=int(input("Enter the number(1-6) for wicket: "))
            num2=ran.randint(1,6)
            print("Computer chose ",num2)
            if num1!=num2:
                target=target-num2
                if target<=0:
                    print("YOU LOSE ! COMPUTER WON THE GAME")
                    break
                else:
                    pass
            else:
                print("YOU WIN ! PLAYER WON THE GAME")
                break
    elif Player_win=="BALL":
        while True:
            num1=int(input("Enter the number(1-6) for wicket: "))
            num2=ran.randint(1,6)
            print("Computer chose ",num2)
            if num1!=num2:
                runs=runs+num2
            else:
                print("COMPUTER IS OUT! at ",runs)
                target=runs+1
                print("Target is ",target)
                break
        print("Time for Player's batting and Computer's balling")
        while True:
            num1=int(input("Enter the number(1-6) of runs to score: "))
            num2=ran.randint(1,6)
            print("Computer chose ",num2)
            if num1!=num2:
                target=target-num1
                if target<=0:
                    print("YOU WIN ! PLAYER WON THE GAME")
                    break
                else:
                    pass
            else:
                print("YOU LOSE ! COMPUTER WON THE GAME")
                break
elif flag==0:
    comp_choice=ran.choice(Toss_comp)
    print("Computer has chose ",comp_choice)
    if comp_choice=="BAT":
        while True:
            num1=int(input("Enter the number(1-6) for wicket: "))
            num2=ran.randint(1,6)
            print("Computer chose ",num2)
            if num1!=num2:
                runs=runs+num2
            else:
                print("COMPUTER IS OUT! at ",runs)
                target=runs+1
                print("Target is ",target)
                break
        print("Time for Player's batting and Computer's balling")
        while True:
            num1=int(input("Enter the number(1-6) of runs to score: "))
            num2=ran.randint(1,6)
            print("Computer chose ",num2)
            if num1!=num2:
                target=target-num1
                if target<=0:
                    print("YOU WIN ! PLAYER WON THE GAME")
                    break
                else:
                    pass
            else:
                print("YOU LOSE ! COMPUTER WON THE GAME")
                break
    elif comp_choice=="BALL":
        while True:
            num1=int(input("Enter the number(1-6) of runs to score: "))
            num2=ran.randint(1,6)
            print("Computer chose ",num2)
            if num1!=num2:
                runs=runs+num1
            else:
                print("Player is OUT!")
                print("Total runs made by player is, ",runs)
                target=runs+1
                print("Target is ",target)
                break
        print("Time for Computer's batting and player's balling")
        while True:
            num1=int(input("Enter the number for wicket: "))
            num2=ran.randint(1,6)
            print("Computer chose ",num2)
            if num1!=num2:
                target=target-num2
                if target<=0:
                    print("YOU LOSE ! COMPUTER WON THE GAME")
                    break
                else:
                    pass
            else:
                print("YOU WIN ! PLAYER WON THE GAME")
                break

