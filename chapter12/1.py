"""
Multiplication Table Maker
Create a program multiplicationTable.py that takes a number N from the command line and creates an N×N multiplication table in an Excel spreadsheet.
For example, when the program is run like this:

"""

import openpyxl

def create_table():
    
    total_columns_rows = int(input('How many columns and rows: '))

    print('Creating table...')
    wb = openpyxl.Workbook()
    sheet = wb['Sheet']

    for i in range(1, total_columns_rows + 2):
        for j in range(1, total_columns_rows + 2):
            if i == j and j == 1:
                continue
            else:
                sheet.cell(row=j, column=i).value = j + 1
    

    name_file = input('How do you wanna call the file? ')
    wb.save(name_file + '.xlsx')
    print('Done')





if __name__ == '__main__':

    create_table()

