def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


# Nonlocal : In Python, the nonlocal keyword is used inside
# a nested function to indicate that a variable is not local
# to the inner function, but is from an outer (enclosing)
# function.
# It allows you to modify the value of a variable in the
# outer function's scope from within the inner function.
# Without nonlocal, a variable in a nested function is
# treated as local to that function, and changes made to it
# won’t affect the outer function’s variable.


def outer(x: int | float, function) -> object:
    count = 0
    # nonlocal variables from the inner function are in the scope
    # of this function

    def inner() -> float:
        nonlocal count
        nonlocal x

        try:
            print(isinstance(x, (int, float)))
            count = function(x)
            x = count
            return x
        except Exception as e:
            raise AssertionError(f"Error: {e}")
    return inner
