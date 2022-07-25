def fnc(test, sep):
    if sep not in test:
        return test
    key, val = test.split(sep, 1)
    return {key: fnc(val, sep)}



test = "a/b/c"
# object = {'a':{'b':{'c':'d'}}}

# printing original string
print("The original string is : " + str(test))

# initializing separator
sep = '/'

# Convert String to Nested Dictionaries
# Using loop
res = fnc(test, sep)
print(res)

# printing result
# print("The nested dictionary is : " + str(res))
object = {'a': {'b': {'c': 'd'}}}
#
#
def dict(object, res):
    for id in res:
        print(id)
        for k in res[id]:
            print(k)
            # for l in res[id][k]:
            result1 = res[id][k]
            print(result1)
    for i in object:
        if result1 == i:
            print(object[result1])
        else:

            for j in object[i]:
                if result1 == j:

                    print(object[i][result1])
                else:

                    for m in object[i][j]:
                        if result1 == m:
                            print(object[i][j][result1])
                        else:
                            print("NA")


result = dict(object, res)
