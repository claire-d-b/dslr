def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        """1st level nested function"""

        def limit_function(*args: any, **kwds: any):
            """2nd level nested function that increases nonlocal value count
            and compares it with limit"""
            nonlocal count
            nonlocal limit
            nonlocal function
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
            else:
                print(function.__name__ + "()")
        return limit_function
    return callLimiter
