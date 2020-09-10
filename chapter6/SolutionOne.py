"""  
For practice, write a program that does the following.
Table Printer
Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
For example, the value could look like this:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:
 apples Alice dogs
 oranges Bob cats
 cherries Carol moose
 banana David goose
Hint: Your code will first have to find the longest string in each of the
inner lists so that the whole column can be wide enough to fit all the strings.
You can store the maximum width of each column as a list of integers. The
printTable() function can begin with colWidths = [0] * len(tableData), which
will create a list containing the same number of 0 values as the number
of inner lists in tableData. That way, colWidths[0] can store the width of the
longest string in tableData[0], colWidths[1] can store the width of the longest string in tableData[1], and so on. You can then find the largest value in
the colWidths list to find out what integer width to pass to the rjust() string
method.

"""

def printTable(data, init, final, ans):
    data = returnData(data)
    arr = []
    if init >= final:
        return 0
    else:
        for i in data:
            arr.append(len(i[init]))
            arr.sort()
            ans += i[init] + ' '
        ans += '\n'
        
        print(ans)
        return printTable(data, init + 1, final, '')


def returnData(data):
    ans = ''
    arr = []
    for x in data:
        maxLengthNumber = maxLenght(x)
        arrtemp = []
        for i in range(0, len(x)):
            arrtemp.append(x[i].rjust(maxLengthNumber))
        ans += '\n'
        arr.append(arrtemp)
    
    return arr
        

def maxLenght(array):
    arr = []
    for i in array:
        arr.append(len(i))
    arr.sort()
    return arr[-1]

    


if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']
                ]

    printTable(tableData, 0, len(tableData[0]), '')