def greet():
    print("Hi Puneeth!!!")
greet()
greet()
greet()


def marriage():
    print("P marries P")
marriage()    


def marriage(boy,girl):
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} and {girl} are best friends")
marriage("Puneeth", "Vinutha")    
marriage("Manjaa","Vinutha")

def tables(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
tables(1)          
tables(23)


def marriage(boy,girl="girl"):
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} and {girl} are best friends")
marriage("Puneeth",)    
marriage("Manjaa",)