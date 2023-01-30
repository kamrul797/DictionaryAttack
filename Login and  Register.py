import hashlib
check = True
Login_Register = input("Welcome,\nType L to Login, R to Register\n")
if Login_Register == "l" or Login_Register =="L":
    while check:
        with open('accountfile.txt', 'r') as f:
            username1 = input("Enter your username: ")
            password1 = input("Enter your password: ")
            hashpass = hashlib.md5(password1.encode('utf8')).hexdigest()
            for line in f:
                as_list = line.split("\t")
                if (username1==as_list[0]):
                    if(username1+"\t"+hashpass) == line.strip():
                        print("You are logged in!")
                        check = False
                        break;
                    else:
                        print("Username or password does not exist!")

elif Login_Register == "r" or Login_Register == "R":
    f = open("accountfile.txt","a+")
    username2 = input("Please enter your username: ")
    password2 = input("Please enter your password: ")
    hashpass = hashlib.md5(password2.encode('utf8')).hexdigest()
    f.write(f"{username2}\t{hashpass}\n")
    f.close()
    print("User Created Successfully!")


    