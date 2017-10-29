#  python3

import sys

if __name__ == '__main__':
    (n, m) = [int(i) for i in input().strip().split()]

    vals = [0] * n

    for i in range(m):
        (a, b, k) = [int(i) for i in input().strip().split()]
        # start the addition
        vals[a-1] += k
        try:
            # end the addition
            vals[b] -= k
        except:
            # out of range of list (at the end)
            pass

    prev = 0
    for i in range(len(vals)):
        prev += vals[i]
        vals[i] = prev

    print(max(vals))
    
    
# Let's try an example
# Let's try to walk through an example. If we have 1 query and it wants to add 100 to elements 2 through 4 inclusive in a 7-element array, we want to have:
# [0, 0, 100, 100, 100, 0, 0]
# The idea is that we can represent this initially as:
# [0, 0, 100, 0, 0, -100, 0]
# It's important to realize that this above array is not our final answer. We will walk through the array from array[0] to array[6] to create our final answer. When we reach array[2], it basically tells us that every element from here and to the right of it (array[2] to array[6]) should have 100 added to them. When we reach array[5], it tells us the same thing, except that every element should have -100 added to it. By following these 2 rules, we get
# array[0] = 0;
# array[1] = 0;
# array[2] = 0 + 100 = 100;
# array[3] = 0 + 100 = 100;
# array[4] = 0 + 100 = 100;
# array[5] = 0 + 100 - 100 = 0;
# array[5] = 0 + 100 - 100 = 0;
# giving us the final array of
# [0, 0, 100, 100, 100, 0, 0]