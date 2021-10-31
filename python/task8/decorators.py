"""there are 2 different programs in the file.
just uncomment one or another part"""

"""first"""


def outside_decorator(var_type):
    """our decorator, take: type of argument what we want to check"""
    def type_check(func):
        """checker, take function like argument"""
        def wrapper(func_var):
            """wrapper, take argument of decoration function"""
            if isinstance(func_var, var_type):
                return func(func_var)
            raise TypeError
        return wrapper
    return type_check


@outside_decorator(float)
def some_func(num):
    """some func, count power of number"""
    return num ** 2


@outside_decorator(str)
def another_funk(string):
    """some func, concatenate strings"""
    return string + "!!!"


print(some_func(6.252))
print(another_funk(6))

#
# """second"""
#
#
# def remember_last_count(func):
#     """remember previous counts"""
#     cash = {}
#
#     def wrapper(*args, **kwargs):
#         key = str(*args) + str(**kwargs)
#         if key not in cash:
#             cash[key] = func(*args, **kwargs)
#         return cash[key]
#
#     return wrapper
#
#
# @remember_last_count
# def fib(num):
#     """count fibonachi sequence"""
#     return fib(num-1) + fib(num-2) if num > 1 else num
#
#
# print(fib(8))
