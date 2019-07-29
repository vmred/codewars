def men_from_boys(arr):
    boys = []
    mens = []
    for i in arr:
        if not i % 2:
            boys.append(i)

        else:
            mens.append(i)

    return sorted(set(boys)) + sorted(set(mens), reverse=True)


print(men_from_boys([72, 76, 76, 82, 100, 91, 85]))
