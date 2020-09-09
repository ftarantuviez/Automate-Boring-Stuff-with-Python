"""  
Comma Code
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.

"""

def comma_code(array):
    ans = ''
    index = 0
    for i in array:
        if index == len(array) - 1:
            ans += 'and ' + str(i)
        else:
            ans += str(i) + ', '
        index += 1

    print(ans)


if __name__ == '__main__':
    comma_code([1, 2, 3, 4, 5, 6])