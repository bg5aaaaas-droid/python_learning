def make_counter():
    counter= 0
    def count1():
        nonlocal counter
        counter+=1
        return counter
    return count1
c1=make_counter()
c1()
print(c1.__closure__[0].cell_contents)
