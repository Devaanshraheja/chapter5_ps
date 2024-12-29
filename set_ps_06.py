#if elif ladder
age= int(input("Enter your Age: "))
if(age<18):
    print("You are not eligible")
    print("You are a minor")


elif(age<0):
    print("Invalid age")
    print("your age can't be ")     