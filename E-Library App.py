print("WELCOME TO E-library REGISTERATION APP")
adminn=["admin926@gmail.com",9265467332]
nameOfPeople=[]
no=[]
ans="y"
while ans=="y":
    name=input("Enter your name:")
    number=int(input("Enter your number:"))
    nameOfPeople.insert(0,name)
    no.insert(0,number)
    ans=input("Press 'y' to continue:")
print("Code ends here")
admin=input("(list/nolist):")
if admin=='list':
    num=input("Enter your Username:")
    passw=int(input("Enter your Password:"))
else:
    print("Thanks for using this app")

if num==adminn[0]:
    if passw==adminn[1]:
        print("The list of people name is ")
        print(nameOfPeople)
        print("The list of people number is ")
        print(no)
    else:
        print("error")
else:
    print("Error")
