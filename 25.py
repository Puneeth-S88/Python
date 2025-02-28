#important technique Debugging
#=0
#hile i<=10:
   #print(i,end = " ") # red dot ......we say it to stop there or end there.
   #i+=1

    

l = [1,2,3,4,5,6]
cl = []
for i in range (len(l)):
    c = l[i]
    d =l[-i]
    x= c*d
    if x%2==0:
        cl.append(x)
