def outer():
    count=0
    def inc():
        nonlocal count
        count+=1
        return count
    return inc
c1=outer()
c2=outer()
print(c1.__closure__[0] is c2.__closure__[0])
print(c1.__code__ is c2.__code__)
