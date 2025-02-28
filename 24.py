#list comprehension
l=[1,2,3,4]
dl=[num*2 for num in l]
print(dl)

l=[x  for x in range(1,19)]
edl=[x**2 for x  in l if x%2==0]
print(edl)

names=["anand","geetha", "bubbly"]
d= {name:len(name) for name  in names}
print(d) 



s= "puneeth"
l=s.split()
print(l)
#"_" it breaks elements.


print("list input practice")
x=input(" enter the integers:")
print(x)