def function():
    L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    sum = 0
    for numbers in L:
        if numbers % 2 == 0:
            sum = sum + numbers
    print(sum)

function()