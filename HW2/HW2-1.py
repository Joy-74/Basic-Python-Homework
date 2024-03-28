def longestpath(d):
    # initializing length of longest path
    longest = 0
    for key in d:
        path = []  # create empty list
        while key in d:
            if key in path:
                # It will terminate when the key appears repeatedly
                break
            # add key to empty list
            path.append(key)
            # Setting the value corresponding to the previous key as the key for the next iteration
            key = d[key]

        # Find the longest path
        if len(path)>longest:
            longest = len(path)
    return longest


# Test
d1 = {"a":"b", "b":"c"}
# d2 = {"a":"b", "b":"c", "c":"d", "e":"a", "f":"a", "d":"b"}
# d3 = {"a":"b", "b":"c", "c":"d", "e":"a", "f":"a", "d":"e"}
print(longestpath(d1))
# print(longestpath(d2))
# print(longestpath(d3))


# HW 2-2
def solve(function, x0, tol):
    current_x = x0
    f = function(current_x)
    while  abs(f[0]) > tol:
        current_x = current_x - f[0]/f[1]
        f = function(current_x)
        
    return current_x
        
        
initial_guess = solve(lambda x : (x ** 2 - 1, 2 * x), 3, 1e-4) # function 1
print(initial_guess)


