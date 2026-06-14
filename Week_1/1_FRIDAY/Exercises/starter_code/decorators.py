"""
decorators.py : 
Involves :
- 
"""


import time
from functools import wraps


# TODO: Implement Decorator that measures and prints execution time.
# Output format: "⏱️ {func_name} completed in {seconds:.4f}s"

def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        # Record Start Time
        start_time= time.perf_counter()

        # Execute The Original Function
        result = func(*args, **kwargs)

        # Record The End Time
        end_time = time.perf_counter()

        # Calculate And Print The Duration
        execution_time = end_time - start_time
        print(f"⏱️  Function : {func.__name__} completed in {execution_time:.4f}s") 

        return result
    
    return wrapper
    


# **Test:**
@timer
def slow_operation():
    time.sleep(0.5)
    return "done"

result = slow_operation()
# Should print: ⏱️ slow_operation completed in 0.50XXs
assert result == "done"
assert slow_operation.__name__ == "slow_operation"  # @wraps preserves metadata
