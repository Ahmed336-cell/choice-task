import math

# this function to show the menu
def showmenu():
    print("[0] check palindrome          "  + "[1] check if prime")
    print("[99] Exit")


# this function when choose 1 from the menu to check if number is prime or not
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if math.fmod(number , i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
# if number is less than 0 = not prime
    else:
        print(number, "is not a prime number")
# this function to check if word is palindrome
def is_palindrome():
    word = input("enter word")
    if word == word[::-1]:
        print("yes")
    else:
        print("no")

op = 1
# while code is running op =1
while op == 1:
    showmenu()
    choic =int(input("choose an opeartion"))
    if choic == 1:
        is_prime(int(input("enter number")))
    elif choic == 0:
        is_palindrome()
# if choose exit with num 99 the op = -1 so code will stop
    elif choic == 99:
        op = -1
    else:
        print("invalid ,, please try again")

