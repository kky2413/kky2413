# 2-1번
def fib(arg1):
    if arg1==0:
        return 0
    elif arg1==1:
        return 1
    else:
        a,b=0,1
        for n in range(2,arg1+1):
            a,b=b,a+b
        return b    

#2-2번
fib_list = [number for number in range(fib(0),fib(26))]
print(fib_list)

#2-3번
def fib_multi(*arg2):
    return 
print(fib_multi)

#2-4번
def fib(arg1):
    
