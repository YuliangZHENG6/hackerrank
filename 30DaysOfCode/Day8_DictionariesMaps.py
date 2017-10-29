# python 3

import sys

n = int(input().strip())
name_number = [input().strip().split() for _ in range(n)]
book = {k: v for k,v in name_number}

while True:
    try:
        query = input().strip()
        if query in book:
            print("%s=%s" % (query, book[query]))
        else:
            print("Not found")
    except:
        break