#this is the code for the fibonacci series
num = int(input("enter the number for fibonacci series"))
fb=0
fn=1
for i in range (0,num):
    print(fb)
    fib=fb+fn
    fb=fn
    fn=fib
