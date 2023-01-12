from pyexample import n

test1 = False
if (n % 2) == 0:
    test1 = True

test2 = False
if n <= 20:
    test2 = True

test3 = False
if n >= 2:
    test3 = True

if test1:
    print("Test 1 passed✅")
if test2:
    print("Test 2 passed✅")
if test3:
    print("Test 3 passed✅")
if test1 and test2 and test3:
    print("All test passed✅✅✅")