def function():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

    count = 1

    for numbers in L:
        if 25 <= numbers <= 90:
            count *= numbers
    print(count)

function()