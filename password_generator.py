import random
import string

#main function
def main():
    total = input("How many passwords do you want? ")
    while total.isalpha():
        print("Please enter a number")
        total = input("How many passwords do you want? ")
    while int(total) < 1:
        print("At least one password will be generated")
        total = input("How many passwords do you want? ") 
    length = input("Enter the maximum length of your password: ")
    while length.isalpha():
        print("Please enter a number")
        length = input("Enter the maximum length of your password: ")
    while int(length) < 4 or int(length) > 50:
        print("Password length should be between 4 and 50 characters")
        length = input("Enter the maximum length of your password: ")
    for _ in range(int(total)):
        a = 1
        while a <= int(total):
            print(f"{a}. ", end="") 
            real_password(int(length))
            a +=1
            print(" ")
        break

#generate random digits
def digit(n):
    return random.choice(string.digits)

#generate uppper case characters
def uppercase(n):       
    return random.choice(string.ascii_uppercase)

#generate lower case characters
def lowercase(n):
    return random.choice(string.ascii_lowercase)

#generate punctuation characters
def punctuation(n):
    return random.choice(string.punctuation)

#compile everything
def real_password(n):
    for _ in range(n):
        password=[]
        password.append(digit(n))
        password.append(lowercase(n))
        password.append(uppercase(n))
        password.append(punctuation(n))
        r1 = random.choice(password)
        print(r1, end="")
         
if __name__ == "__main__":
    main()