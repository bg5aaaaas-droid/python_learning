import dis
x =10
def f():
    print(x)
print("---print bytecode---")
dis.dis(f)
print("--checking error--")
try:
    f()
except UnboundLocalError as e:
    print("UnboundLocalError: ", e)
