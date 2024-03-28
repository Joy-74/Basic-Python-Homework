'''
    PIC 16A Homework 2
    Author: Jiayu Li
    UID: 605348766
    Discussion Section: 3B
    Date: 01/24/2023
'''


def longestpath(d):
    # initializing length of longest path
    longest = 0
    for key in d:
        path = 0 # Longest path of the key
        keys_dictionary= {}  # create empty dict
        for tempkey in d:
            keys_dictionary[tempkey] = False
        while True:
            if key not in d:
                # This key is undefined
                break                
            if keys_dictionary[key]:
                # It will terminate when the key appears repeatedly
                break
            # Setting key
            keys_dictionary[key] = True
            path += 1
            # Setting the value corresponding to the previous key as the key for the next iteration            
            nextkey=d[key]
            key = nextkey

        # Update the longest path
        longest= max(path,longest)
    return longest


# Test
# d1 = {"a":"b", "b":"c"}
# d2 = {"a":"b", "b":"c", "c":"d", "e":"a", "f":"a", "d":"b"}
# d3 = {"a":"b", "b":"c", "c":"d", "e":"a", "f":"a", "d":"e"}
# print(longestpath(d1))
# print(longestpath(d2))
# print(longestpath(d3))

