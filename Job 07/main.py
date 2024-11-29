def function():
    L = [8, 24,48,2,16]
    count = 0
    for numbers in L:
        if numbers % 3 == 0:
            count += 1
    print(count)

function()