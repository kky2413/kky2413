def int_sum(arg1):
    b=0
    for i in arg1:
        if i.isdigit():
            b=b+int(i)
    return int(b)




c=int_sum('sh452 ?sf56d')
print(c)
