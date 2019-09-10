def dirReduc(arr):
    result = ['default']
    arr = arr
    while len(arr) != 0:
        end = result[len(result) - 1]
        coming = arr[0]
        flag = 0

        if end == "NORTH" and coming == "SOUTH":
            flag = 1
        elif end == "SOUTH" and coming == "NORTH":
            flag = 1
        elif end == "WEST" and coming == "EAST":
            flag = 1
        elif end == "EAST" and coming == "WEST":
            flag = 1

        if flag == 1:
            result = result[:-1]
            arr = arr[1:]
        else:
            result.append(arr[0])
            arr = arr[1:]

    return result[1:]


a = dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
e = ['WEST']
assert (a == e), '--> actual: %s, expected %s' % (a, e)

a = dirReduc(["NORTH", "WEST", "SOUTH", "EAST"])
e = ["NORTH", "WEST", "SOUTH", "EAST"]
assert (a == e), '--> actual: %s, expected %s' % (a, e)
