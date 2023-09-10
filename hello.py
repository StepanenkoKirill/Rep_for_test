
def fun1():
    print("hello")
    i = 1
    while(i < 5):
        i+=1
    print(i)
def fun2(a,b):
    while(a != 0 and b != 0):
        if(a > b):
            a = a % b
        else:
            b = b % a
    return a + b