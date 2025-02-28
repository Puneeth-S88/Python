# return in functions
def func(num):
    print(int(str(num)*8))
func(2)
#new
def func(num):
    return int (str(num*8))

a = 100
b = func(2)
c = a+b
print(c)


 #local and global variable
def func():
    x = " chandan" # loacl var, inside the defined function
    print("hello world")
    print(y)

y="bubbly"  #global var, which is in outside  the block.
print(y)
