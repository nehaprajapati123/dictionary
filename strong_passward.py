password=input("Enter your password:")
if len(password)>=6 and len(password)<=16:
    if password>="A" and password <="Z":
        if password>="a" and password <="z":
            if password>="0" and password<="9":
                if "@" in password or "#" in password:
                    print("strong password")
                else:
                    print("password must contain special character!")
            else:
                print("numbers nust be present!")
        else:
            print("lowrercase must be present")
    else:
        print("uppercase must be present!")
else:
    print("length must be greater then 6 and lower than 16" )
