a = [["*", "*", "*", "*", "*", "*", "*"],
     ["*", "*", "*", "*", "*", "*", "*"],
     ["*", "*", "x", "x", "x", "*", "*"],
     ["*", "*", "x", "*", "x", "*", "*"],
     ["*", "*", "x", "x", "x", "x", "*"],
     ["*", "*", "x", "x", "x", "*", "*"],
     ["*", "*", "x", "x", "x", "*", "*"],
     ["*", "*", "*", "x", "*", "*", "*"]]


def checked_pattern():
    list_1 = []
    list_3 = []
    for i in range(len(a)):
        count_x = 0
        for j in range(len(a[i])):
            if a[i][j] == "x":
                count_x += 1
                list_1.append([i, j])
                if count_x == 3:
                    list_3.append(i)

    print(list_1)
    print(list_3)
    for i in range(len(list_3)):
        for j in range(len(list_1)):
            k = list_3[i]
            b = list_1[j][0]
            c = list_1[j][1]
            if list_1[j][0] == k:
                try:
                    if list([b, c - 1]) in list_1 and list([b, c + 1]) in list_1 and list([b + 1, c]) in list_1 and list(
                            [b - 1, c]) in list_1:
                        return 'True'
                except:
                    pass
    return False

print(checked_pattern())