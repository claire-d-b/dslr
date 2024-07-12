def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
        #your code here
            nonlocal count
            nonlocal limit
            nonlocal function
            # print(args)
            # print(kwds)
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
            else:
                print(function.__name__ + "()")
        return limit_function
    return callLimiter
