#WAP to print sum
while True:
    try:
        a = int(input("Enter First Integer Number "))
        b = int(input("Enter second Integer Number "))
        print(a+b)
        break
    except:
        print("ENTER CORRECT NUMBER")
        continue