
# made by kuro

import random

mode = int(input("Please enter what mode you would like to play in \n1=easy\n2=medium\n3=hard\n"))

def easy_mode():
    print("please guess a number between 0 - 5\n")
    userpoints = 0
    robotnum1 = random.randint(0, 5)
    robotnum2 = random.randint(0, 5)
    robotnum3 = random.randint(0, 5)
    robotnum4 = random.randint(0, 5)
    robotnum5 = random.randint(0, 5)
    robotnum6 = random.randint(0, 5)
    robotnum7 = random.randint(0, 5)
    robotnum8 = random.randint(0, 5)
    robotnum9 = random.randint(0, 5)
    robotnum10 = random.randint(0, 5)
    usernum1 = int(input("Enter Your first guess: "))
    if robotnum1 == usernum1:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum1}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum1}")
        print("\n")
    usernum2 = int(input("Enter Your second guess: "))
    if robotnum2 == usernum2:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum2}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum2}")
        print("\n")
    usernum3 = int(input("Enter Your third guess: "))
    if robotnum3 == usernum3:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum3}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum3}")
        print("\n")
    usernum4 = int(input("Enter Your fourth guess: "))
    if robotnum4 == usernum4:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum4}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum4}")
        print("\n")
    usernum5 = int(input("Enter Your fith guess: "))
    if robotnum5 == usernum5:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum5}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum5}")
        print("\n")
    usernum6 = int(input("Enter Your sixth guess: "))
    if robotnum6 == usernum6:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum6}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum6}")
        print("\n")
    usernum7 = int(input("Enter Your seventh guess: "))
    if robotnum7 == usernum7:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum7}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum7}")
        print("\n")
    usernum8 = int(input("Enter Your eighth guess: "))
    if robotnum8 == usernum8:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum8}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum8}")
        print("\n")
    usernum9 = int(input("Enter Your ninth guess: "))
    if robotnum9 == usernum9:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum9}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum9}")
        print("\n")
    usernum10 = int(input("Enter Your last guess: "))
    if robotnum10 == usernum10:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum10}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum10}")
        print("\n")



def med_mode():
    print("Please enter your guesses from 0 - 10\n")
    userpoints = 0
    robotnum1 = random.randint(0, 10)
    robotnum2 = random.randint(0, 10)
    robotnum3 = random.randint(0, 10)
    robotnum4 = random.randint(0, 10)
    robotnum5 = random.randint(0, 10)
    robotnum6 = random.randint(0, 10)
    robotnum7 = random.randint(0, 10)
    robotnum8 = random.randint(0, 10)
    robotnum9 = random.randint(0, 10)
    robotnum10 = random.randint(0, 10)
    usernum1 = int(input("Enter Your first guess: "))
    if robotnum1 == usernum1:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum1}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum1}")
        print("\n")
    usernum2 = int(input("Enter Your second guess: "))
    if robotnum2 == usernum2:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum2}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum2}")
        print("\n")
    usernum3 = int(input("Enter Your third guess: "))
    if robotnum3 == usernum3:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum3}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum3}")
        print("\n")
    usernum4 = int(input("Enter Your fourth guess: "))
    if robotnum4 == usernum4:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum4}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum4}")
        print("\n")
    usernum5 = int(input("Enter Your fith guess: "))
    if robotnum5 == usernum5:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum5}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum5}")
        print("\n")
    usernum6 = int(input("Enter Your sixth guess: "))
    if robotnum6 == usernum6:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum6}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum6}")
        print("\n")
    usernum7 = int(input("Enter Your seventh guess: "))
    if robotnum7 == usernum7:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum7}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum7}")
        print("\n")
    usernum8 = int(input("Enter Your eighth guess: "))
    if robotnum8 == usernum8:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum8}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum8}")
        print("\n")
    usernum9 = int(input("Enter Your ninth guess: "))
    if robotnum9 == usernum9:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum9}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum9}")
        print("\n")
    usernum10 = int(input("Enter Your last guess: "))
    if robotnum10 == usernum10:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum10}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum10}")
        print("\n")



def hard_mode():
    print("please enter your guesses in the range of 0 - 20\n")
    userpoints = 0
    robotnum1 = random.randint(0, 20)
    robotnum2 = random.randint(0, 20)
    robotnum3 = random.randint(0, 20)
    robotnum4 = random.randint(0, 20)
    robotnum5 = random.randint(0, 20)
    robotnum6 = random.randint(0, 20)
    robotnum7 = random.randint(0, 20)
    robotnum8 = random.randint(0, 20)
    robotnum9 = random.randint(0, 20)
    robotnum10 = random.randint(0, 20)
    usernum1 = int(input("Enter Your first guess: "))
    if robotnum1 == usernum1:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum1}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum1}")
        print("\n")
    usernum2 = int(input("Enter Your second guess: "))
    if robotnum2 == usernum2:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum2}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum2}")
        print("\n")
    usernum3 = int(input("Enter Your third guess: "))
    if robotnum3 == usernum3:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum3}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum3}")
        print("\n")
    usernum4 = int(input("Enter Your fourth guess: "))
    if robotnum4 == usernum4:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum4}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum4}")
        print("\n")
    usernum5 = int(input("Enter Your fith guess: "))
    if robotnum5 == usernum5:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum5}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum5}")
        print("\n")
    usernum6 = int(input("Enter Your sixth guess: "))
    if robotnum6 == usernum6:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum6}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum6}")
        print("\n")
    usernum7 = int(input("Enter Your seventh guess: "))
    if robotnum7 == usernum7:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum7}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum7}")
        print("\n")
    usernum8 = int(input("Enter Your eighth guess: "))
    if robotnum8 == usernum8:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum8}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum8}")
        print("\n")
    usernum9 = int(input("Enter Your ninth guess: "))
    if robotnum9 == usernum9:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum9}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum9}")
        print("\n")
    usernum10 = int(input("Enter Your last guess: "))
    if robotnum10 == usernum10:
        userpoints += 3
        print(f"YAY you got guessed the number you get 1 point! you now have {userpoints}")
        print(f"The robot was thinking of {robotnum10}")
    else:
        userpoints -= 1
        print(f"Whoops look like that was the wrong number, you have {userpoints} points!")
        print(f"The robot was thinking of {robotnum10}")
        print("\n")


try:
    if mode == 1:
        easy_mode()
    elif mode == 2:
        med_mode()
    elif mode == 3:
        hard_mode()
except:
    print("oops looks like there was a error, please try again later!")
