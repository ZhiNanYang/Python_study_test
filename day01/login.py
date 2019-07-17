
def verifyuser():
    with open("login.txt", "r") as f:
        names = f.read().splitlines()
        if name in names[::2]:
            if password == names[names.index(name) + 1]:
                return 1
        else:
            return 0


count = 0
while count < 3:
    name = input("Name: ")
    password = input("Password: ")
    if verifyuser():
        print("Wellcome ", name)
        break
    else:
        count += 1
        if count < 3:
            print('''Incorrect user name or password.
                Please enter again!
                You can try %d more times''' % ((3 - count)))
