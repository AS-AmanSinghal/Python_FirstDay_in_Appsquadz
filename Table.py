def calculation(a,b):
    for i in range(1,b+1):
        print("{} * {} = {}".format(a,i,a*i))


if __name__ == '__main__':
    while True:
        try:
            a = int(input("Enter First Integer Number "))
            b = int(input("Enter second Integer Number "))
            calculation(a,b)
            break
        except:
            print("ENTER CORRECT NUMBER")
            continue