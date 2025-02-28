 #functions, DRY DO NOT REPEAT YOURSELF. avoid repetition.
def greet():
    print("Hello good morning!")

greet()
greet()
greet()

def marriage(boy, girl):             #parameters we can give default girl or boy name like girl="girl", the op is chandan married girl.
    print(f"boy is {boy}")
    print(f"girl is {girl}")
    print(f"{boy} married {girl}")
marriage("chandan","chandana")              #positional arguments
marriage("chethan","puneetha")                 #marriage()= keyword arguments


for i in range (1,11):
    print(f"2x{i}={2*i}")


def tables(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")

tables(5)
tables(99)
