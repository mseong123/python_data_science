from callLimit import callLimit


# calling the below callLimit decorator will decorate with callLimiter
# function (returned from calling callLimit). Then when call f() will
# call the limit_function wrapper. Closure still happens the same way
# doesn't matter which level of nested function it is.

@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


for i in range(3):
    f()
    g()

# @callLimit(0)
# def h():
#     print("h()")


# @callLimit(2)
# def j():
#     print("j()")


# @callLimit(1)
# def k():
#     print("k()")


# for i in range(2):
#     h()
#     j()
#     k()
