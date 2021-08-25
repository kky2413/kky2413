def int_generator(arg1):
    b=''
    for i in arg1:
        if i.isdigit():
            b=b+i
    return int(b)

c=int_generator(' abc35? 567*kt0')
print(c)
