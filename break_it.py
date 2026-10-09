def add(item, box=None):
    if box==None:
        box=[]
    box.append(item)
    return box
print(add.__defaults__)
print(add("a"))
print(add("b"))
print(add.__defaults__)
