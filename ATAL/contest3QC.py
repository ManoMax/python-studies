amount = int(input())

nums = []
for i in range(amount):
    nums.append(input())

for num in nums:
    num_int = int(num)
    if (num_int > 45):
        print(-1)
    elif (num_int < 10):
        print(num_int)
    elif (num_int < 18):
        cont_aux = 1
        value = 9 * cont_aux + num_int
        sum_dig = sum(int(i) for i in str(value))

        while (sum_dig < num_int):
            cont_aux += 1
            value = 9 * cont_aux + num_int
            sum_dig = sum(int(i) for i in str(value))

        if (sum_dig == num_int):
            print(value)
        else:
            print(-1)
    elif (num_int < 25):
        cont_aux = 100
        value = cont_aux + 89
        sum_dig = sum(int(i) for i in str(value))

        while (sum_dig < num_int):
            cont_aux += 100
            value = cont_aux + 89
            sum_dig = sum(int(i) for i in str(value))

        if (sum_dig == num_int):
            print(value)
        else:
            print(-1)
    elif (num_int < 31):
        cont_aux = 1000
        value = cont_aux + 789
        sum_dig = sum(int(i) for i in str(value))

        while (sum_dig < num_int):
            cont_aux += 1000
            value = cont_aux + 789
            sum_dig = sum(int(i) for i in str(value))

        if (sum_dig == num_int):
            print(value)
        else:
            print(-1)

    elif (num_int < 36):
        cont_aux = 10000
        value = cont_aux + 6789
        sum_dig = sum(int(i) for i in str(value))

        while (sum_dig < num_int):
            cont_aux += 10000
            value = cont_aux + 6789
            sum_dig = sum(int(i) for i in str(value))

        if (sum_dig == num_int):
            print(value)
        else:
            print(-1)
    elif (num_int < 40):
        cont_aux = 100000
        value = cont_aux + 56789
        sum_dig = sum(int(i) for i in str(value))

        while (sum_dig < num_int):
            cont_aux += 100000
            value = cont_aux + 56789
            sum_dig = sum(int(i) for i in str(value))

        if (sum_dig == num_int):
            print(value)
        else:
            print(-1)
    elif (num_int == 40):
        print(1456789)
    elif (num_int == 41):
        print(2456789)
    elif (num_int == 42):
        print(3456789)
    elif (num_int == 43):
        print(13456789)
    elif (num_int == 44):
        print(23456789)
    elif (num_int == 45):
        print(123456789)
