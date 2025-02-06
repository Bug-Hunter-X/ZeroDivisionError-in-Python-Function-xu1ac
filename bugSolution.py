def function(a, b):
    if b == 0:
        return 0 # Or raise an exception, return a default value or handle it appropriately
    else:
        return a / b

result = function(10, 0)
print(result) # Output: 0 