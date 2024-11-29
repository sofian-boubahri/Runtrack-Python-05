def function():
    l = [1, 2, 3, 4, 5]
    l[0], l[-1] = l[-1], l[0]
    print(l)
function()