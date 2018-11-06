# def repeat(function, times):
#     for calls in range(times):
#         function()
#
# def foo(s):
#         print s
#
# repeat(foo("test"), 1)

def repeat(times, f, *args):
    for _ in range(times):
        f(*args)

def foo(s,s2):
        print(s,s2)

repeat(4, foo, "test", "test2")

def foo2(f,x,y,z):
    print(z)
    return f(x,y)

def foo(x,y):
    return x+y

x = 1
y = 2
z = 3
out = foo2(foo,x,y,z)
print(out)