# def uppercase(func):
#     def wrapper():
#         result = func()
#         upper_res = result.upper()
#         return upper_res
#
#     return wrapper()


def uppercase(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        upper_res = result.upper()
        return upper_res

    return wrapper


@uppercase
def some_str():
    return "nikola e debelak mazen"

print(some_str())

@uppercase
def my_func(a):
    return a
print(my_func("hello world"))


# def uppercase(function):
#     def wrapper():
#         result = function()
#         uppercase_result = result.upper()
#         return uppercase_result
#     return wrapper
#
#
#
# def say_hi():
#     return 'hello there'
#
# decorate = uppercase(say_hi)
# print(decorate())
