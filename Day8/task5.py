#function for checking the greetings
def language_code(num1):
    if num1 =="en":
        print(" Hello ")

    elif num1 =="es":
     print(" Hola ")

    elif num1 =="fr":
     print(" Bonjour ")
     
    else:
        print("Language code not matched")

#input from user and display  the result
print("Enter the following three code languages to see the result ::     en , es , fr ")
num1 =str(input("Enter the first language code "))
language_code (num1)

num1 =str(input("Enter the second language code "))
language_code (num1)

num1 =str(input("Enter the third language code "))
language_code (num1)

