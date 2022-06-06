test = int(input())

while test >= 1:
    dict = {}
    n, k = input().split()
    n = int(n)
    k = int(k)
    flag1 = 0
    flag2 = 0
    for i in range(k):
        a, b = input().split()
        dict[int(a)] = int(b)
    sorted_dict = {k: dict[k] for k in sorted(dict)}
    sorted_dict_key = list(sorted_dict.keys())
    sorted_dict_value = list(sorted_dict.values())
    for i in range(len(sorted_dict_key) - 1):
        if abs(sorted_dict_key[i+1] - sorted_dict_key[i]) == 1:
            flag1 = 1
    for i in range(len(sorted_dict_value) - 1):
        if abs(sorted_dict_value[i + 1] - sorted_dict_value[i]) == 1:
            flag2 = 1
    if flag1 == 1 and flag2 == 1:
        print('No')
    else:
        print("Yes")
    test -= 1
