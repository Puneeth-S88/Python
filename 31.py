def add (a,b):
    return a+b
c = add(1,2)                # we should assig value to add 2 or 3 numbers
print(c)
 #variable length arguments
   
def add(*a):
    print(a)
add(1,2,3,4,5,6)



def add(*numbers):
    return sum(numbers)
print(add(1,23,45,5))



#key word arguments, we use **args except python key words 
# lamda functions, 

def add(a,b):
    return a+b 
# above function acn be written as
add = lamda  a,b : a+b
double = lamda x; 2*x
print (double(200))
 