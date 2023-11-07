from typing import Any


def callLimit(limit: int):
    """callLimit"""
    count = 0

    def callLimiter(function):
        """callLimiter"""
        def limit_function(*args: Any, **kwds: Any):
            """limit_function"""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} called too many times")
            else:
                function()
                count += 1
        return limit_function
    return callLimiter
